# Paymeant (TASE 1180876) - reconciliation of extractions A and B

Date 2026-11-03. Inputs: `fin_A.json` (statements first), `fin_B.json` (notes and cash flow first).
Output: `financials.json` (A's structure and sign convention; B-only fields added under A-style names; every
value carries `v` + `ref`), built by `recon_tools/build_financials.py`; comparison by `recon_tools/compare.py`.
Units ILS thousands unless stated.

## Method

* B's field names (142) were mapped onto A's (167) where they correspond, and B's cash-flow outflows (stated positive) were re-signed to A's
  statement signs. 767 field-period pairs had a number on both sides: 766 agree within 0.5% (all but one exactly).
  The 33 overlapping quarterly figures (Q4 2023-Q4 2025) agree exactly. 121 field-period pairs existed on one side
  only. Outside the period tables, three dividend-per-share figures and one one-off amount differ.
* Every item below was checked on the PDF page image with the Read tool. In addition, because both extractions
  could share the same text-layer misreading, all primary statements were re-read from the images and every
  figure used by `derived.py` was ticked: paymeant_fy2023 p.19, p.39, p.56-57, p.62-63, p.65, p.81-85, p.94,
  p.96-98, p.103-114; paymeant_fy2024 p.42, p.80-84, p.94, p.111-117; paymeant_fy2025 p.67, p.82-86, p.95-99,
  p.103-117, p.123; paymeant_h1_2026 p.13-16, p.23-28.
* Result: no primary-statement figure (P&L, balance sheet, equity, cash flow) was wrong in either extraction; the
  balance-sheet, gross-profit, net-income and financing-cash-flow identities hold for every period (asserted in the
  build script).

## A. Numeric conflicts (> 0.5%)

| # | Item | A | B | Evidence on the page | Resolution |
|---|------|---|---|----------------------|------------|
| D1 | FY2021 net income to owners | (769) | (765) | P&L paymeant_fy2023 p.82, equity statement p.83, cash flow p.84 and Part A table p.19 all show (769); the EPS note p.109 prints (765) | **(769)**. The 4K gap is an internal inconsistency of the filing; EPS (0.03) either way. (765) kept as `alt_v_eps_note`. |
| D2 | Dividend per share, declared 27.2.2023 / 1.8.2023 / 25.2.2024 | 0.0834 / 0.081253 / 0.054168 | 0.08 / 0.08 / 0.05 | Directors' report paymeant_fy2023 p.56 (sections 2.6-2.8) gives the precise figures; the FS notes (paymeant_fy2023 p.112-113, paymeant_fy2024 p.112) say "~0.08" / "0.05" | **Precise values (A)**; amounts 3,000 / 3,000 / 2,000 agree. Later DPS (0.08, 0.05) are stated as approximate in the filings. |
| D3 | FY2022 tax one-off | 2,085 | 2,150 | Tax reconciliation paymeant_fy2023 p.105: statutory 2,008; prior-year deferred tax (1,024); losses with no DTA (1,126); other 65; actual (77) | **Both correct, different definitions.** 2,085 = NI uplift versus a 23% charge (2,008 + 77) - use this to normalise FY2022; 2,150 = the two identified credits (1,024 + 1,126). Both stored in `one_offs`. |
| - | Largest bank's share of drawn credit 31.12.2025 | 0.885 | 0.883 | paymeant_fy2025 p.99: bank B line 100,000, unused ~8,000 | Within tolerance (denominator 104,000 from the line table vs 104,241 balance sheet). B's 0.883 kept, A's noted. |

## B. Figures present in only one extraction (all verified, all filled)

