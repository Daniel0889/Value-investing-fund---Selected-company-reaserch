# Paymeant Financial Technologies (TASE 1180876): market data and events after 30.6.2026

Researched 3.11.2026, pages read between 17:27 and 17:50 Israel time (UTC+2). Every derived number
below comes from `market_calc.py` (output in `market_calc_output.txt`, cited as "calc §n"). Source keys
such as [BZ-GV] are listed with full URLs and read times in the Sources section at the end.

**Status.** The price, share count, holder data and price history are confirmed by two or more
independent sites. The Maya filings were not opened, because Maya and www.tase.co.il block scripted
access (tase.co.il returned HTTP 403 from a bot check). Events that rest only on a Maya headline (as
Globes shows it) are marked **headline only**. Their content is UNVERIFIED.

## 0. Settled figures (use these)

| Item | Value | Source |
|---|---|---|
| Price used for the study | **318.0 agorot** (3.11.2026, intraday, the Mega snapshot) | [TM] 15:01: 318.00, +1.99%, market cap 125.06M; [SA] 318.00 at 3:01 PM; equals Mega market cap ÷ shares to the agora (calc §1) |
| Official close 3.11.2026 | 317.3 agorot (+1.76% on the 311.8 base) | [TM] 17:24 (phase "pre-opening", so trading had ended); [BZ-GV] |
| Shares outstanding | **39,330,034** | [BZ-GV] "הון רשום למסחר" (capital registered for trading), 3.11.2026; [SA] "Shares Out 39.33M" |
| Market cap | **125,069,508 ILS** at 318.0. This is Mega's figure to the shekel. At the 317.3 close it is 124,794,198 ILS (−0.22%) | calc §1 |
| Market cap in USD | about $39.6M at 3.157 ILS/USD | calc §1 |
| P/E (TTM net income 18,466k) / P/B (equity 86,912k) | 6.77x / 1.44x at 318.0. Mega's 6.64 / 1.41 are on the 2.11.2026 close of 311.8 | calc §2 |
| Dividends paid in the last 12 months | 22.93 agorot per share, a 7.21% yield at 318.0 | [BZ-DIV]; calc §2 |
| Israel 10-year yield | 4.16% generic; 4.29% yield to maturity on ממשל שקלית 0537 | [TE]; [TM-0537] |
| Hurdle r | **10%**. Yield + 3 points = 7.2–7.3%, below 10% | calc §7 |

## 1. Price, share count and market cap: reconciliation

- **Shares in the filings.** The company had 39,245,034 shares at 31.12.2025, and the same count at
  the FY2025 report date of 23.2.2026 (paymeant_fy2025 p.108 note 17a; p.123 Reg. 24A; both checked
  on the PDF page). Registered capital is 100,000,000 shares of 0.0001 ILS par. The Q2 2026 report
  gives no share count. Its statement of changes in equity shows an "exercise of options into
  shares" in H1 2026 that brought in only about 1k ILS (share premium +179k, share-based-payment
  reserve −178k; paymeant_h1_2026 p.25, checked on the PDF page). That pattern fits RSU-type
  conversions, which bring in no cash.
- **Shares now.** Bizportal shows 39,330,034 on 3.11.2026 [BZ-GV], which is +85,000 (+0.22%) since
  31.12.2025 (calc §1). The 175,000 RSUs convert at 12.5% a quarter from 1.4.2026
  (paymeant_fy2025 p.110), so they explain at most 43,750 shares by 30.9.2026. The rest presumably
  came from option exercises. The exact source of the +85,000 is UNVERIFIED and immaterial.
- **Mega.** 39,330,034 × 3.180 = 125,069,508.12 ILS, the Mega market cap exactly (calc §1), so Mega
  uses the same share count. With the filings' 39,245,034 shares, the implied price would be 318.69
  agorot. The difference is immaterial.
- **Mega's ratios.** P/E 6.64 and P/B 1.41 reproduce only on the base price of 311.8, the 2.11.2026
  close (calc §2). Mega's dividend yield of 3.68% could not be reproduced: dividends paid in the 12
  months to 3.11.2026 come to 22.93 agorot, or 7.21% (calc §2).
