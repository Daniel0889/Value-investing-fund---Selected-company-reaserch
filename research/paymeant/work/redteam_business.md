# Paymeant Financial Technologies (TASE 1180876): red team, business, management, Israel and inversion

Charter step 8. Written 3.11.2026 (finished about 22:15 Israel time). The red team argues the bear case and tests
the valuation team's claims (`research/paymeant/output.txt`, cited "out §n"; `work/paymeant/valuation_notes.md`)
against the filings and the web. Lens: checklist A0-A8, B1-B7, E1-E9, F1, F2, F5, F6, H1-H6.

**Conventions.**
- Filings are `paymeant_fy2023`, `paymeant_fy2024`, `paymeant_fy2025` and `paymeant_h1_2026`. "p.N" is the PDF page
  index. Every table figure used here was re-read on the page image (list in §9).
- Every derived figure comes from `work/paymeant/redteam_calc/redteam_business_calc.py`. Its output is
  `redteam_calc/redteam_business_calc_output.txt`, cited "rt §Sn". No arithmetic is done in this prose.
- Web pages were read on 3.11.2026. An item seen only in a search-engine summary is marked **UNVERIFIED**.
- Units are ILS thousands unless stated; per-share values in ILS (1 ILS = 100 agorot).

---

## 0. Bottom line

1. **No position: I agree with the output, but not with several of the reasons.** The record overstates how cheap the
   stock is and understates how many gates fail.
2. **The "price well below value" finding rests on two things the fund will not pay for.**
   - The base value of 5.36 (price/base 0.59) is a lender-basis DCF. It credits the on-call warehouse leverage
     (1.41 a share, out §3) and assumes a 22.2% incremental return for ten years (out §3).
   - The same file finds no moat (A3, A4 fail) and calls that leverage the thing "the fund declines to pay for".
   - On the charter's own EPV, which is unlevered (charter, "Valuation methods"), the stock is about fairly priced:
     - EPV 2.95;
     - DCF 3.10 at g 2% and 3.37 at g 5% (3.70 on average capital);
     - grid minimum 2.52 (2.69 on average capital), below the 3.173 price (rt §S9).
   - So Q3 is "no" and D3 fails, on price as well as on quality.
3. **VETO items that fail and are missing from the list:**
   - B5: the company's headline measure is an "Adjusted EBITDA" that adds back stock pay, and its credit-quality
     claims are promotional.
   - B3: the share count rose 5.3% in 2025.
   - A1 and A6.
   - A2 fails on its second clause too: key people and fast-changing payments rules.
   - H4 and H5 for Lane C.
   - Open, so failing closed: B7, F1 and F2.
4. **New outside evidence the scuttlebutt missed.**
   - TheMarker (18.6.2026 and 12.7.2026) reports dentists who say they were left owing Paymeant on equipment they
     returned, and calls the Paymeant/Blender model one that "looks away" when merchants fall out with customers.
   - It is UNVERIFIED: paywalled, HTTP 403.
   - It fits the anonymous class-action comment of 28.10.2026 and the FY2025 change to "no *material* legal
     proceedings".
5. **The informed holders sold.**
   - The founders sold 6.00M ILS at 6.90 on 13.3.2026. This came between the board's and the general meeting's
     approval of their 19.6% raise, which followed the minority's refusal of their options.
   - No insider bought in the 54% fall since.
   - The buyback approved at the 2024 low was never used.
   - Dividends are paid with on-call bank credit.
6. **File it in the too-hard pile, not on a price trigger.** If the record keeps NO_THESIS, it must say that price
   alone never reopens the file.

---

## 1. The valuation team's claims in my lens, checked against the pages

