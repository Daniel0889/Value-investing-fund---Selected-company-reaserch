# Paymeant Financial Technologies Ltd (TASE 1180876): governance, capital allocation and risk

Prepared 3.11.2026 for the Rev 4 study. Sources are the company's own filings:
`paymeant_fy2023`, `paymeant_fy2024`, `paymeant_fy2025` (annual reports) and `paymeant_h1_2026` (Q2 2026 report).
Page numbers are PDF page indexes (p.1 = first PDF page). Table figures were checked against the PDF page image.
Units: ILS thousands ("k") unless stated; "M" = ILS millions; per-share figures in ILS (1 ILS = 100 agorot).
Every derived figure (sums, ratios, percentages) comes from
`work/paymeant/governance_calc.py`; its full output is in `work/paymeant/governance_calc_output.txt`.
Items taken from web-search summaries (sites not opened) are marked **UNVERIFIED**. Figures in the bottom line are repeated
from the sections below, which give their sources.

---

## 0. Bottom line

1. **Control.** Two founders, Yaniv Gilor (CEO) and Guy Yochanan (CTO), control the company with
   33.68% of the capital (31.82% after shares they hold for another shareholder), bound by a voting
   agreement that lasts while they hold more than 25% together. They are the only independent signatories.
   No pledge of their shares is disclosed. Minority shareholders are not powerless: on 23.12.2025 the general meeting
   rejected a second grant of 500,000 options to each founder.
