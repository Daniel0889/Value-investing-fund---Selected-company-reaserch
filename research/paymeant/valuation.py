"""Paymeant Financial Technologies Ltd (פיימנט טכנולוגיות פיננסיות בע"מ), TASE 1180876.
Charter Revision 4 valuation, 3 November 2026, as revised at the CIO gate the same day.

Units: ILS thousands ("k") unless stated; per-share values in ILS, with agorot (1 ILS = 100 agorot), on a DILUTED
count (treasury method, instrument by instrument). The company reports in ILS, so no conversion is needed (USD/ILS
3.157 only shows the market cap in dollars). Price: official close of 3.11.2026, 317.3 agorot.

The business. A licensed non-bank consumer lender: point-of-sale instalment loans originated through merchants, held
before sale on on-call bank warehouse lines, and sold to banks and to the company's own unconsolidated SPCs. Its own
P&L puts funding cost and credit losses above operating profit (paymeant_fy2023 p.82), which is why Mega shows an 88%
"gross" and a 41% "operating" margin: they are a lender's margins after interest.

Charter sections applied (charter_rev4_draft.md "Text to paste" governs; framework.md, checklist.md,
small_investor_and_israel.md and screen_spec.md supply the formulas): the four-question investment test; the lanes and
the tier table with the capped data additions; capital preservation and the three impairment markers; framework (d)
d1-d11, (e2) and (h); screen_spec 2.2-2.3 (window, EBIT_adj, cyclical test), 3 (X5 liquidity floor) and 3.1/4.7
(routing of lenders, bank-route gates).

CIO GATE REVISION (3.11.2026). The red team (paymeant:redteam-accounting, paymeant:redteam-business) objected to
the first version. Accepted and implemented here:
  * EBIT_adj follows screen_spec 2.3: only the 1,188 termination gain of 2022 is removed (sign-aware). The IPO
    share-based pay of note 19e (288 / 751 / 228, and 1,997 of options vested at once) stays a cost, because
    stock compensation "is never added back" (framework d1). [B1]
  * The window W is the fiscal years FY2021-FY2025; TTM supplies only Rev_ttm (framework d2; screen_spec 2.2). [B3]
  * FY2021 is then an operating loss, so the business is cyclical (d2; screen_spec 2.3) and
    EBIT_norm = min(mean EBIT_adj, median EBIT_adj, mean revenue x m_norm). [B1]
  * Maintenance capex at the H1 2026 run-rate; base growth at CPI (2%); the growth record restated before net
    capitalisation. [B4]
  * Credit: framework f3 stress, provision coverage, the UNVERIFIED provision shortfall; the conservative case is
    tangible book at amortised cost less that shortfall (no moat: ROE converges on r). [B5, B8]
  * All four bank covenants and the change-of-control clause. [B6]
  * F4: a 2-point rise through the warehouse, the held book's fair value and the sale price. [B7]
  * The worst case as a range, sized off its low end. [B9]
  * Per-share values on a diluted count; the B3 dilution test. [B10]
  * The TTM cash figures are marked unreconciled and are not used as evidence. [B12]
  * No shadow buy price. Reference lines only (Tier C net-net line, bank-route line). [O6; B2 in part]
  * Liquidity from Bizportal's daily proceeds, the one primary series. [O11]
Rejected, with evidence printed below: B11 (the three-year tax reconciliation supports 23%; 24.5% is shown as a
sensitivity), and the part of B2 that calls the EV basis the charter-literal basis for a lender (screen_spec 3.1:
"EBIT, EV and ROIC [are] meaningless" for financials). The EV basis is still printed beside the lender basis.

Every input cites document id and PDF page (table figures checked on the page images) or is marked derived / assumed.
Market and scuttlebutt inputs cite work/paymeant/market.md and work/paymeant/scuttlebutt.md (with their calc files).
All valuation arithmetic runs through lib/charter_valuation.py.
Run: python3 -I research/paymeant/valuation.py > research/paymeant/output.txt
"""
from __future__ import annotations

import pathlib
import statistics
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "lib"))
import charter_valuation as cv  # noqa: E402

# =====================================================================================================
# 0. Dated market inputs
# =====================================================================================================
COMPANY = "Paymeant Financial Technologies (TASE 1180876), per diluted share"
PRICE = 3.173               # ILS: official close 3.11.2026, 317.3 ag [TM 17:24; BZ-GV] (market.md §0)
PRICE_DATE = "2026-11-03 close"
PRICE_MEGA = 3.18           # ILS: Mega "Ace" snapshot 3.11.2026 14:04 (brief); reconciliation only (market.md §1)
SHARES = 39_330_034         # registered for trading 3.11.2026 [BZ-GV]; Mega cap 125,069,508 / 3.18 = this exactly
SHARES_FY2025 = 39_245_034  # paymeant_fy2025 p.108 (note 17a), 31.12.2025
SHARES_FY2024 = 37_278_200  # paymeant_fy2025 p.108
SHARES_FY2023 = 37_021_525  # paymeant_fy2023 p.107 (note 17a, image checked)
SHARES_FY2022 = 36_890_750  # paymeant_fy2023 p.107
SHARES_FY2021 = 30_903_464  # derived: 36,890,750 - 4,852,476 (Aug-2022 placement) - 1,134,810 (2022 exercises),
                            # paymeant_fy2023 p.107-109 (work/paymeant/financials.json)
EXERCISES_2025 = (1_966_835, 2.02)   # shares issued on exercise in 2025 and their weighted strike (paymeant_fy2025 p.112)
FOUNDERS_EXERCISE_2022 = (985_000, 10)   # 1.3.2022: 985,000 shares for 10k ILS in total (paymeant_fy2023 p.107)
Y10_ILS = 0.0429            # Israel 10y on 3.11.2026: 4.29% YTM on ממשל שקלית 0537 [TM-0537]; generic 4.162% [TE]
USDILS = 3.157              # Bank of Israel representative rate 3.11.2026 (brief)
LIQ_FLOOR = 50_000          # ILS median daily turnover over 60 sessions (charter; screen_spec X5, a hard exclusion)
LIQ_RELIABILITY = 100_000   # ILS: below this the price-reliability block and the control section are mandatory

# 60 sessions to 3.11.2026, Bizportal's own daily series (the quote page's history call; on-exchange trades only):
# (date 2026, volume in shares, close in agorot as Bizportal adjusts it for dividends, proceeds in ILS).
# Saved as work/paymeant/scuttle/raw2/rt1_refetch.json (scuttlebutt.md [BZ-RT]); 3.11.2026 from the general view
# [BZ-GV]: 352,392 ILS, 111,691 shares. Checked against Bank Leumi's calendar: no session missing (scuttlebutt §7).
# This replaces the volume x close series of the first version, which missed the 12.10.2026 session (O11).
BZ_SESSIONS = [
    ("08-04", 11084, 570.3842, 63871), ("08-05", 2868, 568.4037, 16463), ("08-06", 30024, 558.2042, 169311), ("08-07", 8205, 554.1441, 45917),
    ("08-10", 2702, 566.4232, 15455), ("08-11", 17, 566.4232, 97), ("08-12", 14397, 546.1231, 79522), ("08-13", 4983, 558.2042, 28089),
    ("08-14", 256, 566.5223, 1471), ("08-17", 3385, 557.3129, 19051), ("08-18", 890, 567.8096, 5103), ("08-19", 4186, 556.0256, 23503),
    ("08-20", 111, 558.7983, 633), ("08-21", 8586, 543.0533, 47130), ("08-24", 7605, 528.3976, 40602), ("08-25", 1969, 531.8635, 10575),
    ("08-26", 42, 529.1898, 217), ("08-27", 1353, 519.2873, 7095), ("08-28", 109, 522.3571, 582), ("08-31", 5713, 523.4464, 30197),
    ("09-01", 9245, 518.0, 48360), ("09-02", 500, 521.0, 2605), ("09-03", 204, 526.2, 1083), ("09-04", 475, 536.1, 2546),
    ("09-07", 2870, 540.9, 15525), ("09-08", 10, 540.9, 54), ("09-09", 3839, 528.3, 20282), ("09-10", 189, 540.5, 1046),
    ("09-14", 1087, 542.0, 5891), ("09-15", 1581, 529.3, 8368), ("09-16", 15, 530.2, 83), ("09-17", 16115, 534.9, 84724),
    ("09-22", 4403, 516.8, 22753), ("09-23", 5048, 519.8, 26240), ("09-24", 31425, 508.0, 160156), ("09-28", 2269, 508.8, 11544),
    ("09-29", 6, 508.8, 31), ("09-30", 5625, 499.9, 28120), ("10-01", 196, 499.9, 980), ("10-05", 1061, 497.5, 5279),
    ("10-06", 1171, 497.9, 5830), ("10-07", 6151, 492.7, 30305), ("10-08", 2787, 481.1, 13409), ("10-09", 3, 481.1, 14),
    ("10-12", 4028, 476.6, 19199), ("10-13", 5373, 469.4, 25223), ("10-14", 221, 469.4, 1037), ("10-15", 841, 463.2, 3895),
    ("10-16", 4212, 471.7, 19866), ("10-19", 19, 471.8, 90), ("10-20", 15809, 459.5, 72640), ("10-21", 225098, 403.9, 918729),
    ("10-22", 96274, 390.4, 384014), ("10-23", 50595, 370.9, 189865), ("10-26", 226865, 308.2, 738950), ("10-28", 1742446, 251.0, 4601441),
    ("10-29", 815181, 315.9, 2405056), ("10-30", 78060, 324.9, 250722), ("11-02", 123374, 311.8, 389539), ("11-03", 111691, 317.3, 352392),
]

# =====================================================================================================
# 1. Income statement, ILS k (FY2021-FY2023 paymeant_fy2023 p.82; FY2024 paymeant_fy2024 p.81;
#    FY2025 paymeant_fy2025 p.83; H1 paymeant_h1_2026 p.24; overlapping columns agree on the images)
# =====================================================================================================
FY = ["FY2021", "FY2022", "FY2023", "FY2024", "FY2025"]
REV = {"FY2021": 7_850, "FY2022": 23_874, "FY2023": 38_524, "FY2024": 43_046, "FY2025": 56_616,
       "H1_2025": 24_827, "H1_2026": 28_512}