- **What Mega's margins mean.** Mega's TTM lines reconcile exactly to the filings (FY2025 − H1 2025
  + H1 2026, all from paymeant_h1_2026 p.24, checked on the PDF page; calc §2):
  - TTM revenue: 60,301k.
  - Mega's "gross profit" of 53,317k is total revenue after deducting financing expense (5,972k)
    and the credit-loss provision (1,012k).
  - Mega's "operating income" of 24,460k is **pre-tax profit after interest**.
  - So the "88% gross margin / 41% operating margin" are the margins of a **lender funded by bank
    debt**, not of a software company. The balance sheet shows 115,225k of short-term bank credit at
    30.6.2026 (paymeant_h1_2026 p.23).
- **Dilution items after 30.6.2026:**
  - **New options.** On 20.8.2026 the company granted 512,000 unlisted options at a strike of 5.74
    ILS (1.30% of shares). The share price used at grant was 5.61 ILS, and fair value was
    3.85–4.64 ILS per option (paymeant_h1_2026 p.6, p.33). At 318.0 the options are 44.6% out of
    the money (calc §5).
  - **Amitim warrants.** The first tranche of 255,000 warrants (strike 6.05 ILS) expired on
    24.7.2026 (paymeant_fy2025 p.17, p.108). The close that day was 580.3 agorot [SA-H], 4.1% below
    the strike (calc §4), so the tranche was out of the money at expiry. No exercise report was
    found, and the lapse is UNVERIFIED.

## 2. Price range and liquidity

Two price series were saved:

- `web/pmnt_daily_closes_bizportal.csv`: Bizportal daily closes from 3.11.2021 to 2.11.2026 (1,228
  closes) [BZ-HIST]. These are **adjusted for dividends**: older prices are scaled down for later
  dividends.
- `web/pmnt_ohlcv_stockanalysis.csv`: unadjusted daily open/high/low/close and volume from
  4.5.2026 to 2.11.2026, from StockAnalysis (S&P Global data) [SA-H].

| Window (adjusted closes) | High | Low | 318.0 vs high | 318.0 vs low |
|---|---|---|---|---|
| 52 weeks | 781.09 (23.2.2026, FY2025 results day, +4.55%) | 251.0 (28.10.2026) | −59.3% | +26.7% |
| 2 years | 781.09 (23.2.2026) | 228.29 (7.11.2024) | −59.3% | +39.3% |
| 3 years | 781.09 (23.2.2026) | 220.07 (25.9.2024) | −59.3% | +44.5% |
| Since 1.7.2026 | 605.93 (27.7.2026) | 251.0 (28.10.2026) | −47.5% | +26.7% |
| Since 1.10.2026 | 499.9 (1.10.2026) | 251.0 (28.10.2026) | −36.4% | +26.7% |

(calc §3)

- **Unadjusted 52-week range** (intraday, [SA]): 242.00–830.70 agorot. The 242.00 low was intraday
  on 28.10.2026 [SA-H].
- **Year-end adjusted closes:** 2023: 356.56; 2024: 303.93; 2025: 567.31 (calc §3).
- **Calendar-year returns** [BZ-PERF]:

  | Period | Return |
  |---|---|
  | 2022 | −52.96% |
  | 2023 | +37.18% |
  | 2024 | −14.76% |
  | 2025 | +86.66% |
  | 2026 to the 2.11 close | −45.04% |
  | 2026 to 318.0 | −43.95% (calc §3) |

- **Rolling returns** [BZ-PERF]:

  | Window | Return |
  |---|---|
  | 30 days | −37.63% |
  | 3 months | −46.41% |
  | 6 months | −57.16% |
  | 12 months | −31.96% |
  | 3 years | +6.82% |
  | 5 years | −16.5% |
  | 30.6.2026 to 318.0 (dividend-adjusted) | −45.7% (calc §3) |

- **Risk statistics** [BZ-PERF]:
  - Standard deviation: 48.68% (12 months), 40.97% (36 months).
  - Beta: 0.49 (12 months), 0.54 (36 months).
  - The company's own August 2026 option valuation assumed 127.54% volatility (paymeant_h1_2026 p.33).

**The October 2026 fall** (unadjusted close, change, volume in shares [SA-H]; closes match [BZ-HIST]):

