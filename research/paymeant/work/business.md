# Paymeant Financial Technologies (TASE 1180876): business and moat

Workstream: business and moat, for the Revision 4 study. Written 3.11.2026.

**Sources.** The company's own filings: `paymeant_fy2023`, `paymeant_fy2024` and `paymeant_fy2025` (Parts A, B and C) and `paymeant_h1_2026` (the main-developments report and the interim statements to 30.6.2026). `p.N` is the PDF page index. Every table figure used here was checked on the PDF page image (fy2023 p.19, p.37, p.39; fy2024 p.40-42; fy2025 p.20, p.39-46, p.64-68; h1_2026 p.5-6, p.13-15, p.32-33). Balance-sheet history for 2021-2023 comes from the statements as extracted in `fin_A.json`, and the references are repeated in the script. Every ratio, growth rate, average and scenario below is printed by `business_metrics.py` (run `python3 -I business_metrics.py`; the output is saved in `business_metrics_output.txt`). Section numbers in the form "§n" point to that output. Units are ILS thousands unless stated; originations are in ILS millions.

**Reporting reliefs.** The company uses the TA Tech-Elite reliefs and the small-corporation reliefs (fy2025 p.58; h1_2026 p.5). Because of the Tech-Elite relief, the half-year report is a short "main developments" report in place of a full directors' report. Disclosure is thinner than for a normal TASE issuer, and this matters for data verification below.

---

## 0. Summary

1. **What it is.** Paymeant is not a software company. It is a licensed non-bank consumer lender that originates point-of-sale (POS) instalment loans through merchants and sells most of them on: monthly or weekly to banks, and in portfolios to its own unconsolidated special-purpose companies, which are financed by a bank (fy2025 p.6-7, p.12-13, p.50-53). Mega's 88% "gross margin" and 41% "operating margin" are measured after funding cost and credit losses, because the P&L nets these above "total revenues, net" (h1_2026 p.24). On loans originated, the business earned about ILS 4.4 of pre-tax profit per ILS 100 lent over the TTM (§3).
2. **There is one segment.** Revenue rose from 7,850 (2021) to 56,616 (2025) and 60,301 TTM. Net income went from a loss of 769 to 18,188 and 18,466 TTM (§1). Growth stalled in 2023-2024 (war, peak rates), originations jumped 37.5% in 2025, and growth slowed again in H1 2026. In H1 2026 originations rose 7.5% and net income 3.5%; Q2 net income fell 1.2% (§1).
3. **The mix of how it makes money changed.** Merchant fees rose from 31% of revenue (2023) to 48% (2025) and 55% (H1 2026). Over the same period, loan-sale and fair-value income and interest fell as shares of revenue (§4). In 2025 the company introduced fixed monthly merchant subscriptions and the "360" operations and payment-guarantee product (fy2025 p.13, p.39-41, p.64). The FY2024 report had said there was no fixed merchant fee (fy2024 p.13).
4. **Concentration.** There are no material merchant or borrower customers (fy2025 p.40). The concentration is on the funding side: four bank lines totalling 340M, and portfolio take-outs financed by one banking corporation through the SPCs (fy2025 p.49, p.51-53).
5. **Backlog.** There is none; loans are made and booked at the point of sale (fy2025 p.43). The proxies are mixed. The stated annualised pace was cut from 640M (Feb 2026) to 600M (Aug 2026), and H1 2026 annualised to 516M (§10).
6. **Moat.** The moat is narrow at best and not proven durable. Returns are good: ROE 17.5-24.2% in 2023-2025 and 22.6% TTM (§6). Net revenue per ILS 100 originated rose from 5.97 (2022) to 9.64 (TTM) (§3). Against that, switching costs are low (merchant agreements can be cancelled at any time, fy2025 p.41), nothing is patented (fy2025 p.45), and the credit-data and licence "barriers" are open to every licensed lender. Rivals have larger balance sheets, which the company itself names as its weak point (fy2025 p.44). The profit history is four years long and covers no full credit cycle.
7. **TTM is a high-normal year, not a one-off peak.** It contains no other income, tax is at the normal rate, and the fair-value step-up is small. But the margin on originations is at the top of the range: TTM 4.42% against a 2022-2025 average of 3.74% (§11). Arrears on the pre-sale book rose from 2.65% to 4.57% in H1 2026 (§8). Regulation from January 2027 adds risk (h1_2026 p.7-8). **Normalised base case: pre-tax about 20.7M and net about 15.9M, 14% below TTM. Bear: net about 9.4M. Bull: net about 20.4M** (§11).
8. **Circle of competence.** The mechanics are understandable, but the business cannot be predicted 5-10 years out. Earnings depend on bank appetite to buy loans, funding rates, the credit cycle, the new BNPL regulation and fair-value marks. Several key figures cannot be verified from public filings: actual loss curves of sold portfolios, the economics of the SPCs, and the exposure under the payment guarantee. Verdict: outside the fund's circle for a moat-based grade. If it is looked at at all, it belongs only in the cheap track (grade C, at least +5 points for data verification). Even there it collides with the no-leverage rule: net bank debt was 110,348 at 30.6.2026 (§7).
9. **Why the market pays about 6.6x.** (a) The market reads it as a lender, and non-bank lenders trade at low multiples. (b) Growth stalled in 2026 and arrears rose. (c) BNPL rules and the credit-data change take effect in 2027. (d) Revenue rests on gain-on-sale and fair-value accounting with unconsolidated SPCs. (e) The two controlling holders took 21% of 2025 pre-tax profit in pay (§9). (f) The stock fell sharply in Sept-Oct 2026. Mega's market value implies about ILS 3.19 a share, against ILS 5.61 on 20.8.2026 (h1_2026 p.33; §13). No filing in the pack explains the fall: **UNVERIFIED, so check Maya immediate reports for Sept-Oct 2026.**