REV_Q1_2024, REV_Q2_2024 = 9_686, 8_776      # paymeant_fy2024 p.117 (Reg. 10A quarterly table)
NI_Q1_2024, NI_Q2_2024 = 2_702, 2_308        # paymeant_fy2024 p.117
FUND = {"FY2021": 90, "FY2022": 1_982, "FY2023": 7_750, "FY2024": 5_224, "FY2025": 4_711,  # funding cost, above
        "H1_2025": 1_477, "H1_2026": 2_738}                                               # operating profit
CREDIT_CHARGE = {"FY2025": 783, "H1_2025": 441, "H1_2026": 670}   # credit-loss charge (paymeant_h1_2026 p.24)
OPEX = {"FY2025": 27_350, "H1_2025": 12_637, "H1_2026": 14_144}   # S&M + R&D + G&A (paymeant_h1_2026 p.24)
OP = {"FY2021": 1_516, "FY2022": 8_295, "FY2023": 13_500, "FY2024": 17_216, "FY2025": 23_772,  # before other items
      "H1_2025": 10_272, "H1_2026": 10_960}
OTHER = {"FY2021": -2_285, "FY2022": 437, "FY2023": -228, "FY2024": 0, "FY2025": 0,  # note 19e, fy2023 p.111
         "H1_2025": 0, "H1_2026": 0}
# note 19e (paymeant_fy2023 p.111, image checked): IPO grant to senior officers and share-based payment 288 / 751 / 228;
# options vested immediately 1,997 (2021); income on ending the engagement with acquiring corporation A (1,188) in 2022.
SBP_IN_OTHER = {"FY2021": 288 + 1_997, "FY2022": 751, "FY2023": 228}
GAIN_TERMINATION = {"FY2022": 1_188}         # the only one-off screen_spec 2.3 removes (a settlement-type gain)
TAX = {"FY2021": 0, "FY2022": -77, "FY2023": 2_974, "FY2024": 3_925, "FY2025": 5_584, "H1_2025": 2_265,
       "H1_2026": 2_675}
NI = {"FY2021": -769, "FY2022": 8_809, "FY2023": 10_298, "FY2024": 13_291, "FY2025": 18_188, "H1_2025": 8_007,
      "H1_2026": 8_285}
EPS = {"FY2021": -0.03, "FY2022": 0.26, "FY2023": 0.28, "FY2024": 0.36, "FY2025": 0.47}   # reported basic EPS
T_STATUTORY = 0.23          # paymeant_fy2025 p.106 (statutory 23% in 2023-2025)
TAX_OTHER = {"FY2023": -79, "FY2024": -35, "FY2025": 116}   # "other" line of the reconciliation, fy2025 p.106
# revenue by source (paymeant_h1_2026 p.32, note 4, image checked): fees; loan sales + fair-value changes
FEES = {"FY2025": 27_278, "H1_2025": 11_154, "H1_2026": 15_699}
SALE_FV = {"FY2025": 16_301, "H1_2025": 8_575, "H1_2026": 6_068}
ORIG = {"FY2023": 365_000, "FY2024": 389_000, "FY2025": 535_000,   # originations, ILS k (paymeant_fy2025 p.42)
        "H1_2026": 258_000, "H1_2025": 240_000}                    # H1: 258M, +18M y/y (paymeant_h1_2026 p.15)
SOLD_SHARE_2025 = 0.60      # share of 2025 credit sold to buyers (paymeant_fy2025 p.42)
DURATION_MONTHS = 14        # average duration (מח"מ) of 2025 loans, months (paymeant_fy2025 p.42)
RATE_NOMINAL = {"FY2023": 0.0983, "FY2024": 0.0859, "FY2025": 0.0796}   # average nominal rate (paymeant_fy2025 p.42)

# =====================================================================================================
# 2. Cash flow, ILS k (FY2023-FY2025 paymeant_fy2025 p.85; H1 paymeant_h1_2026 p.28, image checked)
# =====================================================================================================
DA = {"FY2023": 944, "FY2024": 2_140, "FY2025": 3_194, "H1_2025": 1_470, "H1_2026": 1_554}
SBC = {"FY2023": 750, "FY2024": 78, "FY2025": 816, "H1_2025": 411, "H1_2026": 336}
OCF = {"FY2023": -5_296, "FY2024": 3_910, "FY2025": 2_785, "H1_2025": -4_942, "H1_2026": 5_236}
CAPEX_PPE = {"FY2023": 116, "FY2024": 128, "FY2025": 559, "H1_2025": 266, "H1_2026": 28}
CAPEX_DEV_CASH = {"FY2023": 2_789, "FY2024": 2_211, "FY2025": 1_167, "H1_2025": 642, "H1_2026": 1_902}
CAPEX_DEV_SBP = {"FY2023": 104, "FY2024": 145, "FY2025": 112, "H1_2025": 55, "H1_2026": 92}
CAPEX_ROU = {"FY2023": 0, "FY2024": 0, "FY2025": 25, "H1_2025": 25, "H1_2026": 0}
LEASE_PRIN = {"FY2023": 520, "FY2024": 575, "FY2025": 1_017, "H1_2025": 466, "H1_2026": 368}
DIVIDENDS = {"FY2025": 9_000, "H1_2025": 4_000, "H1_2026": 4_000}
TAX_PAID = {"FY2025": 7_124, "H1_2025": 0, "H1_2026": 3_758}       # paymeant_h1_2026 p.28: H1 2025 shows none
BANK_CF = {"FY2025": 21_831, "H1_2025": -19_060, "H1_2026": 10_985}  # change in bank credit inside OCF (h1 p.28)
# true sales to the company's own unconsolidated SPCs, ILS k, by completion (paymeant_fy2025 p.106-108;
# paymeant_h1_2026 p.6-7; governance_risk.md §4); a further ~100M assignment of 23.9.2026 is a headline only
SPC_SALES = {"2023-06": 60_000, "2024-02": 90_000, "2024-09": 85_000, "2025-01": 80_000, "2025-03": 60_000,
             "2025-10": 84_000, "2026-02": 80_000}
# capitalised development (note 10: paymeant_fy2023 p.98, paymeant_fy2025 p.98, images checked; H1 from p.28)
DEV_ADD = {"FY2022": 2_377, "FY2023": 2_892, "FY2024": 2_356, "FY2025": 1_279,
           "H1_2025": 642 + 55, "H1_2026": 1_902 + 92}
DEV_AMORT = {"FY2022": 127, "FY2023": 226, "FY2024": 1_373, "FY2025": 1_892}
CTRL_PAY_CAPITALISED = {"FY2023": 1_363, "FY2024": 751, "FY2025": 500}   # note 21b, paymeant_fy2025 p.115

# =====================================================================================================
# 3. Balance sheets, ILS k (consolidated). 31.12.2022: paymeant_fy2023 p.81; 31.12.2023 (restated) and
#    31.12.2024: paymeant_fy2024 p.80; 31.12.2025: paymeant_fy2025 p.82; 30.6.2025 and 30.6.2026:
#    paymeant_h1_2026 p.23 (image checked). 31.12.2021: no balance sheet in the documents.
# =====================================================================================================
D21, D22, D23, D24, D25, J25, J26 = ("2021-12-31", "2022-12-31", "2023-12-31", "2024-12-31", "2025-12-31",
                                     "2025-06-30", "2026-06-30")
CASH = {D22: 31_411, D23: 16_922, D24: 10_920, D25: 5_938, J25: 4_581, J26: 4_877}
LOANS_FV = {D22: 124_860, D23: 156_490, D24: 141_714, D25: 186_696, J25: 131_460, J26: 203_167}
LOANS_FV_AT_COST_J26 = 193_652      # the same book at amortised cost (paymeant_h1_2026 p.31, image checked)
FV_UPLIFT_J26 = 9_515               # fair-value step-up (paymeant_h1_2026 p.31)
LOANS_AC = {D22: 325 + 432, D23: 720 + 1_473, D24: 402 + 626, D25: 2_570 + 2_227, J25: 2_213 + 2_020,
            J26: 3_632 + 3_054}
RECV = {D22: 290 + 468, D23: 1_780 + 702, D24: 2_480 + 1_265, D25: 2_732 + 2_313, J25: 3_491 + 1_184,
        J26: 3_658 + 2_217}         # mostly income receivable from assignments and SPC deferred consideration
PPE = {D21: 88, D22: 396, D23: 386, D24: 353, D25: 738, J25: 543, J26: 677}
ROU = {D21: 482, D22: 1_348, D23: 932, D24: 883, D25: 2_671, J25: 2_950, J26: 2_392}
INTANG = {D22: 4_271, D23: 6_937, D24: 7_920, D25: 7_307, J25: 7_757, J26: 8_269}
CURRENT_ASSETS_J26 = 215_334
TOTAL_ASSETS = {D21: 32_944, D22: 163_878, D23: 186_342, D24: 166_563, D25: 213_192, J25: 156_199, J26: 231_943}
BANK = {D22: 101_245 + 23, D23: 114_892, D24: 82_410, D25: 104_241, J25: 63_350, J26: 115_225}
PAY_CT = {D22: 3_256, D23: 3_650, D24: 5_133, D25: 14_146, J25: 8_487, J26: 19_273}
OP_PAYABLES = {D22: 450 + 1_422, D23: 222 + 2_158 + 1_459, D24: 111 + 3_068 + 5_707, D25: 590 + 3_925 + 4_054,
               J25: 314 + 1_970 + 1_066, J26: 858 + 2_883 + 2_279}
LEASES = {D22: 610 + 686, D23: 511 + 443, D24: 610 + 326, D25: 781 + 2_027, J25: 897 + 2_148, J26: 781 + 1_813}
EQUITY = {D21: 22_163, D22: 56_186, D23: 61_569, D24: 68_081, D25: 82_198, J25: 76_556, J26: 86_912}
NCI = 0
PREFERRED = 0

