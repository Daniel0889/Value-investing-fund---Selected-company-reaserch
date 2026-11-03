# Gilat Telecom Global (TASE 1080597): governance, capital allocation and risk

Prepared 2026-11-03 as part of the Rev 4 study. This is one input to the CIO; it does not give a verdict.

**Sources.** The four filings supplied by the investor, cited as document id plus PDF page (p.1 = first PDF page):
`gilat_fy2023`, `gilat_fy2024`, `gilat_fy2025` (periodic reports) and `gilat_h1_2026` (Q2-2026 report).
Every table figure used here was checked on the PDF page itself. Every derived number (ratio, share count,
price, multiple) comes from `governance_calc.py` and is cited as "calc §n". Its output is in
`governance_calc_output.txt`, in the same folder as this file.

**Unverified items.** The web context comes from search-engine summaries only, because bizportal.co.il,
finance.themarker.com and Maya do not resolve from this environment. Every such item is labelled
UNVERIFIED and none of them carries a conclusion.

**Data gaps.**
- The holdings report of 8.1.2026 and the shareholder register of 16.3.2026 are only incorporated by
  reference (gilat_fy2025 p.215) and were not supplied.
- The H1-2026 file contains the directors' report and the separate (solo) interim data. It does not
  contain the consolidated interim statements or their notes (gilat_h1_2026 p.1-48).
- No Q3-2026 filing was supplied.

---

## 0. Bottom line

1. **Control.** Nobody controls the company: it has had no controlling holder since 17.2.2021. This means
   there is no tunnelling route, and the filings show no related-party dealings beyond pay. The CEO is the
   largest known insider. He holds 8.45% of the shares (8.54% fully diluted), most of them bought in 2023
   with his own money at 30 agorot a share. That is real alignment.
2. **Off-balance-sheet commitments.** The biggest economic risk is the Bezeq fibre IRU. Two layers are
   firm or likely: the 2024 deal and the first tranche of the 2025 expansion, totalling ILS 248M. That is
   1.87 times equity and 1.25 times the market cap. A further ILS 240M is conditional, and an O&M fee of
   4% a year applies on top (calc §6).
   - These amounts are not on the balance sheet.
   - The IRU is amortised over 25 years.
   - The amortisation is added back in Adjusted EBITDA, the metric that drives 70% of the CEO's bonus.
   - The commitment is not listed as a risk factor.
3. **Dilution.** Shares outstanding have roughly doubled since end-2022, to at least 119.0M by 19.8.2026.
   They could reach about 160M once Series D (in the money) and the options are counted, 2.74 times the
   2022 count (calc §1).
   - Equity was issued at ILS 0.30–1.35 a share.
   - The June 2026 buyback paid ILS 2.60, which is 2.60 times the Series D conversion price (calc §2).
4. **Concentration.** Two customers made up 41.8% of 2025 revenue. One of them, Vodacom (16.3%), has a
   contract that ends on 31.3.2027, 4.9 months from today (calc §7). Part of the government revenue is
   war-driven.
5. **Accounting quality and candour.** Mediocre: non-GAAP framing, an inconsistent backlog figure, a
   "no hedging" boilerplate that contradicts the hedges the company discloses, and a 2025 bonus cap that
   was raised retroactively (sections 2 and 6). No item is fraudulent-looking, and the audit opinions are
   clean with no emphasis of matter.
6. **Suggestion to the CIO.**
   - No governance disqualifier was found.
   - Add **+5 points of extra margin** for the off-balance-sheet commitments, the disclosure quality and the
     Africa/DRC exposure.
   - Count Series D as 29.1M extra shares.
   - Treat the Bezeq IRU cash payments as operating costs.
   - Keep any position **below 5% of the shares**: the licence requires Ministry approval at that level
     (section 1.3).

---

## 1. Who controls the company, and how

### 1.1 No controlling holder