---

## 1. What the company sells, to whom, and how it makes money

### 1.1 The product
- The company was incorporated on 9.12.2014 as Credit Shop Ltd, renamed on 2.6.2021, and listed on TASE in October 2021. It has one segment, "payments, partly by way of consumer credit at the point of sale", under the PaymenT brand (fy2025 p.6).
- The flow works as follows (fy2025 p.7-8, p.12). The merchant's rep keys the customer's application into the PaymenT system. The system automatically identifies the customer, scores them (using the Bank of Israel credit-data system among other sources) and approves or declines within seconds. The borrower signs a digital loan agreement and, for equipment and vehicle loans, a lien. The loan money goes straight to the merchant through the bank clearing house (Masav), never to the borrower. The company then either keeps the loan on its balance sheet or assigns it by true sale to a funder, and it usually goes on servicing the loan.
- Loans are small and many: 23,498 loans averaging ILS 22,792 with a 14-month duration in 2025 (fy2025 p.42). Most loans on the balance sheet are fixed-rate and CPI-linked (fy2025 p.59, p.71).
- The verticals are aesthetics, surgical aesthetics, dentistry, home renovation, professional services, consulting, equipment and tuition (fy2025 p.40). Cars appear in earlier reports and in the FY2025 directors' report (fy2023 p.6; fy2024 p.13; fy2025 p.59). The company estimates its share in its target verticals at no more than 10% (fy2025 p.40).
- The pitch to the merchant is immediate full payment, no credit risk and higher sales. The company says merchants see sales and average tickets rise by "tens of percent" (fy2025 p.59); this is a company claim and unverified. The pitch to the consumer is instalments that do not use up credit-card limits (fy2025 p.15).

### 1.2 Who the customers are, and the contract terms
- **Merchants**, the distribution channel (fy2025 p.40-41). Agreements run for an indefinite term and **either side can cancel at any time** on written notice. Where a minimum fee applies, it remains payable for 3 months after notice. The merchant pays fixed monthly subscription fees, variable fees by financing track, and operations, clearing and discounting fees based on loan size and term. The merchant indemnifies the company for breaches and for customer claims about the underlying sale. The company states that today it is not exposed to failure of consideration or cancellations between customer and merchant (fy2025 p.41). The new BNPL circular puts this in question (section 6). Each merchant is underwritten and given automatic limits: an obligo and minimum and maximum ticket sizes (fy2025 p.9).
- **Borrowers.** These are "occasional" customers who meet the company at the point of sale. Borrowing is limited to Israeli citizens over a minimum age with an Israeli bank account (fy2025 p.10). The merchant decides whether interest and fees fall on the customer or whether it subsidises them, fully or partly (fy2025 p.15).
- **Loan buyers and funders**, which the company calls "suppliers" (fy2025 p.47). Sales are true sales without recourse. The price is the loan's cash flows discounted at a rate that splits the interest between buyer and company. **Expected default is fixed in the formula in advance, so actual defaults do not change the company's share** of a sold pool (fy2025 p.51-52; fy2024 p.48). The company keeps all the fees it charged, whatever happens to the loan afterwards (fy2025 p.13-14). Two caveats: the buyer agreements are renewed from time to time, and the pricing takes realised default rates into account (fy2025 p.35; fy2024 p.34; fy2023 p.33). Credit performance therefore feeds back into future margins.

### 1.3 Revenue streams and recognition
The company names four sources: interest; loan sales and fair-value changes; fees paid by merchants and borrowers; and operating (servicing) income (fy2025 p.39; note: fy2025 p.88).

- Fees are recognised when the transaction is completed in the system. Loan-sale income is recognised when full-sale agreements are signed. Interest and fair-value changes are recognised monthly (fy2025 p.88).
- Loans held for sale are carried at fair value through profit or loss. The marks are model-based: discount curves for "assets of similar risk", set by reference to the company's own sale transactions (h1_2026 p.32). The step-up over amortised cost was 9,515 at 30.6.2026 (h1_2026 p.31), equal to 12.1% of tangible equity (§6).
- The directors repeat every year that reported revenue is only the company's share after the buyers' share, and that expected credit losses on loans held for sale sit inside the fair-value measurement (fy2025 p.64; fy2024 p.61; fy2023 p.61; h1_2026 p.13).

**Revenue mix (§4; fy2023 p.37, fy2025 p.39, h1_2026 p.32):**

| Share of revenue | 2021 | 2022 | 2023 | 2024 | 2025 | H1 2025 | H1 2026 |
|---|---|---|---|---|---|---|---|
| Fees (platform use and loan set-up) | 52.5% | 35.5% | 31.2% | 33.8% | 48.2% | 44.9% | 55.1% |
| Loan sales + fair-value changes | 46.9% | 52.1% | 35.3% | 39.0% | 28.8% | 34.5% | 21.3% |
| (of which FV change on unsold loans) | 3.8% | 25.1% | 11.4% | n/d | n/d | n/d | n/d |
| Interest and CPI linkage | 0.6% | 10.2% | 29.2% | 26.2% | 19.7% | 17.9% | 16.7% |
| Servicing / operating income | 0.0% | 2.2% | 4.3% | 1.0% | 3.3% | 2.7% | 7.0% |