# =====================================================================================================
# 4. Other filed facts used by the tests
# =====================================================================================================
# bank covenants, note 11a(6) (paymeant_fy2025 p.99, image checked; repeated paymeant_h1_2026 p.18, p.33)
COV_TE_RATIO = 0.20         # tangible equity >= 20% of the (tangible) balance sheet
COV_TE_MIN = 25_000         # tangible equity >= 25M
COV_SENIOR_DEBT = 0.80      # senior financial debt <= 80% of loans to customers
COV_NI_MIN = 1_000          # annual net profit >= 1M
TE_COMPANY_J26 = 76_000     # the company's own covenant "tangible equity" (paymeant_h1_2026 p.18)
# The same note restricts changes of control of the company and of its controlling holders and lists grounds for
# immediate repayment (paymeant_fy2025 p.99). The controllers' voting agreement lasts while they hold > 25%
# (paymeant_fy2025 p.123).
FOUNDERS_SHARES = 11_617_267  # Gilor 6,907,886 + Yochanan 4,709,381 (Globes / Bizportal registers 3.11.2026;
                              # scuttlebutt.md §5, scuttle_calc §2)
CTRL_FLOOR = 0.25
RATE_SENS_1PT = 1_152       # pre-tax cost of +1 point on the 115,225 bank credit (paymeant_h1_2026 p.9)
CPI_SENS_1PT = 1_981        # fair value of loans held for sale per 1 point of CPI (paymeant_h1_2026 p.8)
LINES_TOTAL = 340_000       # four on-call lines, 31.12.2025 (paymeant_fy2025 p.49, image checked)
DRAWN = {"A": 0, "B": 92_000, "C": 1_000, "D": 11_000}     # paymeant_fy2025 p.49 (lines less unused amounts)
ARREARS = {D25: {"current": 186_422, "1-90 days": 3_590, "default": 1_481},    # paymeant_fy2025 p.66
           J26: {"current": 200_260, "1-90 days": 5_198, "default": 4_395}}    # paymeant_h1_2026 p.15
PROVISION_AC = {D24: (2_859, 1_831), D25: (5_731, 934)}   # amortised-cost book (gross, provision), fy2025 p.95
# options and RSUs (treasury method, instrument by instrument; B10)
OPTIONS = [  # (instrument, number, strike ILS, source)
    ("founders' options, 15.1.2025", 1_000_000, 3.01, "paymeant_fy2025 p.111"),
    ("employee options 6.4.2025, less 100,040 forfeited", 519_000 - 100_040, 3.97, "paymeant_fy2025 p.111-112"),
    ("Amitim warrants, second tranche, to 12.1.2027", 255_000, 6.05, "paymeant_fy2025 p.108-109"),
    ("employee options at 0.01 (313,000 + 75,000 granted; 257,475 + 46,835 exercised)",
     313_000 + 75_000 - 257_475 - 46_835, 0.01, "paymeant_fy2025 p.109, p.110, p.112"),
    ("restricted share units (all counted; some converted after 1.4.2026: conservative)", 175_000, 0.0,
     "paymeant_fy2025 p.110"),
    ("options granted 20.8.2026", 512_000, 5.74, "paymeant_h1_2026 p.33"),
]
NOTE17_OPTIONS, NOTE17_STRIKE = 2_189_875, 4.02    # 31.12.2025 (paymeant_fy2025 p.112); Reg. 24A shows 1,136,125 (p.123)
AMITIM_TRANCHE1 = (255_000, 6.05)                  # expired 24.7.2026, out of the money (market.md §1)
# peers and holders (Tier 2, read 3.11.2026; scuttlebutt.md §1.2 and §6, scuttle_calc §3-§5)
PEER_PE_MEDIAN, PEER_PB_MEDIAN = 7.67, 1.37        # profitable Israeli specialist lenders, TTM
FOUNDERS_SALE = (869_564, 6.90, "13.3.2026")       # Globes interested-party register (one source)
# business workstream's through-cycle normalisation, pre-tax (business.md §12): 3.74% x 553M
BUSINESS_NORM_PRETAX = 20_679

# =====================================================================================================
# 5. Assumptions (each explained in work/paymeant/valuation_notes.md and work/paymeant/gate.md)
# =====================================================================================================
G_BASE = 0.02               # assumed: CPI-level nominal growth (the midpoint of the Bank of Israel's 1-3% target)
G_OPT = 0.05                # assumed: the first version's base growth, kept for the optimistic case only
SCENARIO_P = {"worst": 0.15, "conservative": 0.25, "base": 0.40, "optimistic": 0.20}  # assumed, uncalibrated
RECOVERY_DEFAULT = 0.30     # assumed recovery on defaulted loans in a run-off (worst case, low end)
RECOVERY_RECV = 0.50        # assumed: receivables that are mostly SPC deferred consideration and accrued income
WIND_DOWN_YEARS, WIND_DOWN_OPEX_SHARE = 0.5, 0.5   # assumed: six months of half the TTM opex
COVERAGE_TESTS = (0.50, 0.70)                      # provision coverage on defaulted loans (B5, UNVERIFIED location)
SEVERITY_F3 = 0.60          # loss severity in Buffett's bank stress test (framework f3)
RATE_SHOCK = 0.02           # F4: +2 points
REPRICE_LAG_YEARS = 0.5     # assumed: new-loan pricing catches up in six months (the company repriced in 2023, p.42)
HELD_DURATION_LOW_M = 7     # assumed lower bound for the held book's remaining duration, months
DATA_FLAGS = ["cycle_window_short", "derived_tier2_field", "microcap_field_unavailable"]


# =====================================================================================================
# helpers (no valuation arithmetic here: dilution, per-share conversion and formatting)
# =====================================================================================================
def ttm(d: dict) -> float:
    """TTM to 30.6.2026 = FY2025 + H1 2026 - H1 2025 (screen_spec X6 for semi-annual reporters)."""
    return d["FY2025"] + d["H1_2026"] - d["H1_2025"]


def residual_note17() -> tuple[float, float]:
    """Note-17 options not identified instrument by instrument, and their implied strike (derived)."""
    known = [o for o in OPTIONS if o[2] > 0 and "20.8.2026" not in o[0]]       # in note 17 at 31.12.2025
    n_known = sum(o[1] for o in known) + AMITIM_TRANCHE1[0]
    v_known = sum(o[1] * o[2] for o in known) + AMITIM_TRANCHE1[0] * AMITIM_TRANCHE1[1]
    n_res = NOTE17_OPTIONS - n_known
    return n_res, (NOTE17_OPTIONS * NOTE17_STRIKE - v_known) / n_res


RES_N, RES_K = residual_note17()
INSTRUMENTS = [(o[1], o[2]) for o in OPTIONS] + [(RES_N, RES_K)]


def dilutive_shares(v: float) -> float:
    """Treasury method at a per-share value v: sum of n x max(0, 1 - strike / v)."""
    if v <= 0:
        return 0.0
    return sum(n * max(0.0, 1 - k / v) for n, k in INSTRUMENTS)


def ps(x_k: float) -> float:
    """ILS thousands of equity -> ILS per diluted share (treasury method, iterated to a fixed point)."""
    v = x_k * 1000 / SHARES
    for _ in range(20):
        v = x_k * 1000 / (SHARES + dilutive_shares(v))
    return v


def money(x_ps: float) -> str:
    return f"{x_ps:6.2f} ILS ({x_ps * 100:5.0f} ag)"


def fmt_d(d: dict) -> str:
    """{'FY2023': 1363, ...} -> 'FY2023 1,363; ...' (formatting only)."""
    return "; ".join(f"{k} {v:,.0f}" for k, v in d.items())


def pct(x: float) -> str:
    return f"{x * 100:6.1f}%"


def tangible_operating_capital(d: str) -> float:
    """Loan book + receivables + PP&E + ROU - non-interest-bearing operating payables (the lender's ROTC capital)."""
    return LOANS_FV[d] + LOANS_AC[d] + RECV[d] + PPE[d] + ROU[d] - PAY_CT[d] - OP_PAYABLES[d]


def total_liabilities(d: str) -> float:
    return TOTAL_ASSETS[d] - EQUITY[d]


# =====================================================================================================
# computations
# =====================================================================================================
R = cv.hurdle(Y10_ILS)
MCAP = PRICE * SHARES / 1000                                   # ILS k, basic shares
for dct in (REV, FUND, OP, OTHER, TAX, NI, CREDIT_CHARGE, OPEX, FEES, SALE_FV, ORIG):
    dct["TTM"] = ttm(dct)
for dct in (DA, SBC, OCF, CAPEX_PPE, CAPEX_DEV_CASH, CAPEX_DEV_SBP, CAPEX_ROU, LEASE_PRIN, DIVIDENDS, TAX_PAID, DEV_ADD):
    dct["TTM"] = ttm(dct)
PERIODS = FY + ["H1_2025", "H1_2026", "TTM"]
PBT = {p: OP[p] + OTHER[p] for p in PERIODS}
EBIT_ADJ = {p: PBT[p] - GAIN_TERMINATION.get(p, 0) for p in PERIODS}     # screen_spec 2.3, lender basis
EBIT_ADJ_V1 = {p: OP[p] for p in PERIODS}                                  # first version: all of note 19e removed
EBIT_UNL = {p: EBIT_ADJ[p] + FUND[p] for p in PERIODS}                     # before funding cost (EV basis)
REV_TTM_PRIOR = REV["FY2024"] + REV["H1_2025"] - (REV_Q1_2024 + REV_Q2_2024)
TE_J26 = cv.tangible_book(EQUITY[J26], 0, INTANG[J26])                     # no goodwill
TL_J26 = total_liabilities(J26)
NET_DEBT_LEASES = BANK[J26] + LEASES[J26] - CASH[J26]
LOAN_BOOK_J26 = LOANS_FV[J26] + LOANS_AC[J26]

out = []
p = out.append

p("PAYMEANT FINANCIAL TECHNOLOGIES LTD (TASE 1180876) - CHARTER REV 4 VALUATION, 3.11.2026, CIO GATE REVISION")
p("ILS thousands unless stated; per-share values in ILS per DILUTED share (agorot in brackets). Lender (equity) basis")
p("primary for a lender (screen_spec 3.1, 4.7); the EV basis of framework d3 as written is printed beside it.")
p("")
p("== 0. Market inputs")
p(f"  price {PRICE:.3f} ILS ({PRICE * 100:.1f} ag), {PRICE_DATE}; Mega snapshot {PRICE_MEGA:.2f} at 14:04")
p(f"  shares {SHARES:,} basic (31.12.2025 filed: {SHARES_FY2025:,}); market cap {MCAP:,.0f}k ILS = USD"
  f" {MCAP / USDILS / 1000:,.1f}M at {USDILS}; dilutive shares at the price {dilutive_shares(PRICE):,.0f}"
  f" ({dilutive_shares(PRICE) / SHARES:.2%})")
