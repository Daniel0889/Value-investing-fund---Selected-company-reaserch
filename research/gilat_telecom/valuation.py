"""Gilat Telecom Global Ltd (TASE 1080597) - Charter Revision 4 valuation, 3.11.2026.

UNITS. ILS thousands unless stated; per-share values in ILS, agorot (1 ILS = 100 agorot) and USD.
The company reported in USD to 31.12.2025 and in ILS from 1.1.2026 (functional and presentation
currency ILS: gilat_q2_2026_full p.42). The TTM to 30.6.2026 exists only in ILS, so the valuation is
done in ILS: the USD window FY2021-FY2025 is converted at ONE dated rate, the Bank of Israel
representative rate of 3.157 ILS/USD on 3.11.2026, and per-share values are shown in USD at the same
rate. With a single rate this is arithmetically identical to valuing in USD and converting at 3.157.

CHARTER SECTIONS APPLIED (charter_rev4_draft.md "Text to paste" governs): Mandate (impairment =
the three filed markers; worst-case value); the investment test (Q1-Q4, NO_THESIS); Valuation
methods; Margin of safety by tier (data additions capped at +10); Portfolio constraints (sizing).
framework.md (c) steps 4-10, (d) d1-d11, (e2), (h); checklist.md items by lane (Lane C: groups
B-H as they bind C); small_investor_and_israel.md Part 2.9 and Part 3.
All valuation arithmetic runs through lib/charter_valuation.py (lib/rev4_value.py is superseded).

DOCUMENTS (cited as document id + PDF page index, p.1 = first PDF page):
  gilat_fy2023, gilat_fy2024, gilat_fy2025  annual reports (USD thousands)
  gilat_h1_2026        the Q2 2026 report as supplied: directors' report + separate (solo) data only
  gilat_q2_2026_full   the SAME Q2 2026 report as published on the company's site, which also holds
                       the reviewed consolidated condensed statements (p.27-49) the supplied file lacks;
                       saved at scratchpad/work/gilat_telecom/web/pdf/company_site_q2_2026_full.pdf;
                       its p.1-26 (directors' report) are page-for-page gilat_h1_2026 p.1-26.
  market.md            market data compiled 3.11.2026 (Bizportal, TheMarker, TASE series, Globes feed).

Every input is on its own line with its source. "derived" = computed here from cited inputs;
"assumed" = an analyst assumption with its reason; UNVERIFIED = not tied to a filing.
"""
from __future__ import annotations

import pathlib
import re
import statistics
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "lib"))
from charter_valuation import (  # noqa: E402
    ValueRange, dcf_operations, dempster_value, enterprise_value, epv_operations, equity_bridge,
    excess_cash, graham_yardstick, growth_cap, hurdle, implied_growth, is_cyclical, maintenance_capex,
    ncav, netnet_buy_test, normalised_ebit, owner_earnings, owner_earnings_cash, position_size,
    pretax_multiple, required_margin, sensitivity_grid, tangible_book, unlevered_owner_earnings,
)

# =====================================================================================================
# 0. MARKET INPUTS
# =====================================================================================================
PRICE = 1.653                    # ILS/share: close 3.11.2026 = 165.3 agorot (Bizportal general view "as of 03/11/2026"; TheMarker 17:24; market.md §0, §1.1)
PRICE_DATE = "2026-11-03"        # date of that close
MEGA_MCAP = 198_207_420.626      # ILS, Mega "Ace" snapshot 3.11.2026 14:03 (task input)
SHARES_LISTED = 120_417_631      # TASE "registered capital for trading" 3.11.2026, excludes 4,574,810 dormant (bought-back) shares (Bizportal 3.11.2026; market.md §1.2)
SHARES_30JUN = 118_063_162       # outstanding 30.6.2026, derived from the share-capital line and the 2.3M dormant shares (market.md calc §2; gilat_q2_2026_full p.31, p.49)
FX = 3.157                       # ILS per USD, Bank of Israel representative rate 3.11.2026 (task input)
FX_31DEC25 = 3.19                # ILS per USD at 31.12.2025 (gilat_q2_2026_full p.43)
FX_30JUN26 = 2.978               # ILS per USD at 30.6.2026 (gilat_q2_2026_full p.43), for the FX narrative only
Y10_IL = 0.0416                  # Israel 10-year government yield 3.11.2026 (TradingEconomics; market.md §5)
Y10_US = 0.0491                  # US 10-year 2.11.2026 (US Treasury par curve; market.md §5), cross-check only
TAX = 0.23                       # Israeli statutory corporate tax rate (gilat_fy2025 p.164)

# Liquidity, 60 sessions to 29.10.2026 (TASE daily series from the company IR page; market.md calc §9)
TURNOVER_MEDIAN_60 = 1_303_000   # ILS, median daily turnover over 60 sessions
TURNOVER_P25_60 = 960_250        # ILS, 25th percentile of daily turnover over 60 sessions

# =====================================================================================================
# 1. WINDOW FY2021-FY2025 (USD thousands, audited)
# =====================================================================================================
YEARS = (2021, 2022, 2023, 2024, 2025)
REV_USD = {
    2021: 51_816,                # gilat_fy2023 p.118 (2021 restated)
    2022: 42_997,                # gilat_fy2023 p.118
    2023: 55_154,                # gilat_fy2023 p.118
    2024: 69_592,                # gilat_fy2024 p.120
    2025: 75_793,                # gilat_fy2025 p.127
}
EBIT_USD = {
    2021: -2_731,                # gilat_fy2023 p.118 (includes 3,191 of doubtful debts, gilat_fy2023 p.158: NOT added back, see notes)
    2022: -1_499,                # gilat_fy2023 p.118
    2023: 2_178,                 # gilat_fy2023 p.118
    2024: 4_949,                 # gilat_fy2024 p.120
    2025: 9_689,                 # gilat_fy2025 p.127
}
NI_USD = {2021: -5_423, 2022: -4_064, 2023: 715, 2024: 1_786, 2025: 6_350}       # gilat_fy2023 p.118; gilat_fy2024 p.120; gilat_fy2025 p.127
OCF_USD = {2021: 14_028, 2022: 10_099, 2023: 8_718, 2024: 10_587, 2025: 20_533}   # gilat_fy2023 p.122; gilat_fy2024 p.124; gilat_fy2025 p.131
SBC_USD = {2021: 63, 2022: 123, 2023: 53, 2024: 51, 2025: 88}                    # same pages
CAPEX_PPE_USD = {2021: 1_810, 2022: 1_402, 2023: 3_082, 2024: 2_529, 2025: 1_362}  # gilat_fy2023 p.123; gilat_fy2024 p.125; gilat_fy2025 p.132
CAPEX_INT_USD = {2021: 271, 2022: 62, 2023: 196, 2024: 118, 2025: 82}             # same pages
DEP_PPE_USD = {2021: 3_729, 2022: 2_640, 2023: 1_776, 2024: 1_905, 2025: 2_130}   # gilat_fy2023 p.140; gilat_fy2024 p.143; gilat_fy2025 p.149
AMORT_LIC_USD = {2021: 141, 2022: 151, 2023: 135, 2024: 136, 2025: 177}           # licences/software amortisation, gilat_fy2023 p.141; gilat_fy2025 p.150
AMORT_ACQ_USD = 809              # customer-relations amortisation a year, 2021-2025 (gilat_fy2023 p.141; gilat_fy2025 p.150) = Amort_acq
LEASE_PRIN_USD = {2021: 13_387, 2022: 7_986, 2023: 4_297, 2024: 6_717, 2025: 9_521}  # financing CF, gilat_fy2023 p.123; gilat_fy2024 p.125; gilat_fy2025 p.132
LEASE_INT_USD = {2021: 1_396, 2022: 724, 2023: 408, 2024: 1_698, 2025: 1_788}      # financing CF (Gilat classifies interest in financing), same pages
OTHER_INT_USD = {2021: 1_075, 2022: 910, 2023: 733, 2024: 470, 2025: 858}          # interest paid excl. leases (bonds, loans), same pages
NETPPE_USD = {2021: 4_529, 2022: 3_292, 2023: 4_599, 2024: 5_223, 2025: 4_455}    # 2021 = 1.1.2022 opening (gilat_fy2023 p.140); gilat_fy2023 p.116; gilat_fy2024 p.118; gilat_fy2025 p.125
ROU_USD = {2021: 14_937, 2022: 9_168, 2023: 7_541, 2024: 23_856, 2025: 16_769}    # 2021 = 1.1.2022 opening (gilat_fy2023 p.145); gilat_fy2023 p.116; gilat_fy2024 p.118; gilat_fy2025 p.125

