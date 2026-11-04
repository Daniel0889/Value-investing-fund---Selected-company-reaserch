"""Gilat Telecom Global Ltd (TASE 1080597) - Charter Revision 4 valuation, 3.11.2026, as revised at the CIO gate.

UNITS. ILS thousands unless stated; per-share values in ILS, agorot (1 ILS = 100 agorot) and USD.
The company reported in USD to 31.12.2025 and in ILS from 1.1.2026 (functional and presentation
currency ILS: gilat_q2_2026_full p.42). The TTM to 30.6.2026 exists only in ILS, so the valuation is
done in ILS: the USD window FY2020-FY2025 is converted at ONE dated rate, the Bank of Israel
representative rate of 3.157 ILS/USD on 3.11.2026, and per-share values are shown in USD at the same
rate. With a single rate this is arithmetically identical to valuing in USD and converting at 3.157.

CHARTER SECTIONS APPLIED (charter_rev4_draft.md "Text to paste" governs): Mandate (impairment =
the three filed markers; worst-case value); the investment test (Q1-Q4, NO_THESIS); Valuation
methods; Margin of safety by tier (data additions capped at +10); Portfolio constraints (sizing).
framework.md (c) steps 4-10, (d) d1-d11, (e2), (h); checklist.md items by lane (Lane C);
small_investor_and_israel.md Part 2.9 and Part 3. All valuation arithmetic runs through
lib/charter_valuation.py (lib/rev4_value.py is superseded; lib/valuation.py is not available here).

CIO GATE REVISION (3.11.2026). The red-team objections (gilat_telecom:redteam-accounting O1-O11,
gilat_telecom:redteam-business O1-O10) are answered one by one in
research/gilat_telecom/work/gate.md (drafted in scratchpad/work/gilat_telecom/). What changed in this file:
  A-O1  the cyclical window W is fiscal years FY2020-FY2025 (framework d2: "FY2020 to the latest year"); FY2020
        was obtained from the company's own FY2022 and FY2021 annual reports on its website; the TTM is no
        longer a W observation (it counted H2 2025 twice and added the war-peak H1 2026).
  A-O2  F4 stresses use the filed linkage table (flow plus remeasurement) at +10% and +20%, and a CPI stress
        on the half-CPI-linked Bezeq IRU commitments.
  A-O3  E1 is tested as a dated cash runway; the old marker (2)/(3) lines are withdrawn.
  A-O4  the equity bridge restates the 30.6.2026 USD monetary items at the 3.11.2026 rate.
  A-O6..A-O11  lease interest on both splits; C6 stress-year cover; tangible book on the 3.11.2026 basis and the
        method spread against the lane's asset methods; TTM ROTC on average capital; FX stripped from
        NI_norm_ttm; segment figures from the FS note.
  B-O2  the "shadow" Tier C buy line (base x 40%) is withdrawn: EPV is not private-owner value (d7, d11).
  B-O3  probabilities 15/30/45/10; the conservative case is Vodacom not renewed; the optimistic case is net of
        the IRU accounting gap.
  B-O6  the base carries an expected cost for committed but unfilled IRU lines.

FINAL EDIT AFTER VERIFICATION (record as of 3.11.2026; no price, rate or date changed). Findings and dispositions are
in research/gilat_telecom/verification.md. What changed in this file:
  AR-1  the d3 add-back Amort_acq now matches the acquired amortisation inside EBIT_norm: its W mean, USD 968k a year
        (customer relations 809, 814 in FY2023, plus FY2020's 949 of acquired contract-backlog amortisation,
        gilat_fy2021 p.146), not 809 alone. The 949 is a mandated add-back (d1, d3), not an endogenous one.
  AR-2  FY2021 PP&E depreciation is the filed 3,353 (gilat_fy2021 p.145), not the residual 3,729.
  AR-3  the PV of each unfilled IRU line is dated from its tranche's delivery back to 3.11.2026.
  AR-4, AR-5, CH-2, CH-4, CH-5, CH-8, MF-8, MF-9: labels and printed reasons (net-net reference line, not a buy
        price; F4 split into flow and remeasurement; the verdict's price-independent list; Q2/Q3 on the Lane C tests;
        the three falsification conditions as in gate.md §3; CEO quote and filing quotes as filed). CH-1: B7 fails closed.

DOCUMENTS (cited as document id + PDF page index, p.1 = first PDF page):
  gilat_fy2023, gilat_fy2024, gilat_fy2025  annual reports (USD thousands), supplied by the investor
  gilat_h1_2026        the Q2 2026 report as supplied: directors' report + separate (solo) data only
  gilat_q2_2026_full   the SAME Q2 2026 report as published on the company's site, with the reviewed
                       consolidated condensed statements (p.27-49); its p.1-26 are page for page gilat_h1_2026
                       (scratchpad/work/gilat_telecom/web/pdf/company_site_q2_2026_full.pdf)
  gilat_fy2022         the 2022 annual report, company site, filed 30.3.2023 (FY2020 comparatives, restated):
                       https://satcom-gilat.co.il/wp-content/uploads/2023/03/דוח-תקופתי-ושנתי-לשנת-2022-1-merged.pdf
                       (scratchpad/work/gilat_telecom/cio_dl/gilat_fy2022_mar.pdf; the 18.5.2023 re-issue prints
                       the same P&L)
  gilat_fy2021         the 2021 annual report, company site, filed 30.3.2022 (balance sheets 31.12.2020/2021):
                       https://satcom-gilat.co.il/wp-content/uploads/2022/03/דוח-תקופתי-ושנתי-לשנת-2021-merged.pdf
                       (scratchpad/work/gilat_telecom/cio_dl/gilat_fy2021.pdf)
  market.md, scuttle_calc_output.txt   market data compiled 3.11.2026 (Bizportal, TheMarker, TASE series)

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
    excess_cash, graham_yardstick, growth_cap, hurdle, implied_growth, maintenance_capex,
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
FX_30JUN26 = 2.978               # ILS per USD at 30.6.2026 (gilat_q2_2026_full p.43): the rate of the 30.6.2026 balance sheet
Y10_IL = 0.0416                  # Israel 10-year government yield 3.11.2026 (TradingEconomics; market.md §5)
Y10_US = 0.0491                  # US 10-year 2.11.2026 (US Treasury par curve; market.md §5), cross-check only
TAX = 0.23                       # Israeli statutory corporate tax rate (gilat_fy2025 p.164)

# Liquidity, 60 sessions 4.8.2026-3.11.2026 (Bizportal on-exchange proceeds, cross-checked against the TASE series;
# scuttle_calc_output.txt §1). The earlier market.md series ended 29.10.2026 (median 1,303,000; p25 960,250).
TURNOVER_MEDIAN_60 = 1_325_803   # ILS, median daily turnover over 60 sessions
TURNOVER_P25_60 = 1_001_604      # ILS, 25th percentile (linear interpolation) of daily turnover over 60 sessions

# =====================================================================================================
# 1. WINDOW FY2020-FY2025 (USD thousands, audited). W = FY2020 to the latest fiscal year (framework d2).
# =====================================================================================================
YEARS = (2020, 2021, 2022, 2023, 2024, 2025)
YEARS_5 = (2021, 2022, 2023, 2024, 2025)          # d1's "5 years" for the NetPPE/revenue ratio; the team's earlier window
REV_USD = {
    2020: 54_564,                # gilat_fy2022 p.119 (= gilat_fy2021 p.116); page images checked at the CIO gate
    2021: 51_816,                # gilat_fy2023 p.118 (= gilat_fy2022 p.119)
    2022: 42_997,                # gilat_fy2023 p.118
    2023: 55_154,                # gilat_fy2023 p.118
    2024: 69_592,                # gilat_fy2024 p.120
    2025: 75_793,                # gilat_fy2025 p.127
}
REV_2019_USD = 56_441            # gilat_fy2021 p.116: used only for the sign of the FY2020 revenue change (growth capex)
EBIT_USD = {
    2020: 3_649,                 # gilat_fy2022 p.119: operating profit, including "other income" 286
    2021: -2_731,                # gilat_fy2023 p.118 (restated; includes 3,191 of doubtful debts, gilat_fy2023 p.158: NOT added back)
    2022: -1_499,                # gilat_fy2023 p.118
    2023: 2_178,                 # gilat_fy2023 p.118
    2024: 4_949,                 # gilat_fy2024 p.120
    2025: 9_689,                 # gilat_fy2025 p.127
}
OTHER_INCOME_2020 = 133 + 153    # credit and dividend from the Wiocc stake held at fair value through OCI (gilat_fy2022 p.123): non-operating, removed
NI_USD = {2020: -1_734, 2021: -5_423, 2022: -4_064, 2023: 715, 2024: 1_786, 2025: 6_350}   # gilat_fy2022 p.119 (2020 restated); gilat_fy2023 p.118; gilat_fy2024 p.120; gilat_fy2025 p.127
OCF_USD = {2020: 18_264, 2021: 14_028, 2022: 10_099, 2023: 8_718, 2024: 10_587, 2025: 20_533}   # gilat_fy2022 p.123; gilat_fy2023 p.122; gilat_fy2024 p.124; gilat_fy2025 p.131
SBC_USD = {2020: -67, 2021: 63, 2022: 123, 2023: 53, 2024: 51, 2025: 88}                    # same pages (2020: a credit)
CAPEX_PPE_USD = {2020: 3_050, 2021: 1_810, 2022: 1_402, 2023: 3_082, 2024: 2_529, 2025: 1_362}  # gilat_fy2022 p.124; gilat_fy2023 p.123; gilat_fy2024 p.125; gilat_fy2025 p.132
CAPEX_INT_USD = {2020: 390, 2021: 271, 2022: 62, 2023: 196, 2024: 118, 2025: 82}             # same pages
DEP_PPE_USD = {2020: 2_690, 2021: 3_353, 2022: 2_640, 2023: 1_776, 2024: 1_905, 2025: 2_130}   # gilat_fy2021 p.145 (2020, 2021; 2021 = gilat_fy2022 p.148); gilat_fy2023 p.140; gilat_fy2024 p.143; gilat_fy2025 p.149
AMORT_LIC_USD = {2020: 115, 2021: 141, 2022: 151, 2023: 135, 2024: 136, 2025: 177}           # licences/software, gilat_fy2021 p.146; gilat_fy2023 p.141; gilat_fy2025 p.150
AMORT_ACQ_USD = 809              # customer-relations amortisation a year (gilat_fy2025 p.150) = Amort_acq of the TTM (d1)
# Acquired-intangible amortisation inside each year's EBIT (note 8): customer relations, plus in FY2020 the contract backlog
# (cost 5,698, fully amortised in 2020); both came with goodwill in one purchase price allocation. d1/d3 add it back.
AMORT_ACQ_W_USD = {2020: 809 + 949,  # gilat_fy2021 p.146 (customer relations 809; contract backlog 949, net nil at 31.12.2020)
                   2021: 809,        # gilat_fy2021 p.146
                   2022: 809, 2023: 814,   # gilat_fy2023 p.141
                   2024: 809, 2025: 809}   # gilat_fy2025 p.150
LEASE_PRIN_USD = {2020: 13_621, 2021: 13_387, 2022: 7_986, 2023: 4_297, 2024: 6_717, 2025: 9_521}  # financing CF, gilat_fy2022 p.124; gilat_fy2023 p.123; gilat_fy2024 p.125; gilat_fy2025 p.132
LEASE_INT_USD = {2020: 1_974, 2021: 1_396, 2022: 724, 2023: 408, 2024: 1_698, 2025: 1_788}      # financing CF (Gilat classifies interest in financing), same pages
OTHER_INT_USD = {2020: 898, 2021: 1_075, 2022: 910, 2023: 733, 2024: 470, 2025: 858}          # interest paid excl. leases (bonds, loans), same pages
NETPPE_USD = {2020: 6_074, 2021: 4_529, 2022: 3_292, 2023: 4_599, 2024: 5_223, 2025: 4_455}   # gilat_fy2021 p.114 (2020, 2021); gilat_fy2023 p.116; gilat_fy2024 p.118; gilat_fy2025 p.125
ROU_USD = {2020: 25_588, 2021: 14_937, 2022: 9_168, 2023: 7_541, 2024: 23_856, 2025: 16_769}  # same pages

# Balance-sheet lines for the return-on-tangible-capital test (screen_spec 2.3: NWC_op = max(0, (CA - C) - (CL - short-term debt)))
CA_USD = {2020: 26_784 - 9_487,  # gilat_fy2021 p.114: total current assets less the Wiocc stake held for sale (non-operating)
          2021: 30_891,          # gilat_fy2021 p.114 (before the immaterial Uganda-tax restatement, which only adds liabilities)
          2022: 22_201, 2023: 25_149, 2024: 26_793, 2025: 52_669}   # gilat_fy2023 p.116; gilat_fy2024 p.118; gilat_fy2025 p.125
C_USD = {2020: 4_880, 2021: 21_245, 2022: 10_897 + 3_983, 2023: 12_215, 2024: 11_017, 2025: 25_036 + 4_717}  # cash + short-term deposits, same pages
CL_USD = {2020: 35_672, 2021: 25_570, 2022: 22_734, 2023: 33_616, 2024: 36_485, 2025: 54_543}   # gilat_fy2021 p.115; gilat_fy2023 p.117; gilat_fy2024 p.119 (2023 restated); gilat_fy2025 p.126
STDEBT_USD = {                                                              # current financial debt incl. current leases and conversion-option/warrant liabilities
    2020: 2_703 + 448 + 12_735 + 142 + 439 + 173,   # Series B, Series F, leases, state loan, unlisted warrants, Series B warrants (gilat_fy2021 p.115)
    2021: 1_892 + 6_814 + 427 + 965 + 23 + 451,     # Series B, leases, state loan, ST credit, Series B and C warrants (gilat_fy2021 p.115)
    2022: 1_320 + 3_598 + 350 + 853 + 15 + 30,     # Series C, leases, state loan, ST credit, warrants, option (gilat_fy2023 p.117)
    2023: 9_972 + 1_832 + 388 + 76 + 196,           # gilat_fy2024 p.119 (restated)
    2024: 6_081 + 9_016 + 324 + 625 + 129 + 483,    # gilat_fy2024 p.119
    2025: 5_243 + 11_382 + 9_304 + 315 + 5_182,     # gilat_fy2025 p.126
}

# 2025 quarters (USD thousands) for the satellite-supplier credit estimate (gilat_fy2025 p.92; page image checked)
Q25_REV = (15_994, 18_585, 20_075, 21_139)
Q25_GP = (4_521, 5_494, 5_580, 7_455)
H1_2025_REV_USD = Q25_REV[0] + Q25_REV[1]   # derived (gilat_fy2025 p.92)

# FY2025 segments and Vodacom (USD k): global segment revenue 19,655 and result 4,106 (gilat_fy2025 p.181; the three
# segments sum to the consolidated 75,793 and 21,250); Vodacom DRC revenue 12,392 (gilat_fy2025 p.55)
GLOBAL_SEG_REV_2025, GLOBAL_SEG_RES_2025, VODACOM_REV_2025 = 19_655, 4_106, 12_392

# =====================================================================================================
# 2. TTM TO 30.6.2026 (ILS thousands) = FY2025 (as translated by the company) - H1 2025 + H1 2026
#    P&L gilat_q2_2026_full p.32; cash flow p.38-39; segment and revenue notes p.46-49 (page images checked)
# =====================================================================================================
REV_ILS = {"FY25": 260_335, "H1_25": 124_234, "H1_26": 139_991}        # p.32
EBIT_ILS = {"FY25": 32_980, "H1_25": 12_841, "H1_26": 19_395}          # p.32 (directors' report p.11 prints FY2025 32,981)
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
LEASE_INT_ILS = {"FY25": 9_584, "H1_25": 3_526, "H1_26": 1_892}        # p.39: the FY2025 ILS split puts 24.6% of lease cash in interest
BOND_INT_ILS = {"FY25": 2_436, "H1_25": 538, "H1_26": 1_246}           # p.39
SAT_LEASE_DEP_TTM = 29_676       # satellite-lease (ROU) depreciation TTM, directors' report tables (gilat_h1_2026 p.6-7, p.13; derived in financials.json)
OTHER_ROU_DEP_USD = 9_983 - 9_082  # non-satellite ROU depreciation FY2025 (gilat_fy2025 p.159), used only to split TTM D&A (UNVERIFIED for TTM)
EQUIP_REV_SAT = {"H1_25": 10_152, "H1_26": 14_331}                      # satellite-segment equipment revenue (gilat_q2_2026_full p.49)
EQUIP_GM_2025 = 0.313            # company equipment gross margin 2025 (business_calcs §3, from gilat_fy2025 p.173): derived
ISP_SEG_H1_26 = (2_613, 3_449)   # internet-and-cloud segment result and its D&A (= IRU amortisation), H1 2026 (gilat_q2_2026_full p.46, the FS note)

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
DTA = 2_403                      # deferred tax asset (p.30)
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
# 30.6.2025 comparatives for average TTM capital (gilat_q2_2026_full p.30-31; page image checked)
CA_30JUN25, CASH_30JUN25, CL_30JUN25 = 149_039, 66_702, 183_167
STD_30JUN25 = 19_480 + 35_305 + 31_228 + 482 + 145 + 1_234 + 16_071   # Series C, Series D, current leases, state loan, warrants, Series C and D conversion options
PPE_30JUN25, ROU_30JUN25, DEFERRED_LT_30JUN25 = 16_447, 71_085, 5_776
# Identity checks (checklist C7)
EPS_BASIC_H1_26 = 0.1459         # ILS, basic EPS H1 2026 (gilat_q2_2026_full p.32)
WEIGHTED_SHARES_H1_26 = 108_088  # thousands, basic weighted shares H1 2026 (p.32)
INVESTING_CF_H1_26 = 7_219       # (p.39)
FINANCING_CF_H1_26 = -26_091     # (p.39)
FX_ON_CASH_H1_26 = -1_284        # effect of exchange-rate changes on cash (p.39)
CASH_OPENING_2026 = 79_865       # cash 1.1.2026 (p.39; = 31.12.2025, p.30)

# Linkage table at 30.6.2026 (gilat_h1_2026 p.19; page image checked). USD column, by row: the printed USD asset total
# (25,110) and the unlinked-ILS asset total (138,321) do not foot to their rows, and the cash row (84,007 + 8,984)
# exceeds the balance sheet's 92,955 by 36: the rows are used (C7 flag).
USD_ASSETS_30JUN = 8_984 + 13_023 + 2_960                 # cash, customers, other receivables (rows; printed total 25,110)
USD_LIAB_30JUN = 24_275 + 60_188 + 3_347 + 116 + 2_504    # current leases, suppliers, payables, current tax, long-term leases (= printed 90,430)
ILS_ASSET_ROWS_30JUN = 84_007 + 3_500 + 50_388 + 66 + 274   # unlinked-ILS asset rows (printed total 138,321)
FWD_NOTIONAL_USD_K = 2_000 * 2 + 1_500 * 12               # forwards left at 3.11.2026: USD 2M a month to 12.2026, 1.5M a month in 2027 (gilat_h1_2026 p.19); strike undisclosed
USD_COST_PROXY = 24_000          # USD k a year: USD 2M a month hedged to 12.2026 (gilat_h1_2026 p.19) as the proxy for the net USD cost flow: UNVERIFIED
# Linkage table at 31.12.2025 (gilat_fy2025 p.106; page image checked): USD liabilities 29,314; USD assets 6,219, of which cash 866
USD_NONCASH_NET_LIAB_1JAN26 = 29_314 - (6_219 - 866)     # USD k: the base of the H1 2026 FX gain on USD liabilities (ILS functional from 1.1.2026)

# Events after 30.6.2026 that move cash or claims (pro forma to 3.11.2026; Q3 operating cash flow unknown and NOT added)
OCT_BUYBACK = 4_620              # 2,274,810 shares at ~203.1 agorot, 7-21.10.2026 (Globes insider feed, TASE counts; market.md calc §3): UNVERIFIED vs Maya
SERIES_C_PUBLIC_PAR_19AUG = 984_967       # ILS par held by the public at 19.8.2026 (gilat_h1_2026 p.22)
SERIES_C_CONVERTED_1JUL_19AUG = 1_240_026  # par converted 1.7-19.8.2026 (gilat_h1_2026 p.37; gilat_q2_2026_full p.49 note 8)
SERIES_C_CONVERTED_AFTER_19AUG = 192_435  # shares, implied by TASE counts (market.md calc §4): derived, UNVERIFIED
SERIES_C_CONV_PRICE = 1.35       # ILS par per share (gilat_h1_2026 p.22)
SERIES_C_COUPON_HALF = 0.045 / 2  # final semi-annual coupon (gilat_h1_2026 p.22)
SERIES_D_PAR = 26_337_927        # ILS par outstanding 3.11.2026: next coupon ILS 724,293 = 2.75% of par (Bizportal bond data; market.md §1.4): derived
SERIES_D_PAR_19AUG = 29_134_661  # ILS par at 19.8.2026 (gilat_h1_2026 p.24; page image checked)
SERIES_D_CONVERTED_1JUL_19AUG = 705_275   # par converted 1.7-19.8.2026 (gilat_h1_2026 p.37; market.md §1.2)
SERIES_D_OCT_CONVERSIONS = 509_030  # shares issued in October 2026 on conversion (TASE counts; market.md calc §3): derived
SERIES_D_COUPON_HALF = 0.055 / 2  # 1.10.2026 coupon (gilat_h1_2026 p.24)
SERIES_D_COUPON = 0.055          # fixed annual coupon, unlinked (gilat_h1_2026 p.24)
SERIES_D_CONV_PRICE = 1.00       # ILS par per share until 1.4.2028, then 1.40 (gilat_h1_2026 p.24); principal 25% a year 1.4.2028-1.4.2031

# Options (net exercise; gilat_fy2025 p.166, p.172)
OPTIONS = [
    (2_000_000, 1.1015),         # CEO package A, December 2025 (gilat_fy2025 p.166, p.206)
    (2_000_000, 0.927),          # CEO package B (p.166, p.206)
    (750_000, 1.1015),           # 32 employees/officers package A, November 2025 (p.166)
    (3_915_000, 0.927),          # package B (p.166)
    (12_093_500 - 8_665_000, 0.23 * FX_31DEC25),  # older options at 31.12.2025 (p.172); weighted strike of the exercisable ones USD 0.23 (p.172) at 3.19: derived; upper bound on the count
]

# =====================================================================================================
# 4. BEZEQ FIBRE IRU (off balance sheet except amounts paid; gilat_fy2025 p.40-42, p.152-153, p.183, page images checked)
# =====================================================================================================
IRU1_LINES = 18_000              # original agreement, December 2024 (gilat_fy2025 p.152)
IRU1_PRICE = 4_890               # ILS per line for 15 years (gilat_fy2025 p.152); total ILS 88.02M + VAT (p.153)
IRU2_LINES = 36_000              # addendum pulse 1, December 2025-2028, 12 quarterly tranches of 3,000 (gilat_fy2025 p.183)
IRU2_TOTAL = 160_000             # ILS thousands "assuming full exercise" (gilat_fy2025 p.183, p.42)
IRU_OM_RATE = 0.04               # annual O&M fee, % of consideration, plus 50% of CPI differences (gilat_fy2025 p.153, p.183)
IRU_VENDOR_RATE = 0.05           # interest if a pulse is spread over 10 annual payments: 5% for IRU-1 pulse 1 (p.153); assumed 5% for the rest (Bezeq bond yield at each pulse: UNVERIFIED)
IRU_INSTALMENTS = 10             # annual payments if spread (gilat_fy2025 p.153, p.183)
IRU_TERM = 15                    # years of use per line (p.152)
BSA_MONTHLY = 58                 # ILS/line/month, regulated fibre BSA up to 1 Gbps, fixed 2026-2031, unlimited for small ISPs (gilat_fy2025 p.40)
ACTIVE_LINES = 27_600            # "more than ~27,600" lines active under the Bezeq agreement at the report date 19.8.2026 (gilat_h1_2026 p.5)
IRU_PAID_TO_30JUN = IRU_PAID_ILS["FY25"] + IRU_PAID_ILS["H1_26"]   # derived (gilat_q2_2026_full p.38)
# Tranches as (start, consideration ILS k, CPI-linkage share of the consideration). IRU-1: pulse 1 8,000 lines from 1.1.2025
# (39.12M, no linkage stated); pulses 2 and 3, 5,000 lines each in 4 quarterly tranches from 1.4.2025 and 1.4.2026 (24.45M each,
# "plus 50% of CPI differences") (gilat_fy2025 p.152-153). IRU-2 pulse 1: 12 quarterly tranches of 3,000 lines from 12.2025,
# ILS 160M, "CPI-linked" (p.42, p.183): 50% assumed, as stated for IRU-1 (UNVERIFIED). Whether pulse-1 tranches can be declined
# is not stated ("assuming full exercise"): UNVERIFIED. Release applies only to a SUBSEQUENT pulse (p.183).
IRU_TRANCHES = ([(2025.00, 39_120.0, 0.0)]
                + [(2025.25 + 0.25 * i, 24_450 / 4, 0.5) for i in range(4)]
                + [(2026.25 + 0.25 * i, 24_450 / 4, 0.5) for i in range(4)]
                + [(2025.92 + 0.25 * i, IRU2_TOTAL / 12, 0.5) for i in range(12)])
# The same tranches as (delivery start, lines): IRU-1 8,000 + 2 x 4 x 1,250; IRU-2 12 x 3,000 (gilat_fy2025 p.152-153, p.183)
IRU_LINE_TRANCHES = ([(2025.00, 8_000)]
                     + [(2025.25 + 0.25 * i, 1_250) for i in range(4)]
                     + [(2026.25 + 0.25 * i, 1_250) for i in range(4)]
                     + [(2025.92 + 0.25 * i, 3_000) for i in range(12)])
VAL_T = 2026.84                  # 3.11.2026 as a year fraction, the date of every bridge (as in iru_schedule)
# Probability that the base carries for "half of the committed but unfilled lines are paid for and never used" (B-O6): assumed,
# a model judgement (uncalibrated). Private net additions ran ~3,500 a quarter in H2 2025-H1 2026 (gilat_h1_2026 p.8) against
# tranches of 3,000, so filling is on track today; fast recruitment at a lower ARPU (Q2 2026 80.19 against 88.71 a year earlier,
# -9.6%, which the company attributes to the surge in new customers: gilat_h1_2026 p.8) and the regulated BSA available to every
# rival are the risks.
P_IRU_HALF_DEAD = 0.25
# IRU line-years inside the TTM for the accounting-gap estimate (B-O1/B-O3): IRU-1 assumed in use all TTM (upper bound; the
# contractual delivery dates give 12,375), IRU-2 tranches of 12.2025, 3.2026 and 6.2026 (7 + 4 + 1 months x 3,000): UNVERIFIED
IRU1_TTM_LINE_YEARS = 18_000
IRU1_TTM_LINE_YEARS_CONTRACT = 8_000 + 1_250 * (1 + 1 + 0.75 + 0.5) + 1_250 * 0.25
IRU2_TTM_LINE_YEARS = 3_000 * (7 + 4 + 1) / 12

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


def pv_iru_line(price: float, r: float, vendor: float = IRU_VENDOR_RATE) -> float:
    """PV at r of one IRU line on the contract terms: 10 annual principal payments from delivery
    (t = 0..9) with vendor interest on the unpaid balance, plus the 4% O&M fee for 15 years (mid-year)."""
    pv = 0.0
    for t in range(IRU_INSTALMENTS):
        interest = vendor * price * (1 - t / IRU_INSTALMENTS) if t > 0 else 0.0
        pv += (price / IRU_INSTALMENTS + interest) / (1 + r) ** t
    pv += sum(IRU_OM_RATE * price / (1 + r) ** (t - 0.5) for t in range(1, IRU_TERM + 1))
    return pv


def pv_bsa_line(r: float) -> float:
    """PV at r of renting the same line at the regulated BSA price for 15 years (mid-year)."""
    return sum(BSA_MONTHLY * 12 / (1 + r) ** (t - 0.5) for t in range(1, IRU_TERM + 1))


def iru_schedule(cpi: float = 0.0, om_from: float = 2026.5) -> dict:
    """Calendar-year cash on the committed IRU tranches: 10 annual instalments from each tranche start with vendor
    interest on the unpaid balance (pv_iru_line terms), plus the 4% O&M on tranches that start after om_from (O&M on
    earlier tranches is already inside the TTM cost base). CPI escalation applies from 3.11.2026 at the tranche's linkage
    share (O&M: 50%). Terms UNVERIFIED: the filings state neither the unpaid balance nor the instalment schedule."""
    out: dict = {}
    for start, c, link in IRU_TRANCHES:
        for k in range(IRU_INSTALMENTS):
            t = start + k
            amt = c / IRU_INSTALMENTS + (IRU_VENDOR_RATE * c * (1 - k / IRU_INSTALMENTS) if k > 0 else 0.0)
            amt *= (1 + link * cpi) ** max(0.0, t - 2026.84)
            out[int(t)] = out.get(int(t), 0.0) + amt
        if start > om_from:
            for q in range(IRU_TERM * 4):
                t = start + q / 4
                out[int(t)] = out.get(int(t), 0.0) + IRU_OM_RATE * c / 4 * (1 + 0.5 * cpi) ** max(0.0, t - 2026.84)
    return out


def fmt(v: float) -> str:
    return f"{v:7.3f} ILS ({v * 100:6.1f} ag; USD {v / FX:6.3f})"


out: list[str] = []
P = out.append

# =====================================================================================================
# 0. Market, hurdle
# =====================================================================================================
R = hurdle(max(Y10_IL, 0.0))                       # ILS cash flows: r = max(10%, y10 + 3 points)
MCAP = PRICE * SHARES_LISTED / 1000                # ILS thousands
P("GILAT TELECOM GLOBAL LTD (TASE 1080597) - CHARTER REV 4 VALUATION, 3.11.2026 (revised at the CIO gate)")
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
# Q4 2025 gross profit above the Q1-Q3 2025 gross margin. An UPPER BOUND: p.96 names three causes of the 2025 margin rise
# (high-margin defence deals, the Bezeq IRU, the supplier credits), and all of the Q4 excess is removed (A-O10).
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
P(f"  one-off 1, 2025 satellite-supplier credit (UPPER-BOUND estimate): Q4 2025 GP above the Q1-Q3 margin {gm_q1_q3:.2%} = USD {SUPPLIER_CREDIT_USD:,.0f}"
  f" = ILS {SUPPLIER_CREDIT_TTM:,.0f} at the implied H2 2025 rate {FX_H2_2025:.4f}; gilat_fy2025 p.96 also names high-margin deals and the IRU")
P(f"  one-off 2, H1 2026 war equipment (estimate): equipment revenue +{ONEOFF_EQUIP_REV:,.0f} x {EQUIP_GM_2025:.1%} = {ONEOFF_EQUIP_PROFIT:,.0f}")
P("  not removed (UNVERIFIED): any 2026 Intelsat credit (the agreement grants 'one-off credits', plural, gilat_fy2025 p.160)")
cf_foot = OCF_ILS["H1_26"] + INVESTING_CF_H1_26 + FINANCING_CF_H1_26 + FX_ON_CASH_H1_26 - (CASH - CASH_OPENING_2026)
P(f"  C7 identities (30.6.2026, consolidated): assets - liabilities - equity = {TOTAL_ASSETS - TOTAL_LIAB - EQUITY:,.0f};"
  f" H1 2026 cash flow foots to the cash change: difference {cf_foot:,.0f}; NI / basic EPS = {NI_ILS['H1_26'] / EPS_BASIC_H1_26:,.0f}k"
  f" vs weighted basic shares {WEIGHTED_SHARES_H1_26:,}k")
P(f"  C7 flags (single-source tables that do not foot; rows / FS note used): linkage table USD assets rows {USD_ASSETS_30JUN:,} vs printed 25,110;"
  f" unlinked-ILS asset rows {ILS_ASSET_ROWS_30JUN:,} vs printed 138,321; cash row {84_007 + 8_984:,} vs balance sheet {CASH:,} (gilat_h1_2026 p.19);"
  f" H1 2025 segment results {23_440 + 1_423:,} in the directors' report (gilat_h1_2026 p.12) vs {27_886 + 2_891:,} in the FS note"
  " (gilat_q2_2026_full p.46, which reconciles to pre-tax 4,313); FY2020 operating lines agree across gilat_fy2021 p.116 and gilat_fy2022 p.119")

# =====================================================================================================
# 2. Lane and tier evidence
# =====================================================================================================
EBIT_ADJ_USD = dict(EBIT_USD)
EBIT_ADJ_USD[2020] = EBIT_USD[2020] - OTHER_INCOME_2020         # sign-aware: the Wiocc dividend and credit removed
EBIT_ADJ_USD[2025] = EBIT_USD[2025] - SUPPLIER_CREDIT_USD      # sign-aware: a one-off gain removed
EBIT_ADJ_TTM = EBIT_TTM - SUPPLIER_CREDIT_TTM - ONEOFF_EQUIP_PROFIT
REV_ADJ_TTM = REV_TTM - ONEOFF_EQUIP_REV

P("")
P("== 2. Lane and tier evidence (framework d11; checklist A3, C2; screen_spec 2.3)")
P("  2a. Pre-tax return on tangible capital = EBIT_adj / (NWC_op + net PP&E + ROU) (IFRS basis; NWC_op floored at 0)")
rotc = {}
for y in YEARS:
    nwc_op = max(0.0, (CA_USD[y] - C_USD[y]) - (CL_USD[y] - STDEBT_USD[y]))
    cap = nwc_op + NETPPE_USD[y] + ROU_USD[y]
    rotc[y] = EBIT_ADJ_USD[y] / cap
    P(f"      FY{y}  EBIT_adj {EBIT_ADJ_USD[y]:>8,.0f} USD k  NWC_op {nwc_op:>7,.0f}  capital {cap:>8,.0f}  ROTC {rotc[y]:>7.1%}")
nwc_ttm = max(0.0, (CURRENT_ASSETS - CASH) - (CURRENT_LIAB - (SERIES_C_LIAB + LEASES_ST)))
cap_ttm = nwc_ttm + PPE + ROU
nwc_25 = max(0.0, (CA_30JUN25 - CASH_30JUN25) - (CL_30JUN25 - STD_30JUN25))
cap_25 = nwc_25 + PPE_30JUN25 + ROU_30JUN25
cap_avg = (cap_25 + cap_ttm) / 2
iru_lt_avg = (DEFERRED_LT_30JUN25 + DEFERRED_LT) / 2
ROTC_TTM_END = EBIT_ADJ_TTM / cap_ttm
ROTC_TTM_AVG = EBIT_ADJ_TTM / cap_avg
ROTC_TTM_AVG_IRU = EBIT_ADJ_TTM / (cap_avg + iru_lt_avg)
P(f"      TTM     EBIT_adj {EBIT_ADJ_TTM:>8,.0f} ILS k  capital 30.6.2025 {cap_25:,.0f} (ROU {ROU_30JUN25:,}), 30.6.2026 {cap_ttm:,.0f} (ROU {ROU:,})")
P(f"              ROTC on end capital {ROTC_TTM_END:.1%}; on average capital {ROTC_TTM_AVG:.1%}; average + long-term IRU prepayment {ROTC_TTM_AVG_IRU:.1%} (A-O9)")
rotc_w = [rotc[y] for y in YEARS]
rotc_all = rotc_w + [ROTC_TTM_AVG_IRU]
P(f"      W = FY2020-FY2025: median {statistics.median(rotc_w):.1%}, minimum {min(rotc_w):.1%}; with the TTM (average capital + IRU)"
  f" median {statistics.median(rotc_all):.1%} -> Tier A needs >= 20% and never < 10%: fails; B's 12-20% band only on the median")

# =====================================================================================================
# 3. Normalised earnings (d2)
# =====================================================================================================
REV_W_ILS = [REV_USD[y] * FX for y in YEARS]
EBIT_W_ILS = [EBIT_ADJ_USD[y] * FX for y in YEARS]
norm_w = normalised_ebit(REV_ADJ_TTM, EBIT_W_ILS, REV_W_ILS)                                       # BASE: W = FY2020-FY2025, fiscal years
norm_5 = normalised_ebit(REV_ADJ_TTM, EBIT_W_ILS[1:], REV_W_ILS[1:])                               # sensitivity: FY2021-FY2025 (no FY2020)
norm_w_ttm = normalised_ebit(REV_ADJ_TTM, EBIT_W_ILS + [EBIT_ADJ_TTM], REV_W_ILS + [REV_ADJ_TTM])   # sensitivity: W + TTM (double-counts H2 2025)
norm_team = normalised_ebit(REV_ADJ_TTM, EBIT_W_ILS[1:] + [EBIT_ADJ_TTM], REV_W_ILS[1:] + [REV_ADJ_TTM])  # the team's earlier base (FY2021-25 + TTM)
EBIT_NORM = norm_w.ebit_norm
H2_2025_EBIT = EBIT_ILS["FY25"] - EBIT_ILS["H1_25"]
prewar_mean = statistics.mean(EBIT_ADJ_USD[y] for y in (2020, 2021, 2022))
war_mean = statistics.mean(EBIT_ADJ_USD[y] for y in (2023, 2024, 2025))
P("")
P("== 3. Normalised earnings (d2), owner earnings (d1), tax, cash, claims")
P("  EBIT_adj / revenue (one-off gains removed; USD years at 3.157):")
P("      " + "  ".join(f"FY{y} {m:6.1%}" for y, m in zip(YEARS, norm_w.detail["margins"]))
  + f"  (TTM {EBIT_ADJ_TTM / REV_ADJ_TTM:6.1%}, not a W observation)")
P(f"  W = FY2020-FY2025 fiscal years (framework d2: 'FY2020 to the latest year, at most six years'): m_norm {norm_w.m_norm:.2%};"
  f" cyclical {norm_w.cyclical} (operating losses in FY2021-FY2022)")
P(f"  BASE EBIT_norm = min(mean {norm_w.detail['mean_ebit_adj']:,.0f}, median {norm_w.detail['median_ebit_adj']:,.0f},"
  f" mean revenue x m_norm {norm_w.detail['mean_rev_x_m_norm']:,.0f}) = {EBIT_NORM:,.0f} = USD {EBIT_NORM / FX:,.0f}k"
  f"  ({EBIT_NORM / EBIT_ADJ_TTM:.0%} of TTM EBIT_adj {EBIT_ADJ_TTM:,.0f})")
P(f"      reading: the six-year mean, half pre-war and half war: FY2020-22 mean EBIT_adj USD {prewar_mean:,.0f}k, FY2023-25 USD {war_mean:,.0f}k")
P(f"  sensitivities (not the base): FY2021-25 only {norm_5.ebit_norm:,.0f}; W + TTM {norm_w_ttm.ebit_norm:,.0f};"
  f" the team's earlier base FY2021-25 + TTM {norm_team.ebit_norm:,.0f} (it counted H2 2025 EBIT {H2_2025_EBIT:,.0f} twice)")
P(f"  screen flags: ttm_above_norm {EBIT_ADJ_TTM > 1.5 * EBIT_NORM} (TTM EBIT_adj = {EBIT_ADJ_TTM / EBIT_NORM:.1f}x EBIT_norm): a peak, not depressed earnings;"
  " no endogenous add-back used (FY2021 doubtful debts 3,191 USD k left in)")

# Amort_acq (d1, d3). EBIT_adj keeps every year's acquired amortisation as a cost (screen_spec 2.3); d3 adds back the amount that
# sits inside EBIT_norm. EBIT_norm is the W mean here, so the matching add-back is the W mean of acquired amortisation (AR-1).
AMORT_ACQ = AMORT_ACQ_USD * FX                                  # derived, ILS a year: the TTM's (d1)


def amort_acq_mean(years: tuple, with_ttm: bool = False) -> float:
    """Mean acquired-intangible amortisation (ILS k) over a window, the add-back that matches a window-mean EBIT_norm."""
    vals = [AMORT_ACQ_W_USD[y] * FX for y in years] + ([AMORT_ACQ] if with_ttm else [])
    return statistics.mean(vals)


AMORT_ACQ_NORM = amort_acq_mean(YEARS)                          # BASE: W = FY2020-FY2025
P(f"  Amort_acq added back to EBIT_norm (d3) = the W mean of acquired amortisation inside it: USD {AMORT_ACQ_NORM / FX:,.1f}k a year"
  f" (customer relations 809, 814 in FY2023; FY2020 also the acquired contract backlog 949, fully amortised that year: gilat_fy2021 p.146)"
  f" = {AMORT_ACQ_NORM:,.0f}; the TTM's is {AMORT_ACQ:,.0f}. The 949 is a mandated add-back (d1, d3), not an endogenous one")

# Maintenance capex (d1): floored at depreciation. Dep (charter notation) = PP&E + ROU depreciation + licences + IRU amortisation.
DEP_TTM = DA_TTM - AMORT_ACQ + IRU_AMORT_TTM
avg_ppe_rev = statistics.mean(NETPPE_USD[y] / REV_USD[y] for y in YEARS_5)
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
for y in YEARS:
    d_rev = REV_USD[y] - (REV_USD[y - 1] if y - 1 in REV_USD else REV_2019_USD)
    mc_own = maintenance_capex(CAPEX_PPE_USD[y] + CAPEX_INT_USD[y], DEP_PPE_USD[y] + AMORT_LIC_USD[y], avg_ppe_rev, d_rev)
    cash_oe[y] = owner_earnings_cash(OCF_USD[y] - LEASE_INT_USD[y] - OTHER_INT_USD[y], SBC_USD[y], mc_own, LEASE_PRIN_USD[y])
dep_own_ttm = DA_TTM - SAT_LEASE_DEP_TTM - (OTHER_ROU_DEP_USD + AMORT_ACQ_USD) * FX     # PP&E + licences, TTM estimate (UNVERIFIED split)
mc_own_ttm = maintenance_capex(CAPEX_TTM, dep_own_ttm, avg_ppe_rev, REV_TTM - REV_ILS["FY25"])
CASH_OE_TTM = owner_earnings_cash(OCF_TTM - LEASE_INT_TTM - BOND_INT_TTM, SBC_TTM, mc_own_ttm, LEASE_PRIN_TTM)
P("      " + "  ".join(f"FY{y} {cash_oe[y]:,.0f}" for y in YEARS) + f" (USD k)   TTM {CASH_OE_TTM:,.0f} ILS k ({CASH_OE_TTM / NI_TTM:.0%} of TTM NI)")
pos_ni = sum(v for v in NI_USD.values() if v > 0)
c4_recent = sum(cash_oe[y] for y in (2023, 2024, 2025)) / sum(NI_USD[y] for y in (2023, 2024, 2025))
P(f"      C4 cash clause: W sum {sum(cash_oe.values()):,.0f} / sum of positive NI {pos_ni:,.0f} = {sum(cash_oe.values()) / pos_ni:.0%};"
  f" FY2023-FY2025 {c4_recent:.0%} (test >= 80%: fails)")
gross_rec = (17_995, 22_977)     # gross customers 31.12.2024 / 31.12.2025 (gilat_fy2025 p.147; page image checked); customer days 62 -> 69 (p.147)
P(f"      C4 build-up clause: gross customers {gross_rec[1] / gross_rec[0] - 1:+.1%} in FY2025 vs revenue {REV_USD[2025] / REV_USD[2024] - 1:+.1%};"
  f" customer days 62 -> 69; allowance 6,767 = {6_767 / gross_rec[1]:.0%} of gross (gilat_fy2025 p.147); IRU deferred asset 0 -> USD 2,823k (31.12.2025,"
  f" p.152) -> ILS {DEFERRED_ST + DEFERRED_LT:,} (30.6.2026), TTM cash {IRU_PAID_TTM:,.0f} vs charge {IRU_AMORT_TTM:,.0f}: fails")
ocf_lease_adj = {y: OCF_USD[y] - LEASE_PRIN_USD[y] - LEASE_INT_USD[y] for y in YEARS}       # IFRS 16 adjusted (framework h3)
P("  H3 burn test (OCF, and OCF less lease payments under IFRS 16, USD k): "
  + "  ".join(f"FY{y} {OCF_USD[y]:,}/{ocf_lease_adj[y]:,}" for y in YEARS)
  + f"; FY2023-25 average {statistics.mean(ocf_lease_adj[y] for y in (2023, 2024, 2025)):,.0f} lease-adjusted, cash proxy"
  f" {statistics.mean(cash_oe[y] for y in (2023, 2024, 2025)):,.0f}: the floor is not being burned")
P(f"  tax: statutory {TAX:.0%} (gilat_fy2025 p.164) used; effective TTM {(PRETAX_TTM - NI_TTM) / PRETAX_TTM:+.1%}"
  " (unrecognised tax losses USD 19.0M at 31.12.2025, gilat_fy2025 p.163: the shield is not valued, conservative)")

# Cash and claims, pro forma 3.11.2026
SERIES_C_REDEEMED_PAR = SERIES_C_PUBLIC_PAR_19AUG - SERIES_C_CONVERTED_AFTER_19AUG * SERIES_C_CONV_PRICE
SERIES_C_CASH = SERIES_C_REDEEMED_PAR * (1 + SERIES_C_COUPON_HALF) / 1000
SERIES_D_COUPON_PAID = (SERIES_D_PAR + SERIES_D_OCT_CONVERSIONS) * SERIES_D_COUPON_HALF / 1000
CASH_PF = CASH - OCT_BUYBACK - SERIES_C_CASH - SERIES_D_COUPON_PAID
CASH_OPEX_TTM = (REV_TTM - EBIT_TTM) - (DA_TTM + IRU_AMORT_TTM) + (LEASE_PRIN_TTM + LEASE_INT_TTM)   # cash operating costs incl. lease payments
EXCESS = excess_cash(CASH_PF, CASH_OPEX_TTM)
LEASES = LEASES_ST + LEASES_LT
NET_USD_LIAB_30JUN = USD_LIAB_30JUN - USD_ASSETS_30JUN
FX_BRIDGE_ADJ = NET_USD_LIAB_30JUN * (FX / FX_30JUN26 - 1)     # A-O4: the 30.6.2026 USD monetary items at the 3.11.2026 rate
P(f"  cash 30.6.2026 {CASH:,.0f} (restricted {RESTRICTED:,.0f} excluded) - Oct buyback {OCT_BUYBACK:,.0f} - Series C final redemption"
  f" {SERIES_C_CASH:,.0f} - Series D coupon {SERIES_D_COUPON_PAID:,.0f} = {CASH_PF:,.0f} pro forma 3.11.2026 (Q3 operating cash flow not added)")
P(f"  excess cash (d3) = {CASH_PF:,.0f} - 2/12 x cash operating costs {CASH_OPEX_TTM:,.0f} = {EXCESS:,.0f}")
P(f"  claims: leases {LEASES:,.0f}; Series D {SERIES_D_PAR / 1000:,.0f} at par if not converted (book {SERIES_D_LIAB:,.0f} at 30.6.2026);"
  " Series C nil after 1.9.2026; no bank debt; NCI nil; preferred nil")
P(f"  bridge at the 3.11.2026 rate (A-O4): net USD monetary liabilities 30.6.2026 {NET_USD_LIAB_30JUN:,} ILS k at {FX_30JUN26} (USD"
  f" {NET_USD_LIAB_30JUN / FX_30JUN26 / 1000:,.1f}M; USD liabilities {USD_LIAB_30JUN:,} vs USD assets {USD_ASSETS_30JUN:,}) -> +{FX_BRIDGE_ADJ:,.0f} at {FX};"
  f" forwards on USD {FWD_NOTIONAL_USD_K / 1000:.0f}M (strike and mark-to-market undisclosed) not credited")

# Bezeq IRU: committed consideration, payments, and the economics against renting at the regulated BSA price
IRU2_PRICE = IRU2_TOTAL * 1000 / IRU2_LINES
IRU_COMMITTED = IRU1_LINES * IRU1_PRICE / 1000 + IRU2_TOTAL
IRU_UNPAID_ALL = IRU_COMMITTED - IRU_PAID_TO_30JUN
IRU_UNPAID_IN_SERVICE = (IRU1_LINES * IRU1_PRICE + (ACTIVE_LINES - IRU1_LINES) * IRU2_PRICE) / 1000 - IRU_PAID_TO_30JUN
LINES_UNFILLED = IRU1_LINES + IRU2_LINES - ACTIVE_LINES
pv_iru1, pv_iru2, pv_bsa = pv_iru_line(IRU1_PRICE, R), pv_iru_line(IRU2_PRICE, R), pv_bsa_line(R)
IRU_NPV_VS_BSA = (IRU1_LINES * (pv_bsa - pv_iru1) + IRU2_LINES * (pv_bsa - pv_iru2)) / 1000
# AR-3: pv_iru_line is a PV at the line's delivery date. The bridges are dated 3.11.2026, so each unfilled line's PV is
# discounted from its tranche's start to VAL_T. Unfilled = the tranches not yet delivered at VAL_T plus the delivered but
# unfilled remainder (factor 1). Lines fill in delivery order, so the lines that are never used are the latest delivered.
assert sum(n for _, n in IRU_LINE_TRANCHES) == IRU1_LINES + IRU2_LINES
IRU_FUTURE = sorted(((s, n) for s, n in IRU_LINE_TRANCHES if s > VAL_T), reverse=True)    # latest first
LINES_FUTURE = sum(n for _, n in IRU_FUTURE)
LINES_DELIVERED_UNFILLED = LINES_UNFILLED - LINES_FUTURE
assert LINES_DELIVERED_UNFILLED >= 0


def dated_line_count(k: float) -> float:
    """Sum of the 3.11.2026 discount factors of the k latest-delivered unfilled lines (delivered ones count 1 each)."""
    acc, rem = 0.0, k
    for s, n in IRU_FUTURE:
        take = min(n, rem)
        acc += take / (1 + R) ** (s - VAL_T)
        rem -= take
    return acc + rem                      # what remains are delivered-but-unfilled lines, already at VAL_T


DF_HALF = dated_line_count(LINES_UNFILLED / 2) / (LINES_UNFILLED / 2)
DF_ALL = dated_line_count(LINES_UNFILLED) / LINES_UNFILLED
DEAD_HALF = LINES_UNFILLED / 2 * pv_iru2 * DF_HALF / 1000 * (1 - TAX)    # half the unfilled lines paid for and never used, after tax
DEAD_ALL_AT = LINES_UNFILLED * pv_iru2 * DF_ALL / 1000 * (1 - TAX)
DEAD_ALL_PRETAX = LINES_UNFILLED * pv_iru2 * DF_ALL / 1000
IRU_EXP_BASE = P_IRU_HALF_DEAD * DEAD_HALF                      # B-O6: the base's expected cost of the skew
assert abs(sum(c for _, c, _ in IRU_TRANCHES) - IRU_COMMITTED) < 1
P(f"  Bezeq IRU: committed {IRU_COMMITTED:,.0f} for {IRU1_LINES + IRU2_LINES:,} lines; paid to 30.6.2026 {IRU_PAID_TO_30JUN:,.0f};"
  f" unpaid {IRU_UNPAID_ALL:,.0f}, of which for the ~{ACTIVE_LINES:,} lines in service {IRU_UNPAID_IN_SERVICE:,.0f} (UNVERIFIED: the filings do not state it)")
P(f"      PV per line at r over 15 years at its delivery date, contract terms (10 payments at 5%, 4% O&M): IRU-1 {pv_iru1:,.0f}, IRU-2 {pv_iru2:,.0f}"
  f" vs regulated BSA at ILS {BSA_MONTHLY}/month {pv_bsa:,.0f} -> IRU vs BSA if every line is filled: {IRU_NPV_VS_BSA:+,.0f} pre-tax (not credited)")
P(f"      {LINES_UNFILLED:,} committed lines not yet filled: {LINES_FUTURE:,} in tranches delivered after 3.11.2026 (to 9.2028) and"
  f" {LINES_DELIVERED_UNFILLED:,} delivered; each PV dated to 3.11.2026 (AR-3: factor {DF_HALF:.3f} for the latest-delivered half,"
  f" {DF_ALL:.3f} for all)")
P(f"      half unused (the latest-delivered half) costs {DEAD_HALF:,.0f} after tax; the base carries"
  f" {P_IRU_HALF_DEAD:.0%} of it = {IRU_EXP_BASE:,.0f} (B-O6); all unused {DEAD_ALL_PRETAX:,.0f} pre-tax")

# Leverage (C2 / tier table), at 3.11.2026 pro forma
nd_bs = SERIES_D_PAR / 1000 + LEASES + FX_BRIDGE_ADJ - CASH_PF
P(f"  net debt with leases (Series D at par, FX at 3.157) {nd_bs:,.0f} = {nd_bs / EBIT_NORM:.1f}x EBIT_norm (net cash);"
  f" with the IRU unpaid for lines in service {nd_bs + IRU_UNPAID_IN_SERVICE:,.0f} = {(nd_bs + IRU_UNPAID_IN_SERVICE) / EBIT_NORM:.1f}x;"
  f" with all committed IRU {nd_bs + IRU_UNPAID_ALL:,.0f} = {(nd_bs + IRU_UNPAID_ALL) / EBIT_NORM:.1f}x")
lease_cash_fy25 = LEASE_PRIN_ILS["FY25"] + LEASE_INT_ILS["FY25"]
lease_int_fy25_audited = lease_cash_fy25 * LEASE_INT_USD[2025] / (LEASE_INT_USD[2025] + LEASE_PRIN_USD[2025])   # audited USD split (gilat_fy2025 p.132)
LEASE_INT_TTM_AUDITED = lease_int_fy25_audited - LEASE_INT_ILS["H1_25"] + LEASE_INT_ILS["H1_26"]
P(f"  interest cover TTM (A-O6, both splits): EBIT_adj / (lease + bond interest paid) = {EBIT_ADJ_TTM / (LEASE_INT_TTM + BOND_INT_TTM):.1f}x on the ILS"
  f" restatement (lease interest {LEASE_INT_TTM:,.0f}, {LEASE_INT_ILS['FY25'] / lease_cash_fy25:.1%} of FY2025 lease cash) or"
  f" {EBIT_ADJ_TTM / (LEASE_INT_TTM_AUDITED + BOND_INT_TTM):.1f}x on the audited USD split ({LEASE_INT_TTM_AUDITED:,.0f};"
  f" {LEASE_INT_USD[2025] / (LEASE_INT_USD[2025] + LEASE_PRIN_USD[2025]):.1%}); C2 asks >= 8x for A/B. Total lease cash, and so every valuation figure, is the same")
P("  C6 stress years (EBIT_adj / (lease interest + other interest paid), USD k): "
  + "; ".join(f"FY{y} {EBIT_ADJ_USD[y]:,} / ({LEASE_INT_USD[y]:,} + {OTHER_INT_USD[y]:,}) = {EBIT_ADJ_USD[y] / (LEASE_INT_USD[y] + OTHER_INT_USD[y]):.1f}x"
            for y in (2020, 2021, 2022))
  + "  (FY2020 and FY2022 are the designated stress years: not comfortable)")

# =====================================================================================================
# 4. Methods
# =====================================================================================================
OE_NORM = unlevered_owner_earnings(EBIT_NORM, AMORT_ACQ_NORM, TAX, DEP_TTM, MAINT_TTM)     # AR-1: the W-mean add-back
OE_TTM_UNLEV = unlevered_owner_earnings(EBIT_ADJ_TTM, AMORT_ACQ, TAX, DEP_TTM, MAINT_TTM)


def equity_value(oe_unlev: float, r: float = R, iru_cost: float = IRU_EXP_BASE, fx_adj: float = FX_BRIDGE_ADJ) -> float:
    """d3 bridge before Series D: EPV of operations + excess cash - leases - FX restatement of the USD monetary items
    to 3.11.2026 - IRU cost (expected or scenario dead cost)."""
    return equity_bridge(epv_operations(oe_unlev, r), excess_c=EXCESS, lease_liabilities=LEASES, debt=iru_cost + fx_adj)


P("")
P("== 4. Methods")
e_base = equity_value(OE_NORM)
v_epv, how_epv = per_share(e_base)
P(f"  d3 EPV: OE_unlevered = (EBIT_norm {EBIT_NORM:,.0f} + Amort_acq {AMORT_ACQ_NORM:,.0f}, W mean) x (1 - {TAX:.0%}) + Dep - maintenance (floor: 0)"
  f" = {OE_NORM:,.0f}; / r = {epv_operations(OE_NORM, R):,.0f}")
P(f"      + excess cash {EXCESS:,.0f} - leases {LEASES:,.0f} - FX restatement {FX_BRIDGE_ADJ:,.0f} - IRU expected cost {IRU_EXP_BASE:,.0f}"
  f" = {e_base:,.0f} before Series D -> {fmt(v_epv)}  [{how_epv}]")

# d4 DCF. Per-share record: EPS 3-year averages start negative (not computable); revenue per share fell (dilution).
rev_ps = {y: REV_USD[y] / s for y, s in ((2021, 58_438_636), (2025, 93_937_313))}   # shares gilat_fy2023 p.151; gilat_fy2025 p.165
g_rev_ps = (rev_ps[2025] / rev_ps[2021]) ** (1 / 4) - 1
eps_3y = (statistics.mean([-0.033, -0.093, -0.070]), statistics.mean([0.011, 0.0234, 0.0707]))   # basic EPS USD (gilat_fy2022 p.119; gilat_fy2023 p.118; gilat_fy2024 p.120; gilat_fy2025 p.127)
G_CAP = growth_cap(None, None, None)          # the per-share OE/EPS record has no rate (negative base); ROIIC set to r: only the 10% cap remains
dcf_base = dcf_operations(OE_NORM, R, 0.0, None, gT=0.0)
v_dcf, _ = per_share(equity_bridge(dcf_base.operations_value, excess_c=EXCESS, lease_liabilities=LEASES, debt=IRU_EXP_BASE + FX_BRIDGE_ADJ))
dcf_rps = dcf_operations(OE_NORM, R, g_rev_ps, None, gT=0.0)
v_dcf_rps, _ = per_share(equity_bridge(dcf_rps.operations_value, excess_c=EXCESS, lease_liabilities=LEASES, debt=IRU_EXP_BASE + FX_BRIDGE_ADJ))
P(f"  d4 growth cap: per-share EPS, 3-year averages FY2020-22 {eps_3y[0]:+.4f} -> FY2023-25 {eps_3y[1]:+.4f} USD: negative base, no rate (Israeli window, not ten years);"
  f" ROIIC = r (no moat), so growth adds no value; cap g1 <= {G_CAP:.0%}")
P(f"  d4 DCF base, g1 0%, gT 0%: operations {dcf_base.operations_value:,.0f} (terminal {dcf_base.terminal_share:.0%} of total) -> {fmt(v_dcf)} (= EPV)")
P(f"      diagnostic: revenue per share FY2021-FY2025 {g_rev_ps:+.1%} a year (dilution outran growth); at that rate for ten years"
  f" operations {dcf_rps.operations_value:,.0f} -> {fmt(v_dcf_rps)}")
for row in (dcf_base.rows[0], dcf_base.rows[4], dcf_base.rows[9]):
    P(f"      year {row['year']:>2}: OE {row['oe']:,.0f}  reinvestment {row['reinvestment']:,.0f}  FCF {row['fcf']:,.0f}")

# d6/d7 asset values. Charter H2: NCAV and Dempster from ONE balance-sheet date (30.6.2026), identity-checked.
NCAV = ncav(CURRENT_ASSETS, TOTAL_LIAB)
DEMPSTER = dempster_value(CASH, RECEIVABLES, INVENTORY, DEFERRED_ST + OTHER_REC, 0.0, TOTAL_LIAB)
nn = netnet_buy_test(MCAP, NCAV, DEMPSTER)
NETNET_LINE = min(nn["two_thirds_ncav"], DEMPSTER) * 1000 / SHARES_LISTED          # the only charter Tier C line (d6, d11): a reference, not a buy price
# Share basis (AR-4): the 30.6.2026 balance sheet per 3.11.2026 listed share, i.e. the price at which today's market cap (the
# aggregate test above) would equal the 30.6.2026 line; per 30.6.2026 share the same amount is NETNET_LINE_30JUN
NETNET_LINE_30JUN = min(nn["two_thirds_ncav"], DEMPSTER) * 1000 / SHARES_30JUN
# pro forma 3.11.2026 (same events as the EPV bridge): cash after the October buyback and Series C/D payments; Series C gone; Series D at par; FX at 3.157
TL_PF = TOTAL_LIAB - SERIES_C_LIAB - SERIES_D_LIAB + SERIES_D_PAR / 1000 + FX_BRIDGE_ADJ
NCAV_PF = ncav(CURRENT_ASSETS - (CASH - CASH_PF), TL_PF)
DEMPSTER_PF = dempster_value(CASH_PF, RECEIVABLES, INVENTORY, DEFERRED_ST + OTHER_REC, 0.0, TL_PF)
NETNET_LINE_PF = max(0.0, min(2 / 3 * NCAV_PF, DEMPSTER_PF)) * 1000 / SHARES_LISTED
P(f"  d6 NCAV (30.6.2026) = current assets {CURRENT_ASSETS:,.0f} - total liabilities {TOTAL_LIAB:,.0f} = {NCAV:,.0f} -> {NCAV * 1000 / SHARES_30JUN:.3f} ILS/share")
P(f"  d6 Dempster (30.6.2026) = cash 100% + receivables 85% + inventory 60% + prepaid/other 25% - liabilities (PP&E, ROU, IRU at nil) = {DEMPSTER:,.0f}"
  f" -> {DEMPSTER * 1000 / SHARES_30JUN:.3f} ILS/share")
P(f"      net-net test: market cap {MCAP:,.0f} <= 2/3 NCAV {nn['two_thirds_ncav']:,.0f} and <= Dempster {DEMPSTER:,.0f}? {nn['passes']}"
  f" (market cap = {MCAP / NCAV:.1f}x NCAV, {MCAP / DEMPSTER:.1f}x Dempster) -> charter Tier C net-net reference line {NETNET_LINE:.3f} ILS"
  f" per 3.11.2026 listed share ({NETNET_LINE_30JUN:.3f} per 30.6.2026 share)")
P(f"      pro forma 3.11.2026: NCAV {NCAV_PF:,.0f}, Dempster {DEMPSTER_PF:,.0f} -> line {NETNET_LINE_PF:.3f}: the October buyback, the Series C"
  " redemption and the dollar's rise since 30.6 have used up most of the liquidation cushion")
P(f"      off balance sheet: unpaid Bezeq consideration {IRU_UNPAID_ALL:,.0f} (UNVERIFIED) = {IRU_UNPAID_ALL / NCAV:.1f}x NCAV; PV of the"
  f" unfilled lines {DEAD_ALL_PRETAX:,.0f}: the asset value is not firm (H2)")
TBV = tangible_book(EQUITY, 0.0, INTANGIBLES)
v_tbv_30jun = TBV * 1000 / SHARES_30JUN
SD_PAR_30JUN = SERIES_D_PAR_19AUG + SERIES_D_CONVERTED_1JUL_19AUG
SC_CONV_PAR_AFTER = SERIES_C_CONVERTED_1JUL_19AUG + SERIES_C_CONVERTED_AFTER_19AUG * SERIES_C_CONV_PRICE
EQUITY_PF = (EQUITY - OCT_BUYBACK - FX_BRIDGE_ADJ
             + SERIES_D_LIAB * (SD_PAR_30JUN - SERIES_D_PAR) / SD_PAR_30JUN                      # Series D converted after 30.6 moves to equity
             + SERIES_C_LIAB * SC_CONV_PAR_AFTER / (SC_CONV_PAR_AFTER + SERIES_C_REDEEMED_PAR))   # Series C converted after 30.6
TBV_PF = tangible_book(EQUITY_PF, 0.0, INTANGIBLES)
v_tbv = TBV_PF * 1000 / SHARES_LISTED
v_tbv_hard = (TBV_PF - DEFERRED_ST - DEFERRED_LT - DTA) * 1000 / SHARES_LISTED
P(f"  d7 tangible book 30.6.2026 = equity {EQUITY:,.0f} - intangibles incl. goodwill {INTANGIBLES:,.0f} = {TBV:,.0f} -> {v_tbv_30jun:.3f} on 30.6 shares")
P(f"      3.11.2026 basis (A-O8: buyback, conversions, FX at 3.157): equity {EQUITY_PF:,.0f} -> {fmt(v_tbv)}; without IRU prepayments"
  f" {DEFERRED_ST + DEFERRED_LT:,} and the DTA {DTA:,}: {v_tbv_hard:.3f}")
P("  d7 private-owner value: none evidenced. No disclosed control transaction; the only attempt to sell control failed: on 17.2.2021")
P("      Eurocom's liquidators dispersed the 41% block in 2-3% lots for ~ILS 26M at a ~ILS 68M market value 'after previous attempts")
P(f"      to sell the control core did not succeed' (Calcalist L-3894358) = {26 / 0.41 / 68 - 1:+.1%} vs market: no premium (B-O9).")
P("      The placements at 0.30 and 0.88, conversions at 1.00/1.35 and buybacks at 2.60/~2.03 are minority trades (framework d7).")

# d5 pre-tax multiple on EV (at the price Series D converts)
EV = enterprise_value(PRICE * (SHARES_LISTED + SERIES_D_PAR) / 1000, 0.0, CASH_PF, LEASES + FX_BRIDGE_ADJ)
pm_norm, pm_ttm = pretax_multiple(EV, EBIT_NORM), pretax_multiple(EV, EBIT_ADJ_TTM)
v_10x, _ = per_share(equity_bridge(10 * EBIT_NORM, excess_c=EXCESS, lease_liabilities=LEASES, debt=IRU_EXP_BASE + FX_BRIDGE_ADJ))
P(f"  d5 EV {EV:,.0f} (as-converted market cap + leases + FX restatement - cash): EV/EBIT_norm {pm_norm['ev_to_ebit_norm']:.1f}x (yield {pm_norm['pretax_yield']:.1%});"
  f" EV/TTM EBIT_adj {pm_ttm['ev_to_ebit_norm']:.1f}x (yield {pm_ttm['pretax_yield']:.1%})")
P(f"      10x EBIT_norm + excess cash - leases - FX - IRU expected cost -> {fmt(v_10x)} (sanity check; about 10x is d5's fair price for Tier A)")

# d9 Graham's yardstick, ILS government yield (looser than Graham's AA corporate). A-O10: the H1 2026 FX gain on the USD
# liabilities (ILS functional from 1.1.2026) is stripped too; only the cash FX line was removed before. H2 2025 (USD functional)
# carried FX on ILS items in the other direction: net UNVERIFIED, so this strip is one-sided (conservative).
FX_GAIN_H1_26_EST = USD_NONCASH_NET_LIAB_1JAN26 * (FX_31DEC25 - FX_30JUN26)
NI_NORM_TTM = (PRETAX_TTM - SUPPLIER_CREDIT_TTM - ONEOFF_EQUIP_PROFIT + FX_CASH_TTM + OPTION_REVAL_TTM - FX_GAIN_H1_26_EST) * (1 - TAX)
gy = graham_yardstick(NI_NORM_TTM, MCAP, Y10_IL)
P(f"  d9 Graham [I, looser: ILS government yield]: NI_norm_ttm {NI_NORM_TTM:,.0f} (pre-tax less one-offs, non-cash FX/option items and the estimated"
  f" H1 2026 FX gain on USD liabilities {FX_GAIN_H1_26_EST:,.0f}, UNVERIFIED; at 23%); earnings yield {gy['earnings_yield']:.1%} vs {gy['required_yield']:.2%};"
  f" P/E {gy['pe']:.1f} vs cap {gy['pe_cap']:.0f} -> {gy['passes']}")

# d8 implied growth: operations value the price implies (claims as in the base bridge)
FD_PRICE = SHARES_LISTED + SERIES_D_PAR + option_shares(PRICE)
EV_OPS_IMPLIED = PRICE * FD_PRICE / 1000 + LEASES + FX_BRIDGE_ADJ + IRU_EXP_BASE - EXCESS
IG_NORM = implied_growth(EV_OPS_IMPLIED, OE_NORM, R, None)
IG_TTM = implied_growth(EV_OPS_IMPLIED, OE_TTM_UNLEV, R, None)
P(f"  d8 implied growth: operations value at the price {EV_OPS_IMPLIED:,.0f} (fully diluted {FD_PRICE:,.0f} shares x price + leases + FX + IRU expected cost - excess cash)")
P(f"      = {EV_OPS_IMPLIED / OE_NORM:.1f}x normalised OE {OE_NORM:,.0f} -> {IG_NORM:+.1%} a year for ten years (no reinvestment charged: the generous reading)")
P(f"      = {EV_OPS_IMPLIED / OE_TTM_UNLEV:.1f}x TTM OE {OE_TTM_UNLEV:,.0f} -> {IG_TTM:+.1%} a year: the price assumes the war-era earnings largely persist")
P(f"      record: revenue per share {g_rev_ps:+.1%} a year FY2021-FY2025; EPS from losses to profits (no rate); implied growth is"
  " above any per-share record (D4 is a FLAG for A/B/D only)")

# =====================================================================================================
# 5. Value range
# =====================================================================================================
# IRU accounting gap (B-O1, B-O3): booked TTM cost (amortisation + modelled 4% O&M) vs the economic cost at r (level monthly
# equivalent of the contract PV, scaled to BSA = 58). UNVERIFIED: lines in use per period are not disclosed.
econ_pm = {1: BSA_MONTHLY * pv_iru1 / pv_bsa, 2: BSA_MONTHLY * pv_iru2 / pv_bsa}


def iru_gap(l1: float, l2: float) -> float:
    booked = IRU_AMORT_TTM + IRU_OM_RATE * (IRU1_PRICE * l1 + IRU2_PRICE * l2) / 1000
    economic = (econ_pm[1] * l1 + econ_pm[2] * l2) * 12 / 1000
    return economic - booked


IRU_GAP = iru_gap(IRU1_TTM_LINE_YEARS, IRU2_TTM_LINE_YEARS)
IRU_GAP_LOW = iru_gap(IRU1_TTM_LINE_YEARS_CONTRACT, IRU2_TTM_LINE_YEARS)
# optimistic: TTM run-rate (one-offs removed) persists, net of the IRU accounting gap: war-level demand, the 2026 shekel, Vodacom renewed, lines filled
OE_OPT = unlevered_owner_earnings(EBIT_ADJ_TTM - IRU_GAP, AMORT_ACQ, TAX, DEP_TTM, MAINT_TTM)
v_opt, how_opt = per_share(equity_value(OE_OPT, iru_cost=0.0))
v_opt_gross, _ = per_share(equity_value(OE_TTM_UNLEV, iru_cost=0.0))
# base: charter EBIT_norm over W = FY2020-FY2025; IRU expected cost; FX restated
v_base, how_base = v_epv, how_epv
# conservative (B-O3): Vodacom DRC not renewed at 31.3.2027 (gilat_fy2025 p.55-56; Vodacom Group-Starlink partnership of
# 12.11.2025): its 2025 contribution at the 2025 global-segment margin removed (contract margin UNVERIFIED); IRU as in the base
VODACOM_CONTRIB = VODACOM_REV_2025 * GLOBAL_SEG_RES_2025 / GLOBAL_SEG_REV_2025 * FX
OE_CONS = unlevered_owner_earnings(EBIT_NORM - VODACOM_CONTRIB, AMORT_ACQ_NORM, TAX, DEP_TTM, MAINT_TTM)
e_cons = equity_value(OE_CONS)
v_cons, how_cons = per_share(e_cons)
v_cons_iru, _ = per_share(equity_value(OE_NORM, iru_cost=DEAD_HALF))                  # variant: Vodacom renewed, half the unfilled lines unused (the team's conservative)
v_cons_both, _ = per_share(equity_value(OE_CONS, iru_cost=DEAD_HALF))                 # variant: both
v_base_no_iru, _ = per_share(equity_value(OE_NORM, iru_cost=0.0))                      # sensitivity: no IRU expected cost
v_base_no_fx, _ = per_share(equity_value(OE_NORM, fx_adj=0.0))                         # sensitivity: bridge at the 30.6.2026 rate
v_base_5, _ = per_share(equity_value(unlevered_owner_earnings(norm_5.ebit_norm, amort_acq_mean(YEARS_5), TAX, DEP_TTM, MAINT_TTM)))
v_base_w_ttm, _ = per_share(equity_value(unlevered_owner_earnings(norm_w_ttm.ebit_norm, amort_acq_mean(YEARS, True), TAX, DEP_TTM, MAINT_TTM)))
v_base_team, _ = per_share(equity_value(unlevered_owner_earnings(norm_team.ebit_norm, amort_acq_mean(YEARS_5, True), TAX, DEP_TTM, MAINT_TTM)))
v_isp_stall, _ = per_share(equity_value(OE_NORM, iru_cost=DEAD_ALL_AT))               # variant: base earnings, ISP stalls at today's lines
# worst (ten years out): pre-war demand, Vodacom lost (3.2027), ISP stalls; liquidation basis: Dempster value pro forma (Series D
# handled at par in per_share) less every unfilled committed IRU line at its PV, FX at 3.157
DEMPSTER_EX_CD = dempster_value(CASH_PF, RECEIVABLES, INVENTORY, DEFERRED_ST + OTHER_REC, 0.0,
                                TOTAL_LIAB - SERIES_C_LIAB - SERIES_D_LIAB + FX_BRIDGE_ADJ)
v_worst, how_worst = per_share(DEMPSTER_EX_CD - DEAD_ALL_PRETAX)
v_worst_no_iru, _ = per_share(DEMPSTER_EX_CD)
PROBS = {"worst": 0.15, "conservative": 0.30, "base": 0.45, "optimistic": 0.10}   # assumed (model judgements, uncalibrated); B-O3
VALS = {"worst": v_worst, "conservative": v_cons, "base": v_base, "optimistic": v_opt}
v_pw = sum(PROBS[k] * VALS[k] for k in PROBS)
alt_weights = {"team 10/25/45/20": (0.10, 0.25, 0.45, 0.20), "red team 20/30/40/10": (0.20, 0.30, 0.40, 0.10)}

P("")
P("== 5. Value range (per share, at 3.11.2026)")
P(f"  worst case    {fmt(v_worst)}  ten years out, held with confidence as a floor: pre-war defence demand, Vodacom lost (3.2027),")
P(f"                ISP stalls. Liquidation value pro forma {DEMPSTER_EX_CD:,.0f} (before Series D) - {LINES_UNFILLED:,} unused committed IRU lines"
  f" {DEAD_ALL_PRETAX:,.0f} (PV, pre-tax) [{how_worst}]; without the IRU {v_worst_no_iru:.3f}. Rests on UNVERIFIED IRU terms (balance, schedule, tranche opt-out)")
P(f"  conservative  {fmt(v_cons)}  Vodacom not renewed: its 2025 contribution {VODACOM_CONTRIB:,.0f} ({VODACOM_CONTRIB / EBIT_NORM:.0%} of EBIT_norm) removed;"
  f" equity before Series D {e_cons:,.0f} vs par {SERIES_D_PAR / 1000:,.0f} [{how_cons}]")
P(f"                variants: Vodacom renewed, half the unfilled lines unused {v_cons_iru:.3f}; both {v_cons_both:.3f};"
  f" base earnings with the ISP stalled at today's lines {v_isp_stall:.3f}")
P(f"  base          {fmt(v_base)}  EPV on EBIT_norm {EBIT_NORM:,.0f} (W = FY2020-FY2025), IRU expected cost, FX at 3.157 [{how_base}]")
P(f"                sensitivities: without the IRU expected cost {v_base_no_iru:.3f}; bridge at the 30.6 rate {v_base_no_fx:.3f};"
  f" W = FY2021-25 {v_base_5:.3f}; W + TTM {v_base_w_ttm:.3f}; the team's earlier window (FY2021-25 + TTM) {v_base_team:.3f}")
# B-O3: what the base needs, against the CEO's "routine" level (Bizportal 20014148, 4.3.2025: wartime turnover "about double the
# normal period"; defence "about 50%" of turnover in wartime and "about 30%" in routine). Two readings of routine turnover:
# TTM / 2 (the red team's) and, holding non-defence turnover fixed, TTM x 0.5 / 0.7 (the 50%/30% shares).
GP_USD = {2020: 15_141, 2021: 12_444, 2022: 10_495, 2023: 12_016, 2024: 16_120}   # gilat_fy2022 p.119; gilat_fy2023 p.118; gilat_fy2025 p.92
OPEX_USD = {2023: 4_130 + 5_708, 2024: 4_722 + 6_449}                            # S&M + G&A: gilat_fy2023 p.118; gilat_fy2025 p.92 (totals 9,838 / 11,171 confirmed on gilat_fy2025 p.96)
GP_TTM = 78_938 - 35_978 + 42_251                                                # gilat_q2_2026_full p.32
OPEX_TTM_ILS = 45_958 - 23_137 + 22_856                                          # p.32
gm_pre = statistics.mean(GP_USD[y] / REV_USD[y] for y in (2020, 2021, 2022, 2023, 2024))
opex_lean = statistics.mean(OPEX_USD.values()) * FX
routine = {"TTM/2 ('about double')": REV_TTM / 2, "TTM x 0.5/0.7 (defence 50% -> 30%)": REV_TTM * 0.5 / 0.7}
P(f"  what the base needs (B-O3): at the FY2020-24 mean gross margin {gm_pre:.1%} and FY2023-24 opex {opex_lean:,.0f}, EBIT_norm {EBIT_NORM:,.0f} needs"
  f" revenue {(EBIT_NORM + opex_lean) / gm_pre:,.0f} ({(EBIT_NORM + opex_lean) / gm_pre / REV_TTM:.0%} of TTM); with TTM opex {OPEX_TTM_ILS:,}"
  f" {(EBIT_NORM + OPEX_TTM_ILS) / gm_pre:,.0f} ({(EBIT_NORM + OPEX_TTM_ILS) / gm_pre / REV_TTM:.0%})")
for k, rv in routine.items():
    P(f"      routine turnover on the reading {k}: {rv:,.0f} -> EBIT at the pre-war margin with FY2023-24 opex {rv * gm_pre - opex_lean:,.0f},"
      f" with TTM opex {rv * gm_pre - OPEX_TTM_ILS:,.0f}; at the TTM margin {GP_TTM / REV_TTM:.1%} and TTM opex {rv * GP_TTM / REV_TTM - OPEX_TTM_ILS:,.0f}")
P("      reading: the base is reachable only if the business keeps part of its war-era margin or its lean pre-war cost base; it is not")
P("      a floor. The worst and conservative cases (45% together) carry the readings in which it is not reached.")
P(f"  optimistic    {fmt(v_opt)}  EPV on TTM EBIT_adj {EBIT_ADJ_TTM:,.0f} less the IRU accounting gap {IRU_GAP:,.0f} (range {IRU_GAP_LOW:,.0f}-{IRU_GAP:,.0f}"
  f" on the contractual vs assumed line-years; UNVERIFIED); before the gap {v_opt_gross:.3f} [{how_opt}]")
P(f"  probabilities {PROBS} -> probability-weighted {fmt(v_pw)}")
P(f"      stated probability that Vodacom is lost (worst + conservative, both without it): {PROBS['worst'] + PROBS['conservative']:.0%}")
for k, w in alt_weights.items():
    P(f"      under {k}: {sum(wi * VALS[n] for wi, n in zip(w, PROBS)):.3f}")
P(f"  from the price: worst {v_worst / PRICE - 1:+.0%}, conservative {v_cons / PRICE - 1:+.0%}, base {v_base / PRICE - 1:+.0%},"
  f" optimistic {v_opt / PRICE - 1:+.0%}: heads we win a little, tails we lose a lot (Pabrai's test inverts)")

# E1: the filed record and a dated cash runway (A-O3, B-O4)
ISP_CASH = 2 * (ISP_SEG_H1_26[0] + ISP_SEG_H1_26[1])         # ISP cash margin at today's lines before IRU payments, annualised (FS note)
core_prewar = statistics.mean(cash_oe[y] + OTHER_INT_USD[y] for y in (2021, 2022)) * FX                 # FY2021-22 cash proxy before bond interest
core_mid = statistics.mean([cash_oe[2023] + OTHER_INT_USD[2023], cash_oe[2024] + OTHER_INT_USD[2024],
                            cash_oe[2025] + OTHER_INT_USD[2025] + 3_902]) * FX                          # FY2023-25, FY2025 IRU payments added back (gilat_fy2025 p.152)
FLOOR_2M = CASH_OPEX_TTM / 6
SCHEDULE = iru_schedule()


def runway(core: float, cpi: float = 0.0) -> list:
    """Year-end cash 2027-2036: start from pro forma cash; add core + ISP cash; pay the IRU schedule, the Series D coupon
    and, with the share below ILS 1.40 (worst case: no conversion), 25% of par a year on 1.4.2028-1.4.2031."""
    sch = iru_schedule(cpi) if cpi else SCHEDULE
    cash, par, rows = CASH_PF, SERIES_D_PAR / 1000, []
    for y in range(2027, 2037):
        coupon = SERIES_D_COUPON * par
        principal = SERIES_D_PAR / 1000 / 4 if 2028 <= y <= 2031 else 0.0
        par -= principal
        cash += core + ISP_CASH - sch.get(y, 0.0) - coupon - principal
        rows.append((y, cash))
    return rows


P("  E1 impairment markers (charter Mandate; checklist E1), tested on the filed record and a dated runway:")
P("      filed record: three consecutive annual reports carried the dedicated working-capital disclosure of the warning-sign regime")
P("      (Reg. 10(b)(14)): 31.12.2023 consolidated deficit USD 357k, solo OCF negative (gilat_fy2023 p.91); 31.12.2024 deficit USD 9,484k,")
P("      solo OCF negative (gilat_fy2024 p.88); 31.12.2025 deficit USD 1,874k, solo deficit 3,942k (gilat_fy2025 p.99). July 2024: Series C")
P("      9,965,474 par exchanged for 17,439,580 shares + cash, 'a significant debt reduction' (gilat_fy2024 p.88-89). The regime ended only")
P("      at 30.6.2026 (positive working capital 69,035, no warning signs: gilat_h1_2026 p.14). Shelf prospectus open since April 2026 (p.49).")
P(f"      runway: from pro forma cash {CASH_PF:,.0f} at 3.11.2026 (Q3 2026 operating cash flow not added; Nov-Dec 2026 flows ignored), year-end 2027-2036;")
P("      worst-case share price below ILS 1.40, so Series D does not convert and amortises 25% a year from 1.4.2028; ISP at today's lines.")
P("      IRU cash by year on the ten-instalment terms (principal + vendor interest; O&M only on tranches from 7.2026), UNVERIFIED terms:")
P("        " + "  ".join(f"{y}:{SCHEDULE.get(y, 0):,.0f}" for y in range(2025, 2037)))
P(f"        filed payments run AHEAD of this schedule: {IRU_PAID_ILS['FY25']:,} paid in FY2025 vs {SCHEDULE.get(2025, 0):,.0f} modelled (gilat_q2_2026_full p.38)")
runway_rows = {}
for label, core in (("pre-war core (FY2021-22 cash proxy before bond interest)", core_prewar), ("core = 0", 0.0),
                    ("FY2023-25 core, IRU payments added back", core_mid)):
    rows = runway(core)
    runway_rows[label] = rows
    neg = next((y for y, c in rows if c < 0), None)
    floor = next((y for y, c in rows if c < FLOOR_2M), None)
    P(f"      {label:<56} core {core:>8,.0f}/yr + ISP {ISP_CASH:,}/yr: below two months' costs ({FLOOR_2M:,.0f}) in {floor}, below zero in {neg};"
      f" end-2027 {dict(rows)[2027]:,.0f}, end-2028 {dict(rows)[2028]:,.0f}")
NEW_MONEY_YEAR = next((y for y, c in runway_rows["pre-war core (FY2021-22 cash proxy before bond interest)"] if c < 0), None)
P(f"      -> marker (1) (a maturity leading to dilution) is reachable: in the worst case new money is needed by {NEW_MONEY_YEAR}, while Series D")
P("         still amortises 25% a year in 2028-2031 and the 2023 rights issue at 0.30 and the 2024 exchange are the precedent. E1 FAILS.")
P("      markers (2)/(3): no filed going-concern doubt (FY2025 opinion unqualified, one key audit matter on revenue: gilat_fy2025 p.123-124);")
P("         an onerous-contract provision (IAS 37) on unfilled lines could bring the Bezeq commitment onto the balance sheet: possible, not shown.")
P("      not in the runway (UNVERIFIED): the Intelsat purchase commitments, 'currently backed by service orders from existing customers' (p.160)")
p_one_year = all(dict(r)[2027] > 0 for r in runway_rows.values())
P(f"      C1 (a year of flat revenue and EBIT -30%): the runway is a harsher test (the pre-war core is a cash loss), and year-end 2027 cash")
P(f"         stays positive in all three cases: {p_one_year}; no maturity before 1.4.2028; covenants (net financial debt/assets <= 60%,")
P("         equity/assets >= 12%) at -24% and 48% (gilat_h1_2026 p.23, p.25): no breach and no new money within the year")

# F4 stresses on the base (A-O2): flow (hedged-cost proxy) + remeasurement of the filed net USD monetary position
P("  F4 stresses on base (revenue ~77% ILS, Africa USD; satellite costs and 91% of leases+suppliers USD vs 21% of customers;")
P("      Series D ILS unlinked fixed; Bezeq IRU half-CPI-linked):")
f4 = {}
for shock in (0.10, 0.20, -0.10):
    flow = shock * USD_COST_PROXY * FX
    remeasure = NET_USD_LIAB_30JUN * FX / FX_30JUN26 * shock
    oe_s = unlevered_owner_earnings(EBIT_NORM - flow, AMORT_ACQ_NORM, TAX, DEP_TTM, MAINT_TTM)
    v_s, _ = per_share(equity_value(oe_s, iru_cost=IRU_EXP_BASE + remeasure))
    hedge = shock * FWD_NOTIONAL_USD_K * FX
    v_h, _ = per_share(equity_value(oe_s, iru_cost=IRU_EXP_BASE + remeasure - hedge))
    f4[shock] = (v_s, v_h)
    P(f"      USD/ILS {shock:+.0%}: flow {-flow:+,.0f}/yr pre-tax (USD 24M hedged-cost proxy, UNVERIFIED); remeasurement {-remeasure:+,.0f} one-off"
      f" -> base {fmt(v_s)} ({v_s / v_base - 1:+.0%}); if the USD {FWD_NOTIONAL_USD_K / 1000:.0f}M of forwards move fully: {v_h:.3f}")
move_since = (1 - 0.1253) * (FX_30JUN26 / FX_31DEC25) - 1      # USD/ILS -12.53% in 2025 (gilat_q2_2026_full p.43), then 3.19 -> 2.978
P(f"      USD/ILS moved {move_since:+.1%} from 31.12.2024 to 30.6.2026 and {FX / FX_30JUN26 - 1:+.1%} since: a 20% reversal is inside the range already seen")
pv_cpi = {c: sum(v / (1 + R) ** max(0.0, (y + 0.5) - 2026.84) for y, v in iru_schedule(c).items() if y >= 2027) for c in (0.02, 0.05)}
CPI_HIT = pv_cpi[0.05] - pv_cpi[0.02]
v_cpi, _ = per_share(equity_value(OE_NORM, iru_cost=IRU_EXP_BASE + CPI_HIT * (1 - TAX)))
P(f"      high CPI (5% vs 2% a year): PV at r of the committed IRU cash from 2027 +{CPI_HIT:,.0f} pre-tax = {CPI_HIT * (1 - TAX) * 1000 / SHARES_LISTED:.3f} ILS/share"
  f" after tax -> base {v_cpi:.3f}. No CPI-linked FINANCIAL debt (Series D unlinked: gilat_h1_2026 p.24); about ILS {IRU_UNPAID_ALL / 1000:,.0f}M of IRU")
P("         commitments carry 50% CPI linkage on pulses 2-3 and O&M (gilat_fy2025 p.153), and the addendum is 'CPI-linked' (p.42, p.183) (UNVERIFIED balance)")
P(f"      +2 points on rates: no floating debt (Series D fixed 5.5%); r stays 10% (IL y10 {Y10_IL + 0.02:.2%} + 3 < 10%); the vendor rate of later IRU pulses")
P("         resets to Bezeq's yield at each pulse, but those pulses are conditional; cash earns more: no hit to the base")
F4_FAILS = f4[0.10][0] < 0.5 * v_base and f4[0.20][0] < 0.1 * v_base
P(f"      F4 verdict: the base does not survive a sharp shekel move (+10% -> {f4[0.10][0] / v_base - 1:+.0%}; +20% -> {f4[0.20][0] / v_base - 1:+.0%}): F4 FAILS = {F4_FAILS}")


# AR-5: what the F4 failure rests on. The filed linkage table gives the remeasurement; the flow is the UNVERIFIED proxy.
def f4_base(shock: float, usd_flow_k: float, remeasure: bool = True) -> float:
    flow = shock * usd_flow_k * FX
    rem = NET_USD_LIAB_30JUN * FX / FX_30JUN26 * shock if remeasure else 0.0
    oe = unlevered_owner_earnings(EBIT_NORM - flow, AMORT_ACQ_NORM, TAX, DEP_TTM, MAINT_TTM)
    return per_share(equity_value(oe, iru_cost=IRU_EXP_BASE + rem))[0]


def f4_fails_at(usd_flow_k: float) -> bool:
    return f4_base(0.10, usd_flow_k) < 0.5 * v_base and f4_base(0.20, usd_flow_k) < 0.1 * v_base


f4_rem_only = {s: f4_base(s, 0.0) for s in (0.10, 0.20)}
f4_flow_only = {s: f4_base(s, USD_COST_PROXY, remeasure=False) for s in (0.10, 0.20)}
lo, hi = 0.0, USD_COST_PROXY
assert f4_fails_at(hi) == F4_FAILS
for _ in range(60):
    mid = (lo + hi) / 2
    lo, hi = (lo, mid) if f4_fails_at(mid) else (mid, hi)
F4_BREAKEVEN_USD_K = hi
# Cross-check of the proxy from the FY2025 cost structure (USD k): cost lines priced in USD by their nature (satellite services,
# mobile-satellite airtime and telephony, equipment sold: gilat_fy2025 p.173) and satellite-lease cash (p.132), less the global
# segment's USD revenue (p.181). The filings do not split costs by currency: UNVERIFIED, a cross-check only.
USD_COST_LINES_2025 = 11_220 + 12_614 + 5_559 + LEASE_PRIN_USD[2025] + LEASE_INT_USD[2025]
P(f"      what F4 rests on (AR-5): the filed remeasurement alone leaves the base at {f4_rem_only[0.10]:.3f} (+10%) and {f4_rem_only[0.20]:.3f} (+20%),"
  f" which would pass; the flow proxy alone gives {f4_flow_only[0.10]:.3f} and {f4_flow_only[0.20]:.3f}. F4 fails for any net USD cost flow above"
  f" USD {F4_BREAKEVEN_USD_K / 1000:.1f}M a year (proxy USD {USD_COST_PROXY / 1000:.0f}M, UNVERIFIED); cross-check: FY2025 USD-priced costs"
  f" {USD_COST_LINES_2025:,} less global-segment revenue {GLOBAL_SEG_REV_2025:,} = USD {(USD_COST_LINES_2025 - GLOBAL_SEG_REV_2025) / 1000:.1f}M")

# Sensitivity grid around base (D3): r +/- 1 point, g +/- 2 points; ROIIC held at 10% (no moat), terminal growth min(g, 2.5%) >= 0
def base_value(r: float, g: float) -> float:
    res = dcf_operations(OE_NORM, r, g, 0.10 if g > 0 else None, gT=max(0.0, min(g, 0.025)), roiic_T=0.10)
    return per_share(equity_bridge(res.operations_value, excess_c=EXCESS, lease_liabilities=LEASES, debt=IRU_EXP_BASE + FX_BRIDGE_ADJ))[0]


grid = sensitivity_grid(base_value, R, 0.0)
P("  sensitivity grid, base value per share (r +/- 1 point; g +/- 2 points around g 0%; ROIIC 10%):")
P("      r \\ g        -2%      0%     +2%")
for rr in (R - 0.01, R, R + 0.01):
    P(f"      {rr:4.0%}   " + "  ".join(f"{grid['grid'][(round(rr, 4), round(gg, 4))]:6.3f}" for gg in (-0.02, 0.0, 0.02)))
P(f"      minimum {grid['min']:.3f}, maximum {grid['max']:.3f} vs price {PRICE:.3f}: base > price everywhere (D3): {grid['min'] > PRICE}")

# =====================================================================================================
# 6. Margin and buy line
# =====================================================================================================
DATA_FLAGS = ["cycle_window_short", "derived_tier2_field", "microcap_field_unavailable"]
margin = required_margin("C", DATA_FLAGS, endogenous_addback=False)
methods = {
    "EPV, EBIT_norm W = FY2020-25 (d3)": v_epv,
    "DCF 10y, g 0%, ROIIC = r (d4)": v_dcf,
    "10x EBIT_norm + net excess cash (d5)": v_10x,
    "tangible book 3.11.2026 basis (d7)": v_tbv,
}


class CioValueRange(ValueRange):
    """ValueRange with two presentational changes made at the CIO gate (the arithmetic is the library's):
    (1) a zero scenario value prints price/value as n/m (report() divides the price by each value);
    (2) the line printed is the charter's Tier C net-net line (framework d6, d11), not base x (1 - margin): an earnings
        value is not private-owner value (d7), so the library's base-times-margin line does not apply to Lane C here.
        Under NO_THESIS it is a reference line, not a buy price (constitution checklist, "Recording the result"; CH-2)."""

    NAMES = ("worst_case", "conservative", "base", "optimistic")

    def buy_price(self) -> float:
        return NETNET_LINE

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
        text = re.sub(r"buy price \(\d+% of base\)\s{10}", "net-net reference line (no buy price)", text)
        return text.replace("price/buy price", "price/line")


vr = CioValueRange("Gilat Telecom Global (TASE 1080597), per share", "ILS", PRICE, f"{PRICE_DATE} close",
                   v_worst, v_cons, v_base, v_opt, margin, methods)
BUY = vr.buy_price()          # the net-net reference line; NO_THESIS sets no buy price
P("")
P("== 6. Margin of safety and the net-net reference line (no buy price: NO_THESIS)")
P(vr.report())
P(f"  data additions: {', '.join(DATA_FLAGS)} (+5 each, capped at +10); no endogenous add-back. The {margin.total_margin:.0%} Tier C margin would apply")
P("      to an EVIDENCED private-owner value (d7, d11); none exists, so it yields no line here.")
P("  the earlier 'shadow' line (40% of the EPV base) is WITHDRAWN (B-O2, A-O8): EPV is not private-owner value; it is not a buy price.")
P(f"  the charter's only Tier C line is the net-net route: <= 2/3 NCAV and <= Dempster (30.6.2026 balance sheet, one date; per 3.11.2026 listed"
  f" share: the price at which today's market cap equals it) = {fmt(BUY)}; per 30.6.2026 share {NETNET_LINE_30JUN:.3f}; price / line {PRICE / BUY:.1f};"
  f" pro forma 3.11.2026 {NETNET_LINE_PF:.3f}.")
P("      It is a reference line, NOT a buy price: under NO_THESIS no buy price is set (only a watchlist name, whose only failure is price,")
P("      gets a dated one). Before any Tier C line could become a buy price, Q1 must be answered yes (CIRCLE.md or an industry study) and")
P("      B3, B5, E1, F4, H2, H4 and H5, which fail at any price, must clear; D2, D5 and E3 also fail at today's price.")
asset_ps = {"NCAV 30.6.2026": NCAV * 1000 / SHARES_30JUN, "Dempster 30.6.2026": DEMPSTER * 1000 / SHARES_30JUN}
P(f"  method spread (A-O8): earnings methods + tangible book {vr.method_spread():.0%}; EPV vs NCAV {v_epv / asset_ps['NCAV 30.6.2026'] - 1:+.0%};"
  f" EPV vs Dempster {v_epv / asset_ps['Dempster 30.6.2026'] - 1:+.0%}. The >30% disagreement is resolved as follows (charter: resolve first):")
P(f"      (1) EPV / tangible book = {v_epv / v_tbv:.2f} because normalised NOPAT {OE_NORM:,.0f} on tangible equity {TBV_PF:,.0f} is {OE_NORM / TBV_PF:.1%} < r:")
P("          book is not earned, so a going-concern owner pays less than book (EPV governs the base);")
P(f"      (2) book is not realisable either: {DEFERRED_ST + DEFERRED_LT:,} of IRU prepayments and the DTA are soft (hard TBV {v_tbv_hard:.3f}),"
  f" and liquidation (Dempster) gives {asset_ps['Dempster 30.6.2026']:.3f};")
P("      (3) the lane's own test is the asset floor (NCAV, Dempster), which sits far below EPV. Every method is far below the price,")
P("          so no reading of the disagreement favours a purchase. Base = EPV; TBV is an upper reference, NCAV/Dempster the floor.")
SEG_NORM_AFTER_LEASE_INT = 15_099              # analyst segment normalisation, leases as operating costs (business.md §12; business_calcs_output §11): reference only
v_seg, _ = per_share(equity_bridge(epv_operations(unlevered_owner_earnings(SEG_NORM_AFTER_LEASE_INT, AMORT_ACQ, TAX, DEP_TTM, MAINT_TTM), R),
                                   excess_c=EXCESS, debt=IRU_EXP_BASE + FX_BRIDGE_ADJ))   # lease cost already charged there, so the lease liability is not deducted again
P(f"  reference only (not a charter method): the analyst's segment normalisation (business.md §12: {SEG_NORM_AFTER_LEASE_INT:,} after lease interest)"
  f" would give {fmt(v_seg)}; price / that value {PRICE / v_seg:.2f}. Re-checked (A-O11): its base uses segment revenues and FY2025 audited margins")
P("      (gilat_fy2025 p.181), not the inconsistent H1 2025 segment results; only its bull case uses the directors'-report ISP result.")

# =====================================================================================================
# 7. Liquidity, sizing and verdict
# =====================================================================================================
size = position_size(PRICE, v_worst, [(PROBS[k], VALS[k]) for k in PROBS], "C",
                     turnover_p25_daily=TURNOVER_P25_60, tase_room=0.30)
P("")
P("== 7. Liquidity, sizing and verdict")
P(f"  liquidity (60 sessions to 3.11.2026): median turnover {TURNOVER_MEDIAN_60:,} ILS (floor 50,000: passes; above 100,000: no price-reliability"
  f" block needed); 25th percentile {TURNOVER_P25_60:,} ILS; a year earlier the median was 211,291 (scuttle_calc_output §1)")
P(f"  e2 position_size(): full Kelly {size['kelly_full']:.1%}; L_worst {size['l_worst']:.0%}; limits "
  + ", ".join(f"{k} {v:.1%}" for k, v in size['limits'].items())
  + f"; liquidity maximum {size['liquidity_amount']:,.0f} ILS at cost (NAV unknown) -> size {size['size']:.1%} of NAV ({size['binding']})")
BB_JUNE = (2_300_000, 5_988)     # shares, ILS k incl. fees, 12-30.6.2026 (gilat_q2_2026_full p.49 note 7: average 260.36 agorot; p.39)
BB_OCT = (2_274_810, OCT_BUYBACK) # 7-21.10.2026 (market.md calc §3; UNVERIFIED vs Maya)
CONV_SHARES_H1_26 = 9_741_785 + 16_032_064   # shares issued on Series C (at 1.35) and Series D (at 1.00) conversion in H1 2026 (gilat_q2_2026_full p.49 note 7)
bb_px = {k: v[1] * 1000 / v[0] for k, v in (("June", BB_JUNE), ("October", BB_OCT))}
P("  B2 buybacks: " + "; ".join(f"{k} {px:.3f} ILS = {px / v_base:.1f}x base value, {px / v_pw:.1f}x probability-weighted" for k, px in bb_px.items())
  + f"; {BB_JUNE[0] + BB_OCT[0]:,} shares bought = {(BB_JUNE[0] + BB_OCT[0]) / CONV_SHARES_H1_26:.1%} of the {CONV_SHARES_H1_26:,} shares issued"
  " on conversion in H1 2026 at 1.00-1.35: bought above value, offsetting a fraction of the dilution")
SHARES_END_2022 = 58_438_636     # gilat_fy2023 p.151
share_multiple = SHARES_LISTED / SHARES_END_2022
share_cagr = share_multiple ** (1 / ((2026 + 307 / 365) - 2023.0)) - 1   # 31.12.2022 (= 2023.0) to 3.11.2026 (day 307): derived
P(f"  lane C (cyclical), tier C: A/B fail A3 (no moat in the numbers: operating losses FY2021-22, ROTC minimum {min(rotc_w):.0%}; competition")
P("      'focuses mainly on price and on the ability to provide the customer a total solution', share 'not material', gilat_fy2025 p.32);")
P("      D needs an A/B franchise; E has no deal. C is the only lane whose basis (assets, normalised earnings) could ever apply; today it is")
P(f"      not a C bargain: the asset value is not firm (H2), there is no catalyst or basket (H4), market cap {MCAP / NCAV:.1f}x NCAV, TTM EBIT_adj"
  f" {EBIT_ADJ_TTM / EBIT_NORM:.1f}x EBIT_norm (a peak), no evidenced private-owner value. No lane is satisfied today.")
P(f"  VETO items that fail: B3 (listed shares x{share_multiple:.2f} since 31.12.2022, {share_cagr:.0%} a year, issued at 0.30-1.35; Series D adds"
  f" {SERIES_D_PAR / SHARES_LISTED:.0%}), B5 (metrics and pay exclude the IRU cost; policy and charge irreconcilable), D1 (process: the price")
P("      was in the valuation brief before value was estimated, so 'before looking at the price' fails closed; CIO review of the")
P(f"      verification, as in the Paymeant study's C-1), D2 (price {PRICE / BUY:.0f}x the")
P(f"      net-net reference line), D5 (price/base {PRICE / v_base:.1f}, price/probability-weighted {PRICE / v_pw:.1f}), E1 (new money by {NEW_MONEY_YEAR} in the worst"
  " case), E3 (the discount to TTM is explained by known facts), F4 (shekel stress), H2 (asset value not firm), H4 (no catalyst,")
P("      no basket), H5 (no low-cost position; net debt once the IRU is counted). Open, failing closed: B7 (court and class-action databases")
P("      unread), D8 (Maya immediate reports unread), G2, G3 (fund data not available).")
P("  investment test: Q1 no (not in a written circle: CIRCLE.md unavailable; not predictable 5-10 years out, business.md §13);")
P(f"      Q2 no (Lane C: the asset value is not firm, H2, unpaid Bezeq consideration {IRU_UNPAID_ALL / NCAV:.1f}x NCAV; no catalyst or basket, H4;"
  " not burned, H3);")
P(f"      Q3 no (Tier C test: market cap {MCAP / NCAV:.1f}x NCAV and {MCAP / DEMPSTER:.1f}x Dempster, no evidenced private-owner value; price/EPV"
  f" {PRICE / v_base:.1f} as context);")
P(f"      Q4 the price implies {IG_NORM:+.1%} a year from normalised earnings, or {IG_TTM:+.1%} from TTM: it already pays for the war-era")
P("      earnings; the CEO told the market turnover reached 'about double the normal period' in the war (Bizportal 20014148; asked about")
P("      the defence activity, so company-wide or defence turnover: both readings in §5).")
P("  VERDICT: NO_THESIS (not WATCHLIST: price is not the only failure; B3, B5, E1, F4, H2, H4 and H5 fail at any price until the facts")
P("      change, D1 fails on process, and D2, D5 and E3 also fail at today's price).")
P("  falsification conditions (gate.md §3; dated, observable; the net-net line is a reference, not a buy price, and the withdrawn shadow")
P("  line must not be used):")
P("      1. by 31.1.2027: 2027 orders from Israeli defence and government customers reported in Dec 2026-Jan 2027 at least the ~ILS 110M")
P("         incl. VAT reported for 2026 (gilat_h1_2026 p.14) falsifies the peak premise (re-underwrite EBIT_norm); below half confirms it.")
P("      2. by 31.3.2027 (FY2026 report): the unpaid IRU consideration and its payment schedule are stated (or that pulse-1 tranches can be")
P("         declined), and the runway re-run here on the filed schedule keeps cash above two months' costs through 2031 with a zero core.")
P("      3. by 31.3.2027: Vodacom DRC (16% of 2025 revenue, gilat_fy2025 p.55) renewed for >= 24 months at >= USD 1M a month.")
P("  monitoring triggers (not falsification conditions):")
P("      a. quarterly: private ISP net additions below 3,000 a quarter for two consecutive quarters (gilat_h1_2026 p.8 reports 7,116 in H1 2026).")
P("      b. by 31.12.2026: renewal of the unified satellite, Iridium, trade and OneWeb licences that expire on that date (gilat_fy2025 p.69-72).")
P("      c. FY2026 report: the IRU amortisation applied, and whether the Bezeq commitment and LEO substitution appear as risk factors (B5).")

# =====================================================================================================
# 8. What the CIO gate and the final edit changed (previous run = output.txt before the gate; gate = output.txt as committed
#    at the gate, 3.11.2026; both quoted as inputs). The final edit changed no price, rate or date (verification.md).
# =====================================================================================================
PREV = {"EBIT_norm": 11_100, "worst": 0.0, "conservative": 0.3563, "base": 0.7888, "optimistic": 1.9215, "probability-weighted": 0.8283,
        "line (buy -> reference)": 0.3155, "implied growth (normalised)": 0.114, "sensitivity minimum": 0.614}
GATE = {"EBIT_norm": 7_643, "worst": 0.0, "conservative": 0.0, "base": 0.4281, "optimistic": 1.7177, "probability-weighted": 0.3644,
        "line (buy -> reference)": 0.0921, "implied growth (normalised)": 0.165, "sensitivity minimum": 0.2967}
NOW = {"EBIT_norm": EBIT_NORM, "worst": v_worst, "conservative": v_cons, "base": v_base, "optimistic": v_opt, "probability-weighted": v_pw,
       "line (buy -> reference)": BUY, "implied growth (normalised)": IG_NORM, "sensitivity minimum": grid["min"]}
P("")
P("== 8. Changes at the CIO gate and at the final edit (previous run -> gate -> now)")
for k in PREV:
    a, g, b = PREV[k], GATE[k], NOW[k]
    if k == "EBIT_norm":
        P(f"  {k:<30} {a:>10,.0f} -> {g:>10,.0f} -> {b:>10,.0f}")
    elif "growth" in k:
        P(f"  {k:<30} {a:>+10.1%} -> {g:>+10.1%} -> {b:>+10.1%}")
    else:
        P(f"  {k:<30} {a:>10.4f} -> {g:>10.4f} -> {b:>10.4f}" + ("   (previous: 'shadow' buy line, 40% of EPV, withdrawn; then the"
                                                                 " net-net reference line, not a buy price)" if k.startswith("line") else ""))
IRU_EXP_UNDATED = P_IRU_HALF_DEAD * LINES_UNFILLED / 2 * pv_iru2 / 1000 * (1 - TAX)       # the gate's undated expected cost
OE_NORM_GATE = unlevered_owner_earnings(EBIT_NORM, AMORT_ACQ, TAX, DEP_TTM, MAINT_TTM)      # the gate's add-back (809 a year)
v_gate_check = per_share(equity_value(OE_NORM_GATE, iru_cost=IRU_EXP_UNDATED))[0]
v_ar1_only = per_share(equity_value(OE_NORM, iru_cost=IRU_EXP_UNDATED))[0]
v_ar3_only = per_share(equity_value(OE_NORM_GATE))[0]
P(f"  final edit: Amort_acq matched to the W mean (AR-1), IRU dead-line PVs dated to 3.11.2026 (AR-3: expected cost {IRU_EXP_UNDATED:,.0f} at the gate"
  f" -> {IRU_EXP_BASE:,.0f}), FY2021 depreciation as filed (AR-2: C4 and the pre-war runway core)")
P(f"  base: gate {v_gate_check:.4f} -> AR-1 alone {v_ar1_only:.4f} (AR-3 alone {v_ar3_only:.4f}) -> both {v_base:.4f}")

P("")
P("Per-share summary (ILS, agorot, USD at 3.157):")
for label, v in (("price", PRICE), ("worst case", v_worst), ("conservative", v_cons), ("base", v_base),
                 ("optimistic", v_opt), ("probability-weighted (15/30/45/10)", v_pw), ("charter Tier C net-net line (not a buy price)", BUY)):  # per 3.11.2026 listed share
    P(f"  {label:<46}{fmt(v)}")
P(f"  implied growth (normalised OE, ten years)   {IG_NORM:+.1%};  on TTM OE {IG_TTM:+.1%}")
P(f"  Tier C margin {margin.total_margin:.0%} (applies only to an evidenced private-owner value); sensitivity minimum {grid['min']:.3f};"
  f" spread of earnings methods + TBV {vr.method_spread():.0%}")

if __name__ == "__main__":
    print("\n".join(out))