Fees grew 88% in 2025 and 41% in H1 2026, while loan-sale and fair-value revenue fell 29% in H1 2026 (§4). Management puts the H1 2026 fee growth down "mainly" to fees collected after the 360 platform was introduced (h1_2026 p.13). On the 360 product: after development ended, the company began selling merchants a product for operating and securing digital payments, which includes collection services (fy2025 p.39), "payment operations and payment guarantee" (fy2025 p.40). Its deferred income sits in "amounts payable for credit transactions" (fy2025 p.62; h1_2026 p.11), and that line grew from 5,133 (2024) to 19,273 (30.6.2026) (§9). **How much volume is guaranteed, and what losses have been suffered under the guarantee, is not disclosed: UNVERIFIED.** If 360 guarantees merchants' own instalment receivables, part of the fee growth is in effect a credit-insurance premium whose losses would arrive later.

### 1.4 Unit economics (§3, P&L divided by originations)

| Per ILS 100 originated | 2022 | 2023 | 2024 | 2025 | TTM 6/2026 |
|---|---|---|---|---|---|
| Revenue | 6.71 | 10.55 | 11.07 | 10.58 | 10.90 |
| Funding cost | 0.56 | 2.12 | 1.34 | 0.88 | 1.08 |
| Credit-loss charge | 0.18 | 0.21 | 0.32 | 0.15 | 0.18 |
| Net revenue ("gross profit") | 5.97 | 8.22 | 9.40 | 9.56 | 9.64 |
| Opex (S&M + R&D + G&A) | 3.64 | 4.52 | 4.98 | 5.11 | 5.22 |
| **Pre-tax profit** | **2.45** | **3.64** | **4.43** | **4.44** | **4.42** |
| of which fees | 2.38 | 3.30 | 3.74 | 5.10 | 5.75 |

Per loan in 2025, the company earned revenue of ILS 2,409 and pre-tax profit of ILS 1,012 on an average loan of ILS 22,792 (§3). Average loan size fell from ILS 35,327 (2023) to ILS 22,792 (2025), and duration shortened from 18 to 14 months (fy2025 p.42). The average stated borrower rate fell from 9.83% (2023) to 7.96% (2025) (fy2025 p.42), while fee income per ILS 100 rose from 3.30 to 5.10 (§3). The economic payer is moving from the borrower to the merchant: subsidised tracks and subscriptions are replacing borrower interest.

### 1.5 Recurring or one-off revenue
Every loan is a one-off transaction. There is no contracted backlog, and revenue is re-earned every month from new originations (fy2025 p.43). The recurring elements are:
- the merchant relationship (but cancellable at will);
- the fixed monthly subscription, new in the FY2025 report (fy2025 p.13, p.41);
- interest on loans while they are held;
- servicing fees on sold pools, described as "not material" (fy2025 p.12).

Cumulative loans sold since inception are "over a billion" ILS (h1_2026 p.15). The company points out that the lifetime income on its loans exceeds what it books, because buyers keep the rest of the spread (fy2025 p.64). That spread belongs to the buyers, not to Paymeant shareholders.

### 1.6 Who carries the credit risk
Sold loans transfer default risk to the buyer, with the expected-default input fixed in the price (fy2025 p.51). Paymeant still carries six kinds of exposure:
- loans held before sale, 203,167 at fair value at 30.6.2026 (h1_2026 p.23);
- loans that default before they can be sold: the defaulted balance was 4,395 at 30.6.2026, and the company says it comes from loans that defaulted before sale (h1_2026 p.15);
- representations and indemnities to the SPCs "for breaches and other cases set in the agreement" (h1_2026 p.7, p.33);
- deferred consideration paid out only as sold pools repay, held in the SPCs at about 4% (fy2025 p.108); other long-term receivables were 2,217 at 30.6.2026 (h1_2026 p.23);
- repricing of future sales when realised defaults rise (fy2025 p.35);
- the undisclosed 360 payment guarantee (section 1.3).

The SPCs, Paymeant Series 1 and Series 2, are 100% owned but **not consolidated**. Management's reasons: voting rights do not direct the relevant activities, the lenders can replace the company as servicer, and the servicing fee is at fair value (fy2025 p.93-94). This is a critical accounting judgement for the financials workstream.

---

## 2. Segment revenue and profit, 2021 to H1 2026, and why it moved

There is one segment, so segment results equal company results (fy2025 p.6, p.20).

| ILS k | 2021 | 2022 | 2023 | 2024 | 2025 | H1 2025 | H1 2026 | TTM |
|---|---|---|---|---|---|---|---|---|
| Originations (ILS m) | 146 | 356 | 365 | 389 | 535 | 240 | 258 | 553 |
| Revenue | 7,850 | 23,874 | 38,524 | 43,046 | 56,616 | 24,827 | 28,512 | 60,301 |
| Funding cost | 90 | 1,982 | 7,750 | 5,224 | 4,711 | 1,477 | 2,738 | 5,972 |
| Credit-loss charge | 0 | 653 | 758 | 1,253 | 783 | 441 | 670 | 1,012 |
| Net revenue | 7,760 | 21,239 | 30,016 | 36,569 | 51,122 | 22,909 | 25,104 | 53,317 |
| Opex | 6,244 | 12,944 | 16,516 | 19,353 | 27,350 | 12,637 | 14,144 | 28,857 |
| Other income (expense) | (2,285) | 437 | (228) | 0 | 0 | 0 | 0 | 0 |
| Pre-tax | (769) | 8,732 | 13,272 | 17,216 | 23,772 | 10,272 | 10,960 | 24,460 |
| Net income | (769) | 8,809 | 10,298 | 13,291 | 18,188 | 8,007 | 8,285 | 18,466 |
| Pre-tax / revenue | -9.8% | 36.6% | 34.5% | 40.0% | 42.0% | 41.4% | 38.4% | 40.6% |