# Balance-sheet lines for the return-on-tangible-capital test (screen_spec 2.3: NWC_op = max(0, (CA - C) - (CL - short-term debt)))
CA_USD = {2022: 22_201, 2023: 25_149, 2024: 26_793, 2025: 52_669}          # gilat_fy2023 p.116; gilat_fy2024 p.118; gilat_fy2025 p.125 (FY2021 balance sheet not in the documents)
C_USD = {2022: 10_897 + 3_983, 2023: 12_215, 2024: 11_017, 2025: 25_036 + 4_717}  # cash + short-term deposits, same pages
CL_USD = {2022: 22_734, 2023: 33_616, 2024: 36_485, 2025: 54_543}          # gilat_fy2023 p.117; gilat_fy2024 p.119 (2023 restated); gilat_fy2025 p.126
STDEBT_USD = {                                                              # current financial debt incl. current leases and conversion-option/warrant liabilities
    2022: 1_320 + 3_598 + 350 + 853 + 15 + 30,     # Series C, leases, state loan, ST credit, warrants, option (gilat_fy2023 p.117)
    2023: 9_972 + 1_832 + 388 + 76 + 196,           # gilat_fy2024 p.119 (restated)
    2024: 6_081 + 9_016 + 324 + 625 + 129 + 483,    # gilat_fy2024 p.119
    2025: 5_243 + 11_382 + 9_304 + 315 + 5_182,     # gilat_fy2025 p.126
}

# 2025 quarters (USD thousands) for the satellite-supplier credit estimate (gilat_fy2025 p.92)
Q25_REV = (15_994, 18_585, 20_075, 21_139)
Q25_GP = (4_521, 5_494, 5_580, 7_455)
H1_2025_REV_USD = Q25_REV[0] + Q25_REV[1]   # derived (gilat_fy2025 p.92)

# =====================================================================================================
# 2. TTM TO 30.6.2026 (ILS thousands) = FY2025 (as translated by the company) - H1 2025 + H1 2026
#    P&L gilat_q2_2026_full p.32; cash flow p.38-39; segment and revenue notes p.46-49
# =====================================================================================================
REV_ILS = {"FY25": 260_335, "H1_25": 124_234, "H1_26": 139_991}        # p.32
EBIT_ILS = {"FY25": 32_980, "H1_25": 12_841, "H1_26": 19_395}          # p.32 (directors' report p.6 prints FY2025 32,981)
PRETAX_ILS = {"FY25": 19_669, "H1_25": 4_313, "H1_26": 15_959}         # p.32
NI_ILS = {"FY25": 21_259, "H1_25": 4_044, "H1_26": 15_770}             # p.32
DA_ILS = {"FY25": 45_310, "H1_25": 24_528, "H1_26": 21_178}            # CF "depreciation and amortisation", p.38
IRU_AMORT_ILS = {"FY25": 3_506, "H1_25": 0, "H1_26": 3_449}            # CF "amortisation of deferred expenses - fibre IRU", p.38
SBC_ILS = {"FY25": 292, "H1_25": 72, "H1_26": 1_050}                   # p.38
FX_CASH_LOSS_ILS = {"FY25": -7_686, "H1_25": 693, "H1_26": 1_194}      # CF "FX loss (gain) on cash balances" (negative = gain), p.38
OPTION_REVAL_ILS = {"FY25": 8_663 - 609 - 456, "H1_25": 7_303 - 423 - 311, "H1_26": 0}  # Series D, Series C options, warrants revaluation, p.38
OCF_ILS = {"FY25": 69_146, "H1_25": 21_425, "H1_26": 33_246}           # net cash from operations, p.38
IRU_PAID_ILS = {"FY25": 13_752, "H1_25": 10_711, "H1_26": 10_673}      # CF "increase in deferred expenses" = Bezeq IRU payments, p.38
CAPEX_ILS = {"FY25": 4_719 + 276, "H1_25": 2_596 + 68, "H1_26": 7_546 + 282}   # PP&E + intangibles, p.39
LEASE_PRIN_ILS = {"FY25": 29_364, "H1_25": 16_092, "H1_26": 15_318}    # p.39
LEASE_INT_ILS = {"FY25": 9_584, "H1_25": 3_526, "H1_26": 1_892}        # p.39 (the FY2025 ILS split differs from the USD statement; total lease cash is consistent)
BOND_INT_ILS = {"FY25": 2_436, "H1_25": 538, "H1_26": 1_246}           # p.39
SAT_LEASE_DEP_TTM = 29_676       # satellite-lease (ROU) depreciation TTM, directors' report tables (gilat_h1_2026 p.6-7, p.13; derived in financials.json)
OTHER_ROU_DEP_USD = 9_983 - 9_082  # non-satellite ROU depreciation FY2025 (gilat_fy2025 p.159), used only to split TTM D&A (UNVERIFIED for TTM)
EQUIP_REV_SAT = {"H1_25": 10_152, "H1_26": 14_331}                      # satellite-segment equipment revenue (gilat_q2_2026_full p.49)
EQUIP_GM_2025 = 0.313            # company equipment gross margin 2025 (business_calcs §3, from gilat_fy2025 p.173): derived

# =====================================================================================================
# 3. BALANCE SHEET 30.6.2026 (ILS thousands; gilat_q2_2026_full p.30-31; summary gilat_h1_2026 p.9-10)
# =====================================================================================================
CASH = 92_955                    # cash and equivalents (p.30)
RESTRICTED = 3_500               # restricted cash, pledged for guarantees (p.30; gilat_fy2025 p.158): excluded from cash
RECEIVABLES = 63_411             # customers (p.30)
DEFERRED_ST = 6_974              # deferred expenses, short-term (Bezeq IRU prepaid) (p.30)
OTHER_REC = 8_862                # other receivables and prepaid (p.30)
INVENTORY = 3_988                # (p.30)
CURRENT_ASSETS = 179_955         # (p.30)
DEFERRED_LT = 9_255              # deferred expenses, long-term (Bezeq IRU prepaid) (p.30)
ROU = 43_241                     # right-of-use assets (p.30)
PPE = 18_017                     # (p.30)
INTANGIBLES = 21_337             # intangibles incl. goodwill (goodwill USD 4,428, gilat_fy2025 p.150) (p.30)
TOTAL_ASSETS = 274_482           # (p.30)
SERIES_C_LIAB = 2_206            # convertible Series C, current (p.31)
LEASES_ST = 26_232               # (p.31)
CURRENT_LIAB = 110_920           # (p.31)
SERIES_D_LIAB = 24_307           # convertible Series D liability component, non-current (p.31)
LEASES_LT = 6_884                # (p.31)
TOTAL_LIAB = 142_111             # (p.31)
EQUITY = 132_371                 # (p.31); NCI nil, preferred nil (p.31)
# Identity checks (checklist C7)
EPS_BASIC_H1_26 = 0.1459         # ILS, basic EPS H1 2026 (gilat_q2_2026_full p.32)
WEIGHTED_SHARES_H1_26 = 108_088  # thousands, basic weighted shares H1 2026 (p.32)
INVESTING_CF_H1_26 = 7_219       # (p.39)
FINANCING_CF_H1_26 = -26_091     # (p.39)
FX_ON_CASH_H1_26 = -1_284        # effect of exchange-rate changes on cash (p.39)
CASH_OPENING_2026 = 79_865       # cash 1.1.2026 (p.39; = 31.12.2025, p.30)

# Events after 30.6.2026 that move cash or claims (pro forma to 3.11.2026; Q3 operating cash flow unknown and NOT added)
OCT_BUYBACK = 4_620              # 2,274,810 shares at ~203.1 agorot, 7-21.10.2026 (Globes insider feed, TASE counts; market.md calc §3): UNVERIFIED vs Maya
SERIES_C_PUBLIC_PAR_19AUG = 984_967       # ILS par held by the public at 19.8.2026 (gilat_h1_2026 p.22)
SERIES_C_CONVERTED_AFTER_19AUG = 192_435  # shares, implied by TASE counts (market.md calc §4): derived, UNVERIFIED
SERIES_C_CONV_PRICE = 1.35       # ILS par per share (gilat_h1_2026 p.22)
SERIES_C_COUPON_HALF = 0.045 / 2  # final semi-annual coupon (gilat_h1_2026 p.22)
SERIES_D_PAR = 26_337_927        # ILS par outstanding 3.11.2026: next coupon ILS 724,293 = 2.75% of par (Bizportal bond data; market.md §1.4): derived
SERIES_D_OCT_CONVERSIONS = 509_030  # shares issued in October 2026 on conversion (TASE counts; market.md calc §3): derived
SERIES_D_COUPON_HALF = 0.055 / 2  # 1.10.2026 coupon (gilat_h1_2026 p.24)
SERIES_D_CONV_PRICE = 1.00       # ILS par per share until 1.4.2028, then 1.40 (gilat_h1_2026 p.24)