| Claim (team) | Check | Result |
|---|---|---|
| Bank B 88.5% of drawn credit at 31.12.2025 | fy2025 p.49 (image): B line 100,000, unused 8,000; total drawn 104,000 | **Correct.** But A (100,000) and D (89,000) were unused (rt §S6), so the single variable is the banks' collective appetite. Objection 10 |
| All funding is on-call | fy2025 p.48 ("on-call", no long-term credit); p.49 fn 14; p.55 ("may stop the engagement unilaterally") | Correct |
| Take-outs go to own SPCs funded by "a banking corporation" | fy2025 p.50-53 (buyer table lists only Series 1 and Series 2); h1_2026 p.6-7 | Correct. Indemnities "for breach of representations **and in other cases**" (h1_2026 p.7) |
| Merchants can cancel at will | fy2025 p.41: "either party may cancel at any time and for any reason"; 3 months of minimum fee | Correct |
| Nothing patented | fy2025 p.45 §20 | Correct |
| The regulator is adding competitors | Calcalist 23.9.2024 [CAL-0923]: the CMA's BNPL rules are meant "to attract new players to the field and increase competition". The Payment Services Law (June 2024) lets ISA-supervised fintechs offer credit alongside payments | **Correct, and stronger than stated** |
| "No peer returns are available" (tier_reason) | scuttlebutt.md §1.2 has them: ROE 22.6% against a core median of 17.5% | **Inaccurate.** A3 still fails: the figures are TTM only and are flattered by gain-on-sale through own SPCs. Objection 6 |
| Arrears up: default 4,395, 1-90 days 5,198 on 209,853 | h1_2026 p.15 (image); fy2025 p.66 for 31.12.2025 | Correct. Defaults x2.97, non-current 2.6% to 4.6% in six months (rt §S3) |
| BNPL circular from 12.1.2027 | h1_2026 p.7-8 (image): cancellation of the credit when goods or services are not supplied; checks on the merchant's reliability and financial strength | Correct |
| "An unexplained block sale on 21-28.10.2026" | No off-exchange block was reported. 1,742,446 shares traded on-exchange on 28.10 alone (market.md §2). No interested-party transaction since 3.8.2026 (Globes, 3.11.2026 18:02) | **Wording wrong.** It was heavy on-exchange selling by holders below 5%. Objection 11 |
| No buybacks at about 3 ILS while options went to the controllers | fy2025 p.69 (no purchases under the 13.11.2024 plan, which runs to 18.11.2026); p.120 (options at 3.01 against 3.19) | Correct |
| C4 passes, A0 cannot be assessed, D8 fails | Outside my lens except D8. Maya is still unread: mayafiles.tase.co.il does not resolve from this session | D8 failure confirmed |

---

## 2. Objections (most severe first)

### O1 (high). "Price well below value" credits leverage and a moat the same file rejects
- **Items:** Q3, D2, D3, D4, A3, A4, A6, E3.
- **What the team says.** The base value is 5.36 and price/base is 0.59. D3 passes with a grid minimum of 4.41
  (out §4-§5).
- **What that base contains.** It is a lender-basis DCF with the on-call bank funding treated as an operating cost,
  ROIIC of 22.2% for ten years and g of 5% (out §3). The team itself says:
  - the gap to the no-leverage value is "exactly the value of the warehouse leverage" (1.41 a share, out §3);
  - the moat items fail (out §6);
  - the earnings-against-assets spread is "explained but not closed" (out §5).
- **What the charter says.**
  - EPV is "normalised unlevered owner earnings ÷ r" (charter, "Valuation methods").
  - Growth adds value only where returns on incremental capital exceed r (framework d3).
  - Base-case inputs are "realistic, erring conservative" (framework (d)).
  - A spread above 30% is resolved before anything else.
- **The unlevered after-tax return on tangible operating capital is 12.1% against r of 10%** (rt §S7). Without
  leverage, growth adds little.
- **On the no-leverage basis (rt §S9):**

  | Measure | Value | Price/value |
  |---|---|---|
  | EPV | 2.95 | |
  | DCF, g 2% | 3.10 | 1.02 |
  | DCF, g 5% | 3.37 | 0.94 |
  | DCF, g 5%, average-capital ROIIC | 3.70 | |
  | Grid minimum (r ± 1, g ± 2) | 2.52 (2.69 on average capital) | below the 3.173 price |

  The shadow-B line on that base would be 1.86-2.03 (rt §S9).
- **The probability-weighted 4.67 also leans on the same base** (rt §S7):
  - red-team weights 20/35/35/10 on the team's values give 3.79;
  - on a ladder whose base is the lender EPV, with the lender DCF as optimistic, they give 3.25;
  - all of these weights are uncalibrated.
- **Required change.**
  - Record Q3 as "no" and D3 as failing on the charter's unlevered EPV.
  - Relabel 5.36 as a "lender-basis, moat-assumed" sensitivity.
  - Restate the base on the no-leverage basis (2.95-3.37) in the summary, the probability weights and any
    re-examination price.
  - Delete "price/base 0.59" from the summary.

### O2 (high). VETO failures missing from the list: B5, B3, A1, A6, and A2 on both clauses
- **Items:** B5, B3, A1, A2, A6.
- **B5 fails on its own wording**: "without 'adjusted' earnings that exclude stock pay".
  - The company's performance measure is "Adjusted EBITDA". It adds back share-based payment: 816 in 2025
    (fy2025 p.67) and 336 in H1 2026 (h1_2026 p.16).
  - It headlines that measure in every directors' report (fy2025 p.64; h1_2026 p.13-14).
