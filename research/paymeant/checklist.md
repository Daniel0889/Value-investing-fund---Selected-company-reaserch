# Paymeant Financial Technologies (TASE 1180876): pre-purchase checklist, CIO gate

Run on 3.11.2026 against `constitution_zip/checklist.md` (Revision 4, 60 items in eight groups A-H). The checklist is
answered from the revised valuation, which follows the red-team objections the CIO accepted.

**Sources.**
- **Numbers.** Every number comes from `research/paymeant/output.txt`, cited "out §n", which `research/paymeant/valuation.py`
  prints through `lib/charter_valuation.py`. The rest are filed figures with their PDF page, read on the page image.
- **Workstream files** are in `work/paymeant/`: `scuttlebutt.md`, `governance_risk.md`, `business.md`, `market.md`,
  `redteam_accounting.md` and `redteam_business.md`.
- **Rules.** Yes = pass. A "don't know" or "cannot assess here" counts as "no": gates fail closed.

**Lane declared (G4): none.**
- **Why none.** No lane fits: A/B fail on the moat, leverage and funding; C is not a net-net and has net debt; D has no
  A/B franchise; E has no deal (out §6).
- **How the items were run.** Because no lane fits, each item is run against the lanes a thesis could claim:
  - Items that bind only A, B and D are run as **B**, the nearest tier on unlevered returns (out §1a).
  - Group H is run as **C**, the cheap track the brief gives a cyclical.
  - Items that bind every lane are run as written.
  - Items binding only D, only holding companies, or only adds are "n/a", with that reason.

**Result.**

| Type | Items | Yes | No | Cannot assess here (counts as no) | n/a |
|---|---|---|---|---|---|
| VETO | 40 | 8 | 23 | 6 | 3 |
| FLAG | 20 | 7 | 9 | 3 | 1 |

Applicable VETO items fail, so the output is **NO_THESIS**. It is not WATCHLIST, because price is not the only failure
(gate.md §3).

---

## A. Business and moat (9)

| # | Question (yes = pass, abridged) | Type | Applies / run as | Answer | Evidence (one line) |
|---|---|---|---|---|---|
| A0 | Inside the written circle (`theses/CIRCLE.md`)? | VETO | A, B, D / B | **cannot assess here** | CIRCLE.md is not available here. The model is on framework f2's avoid list: "dependent on refinancing markets ... Delta Financial's warehouse lines". business.md §14 puts it outside the circle as a moat case |
| A1 | Explain in 3-4 sentences how it makes money, and why it should make more in ten years? | VETO | A, B, D / B | **no** | How it earns is clear: fees, loan-sale gains and interest (paymeant_h1_2026 p.32). Nothing shows why it should earn more: merchants may cancel "at any time and for any reason" (paymeant_fy2025 p.41), and the run-rate was cut from 640M to 600M (fy2025 p.59; h1_2026 p.5) |
| A2 | Worst case held with high confidence, and free of rapid change and of superstar dependence? | VETO | A, B, D / B | **no** | The worst case runs 0.59-1.09, before the SPC indemnities and the 360 guarantee exposure, which are not disclosed (out §4; h1_2026 p.7). The two founders are CEO and CTO, and the lines restrict changes of control (fy2025 p.99). BNPL rules change from 12.1.2027 (h1_2026 p.7-8) |
| A3 | Moat named, and showing in returns on tangible capital above peers over the window? | VETO | A, B, D / B | **no** | Unlevered ROTC has a median of 15.7% and a minimum of 7.7% (out §1a). Peer returns exist for TTM only (ROE 22.6% against a 17.5% median, scuttlebutt.md §1.2) and are helped by gains on sales to the company's own SPCs. Nothing is patented (fy2025 p.45) |
| A4 | Could a well-funded competitor do no serious damage ($1bn test)? | VETO | A, B, D / B | **no** | Merchants cancel at will (fy2025 p.41). Banks and card issuers sit at every terminal (fy2025 p.38, p.44). The regulator wants more entrants: Calcalist 23.9.2024, https://www.calcalist.co.il/investing/article/hj3y11krac |
| A5 | Real price rises without volume loss, with owners keeping the gains? | FLAG | A, B, D / B | **no** | The average nominal borrower rate fell from 9.83% (2023) to 7.96% (2025) (fy2025 p.42), and merchants can leave (p.41) |
| A6 | Growth needs little capital, or earns well above r? | VETO | A, B, D / B | **no** | About 35% of a year's originations is held, 44% of it equity-funded (business.md §11). Normalised ROIIC is 11.2% against r of 10% (out §3) |
| A7 | Industry rational: no player buying share at a loss, supply slow to arrive? | FLAG | all but E / as written | **no** | Blender lost 72.5M in 2021-2025 while lending (scuttlebutt.md §1.3). Any licensed lender or bank can enter, and the regulator is adding entrants (A4) |
| A8 | Old and dull, and holds real earnings through inflation without more capital? | FLAG | A, B, D / B | **no** | A BNPL lender listed in 2021 (fy2025 p.6). A CPI-linked loan book needs more equity as CPI rises (fy2025 p.71; business.md §11) |