2. **Pay.** In 2025 the two founders cost 4,968k (20.9% of pre-tax profit; 12.5% of the market value of their own
   stake at today's price). Their bonus is an uncapped share of pre-tax profit, including unrealised fair-value
   gains, with quarterly advances. Salaries rose 19.6% from 2026, and in January 2025 each founder received
   500,000 options struck about 6% below the market price.
3. **Related parties.** The only Reg. 22 transactions are the founders' employment terms, D&O
   indemnity/insurance and an undescribed June 2023 agreement with both founders. That agreement was approved under
   the relief regulations without a shareholder vote, on the day they sold 1M shares off-exchange. The economically
   important related entities are the company's own wholly owned but **unconsolidated** SPCs, Paymeant Series 1 and
   Series 2. They have bought 539M of loans since June 2023. The company services those loans, gives indemnities and
   holds deferred consideration of 4,915k (6.0% of equity) in them.
4. **Capital allocation.** The company raised about 47.6M of equity in 2021-2025 (IPO at 2.90 per unit; 2022
   placement at 5.05), paid 28.0M of dividends from March 2023 to September 2026 (payout of 49.5-58.3% of annual profit) and
   bought back nothing under a 5M plan that runs to 18.11.2026. It made no acquisitions. Cash has been run down
   to 4.9M; equity funds the loan warehouse. The founders sold 2M shares in 2023-2024 at 3.25-3.85, 24-36% below
   what institutions paid in 2022.
5. **The binding risk is funding, not governance.** At 30.6.2026 the company had 115.2M of short-term bank credit
   (1.33x equity; net bank debt 110.3M). These are on-call lines that the banks can cut unilaterally, secured on the
   loans and carrying change-of-control clauses. At 31.12.2025 a single bank (B) supplied 88.5% of the drawn credit.
   Under fund rule 4 this is debt that could force a sale of assets.
6. **Credit is turning.** On the balance sheet, defaults rose from 0.8% of loans (31.12.2025) to 2.1% (30.6.2026),
   2.97 times as much in six months. Loans 1-90 days past due rose 44.8%. Management still calls the change "negligible".
7. **Candour is mixed.** There are no emphasis-of-matter or going-concern paragraphs, no litigation and quarterly
   reporting was kept voluntarily. Against that: inconsistent covenant figures, unexplained pay items, a 2023
   dividend above a bank cap with no disclosed waiver, an assignment model described as "daily", then "weekly",
   then "monthly", and an external buyer that has dropped out of the buyer table.
8. **Market event (UNVERIFIED).** A news summary reports a fall of more than 40% in one week. The date is not shown;
   a quoted price of about 5.00 on 1.10.2026 and today's snapshot suggest October 2026. The company answered the exchange that it knew of no unusual event. The Mega snapshot implies about 3.19
   ILS a share, 43% below the 5.61 used for the 20.8.2026 option grant.
9. **Implication for the Rev 4 rules.** On governance and data alone this is investable with an extra margin of
   about 5 points (controlling holders, small-corporation disclosure reliefs, SPC exposure not quantified). The
   funding structure and the credit trend are what the grade and the verdict will turn on (section 13).

---

## 1. Who controls the company and how

### 1.1 Holdings of the controlling holders

| Date (report) | Gilor | Yochanan | Together | Source |
|---|---|---|---|---|
| FY2023 report (25.2.2024) | 20.77% | 14.84% | 35.61% | fy2023 p.117 |
| FY2024 report (16.2.2025) | 20.67% (19.17% fully diluted) | 14.78% (13.70% FD) | 35.45% | fy2024 p.118 |
| FY2025 report (22.2.2026) | 19.64% (19.72% FD) | 14.04% (14.44% FD) | 33.68% (34.16% FD) | fy2025 p.118 |
| FY2025, net of shares held for another holder | 18.71% (18.85% FD) | 13.11% (13.56% FD) | **31.82%** (32.41% FD) | fy2025 p.118 fn 2-3 |
| TheMarker holder list, 24.6.2026 | 18.51% | 12.91% | 31.42% (governance_calc §10) | search summary, **UNVERIFIED** |

- **Nominee holding.** "Part of the shares held by Mr. Gilor [and by Mr. Yochanan] are held for the benefit of another
  shareholder" (fy2025 p.118 fn 2-3). Together that is 1.86% of the capital, about 729,958 shares (governance_calc §1). The other holder is not named.
  The disclosure first appears in FY2025, so the earlier holding percentages (2023-2024) probably include these
  shares.
- **Voting agreement.** The founders have a shareholders' agreement covering the appointment of directors and voting at
  general meetings. It runs indefinitely from the IPO "as long as the parties hold together more than 25%" of the issued
  capital (fy2025 p.123; fy2024 p.122; fy2023 p.121 refers to prospectus §3.6.2). Their headroom above 25% is
  6.82 points, about 2.68M shares (governance_calc §1).
- **Pledges.** None disclosed. Reg. 21A mentions only the shareholders' agreement (fy2025 p.123). The Reg. 24 holdings
  report is incorporated by reference (immediate report 2026-01-003679) and was not available to us: **UNVERIFIED**.
- **Signatories.** The two founders are the company's only independent authorised signatories (fy2025 p.130).
- **Board control.** Both founders sit on the board. The chairman (Shimon Hadad, since 18.11.2025) and director Sarah Gani are
  classed as not independent. The only independent members are the two statutory external directors (section 2).
- **Change-of-control lock.** All bank credit-line agreements restrict changes of control and of line of business,
  with standard acceleration triggers (fy2025 p.99). In practice, a sale of control needs the banks' consent.
- **Outside pressure on control.** The founders together hold about 32% net. That is effective control in a dispersed
  register, but not a majority. Their own pay needs a special majority of the disinterested shareholders, which failed
  on 23.12.2025 (section 3.3).

### 1.2 Interested-party and insider block trades (off-exchange unless stated)

| Date | Party | Trade | Price (agorot) | Source |
|---|---|---|---|---|
| 5.1.2023 | Alon Gonen (became interested party) / Shalom Bar Chen | +200,000 / -200,000 | 300.3 | fy2023 p.17, p.57 |
| 27.6.2023 | Gilor; Yochanan -> Alon Gonen | -500,000 each; +1,000,000 | 324.67 | fy2023 p.17 |
| 9.1.2024 | Gilor; Yochanan -> Udi Dor (became interested party) | -500,000 each; +1,000,000 | 385 | fy2023 p.17, p.57 |
| 11-19.8.2025 | Uri Shoker (chairman to 15.9.2025), on exchange | -149,810 | ~426.94 avg | fy2025 p.17-18 |
| 24.12.2025 | Alon Gonen | +1,581,844 | 498 | fy2025 p.17 |
| 6.1.2026 | Alon Gonen | -1,170,000 | 525 | fy2025 p.17 |

- The founders sold 2.0M shares for 7.10M ILS, an average of 3.55 ILS. That was 35.7% (June 2023) and 23.8%
  (January 2024) below the 5.05 ILS institutions paid in the August 2022 placement (governance_calc §1, §3).
- On 1.3.2022 the founders exercised about 985,000 pre-IPO options for a total of 10k ILS, i.e. 0.01 ILS a share
  (fy2023 p.107).
- Other holders: the August 2022 placement went to "first schedule" (institutional) investors and made up 13.16% of the
  capital (fy2023 p.115, p.108). A search summary says the placement was led by Mor (**UNVERIFIED**). Their current
  holdings are not in our documents.

---

## 2. Board, committees, controls and auditors

### 2.1 Board at the FY2025 report date (fy2025 p.125-128)

| Director | Role | Independent / external | Committees | Since |
|---|---|---|---|---|
| Yaniv Gilor | CEO, controlling holder | No | none | 9.12.2014 |
| Guy Yochanan | CTO, controlling holder | No | none | 9.12.2014 |
| Shimon Hadad | Chairman (ex-CEO Shufersal Finance to 10.2025; ex-Isracard SVP) | No | none | 18.11.2025 |
| Nadav Arzuan | External director (second term from 15.1.2025) | Yes | audit, compensation | 16.1.2022 |
| Liat Zmora | External director, CPA (second term from 15.1.2025) | Yes | audit, compensation | 16.1.2022 |
| Sarah Gani | Director, accounting expertise | No | none | 25.4.2022 |

- The company **did not adopt** the Companies Law provision on a minimum share of independent directors
  (fy2025 p.74). The required minimum number of directors with accounting expertise was set at 1 (fy2025 p.74).
- Committee seats are shown only for the two external directors (fy2025 p.126). An audit committee needs at least
  three members, so either the table is incomplete or the committee composition needs checking (**UNVERIFIED**).
- Chair history: Uri Shoker chaired from 1.11.2020 to 15.9.2025. He worked 20% of full time for a fee of up to 20k a
  month, plus a one-off bonus of up to 200k for raising credit lines (45M = 100% of target) (fy2024 p.122; fy2023 p.120).
  In 2021-2022 he received 123,100 options at 0.01 and 26,810 at 0.3, all vested at grant (fy2023 p.120). The
  chair was vacant from 15.9.2025 to 18.11.2025. Hadad receives 60k a year for 10% of full time plus meeting fees
  (fy2025 p.122). The FY2025 report dates his start and his general-meeting approval in **2026** instead of
  2025, a typo (fy2025 p.122, checked on the PDF image).

### 2.2 Internal control, internal audit, external audit

- **No ICFR report.** The board and management do not attach an internal-control effectiveness report, relying on the
  small-corporation relief (Reg. 5D(4); fy2025 p.117; fy2024 p.117; fy2023 p.114). The board adopted all
  small-corporation reliefs on 26.8.2021 except the relief on reporting frequency: it still reports quarterly
  (fy2025 p.58). It uses all Tech-Elite reliefs except comparatives (fy2025 p.58). In quarterly reports a short
  "main developments" report signed by the chairman and CEO replaces the directors' report (h1_2026 p.5).
- **Internal auditor.** Nir Gimpelvich (Leon Orlitzky & Co.), in office since 25.4.2022. He **reports organisationally to the
  CEO**, who is a controlling holder (fy2025 p.75). Hours and fees: 215 h / 47k (2022), 200 h / 44k (2023), 200 h / 44k
  (2024), 280 h / 61.6k (2025) (fy2023 p.74; fy2024 p.74; fy2025 p.75). He examined no material transactions in any year
  (fy2025 p.75; fy2024 p.74; fy2023 p.74). The audit committee discussed his reports on 4.5.2023 and 17.1.2024 (for
  2023), on 17.1, 25.8 and 10.12.2024 (for 2024), and only on 16.11.2025 (for 2025) (fy2023 p.74; fy2024 p.74; fy2025 p.76).
  That is a thin internal-audit effort for a licensed lender originating 535M a year.
- **External auditor.** Kost Forer Gabbay & Kasierer (EY Israel). Fees: 230k (2022), 280k (2023), 370k (2024, of which 90k
  tax), 280k (2025) (fy2023 p.75; fy2024 p.75; fy2025 p.77). The FY2025 engagement partner is Nir Mordechai (fy2025 p.81).
- **Audit opinions.** All three opinions are unqualified, **with no emphasis-of-matter paragraph and no going-concern
  doubt**. The one key audit matter each year is the fair-value measurement of loans held for sale (156M at
  31.12.2023, 142M at 31.12.2024, 186M at 31.12.2025): unobservable discount rates and wide management judgement
  (fy2023 p.79-80; fy2024 p.78-79; fy2025 p.79-81). The H1 2026 review report is clean (h1_2026 p.22).
- **D&O insurance.** Cover is US$5M per claim and per year, including for the controlling holders. The premium fell from
  US$29.15k (2022 policy) to 21.5k (2023), 13.85k (2024) and 11.8k (policy to 13.10.2026); the deductible is US$10k-35k
  (fy2023 p.128; fy2024 p.130; fy2025 p.132, p.61). Officers, controlling holders included, hold indemnity and
  exemption letters as set out in the 2021 prospectus §8.3 (not supplied).
- **Policies.** The company has no donations policy (fy2025 p.74).

---

## 3. Pay of the top officers versus profit

### 3.1 Reg. 21 tables (cost to the company, ILS k)

| Officer | 2023 (fy2023 p.117) | 2024 (fy2024 p.118) | 2025 (fy2025 p.118) |
|---|---|---|---|
| Gilor, CEO | 2,324 = salary 1,327 + bonus 520 + **other 477** | 1,978 = 1,368 + 610 | 2,484 = 1,524 + 750 + options 210 |
| Yochanan, CTO | 2,324 (same split) | 1,978 (same) | 2,484 (same) |
| Oz Gabai, VP sales | 1,052 | 1,346 (incl. RSU 252) | 1,451 (incl. bonus 280, options 78) |
| Daniel Mastorov, CFO | 614 | 1,135 (incl. RSU 336) | 961 (incl. bonus 200, options 98) |
| Chair Shoker / VP R&D Yeshua | Shoker 201 | Shoker 180 | Yeshua 772 |

Ratios (governance_calc §2):

| | 2023 | 2024 | 2025 |
|---|---|---|---|
| Founders' combined pay | 4,648 | 3,956 | 4,968 |
| ... as % of pre-tax profit | 35.0% | 23.0% | 20.9% |
| ... as % of net income | 45.1% | 29.8% | 27.3% |
| ... as % of pre-tax profit before founders' pay | 25.9% | 18.7% | 17.3% |
| Top-5 pay as % of pre-tax profit | 49.1% | 38.4% | 34.3% |
| Founders' cost incl. pay capitalised to intangibles (RP note) | 4,648 | 4,707 | 5,040 |

Pre-tax profit: 13,272 / 17,216 / 23,772; net income: 10,298 / 13,291 / 18,188 (fy2025 p.106, p.113). The
related-party note shows founders' pay was also **capitalised into development costs**: 1,812 (2021), 910 (2022), 1,363 (2023),
751 (2024) and 500 (2025) (fy2023 p.112; fy2025 p.115). Part of their pay therefore never passes through the P&L
when paid, but returns later as amortisation.

### 3.2 Terms of the controlling holders (fy2025 p.119-121)

- **Salary.** Base 80k a month each, CPI-linked from September 2021, about 92k at the report date. Gilor's salary
  is paid to a company he wholly owns, against invoices (fy2025 p.119 fn 6). On 22.2.2026 the board approved
  110k each, CPI-linked from January 2026 (fy2025 p.119-120), and the general meeting approved the update on 30.3.2026
  (h1_2026 p.19). The rise is 19.6%, about 432k a year gross for the two (governance_calc §2). Final terms were in the 26.2.2026 notice,
  which was not supplied.
- **Bonus.** 4% of pre-tax profit up to 10M, 3% of 10-20M and 2.5% above 20M, with a floor of 3 monthly
  salaries once profit exceeds about 1M. It has **no cap** and is **paid in quarterly advances** based on management
  accounts, trued up on the audited accounts. On audited pre-tax profit the formula gives 498 / 616 / 794 for
  2023-2025, against roughly 520 / 610 / 750 reported, so it is applied roughly as written. The bonus is driven by
  pre-tax profit, which includes unrealised fair-value gains on loans held for sale (section 9.3); it is not tied to
  per-share results or returns on capital.
- **Other terms.** Indefinite term, 90 days' notice, 6-month non-compete on full pay, car and phone.
- **Options, January 2025.** The general meeting of 15.1.2025 approved 500,000 options to each founder at a strike of
  3.01 against a price of 3.19 the day before the board decision, i.e. 5.6% in the money. They vest quarterly from
  10.3.2027 to 10.12.2028, and each tranche expires one year after vesting (fy2025 p.120, p.111, p.130). Fair value
  is 1.24-1.54M for the 1,000,000 options, measured with 47.23% volatility (fy2025 p.111). The same meeting
  amended the compensation policy, including "the minimum exercise price for options granted to officers"
  (fy2025 p.61).
- **Second option request rejected.** On 23.12.2025 the general meeting **did not approve** another 500,000 options for
  each founder (fy2025 p.131). The founders had asked for 2M options in 12 months; the disinterested majority refused.

### 3.3 Other officers and directors

- In February 2024 Gabai received 75k RSUs and Mastorov 100k RSUs, convertible quarterly from 1.4.2026 (fy2024 p.121;
  fy2023 p.113). In April 2025 they received 75k and 50k options inside a 519,000-option grant at 3.97 (fy2025 p.111,
  p.121-122). Discretionary bonuses for 2025 were Gabai 385k and Mastorov 275k, approved 22.2.2026 (fy2025 p.122). On
  20.5.2024 annual bonuses of four monthly salaries were approved for officers for 2023 (fy2025 p.112).
- On 20.8.2026, 512,000 options at a strike of 5.74 went to five officers and employees. The share price was 5.61 and
  volatility was set at 127.54%, giving a fair value of 3.85-4.64 per option, 1.97-2.38M in total (h1_2026 p.6, p.33).
- Potential dilution from options and RSUs is 2,876,875 shares, 7.3% of the 39,245,034 shares. The note-17
  option count (2,189,875) and the Reg. 24A count (1,136,125) differ by 1,053,750 without explanation (fy2025 p.112,
  p.123).
- **Directors' fees are unexplained.** The related-party note shows 885k for directors not employed by the company in
  2025, against 331k in 2024 and 340k in 2023 (fy2025 p.115). Part D accounts for only 136k for the three
  non-executive directors (fy2025 p.122), plus Shoker's fee and possible one-off and Hadad's pro-rated fee. That is at most
  about 513k, which leaves at least 372k unexplained (governance_calc §2).
- The **2023 "other" of 477k per founder** (954k for the two, governance_calc §10) is not explained anywhere in the FY2023 report
  (fy2023 p.117). Note 19e shows 228k of "IPO grant to senior officers and share-based payment" in 2023
  (fy2023 p.111), and the directors' report calls the IPO grant a one-off paid to the founders (fy2023 p.65).

**Assessment.** The pay level is high for a company earning about 18M net, but not extreme by TASE small-cap
standards. The structure is the problem: an uncapped share of accounting profit, paid quarterly in advance, plus in-the-money
options and a 20% raise in the same year the founders asked for a second option grant. The minority veto shows the check
works.

---

## 4. Related-party transactions (Reg. 22) and their economics

| # | Transaction | Economics | Source |
|---|---|---|---|
| 1 | CEO employment (controlling holder), paid through his own company | See section 3; about 2.5M in 2025; +19.6% salary from 2026 | fy2025 p.119-120, p.123 |
| 2 | CTO employment (controlling holder) | Same terms as the CEO | fy2025 p.120-121, p.123 |
| 3 | Agreement with both founders approved 27.6.2023 by the compensation committee and board under Relief Regulations reg. 1B(a)(2), **without a general-meeting vote** | **Terms not described** in any periodic report; reference only to immediate report 2023-01-060154. It was approved the day the founders sold 1M shares to Alon Gonen at 3.2467. The relief route is, as we understand it, for transactions the committee and board find solely beneficial to the company (**UNVERIFIED**) | fy2023 p.57, p.121; fy2024 p.123 |
| 4 | Indemnity, exemption and D&O insurance, including the controlling holders | US$5M cover; premium US$11.8k | fy2025 p.132 |
| 5 | Pre-IPO related-party funding (2021) | Repaid 3,909k of loans and capital notes from related parties in 2021; related-party interest 24k; equity reserve from a transaction with the controlling holder 185k (170k before 2021 plus a 15k capital benefit in 2021). Nothing after 2021 | fy2023 p.84, p.83, p.111-112 |
| 6 | IPO grant to the founders (2021-2023) | 288k (2021), 751k (2022), 228k (2023), shown with share-based payment in "other expenses", plus 1,997k of options that vested immediately in 2021 | fy2023 p.111, p.65 |
| 7 | Founders' option exercise, 1.3.2022 | 985,000 shares for 10k in total | fy2023 p.107 |
| 8 | **Wholly owned, unconsolidated SPCs** (Paymeant Series 1 Ltd, Paymeant Technologies Series 2 Ltd), with trustee Shein Trust Services | "True sale" portfolios: 60M (6.2023), 90M (2.2024), 85M (9.2024), 80M (1.2025), 60M (3.2025), 84M (10.2025), 80M (2.2026), **539M in total**. Each SPC borrows from "a banking corporation", with floating and fixed charges over its assets and loans, repaid from portfolio collections. The company services the loans for a fee it calls immaterial, gives representations and **indemnities**, and part of the price is **deferred** and held in the SPCs in a deposit earning about 4% that is released as the portfolio pays down. The company owns all the shares but claims no control: voting rights do not direct the relevant activities, the lenders can remove it as servicer, and the servicing fee is at fair value | fy2025 p.94, p.106-108, p.50-53; h1_2026 p.6-7, p.32-33 |
| 9 | Amitim pension funds (funding partner, not a related party) | Portfolio sale of up to 120M (2022-2023). In place of cash fees it received 510,000 options at 6.05, expiring 24.7.2026 (255k) and 12.1.2027 (255k) | fy2025 p.17, p.106, p.108-109 |

**SPC economics (governance_calc §5).** Loans sold to the SPCs were 16.4% of originations in 2023, 45.0% in 2024 and
41.9% in 2025. As a share of all loans sold, the SPC share rose from about 41% (2023) to about 70% (2025), using
"share of credit sold" of 40% / 90% / 60% (fy2025 p.42). In 2024, SPC sales were 66.0% of the 265M assigned
(fy2024 p.59). The FY2025 buyer table lists **only the two SPCs** (fy2025 p.51-53). "Acquiring corporation A", the
external flow buyer since 13.11.2019 (fy2024 p.48), no longer appears. Deferred consideration at 31.12.2025 was
4,915k: 2,602k income receivable plus 2,313k long-term receivables, 6.0% of equity (fy2025 p.95, p.62, p.108).
The notes give no table of the maximum exposure to loss from the SPCs (indemnities, deferred price, servicing).
The company says expected default is fixed in the price formula, "so actual default does not affect the company's
share" (fy2025 p.51-52). Yet repayment of the deferred price depends on how the SPC portfolio pays down.

---

## 5. Capital allocation 2021 to 2026

### 5.1 Money in

| Event | Amount | Price | Source |
|---|---|---|---|
| IPO, 11.10.2021: 7,310,400 shares + 5,482,000 Series 1 warrants | 21.2M "gross" (footnoted "net of 1.542M issue costs"); 19,213k net cash | 2.90 per unit | fy2023 p.115, p.84 |
| 2021 convertible loan | 5,000k received; 2,242k converted to equity; 2,498k repaid | n/a | fy2023 p.83-84 |
| Private placement, 14.8.2022: 4,852,476 shares (13.16%) to institutions | 24.5M gross; 24,167k net | 5.05 | fy2023 p.115, p.108 |
| Option exercises 2021-H1 2026 | 4,255k. Of this, 4,001k came in 2025, when 1,920,000 unlisted "third-party" warrants (holder not named) and 46,835 employee options were exercised; weighted-average exercise price of all 2025 exercises 2.02 | | fy2025 p.112, p.118, p.85 |
| Series 1 public warrants (5,482,000) | lapsed in 2024: 5,762,000 options/warrants expired at an average strike of 3.54, and the 1,316k warrant reserve was released to premium | | fy2025 p.112; fy2024 p.82 |

Net equity raised was about 47.6M (governance_calc §3).

### 5.2 Money out: dividends (no dividends in 2021-2022: fy2023 p.83)

| Declared | Paid | Amount | Per share | Source |
|---|---|---|---|---|
| 27.2.2023 | 20.3.2023 | 3,000 | 0.0834 | fy2023 p.17, p.56 |
| 1.8.2023 | 24.8.2023 | 3,000 | 0.081253 | fy2023 p.17, p.56 |
| 25.2.2024 | 18.3.2024 | 2,000 | 0.054023 | fy2024 p.18, p.129 |
| 25.8.2024 | 12.9.2024 | 3,000 | 0.080633 | fy2024 p.18, p.129 |
| 13.11.2024 | 3.12.2024 | 2,000 | 0.05365 | fy2024 p.18, p.129 |
| 16.2.2025 | 5.3.2025 | 2,000 | 0.053131 | fy2025 p.18, p.130 |
| 15.5.2025 | 5.6.2025 | 2,000 | 0.0510146 | fy2025 p.18, p.130 |
| 7.8.2025 | 24.8.2025 | 2,000 | 0.0509797 | fy2025 p.18, p.130 |
| 16.11.2025 | 3.12.2025 | 3,000 | 0.07647 | fy2025 p.18, p.130 |
| 22.2.2026 | 9.3.2026 | 2,000 | 0.05096 | fy2025 p.18, p.130; h1 p.6 |
| 24.5.2026 | 18.6.2026 | 2,000 | ~0.05 | h1_2026 p.6, p.33 |
| 20.8.2026 | 17.9.2026 | 2,000 | ~0.05 | h1_2026 p.6, p.33 |

- Total paid from March 2023 to September 2026: 28,000k. Payout was 58.3% of net income (2023), 52.7% (2024), 49.5% (2025)
  and 48.3% (H1 2026). Declared dividends per share were 0.1647 (2023), 0.1883 (2024) and 0.2316 (2025); the 2025
  figure is a 7.3% yield on the implied snapshot price (governance_calc §3).
- **Policy.** There was no policy until 16.2.2025 (fy2023 p.18). Since then the policy is a quarterly dividend of at least 30% of
  comprehensive income, subject to the distribution tests and covenants, and expressly not binding (fy2025 p.18-19).
  Distributable earnings: 3,320k (31.12.2023), 13,591k (31.12.2024), 18,799k (31.12.2025) (fy2023 p.17; fy2024 p.18;
  fy2025 p.18).
- **Bank cap breached or waived?** For 2023, bank C's facility barred dividends above 4M without the bank's consent
  (fy2023 p.46, checked on the PDF image). The company paid 6M in 2023, 2M over the cap. The report says only that
  covenants were met after the dividends (fy2023 p.112) and does not mention a consent.

### 5.3 Buybacks, acquisitions and retained cash

- **Buyback.** On 13.11.2024 the board approved up to 5M over two years, from 18.11.2024 to 18.11.2026. **No shares had been bought**
  by the FY2025 report (fy2025 p.69, p.112), and the H1 2026 equity statement shows none (h1_2026 p.25). The plan equals
  4.0% of the snapshot market value. It went unused while the founders received options at 3.01 (January 2025).
- **Acquisitions and investments.** None. "In the last two years the company made no material investments"
  (fy2025 p.47; fy2023 p.45). Organic spending: development costs capitalised in cash of 740 (2021), 2,301 (2022), 2,789 (2023),
  2,211 (2024), 1,167 (2025) and 1,902 (H1 2026), 11,110k in total (fy2023 p.84; fy2025 p.85; h1_2026 p.28). The main
  project, the "360" platform, was completed in 2025 (fy2025 p.64). Management credits it for fee revenue of 27,278 in 2025
  against 14,538 in 2024 (fy2025 p.113; h1_2026 p.13). A new licensed-lending subsidiary, Paymeant Financing
  Solutions, started operating in early 2026 with an extended-credit licence dated 5.11.2025 (h1_2026 p.29).
- **Cash is not hoarded.** Cash and equivalents went from 31,411 (2022) to 16,922 (2023), 10,920 (2024), 5,938 (2025) and
  4,877 (30.6.2026) (fy2023 p.84; fy2025 p.85; h1_2026 p.28). Retained profit is recycled into loans held before sale
  and into dividends.
- **Verdict on capital allocation.** It is sensible and shareholder-friendly in cash (about 50% payout, no deals, equity raised
  at good prices in 2022). It falls short on per-share discipline: no buyback at about 3 ILS while cheap options went to the
  controllers. Dilution from employee equity is about 7.3%.

---

## 6. Insider ownership and alignment

- The founders' net 31.82% was worth about 39.8M at the snapshot price. Their 2025 cash and share pay (4,968k) is
  12.5% of that, and 1.73 times their share of 2025 dividends (2,864k) (governance_calc §2, §10). They are owners, but
  a large part of their annual return comes from pay set by formula on accounting profit.
- **Direction of travel.** They sold 2M shares in 2023-2024 at 3.25-3.85, asked for 2M options in 2025 and received
  1M at a below-market strike. Their capital share fell from 35.61% to 33.68%, and to 31.82% net of the nominee shares.
- **Other officers.** Small stakes: Gabai 0.63% (0.95% fully diluted), Mastorov 0% (0.36% FD), Yeshua 0% (fy2025 p.118). The
  former chairman sold 149,810 shares in August 2025 before leaving (fy2025 p.17-18).
- **Other holders.** Active outside holders such as Alon Gonen trade in large blocks (section 1.2). The register is thin
  and concentrated, which matters for liquidity (section 12).

---

## 7. Management candour: statements against outcomes

| Statement | What the record shows | Source |
|---|---|---|
| Origination run-rate "about 400M for 2024" (25.2.2024) | 389M actual (97.2% of the claim) | fy2023 p.5; fy2025 p.42 |
| Run-rate "about 500M for 2025" (16.2.2025) | 535M actual (107.0%) | fy2024 p.7; fy2025 p.42 |
| Run-rate "about 640M for 2026, based on the January 2026 daily average" | H1 2026 258M, 516M annualised (80.6%); the claim was cut to "about 600M" on the July 2026 daily average | fy2025 p.7, p.59; h1_2026 p.5 |
| Default rate "below 1%" / "about 1%, externally verified by the buyers" | On-balance-sheet defaults 1.2% (2023), 0.7% (2024), 0.8% (2025), **2.1% (30.6.2026)**; all non-current loans 2.3% / 1.5% / 2.6% / **4.6%** | fy2023 p.56, p.63; fy2024 p.58, p.63-64; fy2025 p.60, p.66; h1 p.6, p.15 |
| H1 2026: "no increase in loans in arrears except a negligible change" | Defaults 2.97 times as much and 1-90 dpd +44.8% in six months, while the book grew 9.6% | h1_2026 p.15 |
| The "unique" assignment model, "considered ground-breaking", is **daily (overnight)** (FY2023), **weekly** (FY2024), **monthly** (FY2025) | The flow-sale cadence has slowed each year, and the only buyers listed for 2025 are the company's own SPCs | fy2023 p.55; fy2024 p.57; fy2025 p.59, p.51-53 |
| "Sells its credit to leading financial bodies such as banks, credit-card companies and the largest institutional body" | 2025 full sales in the buyer table were to its own SPCs funded by "a banking corporation" | fy2025 p.70, p.51-53 |
| "No dependence on any buyer" | 88.5% of drawn bank credit came from one bank at 31.12.2025, and the buyer table lists only the SPCs | fy2025 p.47, p.49 |
| FS note 13: exposure to Bank of Israel rate changes "is not material" | The directors' report describes a direct effect: prime-based funding, -1,042k pre-tax per +1 point | fy2025 p.101 vs p.72-73 |
| Risk table rates collection risk "small" | The same report calls credit risk "the company's most material risk" | fy2025 p.57 vs p.101 |
| Covenant "tangible equity 82M" (31.12.2025) | Equity 82,198k less intangibles 7,307k = 74,891k (governance_calc §4); 82M is **total** equity | fy2025 p.68; h1 p.23 |
| Covenant "senior debt / loans 36%" (31.12.2024) | 82,410 / 142,742 = 57.7% on the balance sheet (50.1% net of cash). The 2023 figure (63%) appears to be net of cash, the 2025-26 figures gross | fy2024 p.67, p.80; governance_calc §4 |
| "Loans extended" (FY2023-24) became "transactions extended" (FY2025), up 38% | Not reconciled. Unclear whether 2025's 535M includes non-credit "360" payment transactions; the number of deals rose 67.2% while the average deal fell 17.6% (governance_calc §10) | fy2024 p.57; fy2025 p.14, p.42, p.59 |
| "Not a party to any legal proceedings" (FY2023, FY2024) became "not party to any **material** legal proceedings" (FY2025) | Wording widened; nothing is described | fy2023 p.50; fy2024 p.52; fy2025 p.54 |
| CTO salary written as "80,000 **thousand** ILS" in three reports; chairman dates written as 2026 | Repeated typos in the Reg. 21 section | fy2023 p.118; fy2024 p.120; fy2025 p.120, p.122 |
| Unexplained pay items | 477k "other" per founder (2023); 885k directors' fees (2025) | fy2023 p.117; fy2025 p.115 |

On the positive side, the company keeps quarterly reporting it could drop, discloses the SPC structure and the
accounting judgement behind it (fy2025 p.94), reported the failed option vote, and its run-rate guidance has been
roughly right in two of three years. The overall impression is promotional language and careless numbers rather than
concealment. Even so, the fund cannot rely on management's description of credit quality or funding diversity without
checking the tables.

---

## 8. Litigation, regulation, tax and contingent exposures

- **Litigation.** None material (fy2025 p.54). The filings disclose no class actions, sanctions or investigations (no hits in
  any of the four reports).
- **Licences.** The extended-credit licence was renewed on 27.9.2023 to 31.12.2028 (fy2023 p.128). The subsidiary's licence
  also runs to 31.12.2028 (h1_2026 p.29). Losing a licence is the end-game risk, and the company rates its AML and
  compliance risk "medium" (fy2025 p.56-57).
- **BNPL circular 2026-10-4.** Published 12.7.2026, effective **12.1.2027** (h1_2026 p.7-8). It requires disclosure that the purchase
  and the credit are separate, special rules above 7,500 ILS and for special populations, **cancellation of the credit
  when the goods or service are not delivered or only partly delivered**, written merchant agreements, and checks of merchant
  reliability. For a lender to aesthetics clinics, dentists, home renovators and schools, the cancellation right moves
  part of the merchants' performance risk onto the lender (or onto whoever buys the loan). The company is "examining the
  implications" and gives no estimate.
- **Credit Data Law amendment 6.** Published 26.7.2026, in force six months later (h1_2026 p.7). Negative credit data will be kept
  for 1 year instead of 3, and in emergencies negative data may be excluded. This could blunt an underwriting model
  built on Bank of Israel credit-register data (fy2025 p.101). Management thinks the amendment may help.
- **Price caps.** CPI-linked loans are capped at 13% real interest and 17% default interest (Interest Order), and
  unlinked loans fall under the Fair Credit Law cap (fy2025 p.27-28). The average nominal rate charged in 2025 was 7.96% (fy2025 p.42), so the
  cap does not bind today.
- **Tax.** Corporate tax is 23%. Assessments are final up to tax year 2019, so 2020 onward is open (fy2025 p.104). No disputes are disclosed.
  **No income tax was paid in cash in 2023-2024**; 7,124k was paid in 2025, covering 2023-2024 (fy2025 p.85, p.62; payable 5,707k at
  31.12.2024, fy2024 p.80), and 3,758k in H1 2026 (h1_2026 p.28). The company is not a "financial institution" for VAT
  purposes (fy2025 p.54). That is a classification on which its VAT and profit-tax position depends; it is not challenged in the
  filings.
- **Contingent and off-balance-sheet items with no amount disclosed.**
  1. Indemnities to Series 1 and Series 2 for breach of representations "and other cases" (h1_2026 p.7, p.33).
  2. Deferred consideration held in the SPCs, 4,915k at 31.12.2025 (section 4).
  3. Servicing obligations and the risk of removal as servicer (fy2025 p.94).
  4. A "payment guarantee" product for merchants (fy2025 p.40). Deferred income "for the operation product and the guarantee"
     sits in payables of 14,146k (31.12.2025) and 19,273k (30.6.2026) (fy2025 p.62; h1_2026 p.11). No guarantee
     exposure is quantified.

  None of the four filings has a contingent-liabilities note (FS note list: fy2025 p.86-115).

---

## 9. FX, interest-rate, credit and liquidity risk

### 9.1 FX
Not material: no foreign-currency assets or liabilities apart from the US$ D&O premium (fy2025 p.101).

### 9.2 Interest rate and CPI
- **Mismatch.** Loans are mostly fixed-rate and CPI-linked; funding is floating at prime + 0.5% to prime + 0.8%
  (fy2025 p.49, p.100, p.71).
- **Sensitivity.** +1 point on the funding rate costs 1,042k (31.12.2025) and 1,152k (30.6.2026), 4.4% and 5.3% of annual
  pre-tax profit. ±1 point of CPI moves the fair value of loans held for sale by ±1,816k and ±1,981k (fy2025 p.73; h1_2026 p.8-9;
  governance_calc §8). The Bank of Israel rate is 3.5% after cuts from November 2025 (h1_2026 p.9).
- **Discount-rate risk on the fair value of loans held for sale.** The price buyers pay is set off CPI-linked government bond
  yields plus a spread (fy2025 p.51, p.72). No sensitivity to that spread is given, although it is the key audit matter.

### 9.3 Credit
- The book is unsecured consumer credit: 191,493k at 31.12.2025 and 209,853k at 30.6.2026. It is concentrated in discretionary
  services: aesthetics, cosmetic surgery, dental, home renovation, equipment, tuition (fy2025 p.40). Average deal 22,792 ILS,
  average maturity 14 months (fy2025 p.42).

| Ageing (on balance sheet) | 31.12.2023 | 31.12.2024 | 31.12.2025 | 30.6.2026 |
|---|---|---|---|---|
| Default | 1.2% | 0.7% | 0.8% | **2.1%** |
| 1-90 days past due | 0.5% | 0.7% | 1.9% | **2.5%** |
| Arrangements (war deferrals) | 0.7% | 0.1% | 0.0% | 0.0% |
| All non-current | 2.3% | 1.5% | 2.6% | **4.6%** |

Sources: fy2023 p.63; fy2024 p.63-64; fy2025 p.66; h1_2026 p.15; ratios from governance_calc §6.

- Loans held for sale carry a fair-value uplift over amortised cost of 8,278k (2024), 8,409k (2025) and 9,515k (30.6.2026), equal to 12.1% of
  tangible equity at 30.6.2026 (fy2025 p.95; h1_2026 p.31; governance_calc §5). Credit losses expected on loans held for sale sit inside
  that fair value (h1_2026 p.13). The company also keeps exposure after sale through the SPC deferred price and
  indemnities (section 4).

### 9.4 Liquidity and funding
- **Credit lines.** Total lines are 340M across four banks. They are **non-committed on-call lines**, and "the financing bodies may
  terminate unilaterally" (fy2025 p.48, p.55). The company has no material long-term debt (fy2025 p.48). Unused lines were 236M at
  31.12.2025 and 201M at the FY2025 report date (fy2025 p.60, p.99).
- **Concentration.** At 31.12.2025 the drawn credit was bank A 0, **bank B 92,000**, bank C 1,000 and bank D 11,000, so bank B
  supplied 88.5% of the drawn total. A year earlier the largest share was 34.1% (fy2025 p.49; fy2024 p.46, both checked on the
  PDF image; governance_calc §4).
- **Maturities.** 98.4% of financial liabilities (121,404k of 123,431k) were due within a year at 31.12.2025 (fy2025 p.103).
  Cash was 4,877k against bank credit of 115,225k at 30.6.2026 (h1_2026 p.23).
- **Exit route.** Liquidity depends on selling 60-90M portfolios to the SPCs, on average every 5.3 months (intervals of 2.1 to
  8.0 months), funded by bank loans (section 4; governance_calc §10). If the SPC lender or the on-call lines step back, the company must stop originating or sell
  loans at a lower price.
- **Liens.** Each line is secured by a pledge of the dedicated bank account and of all the company's rights in loans funded
  from that line (fy2025 p.99).

| Leverage | 31.12.2023 | 31.12.2024 | 31.12.2025 | 30.6.2026 |
|---|---|---|---|---|
| Bank credit (k) | 114,892 | 82,410 | 104,241 | 115,225 |
| Net bank debt (k) | 97,970 | 71,490 | 98,303 | **110,348** |
| Bank credit / equity | 1.87x | 1.21x | 1.27x | 1.33x |

Sources: fy2024 p.80; h1_2026 p.23; governance_calc §4.

---

## 10. Covenants

Covenants apply under some or all bank lines (fy2025 p.99; h1_2026 p.33). Each line below gives the reported
figure first and our recomputation in brackets.

| Covenant | Threshold | 31.12.2023 | 31.12.2024 | 31.12.2025 | 30.6.2026 |
|---|---|---|---|---|---|
| Tangible equity / total (or tangible) balance sheet | at least 20% | 29% / 27% (29.3% / 30.5%) | 36% / 33% (36.1% / 37.9%) | 35% / 32-40% (35.1% / 36.4%) | 34% / 33-34% (33.9% / 35.2%) |
| Tangible equity | at least 25M (20M in 2022) | 55M (54.6M) | 59M (60.2M) | **82M** (74.9M) | 76M (78.6M) |
| Senior financial debt / loans and receivables | at most 80% | 63% (72.4% gross; 61.7% net of cash) | **36%** (57.7%) | 54% (54.4%) | 55% (54.9%) |
| Annual net income | at least 1M (2023: positive) | 10.6M | 13.3M | 18M | 8.2M for H1 |

Sources: fy2023 p.67; fy2024 p.66-67; fy2025 p.68; h1_2026 p.18; recomputation in governance_calc §4.

- **Headroom is wide.** A loss of about 42.4M, 20.2% of loans, would be needed to bring tangible equity to 20% of the tangible
  balance sheet at 30.6.2026. Tangible equity is 53.6M above the 25M floor (governance_calc §4).
- **Weak points.**
  1. The lines are on-call, so covenants are not the real constraint: the banks' discretion is.
  2. The change-of-control and line-of-business restrictions (fy2025 p.99).
  3. The bank C dividend cap in 2023 (section 5.2). No dividend limits were reported for 2024-2025 (fy2025 p.49).
  4. Reported covenant figures do not reconcile in two of the four periods.

---

## 11. Key-person risk

- The two founders are CEO and CTO, controlling holders, directors and the only independent signatories (fy2025 p.130).
  The underwriting platform is built in-house (R&D staff of 9; 52 employees in total, fy2025 p.46). The founders are on
  90 days' notice with a 6-month paid non-compete (fy2025 p.120-121).
- Management depth is thin and recent: CFO since 1.1.2023, VP R&D since 1.2024, new collections VP since 26.10.2025, new clearing and risk VP
  since 1.9.2025, new chairman since 18.11.2025 (fy2025 p.129, p.125). Key-person risk is **not listed** among the risk
  factors (fy2025 p.55-57), and no key-person insurance is disclosed.
- The banks' change-of-control clauses tie the founders' departure or sale to the funding (fy2025 p.99).

---

## 12. Market event and liquidity (UNVERIFIED)

- The Mega snapshot market value of 125,069,508 ILS on 39,245,034 shares implies 3.187 ILS a share. That is 43.2% below the
  5.61 used for the 20.8.2026 grant (h1_2026 p.33) and only 5.9% above the founders' 3.01 strike (governance_calc §9).
  Search summaries show about 5.00 ILS on 1.10.2026 (Investing.com) and a 52-week low of 366.10 agorot (Google Finance) (**UNVERIFIED**).
- An ICE (ice.co.il, article 1135574) summary reports a fall of more than 14% in one day, completing a fall of more than 40% in a week, after
  weakness since February 2026. The exchange asked about the move; the company replied that it knew of no unusual event
  and business was normal. Market participants pointed to a large holder selling, forced liquidation or a cascade of
  stop-loss orders in a thin stock (**UNVERIFIED**; date not shown; site not opened).
- If confirmed, the sale looks technical: a block holder exiting an illiquid, concentrated register (section 6). But
  our documents end on 20.8.2026, so any September-October 2026 event on Maya must be checked before acting:
  bank-line changes, SPC funding, the Q3 dividend decision, sales by interested parties.

---

## 13. Ranked red-flag list (most severe first)

| # | Red flag | Why it matters | Evidence |
|---|---|---|---|
| 1 | **On-call, uncommitted bank funding concentrated in one bank** | Net bank debt 110.3M (1.33x equity). Bank B supplied 88.5% of drawn credit at 31.12.2025. Lines can be withdrawn unilaterally, and liabilities are 98.4% short-term. Under rule 4 this is debt that could force a sale of the loan book: close to disqualifying unless the valuation treats it as self-liquidating warehouse funding | fy2025 p.48-49, p.55, p.103; h1 p.23 |
| 2 | **Risk transfer runs through the company's own unconsolidated SPCs** (539M since 2023), funded by bank loans | The company keeps servicing, indemnities and a 4.9M deferred price. Maximum loss is not quantified. The external flow buyer has dropped out of the table. The off-balance-sheet structure lets the company report a "true sale" while depending on one bank's appetite | fy2025 p.94, p.106-108, p.51-53, p.95 |
| 3 | **Credit quality deteriorating, described as "negligible"** | Defaults 0.8% to 2.1% and all non-current loans 2.6% to 4.6% in six months. The BNPL circular and credit-data changes take effect in early 2027 | fy2025 p.66; h1 p.15, p.7-8 |
| 4 | **Profit includes fair-value gains, and pay is a share of that profit** | Fair-value uplift 9.5M (12.1% of tangible equity). Founders' uncapped bonus on pre-tax profit paid in quarterly advances. Fair value is the key audit matter | h1 p.31; fy2025 p.79, p.119-121 |
| 5 | **Controller pay and equity grabs** | 21% of pre-tax profit in 2025, +19.6% salary from 2026, 1M options at a below-market strike, a second 1M rejected by the minority. Pay capitalised into intangibles | fy2025 p.118-121, p.131; h1 p.19 |
| 6 | **Disclosure quality** | Covenant figures that do not reconcile; unexplained "other" 954k (2023) and directors' fees 885k (2025); 2023 dividend above the bank C cap with no disclosed consent; option counts that differ; typos | sections 3, 5, 7, 10 |
| 7 | **Undisclosed June 2023 agreement with the controllers** | Approved without a general-meeting vote on the day of their share sale; terms only in a Maya report we could not read | fy2023 p.57, p.121 |
| 8 | **Thin governance structure** | Only the two statutory external directors are independent; chairman not independent; internal auditor reports to the CEO, about 280 hours a year; no ICFR report under small-corporation relief | fy2025 p.74-75, p.117, p.125-128 |
| 9 | **Regulation** | BNPL circular puts merchant non-delivery risk on the lender from 12.1.2027; credit-register history cut from 3 years to 1 year; licence renewal due 2028 | h1 p.7-8; fy2023 p.128 |
| 10 | **Price collapse and thin liquidity (UNVERIFIED)** | More than 40% down in a week with no company explanation; a block holder trades blocks of over 1M shares off-exchange | section 12; fy2025 p.17 |
| 11 | **Founders reducing their stake; nominee shares** | 2M shares sold at 3.25-3.85; 1.86% held for an unnamed holder; agreement threshold 25% (headroom 6.82 points) | fy2023 p.17; fy2025 p.118, p.123 |
| 12 | **Key-person concentration** | Founders run the business, the technology and the signatures; no succession or key-person disclosure | fy2025 p.120-121, p.130, p.55-57 |
| 13 | **Tax and cash-flow timing** | No tax paid in 2023-2024 and a 7.1M catch-up in 2025, which distorts operating cash flow; open years from 2020 | fy2025 p.85, p.104 |

**Mitigating facts:** clean EY opinions with no emphasis of matter; no litigation or sanctions; licence to 2028; wide covenant headroom;
a consistent dividend of about 50% of profit; no acquisitions; founders still own about 32%; minority shareholders have used their
veto; quarterly reporting kept voluntarily.

**Suggested treatment under Rev 4 (for the valuation lead).**
- Governance and data: **+5 extra margin points**, on the same basis as the Aluma and Thor precedents: controlling holders,
  small-corporation and Tech-Elite reliefs, SPC exposure not quantified, figures that do not reconcile.
- Business type: a consumer-credit originator funded by on-call bank lines. It is exposed to the credit and funding cycle,
  which points to the "cheap" track (grade C, normalised earnings).
- Rule 4: the company has **no net cash** and is structurally levered. The CIO must decide whether warehouse debt secured
  on saleable loans counts as disqualifying leverage.

---

## 14. Open items to verify on Maya or with investor relations before any decision

1. Immediate report 2023-01-060154: terms of the 27.6.2023 agreement with the controlling holders.
2. Holdings report 2026-01-003679 and later reports: current holdings, pledges, identity of the "other shareholder"
   behind the 1.86% nominee shares, and who sold during the fall (probably October 2026).
3. The 26.2.2026 (amended) general-meeting notice and the 30.3.2026 results: final founder terms.
4. Bank C consent for the 6M of 2023 dividends; the covenant definitions (why 36% for 2024 and "tangible equity" 82M for 2025).
5. SPC documentation: lender identity (the same bank B?), deferred-price waterfall, indemnity scope, servicer-removal triggers,
   maximum exposure to loss.
6. The 885k directors' fees in 2025 and the 477k "other" per founder in 2023.
7. September-October 2026 immediate reports: price inquiry response, bank-line changes, the Q3 dividend, sales by interested parties.
8. The guarantee exposure of the merchant "payment guarantee" product, and whether 2025 "transactions" include non-credit volume.
