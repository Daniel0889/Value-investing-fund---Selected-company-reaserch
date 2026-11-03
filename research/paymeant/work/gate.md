# Paymeant Financial Technologies (TASE 1180876): CIO gate

Written 3.11.2026 (Israel time) under charter Revision 4 ("Text to paste" in `charter_rev4_draft.md` governs).

**How to read this file.**
- **Numbers.** Every number is printed by `research/paymeant/valuation.py`, cited "out §n" from
  `research/paymeant/output.txt`, or is a filed figure with its PDF page. The pages were opened as images.
- **Files.** Workstream files are in `work/paymeant/`. The checklist is `work/paymeant/checklist.md`.
- **Units.** Per-share values are in ILS per diluted share (1 ILS = 100 agorot).

---

## 0. Verdict: NO_THESIS

| Per diluted share (ILS) | Value | Source |
|---|---|---|
| Price, official close 3.11.2026 | 3.173 | out §0 |
| Worst case (run-off of the 30.6.2026 book) | 0.59 to 1.09 | out §4 |
| Conservative (no moat: amortised-cost tangible book less the UNVERIFIED provision shortfall) | 1.75 | out §4 |
| **Base** (ten-year DCF, lender basis, charter normalisation, g 2%) | **2.19** | out §3-§4 |
| Optimistic (today's scale holds, g 5%) | 4.68 | out §4 |
| Probability-weighted (15/25/40/20, uncalibrated) | 2.34 | out §4 |
| Buy price | **none: no lane fits** | out §5 |
| Reference only: Tier C net-net line / bank-route line | 1.09 / 2.28 | out §5 |

**Why NO_THESIS.**
- **No lane fits** (G4):
  - Lanes A and B fail on the moat, leverage and funding.
  - Lane C fails because the stock is not a net-net, has net debt and has no catalyst.
  - Lane D needs an A/B franchise, and there is none. Lane E needs an announced deal, and there is none.
- **The price is not below value.** It is 1.45x the base. The whole sensitivity grid (1.95-2.55) sits below it.
- **The price pays for today's scale persisting.** It implies −3.2% a year on today's scale, and +5.3% to +13.8% on
  the charter's normalisation.
- **What is left of the discount is priced.** Known facts the filings do not refute explain it (the Petco rule).
- **Many VETO items fail on verified pages:**

  | Item | Failure |
  |---|---|
  | C1, C3, E8 | Funding is on-call and concentrated |
  | C2 | Net debt is 9.6x normalised EBIT |
  | E1 | Plausible paths lead to impairment markers 1 and 2 |
  | A3, A4, A6 | No moat |
  | B3 | Dilution of 5.3% in 2025 |
  | B5 | "Adjusted EBITDA" adds back stock pay |
  | D2, D3, D5 | Price |
  | C7, F4, H2, H4, H5 | See checklist.md |

**Why not WATCHLIST.** Price is not the only failure.

**Why not TOO_HARD.**
- The deciding failures rest on filed pages, read as images.
- Those failures would stand even if every unverifiable figure resolved favourably. The unverifiable figures are
  the Level 2 marks, the SPC and 360 exposures and the economic credit cost.
- The TOO_HARD key-figure test is met in part, and that is recorded.

**Price alone never reopens this file** (§10).

---

## 1. The red-team objections: the decision on each

Reviewers: **paymeant:redteam-accounting** (B1-B12, `redteam_accounting.md`) and **paymeant:redteam-business**
(O1-O11, `redteam_business.md`).

- **Accepted:** 18.
- **Accepted in part:** 4 (B2, O1, O4, O8).
- **Rejected:** 1 (B11).

Each accepted change is implemented in `valuation.py`, which was re-run to produce `output.txt`.

| ID | Objection | Decision | Evidence, and what changed |
|---|---|---|---|
| B1 (high) | The base value, the D3 pass and the −4.7% implied growth rest on adding back IPO share-based pay. FY2021 was then a loss, so the business is cyclical | **Accepted** | Read on the images: paymeant_fy2023 p.82 (FY2021: 1,516 before other items, other items (2,285), pre-tax (769)) and p.111 (note 19e: 288 / 751 / 228 IPO grant and share-based pay; 1,997 of options vested immediately; (1,188) termination income). screen_spec 2.3 has no pay add-back, and framework d1 forbids one. EBIT_adj is rebuilt with only the 1,188 gain removed. The business is now cyclical; EBIT_norm is 11,707 and the base 2.19. D3 fails on a grid of 1.95-2.55. C5 passes on the rebuilt figure (out §2-§4) |
| B2 (med) | The headline numbers sit on a "lender basis" outside the charter. The EV basis fails D3, and the method spread is unresolved | **Accepted in part** | **Accepted:** both bases are printed. D3, Q3 and Q4 fail on both: the lender grid is 1.95-2.55 and the EV grid 2.44-4.52. The shadow price is withdrawn. **Rejected:** that the EV basis is charter-literal for a lender. screen_spec 3.1 says "EBIT, EV and ROIC [are] meaningless" for financials and routes lenders to the bank route, which judges equity. On the charter normalisation the EV basis values the equity at 0.11, below the book's run-off value (out §3). The method spread is now 10% (EPV 2.15, DCF 2.19, tangible book 1.99), so D1 is resolved (out §5) |
| B3 (low) | TTM counted as a sixth year | **Accepted** | Framework d2 and screen_spec 2.2 define W as fiscal years. W is now FY2021-FY2025, and TTM supplies only Rev_ttm (out §2) |
| B4 (med) | Capitalised development flatters the trend, and controllers' pay is capitalised | **Accepted** | Read: h1_2026 p.13 and p.28; fy2023 p.98; fy2025 p.98 and p.115. H1 2026 pre-tax growth was −4.2% before net capitalisation, against +6.7% reported. Maintenance capex is now at the H1 run-rate (3,514), the base growth at CPI (2%), and C4 and B4 are "no". **One correction:** net capitalisation fell from 2,250 (FY2022) to −613 (FY2025). The annual record is therefore not flattered (per share +35.3% a year before net capitalisation, +24.7% reported); only the latest half is (out §2) |
| B5 (med) | The credit cost is invisible, and provision coverage fell as defaults trebled | **Accepted** | Read: fy2025 p.95 (5,731 gross, 934 provision), fy2025 p.66 and h1_2026 p.15 (defaults 1,481 to 4,395; "a negligible change"). The economic credit cost is UNVERIFIED. The f3 stress covers defaults of 20.2% of the book at 60% severity. The shortfall is 2,791-8,651 if the defaulted loans sit in the amortised-cost book [UNVERIFIED]. The conservative case deducts the 50% shortfall; the worst case takes defaults at 30% (out §4) |
| B6 (med) | Three covenants and the change-of-control clause are missing, and C1 is unanswered | **Accepted** | Read: fy2025 p.99 lists four ratios (TE ≥ 20% of the balance sheet; TE ≥ 25M; senior debt ≤ 80% of loans; annual net profit ≥ 1M), restrictions on a change of control, and grounds for immediate repayment. All are now in code. The profit covenant is the nearest: it breaks after a pre-tax fall of 23,161, which a 50.8% fall in originations would cause. C1 is "no" (out §4) |
| B7 (med) | The F4 stress leaves out the sale-price and fair-value channels | **Accepted** | Read: fy2025 p.51 (sale price discounted off government bonds plus a margin); h1_2026 p.10 (indirect effect on the consideration in assignments); fy2025 p.42 (14 months is the loans' average duration, מח"מ). Three channels, a six-month repricing lag. The first-year hit is 8,545-10,916, or 35-45% of TTM pre-tax. On normalised earnings the profit covenant breaks in the 14-month case. F4 is "no" (out §4) |
| B8 (med) | The Level 2 marks against the company's own SPCs, the retained SPC exposure, the 360 guarantee and the credit cost cannot be verified | **Accepted** | Listed as UNVERIFIED (§5). The conservative case strips the 9,515 step-up after tax and the shortfall. SPC-consolidated leverage "cannot be computed" (out §1b). The TOO_HARD test is met in part, but the verdict does not depend on it (§0) |
| B9 (low) | The worst case is overstated | **Accepted** | The worst case is now 0.59-1.09, and sizing uses 0.59 (L_worst 81.3%) (out §4, §6) |
| B10 (low) | Dilution is understated, and B3 is unanswered | **Accepted** | Read: fy2025 p.110-112 and p.123; fy2023 p.107. Treasury method, instrument by instrument: 309,797 dilutive shares at the price. Every per-share value is diluted. B3 is "no" (+19.4% in 2022, +5.3% in 2025). Note 17 and Reg. 24A do not reconcile (out §0, §2) |
| B11 (low) | Tax at 23% although the effective rate runs higher | **Rejected** | fy2025 p.106 (image): the reconciliation's "other" was −79, −35 and +116 in 2023-2025, so it alternates in sign. The cumulative FY2023-FY2025 effective rate is 23.01%. The statutory rate therefore passes the check that framework (d)'s notation asks for. Sensitivity at the TTM rate of 24.5%: base 2.13 (−2.3%) (out §2, §4) |
| B12 (low) | The H1 2025 cash flow does not reconcile, bank credit sits inside OCF, and the covenant TE does not match | **Accepted** | Read: h1_2026 p.28 (H1 2025 shows no tax paid; Q2 2025 no interest received). The TTM cash figures are marked unreconciled and are not used as evidence. C7 is "no". Covenant headroom is shown on both definitions (42,385 / 39,742) (out §2, §4) |
| O1 (high) | "Price well below value" credits leverage and a moat the file rejects | **Accepted in part** | The 5.36 base and "price/base 0.59" are withdrawn; Q3 is "no" and D3 fails. The adopted base (2.19, lender basis, charter normalisation) is below the red team's no-leverage 2.95-3.37. The EV basis is therefore a cross-check, not the base (see B2) |
| O2 (high) | B5, B3, A1 and A6 fail, and A2 fails on both clauses | **Accepted** | All recorded as "no". Read: fy2025 p.66-67 (Adjusted EBITDA adds back share-based pay); fy2025 p.60 and h1_2026 p.6 ("about 1%"); fy2025 p.54 against fy2024 p.52 ("material" added). **Nuance:** the "about 1%" may measure sold pools (fy2025 p.42), so B5 rests on the adjusted measure and the "negligible" wording. The note-13 rate wording was not re-checked by the CIO |
| O3 (high) | The press reports merchant disputes on Paymeant-financed sales | **Accepted** | A search on 3.11.2026 confirmed both TheMarker headlines, their dates and URLs (18.6.2026 and 12.7.2026, §11). The article bodies are UNVERIFIED: themarker.com does not resolve here. No class action naming Paymeant was found. B7 stays open; E1 names the path (h1_2026 p.7-8) |
| O4 (high) | The controllers sold at the top and ratcheted their pay; dividends are paid with bank money | **Accepted in part** | **Accepted:** B4 is "no"; F1 and F2 are "cannot assess here"; E3 records the informed sellers; the founders' stake is a kill condition (§9). OCF before bank credit was −19,046 in FY2025, against dividends of 9,000 (out §2). **Rejected:** B2 "no". B2 tests buybacks that were made, and none was made (fy2025 p.112; h1_2026 p.25). At the revised base, not buying was right. The unused plan is a B5 point |
| O5 (med) | TTM is the top of the range, and the base normalisation is not conservative | **Accepted** | The adopted EBIT_norm of 11,707 is below the business workstream's 20,679 that the red team proposed. Base growth is at CPI, and 360 fee growth is not in the base (out §2-§3) |
| O6 (med) | The shadow Tier B price misleads; H4 and H5 fail; the peer wording is wrong | **Accepted** | The shadow price is withdrawn. Only reference lines remain (Tier C 1.09; bank route 2.28). H4 and H5 are "no". A3 now cites the TTM peer returns (out §5; checklist A3) |
| O7 (med) | The pre-mortem must name the path, its dates and the kill conditions | **Accepted** | §9 |
| O8 (med) | File as TOO_HARD, or as NO_THESIS with price never reopening the file | **Accepted in part** | Filed as NO_THESIS with "price alone never reopens the file" (§10). The TOO_HARD label is rejected, for the reason given in §0 |
| O9 (med) | E3 is framed on the lender basis, but there is little discount on lender metrics | **Accepted** | Q4 now leads with today's scale (−3.2% implied) and the peers: P/E −11.9% and P/B +4.8% against the Israeli specialist-lender medians. There is no material discount (out §6) |
| O10 (low) | E8 is stated on the wrong basis | **Accepted** | Restated as dependence on Israeli banks' collective appetite. There are four on-call lines; A and D are unused (189,000); bank B holds 88.5% of drawn credit; one bank funds the SPCs (out §1b; fy2025 p.49, p.108) |
| O11 (low) | The liquidity figures disagree, and "block sale" is the wrong word | **Accepted** | One primary series is used: Bizportal's daily proceeds (median 19,125; 25th percentile 2,590; cap 10,361). The first version's series missed the 12.10.2026 session. The October event is now "heavy on-exchange selling by holders under 5%, seller unidentified" (out §6) |

---

## 2. The CIO's own reading: the bear case (E4) and the misjudgment check (E7)

**The bear case, which the CIO accepts.**
- **What the business is.** A 125M-shekel point-of-sale consumer lender. It funds about 210M of loans on four on-call
  bank lines and sells pools to its own unconsolidated SPCs, which one bank finances.
- **Every shekel of profit needs three yeses:**
  - the warehouse banks, who "may stop the engagement unilaterally" (fy2025 p.55);
  - the SPC lender;
  - the regulator, whose circular makes the lender answer for merchants that fail to deliver from 12.1.2027 (h1_2026 p.8).
- **In 2026 the signals turned:**
  - defaults rose 2.97 times in six months, and management called it "negligible";
  - underlying pre-tax growth was −4.2% in H1;
  - the founders sold at 6.90 between the board's and the meeting's approval of their raise.
- **On the charter's own arithmetic the stock is above value.** It is 1.45x base; even the bank route's own line is 2.28
  (out §5).
- **Inversion.** It dies the day two banks say no.

**The misjudgment check (E7).**
- **Incentive bias in guidance.**
  - The run-rate was cut from 640M to 600M (fy2025 p.59; h1_2026 p.5), with no forecast given.
  - The "about 1%" default claim and the Adjusted EBITDA headline are management framing.
  - Neither was used as an input.
- **Consistency with our own earlier work.** The first version's base of 5.36 was revised down to 2.19 against the
  price, not toward it.
- **Social proof.** Alon Gonen (Plus500 co-founder) holds 9.48% (scuttlebutt.md §5). That is not evidence of value.
- **Anchoring.** None of these is a value:
  - 6.90, the founders' sale;
  - 5.61, the option-grant price (h1_2026 p.33);
  - 5.36, the first version's base.
- **Deprival.** The 47% October fall makes the stock look cheap. A fall is not a reason to buy (charter rule 7).

---

## 3. The investment test (four questions, in order) and who is selling

1. **Inside the circle?**
   - Cannot be assessed here, because `theses/CIRCLE.md` is not available.
   - The model is on the avoid list: "dependent on refinancing markets ... Delta Financial's warehouse lines"
     (framework f2).
   - Fails closed. Goes to the principal.
2. **A good business by its lane?** No lane fits (§0).
3. **Price well below value?** No (out §6):
   - price / base 1.45;
   - price / EPV 1.47;
   - price / tangible book 1.60;
   - probability-weighted value 2.34.
4. **What does the price assume, and why is that wrong?**
   - **What it assumes** (out §6):
     - On today's scale (optimistic owner earnings of 15,761), the price implies −3.2% a year: it pays for today's
       earnings persisting.
     - On the charter's normalisation it needs +5.3% a year if growth were free, and +13.8% with the reinvestment
       charged.
     - It equals the probability-weighted value only if the optimistic case carries 49% of the weight (out §4).
   - **Why that cannot be called wrong.**
     - The record cannot show it is too pessimistic: H1 2026 underlying pre-tax growth was −4.2% (out §2).
     - Against Israeli specialist lenders, P/E is 11.9% below the median and P/B 4.8% above it.
     - What remains is explained by known facts the filings do not refute: funding, credit, the circular, informed
       selling and illiquidity. **Priced (the Petco rule).**
   - **Who is selling, and why** (Klarman's question):
     - The founders sold 869,564 shares at 6.90 on 13.3.2026. The price is now 54.0% below that (out §6; Globes, one
       source).
     - Mor, the 2022 anchor institution, has left the register (scuttlebutt.md §6).
     - From 20.10 to 3.11.2026, 8.86% of the company traded on-exchange (out §6). No holder above 5% reported a sale,
       so the seller is unidentified.
     - The most informed holders were sellers.

The VETO failures are listed in `checklist.md`: 23 answered "no" and 6 "cannot assess here".

---

## 4. Three falsification conditions (specific, observable, dated)

These test the NO_THESIS reading. If one is met, the file reopens for a full re-underwriting. It is not a buy signal.

1. **Funding becomes committed, and the off-balance-sheet exposures are sized.**
   - **When:** the FY2026 annual report, expected late February 2027 and due by 31.3.2027.
   - **The test:**
     - committed facilities with at least 24 months to run;
     - from at least two unrelated funders;
     - covering at least the credit drawn at that date;
     - no single bank above 50% of drawn credit (today's line table is fy2025 p.49, the covenants p.99);
     - the maximum exposure under the SPC indemnities and the 360 guarantee quantified.
   - **What it falsifies:** C1, C3, E8 and the funding path in E1.
2. **Credit holds under the circular.**
   - **When:** the Q1 2027 report, expected by 31.5.2027. It is the first quarter with the BNPL circular in force (from
     12.1.2027).
   - **The test:**
     - loans 1-90 days past due plus defaulted loans at or below 2.65% of the on-balance-sheet book (the 31.12.2025
       level; out §4, from fy2025 p.66);
     - the gross amortised-cost book and its provision disclosed, with coverage of at least 50%.
   - **What it falsifies:** the credit-turn reading and the unknown credit cost (A2, B5).
3. **Today's scale proves durable.**
   - **When:** the FY2026 report (February-March 2027) and the H1 2027 report (expected by 31.8.2027).
   - **The test:** pre-tax profit before net capitalisation of development, for FY2026 and for H1 2027 annualised, both
     at or above the TTM pre-tax of 24,460 (out §2), with the circular in force.
   - **What it falsifies:** Q3 and Q4. The charter's cyclical normalisation of 11,707 would then understate earning
     power.

---

## 5. Li Lu's four categories (E9)

- **What we know** (verified on the filing pages):
  - **The business.** It earns fees, gains on loan sales and interest. Funding is on-call: bank B held 88.5% of drawn
    credit, and the funders may stop unilaterally.
  - **Covenants.** There are four, plus change-of-control restrictions.
  - **Credit.** Defaults rose 2.97 times in H1 2026, and provision coverage fell to 16.3% (2025).
  - **Earnings quality.** Capitalisation rose to 34% of gross R&D, and part of the controllers' pay is capitalised.
  - **Shareholders.** Dilution was 5.3% in 2025. The "Adjusted EBITDA" adds back stock pay. The founders sold at 6.90
    and their raise followed a minority refusal.
  - **Regulation.** The BNPL circular applies from 12.1.2027, and the credit-data amendment from early 2027.
  - **Trading.** Turnover is far below the floor.
  - **The charter's arithmetic** puts value at about 2.2 a share (out §3-§5).
- **What we do not know** (UNVERIFIED):
  - the economic credit cost on the 203,167 fair-value book;
  - where the defaulted loans sit;
  - the SPC lender, its terms, indemnity caps and outstanding pools;
  - the 360 guarantee volume and losses;
  - what the TheMarker articles say, and whether any suit exists;
  - the October seller;
  - any pledge of the founders' shares;
  - the terms of the June 2023 founders' agreement;
  - why shares in Paymeant Series 1 changed hands on 10.9.2026;
  - the held book's discount-rate sensitivity;
  - the Q3 2026 results;
  - the Maya reports filed since 30.6.2026.
- **What we do not need to know:**
  - global BNPL growth and foreign BNPL multiples;
  - Isracard's BNPL volumes;
  - passive index weights, which are tiny (scuttlebutt.md §6);
  - the exact option overhang, which barely matters at values below the 3.01 strike.
- **What could be unknown to us:**
  - how the book behaves in a recession, since there has been no credit cycle since the 2021 listing;
  - whether Israeli banks keep funding point-of-sale credit through a downturn;
  - how courts will apply the circular's cancellation right;
  - the next turn of payments regulation;
  - the founders' intentions.

---

## 6. Destination (dated 3.11.2026): where the business is likely to be in 2031-2036

- **Destination 1: owned by a bank or card issuer.** Banks already buy these loans rather than build the platform
  (Leumi bought pools in 2023 and 2026; Hapoalim is leaving blenderPay; scuttlebutt.md §1.3-§1.4). Paymeant is likely
  to become an origination channel owned by, or contractually tied to, one of them. The price would be near book plus a
  modest premium for the merchant network.
- **Destination 2: an independent niche lender.** It would win committed funding, absorb the circular and a first
  credit cycle, and, with no moat, earn roughly the hurdle on its equity. It would be worth about tangible book plus
  retained earnings.
- **Destination 3: a run-off.** Possible after a funding stop or an indemnity dispute, at well below book (out §4).
- **A compounder needs more.** It would have to keep today's earnings scale with excess returns through a credit
  cycle. Nothing in four profitable years without one shows pricing power or a cost advantage that would allow that.
- **Conclusion.** The destination is mediocre at best. The record does not support buying the business at 1.45x the
  charter's base value.

---

## 7. Sell rule for the lane

- **In force now: none.** There is no lane and no position.
- **Declared for the record.** If the name were ever bought, it could only be under **Lane C** (the cheap track for a
  cyclical), and Lane C's rule would bind:
  - sell at base-case private-owner value, after re-testing second-order supply and the allocator;
  - as a cyclical, take the principal out at a double, then half at each further double;
  - sell at once if a kill condition in §9 fires;
  - never sell on a price fall alone (charter rule 7).

---

## 8. Size (framework e2, `position_size()` in `lib/charter_valuation.py`; out §6)

| Limit | Value |
|---|---|
| Full Kelly on the four scenarios at 3.173 | 0.0% (the probability-weighted value 2.34 is below the price) |
| Quarter-Kelly | **0.0% of NAV: binds** |
| Tier cap (C, the cheap track; tier B gives the same result) | 5.0% |
| Permanent-loss budget, 5% / L_worst (L_worst 81.3% to the 0.59 low-end worst case) | 6.1% |
| Sector room / TASE room | 25% / cannot assess here (holdings not available) |
| Liquidity maximum, 20 days × 20% × 25th percentile (Bizportal, 2,590 ILS) | **10,361 ILS at cost** |

**Size: 0% of NAV.** The fund's NAV is not available here, so the liquidity cap is stated in ILS. The stock is also
below the ILS 50,000 floor, a hard exclusion under screen_spec X5, with a median of 19,125 (out §6).

---

## 9. Pre-mortem: the path to a permanent loss, dated signals and kill conditions (E1, O7)

**The path.**
1. The circular takes force on 12.1.2027. A clinic chain or equipment merchant financed through Paymeant fails or is
   found to have mis-sold.
2. Borrowers cancel. The press has already reported such disputes (TheMarker, 18.6.2026 and 12.7.2026; bodies
   UNVERIFIED).
3. The SPC's bank claims under the indemnities "in other cases" (h1_2026 p.7).
4. The take-out bank pauses, and the warehouse banks cut their on-call lines.
5. Origination stops. The fees stop with it (55.1% of H1 2026 revenue, redteam_business_calc §S4), while opex of 28,857
   continues (out §4).
6. The 1M profit covenant breaks, or the lines are simply called.
7. The outcome is dilutive rescue equity (marker 1) or a going-concern note while the book runs off (marker 2).

**Dated signals.**

| When | What to read |
|---|---|
| ~17.11.2026 | Q3 2026 report: arrears, provision, line table, any SPC disclosure. The buyback plan lapses on 18.11.2026 |
| Mid-November 2026 | October fund holdings: who sold |
| 23.11.2026 | Bank of Israel rate decision |
| 12.1.2027 | The circular takes force. The Amitim second tranche expires |
| About 26.1.2027 | The credit-data amendment takes force (six months after 26.7.2026, h1_2026 p.7) |
| Late February 2027 | FY2026 report: lines, lenders, guarantees, the intangible note |
| By 31.5.2027 | Q1 2027 report: arrears after the circular |

**Kill conditions.** Any one of these confirms the bear case and keeps the file closed for at least two years:
1. any disclosed SPC indemnity, repurchase or recourse claim, or a cut, non-renewal or adverse repricing of a bank line;
2. loans 1-90 days past due plus defaults above 6% of the on-balance-sheet book at a quarter-end;
3. the founders' joint stake falling below 25% (headroom 4.54 points = 1,784,758 shares, out §4), or any
   change-of-control notice to the banks;
4. a certified class action, or a regulatory sanction, over merchant disputes;
5. a going-concern paragraph or an emphasis of matter.

---

## 10. What reopens the file (price alone never does)

The file reopens only when all of the following hold:
- falsification conditions 1 and 2 (§4) are met;
- the open items in §11 are closed: courts, pledges, the June 2023 agreement, and the Maya reports since 30.6.2026.

Value is then recomputed on the charter normalisation (lender basis, with the EV basis beside it), and price is
compared with that recomputed value, never with 5.36.

---

## 11. Open items for the principal ("cannot assess here" counts as open; gates fail closed)

1. **A0.** `theses/CIRCLE.md`.
2. **B7.**
   - Search the court and class-action registers for "פיימנט טכנולוגיות פיננסיות" (515166544) and "אפלידנט".
   - Read the two TheMarker articles. themarker.com would have to be allowed in the session's network settings:
     - https://www.themarker.com/law/2026-06-18/ty-article/.highlight/0000019e-cf4c-d45a-ab9e-cfeec4490000
     - https://www.themarker.com/law/2026-07-12/ty-article-magazine/.highlight/0000019f-4153-d07c-af9f-c95f90af0000
3. **F1.** Search the Pledges Registrar by name for Yaniv Gilor and Guy Yochanan.
4. **F2.**
   - The June 2023 founders' agreement (immediate report 2023-01-060154).
   - The results of the 30.3.2026 meeting.
5. **D8.** The Maya reports since 30.6.2026:
   - the assignment of 23.9.2026 and 29.9.2026;
   - the clarification of 28.10.2026;
   - the transfer of shares in Paymeant Series 1 on 10.9.2026;
   - any change to the lines.
   Maya blocks scripted access.
6. **The Q3 2026 report** (expected about 17.11.2026).
7. **D6, G2, G3, G6, G8.** Holdings, the principal's cash needs and tax_params.
8. **C6 and the X4 history gate.** The FY2020 comparatives in the FY2021 annual report.

---

## 12. Files

- `research/paymeant/valuation.py` (revised at this gate) and `research/paymeant/output.txt` (regenerated).
- `work/paymeant/checklist.md`: the 60 items.
- `work/paymeant/valuation_notes.md`: the first version, now with a superseded banner.
- `work/paymeant/gate_tools/`: the scratch scripts used to compare the liquidity series and extract values. They hold
  no record figures.