## B. Management and capital allocation (7)

| # | Question (yes = pass, abridged) | Type | Applies / run as | Answer | Evidence (one line) |
|---|---|---|---|---|---|
| B1 | Each retained shekel created at least a shekel: book value per share plus distributions beat the index? | FLAG | A, B, D / B | **cannot assess here** | Index total returns are not in the documents. Book value per share was lifted by the 2022 placement at 5.05, above book (governance_risk.md §5.1) |
| B2 | Buybacks only below value, from surplus cash, never just to offset dilution? | FLAG | all but E / as written | **yes** | No share was bought under the 5M plan of 13.11.2024-18.11.2026 (fy2025 p.112; h1_2026 p.25). At the revised base of 2.19 (out §4), not buying at 3-7 ILS was right. The business red team's "no" is rejected (gate.md §1, O4) |
| B3 | Stock issued only for full value, with dilution of at most 2% a year? | VETO | all / as written | **no** | Shares rose 19.4% in 2022 and 5.3% in 2025, a 6.2% CAGR over FY2021-FY2025 (out §2). The 2025 exercises came in at 2.02 (fy2025 p.112). The founders took 985,000 shares for 10k in 2022 (fy2023 p.107) |
| B4 | Pay tied to per-share value, and insiders own stock they bought? | FLAG | A, B, D / B | **no** | The bonus is an uncapped share of pre-tax profit, paid in quarterly advances (fy2025 p.119-121). Monthly salary went from 92k to 110k on 22.2.2026, after the general meeting refused options on 23.12.2025 (fy2025 p.119-120, p.131). The founders were sellers (out §6) |
| B5 | Accounts understandable without "adjusted" earnings that exclude stock pay, and mistakes reported candidly? | VETO | all / as written | **no** | The headline "Adjusted EBITDA" adds back share-based pay of 816 in 2025 (fy2025 p.66-67; h1_2026 p.16). Defaults rose 2.97 times and were called a "negligible change" (h1_2026 p.15). "Material" was added to the legal-proceedings sentence (fy2025 p.54 against fy2024 p.52) |
| B6 | Resisted the institutional imperative: no empire-building deals? | FLAG | all but E / as written | **yes** | No acquisitions, and "no material investments" in two years (fy2025 p.47) |
| B7 | No record of personal misconduct, sanction or conviction? | VETO | all / as written | **cannot assess here** | The CMA sanctions lists for 2023-2025 and the Companies Registrar are clear (scuttlebutt.md §4). The court and class-action registers could not be searched. TheMarker reported merchant disputes on 18.6.2026 and 12.7.2026; the headlines are confirmed by search and the bodies are UNVERIFIED: https://www.themarker.com/law/2026-07-12/ty-article-magazine/.highlight/0000019f-4153-d07c-af9f-c95f90af0000 |

## C. Financial strength and earnings quality (7)