p(f"  hurdle r = max(10%, y10 {Y10_ILS:.2%} on 3.11.2026 + 3 points) = {R:.0%}")
p(f"  P/E TTM {MCAP / NI['TTM']:.2f}; P/B {MCAP / EQUITY[J26]:.2f}; P/TBV {MCAP / TE_J26:.2f}; tangible equity"
  f" {TE_J26:,.0f}k")

# ---------------------------------------------------------------------------- 1. lane and tier evidence
p("")
p("== 1. Lane and tier evidence")
p("  1a. Pre-tax return on tangible operating capital, UNLEVERED: (EBIT_adj + funding cost) / (loan book + receivables")
p("      + PP&E + ROU - operating payables). EBIT_adj per screen_spec 2.3 (stock pay a cost). FY2021: no balance sheet.")
ends = {"FY2022": D22, "FY2023": D23, "FY2024": D24, "FY2025": D25, "TTM": J26}
starts = {"FY2023": D22, "FY2024": D23, "FY2025": D24, "TTM": J25}
rotc_ye, rotc_avg, rote_ye = {}, {}, {}
for per, d in ends.items():
    cap = tangible_operating_capital(d)
    rotc_ye[per] = EBIT_UNL[per] / cap
    line = f"      {per:<7} EBIT_unl {EBIT_UNL[per]:>7,} capital {cap:>9,.0f}  year-end {pct(rotc_ye[per])}"
    if per in starts:
        avg_cap = (tangible_operating_capital(starts[per]) + cap) / 2
        rotc_avg[per] = EBIT_UNL[per] / avg_cap
        line += f"  on average capital {pct(rotc_avg[per])}"
    rote_ye[per] = EBIT_ADJ[per] / cv.tangible_book(EQUITY[d], 0, INTANG[d])
    line += f"  | pre-tax RoTE {pct(rote_ye[per])}"
    p(line)
p(f"      unlevered ROTC: median year-end {pct(statistics.median(rotc_ye.values()))}, minimum {pct(min(rotc_ye.values()))};"
  f" median on average capital {pct(statistics.median(rotc_avg.values()))}, minimum {pct(min(rotc_avg.values()))}")
p(f"      bank lens, pre-tax return on tangible equity: median {pct(statistics.median(rote_ye.values()))},"
  f" minimum {pct(min(rote_ye.values()))} (levered: equity is {EQUITY[J26] / TOTAL_ASSETS[J26]:.1%} of assets)")
p("      tier test: A needs median >= 20% and never < 10%; B is 12-20%. Unlevered returns sit in B's band only, and the")
p("      TTM return on equity is a single benign-credit reading (no credit cycle in the window).")
p("  1b. Leverage (30.6.2026)")
p(f"      bank credit {BANK[J26]:,} (on-call, all due within a year) + leases {LEASES[J26]:,} - cash {CASH[J26]:,}"
  f" = net debt with leases {NET_DEBT_LEASES:,}")
n_base_pre = cv.normalised_ebit(REV["TTM"], [EBIT_ADJ[x] for x in FY], [REV[x] for x in FY])
n_unl_pre = cv.normalised_ebit(REV["TTM"], [EBIT_UNL[x] for x in FY], [REV[x] for x in FY])
p(f"      net debt with leases / normalised EBIT: {NET_DEBT_LEASES / n_base_pre.ebit_norm:.1f}x after funding cost"
  f" (EBIT_norm {n_base_pre.ebit_norm:,.0f}), {NET_DEBT_LEASES / n_unl_pre.ebit_norm:.1f}x before it"
  f" ({n_unl_pre.ebit_norm:,.0f}); Tier A allows 1x, Tier B 2x (C2)")
p(f"      bank credit / equity {BANK[J26] / EQUITY[J26]:.2f}x; drawn 31.12.2025 {sum(DRAWN.values()):,} of {LINES_TOTAL:,}"
  f" of lines; bank B {DRAWN['B'] / sum(DRAWN.values()):.1%} of drawn; lines A and D unused"
  f" {LINES_TOTAL - sum(DRAWN.values()) - (100_000 - DRAWN['B']) - (40_000 - DRAWN['C']):,}")
p(f"      interest cover TTM (EBIT before funding / funding cost) {EBIT_UNL['TTM'] / FUND['TTM']:.1f}x (C2 needs >= 8x);"
  f" FY2022 stress year {EBIT_UNL['FY2022'] / FUND['FY2022']:.1f}x; FY2020 not in the documents (C6)")
spc_since_2025 = sum(v for k, v in SPC_SALES.items() if k >= "2025")
p(f"      SPC debt consolidated: cannot be computed. The SPCs' bank borrowings and outstanding pools are not disclosed"
  f" (paymeant_fy2025 p.94, p.106-108).")
p(f"      Sold to them since 6.2023 {sum(SPC_SALES.values()):,}; since 1.2025 {spc_since_2025:,} ="
  f" {spc_since_2025 / (LOANS_FV[J26] + LOANS_AC[J26]):.2f}x the on-balance-sheet book (indemnities attach to these pools).")

# ---------------------------------------------------------------------------- 2. normalisation and owner earnings
p("")
p("== 2. Normalised earnings (d2), owner earnings (d1), tax, capitalisation, cash")
p("  EBIT_adj (screen_spec 2.3, lender basis) = pre-tax profit less the 1,188 termination gain of 2022; the IPO")
p(f"  share-based pay of note 19e stays a cost ({fmt_d(SBP_IN_OTHER)}; framework d1: never added back)")
p("  " + "  ".join(f"{x} {EBIT_ADJ[x]:,} ({EBIT_ADJ[x] / REV[x]:.1%})" for x in FY) + f"  | TTM {EBIT_ADJ['TTM']:,}")
n_base = cv.normalised_ebit(REV["TTM"], [EBIT_ADJ[x] for x in FY], [REV[x] for x in FY])
sd = statistics.stdev(n_base.detail["margins"])
p(f"  window W = FY2021-FY2025 (fiscal years; TTM supplies Rev_ttm only). m_norm {n_base.m_norm:.2%}; stdev {sd:.2%}"
  f" vs half the median {0.5 * n_base.m_norm:.2%}; operating loss in FY2021 -> cyclical: {n_base.cyclical}")
p(f"  EBIT_norm (cyclical) = min(mean {n_base.detail['mean_ebit_adj']:,.0f}, median {n_base.detail['median_ebit_adj']:,.0f},"
  f" mean revenue x m_norm {n_base.detail['mean_rev_x_m_norm']:,.0f}) = {n_base.ebit_norm:,.0f}")
p(f"      TTM EBIT_adj {EBIT_ADJ['TTM']:,} = {EBIT_ADJ['TTM'] / n_base.ebit_norm:.2f}x EBIT_norm: screen_spec flag"
  f" ttm_above_norm (> 1.5x, possible peak): {EBIT_ADJ['TTM'] > 1.5 * n_base.ebit_norm}")
p("      reading: the formula is conservative partly for the wrong reason (the window holds the 2021-2022 start-up scale,")
p("      not a credit cycle); the real cyclical risk, a credit cycle, is in no window statistic. It is the charter's rule")
p("      for a cyclical and it is used. The alternatives are printed so the effect of each choice is visible:")
n_opt = cv.normalised_ebit(REV["TTM"], [EBIT_ADJ[x] for x in FY], [REV[x] for x in FY], force_cyclical=False)
n_v1 = cv.normalised_ebit(REV["TTM"], [EBIT_ADJ_V1[x] for x in FY + ["TTM"]], [REV[x] for x in FY + ["TTM"]])
n_v1fy = cv.normalised_ebit(REV["TTM"], [EBIT_ADJ_V1[x] for x in FY], [REV[x] for x in FY])
n_w6 = cv.normalised_ebit(REV["TTM"], [EBIT_ADJ[x] for x in FY + ["TTM"]], [REV[x] for x in FY + ["TTM"]])
for lab, n in (("first version: note 19e removed, W = FY + TTM (stable)", n_v1),
               ("note 19e removed, fiscal years (stable)", n_v1fy),
               ("screen_spec EBIT_adj, W = FY + TTM (cyclical)", n_w6),
               ("ADOPTED: screen_spec EBIT_adj, fiscal years (cyclical)", n_base),
               ("optimistic input: same, FY2021 loss read as start-up (stable)", n_opt)):
    p(f"      {lab:<64} m_norm {n.m_norm:6.2%} cyclical {str(n.cyclical):5} EBIT_norm {n.ebit_norm:7,.0f}")
p(f"      cross-check: business workstream through-cycle pre-tax (3.74% of 553M originations) {BUSINESS_NORM_PRETAX:,}")

eff = {per: TAX[per] / PBT[per] for per in ("FY2023", "FY2024", "FY2025", "TTM")}
cum3 = sum(TAX[x] for x in ("FY2023", "FY2024", "FY2025")) / sum(PBT[x] for x in ("FY2023", "FY2024", "FY2025"))
p(f"  tax: statutory {T_STATUTORY:.0%} used (B11 rejected). Reconciliation 'other' ({fmt_d(TAX_OTHER)}) alternates in sign; cumulative"
  f" FY2023-FY2025 effective rate {cum3:.2%}; yearly " + ", ".join(f"{k} {v:.1%}" for k, v in eff.items()))

capex_ttm = CAPEX_PPE["TTM"] + CAPEX_DEV_CASH["TTM"] + CAPEX_DEV_SBP["TTM"] + CAPEX_ROU["TTM"]
capex_run = 2 * (CAPEX_PPE["H1_2026"] + CAPEX_DEV_CASH["H1_2026"] + CAPEX_DEV_SBP["H1_2026"] + CAPEX_ROU["H1_2026"])
netppe_to_rev = sum(PPE[d] + ROU[d] for d in (D21, D22, D23, D24, D25)) / sum(REV[x] for x in FY)
g_capex = cv.growth_capex(netppe_to_rev, REV["TTM"] - REV_TTM_PRIOR)
maint_v1 = cv.maintenance_capex(capex_ttm, DA["TTM"], netppe_to_rev, REV["TTM"] - REV_TTM_PRIOR)
maint = cv.maintenance_capex(capex_run, DA["TTM"], netppe_to_rev, REV["TTM"] - REV_TTM_PRIOR)
p(f"  maintenance capex: H1 2026 run-rate capex {capex_run:,} (TTM {capex_ttm:,}) - growth part {g_capex:,.0f}, floor D&A"
  f" {DA['TTM']:,} -> {maint:,.0f} (first version {maint_v1:,.0f}; B4)")
