# Gilat Telecom Global (TASE 1080597, GLTL): market data and events after 30.6.2026

This note was prepared on 3.11.2026, after the TASE close. Web pages were fetched between 17:38 and 18:15 Israel time (15:38–16:15 UTC).

Files in this folder:
- **Calculations.** Every derived number below comes from `market_calcs.py`; its output is in `market_calcs_output.txt`. References to "calc §n" point to sections of that output.
- **Price history.** The daily series is TASE data embedded in the company's own investor-relations page (https://satcom-gilat.co.il/גרף-מניה/, as of 30.10.2026 17:34). It runs from 31.10.2021 to 29.10.2026, 1,228 sessions, and is saved as `web/history_data.json`. Its fields include the close, the daily high and low, turnover in ILS, volume, and the TASE number of shares listed for trading on each day.
- **Snapshots.** Raw copies of every page used are in `web/`.

How the pages were obtained:
- Pages were fetched directly with plain curl through the session proxy, with default headers.
- Investing.com returned 403 and was not retried.
- Maya and Magna were not used, because they block scripted access. Wherever an item rests only on a Maya filing, it is marked UNVERIFIED.

## 0. Figures to use

| Item | Value | Source |
|---|---|---|
| Share price | **165.3 agorot**, close on **3.11.2026** (17:24). Base price 170.1, so −2.82% on the day. | Bizportal general view, "as of 03/11/2026"; TheMarker Finance, 03.11.2026 17:24 |
| Price in the Mega snapshot (14:03) | **164.6 agorot**, derived. Mega's ILS 198,207,420.626 ÷ 120,417,631 shares = 164.6000 exactly. | calc §1 |
| Shares outstanding (excluding dormant shares) | **120,417,631** | TASE "registered capital for trading" (הון רשום למסחר): Bizportal 3.11.2026, and the TASE series on 29.10.2026 |
| Dormant (treasury) shares | About 4,574,810: 2,300,000 bought in June 2026 plus 2,274,810 bought in October 2026 | gilat_h1_2026 p.37; Globes insider feed; calc §3 |
| Issued shares including dormant | About 124,992,441 | calc §3 |
| Market cap | **ILS 199.05M** at the close (USD 63.05M at 3.157). ILS 198.21M at the 14:03 Mega snapshot. | calc §1 |
| Series D convertible still outstanding | About 26,337,927 ILS par. It converts at 1 share per ILS 1 par until 1.4.2028, so about 26.34M shares, or +21.9%. | Bizportal bond data, 3.11.2026; gilat_h1_2026 p.24; calc §4 |
| Shares if Series D converts | 146,755,558, worth ILS 242.6M at 165.3. On this basis, take the Series D liability out of debt. | calc §4 |
| Listed options (net exercise, unvested) | About 3.52M net shares at 165.3, or 2.9% | gilat_fy2025 p.166; calc §5 |
| Israel 10-year yield | 4.16% (3.11.2026) | TradingEconomics |
| US 10-year yield | 4.91% (2.11.2026) | US Treasury daily par yield curve |
| Hurdle r | **10%** = max(10%, 4.16+3, 4.91+3) | calc §10 |

**Currency warning for the valuation:**
- **The statements are now in shekels.** From 1.1.2026 the company's functional currency and its presentation currency are both the shekel (gilat_h1_2026 p.2, p.36–37). The H1 2026 statements are in ILS thousands, with the comparative periods translated into ILS.
- **The older reports are in dollars.** The FY2023–FY2025 annual reports are in USD thousands.
- **Mega's TTM figures are also in shekels.** They are rebuilt exactly from gilat_h1_2026 p.6–7 as FY2025 − H1 2025 + H1 2026 (calc §10a): net income 32,985, gross profit 85,211, operating profit 39,535 (Mega shows 39,534), and operating cash flow 80,967. They therefore run to 30.6.2026.

**Data gap: the supplied Q2 file has no consolidated statements.**
- **What the supplied file contains.** The Q2 2026 PDF supplied as gilat_h1_2026 (52 pages) has only:
  - the directors' report;
  - the separate (solo) interim information, printed twice;
  - the auditor's consent;
  - the management declarations.