| # | Item | A | B | Evidence | Resolution in financials.json |
|---|------|---|---|----------|------------------------------|
| M1 | Bank credit 31.12.2021 | null (UNVERIFIED) | 0 (CONFLICT) | Cash flow paymeant_fy2023 p.84: +6,389 in 2021 and +94,856 in 2022 against 101,245 at 31.12.2022 (p.81), so 6,389 at 31.12.2021; note 13f p.103 shows nil and books 101,245 as a 2022 flow (the same note also books the purchaser-A balance 1,624 as a cash outflow although 1,188 of it was income) | **6,389, status UNVERIFIED** (conservative: treated as debt); `alt_v_note13f` 0. |
| M2 | FY2021 balance sheet (no FY2021 balance sheet in the documents) | total assets 32,944, liabilities 10,781 (p.19); equity components 3 / 27,067 / 4,880 / (9,787) (p.83) | PPE 88 (p.96), ROU 482 (p.97), intangibles 2,021 (p.98), loan book 9,221 (derived) | All confirmed on the images. Loan book 9,221 = 125,617 + 2,441 - 118,837 from the relation "CF customer-credit line = -(change in loan book) - interest received", which holds exactly for FY2023-FY2025, and it rebuilds total assets: 18,426 cash + ~2,519 designated cash + 9,221 + ~187 receivables + 482 + 88 + 2,021 = 32,944 | **All kept**; loan book status `derived`. |
| M3 | FY2021-FY2025 operating KPIs (originations, share sold, deals, average deal, nominal/effective rate, duration, default rate) | originations only from FY2022 | all years | paymeant_fy2023 p.39 (2021-2023), paymeant_fy2025 p.42 (2023-2025) | **Kept (B)**; FY2021 originations 146. |
| M4 | FY2021 adjusted EBITDA 1,945; tax current/deferred 0/0; ROU investment 0; convertibles 0 | yes | no | p.65 (1,945); p.105 ('-' for 2021); p.84 ('-'); p.103 (convertible column nil at 31.12.2021) | **Kept (A)**. |
| M5 | FY2021-FY2022 other financing flows | nested under `financing_other` (no `v`) | flat fields + `other_financing` (-607, -436) | p.84: convertible loan received 5,000, repaid (2,498), capital notes 2,600, related-party loans/notes repaid (3,909), credit-provider balances repaid (607) / (436); non-cash conversion 2,242 (p.85) | Values agree; **flattened** into `financing_*` fields; `financing_other` = 586 (2021, derived) and (436) (2022). Financing CF identity holds. |
| M6 | Zero lines recorded only by A: related-party interest FY2022-25; contract assets; long-term credit-provider balance FY2023-H1 2026; restricted-cash change FY2023-25; DTA and warrant liabilities 30.6.2025/2026 | 0 | missing | Statements show no such line or '-' (fy2023 p.81, p.84, p.111; fy2024 p.80, p.83, p.114; fy2025 p.82, p.85, p.114; h1_2026 p.23, p.28) | **0 kept**; contract assets noted as "no separate line - closest is income receivable" (M14). |
| M7 | Lease liabilities total | derived current + non-current | missing | components confirmed on the balance sheets | **Kept (derived)**: 1,296 / 954 / 936 / 2,808 / 3,045 (30.6.2025) / 2,594 (30.6.2026). |
| M8 | Company EBITDA FY2025 26,966; H1 12,484 / 11,741; Q2 6,320 / 6,221 | yes | no | paymeant_h1_2026 p.13 | **Kept (A)**; TTM 27,709 derived. |
| M9 | Tax paid H1 2025 and Q2 2025 | null (UNVERIFIED) | 0 | Interim cash flow paymeant_h1_2026 p.28: the line exists and shows '-' for both; taxes payable fell 5,707 -> 1,066 with current tax ~1,971, so ~6,612 was paid inside the H1-2025 'payables' change (7,710) | **0 "as presented"** + `economic_estimate` -6,612. TTM tax paid stays -10,882 as presented with economic estimate -4,270; TTM OCF 12,963 unaffected. |
| M10 | Q2 2025 / Q2 2026 lines only in A (operating income, NI to owners, working-capital lines, SBP to equity / capitalised, ROU investment, acquisitions, buybacks, NCI dividends) | yes | no | paymeant_h1_2026 p.24, p.25-26, p.28 | **Kept (A)**. |
| M11 | TTM lines | operating income 24,460, SBP to equity 890, EBITDA 27,709 | receivables 1,713, payables re credit transactions 10,786, other payables 7,520, suppliers 544 | FY2025 + H1 2026 - H1 2025 from verified statements | **All kept (derived)**; added TTM capitalised development 2,576 (cash 1,902/642 + capitalised SBP 92/55, h1_2026 p.28; FY2025 1,279, fy2025 p.98). |
| M12 | Quarterly P&L | Q4 2022, Q4 2023-2025, Q4 originations 2022-2023 | Q1 2023 - Q4 2025, Q2 2026, derived Q1 2026, originations 2024-2026 | fy2023 p.62-63 and p.114; fy2024 p.42 and p.117; fy2025 p.45 and p.117; h1_2026 p.24 and p.5. Overlaps identical | **Merged into `quarters`** (replaces A's `quarters_extra`), originations Q1 2022 - Q2 2026. |
| M13 | Income receivable (accrued income) | no | 161 / 1,535 / 1,618 / 2,602 | fy2023 p.94, fy2024 p.94, fy2025 p.95 | **Kept (B)** as `accrued_income_receivable`. |
| M14 | Expense breakdowns (S&M, R&D gross, G&A components) | yes | no | fy2023 p.110-111, fy2024 p.113-114, fy2025 p.114 | **Kept (A)**; all components re-added to the line totals. |
| M15 | Option roll-forward (opening, granted, exercised, expired, closing, exercisable, wavg strike) | yes | no | fy2023 p.109, fy2024 p.111, fy2025 p.112 | **Kept (A)**. |
| M16 | Cash split (`of_which_cash`), non-operating finance (adjusted-EBITDA bridge) | yes | deposits only | fy2023 p.94 (143), fy2024 p.94 (1,821 restated; 464), fy2025 p.95 (724); fy2023 p.65 ((32) / 76 / 51), fy2025 p.67 (nil) | **Kept (A)**. |
| M17 | FY2025 ROU additions | no | 2,560 | note 9 p.97 = 2,560; CF non-cash p.85 = 2,864; note 13f p.104 lease-liability recognition = 2,889 | **Kept** as `rou_additions_note` with the three figures noted (filing inconsistency). |
| M18 | Share events | 31 events | 33 events | B-only: officer options 25.8.2021 (fy2023 p.119-120), Shoker 123,100 exercise 21.2.2022 (p.120), Gabay 30,775 exercise 20.2.2023 (p.119), note 17 vs Reg. 24A option count (fy2025 p.112 vs p.123: 2,189,875 vs 1,136,125), Amitim expiry 24.7.2026 (fy2025 p.108-109) | **Merged**, sorted by date. |
| M19 | Share count 30.6.2026 | null | null | Not in the interim report. Mega market value 125,069,508.12 / 3.18 ILS = 39,330,034.0 exactly; TheMarker quote 3.11.2026 shows last 318.00 agorot and 125.06M | **`share_count_latest` 39,330,034 (derived, UNVERIFIED)**; the 30.6.2026 count lies between 39,245,034 and 39,330,034; TTM per-share figures use the upper bound. |
| M20 | Intangible useful life | "cut from 8 to 5 years" (change in estimate) | "no change-in-estimate disclosure found" | Note 10: 8 years in fy2023 p.97, 5 years in fy2024 p.97 and fy2025 p.98; no "שינוי באומדן" wording in any report | **Facts recorded, no claim of a formal change in estimate**; amortisation 226 -> 1,373 -> 1,892 also reflects the platform entering use. |
| M21 | Market snapshot | flagged inconsistent (3.19 vs 5.61 ILS) | flagged inconsistent | bizportal daily closes (work/paymeant/web): 4.72 ILS on 19.10.2026, 2.51 on 28.10, 3.12-3.25 on 29.10-2.11.2026; the 5.61 ILS grant price (h1_2026 p.33) is from 20.8.2026 | Snapshot is consistent with a late-October 2026 price fall of ~33%; the cause is not in the documents - UNVERIFIED, flagged for the governance/news step. |

## C. Internal inconsistencies in the filings (both extractions agree; carried as notes)

* D&A: cash-flow add-back exceeds the note charges by 197 (FY2022), -1 (FY2023), 15 (FY2024), 356 (FY2025);
  by-function depreciation (R&D + G&A) equals the cash-flow figure in FY2022, FY2024 and FY2025.
* Leases: in FY2024-FY2025 the cash-flow line 'repayment of lease liability' equals note 9 'total lease cash outflow'
  (575 / 1,017), yet note 13f shows the full 1,017 reducing the liability (936 + 2,889 - 1,017 = 2,808). FY2024 note
  13f shows (624) cash and 249 recognition versus (575) and 557 in the cash-flow statement.
* H1 2025 cash flow: no tax-paid figure despite ~6.6M paid; Q2 2025 interest received nil against 2,340 of interest
  income; the customer-credit line does not reconcile with the balance-sheet loan book for H1 2025 (B's check).
* Options: 2025 exercises 1,966,835 in note 17 versus 1,966,834 shares issued; 2024 exercises 257,475 versus 256,675
  shares listed; options outstanding 2,189,875 (note 17) versus 1,136,125 (Reg. 24A).
* Q4 2025 originations: 157 in the table (sums to 535) versus ~152 in the directors' report (fy2025 p.59).
* 1.1.2025 equity components: premium 56,549 / retained 9,611 (fy2025 p.84) versus 56,548 / 9,612 (h1_2026 p.25).
* Restated FY2023 balance sheet (fy2024 p.80): cash 15,180 + designated 1,742 = 16,922; payables 3,617 split into
  2,158 + taxes payable 1,459. Restated figures used; originals kept in `original_presentation` and `restatements`.

## D. Conventions carried into derived.py

* Cash is on the cash-flow basis (designated cash included: 31,411 at 31.12.2022).
* FY2021 has no balance sheet; working capital is rebuilt from the totals and flagged approximate.
* Maintenance capex = max(PPE purchases + capitalised development incl. capitalised SBP + ROU investment,
  D&A excluding ROU depreciation); the full lease cash-flow line is deducted in both owner-earnings measures.