ni_norm = n_base.ebit_norm * (1 - T_STATUTORY)            # no finance line below operating profit for this lender
oe_norm = cv.owner_earnings(ni_norm, DA["TTM"], 0, 0, maint, 0)
oe_ttm = cv.owner_earnings(NI["TTM"], DA["TTM"], 0, 0, maint, 0)
oe_opt = cv.owner_earnings(n_opt.ebit_norm * (1 - T_STATUTORY), DA["TTM"], 0, 0, maint, 0)
oe_v1 = cv.owner_earnings(n_v1.ebit_norm * (1 - T_STATUTORY), DA["TTM"], 0, 0, maint_v1, 0)
p(f"  owner earnings (d1), lender basis: OE_norm = EBIT_norm x (1 - t) + D&A - maintenance = {oe_norm:,.0f};"
  f" TTM {oe_ttm:,.0f}; optimistic input {oe_opt:,.0f}; first version {oe_v1:,.0f}")
p("      (SBC stays expensed; the D&A floor charges ROU depreciation, so leases stay an operating cost; dWC_maint = 0.)")

net_cap = {k: DEV_ADD[k] - DEV_AMORT[k] for k in DEV_AMORT}
amort_h1_25 = INTANG[D24] + DEV_ADD["H1_2025"] - INTANG[J25]
amort_h1_26 = INTANG[D25] + DEV_ADD["H1_2026"] - INTANG[J26]
net_cap["H1_2025"] = DEV_ADD["H1_2025"] - amort_h1_25
net_cap["H1_2026"] = DEV_ADD["H1_2026"] - amort_h1_26
net_cap["TTM"] = ttm(net_cap)
h1_rep = PBT["H1_2026"] / PBT["H1_2025"] - 1
h1_und = (PBT["H1_2026"] - net_cap["H1_2026"]) / (PBT["H1_2025"] - net_cap["H1_2025"]) - 1
cap_share = {k: DEV_ADD[k] / (rd + DEV_ADD[k]) for k, rd in (("H1_2025", 4_177), ("H1_2026", 3_950))}  # R&D, h1 p.24
p(f"  capitalised development (B4): net capitalisation (additions - amortisation): {fmt_d(net_cap)}")
p(f"      H1 pre-tax growth reported {h1_rep:+.1%}; before net capitalisation {h1_und:+.1%}; capitalised share of gross R&D"
  f" H1 2025 {cap_share['H1_2025']:.0%} -> H1 2026 {cap_share['H1_2026']:.0%}; controllers' pay capitalised"
  f" {fmt_d(CTRL_PAY_CAPITALISED)} (fy2025 p.115)")
ps_rep = {y: NI[y] / s for y, s in (("FY2022", SHARES_FY2022), ("FY2025", SHARES_FY2025))}
ps_bnc = {y: (NI[y] - net_cap[y] * (1 - T_STATUTORY)) / s for y, s in (("FY2022", SHARES_FY2022),
                                                                        ("FY2025", SHARES_FY2025))}
eps_start = statistics.mean(EPS[x] for x in ("FY2021", "FY2022", "FY2023"))
eps_end = statistics.mean(EPS[x] for x in ("FY2023", "FY2024", "FY2025"))
g_hist = (eps_end / eps_start) ** (1 / 2) - 1
p(f"      growth record: reported EPS, 3-year averages {eps_start:.3f} -> {eps_end:.3f}: {g_hist:.1%} a year (from a")
p(f"      start-up base); NI per period-end share FY2022 -> FY2025 {(ps_rep['FY2025'] / ps_rep['FY2022']) ** (1 / 3) - 1:+.1%}"
  f" a year reported, {(ps_bnc['FY2025'] / ps_bnc['FY2022']) ** (1 / 3) - 1:+.1%} before net capitalisation (capitalisation"
  f" fell over FY2022-FY2025, so the annual record is not flattered by it; the latest half is)")
p(f"      H1 2026 pre-tax annualised {2 * PBT['H1_2026']:,} = {2 * PBT['H1_2026'] / PBT['TTM'] - 1:+.1%} vs TTM {PBT['TTM']:,}")

d_bank = BANK[J26] - BANK[J25]
d_book = LOAN_BOOK_J26 - (LOANS_FV[J25] + LOANS_AC[J25])
d_payct = PAY_CT[J26] - PAY_CT[J25]
ocf_adj_ttm = OCF["TTM"] - d_bank + d_book - d_payct
cash_adj = cv.owner_earnings_cash(ocf_adj_ttm, SBC["TTM"], maint, LEASE_PRIN["TTM"])
p(f"  TTM cash figures UNRECONCILED (B12; not used as evidence): TTM OCF {OCF['TTM']:,} includes {d_bank:,} of new bank")
p(f"      credit; the H1 2025 column shows no tax paid ({TAX_PAID['H1_2025']}) although taxes payable fell from 5,707 to"
  f" 1,066, and Q2 2025 shows no interest received (paymeant_h1_2026 p.28). Lender-adjusted cash proxy {cash_adj:,.0f}.")
c4_oe, c4_ni = 0.0, 0.0
for per, a, b in (("FY2023", D22, D23), ("FY2024", D23, D24), ("FY2025", D24, D25)):
    capex = CAPEX_PPE[per] + CAPEX_DEV_CASH[per] + CAPEX_DEV_SBP[per] + CAPEX_ROU[per]
    m = cv.maintenance_capex(capex, DA[per], netppe_to_rev, REV[per] - REV[FY[FY.index(per) - 1]])
    ocf_adj = (OCF[per] - (BANK[b] - BANK[a]) + (LOANS_FV[b] + LOANS_AC[b] - LOANS_FV[a] - LOANS_AC[a])
               - (PAY_CT[b] - PAY_CT[a]))
    c4_oe += cv.owner_earnings_cash(ocf_adj, SBC[per], m, LEASE_PRIN[per])
    c4_ni += NI[per]
held_months = {d: (LOANS_FV[d]) / (orig / 12) for d, orig in ((D23, ORIG["FY2023"]), (D24, ORIG["FY2024"]),
                                                               (D25, ORIG["FY2025"]), (J26, ORIG["TTM"]))}
p(f"  H3 burn test: reported OCF FY2023-FY2025 {fmt_d({k: OCF[k] for k in ('FY2023', 'FY2024', 'FY2025')})}, average"
  f" {statistics.mean(OCF[k] for k in ('FY2023', 'FY2024', 'FY2025')):,.0f} (>= 0; it includes bank-credit and loan-book"
  f" changes)")
p(f"  C4 (annual audited figures): FY2023-FY2025 lender-adjusted cash owner earnings / net income {c4_oe / c4_ni:.0%}"
  f" (>= 80%); loans held for sale in months of originations " + ", ".join(f"{k[:7]} {v:.2f}" for k, v in held_months.items())
  + " (no build-up); capitalised development is building (above): C4 'no' on its deferred-asset clause")
op_costs_lender = REV["TTM"] - EBIT_ADJ["TTM"]
xs_cash = cv.excess_cash(CASH[J26], op_costs_lender)
xs_cash_unl = cv.excess_cash(CASH[J26], REV["TTM"] - EBIT_UNL["TTM"])
p(f"  excess cash: cash {CASH[J26]:,} vs two months of operating costs {op_costs_lender * 2 / 12:,.0f} -> {xs_cash:,.0f}"
  f" (the cash sits in pledged dedicated accounts, paymeant_fy2025 p.99 note 11b)")
p(f"  dilution (B10): note-17 residual {RES_N:,.0f} options at an implied strike {RES_K:.2f}; diluted shares at 2.00 /"
  f" 3.173 / 5.00: {dilutive_shares(2.0):,.0f} / {dilutive_shares(PRICE):,.0f} / {dilutive_shares(5.0):,.0f};"
  f" note 17 ({NOTE17_OPTIONS:,}) and Reg. 24A (1,136,125) are not reconciled by the company")
sh = {"FY2021": SHARES_FY2021, "FY2022": SHARES_FY2022, "FY2023": SHARES_FY2023, "FY2024": SHARES_FY2024,
      "FY2025": SHARES_FY2025, "3.11.2026": SHARES}
keys = list(sh)
p("  share count (B3, dilution at most 2% a year): " + "; ".join(
    f"{keys[i]} {sh[keys[i]] / sh[keys[i - 1]] - 1:+.1%}" for i in range(1, len(keys)))
  + f"; FY2021-FY2025 CAGR {(SHARES_FY2025 / SHARES_FY2021) ** (1 / 4) - 1:.1%} (screen_spec X3 tests > 5%)")
p(f"      2025: {EXERCISES_2025[0]:,} shares issued on exercise at a weighted {EXERCISES_2025[1]:.2f} (p.112), against a price of"
  f" 3.19 at the founders' January 2025 grant (p.111); 2022: the founders took {FOUNDERS_EXERCISE_2022[0]:,} shares for"
  f" {FOUNDERS_EXERCISE_2022[1]}k in total (fy2023 p.107)")
for per in ("FY2025", "H1_2026"):
    p(f"  {per}: operating cash flow before the change in bank credit {OCF[per] - BANK_CF[per]:,} (OCF {OCF[per]:,} less bank"
      f" credit {BANK_CF[per]:,}) against dividends paid {DIVIDENDS[per]:,}: the payout is funded by on-call credit while"
      f" the book grows")

# ---------------------------------------------------------------------------- 3. methods
p("")
p("== 3. Methods")
roiic = oe_norm / TE_J26
roiic_opt = oe_opt / TE_J26
retention = 1 - DIVIDENDS["TTM"] / NI["TTM"]
g1_cap = cv.growth_cap(g_hist, retention, roiic)
epv_l = cv.equity_bridge(cv.epv_operations(oe_norm, R), xs_cash, 0, 0, LEASES[J26], 0, NCI, PREFERRED)
p(f"  d3 EPV, lender basis: OE_norm {oe_norm:,.0f} / r = {cv.epv_operations(oe_norm, R):,.0f}; + excess cash {xs_cash:,.0f}"
  f" - leases {LEASES[J26]:,} = {epv_l:,.0f} -> {money(ps(epv_l))}")