- **Where the full report is.** The full 64-page report, with the consolidated condensed statements, is posted on the company's site: https://satcom-gilat.co.il/wp-content/uploads/2026/08/דוח-רבעון-2חצי-שנתי.pdf. A copy is saved as `web/pdf/company_site_q2_2026_full.pdf`. This note cites it as "company Q2 PDF".

## 1. Price, share count and market cap

### 1.1 Price

- **Trading on 3.11.2026** (Bizportal general-view and transactions pages; TheMarker):

  | Field | Value |
  |---|---|
  | Close | 165.3 agorot |
  | Base | 170.1 |
  | Open | 170.1 |
  | High | 169.2 |
  | Low | 163.4 |
  | Average | 165.1 |
  | Volume | 1,046,631 shares |
  | Turnover | ILS 1,727,998 |
  | Trades | 592 |

- **Recent closes**, from the TASE series to 29.10, then Bizportal:

  | Date | Close |
  |---|---|
  | 23.10 | 200.3 |
  | 26.10 | 186.2 |
  | 27.10 | No trading: Knesset election day, TASE closed |
  | 28.10 | 179.4 |
  | 29.10 | 179.9 |
  | 30.10 | 174.5 |
  | 2.11 | 170.1 |
  | 3.11 | 165.3 |

  - The 30.10 close comes from a Bizportal page snapshot dated 30/10/2026 (174.5, −3%).
  - It is consistent with Bizportal's "last trading day −2.52%" as of 2.11, since 170.1/174.5 = −2.52%.
- **Fall since 23.10:** −17.5% (calc §8).
- **No company news explains the drop.** None was found. It coincides with the 27.10.2026 election and a broad market sell-off; Globes ran the headline "the stock exchange in panic" on 28.10.2026.

### 1.2 Shares outstanding: reconciliation with the filings

TASE's "registered capital for trading" leaves out dormant (bought-back) shares:
- **June buyback.** The listed count fell by exactly 2,300,000 between 17.6 and 24.6.2026.
- **October buyback.** It fell by 2,274,810, net of conversions, between 9.10 and 23.10.2026 (TASE series).
- **Insider-report percentages use the same base.** The CEO's 9,547,586 shares are 7.81% of the 30.9 count of 122,183,411, and the Ayalon funds' 7,494,833 shares are 6.13% of it (calc §6).

| Step | Shares | Source |
|---|---|---|
| Issued at 31.12.2025 | 93,937,313 | gilat_fy2025 p.165 (TASE count on 15.12.2025 is the same) |
| H1 2026: option exercises, net | +about 652,000 (ILS 652K of share capital at ILS 1 par) | company Q2 PDF p.33, consolidated statement of changes in equity |
| H1 2026: Series C conversions (13,151,410 par ÷ 1.35) | +9,741,785 | gilat_h1_2026 p.37 |
| H1 2026: Series D conversions | +16,032,064 | gilat_h1_2026 p.37 |
| June buyback, now dormant (12–30.6, weighted average 258.97 agorot; ILS 5,988K with fees) | −2,300,000 | gilat_h1_2026 p.37 |
| **Outstanding at 30.6.2026, derived** | **118,063,162** (TASE 1.7.2026: 118,079,459; gap 16,297, from rounding the option figure to thousands) | calc §2 |
| Conversions 1.7–19.8: Series C 1,240,026 par gives 918,537 shares; Series D gives 705,275 | +1,623,812 (TASE change: +1,623,813) | gilat_h1_2026 p.37; calc §2 |
| TASE count, 19.8.2026 (Q2 report approval date) | 119,703,272 | TASE series |
| Conversions 19.8–30.9: Series D about 2.80M, final Series C about 0.19M | +2,480,139 | TASE series; calc §4 |
| TASE count, 30.9.2026 | 122,183,411 | TASE series |
| October buyback, dormant | −2,274,810 | Globes insider feed; TASE series |
| October conversions | +509,030 | calc §3 |
| **TASE count, 29.10.2026 and 3.11.2026** | **120,417,631** | TASE series; Bizportal 3.11.2026 |

