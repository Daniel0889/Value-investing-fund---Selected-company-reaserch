# Gilat Telecom Global (TASE 1080597): pre-purchase checklist at the CIO gate

Run on 3.11.2026 against `constitution_zip/checklist.md` (Revision 4, 60 items in groups A-H). The charter governs.

**How to read this.**
- **Yes means pass.** A "cannot assess here" counts as "no": gates fail closed.
- **Figures come from code.** "out §n" is `research/gilat_telecom/output.txt` section n, produced by `valuation.py`. "scuttle §n" is `scuttle_calc_output.txt`.
- **Filings** are cited by document id and PDF page. Two documents were added at this gate, both downloaded from the company's own website:
  - `gilat_fy2021`: the 2021 annual report (balance sheets at 31.12.2020 and 31.12.2021).
  - `gilat_fy2022`: the 2022 annual report (restated FY2020 comparatives).

## The declared lane, and the result

**Lane C (bargain; cyclical sub-rule).** C is the only lane under which Gilat could ever be bought, and only as a net-net. No lane is satisfied today:
- Lanes A and B fail on the moat. ROTC over FY2020-FY2025 has a median of 13.8% and a minimum of −14.0% (out §2), and competition is "mainly on price" (gilat_fy2025 p.32).
- Lane D needs an A/B franchise.
- Lane E has no announced deal.

**Applicability.** 39 items apply to lane C: 28 VETO and 11 FLAG. The other 21 are n/a for the lane.

| | Pass | Fail | Cannot assess here (counts as fail) |
|---|---|---|---|
| **VETO (28)** | 15 | **10:** B3, B5, D2, D5, E1, E3, F4, H2, H4, H5 | **3:** D8, G2, G3 |
| **FLAG (11)** | 3: E4, E5, F6 | **6:** A7, B2, B6, C4, C6, E7 | **2:** D6, G8 |

**The investment test (charter).** Q1 circle: **no**. Q2 good business by its lane: **no**. Q3 price well below value: **no**, at price/base 3.9. Q4 what the price assumes: **+16.5% a year for ten years** from normalised owner earnings (out §4).

**Outcome: NO_THESIS.** It is not WATCHLIST, because price is not the only failure.

## A. Business and moat

| # | Question (yes = pass) | Type | Answer | Evidence |
|---|---|---|---|---|
| A0 | Inside the written circle of competence, or circle first extended by a study? | VETO | n/a (lane C; binds A, B, D) | Recorded under the investment test as **Q1 = no**. `theses/CIRCLE.md` is not available here. The team's own study finds the business understandable but "not predictable 5-10 years out" (business.md §13) |
| A1 | Explain in 3-4 sentences how it makes money and why more in ten years? | VETO | n/a (lane C; H1 replaces it) | — |
| A2 | Worst case ten years out stated with confidence; no rapid technology change or superstar dependence? | VETO | n/a (lane C) | Would fail: LEO operators are "changing the industry radically" (gilat_fy2025 p.50) |
| A3 | Moat named by type and visible in returns on tangible capital above peers? | VETO | n/a (lane C) | Would fail: ROTC −14.0% to 38.9%, median 13.8% (out §2); peer rank 10th of 15 on the 2021-25 margin (scuttlebutt.md §1.2) |
| A4 | Could a well-funded competitor not do serious damage ($1bn test)? | VETO | n/a (lane C) | Would fail: Starlink sells direct "at prices much lower than customary" (gilat_fy2025 p.50) |
| A5 | Real price rises without volume loss; owners keep efficiency gains? | FLAG | n/a (lane C) | — |
| A6 | Growth needs little capital or earns well above r? | VETO | n/a (lane C) | — |
| A7 | Industry rational: no major player buying share at a loss; supply cannot arrive quickly? | FLAG | **no** | Starlink "sells its services at prices much lower than customary ... changing the industry radically" (gilat_fy2025 p.50) and is "a direct competitor" (p.16). Regulated BSA at ILS 58 is unlimited for every small ISP (p.40). Gilat's own ARPU fell 9.6% year on year on promotions (gilat_h1_2026 p.8) |
| A8 | Old and dull; holds real earnings through high inflation? | FLAG | n/a (lane C) | — |

