# Gilat Telecom Global (TASE 1080597) — inputs and sources, 3.11.2026

**Status: statement figures VERIFIED against the filings on page images; market data confirmed on two or more
sites; the Bezeq IRU balance and schedule, the one-off amounts, the October 2026 buyback, Series D par at 3.11.2026
and the other items marked UNVERIFIED are not verified.**

- **Filings.** Every P&L, balance-sheet, cash-flow and note figure comes from the company's own filings. Page numbers
  are PDF page indexes of each file (p.1 = first PDF page).
  - Supplied by the investor: `gilat_fy2023`, `gilat_fy2024` (the file name said 2025; the cover says 2024) and
    `gilat_fy2025` (annual reports, USD thousands), and `gilat_h1_2026` (the Q2 2026 report as supplied: directors'
    report and separate (solo) data only, no consolidated interim statements).
  - Downloaded from the company's own site (satcom-gilat.co.il), saved under `scratchpad/work/gilat_telecom/`:
    - `gilat_q2_2026_full`: the same Q2 2026 report with the reviewed consolidated condensed statements (p.27-49);
      its p.1-26 are page for page `gilat_h1_2026` (`web/pdf/company_site_q2_2026_full.pdf`);
    - `gilat_fy2022`: the 2022 annual report, filed 30.3.2023, with the restated FY2020 comparatives
      (`cio_dl/gilat_fy2022_mar.pdf`; the 18.5.2023 re-issue, `cio_dl/gilat_fy2022_may.pdf`, prints the same P&L);
    - `gilat_fy2021`: the 2021 annual report, filed 30.3.2022, with the 31.12.2020 and 31.12.2021 balance sheets
      (`cio_dl/gilat_fy2021.pdf`).
  - Two independent extractions were reconciled (`work/gilat_telecom/reconcile.md`, `financials.json`): 1,322 pairs
    compared, 1,131 identical, 2 definitional differences above 0.5%, 8 rounding differences; all 502 one-sided figures
    checked (350 on page images, 151 by re-computation, 11 on the text layer); none rejected.
  - Page images: 117 pages in the reconciliation (`recon/viewed_log.md`); `gilat_q2_2026_full` p.30-32, 38-39, 46-48
    in the valuation; the disputed pages re-opened by the red team and the CIO gate (`gate.md` §1).
  - The TTM to 30.6.2026 (FY2025 − H1 2025 + H1 2026, ILS) reproduces Mega exactly: operating income 39,534, net income
    32,985, operating cash flow 80,967. The 30.6.2026 identities pass (balance sheet, cash flow, NI / EPS).
  - The company is a "small corporation" and uses the disclosure reliefs (gilat_fy2025 p.2, p.108): no auditor's
    report on internal control.
- **Market data.** Price, share count and market value come from the Bizportal general view and TheMarker (close of
  3.11.2026), cross-checked against the TASE daily series embedded in the company's investor-relations page (to
  29.10.2026). Mega's ILS 198,207,420.626 equals 164.6 agorot × 120,417,631 listed shares exactly. Liquidity uses
  Bizportal's on-exchange proceeds for the 60 sessions to 3.11.2026, cross-checked against the TASE series (1,226
  sessions agree within ILS 999).
- **Not read.**
  - maya.tase.co.il and mayafiles.tase.co.il (HTTP 403) and Magna: the immediate reports since 19.8.2026, the
    general-meeting vote tallies, the holdings reports, the October 2026 buyback reports, the Series C final payment
    report and Bezeq's Hebrew report of 4.11.2025 (only an unofficial English translation was read).
  - funder.co.il and Investing.com (HTTP 403); engineeringnews.co.za (a Cloudflare check, not retried); ynetnews.com
    and ecofinagency.com (did not resolve from the session).
  - The court databases (Nevo, Takdin, Net HaMishpat), the class-action register, the Pledges Registrar by name
    (its open data carries no names) and the Ministry of Defence's procurement records (not searchable here).