Two notes on the reconciliation:
- **A figure the Q2 note leaves out.** The Q2 events note (gilat_h1_2026 p.37) does not mention the roughly 0.65M shares from option exercises. Using that note alone undercounts by about 0.67M shares.
- **The separate statement agrees.** In the separate statement (gilat_h1_2026 p.31), share capital rose from ILS 87,063K to ILS 113,489K. That is +26,426K, which equals 652 + 9,742 + 16,032.

### 1.3 Reconciliation with Mega's ILS 198.2M market cap

- **Mega's market cap reconciles exactly.** 164.6 agorot × 120,417,631 = ILS 198,207,420.6, which is Mega's figure to the shekel. Mega used the TASE listed count and the 14:03 price.
- **Mega's ratios use the previous close.** Its P/E of 6.21 and P/B of 1.55 are based on the 2.11 close of 170.1. That close gives a market cap of ILS 204.83M, the same as Bizportal's "company value" of ILS 204,830.4K, and the same as the "about ILS 205M (2.11.2026)" on Hebrew Wikipedia.
- **Ratios at today's prices** (calc §1):

  | Basis | P/E (TTM net income to 30.6.2026) | P/B (equity at 30.6.2026) |
  |---|---|---|
  | 14:03 market cap | 6.01 | 1.50 |
  | Close | 6.03 | 1.50 |

### 1.4 Dilution still outstanding

**Series D (TASE 1218205; unsecured, negative pledge):**
- **Size.**
  - About 26,337,927 ILS par was outstanding on 3.11.2026.
  - Source: Bizportal's coupon schedule shows ILS 724,293 due on 1.4.2027, which is 2.75% of par.
  - Cross-check: market value ILS 45,617K ÷ price 173.2 = 26.34M.
  - Of the 45,872,000 issued, 19,534,073 par (42.6%) has already converted (calc §4).
- **Conversion terms** (gilat_h1_2026 p.24):
  - 1 share per ILS 1 par until 1.4.2028;
  - then 1 share per ILS 1.40 par until 21.3.2031.
- **Coupon and repayment** (gilat_h1_2026 p.24):
  - 5.5% coupon, paid 1.4 and 1.10;
  - principal repaid in four 25% instalments on 1.4.2028–2031.
- **Trading.** The bond closed at 173.2 on 3.11.2026 (−1.76%), a 4.8% premium to conversion parity (calc §4). Its 52-week range is 112.56–279.53 and it is up 48.05% year to date (Bizportal).
- **Distribution limits** (gilat_h1_2026 p.25; Bizportal bond page):
  - equity of at least ILS 35M after any distribution;
  - net debt/EBITDA of at most 4.5;
  - liquidity covering 18 months of debt service;
  - no "warning signs".
- **Covenants:**
  - net financial debt/balance sheet of at most 60%;
  - net debt/EBITDA of at most 5;
  - equity/balance sheet of at least 12%.

**Series C:**
- **Final payment.** The last 34% of principal was due on 1.9.2026 (gilat_h1_2026 p.3, p.22).
- **Outstanding before the payment.**
  - On 19.8.2026: 6,465,845 par, of which 5,480,878 was held by a subsidiary.
  - The public part was 984,967 par, at most 729,605 shares.
- **Status now.**
  - The bond is no longer quoted: the TheMarker and Bizportal pages for 1177823 were empty on 3.11.2026.
  - The TASE share counts imply that about 192K shares were converted after 19.8, with the rest redeemed in cash (calc §4).
  - The payment report itself was not seen (Maya), so this is UNVERIFIED.

**Options** (gilat_fy2025 p.166). All of these vest 25% a year over four years and are exercised net.

| Holder | Grant | Number | Exercise price |
|---|---|---|---|
| CEO | December 2025 | 2,000,000 | 110.15 agorot |
| CEO | December 2025 | 2,000,000 | 92.7 agorot |
| 32 employees and officers | November 2025 | 750,000 | 110.15 agorot |
| 32 employees and officers | November 2025 | 3,915,000 | 92.7 agorot |

