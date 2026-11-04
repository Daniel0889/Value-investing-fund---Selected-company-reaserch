# Gilat Telecom Global - reconciliation of the two financial extractions (fin_A vs fin_B)

Prepared 3.11.2026. Inputs: `fin_A.json` (statements first) and `fin_B.json` (notes and cash flow first), extracted independently from the
company's filings: `gilat_fy2023`, `gilat_fy2024`, `gilat_fy2025` (annual reports) and `gilat_h1_2026` (Q2 2026 directors' report and separate
interim data; the consolidated interim statements are not in that PDF). Output: `financials.json` (same structure as fin_A; every value has
its ref), copied to `research/gilat_telecom/financials.json`.

## 1. Method

* `recon/full_compare.py` flattens every numeric leaf of both files and pairs them: same key, key aliases (A `rnd` = B `r_and_d`, ...),
  composites (A Series C + Series D liability = B `convertibles`; A option C + option D + warrants = B `warrants_options_liabilities`; A IRU current +
  non-current = B total), and the non-period sections (quarterly tables, segments, share counts, net cash, KPIs, one-offs, backlog,
  concentration, capex and working-capital analyses). Leaves not used by any pair are listed as one-sided.
* Every difference and every one-sided figure was then checked (`recon/verify_items.py` -> `recon/discrepancies.json`):
  - **page image**: the cited PDF page was opened as an image with the Read tool in this session and its figures transcribed to
    `recon/viewed_log.md` (117 pages: gilat_fy2023 p.86, 116-118, 120-124, 138-142, 145-146, 149, 151, 157-161, 163-169; gilat_fy2024 p.82-83,
    118-120, 124-126, 140-141, 149-150, 161-163, 169-170; gilat_fy2025 p.92-94, 97-100, 125-128, 131-132, 146-160, 163-166, 172-176, 178-184, 205;
    gilat_h1_2026 p.2-4, 6-14, 19-24, 31-37). The value was matched against that transcription or the page text;
  - **arithmetic**: derived figures (sums, differences, TTM, ratios) re-computed from page-checked inputs;
  - **text layer**: narrative (non-table) figures, e.g. option grants, backlog sentences, employees.
* Real disagreements were resolved on the page; where the filings disagree with themselves the choice is stated (section 4).
* The earlier, interrupted attempt left `build_financials.py`, `recon/` and a draft `financials.json`. Its builder was re-read line by line and
  its arithmetic re-checked; it is reused with a completion-pass section added (4b). Its claims of pages "viewed" were not relied on: every
  page was opened again in this session. Its comparison had found 1 difference > 0.5%; the full comparison finds 2, plus 8 <= 0.5%.
  Its superseded report script and index are kept in `recon/superseded/` (not used).

## 2. Summary

| measure | count |
|---|---:|
| A/B pairs compared | 1,322 |
| pairs identical | 1,131 |
| pairs differing > 0.5% | 2 |
| pairs differing <= 0.5% | 8 |
| figures held by one extraction only | 502 |
| ... checked on a page image | 350 |
| ... checked by re-computation | 151 |
| ... checked on the text layer | 11 |
| agreed "not disclosed" nulls | 19 |
| figures rejected | 0 |

No figure of either extraction was found wrong on the page. The two real differences are definitional (what a line includes), and the
sub-0.5% ones are rounding or a choice between a printed total and the sum of its parts.

## 3. Matched figures that differ

| kind | item | A | B | final | check | resolution |
|---|---|---:|---:|---:|---|---|
| DIFF>0.5% | FY2021.bond_issue_proceeds | 15,317 | 17,378 | 17,378 | page image: gilat_fy2023 p.123 | gilat_fy2023 p.123 shows two Series C lines: bonds 15,317 and conversion options 2,061. A took the bond line only, B the total. FINAL 17,378 total cash raised (comparable with the single 12,381 Series D line in 2025); components kept as bond_issue_proceeds_liability_line 15,317 and bond_conversion_component_proceeds 2,061. |
| DIFF>0.5% | concentration FY2022: named customers / revenue (A amounts) vs B share | 0.2758 | 0.256 | 0.276 | arithmetic: re-computed 0.276 ((11,000 + 859) / 42,997 (amounts on gilat_fy2023 p.168)) | gilat_fy2023 p.168 prints amounts only (customer A ~11M USD, customer B 859K USD in 2022; no %). B's 0.256 = 11,000 / 42,997 (customer A alone) while its label lists both customers; A's amounts are right. FINAL: amounts 11,000 and 859; share of the two named customers 27.6% (customer A alone 25.6%). |
| diff<=0.5% | TTM.mega_crosscheck.operating_income | 39,535 | 39,534 | 39,535 | arithmetic: re-computed 39,535 (FY2025 + H1 2026 - H1 2025 EBIT (gilat_h1_2026 p.6)) | TTM EBIT built from gilat_h1_2026 p.6 = 32,981 + 19,395 - 12,841 = 39,535; Mega shows 39,534 (rounding). FINAL 39,535. |
| diff<=0.5% | quarterly 2025 FY ebitda_company (vs B annual) | 23,868 | 23,869 | 23,869 | page image: gilat_fy2025 p.92, gilat_fy2025 p.93 | gilat_fy2025 p.92 prints FY 23,869; the quarters sum to 23,868 (A summed). FINAL printed 23,869. |
| diff<=0.5% | quarterly 2025 FY satellite_lease_depreciation_company (vs B annual) | 9,082 | 9,083 | 9,083 | page image: gilat_fy2025 p.92, gilat_fy2025 p.93 | gilat_fy2025 p.92 prints FY (9,083); quarters sum to 9,082 and the ROU note (p.159) prints 9,082. FINAL 9,083 for the directors' report table; ROU-note 9,082 kept as da_rou_satellite. |
| diff<=0.5% | revtype 2022 israel_comm_internet services | 882 | 881 | 881 | page image: gilat_fy2023 p.157, gilat_fy2025 p.173, gilat_fy2024 p.161 | gilat_fy2023 p.157 prints 882 (and a 822 total typo); gilat_fy2024 p.161 prints 881, which ties to the segment note (881, gilat_fy2023 p.166) and to total revenue 42,997. FINAL 881. |
| diff<=0.5% | concentration FY2023: named customers / revenue (A amounts) vs B share | 0.3155 | 0.315 | 0.315 | arithmetic: re-computed 0.315 ((11,000 + 6,400) / 55,154) | rounding of a derived share: (11,000 + 6,400) / 55,154 = 31.5% |
| diff<=0.5% | concentration FY2024: named customers / revenue (A amounts) vs B share | 0.4167 | 0.417 | 0.417 | arithmetic: re-computed 0.417 ((10,500 + 9,400 + 9,100) / 69,592) | rounding: (10,500 + 9,400 + 9,100) / 69,592 = 41.7% |
| diff<=0.5% | concentration FY2025: named customers / revenue (A amounts) vs B share | 0.4182 | 0.418 | 0.418 | arithmetic: re-computed 0.418 ((12,400 + 19,300) / 75,793) | rounding: (12,400 + 19,300) / 75,793 = 41.8% |
| diff<=0.5% | concentration FY2021 DR Congo share | 0.4441 | 0.444 | 0.444 | arithmetic: re-computed 0.444 (23,013 / 51,816 (gilat_fy2023 p.167)) | rounding: 23,013 / 51,816 = 44.4% |

Also settled on the page (one side null, the other 0): R&D (no line, FY2021-FY2025), FY2021 goodwill impairment (no line), FY2021
government-segment D&A ('-'), FY2025 long-term-loan finance expense ('-') - all 0.

## 4. Document inconsistencies (both extractions agree; the filings disagree with themselves)

| where | issue and choice |
|---|---|
| gilat_h1_2026 p.10 vs p.31 | Series D conversion-option liability 31.12.2025 in ILS: consolidated table prints 16,351; separate statement prints 16,531 (= 5,182 USD x 3.19; gilat_fy2025 p.158 says ~16,532). Both extractions use 16,531 - kept; 16,351 is a digit transposition. |
| gilat_h1_2026 p.6 vs p.32/p.35 | H1 2026 net profit: consolidated (directors' report) 15,770; separate statement 15,261 (+ OCI 548 = TCI 15,809); note text "net profit 15,809" (= TCI). FINAL 15,770 (consolidated; also what Mega's TTM uses); 15,261 kept as alt. |
| gilat_fy2025 p.131 vs p.93 vs p.98 | FY2025 OCF: CF statement 20,533 (used); directors' FCF table 20,530; directors' liquidity table 20,611 with investing (7,156) instead of (7,078) - a 78 classification difference. Statements used. |
| gilat_fy2024 p.124 vs p.83 | FY2024 OCF: CF statement 10,587 (used); directors' FCF table 10,586 (rounding). |
| gilat_fy2023 p.118 vs p.166 | FY2023 pretax: P&L 944 (used) vs segment note 972; segment-result total printed "810,92" (= 10,928). |
| gilat_fy2023 p.118 vs p.159 | FY2023 finance: P&L expense 2,682 / income 1,448; note gross 2,913 / 1,679 (FX 231 netted in the P&L); net -1,234 either way. |
| gilat_fy2023 p.151 | Shares 31.12.2023: 58,438,636 + 6,148,754 + 4,056,402 = 68,643,792, but the note prints 68,629,480 (14,312 fewer); the printed count ties forward (+17,439,580 = 86,069,060 at 31.12.2024, gilat_fy2025 p.165). Printed count used. |
| gilat_fy2025 p.89/p.134 vs p.102 | Backlog at the FY2025 report date: 52.3M USD to 2029 (p.89, p.134) vs 58.3M USD to 2028 (p.102). 52.3 used, 58.3 kept as alt. |
| gilat_h1_2026 p.7 | H1 2025 revenue by region sums to 124,324 vs revenue 124,234 (p.6): a 90 typo in one regional figure. |
| gilat_h1_2026 p.12 vs p.14 | H1 2026 satellite segment revenue: table 119,422 (used) vs text 119,847. |
| gilat_h1_2026 p.7 | Free-capacity table: third column headed '31.12.2024' prints 784 / 3,516 / 3,100 = the 31.12.2025 figures of gilat_fy2025 p.93 (header typo). |
| gilat_fy2023 p.146 vs gilat_fy2024 p.150 | Total lease cash outflow 2023: 4,161 in the FY2023 report text vs 15,678 (principal 4,297 + interest 408 + short-term 10,973) in the FY2024/FY2025 reports; 2022: 8,224 vs 15,769. Later basis used. |
| gilat_fy2023 p.145/p.160; gilat_fy2024 p.149/p.163; gilat_fy2025 p.159/p.175 | ROU additions differ between notes in the same report: 2022 2,412 vs 1,055; 2024 23,875 / 23,528 / 24,528; 2025 3,428 vs 2,895. Not used in any valuation figure. |

## 5. Decision log carried in financials.json

| kind | period | field | A | B | final | pages | resolution |
|---|---|---|---:|---:|---:|---|---|
| DIFF>0.5% | FY2021 | bond_issue_proceeds | 15,317 | 17,378 | 17,378 | gilat_fy2023 p.123; gilat_fy2025 p.132, p.175 | Both are on the page: the 2021 CF shows two lines, Series C bonds 15,317 and Series C options 2,061. A took the first line, B the sum. Final = 17,378 total proceeds (comparable with the single FY2025 Series D line 12,381); components kept as bond_issue_proceeds_liability_line 15,317 and bond_conversion_component_proceeds 2,061. |
| diff<=0.5% | FY2023 | lease_liabilities_total | 2,764 | 2,765 | 2,765 | gilat_fy2023 p.117, p.160 | Balance-sheet lines sum to 2,765; the note prints 2,764 (rounding). Balance-sheet sum used (it is what net cash uses). |
| diff<=0.5% | FY2025 | lease_liabilities_total | 14,247 | 14,246 | 14,246 | gilat_fy2025 p.126, p.175 | Balance-sheet lines sum to 14,246; note 18b prints 14,247 (rounding). Balance-sheet sum used. |
| diff<=0.5% | FY2022 | revenue_by_type.israel_services | 882 | 881 | 881 | gilat_fy2023 p.157; gilat_fy2024 p.161 | FY2023 report prints 882 (and a 822 total typo); FY2024 report prints 881, which ties to the segment note (881) and to total revenue 42,997. 881 used. |
| internal | quarterly 2025 | ebitda_company / satellite_lease_depreciation FY | 23,868 / 9,082 (sum of quarters) | - (B has quarters only) | 23,869 / 9,083 | gilat_fy2025 p.92 | FY column printed 23,869 and (9,083); quarters sum to 1 less (rounding). Printed FY values used. |
| DIFF>0.5% | FY2022 | concentration share of named customers | 11,000 + 859 (amounts) | 0.256 | 0.276 | gilat_fy2023 p.168 | The note prints amounts only (customer A ~11M USD, customer B 859K USD). B's 0.256 = customer A alone / revenue 42,997 although its label lists both customers. Final: amounts kept; share of the two named customers 0.276 (derived), customer A alone 0.256. |
| one-sided null vs 0 | FY2021-FY2025 | rnd; FY2021 goodwill_impairment; FY2021 gov segment D&A; FY2025 LT-lo… | null | 0 | 0 | gilat_fy2023 p.118, p.167; gilat_fy2025 p.127, p.174 | No such line / '-' printed on the page: 0 (R&D marked not_presented). |
| document | FY2025_ILS | conversion_option_liability_D | 16,531 | 16,531 | 16,531 | gilat_h1_2026 p.10, p.31; gilat_fy2025 p.158 | Both extractions 16,531 (separate statement p.31; = 5,182 USD x 3.19). The consolidated table on p.10 prints 16,351 (typo). |
| document | H1_2026 | net_income | 15,770 | 15,770 | 15,770 | gilat_h1_2026 p.6, p.32, p.35 | Consolidated 15,770 kept; separate statement 15,261 and note text 15,809 (= TCI) stored as alt. |
| document | FY2025 | ocf | 20,533 | 20,533 | 20,533 | gilat_fy2025 p.131, p.93, p.98 | CF statement 20,533 kept; directors' report tables print 20,530 and 20,611 (78 classified differently). |
| added | FY2022-FY2025 | current tax assets/liabilities, contract-cost split, intangible split… | - | - | see fields | gilat_fy2023 p.116-117, p.141; gilat_fy2024 p.118-119; gilat_fy2025 p… | Read on the page images in the completion pass; needed for working capital and tangible capital in derived.py. |

## 6. Every figure held by one extraction only

Each row: the value, where it was checked, and the resolution. "kept" means the figure enters `financials.json` as extracted (A-style key).
Rows marked (composite-matched) are held by the other extraction under a different key or as a total.

### 6.1 Backlog (2)

| # | side | item | value | ref | check | resolution |
|---:|---|---|---:|---|---|---|
| 1 | A only | backlog/3/value | 2.08 | gilat_fy2025 p.100 | page image: gilat_fy2025 p.100 | kept (one extraction only; see check) |
| 2 | B only | backlog/4 | 110 | gilat_h1_2026 p.14 | page image: gilat_h1_2026 p.14 | kept (one extraction only; see check) |

### 6.2 Capex analysis (B) (14)