Sources: fy2023 p.19; fy2024 p.19; fy2025 p.20, p.64; h1_2026 p.13-14. Opex (S&M + R&D + G&A), TTM and margins are from §1-§2. TTM reconciles exactly to Mega's revenue, gross profit (53,317), operating income (24,460) and net income (18,466).

**Year by year:**
- **2021, start-up and IPO year.** Originations were 146M (fy2023 p.39). Other expenses of 2,285 were IPO grants and options that vested immediately (fy2023 p.111).
- **2022, scale-up.** Originations rose 144% to 356M (§1). Profit was flattered by three items: (a) 5,998 of non-cash fair-value gains on unsold loans, 25% of revenue (fy2023 p.37); (b) other income of 1,188 when a loan buyer's engagement ended. The notes call it acquiring corporation A (fy2023 p.111), while Part A says buyer B's facility expired in April 2022 (fy2023 p.49); (c) a tax benefit of 77 in place of a tax charge (fy2023 p.19). Equity went from 22,163 to 56,186, helped by a private placement on 14.8.2022: 4,852,476 shares (13.16%) for net proceeds of about 24,167 (fy2023 p.108).
- **2023, peak rates and war.** Originations rose only 2.5% (§1). Only 40% of loans were sold during the year (fy2023 p.39), so interest income rose to 11,237. Funding cost rose 291% to 7,750, because the company carried more loans on bank lines while the Bank of Israel rate was high (fy2023 p.61). Q4 originations fell to 67M from 101M because of the war (fy2024 p.42). Net income rose only 16.9% (§1).
- **2024, recovery.** Originations rose 6.6% (§1), and 90% of loans were sold, partly through two Series 1 SPC deals of 90M and 85M (fy2025 p.107). Revenue rose 11.7%. Funding cost fell 33% on lower utilisation and better spreads (fy2024 p.61), so pre-tax profit rose 29.7% (§1). The sales force went from 4 to 17 people and the number of merchants joining rose 245% (fy2024 p.40, p.44).
- **2025, the growth year.** Originations rose 37.5% to 535M (§1), helped by the larger sales force and a soft 2024 base (fy2025 p.64). Fees nearly doubled, up 88% (§4), with the 360 product and the new subscriptions. Net revenue per ILS 100 originated reached 9.56 (§3). Opex rose 41.3% (§1). R&D rose 43% as 360 capitalisation stopped and amortisation began, and G&A rose 50%, including advisers for the assignment deals (fy2025 p.64). Net income rose 36.8% (§1).
- **H1 2026, deceleration.** Originations rose 7.5% (§1) through Operation "Roaring Lion", which brought about a week of partial economic shutdown from 28.2.2026 (h1_2026 p.29), and "a decline in turnover at some merchants" (h1_2026 p.6). Revenue rose 14.8% on fees. Funding cost rose 85% as average bank credit doubled, up 102% (§5; h1_2026 p.18). G&A rose 40% on payroll and advisers (h1_2026 p.13). Net income rose 3.5%, and Q2 net income fell 1.2% (§1).

---

## 3. Customer concentration

- **Merchants and borrowers: none.** "No dependence on any customer and no material customers" (fy2025 p.40; fy2024 p.38; fy2023 p.38), and no dependence on any single merchant or marketer (fy2025 p.43). The FY2025 report contradicts itself on scale: "thousands" of merchants on p.14 but "hundreds" on p.43. There are tens of thousands of borrowers (fy2025 p.14).
- **Vertical concentration is real but unquantified.** Aesthetics, surgical aesthetics and dentistry lead every list (fy2025 p.40; h1_2026 p.5). No split by vertical is disclosed: UNVERIFIED. These are discretionary medical and cosmetic purchases. Under the new BNPL circular the lender may be exposed when the service is not delivered (section 6).
- **The real concentration is in funding and loan buyers.** The prominent buyers in 2020-2025 were "banking corporations and a large institutional body" (fy2025 p.13). In 2020-2024 an Israeli credit-card company was also listed (fy2024 p.14); in 2026, "credit card companies" are mentioned again (h1_2026 p.17). Portfolio take-outs since mid-2023 have all gone to the company's own SPCs, financed by a banking corporation (fy2025 p.51-53; h1_2026 p.6). Section 7 has the details.

---

## 4. Backlog and its trend

The company states it has no order backlog: "all orders are recognised immediately as revenue" (fy2025 p.43; fy2024 p.41; fy2023 p.40). The useful proxies:

| Proxy | Feb-Mar 2024 | Feb-Mar 2025 | Feb 2026 | Aug 2026 |
|---|---|---|---|---|
| Stated annualised origination pace (ILS m) | ~400 (fy2023 p.5) | ~500 (fy2024 p.7) | ~640 (fy2025 p.7, p.59) | ~600 (h1_2026 p.5) |
| Loans held for sale at report date (ILS m) | ~156 (fy2023 p.56) | ~142 (fy2024 p.57) | ~187 (fy2025 p.60) | ~203 (h1_2026 p.5) |

**Delivery against stated pace (§10):** 2024 came in 2.7% below the stated 400; 2025 came in 7.0% above the stated 500. For 2026, H1 annualised is 19.4% below the stated 640, and the July 2026 pace is 6.2% below it. In the quarterly data, Q1 2026 (134M) beat Q1 2025 (127M), and Q2 2026 (124M) beat Q2 2025 (113M) by 9.7% (§10, §1). But the second half of 2025 ran at 138M and 157M a quarter, so the 600M pace implies an H2 2026 of 300M against 295M in H2 2025, only 1.7% higher (§10). Note that the FY2025 directors' report gives Q4 2025 as about 152M (fy2025 p.59), while the seasonality table gives 157M (fy2025 p.45).