## B. Management and capital allocation

| # | Question (yes = pass) | Type | Answer | Evidence |
|---|---|---|---|---|
| B1 | Each retained dollar created a dollar of value? | FLAG | n/a (lane C; not applied to C) | — |
| B2 | Buybacks only below a conservative intrinsic value, from surplus cash, never just to offset dilution? | FLAG | **no** | June buyback at ILS 2.603 = 6.1x base value; October at 2.031 = 4.7x. 4,574,810 shares bought = 17.7% of the 25,773,849 conversion shares issued in H1 2026 at 1.00-1.35 (out §7; gilat_q2_2026_full p.49) |
| B3 | Stock issued only at full value; dilution at most 2% a year? | VETO | **no** | Listed shares ×2.06 since 31.12.2022 (21% a year), issued at 0.30-1.35. Series D adds 22% more (out §7; gilat_fy2023 p.151, p.183; gilat_fy2024 p.155; gilat_h1_2026 p.37) |
| B4 | Pay tied to per-share value over years; insiders own stock they bought? | FLAG | n/a (lane C) | Would fail: 70% of the CEO's 2025 bonus rides on Adjusted EBITDA (gilat_fy2025 p.207) |
| B5 | Accounts understandable, without "adjusted" earnings excluding real costs; mistakes reported candidly? | VETO | **no** | **Pay.** Adjusted EBITDA strips only satellite-lease depreciation, so the IRU charge stays added back (gilat_fy2025 p.92). It carries 70% of the CEO's bonus (p.207). Free cash flow was dropped as a metric for 2025 (gilat_fy2024 p.193 vs gilat_fy2025 p.207), and the cap went from 6 to 8 salaries in the year's last month (p.206).<br>**Headline FCF.** "FCF excluding prepaid expenses" adds back USD 2,929k (p.93).<br>**Leverage claim.** "Not leveraged ... zero levels" (p.90), while the Bezeq commitment is absent from the risk factors (p.81-87).<br>**Accounting.** The 25-year amortisation policy cannot be reconciled with the charge (p.152-153; out §3) |
| B6 | No empire-building or synergy deals; acquisitions below half of OCF? | FLAG | **no** | **Record.** Only one acquisition in the window: USD 1,500k in 2020 (gilat_fy2022 p.124).<br>**Intent.** Series D was raised partly for "synergistic strategic deals" (gilat_fy2025 p.100). The 20.8.2026 presentation lists "inorganic growth – examining potential acquisitions" (p.8, p.23).<br>**Means.** Pro forma cash is ILS 86,855k (out §3) |
| B7 | No record of misconduct, sanction or conviction of a controller or executive? | VETO | yes | Nothing found in the Companies Registrar, procurement records, ISA and Ministry searches or the press (scuttlebutt.md §4). Court databases were not searchable: an open item for the principal |

## C. Financial strength and earnings quality