# Options (net exercise; gilat_fy2025 p.166, p.172)
OPTIONS = [
    (2_000_000, 1.1015),         # CEO package A, December 2025 (gilat_fy2025 p.166)
    (2_000_000, 0.927),          # CEO package B (p.166)
    (750_000, 1.1015),           # 32 employees/officers package A, November 2025 (p.166)
    (3_915_000, 0.927),          # package B (p.166)
    (12_093_500 - 8_665_000, 0.23 * FX_31DEC25),  # older options at 31.12.2025 (p.172); weighted strike of the exercisable ones USD 0.23 (p.172) at 3.19: derived; upper bound on the count (some exercised in H1 2026)
]

# =====================================================================================================
# 4. BEZEQ FIBRE IRU (off balance sheet except amounts paid)
# =====================================================================================================
IRU1_LINES = 18_000              # original agreement, December 2024 (gilat_fy2025 p.152)
IRU1_PRICE = 4_890               # ILS per line for 15 years (gilat_fy2025 p.152); total ILS 88.02M + VAT (p.153)
IRU2_LINES = 36_000              # addendum pulse 1, December 2025-2028, 12 quarterly tranches of 3,000 (gilat_fy2025 p.183)
IRU2_TOTAL = 160_000             # ILS thousands "assuming full exercise", CPI-linked (gilat_fy2025 p.183, p.42)
IRU_OM_RATE = 0.04               # annual O&M fee, % of consideration (gilat_fy2025 p.153)
IRU_VENDOR_RATE = 0.05           # interest if a pulse is spread over 10 annual payments: 5% for pulse 1 (p.153); assumed 5% for the rest (Bezeq bond yield, not disclosed)
IRU_INSTALMENTS = 10             # annual payments if spread (gilat_fy2025 p.153, p.183)
IRU_TERM = 15                    # years of use per line (p.152)
BSA_MONTHLY = 58                 # ILS/line/month, regulated fibre BSA up to 1 Gbps, fixed 2026-2031, unlimited for small ISPs (gilat_fy2025 p.40)
ACTIVE_LINES = 27_600            # "more than ~27,600" lines active under the Bezeq agreement at the report date 19.8.2026 (gilat_h1_2026 p.5)
IRU_PAID_TO_30JUN = IRU_PAID_ILS["FY25"] + IRU_PAID_ILS["H1_26"]   # derived (gilat_q2_2026_full p.38)

# =====================================================================================================
# 5. HELPERS (share-count and present-value arithmetic only; every valuation step uses the library)
# =====================================================================================================

def ttm(d: dict) -> float:
    """TTM = FY2025 - H1 2025 + H1 2026 (all ILS)."""
    return d["FY25"] - d["H1_25"] + d["H1_26"]


def option_shares(v: float) -> float:
    """Net-exercise dilution at a per-share value v: sum n x max(0, 1 - K / v)."""
    return sum(n * max(0.0, 1 - k / v) for n, k in OPTIONS) if v > 0 else 0.0


def _per_share(numerator_k: float, shares: float) -> float:
    """Fixed point v = numerator / (shares + option_shares(v)); numerator in ILS thousands."""
    if numerator_k <= 0:
        return 0.0
    v = numerator_k * 1000 / shares
    for _ in range(200):
        v = numerator_k * 1000 / (shares + option_shares(v))
    return v


def per_share(equity_before_d: float) -> tuple[float, str]:
    """Shareholders' value per share. Series D holders convert (1 share per ILS 1 par) only when that is
    worth more to them than par; shareholders then get min(converted, not converted) (proof in notes)."""
    v_conv = _per_share(equity_before_d, SHARES_LISTED + SERIES_D_PAR)
    v_debt = _per_share(equity_before_d - SERIES_D_PAR / 1000, SHARES_LISTED)
    if min(v_conv, v_debt) <= 0:
        return 0.0, "equity nil: claims exceed value"
    return (v_conv, "Series D converts") if v_conv <= v_debt else (v_debt, "Series D stays debt at par")


def pv_iru_line(price: float, r: float) -> float:
    """PV at r of one IRU line on the contract terms: 10 annual principal payments from delivery
    (t = 0..9) with vendor interest on the unpaid balance, plus the 4% O&M fee for 15 years (mid-year)."""
    pv = 0.0
    for t in range(IRU_INSTALMENTS):
        interest = IRU_VENDOR_RATE * price * (1 - t / IRU_INSTALMENTS) if t > 0 else 0.0
        pv += (price / IRU_INSTALMENTS + interest) / (1 + r) ** t
    pv += sum(IRU_OM_RATE * price / (1 + r) ** (t - 0.5) for t in range(1, IRU_TERM + 1))
    return pv


def pv_bsa_line(r: float) -> float:
    """PV at r of renting the same line at the regulated BSA price for 15 years (mid-year)."""
    return sum(BSA_MONTHLY * 12 / (1 + r) ** (t - 0.5) for t in range(1, IRU_TERM + 1))


def fmt(v: float) -> str:
    return f"{v:7.3f} ILS ({v * 100:6.1f} ag; USD {v / FX:6.3f})"


out: list[str] = []
P = out.append

# =====================================================================================================
# 0. Market, hurdle
# =====================================================================================================
R = hurdle(max(Y10_IL, 0.0))                       # ILS cash flows: r = max(10%, y10 + 3 points)
MCAP = PRICE * SHARES_LISTED / 1000                # ILS thousands
P("GILAT TELECOM GLOBAL LTD (TASE 1080597) - CHARTER REV 4 VALUATION, 3.11.2026")
P("ILS thousands unless stated; per-share values in ILS (agorot; USD at the BoI rate 3.157 of 3.11.2026).")
P("Reporting currency: USD to FY2025, ILS from 1.1.2026; the TTM to 30.6.2026 is ILS. USD window converted at 3.157.")
P("")
P("== 0. Market inputs")
P(f"  price {PRICE:.3f} ILS ({PRICE * 100:.1f} ag), close {PRICE_DATE}; Mega snapshot 14:03 implies {MEGA_MCAP / SHARES_LISTED:.4f} ILS "
  f"({(MEGA_MCAP / SHARES_LISTED / PRICE - 1):+.1%})")
P(f"  shares listed {SHARES_LISTED:,} (ex dormant); market cap {MCAP:,.0f}k ILS = USD {MCAP / FX / 1000:,.1f}M at {FX}")
P(f"  hurdle r = max(10%, IL y10 {Y10_IL:.2%} + 3 points) = {R:.0%} (US y10 {Y10_US:.2%} + 3 = {Y10_US + 0.03:.2%}: also below 10%)")
P(f"  Series D {SERIES_D_PAR:,} ILS par converts 1:1 at ILS {SERIES_D_CONV_PRICE:.2f} until 1.4.2028 -> {SERIES_D_PAR:,} shares if converted")
P(f"  options: {sum(n for n, _ in OPTIONS):,} gross; net-exercise shares at the price {option_shares(PRICE):,.0f}")
P(f"  fully diluted at the price: {SHARES_LISTED + SERIES_D_PAR + option_shares(PRICE):,.0f} shares")

# =====================================================================================================
# 1. TTM build and one-offs
# =====================================================================================================
REV_TTM = ttm(REV_ILS)
EBIT_TTM = ttm(EBIT_ILS)
PRETAX_TTM = ttm(PRETAX_ILS)
NI_TTM = ttm(NI_ILS)
DA_TTM = ttm(DA_ILS)
IRU_AMORT_TTM = ttm(IRU_AMORT_ILS)
SBC_TTM = ttm(SBC_ILS)
FX_CASH_TTM = ttm(FX_CASH_LOSS_ILS)
OPTION_REVAL_TTM = ttm(OPTION_REVAL_ILS)
OCF_TTM = ttm(OCF_ILS)
IRU_PAID_TTM = ttm(IRU_PAID_ILS)
CAPEX_TTM = ttm(CAPEX_ILS)
LEASE_PRIN_TTM = ttm(LEASE_PRIN_ILS)
LEASE_INT_TTM = ttm(LEASE_INT_ILS)
BOND_INT_TTM = ttm(BOND_INT_ILS)