---

## 5. Competition and market structure

- **Market.** Israeli consumer credit is dominated by the banks, followed by the credit-card companies and non-bank lenders (fy2025 p.23). Household credit was ILS 889.67bn in September 2025, of which ILS 85.58bn was non-bank (fy2025 p.35). Paymeant's 2025 originations equal 0.23% of the non-housing household credit stock and 0.63% of the non-bank household stock (§12). These compare an annual flow with a stock, so they show order of magnitude only. Either way, Paymeant is a niche player.
- **Direct competition.** POS credit in Israel is "not developed or widespread", and PaymenT is "one of the few dedicated systems" (fy2025 p.43). The main competitors named are banks and card companies, plus specialist lenders such as Kalmobil, the Lubinski group, Blender and the Meir group, and institutional bodies (fy2025 p.44). Competition is on price, loan terms and speed, and the company says its own share is small (fy2025 p.44). In practice the strongest substitute is the merchant's own credit-card instalment plan (fy2025 p.38). Search-engine snippets mention BNPL launches by Isracard with partners and by Blender with Bank Hapoalim; these were search-cited and not opened, so they are UNVERIFIED.
- **The company's claimed edges** (fy2025 p.44): POS know-how; tailor-made technology and instant scoring; an underwriting record trusted by banks; experienced managers; and the claim to be "the only one in Israel" combining loan sales on a monthly basis. **The weakness it names itself:** competitors' capital advantages (fy2025 p.44).
- **Direction of change.** The regulator is deliberately lowering barriers. Card companies were separated from the banks, the BoI credit-data system was built, open banking was introduced, "lean banks" and new bank licences are planned (August 2025 recommendations), and the credit-data system will be extended to corporate borrowers (fy2025 p.24-25; h1_2026 p.7). The company itself cites a BoI study showing that the credit-data system eroded the banks' information advantage (fy2025 p.24). The same erosion works against any information edge Paymeant has.
- **Entry barriers the company lists** (fy2025 p.38): technology; underwriting models and a reputation for model performance; the supervisory licence and minimum equity; BoI approval for credit-data access; POS know-how; and financial capacity. All but the track record and the balance sheet can be bought or built by a funded entrant.

---

## 6. Regulation and licences

- **Licences.** The company has held a permanent extended-credit licence under the Supervision of Financial Services (Regulated Financial Services) Law since 3.10.2021, renewed to 31.12.2028. Its subsidiary Paymeant Financing Solutions has held one since 5.11.2025, also to 31.12.2028, and started lending with the company from 1.1.2026 (fy2025 p.6, p.29; h1_2026 p.29). The company is an R&D company recognised by the Innovation Authority (4.4.2021), but has not taken grants (fy2025 p.6, p.45). It is a "qualified source" that must report to the BoI credit-data system (fy2025 p.30).
- **Price ceilings.** The Fair Credit Law caps the cost of credit on non-indexed loans. For CPI-linked loans, the Interest Order caps interest at 13% a year and default interest at 17% (fy2025 p.27-28). These ceilings are far above the company's average stated rate of 7.96% (fy2025 p.42).
- **Conduct and risk rules already in force** (fy2025 p.26-34): AML and KYC (the 2018 order), the consumer-credit circular (25.8.2021), the risk-management circular (November 2023), cyber, financial-information services (open-banking API, implemented by 14.5.2025), privacy, the cash law, and insolvency law, which can cut recoveries.
- **New in 2026, effective early 2027, and the most important for the model:**
  - **BNPL circular 2026-10-4**, published 12.7.2026 and in force from 12.1.2027 (h1_2026 p.7-8). It requires pre-contract disclosure, including that the purchase and the credit are separate transactions, and special rules above ILS 7,500 or for special populations. **It provides for cancellation of the credit transaction in certain cases, including when the asset or service is not supplied or only partly supplied.** It requires a written merchant agreement, borrower consent before the transaction, and an assessment of the merchant's reliability and financial strength. This can shift merchant non-performance risk, which the company says it does not carry today (fy2025 p.41), onto the lender. That matters for clinics in aesthetics and dentistry. The company says it is "examining" the effects (h1_2026 p.8).
  - **Credit Data Law amendment 6**, published 26.7.2026 and effective about six months later (h1_2026 p.7). Negative credit data will be kept for 1 year instead of 3, and in emergencies the commissioner may exclude negative data. This weakens the very data the instant-scoring model relies on for unknown walk-in borrowers. The company itself sees only an upside, from better data and a corporate registry.
  - **Securitisation bill**, which passed first reading on 25.5.2025. If enacted, it would widen loan-sale outlets (fy2025 p.33).

---

## 7. Supplier and funding dependencies

The company's "suppliers" are its funders (fy2025 p.47). The business cannot grow or even run without them.