| # | Question (yes = pass, abridged) | Type | Applies / run as | Answer | Evidence (one line) |
|---|---|---|---|---|---|
| C1 | Survives a year of flat revenue and EBIT down 30%, with no covenant breach and no new money? | VETO | all / as written | **no** | Covenants hold: net profit would be 13,184 against the 1,000 minimum (out §4). But all 115,225 of bank credit is on-call, and the funders "may stop the engagement unilaterally" (fy2025 p.55; p.49 fn 14) |
| C2 | Net debt including leases at most 2x normalised EBIT (B), and cover of at least 8x? | VETO | A, B / B | **no** | Net debt with leases is 9.6x EBIT_norm after funding cost and 7.0x before it. Cover is 5.1x (out §1b) |
| C3 | No maturity within 24 months that needs refinancing markets open? | VETO | all / as written | **no** | 115,225 of on-call, short-term bank credit (h1_2026 p.23, p.31) |
| C4 | Cash owner earnings at least 80% of net income, with no build-up of deferred assets? | FLAG | all but E / as written | **no** | Annual lender-adjusted conversion was 100%, and the loan book is not building ahead of originations (out §2). But capitalised development reached 34% of gross R&D in H1 2026 (h1_2026 p.13, p.28), and controllers' pay is capitalised (fy2025 p.115) |
| C5 | Normalised earnings free of endogenous add-backs? | VETO | all but E / as written | **yes** | The rebuilt EBIT_adj removes only the 1,188 termination gain (fy2023 p.111). IPO share-based pay stays a cost (out §2) |
| C6 | Covered interest comfortably in FY2020 and FY2022? | FLAG | all but E / as written | **no** | FY2022 cover was 4.8x (out §1b). FY2020 is not in the documents (IPO in October 2021) |
| C7 | Identities pass, and every single-source figure confirmed by one? | VETO | all / as written | **no** | The H1 2025 cash flow shows no tax paid and no Q2 interest received (h1_2026 p.28). The company's covenant tangible equity (82M; 76M) does not match equity less intangibles (fy2025 p.68; h1_2026 p.18; out §4) |

## D. Valuation and margin of safety (8)

| # | Question (yes = pass, abridged) | Type | Applies / run as | Answer | Evidence (one line) |
|---|---|---|---|---|---|
| D1 | At least two independent methods, a range with a worst case, no EBITDA, all in code? | VETO | all but E / as written | **yes** | EPV 2.15, DCF 2.19 and tangible book 1.99: a spread of 10% (out §5). Range 0.59-4.68. All in lib/charter_valuation.py, as the brief directs. Note: the price was in the brief, but no value input uses it |
| D2 | Price at or below the tier's share of base value? | VETO | all but E / as written | **no** | No lane, so no buy price. The price is 1.45x base and 2.91x the Tier C net-net line of 1.09 (out §5) |
| D3 | Base value above the price everywhere in the grid? | VETO | A, B, D / B | **no** | The lender-basis grid runs 1.95-2.55 against 3.173. The EV-basis reading runs 2.44-4.52 (out §4) |
| D4 | Implied growth below the per-share record? | FLAG | A, B, D / B | **yes** (weak) | Implied growth is +5.3% to +13.8% against a 47.5% EPS record, which starts from a start-up base and stalled in H1 2026 at −4.2% (out §2, §6) |
| D5 | Expected return clears r with a dated y10? | VETO | all / as written | **no** | r is 10%, with y10 at 4.29% on 3.11.2026. The probability-weighted value of 2.34 is below the price (out §0, §4) |
| D6 | Beats the weakest holding, or the better of cash and the index, after tax? | FLAG | all / as written | **no** | The expected return is negative (D5), so it is below bills. Holdings and tax_params are not available here |
| D7 | Price is the latest dated close, and identifiers come from the brief? | VETO | all / as written | **yes** | 3.173, the official close of 3.11.2026. TASE 1180876. The 39,330,034 shares reproduce Mega's cap (market.md §0-§1) |
| D8 | TTM basis, and every filing since the period end read? | VETO | all / as written | **no** | TTM runs to 30.6.2026. The Maya reports since then (assignment of 23.9.2026, clarification of 28.10.2026) were read as headlines only (market.md §3) |

## E. Risks and inversion: the pre-mortem (9)

| # | Question (yes = pass, abridged) | Type | Applies / run as | Answer | Evidence (one line) |
|---|---|---|---|---|---|
| E1 | No plausible path to any of the three impairment markers? | VETO | all / as written | **no** | Paths exist to marker 1: on-call lines, the profit covenant at a fall in originations of about 51%, and SPC indemnities "in other cases" (h1_2026 p.7). A path also exists to marker 2 (out §4) |
| E2 | Three falsification conditions, specific, observable and dated? | VETO | all / as written | **yes** | gate.md §4 |
| E3 | Price's assumption shown wrong, the seller known, and the discount not fully explained by a known fact? | VETO | all / as written | **no** | The price assumes today's scale persists (−3.2% a year on it). P/E is 11.9% below the lender median and P/B 4.8% above it. Known, unrefuted facts explain the rest (out §6), so it is priced (Petco) |
| E4 | Can I argue the bear case better than the best bear? | FLAG | all / as written | **yes** | gate.md §2 adopts and extends redteam_business.md §3 |
| E5 | Second-order effects thought through? | FLAG | all but E / as written | **yes** | Banks buy the loans, not the platform. The circular raises every lender's costs. The regulator is adding entrants (scuttlebutt.md §1.4) |
| E6 | Thesis about the destination in five to ten years? | FLAG | A, B, D / B | **yes** | gate.md §6, dated 3.11.2026 |
| E7 | Misjudgment tendencies checked? | FLAG | all / as written | **yes** | gate.md §2 covers management's incentive bias, the team's first version, social proof from Gonen's 9.48%, and anchoring on 6.90 and 5.61 |
| E8 | Earnings independent of any single variable? | VETO | A, B, D / B | **no** | Everything rests on Israeli banks' appetite for point-of-sale credit. Four on-call lines, with bank B at 88.5% of drawn credit (fy2025 p.49). One bank funds the SPCs (fy2025 p.108) |
| E9 | Li Lu's four categories, plus scuttlebutt beyond the company's filings, including courts? | FLAG | A, B, D / B | **no** | The four categories are in gate.md §5. Competitors, regulators, the registrar and the press were searched (scuttlebutt.md). Courts and the class-action register were not |

