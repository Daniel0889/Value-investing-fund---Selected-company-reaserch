"""Valuation, margin-of-safety and sizing arithmetic of Charter Revision 4.

Implements `framework.md` section (d) (valuation methods d1-d11) and section (e2) (sizing), as
the charter's "Valuation methods", "Margin of safety by tier" and "Portfolio constraints"
sections require. The charter says all arithmetic runs in code (rule 1); every number in a
thesis must come from these functions, not from prose.

Conventions
-----------
* Amounts are in the cash flows' currency and in one unit (e.g. USD thousands or ILS millions).
  Per-share values divide by a share count in the same units.
* The hurdle r is passed explicitly: r = max(10%, y10 + 3 points), y10 dated, no beta, no equity
  risk premium (framework d4, "[PROPOSED] Implementation").
* Notation follows framework.md (d): EBIT_adj = EBIT with identified one-offs removed;
  Dep = depreciation of PP&E and right-of-use assets; Amort_acq = amortisation of acquired
  intangibles; C = cash plus short-term investments; D = debt including leases.
* EBITDA is never used (checklist D1).
"""

from __future__ import annotations

import math
import statistics
from dataclasses import dataclass, field

MAX_GROWTH = 0.10            # d4: g1 capped at 10%
MAX_TERMINAL_GROWTH = 0.025  # d4: gT <= 2.5%


# --------------------------------------------------------------------------- hurdle

def hurdle(y10: float) -> float:
    """r = max(10%, y10 + 3 points), nominal, in the cash flows' currency (charter)."""
    return max(0.10, y10 + 0.03)


# --------------------------------------------------------------------------- d1 owner earnings

def growth_capex(avg_netppe_to_rev: float, delta_rev: float) -> float:
    """d1: GrowthCapEx = (avg NetPPE / Rev over 5 years) x max(dRev, 0)."""
    return avg_netppe_to_rev * max(delta_rev, 0.0)


def maintenance_capex(capex: float, dep: float, avg_netppe_to_rev: float, delta_rev: float,
                      filed_maintenance: float | None = None) -> float:
    """d1: MaintCapEx = max(CapEx - GrowthCapEx, Dep).

    The floor at depreciation is deliberate. An analyst may go below it only with filed
    evidence: pass `filed_maintenance` (a disclosed maintenance-capex figure) to use it.
    """
    if filed_maintenance is not None:
        return filed_maintenance
    return max(capex - growth_capex(avg_netppe_to_rev, delta_rev), dep)


def owner_earnings(ni: float, dep: float, amort_acq: float, other_non_cash: float,
                   maint_capex: float, dwc_maint: float = 0.0) -> float:
    """d1: OE = NI + Dep + Amort_acq + other non-cash charges (excluding SBC) - MaintCapEx - dWC_maint.

    Stock compensation is a real cost and is never added back: do not include it in
    `other_non_cash`.
    """
    return ni + dep + amort_acq + other_non_cash - maint_capex - dwc_maint


def owner_earnings_cash(ocf: float, sbc: float, maint_capex: float,
                        lease_principal: float = 0.0) -> float:
    """Cash proxy (d1 screen proxy, checklist C4): OCF - SBC - MaintCapEx.

    Under IFRS 16 lease principal sits in financing cash flow and inflates OCF (framework h3);
    pass it to deduct it.
    """
    return ocf - sbc - maint_capex - lease_principal


# --------------------------------------------------------------------------- d2 normalised earnings

def is_cyclical(margins: list[float]) -> bool:
    """d2: cyclical if the stdev of the operating margin exceeds half its median, or any
    operating loss in the window."""
    if any(m < 0 for m in margins):
        return True
    if len(margins) < 2:
        return False
    med = statistics.median(margins)
    return statistics.stdev(margins) > 0.5 * med


@dataclass
class NormalisedEbit:
    m_norm: float
    cyclical: bool
    ebit_norm: float
    detail: dict