- **UNVERIFIED** (treated conservatively, and listed as open in `thesis_he.md` §14):
  - the Bezeq IRU: the unpaid consideration (223,595, derived), the instalment schedule, whether pulse-1 tranches can
    be declined, the amortisation actually applied, the vendor rate and CPI share of the addendum;
  - the one-off amounts: the 2025 satellite-supplier credit (an upper-bound estimate, 4,700) and the H1 2026 war
    equipment (1,308);
  - the October 2026 buyback (2,274,810 shares, about 4,620), from insider feeds and TASE share counts, not Maya;
  - Series D par at 3.11.2026 (26,337,927, derived from the coupon schedule), the Series C final redemption (741)
    and the Series D coupon of 1.10.2026 (738);
  - the count of older options after the H1 2026 exercises (an upper bound);
  - the TTM split of D&A between owned assets and right-of-use assets (used only in the cash proxy);
  - the net USD cost flow (the USD 24M hedge size is the proxy) and the strike and mark-to-market of the remaining
    USD 22M of forwards;
  - the FY2025 lease-interest split in the ILS restatement (both splits are carried);
  - the Intelsat purchase commitments (amount not disclosed);
  - Customer A's identity, the Vodacom renewal, any pledge of the CEO's shares, court cases, the licence renewals due
    31.12.2026, and the Q3 2026 results;
  - peer figures (Tier 2: S&P Global via StockAnalysis, not checked against the peers' filings).
- **Before any decision, read:**
  - the Q3 2026 report (expected late November 2026) and the Maya reports since 19.8.2026;
  - the FY2026 annual report (due by 31.3.2027), for the Bezeq balance, schedule and amortisation;
  - Bezeq's Hebrew report of 4.11.2025;
  - the court databases and the Pledges Registrar (the CEO's shares);
  - the vote tallies of the general meetings of 13-14.3.2024 and 4.12.2025.

## Inputs (as used in `valuation.py`)

Units: ILS thousands unless stated; FY2020-FY2025 in USD thousands (the reporting currency to 31.12.2025); per-share
figures in ILS (1 ILS = 100 agorot). The USD window is converted at one dated rate, 3.157.

### Market and rates

| Input | Value | Source |
|---|---|---|
| Price used | 1.653 ILS (165.3 agorot), close 3.11.2026 (base 170.1) | Bizportal general view "as of 03/11/2026"; TheMarker 17:24 (market.md §0, §1.1) |
| Mega snapshot | ILS 198,207,420.626 at 14:03 = 164.6 agorot × 120,417,631 (−0.4% against the close); P/E 6.21 and P/B 1.55 on the 2.11.2026 close of 170.1 | Mega "Ace" export (brief); market.md §1.3; out §0 |
| Shares listed for trading | 120,417,631, excluding 4,574,810 dormant (bought-back) shares | TASE "registered capital for trading" (Bizportal 3.11.2026; TASE series 29.10.2026); market.md §1.2 |
| Shares outstanding 30.6.2026 | 118,063,162 (derived: conversions, about 652,000 option exercises, less 2,300,000 dormant) | gilat_q2_2026_full p.31, p.49; market.md §1.2; TASE 1.7.2026 118,079,459 |
| Market cap at the price | 199,050 = USD 63.1M | out §0 |
| USD/ILS | 3.157 (Bank of Israel representative rate, 3.11.2026); 3.19 (31.12.2025); 2.978 (30.6.2026) | brief; gilat_q2_2026_full p.43 |
| Israel 10-year | 4.16% (3.11.2026); 4.160% on a second source | TradingEconomics; Investing.com table via search snippet (page 403) |
| US 10-year | 4.91% (2.11.2026); 4.94% (30.10.2026) | US Treasury par yield curve CSV; FRED DGS10 |
| Hurdle r | 10% = max(10%, 4.16% + 3 points); US 4.91% + 3 = 7.91% | out §0 |
| Tax rate | 23% statutory | gilat_fy2025 p.164 |
| Daily turnover, 60 sessions 4.8-3.11.2026 | median 1,325,803 ILS; 25th percentile 1,001,604; mean 1,772,960; no session below ILS 100,000 | Bizportal history call (scuttlebutt.md §7; scuttle_calc_output §1) |
| Turnover a year earlier (60 sessions to 3.11.2025) | median 211,291; 25th percentile 113,160 | same |
| Liquidity cap | 4,006,416 ILS at cost (20 days × 20% × p25) | out §7 |
| Published cross-check | Bizportal 90-day average 1,773,721 (3.11.2026) | Bizportal general view |
| Public holdings | 85.77% excluding every reported interested party; 91.99% if the institutional holder counts as public | scuttle_calc_output §2 (maintenance list: not on it) |
| Largest holders (3.11.2026 count) | CEO Itzik Ben Eliezer 9,547,586 (7.93%); Ayalon mutual funds 7,494,833 (6.22%) | Globes interested parties; Bizportal (scuttlebutt.md §5) |
| Trades | CEO +28,893 at 2.07 (1.10.2026); Meitav funds −1,891,278 at 1.96 (5.10.2026) | Globes insider feed (market.md §3) |
| Short interest | 1.18% of public holdings (23.10.2026), 1.6 days to cover | deeptase.co.il (market.md §2.1) |
| Index weights | TA Tel-Tech 2.46%; TA Growth 1.82%; TA All-Share 0.27% | Bizportal general view |
| Series D quote | 173.2 on 3.11.2026; coupon ILS 724,293 due 1.4.2027 (2.75% of par) | Bizportal bond data 1218205 (market.md §1.4) |

### Window FY2020-FY2025 (USD thousands, audited)

FY2020 from gilat_fy2022 p.119, p.123-124 (cross-checked with gilat_fy2021 p.114-116, p.145-146); FY2021-FY2023
gilat_fy2023 p.116-118, p.122-123; FY2024 gilat_fy2024 p.118-120, p.124-125; FY2025 gilat_fy2025 p.125-127,
p.131-132.

| Input | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|---|
| Revenue | 54,564 | 51,816 | 42,997 | 55,154 | 69,592 | 75,793 |
| Operating profit (EBIT) | 3,649 | −2,731 | −1,499 | 2,178 | 4,949 | 9,689 |
| One-off gain removed (EBIT_adj) | Wiocc credit and dividend 286 (gilat_fy2022 p.123) | — | — | — | — | supplier-credit estimate 1,423 |
| Net income to owners | −1,734 | −5,423 | −4,064 | 715 | 1,786 | 6,350 |
| Operating cash flow | 18,264 | 14,028 | 10,099 | 8,718 | 10,587 | 20,533 |
| Share-based pay | −67 | 63 | 123 | 53 | 51 | 88 |
| Capex: PP&E / intangibles | 3,050 / 390 | 1,810 / 271 | 1,402 / 62 | 3,082 / 196 | 2,529 / 118 | 1,362 / 82 |
| Depreciation of PP&E / licence amortisation | 2,690 / 115 | 3,729 / 141 | 2,640 / 151 | 1,776 / 135 | 1,905 / 136 | 2,130 / 177 |
| Lease principal / lease interest paid | 13,621 / 1,974 | 13,387 / 1,396 | 7,986 / 724 | 4,297 / 408 | 6,717 / 1,698 | 9,521 / 1,788 |
| Other interest paid (bonds, loans) | 898 | 1,075 | 910 | 733 | 470 | 858 |
| Net PP&E / right-of-use assets | 6,074 / 25,588 | 4,529 / 14,937 | 3,292 / 9,168 | 4,599 / 7,541 | 5,223 / 23,856 | 4,455 / 16,769 |
| Current assets (operating) / cash and deposits | 17,297 (26,784 less the Wiocc stake 9,487) / 4,880 | 30,891 / 21,245 | 22,201 / 14,880 | 25,149 / 12,215 | 26,793 / 11,017 | 52,669 / 29,753 |
| Current liabilities / short-term debt incl. current leases and option liabilities | 35,672 / 16,640 | 25,570 / 10,572 | 22,734 / 6,166 | 33,616 / 12,464 | 36,485 / 16,658 | 54,543 / 31,426 |

Other window inputs:

| Input | Value | Source |
|---|---|---|
| FY2019 revenue (used only for the sign of the FY2020 revenue change) | 56,441 | gilat_fy2021 p.116 |
| Customer-relations amortisation (Amort_acq) | 809 a year, 2020-2025; FY2020 also 949 of contract-backlog amortisation, left in EBIT | gilat_fy2021 p.146; gilat_fy2025 p.150 |
| FY2021 doubtful debts (not added back) | 3,191 | gilat_fy2023 p.158 |
| 2025 quarters: revenue / gross profit | 15,994 / 4,521; 18,585 / 5,494; 20,075 / 5,580; 21,139 / 7,455 | gilat_fy2025 p.92 |
| Gross profit FY2020-FY2024 (for "what the base needs") | 15,141; 12,444; 10,495; 12,016; 16,120 | gilat_fy2022 p.119; gilat_fy2023 p.118; gilat_fy2025 p.92 |
| S&M + G&A FY2023 / FY2024 | 9,838 / 11,171 | gilat_fy2023 p.118; gilat_fy2025 p.92, p.96 |
| Basic EPS (USD) FY2020-FY2025 | −0.033; −0.093; −0.070; 0.011; 0.0234; 0.0707 | gilat_fy2022 p.119; gilat_fy2023 p.118; gilat_fy2024 p.120; gilat_fy2025 p.127 |
| Global segment 2025: revenue / result; Vodacom DRC revenue 2025 | 19,655 / 4,106; 12,392 | gilat_fy2025 p.181; p.55 |
| Gross customers 31.12.2024 / 31.12.2025; allowance; customer days | 17,995 / 22,977; 6,767; 62 → 69 | gilat_fy2025 p.147 |
| IRU deferred expense 31.12.2025; IRU paid / amortised in FY2025 | 2,823; 3,902 / 1,079 | gilat_fy2025 p.152, p.131 |
| Unrecognised tax losses 31.12.2025 | USD 19.0M (19,022) | gilat_fy2025 p.163 |
| USD/ILS in 2025 | −12.53% | gilat_q2_2026_full p.43 |
| Shares 31.12.2022 / 31.12.2025 | 58,438,636 / 93,937,313 | gilat_fy2023 p.151; gilat_fy2025 p.165 |

### TTM to 30.6.2026 (ILS thousands; gilat_q2_2026_full p.32, p.38-39, page images)

| Input | FY2025 (translated) | H1 2025 | H1 2026 | TTM |
|---|---|---|---|---|
| Revenue | 260,335 | 124,234 | 139,991 | 276,092 |
| Operating profit | 32,980 (the directors' report p.11 prints 32,981) | 12,841 | 19,395 | 39,534 |
| Pre-tax profit | 19,669 | 4,313 | 15,959 | 31,315 |
| Net income | 21,259 | 4,044 | 15,770 | 32,985 |
| D&A (cash flow) / IRU amortisation | 45,310 / 3,506 | 24,528 / 0 | 21,178 / 3,449 | 41,960 / 6,955 |
| Share-based pay | 292 | 72 | 1,050 | 1,270 |
| FX loss (gain) on cash | (7,686) | 693 | 1,194 | (7,185) |
| Option and warrant revaluation | 8,663 − 609 − 456 | 7,303 − 423 − 311 | 0 | 1,029 |
| Operating cash flow | 69,146 | 21,425 | 33,246 | 80,967 |
| Bezeq IRU payments ("increase in deferred expenses") | 13,752 | 10,711 | 10,673 | 13,714 |
| Capex (PP&E + intangibles) | 4,719 + 276 | 2,596 + 68 | 7,546 + 282 | 10,159 |
| Lease principal / lease interest | 29,364 / 9,584 | 16,092 / 3,526 | 15,318 / 1,892 | 28,590 / 7,950 |
| Bond interest paid | 2,436 | 538 | 1,246 | 3,144 |
| Gross profit; S&M + G&A | 78,938; 45,958 | 35,978; 23,137 | 42,251; 22,856 | 85,211; 45,677 |

| Input | Value | Source |
|---|---|---|
| Satellite-lease depreciation, TTM | 29,676 | gilat_h1_2026 p.6-7, p.13 (financials.json) |
| Non-satellite ROU depreciation FY2025 (TTM split only, UNVERIFIED) | USD 901 (9,983 − 9,082) | gilat_fy2025 p.159 |
| Satellite-segment equipment revenue H1 2025 → H1 2026 | 10,152 → 14,331 | gilat_q2_2026_full p.49 |
| Equipment gross margin 2025 | 31.3% | business_calcs §3, from gilat_fy2025 p.173 |
| ISP segment H1 2026: result / D&A (= IRU amortisation) | 2,613 / 3,449 | gilat_q2_2026_full p.46 (FS note) |
| H1 2025 segment results: directors' report vs FS note | 24,863 vs 30,777 | gilat_h1_2026 p.12; gilat_q2_2026_full p.46 |
| Implied H2 2025 rate (one-off translation) | 3.3023 | derived (gilat_h1_2026 p.6; gilat_fy2025 p.92, p.127) |

### Balance sheet (ILS thousands; 30.6.2026 and 30.6.2025, gilat_q2_2026_full p.30-31, page images)

| Input | 30.6.2026 | Note |
|---|---|---|
| Cash and equivalents | 92,955 | restricted cash 3,500 pledged for guarantees, excluded (gilat_fy2025 p.158) |
| Customers; other receivables and prepaid; inventory | 63,411; 8,862; 3,988 | |
| Bezeq IRU deferred expenses, short / long term | 6,974 / 9,255 | |
| Current assets; total assets | 179,955; 274,482 | |
| Deferred tax asset; ROU; PP&E; intangibles incl. goodwill | 2,403; 43,241; 18,017; 21,337 | goodwill USD 4,428 (gilat_fy2025 p.150) |
| Series C (current); Series D liability component (non-current) | 2,206; 24,307 | |
| Leases, current / long term | 26,232 / 6,884 (total 33,116) | |
| Current liabilities; total liabilities; equity | 110,920; 142,111; 132,371 | no NCI, no preferred, no bank debt |
| 30.6.2025: current assets; cash; current liabilities | 149,039; 66,702; 183,167 | |
| 30.6.2025: short-term debt incl. leases and option liabilities | 103,945 (19,480 + 35,305 + 31,228 + 482 + 145 + 1,234 + 16,071) | |
| 30.6.2025: PP&E; ROU; long-term IRU prepayment | 16,447; 71,085; 5,776 | |
| Identities: basic EPS H1 2026; weighted shares | 0.1459 ILS; 108,088 thousand | p.32 |
| H1 2026 cash flow: investing; financing; FX on cash; opening cash | 7,219; (26,091); (1,284); 79,865 | p.39 |
| Covenants (Series C and D) | net financial debt / assets ≤ 60% (30.6.2026: −24%); equity / assets ≥ 12% (48%); net financial debt / EBITDA ≤ 5 | gilat_h1_2026 p.23, p.25 |

### Currency and linkage (gilat_h1_2026 p.19; gilat_fy2025 p.106; page images)

| Input | Value | Note |
|---|---|---|
| USD monetary assets 30.6.2026 | 24,967 by row (8,984 cash + 13,023 customers + 2,960 other); printed total 25,110 | the column does not foot (C7 flag) |
| USD liabilities 30.6.2026 | 90,430 (24,275 current leases + 60,188 suppliers + 3,347 payables + 116 tax + 2,504 long-term leases) | foots |
| Net USD monetary liabilities | 65,463 at 2.978 (USD 22.0M) → +3,935 at 3.157 | out §3 |
| Unlinked-ILS asset rows; cash row | 138,235 (printed 138,321); 84,007 + 8,984 = 92,991 against 92,955 | C7 flags; rows used |
| Forwards | buy USD 2M a month to 12.2026 and USD 1.5M a month in 2027: USD 22M left at 3.11.2026; strike undisclosed, not credited | gilat_h1_2026 p.19 |
| Net USD cost flow proxy | USD 24M a year (the hedge size) | UNVERIFIED |
| 31.12.2025 linkage | USD liabilities 29,314; USD assets 6,219, of which cash 866 (USD k) | gilat_fy2025 p.106 |

### Events after 30.6.2026 (pro forma to 3.11.2026; Q3 operating cash flow not added)

| Input | Value | Source |
|---|---|---|
| October buyback (ILS 7M programme of 7.10.2026) | 2,274,810 shares at about 203.1 agorot = 4,620 | Globes insider feed, TASE counts (market.md calc §3); UNVERIFIED against Maya |
| June buyback | 2,300,000 shares, 5,988 incl. fees (260.36 agorot; 258.97 before fees) | gilat_q2_2026_full p.49 (note 7), p.39; gilat_h1_2026 p.37 |
| Series C public par 19.8.2026; converted 1.7-19.8 / after 19.8 | 984,967; 1,240,026 par / about 192,435 shares (derived, UNVERIFIED); the rest redeemed on 1.9.2026 (final 34%) with the last half-year coupon (4.5% a year) → 741 | gilat_h1_2026 p.22, p.37; market.md calc §4 |
| Series D par 19.8.2026 → 3.11.2026 | 29,134,661 → 26,337,927 (derived from the coupon schedule); October conversions 509,030 shares; coupon of 1.10.2026 → 738 | gilat_h1_2026 p.24; Bizportal bond data; market.md calc §3-4 |
| Pro forma cash | 92,955 − 4,620 − 741 − 738 = 86,855 | out §3 |

### Bonds, options and share count

| Input | Value | Source |
|---|---|---|
| Series D terms | 5.5% fixed, unlinked; converts 1 share per ILS 1 par until 1.4.2028, then per ILS 1.40 to 21.3.2031; principal 25% a year on 1.4.2028-1.4.2031 | gilat_h1_2026 p.24; gilat_fy2025 p.157 |
| Series D issued (2.2025) | 45,872,000 par | gilat_fy2025 p.157 |
| H1 2026 conversions | Series C 13,151,410 par → 9,741,785 shares (at 1.35); Series D 16,032,064 par → 16,032,064 shares | gilat_h1_2026 p.37; gilat_q2_2026_full p.49 |
| Options (net exercise) | CEO December 2025: 2,000,000 at 1.1015 + 2,000,000 at 0.927; employees and officers November 2025: 750,000 at 1.1015 + 3,915,000 at 0.927; older 3,428,500 at USD 0.23 × 3.19 (upper bound) | gilat_fy2025 p.166, p.172, p.206 |
| Options outstanding 31.12.2025 | 12,093,500, of which 2,899,047 exercisable | gilat_fy2025 p.172 |
| Earlier issues | CEO placement and rights issue at 0.30 (7.2023); Series C exchange 17,439,580 shares (7.2024); placement 7,710,000 at 0.88 (7.2025) | gilat_fy2023 p.151, p.183; gilat_fy2024 p.155; gilat_fy2025 p.165 |

### Bezeq IRU (off balance sheet except amounts paid; gilat_fy2025 p.40-42, p.152-153, p.183, page images)

| Input | Value | Note |
|---|---|---|
| IRU-1 (12.2024) | 18,000 lines at ILS 4,890 a line for 15 years (88.02M + VAT): pulse 1 8,000 lines from 1.1.2025 (39.12M); pulses 2 and 3, 5,000 lines each in four quarterly tranches from 1.4.2025 and 1.4.2026 (24.45M each, + 50% of CPI differences) | p.152-153 |
| IRU-2 pulse 1 (addendum, 11.2025) | 36,000 lines in 12 quarterly tranches of 3,000 from 12.2025; about ILS 160M "assuming full exercise", CPI-linked (50% assumed) | p.42, p.183 |
| Later pulses | 18,000 lines each in 2029, 2031 and 2033 (about ILS 80M each); release only from a subsequent pulse if growth targets are missed | p.42, p.183 |
| Payment terms | each pulse may be spread over 10 annual payments with interest (5% on pulse 1; assumed 5% for the rest, UNVERIFIED); O&M 4% of consideration a year | p.153, p.183 |
| Accounting | amounts paid are deferred expenses amortised over 25 years (incl. two unexercised 5-year options); the unpaid balance is not shown | p.153 |
| Lines in service | more than ~27,600 at 19.8.2026 | gilat_h1_2026 p.5 |
| Regulated fibre BSA | ILS 58 a month up to 1 Gbps, fixed 2026-2031; unlimited for small ISPs | gilat_fy2025 p.40 (Minister's decision of 26.2.2026) |
| Paid to 30.6.2026 | 24,425 (13,752 in FY2025 + 10,673 in H1 2026) | gilat_q2_2026_full p.38 |
| Committed / unpaid / unpaid for lines in service | 248,020 / 223,595 / 106,262 | derived, UNVERIFIED (out §3) |
| ISP cash margin at today's lines (runway) | 12,124 a year (2 × (2,613 + 3,449)) | gilat_q2_2026_full p.46 |
| Private ISP net additions | 7,116 in H1 2026 | gilat_h1_2026 p.8 |
| Bezeq's own report (4.11.2025) | addendum consideration "over NIS 600 million" including maintenance, interest and linkage, "the majority … paid over the first years" | unofficial English translation (scuttlebutt.md [BZQ-IRU]); Hebrew original not read |

### Other facts cited in the record

| Input | Value | Source |
|---|---|---|
| Segments 2025 (USD k): government/defence; global (Africa); Israeli ISP | revenue 48,065; 19,655; 8,073; result 16,620; 4,106; 524 | gilat_fy2025 p.181 |
| Named customers 2025 (FS note) | government customer 19,300 (25.5%); Vodacom DRC 12,400 (16.4%) | gilat_fy2025 p.182; directors' report p.32 (19,278) and p.55 (12,392) |
| Vodacom DRC contract | renewed 5.2024 to 31.3.2027, about USD 45M over the term; about USD 1M a month in 2023-2025; "working to renew" | gilat_fy2025 p.55-56; gilat_h1_2026 p.15 |
| Government backlog 2027-2029 at the FY2025 report date | USD 2,195k | gilat_fy2025 p.32 |
| 2026 government orders (12.2025-1.2026) | about ILS 110M including VAT "for the coming year" | gilat_fy2025 p.101; gilat_h1_2026 p.14-15 |
| Licences expiring 31.12.2026 | unified satellite, Iridium, trade, OneWeb | gilat_fy2025 p.69-72 |
| Holding of 5% or more | needs the Minister's prior consent and an "Israeli" holder | gilat_fy2025 p.72-74 |
| Warning-sign working-capital disclosures | 31.12.2023 deficit USD 357k (gilat_fy2023 p.91); 31.12.2024 USD 9,484k (gilat_fy2024 p.88); 31.12.2025 USD 1,874k, solo 3,942k (gilat_fy2025 p.99); ended at 30.6.2026 (working capital 69,035, gilat_h1_2026 p.14) | page images at the gate |
| Shelf prospectus | open since April 2026 | gilat_h1_2026 p.49 |
| CEO pay terms | 70% of the 2025 bonus on Adjusted EBITDA, 30% on gross profit; free cash flow dropped (30% in 2023-24); cap raised from 6 to 8 salaries on 4.12.2025 | gilat_fy2025 p.206-207; gilat_fy2024 p.193-194 |
| "FCF excluding prepaid expenses" add-back 2025 | USD 2,929k | gilat_fy2025 p.93 |
| "Not leveraged … zero levels" | — | gilat_fy2025 p.90 (risk factors, section 27: p.82-87) |
| No controller; related-party dealings | none since 17.2.2021; pay only | gilat_fy2025 p.214-215, p.176 |
| 2021 dispersal of the control block | 41% sold in 2-3% lots for about ILS 26M at a market value of about ILS 68M, "after previous attempts to sell the control core did not succeed" | Calcalist L-3894358 (17.2.2021, saved copy re-read) |
| CEO interview | wartime turnover "about double" the normal period; defence about 50% of turnover in wartime, about 30% in routine | Bizportal 20014148 (4.3.2025, saved copy re-read) |
| Vodacom Group and Starlink | pan-African backhaul and resale partnership, 12.11.2025 | Space in Africa; Connecting Africa; Total Telecom |
| Analyst segment normalisation (reference only) | 15,099 after lease interest | business.md §12 (business_calcs_output §11) |

### Assumptions (stated, not facts; `valuation.py` §4-§5)

| Assumption | Value | Basis |
|---|---|---|
| Scenario probabilities | worst 15%, conservative 30%, base 45%, optimistic 10% | model judgements, uncalibrated (B-O3) |
| Expected IRU cost in the base | 25% of "half the unfilled lines unused" (52,268 after tax) = 13,067 | B-O6; private net additions ran about 3,500 a quarter against tranches of 3,000 |
| Conservative case | Vodacom not renewed: 2025 contribution at the 2025 global-segment margin, 8,173 | contract margin UNVERIFIED |
| Worst case | pre-war demand, Vodacom lost, ISP stalls; Dempster value pro forma less every unfilled line at its PV (135,760, pre-tax) | B-O4, A-O3 |
| One-offs | the whole Q4 2025 gross-margin excess as the supplier credit (upper bound); the H1 2026 equipment rise at the 2025 equipment margin | A-O10 |
| Maintenance capex | floored at depreciation incl. ROU and the IRU (46,361): leases stay an operating cost | framework d1 |
| Growth | 0% in the base DCF; ROIIC = r (no moat) | framework d4 |
| Runway | Series D does not convert in the worst case and amortises 25% a year from 1.4.2028; ISP at today's lines; core cash at the FY2021-22 level, nil, or the FY2023-25 level | A-O3 |
| Data additions | cycle_window_short, derived_tier2_field, microcap_field_unavailable (+5 each, capped at +10) | charter tier table |

## Differences of basis between workstream files (the record uses `output.txt`)

- **TTM operating profit.** 39,534 in `output.txt` (consolidated statements, FY2025 32,980) against 39,535 in
  `financials.json` (directors' report, 32,981). Mega shows 39,534. TTM pre-tax: 31,315 against 31,316.
- **Shares at 30.6.2026.** 118,063,162 in `valuation.py` (market.md, with about 652,000 option exercises) against
  117,411,162 in `financials.json`, whose upper bound is 118,063,313.
- **Customer letters.** "Customer A" in business.md, gate.md and checklist.md is the unnamed Israeli government
  customer (25.4% of 2025 revenue, gilat_fy2025 p.32). The financial-statement note that `financials.json` follows
  (p.182) calls it "C" (19,300, 25.5%) and calls Vodacom "A" (12,400, 16.4%).
- **June buyback price.** 258.97 agorot before fees (market.md) and 260.36 including fees (governance_risk.md;
  out §7 uses 2.603). Both are in the filing.
- **Fully diluted count.** market.md: about 150.27M (net options about 3.52M, December and November 2025 packages
  only). out §0: 152,177,660 (net options 5,422,102, including the older 3,428,500 at an upper bound).
- **Liquidity.** valuation_notes.md (pre-gate) used the TASE series to 29.10.2026 (median 1,303,000; p25 960,250;
  cap 3,841,000). The record uses the 60 sessions to 3.11.2026 (1,325,803; 1,001,604; 4,006,416).
- **Ayalon funds.** 6.22% on the 3.11.2026 count (scuttlebutt.md §5), 6.13% on the 30.9.2026 count (market.md) and
  6.46% in Bizportal's fund snapshot of 31.8.2026: dates and bases differ.
- **The CEO's 2023 placement.** 6,148,754 shares in note 15d and in `financials.json`; 6,134,442 in
  governance_risk.md, the only count that reconciles the share bridge (gilat_fy2023 p.151).
- **Mega's share count.** A `financials.json` caveat says Mega "probably uses the stale count" (2.110 ILS on
  93,937,313 shares). market.md and out §0 show Mega's figure equals 164.6 agorot × 120,417,631 exactly; the caveat is
  superseded.
- **Pre-gate files.** valuation_notes.md (base 0.789, shadow line 0.316), the red-team reports (base 0.520; CPI
  stress 0.113) and governance_risk.md (+5 points of extra margin) carry pre-gate figures and recommendations. The
  record is `output.txt` and `gate.md`.

URLs (read on 3.11.2026 unless marked; Israel time):
- https://www.bizportal.co.il/capitalmarket/quote/generalview/1080597
- https://www.bizportal.co.il/capitalmarket/quote/transactions/1080597
- https://www.bizportal.co.il/capitalmarket/quote/profile/1080597
- https://www.bizportal.co.il/capitalmarket/quote/performance/1080597
- https://www.bizportal.co.il/capitalmarket/quote/stakeholders/1080597
- https://www.bizportal.co.il/capitalmarket/quote/dividends/1080597
- https://www.bizportal.co.il/capitalmarket/quote/analystadvice/1080597 (empty)
- https://www.bizportal.co.il/capitalmarket/quote/reports/1080597
- https://www.bizportal.co.il/capitalmarket/quote/news/1080597
- https://www.bizportal.co.il/ajax/biz_papers_helper.ashx?action=get_paper_yearly_graph&request_type=1&paper_id=1080597&period=6
- https://www.bizportal.co.il/ajax/biz_papers_helper.ashx?action=get_holding_flow_summary_data_json&paperId=1080597&period=y
- https://www.bizportal.co.il/ajax/biz_papers_helper.ashx?action=get_paper_news_page&paper_id=1080597&page_number=1 (pages 1-5)
- https://www.bizportal.co.il/bonds/quote/generalview/1218205
- https://www.bizportal.co.il/bonds/quote/bondsdata/1218205
- https://www.bizportal.co.il/bonds/quote/stakeholders/1218205
- https://www.bizportal.co.il/capitalmarket/news/article/20014148 (CEO interview, 4.3.2025)
- https://www.bizportal.co.il/capitalmarket/news/article/838877
- https://www.bizportal.co.il/capitalmarket/news/article/834978
- https://www.bizportal.co.il/capitalmarket/news/article/815902
- https://www.bizportal.co.il/capitalmarket/news/article/796082
- https://www.bizportal.co.il/capitalmarket/news/article/20013709
- https://www.bizportal.co.il/capitalmarket/news/article/20019103
- https://www.bizportal.co.il/capitalmarket/news/article/20025845
- https://www.bizportal.co.il/capitalmarket/news/article/20039673
- https://finance.themarker.com/stock/1080597
- https://finance.themarker.com/bond/1177823 (Series C, empty)
- https://www.globes.co.il/portal/instrument.aspx?instrumentid=949&mode=company
- https://www.globes.co.il/portal/instrument.aspx?instrumentid=949&mode=news
- https://www.globes.co.il/portal/instrument.aspx?instrumentid=554949&mode=company
- https://satcom-gilat.co.il/גרף-מניה/ (TASE daily series, as of 30.10.2026 17:34)
- https://satcom-gilat.co.il/דיווחים-מיידיים/
- https://satcom-gilat.co.il/מצגות/
- https://satcom-gilat.co.il/דוחות-כספיים/
- https://satcom-gilat.co.il/wp-content/uploads/2026/08/דוח-רבעון-2חצי-שנתי.pdf (gilat_q2_2026_full)
- https://satcom-gilat.co.il/wp-content/uploads/2026/08/מצגת-סיכום-תוצאות-הרבעון-השני-לשנת-2026-.pdf (presentation 20.8.2026)
- https://satcom-gilat.co.il/wp-content/uploads/2023/03/דוח-תקופתי-ושנתי-לשנת-2022-1-merged.pdf (gilat_fy2022)
- https://satcom-gilat.co.il/wp-content/uploads/2023/05/דוח-תקופתי-לשנת-2022.pdf (gilat_fy2022, re-issue of 18.5.2023)
- https://satcom-gilat.co.il/wp-content/uploads/2022/03/דוח-תקופתי-ושנתי-לשנת-2021-merged.pdf (gilat_fy2021)
- https://satcom-gilat.co.il/wp-content/uploads/2026/07/P1759320-00.pdf (order of 27.7.2026)
- https://satcom-gilat.co.il/wp-content/uploads/2026/08/P1761175-00.pdf (framework of 4.8.2026)
- https://satcom-gilat.co.il/wp-content/uploads/2025/10/זימון-אסיפה-כללית-שנתית-ומיוחדת-ל-4.12.25-merged.pdf (summons only; results not hosted)
- https://satcom-gilat.co.il/wp-content/uploads/2024/03/אסיפה-שזומנה-ליום-13.3.24-נדחית-ליום-14.3.24-merged.pdf (summons only)
- https://www.sponser.co.il/Article.aspx?ArticleId=123559 (7.10.2026)
- https://www.sponser.co.il/Article.aspx?ArticleId=122311 (12.6.2026)
- https://www.ice.co.il/finance/news/article/1132707 (7.10.2026)
- https://www.deeptase.co.il/he/company/1006
- https://www.deeptase.co.il/he/analysis/5148
- https://www.deeptase.co.il/he/analysis/4576
- https://he.wikipedia.org/wiki/גילת_טלקום
- https://www.calcalist.co.il/articles/0,7340,L-3894358,00.html (17.2.2021)
- https://www.calcalist.co.il/articles/0,7340,L-3888431,00.html
- https://www.calcalist.co.il/articles/0,7340,L-3777427,00.html
- https://finance.walla.co.il/item/3147514
- https://www.insurancejournal.com/news/international/2023/08/15/735355.htm
- https://www.calcalistech.com/ctechnews/article/bys4stohn
- https://www.calcalistech.com/ctechnews/article/rj2htx92h
- https://www.calcalistech.com/ctechnews/article/byzgiud1zg
- https://cdn.financialreports.eu/financialreports/media/filings/6676/2025/RNS/6676_rns_2025-11-04_e1aa6820-2af2-43ba-8ca3-38e73d48d81b.pdf (Bezeq, 4.11.2025, unofficial translation)
- https://en.globes.co.il/en/article-1001433549 (Partner's Bezeq IRU, 22.12.2022)
- https://en.globes.co.il/en/article-elon-musks-starlink-launches-israel-internet-services-1001518509
- https://www.ses.com/press-release/ses-delivers-solid-h1-2025-results-completes-intelsat-acquisition
- https://spaceinafrica.com/2025/11/12/vodacom-group-and-starlink-partners-to-transform-connectivity-across-africa/
- https://www.connectingafrica.com/partnerships/atf-2025-vodacom-starlink-partner-to-connect-africa
- https://www.connectingafrica.com/connectivity/starlink-live-in-drc
- https://totaltele.com/vodacom-taps-starlink-for-mobile-backhaul-across-africa/
- https://developingtelecoms.com/telecom-business/operator-news/18907-airtel-africa-vodacom-to-share-infrastructure-in-african-markets.html
- https://itweb.africa/article/nexttel-leverages-gilat-to-deploy-4g-in-cameroon/P3gQ2MGxjmrqnRD1
- https://www.camer.be/77331/12:1/cameroun-affaire-nexttel-baba-danpullo-de-retour-sur-la-table-des-negociations-cameroon.html
- https://ucc.co.ug/wp-content/uploads/2025/02/LICENSED-TELECOM-OPERATORS-AS-AT-30TH-DECEMBER-2024.pdf
- https://data.gov.il/api/3/action/datastore_search?resource_id=f004176c-b85f-4542-8901-7b3176f9a054&q=גילת טלקום (Companies Registrar; also שידורית, גולדפון)
- https://data.gov.il/api/3/action/datastore_search?resource_id=28780ab5-3ef1-44c7-8377-da82c0aa6781&q=511784498
- https://data.gov.il/api/3/action/datastore_search?resource_id=65c8fced-c50c-400e-94fb-ef1a208c43e5&q=גילת טלקום (procurement exemptions)
- https://cdn.financialreports.eu/financialreports/media/filings/6813/2024/RNS/6813_rns_2024-07-11_b3e0303e-65be-41da-bc5e-a6403413d89a.pdf (TASE maintenance rules, 11.7.2024)
- https://stockanalysis.com/quote/tlv/SCC/statistics/ (and the same page for GLTL, BEZQ, PTNR, CEL; US and European peers on the equivalent paths)
- https://breakingdefense.com/2026/03/israel-approves-45b-defense-budget-as-iran-war-rages/
- https://www.drushim.co.il/jobs/search/גילת%20טלקום/
- https://www.ynet.co.il/capital/article/bygon24ree
- https://tradingeconomics.com/israel/government-bond-yield
- https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve&field_tdr_date_value=2026&page&_format=csv
- https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10
- Search summaries only (UNVERIFIED): https://www.satellitetoday.com/government-military/2013/11/11/gilat-satcom-and-ast-chosen-to-provide-mss-services-to-the-israeli-government/ ;
  https://www.gov.il/en/service/satellites-iridium-operators ;
  https://www.semafor.com/article/11/03/2025/elon-musks-starlink-in-talks-with-dr-congo-mobile-firms ;
  https://bankable.africa/en/digital/0611-1948-africell-and-vodacom-explore-starlink-partnership-in-dr-congo ;
  https://www.ynetnews.com/business/article/syvfp7ujzg ;
  https://english.alarabiya.net/News/middle-east/2026/04/12/iran-war-has-cost-israel-115-billion-in-budgetary-expenses-ministry-says ;
  https://simplywall.st/stocks/il/telecom/tase-gltl/gilat-telecom-global-shares/ownership ;
  https://www.globes.co.il/news/article.aspx?did=100221 ; https://www.funder.co.il/article/211179 (HTTP 403)