## F. Israel-specific (6)

| # | Question (yes = pass, abridged) | Type | Applies / run as | Answer | Evidence (one line) |
|---|---|---|---|---|---|
| F1 | Control chain mapped, with no over-levered pledged controller? | VETO | all / as written | **cannot assess here** | Two founders hold 29.54% directly, with no layers (scuttlebutt.md §5; fy2025 p.123). No pledge is disclosed, and the open Pledges Registrar carries no names |
| F2 | Five years of related-party deals, pay and minority votes read, with every rejection explained? | VETO | all / as written | **cannot assess here** | The June 2023 founders' agreement is undescribed; it was approved without a meeting (fy2023 p.57, p.121). The refusal of 23.12.2025 (fy2025 p.131) was followed by a 19.6% raise (redteam_business_calc §S2, from fy2025 p.119-120) |
| F3 | Consolidated statements, currency read, no pre-2020 PDF digits, and one-source figures checked? | VETO | all / as written | **yes** | Consolidated statements (h1_2026 p.23), in ILS, with no pre-2020 figures. Identities were checked, and the figures that fail them are not used (out §2) |
| F4 | Currencies and CPI linkage recorded, and the thesis survives a shekel move, high CPI and +2 points? | VETO | all but E / as written | **no** | +2 points takes 35-45% of TTM pre-tax profit in year 1. On normalised earnings it breaks the profit covenant in the 14-month case (out §4). The held book's rate sensitivity is not disclosed |
| F5 | Holding company: look-through NAV, and holdco debt serviceable? | VETO (holdcos) | holdcos | n/a | Not a holding company. The SPCs are unconsolidated securitisation vehicles (fy2025 p.94) |
| F6 | Outside TA-35 and dual listings, off the maintenance list, price-reliability block, window flag and data addition, TASE at most 30%? | FLAG | all / as written | **no** | Median turnover of 19,125 ILS fails the 50,000 floor (screen_spec X5) and the 100,000 line (out §6). Not TA-35, not dual-listed, off the maintenance list (scuttlebutt.md §7). TASE room cannot be assessed here |

## G. Position sizing, adding and taxes (8)

| # | Question (yes = pass, abridged) | Type | Applies / run as | Answer | Evidence (one line) |
|---|---|---|---|---|---|
| G1 | Size the smallest of quarter-Kelly, tier cap, loss budget, liquidity, sector and TASE caps? | VETO | all / as written | **yes** | position_size() gives 0.0% of NAV, with quarter-Kelly binding. The liquidity cap is 10,361 ILS (out §6) |
| G2 | Could hold through a 50% fall without forced selling? | VETO | all / as written | **cannot assess here** | The fund uses no leverage (charter). The principal's cash needs are not known here |
| G3 | Fits within twelve monitoring slots? | VETO | all / as written | **cannot assess here** | Holdings are not available here, and no position is proposed |
| G4 | Lane declared now, with its sell rule? | VETO | all / as written | **no** | No lane fits (out §6); gate.md §7 records the rule that would bind |
| G5 | Sized to matter if every VETO passes? | FLAG | A, B, D / B | n/a | Its condition, that every VETO passes, is not met |
| G6 | Better than adding to an existing holding (the punch card)? | FLAG | A, B, D / B | **cannot assess here** | Holdings are not available here, and no commitment is proposed |
| G7 | For an add after a fall: filings read, nothing fired, within the cap? | VETO (adds) | adds | n/a | Not an add to a position |
| G8 | Returns and swaps after the principal's taxes; not a US PTP? | FLAG | all / as written | **cannot assess here** | tax_params is not available here. Not a US publicly traded partnership |