- Net dilution at 165.3 is about 3.52M shares (calc §5).
- Older option grants may also still be outstanding. These are not counted here.

**Fully diluted count** (listed shares + Series D + the options above): about **150.27M shares**.

## 2. Price range and liquidity

### 2.1 Range (calc §8)

| Window to 3.11.2026 | Closing high | Closing low | Intraday high and low |
|---|---|---|---|
| 1 year | 282.8 (12.6.2026) | 88.0 (11.11.2025) | 294.2 / 87.5 |
| 2 years | 282.8 (12.6.2026) | 63.4 (17.11.2024) | 294.2 / 61.6 |
| 3 years | 282.8 (12.6.2026) | 35.4 (8.11.2023) | 294.2 / 35.0 |

- **Bizportal agrees.** Its 52-week range on 3.11.2026 is 88 to 282.8.
- **Distance from the peak.** The close is 41.5% below the 12.6.2026 closing high, when the market cap was ILS 339.0M.
- **The June buyback began at the peak.** It started on 12.6.2026, the day of the high, and was executed at an average of 258.97. The close is 36.2% below that average.

**Year-end closes and market caps**, using the TASE share count:

| Year end | Close | Market cap |
|---|---|---|
| 2021 | 53.8 | ILS 31.4M |
| 2022 | 27.0 | ILS 15.8M |
| 2023 | 45.5 | ILS 31.2M |
| 2024 | 80.7 | ILS 69.5M |
| 2025 | 121.8 | ILS 114.4M |
| 30.6.2026 | 247.5 | ILS 292.0M |

**Change to 3.11.2026:**

| From | Change |
|---|---|
| 31.12.2025 | +35.7% |
| 1 year | +93.8% |
| 2 years | +137.8% |
| 3 years | +317.4% |
| 30.6.2026 | −33.2% |
| 19.8.2026 | −26.5% |
| 30.9.2026 | −20.1% |

**Risk statistics** (Bizportal performance page, as of 2.11.2026):

| Window | Standard deviation | Beta |
|---|---|---|
| 12 months | 42.2% | 0.70 |
| 36 months | 51.2% | 0.79 |

**Short interest:** 1.18% of public holdings on 23.10.2026, equal to 1.6 days to cover (deeptase.co.il).

### 2.2 Liquidity: daily turnover in ILS (calc §9, TASE series to 29.10.2026)

| Window | Mean | Median | 25th percentile | Mean as % of market cap per day |
|---|---|---|---|---|
| 1 month | 2.35M | 1.84M | 1.22M | 0.97% |
| 3 months | 1.74M | 1.30M | 0.96M | 0.67% |
| 6 months | 2.22M | 1.48M | 1.08M | 0.82% |
| 12 months | 1.78M | 1.23M | 0.64M | 0.85% |
| Calendar 2025 | 0.36M | 0.18M | 0.09M | 0.45% |

- **Cross-check.** Bizportal on 3.11.2026 gives a 90-day average of ILS 1,773,721. Its performance page gives 30-day, 180-day and 365-day averages of ILS 2,311,066, 2,228,291 and 1,789,519.
- **Typical day.** A typical day now trades about **ILS 1.2–1.8M**, with no zero-turnover days in the last 12 months.
- **Building a position.** At 20% of the 12-month median:
  - ILS 1M takes about 4 sessions;
  - ILS 2M takes about 8;
  - ILS 5M takes about 20.
- **This liquidity is new.** In 2025 the median day traded only ILS 0.18M.
- **Index membership** (Bizportal):

  | Index | Weight |
  |---|---|
  | TA Telecom and IT | 2.46% |
  | TA Growth | 1.82% |
  | TA All-Share | 0.27% |

## 3. Announcements and news after 30.6.2026 (chronological)