- **B5, candour.**
  - "A consistent credit default rate of about 1%, data verified and audited externally by the financial bodies
    buying the loans" (fy2025 p.60; h1_2026 p.6). Over the same six months, on-balance-sheet defaults went from
    0.8% to 2.1% and non-current loans from 2.6% to 4.6% (rt §S3).
  - Management calls this "a negligible change" while "adjusting models and underwriting processes" (h1_2026 p.15;
    fy2025 p.65).
  - Note 13 calls the exposure to Bank of Israel rates "not material" (fy2025 p.101). The directors' report puts it
    at ±1,042 per point (fy2025 p.73).
  - The report says "thousands" of merchants on fy2025 p.14 and "hundreds" on p.43 and p.59 (and h1_2026 p.5).
  - The legal-proceedings sentence gained the word "material" in FY2025 (fy2025 p.54, against fy2024 p.52 and
    fy2023 p.50), with no explanation.
- **B3 (dilution at most 2% a year, stock only for full value).**
  - Shares rose 5.3% in 2025 (rt §S1; fy2025 p.108).
  - Most of the rise was 1,920,000 third-party options, with all 2025 exercises averaging 2.03 a share (rt §S1;
    fy2025 p.112, p.118; h1_2026 p.27). That is 47.6% of the ~4.27 the chairman sold at in August 2025
    (fy2025 p.17).
  - The founders' January 2025 options were struck at 3.01 against a price of 3.19 (fy2025 p.120).
  - Further options went out on 20.8.2026 (h1_2026 p.33). The overhang is 7.3% (rt §S1).
- **A1 (why will it make more in ten years?).** The record gives no answer:
  - merchants can cancel at will (fy2025 p.41);
  - the regulator aims to add entrants [CAL-0923];
  - the negative-data history is cut from 3 years to 1 (h1_2026 p.7);
  - growth has stalled (H1 2026 net income +3.5%), and the run-rate was cut from 640M to 600M (fy2025 p.59;
    h1_2026 p.5).
- **A2, second clause.**
  - The two founders are CEO and CTO and the only independent signatories (fy2025 p.130).
  - Key-person risk is absent from the risk table (fy2025 p.57).
  - The bank lines restrict changes of control (fy2025 p.99).
  - Payments regulation is changing fast: the Payment Services Law, open banking, the BNPL circular.
- **A6.** The unlevered after-tax return is 12.1% against r of 10% (rt §S7). Growth needs equity (business.md §11).
- **Required change.**
  - Record B5, B3, A1 and A6 as "no" (VETO), and A2 as failing on both clauses.
  - Add them to out §6 and to valuation_notes §7.

### O3 (high). Outside evidence of merchant disputes on Paymeant-financed sales: the legal risk is live now
- **Items:** B7, E1, E5, E9, A2, B5.
- **What the press reports (UNVERIFIED: summaries only; the pages returned HTTP 403 to a plain request).**
  - [TM-0618] TheMarker, 18.6.2026, "לקחתם כסף בשמי": dentists who tried a scanner from the merchant Applident
    say they were left owing Paymeant tens of thousands of shekels, even after returning the device within the
    trial period. Paymeant reportedly says it had already paid the merchant and cannot help. Applident rejects the
    fraud claims.
  - [TM-0712] TheMarker, 12.7.2026, "כולם טוענים להונאות": "many customers were burned by Paymeant's and Blender's
    loan machine". The lead says the model gives the lenders an incentive to look away when merchants fall out
    with their customers.
- **What corroborates it.**
  - An anonymous Sponser comment of 28.10.2026 alleges a class action over a merchant that turned customers into
    Paymeant debtors (scuttlebutt.md §3).
  - The FY2025 wording changed to "no **material** legal proceedings" (fy2025 p.54).
  - Equipment and dentistry are core verticals (fy2025 p.40; h1_2026 p.5).
  - The merchant agreement states the company "is not exposed to failure of consideration ... and is not a party to
    the transaction" (fy2025 p.41). That is the position the circular reverses (h1_2026 p.8).
  - [CAL-0923] records complaints to the CMA and the Consumer Protection Authority, lawsuits against BNPL lenders,
    and the CMA's intent that a lender stop paying the merchant when goods are not supplied.
- **Why it matters.** Sold pools carry Paymeant's indemnities "in other cases" (h1_2026 p.7). Disputed loans can
  therefore come back even after a "true sale".
- **Required change.**
  - Add [TM-0618], [TM-0712] and [CAL-0923] to the scuttlebutt (E9).
  - Record B7 as open, failing closed, until the court and class-action registers are searched for
    "פיימנט טכנולוגיות פיננסיות" (515166544) and "אפלידנט".
  - Name this legal path in E1.
  - Add a dated re-examination item.