- **No controlling core.** Since 17.2.2021 the company has had no controlling core ("חברה ללא גרעין
  שליטה") (gilat_fy2023 p.193; gilat_fy2024 p.199; gilat_fy2025 p.214). Reg. 22 therefore has no
  controlling-holder transactions to report (gilat_fy2025 p.214-215).
- **Ministry approvals of 8.10.2024** (reported 9.10.2024; gilat_fy2024 p.199):
  - The CEO, Itzik Ben Eliezer, filed a separate request and was approved to hold up to **25%** of the
    means of control.
  - A.A. Shidurit Telepage 1989 Ltd ("Shidurit") filed a separate request and was approved to hold up to
    **26%**.
  - Both approvals were limited to six months.
  - Goldfon Ltd was approved to hold up to **13.4%**.
- **The Ministry's presumption about Shidurit.** The Ministry stated that Shidurit "is the largest
  shareholder in the company today and is therefore presumed to be the controlling holder". The company
  says the presumption is rebutted, given Shidurit's holding relative to the other holders and its
  inability to direct the company (gilat_fy2024 p.199).
- **Position by March 2026** (gilat_fy2025 p.214):
  - The 25%/26% permit expired.
  - Ben Eliezer and Shidurit may each now hold up to 15%.
  - Neither Shidurit nor Goldfon is an interested party any longer, meaning each holds below 5%.
- **Implication.** Two holders asked at the same time to reach or pass the 25% "significant influence"
  presumption. If ownership consolidates without a takeover premium, that is creeping control. It did not
  happen, but the board should be asked what lay behind the 2024 requests.

### 1.2 Insiders and large holders

| Holder | Capital / fully diluted | Date | Source |
|---|---|---|---|
| Itzik Ben Eliezer (CEO) | 11.41% / 9.9% | near 26.3.2024 | gilat_fy2023 p.186 |
| " | 10.35% / 7.66% | near 27.3.2025 | gilat_fy2024 p.192 |
| " | 8.45% / 8.54% | near 25.3.2026 | gilat_fy2025 p.205 |
| Assaf Rozenhak (COO) | 0.04% / 0.15% | 2026 | gilat_fy2025 p.205 |
| Ami Schneider, Amir Cohen, Orit Gal | 0% / 0.49%, 0.35%, 0.27% (options only) | 2026 | gilat_fy2025 p.205 |
| Chairman Ami Barlev | not disclosed in the supplied documents; holdings report not supplied | | gilat_fy2025 p.215 |

- **CEO share count.** The CEO's percentage implies about 8.9M shares in March 2025 and about 9.1M in
  March 2026 (calc §5). His falling percentage reflects dilution, not sales.
- **UNVERIFIED web context:**
  - Bizportal, data 17.9.2026: CEO 7.79%, which would be about 9.27M shares, implying small net
    purchases; a mutual-fund house shown as "Ilon" 7.4%; Meitav 6.46% (both 30.6.2026).
  - Simply Wall St, undated: Shalom and Ruth Dadush, about 4.83M shares each, together about 8.1% of the
    August 2026 count (calc §8).
  - Globes, undated: Shidurit was described as wholly owned by its CEO Shalom Dadush.
  - If both figures are current, the Dadush family remains a bloc of about the CEO's size, held below the
    5% reporting threshold per person.
  - Sources: https://www.bizportal.co.il/capitalmarket/quote/stakeholders/1080597 ;
    https://simplywall.st/stocks/il/telecom/tase-gltl/gilat-telecom-global-shares/ownership ;
    https://www.globes.co.il/news/article.aspx?did=100221

### 1.3 Pledges, voting agreements and licence-based control rules

- **Voting agreements.** None is disclosed, and no shareholder agreement is mentioned in any of the four
  filings. Without the holdings report this is UNVERIFIED.
- **Pledges of shares by insiders.** None disclosed.
- **Company liens:**
  - In 2023 and 2024, bank loans were secured by a negative pledge (no disposal of assets outside the
    ordinary course without bank consent) and by cross-guarantees between the company and Gilat Telecom
    Ltd (gilat_fy2023 p.145; gilat_fy2024 p.148).
  - Those loans were repaid in 2025.
  - What remains is a pledge on a deposit of about ILS 3.5M backing guarantees (gilat_fy2025 p.158).
- **Licence rules** (satellite licence; gilat_fy2025 p.73-74):
  - Because the licensee has no controlling holder, acquiring **5% or more** of any means of control
    (10% for listed institutional investors) requires the Minister's prior written consent and an
    "Israeli" acquirer.
  - Holding 25% creates a presumption of significant influence.
  - Holders from security-sensitive countries may not reach 5%.
  - At least one third of the board must be Israeli residents with security clearance.
  - A security observer may sit on board meetings.
  - Consequences: there is no foreign buyer of the whole company, any takeover premium is limited, and
    **the fund needs Ministry approval to hold 5% or more.**

### 1.4 Board, audit and internal control

- **Board size.** The board has shrunk from 6 directors, 5 of them independent (gilat_fy2023 p.195-197,
  p.201), to **4**, of whom 3 are independent, 75% (gilat_fy2025 p.216-217, p.222).
- **Departures.** External directors Amir Tamari and Amit Brickman left after 9-year terms in 2024. The
  independent director Mirit Assaf also left (gilat_fy2024 p.202-203, p.207).
- **Current members:**
  - Chairman Ami Barlev, since 6.10.2019.
  - Yahel Yaakov Shahar (independent), since 2.10.2018.
  - Bina Rezinovsky-Sanker (external), since March 2024.
  - Haran Levavot (external), since 5.11.2024 (gilat_fy2025 p.216-217, p.221).
  - All four are listed as having accounting and financial expertise (gilat_fy2025 p.108).
- **The chairman's role.**
  - Barlev is an "active chairman with a significant scope of activity". He takes no dedicated chairman
    fee and no equity, only the statutory directors' fee (gilat_fy2025 p.213).
  - Both he and the CEO are Bezeq-group alumni (gilat_fy2025 p.216-217). Bezeq is now the key ISP
    supplier, and no personal interest is disclosed (gilat_fy2025 p.215).
  - The internal auditor reports organisationally to the chairman (gilat_fy2025 p.111).
- **Meetings.** The board met 6, 4, 4 and 5 times per quarter in 2025, 19 in all (calc §8), with 100%
  attendance (gilat_fy2025 p.225-226). The governance questionnaire answers every item "true"
  (gilat_fy2025 p.221-234).
- **External auditor.**
  - Brightman Almagor Zohar (Deloitte). Opinions on FY2023, FY2024 and FY2025 are unqualified, with no
    emphasis of matter and no going-concern doubt (gilat_fy2023 p.114-115; gilat_fy2024 p.116-117;
    gilat_fy2025 p.123-124).
  - The only key audit matter is the completeness and accuracy of new and changed long-term contracts.
  - The H1-2026 review of the separate data is clean (gilat_h1_2026 p.29).
  - Fees: about USD 150K for audit and USD 35K for other services in 2025 (gilat_fy2025 p.114).
- **Internal audit.**
  - The company uses outsourced partners of Haikin Cohen Rubin: Ilan Haikin from 2008 to 2025, then CPA
    Adi Yirimi from 30.3.2025.
  - Scope: 300 hours and about USD 23K in 2025. Two reports in 2025: DHLS sales and operations, and
    payroll (gilat_fy2025 p.111-114). This is thin for a group operating in six countries.
- **"Small corporation" relief.** The company adopted all the reliefs (gilat_fy2025 p.2, p.108;
  gilat_h1_2026 p.2, p.20). There is no auditor's report on internal control over financial reporting,
  and management's declaration is in a reduced form.
- **D&O cover.**
  - Insurance: USD 12M limit for a premium of about USD 21K, policy to 25.1.2027 (gilat_fy2025 p.219-220).
  - Indemnification letters for all directors and officers; these are the only contingent liabilities
    listed (gilat_fy2025 p.165).

---

## 2. Pay of the top officers against profits (Reg. 21)

USD thousands, employer cost (gilat_fy2023 p.186; gilat_fy2024 p.192; gilat_fy2025 p.205). The derived
ratios come from calc §4.

| | 2023 | 2024 | 2025 |
|---|---|---|---|
| CEO total (salary / bonus / share-based / car) | 515 (297/153/16/49) | 587 (315/208/17/47) | 693 (341/270/33/49) |
| Five highest paid, total | 1,820 | 1,935 | 2,116 |
| Net income | 715 | 1,786 | 6,350 |
| Top-5 pay / net income | 255% | 108% | 33% |
| CEO pay / net income | 72% | 33% | 11% |
| Directors' fees, non-employees | 180 | 238 | 162 |
| Key-management pay (note) | 534 | 562 | 797 |

- **Size.** Pay is modest in absolute terms and is now small relative to profit. The 2025 top-5 total
  equals 20% of trailing-twelve-month net income of about USD 10.4M (calc §4).
- **Growth.** The CEO's pay rose 1.35 times from 2023 to 2025, while net income rose 8.9 times (calc §4).
- **Directors' fees.** The statutory maximum is paid, about USD 40.5K per non-employee director in 2025
  (calc §8).

### CEO terms (gilat_fy2023 p.187; gilat_fy2024 p.193; gilat_fy2025 p.206-207)

- **Salary.** ILS 70K a month, ILS 75K from 1.1.2024, and ILS 80K approved by the general meeting on
  4.12.2025 (+6.7%, calc §8).
- **Notice period.** Raised from 90 to 180 days by the compensation committee on 10.10.2024
  (gilat_fy2024 p.193).
- **Bonus cap.** Up to 6 salaries for 2023 and 2024.
  - For 2024 there was an extra discretionary bonus of 2 salaries "for exceptional achievements"
    (gilat_fy2024 p.193). The CFO received 1 extra salary (gilat_fy2024 p.198).
  - The **2025 cap was raised from 6 to 8 salaries on 4.12.2025** (gilat_fy2025 p.206), in the last month
    of the year being measured. The 2025 targets had been set at "up to 6 salaries" (gilat_fy2024 p.194).
  - At 125% achievement this lifts the bonus from about 7.5 to 10 salaries (calc §4). The printed 2025
    bonus equals 9.5 monthly salary costs.
- **Bonus metrics.**
  - 2023–24: gross profit 20%, free cash flow 30%, Adjusted EBITDA 50%.
  - 2025: **gross profit 30%, Adjusted EBITDA 70%. The free-cash-flow metric was dropped** for the CEO,
    and for the COO and CTO too (gilat_fy2023 p.187; gilat_fy2025 p.207, p.210).
  - Adjusted EBITDA adds back the Bezeq IRU amortisation, USD 1,079K in 2025 (gilat_fy2025 p.92, p.131),
    which is 7.3% of 2025 Adjusted EBITDA (calc §6). The expanded Bezeq contract will make this add-back
    larger.

### Equity grants

- **CEO options.**
  - 900,000 in February 2022 at ILS 0.676.
  - 250,000 in March 2024 at ILS 0.446.
  - **4,000,000 in December 2025**, 4.26% of the end-2025 shares (calc §8): 2M at 110.15 agorot ("a
    significant premium of 20%") and 2M at 92.7 agorot (a 1% premium) (gilat_fy2025 p.166, p.206-207).
  - The strikes were set off the 30-day average before the board decision of no later than 28.10.2025,
    about 91.8 agorot (calc §5).
  - The Bezeq expansion was announced on **4.11.2025** (gilat_fy2025 p.41).
  - At the general meeting's approval the share price used for valuation was **ILS 1.19**. That is 28%
    above the lower strike and 8% above the "premium" strike (gilat_fy2025 p.166; calc §5). The options
    were therefore in the money when granted.
  - This is not evidence of wrongdoing, but the board should be asked whether the Bezeq deal was known
    when the strikes were fixed.
- **Grants to others in November 2025.** 4,665,000 options to 28 employees and 4 officers
  (gilat_fy2025 p.166). Grant-date fair value: ILS 2.3M for the CEO and ILS 1.76M for the others (calc §5),
  against a share-based expense of only USD 53–88K a year in 2023-25 (gilat_fy2025 p.172). The expense
  will step up from 2026.
- **Change of control.** Each VP is entitled to a retention bonus of 2 salaries (gilat_fy2025 p.208-212).

---

## 3. Related-party dealings (Reg. 22): the full list and their economics

The company states that in 2023, 2024 and 2025 it had no extraordinary or ordinary transactions with a
controlling holder, nor transactions in which directors or officers had a personal interest, other than
pay (gilat_fy2023 p.194; gilat_fy2024 p.200; gilat_fy2025 p.215). The related-parties note shows pay only
(gilat_fy2025 p.176).

**Transactions with interested parties or insiders:**

1. **CEO private placement, 27.6.2023.**
   - Terms: 6,134,442 shares at 30 agorot for ILS 1,840,333 in cash (gilat_fy2023 p.7, p.183).
   - Size: 10.5% of the pre-issue share count (calc §8).
   - The same 30-agorot price was then offered to all holders in the July 2023 rights issue
     (gilat_fy2023 p.151).
   - Note 15d prints 6,148,754 shares. The share-count bridge only reconciles with 6,134,442 (calc §1).
2. **CEO participation in the 2023 rights issue.** He exercised 558,978 rights allotted to him and
   1,000,000 more that he bought on the market (gilat_fy2023 p.151). His 2023 subscriptions total 7.69M
   shares for about ILS 2.31M. At the August 2026 parity price they were worth about ILS 16.3M, 7.1 times
   cost (calc §5, §8).
3. **August 2022 officers' options.**
   - 6,000,000 options: 3M to the CEO and 600K each to five VPs.
   - Strikes: ILS 1.00 (36 months) and ILS 0.70 (24 months), against a share price of ILS 0.32.
   - **The officers paid their fair value in cash, about ILS 90.5K.** All the options expired unexercised
     (gilat_fy2025 p.169-170; gilat_fy2023 p.184).
   - This is a shareholder-friendly structure.
4. **Other option grants:**
   - October 2021: 2,338,000 at ILS 0.826 (gilat_fy2025 p.171).
   - November 2022: 430,000 at ILS 0.3517 (p.169).
   - April 2024: 500,000 at ILS 0.541 (p.168).
   - November and December 2025: see section 2.
   - Options outstanding at 31.12.2025: 12,093,500, of which 2,899,047 exercisable (gilat_fy2025 p.172).
5. **Insurance and indemnification.** D&O insurance and indemnification letters (section 1.4) were
   approved as market-term transactions by the compensation committee (gilat_fy2025 p.219-220).
6. **"Negligible transaction" procedure.** A deal with an interested party counts as negligible if it is
   below 1% of each relevant parameter, below 5% per type of deal, or below USD 100K of annual profit
   (gilat_fy2025 p.214-215). No such transaction is listed.
7. **Historical item.** A capital reserve of USD 607K from "transactions with a controlling holder" dates
   from before 2021 and is unchanged (gilat_fy2025 p.129-130).

**Intra-group items** (not related-party in the Reg. 22 sense, but relevant to the economics):

- **Parent loans to subsidiaries at 7%:** ILS 27M (2018), ILS 9.3M (June 2022), ILS 3M (April 2023) and
  ILS 27.2M (March 2025), all not repayable before 31.12.2027. There is also a capital note of
  ILS 3.547M (gilat_fy2025 p.199-200).
- **Series C bonds held by a subsidiary.** At the report date the subsidiary held 5,480,878 par of
  Series C, 84.8% of what was left (gilat_h1_2026 p.22; calc §1).

---

## 4. Capital allocation, 2021–2026

### 4.1 Dividends

- **None** in 2021 through H1 2026, and "during the last decade generally" (gilat_fy2023 p.7-8;
  gilat_fy2024 p.9; gilat_fy2025 p.10). At the end of 2023 the company had no distributable profits and no
  dividend policy (gilat_fy2023 p.8).
- The company now says it "may consider" a policy (gilat_fy2025 p.10).
- The separate (solo) accumulated deficit was still ILS 10.1M at 30.6.2026 (gilat_h1_2026 p.31), so any
  distribution relies on the two-year-profits test.
- **Bond-deed limits** (gilat_h1_2026 p.23, p.25):
  - equity after the distribution of at least ILS 35M;
  - net financial debt / EBITDA of no more than 4.5;
  - no warning signs;
  - no distribution of revaluation gains;
  - liquidity covering 18 months of debt service.
- On the equity test there is about ILS 97M of room (calc §7).

### 4.2 Buybacks

| When | What | Amount | Price | Source |
|---|---|---|---|---|
| June 2022 | Series C bought through a subsidiary | 11,710,089 par (19.51%) | USD 2,887K | gilat_fy2025 p.156; gilat_fy2023 p.7 |
| April 2023 | Series C bought through a subsidiary | 4,189,635 par (7.35%) | USD 823K | gilat_fy2025 p.156 |
| July 2024 | Exchange offer for Series C | 9,965,474 par → 17,439,580 shares + ILS 597,928 | 0.537 of par retired per share (calc §2); loss ILS 381K | gilat_fy2025 p.133, p.156-157 |
| 12–30.6.2026 | Share buyback (board approval 11.6.2026, cap ILS 6M) | 2,300,000 shares, ILS 5,988K incl. fees | **260.36 agorot** average | gilat_h1_2026 p.3, p.37, p.34 |
| ~7.10.2026 | New buyback program of up to ILS 7M | not disclosed | not disclosed | Funder, via search (**UNVERIFIED**), https://www.funder.co.il/article/211179 |

**Assessment.**
- **Bonds bought below par in 2022–23 were good capital allocation.** The company retired debt cheaply
  while it was stressed.
- **The 2026 share buyback is harder to defend:**
  - It was done at 2.31 times book value per share (calc §2).
  - It recovered only 8.9% of the 25.8M shares that conversions issued in the same half-year (calc §2).
  - Its average price was 22.9% above the price implied by bond parity on 19.8.2026 (ILS 2.12, calc §2).
  - If the Mega market cap is right, it was also about 56% above today's implied price of about ILS 1.67.
    That figure is approximate: the share count excludes option exercises during 2026 and should be
    confirmed on TASE.
- The size, ILS 6M or 6.4% of cash (calc §2), was a token. Whether 260 agorot was below intrinsic value
  is for the valuation team.

### 4.3 Share issues, conversions and dilution

| Date | Event | Shares | Price (ILS/share) | Source |
|---|---|---|---|---|
| 31.12.2022 | Shares issued | 58,438,636 | | gilat_fy2023 p.151 (unchanged during 2021–22, p.120-121) |
| July 2023 | CEO private placement | 6,134,442 | 0.30 | gilat_fy2023 p.183 |
| July 2023 | Rights issue | 4,056,402 | ~0.30 | gilat_fy2023 p.151 |
| July 2024 | Series C exchange offer | 17,439,580 | 0.537 of par (calc §2) | gilat_fy2024 p.155 |
| July 2025 | Private placement to Pasternak Shoham (~ILS 5.3M) and Mor (~ILS 1.5M) | 7,710,000 | 0.88 (calc §2); discount to market not disclosed | gilat_fy2025 p.8, p.165 |
| 2025 | Option exercises and small conversions | 158,253 | | calc §1 |
| H1 2026 | Series C conversions (13,151,410 par) | 9,741,785 | 1.35 | gilat_h1_2026 p.37 |
| H1 2026 | Series D conversions (16,032,064 par) | 16,032,064 | 1.00 | gilat_h1_2026 p.37 |
| June 2026 | Treasury (buyback) | −2,300,000 | 2.60 | gilat_h1_2026 p.37 |
| July–August 2026 | Conversions after the period | 1,623,812 (calc §1) | 1.35 / 1.00 | gilat_h1_2026 p.37 |
| **19.8.2026** | **Outstanding, at least** | **119,034,974** | | calc §1 |
| Still to come | Series D still convertible (29,134,661 par) | +29.1M | 1.00 until 1.4.2028 | gilat_h1_2026 p.24 |
| Still to come | Options outstanding at 31.12.2025 (upper bound) | +12.1M | various; exercisable ones weighted avg USD 0.23 | gilat_fy2025 p.172 |

- **Scale.** Shares outstanding are 2.04 times the end-2022 count. On a potential basis the count is
  about 160M, 2.74 times (calc §1). The 8.67M options granted in 2025 alone equal 9.2% of the end-2025
  shares (calc §1).
- **Series D is economically equity.**
  - Its market value of ILS 61.7M is 2.54 times its book value of ILS 24.3M (calc §7).
  - Parity implies a share price of about ILS 2.12 on 19.8.2026 (calc §2).
  - The rules say debt that could force dilution is close to disqualifying. This dilution is not forced by
    distress, because the bond is in the money. But it is certain: **count it as 29.1M shares, not as
    debt.**
- **Effective issue price.** Holders of shares bought at today's prices have been diluted by issuance at
  0.30–1.35. The ILS 1.00 conversion price of Series D was set when the share price used in the issue-date
  valuation was ILS 0.70 (gilat_fy2025 p.158).

### 4.4 Debt raised and repaid

- **Series C, June 2021.** ILS 60M par, net ILS 57.63M (USD 17.69M). Coupon 4.5%. Convertible at ILS 1.15,
  then ILS 1.35. It amortised over 2023–26, with the final 34% due on 1.9.2026 (gilat_fy2025 p.155-156;
  gilat_h1_2026 p.22).
- **Series D, February 2025.** ILS 45.872M par, net ILS 44.25M (USD 12.45M). Coupon 5.5%. Repayable in
  2028–31; 36.5% had converted by 19.8.2026 (gilat_fy2025 p.157; calc §1).
- **Repaid:**
  - Series B and Series F, early, in 2021 from the Wiocc proceeds (gilat_fy2023 p.93, p.123).
  - The state-guaranteed loan of ILS 5M (2020).
  - The ILS 7.5M bank loan at prime + 3.04% (taken in December 2024, repaid in 2025)
    (gilat_fy2025 p.158, p.132).
- **Totals.** Cash raised over 2021–H1 2026 was about USD 33.0M: USD 30.1M from convertibles and USD 2.8M
  from equity (calc §3). Cash returned was about USD 3.7M in bond buybacks, USD 0.2M in the exchange-offer cash
  leg and about USD 1.9M in the share buyback (calc §3).

### 4.5 Investments and divestments, and how they turned out

- **Wiocc.** A stake of about 5.9% was sold in November 2021 for USD 9.4M gross, and the proceeds repaid
  Series B and F early (gilat_fy2023 p.93; investing cash flow USD 9,438K, p.123). This was a sensible
  deleveraging.
- **ISP entry.** Announced in March 2022, with retail service from April 2023 (gilat_fy2025 p.133).
  - The early "tens of thousands of customers" were mostly wholesale lines for yes: 44,280 in 2023 and
    81,065 in 2024. The yes contract ended in 2025 (gilat_fy2023 p.85; gilat_fy2024 p.81;
    gilat_fy2025 p.91).
  - Own private customers: about 3,977 in 2023, 8,300 in 2024, 21,000 in March 2026 and 26,000 in
    August 2026 (gilat_fy2023 p.85; gilat_fy2024 p.81; gilat_fy2025 p.91; gilat_h1_2026 p.5).
  - The segment's direct profit was USD 524K in 2025 (gilat_fy2025 p.90).
- **Bezeq IRU, the largest commitment in the company's history** (gilat_fy2024 p.171;
  gilat_fy2025 p.152-153, p.183, p.41-42):
  - The December 2024 deal covers 18,000 lines for ILS 88.02M plus VAT, ILS 4,890 a line, plus a 4% a
    year O&M fee. It was "fully used earlier than expected".
  - The November 2025 expansion adds up to 90,000 lines at about ILS 4,444 a line (calc §6):
    - Tranche 1: 36,000 lines over three years from December 2025, about ILS 160M "assuming full
      exercise".
    - Tranches in 2029, 2031 and 2033: about ILS 80M each, CPI-linked.
    - The company is released only from a *subsequent* tranche if its growth target is missed.
  - Each tranche can be paid over 10 years with interest; the first tranche of the original deal carries
    5%.
  - Only cash already paid is booked, as "deferred expenses". It is amortised over 25 years, including two
    5-year options that have not been exercised. This books 60% of a straight-line 15-year charge each
    year (calc §6; gilat_fy2025 p.153).
  - The unpaid instalments are not shown as liabilities.
  - Size: ILS 248M is firm or likely (1.87 times equity, 1.25 times the market cap); ILS 488M is the total
    if every tranche is bought (calc §6).
  - The price-protection clause of the original deal does not apply to the new lines
    (gilat_fy2025 p.42).
- **Africa.** Exposure has been reduced deliberately. Africa's share of revenue fell from 64.4% in 2022 to
  24.8% in 2025 (calc §8; gilat_fy2024 p.83; gilat_fy2025 p.93). Nigeria is inactive
  (gilat_fy2025 p.8). There have been no acquisitions since 2021; the stated strategy still seeks
  "investments and acquisitions" (gilat_fy2025 p.7).

### 4.6 Cash hoarding against returns

- **Position.** Cash at 30.6.2026 was ILS 93.0M, 46.9% of the market cap. The company's "net financial
  asset" is ILS 66M, 33.3% (calc §8; gilat_h1_2026 p.3, p.9). If Series D is treated as converted, the
  figure is about ILS 90.3M, alongside 29.1M more shares (calc §8).
- **Uses.** The cash is earmarked for "business development, growth engines, strategic deals and working
  capital" (gilat_fy2025 p.202). It will also fund the Bezeq instalments.
- **Assessment.** Returns so far are token: one ILS 6M buyback and no dividends. Cash is rising faster than
  it is being deployed, and the stated use leans towards deals rather than returns. Watch for an
  acquisition.

---

## 5. Insider ownership and alignment

- **For alignment:**
  - The CEO's stake of about 8.9M shares was worth ILS 14.8–18.9M (USD 4.7–6.0M). That is 6.8–8.6 times
    his 2025 pay, measured at the implied November price and the August parity price (calc §5).
  - He built it mostly with his own cash at 30 agorot in 2023, and in 2024 he sought permission to go to
    25%.
  - His 5.15M options carry ILS 3.8–6.1M of intrinsic value (calc §5).
  - The chairman takes only statutory fees.
  - In 2022 the officers paid for out-of-the-money options.
- **Against alignment:**
  - The other officers own almost nothing (0–0.04%; options only).
  - In 2025 the board shifted the CEO's incentives towards Adjusted EBITDA and away from free cash flow,
    raised the cap retroactively, and granted options in the money.
  - Ownership by the chairman and directors cannot be verified from the documents supplied.
- **Net: good alignment at CEO level, weak at the next layer.**

---

## 6. Management candour: statements against results

| Statement | What the documents show | Source |
|---|---|---|
| "ISP accumulated tens of thousands of private and business customers" (2023 and 2024) | Mostly the yes wholesale lines (44,280; 81,065), which ended in 2025. Own private customers were 3,977 and 8,300. | gilat_fy2023 p.83, p.85; gilat_fy2024 p.81; gilat_fy2025 p.91 |
| Backlog | USD 30.5M to 2027 (March 2024); USD 67M to 2028 (March 2025); **USD 52.3M to 2029 and USD 58.3M to 2028 in the same FY2025 report**; ILS 158M to 2029 (August 2026). A declining trend, and inconsistent. | gilat_fy2023 p.83; gilat_fy2024 p.80, p.127; gilat_fy2025 p.89, p.134, p.102; gilat_h1_2026 p.3, p.35 |
| Option revaluation "is not an economic loss … the company has no monetary liabilities for it"; non-GAAP profit excludes it (USD 1,693K, 27% of 2025 net income) | Conversion at ILS 1.00–1.35 while the share trades at about ILS 2 is a real transfer from shareholders. From 2026 the charge disappears from the P&L because of the change of functional currency, which flatters 2026 profit against 2025. | gilat_fy2025 p.89, p.93; gilat_h1_2026 p.2, p.6; calc §8 |
| "Free cash flow before prepaid expenses" and Adjusted EBITDA presented as the headline numbers | Both exclude the Bezeq IRU cost, a recurring cost of the ISP business. | gilat_fy2025 p.92-93, p.131; gilat_h1_2026 p.3, p.7 |
| "The group does not invest in derivatives or hedging transactions" (financial-instruments note, every year) | The directors' reports disclose forwards each year. A USD 516K liability on currency options was booked at 31.12.2025. | gilat_fy2023 p.162 vs p.98; gilat_fy2024 p.165 vs p.97; gilat_fy2025 p.177 vs p.154-155; gilat_h1_2026 p.19 |
| "The company is not leveraged and reduced its debt risks to negligible levels" | Correct for on-balance-sheet debt, but the ILS 248M of IRU commitments is omitted, and the risk-factor table does not mention them. | gilat_fy2025 p.90, p.82-86 |
| Dec-2025 CEO options priced at a "significant premium of 20%" | In the money at approval (ILS 1.19 against strikes of 0.927 and 1.1015). | gilat_fy2025 p.206, p.166 |
| Cause of the working-capital deficit | The note blames Series D; the directors' report blames Series C. | gilat_fy2025 p.133 vs p.99 |

**Smaller errors that indicate lax drafting:**
- Reg. 24A points to "note 15" for share capital, which is note 16 (gilat_fy2025 p.215).
- Note 22 points to "note 7a" for the Bezeq deal, which is in note 9 (gilat_fy2025 p.183).
- The FY2024 Reg. 21 table is headed "USD thousands" but the figures are in USD (gilat_fy2024 p.192).
- In the FY2025 Reg. 21 table, Amir Cohen's components sum to 314 against a printed total of 347, and
  Schneider's to 416 against 413 (calc §4).
- The CEO placement is printed as 6,148,754 shares instead of 6,134,442 (gilat_fy2023 p.151).
- Part D of FY2023 shows 2023 directors' fees of USD 224K against 180 in the note; 224 is the 2022 figure
  (gilat_fy2023 p.192, p.161).
- The H1 report dates the FY2025 report 23.3.2026, although it was approved on 25.3.2026, and calls the
  Q1-2026 report "Q1 2025" (gilat_h1_2026 p.2).
- Reg. 26A still lists Ilan Haikin as internal auditor (gilat_fy2025 p.218), while the directors' report
  names Adi Yirimi from 30.3.2025 (gilat_fy2025 p.111).

**To the company's credit:**
- It disclosed the Uganda tax problem and restated its comparatives (gilat_fy2023 p.168-169).
- It rates Africa and customer concentration as "large" risks (gilat_fy2025 p.86).
- It gives full covenant tables.
- It disclosed the end of the yes contract (gilat_fy2025 p.91).

---

## 7. Litigation, regulatory, tax and contingent exposures

- **Litigation.**
  - A consultant's claim of ILS 552,105, filed 5.12.2022, was settled by mediation for USD 100K and paid
    in December 2023 (gilat_fy2023 p.151).
  - No open claims are disclosed in FY2024 or FY2025. The only contingent items are the indemnification
    letters (gilat_fy2024 p.155; gilat_fy2025 p.165).
- **Uganda tax.**
  - A 2022 claim for 2016–2020 of about USD 2.5M was reduced to about USD 740K of principal, paid in early
    2023, plus about USD 500K of interest and indexation.
  - The company asked for the interest to be waived and called the waiver "highly likely"
    (gilat_fy2023 p.168).
  - **The outcome is not reported in FY2024 or FY2025, so it is UNVERIFIED.** The comparatives were
    restated: equity at 1.1.2021 fell by USD 668K (gilat_fy2023 p.169).
- **Other tax.**
  - Assessments are final through 2020 (gilat_fy2025 p.164).
  - Unrecognised tax losses were USD 19.0M at end-2025 (gilat_fy2025 p.163). This is a potential asset.
- **Supplier dispute risk (Intelsat, now part of SES).**
  - About USD 4.5M is open and payable, and the parties "from time to time" dispute the amount
    (gilat_fy2025 p.160; gilat_fy2024 p.93-94).
  - In March 2020 there were arrears of about USD 6M, rescheduled over 24 months against a USD 2M credit
    (gilat_fy2023 p.146).
  - The new Intelsat agreement includes **future purchase commitments of an undisclosed amount**
    (gilat_fy2025 p.160).
- **Regulatory.**
  - Israeli licences are needed for the satellite and ISP businesses. Uganda's NPSP licence runs to
    30.6.2030 (gilat_fy2025 p.75).
  - 5G C-band interference (gilat_fy2025 p.82).
  - Changes to the wholesale market and the end of Bezeq's structural separation have already cost the
    yes contract (gilat_fy2025 p.91).
  - Licence control rules apply (section 1.3).
- **Compliance.**
  - Outside Israel the company sells partly through agents paid on a success-fee basis
    (gilat_fy2024 p.51; gilat_fy2025 p.60).
  - The Vodacom renewal raised agents' costs (gilat_fy2025 p.96), and a prepayment of about USD 2.4M was
    "part of the Vodacom deal costs" (gilat_fy2024 p.83).
  - Anti-bribery controls are not discussed in any filing.
- **Goodwill.** USD 4.4M, all in the Africa-heavy global segment. Recoverable value is 2.49 times segment
  assets at a 20% discount rate (calc §7; gilat_fy2025 p.109, p.150-151).

---

## 8. FX, interest, credit and liquidity risk; covenants

- **FX.**
  - The functional currency changed from USD to ILS on 1.1.2026 (gilat_fy2025 p.177, p.200;
    gilat_h1_2026 p.36-37).
  - At 30.6.2026 the company was net short USD by ILS 65.3M (USD 20.7M), mostly satellite suppliers and
    satellite leases (calc §7; gilat_h1_2026 p.19).
  - Forwards cover USD 2M a month to December 2026 and USD 1.5M a month in 2027 (gilat_h1_2026 p.19).
  - A stronger dollar hurts margins.
- **Interest.**
  - No floating-rate debt remains.
  - The Series C and D convertibles are fixed at 4.5% and 5.5% (gilat_h1_2026 p.22, p.24).
  - Cash earns 3.75–4.7% (gilat_fy2025 p.178).
  - Bezeq instalments carry interest at Bezeq's bond yield (gilat_fy2025 p.183).
- **Credit.**
  - The credit-loss allowance is USD 6.8M, **29.5% of gross receivables**, mostly a legacy of Africa
    (calc §7; gilat_fy2025 p.147).
  - Receivable days rose from 62 to 69 (gilat_fy2025 p.147).
  - The company has no export credit insurance (gilat_fy2025 p.84).
  - The main customers are the Israeli defence and government sector and Vodacom DRC. Vodacom accounts for
    96% of the company's DRC revenue (calc §8).
- **Liquidity.**
  - At 31.12.2025, financial assets of USD 48.9M covered liabilities due within a year (USD 38.7M)
    1.26 times (calc §7; gilat_fy2025 p.178).
  - At 30.6.2026 working capital was positive at ILS 69.0M consolidated, and the company reported no
    warning signs (gilat_h1_2026 p.14).
  - The board's liquidity review is at gilat_fy2025 p.99-101.
  - Bank credit lines exist, but their size is not disclosed (gilat_fy2025 p.100).
- **Covenants (Series C and D)** (calc §7; gilat_fy2023 p.110; gilat_fy2024 p.110; gilat_fy2025
  p.116-117; gilat_h1_2026 p.23, p.25):
  - Limits: net financial debt to total assets of 60% or less, net financial debt to EBITDA of 5 or less,
    and equity to total assets of at least 12%.
  - At 30.6.2026: −24%, −0.75 and 48%, so the headroom is very large.
  - At 31.12.2025: 3%, 0.11 and 29%, printed without brackets, unlike other years.
  - Other terms: a cross-default clause at 12.5% of financial liabilities or ILS 20M, and a step-up of
    0.25% per breach. The bonds carry no rating.
  - Bank covenants: none remaining.
- **Constraint on the fund's rule.** The covenants do not bind. The binding constraint for the
  no-leverage rule is the IRU (section 4.5).

---

## 9. Key-person risk

- **Exposure.** A four-VP team under a CEO who designed the turnaround (gilat_fy2025 p.217-218):
  - CEO Ben Eliezer, ex-Bezeq, appointed in December 2021; he holds about 8.5% of the shares.
  - Ami Schneider, VP for government and defence since 2012. That segment made 63% of 2025 revenue and
    includes the 25% customer. He earned USD 119K in commissions (gilat_fy2025 p.205).
  - Orit Gal, CFO since 2014, also responsible for market risk.
  - Assaf Rozenhak, COO, responsible for Africa sales.
- **Mitigants.** Notice periods are 120–180 days, there are change-of-control retention bonuses, and
  every officer received new options in late 2025 (gilat_fy2025 p.206-213).
- **Disclosure gap.** No key-person risk factor is disclosed (gilat_fy2025 p.82-86).
- **Board depth.** With 4 directors, one departure would put the external-director composition at risk.

---

## 10. Red flags, ranked

1. **The Bezeq IRU is quasi-leverage kept off the balance sheet.**
   - ILS 248M is firm or likely (1.87 times equity, 1.25 times the market cap), plus up to ILS 240M that is
     conditional.
   - A 4% O&M fee applies; the 25-year amortisation includes options that have not been exercised.
   - The cost is excluded from Adjusted EBITDA and from "free cash flow before prepaid expenses", and it is
     absent from the risk factors (calc §6; gilat_fy2025 p.152-153, p.183).
   - If customer growth stalls, these are fixed costs.
2. **Customer concentration and the renewal cliff.**
   - Customer A and Vodacom made up 41.8% of 2025 revenue.
   - Vodacom's contract ends 31.3.2027, in 4.9 months (calc §7).
   - Defence demand is partly war-driven: the "Iron Swords" war, "Am KeLavi" (June 2025) and
     "Sha'agat HaAri" (2026) (gilat_fy2025 p.134; gilat_h1_2026 p.12, p.36).
3. **Serial dilution and timing of capital returns.**
   - Shares outstanding are 2.04 times the end-2022 count, and the potential count is 2.74 times.
   - Equity was issued at 0.30–1.35, while ILS 6M of shares was bought back at 2.60 in the same half-year
     in which conversions issued 25.8M shares (calc §1-2).
4. **Pay-setting.**
   - The 2025 bonus cap was raised from 6 to 8 salaries in December 2025.
   - The free-cash-flow metric was dropped, and 70% of the bonus now rides on Adjusted EBITDA, which
     excludes the IRU.
   - The CEO's options were in the money at grant and priced a week before the Bezeq announcement
     (section 2).
5. **Disclosure quality.**
   - The issues are set out in section 6: non-GAAP framing, inconsistent backlog, the "no hedging"
     boilerplate and cross-reference errors.
   - Small-corporation reliefs apply, there is no internal-control audit, and internal audit is thin
     (300 hours).
6. **Ownership ambiguity and licence limits.**
   - In 2024 the Ministry presumed Shidurit to be the controlling holder, and both the CEO and Shidurit
     sought approval for 25–26%.
   - Current holdings are not in the supplied documents; the Dadush family may hold about 8% (UNVERIFIED).
   - The licence caps holdings of 5% or more without approval, which limits any takeover premium and the
     fund's position size.
7. **Legacy Africa and compliance.**
   - Receivable allowance of 29.5%.
   - DRC is 17.1% of revenue (calc §8).
   - Uganda interest of USD 0.5M with an undisclosed outcome.
   - Success-fee agents, with no anti-bribery disclosure.
   - Intelsat payable of USD 4.5M, disputed from time to time, with undisclosed purchase commitments.
8. **Comparability after the change of functional currency.** From 2026 the P&L is in ILS and the
   conversion-option charge (27% of 2025 net income) no longer appears. The company is net short USD by
   USD 20.7M, partly hedged (calc §7-8).
9. **Key-person concentration** in the CEO and the government and defence VP (section 9).
10. **Litigation and other contingencies.** Low. One small settled claim, and no open claims disclosed.

**Offsetting positives:**
- No controlling holder and no related-party transactions.
- The CEO bought about 10.5% of the company with his own cash.
- Officers paid for options in 2022.
- Pay is modest and is now 20–33% of profit.
- Bonds were bought back below par, and Wiocc was sold to deleverage.
- Clean audit opinions.
- Net financial asset of ILS 66M, with very large covenant headroom.

---

## 11. Implications for the valuation team and open items

- **Share count.** Use at least 119.0M outstanding at 19.8.2026, plus 29.1M Series D shares, plus the
  dilution from in-the-money options. Remove the Series D book liability (ILS 24.3M) from debt (calc §1,
  §7-8).
- **Bezeq IRU.** Treat the cash cost (instalments, interest and the 4% O&M) as an operating cost, the same
  way IFRS 16 lease payments are treated. Do not use Adjusted EBITDA or "free cash flow before prepaid
  expenses".
- **Normalisation.** Normalise the government and defence revenue for the war spike. Put the loss or
  repricing of Vodacom (about USD 15M a year, calc §7) into the bear case.
- **Margin.** A suggested **+5 points** of extra margin, for the reasons in section 0.
- **Open items for the investor to check on Maya:**
  - the holdings report of 8.1.2026 and any later changes in holdings, including the chairman's stake and
    the Dadush, Shidurit and Goldfon holdings;
  - the immediate reports of 28.10.2025 (options and pay) and 4.11.2025 (the Bezeq expansion);
  - the October 2026 buyback of up to ILS 7M (UNVERIFIED);
  - the outcome of the Uganda interest waiver;
  - the status of the Vodacom renewal;
  - the consolidated H1-2026 statements, not supplied;
  - the current share count and price. The Mega market cap of ILS 198.2M implies about ILS 1.67 a share at
    119.0M shares, against ILS 2.12 at bond parity in August (calc §2).