| Date | Event | Source |
|---|---|---|
| 30.6.2026 | Ayalon mutual funds report a reduction of 1,978,591 shares, leaving 7.4%. | Globes insider feed |
| 1.7–19.8.2026 | Conversions: Series C 1,240,026 par into 918,537 shares; Series D 705,275 par into 705,275 shares. | gilat_h1_2026 p.37; company Q2 PDF p.49 (note 8) |
| 27.7.2026 | **Order increased by about ILS 4.25M (excluding VAT)** for satellite services to an Israeli customer, for 12 months from August. It adds to the ILS 14.3M 12-month contract from January 2026; the cumulative total is about ILS 18.55M. Reference 2026-01-070671. | Company PDF P1759320-00 (satcom-gilat.co.il, 27.7.2026); Globes Maya list; gilat_h1_2026 p.15; Q2 presentation 20.8.2026 |
| 30.7.2026 | Notice that the H1 statements will be published on 20.8.2026, with a conference call. | Company immediate-reports page |
| 4.8.2026 | **Framework orders from an Israeli customer reached about ILS 4.7M (excluding VAT)** for services through the end of 2026. The ILS 3.5M framework for 2025 (22.6.2025) was used in full. The company expects all orders to be used. | Company PDF P1761175-00 (4.8.2026); Globes Maya list |
| 10.8.2026 | Notice of an investor call on 20.8.2026 at 12:00. | Company immediate-reports page |
| 19–20.8.2026 | **Q2/H1 2026 report.** Signed on 19.8 and published on 20.8 at 08:55; a correction ("clerical error") followed at 09:38 and a results presentation at 12:16. See the bullets below the table for the contents. | Globes Maya list; gilat_h1_2026 p.3, p.6, p.26; Bizportal 20.8.2026; company presentation |
| 21.8–30.9.2026 | Conversions added 2,480,139 listed shares, mostly Series D. | TASE series; calc §4 |
| 1.9.2026 | Series C final redemption (34% of principal) under the bond terms. The bond has since been delisted. Payment report not seen: UNVERIFIED. | gilat_h1_2026 p.22 |
| 1.10.2026 | Series D semi-annual coupon of 2.75% due under the terms. Not seen: UNVERIFIED. | gilat_h1_2026 p.24 |
| 1.10.2026 | **CEO Itzik Ben Eliezer bought 28,893 shares at 207 agorot** (about ILS 60K), bringing his holding to 9,547,586 shares (7.81%). | Globes insider feed; Bizportal interested parties |
| 5.10.2026 | **Meitav mutual funds sold 1,891,278 shares at 196 agorot** (about ILS 3.71M), leaving 4.69%. | Globes insider feed |
| 7.10.2026 | **Board approved a buyback of up to ILS 7M.** Management wrote that "the share price does not fully reflect the improvement in performance, the company's financial strength and its growth potential". The program period and other terms were not seen (Maya report 1774251, linked from the company site). | Sponser 7.10.2026 08:03; ice.co.il 7.10.2026 21:08; company immediate-reports page |
| 7.10.2026 | Ayalon mutual funds reported −1,239,881 shares at price 0, which looks like an off-market move, leaving 6.13% (7,494,833 shares). | Globes; Bizportal |
| 7–21.10.2026 | **The company bought 2,274,810 shares at 198–207 agorot**, about ILS 4.62M at an average of about 203.1. That uses 66% of the ILS 7M cap and leaves about ILS 2.38M if the program is still open. No purchases were seen after 21.10. The close is 18.6% below the October average price. | Globes insider feed; TASE series; calc §3, §7 |
| 23.10–3.11.2026 | The share fell from 200.3 to 165.3 (−17.5%) around the 27.10 election. No company announcement was found. | §1.1 |

The 20.8.2026 Q2/H1 report included:
- **Profit.** Net profit of ILS 8.42M for Q2 and ILS 15.77M for H1.
- **Equity and net financial assets.** Equity of ILS 132.4M; net financial assets of about ILS 66M.
- **Backlog.** About ILS 158M to 2029.

The 20.8.2026 presentation set out the following strategy:
- organic growth in internet and cloud;
- "inorganic growth – examining potential acquisitions";
- investment alongside buybacks.