### O4 (high). The controllers sold at the top and ratcheted their pay; dividends are paid with bank money
- **Items:** B2, B4, F1, F2, E3, E7.
- **The March 2026 sale.**
  - The founders sold 869,564 shares at 6.90, 6.00M ILS or 2.2% of the company, on 13.3.2026 (Globes interested
    parties; rt §S2).
  - That was three weeks after the results-day high (market.md §2) and before the run-rate cut (h1_2026 p.5).
  - It fell between the board's approval of their raise (22.2.2026, fy2025 p.119-120) and the general meeting's
    (30.3.2026, h1_2026 p.19).
  - The price is now 54.0% below that sale (rt §S2).
- **Pay ratcheted after a minority refusal.**
  - On 23.12.2025 the general meeting refused 2 × 500,000 options to the founders (fy2025 p.131).
  - Two months later the board approved +19.6% salaries (rt §S2).
  - The bonus is an uncapped share of pre-tax profit, including unrealised fair-value gains, paid in quarterly
    advances (fy2025 p.119-121).
  - Their 2026 cost is estimated at 5,687 (assumption stated): 30.8% of TTM net income and 4.6% of the market value
    a year (rt §S2).
- **No buyback.** The plan approved on 13.11.2024 was never used and expires on 18.11.2026 (fy2025 p.69).
  - In fairness, a pre-results blackout ahead of the Q3 report (about 17.11.2026) may explain the absence of insider
    and company buying in late October.
  - It does not explain the March sale, or the plan lying unused through 2024-2025.
- **Dividends funded by bank credit** (rt §S6; h1_2026 p.28):
  - FY2025: operating cash flow before bank credit −19,046, against dividends of 9,000;
  - H1 2026: −5,749, against 4,000;
  - bank credit / equity rose from 1.27x to 1.33x.
- **Unread related-party items.**
  - An undescribed June 2023 agreement with the founders was approved under the relief regulations, without a
    general-meeting vote, on the day they sold 1M shares (fy2023 p.57, p.121).
  - The results of the 30.3.2026 meeting are unread.
- **Control and funding are linked.**
  - The founders' joint stake is 29.5%, 4.54 points above the 25% floor of their voting agreement (rt §S2;
    fy2025 p.123).
  - The bank lines restrict changes of control (fy2025 p.99).
  - Pledges are unknown (scuttlebutt §5).
- **Required change.**
  - B4: "no".
  - B2: "no" (plan never used; dividends funded by debt).
  - F1 and F2: "cannot assess here", open, failing closed, and added to the VETO list.
  - E3 records that the sellers before the fall were the most informed holders.
  - Kill condition: the founders' joint stake falls below 25%, or a change-of-control notice is given.

### O5 (medium). TTM is the top of the observed range; the base normalisation does not err conservative
- **Items:** E1, E6, A2 (base-case realism).
- **TTM is two record quarters plus two weaker ones.**
  - TTM pre-tax profit is 24,460 = H2 2025, 13,500 (6,746 and 6,754, fy2025 p.117), plus H1 2026, 10,960 (5,555 and
    5,405, h1_2026 p.24).
  - H1 2026 annualised is 21,920: 10.4% below TTM, and below the team's EBIT_norm of 22,624 (rt §S4).
- **Two internal estimates disagree, and the valuation took the higher.** The business workstream's normalised
  base (net 15,923) is 8.6% below OE_norm of 17,421 (rt §S7).
- **The low credit-loss line says nothing about credit cost.** Credit losses on fair-value loans sit inside revenue
  (h1_2026 p.13), so the 1,012 line does not measure them. Defaults rose x2.97 (rt §S3).
- **The fee growth carries guarantee risk.**
  - Fees rose 40.7% in H1 2026 (rt §S4), "mainly" from the 360 product (h1_2026 p.13). 360 is a payment-operations
    and payment-guarantee product (fy2025 p.39-40).
  - Its deferred income sits in payables that are up x3.75 since the end of 2024 (rt §S4; fy2025 p.62;
    h1_2026 p.11).
  - No guarantee exposure is disclosed.
  - The guarantees market is being licensed (scuttlebutt §1.4).
- **The window holds no credit cycle.**
- **Required change.**
  - Base on the lower normalisation, or on the H1 2026 run-rate, with g no higher than CPI. Even on the lender basis
    this gives an EPV of 3.98 and a DCF (g 2%) of 4.31 (rt §S7).
  - Exclude 360 fee growth from base growth until its exposure is disclosed.

