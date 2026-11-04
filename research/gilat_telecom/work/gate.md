# Gilat Telecom Global (TASE 1080597): CIO gate

3 November 2026. Charter Revision 4 governs (`constitution_zip/charter_rev4_draft.md`, "Text to paste"). This gate owns
the conclusion.

**Where the numbers come from.**
- Model: `/home/user/value-investing-fund---selected-company-reaserch/research/gilat_telecom/valuation.py`, revised at this gate.
- Printout: `/home/user/value-investing-fund---selected-company-reaserch/research/gilat_telecom/output.txt`, cited as "out §n".
- Checklist: `checklist.md` in this folder.

Every figure below is copied from the printout or from a cited filing page. This file does no arithmetic of its own.

**Final edit after verification (record as of 3.11.2026).** Three independent verifiers audited this gate. The confirmed
defects were fixed here, in `valuation.py` and in the other record files; `verification.md` lists every finding and its
disposition. No price, rate or date changed. The base rose from 0.428 to 0.474, because the d3 add-back of acquired
amortisation now matches the six-year mean inside EBIT_norm (AR-1) and the expected IRU cost is dated to 3.11.2026 (AR-3).
B7 now fails closed (CH-1), and E7 is now "yes" (CH-6). At the CIO's review of the verification D1 also became "no" (the
price was in the valuation brief; the Paymeant study's C-1). **No decision rule changed its outcome: the verdict stays
NO_THESIS.**

## Verdict: NO_THESIS

| Per share, ILS (3.11.2026; USD/ILS 3.157) | Value | Price / value |
|---|---|---|
| Price, close 3.11.2026 | 1.653 (165.3 agorot) | — |
| Worst case (ten years out) | 0.000 | n/m |
| Conservative (Vodacom not renewed) | 0.000 | n/m |
| **Base** (EPV on EBIT_norm, W = FY2020-FY2025) | **0.474** | **3.49** |
| Optimistic (TTM run-rate, net of the IRU accounting gap) | 1.718 | 0.96 |
| Probability-weighted (15/30/45/10) | 0.385 | 4.3 |
| Charter Tier C net-net reference line: the 30.6.2026 balance sheet per 3.11.2026 listed share, 0.094 per 30.6.2026 share (**not a buy price**: NO_THESIS sets none) | 0.092 | 17.94 |

**What the price implies:** owner earnings growing +15.7% a year for ten years from the normalised base, or falling
only −1.5% a year from the TTM (out §4).

**Why NO_THESIS and not WATCHLIST.** WATCHLIST needs price (D2) to be the only failure. Here eleven applicable VETO items fail.
Seven of them fail on facts that hold at any price:
- B3 dilution;
- B5 accounts and candour;
- E1 impairment path;
- F4 currency and CPI;
- H2 firm asset value;
- H4 catalyst;
- H5 cyclical tests.

Three depend on the price and fail at today's: D2 (price against the C line), D5 (expected return) and E3 (what
the price implies).

D1 fails on process. Its first clause asks whether value was estimated before looking at the price, and the price was in
the valuation brief. This gate answered "yes" because no value input uses the price, which is a different test. At the
CIO's review of the verification it was made "no", the reading the Paymeant study's verification gave the same pipeline
(C-1). A valuation run without the price would cure it; it moves no number.

Four more VETO items (B7, D8, G2, G3) cannot be assessed here and fail closed. The investment test fails at Q1, Q2 and Q3.

**Why not TOO_HARD.** The business is understandable and the key figures were verified on page images. What is
unknown (the Bezeq balance and schedule, Customer A, Vodacom) is named, bounded and dated, and the conclusion holds
across it.

**The investment test (charter).**

| Question | Answer |
|---|---|
| 1. Inside the circle? | **No.** `theses/CIRCLE.md` is not available here. The team's own industry study finds the business understandable but not predictable 5-10 years out (business.md §13). It is outside the circle. The checklist's A0 does not bind Lane C, but the charter's Q1 binds every thesis |
| 2. A good business by its lane? | **No.** Lane C asks for a firm asset value not being burned, and a catalyst or a basket. H2 fails: the unpaid Bezeq consideration is 5.9x NCAV. H4 fails: no catalyst, a single name. H3 passes (out §4, §7) |
| 3. Price well below value? | **No.** On the Tier C test, the market cap is 5.3x NCAV and 17.9x Dempster, and no private-owner value is evidenced (D2). As context, price is 3.5 times the EPV base, which is below the price everywhere in the sensitivity grid (0.336-0.573; out §5) |
| 4. What the price assumes, and why that is wrong | **The price assumes the war-era earnings persist, and we cannot show that is too pessimistic.** The CEO told the market that turnover reached "about double the normal period" in the war (Bizportal 20014148). He said it in answer to a question on the defence activity, so it may mean the company's or the defence division's turnover; out §5 carries both readings. Known facts explain the low multiple on TTM earnings, so the Petco rule applies |