| Date | Close | Change | Volume | Note |
|---|---|---|---|---|
| 19.10 | 471.8 | +0.02% | 19 | |
| 20.10 | 459.5 | −2.61% | 15,809 | |
| 21.10 | 403.9 | −12.10% | 225,098 | The Bank of Israel held its rate at 3.25% that day, as all 15 economists in a Reuters poll expected [BZ-BOI] |
| 22.10 | 390.4 | −3.34% | 96,274 | |
| 23.10 | 370.9 | −4.99% | 50,595 | |
| 26.10 | 308.2 | −16.90% | 226,865 | |
| 27.10 | (no trading) | | | Knesset election day [BZ-BOI]; 28.10 was "the first trading day after the elections" [BZ-28] |
| 28.10 | 251.0 | −18.56% | 1,742,446 | Intraday low 242.0. The volume was 4.43% of all shares. The company published a clarification at 16:05 (§3) |
| 29.10 | 315.9 | +25.86% | 815,181 | |
| 30.10 | 324.9 | +2.85% | 78,060 | |
| 2.11 | 311.8 | −4.03% | 123,374 | |
| 3.11 | 317.3 (close) | +1.76% | 111,691 shares in 46 trades; turnover 352,392 ILS | [BZ-TRANS], [BZ-GV] |

- From 19.10 to the 28.10 close the share fell 46.8%. From 19.10 to 318.0 it is down 32.6% (calc §3).
- Volume from 20.10 to 2.11.2026 was 3,373,702 shares. That is 8.58% of the company and about
  28.8% of the public float (calc §4).

**Liquidity:**

- **Bizportal averages** [BZ-PERF], [BZ-GV]:
  - Average daily turnover: 479,813 ILS (30 days), 188,480 ILS (90 days), 116,441 ILS (365 days).
  - Bizportal's 180-day figure (118,543) equals its own 180-day share-volume figure, so it looks
    like a site error and is not used.
- **S&P daily data** (turnover approximated as volume × close; calc §4):

  | Window | Trading days | Median daily turnover | Mean daily turnover | Median / mean daily volume |
  |---|---|---|---|---|
  | 4.5–19.10.2026 (before the fall) | 111 | ≈16.5k ILS | ≈39.9k ILS | 2,787 / 6,386 shares |
  | 1.7–19.10.2026 | 72 | ≈14.2k ILS | ≈28.9k ILS | |

  Some days traded almost nothing: 3 shares on 9.10.2026 and 19 shares on 19.10.2026.
- **Typical daily turnover in normal times is about 15–40k ILS (median to mean).** Bizportal's
  averages of 116–188k ILS are lifted by event days. A 1M ILS position is 0.80% of the company. At
  20% of daily turnover it would take 125–303 trading days on the S&P mean and median, or 27–43 days
  on Bizportal's averages (calc §4), unless it came as an off-market block.
- **Float and funds:**
  - Interested parties (8 holders) hold 70.22% and the public 29.78% [BZ-STAKE], so the public
    float is about 11.7M shares, worth about 37M ILS (calc §4).
  - Globes puts the public, including provident and mutual funds, at 34.92% [GL-INS].
  - 49 mutual funds hold 7.29%: Sigma 3.58%, Ayalim 2.33%, Migdal 1.04%, Ayalon 0.22% [BZ-STAKE].
    The date of this snapshot is not shown.

## 3. Announcements and news after 30.6.2026