- **Warehouse lines.** Four banks, total 340M, all on-call and revolving, at prime+0.5% to prime+0.8%. At 31.12.2025 the unused amounts were 100M (A), 8M (B), 39M (C) and 89M (D), so 236M unused in total, falling to 201M at the report date (fy2025 p.49, p.60). The lines are secured on the loans and dedicated bank accounts (fy2025 p.99) and carry covenants. At 30.6.2026: tangible equity 34% of the balance sheet against a 20% minimum; tangible equity 76M against 25M; senior debt 55% of loans against an 80% maximum (h1_2026 p.18). The lenders "may stop unilaterally" (fy2025 p.55). History: 280M of lines in 2023 (fy2023 p.44), 340M from 2024 after Bank D opened 100M and Bank C was cut from 80M to 40M (fy2024 p.58).
- **Loan buyers.** These are, first, banks buying flow; corporation A has bought under an agreement since 13.11.2019 with a 30-day termination right and no minimum purchase (fy2024 p.48). Second, Amitim (old pension funds in special management) bought 120M in 2022-2023 for 510,000 options in place of cash fees (fy2025 p.17, p.106). Third, since 2023 there have been portfolio sales to Series 1 and Series 2, financed by a banking corporation with security over the pools, under Shein trust services: 60M (6/2023), 90M (2/2024), 85M (9/2024), 80M (1/2025), 60M (3/2025), 84M (10/2025) and 80M (2/2026) (fy2025 p.106-108; h1_2026 p.6). Search-cited and unopened: a further ~100M portfolio assignment completed on 29.9.2026, UNVERIFIED.
- **Signs that the flow-buyer channel weakened in 2025.**
  - The cadence described changed from "daily (Over-Night)" (fy2023 p.38, p.55) to "weekly" (fy2024 p.42, p.57) to "monthly" (fy2025 p.44, p.59), and back to "weekly" in 2026 (h1_2026 p.17).
  - Corporation A's row disappears from the FY2025 buyer table (fy2025 p.51-53 against fy2024 p.48).
  - The sold share fell from 90% to 60% (fy2025 p.42).
  - Implied non-portfolio sales fell from about 175M (2024) to about 97M (2025) (§7). This last figure is a derived estimate, labelled as an inference.
  - The 2025 plan to sell about 300M to Series 1 (fy2024 p.50) produced 144M with Series 1, 48% of plan (§7), plus 80M with Series 2 (fy2025 p.107-108).

  Taken together this suggests take-outs are now concentrated in the bank that finances the SPCs. **The identity of that bank and the SPC loan terms are not disclosed: UNVERIFIED.** The company denies any dependence on a single buyer (fy2025 p.47).
- **Data and technology.** Access to the BoI credit-data system is essential (fy2025 p.16, p.38). The platform is built and run in-house, and its databases are not exposed to third parties such as suppliers (fy2025 p.9).

---

## 8. Employees

| Year-end | 2021 | 2022 | 2023 | 2024 | 2025 | Feb 2026 |
|---|---|---|---|---|---|---|
| Staff | 14 | 25 | 25 | 45 | 55 | 52 |
| of which sales and marketing | 4 | 5 | 4 | 17 | 20 | 18 |

Sources: fy2023 p.43; fy2024 p.44; fy2025 p.46. Revenue per average employee was 1,541k (2023) and 1,132k (2025), and pre-tax profit per average employee 531k and 475k (§9). The 2024-2025 hiring went into sales and account managers, as part of a strategy "to significantly increase the number of merchants" (fy2025 p.64).

The business is people-light but depends on its two founders and controlling holders, CEO Yaniv Gilor and CTO Guy Yochanan. Each cost 2,484k in 2025: salary 1,524k, bonus 750k and share-based pay 210k. Together they cost 4,968k, or 21% of 2025 pre-tax profit; the top five cost 8,152k, or 34% (fy2025 p.118; §9). Their terms were raised again by the general meeting of 30.3.2026 (h1_2026 p.19). Pay and governance belong to the governance workstream; they are noted here because they absorb a large share of the operating profit.

---

## 9. Seasonality

The company calls itself non-seasonal, apart from the holidays: fewer working days lower originations, which recover in the months after (fy2025 p.44). In practice Q4 was the strongest quarter in 2022, 2024 and 2025, at 28-29% of the year (§10; fy2024 p.42; fy2025 p.45). Q4 2023 was the exception: 67M, or 18%, because of the war. Wars and emergencies (October 2023, February-March 2026) are a bigger swing factor than the calendar.

---

## 10. Strategy across the 2023, 2024 and 2025 reports, and delivery

The strategy text is largely boilerplate, identical from year to year: accelerate non-bank and POS lending, enter adjacent sectors, add services, diversify and cheapen funding through a "combined model" of assignment, balance-sheet holding and portfolio sales, and invest in R&D (fy2023 p.50; fy2024 p.52; fy2025 p.54). What changed:

| Theme | FY2023 report (Mar 2024) | FY2024 report (Mar 2025) | FY2025 report (Feb 2026) | Delivered? |
|---|---|---|---|---|
| Origination pace | ~400M for 2024 (p.5) | ~500M for 2025 (p.7) | ~640M for 2026 (p.7) | 389M (-2.7%); 535M (+7.0%); H1 2026 annualised 516M, July pace 600M (§10) |
| Cars | New car-dealer products (p.6); a used-car finance marketplace in a "~25bn ILS" market (p.37-38) | Car still a vertical (p.13, p.39); marketplace no longer mentioned | Car dropped from the main vertical list (p.40), still named in the directors' report (p.59) | The marketplace was abandoned quietly, never reported as a failure |
| New lines | E-commerce, renewable energy, payment services (p.37-38, p.51) | E-commerce, private-party sales, payment-operations services (p.38) | 360 operations and payment guarantee launched; cash-flow suite (B2B advance, working capital, card clearing, voucher discounting) (p.39-40) | 360 delivered and is the main fee driver (h1_2026 p.13). E-commerce has been "developed" for three years with no disclosed revenue. Renewable energy dropped |
| Pricing | Fees proportional to the ticket, "no fixed fee or cost to the merchant" (p.12) | Same (p.13) | Fixed monthly subscription added (p.13, p.41) | Fees +88% in 2025 (§4) |
| Funding | Lines of 280M (p.44); daily flow sales | Lines of 340M (p.45); weekly; ~300M Series 1 planned for 2025 (p.50) | Lines of 340M (p.47); monthly; a new licensed subsidiary (p.4) | Series 1 2025 came to 144M against ~300M planned, 48% of plan (§7); sold share fell to 60% (fy2025 p.42) |
| Sales force | 4 people (p.43) | 17 people (p.44) | 20 people (p.46) | Merchants joining +245% (2024) and +54% (2025) (fy2025 p.42) |
| R&D | 8,633 spent (fy2025 p.45) | 2025 plan ~9.5M (p.43) | Spent 10,754; 2026 plan ~10M (p.45) | Spent more than planned (10,754 against ~9.5M) |
| Capital return | Dividends of 6M in 2023 (p.17) | 7M (2024); buyback of up to 5M approved 13.11.2024 | ≥30% payout policy from 16.2.2025 (p.18); 9M paid in 2025 | Payout 49-58% of net income (§9); **buyback unused** as of the reports (fy2025 p.69) |