| # | Question (yes = pass) | Type | Answer | Evidence |
|---|---|---|---|---|
| C1 | Survives a year of flat revenue and EBIT −30% with no covenant breach and no new money? | VETO | yes | Year-end 2027 cash stays positive in all three runway cases, including a pre-war cash-loss core. No maturity falls before 1.4.2028. Covenants stand at −24% and 48% against limits of 60% and 12% (out §5; gilat_h1_2026 p.23, p.25) |
| C2 | Net debt with leases ≤1x (A) / ≤2x (B) EBIT_norm; cover ≥8x? | VETO | n/a (lane C) | Would fail: 10.8x-26.2x EBIT_norm once the IRU is counted; cover 3.0-4.4x (out §3) |
| C3 | No maturity in 24 months needing open refinancing markets? | VETO | yes | Series C repaid on 1.9.2026. Series D's first 25% falls due on 1.4.2028 (gilat_h1_2026 p.24) and is covered by cash: end-2028 cash is positive in every runway case (out §5). No bank debt |
| C4 | Cumulative owner earnings ≥80% of NI; no build-up of receivables or deferred assets? | FLAG | **no** | **Cash clause.** The W sum is −38% of positive NI; FY2023-25 is 73% (out §3).<br>**Build-up clause.** Gross receivables rose 27.7% against revenue +8.9%, and customer days went from 62 to 69 (gilat_fy2025 p.147). The IRU deferred asset went from 0 to ILS 16,229k in 18 months (out §3) |
| C5 | Normalised figure free of endogenous add-backs? | VETO | yes | Nothing endogenous was added back: the FY2021 doubtful debts (3,191) and the FY2020 backlog amortisation (949) stay in. Only exogenous one-off gains were removed (out §1-3) |
| C6 | Interest covered comfortably in the stress years FY2020 and FY2022? | FLAG | **no** | Cover was 1.2x in FY2020 and −0.9x in FY2022 (−1.1x in FY2021) (out §3; gilat_fy2022 p.119, p.124) |
| C7 | Identities pass; every single-source figure confirmed by an identity? | VETO | yes | **Identities (30.6.2026).** The balance sheet balances, the H1 2026 cash flow foots, and NI/EPS equals the weighted shares (out §1). FY2020 is identical in gilat_fy2021 p.116 and gilat_fy2022 p.119.<br>**Flags (rows, FS note or audited figure used).** The linkage-table totals do not foot (gilat_h1_2026 p.19). The H1 2025 segment results differ between the directors' report and the FS note. The FY2025 lease-interest split differs between the audited USD and the ILS restatement (out §1, §3) |

## D. Valuation and margin of safety

| # | Question (yes = pass) | Type | Answer | Evidence |
|---|---|---|---|---|
| D1 | Value from ≥2 independent methods, as a range with a worst case, no EBITDA, all in code? | VETO | yes | **Methods.** EPV/DCF plus NCAV, Dempster and tangible book, as a range with a worst case. No EBITDA.<br>**Code.** Computed in `lib/charter_valuation.py`, because `lib/valuation.py` is not available here.<br>**Spread.** The 116% method spread is resolved (out §6). |
| D2 | Price at or below the tier's share of base value (C: ≤2/3 NCAV and ≤ Dempster, or ≤50% of private-owner value)? | VETO | **no** | Market cap 199,050k is 5.3x NCAV and 17.9x Dempster. The price is 17.9x the net-net line of 0.092. No private-owner value is evidenced (out §4, §6) |
| D3 | Base value above the price everywhere in the sensitivity grid? | VETO | n/a (lane C) | Would fail: the grid runs 0.297-0.523 against the price of 1.653 (out §5) |
| D4 | Implied growth below the per-share record? | FLAG | n/a (lane C) | Would fail: +16.5% a year implied against revenue per share −2.3% a year (out §4) |
| D5 | Expected return clears r = max(10%, y10 + 3) with a dated y10? | VETO | **no** | r = 10% (IL y10 4.16% on 3.11.2026; US 4.91%). Price/base is 3.9 and price/probability-weighted 4.5, so the expected return is negative (out §0, §7) |
| D6 | Beats the weakest holding, or the better of cash and the index, after tax? | FLAG | cannot assess here (counts as no) | Holdings, `swap_hurdle` and `tax_params` are not available. The expected value (0.364) is below the price, so it cannot beat cash |
| D7 | Latest dated close; identifiers from the brief; issuer asserted? | VETO | yes | Close 165.3 agorot on 3.11.2026 (market.md §1.1). TASE 1080597 comes from the brief. The issuer is named on every cover; three reports come from the company's own site |
| D8 | TTM basis, and every filing since the period end read? | VETO | cannot assess here (fails closed) | **TTM.** Yes, to 30.6.2026, and it reproduces Mega (out §1).<br>**Filings since then.** Maya immediate reports were not readable (HTTP 403). Q3 2026 is not yet filed |