| Date | Event | Source | Status / comment |
|---|---|---|---|
| 30.6.2026 | Erez Dahbani (דהבני ארז) moved 2,223,000 shares to "Baldi" (בלדי) at a recorded price of 0.00. Baldi now holds 5.65% | [GL-INS] (sell and buy rows); [BZ-STAKE] (Baldi 2,223,000, dated 30.6.2026) | Probably a transfer to a related holder rather than a sale. Nature UNVERIFIED |
| 12.7.2026 | The Capital Market Authority published circular 2026-10-4, rules for credit offered alongside a purchase (BNPL). Key rules: disclosure that the purchase and the credit are separate; a direct call to the borrower within 3 business days for credit above 7,500 ILS or for special populations; cancellation of the credit when goods or services are not supplied; no merchant without a written agreement and a check of the merchant's finances, with a possible merchant guarantee; the board is responsible. It takes effect 6 months after publication, i.e. early 2027 | paymeant_h1_2026 p.7; [GNY] (client update dated 29.7.2026) | The company says it is studying the circular (p.7). The risk that a merchant fails to deliver moves toward the lender |
| 24.7.2026 | First tranche of Amitim warrants expired: 255,000 at 6.05 ILS | paymeant_fy2025 p.17, p.108; close 580.3 [SA-H] | Out of the money at expiry, so probably lapsed. UNVERIFIED |
| 26.7.2026 | Credit Data Law (Amendment 6) published. Negative credit data is kept for 1 year instead of 3. In effect 6 months after publication | paymeant_h1_2026 p.7 | The company cannot yet assess the effect |
| 3.8.2026 | Gilor and Yochanan each moved 363,902 shares at a recorded price of 0.00 (afterwards 17.58% and 11.98%). Pini Yaakobi received 696,349 shares at 0.00 and now holds 2,378,149 (6.05%) | [GL-INS]; [BZ-STAKE]; Bizportal 180-day flows [BZ-FLOW] | Fits the release of the shares the founders held "for another shareholder", about 0.93 points each in paymeant_fy2025 p.118 (about 729,958 shares; calc §5). The founders' own economic stake did not change on this date. Founders' holdings rolled forward from the FY2025 report match Bizportal within 1,154 and 1,939 shares, which is percentage rounding (calc §5) |
| 20.8.2026 | Board approved the H1 2026 statements (p.23). It declared a dividend of about 2.0M ILS (5.09 agorot per share; record/ex-date 2.9.2026, paid 17.9.2026). It granted 512,000 options to five officers and employees (strike 5.74 ILS) | paymeant_h1_2026 p.6, p.33; [BZ-DIV] | Dividend confirmed in two sources. The private-placement report for the options was not opened |
| 21.8.2026, 11:28 | Q2 / H1 2026 report and investor presentation published | [GL-MAYA] | H1 net income 8,285k vs 8,007k (p.24). The share closed −2.82% that day [BZ-HIST] |
| 23.9.2026, 10:14 | Agreement to assign a loan portfolio of about 100M ILS | [GL-MAYA] | **Headline only.** Buyer, price and terms UNVERIFIED. The previous deal (about 80M ILS, February 2026) went to the company's wholly owned, unconsolidated, bank-funded SPC "Paymeant Series 2" (paymeant_h1_2026 p.6–7, p.32–33). The October 2025 deal (about 84M ILS) went to "Paymeant Series 1" (paymeant_fy2025 p.108) |
| 29.9.2026, 08:27 | That assignment was completed | [GL-MAYA] | **Headline only** |
| 21–28.10.2026 | The share fell 46.8% in six trading sessions on heavy volume (§2), with no company announcement | [SA-H]; [BZ-28] | The Bizportal market report of 28.10 found no report that explained the fall, and noted turnover far above average |
| 28.10.2026, 16:05 | Company clarification: "Further to the decline in the company's share price over the last week, the company wishes to clarify that, to the best of its knowledge, no unusual event has occurred at the company, and its business is being conducted as usual" | [GL-MAYA] headline; full sentence quoted by [SP] (28.10.2026 17:49) and paraphrased by [BZ-28] | Sponser: the share "completed a 49% crash in the last month"; market players asked whether a large holder decided to exit. The same day the TA-90 fell 4.4–4.5% after the election results, and the bank and insurance indices fell about 5% [BZ-28] |
| 29.10.2026 | Rebounded 25.9% "on thin turnover" and recovered the previous day's fall | [BZ-29] | |
| Last 90 days | No interested-party transactions | [BZ-FLOW] (3 months: empty) | **Insiders did not buy during the fall.** |

**Checked and not found:**

- **Q3 2026 results.** Not published by 3.11.2026: the latest Maya headline is the 28.10.2026
  clarification [GL-MAYA]. The Q3 2025 report came out on 17.11.2025 [GL-MAYA], and StockAnalysis
  shows an "earnings date" of 17.11.2026 [SA], probably an estimate. In 2025 the Q3 dividend was
  declared with the Q3 report (ex-date 26.11.2025, 7.65 agorot) [BZ-DIV].
- **Buybacks.** The board approved a buyback plan of up to 5M ILS for 18.11.2024–18.11.2026, and
  nothing had been bought by the FY2025 report (paymeant_fy2025 p.69, p.112). No buyback report was
  found after 30.6.2026, and the share count rose. As far as can be seen the plan was not used
  during the fall. It expires on 18.11.2026.