**Delivery verdict.** Management delivered in 2025 (origination growth, the 360 product, fees) and paid steady dividends. But it quietly dropped the projects it once called highly feasible (the car marketplace, renewable energy), missed its own 2025 Series 1 sale plan by half, and its 2026 pace statement already looks optimistic. Candour is average: the reports never explain why the flow buyer's cadence changed, or why the sold share fell.

---

## 11. Moat: source, durability, evidence

**Sources claimed** (fy2025 p.16, p.37-38, p.44, p.59): proprietary underwriting and scoring with a record of about 1% defaults on "occasional" borrowers, "verified" by the buyers (fy2025 p.60); POS integration and automatic merchant onboarding; the trust of banks and a large institutional body (more than ILS 1bn sold, h1_2026 p.15); licences and access to the BoI data system; a brand in niche verticals.

**Evidence in the numbers:**
- **Returns** (§6). ROE was 22.5% (2022, distorted by the 2022 placement), 17.5% (2023), 20.5% (2024), 24.2% (2025) and 22.6% (TTM). RoTE was 19.3%, 23.2%, 26.9% and 25.0% (TTM); pre-tax RoTE was 24.9%, 30.0%, 35.2% and 33.2%. These are above the 10% hurdle, but they are a lender's returns, earned with equity at 33-41% of assets in 2023 to June 2026 (§7), plus off-balance-sheet SPC funding, in a benign credit period.
- **Margins** (§3). Net revenue per ILS 100 originated rose from 5.97 to 9.64, and pre-tax from 2.45 to 4.42. Funding cost per ILS 100 fell from its 2023 peak of 2.12 to 1.08. The gains came from a richer fee mix (merchant-paid) and falling rates, not from a structural cost advantage: opex per ILS 100 rose from 3.64 to 5.22 (§3).
- **Pricing power** is mixed. The average stated borrower rate fell 187 basis points between 2023 and 2025 (fy2025 p.42; §10), while fees per ILS 100 rose (§3). The company can charge merchants more, which suggests real value to a clinic closing a sale. But it cannot hold borrower pricing, and merchants can leave at any time (fy2025 p.41).
- **Growth needs capital** (§7). At 2025 ratios, every additional ILS 100m of annual originations ties up about ILS 15.4m of equity: 35% of a year's originations are held at any time, and 44% of that is equity-funded. Growth is therefore not capital-light. The roughly 50% payout (§9) is affordable only while the take-out channels hold.

**Durability.**
- Against: switching costs are low; nothing is patented (fy2025 p.45); the credit data is shared across the industry and becomes thinner from 2027; licences are standard; banks and card issuers have larger balance sheets and their own instalment products (fy2025 p.38, p.44); the regulator is actively adding competitors (fy2025 p.24-25); the BNPL circular raises compliance costs and may shift merchant risk to lenders (h1_2026 p.7-8).
- For: years of proprietary loss data in niche verticals, a merchant network, and a sale-and-service machine that banks already use.

**Verdict.** At best a narrow, process-based edge, not a Buffett-type moat. The castle has existed for about four profitable years (2022-TTM) without a full credit cycle (§1). The $1bn test fails easily: a bank or card issuer that decided to subsidise POS credit for clinics could take the merchants, because the agreements are cancellable and the merchant cares about price and approval rates. The best plain description is a well-run specialty-finance originator whose profits depend on funding markets and credit conditions it does not control.

---

## 12. Is TTM-to-June-2026 earnings power representative?

**Clean of one-offs?** Largely yes. Other income is nil and the effective tax rate is 24.5% (§2). The fair-value step-up in TTM revenue is 1,216 (§11). 2022 is the year that was flattered: 5,998 of fair-value gains, 1,188 of termination income, and a tax benefit (section 2).

**Signs that TTM is at the top of the range rather than mid-cycle (§3, §8, §11):**
- The pre-tax margin on originations is 4.42% TTM, against 2.45% (2022), 3.64% (2023), 4.43% (2024) and 4.44% (2025). The 2022-2025 average is 3.74% and the 2023-2025 average 4.17%. Excluding the unrealised fair-value step-up, TTM is 4.20% against a 2023-2025 average of 3.88%.
- The credit-loss charge is only 0.18% of originations TTM, while arrears in the pre-sale book rose. Days past due plus default were 1.43% (end-2024), 2.65% (end-2025) and 4.57% (30.6.2026). The defaulted balance nearly tripled in six months, from 1,481 to 4,395 (fy2025 p.66; h1_2026 p.15). The company calls the rise "negligible" (h1_2026 p.15).
- Fees, now 55% of revenue, partly come from the 360 payment guarantee. Its premiums are booked now; losses, if any, come later and are not disclosed (section 1.3).
- Momentum has faded: the pace fell from 640M to 600M, Q2 net income fell 1.2%, and arrears are rising, all while the Bank of Israel was cutting rates (h1_2026 p.9).