## 1. The red-team objections, one by one

Two reviewers argued the bear case: **gilat_telecom:redteam-accounting** (`redteam_accounting.md`, O1-O11) and
**gilat_telecom:redteam-business** (`redteam_business.md`, O1-O10).

**Result:** 18 objections accepted, 3 accepted in part, none rejected outright. The disputed figures were re-opened as
page images at this gate:
- **gilat_q2_2026_full:** p.30-32, p.38-39, p.46.
- **gilat_h1_2026:** p.12-14, p.19, p.24.
- **gilat_fy2025:** p.92-93, p.96, p.99, p.106, p.132, p.147, p.152-153, p.183, p.206-207.
- **gilat_fy2024:** p.88-89, p.193-194.
- **gilat_fy2023:** p.91.
- **gilat_fy2022:** p.119, p.123-124.
- **gilat_fy2021:** p.114-116, p.145-146.

### Accounting reviewer (gilat_telecom:redteam-accounting)

| # | Objection | Decision | What changed, and the evidence |
|---|---|---|---|
| A-O1 (high) | The cyclical window counted the TTM as a sixth observation (H2 2025 twice). FY2020 was missing | **Accepted** | **Window.** W is now fiscal years FY2020-FY2025, as framework d2 defines it. H2 2025 EBIT of 20,139 sat in both the FY2025 and the TTM observations (gilat_q2_2026_full p.32, page image).<br>**FY2020 source.** FY2020 was obtained from the company's own FY2022 report (gilat_fy2022 p.119, p.123-124) and cross-checked with the FY2021 report (gilat_fy2021 p.116). The FY2020 "other income" of 286 is a dividend and credit from the Wiocc stake (p.123), so it is removed; EBIT_adj is USD 3,363k.<br>**Result.** EBIT_norm is 7,643 (USD 2,421k), against 11,100 before. FY2021-25 alone gives 6,876, and the TTM-augmented windows are kept only as sensitivities (out §3).<br>**Base value.** 0.428 at the gate, against 0.789 before; 0.474 after the final edit (AR-1, AR-3; verification.md). The red team's 0.520 was on FY2021-25 without the A-O4 and B-O6 changes. |
| A-O2 (medium) | F4 unrecorded and failing. The stress used a hedge proxy and ignored the balance sheet. "No CPI-linked debt" was wrong in substance | **Accepted** | **Currency.** The stress now uses the filed linkage table: USD liabilities 90,430 against USD assets 24,967 by row (gilat_h1_2026 p.19). USD/ILS +10% takes the base to 0.000, and so does +20% (out §5).<br>**What the failure rests on** (final edit, AR-5). The net USD cost flow, whose USD 24M proxy is the hedge size (UNVERIFIED), carries it. The filed remeasurement alone leaves the base at 0.416 (+10%) and 0.358 (+20%), which would pass. F4 fails for any net USD cost flow above USD 8.9M a year. A cross-check from the FY2025 cost structure puts the flow near USD 21.0M: USD-priced costs of 40,702 (satellite services, mobile-satellite airtime, equipment: gilat_fy2025 p.173; lease cash: p.132) less global-segment revenue of 19,655 (p.181). The currency split of costs is not disclosed, so the cross-check is UNVERIFIED too, but it clears the break-even by a wide margin.<br>**CPI.** Pulses 2-3 and the O&M carry 50% CPI linkage (gilat_fy2025 p.153), and the addendum is "CPI-linked" (p.42, p.183). CPI at 5% instead of 2% costs 0.096 a share.<br>**Wording.** The CPI line now reads "no CPI-linked financial debt; about ILS 224M of IRU commitments half-CPI-linked (UNVERIFIED balance)". **F4 = no.** |
| A-O3 (medium) | E1's printed evidence compared one-date balances with undiscounted ten-year commitments | **Accepted** | **Withdrawn.** The old marker (2)/(3) lines are gone.<br>**New test.** E1 is now a dated runway in code: the IRU schedule, Series D coupon and amortisation, and core plus ISP cash. Cash falls below two months' costs in 2028 and below zero in 2029, with a pre-war or zero core; with the FY2023-25 core, below zero in 2031 (out §5).<br>**Result.** Marker (1) is reachable: new money is needed by 2029. **E1 = no.**<br>**Caveats.** The schedule is UNVERIFIED. The filed FY2025 payments (13,752) run ahead of the modelled 7,079 (gilat_q2_2026_full p.38). No going-concern doubt is filed (gilat_fy2025 p.123-124). |
| A-O4 (medium) | The bridge mixed 30.6.2026 balances at 2.978 with a 3.11.2026 rate of 3.157 | **Accepted** | **Restatement.** Net USD monetary liabilities of 65,463 are restated at 3.157: +3,935, deducted in every bridge (out §3).<br>**Footing errors** in the linkage table are recorded as C7 flags and the rows are used: USD assets 24,967 against a printed 25,110; unlinked-ILS assets 138,235 against 138,321; the cash row 92,991 against 92,955.<br>**Forwards.** USD 22M remains, strike undisclosed; no credit is taken. |
| A-O5 (low) | C4's build-up clause and B5 have unrecorded evidence | **Accepted** | **C4** fails on both clauses: gross receivables +27.7% against revenue +8.9%, and customer days 62 to 69 (gilat_fy2025 p.147). The IRU deferred asset went from 0 to ILS 16,229k.<br>**B5 = no.** The 25-year policy (p.153) cannot be reconciled with a first-year charge of 1,079 on a cost of 3,902 (p.152). |
| A-O6 (low) | The ILS restatement's lease-interest split was used unquestioned | **Accepted** | **Two splits.** Interest cover is 3.0x on the restatement and 4.4x on the audited USD split (gilat_fy2025 p.132, 15.8% against 24.6%; out §3).<br>**Effect.** Total lease cash is the same, so no value changes. The inconsistency is a C7 flag. |
| A-O7 (low) | C6 missing | **Accepted** | **C6 = no.** Cover was 1.2x in FY2020 (now in the record), −1.1x in FY2021 and −0.9x in FY2022 (gilat_fy2022 p.119, p.124; out §3). |
| A-O8 (low) | Lane C has no EPV base; the spread mixed dates; the shadow line must not be used | **Accepted** | **Tangible book.** On the 3.11.2026 basis it is 0.887, or 0.732 without the IRU prepayments and the DTA (out §4).<br>**Spread.** The 109% spread is resolved explicitly (out §6): book is not earned, at 7.7% NOPAT on tangible equity against r, and not realisable, at a Dempster value of 0.094. The base stays EPV.<br>**Line.** The shadow line is withdrawn; the only charter C line is the net-net reference line, 0.092, which is not a buy price. |
| A-O9 (low) | TTM ROTC on end-of-period capital | **Accepted** | TTM ROTC is 42.9% on average capital, or 39.1% with the IRU prepayment (out §2). The tier result is unchanged. |
| A-O10 (low) | One-offs and FX left in the TTM | **Accepted** | **Supplier credit.** Labelled an upper bound: gilat_fy2025 p.96 names three causes of the margin rise.<br>**Intelsat.** The purchase commitments are listed as UNVERIFIED under E1 and C1 (p.160: "currently backed by service orders from existing customers").<br>**FX.** The estimated H1 2026 FX gain of 5,080 is stripped from NI_norm_ttm (gilat_fy2025 p.106). Graham's test still fails, at an earnings yield of 5.4% against 8.32% (out §4). |
| A-O11 (low) | Two versions of the H1 2025 segment results | **Accepted** | **Which source.** The FS note is used (gilat_q2_2026_full p.46: 30,777, reconciling to pre-tax), and the directors' report table (gilat_h1_2026 p.12: 24,863) is flagged.<br>**business.md §12 re-checked.** Its base uses segment revenues, which agree between the two sources, and the FY2025 audited margins. Only its bull case uses the directors'-report ISP result. |