# One-off 1: satellite-supplier credit in 2025 (named gilat_fy2025 p.96, p.160; amount not disclosed). Estimate =
# Q4 2025 gross profit above the Q1-Q3 2025 gross margin (derived, UNVERIFIED).
gm_q1_q3 = sum(Q25_GP[:3]) / sum(Q25_REV[:3])
SUPPLIER_CREDIT_USD = Q25_GP[3] - gm_q1_q3 * Q25_REV[3]
FX_H2_2025 = (REV_ILS["FY25"] - REV_ILS["H1_25"]) / (REV_USD[2025] - H1_2025_REV_USD)   # implied H2 2025 average rate (derived)
SUPPLIER_CREDIT_TTM = SUPPLIER_CREDIT_USD * FX_H2_2025   # the credit sits in H2 2025, inside the TTM
# One-off 2: one-off war equipment revenue in H1 2026 (named gilat_h1_2026 p.12; amount not disclosed). Estimate = the rise
# in satellite equipment revenue H1 2026 over H1 2025 (gilat_q2_2026_full p.49) at the 2025 equipment gross margin (UNVERIFIED).
ONEOFF_EQUIP_REV = EQUIP_REV_SAT["H1_26"] - EQUIP_REV_SAT["H1_25"]
ONEOFF_EQUIP_PROFIT = ONEOFF_EQUIP_REV * EQUIP_GM_2025

P("")
P("== 1. TTM to 30.6.2026 (FY2025 - H1 2025 + H1 2026, ILS; gilat_q2_2026_full p.32, p.38-39)")
P(f"  revenue {REV_TTM:,.0f}; EBIT {EBIT_TTM:,.0f} ({EBIT_TTM / REV_TTM:.1%}); pre-tax {PRETAX_TTM:,.0f}; net income {NI_TTM:,.0f}; OCF {OCF_TTM:,.0f}"
  "   (Mega: op. income 39,534, NI 32,985, OCF 80,967)")
P(f"  D&A {DA_TTM:,.0f} + IRU amortisation {IRU_AMORT_TTM:,.0f}; SBC {SBC_TTM:,.0f}; capex {CAPEX_TTM:,.0f}; IRU payments {IRU_PAID_TTM:,.0f}")
P(f"  lease principal {LEASE_PRIN_TTM:,.0f} + lease interest {LEASE_INT_TTM:,.0f} = {LEASE_PRIN_TTM + LEASE_INT_TTM:,.0f}; bond interest paid {BOND_INT_TTM:,.0f}")
P(f"  non-operating items inside TTM NI: FX gain on cash {-FX_CASH_TTM:,.0f}; option/warrant revaluation loss {OPTION_REVAL_TTM:,.0f};"
  f" tax line {PRETAX_TTM - NI_TTM:,.0f} (a benefit: DTA recognition and tax losses)")
P(f"  one-off 1, 2025 satellite-supplier credit (estimate): Q4 2025 GP above the Q1-Q3 margin {gm_q1_q3:.2%} = USD {SUPPLIER_CREDIT_USD:,.0f}"
  f" = ILS {SUPPLIER_CREDIT_TTM:,.0f} at the implied H2 2025 rate {FX_H2_2025:.4f}")
P(f"  one-off 2, H1 2026 war equipment (estimate): equipment revenue +{ONEOFF_EQUIP_REV:,.0f} x {EQUIP_GM_2025:.1%} = {ONEOFF_EQUIP_PROFIT:,.0f}")
cf_foot = OCF_ILS["H1_26"] + INVESTING_CF_H1_26 + FINANCING_CF_H1_26 + FX_ON_CASH_H1_26 - (CASH - CASH_OPENING_2026)
P(f"  C7 identities (30.6.2026, consolidated): assets - liabilities - equity = {TOTAL_ASSETS - TOTAL_LIAB - EQUITY:,.0f};"
  f" H1 2026 cash flow foots to the cash change: difference {cf_foot:,.0f}; NI / basic EPS = {NI_ILS['H1_26'] / EPS_BASIC_H1_26:,.0f}k"
  f" vs weighted basic shares {WEIGHTED_SHARES_H1_26:,}k")

# =====================================================================================================
# 2. Lane and tier evidence
# =====================================================================================================
EBIT_ADJ_USD = dict(EBIT_USD)
EBIT_ADJ_USD[2025] = EBIT_USD[2025] - SUPPLIER_CREDIT_USD      # sign-aware: a one-off gain removed
EBIT_ADJ_TTM = EBIT_TTM - SUPPLIER_CREDIT_TTM - ONEOFF_EQUIP_PROFIT
REV_ADJ_TTM = REV_TTM - ONEOFF_EQUIP_REV

P("")
P("== 2. Lane and tier evidence (framework d11; checklist A3, C2; screen_spec 2.3)")
P("  2a. Pre-tax return on tangible capital = EBIT_adj / (NWC_op + net PP&E + ROU) (IFRS basis; NWC_op floored at 0)")
rotc = {}
for y in YEARS:
    if y in CA_USD:
        nwc_op = max(0.0, (CA_USD[y] - C_USD[y]) - (CL_USD[y] - STDEBT_USD[y]))
    else:
        nwc_op = 0.0                                            # FY2021 balance sheet missing: lower bound on capital
    cap = nwc_op + NETPPE_USD[y] + ROU_USD[y]
    rotc[y] = EBIT_ADJ_USD[y] / cap
    P(f"      FY{y}  EBIT_adj {EBIT_ADJ_USD[y]:>8,.0f} USD k  capital {cap:>8,.0f}  ROTC {rotc[y]:>7.1%}"
      + ("   (FY2021: NWC_op unknown, set to 0)" if y == 2021 else ""))
nwc_ttm = max(0.0, (CURRENT_ASSETS - CASH) - (CURRENT_LIAB - (SERIES_C_LIAB + LEASES_ST)))
cap_ttm = nwc_ttm + PPE + ROU
rotc["TTM"] = EBIT_ADJ_TTM / cap_ttm
P(f"      TTM     EBIT_adj {EBIT_ADJ_TTM:>8,.0f} ILS k  capital {cap_ttm:>8,.0f}  ROTC {rotc['TTM']:>7.1%}")
rotc_vals = list(rotc.values())
P(f"      median {statistics.median(rotc_vals):.1%}, minimum {min(rotc_vals):.1%} over FY2021-FY2025 + TTM"
  " -> Tier A needs >= 20% and never < 10%: fails; B's 12-20% band only on the median")

# =====================================================================================================
# 3. Normalised earnings (d2)
# =====================================================================================================
REV_W_ILS = [REV_USD[y] * FX for y in YEARS]
EBIT_W_ILS = [EBIT_ADJ_USD[y] * FX for y in YEARS]
norm6 = normalised_ebit(REV_ADJ_TTM, EBIT_W_ILS + [EBIT_ADJ_TTM], REV_W_ILS + [REV_ADJ_TTM])   # base window: FY2021-FY2025 + TTM
norm5 = normalised_ebit(REV_ADJ_TTM, EBIT_W_ILS, REV_W_ILS)                                       # fiscal years only
EBIT_NORM = norm6.ebit_norm
EBIT_NORM_CONS = norm5.ebit_norm
P("")
P("== 3. Normalised earnings (d2), owner earnings (d1), tax, cash, claims")
P("  EBIT_adj / revenue (one-off gains removed; USD years at 3.157):")
P("      " + "  ".join(f"FY{y} {m:6.1%}" for y, m in zip(YEARS, norm6.detail["margins"][:5]))
  + f"  TTM {norm6.detail['margins'][5]:6.1%}")
P(f"  window FY2021-FY2025 + TTM (six observations; the TTM overlaps FY2025 by six months): m_norm {norm6.m_norm:.2%};"
  f" cyclical {norm6.cyclical} (operating losses in FY2021-FY2022)")
P(f"  BASE EBIT_norm = min(mean {norm6.detail['mean_ebit_adj']:,.0f}, median {norm6.detail['median_ebit_adj']:,.0f},"
  f" mean revenue x m_norm {norm6.detail['mean_rev_x_m_norm']:,.0f}) = {EBIT_NORM:,.0f}"
  f"  ({EBIT_NORM / EBIT_ADJ_TTM:.0%} of TTM EBIT_adj {EBIT_ADJ_TTM:,.0f})")
P(f"  CONSERVATIVE EBIT_norm, fiscal years only: m_norm {norm5.m_norm:.2%}; min(mean {norm5.detail['mean_ebit_adj']:,.0f},"
  f" median {norm5.detail['median_ebit_adj']:,.0f}, mean revenue x m_norm {norm5.detail['mean_rev_x_m_norm']:,.0f}) = {EBIT_NORM_CONS:,.0f}")
P(f"  screen flags: ttm_above_norm {EBIT_ADJ_TTM > 1.5 * EBIT_NORM} (TTM EBIT_adj = {EBIT_ADJ_TTM / EBIT_NORM:.1f}x EBIT_norm): a peak, not depressed earnings;"
  " no endogenous add-back used (FY2021 doubtful debts 3,191 USD k left in)")