**Factors that make TTM look depressed:** the February-March 2026 war week (h1_2026 p.29); falling Bank of Israel rates (3.5% at August 2026, h1_2026 p.9), which cut funding cost and raise sale prices (fy2025 p.72); and continued investment in sales and R&D.

**War-related demand?** No evidence of it. Wars reduced originations (Q4 2023; H1 2026) and did not raise them (fy2024 p.42; h1_2026 p.15).

**Normalised earnings, for the valuation workstream (§11):**

| Scenario | Pre-tax margin on originations | Originations (ILS m) | Pre-tax (ILS k) | Net at 23% (ILS k) | vs TTM net 18,466 |
|---|---|---|---|---|---|
| Bear: credit and regulation bite, flat-to-down volumes | 2.45% (2022, lowest year) | 500 | 12,264 | 9,443 | -49% |
| **Base: through-cycle** | **3.74% (2022-25 average)** | **553 (TTM)** | **20,679** | **15,923** | **-14%** |
| Bull: TTM economics hold at the July 2026 pace | 4.42% (TTM) | 600 | 26,539 | 20,435 | +11% |

Why this base: it is the average of all profitable years, including one stress year (2023: peak rates and war) and one flattered year (2022). It sits close to the 2023-2025 average excluding fair-value marks (3.88%, §11). It is applied to volume already achieved, not to the guided pace. The 23% statutory rate comes from fy2025 p.106. Two caveats for owner earnings, which other workstreams compute:
- growth consumes equity (section 11);
- D&A (3,194 in 2025) now exceeds capitalised development (1,279) (§9), so maintenance capex looks covered, but capitalised development was larger than D&A in 2022-2024 (§9).

---

## 13. Inversion: what would kill it

1. **Take-out failure.** The SPC bank or the flow buyers stop buying or reprice after defaults rise. The company must then hold loans on 340M of on-call lines with a 20% tangible-equity covenant, so originations shrink and the fair-value marks fall (fy2025 p.49, p.55, p.68).
2. **A credit turn in discretionary medical and cosmetic spending,** together with thinner negative data from 2027 (h1_2026 p.7). Buyers reprice, and the 360 guarantee pays out.
3. **The BNPL circular making the lender answer for merchant non-delivery** (h1_2026 p.8). One failed clinic chain financed through Paymeant would show the exposure.
4. **A bank or card issuer bundling subsidised POS credit for clinics.** Merchants can leave at any time (fy2025 p.41).
5. **Accounting.** A reassessment that consolidates the SPCs, or a mark-down of loans held for sale. The step-up equals 12.1% of tangible equity (§6).
6. **Key people.** The business depends on the two founder-controllers (fy2025 p.118).

---

## 14. Circle-of-competence verdict

- **Can an outside owner understand it?** Yes, in outline. A merchant-sourced instalment lender, paid mostly by merchant fees, earns a spread on loans it sells to banks.
- **Can an outside owner predict it 5-10 years out?** No.
  - Volumes depend on bank appetite and on licences and rules that change every year (h1_2026 p.7-8).
  - Margins depend on rates and fair-value discount curves (fy2025 p.72).
  - Credit has not been tested through a recession; the ~1% default figure is a company statement, and pool loss data are not published.
  - The SPC terms, the identity of the SPC bank and the 360 guarantee exposure are not disclosed.
  - The company reports with reduced disclosure (fy2025 p.58).

Several key figures are therefore **unverifiable**. On the fund's rules this is **TOO_HARD as a moat or compounder case**. If the CIO wants it valued at all, it belongs only in the cheap track: grade C, valued on the base normalised earnings above, with at least +5 points of extra margin for data verification and possibly governance. Even then, the cheap track requires no net debt, and the company runs net bank debt of 110,348 against its loan warehouse at 30.6.2026 (§7; h1_2026 p.23). That conflict with rule 4 needs an explicit CIO decision. My view is that self-liquidating warehouse debt is still debt that can force a sale of assets when the take-out window shuts.

---

## 15. Open items and UNVERIFIED (hand-offs)

1. **The September-October 2026 share-price fall.** Mega's market value implies about ILS 3.19 a share (§13; share count at 31.12.2025, fy2025 p.108) against ILS 5.61 on 20.8.2026 (h1_2026 p.33). Search snippets, not opened, mutually inconsistent and UNVERIFIED, put the stock at 399.8 agorot on 22.10 and 324.9 agorot on 30.10; one source shows a one-day fall of about 18.6% around 28.10. Check Maya immediate reports for the cause: buyer or bank news, the Q3 trading update, regulation, controller sales.
2. **The 360 payment guarantee:** guaranteed volume, loss experience, and how revenue is recognised.
3. **The SPCs:** identity of the financing bank, advance rate, waterfall, who gets the excess spread, the indemnity triggers, and the deferred-consideration mechanics (fy2025 p.93-94, p.108).
4. **Whether flow-buyer corporation A is still active** after its absence from the FY2025 buyer table.
5. **A split of originations and arrears by vertical.**
6. **Search-cited, not opened:** the ~100M portfolio sale completed on 29.9.2026, and the competitor BNPL launches (Isracard, Blender with Hapoalim).

**Search-cited URLs (not opened; network blocks on stockanalysis.com and bizportal.co.il):**
- https://www.bizportal.co.il/capitalmarket/quote/generalview/1180876
- https://www.globes.co.il/portal/instrument.aspx?instrumentid=370226&mode=reports
- https://www.investing.com/equities/payment-financial-technologies-advanced-chart
- https://www.bizportal.co.il/capitalmarket/news/article/797516
- https://en.globes.co.il/en/article-1001383752