p(f"  d4 growth cap: record {g_hist:.1%}; retention {retention:.1%} x ROIIC {roiic:.1%} = {retention * roiic:.1%}; cap 10%"
  f" -> g1 <= {g1_cap:.1%}. ROIIC = OE_norm / tangible equity {TE_J26:,.0f}")
dcf_b = cv.dcf_operations(oe_norm, R, G_BASE, roiic)
dcf_base = cv.equity_bridge(dcf_b.operations_value, xs_cash, 0, 0, LEASES[J26], 0, NCI, PREFERRED)
p(f"  d4 DCF, lender basis, base g {G_BASE:.0%} (CPI), ROIIC {roiic:.1%}, gT 2.5%, ROIIC_T = r: operations"
  f" {dcf_b.operations_value:,.0f} (explicit {dcf_b.pv_explicit:,.0f}, terminal {dcf_b.pv_terminal:,.0f},"
  f" {dcf_b.terminal_share:.0%} of total) -> equity {dcf_base:,.0f} -> {money(ps(dcf_base))}")
ncav_v = cv.ncav(CURRENT_ASSETS_J26, TL_J26, PREFERRED)
recv_all = LOAN_BOOK_J26 + RECV[J26]
dempster = cv.dempster_value(CASH[J26], recv_all, 0, 0, 0, TL_J26, PREFERRED)
netnet = cv.netnet_buy_test(MCAP, ncav_v, dempster)
p(f"  d6 NCAV = current assets {CURRENT_ASSETS_J26:,} - total liabilities {TL_J26:,} = {ncav_v:,.0f} -> {money(ps(ncav_v))}")
p(f"  d6 Dempster = cash {CASH[J26]:,} + 85% x loans and receivables {recv_all:,} - liabilities {TL_J26:,} = {dempster:,.0f}"
  f" -> {money(ps(dempster))}; net-net test (MCap <= 2/3 NCAV and <= Dempster): {netnet['passes']}")
tbv_cost = TE_J26 - FV_UPLIFT_J26 * (1 - T_STATUTORY)
p(f"  d7 tangible book {TE_J26:,.0f} -> {money(ps(TE_J26))}; at amortised cost (step-up {FV_UPLIFT_J26:,} removed after tax)"
  f" {tbv_cost:,.0f} -> {money(ps(tbv_cost))}")
p("  d7 private-owner value: none. No disclosed control transaction; minority placements and blocks are not owner value.")
ev_l = cv.enterprise_value(MCAP, 0, CASH[J26], LEASES[J26], NCI, PREFERRED)
pm_l = cv.pretax_multiple(ev_l, n_base.ebit_norm)
p(f"  d5 pre-tax multiple, lender basis: EV {ev_l:,.0f} / EBIT_norm {n_base.ebit_norm:,.0f} = {pm_l['ev_to_ebit_norm']:.2f}x"
  f" (yield {pm_l['pretax_yield']:.1%}); on TTM {ev_l / EBIT_ADJ['TTM']:.2f}x")
gy_n = cv.graham_yardstick(ni_norm, MCAP, Y10_ILS)
gy_t = cv.graham_yardstick(NI["TTM"], MCAP, Y10_ILS)
p(f"  d9 Graham's yardstick [I, looser: ILS government yield]: on normalised NI {gy_n['earnings_yield']:.1%} vs"
  f" {gy_n['required_yield']:.1%}, P/E {gy_n['pe']:.1f} vs cap {gy_n['pe_cap']:.0f} -> {gy_n['passes']}; on TTM NI"
  f" {gy_t['earnings_yield']:.1%}, P/E {gy_t['pe']:.2f} -> {gy_t['passes']}")
p("  EV basis of framework d3 as written (cross-check; screen_spec 3.1: meaningless for a lender):")
n_unl = cv.normalised_ebit(REV["TTM"], [EBIT_UNL[x] for x in FY], [REV[x] for x in FY])
n_unl_v1 = cv.normalised_ebit(REV["TTM"], [EBIT_ADJ_V1[x] + FUND[x] for x in FY + ["TTM"]],
                              [REV[x] for x in FY + ["TTM"]])
ev_methods = {}
for lab, n in (("charter normalisation (cyclical)", n_unl), ("first-version normalisation (stable)", n_unl_v1)):
    oe_u = cv.unlevered_owner_earnings(n.ebit_norm, 0, T_STATUTORY, DA["TTM"], maint)
    epv_e = cv.equity_bridge(cv.epv_operations(oe_u, R), xs_cash_unl, 0, BANK[J26], LEASES[J26], 0, NCI, PREFERRED)
    ev_methods[lab] = (n, oe_u, epv_e)
    p(f"      {lab:<38} EBIT_norm before funding {n.ebit_norm:7,.0f}; OE_unlevered {oe_u:7,.0f}; EPV equity"
      f" {epv_e:9,.0f} -> {money(ps(epv_e))}")
p(f"      reading: on the charter normalisation the EV basis values the equity below the run-off value of the book")
p(f"      (Dempster {money(ps(dempster))}), i.e. it treats self-liquidating, matched warehouse debt as a claim on a")
p("      cycle-depressed income stream. That is screen_spec 3.1's point; the lender basis is primary, the EV basis shown.")
p(f"  bank-route gates (screen_spec 4.7):")
roe = {}
roa = {}
for per, a, b in (("FY2022", D21, D22), ("FY2023", D22, D23), ("FY2024", D23, D24), ("FY2025", D24, D25),
                  ("TTM", J25, J26)):
    roe[per] = NI[per] / ((EQUITY[a] + EQUITY[b]) / 2)
    roa[per] = NI[per] / ((TOTAL_ASSETS[a] + TOTAL_ASSETS[b]) / 2)
pe_norm = MCAP / ni_norm
bank_line = min(1.2 * TE_J26, 10 * ni_norm)
p(f"      F.1 NI > 0 in every FY of W: {all(NI[x] > 0 for x in FY)} (FY2021 {NI['FY2021']:,}); F.2 ROE median"
  f" {statistics.median(roe.values()):.1%}, ROA median {statistics.median(roa.values()):.1%}: True; F.3 equity / assets"
  f" {EQUITY[J26] / TOTAL_ASSETS[J26]:.1%}: True")
p(f"      F.4 P/TBV {MCAP / TE_J26:.2f} (<= 1.2) and pe_norm {pe_norm:.1f} (<= 10): False; bank-route price line"
  f" min(1.2 x TBV, 10 x NI_norm) = {money(ps(bank_line))}")

# ---------------------------------------------------------------------------- 4. the range and the stresses
p("")
p("== 4. Value range (per diluted share) and stresses")
worst_high = ps(dempster)
performing_cost = LOANS_FV_AT_COST_J26 + LOANS_AC[J26] - ARREARS[J26]["default"]
wind_down = WIND_DOWN_YEARS * WIND_DOWN_OPEX_SHARE * OPEX["TTM"]
runoff_low = cv.dempster_value(CASH[J26], performing_cost, 0, 0, 0, TL_J26 + wind_down, PREFERRED,
                               other_assets_at_value=RECOVERY_DEFAULT * ARREARS[J26]["default"]
                               + RECOVERY_RECV * RECV[J26])
worst_low = ps(runoff_low)
cov_hist = {d: prov / gross for d, (gross, prov) in PROVISION_AC.items()}
writeoffs_2025 = PROVISION_AC[D24][1] + CREDIT_CHARGE["FY2025"] - PROVISION_AC[D25][1]
prov_max_j26 = PROVISION_AC[D25][1] + CREDIT_CHARGE["H1_2026"]
shortfall = {c: c / (1 - c) * ARREARS[J26]["default"] - prov_max_j26 for c in COVERAGE_TESTS}
conservative_k = tbv_cost - shortfall[COVERAGE_TESTS[0]] * (1 - T_STATUTORY)
conservative = ps(conservative_k)
base = ps(dcf_base)
dcf_o = cv.dcf_operations(oe_opt, R, G_OPT, roiic_opt)
optimistic = ps(cv.equity_bridge(dcf_o.operations_value, xs_cash, 0, 0, LEASES[J26], 0, NCI, PREFERRED))
p(f"  worst case  {money(worst_low)} to {money(worst_high)}  run-off of the 30.6.2026 book (funding withdrawn, origination")
p(f"              stops). Low end: book at amortised cost {LOANS_FV_AT_COST_J26:,}, performing loans at 85%, defaults"
  f" {ARREARS[J26]['default']:,} at {RECOVERY_DEFAULT:.0%},")
p(f"              receivables {RECV[J26]:,} at {RECOVERY_RECV:.0%}, wind-down cost {wind_down:,.0f}. High end: Dempster at"
  f" 85% on every loan. Both exclude the SPC")
p("              indemnities and the 360 guarantee exposure (not disclosed), so neither is held with confidence (A2).")
p(f"  conservative {money(conservative)}  no moat: ROE converges on r, so equity is worth tangible book at amortised cost"
  f" {tbv_cost:,.0f}")
p(f"              less the UNVERIFIED provision shortfall at {COVERAGE_TESTS[0]:.0%} coverage on defaulted loans"
  f" ({shortfall[COVERAGE_TESTS[0]]:,.0f} pre-tax)")
p(f"  base        {money(base)}  DCF, lender basis, OE_norm {oe_norm:,.0f} (cyclical EBIT_norm {n_base.ebit_norm:,.0f}),"
  f" g {G_BASE:.0%}, ROIIC {roiic:.1%}, r {R:.0%}")
p(f"  optimistic  {money(optimistic)}  DCF, lender basis, OE {oe_opt:,.0f} (TTM revenue x m_norm {n_opt.ebit_norm:,.0f}:"
  f" today's scale holds), g {G_OPT:.0%}, ROIIC {roiic_opt:.1%}")
fv_equity = cv.equity_bridge(cv.dcf_operations(oe_v1, R, 0.05, oe_v1 / TE_J26).operations_value, xs_cash, 0, 0,
                             LEASES[J26], 0, NCI, PREFERRED)
first_version_base = ps(fv_equity)
p(f"  superseded first-version base (note 19e added back, W + TTM, g 5%): {money(first_version_base)} per diluted share"
  f" ({fv_equity * 1000 / SHARES:.2f} per basic share, as first published)")