## H. Lane C bargains (6)

| # | Question (yes = pass, abridged) | Type | Applies / run as | Answer | Evidence (one line) |
|---|---|---|---|---|---|
| H1 | Explain how it makes money and what its assets are worth to a buyer? | VETO | C / C | **yes** | Fees, loan-sale gains and interest (h1_2026 p.32). The roughly 210M of loans are sold at a discount rate built on government bonds plus a margin (fy2025 p.51; h1_2026 p.31) |
| H2 | Asset value firm: NCAV and Dempster from one date, identity-checked? | VETO | C / C | **no** | The loans are Level 2 marks set against the company's own SPCs (fy2025 p.91, p.103). Run-off value spans 0.59-1.09, before exposures that are not disclosed (out §4) |
| H3 | Floor not being burned: three-year average OCF at least zero? | VETO | C / C | **yes** | Reported OCF for FY2023-FY2025 averages 466 (out §2) |
| H4 | A catalyst, or a basket of at least 20? | VETO | C / C | **no** | No catalyst, and a single name. The buyback plan lapses unused on 18.11.2026 (fy2025 p.112) |
| H5 | For a cyclical: no net debt, and valued over the whole cycle? | VETO | C cyclicals / C | **no** | Net debt with leases is 112,942 (out §1b), and the window holds no credit cycle |
| H6 | For Lane D: problem isolated beside the franchise? | VETO | D | n/a | Not Lane D: there is no A/B franchise |

---

## FLAG items answered "no": 12, with explanations accepted by the CIO

1. **A5 (pricing power).** Borrower rates fell 187 basis points over 2023-2025 (business_metrics_output, from
   fy2025 p.42) while merchant fees rose. The payer is
   shifting from borrower to merchant, and merchants can leave on notice. No pricing power over either side is shown.
2. **A7 (industry rationality).** The one listed rival lent at a loss for five years. Licences and credit data are open
   to every lender, and the regulator is deliberately adding entrants, so new supply can arrive fast.
3. **A8 (old, dull, inflation-proof).** A young, regulation-shaped product. The CPI-linked book needs proportionally more
   equity as prices rise.
4. **B1 (retained earnings test).** It cannot be assessed here, because there is no index series. It would be
   flattered anyway, since book value per share rose mainly through the 2022 placement above book.
5. **B4 (pay alignment).** Pay is a formula on pre-tax accounting profit, including unrealised fair-value gains. The
   raise followed a minority refusal. The founders are net sellers, including 869,564 shares at 6.90 between the board's
   and the meeting's approval of the raise.
6. **C4 (earnings quality).** Cash conversion is adequate on annual audited figures. But development capitalisation
   jumped in H1 2026: before it, H1 pre-tax profit fell 4.2%. Part of the controllers' pay is capitalised.
7. **C6 (stress-year cover).** Cover was 4.8x in FY2022, below Graham's 7x for industrials. FY2020 predates the listing
   and is not in the documents.
8. **D6 (beats the alternatives).** The expected return at the price is negative on the probability-weighted value.
   The holdings and tax_params needed for the after-tax swap are not available.
9. **E9 (scuttlebutt).** The court and class-action registers could not be searched. The TheMarker articles could not
   be read beyond their headlines, because themarker.com is outside this session's network allow-list.
10. **F6 (liquidity and TASE items).** It fails the liquidity floor, a hard exclusion under screen_spec X5. The
    shekel 30% room cannot be checked without holdings.
11. **G6 (punch card).** There is no commitment, and the holdings are unavailable.
12. **G8 (taxes).** tax_params is unavailable. The security is not a US PTP.

## Red-team reviewers

- **paymeant:redteam-accounting** raised 12 objections, B1-B12 in `redteam_accounting.md`:
  - accepted: 10;
  - accepted in part: 1 (B2);
  - rejected: 1 (B11, tax).
- **paymeant:redteam-business** raised 11 objections, O1-O11 in `redteam_business.md`:
  - accepted: 8;
  - accepted in part: 3 (O1, O4, O8);
  - rejected: none.

The decision on each objection, with evidence, is in `gate.md` §1.

The FLAG explanations above restate findings the reviewers reached themselves:
- A5, A7, A8 and B4: `redteam_business.md` §7;
- C4: `redteam_accounting.md` B4.

The CIO departs from a reviewer on one item:
- **B2.** The CIO answers "yes", where the business reviewer answered "no". Reason: no buyback was made, so none was
  made above value.