# Maintenance capex (d1): floored at depreciation. Dep (charter notation) = PP&E + ROU depreciation + licences + IRU amortisation.
AMORT_ACQ = AMORT_ACQ_USD * FX                                  # derived, ILS a year
DEP_TTM = DA_TTM - AMORT_ACQ + IRU_AMORT_TTM
avg_ppe_rev = statistics.mean(NETPPE_USD[y] / REV_USD[y] for y in YEARS)
MAINT_TTM = maintenance_capex(CAPEX_TTM + IRU_PAID_TTM, DEP_TTM, avg_ppe_rev, REV_TTM - REV_ILS["FY25"])
OTHER_NON_CASH_TTM = FX_CASH_TTM + OPTION_REVAL_TTM           # remove the FX gain on cash, add back the option revaluation loss
OE_D1_TTM = owner_earnings(NI_TTM, DEP_TTM, AMORT_ACQ, OTHER_NON_CASH_TTM, MAINT_TTM)
P(f"  maintenance capex TTM: capex {CAPEX_TTM:,.0f} + IRU payments {IRU_PAID_TTM:,.0f}, growth part {avg_ppe_rev:.2%} x revenue growth"
  f" {REV_TTM - REV_ILS['FY25']:,.0f}; floor Dep {DEP_TTM:,.0f} (PP&E, ROU, licences, IRU) -> {MAINT_TTM:,.0f} (floor binds: leases stay a cost)")
P(f"  owner earnings d1, TTM reported: NI {NI_TTM:,.0f} + Dep {DEP_TTM:,.0f} + Amort_acq {AMORT_ACQ:,.0f} + other non-cash {OTHER_NON_CASH_TTM:,.0f}"
  f" - maintenance {MAINT_TTM:,.0f} = {OE_D1_TTM:,.0f}  (SBC {SBC_TTM:,.0f} stays expensed; tax line is a benefit)")

# Cash proxy (checklist C4): OCF - SBC - maintenance capex on OWNED assets - lease principal; Gilat books lease and bond
# interest in financing, so both are deducted too. IRU payments stay inside OCF (all charged: conservative).
P("  cash proxy (C4) = OCF - lease and other interest - SBC - maintenance capex (owned assets) - lease principal:")
cash_oe = {}
for i, y in enumerate(YEARS):
    d_rev = REV_USD[y] - REV_USD[YEARS[i - 1]] if i > 0 else 0.0   # FY2020 revenue not in the documents
    mc_own = maintenance_capex(CAPEX_PPE_USD[y] + CAPEX_INT_USD[y], DEP_PPE_USD[y] + AMORT_LIC_USD[y], avg_ppe_rev, d_rev)
    cash_oe[y] = owner_earnings_cash(OCF_USD[y] - LEASE_INT_USD[y] - OTHER_INT_USD[y], SBC_USD[y], mc_own, LEASE_PRIN_USD[y])
dep_own_ttm = DA_TTM - SAT_LEASE_DEP_TTM - (OTHER_ROU_DEP_USD + AMORT_ACQ_USD) * FX     # PP&E + licences, TTM estimate (UNVERIFIED split)
mc_own_ttm = maintenance_capex(CAPEX_TTM, dep_own_ttm, avg_ppe_rev, REV_TTM - REV_ILS["FY25"])
CASH_OE_TTM = owner_earnings_cash(OCF_TTM - LEASE_INT_TTM - BOND_INT_TTM, SBC_TTM, mc_own_ttm, LEASE_PRIN_TTM)
P("      " + "  ".join(f"FY{y} {cash_oe[y]:,.0f}" for y in YEARS) + f" (USD k)   TTM {CASH_OE_TTM:,.0f} ILS k ({CASH_OE_TTM / NI_TTM:.0%} of TTM NI)")
pos_ni = sum(v for v in NI_USD.values() if v > 0)
P(f"      C4: window sum {sum(cash_oe.values()):,.0f} / sum of positive NI {pos_ni:,.0f} = {sum(cash_oe.values()) / pos_ni:.0%};"
  f" FY2023-FY2025 {sum(cash_oe[y] for y in (2023, 2024, 2025)) / sum(NI_USD[y] for y in (2023, 2024, 2025)):.0%} (test >= 80%: fails)")
P(f"  tax: statutory {TAX:.0%} (gilat_fy2025 p.164) used; effective TTM {(PRETAX_TTM - NI_TTM) / PRETAX_TTM:+.1%}"
  " (unrecognised tax losses USD 19.0M at 31.12.2025, gilat_fy2025 p.163: the shield is not valued, conservative)")

# Cash and claims, pro forma 3.11.2026
SERIES_C_REDEEMED_PAR = SERIES_C_PUBLIC_PAR_19AUG - SERIES_C_CONVERTED_AFTER_19AUG * SERIES_C_CONV_PRICE
SERIES_C_CASH = SERIES_C_REDEEMED_PAR * (1 + SERIES_C_COUPON_HALF) / 1000
SERIES_D_COUPON = (SERIES_D_PAR + SERIES_D_OCT_CONVERSIONS) * SERIES_D_COUPON_HALF / 1000
CASH_PF = CASH - OCT_BUYBACK - SERIES_C_CASH - SERIES_D_COUPON
CASH_OPEX_TTM = (REV_TTM - EBIT_TTM) - (DA_TTM + IRU_AMORT_TTM) + (LEASE_PRIN_TTM + LEASE_INT_TTM)   # cash operating costs incl. lease payments
EXCESS = excess_cash(CASH_PF, CASH_OPEX_TTM)
LEASES = LEASES_ST + LEASES_LT
P(f"  cash 30.6.2026 {CASH:,.0f} (restricted {RESTRICTED:,.0f} excluded) - Oct buyback {OCT_BUYBACK:,.0f} - Series C final redemption"
  f" {SERIES_C_CASH:,.0f} - Series D coupon {SERIES_D_COUPON:,.0f} = {CASH_PF:,.0f} pro forma 3.11.2026 (Q3 operating cash flow not added)")
P(f"  excess cash (d3) = {CASH_PF:,.0f} - 2/12 x cash operating costs {CASH_OPEX_TTM:,.0f} = {EXCESS:,.0f}")
P(f"  claims: leases {LEASES:,.0f}; Series D {SERIES_D_PAR / 1000:,.0f} at par if not converted (book {SERIES_D_LIAB:,.0f} at 30.6.2026);"
  " Series C nil after 1.9.2026; no bank debt; NCI nil; preferred nil")

# Bezeq IRU: committed consideration, payments, and the economics against renting at the regulated BSA price
IRU2_PRICE = IRU2_TOTAL * 1000 / IRU2_LINES
IRU_COMMITTED = IRU1_LINES * IRU1_PRICE / 1000 + IRU2_TOTAL
IRU_UNPAID_ALL = IRU_COMMITTED - IRU_PAID_TO_30JUN
IRU_UNPAID_IN_SERVICE = (IRU1_LINES * IRU1_PRICE + (ACTIVE_LINES - IRU1_LINES) * IRU2_PRICE) / 1000 - IRU_PAID_TO_30JUN
LINES_UNFILLED = IRU1_LINES + IRU2_LINES - ACTIVE_LINES
pv_iru1, pv_iru2, pv_bsa = pv_iru_line(IRU1_PRICE, R), pv_iru_line(IRU2_PRICE, R), pv_bsa_line(R)
IRU_NPV_VS_BSA = (IRU1_LINES * (pv_bsa - pv_iru1) + IRU2_LINES * (pv_bsa - pv_iru2)) / 1000
P(f"  Bezeq IRU: committed {IRU_COMMITTED:,.0f} for {IRU1_LINES + IRU2_LINES:,} lines; paid to 30.6.2026 {IRU_PAID_TO_30JUN:,.0f};"
  f" unpaid {IRU_UNPAID_ALL:,.0f}, of which for the ~{ACTIVE_LINES:,} lines in service {IRU_UNPAID_IN_SERVICE:,.0f} (UNVERIFIED: the filings do not state it)")
P(f"      PV per line at r over 15 years, contract terms (10 payments at 5%, 4% O&M): IRU-1 {pv_iru1:,.0f}, IRU-2 {pv_iru2:,.0f}"
  f" vs regulated BSA at ILS {BSA_MONTHLY}/month {pv_bsa:,.0f} -> IRU vs BSA if every line is filled: {IRU_NPV_VS_BSA:+,.0f} pre-tax")
P(f"      base treats the lines as NPV-neutral when filled (no credit taken for the {IRU_NPV_VS_BSA:+,.0f});"
  f" {LINES_UNFILLED:,} committed lines are not yet filled; an unused IRU-2 line costs {pv_iru2:,.0f} (PV, pre-tax)")