def normalised_ebit(rev_ttm: float, ebit_adj: list[float], rev: list[float],
                    force_cyclical: bool | None = None) -> NormalisedEbit:
    """d2. m_norm = median of EBIT_adj / Rev over the window W (one-offs removed first).

    Stable:   EBIT_norm = Rev_ttm x m_norm
    Cyclical: EBIT_norm = min(mean EBIT_adj over W, median EBIT_adj over W, mean Rev over W x m_norm)
    """
    assert len(ebit_adj) == len(rev) and rev
    margins = [e / r for e, r in zip(ebit_adj, rev)]
    m_norm = statistics.median(margins)
    cyc = is_cyclical(margins) if force_cyclical is None else force_cyclical
    if cyc:
        cands = {
            "mean_ebit_adj": statistics.mean(ebit_adj),
            "median_ebit_adj": statistics.median(ebit_adj),
            "mean_rev_x_m_norm": statistics.mean(rev) * m_norm,
        }
        value = min(cands.values())
    else:
        cands = {"rev_ttm_x_m_norm": rev_ttm * m_norm}
        value = rev_ttm * m_norm
    return NormalisedEbit(m_norm, cyc, value, {"margins": margins, **cands})


# --------------------------------------------------------------------------- d3 EPV

def excess_cash(cash_and_sti: float, annual_operating_costs: float) -> float:
    """d3: excess cash is cash above two months of operating costs [I]."""
    return max(cash_and_sti - annual_operating_costs * 2.0 / 12.0, 0.0)


def unlevered_owner_earnings(ebit_norm: float, amort_acq: float, tax: float, dep: float,
                             maint_capex: float) -> float:
    """d3: OE_unlevered_norm = (EBIT_norm + Amort_acq) x (1 - t) + Dep - MaintCapEx."""
    return (ebit_norm + amort_acq) * (1 - tax) + dep - maint_capex


def equity_bridge(operations_value: float, excess_c: float = 0.0, non_operating_assets: float = 0.0,
                  debt: float = 0.0, lease_liabilities: float = 0.0, pension_deficit: float = 0.0,
                  nci: float = 0.0, preferred: float = 0.0) -> float:
    """d3: equity = operations + excess C + non-operating assets - D - leases - pension - NCI - preferred."""
    return (operations_value + excess_c + non_operating_assets
            - debt - lease_liabilities - pension_deficit - nci - preferred)


def epv_operations(oe_unlevered_norm: float, r: float) -> float:
    """d3: EPV_operations = OE_unlevered_norm / r."""
    return oe_unlevered_norm / r


# --------------------------------------------------------------------------- d4 DCF

def growth_cap(g_hist_per_share: float | None, reinvestment_rate: float | None,
               roiic: float | None) -> float:
    """d4: g1 = min(per-share OE/EPS growth record, reinvestment rate x incremental ROIC, 10%)."""
    cands = [MAX_GROWTH]
    if g_hist_per_share is not None:
        cands.append(g_hist_per_share)
    if reinvestment_rate is not None and roiic is not None:
        cands.append(reinvestment_rate * roiic)
    return min(cands)


@dataclass
class DcfResult:
    operations_value: float
    pv_explicit: float
    pv_terminal: float
    terminal_share: float
    rows: list = field(default_factory=list)

    @property
    def terminal_warning(self) -> bool:
        """d4: if the terminal value exceeds 75% of the total, the thesis rests on assumptions
        nobody can observe."""
        return self.terminal_share > 0.75


def dcf_operations(oe0: float, r: float, g1: float, roiic: float | None,
                   gT: float = MAX_TERMINAL_GROWTH, roiic_T: float | None = None,
                   years: int = 10, cap_growth: bool = True) -> DcfResult:
    """d4: ten-year owner-earnings DCF with the reinvestment charged.

    OE_t  = OE_0 x (1 + g1)^t
    FCF_t = OE_t - Reinv_t,   Reinv_t = g_(t+1) / ROIIC x OE_t   (none when growth <= 0)
    TV    = OE_10 x (1 + gT) x (1 - gT / ROIIC_T) / (r - gT),  gT <= 2.5%, ROIIC_T >= r

    Timing: the reinvestment made in year t funds the growth of year t+1, so the year-1 growth is
    paid for at t = 0 and the year-10 reinvestment funds terminal growth gT. With this timing a
    business whose incremental return equals r is worth exactly its EPV at any growth rate,
    which is framework d3's rule ("if ROIC on new capital is at or below r ... growth adds
    nothing"). framework d4 writes the charge as g / ROIIC x OE_t without the timing; this is the
    same charge, dated. `roiic=None` with g1 > 0 is not allowed: growth is never free.
    """
    if cap_growth:
        g1 = min(g1, MAX_GROWTH)
    gT = min(gT, MAX_TERMINAL_GROWTH)
    roiic_T = r if roiic_T is None else max(roiic_T, r)
    if g1 > 0:
        assert roiic is not None and roiic > 0, "growth needs an incremental return on capital"
        reinvest = min(g1 / roiic, 1.0)
    else:
        reinvest = 0.0
    reinvest_T = max(gT, 0.0) / roiic_T
    pv = -oe0 * reinvest                       # t = 0: funds year-1 growth
    oe, rows = oe0, []
    for t in range(1, years + 1):
        oe = oe * (1 + g1)
        rate = reinvest if t < years else reinvest_T
        fcf = oe * (1 - rate)
        pv += fcf / (1 + r) ** t
        rows.append({"year": t, "oe": oe, "reinvestment": oe * rate, "fcf": fcf})
    tv = oe * (1 + gT) * (1 - gT / roiic_T) / (r - gT)
    pv_tv = tv / (1 + r) ** years
    total = pv + pv_tv
    return DcfResult(total, pv, pv_tv, pv_tv / total if total else float("nan"), rows)