## E. Risks and inversion (pre-mortem)

| # | Question (yes = pass) | Type | Answer | Evidence |
|---|---|---|---|---|
| E1 | In the worst case, no plausible path to a covenant/maturity dilution, a going-concern doubt, or assets below debt? | VETO | **no** | **Runway.** New money is needed by 2029 while Series D amortises 2028-2031 (out §5).<br>**Filed record.** Three years of dedicated working-capital disclosures (gilat_fy2023 p.91; gilat_fy2024 p.88; gilat_fy2025 p.99). The July 2024 bond-for-share exchange (gilat_fy2024 p.88-89). A shelf prospectus from April 2026 (gilat_h1_2026 p.49) |
| E2 | Three falsification conditions, specific, observable, dated? | VETO | yes | gate.md §3 |
| E3 | What the price implies stated and shown wrong; who is selling; discount not fully explained by a known fact? | VETO | **no** | **Implied.** The price needs +16.5% a year on normalised owner earnings (out §4).<br>**Known facts explain the low TTM multiple.** The CEO said the war roughly doubled turnover (Bizportal 20014148). Vodacom Group partnered with Starlink (12.11.2025). Add the Bezeq commitment and the Series D overhang (scuttlebutt.md §6).<br>**Who sold.** The would-be controller, funds trimming, and converting bondholders. The Petco rule applies |
| E4 | Bear case argued better than the best bear? | FLAG | yes | redteam_business.md §2-3, accepted; gate.md §2 adds the IRU skew, the FX remeasurement and the runway |
| E5 | Second-order effects: supply response, competitors, who else benefits? | FLAG | yes | **Supply.** LEO price erosion (gilat_fy2025 p.50); Vodacom reselling Starlink.<br>**Competitors and the regulator.** BSA at 58 for every small ISP (p.40); later IRU pulses come without price protection (p.42).<br>**Suppliers.** SES-Intelsat consolidation (scuttlebutt.md §1.3-1.4) |
| E6 | Thesis about the destination, not purchase-date numbers? | FLAG | n/a (lane C) | A destination paragraph is written anyway (gate.md §5) |
| E7 | Checked for incentive bias, consistency, social proof, deprival? | FLAG | **no** | **Incentive bias in guidance.** The bonus metric excludes the IRU, and FCF was dropped in the first IRU year (gilat_fy2025 p.92, p.207; gilat_fy2024 p.193).<br>**Social proof.** "Unprecedented expression of confidence" (p.90).<br>**Consistency.** The team's base of 0.789 was cut to 0.428 at this gate |
| E8 | Independent of any single outside variable? | VETO | n/a (lane C; binds A, B, D and bonds) | Would fail: Customer A is 25% of revenue and Vodacom 16% (gilat_fy2025 p.32, p.55) |
| E9 | Written in Li Lu's four categories, with outside scuttlebutt? | FLAG | n/a (lane C) | Written anyway (gate.md §4; scuttlebutt.md §8) |

## F. Israel-specific