### O6 (medium). The shadow Tier B buy price misleads; the only fitting tier is C, at 1.10
- **Items:** G4, D2, H4, H5, A3.
- **The print.** out §5 shows "buy price (shadow Tier B) 2.95" and "price / buy price 1.08".
- **Why B is the wrong reference.**
  - A credit-cyclical lender belongs in the cheap track, as the brief's precedent for cyclicals sets: grade C, with
    no net debt. Paymeant's net debt with leases is 112,942 (out §1b).
  - The Tier C line is 1.10, so the price is 2.89x it (rt §S7). The bank route gives 2.40, so the price is 1.32x it.
- **Lane C fails on more than the team lists.**
  - H5: a cyclical with net debt.
  - H4: there is no catalyst, and the buyback lapses on 18.11.2026.
- **The peer returns.** They exist (scuttlebutt §1.2), but they are TTM only. They are also flattered by gain-on-sale
  through own SPCs: 304M sold since 1.2025, 1.45x the on-balance-sheet book (rt §S5).
- **Required change.**
  - Remove the shadow-B price from the summary, or print "no buy price under any lane (Tier C 1.10; bank route
    2.40)".
  - Record H4 and H5 as failing.
  - Correct the "no peer returns" wording.

### O7 (medium). The pre-mortem must name the path, its signals and its dates
- **Items:** E1, E2, A2, C1.
- **Buffett's bank test (framework f3).** Pre-provision pre-tax profit (TTM 25,472) is 12.1% of the on-balance-sheet
  book (rt §S5).
- **Covenant.** The 20% tangible-equity covenant breaks at a loss of 42,385, 20.2% of the book (rt §S5).
- **The SPC pools.**
  - The 304M sold since 1.2025 carry indemnities (h1_2026 p.7).
  - The deferred price is released "according to the rate of repayment" (fy2025 p.108).
- **What stops when origination stops.** Fees are 55.1% of H1 2026 revenue (rt §S4), while opex of about 28,857
  continues.
- **Required change.**
  - Write the chain in §4 into the thesis file.
  - Add kill conditions:
    - any SPC indemnity or repurchase claim, or any cut in a bank line, is disclosed;
    - non-current loans exceed 6% of the book at a quarter-end (red-team proposal).

### O8 (medium). Classify as TOO_HARD, so that a lower price never reopens the file on its own
- **Items:** A0, A1, A2, E9, D8.
- **The business workstream already concluded it.** business.md §14: "TOO_HARD as a moat or compounder case".
- **The key figures cannot be verified:**
  - losses on sold pools;
  - the SPC lender, terms and indemnity caps;
  - the 360 guarantee volume;
  - the October seller;
  - litigation.
- **Sources are unread or unreachable.**
  - The Maya filings since 30.6.2026 are unread.
  - From this session, mayafiles.tase.co.il, themarker.com and calcalist.co.il do not resolve through WebFetch, and
    TheMarker returns 403.
- **The team's re-examination trigger 3 is a price.**
- **Required change.**
  - File it as TOO_HARD, or as NO_THESIS with the line "price is not a re-examination trigger".
  - Reopen only on the structural disclosures in §8.

### O9 (medium). E3 and the Petco rule: on lender metrics there is little discount to explain
- **Items:** E3, E7, F6.
- **The market prices about the no-leverage value.**
  - On the EV basis, implied growth is +2.8% at an unlevered ROIIC of 12.1%, and price/EPV is 1.07 (out §3).
- **Against Israeli specialist lenders** (scuttlebutt §1.2):

  | Metric | Peer median | Paymeant |
  |---|---|---|
  | P/E | 7.67 | 6.93 |
  | P/B | 1.37 | 1.44 (P/TBV 1.59, out §0) |

  It is cheaper on earnings and dearer on book, with on-call funding.
- **Why the headline looks cheap.** TASE classes the stock as "Software & Internet", so Mega shows a software framing
  ("P/E 6.6, 88% gross"; scuttlebutt §6).
- **Required change.**
  - Lead Q4 with the EV-basis implied growth and the peer P/B.
  - State that what remains of the discount is explained by known facts: funding, insider selling and illiquidity.

### O10 (low). E8 is stated on the wrong basis; the failure stands
- **Items:** E8, C3.
- **Bank B is not the whole story.** Bank B had 88.5% of drawn credit, but lines A and D (189,000) were unused
  (rt §S6; fy2025 p.49).
- **The real single variable** is the banks' collective appetite for consumer credit at the point of sale. All lines
  are on-call (fy2025 p.55), and one SPC lender funds the take-outs (fy2025 p.51-53).
