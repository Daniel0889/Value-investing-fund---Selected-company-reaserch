# Paymeant Financial Technologies (TASE 1180876) — inputs and sources, 3.11.2026

**Status: statement figures VERIFIED against the filings; market data confirmed by two or more sites; the items
marked UNVERIFIED are not verified.** The final verification (`verification.md`) re-read the disputed pages as images
and corrected these input rows: y10, covenants, options, lease interest and the deferred tax liability. No price, rate
or date was updated.

- **Filings.** Every P&L, balance-sheet, cash-flow and note figure comes from the company's four filings, supplied by
  the investor: `paymeant_fy2023`, `paymeant_fy2024`, `paymeant_fy2025` (annual reports) and `paymeant_h1_2026` (Q2 2026
  report). Page numbers are PDF page indexes.
  - Two independent extractions were reconciled (`research/paymeant/work/reconcile.md`, `financials.json`).
  - The figures used were read on the PDF page images, and the red team and the CIO gate re-read the disputed ones.
  - The reports use the small-corporation and TA Tech-Elite reliefs, so disclosure is thinner than usual. There is no
    ICFR report, and the half-year report is a short "main developments" report.
- **Market data.** Price, share count, turnover and holders come from Bizportal, TheMarker, Globes and StockAnalysis,
  read on 3.11.2026 (Israel time). The 39,330,034 shares × 3.18 reproduce Mega's market value of 125,069,508.12 exactly.
- **Not read.**
  - maya.tase.co.il, mayafiles.tase.co.il and www.tase.co.il block scripted access (HTTP 403).
  - The bodies of the two TheMarker articles (HTTP 403; themarker.com does not resolve for WebFetch).
  - funder.co.il (HTTP 403).
  - The court databases and the class-action register (not searchable here).
  - The Pledges Registrar by name (its open data carries no names).