**Searched for and not found** (as of 3.11.2026):
- **Q3 2026 results.** Not yet published.
  - Bizportal's latest quarter is Q2/2026, and Mega's TTM runs to 30.6.2026.
  - Last year's Q3 came out on 23.11.2025 (company presentations page).
  - Expect the Q3 2026 report around late November 2026.
- **Dividends.** None since 2010; the last were 31.45 agorot in March 2010 and 126.2 agorot in December 2009 (Bizportal dividends page).
- **Share issues for cash.** None since the July 2025 placement of 7,710,000 shares at 88 agorot (gilat_fy2025 p.165). An April 2026 shelf prospectus is open (gilat_h1_2026 p.49), so equity can be issued quickly.
- **Large contracts after 4.8.2026.** None found by searching Bizportal, Globes, Sponser and the company site.
- **Changes in management, the board or control.** None found.
  - The Q2 report was signed by Chairman Ami Barlev, CEO Itzik Ben Eliezer and CFO Orit Gal (gilat_h1_2026 p.26, p.31).
  - Bizportal's list of officers on 3.11.2026 is the same.
  - The company has no controlling holder (see governance_risk.md).
- **Controlling-holder sales or purchases.** Not applicable, because there is no controlling holder. The trades by the CEO and the funds are listed in the table above.
- **Lawsuits or class actions.** None found by web search. This is UNVERIFIED because Maya was not accessible.
- **Guidance.** There is no numeric guidance.
  - Long-term internet ARPU target of ILS 90 (gilat_h1_2026 p.8).
  - Medium-term ARPU target of ILS 80, reached in Q2.

## 4. Analyst and sponsored coverage

- **No formal coverage was found.** There is no broker or sponsored research, rating or price target.
  - Bizportal's "analyst recommendations" tab for the share was empty on 3.11.2026.
  - A search-engine snippet of Simply Wall St says 0 analysts cover the stock; the page could not be opened.
  - The Series D bonds are unrated: Maalot and Midroog both show 0 on Bizportal.
- **Independent commentary from deeptase.co.il.** "Tel Aviv in depth" has published six notes on the company (26.3.2026 ×4, 31.5.2026, 20.8.2026). They are not recommendations and give no price target. Their main points:
  - Profit is carried by the commercial and government satellite segment.
  - The roughly ILS 110M 2026 order headline is concentrated: about two-thirds is a chain of increases from one Israeli customer, and part of it sits in non-binding frameworks.
  - The Bezeq IRU adds a material fixed-cost layer, and is a moat only if line utilisation stays high.
  - Capital flexibility is limited by heavy satellite leases.
  - (20.8.2026) Internet ARPU reached ILS 80.19 and the ISP segment's profit rose to ILS 1.88M.
- **Press tone.**
  - Sponser headlined the October program "a modest ILS 7M buyback".
  - Bizportal on 20.8.2026 noted that ARPU was eroded against the same quarter a year earlier.

## 5. Yields and hurdle rate

| Yield | Value | Source |
|---|---|---|
| Israel 10-year | **4.16%** on 3.11.2026 ("held steady"; +0.23 points over the year) | https://tradingeconomics.com/israel/government-bond-yield, fetched 3.11.2026 |
| Israel 10-year, second source | 4.160% close on 3.11.2026 | Search snippet of Investing.com's table; the page itself returned 403 |
| US 10-year | **4.91%** on 2.11.2026; 4.94% on 30.10.2026 | US Treasury daily par yield curve CSV |
| US 10-year, FRED | 4.94% on 30.10.2026; mid-October high of 5.21% on 13.10.2026 | FRED DGS10 |

- No 10-year yield is above 7%, so **r = 10%** (calc §10).
- The Bank of Israel series on edge.boi.org.il was not used. The figures above are market quotes.

## 6. Open items and UNVERIFIED