- **Share issues and conversions.** The only ones were the option/RSU shares (+85,000) and the
  option grant above. The company has no listed bonds or convertibles on Bizportal.
- **Management or control changes.** None found other than the holder transfers above. Control
  stays with Yaniv Gilor and Guy Yochanan under their shareholders' agreement, which lapses below 25%
  jointly (paymeant_fy2025 p.123). They now hold 11,617,267 shares, or 29.54% (Gilor 17.56%,
  Yochanan 11.97%), which leaves 4.54 points of headroom (calc §5).
- **Controlling holders' market sales after 30.6.2026.** None.
- **Lawsuits.** None found (web search only, not exhaustive, because Maya was not accessible).
- **Guidance.** The company gives no formal forecast, only origination run-rates:

  | Report | Stated annual run-rate | Basis |
  |---|---|---|
  | FY2025 report (paymeant_fy2025 p.7, p.59) | about 640M ILS | daily average for January 2026 |
  | Q2 2026 report (paymeant_h1_2026 p.5) | about 600M ILS | daily average for July 2026 |

  Actual originations were about 258M ILS in H1 2026 (124M in Q2). Doubled, that is 516M ILS:
  19.4% below the February claim and 3.6% below 2025's actual 535M (calc §6).

**Context from before the period (relevant to insider alignment):**

- On 13.3.2026 the founders sold 434,783 (Gilor) and 434,781 (Yochanan) shares at 690 agorot,
  6.00M ILS in total and 2.22% of the company [GL-INS]. Today's 318.0 is 53.9% below that price
  (calc §5). This came about three weeks after the 52-week high on the FY2025 results day.
- Bizportal's 365-day flows do not list these sales [BZ-FLOW], but Globes does [GL-INS]. Treat
  the sale as confirmed by one source only, until the Maya report is read.

## 4. Analyst and sponsored-research coverage

- **No sell-side or sponsored research found.**
  - Bizportal's analyst-recommendation tab for the share is empty [BZ-AN].
  - StockAnalysis shows "Analysts n/a" [SA].
  - Simply Wall St says no analysts cover the company [SWS, search snippet only].
  - Searches of Sponser, Bizportal and the general web found no sponsored-research report. TASE's
    sponsored-research pages could not be checked because tase.co.il returned 403.
- **Machine-generated output, not research:**
  - TipRanks "AI analyst" report dated 30.5.2026: Neutral, price target 608 agorot (search snippet
    only, UNVERIFIED [TR]).
  - Simply Wall St model "fair value" of about ₪3.72 against a price of ₪5.52; snapshot date unknown
    [SWS].
- **Only human analysis found:** an opinion column by Yaakov Akilov, owner of Y.M.L.A. Advisory,
  on Bizportal, 2.1.2025, before the period [BZ-AK].
  - Pessimistic case: net income of 10–12M ILS a year, and about 3.3 ILS is fair.
  - Base case: net income of 15–20M, target about 5 ILS (+50%).
  - Optimistic case: a takeover by a financial group or net income of 25–30M, target about 6.6 ILS.
  - He criticises the unused buyback ("not a single share bought ... looks completely unserious")
    and notes that Mor, once a large holder, had cut its position.
  - Disclosure: he may hold the securities and received no payment from the company.
  - Outcome so far: 2025 net income came in at 18.2M, inside his base case, and the share passed his
    targets in 2026 before falling back to 3.18.
- **News coverage after 30.6.2026:** only the market reports of 28–29.10 [BZ-28], [BZ-29] and the
  Sponser item [SP]. The Bizportal results article of 23.2.2026 [BZ-23F] is the latest company
  feature.

## 5. Rates

- **Israel 10-year government yield:**
  - 4.162% on 3.11.2026 (generic, over-the-counter quotes; +0.23 points over a year) [TE].
  - Cross-check: ממשל שקלית 0537 (security 1166180; fixed-rate shekel bond maturing 30.5.2037, 10.58
    years to maturity) yields 4.29% to maturity at a price of 77.20, modified duration 9.66
    [TM-0537].
  - Hurdle r = max(10%, 4.29% + 3) = **10%** (calc §7).