- **Required change.** Restate E8 on the systemic basis.

### O11 (low). Record hygiene
- **Items:** F6, E3, D7.
- **Liquidity figures disagree** (rt §S8):

  | Measure | out §6 | scuttlebutt §7 |
  |---|---|---|
  | Median daily turnover | 17,757 | 19,125 |
  | 25th percentile | 1,735 | 2,590 |
  | Liquidity cap | 6,940 | 10,361 |

  The two use different windows and sources.
- **"Block sale"** is the wrong description of the October selling (§1).
- **Required change.** Use one dated primary series, Bizportal's daily proceeds, and correct the wording.

---

## 3. The bear case, argued as the best bear would (E4)

**What it is.** Paymeant is a 125M-shekel consumer lender dressed as a fintech.
- It writes 14-month instalment loans at the till of aesthetics clinics, dentists and equipment sellers.
- It funds them on four on-call bank lines. One bank held 88.5% of the drawn credit at year-end.
- It sells the loans and books the gain up front. Since 2025 the sales have gone almost entirely to its own
  unconsolidated SPCs, which a bank finances. The company keeps the indemnities and a deferred price.

**Who it depends on.** Every shekel of profit depends on three counterparties saying yes: the warehouse banks, the
SPC lender and the regulator. In 2026 all three moved against it.
- The BNPL circular makes the lender answer for merchants that do not deliver (from 12.1.2027).
- The Credit Data Law amendment cuts the negative-data history that instant scoring relies on.
- The press began documenting merchant disputes on Paymeant-financed sales, in June and July 2026.

**Credit is turning.**
- Defaults rose almost threefold in six months.
- Management called the change negligible and quietly tightened underwriting.
- Growth stalled: the run-rate was cut from 640M to 600M, and Q2 net income fell.

**The insiders.**
- The founders sold at 6.90 three weeks after the results-day high.
- That was after they pushed through a 19.6% raise, two months after the minority refused them a million options.
- The buyback approved at the 2024 low was never used.

**Where the profit goes.**
- Roughly 30% of what is left goes to the controllers (estimate, rt §S2).
- About half is paid out in dividends that are funded with borrowed bank money.

**The price.**
- On the charter's own no-leverage EPV the stock is fairly priced: 2.95 to 3.37, against 3.173.
- The grid minimum is 2.52.
- The only lane it fits, C, would pay 1.10.

**The October fall.** A 47% fall in a week with no news, in a stock whose best-informed holders were sellers, is
not an opportunity until someone explains it.

---

## 4. Pre-mortem: it is 2031 and this was a permanent loss (E1)

**Scenario.**
1. **2027.** The circular is in force. A clinic chain or equipment merchant financed through Paymeant fails, or is
   shown to have mis-sold. Borrowers cancel or refuse to pay, and class actions follow (O3).
2. **The SPC claims.** The SPC's bank claims under the representations and indemnities on the sold pools
   (h1_2026 p.7).
3. **Pricing tightens.** The take-out bank pauses or reprices. At the same time the shorter negative-data history
   raises defaults on new loans.
4. **Funding shrinks.** The warehouse banks cut their on-call lines. Origination stops, and with it the fees: 55.1%
   of revenue (rt §S4). Opex (28,857 TTM, rt §S4) does not stop.
5. **Losses.** Losses run through the 20% tangible-equity covenant (breaks at a loss of 42,385, rt §S5), or the
   banks call the lines without one.
6. **Rescue.**
   - The company raises equity at a deep discount from block holders, which is **marker 1**.
   - Or it carries a going-concern note while it runs the book off, which is **marker 2**.
   - Marker 3, assets worth less than debt, is unlikely on the balance sheet. It is possible only through
     undisclosed off-balance-sheet claims.

**Early-warning signals and their dates:**

| When | What to watch |
|---|---|
| Q3 2026 report, about 17.11.2026 | Arrears; the bank-line table; any SPC disclosure |
| Mid-November 2026 | October fund holdings: who sold |
| FY2026 report, about February 2027 | Lines, lenders, the guarantee note |
| Q1 2027 report, about May 2027 | Arrears after the circular |
| Ongoing | Any immediate report on lines, SPCs or litigation |

**Reading.** A plausible path exists to markers 1 and 2, so E1 fails, and the charter rejects it "regardless of
expected value".

---

## 5. Would Buffett, Munger, Pabrai or Li Lu buy it? No

- **Buffett.**
  - "Never depend on the kindness of strangers" [BH2009]. Here every line is on-call and the take-outs depend on one
    SPC lender.
  - Never buy a poorly run bank cheap [BH1990]. This is a non-bank with no deposit franchise and no moat, so the
    excess return is not durable.