- **UNVERIFIED** (treated conservatively, and listed as open in `thesis_he.md` §14):
  - the economic credit cost on the 203,167 fair-value book, and where the 4,395 of defaulted loans sit;
  - the SPC lender, its terms, the indemnity caps and the outstanding pools;
  - the "360" payment-guarantee volume and losses;
  - the held book's discount-rate sensitivity;
  - the October 2026 seller;
  - pledges of the founders' shares;
  - the June 2023 agreement with the founders, and the results of the 30.3.2026 general meeting;
  - the Maya reports since 30.6.2026 (headlines only);
  - the 30.6.2026 share count (between 39,245,034 and 39,330,034);
  - FY2021 bank credit of 6,389 (the cash-flow statement and note 13f of the filing disagree);
  - the founders' sale of 13.3.2026 (one source, Globes);
  - peer figures (Tier 2: S&P Global via StockAnalysis, not checked against the peers' filings).
- **Before any decision, read:**
  - the Q3 2026 report (expected about 17.11.2026);
  - the Maya reports since 30.6.2026;
  - the court and class-action registers;
  - the Pledges Registrar, searched by name.

## Inputs (as used in `valuation.py`)

Units: ILS thousands unless stated; per-share figures in ILS (1 ILS = 100 agorot).

### Market and rates

| Input | Value | Source |
|---|---|---|
| Price used | 3.173 ILS (317.3 agorot), official close 3.11.2026 | TheMarker quote page 17:24; Bizportal general view (market.md §0) |
| Mega snapshot | 3.18 ILS at 14:04; market value 125,069,508.12 ILS; P/E 6.64, P/B 1.41 (on the 2.11.2026 close of 311.8) | Mega "Ace" export (brief); market.md §1 |
| Shares registered for trading | 39,330,034 (3.11.2026) | Bizportal general view ("הון רשום למסחר"); StockAnalysis "Shares Out 39.33M"; Mega cap ÷ 3.18 |
| Shares at year-end | FY2021 30,903,464 (derived); FY2022 36,890,750; FY2023 37,021,525; FY2024 37,278,200; FY2025 39,245,034 | paymeant_fy2023 p.107-109; paymeant_fy2025 p.108 (note 17a) |
| Market cap at the price | 124,794 = USD 39.5M | out §0 |
| Israel 10-year (y10) | 4.162%, the generic 10-year on 3.11.2026 (the series the Gilat Telecom study of the same date uses). Cross-check: 4.29% YTM on ממשל שקלית 0537, a single bond with 10.58 years to run (3.11.2026 17:14) | Trading Economics (17:42); TheMarker bond page 1166180 (market.md §5). Neither is a primary source; the Bank of Israel or Ministry of Finance benchmark would be |
| Hurdle r | 10% = max(10%, 4.16% + 3); 10% on the cross-check too, and still 10% at y10 + 2 points | out §0 |
| USD/ILS | 3.157 (Bank of Israel representative rate, 3.11.2026) | brief |
| Bank of Israel rate | 3.25%, held 21.10.2026; next decision 23.11.2026 | Bizportal 21.10.2026 (market.md §5) |
| Daily turnover, 60 sessions 4.8-3.11.2026 | median 19,125 ILS; 25th percentile 2,590 ILS; 3.11.2026 session 352,392 ILS (111,691 shares) | Bizportal history call, read 3.11.2026 21:15 (scuttlebutt.md [BZ-RT]); Bizportal general view |
| Price-reliability block (out §6) | the 3.11.2026 close came from 46 trades in a range of 307.5-319 agorot | Bizportal transactions page, read 18:01 (scuttlebutt.md [BZ-TRANS]) |
| October trading | 3,485,393 shares, 20.10-3.11.2026 = 8.86% of the company, all on-exchange | Bizportal / StockAnalysis daily data (out §6; market.md §2) |
| Liquidity floor / price-reliability line | 50,000 / 100,000 ILS median daily turnover | charter; screen_spec X5 |
| Peer medians (Direct Finance, Menif, Michlol, Jacob, Opal; TTM) | P/E 7.67; P/B 1.37; ROE 17.5% (Tier 2) | StockAnalysis statistics pages, 3.11.2026 21:29 (scuttlebutt.md §1.2) |
| Blender (listed BNPL rival) | net losses 72.5M ILS in 2021-2025 (Tier 2) | StockAnalysis BLND income statement (scuttlebutt.md §1.3) |

### Income statement (FY2021-FY2023 paymeant_fy2023 p.82; FY2024 paymeant_fy2024 p.81; FY2025 paymeant_fy2025 p.83; H1 paymeant_h1_2026 p.24)

| Input | Value | Source |
|---|---|---|
| Revenue | 7,850 / 23,874 / 38,524 / 43,046 / 56,616 (FY2021-FY2025); H1 2025 24,827; H1 2026 28,512; TTM 60,301 | pages above; TTM = FY2025 + H1 2026 − H1 2025 |
| Funding cost (above operating profit) | 90 / 1,982 / 7,750 / 5,224 / 4,711; H1 1,477 / 2,738 | pages above |
| Operating profit before other items | 1,516 / 8,295 / 13,500 / 17,216 / 23,772; H1 10,272 / 10,960; TTM 24,460 | pages above |
| Other items (note 19e) | (2,285) / 437 / (228) / 0 / 0: IPO grant and share-based pay 288 / 751 / 228; options vested at once 1,997 (2021); termination income (1,188) (2022) | paymeant_fy2023 p.111 |
| Tax | 0 / (77) / 2,974 / 3,925 / 5,584; H1 2,265 / 2,675; statutory 23%; reconciliation "other" −79 / −35 / +116 (FY2023-FY2025) | pages above; paymeant_fy2025 p.106 |
| Net income to owners | (769) / 8,809 / 10,298 / 13,291 / 18,188; H1 8,007 / 8,285; TTM 18,466 | pages above |
| Basic EPS (ILS) | (0.03) / 0.26 / 0.28 / 0.36 / 0.47 | pages above |
| Q1 / Q2 2024 revenue and NI | 9,686 / 8,776; 2,702 / 2,308 | paymeant_fy2024 p.117 |
| Credit-loss charge; opex | FY2025 783, H1 441 / 670; opex FY2025 27,350, H1 12,637 / 14,144 | paymeant_h1_2026 p.24 |
| Fees; loan sales + fair value | FY2025 27,278 / 16,301; H1 2025 11,154 / 8,575; H1 2026 15,699 / 6,068 | paymeant_h1_2026 p.32 (note 4) |
| Originations (ILS M) | 365 / 389 / 535 (2023-2025); H1 2025 240; H1 2026 258 | paymeant_fy2025 p.42; paymeant_h1_2026 p.15 |
| Share sold 2025; loan duration; nominal borrower rate | 60%; 14 months; 9.83% / 8.59% / 7.96% (2023-2025) | paymeant_fy2025 p.42 |
| Stated origination run-rate | about 640M (Feb 2026), cut to about 600M (Aug 2026) | paymeant_fy2025 p.7, p.59; paymeant_h1_2026 p.5 |

### Cash flow (FY2023-FY2025 paymeant_fy2025 p.85; H1 paymeant_h1_2026 p.28)

| Input | Value | Source |
|---|---|---|
| D&A | 944 / 2,140 / 3,194; H1 1,470 / 1,554; TTM 3,278 | pages above |
| Share-based pay | 750 / 78 / 816; H1 411 / 336 | pages above |
| Operating cash flow (reported) | −5,296 / 3,910 / 2,785; H1 −4,942 / 5,236; TTM 12,963 (UNRECONCILED, see C7) | pages above |
| Change in bank credit inside OCF | FY2025 21,831; H1 2025 −19,060; H1 2026 10,985 | pages above |
| Capex: PP&E; development (cash); capitalised SBP; ROU | 116 / 128 / 559 and 266 / 28; 2,789 / 2,211 / 1,167 and 642 / 1,902; 104 / 145 / 112 and 55 / 92; 0 / 0 / 25 and 25 / 0 | pages above |
| Lease principal | 520 / 575 / 1,017; H1 466 / 368 | pages above |
| Lease interest | 49 (FY2024) / 191 (FY2025), inside the funding-cost line (finance expense 4,711, note 20); 191 leaves the lender-basis earnings, because the lease liability is deducted in the bridge | paymeant_fy2025 p.97 (note 9a), p.114 |
| Dividends paid | FY2025 9,000; H1 2025 4,000; H1 2026 4,000 (FY2023 6,000; FY2024 7,000) | pages above; financials.json |
| Tax paid | FY2025 7,124; H1 2025 none as presented; H1 2026 3,758 | paymeant_h1_2026 p.28 |
| Capitalised development (additions; amortisation) | 2,377 / 2,892 / 2,356 / 1,279 (FY2022-FY2025); 127 / 226 / 1,373 / 1,892 | paymeant_fy2023 p.98; paymeant_fy2025 p.98 |
| Controllers' pay capitalised | 1,363 / 751 / 500 (2023-2025) | paymeant_fy2025 p.115 (note 21b) |

### Balance sheets (31.12.2022 paymeant_fy2023 p.81; 31.12.2023 restated and 31.12.2024 paymeant_fy2024 p.80; 31.12.2025 paymeant_fy2025 p.82; 30.6.2025 and 30.6.2026 paymeant_h1_2026 p.23)

| Input | Value at 30.6.2026 | Source |
|---|---|---|
| Cash (in pledged, dedicated accounts) | 4,877 | p.23; paymeant_fy2025 p.99 (note 11b) |
| Loans held for sale at fair value | 203,167; at amortised cost 193,652; step-up 9,515 | p.23; paymeant_h1_2026 p.31 |
| Loans at amortised cost; receivables | 6,686; 5,875 | p.23 |
| Bank credit (on-call, short-term) | 115,225 | p.23, p.31 |
| Payables for credit transactions | 19,273 | p.23 |
| Lease liabilities | 2,594 (781 current + 1,813 non-current) | p.23 |
| Intangibles | 8,269 | p.23 |
| Deferred tax liability, net | 1,919 (non-current). At 31.12.2025 it was the liability on the intangible asset (1,681) and on the loans' fair-value step-up (1,934) less deferred tax assets (2,385); released in the worst-case low end, which removes both | p.23; paymeant_fy2025 p.105 (note 15d, image) |
| Equity to owners | 86,912 (no NCI, no preferred) | p.23 |
| Total assets; current assets | 231,943; 215,334 | p.23 |
| Equity, earlier dates | 22,163 (31.12.2021, paymeant_fy2023 p.83); 56,186; 61,569; 68,081; 82,198; 76,556 (30.6.2025) | pages above |
| FY2021 total assets | 32,944 | paymeant_fy2023 p.19 |

### Funding, covenants, credit, dilution and holders

| Input | Value | Source |
|---|---|---|
| Bank lines (31.12.2025) | 340,000 at four banks, on-call, prime +0.5% to +0.8%; drawn A 0, B 92,000, C 1,000, D 11,000 (bank B 88.5% of 104,000 drawn) | paymeant_fy2025 p.48-49 (image) |
| "The financing bodies may stop the engagement unilaterally" | — | paymeant_fy2025 p.55 |
| Covenants (note 11a(6)) | (a) tangible equity ≥ 20% of the total balance sheet (or the tangible balance sheet); (b) equity ≥ 25M; (c) senior debt ≤ 80% of loans; (d) annual net profit ≥ 1M; change-of-control restrictions; grounds for immediate repayment | paymeant_fy2025 p.99 (image); paymeant_h1_2026 p.33 (note 5e) |
| Directors' report covenant tables | (a) 34% of the balance sheet, 33%-34% of the tangible balance sheet (30.6.2026); 35% and 32%-40% (31.12.2025). (b) is written as tangible equity there, the stricter reading, which the record tests | paymeant_h1_2026 p.18; paymeant_fy2025 p.68 (images) |
| Company's covenant "tangible equity" | 82M (31.12.2025); 76,000 (30.6.2026) | paymeant_fy2025 p.68; paymeant_h1_2026 p.18 |
| Rate sensitivity | 1,152 pre-tax per point on bank credit | paymeant_h1_2026 p.9 |
| CPI sensitivity | 1,981 fair value per CPI point | paymeant_h1_2026 p.8 |
| Arrears (current / 1-90 days / default) | 186,422 / 3,590 / 1,481 (31.12.2025); 200,260 / 5,198 / 4,395 (30.6.2026) | paymeant_fy2025 p.66; paymeant_h1_2026 p.15 |
| Amortised-cost book (gross; provision) | 2,859; 1,831 (2024) and 5,731; 934 (2025) | paymeant_fy2025 p.95 |
| Sales to own unconsolidated SPCs | 60,000 (6.2023); 90,000 (2.2024); 85,000 (9.2024); 80,000 (1.2025); 60,000 (3.2025); 84,000 (10.2025); 80,000 (2.2026) | paymeant_fy2025 p.106-108; paymeant_h1_2026 p.6-7 |
| SPC indemnities "for breach of representations and in other cases" | not quantified | paymeant_h1_2026 p.7, p.33 |
| Merchants may cancel "at any time and for any reason" | — | paymeant_fy2025 p.41 |
| BNPL circular 2026-10-4 | published 12.7.2026, in force 12.1.2027; credit cancelled when goods or services are not supplied | paymeant_h1_2026 p.7-8; Gornitzky note 29.7.2026 |
| Credit Data Law amendment 6 | published 26.7.2026, in force six months later; negative data kept 1 year, not 3 | paymeant_h1_2026 p.7 |
| Options and RSUs (treasury method) | 1,000,000 at 3.01 (founders, 15.1.2025); 519,000 at 3.97 less 100,040 forfeited; Amitim 255,000 at 6.05 to 12.1.2027; at 0.01: 260,915 at 31.12.2025 by note 17's roll-forward (2,737,750 − 1,920,000 warrants − 510,000 Amitim − 46,835 exercised in 2025), less the 85,000 shares issued in 2026; 175,000 RSUs; 512,000 at 5.74 (20.8.2026). The 31.7.2023 and 25.2.2024 grants vest nothing before 1.8.2025 and 1.4.2026, so the 2024 exercises came from earlier grants | paymeant_fy2025 p.108-112 (p.109-112 images); paymeant_h1_2026 p.25, p.33; out §2 (the netting is done in valuation.py) |
| Note 17 against Reg. 24A option counts | 2,189,875 at 4.02 against 1,136,125 (not reconciled by the company). The 2,189,875 are all identified; they average 3.54, and 4.02 without the 0.01 options | paymeant_fy2025 p.112, p.123; out §2 |
| 2025 exercises | 1,966,835 shares at a weighted 2.02 | paymeant_fy2025 p.112 |
| Founders' 2022 exercise | 985,000 shares for 10k in total | paymeant_fy2023 p.107 |
| Founders' holdings | Gilor 6,907,886 + Yochanan 4,709,381 = 11,617,267 (29.54%); voting agreement while above 25% | Globes and Bizportal registers 3.11.2026 (scuttlebutt.md §5); paymeant_fy2025 p.123 |
| Founders' sale | 869,564 shares at 6.90 on 13.3.2026 | Globes interested-party register (one source; market.md §3) |
| Founders' pay 2025 | 2,484 each (salary 1,524, bonus 750, options 210); bonus 4% / 3% / 2.5% of pre-tax profit, uncapped; salary 92k to 110k a month (board 22.2.2026) | paymeant_fy2025 p.118-121; paymeant_h1_2026 p.19 |
| Options refused by the general meeting | 23.12.2025 | paymeant_fy2025 p.131 |
| Buyback plan | up to 5M, 18.11.2024-18.11.2026; nothing bought | paymeant_fy2025 p.69, p.112; paymeant_h1_2026 p.25 |
| "Adjusted EBITDA" adds back share-based pay | 816 (2025); 336 (H1 2026) | paymeant_fy2025 p.66-67; paymeant_h1_2026 p.16 |
| FX exposure | "not material" | paymeant_fy2025 p.101 |
| Business workstream's through-cycle pre-tax (cross-check only) | 20,679 (3.74% × 553M) | business.md §12 |

### Assumptions (stated, not facts; `valuation.py` §5)

| Assumption | Value | Basis |
|---|---|---|
| Base growth | 2% a year (CPI, midpoint of the Bank of Israel's 1-3% target) | B4 accepted at the gate |
| Optimistic growth | 5% | the first version's base, kept for the optimistic case only |
| Scenario probabilities | worst 15%, conservative 25%, base 40%, optimistic 20% | uncalibrated |
| Worst-case recoveries | defaulted loans 30%; receivables 50%; wind-down: six months of half the TTM opex | B9 accepted |
| Provision coverage tests | 50% / 70% on defaulted loans (their location is UNVERIFIED) | B5 accepted |
| f3 loss severity | 60% | framework f3 |
| Rate shock; repricing lag; low held-book duration | +2 points; six months; 7 months | B7 accepted |
| Data flags | cycle_window_short, derived_tier2_field, microcap_field_unavailable (capped at +10) | charter tier table |

## Differences of basis between workstream files (the record uses `output.txt`)

- **Bank B's share of drawn credit.** 88.5% on the line table (92,000 of 104,000, paymeant_fy2025 p.49), against
  0.883 in `financials.json` (denominator 104,241 from the balance sheet; reconcile.md §A).
- **Peer P/E.** scuttlebutt.md uses StockAnalysis' 6.93 (−9.6% to the median; P/B +5.3%). out §6 computes 6.76 at 3.173
  (−11.9%; P/B +4.8%).
- **Liquidity before the fall.** out §6 gives 12,476 for the sessions before 20.10 inside the 60-session window.
  scuttlebutt.md §7 gives 12,250 for the 60 sessions to 19.10.
- **October volume.** market.md §2 gives 3,373,702 shares (8.58%, to 2.11). out §6 gives 3,485,393 (8.86%, to 3.11).
- **Mega's dividend yield.** Mega shows 3.68%, which cannot be reproduced. Dividends paid in the 12 months to 3.11.2026
  were 22.93 agorot, 7.21% at 318.0 (market.md §1).

URLs (all read on 3.11.2026 unless marked):
- https://www.bizportal.co.il/capitalmarket/quote/generalview/1180876
- https://www.bizportal.co.il/ajax/biz_papers_helper.ashx?action=get_paper_yearly_graph&request_type=1&paper_id=1180876&period=6
- https://www.bizportal.co.il/ajax/biz_papers_helper.ashx?action=get_paper_yearly_graph&request_type=2&paper_id=1180876&period=6&page_number=1
- https://www.bizportal.co.il/capitalmarket/quote/performance/1180876
- https://www.bizportal.co.il/capitalmarket/quote/transactions/1180876
- https://www.bizportal.co.il/capitalmarket/quote/dividends/1180876
- https://www.bizportal.co.il/capitalmarket/quote/stakeholders/1180876
- https://www.bizportal.co.il/ajax/biz_papers_helper.ashx?action=get_holding_flow_summary_data_json&paperId=1180876&period=y
- https://www.bizportal.co.il/capitalmarket/quote/analystadvice/1180876
- https://www.bizportal.co.il/mutualfunds/quote/holdings/5141650
- https://www.bizportal.co.il/capitalmarket/news/article/20046372
- https://www.bizportal.co.il/capitalmarket/news/article/20046488
- https://www.bizportal.co.il/general/news/article/20045608
- https://www.bizportal.co.il/capitalmarket/news/article/20011989
- https://www.bizportal.co.il/capitalmarket/news/article/807179
- https://www.bizportal.co.il/capitalmarket/news/article/809379
- https://www.bizportal.co.il/capitalmarket/news/article/813171
- https://www.bizportal.co.il/capitalmarket/news/article/797516
- https://www.bizportal.co.il/financialconsumerism/news/article/804121
- https://finance.themarker.com/stock/1180876
- https://finance.themarker.com/bond/1166180
- https://www.themarker.com/law/2026-06-18/ty-article/.highlight/0000019e-cf4c-d45a-ab9e-cfeec4490000 (headline only, UNVERIFIED)
- https://www.themarker.com/law/2026-07-12/ty-article-magazine/.highlight/0000019f-4153-d07c-af9f-c95f90af0000 (headline only, UNVERIFIED)
- https://www.globes.co.il/portal/instrument.aspx?instrumentid=370226&mode=reports
- https://www.globes.co.il/news/Instrument/InstrumentHandlers/Get_Instrument_BursaMessage.ashx?instrumentid=370226&feeder=&maxItemsToShow=60
- https://www.globes.co.il/portal/instrument.aspx?instrumentid=370226&mode=company
- https://www.sponser.co.il/Article.aspx?ArticleId=123772
- https://www.ice.co.il/finance/news/article/1135574
- https://www.ice.co.il/finance/news/article/969002
- https://www.ice.co.il/financial-gossip/news/article/1133336
- https://www.ice.co.il/finance/news/article/974528
- https://www.ice.co.il/law/news/article/869052
- https://www.ice.co.il/finance/news/article/863358
- https://www.calcalist.co.il/investing/article/hj3y11krac
- https://www.calcalist.co.il/market/article/ryc7afxbwl
- https://www.calcalist.co.il/market/article/ry3vltoeze
- https://stockanalysis.com/quote/tlv/PMNT/
- https://stockanalysis.com/quote/tlv/PMNT/history/
- https://stockanalysis.com/quote/tlv/PMNT/statistics/ (and the same page for the peers)
- https://stockanalysis.com/quote/tlv/BLND/financials/
- https://tradingeconomics.com/israel/government-bond-yield
- https://www.gornitzky.co.il/wp-content/uploads/pdf/post/31940_bnpl-buy-n.pdf
- https://www.gornitzky.co.il/wp-content/uploads/pdf/post/30672_----------.pdf
- https://www.gov.il/BlobFolder/dynamiccollectorresultitem/knas/he/repository-of-answers_capital-market-authority_knas.pdf
- https://www.gov.il/BlobFolder/reports/report_0010/he/Commisioner%20Report%20Design%20B_chapter2%20ver6_digital.pdf
- https://www.gov.il/BlobFolder/reports/report_0006/he/The_Commissioner's_Report_Chapter_2%20(1).pdf
- https://data.gov.il/api/3/action/datastore_search?resource_id=f004176c-b85f-4542-8901-7b3176f9a054&q=515166544
- https://data.gov.il/api/3/action/datastore_search?resource_id=28780ab5-3ef1-44c7-8377-da82c0aa6781&q=515166544
- https://data.gov.il/api/3/action/datastore_search?resource_id=e7266a9c-fed6-40e4-a28e-8cddc9f44842
- https://cdn.financialreports.eu/financialreports/media/filings/6813/2024/RNS/6813_rns_2024-07-11_b3e0303e-65be-41da-bc5e-a6403413d89a.pdf
- https://www.drushim.co.il/דרושים-3628319-פיימנט-טכנולוגיות-פיננסיות/