# --------------------------------------------------------------------------- d5 pre-tax rule

def enterprise_value(mcap: float, debt: float, cash_and_sti: float, lease_liabilities: float = 0.0,
                     nci: float = 0.0, preferred: float = 0.0) -> float:
    """EV = MCap + D - C + preferred + NCI (leases included in D for IFRS filers)."""
    return mcap + debt + lease_liabilities - cash_and_sti + preferred + nci


def pretax_multiple(ev: float, ebit_norm: float) -> dict:
    """d5: pre-tax earnings yield on EV = EBIT_norm / EV. About 10x is fair for Tier A while r = 10%."""
    return {"ev_to_ebit_norm": ev / ebit_norm, "pretax_yield": ebit_norm / ev}


# --------------------------------------------------------------------------- d6/d7 asset values

def ncav(current_assets: float, total_liabilities: float, preferred: float = 0.0) -> float:
    """d6: NCAV = CA - TL - preferred (same balance-sheet date)."""
    return current_assets - total_liabilities - preferred


def dempster_value(cash_and_sti: float, receivables: float, inventory: float, prepaid: float,
                   ppe_auction_value: float, total_liabilities: float, preferred: float = 0.0,
                   other_assets_at_value: float = 0.0) -> float:
    """d6: Buffett's Dempster discounts: cash 100%, receivables 85%, inventory 60%, prepaid 25%,
    PP&E at estimated auction value (zero if unknown), all liabilities and preferred at 100%."""
    return (cash_and_sti + 0.85 * receivables + 0.60 * inventory + 0.25 * prepaid
            + ppe_auction_value + other_assets_at_value - total_liabilities - preferred)


def tangible_book(equity: float, goodwill: float, intangibles: float) -> float:
    """d7: tangible book = E - goodwill - intangibles."""
    return equity - goodwill - intangibles


# --------------------------------------------------------------------------- d8 reverse DCF

def implied_growth(ev: float, oe0: float, r: float, roiic: float | None,
                   gT: float = MAX_TERMINAL_GROWTH, roiic_T: float | None = None) -> float:
    """d8: the ten-year owner-earnings growth that makes the d4 DCF at r equal today's EV.

    Not capped at 10%: it is the market's forecast. With `roiic=None` growth is assumed free of
    reinvestment (the most generous reading of the price).
    """
    def value(g: float) -> float:
        if g > 0 and roiic is None:
            # generous variant: no reinvestment charge in the ten explicit years
            oe, pv = oe0, 0.0
            for t in range(1, 11):
                oe *= 1 + g
                pv += oe / (1 + r) ** t
            rT = r if roiic_T is None else max(roiic_T, r)
            tv = oe * (1 + gT) * (1 - gT / rT) / (r - gT)
            return pv + tv / (1 + r) ** 10
        return dcf_operations(oe0, r, g, roiic if g > 0 else None, gT, roiic_T,
                              cap_growth=False).operations_value

    lo, hi = -0.5, 0.6
    if value(lo) > ev:
        return lo
    if value(hi) < ev:
        return hi
    for _ in range(200):
        mid = (lo + hi) / 2
        if value(mid) < ev:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


# --------------------------------------------------------------------------- d9 Graham yardstick

def graham_pe_cap(y_aaa: float) -> float:
    """d9: P/E cap 10 when y_AAA <= 5%, 7 when y_AAA >= 7%, linear in between."""
    if y_aaa <= 0.05:
        return 10.0
    if y_aaa >= 0.07:
        return 7.0
    return 10.0 - (y_aaa - 0.05) / 0.02 * 3.0