### Business reviewer (gilat_telecom:redteam-business)

| # | Objection | Decision | What changed, and the evidence |
|---|---|---|---|
| B-O1 (high) | B5 is a "no", not "open" | **Accepted** | **Pay metrics.** 70% of the CEO's 2025 bonus rides on Adjusted EBITDA (gilat_fy2025 p.207), which strips only satellite-lease depreciation (p.92). The free-cash-flow metric (30% in 2024, gilat_fy2024 p.193) was dropped for 2025, the first year of IRU payments. The cap went from 6 to 8 salaries in December 2025 (gilat_fy2025 p.206; gilat_fy2024 p.194).<br>**Headline figures.** "FCF excluding prepaid expenses" adds back 2,929 (p.93). "Not leveraged ... zero levels" (p.90), while the risk-factor chapter never mentions Bezeq (chapter 27, p.82-87).<br>**Changes.** The optimistic case is now net of the IRU accounting gap of 3,691 (range 802-3,691; out §5). Re-examination is conditional on the FY2026 report (trigger 2). |
| B-O2 (high) | Delete the shadow buy price; H2 = no; no charter buy price; lane "none" | **Accepted in part** | **Accepted.** The shadow line is withdrawn. H2 = no: the unpaid Bezeq consideration is 5.9x NCAV (out §4). No buy price exists: NO_THESIS sets none.<br>**Not accepted: lane "none".** The lane stays declared as C, because G4 needs a declared lane and a sell rule, and the C cyclical sell rule can be stated. It is recorded as "no lane satisfied today". The structured output carries the net-net line (0.092) as a number, labelled "not a buy price". |
| B-O3 (medium) | The base leans on war-level revenue or margin; Vodacom is implicit; the optimistic case is overweighted | **Accepted in part** | **Accepted.**<br>- Weights are now 15/30/45/10.<br>- Vodacom non-renewal is the conservative scenario. With the worst case, which also loses Vodacom, the stated probability of loss is 45% (out §5).<br>- The optimistic case is net of the IRU gap.<br>- The probability-weighted value is shown under three weightings: 0.385, against 0.557 (team weights) and 0.361 (20/30/40/10; out §5).<br>**Replaced: the label.** Instead of "requires war-level revenue or margin", the computed reading is recorded:<br>- the new base is the six-year mean, half pre-war (USD −289k) and half war (USD 5,131k);<br>- it is reached at routine turnover only on the CEO's "defence 50% to 30%" reading with lean costs or a war-era margin;<br>- on the "about double" reading it is not reached (out §5). |
| B-O4 (medium) | E1 should rest on the filed record; worst-case weight too low | **Accepted** | **Filed record cited.** The 2023, 2024 and 2025 dedicated working-capital disclosures (gilat_fy2023 p.91; gilat_fy2024 p.88; gilat_fy2025 p.99) and the July 2024 exchange, which the company calls "a significant debt reduction" (gilat_fy2024 p.88-89). The regime ended only at 30.6.2026 (gilat_h1_2026 p.14), and a shelf prospectus has been open since April 2026 (p.49).<br>**Weight.** The worst case is now 15%.<br>**Condition.** E1 fails at any price until the FY2026 report quantifies the Bezeq obligation and a non-war year shows positive lease-adjusted cash flow. |
| B-O5 (medium) | A7, B2, B6 and E7 bind lane C and are each "no" | **Accepted** | Recorded "no" with explanations (checklist.md). B2's multiples are now in code: buybacks at 5.5x and 4.3x base value (6.1x and 4.7x at the gate), taking back 17.7% of the conversion shares (out §7).<br>**Final edit (CH-6).** E7 is now "yes": it asks whether the fund checked itself for misjudgment tendencies, and the record shows the check was run and passed. Management's incentive bias and social proof stay recorded under B4 and B5. |
| B-O6 (medium) | The IRU is a negatively skewed option that the base prices at zero | **Accepted** | **Base.** It now carries 25% of the "half the unfilled lines unused" cost: 11,442 after tax (out §3). At the final edit each line's PV was dated from its tranche's delivery back to 3.11.2026, and the unused half is the latest-delivered half (AR-3; 13,067 at the gate, undated). The probability is a stated model judgement; private net additions ran about 3,500 a quarter against tranches of 3,000 (gilat_h1_2026 p.8).<br>**Not credited.** The +12,850 saving against BSA if every line fills.<br>**Trigger added.** Net additions below 3,000 a quarter for two quarters. |
| B-O7 (low) | Q1/A0 should be "no" | **Accepted** | Q1 = no: outside the circle. A0 is n/a for lane C (it binds A, B and D), and the finding is recorded under Q1, which binds every lane. |
| B-O8 (low) | F2 should be "pass on questionnaire; tallies unread (open)" | **Accepted in part** | **Accepted.** The tallies are unread (Maya returns 403) and go to the principal.<br>**Not accepted: F2 as a fail-closed open item.** The pass test is met from the filings, for all five years 2021-2025 (Reg. 21A and 22: gilat_fy2021 p.198-199; gilat_fy2022 p.206-207; gilat_fy2023 p.193-194; gilat_fy2024 p.199-200; gilat_fy2025 p.214-215):<br>- there is no controller (gilat_fy2025 p.214);<br>- related-party dealings are pay only (p.215, p.176);<br>- both pay votes passed: the policy at the meeting called for 13.3.2024 and adjourned to 14.3.2024 (p.63 prints 13.3.2024; p.207 and the company's adjournment notice give 14.3.2024), and the CEO package on 4.12.2025 (p.206);<br>- no meeting's rejection was overridden (p.233, item 32).<br>The company's site hosts the summonses but not the results (searched at this gate). |
| B-O9 (low) | The 2021 sale of control failed, at no premium | **Accepted** | **Fact recorded under d7 and H4.** In 2021 the 41% block was dispersed for about ILS 26M at a market value of about ILS 68M "after previous attempts to sell the control core did not succeed" (Calcalist L-3894358, saved copy re-read). That is −6.7% against the market (out §4).<br>**Consequence.** No takeover catalyst is assumed. |
| B-O10 (low) | Earlier, sharper triggers | **Accepted** | Three triggers added: defence orders by 31.1.2027, licence renewals by 31.12.2026, and ISP net additions (out §7). |

**What the gate and the final edit changed in the numbers (out §8).**

| | Previous run | At the gate | After the final edit |
|---|---|---|---|
| EBIT_norm | 11,100 | 7,643 | 7,643 |
| Base | 0.789 | 0.428 | 0.474 |
| Conservative | 0.356 | 0.000 | 0.000 |
| Optimistic | 1.921 | 1.718 | 1.718 |
| Probability-weighted | 0.828 | 0.364 | 0.385 |
| Line | shadow buy line 0.316 (withdrawn) | net-net 0.092 | net-net reference line 0.092 (not a buy price) |
| Implied growth (normalised) | +11.4% | +16.5% | +15.7% |

## 2. Inversion: how a buyer at 165.3 agorot loses money permanently

The asymmetry from the price (out §5):

| Scenario | From the price |
|---|---|
| Optimistic | +4% |
| Base | −71% |
| Conservative | −100% |
| Worst | −100% |

This inverts Pabrai's "heads I win, tails I don't lose much". The loss path has four parts.

1. **Defence demand normalises.** The government backlog for 2027-2029 was only USD 2,195k at the FY2025 report date
   (gilat_fy2025 p.32; summed in redteam_business.md calc §3).
2. **Vodacom is lost or shrinks at 31.3.2027.** Its group partnered with Starlink. Without Vodacom, normalised earnings
   do not cover Series D par, leases and the expected IRU cost, so the conservative equity is nil (out §5).
3. **The IRU and Series D squeeze cash from 2028.** Bezeq instalments rise to 30,023 (2027) and 37,955 (2028) on the
   modelled terms, and Series D amortises from 1.4.2028. On a pre-war core, cash runs out in 2029 (out §5).
4. **Dilution follows.** The 2023 rights issue at 0.30 and the 2024 exchange show how this company closes gaps. The shelf
   prospectus has been open since April 2026.

**The currency leg.** A 10% stronger dollar alone takes the base to nil (out §5). That rests on the net USD cost flow
(UNVERIFIED proxy, USD 24M a year; break-even USD 8.9M; cost-structure cross-check about USD 21.0M); the filed balance-sheet
remeasurement alone would leave 0.416. The dollar fell 18.3% from end-2024 to mid-2026, so a reversal of that size has
already been seen.

## 3. Three falsification conditions (specific, observable, dated)

Each condition, if it occurs, falsifies a premise of the NO_THESIS conclusion and requires re-running `valuation.py`
before anything else.

1. **The war premium does not normalise.**
   - **When:** by 31 January 2027.
   - **What to watch:** the 2027 orders Gilat reports from Israeli defence and government customers in its immediate
     reports of December 2026 and January 2027.
   - **Falsified if:** they total at least the "about ILS 110M including VAT for the coming year" reported for 2026
     (gilat_h1_2026 p.14). The premise that TTM earnings are a peak (TTM EBIT_adj 4.4x EBIT_norm) would then be wrong for
     a third year, and EBIT_norm must be re-underwritten.
   - **Confirmed if:** they total below half that level.
2. **The Bezeq commitment is benign.**
   - **When:** in the FY2026 annual report, due by 31 March 2027.
   - **Falsified if:** the report states the unpaid IRU consideration and its payment schedule (or that pulse-1 tranches
     can be declined), and the runway re-run in `valuation.py` on the filed schedule keeps cash above two months' costs
     through 2031 with a zero core.
   - **Consequence:** E1's marker (1) would clear and H2 could be re-tested. On the modelled schedule, cash falls below
     two months' costs in 2028 (out §5).
3. **Vodacom renews.**
   - **When:** by 31 March 2027.
   - **Falsified if:** Gilat announces a renewal of the Vodacom DRC contract for at least 24 months at no less than
     USD 1M a month, the 2023-2025 average (gilat_fy2025 p.55).
   - **Consequence:** the conservative scenario (non-renewal, 30% weight, value 0.000) would be refuted.

**Monitoring triggers, not counted among the three (out §7):**
- private ISP net additions below 3,000 a quarter for two consecutive quarters;
- renewal of the satellite, Iridium, trade and OneWeb licences that expire on 31.12.2026 (gilat_fy2025 p.69-72);
- in the FY2026 report: the IRU amortisation applied, and whether the Bezeq commitment and LEO substitution appear among
  the risk factors (B5).

**Lines that must not be used as a buy price.** The net-net line of 0.092 is the only charter Tier C line. It is a
reference line, not a buy price: under NO_THESIS no buy price is set, and only a watchlist name, whose only failure is
price, gets a dated one. Before any Tier C line could become a buy price, Q1 must be answered yes (from `CIRCLE.md` or a
written industry study), and B3, B5, E1, F4, H2, H4 and H5, which fail at any price, must clear. The withdrawn shadow
line (0.316, or 0.208 on the red team's window) must never be used as a dated buy price.

## 4. Li Lu's four categories

**What we know** (filings checked on page images; out §1-§5):
- **The business.** A reseller and integrator of capacity it does not own: satellite capacity and airtime, and Bezeq fibre.
- **The record.** FY2020-FY2025 and the TTM. Operating losses in FY2021-22; a war-era margin since 2023.
- **The capital structure.**
  - Series D: ILS 26.3M par, converting at 1.00 until 1.4.2028, then at 1.40, and amortising 2028-2031.
  - Leases of 33,116; no bank debt.
- **The Bezeq IRU terms as filed.**
  - 54,000 committed lines: ILS 88.02M plus about ILS 160M.
  - 10 annual instalments, with 5% vendor interest on pulse 1.
  - 4% O&M, with 50% CPI linkage.
  - Release only from a subsequent pulse.
  - A 25-year amortisation policy.
- **Dilution.** ×2.06 since 2022.
- **Pay.** The structure and metrics, and that no controller exists.
- **Trading.** Liquidity (median ILS 1,325,803 a day).
- **Who sold and who bought.** Shidurit, the funds and converters sold; the CEO and the company bought.
- **The CEO's own statement** that turnover reached "about double the normal period" in the war (whether the company's
  or the defence division's is not clear from the interview).
- **Vodacom Group's Starlink partnership.**
- **The regulated BSA price** of ILS 58 a month, unlimited for small ISPs.

**What we do not know:**
- **The Bezeq IRU.**
  - The unpaid consideration and its schedule.
  - Whether pulse-1 tranches can be declined.
  - The amortisation actually applied.
- **Customers.** Customer A's identity and its 2027 orders; whether Vodacom renews.
- **Other commitments.** The Intelsat purchase commitments.
- **Currency.** The net USD flow exposure (only the hedge size is known) and the forwards' strike.
- **Recent results.** Q3 2026.
- **Unread records.**
  - Maya immediate reports since 19.8.2026.
  - The vote tallies.
  - Whether the CEO's shares are pledged.
  - Court records.

**What we do not need to know:**
- the size of the global satellite market;
- Starlink's Israeli subscriber count;
- the affairs of Gilat Satellite Networks, a different company;
- the exact H1 2026 war-equipment one-off and the exact tax-loss shield (USD 19.0M unrecognised);
- the IPv4 pool.

None of these could move the price-to-value gap enough to change the verdict.

**What could be unknown to us (unknowable):**
- **War and budgets.** The course of the wars and of Israeli defence budgets.
- **Technology.** Low-orbit pricing over a decade.
- **Regulation.** The wholesale regime after 2028-2031.
- **Currency.** The path of USD/ILS.
- **Capital allocation.** Whether management spends its cash on the acquisitions it advertises.
- **Counterparties.** Bezeq's and Vodacom's choices.

The last list sizes the position; it does not justify one.

## 5. Destination (written 3 November 2026, for 2031-2036)

**The most likely business, 5-10 years out:**
- **Defence.** A smaller Israeli government and defence satellite reseller, kept by licences, cleared staff and
  incumbency, but in a field where competition "focuses mainly on price and on the ability to provide the customer a
  total solution" (gilat_fy2025 p.32) once the war premium fades.
- **ISP.** A fibre ISP on Bezeq lines bought at cost parity with the large groups, whose margin over the regulated BSA
  price depends on filling the committed lines.
- **Africa.** A shrinking business, unless Vodacom renews against Starlink.

**Earnings.** In an ordinary year they should sit near the six-year mean that the base uses (EBIT_norm USD 2,421k). The
range runs from FY2021-22-style losses if defence normalises fully and Vodacom goes, to war-era margins only if demand
stays elevated.

**Per share.** Series D and the options will raise the share count again: they convert or are repaid in 2028-2031, and
the share count has already doubled since 2022 (out §7). Bezeq instalments absorb most of the free cash flow to the
mid-2030s.

**The bet.** The business is unlikely to be worth more per share in 2031 than the base value today unless the war-era
margin persists, and that persistence is exactly what the current price already pays for. No destination we can state
with confidence justifies 165.3 agorot.

## 6. Sell rule declared for the lane

**Lane C, cyclical sub-rule (charter, "Buying, adding and selling"):**
- principal out at a double, then half at each further double;
- never sell on a price fall alone.

**No private-owner value is evidenced**, so the "sell at base-case private-owner value" variant cannot be used. **No
position is held.** The rule is declared for any future purchase, which could only come through the net-net route, after
Q1 is answered yes and B3, B5, E1, F4, H2, H4 and H5 clear.

## 7. Size (position_size, charter_valuation.py; out §7)

**Inputs:**
- outcomes: 15% at 0.000, 30% at 0.000, 45% at 0.474, 10% at 1.718;
- worst case 0.000;
- tier C;
- 25th-percentile turnover ILS 1,001,604 over the 60 sessions to 3.11.2026.

**Limits:**

| Limit | Value |
|---|---|
| Full Kelly | 0.0% (quarter-Kelly 0.0%) |
| Tier cap | 5.0% |
| Permanent-loss budget | 5.0% (5% of NAV ÷ L_worst of 100%) |
| Sector room | 25.0% |
| TASE room | 30.0% (fund holdings unknown) |
| **Liquidity maximum** | **ILS 4,006,416 at cost** (20 days × 20% × p25) |

**Size: 0.0% of NAV.** Quarter-Kelly binds, because every outcome except the optimistic one sits below the price. The
fund's NAV is not available here, so the liquidity cap is given as an ILS amount.

**One more constraint:** a holding of 5% or more of the company (10% for an institutional investor as the licence
defines it) needs the Minister's prior written consent (gilat_fy2025 p.73, §3(c)).

## 8. Open items for the principal

**Items that fail closed until answered** (each counts as "no" today):
- B7: a search of the court databases and the class-action register for the company, the subsidiary and the officers;
- D8: the Maya immediate reports since 19.8.2026, and the Q3 2026 report, expected late November 2026;
- G2, G3, D6 and the TASE cap: the fund's holdings, NAV and the principal's cash needs;
- G8: `tax_params`.

**Not available in this environment:**
- `theses/CIRCLE.md` (Q1);
- `lib/valuation.py` (`lib/charter_valuation.py` was used) and `lib/liquidity.py` (the charter formula was computed from
  the series);
- the calibration ledger (the probabilities are uncalibrated).

**To read, without gating a pass:**
- Maya: the vote tallies of the meetings of 14.3.2024 (called for 13.3.2024) and 4.12.2025. F2 passes on the filings
  (B-O8); the tallies would only add detail.
- A Pledges Registrar search for the CEO's shares. F1 passes: there is no controller, and the CEO's 7.93% is not a
  controlling stake.
- Bezeq's Hebrew report of 4.11.2025, for the all-in consideration and its schedule.