- **Munger.**
  - Invert: the business dies the day two banks say no.
  - Incentives: the controllers are paid on accounting profit, including unrealised fair-value gains.
  - Too hard.
- **Pabrai.**
  - His checklist exists because Delta Financial went to zero: a consumer lender on warehouse lines, selling loans
    into its own securitisations on gain-on-sale accounting [P-PKU2017].
  - "Heads I win, tails I don't lose much" fails, because tails is dilution.
- **Li Lu.**
  - To know it better than the market you need loss curves of sold pools, the SPC terms and the guarantee book. None
    is public.
  - The worst case cannot be estimated "with confidence" (A2).

---

## 6. The Petco rule (E3)

- **No material discount on lender metrics** (O9).
- **What is left is explained by known facts that cannot be refuted from the record:**
  - on-call, concentrated funding;
  - credit turning;
  - the circular;
  - insiders selling near the top;
  - illiquidity;
  - press-documented merchant disputes.
- **Verdict:** priced. NO_THESIS on E3, for a stronger reason than the one recorded.

---

## 7. Checklist answers in my lens (team answer, then red team)

| Item | Team | Red team | Evidence |
|---|---|---|---|
| A0 | Cannot assess | Cannot assess, fails closed | CIRCLE.md unavailable |
| A1 | Not listed | **No (VETO)** | O2 |
| A2 | No (worst case) | **No, on both clauses** | O2, §4 |
| A3 | No | No; the peer-return wording needs correcting | O6 |
| A4 | No | No. The regulator is deliberately adding entrants, and payment fintechs can now lend | [CAL-0923]; business.md §5 |
| A5 (FLAG) | — | No. Borrower rate −187bp; merchants can leave | business.md §11 |
| A6 | Not listed | **No (VETO)** | O2; rt §S7 |
| A7 (FLAG) | — | Don't know. Blender lost money; Hapoalim exited; the regulator is adding entrants | scuttlebutt §1 |
| A8 (FLAG) | — | No. "New and exciting"; a CPI-linked book needs more equity as CPI rises | fy2025 p.71; business.md §11 |
| B1 (FLAG) | — | Not decisive. Much of the book growth came from the 2022 placement | governance_risk.md §5 |
| B2 (FLAG) | — | No. Plan never used; dividends funded by debt | O4 |
| B3 | Not listed | **No (VETO)** | O2 |
| B4 (FLAG) | — | No | O4 |
| B5 | "Candour mixed" | **No (VETO)** | O2 |
| B6 (FLAG) | — | Yes. No acquisitions | fy2025 p.47 |
| B7 | Pass on the record checked, courts open | **Open, fails closed** | O3 |
| E1 | Fails | Fails, with a named path | §4 |
| E2 | Re-examination conditions | Replace the price trigger with structural items | §8 |
| E3 | Priced (Petco) | Priced, with little discount on lender metrics | O9 |
| E4 (FLAG) | — | §3 | |
| E5 (FLAG) | Done | Add: the regulator's intent to add entrants; lenders answerable for merchants; banks buy loans, not platforms | [CAL-0923]; scuttlebutt §1.4 |
| E6 (FLAG) | — | Not written. In 5-10 years: a bank-owned origination channel, a regulated niche, or a run-off | — |
| E7 (FLAG) | — | Watch social proof (Gonen, 9.48%) and anchoring on 6.90 or 5.61 | scuttlebutt §5 |
| E8 | Fails (one bank) | Fails on the systemic basis | O10 |
| E9 (FLAG) | Done | **Incomplete**: TheMarker June and July 2026 missing | O3 |
| F1 | Pledges unverified | **Cannot assess, open, fails closed** | O4 |
| F2 | Not listed | **Cannot assess, open, fails closed** | O4 |
| F5 | — | n/a, not a holdco. The SPCs are not consolidated, which is noted | fy2025 p.94 |
| F6 (FLAG) | Raised | Raised; figures to reconcile | O11 |
| H1 | — | Yes in outline | business.md §0 |
| H2 | — | Partly. The fair-value step-up is model-based and the key audit matter | h1_2026 p.31; governance_risk.md §2.2 |
| H3 | — | Yes, on reported operating cash flow (which includes bank-credit changes) | h1_2026 p.28 |
| H4 | Not listed | **No** | O6 |
| H5 | Not listed | **No** | O6 |
| H6 | n/a | n/a | — |

---

## 8. Li Lu's categories, and re-examination items

- **What we know.**
  - The funding is on-call and concentrated.
  - Credit worsened in H1 2026.
  - Insiders sold at 6.90.
  - The circular and the Credit Data Law amendment.
  - The press reports of merchant disputes.