| # | side | item | value | ref | check | resolution |
|---:|---|---|---:|---|---|---|
| 3 | B only | capex_analysis/bezeq_iru_prepayments/FY2025 | 3,902 | gilat_fy2025 p.152 | page image: gilat_fy2025 p.152 | kept (one extraction only; see check) |
| 4 | B only | capex_analysis/bezeq_iru_prepayments/H1_2026_ILS | 10,019 | gilat_h1_2026 p.7 | page image: gilat_h1_2026 p.7 | kept (one extraction only; see check) |
| 5 | B only | capex_analysis/bezeq_iru_prepayments/amortisation_FY2025 | 1,079 | gilat_fy2025 p.152 | page image: gilat_fy2025 p.152 | kept (one extraction only; see check) |
| 6 | B only | capex_analysis/capex_above_base_maintenance_TTM_ILS | 3,005 | derived: TTM capex 10,159k ILS - base maintenance at FY2025 avg rate | arithmetic: re-computed 3,005.0 (TTM capex - base maintenance in ILS) | kept as B's analytic estimate (not a document figure); derived.py states its own maintenance-capex assumption |
| 7 | B only | capex_analysis/capex_above_base_maintenance_usd/FY2021 | -1.8 | derived: capex PPE + intangibles - base maintenance (negative = spent… | arithmetic: re-computed -1.8 (capex - B's base maintenance 2,082.8) | kept as B's analytic estimate (not a document figure); derived.py states its own maintenance-capex assumption |
| 8 | B only | capex_analysis/capex_above_base_maintenance_usd/FY2022 | -618.8 | derived: capex PPE + intangibles - base maintenance (negative = spent… | arithmetic: re-computed -618.8 (capex - B's base maintenance 2,082.8) | kept as B's analytic estimate (not a document figure); derived.py states its own maintenance-capex assumption |
| 9 | B only | capex_analysis/capex_above_base_maintenance_usd/FY2023 | 1,195.2 | derived: capex PPE + intangibles - base maintenance (negative = spent… | arithmetic: re-computed 1,195.2 (capex - B's base maintenance 2,082.8) | kept as B's analytic estimate (not a document figure); derived.py states its own maintenance-capex assumption |
| 10 | B only | capex_analysis/capex_above_base_maintenance_usd/FY2024 | 564.2 | derived: capex PPE + intangibles - base maintenance (negative = spent… | arithmetic: re-computed 564.2 (capex - B's base maintenance 2,082.8) | kept as B's analytic estimate (not a document figure); derived.py states its own maintenance-capex assumption |
| 11 | B only | capex_analysis/capex_above_base_maintenance_usd/FY2025 | -638.8 | derived: capex PPE + intangibles - base maintenance (negative = spent… | arithmetic: re-computed -638.8 (capex - B's base maintenance 2,082.8) | kept as B's analytic estimate (not a document figure); derived.py states its own maintenance-capex assumption |
| 12 | B only | capex_analysis/maintenance_estimate_usd_per_year/base | 2,082.8 | derived: avg PPE depreciation 2023-25 1,937 + avg intangible (licence… | arithmetic: re-computed 2,082.8 (B's estimate: avg PPE dep 2023-25 + avg intangible capex 2021-25) | kept as B's analytic estimate (not a document figure); derived.py states its own maintenance-capex assumption |
| 13 | B only | capex_analysis/maintenance_estimate_usd_per_year/base_in_ILS_at_3.157 | 6,575.4 | derived: base x 3.157 | arithmetic: re-computed 6,575.4 (x 3.157) | kept as B's analytic estimate (not a document figure); derived.py states its own maintenance-capex assumption |
| 14 | B only | capex_analysis/maintenance_estimate_usd_per_year/base_in_ILS_at_FY2025_avg_rate | 7,154 | derived: base x FY2025 implied average rate 3.4348 | arithmetic: re-computed 7,154.0 (x 3.4348) | kept as B's analytic estimate (not a document figure); derived.py states its own maintenance-capex assumption |
| 15 | B only | capex_analysis/maintenance_estimate_usd_per_year/high | 2,307 | derived: 2025 PPE depreciation 2,130 + 2025 licence amortisation 177 | arithmetic: re-computed 2,307 (2025 PPE dep + licence amortisation 177 (gilat_fy2025 p.150)) | kept as B's analytic estimate (not a document figure); derived.py states its own maintenance-capex assumption |
| 16 | B only | capex_analysis/maintenance_estimate_usd_per_year/low | 1,444 | derived: 2025 actual capex PPE 1,362 + intangibles 82 | arithmetic: re-computed 1,444 (2025 capex) | kept as B's analytic estimate (not a document figure); derived.py states its own maintenance-capex assumption |

### 6.3 Concentration (16)

| # | side | item | value | ref | check | resolution |
|---:|---|---|---:|---|---|---|
| 17 | A only | concentration/2/share_of_revenue | 0.199 | gilat_fy2023 p.168 | arithmetic: re-computed 0.199 (11,000 / revenue 55,154 (no % printed)) | kept (one extraction only; see check) |
| 18 | A only | concentration/3/share_of_revenue | 0.116 | gilat_fy2023 p.168 | arithmetic: re-computed 0.116 (6,400 / revenue 55,154 (no % printed)) | kept (one extraction only; see check) |
| 19 | A only | concentration/4/share_of_revenue | 0.151 | gilat_fy2024 p.170 | arithmetic: re-computed 0.151 (10,500 / revenue 69,592 (no % printed)) | kept (one extraction only; see check) |
| 20 | A only | concentration/5/share_of_revenue | 0.135 | gilat_fy2024 p.170 | arithmetic: re-computed 0.135 (9,400 / revenue 69,592 (no % printed)) | kept (one extraction only; see check) |
| 21 | A only | concentration/6/share_of_revenue | 0.131 | gilat_fy2024 p.170 | arithmetic: re-computed 0.131 (9,100 / revenue 69,592 (no % printed)) | kept (one extraction only; see check) |
| 22 | A only | concentration/7/share_of_revenue | 0.164 | gilat_fy2025 p.182 | arithmetic: re-computed 0.164 (12,400 / revenue 75,793 (no % printed)) | kept (one extraction only; see check) |
| 23 | A only | concentration/8/share_of_revenue | 0.255 | gilat_fy2025 p.182 | arithmetic: re-computed 0.255 (19,300 / revenue 75,793 (no % printed)) | kept (one extraction only; see check) |
| 24 | A only | concentration/9/revenue_usd_k/2022 | 13,485 | gilat_fy2025 p.182; gilat_fy2023 p.167; gilat_fy2024 p.126 | page image: gilat_fy2025 p.182, gilat_fy2023 p.167, gilat_fy2024 p.126 | kept (one extraction only; see check) |
| 25 | A only | concentration/9/revenue_usd_k/2023 | 12,450 | gilat_fy2025 p.182; gilat_fy2023 p.167; gilat_fy2024 p.126 | page image: gilat_fy2025 p.182, gilat_fy2023 p.167, gilat_fy2024 p.126 | kept (one extraction only; see check) |
| 26 | A only | concentration/9/revenue_usd_k/2024 | 11,101 | gilat_fy2025 p.182; gilat_fy2023 p.167; gilat_fy2024 p.126 | page image: gilat_fy2025 p.182, gilat_fy2023 p.167, gilat_fy2024 p.126 | kept (one extraction only; see check) |
| 27 | A only | concentration/9/revenue_usd_k/2025 | 12,948 | gilat_fy2025 p.182; gilat_fy2023 p.167; gilat_fy2024 p.126 | page image: gilat_fy2025 p.182, gilat_fy2023 p.167, gilat_fy2024 p.126 | kept (one extraction only; see check) |
| 28 | A only | concentration/10/share_of_revenue/2021 | 0.24 | gilat_fy2025 p.182; gilat_fy2023 p.167 | arithmetic: re-computed 0.24 (Israel 12,453 / revenue 51,816) | kept (one extraction only; see check) |
| 29 | A only | concentration/10/share_of_revenue/2022 | 0.332 | gilat_fy2025 p.182; gilat_fy2023 p.167 | arithmetic: re-computed 0.332 (Israel 14,265 / revenue 42,997) | kept (one extraction only; see check) |
| 30 | A only | concentration/10/share_of_revenue/2023 | 0.544 | gilat_fy2025 p.182; gilat_fy2023 p.167 | arithmetic: re-computed 0.544 (Israel 29,977 / revenue 55,154) | kept (one extraction only; see check) |
| 31 | A only | concentration/10/share_of_revenue/2024 | 0.721 | gilat_fy2025 p.182; gilat_fy2023 p.167 | arithmetic: re-computed 0.721 (Israel 50,181 / revenue 69,592) | kept (one extraction only; see check) |
| 32 | B only | concentration/6/share | 0.767 | gilat_h1_2026 p.4,7 | arithmetic: re-computed 0.767 (Israel H1 2026 revenue / revenue (p.7)) | kept (one extraction only; see check) |

### 6.4 Debt and covenants (29)

| # | side | item | value | ref | check | resolution |
|---:|---|---|---:|---|---|---|
| 33 | B only | debt_and_covenants/bank_debt | 0 | gilat_fy2025 p.68,158; gilat_h1_2026 p.19 | page image: gilat_fy2025 p.158, gilat_h1_2026 p.19 | kept (one extraction only; see check) |
| 34 | B only | debt_and_covenants/convertible_maturity_undiscounted_USD_k_2025_12_31/1_2y | 791 | gilat_fy2025 p.178 | page image: gilat_fy2025 p.178 | kept (one extraction only; see check) |
| 35 | B only | debt_and_covenants/convertible_maturity_undiscounted_USD_k_2025_12_31/2_3y | 4,289 | gilat_fy2025 p.178 | page image: gilat_fy2025 p.178 | kept (one extraction only; see check) |
| 36 | B only | debt_and_covenants/convertible_maturity_undiscounted_USD_k_2025_12_31/3_4y | 4,089 | gilat_fy2025 p.178 | page image: gilat_fy2025 p.178 | kept (one extraction only; see check) |
| 37 | B only | debt_and_covenants/convertible_maturity_undiscounted_USD_k_2025_12_31/gt_4y | 7,585 | gilat_fy2025 p.178 | page image: gilat_fy2025 p.178 | kept (one extraction only; see check) |
| 38 | B only | debt_and_covenants/convertible_maturity_undiscounted_USD_k_2025_12_31/lt_1y | 6,275 | gilat_fy2025 p.178 | page image: gilat_fy2025 p.178 | kept (one extraction only; see check) |
| 39 | B only | debt_and_covenants/convertible_maturity_undiscounted_USD_k_2025_12_31/total | 23,029 | gilat_fy2025 p.178 | page image: gilat_fy2025 p.178 | kept (one extraction only; see check) |
| 40 | B only | debt_and_covenants/lease_maturity_undiscounted_USD_k/2022-12-31/1_2y | 527 | gilat_fy2023 p.163 | page image: gilat_fy2023 p.163 | kept (one extraction only; see check) |
| 41 | B only | debt_and_covenants/lease_maturity_undiscounted_USD_k/2022-12-31/2_3y | 16 | gilat_fy2023 p.163 | page image: gilat_fy2023 p.163 | kept (one extraction only; see check) |
| 42 | B only | debt_and_covenants/lease_maturity_undiscounted_USD_k/2022-12-31/lt_1y | 3,787 | gilat_fy2023 p.163 | page image: gilat_fy2023 p.163 | kept (one extraction only; see check) |
| 43 | B only | debt_and_covenants/lease_maturity_undiscounted_USD_k/2022-12-31/total | 4,330 | gilat_fy2023 p.163 | page image: gilat_fy2023 p.163 | kept (one extraction only; see check) |
| 44 | B only | debt_and_covenants/lease_maturity_undiscounted_USD_k/2023-12-31/1_2y | 667 | gilat_fy2023 p.164 | page image: gilat_fy2023 p.164 | kept (one extraction only; see check) |
| 45 | B only | debt_and_covenants/lease_maturity_undiscounted_USD_k/2023-12-31/2_3y | 404 | gilat_fy2023 p.164 | page image: gilat_fy2023 p.164 | kept (one extraction only; see check) |
| 46 | B only | debt_and_covenants/lease_maturity_undiscounted_USD_k/2023-12-31/lt_1y | 1,965 | gilat_fy2023 p.164 | page image: gilat_fy2023 p.164 | kept (one extraction only; see check) |
| 47 | B only | debt_and_covenants/lease_maturity_undiscounted_USD_k/2023-12-31/total | 3,036 | gilat_fy2023 p.164 | page image: gilat_fy2023 p.164 | kept (one extraction only; see check) |
| 48 | B only | debt_and_covenants/lease_maturity_undiscounted_USD_k/2024-12-31/1_2y | 9,384 | gilat_fy2025 p.179 | page image: gilat_fy2025 p.179 | kept (one extraction only; see check) |
| 49 | B only | debt_and_covenants/lease_maturity_undiscounted_USD_k/2024-12-31/2_3y | 2,859 | gilat_fy2025 p.179 | page image: gilat_fy2025 p.179 | kept (one extraction only; see check) |
| 50 | B only | debt_and_covenants/lease_maturity_undiscounted_USD_k/2024-12-31/lt_1y | 10,582 | gilat_fy2025 p.179 | page image: gilat_fy2025 p.179 | kept (one extraction only; see check) |
| 51 | B only | debt_and_covenants/lease_maturity_undiscounted_USD_k/2024-12-31/total | 22,825 | gilat_fy2025 p.179 | page image: gilat_fy2025 p.179 | kept (one extraction only; see check) |
| 52 | B only | debt_and_covenants/lease_maturity_undiscounted_USD_k/2025-12-31/1_2y | 4,078 | gilat_fy2025 p.178 | page image: gilat_fy2025 p.178 | kept (one extraction only; see check) |
| 53 | B only | debt_and_covenants/lease_maturity_undiscounted_USD_k/2025-12-31/2_3y | 560 | gilat_fy2025 p.178 | page image: gilat_fy2025 p.178 | kept (one extraction only; see check) |
| 54 | B only | debt_and_covenants/lease_maturity_undiscounted_USD_k/2025-12-31/3_4y | 430 | gilat_fy2025 p.178 | page image: gilat_fy2025 p.178 | kept (one extraction only; see check) |
| 55 | B only | debt_and_covenants/lease_maturity_undiscounted_USD_k/2025-12-31/gt_4y | 96 | gilat_fy2025 p.178 | page image: gilat_fy2025 p.178 | kept (one extraction only; see check) |
| 56 | B only | debt_and_covenants/lease_maturity_undiscounted_USD_k/2025-12-31/lt_1y | 10,232 | gilat_fy2025 p.178 | page image: gilat_fy2025 p.178 | kept (one extraction only; see check) |
| 57 | B only | debt_and_covenants/lease_maturity_undiscounted_USD_k/2025-12-31/total | 15,396 | gilat_fy2025 p.178 | page image: gilat_fy2025 p.178 | kept (one extraction only; see check) |
| 58 | B only | debt_and_covenants/pledges | deposit ~3.5m ILS pledged for guarantees (restricted cash) | gilat_fy2025 p.158 | page image: gilat_fy2025 p.158: deposit of ~3.5M ILS pledged for guarantees | kept (one extraction only; see check) |
| 59 | B only | debt_and_covenants/series_d/issued_par | 45,872,000 | gilat_h1_2026 p.24; gilat_fy2025 p.157 | page image: gilat_h1_2026 p.24, gilat_fy2025 p.157 | kept (one extraction only; see check) |
| 60 | B only | debt_and_covenants/series_d/outstanding_2026_06_30_par | 29,839,936 | derived: 45,872,000 - 16,032,064 converted in H1 2026 | arithmetic: re-computed 29,839,936 (issued - H1 2026 conversions) | kept (one extraction only; see check) |
| 61 | B only | debt_and_covenants/short_term_lease_commitments_2025_12_31 | 1,118 | gilat_fy2025 p.160 | page image: gilat_fy2025 p.160 | kept (one extraction only; see check) |

### 6.5 FX (2)

| # | side | item | value | ref | check | resolution |
|---:|---|---|---:|---|---|---|
| 62 | A only | fx_implied/avg_H2_2025 | 3.302 | gilat_h1_2026 p.6; gilat_fy2025 p.92, p.127 | arithmetic: re-computed 3.3023 ((FY2025 ILS - H1 2025 ILS revenue) / (FY - H1 USD revenue)) | kept (one extraction only; see check) |
| 63 | B only | fx/Q2_2025_avg | 3.579 | derived: Q2 2025 revenue ILS / USD | arithmetic: re-computed 3.5786 (Q2 2025 revenue ILS 66,508 / USD 18,585) | kept (one extraction only; see check) |

### 6.6 KPIs (16)

| # | side | item | value | ref | check | resolution |
|---:|---|---|---:|---|---|---|
| 64 | A only | isp subscribers 2024-12-31 | 6,566 | gilat_fy2025 p.94; gilat_h1_2026 p.8 | page image: gilat_fy2025 p.94, gilat_h1_2026 p.8 | kept (one extraction only; see check) |
| 65 | A only | isp arpu FY2024 | 87.8 | gilat_fy2025 p.94; gilat_h1_2026 p.8 | page image: gilat_fy2025 p.94, gilat_h1_2026 p.8 | kept (one extraction only; see check) |
| 66 | A only | avg supplier credit FY2025 | 19,100 | gilat_fy2025 p.99; gilat_h1_2026 p.14 | page image: gilat_fy2025 p.99, gilat_h1_2026 p.14 | kept (one extraction only; see check) |
| 67 | A only | avg customer credit FY2025 | 18,121 | gilat_fy2025 p.99; gilat_h1_2026 p.14 | page image: gilat_fy2025 p.99, gilat_h1_2026 p.14 | kept (one extraction only; see check) |
| 68 | A only | kpis/free_satellite_capacity/MHz/2023 | 822 | gilat_fy2025 p.93; gilat_h1_2026 p.7 | page image: gilat_fy2025 p.93, gilat_h1_2026 p.7 | kept (one extraction only; see check) |
| 69 | A only | kpis/free_satellite_capacity/MHz/2024 | 672 | gilat_fy2025 p.93; gilat_h1_2026 p.7 | page image: gilat_fy2025 p.93, gilat_h1_2026 p.7 | kept (one extraction only; see check) |
| 70 | A only | kpis/free_satellite_capacity/MHz/2025 | 784 | gilat_fy2025 p.93; gilat_h1_2026 p.7 | page image: gilat_fy2025 p.93, gilat_h1_2026 p.7 | kept (one extraction only; see check) |
| 71 | A only | kpis/free_satellite_capacity/MHz/2026-06-30 | 1,068 | gilat_fy2025 p.93; gilat_h1_2026 p.7 | page image: gilat_fy2025 p.93, gilat_h1_2026 p.7 | kept (one extraction only; see check) |
| 72 | A only | kpis/free_satellite_capacity/Mbps/2023 | 1,577 | gilat_fy2025 p.93; gilat_h1_2026 p.7 | page image: gilat_fy2025 p.93, gilat_h1_2026 p.7 | kept (one extraction only; see check) |
| 73 | A only | kpis/free_satellite_capacity/Mbps/2024 | 3,325 | gilat_fy2025 p.93; gilat_h1_2026 p.7 | page image: gilat_fy2025 p.93, gilat_h1_2026 p.7 | kept (one extraction only; see check) |
| 74 | A only | kpis/free_satellite_capacity/Mbps/2025 | 3,516 | gilat_fy2025 p.93; gilat_h1_2026 p.7 | page image: gilat_fy2025 p.93, gilat_h1_2026 p.7 | kept (one extraction only; see check) |
| 75 | A only | kpis/free_satellite_capacity/Mbps/2026-06-30 | 4,362 | gilat_fy2025 p.93; gilat_h1_2026 p.7 | page image: gilat_fy2025 p.93, gilat_h1_2026 p.7 | kept (one extraction only; see check) |
| 76 | A only | kpis/free_satellite_capacity/O3B/2023 | 660 | gilat_fy2025 p.93; gilat_h1_2026 p.7 | page image: gilat_fy2025 p.93, gilat_h1_2026 p.7 | kept (one extraction only; see check) |
| 77 | A only | kpis/free_satellite_capacity/O3B/2024 | 1,700 | gilat_fy2025 p.93; gilat_h1_2026 p.7 | page image: gilat_fy2025 p.93, gilat_h1_2026 p.7 | kept (one extraction only; see check) |
| 78 | A only | kpis/free_satellite_capacity/O3B/2025 | 3,100 | gilat_fy2025 p.93; gilat_h1_2026 p.7 | page image: gilat_fy2025 p.93, gilat_h1_2026 p.7 | kept (one extraction only; see check) |
| 79 | A only | kpis/free_satellite_capacity/O3B/2026-06-30 | 2,220 | gilat_fy2025 p.93; gilat_h1_2026 p.7 | page image: gilat_fy2025 p.93, gilat_h1_2026 p.7 | kept (one extraction only; see check) |

### 6.7 Net cash (31)

| # | side | item | value | ref | check | resolution |
|---:|---|---|---:|---|---|---|
| 80 | A only | net cash incl leases 2021-12-31 | -9,268 | gilat_fy2023 p.123, p.160 | arithmetic: re-computed -9,268 (net cash 554 - leases 9,822) | kept (one extraction only; see check) |
| 81 | B only | option liabilities 2021-12-31 | 451 |  | arithmetic: re-computed 451 (Series C option 451 (gilat_fy2023 p.160, 1.1.2022 balance)) | kept (one extraction only; see check) |
| 82 | A only | net cash incl leases 2022-12-31 | -3,236 | gilat_fy2023 p.116-117 | arithmetic: re-computed -3,236 (net cash 877 - leases 4,113) | kept (one extraction only; see check) |
| 83 | A only | cash+deposits 2022-12-31 | 14,880 | gilat_fy2023 p.116-117 | arithmetic: re-computed 14,880 (cash + ST deposits (gilat_fy2023 p.116)) | kept (one extraction only; see check) |
| 84 | A only | financial debt excl leases 2022-12-31 | 14,003 | gilat_fy2023 p.116-117 | arithmetic: re-computed 14,003 (ST credit + state loan + Series C) | kept (one extraction only; see check) |
| 85 | B only | option liabilities 2022-12-31 | 45 |  | arithmetic: re-computed 45 (Series C option 30 + warrants 15 (gilat_fy2023 p.117)) | kept (one extraction only; see check) |
| 86 | B only | restricted cash 2022-12-31 | 72 |  | arithmetic: re-computed 72 (gilat_fy2023 p.116) | kept (one extraction only; see check) |
| 87 | A only | net cash incl leases 2023-12-31 | -1,201 | gilat_fy2024 p.118-119 | arithmetic: re-computed -1,201 (net cash 1,564 - leases 2,765) | kept (one extraction only; see check) |
| 88 | A only | cash+deposits 2023-12-31 | 12,215 | gilat_fy2024 p.118-119 | arithmetic: re-computed 12,215 (cash (no deposits)) | kept (one extraction only; see check) |
| 89 | A only | financial debt excl leases 2023-12-31 | 10,651 | gilat_fy2024 p.118-119 | arithmetic: re-computed 10,651 (state loan + Series C) | kept (one extraction only; see check) |
| 90 | B only | option liabilities 2023-12-31 | 272 |  | arithmetic: re-computed 272 (Series C option 196 + warrants 76 (gilat_fy2023 p.117)) | kept (one extraction only; see check) |
| 91 | B only | restricted cash 2023-12-31 | 71 |  | arithmetic: re-computed 71 (gilat_fy2023 p.116) | kept (one extraction only; see check) |
| 92 | A only | net cash incl leases 2024-12-31 | -18,027 | gilat_fy2024 p.118-119 | arithmetic: re-computed -18,027 (net cash 2,546 - leases 20,573) | kept (one extraction only; see check) |
| 93 | A only | cash+deposits 2024-12-31 | 11,017 | gilat_fy2024 p.118-119 | arithmetic: re-computed 11,017 (cash (no deposits)) | kept (one extraction only; see check) |
| 94 | A only | financial debt excl leases 2024-12-31 | 8,471 | gilat_fy2024 p.118-119 | arithmetic: re-computed 8,471 (state loan + bank loan + Series C) | kept (one extraction only; see check) |
| 95 | B only | option liabilities 2024-12-31 | 612 |  | arithmetic: re-computed 612 (Series C option 483 + warrants 129 (gilat_fy2024 p.119)) | kept (one extraction only; see check) |
| 96 | B only | restricted cash 2024-12-31 | 78 |  | arithmetic: re-computed 78 (gilat_fy2024 p.118) | kept (one extraction only; see check) |
| 97 | A only | cash+deposits 2025-12-31 | 29,753 | gilat_fy2025 p.125-126 | arithmetic: re-computed 29,753 (cash + ST deposits (gilat_fy2025 p.125)) | kept (one extraction only; see check) |
| 98 | A only | financial debt excl leases 2025-12-31 | 16,625 | gilat_fy2025 p.125-126 | arithmetic: re-computed 16,625 (Series C + Series D) | kept (one extraction only; see check) |
| 99 | B only | option liabilities 2025-12-31 | 5,497 |  | arithmetic: re-computed 5,497 (Series C option 315 + Series D option 5,182 (gilat_fy2025 p.126)) | kept (one extraction only; see check) |
| 100 | B only | restricted cash 2025-12-31 | 1,097 |  | arithmetic: re-computed 1,097 (gilat_fy2025 p.125) | kept (one extraction only; see check) |
| 101 | A only | cash+deposits 2026-06-30 | 92,955 | gilat_h1_2026 p.9-10, p.19 | arithmetic: re-computed 92,955 (cash (no deposits) (gilat_h1_2026 p.9)) | kept (one extraction only; see check) |
| 102 | A only | financial debt excl leases 2026-06-30 | 26,513 | gilat_h1_2026 p.9-10, p.19 | arithmetic: re-computed 26,513 (Series C + Series D) | kept (one extraction only; see check) |
| 103 | B only | restricted cash 2026-06-30 | 3,500 |  | arithmetic: re-computed 3,500 (gilat_h1_2026 p.19) | kept (one extraction only; see check) |
| 104 | B only | net cash 2025-06-30 (B only) | 11,435 | derived: 66,702 - (Series C 19,480 + Series D 35,305 + bank 482) (gil… | arithmetic: re-computed 11,435 (cash - Series C - Series D - bank loan (gilat_h1_2026 p.9)) | kept (one extraction only; see check) |
| 105 | B only | net_cash/FY2022/lt_supplier_liability | 40 |  | arithmetic: re-computed 40 (LT suppliers 40 (gilat_fy2023 p.117)) | kept (one extraction only; see check) |
| 106 | B only | net_cash/H1_2025_ILS/leases | 61,994 |  | arithmetic: re-computed 61,994 (lease current + non-current (p.9-10)) | kept (one extraction only; see check) |
| 107 | B only | net_cash/H1_2025_ILS/option_liabilities | 17,450 |  | arithmetic: re-computed 17,450 (warrants + C option + D option (p.9-10)) | kept (one extraction only; see check) |
| 108 | B only | net_cash/H1_2026_ILS/as_converted_view/extra_shares_at_2026_06_30 | 31,488,079 | derived: Series D par 29,839,936 at 1.00 + Series C public par 2,224,… | arithmetic: re-computed 31,488,079 (D par + public C par / 1.35) | kept (one extraction only; see check) |
| 109 | B only | net_cash/H1_2026_ILS/as_converted_view/net_cash_if_all_converted | 92,955 | derived: cash 92,955 with no bond debt | arithmetic: re-computed 92,955 (cash, no bond debt) | kept (one extraction only; see check) |
| 110 | B only | net_cash/H1_2026_ILS/net_cash_bonds_at_par | 60,890.1 | derived: cash - Series D par 29,839,936 (45,872,000 - 16,032,064) - S… | arithmetic: re-computed 60,890.1 (cash - D par - public C par) | kept (one extraction only; see check) |

### 6.8 One-offs (12)

| # | side | item | value | ref | check | resolution |
|---:|---|---|---:|---|---|---|
| 111 | A only | one_offs/4/amount_usd_k | 2,081 | gilat_fy2023 p.122 | page image: gilat_fy2023 p.122 | kept (one extraction only; see check) |
| 112 | A only | one_offs/7/amount_usd_k | -401 | gilat_fy2023 p.138 | page image: gilat_fy2023 p.138 | kept (one extraction only; see check) |
| 113 | A only | one_offs/11/amount_usd_k | 2,400 | gilat_fy2024 p.83 | page image: gilat_fy2024 p.83: '~2.4 million USD prepaid in Q2 2024, ~1.8M of it for 2025-2027' = 2,400 USD k | kept (one extraction only; see check) |
| 114 | A only | one_offs/13/amount_usd_k | 1,693 | gilat_fy2025 p.93, p.131 | page image: gilat_fy2025 p.93, gilat_fy2025 p.131 | kept (one extraction only; see check) |
| 115 | A only | one_offs/16/amount_usd_k | 1,063 | gilat_fy2025 p.174 | arithmetic: re-computed 1,063 (FX income - FX expense 2025 (gilat_fy2025 p.174)) | kept (one extraction only; see check) |
| 116 | B only | one_offs/4 | -437 | gilat_fy2023 p.122 | arithmetic: re-computed -437 (option revaluation gains: non-tradable 13 + Series B 23 + Series C 401 (gilat_fy2023 p.12… | kept (one extraction only; see check) |
| 117 | B only | one_offs/7 | 18,830 | gilat_fy2023 p.86,125 | page image: gilat_fy2023 p.86 | kept (one extraction only; see check) |
| 118 | B only | one_offs/9 | 9,400 | gilat_fy2024 p.170; gilat_fy2025 p.91 | page image: gilat_fy2024 p.170: second major customer (Israel internet) ~9.4M USD = 9,400 USD k | kept (one extraction only; see check) |
| 119 | B only | one_offs/11 | 2,162 | gilat_fy2025 p.131,93 | arithmetic: re-computed 2,162 (Series D option loss - Series C option gain - warrants gain (p.131)) | kept (one extraction only; see check) |
| 120 | B only | one_offs/12 | -2,331 | gilat_fy2025 p.131 | page image: gilat_fy2025 p.131 | kept (one extraction only; see check) |
| 121 | B only | one_offs/14 | - | gilat_h1_2026 p.12; gilat_fy2025 p.134 | page image: explicit null: not disclosed in the supplied documents (no consolidated interim statements in gilat_h1_2026) | kept as not_in_documents |
| 122 | B only | one_offs/15 | - | gilat_h1_2026 p.6 | page image: explicit null: not disclosed in the supplied documents (no consolidated interim statements in gilat_h1_2026) | kept as not_in_documents |

### 6.9 Period tables (243)

| # | side | item | value | ref | check | resolution |
|---:|---|---|---:|---|---|---|
| 123 | B only | FY2021.rnd | 0 | gilat_fy2023 p.118 | page image: gilat_fy2023 p.118 | no R&D line in the P&L (A: not_presented; B: 0). FINAL 0 (not presented). |
| 124 | A only | FY2021.eps_diluted_usd | -0.093 | gilat_fy2023 p.118 | page image: gilat_fy2023 p.118 | kept (one extraction only; see check) |
| 125 | A only | FY2021.credit_losses_in_ga | 3,191 | gilat_fy2023 p.158 | page image: gilat_fy2023 p.158 | kept (one extraction only; see check) |
| 126 | B only | FY2021.goodwill_impairment | 0 | gilat_fy2023 p.142 | page image: gilat_fy2023 p.142, gilat_fy2023 p.118 | no impairment line in the 2021 P&L (gilat_fy2023 p.118); goodwill 4,428 at 1.1.2022 = cost 5,738 - old impairment 1,310 (p.141). A left it null, B 0. FINAL 0. |
| 127 | A only | FY2021.ocf_before_tax_paid | 14,118 | gilat_fy2023 p.122 | page image: gilat_fy2023 p.122 | kept (one extraction only; see check) |
| 128 | A only | FY2021.bond_conversion_component_proceeds | 2,061 | gilat_fy2023 p.123 | page image: gilat_fy2023 p.123 | kept (one extraction only; see check) |
| 129 | A only | FY2021.series_B_principal_repaid | 8,842 | gilat_fy2023 p.123 | page image: gilat_fy2023 p.123 | kept (one extraction only; see check) |
| 130 | A only | FY2021.series_F_convertible_principal_repaid | 1,642 | gilat_fy2023 p.123 | page image: gilat_fy2023 p.123 | kept (one extraction only; see check) |
| 131 | A only | FY2021.investing_cf | 9,714 | gilat_fy2023 p.123 | page image: gilat_fy2023 p.123 | kept (one extraction only; see check) |
| 132 | A only | FY2021.financing_cf | -7,982 | gilat_fy2023 p.123 | page image: gilat_fy2023 p.123 | kept (one extraction only; see check) |
| 133 | A only | FY2021.fx_effect_on_cash | 605 | gilat_fy2023 p.123 | page image: gilat_fy2023 p.123 | kept (one extraction only; see check) |
| 134 | A only | FY2021.st_deposits | 0 | gilat_fy2023 p.116, p.122-123 | arithmetic: re-computed 0 (no deposit line in 2021; 4,026 placed in 2022 (gilat_fy2023 p.123)) | kept (one extraction only; see check) |
| 135 | A only | FY2021.restricted_cash | 1,836 | gilat_fy2023 p.116, p.123 | arithmetic: re-computed 1,836 (31.12.2022 restricted 72 (p.116) + 1,764 released in 2022 (p.123)) | kept (one extraction only; see check) |
| 136 | A only | FY2021.goodwill | 4,428 | gilat_fy2023 p.141 | page image: gilat_fy2023 p.141 | kept (one extraction only; see check) |
| 137 | B only | FY2022.rnd | 0 | gilat_fy2023 p.118 | page image: gilat_fy2023 p.118 | no R&D line. FINAL 0 (not presented). |
| 138 | A only | FY2022.oci | -9 | gilat_fy2023 p.118 | page image: gilat_fy2023 p.118 | kept (one extraction only; see check) |
| 139 | A only | FY2022.eps_diluted_usd | -0.07 | gilat_fy2023 p.118 | page image: gilat_fy2023 p.118 | kept (one extraction only; see check) |
| 140 | A only | FY2022.da_rou_satellite | 7,276 | gilat_fy2023 p.145 | page image: gilat_fy2023 p.145 | kept (one extraction only; see check) |
| 141 | A only | FY2022.credit_losses_in_ga | 310 | gilat_fy2023 p.158 | page image: gilat_fy2023 p.158 | kept (one extraction only; see check) |
| 142 | A only | FY2022.receivables_impairment_loss | 328 | gilat_fy2023 p.138 | page image: gilat_fy2023 p.138 | kept (one extraction only; see check) |
| 143 | A only | FY2022.ocf_before_tax_paid | 10,256 | gilat_fy2023 p.122 | page image: gilat_fy2023 p.122 | kept (one extraction only; see check) |
| 144 | A only | FY2022.investing_cf | -3,726 | gilat_fy2023 p.123 | page image: gilat_fy2023 p.123 | kept (one extraction only; see check) |
| 145 | A only | FY2022.financing_cf | -14,640 | gilat_fy2023 p.123 | page image: gilat_fy2023 p.123 | kept (one extraction only; see check) |
| 146 | A only | FY2022.fx_effect_on_cash | -2,081 | gilat_fy2023 p.123 | page image: gilat_fy2023 p.123 | kept (one extraction only; see check) |
| 147 | A only | FY2022.total_current_assets | 22,201 | gilat_fy2023 p.116 | page image: gilat_fy2023 p.116 | kept (one extraction only; see check) |
| 148 | A only | FY2022.deferred_tax_assets | 154 | gilat_fy2023 p.116 | page image: gilat_fy2023 p.116 | kept (one extraction only; see check) |
| 149 | A only | FY2022.lease_liabilities_total | 4,113 | gilat_fy2023 p.160 | page image: gilat_fy2023 p.160 | kept (one extraction only; see check) |
| 150 | A only | FY2022.total_current_liabilities | 22,734 | gilat_fy2023 p.117 | page image: gilat_fy2023 p.117 | kept (one extraction only; see check) |
| 151 | A only | FY2022.total_liabilities | 34,794 | gilat_fy2023 p.117 | page image: gilat_fy2023 p.117 | kept (one extraction only; see check) |
| 152 | B only | FY2023.rnd | 0 | gilat_fy2023 p.118 | page image: gilat_fy2023 p.118 | no R&D line. FINAL 0 (not presented). |
| 153 | A only | FY2023.oci | 10 | gilat_fy2023 p.118 | page image: gilat_fy2023 p.118 | kept (one extraction only; see check) |
| 154 | A only | FY2023.eps_diluted_usd | 0.011 | gilat_fy2023 p.118 | page image: gilat_fy2023 p.118 | kept (one extraction only; see check) |
| 155 | A only | FY2023.da_rou_satellite | 3,717 | gilat_fy2023 p.145 | page image: gilat_fy2023 p.145 | kept (one extraction only; see check) |
| 156 | A only | FY2023.credit_losses_in_ga | 224 | gilat_fy2023 p.158 | page image: gilat_fy2023 p.158 | kept (one extraction only; see check) |
| 157 | A only | FY2023.receivables_impairment_loss | 363 | gilat_fy2023 p.138 | page image: gilat_fy2023 p.138 | kept (one extraction only; see check) |
| 158 | A only | FY2023.ocf_before_tax_paid | 9,591 | gilat_fy2023 p.122 | page image: gilat_fy2023 p.122 | kept (one extraction only; see check) |
| 159 | A only | FY2023.investing_cf | 594 | gilat_fy2023 p.123 | page image: gilat_fy2023 p.123 | kept (one extraction only; see check) |
| 160 | A only | FY2023.financing_cf | -7,459 | gilat_fy2023 p.123 | page image: gilat_fy2023 p.123 | kept (one extraction only; see check) |
| 161 | A only | FY2023.fx_effect_on_cash | -535 | gilat_fy2023 p.123 | page image: gilat_fy2023 p.123 | kept (one extraction only; see check) |
| 162 | A only | FY2023.total_current_assets | 25,149 | gilat_fy2023 p.116 | page image: gilat_fy2023 p.116 | kept (one extraction only; see check) |
| 163 | A only | FY2023.deferred_tax_assets | 0 | gilat_fy2023 p.116 | page image: gilat_fy2023 p.116 | kept (one extraction only; see check) |
| 164 | A only | FY2023.lease_liabilities_total | 2,764 | gilat_fy2023 p.160 | page image: gilat_fy2023 p.160 | BS lines 1,832 + 933 = 2,765 (gilat_fy2023 p.117); note 17 prints 2,764 (p.160). FINAL 2,765 (what net cash uses); 2,764 kept as alt. |
| 165 | A only | FY2023.total_current_liabilities | 33,616 | gilat_fy2024 p.119 | page image: gilat_fy2024 p.119 | first reported 25,506 (gilat_fy2023 p.117); restated 33,616 for the IAS 1 amendment (Series C wholly current) in gilat_fy2024 p.119. FINAL 33,616 (restated), 2… |
| 166 | A only | FY2023.total_liabilities | 34,850 | gilat_fy2023 p.117 | page image: gilat_fy2023 p.117 | kept (one extraction only; see check) |
| 167 | A only | FY2023.finance_expense_detail.gross_total_in_note | 2,913 | gilat_fy2023 p.159 | page image: gilat_fy2023 p.159 | kept (one extraction only; see check) |
| 168 | B only | FY2024.rnd | 0 | gilat_fy2024 p.120 | page image: gilat_fy2024 p.120 | no R&D line. FINAL 0 (not presented). |
| 169 | A only | FY2024.oci | 16 | gilat_fy2024 p.120 | page image: gilat_fy2024 p.120 | kept (one extraction only; see check) |
| 170 | A only | FY2024.da_rou_satellite | 6,285 | gilat_fy2024 p.149 | page image: gilat_fy2024 p.149 | kept (one extraction only; see check) |
| 171 | A only | FY2024.credit_losses_in_ga | 127 | gilat_fy2024 p.162 | page image: gilat_fy2024 p.162 | kept (one extraction only; see check) |
| 172 | A only | FY2024.receivables_impairment_loss | 182 | gilat_fy2024 p.141 | page image: gilat_fy2024 p.141 | kept (one extraction only; see check) |
| 173 | A only | FY2024.ocf_before_tax_paid | 10,599 | gilat_fy2024 p.124 | page image: gilat_fy2024 p.124 | kept (one extraction only; see check) |
| 174 | A only | FY2024.capitalised_contract_costs | 1,127 | gilat_fy2024 p.124 | page image: gilat_fy2024 p.124 | kept (one extraction only; see check) |
| 175 | A only | FY2024.investing_cf | -2,647 | gilat_fy2024 p.125 | page image: gilat_fy2024 p.125 | kept (one extraction only; see check) |
| 176 | A only | FY2024.financing_cf | -8,977 | gilat_fy2024 p.125 | page image: gilat_fy2024 p.125 | kept (one extraction only; see check) |
| 177 | A only | FY2024.fx_effect_on_cash | -161 | gilat_fy2024 p.125 | page image: gilat_fy2024 p.125 | kept (one extraction only; see check) |
| 178 | A only | FY2024.total_current_assets | 26,793 | gilat_fy2024 p.118 | page image: gilat_fy2024 p.118 | kept (one extraction only; see check) |
| 179 | A only | FY2024.deferred_tax_assets | 208 | gilat_fy2024 p.118 | page image: gilat_fy2024 p.118 | kept (one extraction only; see check) |
| 180 | A only | FY2024.lease_liabilities_total | 20,573 | gilat_fy2024 p.163 | page image: gilat_fy2024 p.163 | kept (one extraction only; see check) |
| 181 | A only | FY2024.total_current_liabilities | 36,485 | gilat_fy2024 p.119 | page image: gilat_fy2024 p.119 | kept (one extraction only; see check) |
| 182 | A only | FY2024.total_liabilities | 49,483 | gilat_fy2024 p.119 | page image: gilat_fy2024 p.119 | kept (one extraction only; see check) |
| 183 | A only | FY2024.option_revaluation_loss_company | 465 | gilat_fy2024 p.82 | page image: gilat_fy2024 p.82 | kept (one extraction only; see check) |
| 184 | B only | FY2025.rnd | 0 | gilat_fy2025 p.127 | page image: gilat_fy2025 p.127 | no R&D line. FINAL 0 (not presented). |
| 185 | A only | FY2025.oci | 24 | gilat_fy2025 p.127 | page image: gilat_fy2025 p.127 | kept (one extraction only; see check) |
| 186 | A only | FY2025.da_rou_satellite | 9,082 | gilat_fy2025 p.159 | page image: gilat_fy2025 p.159 | kept (one extraction only; see check) |
| 187 | A only | FY2025.credit_losses_in_ga | 325 | gilat_fy2025 p.174 | page image: gilat_fy2025 p.174 | kept (one extraction only; see check) |
| 188 | A only | FY2025.receivables_impairment_loss | 498 | gilat_fy2025 p.147 | page image: gilat_fy2025 p.147 | kept (one extraction only; see check) |
| 189 | A only* | FY2025.option_revaluation_loss_company | 1,693 | gilat_fy2025 p.93 | page image: gilat_fy2025 p.93 | agreed: B holds 1,693 as option_revaluation_noncash.company_non_gaap_addback |
| 190 | A only | FY2025.ocf_before_tax_paid | 21,165 | gilat_fy2025 p.131 | page image: gilat_fy2025 p.131 | kept (one extraction only; see check) |
| 191 | A only | FY2025.capitalised_contract_costs | -973 | gilat_fy2025 p.131 | page image: gilat_fy2025 p.131 | kept (one extraction only; see check) |
| 192 | A only | FY2025.investing_cf | -7,078 | gilat_fy2025 p.132 | page image: gilat_fy2025 p.132 | kept (one extraction only; see check) |
| 193 | A only | FY2025.financing_cf | -1,767 | gilat_fy2025 p.132 | page image: gilat_fy2025 p.132 | kept (one extraction only; see check) |
| 194 | A only | FY2025.fx_effect_on_cash | 2,331 | gilat_fy2025 p.132 | page image: gilat_fy2025 p.132 | kept (one extraction only; see check) |
| 195 | A only* | FY2025.deferred_expenses_iru_current | 1,112 | gilat_fy2025 p.125 | page image: gilat_fy2025 p.125 | agreed: B holds the total 2,823 = 1,112 + 1,711 (deferred_expenses_iru) |
| 196 | A only* | FY2025.deferred_expenses_iru_noncurrent | 1,711 | gilat_fy2025 p.125 | page image: gilat_fy2025 p.125 | agreed: B holds the total 2,823 = 1,112 + 1,711 (deferred_expenses_iru) |
| 197 | A only | FY2025.total_current_assets | 52,669 | gilat_fy2025 p.125 | page image: gilat_fy2025 p.125 | kept (one extraction only; see check) |
| 198 | A only | FY2025.deferred_tax_assets | 807 | gilat_fy2025 p.125 | page image: gilat_fy2025 p.125 | kept (one extraction only; see check) |
| 199 | A only | FY2025.lease_liabilities_total | 14,247 | gilat_fy2025 p.175 | page image: gilat_fy2025 p.175 | BS lines 9,304 + 4,942 = 14,246 (gilat_fy2025 p.126); note 18 prints 14,247 (p.175). FINAL 14,246; 14,247 kept as alt. |
| 200 | A only | FY2025.total_current_liabilities | 54,543 | gilat_fy2025 p.126 | page image: gilat_fy2025 p.126 | kept (one extraction only; see check) |
| 201 | A only | FY2025.total_liabilities | 59,485 | gilat_fy2025 p.126 | page image: gilat_fy2025 p.126 | kept (one extraction only; see check) |
| 202 | A only | FY2025.prepaid_expenses_company | 2,929 | gilat_fy2025 p.93 | page image: gilat_fy2025 p.93 | kept (one extraction only; see check) |
| 203 | B only | FY2025.finance_expense_detail.long_term_loan | 0 | gilat_fy2025 p.174 | page image: gilat_fy2025 p.174 | gilat_fy2025 p.174 prints '-' for 2025 (10 in 2024). FINAL 0. |
| 204 | A only | FY2025_ILS.net_income_owners | 21,259 | gilat_h1_2026 p.32 | page image: gilat_h1_2026 p.32 | kept (one extraction only; see check) |
| 205 | A only | FY2025_ILS.total_noncurrent_liabilities | 15,765 | gilat_h1_2026 p.10 | page image: gilat_h1_2026 p.10 | kept (one extraction only; see check) |
| 206 | A only | H1_2025.total_noncurrent_liabilities | 30,766 | gilat_h1_2026 p.10 | page image: gilat_h1_2026 p.10 | kept (one extraction only; see check) |
| 207 | A only | H1_2025.total_assets | 271,205 | gilat_h1_2026 p.9-10 | arithmetic: re-computed 271,205 (equity + current + non-current liabilities (gilat_h1_2026 p.9-10)) | kept (one extraction only; see check) |
| 208 | A only | H1_2025_USD.option_revaluation_loss_company | 1,642 | gilat_fy2025 p.92-93 | arithmetic: re-computed 1,642 (Q1 + Q2 2025) | kept (one extraction only; see check) |
| 209 | A only | Q2_2025.da_total_derived | 12,336 | gilat_h1_2026 p.7; gilat_h1_2026 p.6 | arithmetic: re-computed 12,336 (EBITDA 19,611 - EBIT 7,275 (gilat_h1_2026 p.6)) | kept (one extraction only; see check) |
| 210 | A only | Q2_2025_USD.option_revaluation_loss_company | 2,008 | gilat_fy2025 p.92-93 | page image: gilat_fy2025 p.92, gilat_fy2025 p.93 | kept (one extraction only; see check) |
| 211 | A only | Q2_2026.da_total_derived | 12,663 | gilat_h1_2026 p.7; gilat_h1_2026 p.6 | arithmetic: re-computed 12,663 (EBITDA 22,649 - EBIT 9,986 (gilat_h1_2026 p.6)) | kept (one extraction only; see check) |
| 212 | A only | H1_2026.total_comprehensive_income | 15,809 | gilat_h1_2026 p.32 | page image: gilat_h1_2026 p.32 | kept (one extraction only; see check) |
| 213 | A only | H1_2026.share_issue_proceeds | 0 | gilat_h1_2026 p.34 | page image: gilat_h1_2026 p.34 | kept (one extraction only; see check) |
| 214 | A only | H1_2026.bond_principal_repaid_parent | 4,972 | gilat_h1_2026 p.34 | page image: gilat_h1_2026 p.34 | kept (one extraction only; see check) |
| 215 | A only | H1_2026.employee_benefit_assets | 274 | gilat_h1_2026 p.19 | page image: gilat_h1_2026 p.19 | kept (one extraction only; see check) |
| 216 | A only | H1_2026.contract_costs_capitalised_noncurrent | 0 | gilat_h1_2026 p.9 | page image: gilat_h1_2026 p.9 | kept (one extraction only; see check) |
| 217 | A only | H1_2026.current_tax_liabilities | 121 | gilat_h1_2026 p.19 | page image: gilat_h1_2026 p.19 | kept (one extraction only; see check) |
| 218 | A only | H1_2026.series_C_market_value_at_2026-08-19 | 10,164 | gilat_h1_2026 p.22 | page image: gilat_h1_2026 p.22 | kept (one extraction only; see check) |
| 219 | A only | H1_2026.series_D_market_value_at_2026-08-19 | 61,736 | gilat_h1_2026 p.24 | page image: gilat_h1_2026 p.24 | kept (one extraction only; see check) |
| 220 | A only | H1_2026.series_D_implied_price_per_conversion_share_ils | 2.119 | gilat_h1_2026 p.24 | arithmetic: re-computed 2.119 (market value 61,736K / 29,134,661 NV (p.24)) | kept (one extraction only; see check) |
| 221 | A only | H1_2026.total_liabilities | 142,111 | gilat_h1_2026 p.9-10 | arithmetic: re-computed 142,111 (current + non-current (gilat_h1_2026 p.9-10)) | kept (one extraction only; see check) |
| 222 | A only | H1_2026.lease_liabilities_total | 33,116 | gilat_h1_2026 p.9-10 | arithmetic: re-computed 33,116 (current + non-current (gilat_h1_2026 p.9-10)) | kept (one extraction only; see check) |
| 223 | A only | TTM_2026-06-30.net_income_alt_solo | 32,476 | gilat_h1_2026 p.6, p.32 | arithmetic: re-computed 32,476 (FY2025 21,259 + solo H1 2026 15,261 - H1 2025 4,044) | kept (one extraction only; see check) |
| 224 | B only | H1_2025.shares_outstanding_end | 86,077,313 | derived: 31.12.2024 86,069,060 (gilat_fy2025 p.165) + ~8,253 = 7,868,… | arithmetic: re-computed 86,077,313 (APPROXIMATION (UNVERIFIED)) | B's approximation (31.12.2024 count + ~8,253 shares inferred from the ILS share-capital line). No share count at 30.6.2025 is printed in the supplied documents… |
| 225 | B only | FY2021.ebitda (operating income + D&A) | 15,609 | derived: operating income -2,731 + D&A 18,340 | arithmetic: re-computed 15,609 (EBIT -2,731 + CF D&A 18,340 (gilat_fy2023 p.118, p.122)) | kept (one extraction only; see check) |
| 226 | B only | FY2021 ROU additions (B only) | 3,383 | gilat_fy2023 p.160 | page image: gilat_fy2023 p.160 | kept (one extraction only; see check) |
| 227 | B only | FY2022 ROU additions (B only) | 2,412 | gilat_fy2023 p.160 | page image: gilat_fy2023 p.160 | kept (one extraction only; see check) |
| 228 | B only | FY2023 ROU additions (B only) | 3,103 | gilat_fy2023 p.160 | page image: gilat_fy2023 p.160 | kept (one extraction only; see check) |
| 229 | B only | FY2024 ROU additions (B only) | 24,528 | gilat_fy2025 p.176 | page image: gilat_fy2025 p.176 | kept (one extraction only; see check) |
| 230 | B only | FY2025 ROU additions (B only) | 2,895 | gilat_fy2025 p.175 | page image: gilat_fy2025 p.175 | kept (one extraction only; see check) |
| 231 | A only | FY2021/da_by_function/cogs | 16,807 | gilat_fy2023 p.157 | page image: gilat_fy2023 p.157 | kept (one extraction only; see check) |
| 232 | A only | FY2021/da_by_function/general_admin | 594 | gilat_fy2023 p.158 | page image: gilat_fy2023 p.158 | kept (one extraction only; see check) |
| 233 | A only | FY2021/da_by_function/selling_marketing | 936 | gilat_fy2023 p.158 | page image: gilat_fy2023 p.158 | kept (one extraction only; see check) |
| 234 | A only | FY2022/cash_by_currency/ILS | 9,746 | gilat_fy2023 p.138 | page image: gilat_fy2023 p.138 | kept (one extraction only; see check) |
| 235 | A only | FY2022/cash_by_currency/USD | 788 | gilat_fy2023 p.138 | page image: gilat_fy2023 p.138 | kept (one extraction only; see check) |
| 236 | A only | FY2022/cash_by_currency/other | 363 | gilat_fy2023 p.138 | page image: gilat_fy2023 p.138 | kept (one extraction only; see check) |
| 237 | A only | FY2022/da_by_function/cogs | 10,215 | gilat_fy2023 p.157 | page image: gilat_fy2023 p.157 | kept (one extraction only; see check) |
| 238 | A only | FY2022/da_by_function/general_admin | 622 | gilat_fy2023 p.158 | page image: gilat_fy2023 p.158 | kept (one extraction only; see check) |
| 239 | A only | FY2022/da_by_function/selling_marketing | 942 | gilat_fy2023 p.158 | page image: gilat_fy2023 p.158 | kept (one extraction only; see check) |
| 240 | A only | FY2023/cash_by_currency/ILS | 9,486 | gilat_fy2023 p.138 | page image: gilat_fy2023 p.138 | kept (one extraction only; see check) |
| 241 | A only | FY2023/cash_by_currency/USD | 2,610 | gilat_fy2023 p.138 | page image: gilat_fy2023 p.138 | kept (one extraction only; see check) |
| 242 | A only | FY2023/cash_by_currency/other | 119 | gilat_fy2023 p.138 | page image: gilat_fy2023 p.138 | kept (one extraction only; see check) |
| 243 | A only | FY2023/da_by_function/cogs | 5,788 | gilat_fy2023 p.157 | page image: gilat_fy2023 p.157 | kept (one extraction only; see check) |
| 244 | A only | FY2023/da_by_function/general_admin | 607 | gilat_fy2023 p.158 | page image: gilat_fy2023 p.158 | kept (one extraction only; see check) |
| 245 | A only | FY2023/da_by_function/selling_marketing | 973 | gilat_fy2023 p.158 | page image: gilat_fy2023 p.158 | kept (one extraction only; see check) |
| 246 | A only | FY2024/cash_by_currency/ILS | 9,758 | gilat_fy2024 p.140 | page image: gilat_fy2024 p.140 | kept (one extraction only; see check) |
| 247 | A only | FY2024/cash_by_currency/USD | 1,023 | gilat_fy2024 p.140 | page image: gilat_fy2024 p.140 | kept (one extraction only; see check) |
| 248 | A only | FY2024/cash_by_currency/other | 236 | gilat_fy2024 p.140 | page image: gilat_fy2024 p.140 | kept (one extraction only; see check) |
| 249 | A only | FY2024/da_by_function/cogs | 8,422 | gilat_fy2024 p.161 | page image: gilat_fy2024 p.161 | kept (one extraction only; see check) |
| 250 | A only | FY2024/da_by_function/general_admin | 648 | gilat_fy2024 p.162 | page image: gilat_fy2024 p.162 | kept (one extraction only; see check) |
| 251 | A only | FY2024/da_by_function/selling_marketing | 961 | gilat_fy2024 p.162 | page image: gilat_fy2024 p.162 | kept (one extraction only; see check) |
| 252 | A only | FY2025/cash_by_currency/ILS | 24,171 | gilat_fy2025 p.146 | page image: gilat_fy2025 p.146 | kept (one extraction only; see check) |
| 253 | A only | FY2025/cash_by_currency/USD | 639 | gilat_fy2025 p.146 | page image: gilat_fy2025 p.146 | kept (one extraction only; see check) |
| 254 | A only | FY2025/cash_by_currency/other | 226 | gilat_fy2025 p.146 | page image: gilat_fy2025 p.146 | kept (one extraction only; see check) |
| 255 | A only | FY2025/da_by_function/cogs | 11,429 | gilat_fy2025 p.173 | page image: gilat_fy2025 p.173 | kept (one extraction only; see check) |
| 256 | A only | FY2025/da_by_function/general_admin | 644 | gilat_fy2025 p.174 | page image: gilat_fy2025 p.174 | kept (one extraction only; see check) |
| 257 | A only | FY2025/da_by_function/selling_marketing | 1,028 | gilat_fy2025 p.174 | page image: gilat_fy2025 p.174 | kept (one extraction only; see check) |
| 258 | A only | H1_2026/equity_components_solo/accumulated_deficit | -10,147 | gilat_h1_2026 p.31 | page image: gilat_h1_2026 p.31 | kept (one extraction only; see check) |
| 259 | A only | H1_2026/equity_components_solo/capital_reserves | -118 | gilat_h1_2026 p.31 | page image: gilat_h1_2026 p.31 | kept (one extraction only; see check) |
| 260 | A only | H1_2026/equity_components_solo/option_receipts | 1,398 | gilat_h1_2026 p.31 | page image: gilat_h1_2026 p.31 | kept (one extraction only; see check) |
| 261 | A only | H1_2026/equity_components_solo/premium | 28,213 | gilat_h1_2026 p.31 | page image: gilat_h1_2026 p.31 | kept (one extraction only; see check) |
| 262 | A only | H1_2026/equity_components_solo/share_capital | 113,489 | gilat_h1_2026 p.31 | page image: gilat_h1_2026 p.31 | kept (one extraction only; see check) |
| 263 | A only | H1_2026/equity_components_solo/translation_reserve | -9,107 | gilat_h1_2026 p.31 | page image: gilat_h1_2026 p.31 | kept (one extraction only; see check) |
| 264 | A only | H2_2025_USD/adj_ebitda_company | 8,817 | gilat_fy2025 p.92-93 | arithmetic: re-computed 8,817 (Q3 + Q4 2025 (gilat_fy2025 p.92)) | kept (one extraction only; see check) |
| 265 | A only | H2_2025_USD/cost_of_revenue | 28,179 | gilat_fy2025 p.92-93 | arithmetic: re-computed 28,179 (Q3 + Q4 2025 (gilat_fy2025 p.92)) | kept (one extraction only; see check) |
| 266 | A only | H2_2025_USD/ebitda_company | 13,469 | gilat_fy2025 p.92-93 | arithmetic: re-computed 13,469 (Q3 + Q4 2025 (gilat_fy2025 p.92-93)) | kept (one extraction only; see check) |
| 267 | A only | H2_2025_USD/finance_net | -1,459 | gilat_fy2025 p.92-93 | arithmetic: re-computed -1,459 (Q3 + Q4 2025 (gilat_fy2025 p.92)) | kept (one extraction only; see check) |
| 268 | A only | H2_2025_USD/general_admin | 3,845 | gilat_fy2025 p.92-93 | arithmetic: re-computed 3,845 (Q3 + Q4 2025 (gilat_fy2025 p.92)) | kept (one extraction only; see check) |
| 269 | A only | H2_2025_USD/gross_profit | 13,035 | gilat_fy2025 p.92-93 | arithmetic: re-computed 13,035 (Q3 + Q4 2025 (gilat_fy2025 p.92)) | kept (one extraction only; see check) |
| 270 | A only | H2_2025_USD/net_income | 5,229 | gilat_fy2025 p.92-93 | arithmetic: re-computed 5,229 (Q3 + Q4 2025 (gilat_fy2025 p.92)) | kept (one extraction only; see check) |
| 271 | A only | H2_2025_USD/operating_income | 6,114 | gilat_fy2025 p.92-93 | arithmetic: re-computed 6,114 (Q3 + Q4 2025 (gilat_fy2025 p.92)) | kept (one extraction only; see check) |
| 272 | A only | H2_2025_USD/option_revaluation_loss_company | 51 | gilat_fy2025 p.92-93 | arithmetic: re-computed 51 (Q3 + Q4 2025 (gilat_fy2025 p.92-93)) | kept (one extraction only; see check) |
| 273 | A only | H2_2025_USD/revenue | 41,214 | gilat_fy2025 p.92-93 | arithmetic: re-computed 41,214 (Q3 + Q4 2025 (gilat_fy2025 p.92)) | kept (one extraction only; see check) |
| 274 | A only | H2_2025_USD/satellite_lease_depreciation_company | 4,652 | gilat_fy2025 p.92-93 | arithmetic: re-computed 4,652 (Q3 + Q4 2025 (gilat_fy2025 p.92-93)) | kept (one extraction only; see check) |
| 275 | A only | H2_2025_USD/selling_marketing | 3,076 | gilat_fy2025 p.92-93 | arithmetic: re-computed 3,076 (Q3 + Q4 2025 (gilat_fy2025 p.92)) | kept (one extraction only; see check) |
| 276 | A only | H2_2025_USD/tax_expense | -574 | gilat_fy2025 p.92-93 | arithmetic: re-computed -574 (Q3 + Q4 2025 (gilat_fy2025 p.92)) | kept (one extraction only; see check) |
| 277 | A only | Q1_2026_derived/capex_company | 2,228 | gilat_h1_2026 p.6-7, p.13 | arithmetic: re-computed 2,228 (H1 2026 - Q2 2026 (gilat_h1_2026 p.6-7, p.13)) | kept (one extraction only; see check) |
| 278 | A only | Q1_2026_derived/cost_of_revenue | 47,319 | gilat_h1_2026 p.6-7, p.13 | arithmetic: re-computed 47,319 (H1 2026 - Q2 2026 (gilat_h1_2026 p.6-7, p.13)) | kept (one extraction only; see check) |
| 279 | A only | Q1_2026_derived/fcf_company | -4,887 | gilat_h1_2026 p.6-7, p.13 | arithmetic: re-computed -4,887 (H1 2026 - Q2 2026 (gilat_h1_2026 p.6-7, p.13)) | kept (one extraction only; see check) |
| 280 | A only | Q1_2026_derived/financing_cf | -10,630 | gilat_h1_2026 p.6-7, p.13 | arithmetic: re-computed -10,630 (H1 2026 - Q2 2026 (gilat_h1_2026 p.6-7, p.13)) | kept (one extraction only; see check) |
| 281 | A only | Q1_2026_derived/general_admin | 7,065 | gilat_h1_2026 p.6-7, p.13 | arithmetic: re-computed 7,065 (H1 2026 - Q2 2026 (gilat_h1_2026 p.6-7, p.13)) | kept (one extraction only; see check) |
| 282 | A only | Q1_2026_derived/investing_cf | 7,759 | gilat_h1_2026 p.6-7, p.13 | arithmetic: re-computed 7,759 (H1 2026 - Q2 2026 (gilat_h1_2026 p.6-7, p.13)) | kept (one extraction only; see check) |
| 283 | A only | Q1_2026_derived/lease_payments_company | 8,883 | gilat_h1_2026 p.6-7, p.13 | arithmetic: re-computed 8,883 (H1 2026 - Q2 2026 (gilat_h1_2026 p.6-7, p.13)) | kept (one extraction only; see check) |
| 284 | A only | Q1_2026_derived/prepaid_expenses_company | 7,827 | gilat_h1_2026 p.6-7, p.13 | arithmetic: re-computed 7,827 (H1 2026 - Q2 2026 (gilat_h1_2026 p.6-7, p.13)) | kept (one extraction only; see check) |
| 285 | A only | Q1_2026_derived/satellite_lease_depreciation_company | 7,128 | gilat_h1_2026 p.6-7, p.13 | arithmetic: re-computed 7,128 (H1 2026 - Q2 2026 (gilat_h1_2026 p.6-7, p.13)) | kept (one extraction only; see check) |
| 286 | A only | Q1_2026_derived/selling_marketing | 4,752 | gilat_h1_2026 p.6-7, p.13 | arithmetic: re-computed 4,752 (H1 2026 - Q2 2026 (gilat_h1_2026 p.6-7, p.13)) | kept (one extraction only; see check) |
| 287 | A only | Q1_2026_derived/tax_expense | 103 | gilat_h1_2026 p.6-7, p.13 | arithmetic: re-computed 103 (H1 2026 - Q2 2026 (gilat_h1_2026 p.6-7, p.13)) | kept (one extraction only; see check) |
| 288 | B only | FY2021/fcf_company | -2,103 | gilat_fy2023 p.86 | page image: gilat_fy2023 p.86 | kept (one extraction only; see check) |
| 289 | B only | FY2021/marketable_securities | 0 | gilat_fy2023 p.123 | page image: gilat_fy2023 p.123 | kept (one extraction only; see check) |
| 290 | B only | FY2021/short_term_lease_expense | 7,896 | gilat_fy2023 p.146 | page image: gilat_fy2023 p.146 | kept (one extraction only; see check) |
| 291 | B only | FY2022/impairments | 0 | gilat_fy2023 p.118 | page image: gilat_fy2023 p.118 | kept (one extraction only; see check) |
| 292 | B only | FY2022/short_term_lease_expense | 7,059 | gilat_fy2023 p.146 | page image: gilat_fy2023 p.146 | kept (one extraction only; see check) |
| 293 | B only | FY2022/wc_components/inventory | -489 | gilat_fy2023 p.122 | page image: gilat_fy2023 p.122 | kept (one extraction only; see check) |
| 294 | B only | FY2022/wc_components/other_payables_and_tax | -487 | gilat_fy2023 p.122 | page image: gilat_fy2023 p.122 | kept (one extraction only; see check) |
| 295 | B only | FY2022/wc_components/other_receivables | 266 | gilat_fy2023 p.122 | page image: gilat_fy2023 p.122 | kept (one extraction only; see check) |
| 296 | B only | FY2022/wc_components/payables_incl_lt_suppliers | 998 | gilat_fy2023 p.122 | page image: gilat_fy2023 p.122 | kept (one extraction only; see check) |
| 297 | B only | FY2022/wc_components/receivables_incl_lt | 438 | gilat_fy2023 p.122 | page image: gilat_fy2023 p.122 | kept (one extraction only; see check) |
| 298 | B only | FY2023/short_term_lease_expense | 10,973 | gilat_fy2023 p.146 | page image: gilat_fy2023 p.146 | kept (one extraction only; see check) |
| 299 | B only | FY2023/wc_components/inventory | -599 | gilat_fy2023 p.122 | page image: gilat_fy2023 p.122 | kept (one extraction only; see check) |
| 300 | B only | FY2023/wc_components/other_payables_and_tax | 64 | gilat_fy2023 p.122 | page image: gilat_fy2023 p.122 | kept (one extraction only; see check) |
| 301 | B only | FY2023/wc_components/other_receivables | 62 | gilat_fy2023 p.122 | page image: gilat_fy2023 p.122 | kept (one extraction only; see check) |
| 302 | B only | FY2023/wc_components/payables_incl_lt_suppliers | 5,335 | gilat_fy2023 p.122 | page image: gilat_fy2023 p.122 | kept (one extraction only; see check) |
| 303 | B only | FY2023/wc_components/receivables_incl_lt | -5,033 | gilat_fy2023 p.122 | page image: gilat_fy2023 p.122 | kept (one extraction only; see check) |
| 304 | B only | FY2024/wc_components/inventory | 427 | gilat_fy2024 p.124 | page image: gilat_fy2024 p.124 | kept (one extraction only; see check) |
| 305 | B only | FY2024/wc_components/other_payables | 130 | gilat_fy2024 p.124 | page image: gilat_fy2024 p.124 | kept (one extraction only; see check) |
| 306 | B only | FY2024/wc_components/other_receivables | -2,069 | gilat_fy2024 p.124 | page image: gilat_fy2024 p.124 | kept (one extraction only; see check) |
| 307 | B only | FY2024/wc_components/payables_incl_lt_suppliers | -482 | gilat_fy2024 p.124 | page image: gilat_fy2024 p.124 | kept (one extraction only; see check) |
| 308 | B only | FY2024/wc_components/prepaid_contract_costs_lt | -1,127 | gilat_fy2024 p.124 | page image: gilat_fy2024 p.124 | kept (one extraction only; see check) |
| 309 | B only | FY2024/wc_components/receivables_incl_lt | -1,529 | gilat_fy2024 p.124 | page image: gilat_fy2024 p.124 | kept (one extraction only; see check) |
| 310 | B only | FY2025/lease_cash_outflow_total | 22,860 | gilat_fy2025 p.160 | page image: gilat_fy2025 p.160 | kept (one extraction only; see check) |
| 311 | B only | FY2025/wc_components/deferred_expenses_bezeq_iru | -3,902 | gilat_fy2025 p.131 | page image: gilat_fy2025 p.131 | kept (one extraction only; see check) |
| 312 | B only | FY2025/wc_components/inventory | -228 | gilat_fy2025 p.131 | page image: gilat_fy2025 p.131 | kept (one extraction only; see check) |
| 313 | B only | FY2025/wc_components/other_payables | 3,396 | gilat_fy2025 p.131 | page image: gilat_fy2025 p.131 | kept (one extraction only; see check) |
| 314 | B only | FY2025/wc_components/other_receivables | -407 | gilat_fy2025 p.131 | page image: gilat_fy2025 p.131 | kept (one extraction only; see check) |
| 315 | B only | FY2025/wc_components/payables_incl_lt_suppliers | 1,748 | gilat_fy2025 p.131 | page image: gilat_fy2025 p.131 | kept (one extraction only; see check) |
| 316 | B only | FY2025/wc_components/prepaid_contract_costs | 973 | gilat_fy2025 p.131 | page image: gilat_fy2025 p.131 | kept (one extraction only; see check) |
| 317 | B only | FY2025/wc_components/receivables | -4,318 | gilat_fy2025 p.131 | page image: gilat_fy2025 p.131 | kept (one extraction only; see check) |
| 318 | B only | H1_2025_ILS/contract_assets | - |  | page image: explicit null: not disclosed in the supplied documents (no consolidated interim statements in gilat_h1_2026) | kept as not_in_documents |
| 319 | B only | H1_2025_ILS/contract_liabilities | - |  | page image: explicit null: not disclosed in the supplied documents (no consolidated interim statements in gilat_h1_2026) | kept as not_in_documents |
| 320 | B only | H1_2025_ILS/d_and_a_ppe | - |  | page image: explicit null: not disclosed in the supplied documents (no consolidated interim statements in gilat_h1_2026) | kept as not_in_documents |
| 321 | B only | H1_2025_ILS/employees | - |  | page image: explicit null: not disclosed in the supplied documents (no consolidated interim statements in gilat_h1_2026) | kept as not_in_documents |
| 322 | B only | H1_2025_ILS/interest_paid_bonds_parent | 811 | gilat_h1_2026 p.34 | page image: gilat_h1_2026 p.34 | kept (one extraction only; see check) |
| 323 | B only | H1_2025_ILS/pretax_income | 4,313 | derived: operating income + net finance | arithmetic: re-computed 4,313 (EBIT 12,841 + net finance -8,528 (p.6)) | kept (one extraction only; see check) |
| 324 | B only | H1_2025_ILS/restricted_cash | - |  | page image: explicit null: not disclosed in the supplied documents (no consolidated interim statements in gilat_h1_2026) | kept as not_in_documents |
| 325 | B only | H1_2025_ILS/sbc | - |  | page image: explicit null: not disclosed in the supplied documents (no consolidated interim statements in gilat_h1_2026) | kept as not_in_documents |
| 326 | B only | H1_2025_ILS/tax_paid | - |  | page image: explicit null: not disclosed in the supplied documents (no consolidated interim statements in gilat_h1_2026) | kept as not_in_documents |
| 327 | B only | H1_2025_ILS/wc_change | - |  | page image: explicit null: not disclosed in the supplied documents (no consolidated interim statements in gilat_h1_2026) | kept as not_in_documents |
| 328 | B only | H1_2025_USD/pretax_income | 1,196 | derived: operating income + net finance | arithmetic: re-computed 1,196 (Q1+Q2 EBIT 3,575 + net finance -2,379 (gilat_fy2025 p.92)) | kept (one extraction only; see check) |
| 329 | B only | H1_2026_ILS/capex_intangibles | - |  | page image: explicit null: not disclosed in the supplied documents (no consolidated interim statements in gilat_h1_2026) | kept as not_in_documents |
| 330 | B only | H1_2026_ILS/capex_ppe | - |  | page image: explicit null: not disclosed in the supplied documents (no consolidated interim statements in gilat_h1_2026) | kept as not_in_documents |
| 331 | B only | H1_2026_ILS/contract_assets | - |  | page image: explicit null: not disclosed in the supplied documents (no consolidated interim statements in gilat_h1_2026) | kept as not_in_documents |
| 332 | B only | H1_2026_ILS/contract_liabilities | - |  | page image: explicit null: not disclosed in the supplied documents (no consolidated interim statements in gilat_h1_2026) | kept as not_in_documents |
| 333 | B only | H1_2026_ILS/d_and_a_intangibles | - |  | page image: explicit null: not disclosed in the supplied documents (no consolidated interim statements in gilat_h1_2026) | kept as not_in_documents |
| 334 | B only | H1_2026_ILS/d_and_a_ppe | - |  | page image: explicit null: not disclosed in the supplied documents (no consolidated interim statements in gilat_h1_2026) | kept as not_in_documents |
| 335 | B only | H1_2026_ILS/d_and_a_rou | - |  | page image: explicit null: not disclosed in the supplied documents (no consolidated interim statements in gilat_h1_2026) | kept as not_in_documents |
| 336 | B only | H1_2026_ILS/employees | - |  | page image: explicit null: not disclosed in the supplied documents (no consolidated interim statements in gilat_h1_2026) | kept as not_in_documents |
| 337 | B only | H1_2026_ILS/eps_basic | - |  | page image: explicit null: not disclosed in the supplied documents (no consolidated interim statements in gilat_h1_2026) | kept as not_in_documents |
| 338 | B only | H1_2026_ILS/finance_expense | - |  | page image: explicit null: not disclosed in the supplied documents (no consolidated interim statements in gilat_h1_2026) | kept as not_in_documents |
| 339 | B only | H1_2026_ILS/finance_income | - |  | page image: explicit null: not disclosed in the supplied documents (no consolidated interim statements in gilat_h1_2026) | kept as not_in_documents |
| 340 | B only | H1_2026_ILS/impairments | - |  | page image: explicit null: not disclosed in the supplied documents (no consolidated interim statements in gilat_h1_2026) | kept as not_in_documents |
| 341 | B only | H1_2026_ILS/interest_paid_excl_leases | - |  | page image: explicit null: not disclosed in the supplied documents (no consolidated interim statements in gilat_h1_2026) | kept as not_in_documents |
| 342 | B only | H1_2026_ILS/lease_interest_paid | - |  | page image: explicit null: not disclosed in the supplied documents (no consolidated interim statements in gilat_h1_2026) | kept as not_in_documents |
| 343 | B only | H1_2026_ILS/lease_principal | - |  | page image: explicit null: not disclosed in the supplied documents (no consolidated interim statements in gilat_h1_2026) | kept as not_in_documents |
| 344 | B only | H1_2026_ILS/nci_share | 0 | gilat_h1_2026 p.6 | page image: gilat_h1_2026 p.6 | kept (one extraction only; see check) |
| 345 | B only | H1_2026_ILS/net_income_to_owners | 15,770 | gilat_h1_2026 p.6 | page image: gilat_h1_2026 p.6 | kept (one extraction only; see check) |
| 346 | B only | H1_2026_ILS/pretax_income | 15,959 | derived: operating income 19,395 + net finance -3,436 (gilat_h1_2026 … | arithmetic: re-computed 15,959 (EBIT 19,395 + net finance -3,436 (p.6)) | kept (one extraction only; see check) |
| 347 | B only | H1_2026_ILS/r_and_d | 0 | gilat_h1_2026 p.6 | page image: gilat_h1_2026 p.6 | kept (one extraction only; see check) |
| 348 | B only | H1_2026_ILS/share_of_associates | 0 | gilat_h1_2026 p.6 | page image: gilat_h1_2026 p.6 | kept (one extraction only; see check) |
| 349 | B only | Q2_2025_ILS/finance_items_in_ocf_adjustment | -8,030 | gilat_h1_2026 p.7 | page image: gilat_h1_2026 p.7 | kept (one extraction only; see check) |
| 350 | B only | Q2_2026_ILS/finance_items_in_ocf_adjustment | 1,228 | gilat_h1_2026 p.7 | page image: gilat_h1_2026 p.7 | kept (one extraction only; see check) |
| 351 | B only | TTM_2026H1_ILS/nci_share | 0 | gilat_h1_2026 p.6 | page image: gilat_h1_2026 p.6 | kept (one extraction only; see check) |
| 352 | B only | TTM_2026H1_ILS/net_income_to_owners | 32,985 | derived: no NCI | arithmetic: re-computed 32,985 (no NCI) | kept (one extraction only; see check) |
| 353 | B only | TTM_2026H1_ILS/pretax_income | 31,316 | derived: TTM operating income + TTM net finance | arithmetic: re-computed 31,316 (TTM EBIT + TTM net finance) | kept (one extraction only; see check) |
| 354 | B only | TTM_2026H1_USD_at_3.157/adj_ebitda_company | 18,621.2 | derived: TTM ILS 58,787 / 3.157 | arithmetic: re-computed 18,621.2 (TTM ILS 58,787 / 3.157 (convenience)) | kept (one extraction only; see check) |
| 355 | B only | TTM_2026H1_USD_at_3.157/capex_ppe_and_other | 3,217.9 | derived: TTM ILS 10,159 / 3.157 | arithmetic: re-computed 3,217.9 (TTM ILS 10,159 / 3.157 (convenience)) | kept (one extraction only; see check) |
| 356 | B only | TTM_2026H1_USD_at_3.157/ebitda_company | 28,021.2 | derived: TTM ILS 88,463 / 3.157 | arithmetic: re-computed 28,021.2 (TTM ILS 88,463 / 3.157 (convenience)) | kept (one extraction only; see check) |
| 357 | B only | TTM_2026H1_USD_at_3.157/fcf_company | 13,745.3 | derived: TTM ILS 43,394 / 3.157 | arithmetic: re-computed 13,745.3 (TTM ILS 43,394 / 3.157 (convenience)) | kept (one extraction only; see check) |
| 358 | B only | TTM_2026H1_USD_at_3.157/gross_profit | 26,991.1 | derived: TTM ILS 85,211 / 3.157 | arithmetic: re-computed 26,991.1 (TTM ILS 85,211 / 3.157 (convenience)) | kept (one extraction only; see check) |
| 359 | B only | TTM_2026H1_USD_at_3.157/lease_payments_total | 11,573.3 | derived: TTM ILS 36,537 / 3.157 | arithmetic: re-computed 11,573.3 (TTM ILS 36,537 / 3.157 (convenience)) | kept (one extraction only; see check) |
| 360 | B only | TTM_2026H1_USD_at_3.157/net_income | 10,448.2 | derived: TTM ILS 32,985 / 3.157 | arithmetic: re-computed 10,448.2 (TTM ILS 32,985 / 3.157 (convenience)) | kept (one extraction only; see check) |
| 361 | B only | TTM_2026H1_USD_at_3.157/ocf | 25,646.8 | derived: TTM ILS 80,967 / 3.157 | arithmetic: re-computed 25,646.8 (TTM ILS 80,967 / 3.157 (convenience)) | kept (one extraction only; see check) |
| 362 | B only | TTM_2026H1_USD_at_3.157/operating_income | 12,523 | derived: TTM ILS 39,535 / 3.157 | arithmetic: re-computed 12,523.0 (TTM ILS 39,535 / 3.157 (convenience)) | kept (one extraction only; see check) |
| 363 | B only | TTM_2026H1_USD_at_3.157/prepaid_expenses_company | 3,561 | derived: TTM ILS 11,242 / 3.157 | arithmetic: re-computed 3,561.0 (TTM ILS 11,242 / 3.157 (convenience)) | kept (one extraction only; see check) |
| 364 | B only | TTM_2026H1_USD_at_3.157/pretax_income | 9,919.5 | derived: TTM ILS 31,316 / 3.157 | arithmetic: re-computed 9,919.5 (TTM ILS 31,316 / 3.157 (convenience)) | kept (one extraction only; see check) |
| 365 | B only | TTM_2026H1_USD_at_3.157/revenue | 87,453.9 | derived: TTM ILS 276,092 / 3.157 | arithmetic: re-computed 87,453.9 (TTM ILS 276,092 / 3.157 (convenience)) | kept (one extraction only; see check) |

### 6.10 Quarterly tables (directors' reports) (13)

| # | side | item | value | ref | check | resolution |
|---:|---|---|---:|---|---|---|
| 366 | B only | quarterly 2025 Q1 non_gaap_net_income_company | 702 | gilat_fy2025 p.92,93 | page image: gilat_fy2025 p.92, gilat_fy2025 p.93 | kept (one extraction only; see check) |
| 367 | B only | quarterly 2025 Q2 non_gaap_net_income_company | 2,061 | gilat_fy2025 p.92,93 | page image: gilat_fy2025 p.92, gilat_fy2025 p.93 | kept (one extraction only; see check) |
| 368 | B only | quarterly 2025 Q3 non_gaap_net_income_company | 1,793 | gilat_fy2025 p.92,93 | page image: gilat_fy2025 p.92, gilat_fy2025 p.93 | kept (one extraction only; see check) |
| 369 | B only | quarterly 2025 Q4 non_gaap_net_income_company | 3,487 | gilat_fy2025 p.92,93 | page image: gilat_fy2025 p.92, gilat_fy2025 p.93 | kept (one extraction only; see check) |
| 370 | B only | quarterly/FY2023/sum_check_vs_annual/net_income | 0 | gilat_fy2023 p.86 | arithmetic: quarter sums = audited annual totals (re-checked) | B's own check value, not a document figure |
| 371 | B only | quarterly/FY2023/sum_check_vs_annual/operating_income | 0 | gilat_fy2023 p.86 | arithmetic: quarter sums = audited annual totals (re-checked) | B's own check value, not a document figure |
| 372 | B only | quarterly/FY2023/sum_check_vs_annual/revenue | 0 | gilat_fy2023 p.86 | arithmetic: quarter sums = audited annual totals (re-checked) | B's own check value, not a document figure |
| 373 | B only | quarterly/FY2024/sum_check_vs_annual/net_income | 0 | gilat_fy2024 p.82 | arithmetic: quarter sums = audited annual totals (re-checked) | B's own check value, not a document figure |
| 374 | B only | quarterly/FY2024/sum_check_vs_annual/operating_income | 0 | gilat_fy2024 p.82 | arithmetic: quarter sums = audited annual totals (re-checked) | B's own check value, not a document figure |
| 375 | B only | quarterly/FY2024/sum_check_vs_annual/revenue | 0 | gilat_fy2024 p.82 | arithmetic: quarter sums = audited annual totals (re-checked) | B's own check value, not a document figure |
| 376 | B only | quarterly/FY2025/sum_check_vs_annual/net_income | 0 | gilat_fy2025 p.92,93 | arithmetic: quarter sums = audited annual totals (re-checked) | B's own check value, not a document figure |
| 377 | B only | quarterly/FY2025/sum_check_vs_annual/operating_income | 0 | gilat_fy2025 p.92,93 | arithmetic: quarter sums = audited annual totals (re-checked) | B's own check value, not a document figure |
| 378 | B only | quarterly/FY2025/sum_check_vs_annual/revenue | 0 | gilat_fy2025 p.92,93 | arithmetic: quarter sums = audited annual totals (re-checked) | B's own check value, not a document figure |

### 6.11 Receivables (12)

| # | side | item | value | ref | check | resolution |
|---:|---|---|---:|---|---|---|
| 379 | B only | credit-loss allowance 2022 | -6,548 | gilat_fy2023 p.138; gilat_fy2025 p.147 | page image: gilat_fy2023 p.138, gilat_fy2025 p.147 | kept (one extraction only; see check) |
| 380 | B only | receivables gross 2022 | 11,875 | gilat_fy2023 p.138 | page image: gilat_fy2023 p.138 | kept (one extraction only; see check) |
| 381 | B only | receivables allowance 2022 (B period) | -6,548 | gilat_fy2023 p.138 | page image: gilat_fy2023 p.138 | kept (one extraction only; see check) |
| 382 | B only | credit-loss allowance 2023 | -6,723 | gilat_fy2023 p.138; gilat_fy2025 p.147 | page image: gilat_fy2023 p.138, gilat_fy2025 p.147 | kept (one extraction only; see check) |
| 383 | B only | receivables gross 2023 | 17,043 | gilat_fy2023 p.138 | page image: gilat_fy2023 p.138 | kept (one extraction only; see check) |
| 384 | B only | receivables allowance 2023 (B period) | -6,723 | gilat_fy2023 p.138 | page image: gilat_fy2023 p.138 | kept (one extraction only; see check) |
| 385 | B only | credit-loss allowance 2024 | -6,124 | gilat_fy2023 p.138; gilat_fy2025 p.147 | page image: gilat_fy2023 p.138, gilat_fy2025 p.147 | kept (one extraction only; see check) |
| 386 | B only | receivables gross 2024 | 17,995 | gilat_fy2025 p.147 | page image: gilat_fy2025 p.147 | kept (one extraction only; see check) |
| 387 | B only | receivables allowance 2024 (B period) | -6,124 | gilat_fy2025 p.147 | page image: gilat_fy2025 p.147 | kept (one extraction only; see check) |
| 388 | B only | credit-loss allowance 2025 | -6,767 | gilat_fy2023 p.138; gilat_fy2025 p.147 | page image: gilat_fy2023 p.138, gilat_fy2025 p.147 | kept (one extraction only; see check) |
| 389 | B only | receivables gross 2025 | 22,977 | gilat_fy2025 p.147 | page image: gilat_fy2025 p.147 | kept (one extraction only; see check) |
| 390 | B only | receivables allowance 2025 (B period) | -6,767 | gilat_fy2025 p.147 | page image: gilat_fy2025 p.147 | kept (one extraction only; see check) |

### 6.12 Related parties (20)

| # | side | item | value | ref | check | resolution |
|---:|---|---|---:|---|---|---|
| 391 | A only | related_parties_comp/interested_party_employed_salary/2021 | 399 | gilat_fy2023 p.161; gilat_fy2025 p.176 | page image: gilat_fy2023 p.161, gilat_fy2025 p.176 | kept (one extraction only; see check) |
| 392 | A only | related_parties_comp/interested_party_employed_salary/2022 | 522 | gilat_fy2023 p.161; gilat_fy2025 p.176 | page image: gilat_fy2023 p.161, gilat_fy2025 p.176 | kept (one extraction only; see check) |
| 393 | A only | related_parties_comp/interested_party_employed_salary/2023 | 515 | gilat_fy2023 p.161; gilat_fy2025 p.176 | page image: gilat_fy2023 p.161, gilat_fy2025 p.176 | kept (one extraction only; see check) |
| 394 | A only | related_parties_comp/interested_party_employed_salary/2024 | 543 | gilat_fy2023 p.161; gilat_fy2025 p.176 | page image: gilat_fy2023 p.161, gilat_fy2025 p.176 | kept (one extraction only; see check) |
| 395 | A only | related_parties_comp/interested_party_employed_salary/2025 | 775 | gilat_fy2023 p.161; gilat_fy2025 p.176 | page image: gilat_fy2023 p.161, gilat_fy2025 p.176 | kept (one extraction only; see check) |
| 396 | A only | related_parties_comp/key_management_sbc/2021 | 83 | gilat_fy2023 p.161; gilat_fy2025 p.176 | page image: gilat_fy2023 p.161, gilat_fy2025 p.176 | kept (one extraction only; see check) |
| 397 | A only | related_parties_comp/key_management_sbc/2022 | 24 | gilat_fy2023 p.161; gilat_fy2025 p.176 | page image: gilat_fy2023 p.161, gilat_fy2025 p.176 | kept (one extraction only; see check) |
| 398 | A only | related_parties_comp/key_management_sbc/2023 | 16 | gilat_fy2023 p.161; gilat_fy2025 p.176 | page image: gilat_fy2023 p.161, gilat_fy2025 p.176 | kept (one extraction only; see check) |
| 399 | A only | related_parties_comp/key_management_sbc/2024 | 17 | gilat_fy2023 p.161; gilat_fy2025 p.176 | page image: gilat_fy2023 p.161, gilat_fy2025 p.176 | kept (one extraction only; see check) |
| 400 | A only | related_parties_comp/key_management_sbc/2025 | 33 | gilat_fy2023 p.161; gilat_fy2025 p.176 | page image: gilat_fy2023 p.161, gilat_fy2025 p.176 | kept (one extraction only; see check) |
| 401 | A only | related_parties_comp/key_management_total/2021 | 417 | gilat_fy2023 p.161; gilat_fy2025 p.176 | page image: gilat_fy2023 p.161, gilat_fy2025 p.176 | kept (one extraction only; see check) |
| 402 | A only | related_parties_comp/key_management_total/2022 | 541 | gilat_fy2023 p.161; gilat_fy2025 p.176 | page image: gilat_fy2023 p.161, gilat_fy2025 p.176 | kept (one extraction only; see check) |
| 403 | A only | related_parties_comp/key_management_total/2023 | 534 | gilat_fy2023 p.161; gilat_fy2025 p.176 | page image: gilat_fy2023 p.161, gilat_fy2025 p.176 | kept (one extraction only; see check) |
| 404 | A only | related_parties_comp/key_management_total/2024 | 562 | gilat_fy2023 p.161; gilat_fy2025 p.176 | page image: gilat_fy2023 p.161, gilat_fy2025 p.176 | kept (one extraction only; see check) |
| 405 | A only | related_parties_comp/key_management_total/2025 | 797 | gilat_fy2023 p.161; gilat_fy2025 p.176 | page image: gilat_fy2023 p.161, gilat_fy2025 p.176 | kept (one extraction only; see check) |
| 406 | A only | related_parties_comp/non_employee_directors_fees/2021 | 229 | gilat_fy2023 p.161; gilat_fy2025 p.176 | page image: gilat_fy2023 p.161, gilat_fy2025 p.176 | kept (one extraction only; see check) |
| 407 | A only | related_parties_comp/non_employee_directors_fees/2022 | 224 | gilat_fy2023 p.161; gilat_fy2025 p.176 | page image: gilat_fy2023 p.161, gilat_fy2025 p.176 | kept (one extraction only; see check) |
| 408 | A only | related_parties_comp/non_employee_directors_fees/2023 | 180 | gilat_fy2023 p.161; gilat_fy2025 p.176 | page image: gilat_fy2023 p.161, gilat_fy2025 p.176 | kept (one extraction only; see check) |
| 409 | A only | related_parties_comp/non_employee_directors_fees/2024 | 238 | gilat_fy2023 p.161; gilat_fy2025 p.176 | page image: gilat_fy2023 p.161, gilat_fy2025 p.176 | kept (one extraction only; see check) |
| 410 | A only | related_parties_comp/non_employee_directors_fees/2025 | 162 | gilat_fy2023 p.161; gilat_fy2025 p.176 | page image: gilat_fy2023 p.161, gilat_fy2025 p.176 | kept (one extraction only; see check) |

### 6.13 Restatements (13)

| # | side | item | value | ref | check | resolution |
|---:|---|---|---:|---|---|---|
| 411 | B only | restatements/0/as_reported/cost_of_revenue | 39,418 | gilat_fy2023 p.169 | page image: gilat_fy2023 p.169 | kept; same values stated in A restatements text |
| 412 | B only | restatements/0/as_reported/finance_expense | 4,173 | gilat_fy2023 p.169 | page image: gilat_fy2023 p.169 | kept; same values stated in A restatements text |
| 413 | B only | restatements/0/as_reported/g_and_a | 10,492 | gilat_fy2023 p.169 | page image: gilat_fy2023 p.169 | kept; same values stated in A restatements text |
| 414 | B only | restatements/0/as_reported/net_loss | -5,437 | gilat_fy2023 p.169 | page image: gilat_fy2023 p.169 | kept; same values stated in A restatements text |
| 415 | B only | restatements/0/as_reported/tax | 632 | gilat_fy2023 p.169 | page image: gilat_fy2023 p.169 | kept; same values stated in A restatements text |
| 416 | B only | restatements/0/restated_preferred/cost_of_revenue | 39,372 | gilat_fy2023 p.169 | page image: gilat_fy2023 p.169 | kept; same values stated in A restatements text |
| 417 | B only | restatements/0/restated_preferred/finance_expense | 4,195 | gilat_fy2023 p.169 | page image: gilat_fy2023 p.169 | kept; same values stated in A restatements text |
| 418 | B only | restatements/0/restated_preferred/g_and_a | 10,431 | gilat_fy2023 p.169 | page image: gilat_fy2023 p.169 | kept; same values stated in A restatements text |
| 419 | B only | restatements/0/restated_preferred/net_loss | -5,423 | gilat_fy2023 p.169 | page image: gilat_fy2023 p.169 | kept; same values stated in A restatements text |
| 420 | B only | restatements/0/restated_preferred/tax | 703 | gilat_fy2023 p.169 | page image: gilat_fy2023 p.169 | kept; same values stated in A restatements text |
| 421 | B only | restatements/6/alternatives/note_b_text | 15,809 | gilat_h1_2026 p.6,32,35 | page image: gilat_h1_2026 p.6, gilat_h1_2026 p.32, gilat_h1_2026 p.35 | kept; same values stated in A restatements text |
| 422 | B only | restatements/6/alternatives/separate_statement_profit | 15,261 | gilat_h1_2026 p.6,32,35 | page image: gilat_h1_2026 p.6, gilat_h1_2026 p.32, gilat_h1_2026 p.35 | kept; same values stated in A restatements text |
| 423 | B only | restatements/6/consolidated_preferred | 15,770 | gilat_h1_2026 p.6,32,35 | page image: gilat_h1_2026 p.6, gilat_h1_2026 p.32, gilat_h1_2026 p.35 | kept; same values stated in A restatements text |

### 6.14 Segments (17)

| # | side | item | value | ref | check | resolution |
|---:|---|---|---:|---|---|---|
| 424 | B only | seg FY2021 government_defence d&a | 0 | gilat_fy2023 p.167 | page image: gilat_fy2023 p.167 | gilat_fy2023 p.167 prints '-' for government D&A in 2021. A null, B 0. FINAL 0. |
| 425 | A only | region ILS Q2_2025 africa | 16,875 | gilat_fy2023 p.86; gilat_fy2024 p.83; gilat_fy2025 p.93; gilat_h1_202… | page image: gilat_fy2023 p.86, gilat_fy2024 p.83, gilat_fy2025 p.93, gilat_h1_2026 p.7 | kept (one extraction only; see check) |
| 426 | A only | region ILS Q2_2025 israel | 49,340 | gilat_fy2023 p.86; gilat_fy2024 p.83; gilat_fy2025 p.93; gilat_h1_202… | page image: gilat_fy2023 p.86, gilat_fy2024 p.83, gilat_fy2025 p.93, gilat_h1_2026 p.7 | kept (one extraction only; see check) |
| 427 | A only | region ILS Q2_2025 other | 293 | gilat_fy2023 p.86; gilat_fy2024 p.83; gilat_fy2025 p.93; gilat_h1_202… | page image: gilat_fy2023 p.86, gilat_fy2024 p.83, gilat_fy2025 p.93, gilat_h1_2026 p.7 | kept (one extraction only; see check) |
| 428 | A only | region ILS Q2_2026 africa | 15,257 | gilat_fy2023 p.86; gilat_fy2024 p.83; gilat_fy2025 p.93; gilat_h1_202… | page image: gilat_fy2023 p.86, gilat_fy2024 p.83, gilat_fy2025 p.93, gilat_h1_2026 p.7 | kept (one extraction only; see check) |
| 429 | A only | region ILS Q2_2026 israel | 54,668 | gilat_fy2023 p.86; gilat_fy2024 p.83; gilat_fy2025 p.93; gilat_h1_202… | page image: gilat_fy2023 p.86, gilat_fy2024 p.83, gilat_fy2025 p.93, gilat_h1_2026 p.7 | kept (one extraction only; see check) |
| 430 | A only | region ILS Q2_2026 other | 1,521 | gilat_fy2023 p.86; gilat_fy2024 p.83; gilat_fy2025 p.93; gilat_h1_202… | page image: gilat_fy2023 p.86, gilat_fy2024 p.83, gilat_fy2025 p.93, gilat_h1_2026 p.7 | kept (one extraction only; see check) |
| 431 | A only | segments/segment_expenses_usd_directors_report/global_business/2023 | -20,266 | gilat_fy2025 p.97-98 | page image: gilat_fy2025 p.97, gilat_fy2025 p.98 | kept (one extraction only; see check) |
| 432 | A only | segments/segment_expenses_usd_directors_report/global_business/2024 | -16,404 | gilat_fy2025 p.97-98 | page image: gilat_fy2025 p.97, gilat_fy2025 p.98 | kept (one extraction only; see check) |
| 433 | A only | segments/segment_expenses_usd_directors_report/global_business/2025 | -15,549 | gilat_fy2025 p.97-98 | page image: gilat_fy2025 p.97, gilat_fy2025 p.98 | kept (one extraction only; see check) |
| 434 | A only | segments/segment_expenses_usd_directors_report/government_defence/2023 | -16,348 | gilat_fy2025 p.97-98 | page image: gilat_fy2025 p.97, gilat_fy2025 p.98 | kept (one extraction only; see check) |
| 435 | A only | segments/segment_expenses_usd_directors_report/government_defence/2024 | -26,551 | gilat_fy2025 p.97-98 | page image: gilat_fy2025 p.97, gilat_fy2025 p.98 | kept (one extraction only; see check) |
| 436 | A only | segments/segment_expenses_usd_directors_report/government_defence/2025 | -31,445 | gilat_fy2025 p.97-98 | page image: gilat_fy2025 p.97, gilat_fy2025 p.98 | kept (one extraction only; see check) |
| 437 | A only | segments/segment_expenses_usd_directors_report/israel_comm_internet/2023 | -7,612 | gilat_fy2025 p.97-98 | page image: gilat_fy2025 p.97, gilat_fy2025 p.98 | kept (one extraction only; see check) |
| 438 | A only | segments/segment_expenses_usd_directors_report/israel_comm_internet/2024 | -12,732 | gilat_fy2025 p.97-98 | page image: gilat_fy2025 p.97, gilat_fy2025 p.98 | kept (one extraction only; see check) |
| 439 | A only | segments/segment_expenses_usd_directors_report/israel_comm_internet/2025 | -7,549 | gilat_fy2025 p.97-98 | page image: gilat_fy2025 p.97, gilat_fy2025 p.98 | kept (one extraction only; see check) |
| 440 | B only | segments/isp_kpis/arpu_ils_month/target_long_term | 90 | gilat_h1_2026 p.8 | page image: gilat_h1_2026 p.8 | kept (one extraction only; see check) |

### 6.15 Share counts (7)

| # | side | item | value | ref | check | resolution |
|---:|---|---|---:|---|---|---|
| 441 | B only* | shares issued 2021-12-31 (A period vs B period) | 58,438,636 | gilat_fy2023 p.151,120,121 | page image: gilat_fy2023 p.151, gilat_fy2023 p.120, gilat_fy2023 p.121 | agreed: A holds 58,438,636 in share_counts/2021-12-31 (derived: no 2021-2022 issues) |
| 442 | B only | fully diluted upper bound | 160,992,740 | derived: outstanding 19.8.2026 + Series D at 1.00 + Series C public a… | arithmetic: re-computed 160,992,740 (outstanding 19.8.2026 + Series D + Series C public + options) | kept (one extraction only; see check) |
| 443 | A only | share_counts/potential_dilution_at_2026-08-19/series_C_public_shares_if_converted | 729,605 | gilat_h1_2026 p.22 | arithmetic: re-computed 729,605 (984,967 / 1.35) | kept (one extraction only; see check) |
| 444 | B only | share_counts/ceo_holding/pct_capital | 8.45 | gilat_fy2025 p.205 | page image: gilat_fy2025 p.205 | kept (one extraction only; see check) |
| 445 | B only | share_counts/ceo_holding/pct_fully_diluted | 8.54 | gilat_fy2025 p.205 | page image: gilat_fy2025 p.205 | kept (one extraction only; see check) |
| 446 | B only | share_counts/mega_crosscheck | 1.665 | derived: Mega sec_market_value 198,207,420.626 ILS / outstanding 19.8… | arithmetic: re-computed 1.6651 (Mega market value / 119,034,974) | kept (one extraction only; see check) |
| 447 | B only | share_counts/possible_unitemised_h1_2026_issues | 652,151 | derived: ILS share-capital line 113,489k (30.6.2026) - 87,063k (31.12… | arithmetic: re-computed 652,151 (ILS share-capital line change - conversion shares) | kept (one extraction only; see check) |

### 6.16 Share events (29)

| # | side | item | value | ref | check | resolution |
|---:|---|---|---:|---|---|---|
| 448 | A only | share_events/1/exercise_price_ils | 0.826 | gilat_fy2025 p.171 | text layer: gilat_fy2025 p.171 | kept; B states the same figure in its share-events text |
| 449 | A only | share_events/1/shares | 2,338,000 | gilat_fy2025 p.171 | text layer: gilat_fy2025 p.171 | kept; B states the same figure in its share-events text |
| 450 | A only | share_events/3/exercise_price_ils | 0.676 | gilat_fy2025 p.171 | text layer: gilat_fy2025 p.171 | kept; B states the same figure in its share-events text |
| 451 | A only | share_events/3/shares | 900,000 | gilat_fy2025 p.171 | text layer: gilat_fy2025 p.171 | kept; B states the same figure in its share-events text |
| 452 | A only | share_events/4/cost_usd_k | 2,887 | gilat_fy2025 p.156 | page image: gilat_fy2025 p.156 | kept; B states the same figure in its share-events text |
| 453 | A only | share_events/4/nv | 11,710,089 | gilat_fy2025 p.156 | page image: gilat_fy2025 p.156 | kept; B states the same figure in its share-events text |
| 454 | A only | share_events/5/shares | 6,000,000 | gilat_fy2025 p.169-170 | text layer: gilat_fy2025 p.169, gilat_fy2025 p.170 | kept; B states the same figure in its share-events text |
| 455 | A only | share_events/6/exercise_price_ils | 0.3517 | gilat_fy2025 p.169 | text layer: gilat_fy2025 p.169 | kept; B states the same figure in its share-events text |
| 456 | A only | share_events/6/shares | 430,000 | gilat_fy2025 p.169 | text layer: gilat_fy2025 p.169 | kept; B states the same figure in its share-events text |
| 457 | A only | share_events/7/cost_usd_k | 823 | gilat_fy2025 p.156 | page image: gilat_fy2025 p.156 | kept; B states the same figure in its share-events text |
| 458 | A only | share_events/7/nv | 4,189,635 | gilat_fy2025 p.156 | page image: gilat_fy2025 p.156 | kept; B states the same figure in its share-events text |
| 459 | A only | share_events/8/price_ils | 0.3 | gilat_fy2025 p.165; gilat_fy2023 p.151 | page image: gilat_fy2023 p.151 / gilat_fy2025 p.165: 30 agorot = 0.30 ILS | kept; B states the same figure in its share-events text |
| 460 | A only | share_events/8/shares | 6,148,754 | gilat_fy2025 p.165; gilat_fy2023 p.151 | page image: gilat_fy2025 p.165, gilat_fy2023 p.151 | kept; B states the same figure in its share-events text |
| 461 | A only | share_events/9/price_ils | 0.3 | gilat_fy2025 p.165; gilat_fy2023 p.151 | page image: gilat_fy2023 p.151 / gilat_fy2025 p.165: ~30 agorot = 0.30 ILS | kept; B states the same figure in its share-events text |
| 462 | A only | share_events/9/shares | 4,056,402 | gilat_fy2025 p.165; gilat_fy2023 p.151 | page image: gilat_fy2025 p.165, gilat_fy2023 p.151 | kept; B states the same figure in its share-events text |
| 463 | A only | share_events/10/exercise_price_ils | 0.446 | gilat_fy2025 p.167 | text layer: gilat_fy2025 p.167 | kept; B states the same figure in its share-events text |
| 464 | A only | share_events/10/shares | 250,000 | gilat_fy2025 p.167 | text layer: gilat_fy2025 p.167 | kept; B states the same figure in its share-events text |
| 465 | A only | share_events/11/exercise_price_ils | 0.541 | gilat_fy2025 p.168 | text layer: gilat_fy2025 p.168 | kept; B states the same figure in its share-events text |
| 466 | A only | share_events/11/shares | 500,000 | gilat_fy2025 p.168 | text layer: gilat_fy2025 p.168 | kept; B states the same figure in its share-events text |
| 467 | A only | share_events/12/shares | 17,439,580 | gilat_fy2025 p.156, p.165; gilat_fy2024 p.126 | page image: gilat_fy2025 p.156, gilat_fy2025 p.165, gilat_fy2024 p.126 | kept; B states the same figure in its share-events text |
| 468 | A only | share_events/14/price_ils | 0.88 | gilat_fy2025 p.165, p.100 | page image: gilat_fy2025 p.165: 88 agorot = 0.88 ILS (7,710,000 shares for 6,784K ILS) | kept; B states the same figure in its share-events text |
| 469 | A only | share_events/14/shares | 7,710,000 | gilat_fy2025 p.165, p.100 | page image: gilat_fy2025 p.165, gilat_fy2025 p.100 | kept; B states the same figure in its share-events text |
| 470 | A only | share_events/16/shares | 4,665,000 | gilat_fy2025 p.166-167 | page image: gilat_fy2025 p.166 | kept; B states the same figure in its share-events text |
| 471 | A only | share_events/17/shares | 4,000,000 | gilat_fy2025 p.166 | page image: gilat_fy2025 p.166 | kept; B states the same figure in its share-events text |
| 472 | A only | share_events/18/shares | 12,093,500 | gilat_fy2025 p.172 | page image: gilat_fy2025 p.172 | kept; B states the same figure in its share-events text |
| 473 | A only | share_events/22/shares | 25,773,849 | gilat_h1_2026 p.37 | arithmetic: re-computed 25,773,849 (C + D conversion shares H1 2026 (p.37)) | kept; A only |
| 474 | A only | share_events/23/price_ils | 2.59 | gilat_h1_2026 p.37, p.3 | page image: gilat_h1_2026 p.37: weighted average 258.97 agorot before fees = 2.5897 ILS | kept; A only |
| 475 | A only | share_events/23/shares | -2,300,000 | gilat_h1_2026 p.37, p.3 | page image: gilat_h1_2026 p.37, gilat_h1_2026 p.3 | kept; A only |
| 476 | A only | share_events/24/shares | 1,623,812 | gilat_h1_2026 p.37 | arithmetic: re-computed 1,623,812 (post-period conversion shares (p.37)) | kept; A only |

### 6.17 Tax (9)

| # | side | item | value | ref | check | resolution |
|---:|---|---|---:|---|---|---|
| 477 | A only | tax/final_assessments_through | 2,020 | gilat_fy2025 p.164 | page image: gilat_fy2025 p.164 | kept (one extraction only; see check) |
| 478 | A only | tax/statutory_rate | 0.23 | gilat_fy2025 p.164 | page image: gilat_fy2025 p.164 | kept (one extraction only; see check) |
| 479 | A only | tax/unrecognised_capitalised_finance_expenses/2022 | 2,065 | gilat_fy2023 p.149; gilat_fy2025 p.163 | page image: gilat_fy2023 p.149, gilat_fy2025 p.163 | kept (one extraction only; see check) |
| 480 | A only | tax/unrecognised_capitalised_finance_expenses/2023 | 1,971 | gilat_fy2023 p.149; gilat_fy2025 p.163 | page image: gilat_fy2023 p.149, gilat_fy2025 p.163 | kept (one extraction only; see check) |
| 481 | A only | tax/unrecognised_capitalised_finance_expenses/2024 | 1,964 | gilat_fy2023 p.149; gilat_fy2025 p.163 | page image: gilat_fy2023 p.149, gilat_fy2025 p.163 | kept (one extraction only; see check) |
| 482 | A only | tax/unrecognised_capitalised_finance_expenses/2025 | 2,278 | gilat_fy2023 p.149; gilat_fy2025 p.163 | page image: gilat_fy2023 p.149, gilat_fy2025 p.163 | kept (one extraction only; see check) |
| 483 | A only | tax/unrecognised_tax_losses_gross/2022 | 28,361 | gilat_fy2023 p.149; gilat_fy2025 p.163 | page image: gilat_fy2023 p.149, gilat_fy2025 p.163 | kept (one extraction only; see check) |
| 484 | A only | tax/unrecognised_tax_losses_gross/2023 | 25,580 | gilat_fy2023 p.149; gilat_fy2025 p.163 | page image: gilat_fy2023 p.149, gilat_fy2025 p.163 | kept (one extraction only; see check) |
| 485 | A only | tax/unrecognised_tax_losses_gross/2024 | 21,917 | gilat_fy2023 p.149; gilat_fy2025 p.163 | page image: gilat_fy2023 p.149, gilat_fy2025 p.163 | kept (one extraction only; see check) |

### 6.18 Working capital (B) (17)

| # | side | item | value | ref | check | resolution |
|---:|---|---|---:|---|---|---|
| 486 | B only | working_capital/cf_wc_change_excl_iru_prepayment_FY2025 | 1,164 | derived: WC change -2,738 + IRU prepayment 3,902 | arithmetic: re-computed 1,164 (WC change + IRU prepayment (gilat_fy2025 p.131)) | kept (one extraction only; see check) |
| 487 | B only | working_capital/h1_2026_balance_moves_ILS/deferred_expenses_bezeq | 7,224 | derived: (6,974 + 9,255) - (3,547 + 5,458) | arithmetic: re-computed 7,224 (p.9) | kept (one extraction only; see check) |
| 488 | B only | working_capital/h1_2026_balance_moves_ILS/inventory | 90 | derived: 3,988 - 3,898 | arithmetic: re-computed 90 (p.9) | kept (one extraction only; see check) |
| 489 | B only | working_capital/h1_2026_balance_moves_ILS/trade_payables | 7,517 | derived: 66,532 - 59,015 | arithmetic: re-computed 7,517 (p.9) | kept (one extraction only; see check) |
| 490 | B only | working_capital/h1_2026_balance_moves_ILS/trade_receivables | 11,701 | derived: 30.6.2026 63,411 - 31.12.2025 51,710 (gilat_h1_2026 p.9) | arithmetic: re-computed 11,701 (p.9) | kept (one extraction only; see check) |
| 491 | B only | working_capital/payable_days_vs_cost_of_revenue/FY2022 | 144.7 |  | arithmetic: re-computed 144.7 (payables / COGS x 365) | kept as B's analytic ratio (not a document figure) |
| 492 | B only | working_capital/payable_days_vs_cost_of_revenue/FY2023 | 154.4 |  | arithmetic: re-computed 154.4 (payables / COGS x 365) | kept as B's analytic ratio (not a document figure) |
| 493 | B only | working_capital/payable_days_vs_cost_of_revenue/FY2024 | 114.3 |  | arithmetic: re-computed 114.3 (payables / COGS x 365) | kept as B's analytic ratio (not a document figure) |
| 494 | B only | working_capital/payable_days_vs_cost_of_revenue/FY2025 | 128 |  | arithmetic: re-computed 128.0 (payables / COGS x 365) | kept as B's analytic ratio (not a document figure) |
| 495 | B only | working_capital/payable_days_vs_cost_of_revenue/H1_2026_ttm | 127.2 |  | arithmetic: re-computed 127.2 (payables / TTM COGS x 365) | kept as B's analytic ratio (not a document figure) |
| 496 | B only | working_capital/receivable_days/FY2022/year_end_basis | 45.2 | gilat_fy2023 p.138; gilat_fy2025 p.147; gilat_h1_2026 p.9 | arithmetic: re-computed 45.2 (net receivables / revenue x 365) | kept as B's analytic ratio (not a document figure) |
| 497 | B only | working_capital/receivable_days/FY2023/year_end_basis | 68.3 | gilat_fy2023 p.138; gilat_fy2025 p.147; gilat_h1_2026 p.9 | arithmetic: re-computed 68.3 (net receivables / revenue x 365) | kept as B's analytic ratio (not a document figure) |
| 498 | B only | working_capital/receivable_days/FY2024/year_end_basis | 62.3 | gilat_fy2023 p.138; gilat_fy2025 p.147; gilat_h1_2026 p.9 | arithmetic: re-computed 62.3 (net receivables / revenue x 365) | kept as B's analytic ratio (not a document figure) |
| 499 | B only | working_capital/receivable_days/FY2025/q4_annualised_basis | 70 | gilat_fy2023 p.138; gilat_fy2025 p.147; gilat_h1_2026 p.9 | arithmetic: re-computed 70.0 (receivables / (Q4 revenue x 4) x 365) | kept as B's analytic ratio (not a document figure) |
| 500 | B only | working_capital/receivable_days/FY2025/year_end_basis | 78.1 | gilat_fy2023 p.138; gilat_fy2025 p.147; gilat_h1_2026 p.9 | arithmetic: re-computed 78.1 (net receivables / revenue x 365) | kept as B's analytic ratio (not a document figure) |
| 501 | B only | working_capital/receivable_days/H1_2026/q2_annualised_basis | 81 | gilat_fy2023 p.138; gilat_fy2025 p.147; gilat_h1_2026 p.9 | arithmetic: re-computed 81.0 (receivables / (Q2 x 4) x 365) | kept as B's analytic ratio (not a document figure) |
| 502 | B only | working_capital/receivable_days/H1_2026/ttm_basis | 83.8 | gilat_fy2023 p.138; gilat_fy2025 p.147; gilat_h1_2026 p.9 | arithmetic: re-computed 83.8 (receivables / TTM revenue x 365) | kept as B's analytic ratio (not a document figure) |

## 7. Agreed "not disclosed" (both extractions null)

FY2021.capitalised_contract_costs, FY2021.total_assets, FY2021.trade_receivables, FY2021.inventory, FY2021.trade_payables, FY2021.employees, FY2022.capitalised_contract_costs, FY2023.capitalised_contract_costs, H1_2025.shares_weighted_basic, H1_2025.shares_weighted_diluted, H1_2026.sbc, H1_2026.tax_paid, H1_2026.interest_paid_bonds, H1_2026.wc_change, H1_2026.shares_weighted_basic, H1_2026.shares_weighted_diluted, weighted H1_2026 basic, weighted H1_2026 diluted, fx avg H1 2026.
These are mostly H1 2026 items (SBC, tax paid, interest paid, working-capital change, weighted shares, PPE/ROU/intangible D&A split) that
would be in the consolidated interim statements, which are not in the supplied PDF; `derived.py` estimates the ones it needs and labels them UNVERIFIED.

## 8. Files

* fin_A: `/tmp/claude-0/-home-user-value-investing-fund---selected-company-reaserch/8e9bb9a6-b39f-5c24-a635-b21606f1c8ae/scratchpad/work/gilat_telecom/fin_A.json`
* fin_B: `/tmp/claude-0/-home-user-value-investing-fund---selected-company-reaserch/8e9bb9a6-b39f-5c24-a635-b21606f1c8ae/scratchpad/work/gilat_telecom/fin_B.json`
* reconcile_log: `/tmp/claude-0/-home-user-value-investing-fund---selected-company-reaserch/8e9bb9a6-b39f-5c24-a635-b21606f1c8ae/scratchpad/work/gilat_telecom/reconcile.md`
* item_index: `/tmp/claude-0/-home-user-value-investing-fund---selected-company-reaserch/8e9bb9a6-b39f-5c24-a635-b21606f1c8ae/scratchpad/work/gilat_telecom/recon/discrepancies.json`
* page_image_log: `/tmp/claude-0/-home-user-value-investing-fund---selected-company-reaserch/8e9bb9a6-b39f-5c24-a635-b21606f1c8ae/scratchpad/work/gilat_telecom/recon/viewed_log.md`
* comparison: `/tmp/claude-0/-home-user-value-investing-fund---selected-company-reaserch/8e9bb9a6-b39f-5c24-a635-b21606f1c8ae/scratchpad/work/gilat_telecom/recon/full_compare.py`
* builder: `/tmp/claude-0/-home-user-value-investing-fund---selected-company-reaserch/8e9bb9a6-b39f-5c24-a635-b21606f1c8ae/scratchpad/work/gilat_telecom/build_financials.py`
* derived metrics: `derived.py` -> `derived.txt`