t_ttm = TAX["TTM"] / PBT["TTM"]
oe_t = cv.owner_earnings(n_base.ebit_norm * (1 - t_ttm), DA["TTM"], 0, 0, maint, 0)
base_t = ps(cv.equity_bridge(cv.dcf_operations(oe_t, R, G_BASE, oe_t / TE_J26).operations_value, xs_cash, 0, 0,
                             LEASES[J26], 0, NCI, PREFERRED))
p(f"  tax sensitivity (B11 rejected): base at the TTM effective rate {t_ttm:.1%} {money(base_t)} ({base_t / base - 1:+.1%})")
range_vals = {"worst": worst_low, "conservative": conservative, "base": base, "optimistic": optimistic}
pw = sum(SCENARIO_P[k] * v for k, v in range_vals.items())
others = {k: v for k, v in range_vals.items() if k != "optimistic"}
m_others = sum(SCENARIO_P[k] * v for k, v in others.items()) / sum(SCENARIO_P[k] for k in others)
w_break = (PRICE - m_others) / (optimistic - m_others)
p(f"  probabilities {SCENARIO_P} (uncalibrated) -> probability-weighted {money(pw)}")
p(f"      the price equals the weighted value only if the optimistic case carries {w_break:.0%} of the weight (the other")
p("      cases in their stated proportions): the market is paying for today's scale persisting and growing")

p("  covenants, note 11a(6) (B6), at 30.6.2026:")
tbs = TOTAL_ASSETS[J26] - INTANG[J26]
tbs_co = tbs - (TE_J26 - TE_COMPANY_J26)
cov_loss_bs = (TE_J26 - COV_TE_RATIO * tbs) / (1 - COV_TE_RATIO)
cov_loss_co = (TE_COMPANY_J26 - COV_TE_RATIO * tbs_co) / (1 - COV_TE_RATIO)
p(f"      (a) TE >= 20% of the tangible balance sheet: {TE_J26 / tbs:.1%} on the balance-sheet definition, {TE_COMPANY_J26 / tbs_co:.1%}"
  f" on the company's TE of {TE_COMPANY_J26:,}; breaks after a loss of {cov_loss_bs:,.0f} / {cov_loss_co:,.0f}")
p(f"      (b) TE >= 25M: breaks after a loss of {TE_J26 - COV_TE_MIN:,.0f} / {TE_COMPANY_J26 - COV_TE_MIN:,.0f}")
p(f"      (c) senior debt <= 80% of loans: {BANK[J26] / LOAN_BOOK_J26:.1%}; with debt unchanged the book can shrink to"
  f" {BANK[J26] / COV_SENIOR_DEBT:,.0f} ({BANK[J26] / COV_SENIOR_DEBT / LOAN_BOOK_J26 - 1:+.1%})")
need = PBT["TTM"] - COV_NI_MIN / (1 - T_STATUTORY)
orig_rev = FEES["TTM"] + SALE_FV["TTM"]
p(f"      (d) annual net profit >= 1M: breaks after a pre-tax fall of {need:,.0f} ({need / PBT['TTM']:.1%} of TTM)."
  f" Origination-driven revenue (fees + sales/FV) TTM {orig_rev:,} vs opex {OPEX['TTM']:,}: with opex flat an")
p(f"          origination fall of {need / orig_rev:.1%} reaches it; an origination stop breaches it within the year")
ctrl_pct = FOUNDERS_SHARES / SHARES
p(f"      (e) change of control: founders {ctrl_pct:.2%}; voting agreement lapses below {CTRL_FLOOR:.0%}; headroom"
  f" {ctrl_pct - CTRL_FLOOR:.2%} = {FOUNDERS_SHARES - CTRL_FLOOR * SHARES:,.0f} shares; the lines restrict changes of control")
c1_ni = PBT["TTM"] * 0.7 * (1 - T_STATUTORY)
p(f"  C1 test (flat revenue, EBIT -30%): net profit {c1_ni:,.0f} >= 1,000 and TE unchanged -> no covenant breach; but the")
p(f"      {BANK[J26]:,} of bank credit is on-call and the funders 'may stop the engagement unilaterally' (paymeant_fy2025 p.55):")
p("      survival 'without new money' needs the lines to keep rolling -> C1 fails closed")
p("  impairment markers in the worst case (E1):")
p(f"      (1) covenant breach or maturity -> dilution: plausible. All funding is callable; the profit covenant breaks at an")
p(f"          origination fall of about {need / orig_rev:.0%} or a funding stop; the SPC indemnities 'in other cases'"
  f" (paymeant_h1_2026 p.7)")
p("          and the circular's cancellation right from 12.1.2027 (h1 p.8) can bring sold loans back")
p("      (2) going-concern doubt: plausible if the funders withdraw and origination stops")
p(f"      (3) assets below debt: no on the balance sheet; the run-off value stays positive ({money(worst_low)} at the low end)")
p("      Plausible paths to (1) and (2) exist, so E1 fails closed.")

pre_prov = PBT["TTM"] + CREDIT_CHARGE["TTM"]
f3_zero = pre_prov / (SEVERITY_F3 * LOAN_BOOK_J26)
f3_cov = (pre_prov - COV_NI_MIN / (1 - T_STATUTORY)) / (SEVERITY_F3 * LOAN_BOOK_J26)
dflt_share = {d: a["default"] / sum(a.values()) for d, a in ARREARS.items()}
arrears_share = {d: (a["default"] + a["1-90 days"]) / sum(a.values()) for d, a in ARREARS.items()}
p("  credit (B5; the economic credit cost is UNVERIFIED: expected losses on the fair-value book sit inside revenue):")
p(f"      defaults {ARREARS[D25]['default']:,} -> {ARREARS[J26]['default']:,} (x{ARREARS[J26]['default'] / ARREARS[D25]['default']:.2f});"
  f" share of book {dflt_share[D25]:.1%} -> {dflt_share[J26]:.1%}; all arrears {arrears_share[D25]:.2%} ->"
  f" {arrears_share[J26]:.2%}")
p(f"      amortised-cost provision coverage {', '.join(f'{k[:4]} {v:.1%}' for k, v in cov_hist.items())}; 2025 write-offs"
  f" {writeoffs_2025:,} = {writeoffs_2025 / CREDIT_CHARGE['FY2025']:.2f}x the charge")
p(f"      IF the defaulted loans sit in the amortised-cost book: shortfall at {COVERAGE_TESTS[0]:.0%} coverage"
  f" {shortfall[COVERAGE_TESTS[0]]:,.0f}, at {COVERAGE_TESTS[1]:.0%} {shortfall[COVERAGE_TESTS[1]]:,.0f}"
  f" ({shortfall[COVERAGE_TESTS[0]] / PBT['TTM']:.0%}-{shortfall[COVERAGE_TESTS[1]] / PBT['TTM']:.0%} of TTM pre-tax) [UNVERIFIED]")
p(f"      f3 stress: pre-provision pre-tax TTM {pre_prov:,} covers defaults of {f3_zero:.1%} of the {LOAN_BOOK_J26:,} book at"
  f" {SEVERITY_F3:.0%} severity ({f3_cov:.1%} before the profit covenant); the binding risk is the origination engine")

p("  F4 stresses (B7): revenue, costs and debt are all ILS; FX exposure 'not material' (paymeant_fy2025 p.101)")
wh = RATE_SHOCK * 100 * RATE_SENS_1PT
sold_vol = ORIG["TTM"] * SOLD_SHARE_2025
dur = DURATION_MONTHS / 12
sale_comp = sold_vol * RATE_SHOCK * dur
for lab, held_m in (("held-book duration = loan duration 14 months (fy2025 p.42)", DURATION_MONTHS),
                    (f"held-book duration {HELD_DURATION_LOW_M} months (assumed lower bound)", HELD_DURATION_LOW_M)):
    fv_hit = LOANS_FV[J26] * RATE_SHOCK * held_m / 12
    y1 = wh + fv_hit + sale_comp * REPRICE_LAG_YEARS
    p(f"      +2 points, {lab}: warehouse {wh:,.0f}/yr + one-off fair-value loss {fv_hit:,.0f} + sale-price compression"
      f" {sale_comp:,.0f}/yr for {REPRICE_LAG_YEARS} yr = year-1 pre-tax hit {y1:,.0f} ({y1 / PBT['TTM']:.0%} of TTM);")
    p(f"          profit covenant: TTM NI after the hit {(PBT['TTM'] - y1) * (1 - T_STATUTORY):,.0f}; on EBIT_norm"
      f" {(n_base.ebit_norm - y1) * (1 - T_STATUTORY):,.0f} (>= {COV_NI_MIN:,} needed)")
oe_never = cv.owner_earnings((n_base.ebit_norm - wh - sale_comp) * (1 - T_STATUTORY), DA["TTM"], 0, 0, maint, 0)
epv_never = ps(cv.equity_bridge(cv.epv_operations(oe_never, R), xs_cash, 0, 0, LEASES[J26], 0, NCI, PREFERRED))
oe_rep = cv.owner_earnings((n_base.ebit_norm - wh) * (1 - T_STATUTORY), DA["TTM"], 0, 0, maint, 0)
epv_rep = ps(cv.equity_bridge(cv.epv_operations(oe_rep, R), xs_cash, 0, 0, LEASES[J26], 0, NCI, PREFERRED))
p(f"      lender EPV on the base normalisation: repriced after the lag (warehouse cost kept) {money(epv_rep)}; never repriced"
  f" {money(epv_never)}; the held book's discount-rate sensitivity is not disclosed: F4 open")
p(f"      CPI -1 point: one-off fair-value loss {CPI_SENS_1PT:,} pre-tax (h1 p.8); high CPI helps (CPI-linked loans, unlinked"
  f" funding) until the rate rise follows")


def base_value(rr: float, gg: float) -> float:
    """Base-case value per diluted share at hurdle rr and ten-year growth gg (sensitivity grid, checklist D3)."""
    ops = cv.dcf_operations(oe_norm, rr, gg, roiic).operations_value
    return ps(cv.equity_bridge(ops, xs_cash, 0, 0, LEASES[J26], 0, NCI, PREFERRED))


grid = cv.sensitivity_grid(base_value, R, G_BASE)
p("  sensitivity grid (base value per share, lender basis; r +/- 1 point, g +/- 2 points)")
gs = sorted({k[1] for k in grid["grid"]})
p("      r \\ g   " + "".join(f"{g:>9.0%}" for g in gs))
for rr in sorted({k[0] for k in grid["grid"]}):
    p(f"      {rr:>5.0%}  " + "".join(f"{grid['grid'][(rr, g)]:>9.2f}" for g in gs))