| # | Question (yes = pass) | Type | Answer | Evidence |
|---|---|---|---|---|
| F1 | Control chain mapped; no pledged controller with debt above the pledged value? | VETO | yes | No controller since 17.2.2021 (gilat_fy2025 p.214). The largest holders are the CEO (7.93%) and Ayalon funds (6.22%) (scuttle §2). No pledge is disclosed. Whether the CEO's shares are pledged is an open item |
| F2 | Five years of related-party deals, controller pay and minority votes read; no tunnelling; rejections explained? | VETO | yes | **No controller.** Related-party dealings are pay only (gilat_fy2025 p.215, p.176).<br>**Votes.** The pay policy was re-approved on 13.3.2024 (p.63) and the CEO package on 4.12.2025 (p.206). No meeting's rejection was overridden (p.233, item 32).<br>**Not read.** The vote tallies on Maya: an open item, not a failure |
| F3 | Consolidated statements; currency read before ratios; single-source figures checked? | VETO | yes | **Statements.** Consolidated statements throughout (gilat_q2_2026_full p.30-39), not the solo data.<br>**Currency.** USD to 2025, ILS from 2026 (p.42). The market cap is converted at the dated 3.157 |
| F4 | Currencies and CPI linkage recorded; survives a shekel move, high CPI and +2 points? | VETO | **no** | **Exposure.** USD liabilities 90,430 against USD assets 24,967 (gilat_h1_2026 p.19). The IRU is half CPI-linked (gilat_fy2025 p.153).<br>**Stresses.** USD/ILS +10% takes the base to 0.000, and +20% also to 0.000. CPI at 5% costs 0.096 a share. +2 points: no hit (out §5) |
| F5 | Holdco: look-through NAV; holdco debt serviceable? | VETO for holdcos | n/a (not a holding company) | An operating group (gilat_fy2025 p.8) |
| F6 | No-edge set, maintenance list, liquidity, window flag, TASE cap? | FLAG | yes | **Edge.** Not TA-35, not dual-listed.<br>**Maintenance list.** Not on it: the public holds 85.8-92.0% (scuttle §2).<br>**Liquidity.** Median turnover ILS 1,325,803 (scuttle §1).<br>**Data flag.** `cycle_window_short` carried.<br>**TASE 30% cap.** Fund-level; the size here is 0% |

## G. Position sizing, adding and taxes

| # | Question (yes = pass) | Type | Answer | Evidence |
|---|---|---|---|---|
| G1 | Size = smallest of quarter-Kelly, tier cap, 5%/L_worst, liquidity, sector, TASE? | VETO | yes | `position_size()`: full Kelly 0%, so quarter-Kelly binds at 0.0% of NAV. Tier cap 5%; loss budget 5% (L_worst 100%); liquidity maximum ILS 4,006,416 (out §7) |
| G2 | Could hold through a 50% quote fall without forced selling? | VETO | cannot assess here (fails closed) | No leverage by charter. The principal's cash needs are outside this environment |
| G3 | Fits within twelve monitoring slots? | VETO | cannot assess here (fails closed) | The fund's holdings are not available here (the size is 0%) |
| G4 | Lane declared now with its sell rule? | VETO | yes | Lane C, cyclical. Sell rule: principal out at a double, then half at each further double; never on a price fall alone (charter, "Sell rules") |
| G5 | Sized to matter? | FLAG | n/a (lane C) | — |
| G6 | Better than adding to an existing holding (punch card)? | FLAG | n/a (lane C) | — |
| G7 | Add after a fall: filings read, no condition fired, cap kept? | VETO for adds | n/a (not an add) | No position is held |
| G8 | Expected return, dividend/buyback and swap stated after tax; not a US PTP? | FLAG | cannot assess here (counts as no) | `tax_params` is not available. It is not a US publicly traded partnership |

## H. Lane C bargains