def graham_yardstick(ni_norm_ttm: float, mcap: float, y_aaa: float) -> dict:
    """d9: earnings yield >= 2 x y_AAA (same currency) and P/E within the cap.

    In ILS, until the AA+ corporate series is wired in, pass the government yield and label
    the test "[I], looser than Graham's".
    """
    ey = ni_norm_ttm / mcap
    pe = mcap / ni_norm_ttm if ni_norm_ttm > 0 else float("inf")
    cap = graham_pe_cap(y_aaa)
    return {"earnings_yield": ey, "required_yield": 2 * y_aaa, "pe": pe, "pe_cap": cap,
            "passes": ey >= 2 * y_aaa and pe <= cap}


# --------------------------------------------------------------------------- d11 margin by tier

BASE_MARGIN = {"A": 0.25, "B": 0.35}
DATA_ADDITIONS = {"cycle_window_short", "history_7_to_9_years", "derived_tier2_field",
                  "microcap_field_unavailable"}


@dataclass
class MarginResult:
    tier: str
    base_margin: float
    data_addition: float
    endogenous_addition: float
    total_margin: float
    buy_fraction: float           # buy at or below this share of base-case value
    no_thesis: bool
    notes: list


def required_margin(tier: str, data_flags: list[str] | None = None, endogenous_addback: bool = False,
                    underlying_tier: str | None = None, analyst_required_margin: float | None = None
                    ) -> MarginResult:
    """d11 and the charter's tier table.

    Tier A 25%, B 35%; D = its underlying tier (A or B) plus 10 points, on post-cure value;
    C (private-owner case) 50%. Data additions: +5 points each, `cycle_window_short` and
    `history_7_to_9_years` do not stack, total capped at +10. An endogenous add-back adds +10
    outside the cap. Ceiling: for A, B and D, a business needing a margin above 50% before data
    additions is outside the circle (NO_THESIS).
    For Tier C net-nets use `netnet_buy_test` instead; for E use workout arithmetic.
    """
    flags = list(data_flags or [])
    unknown = set(flags) - DATA_ADDITIONS
    assert not unknown, f"unknown data flags {unknown}"
    notes = []
    if tier in ("A", "B"):
        base = BASE_MARGIN[tier]
    elif tier == "D":
        assert underlying_tier in ("A", "B"), "Tier D needs its underlying tier"
        base = BASE_MARGIN[underlying_tier] + 0.10
    elif tier == "C":
        base = 0.50
    else:
        raise ValueError(tier)
    adds = set(flags)
    if "cycle_window_short" in adds and "history_7_to_9_years" in adds:
        adds.discard("history_7_to_9_years")
        notes.append("cycle_window_short and history_7_to_9_years do not stack")
    data_add = min(0.05 * len(adds), 0.10)
    if 0.05 * len(adds) > 0.10:
        notes.append("data additions capped at +10 points")
    endo = 0.10 if endogenous_addback else 0.0
    pre_add = base if analyst_required_margin is None else max(base, analyst_required_margin)
    no_thesis = tier in ("A", "B", "D") and pre_add > 0.50
    if no_thesis:
        notes.append("margin above 50% before data additions: outside the circle, NO_THESIS")
    total = pre_add + data_add + endo
    return MarginResult(tier, pre_add, data_add, endo, total, 1 - total, no_thesis, notes)


def netnet_buy_test(mcap: float, ncav_value: float, dempster: float) -> dict:
    """Tier C net-net: buy only at or below 2/3 of NCAV and at or below Dempster value."""
    return {"two_thirds_ncav": 2 / 3 * ncav_value, "dempster": dempster,
            "passes": mcap <= 2 / 3 * ncav_value and mcap <= dempster}


# --------------------------------------------------------------------------- D3 sensitivity grid

def sensitivity_grid(value_fn, r: float, g: float, dr: float = 0.01, dg: float = 0.02) -> dict:
    """Checklist D3: base-case value at r +/- 1 point and growth +/- 2 points.

    `value_fn(r, g)` returns the per-share value. Returns the grid and its minimum.
    """
    grid = {}
    for rr in (r - dr, r, r + dr):
        for gg in (g - dg, g, g + dg):
            grid[(round(rr, 4), round(gg, 4))] = value_fn(rr, gg)
    return {"grid": grid, "min": min(grid.values()), "max": max(grid.values())}


# --------------------------------------------------------------------------- e2 sizing