p(f"      range {grid['min']:.2f}-{grid['max']:.2f} vs price {PRICE:.3f}: base > price everywhere (D3): {grid['min'] > PRICE}")
n1, oe_u1, _ = ev_methods["first-version normalisation (stable)"]
roiic_u1 = oe_u1 / tangible_operating_capital(J26)
grid_ev = cv.sensitivity_grid(
    lambda rr, gg: ps(cv.equity_bridge(cv.dcf_operations(oe_u1, rr, gg, roiic_u1).operations_value, xs_cash_unl, 0,
                                       BANK[J26], LEASES[J26], 0, NCI, PREFERRED)), R, 0.05)
p(f"      EV basis, first-version normalisation, g 5% +/- 2 (red team's reading): range {grid_ev['min']:.2f}-{grid_ev['max']:.2f}:"
  f" D3 {grid_ev['min'] > PRICE}. The optimistic case (lender basis) is above the price: it is a scenario, not the base.")

# ---------------------------------------------------------------------------- 5. price lines
p("")
p("== 5. Margin of safety and price lines")
vr = cv.ValueRange(COMPANY, "ILS", PRICE, PRICE_DATE, worst_low, conservative, base, optimistic,
                   cv.required_margin("C", [], endogenous_addback=False),
                   methods={"EPV, lender basis (d3)": ps(epv_l), f"DCF 10y, lender basis, g {G_BASE:.0%} (d4)": base,
                            "tangible book (d7)": ps(TE_J26)})
for k, v in vr.methods.items():
    p(f"  method {k:<40}{v:>8.4f}   price/value {PRICE / v:5.2f}")
p(f"  method spread {vr.method_spread():.0%} (<= 30%: earnings and assets agree once the add-back is removed; the EV basis is"
  f" excluded as meaningless for a lender, screen_spec 3.1)")
for name in ("worst_case", "conservative", "base", "optimistic"):
    v = getattr(vr, name)
    p(f"  {name:<46}{v:>8.4f}   price/value {PRICE / v:5.2f}")
tier_c_line = min(2 / 3 * ps(ncav_v), ps(dempster))
margin_ref = 1 - tier_c_line / base
p("  lane: none, so no tier margin applies and there is NO BUY PRICE under any lane (the shadow Tier B line of the first")
p("  version is withdrawn). Reference lines only:")
p(f"      Tier C net-net line, min(2/3 NCAV {2 / 3 * ps(ncav_v):.2f}, Dempster {ps(dempster):.2f}) = {money(tier_c_line)}"
  f" = {margin_ref:.0%} below base; price / line {PRICE / tier_c_line:.2f}")
p(f"      bank-route line {money(ps(bank_line))}; price / line {PRICE / ps(bank_line):.2f}")
m_ref = cv.required_margin("B", DATA_FLAGS)
p(f"  data additions carried (F6): {', '.join(DATA_FLAGS)} -> +{m_ref.data_addition:.0%} (capped); no endogenous add-back (C5)")

# ---------------------------------------------------------------------------- 6. liquidity, sizing, the test
p("")
p("== 6. Liquidity, sizing, the investment test")
turnover = [t for _, _, _, t in BZ_SESSIONS]
med = statistics.median(turnover)
p25 = statistics.quantiles(turnover, n=4, method="inclusive")[0]
p25_x = statistics.quantiles(turnover, n=4)[0]
oct_idx = [i for i, s in enumerate(BZ_SESSIONS) if s[0] >= "10-20"]
oct_share = sum(turnover[i] for i in oct_idx) / sum(turnover)
oct_vol = sum(BZ_SESSIONS[i][1] for i in oct_idx)
pre_fall = statistics.median(t for d, _, _, t in BZ_SESSIONS if d < "10-20")
p(f"  Bizportal daily proceeds, 60 sessions {BZ_SESSIONS[0][0]}..{BZ_SESSIONS[-1][0]}.2026: median {med:,.0f} ILS (before"
  f" 20.10: {pre_fall:,.0f}); 25th percentile {p25:,.0f} (linear; exclusive method {p25_x:,.0f})")
p(f"  floor {LIQ_FLOOR:,} (screen_spec X5, hard exclusion): passes {med >= LIQ_FLOOR}; price-reliability line"
  f" {LIQ_RELIABILITY:,}: passes {med >= LIQ_RELIABILITY}; {sum(1 for t in turnover if t < LIQ_FLOOR)} of 60 sessions below"
  f" the floor; {oct_share:.1%} of the proceeds in the {len(oct_idx)} sessions from 20.10")
p(f"  October selling: {oct_vol:,} shares traded 20.10-3.11 = {oct_vol / SHARES:.2%} of the company, all on-exchange; no"
  f" holder above 5% reported a sale (seller unidentified, scuttlebutt.md §6)")
outcomes = [(SCENARIO_P[k], v) for k, v in range_vals.items()]
size = cv.position_size(PRICE, worst_low, outcomes, "C", turnover_p25_daily=p25)
size_b = cv.position_size(PRICE, worst_low, outcomes, "B", turnover_p25_daily=p25)
lims = ", ".join(f"{k} {v:.1%}" for k, v in size["limits"].items())
p(f"  e2 position_size (tier C, the cheap track a cyclical lender would have to use): full Kelly {size['kelly_full']:.1%};"
  f" L_worst {size['l_worst']:.1%} (low-end worst case); limits: {lims}")
p(f"      size {size['size']:.1%} of NAV, binding {size['binding']} (tier B gives {size_b['size']:.1%}, binding"
  f" {size_b['binding']}); liquidity maximum 20 x 20% x p25 = {size['liquidity_amount']:,.0f} ILS at cost")
ev_impl_l = MCAP + LEASES[J26] - xs_cash
g_impl = cv.implied_growth(ev_impl_l, oe_norm, R, roiic)
g_impl_free = cv.implied_growth(ev_impl_l, oe_norm, R, None)
g_impl_opt = cv.implied_growth(ev_impl_l, oe_opt, R, roiic_opt)
g_impl_v1 = cv.implied_growth(ev_impl_l, oe_v1, R, oe_v1 / TE_J26)
_, oe_u_v1, epv_e_v1 = ev_methods["first-version normalisation (stable)"]
g_impl_ev = cv.implied_growth(MCAP + BANK[J26] + LEASES[J26] - xs_cash_unl, oe_u_v1, R, roiic_u1)
ni_ttm_prior = NI["FY2024"] + NI["H1_2025"] - (NI_Q1_2024 + NI_Q2_2024)
p(f"  d8 implied growth at {PRICE:.3f} (ten years, lender basis): on OE_norm {g_impl:+.1%} with reinvestment charged at"
  f" ROIIC {roiic:.1%}, {g_impl_free:+.1%} if growth were free;")
p(f"      on today's scale (optimistic OE {oe_opt:,.0f}) {g_impl_opt:+.1%}; first version {g_impl_v1:+.1%}; EV basis, first-version"
  f" normalisation {g_impl_ev:+.1%}")
p(f"      the record: TTM NI {NI['TTM'] / ni_ttm_prior - 1:+.1%} y/y; H1 2026 NI {NI['H1_2026'] / NI['H1_2025'] - 1:+.1%};"
  f" H1 2026 pre-tax before net capitalisation {h1_und:+.1%}")
p(f"  peers (Tier 2): P/E {MCAP / NI['TTM']:.2f} vs Israeli specialist-lender median {PEER_PE_MEDIAN}"
  f" ({MCAP / NI['TTM'] / PEER_PE_MEDIAN - 1:+.1%}); P/B {MCAP / EQUITY[J26]:.2f} vs {PEER_PB_MEDIAN}"
  f" ({MCAP / EQUITY[J26] / PEER_PB_MEDIAN - 1:+.1%}): no material discount on lender metrics")
p(f"  who sold: the founders {FOUNDERS_SALE[0]:,} shares at {FOUNDERS_SALE[1]:.2f} on {FOUNDERS_SALE[2]} (price now"
  f" {PRICE / FOUNDERS_SALE[1] - 1:+.1%}), between the board's (22.2.2026) and the meeting's (30.3.2026) approval of"
  f" their raise")
p("  investment test, in order:")
p("    Q1 inside the circle? Cannot be assessed here (theses/CIRCLE.md); the model is on the avoid list ('dependent on")
p("       refinancing markets', Delta Financial's warehouse lines, framework f2). Fails closed.")
p("    Q2 a good business by its lane? No lane fits: A/B fail on moat (A3, A4), leverage (C2) and funding (C1, C3, E8);")
p("       C fails (not a net-net, no private-owner value, net debt: H2, H4, H5); D has no A/B franchise; E has no deal.")
p(f"    Q3 price well below value? No: price / base {PRICE / base:.2f}, price / EPV {PRICE / ps(epv_l):.2f}, price / tangible"
  f" book {PRICE / ps(TE_J26):.2f}; probability-weighted {money(pw)}.")
p(f"    Q4 what the price assumes: today's earnings scale persisting ({g_impl_opt:+.1%} a year on it); on the charter's")
p(f"       normalisation {g_impl_free:+.1%} to {g_impl:+.1%} a year. The record cannot show that is too pessimistic, and the")
p("       remaining gap to peers is explained by known facts the filings do not refute: on-call funding concentrated in")
p("       one bank, defaults up x2.97, the BNPL circular from 12.1.2027, informed insiders selling at 6.90, illiquidity.")
p("       Priced (the Petco rule).")
p("  CIO VERDICT: NO_THESIS. Price is not the only failure (so not WATCHLIST); the deciding failures rest on filed,")
p("  verified facts (so not TOO_HARD). Price alone never reopens the file (re-examination conditions: gate.md).")
p("")
p("Per-share summary (ILS per diluted share, agorot):")
for name, v in (("price", PRICE), ("worst case, low end (sizing)", worst_low), ("worst case, high end (Dempster)", worst_high),
                ("conservative", conservative), ("base", base), ("optimistic", optimistic),
                ("probability-weighted", pw), ("buy price", None),
                ("reference: Tier C net-net line (not a buy price)", tier_c_line),
                ("reference: bank-route line (not a buy price)", ps(bank_line))):
    p(f"  {name:<50} {money(v) if v is not None else 'none: no lane fits (NO_THESIS)'}")

print("\n".join(out))