# Leverage (C2 / tier table), at 3.11.2026 pro forma
nd_bs = SERIES_D_PAR / 1000 + LEASES - CASH_PF
P(f"  net debt with leases (Series D at par) {nd_bs:,.0f} = {nd_bs / EBIT_NORM:.1f}x EBIT_norm (net cash);"
  f" with the IRU unpaid for lines in service {nd_bs + IRU_UNPAID_IN_SERVICE:,.0f} = {(nd_bs + IRU_UNPAID_IN_SERVICE) / EBIT_NORM:.1f}x;"
  f" with all committed IRU {nd_bs + IRU_UNPAID_ALL:,.0f} = {(nd_bs + IRU_UNPAID_ALL) / EBIT_NORM:.1f}x")
P(f"  interest cover TTM: EBIT_adj / (lease + bond interest paid) = {EBIT_ADJ_TTM / (LEASE_INT_TTM + BOND_INT_TTM):.1f}x (C2 asks >= 8x for A/B)")

# =====================================================================================================
# 4. Methods
# =====================================================================================================
OE_NORM = unlevered_owner_earnings(EBIT_NORM, AMORT_ACQ, TAX, DEP_TTM, MAINT_TTM)
OE_NORM_CONS = unlevered_owner_earnings(EBIT_NORM_CONS, AMORT_ACQ, TAX, DEP_TTM, MAINT_TTM)
OE_TTM_UNLEV = unlevered_owner_earnings(EBIT_ADJ_TTM, AMORT_ACQ, TAX, DEP_TTM, MAINT_TTM)


def equity_value(oe_unlev: float, r: float = R, dead_cost: float = 0.0) -> float:
    """d3 bridge before Series D: EPV of operations + excess cash - leases - IRU dead cost (if any)."""
    return equity_bridge(epv_operations(oe_unlev, r), excess_c=EXCESS, lease_liabilities=LEASES, debt=dead_cost)


P("")
P("== 4. Methods")
e_base = equity_value(OE_NORM)
v_epv, how_epv = per_share(e_base)
P(f"  d3 EPV: OE_unlevered = (EBIT_norm {EBIT_NORM:,.0f} + Amort_acq {AMORT_ACQ:,.0f}) x (1 - {TAX:.0%}) + Dep - maintenance (floor: 0)"
  f" = {OE_NORM:,.0f}; / r = {epv_operations(OE_NORM, R):,.0f}")
P(f"      + excess cash {EXCESS:,.0f} - leases {LEASES:,.0f} = {e_base:,.0f} before Series D -> {fmt(v_epv)}  [{how_epv}]")

# d4 DCF. Per-share record: EPS 3-year averages start negative (not computable); revenue per share fell (dilution).
rev_ps = {y: REV_USD[y] / s for y, s in ((2021, 58_438_636), (2025, 93_937_313))}   # shares gilat_fy2023 p.151; gilat_fy2025 p.165
g_rev_ps = (rev_ps[2025] / rev_ps[2021]) ** (1 / 4) - 1
eps_3y = (statistics.mean([-0.093, -0.070, 0.011]), statistics.mean([0.011, 0.0234, 0.0707]))   # basic EPS USD (gilat_fy2023 p.118; gilat_fy2024 p.120; gilat_fy2025 p.127)
G_CAP = growth_cap(None, None, None)          # the per-share OE/EPS record has no rate (negative base); ROIIC set to r: only the 10% cap remains
dcf_base = dcf_operations(OE_NORM, R, 0.0, None, gT=0.0)
v_dcf, _ = per_share(equity_bridge(dcf_base.operations_value, excess_c=EXCESS, lease_liabilities=LEASES))
dcf_rps = dcf_operations(OE_NORM, R, g_rev_ps, None, gT=0.0)
v_dcf_rps, _ = per_share(equity_bridge(dcf_rps.operations_value, excess_c=EXCESS, lease_liabilities=LEASES))
P(f"  d4 growth cap: per-share EPS, 3-year averages {eps_3y[0]:+.4f} -> {eps_3y[1]:+.4f} USD: negative base, no rate (Israeli window, not ten years);"
  f" ROIIC = r (no moat), so growth adds no value; cap g1 <= {G_CAP:.0%}")
P(f"  d4 DCF base, g1 0%, gT 0%: operations {dcf_base.operations_value:,.0f} (terminal {dcf_base.terminal_share:.0%} of total) -> {fmt(v_dcf)} (= EPV)")
P(f"      diagnostic: revenue per share FY2021-FY2025 {g_rev_ps:+.1%} a year (dilution outran growth); at that rate for ten years"
  f" operations {dcf_rps.operations_value:,.0f} -> {fmt(v_dcf_rps)}")
for row in (dcf_base.rows[0], dcf_base.rows[4], dcf_base.rows[9]):
    P(f"      year {row['year']:>2}: OE {row['oe']:,.0f}  reinvestment {row['reinvestment']:,.0f}  FCF {row['fcf']:,.0f}")

# d6/d7 asset values (30.6.2026 balance sheet, shares outstanding 30.6.2026)
NCAV = ncav(CURRENT_ASSETS, TOTAL_LIAB)
DEMPSTER = dempster_value(CASH, RECEIVABLES, INVENTORY, DEFERRED_ST + OTHER_REC, 0.0, TOTAL_LIAB)
TBV = tangible_book(EQUITY, 0.0, INTANGIBLES)
v_tbv = TBV * 1000 / SHARES_30JUN
P(f"  d6 NCAV = current assets {CURRENT_ASSETS:,.0f} - total liabilities {TOTAL_LIAB:,.0f} = {NCAV:,.0f} -> {NCAV * 1000 / SHARES_30JUN:.3f} ILS/share")
P(f"  d6 Dempster = cash 100% + receivables 85% + inventory 60% + prepaid/other 25% - liabilities (PP&E, ROU, IRU at nil) = {DEMPSTER:,.0f}"
  f" -> {DEMPSTER * 1000 / SHARES_30JUN:.3f} ILS/share")
nn = netnet_buy_test(MCAP, NCAV, DEMPSTER)
P(f"      net-net test: market cap {MCAP:,.0f} <= 2/3 NCAV {nn['two_thirds_ncav']:,.0f} and <= Dempster {DEMPSTER:,.0f}? {nn['passes']}"
  f" (market cap = {MCAP / NCAV:.1f}x NCAV)")
P(f"  d7 tangible book = equity {EQUITY:,.0f} - intangibles incl. goodwill {INTANGIBLES:,.0f} = {TBV:,.0f} -> {fmt(v_tbv)}")
P(f"      of which ROU {ROU:,.0f} and IRU prepayments {DEFERRED_ST + DEFERRED_LT:,.0f}: assets tied to lease and Bezeq obligations")
P("  d7 private-owner value: none. No disclosed control transaction; the 2023 placement and rights at 0.30, the July 2025")
P("      placement at 0.88, conversions at 1.00/1.35 and buybacks at 2.60 and ~2.03 are minority trades (framework d7).")

# d5 pre-tax multiple on EV (at the price Series D converts)
EV = enterprise_value(PRICE * (SHARES_LISTED + SERIES_D_PAR) / 1000, 0.0, CASH_PF, LEASES)
pm_norm, pm_ttm = pretax_multiple(EV, EBIT_NORM), pretax_multiple(EV, EBIT_ADJ_TTM)
v_10x, _ = per_share(equity_bridge(10 * EBIT_NORM, excess_c=EXCESS, lease_liabilities=LEASES))
P(f"  d5 EV {EV:,.0f} (as-converted market cap + leases - cash): EV/EBIT_norm {pm_norm['ev_to_ebit_norm']:.1f}x (yield {pm_norm['pretax_yield']:.1%});"
  f" EV/TTM EBIT_adj {pm_ttm['ev_to_ebit_norm']:.1f}x (yield {pm_ttm['pretax_yield']:.1%})")
P(f"      10x EBIT_norm + excess cash - leases -> {fmt(v_10x)} (sanity check; about 10x is d5's fair price for Tier A)")

# d9 Graham's yardstick, ILS government yield (looser than Graham's AA corporate)
NI_NORM_TTM = (PRETAX_TTM - SUPPLIER_CREDIT_TTM - ONEOFF_EQUIP_PROFIT + FX_CASH_TTM + OPTION_REVAL_TTM) * (1 - TAX)
gy = graham_yardstick(NI_NORM_TTM, MCAP, Y10_IL)
P(f"  d9 Graham [I, looser: ILS government yield]: NI_norm_ttm {NI_NORM_TTM:,.0f} (pre-tax less one-offs and non-cash FX/option items, at 23%);"
  f" earnings yield {gy['earnings_yield']:.1%} vs {gy['required_yield']:.2%}; P/E {gy['pe']:.1f} vs cap {gy['pe_cap']:.0f} -> {gy['passes']}")

