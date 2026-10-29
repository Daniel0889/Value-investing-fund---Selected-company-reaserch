"""Rev 4 valuation methods of the value fund.

Every figure in the research docs comes from these functions, not from prose.
Units are whatever the caller passes (e.g. USD billions, KRW trillions, ILS
millions); per-share values divide by the share count in the same units.

Methods (per the fund constitution, Revision 4):
  * owner earnings (Buffett 1986): NI + D&A - maintenance capex - SBC
  * EPV: no-growth earning-power value = owner earnings / r + net cash
  * conservative 10-year DCF: growth capped at 10%, terminal multiple <= 15x
  * 10x pre-tax earnings test (Buffett, 2012 meeting)
  * reverse DCF: the growth rate the price implies
  * NAV / liquidation value for asset-measured businesses
Hurdle r = max(10%, 10-year government yield + 3 points). No beta, no ERP.
"""

from __future__ import annotations

from dataclasses import dataclass, field

MAX_GROWTH = 0.10
MAX_TERMINAL_MULTIPLE = 15.0

# Fraction of base value the fund pays at most, by grade.
GRADE_BUY_FRACTION = {"A": 0.75, "B": 0.65, "C": 0.50}


def hurdle(gov_10y: float) -> float:
    return max(0.10, gov_10y + 0.03)


def owner_earnings(net_income: float, d_and_a: float, maintenance_capex: float) -> float:
    """GAAP net income already expenses stock compensation, so it is not added back."""
    return net_income + d_and_a - maintenance_capex


def owner_earnings_from_ocf(ocf: float, maintenance_capex: float, sbc: float) -> float:
    """Operating cash flow adds stock compensation back; take it out again."""
    return ocf - maintenance_capex - sbc


def explicit_dcf(revenue0: float, growth: list[float], ebitda_margin: list[float],
                 capex: list[float], capex_history: list[float], r: float,
                 tax: float, terminal_multiple: float = MAX_TERMINAL_MULTIPLE,
                 life: int = 8) -> tuple[float, list[dict]]:
    """Ten explicit years for capital-heavy growth: FCF = EBIT*(1-t) + D&A - capex.

    D&A is straight-line over `life` years on each capex vintage, starting the
    year after it is spent. `capex_history` holds the most recent `life` years,
    oldest first. Returns (PV of the business before net cash, yearly rows).
    """
    assert len(growth) == len(ebitda_margin) == len(capex) == 10
    vintages = list(capex_history)
    rev, pv, rows = revenue0, 0.0, []
    for year in range(10):
        rev *= 1 + min(growth[year], 1.0)
        dep = sum(vintages[-life:]) / life
        ebitda = rev * ebitda_margin[year]
        ebit = ebitda - dep
        fcf = ebit * (1 - tax) + dep - capex[year]
        pv += fcf / (1 + r) ** (year + 1)
        vintages.append(capex[year])
        rows.append({"revenue": rev, "ebitda": ebitda, "d_and_a": dep, "ebit": ebit,
                     "ebit_margin": ebit / rev, "capex": capex[year], "fcf": fcf})
    tm = min(terminal_multiple, MAX_TERMINAL_MULTIPLE)
    pv += rows[-1]["fcf"] * tm / (1 + r) ** 10
    return pv, rows


def epv(owner_earn: float, r: float, net_cash: float = 0.0) -> float:
    return owner_earn / r + net_cash


def ten_x_pretax(pretax_operating_income: float, net_cash: float = 0.0) -> float:
    return 10.0 * pretax_operating_income + net_cash


def dcf(base_cash_flow: float, r: float, growth_1_5: float, growth_6_10: float,
        terminal_multiple: float, net_cash: float = 0.0) -> float:
    """Ten years of owner cash flow, then a multiple on year-10 cash flow."""
    g1 = min(growth_1_5, MAX_GROWTH)
    g2 = min(growth_6_10, MAX_GROWTH)
    tm = min(terminal_multiple, MAX_TERMINAL_MULTIPLE)
    value, cf = 0.0, base_cash_flow
    for year in range(1, 11):
        cf *= 1 + (g1 if year <= 5 else g2)
        value += cf / (1 + r) ** year
    value += cf * tm / (1 + r) ** 10
    return value + net_cash


def reverse_dcf(market_cap: float, base_cash_flow: float, r: float,
                terminal_multiple: float = MAX_TERMINAL_MULTIPLE,
                net_cash: float = 0.0) -> float:
    """Constant 10-year growth rate the price implies (bisection)."""
    target = market_cap - net_cash
    lo, hi = -0.5, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        v = 0.0
        cf = base_cash_flow
        for year in range(1, 11):
            cf *= 1 + mid
            v += cf / (1 + r) ** year
        v += cf * terminal_multiple / (1 + r) ** 10
        if v < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def buy_price(base_value_per_share: float, grade: str, extra_margin: float = 0.0) -> float:
    """Highest price the fund pays: grade fraction minus any extra margin points."""
    return base_value_per_share * (GRADE_BUY_FRACTION[grade] - extra_margin)


@dataclass
class Scenario:
    name: str
    probability: float
    value_per_share: float


@dataclass
class Valuation:
    company: str
    currency: str
    price: float
    shares: float
    grade: str
    extra_margin: float = 0.0
    methods: dict[str, float] = field(default_factory=dict)   # per-share values
    scenarios: list[Scenario] = field(default_factory=list)

    def base_value(self) -> float:
        base = [s for s in self.scenarios if s.name == "base"]
        return base[0].value_per_share

    def weighted_value(self) -> float:
        return sum(s.probability * s.value_per_share for s in self.scenarios)

    def buy_line(self) -> float:
        return buy_price(self.base_value(), self.grade, self.extra_margin)

    def report(self) -> str:
        lines = [f"== {self.company} ({self.currency}) price {self.price:,.2f} grade {self.grade}"]
        for k, v in self.methods.items():
            lines.append(f"  {k:<34}{v:>12,.2f}   price/value {self.price / v:>5.2f}")
        for s in self.scenarios:
            lines.append(f"  scenario {s.name:<8} p={s.probability:.2f}  {s.value_per_share:>12,.2f}")
        lines.append(f"  probability-weighted value         {self.weighted_value():>12,.2f}")
        lines.append(f"  buy line ({GRADE_BUY_FRACTION[self.grade]:.0%} - {self.extra_margin:.0%})"
                     f"            {self.buy_line():>12,.2f}   price/line {self.price / self.buy_line():.2f}")
        return "\n".join(lines)