1. **October buyback.** The program period, the exact dormant count of about 4,574,810, and whether buying continues are all taken from insider-trade feeds and TASE share-count changes. They need checking against the company's buyback and capital-status reports on Maya. It is also possible that +200,000 entries on 20.10 and 28.10 were corrections rather than conversions. If so, there are about 0.2M fewer dormant shares, but the outstanding count of 120,417,631 is unchanged.
2. **Series C.** The final redemption on 1.9.2026, the split between cash and conversion, and the Series D coupon on 1.10.2026 were not seen in filings.
3. **Options.** Older option grants may still be outstanding beyond the December 2025 and November 2025 packages; check the H1 2026 notes in the company Q2 PDF.
4. **Lawsuits and Reg. 22 / Reg. 21 items after 30.6.2026.** Web search found nothing, but Maya was not checked.

## Sources (all accessed 3.11.2026)

- Bizportal, share:
  - https://www.bizportal.co.il/capitalmarket/quote/generalview/1080597 — price, base, range, turnover, 90-day average, registered capital, market cap
  - https://www.bizportal.co.il/capitalmarket/quote/transactions/1080597 and https://www.bizportal.co.il/capitalmarket/quote/profile/1080597
  - https://www.bizportal.co.il/capitalmarket/quote/performance/1080597 — returns, volatility, beta, average turnover
  - https://www.bizportal.co.il/capitalmarket/quote/stakeholders/1080597 — interested parties, mutual funds
  - https://www.bizportal.co.il/capitalmarket/quote/dividends/1080597
  - https://www.bizportal.co.il/capitalmarket/quote/analystadvice/1080597 — empty
  - https://www.bizportal.co.il/capitalmarket/quote/reports/1080597 — latest quarter Q2/2026
  - https://www.bizportal.co.il/capitalmarket/quote/news/1080597 — 20.8.2026 Q2 article
- Bizportal, Series D:
  - https://www.bizportal.co.il/bonds/quote/generalview/1218205
  - https://www.bizportal.co.il/bonds/quote/bondsdata/1218205 — price, market value, coupon schedule, covenants
- TheMarker Finance:
  - https://finance.themarker.com/stock/1080597 — close 165.30, 03.11.2026 17:24, market cap 199.05
  - https://finance.themarker.com/bond/1177823 — Series C, empty
- Globes:
  - https://www.globes.co.il/portal/instrument.aspx?instrumentid=949&mode=company — insider and company trades, Maya headlines
  - https://www.globes.co.il/portal/instrument.aspx?instrumentid=949&mode=news
  - https://www.globes.co.il/portal/instrument.aspx?instrumentid=554949&mode=company
- Company site:
  - https://satcom-gilat.co.il/גרף-מניה/ — TASE daily history, as of 30.10.2026 17:34
  - https://satcom-gilat.co.il/דיווחים-מיידיים/ — immediate reports
  - https://satcom-gilat.co.il/מצגות/ — presentations
  - https://satcom-gilat.co.il/דוחות-כספיים/ — full Q2 2026 report
  - https://satcom-gilat.co.il/wp-content/uploads/2026/07/P1759320-00.pdf
  - https://satcom-gilat.co.il/wp-content/uploads/2026/08/P1761175-00.pdf
  - https://satcom-gilat.co.il/wp-content/uploads/2026/08/מצגת-סיכום-תוצאות-הרבעון-השני-לשנת-2026-.pdf
- News:
  - https://www.sponser.co.il/Article.aspx?ArticleId=123559 — 7.10.2026
  - https://www.sponser.co.il/Article.aspx?ArticleId=122311 — 12.6.2026
  - https://www.ice.co.il/finance/news/article/1132707 — 7.10.2026
- Independent commentary:
  - https://www.deeptase.co.il/he/company/1006
  - https://www.deeptase.co.il/he/analysis/5148
  - https://www.deeptase.co.il/he/analysis/4576
- Hebrew Wikipedia: https://he.wikipedia.org/wiki/גילת_טלקום — market cap ILS 205M on 2.11.2026
- Yields:
  - https://tradingeconomics.com/israel/government-bond-yield
  - https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve&field_tdr_date_value=2026&page&_format=csv
  - https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10
- Documents: gilat_fy2025 (p.165–166); gilat_h1_2026 (p.2–3, 6–10, 15, 22–26, 31, 36–37, 49).