# d8 implied growth: operations value the price implies
FD_PRICE = SHARES_LISTED + SERIES_D_PAR + option_shares(PRICE)
EV_OPS_IMPLIED = PRICE * FD_PRICE / 1000 + LEASES - EXCESS
IG_NORM = implied_growth(EV_OPS_IMPLIED, OE_NORM, R, None)
IG_TTM = implied_growth(EV_OPS_IMPLIED, OE_TTM_UNLEV, R, None)
P(f"  d8 implied growth: operations value at the price {EV_OPS_IMPLIED:,.0f} (fully diluted {FD_PRICE:,.0f} shares x price + leases - excess cash)")
P(f"      = {EV_OPS_IMPLIED / OE_NORM:.1f}x normalised OE {OE_NORM:,.0f} -> {IG_NORM:+.1%} a year for ten years (no reinvestment charged: the generous reading)")
P(f"      = {EV_OPS_IMPLIED / OE_TTM_UNLEV:.1f}x TTM OE {OE_TTM_UNLEV:,.0f} -> {IG_TTM:+.1%} a year: the price assumes the war-era earnings largely persist")
P(f"      record: revenue per share {g_rev_ps:+.1%} a year FY2021-FY2025; EPS from losses to profits (no rate); implied growth is"
  " above any per-share record (D4 is a FLAG for A/B/D only)")

# =====================================================================================================
# 5. Value range
# =====================================================================================================
# optimistic: TTM run-rate (one-offs removed) persists: war-level demand, the 2026 shekel, Vodacom renewed, ISP fills its lines
v_opt, how_opt = per_share(equity_value(OE_TTM_UNLEV))
# base: charter EBIT_norm over FY2021-FY2025 + TTM; IRU lines filled (NPV-neutral)
v_base, how_base = v_epv, how_epv
# conservative: the base with its single largest identified risk at half strength: the ISP fills only half of the unfilled
# committed lines and pays for the rest unused (after tax: the business stays profitable in this case, at the 23% used for EBIT)
DEAD_CONS = LINES_UNFILLED / 2 * pv_iru2 / 1000 * (1 - TAX)
v_cons, how_cons = per_share(equity_value(OE_NORM, dead_cost=DEAD_CONS))
v_cons_fy, _ = per_share(equity_value(OE_NORM_CONS))                       # variant: fiscal-year EBIT_norm, IRU lines filled
v_cons_both, _ = per_share(equity_value(OE_NORM_CONS, dead_cost=DEAD_CONS))  # variant: both
DEAD_FULL_AT = LINES_UNFILLED * pv_iru2 / 1000 * (1 - TAX)
v_isp_stall, _ = per_share(equity_value(OE_NORM, dead_cost=DEAD_FULL_AT))   # variant: base earnings, ISP stalls at today's lines
# worst (ten years out): pre-war demand, Vodacom lost (3.2027), ISP stalls; liquidation basis: Dempster value pro forma (Series D
# handled at par in per_share) less every unfilled committed IRU line at its PV
DEMPSTER_EX_CD = dempster_value(CASH_PF, RECEIVABLES, INVENTORY, DEFERRED_ST + OTHER_REC, 0.0,
                                TOTAL_LIAB - SERIES_C_LIAB - SERIES_D_LIAB)
DEAD_WORST = LINES_UNFILLED * pv_iru2 / 1000
v_worst, how_worst = per_share(DEMPSTER_EX_CD - DEAD_WORST)
v_worst_no_iru, _ = per_share(DEMPSTER_EX_CD)
PROBS = {"worst": 0.10, "conservative": 0.25, "base": 0.45, "optimistic": 0.20}   # assumed (model judgements, uncalibrated)
VALS = {"worst": v_worst, "conservative": v_cons, "base": v_base, "optimistic": v_opt}
v_pw = sum(PROBS[k] * VALS[k] for k in PROBS)

P("")
P("== 5. Value range (per share, at 3.11.2026)")
P(f"  worst case    {fmt(v_worst)}  ten years out, held with confidence as a floor: pre-war defence demand, Vodacom lost (3.2027),")
P(f"                ISP stalls. Today's liquidation value already sits below the claims: Dempster {DEMPSTER_EX_CD:,.0f} (before Series D)"
  f" - {LINES_UNFILLED:,} unused committed IRU lines {DEAD_WORST:,.0f} (PV, pre-tax) [{how_worst}];")
P(f"                losses as in FY2021-FY2022 only widen the gap. Without the IRU the liquidation floor is {v_worst_no_iru:.3f}")
P(f"  conservative  {fmt(v_cons)}  EPV on base EBIT_norm; the ISP fills half of the {LINES_UNFILLED:,} unfilled IRU lines, the rest paid for"
  f" unused ({DEAD_CONS:,.0f} after tax) [{how_cons}]")
P(f"                variants: fiscal-year EBIT_norm {EBIT_NORM_CONS:,.0f} with the lines filled {v_cons_fy:.3f}; both {v_cons_both:.3f};"
  f" base earnings with the ISP stalled at today's lines {v_isp_stall:.3f}")
P(f"  base          {fmt(v_base)}  EPV on EBIT_norm {EBIT_NORM:,.0f} (FY2021-FY2025 + TTM), IRU lines filled at NPV nil [{how_base}]")
P(f"  optimistic    {fmt(v_opt)}  EPV on TTM EBIT_adj {EBIT_ADJ_TTM:,.0f}: war-era demand and the 2026 shekel persist [{how_opt}]")
P(f"  probabilities {PROBS} -> probability-weighted {fmt(v_pw)}")
P("  impairment markers in the worst case (charter Mandate; checklist E1):")
P("      (1) maturity -> dilution: below ILS 1.00 Series D stays debt, 25% a year due 1.4.2028-2031 (gilat_h1_2026 p.24), and the")
P("          Bezeq instalments run ~10 years; the 2023 rights issue at 0.30 and the 2024 bond-for-share exchange are the precedent")
P(f"      (2) going concern: cash {CASH_PF:,.0f} against unpaid IRU {IRU_UNPAID_ALL:,.0f} (UNVERIFIED) and operating losses as in FY2021-FY2022")
P(f"      (3) assets worth less than debt: Dempster {DEMPSTER:,.0f} vs IRU commitments {IRU_UNPAID_ALL:,.0f} (UNVERIFIED) -> yes")
P("      A plausible path to all three exists: E1 fails closed (capital preservation ranks above return).")

# F4 stresses on the base
USD_COST_PROXY = 24_000                        # USD k a year: USD 2M a month hedged to 12.2026 (gilat_h1_2026 p.19) as the proxy for net USD costs: UNVERIFIED
fx_hit = 0.10 * USD_COST_PROXY * FX            # ILS thousands a year for a 10% rise in USD/ILS (derived)
v_fx_up, _ = per_share(equity_value(unlevered_owner_earnings(EBIT_NORM - fx_hit, AMORT_ACQ, TAX, DEP_TTM, MAINT_TTM)))
v_fx_dn, _ = per_share(equity_value(unlevered_owner_earnings(EBIT_NORM + fx_hit, AMORT_ACQ, TAX, DEP_TTM, MAINT_TTM)))
P("  F4 stresses on base (currency of revenue ~77% ILS, Africa USD; satellite costs USD; debt ILS unlinked fixed; IRU half-CPI-linked):")
P(f"      USD/ILS +10%: pre-tax -{fx_hit:,.0f} a year (USD 24M hedged-cost proxy) -> {fmt(v_fx_up)}; -10% -> {fmt(v_fx_dn)}")
P(f"      the USD is already {FX / FX_30JUN26 - 1:+.1%} since the 30.6.2026 balance-sheet rate {FX_30JUN26} (H1 2026 margins were earned"
  " on a weaker dollar); forwards cover USD 2M a month to 12.2026 and 1.5M in 2027 (gilat_h1_2026 p.19)")
P("      +2 points on rates: no floating debt (Series D fixed 5.5%); r stays 10% (IL y10 6.16% + 3 < 10%); cash earns more: no hit")
P("      high CPI: no CPI-linked debt (gilat_q2_2026_full p.41); Bezeq principal half-linked until each pulse starts; wages ILS: small hit")

# Sensitivity grid around base (D3): r +/- 1 point, g +/- 2 points; ROIIC held at 10% (no moat), terminal growth min(g, 2.5%) >= 0
def base_value(r: float, g: float) -> float:
    res = dcf_operations(OE_NORM, r, g, 0.10 if g > 0 else None, gT=max(0.0, min(g, 0.025)), roiic_T=0.10)
    return per_share(equity_bridge(res.operations_value, excess_c=EXCESS, lease_liabilities=LEASES))[0]


grid = sensitivity_grid(base_value, R, 0.0)
P("  sensitivity grid, base value per share (r +/- 1 point; g +/- 2 points around g 0%; ROIIC 10%):")
P("      r \\ g        -2%      0%     +2%")
for rr in (R - 0.01, R, R + 0.01):
    P(f"      {rr:4.0%}   " + "  ".join(f"{grid['grid'][(round(rr, 4), round(gg, 4))]:6.3f}" for gg in (-0.02, 0.0, 0.02)))