| # | Question (yes = pass) | Type | Answer | Evidence |
|---|---|---|---|---|
| H1 | Explain how it makes money and what its assets are worth to a buyer? | VETO | yes | **How it earns.** It resells capacity it does not own (satellite capacity and airtime, Bezeq fibre) with integration and service, billed monthly (business.md §1.2).<br>**What the assets are worth.** Dempster 0.094 a share at 30.6.2026 and 0.010 pro forma (out §4); nil once the unpaid Bezeq consideration counts. Control could not be sold in 2021 (Calcalist L-3894358) |
| H2 | Asset value firm: NCAV and Dempster from one date, identity-checked? | VETO | **no** | NCAV is 37,844 and Dempster 11,095 at 30.6.2026. But the unpaid Bezeq consideration of 223,595 (UNVERIFIED) is 5.9x NCAV, and the PV of the unfilled lines is 135,760 (out §4) |
| H3 | Floor not burned: 3-year average OCF ≥ 0, or burn below 10% of NCAV? | VETO | yes | OCF was positive every year FY2020-25. The FY2023-25 average after lease payments is USD 5,136k (out §3) |
| H4 | A catalyst, or held in a basket of ≥20? | VETO | **no** | No deal. The only attempt to sell control failed, in 2021, at no premium (out §4). The licence restricts acquirers (gilat_fy2025 p.72-74). A single name |
| H5 | Cyclical: no net debt, low-cost position, valued on the whole window? | VETO | **no** | Valued on W = FY2020-25. But it has no low-cost position (cost parity per line at best: scuttlebutt.md §2) and net debt of 10.8x-26.2x EBIT_norm with the IRU (out §3) |
| H6 | Lane D: problem beside the franchise, customers still buying? | VETO | n/a (lane D only) | — |

## FLAG items answered "no", with explanations

The checklist requires a written explanation for every FLAG "no". **Eight FLAG items count as "no": six are answered "no" and two cannot be assessed here.** None of them is explained away. Each is a real weakness, consistent with NO_THESIS.

1. **A7, industry rationality.** Low-orbit operators are adding capacity fast and selling direct below customary prices. Gilat itself buys ISP share on promotions. This is an irrational, fast-supply industry for a reseller.
2. **B2, buybacks.** Shares were bought at 4.7-6.1x base value, and they took back only 17.7% of the shares that conversions at 1.00-1.35 issued in H1 2026 (out §7). This transfers value from the owners who stay.
3. **B6, institutional imperative.** No acquisition yet, but money was raised for "synergistic" deals and management advertises inorganic growth. With pro forma cash of ILS 86.9M, the risk is live.
4. **C4, cash conversion and build-up.** The cash clause and the build-up clause both fail.
5. **C6, stress-year cover.** Interest was not covered comfortably in FY2020 (1.2x) or FY2022 (−0.9x).
6. **E7, misjudgment tendencies.** Management's own guidance carries incentive bias and social proof. The fund's valuation uses none of management's metrics, and the gate corrected its own team's optimistic base.
7. **D6, swap test.** It cannot be computed here: holdings and the tax model are unavailable. The expected value is below the price in any case.
8. **G8, after-tax statement.** `tax_params` is unavailable. This goes to the principal.

## Red-team reviewers and their objections

The two reviewers below argued the bear case. Every objection is answered in `gate.md` §1, with evidence.

| Reviewer | Objections | Accepted | Partly accepted | Rejected |
|---|---|---|---|---|
| **gilat_telecom:redteam-accounting** (`redteam_accounting.md`) | O1-O11 | **all 11** | — | — |
| **gilat_telecom:redteam-business** (`redteam_business.md`) | O1-O10 | **7:** O1, O4, O5, O6, O7, O9, O10 | **3:** O2, O3, O8 | — |

**What the three partial acceptances keep and change:**
- **O2.** The shadow buy line is withdrawn and H2 is recorded "no". But the lane stays declared as C, because G4 requires a declared lane and a sell rule, and the cyclical C sell rule can be stated. It is recorded as "no lane satisfied today".
- **O3.** The weights (15/30/45/10), the explicit Vodacom scenario and the net optimistic case are adopted. The proposed label "requires war-level revenue or margin" is replaced by the computed reading in out §5.
- **O8.** The vote tallies are recorded as unread and sent to the principal. F2 still passes, because no pay vote was rejected (gilat_fy2025 p.63, p.206, p.233).

**The FLAG "no" explanations above match the reviewers' own findings:**
- A7, B2, B6 and E7: gilat_telecom:redteam-business (O5).
- C4 and C6: gilat_telecom:redteam-accounting (O5, O7).