def kelly_fraction(outcomes: list[tuple[float, float]]) -> float:
    """e2: f* = argmax_f sum_i p_i ln(1 + f R_i), f in [0, 1]; R_i = value_i / price - 1."""
    total_p = sum(p for p, _ in outcomes)
    assert abs(total_p - 1) < 1e-6, "probabilities must sum to 1"

    def g(f: float) -> float:
        s = 0.0
        for p, R in outcomes:
            x = 1 + f * R
            if x <= 0:
                return -math.inf
            s += p * math.log(x)
        return s

    best_f, best = 0.0, g(0.0)
    steps = 2000
    for i in range(1, steps + 1):
        f = i / steps
        v = g(f)
        if v > best:
            best_f, best = f, v
    return best_f


def position_size(price: float, worst_case_value: float, outcomes: list[tuple[float, float]],
                  tier: str, nav: float | None = None, turnover_p25_daily: float | None = None,
                  sector_room: float = 0.25, tase_room: float | None = None) -> dict:
    """e2: the position at cost is the smallest of quarter-Kelly, the tier cap, the
    permanent-loss budget (5% of NAV / L_worst), the liquidity cap (20 days x 20% x the 25th
    percentile of daily turnover over 60 sessions), the sector cap and the TASE cap.

    `outcomes` are (probability, value per share) pairs. Fractions are of NAV; the liquidity cap
    is an amount in the price currency and is converted to a fraction only if `nav` is given.
    """
    tier_cap = {"A": 0.15, "B": 0.10, "C": 0.05, "C_basket": 0.015, "D": 0.10, "E": 0.05}[tier]
    rets = [(p, v / price - 1) for p, v in outcomes]
    f_star = kelly_fraction(rets)
    limits = {"quarter_kelly": f_star / 4, "tier_cap": tier_cap, "sector_room": sector_room}
    l_worst = max(0.0, (price - worst_case_value) / price)
    limits["permanent_loss_budget"] = 0.05 / l_worst if l_worst > 0 else math.inf
    if tase_room is not None:
        limits["tase_room"] = tase_room
    liquidity_amount = None
    if turnover_p25_daily is not None:
        liquidity_amount = 20 * 0.20 * turnover_p25_daily
        if nav:
            limits["liquidity"] = liquidity_amount / nav
    binding = min(limits, key=limits.get)
    return {"kelly_full": f_star, "l_worst": l_worst, "limits": limits, "size": limits[binding],
            "binding": binding, "liquidity_amount": liquidity_amount}


# --------------------------------------------------------------------------- the value range

@dataclass
class ValueRange:
    """Charter: value is a range: worst-case, conservative, base, optimistic (per share)."""
    company: str
    currency: str
    price: float
    price_date: str
    worst_case: float
    conservative: float
    base: float
    optimistic: float
    margin: MarginResult
    methods: dict = field(default_factory=dict)      # method name -> per-share value

    def buy_price(self) -> float:
        return self.base * self.margin.buy_fraction

    def method_spread(self) -> float:
        """Charter: two independent methods; a disagreement above 30% is resolved first."""
        vals = list(self.methods.values())
        if len(vals) < 2:
            return float("nan")
        return max(vals) / min(vals) - 1

    def report(self) -> str:
        m = self.margin
        lines = [f"== {self.company} ({self.currency}) price {self.price:,.4f} on {self.price_date}"]
        for k, v in self.methods.items():
            lines.append(f"  method {k:<40}{v:>14,.4f}   price/value {self.price / v:>6.2f}")
        spread = self.method_spread()
        if spread == spread:
            lines.append(f"  method spread {spread:.0%}" + ("   ** above 30%: resolve first **" if spread > 0.30 else ""))
        for name in ("worst_case", "conservative", "base", "optimistic"):
            v = getattr(self, name)
            lines.append(f"  {name:<46}{v:>14,.4f}   price/value {self.price / v:>6.2f}")
        lines.append(f"  tier {m.tier}: margin {m.base_margin:.0%} + data {m.data_addition:.0%}"
                     f" + endogenous {m.endogenous_addition:.0%} = {m.total_margin:.0%}"
                     + ("   NO_THESIS (ceiling)" if m.no_thesis else ""))
        lines.append(f"  buy price ({m.buy_fraction:.0%} of base)          {self.buy_price():>14,.4f}"
                     f"   price/buy price {self.price / self.buy_price():.2f}")
        for n in m.notes:
            lines.append(f"  note: {n}")
        return "\n".join(lines)