P(f"      minimum {grid['min']:.3f}, maximum {grid['max']:.3f} vs price {PRICE:.3f}: base > price everywhere (D3): {grid['min'] > PRICE}")

# =====================================================================================================
# 6. Margin and buy price
# =====================================================================================================
DATA_FLAGS = ["cycle_window_short", "derived_tier2_field", "microcap_field_unavailable"]
margin = required_margin("C", DATA_FLAGS, endogenous_addback=False)
methods = {
    "EPV, EBIT_norm FY2021-25 + TTM (d3)": v_epv,
    "DCF 10y, g 0%, ROIIC = r (d4)": v_dcf,
    "10x EBIT_norm + net excess cash (d5)": v_10x,
    "tangible book 30.6.2026 (d7)": v_tbv,
}


class _ZeroSafeValueRange(ValueRange):
    """ValueRange.report() divides the price by each value; a scenario value of zero (equity wiped
    out) would raise, so its price/value is printed as n/m. Nothing else changes."""

    NAMES = ("worst_case", "conservative", "base", "optimistic")

    def report(self) -> str:
        zero = [n for n in self.NAMES if getattr(self, n) == 0]
        saved = {n: getattr(self, n) for n in zero}
        for n in zero:
            setattr(self, n, float("nan"))
        try:
            text = super().report()
        finally:
            for n, v in saved.items():
                setattr(self, n, v)
        for n in zero:
            text = re.sub(rf"(  {n}\s+)nan(\s+price/value\s+)nan", lambda m: f"{m.group(1)}{0:.4f}{m.group(2)}n/m", text)
        return text


vr = _ZeroSafeValueRange("Gilat Telecom Global (TASE 1080597), per share", "ILS", PRICE, f"{PRICE_DATE} close",
                         v_worst, v_cons, v_base, v_opt, margin, methods)
BUY = vr.buy_price()
P("")
P("== 6. Margin of safety and buy price")
P(vr.report())
P(f"  data additions: {', '.join(DATA_FLAGS)} (+5 each, capped at +10); no endogenous add-back")
P("  method spread resolved: EPV, DCF (ROIIC = r makes it equal EPV) and 10x pre-tax are one earnings view; tangible book is the")
P(f"      independent asset view. EPV / tangible book = {v_epv / v_tbv:.2f}: normalised NOPAT {OE_NORM:,.0f} on tangible equity {TBV:,.0f}"
  f" = {OE_NORM / TBV:.1%} < r, so value below book; book also holds ROU {ROU:,.0f} and IRU prepayments tied to obligations.")
P(f"  buy price, shadow Tier C ({margin.buy_fraction:.0%} of base): {fmt(BUY)}; price / buy price {PRICE / BUY:.2f}")
P(f"      the charter's own Tier C routes: net-net (<= 2/3 NCAV and <= Dempster) -> {min(nn['two_thirds_ncav'], DEMPSTER) * 1000 / SHARES_LISTED:.3f} ILS;"
  " private-owner value: no disclosed transaction -> no evidenced C line")
SEG_NORM_AFTER_LEASE_INT = 15_099              # analyst segment normalisation, leases as operating costs (business.md §12; business_calcs_output §11): reference only
v_seg, _ = per_share(equity_bridge(epv_operations(unlevered_owner_earnings(SEG_NORM_AFTER_LEASE_INT, AMORT_ACQ, TAX, DEP_TTM, MAINT_TTM), R),
                                   excess_c=EXCESS))   # lease cost already charged there, so the lease liability is not deducted again
P(f"  reference only: on the analyst's segment normalisation (business.md §12: {SEG_NORM_AFTER_LEASE_INT:,} after lease interest) the base"
  f" would be {fmt(v_seg)}; price / that value {PRICE / v_seg:.2f}")

# =====================================================================================================
# 7. Liquidity, sizing and preliminary verdict
# =====================================================================================================
size = position_size(PRICE, v_worst, [(PROBS[k], VALS[k]) for k in PROBS], "C",
                     turnover_p25_daily=TURNOVER_P25_60, tase_room=0.30)
P("")
P("== 7. Liquidity, sizing and preliminary verdict")
P(f"  liquidity: 60-session median turnover {TURNOVER_MEDIAN_60:,} ILS (floor 50,000: passes; above 100,000: no price-reliability block needed);"
  f" 25th percentile {TURNOVER_P25_60:,} ILS")
P(f"  e2 (informational): full Kelly {size['kelly_full']:.0%}; L_worst {size['l_worst']:.0%}; limits "
  + ", ".join(f"{k} {v:.1%}" for k, v in size['limits'].items())
  + f"; liquidity maximum {size['liquidity_amount']:,.0f} ILS at cost -> size {size['size']:.0%} ({size['binding']})")
SHARES_END_2022 = 58_438_636     # gilat_fy2023 p.151
share_multiple = SHARES_LISTED / SHARES_END_2022
share_cagr = share_multiple ** (1 / ((2026 + 307 / 365) - 2023.0)) - 1   # 31.12.2022 (= 2023.0) to 3.11.2026 (day 307): derived
P(f"  lane C, tier C: A/B fail A3 (no moat in the numbers: operating losses FY2021-22, ROTC minimum {min(rotc_vals):.0%}; competition")
P("      'mainly on price', share 'not material', gilat_fy2025 p.32); D needs an A/B franchise; E has no deal. C is the only lane whose")
P(f"      basis (normalised earnings, assets) fits; today it is not a C bargain: market cap {MCAP / NCAV:.1f}x NCAV, TTM EBIT_adj"
  f" {EBIT_ADJ_TTM / EBIT_NORM:.1f}x EBIT_norm (a peak), no private-owner transaction.")
P(f"  VETO items that fail: D2 (price {PRICE / BUY:.1f}x the shadow buy price), D5 (expected return from base far below r: price/base"
  f" {PRICE / v_base:.2f}), E1 (impairment path via the IRU commitments), E3 (no refutable pessimism in the price),")
P(f"      B3 (listed shares x{share_multiple:.2f} since 31.12.2022, {share_cagr:.0%} a year, issued at 0.30-1.35; Series D adds"
  f" {SERIES_D_PAR / SHARES_LISTED:.0%}), H4 (no catalyst, no basket), H5 (no low-cost position; net debt once the IRU is counted).")
P("      Open (fail closed): Q1/A0 circle (theses/CIRCLE.md not available here), B5 (headline metrics exclude the IRU cost; unpaid")
P("      IRU balance undisclosed), D8 (immediate reports read via the company site and news feeds; Maya not reachable).")
P(f"  investment test: Q1 cannot be assessed here; Q2 no (no C bargain today); Q3 no (price/base {PRICE / v_base:.2f}); Q4 the price implies")
P(f"      {IG_NORM:+.1%} a year from normalised earnings, or {IG_TTM:+.1%} from TTM: it already pays for the war-era earnings.")
P("  PRELIMINARY VERDICT: NO_THESIS (not WATCHLIST: price is not the only failure; E1 fails at any price until the IRU exposure is known).")
P("  re-examination triggers (dated, observable):")
P("      1. Vodacom DRC (16.3% of 2025 revenue, gilat_fy2025 p.55-56): renewal announced by 31.3.2027 at >= USD 1M a month, or lost.")
P("      2. Bezeq IRU: the FY2026 annual report (due by 31.3.2027) states the unpaid balance and whether pulse-1 tranches can be declined;")
P(f"         and lines active under the agreement reach {IRU1_LINES + IRU2_LINES:,} by 31.12.2028 (gilat_h1_2026 p.5 reports ~{ACTIVE_LINES:,}).")
P("      3. War premium: satellite-segment revenue in H1 2027 (report due ~8.2027) below 75% of H1 2026 (ILS 119,422k, gilat_h1_2026 p.12)")
P("         confirms the normalisation; at or above it for a second year after the April 2026 ceasefire calls for re-underwriting EBIT_norm.")

P("")
P("Per-share summary (ILS, agorot, USD at 3.157):")
for label, v in (("price", PRICE), ("worst case", v_worst), ("conservative", v_cons), ("base", v_base),
                 ("optimistic", v_opt), ("probability-weighted", v_pw), (f"buy price (shadow Tier C, {margin.buy_fraction:.0%} of base)", BUY)):
    P(f"  {label:<44}{fmt(v)}")
P(f"  implied growth (normalised OE, ten years)   {IG_NORM:+.1%};  on TTM OE {IG_TTM:+.1%}")
P(f"  total margin {margin.total_margin:.0%}; sensitivity minimum {grid['min']:.3f}; method spread {vr.method_spread():.0%}")

if __name__ == "__main__":
    print("\n".join(out))