- **Bank of Israel:**
  - Policy rate 3.25%, held on 21.10.2026 after four cuts in 2026 from 4.25%. The next decision is
    on 23.11.2026 [BZ-BOI].
  - Prime is 4.75%: the policy rate + 1.5 points by Israeli convention, as stated in the search
    summary of the same coverage. It is not in the fetched article.
  - This matters because the company's bank lines are priced off prime (paymeant_h1_2026 p.30).
- **USD/ILS:** 3.157 (Bank of Israel representative rate 3.11.2026, from the brief). The dollar
  traded around 3.12 on 28.10.2026 after the elections [BZ-28].
- **US 10-year:** not needed, because the company reports in ILS.

## 6. What the market data says about "why so cheap" (facts for the synthesis)

1. **The low P/E is partly a lender's multiple.** Mega's "88% gross / 41% operating margin" is
   measured after interest and credit provisions on a business funded with 115M ILS of short-term
   bank credit (§1). It is not a capital-light software margin.
2. **There is a fresh, unexplained forced-selling event.** In six sessions (21–28.10.2026), 8.6% of
   the company changed hands and the share fell 47%, with no company news. The company says nothing
   unusual happened. Sponser suggests a large holder was exiting. No interested party reported
   selling, so the seller held less than 5% or was not a reported interested party. The identity of
   the seller is UNVERIFIED.
3. **The election shock hit Israeli financials on 28.10** (TA-90 −4.5%, banks −5%), and it
   coincided with the day of heaviest selling (§3).
4. **The stock is illiquid and neglected.** The market cap is about 125M ILS, the public float about
   37M ILS, and normal daily turnover about 15–40k ILS (§2). No analyst covers it (§4).
5. **Insider signals are weak.**
   - The founders sold at 6.90 ILS in March 2026 (§3).
   - No insider bought in the fall, and the 5M ILS buyback was not used before its 18.11.2026
     expiry (§3).
   - The founders' joint stake (29.54%) is now 4.5 points above the 25% level at which their
     shareholders' agreement lapses.
6. **Regulation and growth.** The new BNPL circular takes effect in early 2027 (§3). Actual H1 2026
   originations (516M annualised) run below both the 640M and the 600M run-rates the company
   published (§3).
7. **Upcoming catalysts:**
   - The Q3 2026 report and the Q3 dividend decision, probably in mid-to-late November 2026.
   - Expiry of the buyback plan on 18.11.2026.
   - The Bank of Israel rate decision on 23.11.2026.

## Sources

All pages were read on 3.11.2026, Israel time.