- **What we do not know.**
  - The October seller.
  - Whether a class action exists.
  - The SPC lender and indemnity caps.
  - The guarantee volume.
  - The pledges.
  - The terms of the June 2023 agreement.
  - Why shares in Paymeant Series 1 changed hands on 10.9.2026 (registrar file, scuttlebutt.md §3).
- **What we do not need to know.** Global BNPL growth.
- **What could be unknown to us.** Claims on sold pools, and losses under the guarantee.

**Reopen only when all of these hold (dated):**
1. The FY2026 report (about February 2027) shows:
   - committed funding of at least two years from at least two unrelated funders;
   - no bank above 50% of drawn credit;
   - the SPC and guarantee maximum exposures quantified.
2. Non-current loans are at or below 2.6% in the first report after 12.1.2027 (Q1 2027, about May 2027).
3. The court and class-action registers have been searched, and the Maya reports of September-November 2026 have
   been read, including the Series 1 transfer and the October seller.
4. F1 and F2 are closed: the founders' pledges and the June 2023 agreement are known.

Only then is price relevant, and the reference value is the no-leverage base (O1), not 5.36.

---

## 9. Pages re-read on the image

| Document | Pages |
|---|---|
| paymeant_fy2023 | p.107 |
| paymeant_fy2025 | p.39-45, p.47-53, p.55-73, p.93-95, p.99-101, p.106-108, p.117-124 |
| paymeant_h1_2026 | p.5-19, p.24-33 |

Text-only checks (used for text, not table figures):
- fy2023 p.57, p.121;
- fy2025 p.14, p.17, p.54, p.112, p.130, p.131;
- fy2024 p.52;
- fy2023 p.50.

## 10. Sources outside the filings

| Key | Item | Status |
|---|---|---|
| [TM-0618] | TheMarker, 18.6.2026, "'לקחתם כסף בשמי': רופאי שיניים רכשו ציוד — והסתבכו בהלוואות שלא רצו", https://www.themarker.com/law/2026-06-18/ty-article/.highlight/0000019e-cf4c-d45a-ab9e-cfeec4490000 | Search summary only; **UNVERIFIED** |
| [TM-0712] | TheMarker, 12.7.2026, "'כולם טוענים להונאות': לקוחות רבים נכוו ממכונת ההלוואות של פיימנט ובלנדר", https://www.themarker.com/law/2026-07-12/ty-article-magazine/.highlight/0000019f-4153-d07c-af9f-c95f90af0000 | Plain curl returned HTTP 403 at 21:58 (empty file `redteam_web/tm_law_20260712.html`); **UNVERIFIED** |
| [CAL-0923] | Calcalist, 23.9.2024, "הרגולטור מנסה לעשות סדר בשוק הפרוע של 'קנה עכשיו, שלם אח"כ'", https://www.calcalist.co.il/investing/article/hj3y11krac | Read 21:58; saved as `redteam_web/cal_hj3y11krac.html` |
| [GL-MAYA] | Globes Maya headline feed, https://www.globes.co.il/news/Instrument/InstrumentHandlers/Get_Instrument_BursaMessage.ashx?instrumentid=370226&feeder=&maxItemsToShow=60 | Read 21:52; saved as `redteam_web/globes_maya60.html`. There is no report after the 28.10.2026 clarification |
| Globes interested parties | `scuttle/web/globes_ip.json` (as of 3.11.2026 18:02) | Read |

**Not reachable from this session.**
- mayafiles.tase.co.il, www.bizportal.co.il, www.themarker.com and www.calcalist.co.il do not resolve through
  WebFetch. They need to be allowed in the session's network settings for a re-check.
- A plain curl from the shell did reach Calcalist and the Globes feed. TheMarker answered it with HTTP 403, which was
  not retried.

**Not found.** A class action against the company, in web searches in Hebrew and English.

## Files

- `/tmp/claude-0/-home-user-value-investing-fund---selected-company-reaserch/8e9bb9a6-b39f-5c24-a635-b21606f1c8ae/scratchpad/work/paymeant/redteam_calc/redteam_business_calc.py`
- `/tmp/claude-0/-home-user-value-investing-fund---selected-company-reaserch/8e9bb9a6-b39f-5c24-a635-b21606f1c8ae/scratchpad/work/paymeant/redteam_calc/redteam_business_calc_output.txt`
- `/tmp/claude-0/-home-user-value-investing-fund---selected-company-reaserch/8e9bb9a6-b39f-5c24-a635-b21606f1c8ae/scratchpad/work/paymeant/redteam_web/`