| Key | What was used | URL |
|---|---|---|
| [BZ-GV] | Price 317.3 (+1.76%), market cap 124,794k, 39,330,034 shares registered for trading, 90-day average turnover 188,480 ILS, 52-week range 251–781.09, interested parties (read 17:27 and 17:50) | https://www.bizportal.co.il/capitalmarket/quote/generalview/1180876 |
| [BZ-PERF] | Returns by period and by year, beta, standard deviation, average turnover and volume, dividends by year (17:28) | https://www.bizportal.co.il/capitalmarket/quote/performance/1180876 |
| [BZ-TRANS] | 3.11.2026 daily summary: 111,691 shares, 46 trades, high 319, low 307.5, average 315.51 (17:29) | https://www.bizportal.co.il/capitalmarket/quote/transactions/1180876 |
| [BZ-HIST] | Daily dividend-adjusted closes, 3.11.2021–2.11.2026, 82 pages (the page's own "historical rates" tab) (17:30–17:33) | https://www.bizportal.co.il/ajax/biz_papers_helper.ashx?action=get_paper_yearly_graph&request_type=2&paper_id=1180876&period=6&page_number=1 (pages 1–82) |
| [BZ-DIV] | Dividend history: amounts, payment and ex-dates (17:27) | https://www.bizportal.co.il/capitalmarket/quote/dividends/1180876 |
| [BZ-STAKE] | Interested parties and their holdings; holder split 70.22/29.78; holding funds (17:27) | https://www.bizportal.co.il/capitalmarket/quote/stakeholders/1180876 |
| [BZ-FLOW] | Interested-party flows for 90, 180 and 365 days (the stakeholders page's own data call) (17:36) | https://www.bizportal.co.il/ajax/biz_papers_helper.ashx?action=get_holding_flow_summary_data_json&paperId=1180876&period=3m (also `6m`, `y`) |
| [BZ-AN] | Analyst-recommendation tab (empty) (17:28) | https://www.bizportal.co.il/capitalmarket/quote/analystadvice/1180876 |
| [BZ-28] | "הבורסה הופתעה מהתוצאות", 28.10.2026 17:05: Paymeant's double-digit fall; company clarification; TA-90 −4.5%; dollar about 3.12 | https://www.bizportal.co.il/capitalmarket/news/article/20046372 |
| [BZ-29] | Market close report, 29.10.2026 13:47: +25.9% on thin turnover | https://www.bizportal.co.il/capitalmarket/news/article/20046488 |
| [BZ-BOI] | Bank of Israel held its rate at 3.25%, 21.10.2026 16:00 | https://www.bizportal.co.il/general/news/article/20045608 |
| [BZ-AK] | Yaakov Akilov analysis, 2.1.2025 | https://www.bizportal.co.il/capitalmarket/news/article/20011989 |
| [BZ-23F] | FY2025 results article, 23.2.2026 (title and summary only, from the company's news list) | https://www.bizportal.co.il/capitalmarket/news/article/20028124 |
| [TM] | 318.00 at 15:01 and 317.30 at 17:24; market cap 125.06M / 124.79M; interested parties | https://finance.themarker.com/stock/1180876 |
| [TM-0537] | ממשל שקלית 0537: yield to maturity 4.29%, 3.11.2026 17:14 | https://finance.themarker.com/bond/1166180 |
| [GL-MAYA] | Maya headline feed for the company, as shown on the Globes reports tab (17:35) | https://www.globes.co.il/news/Instrument/InstrumentHandlers/Get_Instrument_BursaMessage.ashx?instrumentid=370226&feeder=&maxItemsToShow=60 (tab: https://www.globes.co.il/portal/instrument.aspx?instrumentid=370226&mode=reports) |
| [GL-INS] | Interested-party buys and sells: dates, quantities, prices (17:41) | https://www.globes.co.il/portal/instrument.aspx?instrumentid=370226&mode=company |
| [SP] | "השלימה התרסקות של 50% בחודש ללא סיבה...", Sponser news, 28.10.2026 17:49 | https://www.sponser.co.il/Article.aspx?ArticleId=123772 |
| [SA] | Quote 318.00 at 3:01 PM IST, 39.33M shares, 52-week range 242.00–830.70, analysts n/a, earnings date (17:39) | https://stockanalysis.com/quote/tlv/PMNT/ |
| [SA-H] | Daily OHLCV, 4.5–3.11.2026 (S&P Global Market Intelligence data) (17:39) | https://stockanalysis.com/quote/tlv/PMNT/history/ |
| [TE] | Israel 10-year yield 4.162%, 3.11.2026 (17:42) | https://tradingeconomics.com/israel/government-bond-yield |
| [GNY] | Gornitzky client update on the BNPL circular, 29.7.2026 | https://www.gornitzky.co.il/wp-content/uploads/pdf/post/31940_bnpl-buy-n.pdf |
| [SWS] | Simply Wall St valuation page (search-engine snippet only, not opened) | https://simplywall.st/stocks/il/diversified-financials/tase-pmnt/payment-financial-technologies-shares/valuation |
| [TR] | TipRanks AI report (search-engine snippet only, not opened) | https://www.tipranks.com/stocks/il:pmnt/stock-analysis |

**Blocked or not used.**

- **Blocked, not retried:**
  - www.tase.co.il returned HTTP 403 from a bot check.
  - il.investing.com returned 403. A search snippet showed 587.80 on 3.8.2026, a market cap of
    230.76M and a 52-week range of 366.10–830.70; these are UNVERIFIED.
  - www.funder.co.il returned 403.
- **Not attempted:** maya.tase.co.il, because the brief says it blocks scripted access.
- **Not reachable from the WebFetch tool:** uk.marketscreener.com (outside its allowed domains).

## Files

- `market_calc.py` holds every derived figure; its output is `market_calc_output.txt`.
- `web/pmnt_daily_closes_bizportal.csv` holds the adjusted daily closes, 2021–2026.
- `web/pmnt_ohlcv_stockanalysis.csv` holds the unadjusted daily OHLCV with volume, May–November 2026.
- The raw pages are saved in `web/`, and the fetch and parse helpers in `market_tools/`.
