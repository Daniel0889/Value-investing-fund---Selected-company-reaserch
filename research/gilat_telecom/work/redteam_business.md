# Gilat Telecom Global (TASE 1080597): red team on business, management, Israel and inversion

Prepared 3.11.2026 for the Rev 4 study, charter step 8 (an independent analyst argues the bear case). Lens: checklist
A0-A8, B1-B7, E1-E9, F1, F2, F5, F6 and H1-H6. I tested the team's files (`valuation_notes.md`,
`research/gilat_telecom/output.txt`, `business.md`, `governance_risk.md`, `market.md`, `scuttlebutt.md`) against
the filings and the web. I edited no file other than this one.

**How to read this file.**
- Every derived number comes from the code in section 9 of this file. It was run with `python3 -I` on the block
  extracted from this file, and its printout is pasted below it. "calc §n" points to that printout.
- Filing figures cite document id and PDF page. I opened these pages as images: gilat_fy2025 p.32, 55-56, 92-93,
  181-182, 205-207; gilat_fy2023 p.166; gilat_h1_2026 p.8; gilat_q2_2026_full p.11. Narrative quotes from other pages
  come from the text layer: gilat_fy2025 p.12, 16, 27, 39-42, 50, 82-86, 90, 99-100, 152-153, 183, 219, 233;
  gilat_fy2024 p.88-89, 193-194; gilat_fy2023 p.91; gilat_h1_2026 p.12, 14-15, 24, 37.
- Web items: I re-read the saved raw copies of the Bizportal interview of 4.3.2025, the Calcalist article of 17.2.2021
  and Bezeq's report of 4.11.2025 (scuttle/raw/). Items resting on a search-engine summary are marked UNVERIFIED.
  www.ynetnews.com and www.ecofinagency.com did not resolve from this session; they would have to be allowed in the
  session's network settings.

---

## 0. Bottom line

**NO_THESIS stands, and it is robust.** Nothing I found moves Gilat toward WATCHLIST or BUY. The record is too kind
to the business in five places:

1. **B5 (VETO) is a "no", not "open".** The headline metrics leave out the Bezeq cost: the CEO's bonus metric,
   "free cash flow excluding prepaid expenses" and the "not leveraged" claim. The accounting policy defers that cost,
   and the Starlink threat to Vodacom goes unmentioned. Against an economic charge for the fibre lines, TTM EBIT is
   flattered by ILS 2.8-6.6M (7-17%; calc §5).
2. **The 0.316 "shadow" buy price should go, and H2 should be "no".** The charter does not allow an earnings value
   to stand in for private-owner value (d7, d11). The unpaid Bezeq consideration is 5.9x NCAV (calc §8), so the asset
   value is not firm.
3. **The base is not "erring conservative".** EBIT_norm needs either war-level revenue (1.37-1.76x the CEO's own
   "routine" level, at the FY2021-24 gross margin) or a war-level gross margin (calc §1). Vodacom alone is about 74%
   of EBIT_norm (calc §2), and Vodacom's group partnered with Starlink in November 2025 [SIA-VOD]. Under defensible weights the probability-weighted value
   is 0.615-0.654, against the team's 0.828 (calc §7).
4. **E1 fails on the company's own filed history, not only on the UNVERIFIED Bezeq schedule.** Three consecutive annual
   reports (FY2023-FY2025) carried the dedicated working-capital disclosure of the warning-sign regime, and in July 2024
   the company swapped bonds for shares.
5. **Four lane-C items were skipped: A7, B2, B6 and E7.** Each applies to lane C, and each is a "no".

**Pabrai's test inverts.** From 165.3 agorot the optimistic case is +16.2% (about +4.9% after the Bezeq accounting
gap), the base −52.3% and the worst case −100% (calc §7). Heads you win a little; tails you lose a lot.

**The Petco rule.** Known facts explain the market's P/E of about 6 on TTM:
- the CEO's own public statement that the war doubled turnover;
- Vodacom Group's Starlink partnership;
- the Bezeq commitment;
- the convertible overhang;
- the accounting that flatters TTM.

The price is also 2.10x the fund's base value (output.txt), so there is no discount to refute.

---

## 1. Objections, ranked

### O1 (high): B5 is a fail, not "open"

**Claim.** B5 asks two things: are the accounts understandable without "adjusted" earnings that leave out real costs,
and does management report its mistakes candidly? The record shows a pattern, not a single item.

**Evidence.**

1. **The CEO is paid on a metric that excludes the Bezeq cost.**
   - Adjusted EBITDA is EBITDA less satellite-lease depreciation only (gilat_fy2025 p.92). It therefore leaves out
     the Bezeq IRU amortisation, USD 1,079k in 2025 (the ISP segment's D&A, gilat_fy2025 p.181).
   - 70% of the CEO's 2025 bonus rides on it, and the other 30% on gross profit (gilat_fy2025 p.207).
   - Free cash flow carried 30% of the 2023-24 bonus (gilat_fy2024 p.193). It was dropped for 2025, the first year
     of Bezeq payments (ILS 13,752k; gilat_q2_2026_full p.38).
   - The 2025 cap was "up to 6 salaries" (gilat_fy2024 p.194). The meeting of 4.12.2025 raised it to 8 for the year
     then ending, and achievement was 125% (gilat_fy2025 p.206-207).
2. **The headline free cash flow adds the Bezeq payments back.** "Free cash flow excluding prepaid expenses" does so:
   USD 2,929k in 2025 (gilat_fy2025 p.93). The 20.8.2026 presentation repeats it.
3. **"Not leveraged" sits beside an unrecorded commitment.**
   - The report says: "Today the company is not leveraged and has reduced its debt risks to zero levels"
     (gilat_fy2025 p.90).
   - The same page touts the Bezeq agreement. ILS 248M of one-time consideration is not recognised as a liability.
   - The commitment is absent from the risk-factor table (gilat_fy2025 p.82-86). That table does flag fixed
     satellite-capacity purchases (item 27.4), but not the Bezeq commitment.
4. **The accounting defers the cost of the fibre lines.**
   - **The stated policy.** Amounts paid, including the vendor-financing interest, are capitalised and amortised
     over 25 years, including two unexercised five-year options (gilat_fy2025 p.153).
   - **The booked charge does not fit the policy.** TTM amortisation is ILS 6,955k (gilat_q2_2026_full p.38), about
     27.6 per line-month, against 16.3 on 25 years and 27.2 on 15 years (calc §5). The team could not reconcile it
     either (business.md §14 item 10).
   - **Management's attribution.** It credits the H1 2026 rise in gross margin "mainly" to "the engagement with Bezeq
     in the IRU agreement" (gilat_q2_2026_full p.11).
   - **The fund's own comparison.** On the fund's own PV, the IRU costs about what regulated BSA costs: IRU-1 5,658
     and IRU-2 5,142 per line, against BSA 5,552 (output.txt).
   - **The size of the effect.**
     - Against an economic charge (15-year use, vendor interest expensed), TTM EBIT is flattered by ILS 2,818-6,593k,
       or 7.1-16.7% (calc §5).
     - On the stated policy, the gap reaches ILS 13,984-16,131k a year at 54,000 lines, 1.26-1.45x EBIT_norm
       (calc §5).
     - A large part of the reported "IRU margin gain" is therefore accounting. The cost booked per line (calc §5) is
       well below the economic cost, which on the fund's own PV is about the regulated BSA price. The BSA price before
       the decision of 26.2.2026 is not in the documents, so the economic saving against the old wholesale price
       cannot be measured here.
5. **The Vodacom risk is not disclosed.**
   - Vodacom was USD 12,392k of revenue, 16% of 2025 (gilat_fy2025 p.55). Its contract runs to March 2027.
   - The Q2 report says only that the company "is working to renew" (gilat_h1_2026 p.15).
   - Neither report mentions Vodacom Group's Starlink partnership of 12.11.2025 [SIA-VOD]. Nor do they mention
     Vodacom DRC's reported Starlink talks for remote sites [SEMAFOR, UNVERIFIED].
   - In fairness, the FY2025 report does say, in general terms, that Starlink is taking "a significant part" of the
     growth in African satellite demand and pressing on GEO VSAT models (gilat_fy2025 p.27). What is missing is the
     link to the company's own anchor customer.
6. **The CEO's option "premium" was a premium to a lagging average.**
   - The options were described as carrying "a significant premium of 20%" (gilat_fy2025 p.206). The premium was
     over a 30-day average.
   - At the general meeting, the two strikes were 18.7% and 3.4% below the close (calc §10).
   - The board fixed the strikes no later than 28.10.2025. That was a week before the Bezeq addendum, which lifted the
     price 7.4% on its announcement (calc §10).
7. **Smaller items**, already listed in governance_risk.md §6:
   - the "no hedging" note, against the forwards the company discloses;
   - inconsistent backlog figures;
   - the payroll boilerplate;
   - the chairman's Vesttoo role, dropped from his five-year biography (gilat_fy2023 p.195 against gilat_fy2025
     p.216).

**Required change.**
- Record B5 as "no" (the VETO fails) in valuation_notes §13 and in the printout, and remove it from "open".
- Make a re-examination conditional on the FY2026 annual report, due 31.3.2027. It must:
  - state the unpaid Bezeq consideration and its schedule;
  - state the amortisation actually applied;
  - list the Bezeq commitment and Vodacom's LEO substitution as risk factors.
- In any future valuation, restate EBIT with the IRU at its economic cost (15 years, interest expensed). Never use the
  company's Adjusted EBITDA or its "free cash flow excluding prepaid expenses".

### O2 (high): delete the 0.316 "shadow" buy price, record H2 as "no", and say that no charter buy price exists

**Claim.** The printout and the summary JSON carry a buy price of 0.3155 ILS, which is the EPV base times (1 − 60%).
The charter does not allow this construct.
- **What d7 says.** Private-owner value "is evidenced only by disclosed comparable transactions, never by an
  analyst's guess".
- **What d11 allows for Tier C.** At most 2/3 of NCAV and at most Dempster value (the net-net route), or at most 50% of
  an evidenced private-owner value. The shadow line puts an earnings value in place of the private-owner value, the
  substitution the charter excludes.
- **The data additions.** It also carries data additions that, for a Tier C asset case, "apply only where the asset
  figures themselves are derived".
- **The risk of misuse.** If the price ever touched 0.31, every charter route would still say no (net-net 0.092). A
  published number invites misuse at the weekly watchlist check.

**H2 (VETO, C)** asks whether the asset value is firm, and the team passes it. Yet the unpaid Bezeq consideration
(ILS 223,595k, derived and UNVERIFIED) is 5.9x NCAV (calc §8), and the team itself counts it to fail E1 and H5. An asset
value that an unrecorded commitment of 5.9x can erase is not firm.

**G4.** Lane C's sell rule is "at base-case private-owner value". With none evidenced, that sell rule cannot be
stated. The honest declaration is "no lane fits today", as in the paymeant sibling study, with C governing only a
future net-net purchase.

**Required change.**
- Set `buy_price_ils` to null and drop the "shadow" line, or label it "not a buy price".
- State that no charter buy price exists: the net-net route gives 0.092, but H2 fails, so even that is not a buy line.
- Record H2 as "no".
- Record the lane as "none fits; C only for a future net-net".
- Keep NO_THESIS.

### O3 (medium): the base and the optimistic case lean on war-level revenue or war-level margin; re-weight them

**Claim.** The base (45%) and the optimistic case (20%) are not "realistic, erring conservative" (framework (d),
general rules).

**Evidence.**
- **What the base needs.** Base EBIT_norm of ILS 11,100k needs revenue of ILS 189,614-243,223k at the FY2021-24 mean
  gross margin of 23.3%. That is 1.37-1.76x the "routine" level the CEO himself describes, half of TTM or ILS 138,046k
  (calc §1).
  - The alternative is a war-level gross margin of 30.9%, held at routine revenue with FY2023-24 opex (calc §1).
  - At routine revenue and pre-2025 margins, EBIT is between ILS −938k and −13,452k (calc §1).
- **The CEO's own words**, Bizportal 4.3.2025 [BZ-20014148]:
  - "Following the war we reached high turnovers, about double compared to the normal period."
  - "Security is about 50% of turnover in wartime, while in routine it is about 30%."
  - "Part of this increase is expected to stay with us."
  - On that framing, routine defence revenue is about ILS 41,414k. That is 0.27x the 2025 government segment, and
    below the 2022 segment of ILS 46,632k (calc §1).
- **Government backlog at the FY2025 report date** (gilat_fy2025 p.32; calc §3):
  - USD 20,376k for 2026, 42.4% of 2025 segment revenue;
  - USD 2,195k for 2027-2029, 4.6%.
- **Customer A** (25% of 2025 revenue) is an unnamed Israeli buyer (gilat_fy2025 p.32). The segment's reported orders are
  12-month orders and non-binding frameworks (gilat_h1_2026 p.15; business.md §1.4). The Iran ceasefire took effect on
  8.4.2026 [search summary, UNVERIFIED].
- **Vodacom.** At the 2025 global-segment margin, Vodacom contributes about ILS 8,173k, 73.6% of EBIT_norm
  (gilat_fy2025 p.55, p.181; calc §2; the contract's own margin is UNVERIFIED). The base assumes renewal implicitly.
  Only the worst case (10%) removes it.
- **The optimistic case** is EPV on TTM EBIT_adj forever. It inherits the IRU accounting gap. Even untouched it is
  only +16.2% from the price, about +4.9% after the gap (calc §7).
- **The bull's best point, acknowledged.** Israel's defence budget stays elevated: ynet's headline of 13.5.2026 reads
  "record $62.8 billion", and spending is expected to stay high through 2027-28 [search summary, UNVERIFIED]. But
  Gilat's share of the field is "not material" and competition is "mainly on price" (gilat_fy2025 p.32). The budget
  is not Gilat's revenue.

**Required change.**
1. Put Vodacom's non-renewal into the base with an explicit probability, or make it a separate scenario.
2. Cut the optimistic weight to at most 10%, and raise the worst and conservative weights. Report the
   probability-weighted value under the red-team weights next to the team's 0.828 (calc §7):
   - 0.654 at 15/30/45/10;
   - 0.615 at 20/30/40/10.
3. Label the base in the notes: "requires war-level revenue or war-level gross margin".

### O4 (medium): E1 should rest on the filed record, and the worst-case weight is too low

**Claim.** The team's E1 rests on the UNVERIFIED Bezeq schedule and on the phrase "came under Series C maturity
pressure", which is an interpretation. The filed record is stronger.

**Evidence.**
- **Three years in the warning-sign regime.** Three consecutive annual reports carried the dedicated working-capital
  disclosure that the warning-sign rules require (Reg. 10(b)(14)):

  | Date | Consolidated working capital | Solo | Source |
  |---|---|---|---|
  | 31.12.2023 | deficit USD 357k | operating cash flow negative | gilat_fy2023 p.91 |
  | 31.12.2024 | deficit USD 9,484k | operating cash flow negative | gilat_fy2024 p.88-89 |
  | 31.12.2025 | deficit USD 1,874k | working-capital deficit USD 3,942k | gilat_fy2025 p.99 |

  Each year the board had to minute that there was "no liquidity problem". In fairness, part of the 2024-25 deficit
  comes from the convertibles being classed as current.
- **The July 2024 exchange.** Series C holders exchanged 9,965,474 par for 17,439,580 shares plus ILS 597,928. The
  company calls this "significant debt reduction" and a significant reduction of its financing levels
  (gilat_fy2024 p.88-89). A bond-for-share exchange inside that regime is the near-twin of marker 1.
- **The regime ended only at 30.6.2026**, after war-peak earnings and the conversions: working capital was positive and
  no warning signs remained (gilat_h1_2026 p.14).
- **Fixed claims today.** The unpaid IRU, Series D par and leases together are 3.26x pro forma cash (calc §8).
- **No way out of pulse 1.** It has no deferral clause. Gilat is released only from subsequent pulses, and only if it
  misses its growth targets (gilat_fy2025 p.42, p.183).
  - If the ISP succeeds, Gilat must buy pulses 2-4: about ILS 80M each, CPI-linked, with no price protection
    (gilat_fy2025 p.42).
  - Bezeq says most of the addendum's "over NIS 600 million" is paid "over the first years" [BZQ-IRU].
- **Series D.** It converts at ILS 1.00 only until 1.4.2028, then at ILS 1.40, and 25% of par falls due each year from
  1.4.2028 (gilat_h1_2026 p.24).
- **The route to dilution is ready.** A shelf prospectus has been open since April 2026 (gilat_h1_2026 p.49).

**Required change.**
1. Cite the filed warning-sign disclosures and the 2024 exchange as the E1 evidence, in the filing's own words.
2. Raise the worst-case weight from 10% to 15-20% (calc §7).
3. State that E1 fails at any price until two things happen: the FY2026 report quantifies the Bezeq obligation, and a
   non-war year shows positive lease-adjusted cash flow.

### O5 (medium): lane-C items were skipped; A7, B2, B6 and E7 are each "no"

**Claim.** The checklist's "Applies to" column binds four items to lane C:
- A7: "All except E";
- B2: "All except E";
- B6: "All except E";
- E7: "All".

valuation_notes §13 lists A1-A8 and B6 as n/a, and leaves out B2 and E7.

**Evidence.**
- **A7 = no.**
  - Starlink "sells its services at prices much lower than customary in the industry and works directly with end
    customers ... changing the industry radically" (gilat_fy2025 p.50). It is "a direct competitor to the company's
    GEO-based VSAT products" (gilat_fy2025 p.16).
  - Gilat itself buys share in the ISP with promotions: derived Q1 2026 ARPU was 73.2, −15.8% against FY2025
    (gilat_h1_2026 p.8; calc §4).
  - Bezeq signed the IRUs partly to fill its network before its rivals did, at "relatively aggressive" prices
    [BZ-838877].
- **B2 = no.**
  - The company bought 4,574,810 shares at an average of ILS 2.319. That is 2.05x the ILS 1.132 of par each share
    retired in the H1 2026 conversions.
  - The June buyback averaged 3.3x the team's base and the October one 2.6x (calc §6).
  - The June programme began on 12.6.2026, the day of the closing high of 282.8 (TASE series; market.md §2.1).
  - Buybacks offset only 17.7% of the H1 2026 conversion shares (calc §6).
  - Management justified the October programme with "the share price does not fully reflect ..." (Sponser
    7.10.2026, via market.md §3).
- **B6 = no (FLAG).**
  - The stated strategy is "inorganic growth — examining potential acquisitions" and "acquisition of activities and
    synergistic investments" (presentation 20.8.2026, p.8 and p.23).
  - Series D money was raised partly for "synergistic strategic deals" (gilat_fy2025 p.99-100).
  - The largest commitment in the company's history, the Bezeq IRU at 1.25x the market cap (governance_risk.md §4.5),
    was made in the same years.
- **E7 = no.**
  - Incentive bias: see O1 item 1.
  - Social proof in management's own framing: an "unprecedented expression of confidence from leading investment
    bodies and institutional investors" (gilat_fy2025 p.90).

**Required change.** Record the four items with written explanations. The red team does not accept them blank or as
n/a.

### O6 (medium): the Bezeq IRU is a negatively skewed option that the base prices at zero

**Claim.** The base treats all 26,400 committed but unfilled lines as filled and NPV-neutral. The structure is
skewed against the owner, so "NPV-neutral" is an upper bound.

**Evidence.**
- **Fixed delivery.** Pulse 1 (36,000 lines) arrives in 12 fixed quarterly tranches of 3,000 (gilat_fy2025 p.42,
  p.183). The company says "the quarterly deployment aligns the investment with demand" (p.42). That holds only if
  demand reaches 3,000 lines a quarter.
- **Success adds obligations.** Gilat is released from a subsequent pulse only if it misses its growth targets
  (p.42). The later pulses cost about ILS 80M each, are CPI-linked, and lack the original deal's price protection
  (p.42).
- **The regulator has narrowed the edge.** The decision of 26.2.2026 sets fibre BSA at ILS 58 a month for 2026-2031
  and leaves small ISPs unlimited access at the regulated price. The decision's text applies the regulated tariff to
  31.8.2028; whether small ISPs keep it to 2031 is ambiguous (gilat_fy2025 p.40).
  - So any small ISP can rent what Gilat committed to buy, at close to the same cost and with no commitment.
  - Per-line PV at r (output.txt): IRU-1 5,658, dearer than BSA at 5,552; IRU-2 5,142.
  - Management calls the deal "a distinct competitive advantage" (gilat_fy2025 p.42).
- **New customers come in at promotional prices.** Derived Q1 2026 ARPU of 73.2 leaves ILS 15-23 a month after the line
  cost to pay for bandwidth, customer equipment, service, marketing and churn (calc §4).

**Required change.**
- Carry in the base an expected cost for unfilled lines instead of zero: a stated probability times the conservative
  case's dead cost.
- Add a trigger: private net additions below 3,000 a quarter for two consecutive quarters.

### O7 (low): Q1/A0 should be "no", not "open"

**Claim.** The team's own work answers the circle question.
- business.md §13 finds the business "predictable 5-10 years out: no". The drivers are Israeli defence ordering, war
  intensity, LEO substitution, the Vodacom renewal, wholesale regulation and the USD, and Customer A is unnamed.
- Li Lu's test, knowing the business better than the market, cannot be met. Customer A's ordering is not public.
  The CEO's public statement has already told the market that the war doubled turnover.
- "Cannot be assessed here" (CIRCLE.md missing) understates the finding.

**Required change.** Record Q1 as "no: outside the circle except as a net-net". A re-examination needs a written
circle extension, not only new figures.

### O8 (low): F2 passes on the questionnaire, but the vote tallies were not read

**Claim.** There is no controller, so F2's tunnelling test is mostly moot.
- **What the filings show.**
  - The meeting of 4.12.2025 approved the CEO's option grant together with an update to his terms
    (gilat_fy2025 p.219). Per the CEO-pay section, those terms include the salary rise and the bonus cap raised from 6
    to 8 for 2025 (gilat_fy2025 p.206).
  - The governance questionnaire confirms that the board never overrode a general-meeting rejection
    (gilat_fy2025 p.233, item 32).
- **What was not read.** The vote tallies of the disinterested shareholders are in Maya immediate reports, which were
  not read. Neither was the 13.3.2024 vote on the compensation policy.
- **The control history.** In October 2024 three parties obtained permits to rise to 13.4-26%. The Ministry
  presumed one of them, Shidurit, to be the controller (gilat_fy2024 p.199). Control can re-form quickly.

**Required change.** Record F2 as "pass on the questionnaire; vote tallies not read". Read the tallies before any
re-examination.

### O9 (low): H4 and private-owner value; the 2021 attempt to sell control failed

**Claim.** The team writes "no disclosed control transaction". The record holds stronger evidence against a control
premium.
- On 17.2.2021 Eurocom's liquidators spread the 41% control block across institutions in 2-3% lots, for about
  ILS 26M at a ILS 68M market value. They did so "after previous attempts to sell the control core in the company did
  not succeed" [CAL-0217].
- The implied value is 6.7% below the market price (calc §9): no premium.
- The licence requires the Minister's consent for any 5% holding and an Israeli acquirer (gilat_fy2025 p.72-74, via governance_risk.md §1.3).

**Required change.** Record under H4 and d7 that the only disclosed attempt to sell control failed, at no premium. Do
not assume a takeover catalyst.

### O10 (low): sharper, earlier re-examination triggers

**Claim.** The team's triggers mature in March 2027 or later. Earlier observable tests exist.
- Last cycle, the annual government orders were reported in December 2025 and January 2026: about ILS 110M including VAT
  "for the coming year" (business.md §1.4), and an ILS 52M ten-month order on 5.1.2026 [BZ-20025845].
- The unified satellite, Iridium, trade and OneWeb licences all expire on 31.12.2026 (gilat_fy2025 p.69-72, via business.md §6).

**Required change.** Add three dated triggers:
1. By 31.1.2027, compare the 2027 orders reported from the Israeli defence and government customers with the same window
   a year earlier. A fall below half confirms the normalisation.
2. The licence renewals reported by 31.12.2026.
3. Private ISP net additions below 3,000 a quarter for two consecutive quarters (O6).

---

## 2. Pre-mortem: it is November 2031, and buyers at 165.3 agorot lost money permanently. What happened?

**The most likely path: a slow squeeze that ends in dilution.**
1. **2027: defence orders normalise.** The ceasefire held. Customer A's 2027 orders, reported in December 2026 and
   January 2027, came in at a fraction of 2026. That was already visible: the government backlog for 2027 onward was
   USD 2.2M (gilat_fy2025 p.32). Revenue drifted toward the CEO's "routine" level, about half of wartime.
2. **March 2027: Vodacom shrinks.** Vodacom DRC renewed for fewer sites at a lower price, and moved remote-site backhaul
   to Starlink [SIA-VOD; SEMAFOR, UNVERIFIED]. The global segment lost most of a contribution worth about 74% of
   EBIT_norm (calc §2).
3. **2027-2028: the ISP fills its lines on promotions.** Churn rose as promotional cohorts rolled over, and the big
   four answered on price. Gilat had to take all 36,000 pulse-1 lines by September 2028 regardless (gilat_fy2025 p.42).
4. **From April 2028: debt service returns.** With the share below ILS 1.40, Series D no longer converts and 25% of par
   falls due each year (gilat_h1_2026 p.24). Bezeq instalments and interest rise; Bezeq said most of the money is
   paid "over the first years" [BZQ-IRU]. The working-capital deficit returned, and with it the dedicated-disclosure
   regime the company sat in for FY2023-FY2025.
5. **2029: new money.** The company raised it under the open shelf at a deep discount, as in 2023 at the minimum issue
   price [BZ-815902, via scuttlebutt.md §3] and as in the July 2024 bond-for-share exchange. Or it renegotiated with
   Bezeq.

**Does this path reach the impairment markers?**

| Marker | On this path |
|---|---|
| A maturity or obligation leading to dilution | Yes, plausibly |
| A going-concern doubt | Possible if the raise fails |
| Assets worth less than debt | Possible: an onerous-contract provision (IAS 37) for unfilled lines would bring the Bezeq commitment onto the balance sheet |

**Other paths that end in permanent loss without a marker:**
- Management spends the cash on its announced "inorganic growth" at war-peak multiples (presentation 20.8.2026 p.23).
- The regulator lowers the wholesale price after 2028-2031, while the new Bezeq lines carry no price protection
  (gilat_fy2025 p.40, p.42).
- **A compliance event in the African agent model.** The ingredients are success-fee agents, about USD 2.4M of prepaid
  "Vodacom deal costs" (gilat_fy2024 p.83), no anti-bribery disclosure, and 300 hours a year of internal audit
  (governance_risk.md §1.4, §7). No allegation exists; this is an unexamined tail risk.

At today's price the base alone is −52.3% (calc §7): a permanent loss for the buyer even if no marker is ever filed,
because the price pays for war-peak earnings.

---

## 3. The bear case, argued better than the best bear (E4), and the best bull case

**The bear case in five sentences.**
1. Gilat is a reseller of other companies' capacity, with no moat: competition is "mainly on price" and its share is
   "not material" (gilat_fy2025 p.32).
2. Its profits are a war dividend that its own CEO sizes at about double normal turnover [BZ-20014148]. At the FY2025
   report date, government backlog for the years after 2026 was USD 2.2M (gilat_fy2025 p.32).
3. Its second leg, Vodacom DRC, is a single contract worth about three-quarters of normalised operating profit
   (calc §2), held by a customer whose group is now partnering with Starlink [SIA-VOD].
4. Its growth leg, the ISP, has turned a variable, regulated input (BSA at ILS 58, unlimited for small ISPs;
   gilat_fy2025 p.40) into a fixed obligation 5.9x NCAV (calc §8). Its accounting reports that obligation's cost at
   well below its economic cost (calc §5).
5. Management is paid on a metric that excludes that cost (gilat_fy2025 p.92, p.207), buys back stock at 2-3x value
   (calc §6), and plans acquisitions (presentation 20.8.2026).

**The $1bn test (A4; n/a for lane C, answered anyway).** Well-funded competitors are already doing the damage.
- Starlink sells direct to end users "at prices much lower than customary in the industry" (gilat_fy2025 p.50). It has
  been licensed in the DRC since June 2025 and has sold direct in Israel since August 2025 (scuttlebutt.md §0 and §1.1).
- The state launched its own satellite, Dror-1, in July 2025 (gilat_fy2025 p.19-20, via business.md §5).
- SES and Intelsat merged and target synergies, which shifts pricing power to Gilat's main supplier
  (scuttlebutt.md §1.3).
- A4 would fail if it applied.

**The best bull case, and why it does not change the verdict.**
- Israel's defence budget stays elevated through 2027-28 [UNVERIFIED].
- The ISP added 7,635 private subscribers in H2 2025 and 7,116 in H1 2026 (business.md §1.6).
- Vodacom renewed once, in 2024, as the company's "largest and most significant service agreement in the last decade",
  and SES mPOWER is a differentiated MEO product (gilat_fy2025 p.56).
- Cash is ILS 92,955k (gilat_q2_2026_full p.30).

Even granting all of it, the optimistic case is only +16.2% from the price (calc §7). The fund would be paying today for
the bull case, with no margin of safety.

---

## 4. Would Buffett, Munger, Pabrai or Li Lu buy it?

**No. Each for his own reason.**
- **Buffett.** There is no durable advantage and no pricing power: suppliers can reprice on 30 days' notice
  (gilat_fy2025 p.66, via business.md §7), and the largest customer orders 12 months at a time. The board raised the CEO's bonus cap at
  the end of the year being measured. "Adjusted" metrics exclude a real cost. Shares have doubled since 2022
  (governance_risk.md §4.3).
- **Munger.** Invert: what kills it is in plain view (peace, LEO, the fixed Bezeq commitment). Incentives explain the
  rest: 70% of the bonus rides on a metric that the Bezeq deal mechanically raises (O1).
- **Pabrai.** This is not "heads I win, tails I don't lose much". It is high risk (fixed obligations, concentration),
  not merely high uncertainty, and the asymmetry runs the wrong way (calc §7).
- **Li Lu.** Nobody outside can know the one variable that matters, Customer A's ordering, better than the market. The
  market has already been told by the CEO.

---

## 5. Checklist items in my lens: the team's reading against mine

| Item | Applies to | Team | Red team |
|---|---|---|---|
| A0 / Q1 | A, B, D / all | open | **no** (O7) |
| A1-A6, A8 | A, B, D | n/a | n/a. A2, A3, A4 and A6 would fail if they applied |
| A7 | all except E | n/a | **no** (O5) |
| B1 | A, B, D | n/a | n/a |
| B2 | all except E | not recorded | **no** (O5) |
| B3 | all | no | no (agree) |
| B4 | A, B, D | n/a | n/a. It would fail: the bonus rides on Adjusted EBITDA (O1) |
| B5 | all (VETO) | open | **no** (O1) |
| B6 | all except E | n/a | **no, FLAG** (O5) |
| B7 | all (VETO) | pass on the record; open on courts | agree. My own web search on the chairman and the Bezeq/Case 4000 affair found no allegation against him |
| E1 | all (VETO) | no | no, on the filed record; worst-case weight 15-20% (O4) |
| E2 | all | re-examination triggers | sharpen (O10) |
| E3 | all (VETO) | no | no. Add the IRU accounting to the facts that explain the TTM multiple (O1) |
| E4 | all | — | this file |
| E5 | all except E | done (scuttlebutt) | add the regulator's BSA decision and success-triggered pulses (O6) |
| E6 | A, B, D | n/a | n/a |
| E7 | all | not recorded | **no** (O5) |
| E8 | A, B, D, bonds | n/a | n/a. It would fail: Israeli defence demand and one African contract |
| E9 | A, B, D | n/a (scuttlebutt done) | n/a |
| F1 | all (VETO) | pass | pass. Residual: CEO pledge unknown; control re-formed quickly in 2024 permits (O8) |
| F2 | all (VETO) | pass | pass on the questionnaire; vote tallies unread (O8) |
| F5 | holdcos | — | n/a, not a holding company |
| F6 | all | liquidity passes | agree. The liquidity is new and conversion-driven (scuttlebutt §7) |
| H1 | C (VETO) | pass | pass. But the answer to "worth to a buyer" is Dempster value of 0.094 ILS/share with the IRU at nil (output.txt §4), nil once the unpaid IRU is counted, and control could not be sold in 2021 (O9) |
| H2 | C (VETO) | pass | **no** (O2) |
| H3 | C (VETO) | pass | pass, on the IFRS-16-adjusted proxy for FY2023-25 only; FY2021, FY2022 and FY2024 were negative on the team's own proxy (output.txt §3) |
| H4 | C (VETO) | no | no; add the 2021 evidence (O9) |
| H5 | C cyclicals (VETO) | no | no (agree) |
| H6 | D | n/a | n/a |

---

## 6. Where the team may be too harsh

Listed for balance. None of these changes the verdict.
- **Marker 3, as worded, overstates.** It compares Dempster value with all unpaid commitments, including lines not
  yet delivered. In an insolvency, Bezeq's claim for undelivered lines would be for damages, not the full price.
  Marker 1 alone carries E1.
- **The tax losses are not valued.** Unrecognised tax losses were USD 19.0M (gilat_fy2025 p.163, via valuation_notes.md §5).
- **The IPv4 pool may be a hidden asset** (scuttlebutt §3, UNVERIFIED).
- **The ISP may keep filling lines.** Net additions have run at about the tranche rate or above (business.md §1.6).

---

## 7. Open items for the principal

1. **The FY2026 annual report** (by 31.3.2027): the unpaid Bezeq consideration and its schedule, the amortisation
   actually applied, and the risk factors.
2. **Maya:** the vote tallies of the 4.12.2025 meeting (the CEO package) and of the 13.3.2024 compensation-policy vote;
   the October 2026 buyback reports.
3. **Customer A's 2027 orders:** the immediate reports of December 2026 and January 2027.
4. **Vodacom DRC:** renewal status and any Starlink deployment for cell-site backhaul [SEMAFOR, UNVERIFIED].
5. **Licence renewals** due 31.12.2026.
6. **Questions for management:**
   - the amortisation period actually applied to the Bezeq lines;
   - whether pulse-1 tranches can be deferred;
   - anti-bribery controls over success-fee agents in Africa;
   - the blackout policy around buyback decisions (the CEO bought on 1.10.2026, and the programme was approved on
     7.10.2026; market.md §3).
7. **Court search (B7) and the CEO pledge check (F1)**, as already listed in scuttlebutt.md §10.

---

## 8. Sources

| Key | What | Where | Status |
|---|---|---|---|
| [BZ-20014148] | CEO and VP interview, 4.3.2025: wartime turnover about double; defence about 50% in war and 30% in routine | https://www.bizportal.co.il/capitalmarket/news/article/20014148 (saved copy scuttle/raw/biz_art_20014148.html) | re-read 3.11.2026 |
| [CAL-0217] | Eurocom liquidators disperse the 41% control block "after previous attempts to sell the control core did not succeed", 17.2.2021 | https://www.calcalist.co.il/articles/0,7340,L-3894358,00.html (saved copy scuttle/raw/cal_3894358.html) | re-read 3.11.2026 |
| [BZQ-IRU] | Bezeq immediate report, 4.11.2025 (unofficial translation): addendum over NIS 600M, "majority ... paid over the first years" | https://cdn.financialreports.eu/financialreports/media/filings/6676/2025/RNS/6676_rns_2025-11-04_e1aa6820-2af2-43ba-8ca3-38e73d48d81b.pdf (saved copy scuttle/raw/bezeq_rns_2025-11-04.txt) | re-read 3.11.2026 |
| [BZ-838877] | CEO interview on Bezeq's motives, 29.12.2024 | https://www.bizportal.co.il/capitalmarket/news/article/838877 | via scuttlebutt.md |
| [BZ-20025845] | ILS 52M ten-month order, 5.1.2026 | https://www.bizportal.co.il/capitalmarket/news/article/20025845 | via scuttlebutt.md |
| [SIA-VOD] | Vodacom Group and Starlink partnership, 12.11.2025 | https://spaceinafrica.com/2025/11/12/vodacom-group-and-starlink-partners-to-transform-connectivity-across-africa/ | via scuttlebutt.md |
| [SEMAFOR] | "DR Congo mobile firms in talks with Elon Musk's Starlink", 3.11.2025: a Vodacom executive on a "complementary" service for hard-to-reach areas | https://www.semafor.com/article/11/03/2025/elon-musks-starlink-in-talks-with-dr-congo-mobile-firms ; also https://bankable.africa/en/digital/0611-1948-africell-and-vodacom-explore-starlink-partnership-in-dr-congo | search summary only, UNVERIFIED |
| [YNET-DEF] | "Israel's defense budget set to hit record $62.8 billion as tensions persist on all fronts", 13.5.2026 | https://www.ynetnews.com/business/article/syvfp7ujzg | headline via search; host did not resolve; UNVERIFIED |
| [CEASEFIRE] | Iran ceasefire announced 7.4.2026, in effect 8.4.2026 | search summary (e.g. https://english.alarabiya.net/News/middle-east/2026/04/12/iran-war-has-cost-israel-115-billion-in-budgetary-expenses-ministry-says) | UNVERIFIED |
| [PRES-Q2] | Q2 2026 results presentation, 20.8.2026 (p.8, p.23: inorganic growth, acquisitions) | https://satcom-gilat.co.il/wp-content/uploads/2026/08/מצגת-סיכום-תוצאות-הרבעון-השני-לשנת-2026-.pdf (saved copy web/pdf/q2_2026_presentation.pdf) | text re-read |
| gilat_q2_2026_full | Full Q2 2026 report with consolidated statements | https://satcom-gilat.co.il/wp-content/uploads/2026/08/דוח-רבעון-2חצי-שנתי.pdf (saved copy web/pdf/company_site_q2_2026_full.pdf) | p.11 image checked; p.30-31, p.38-39 text |
| TASE series | Daily closes and listed shares (company IR page) | web/history_data.json | used in calc §10 |

---

## 9. Calculations (the code that produced every number above, and its printout)

<!-- CALC-START -->
```python
# Red-team calculations. Run as: python3 -I (code extracted from this file). ILS thousands unless stated.
# Inputs are cited inline: filing id + PDF page, or the team's printout (research/gilat_telecom/output.txt).
FX = 3.157                                   # BoI rate 3.11.2026 (task brief; output.txt)
def pct(x): return f"{x*100:.1f}%"

# ---- history, USD k (gilat_fy2023 p.118 for FY2021-23; gilat_fy2025 p.127 for FY2024-25; via the team's page-checked financials.json)
hist = {  # revenue, gross profit, S&M, G&A, EBIT
 "FY2021": (51816, 12444, 4744, 10431, -2731),
 "FY2022": (42997, 10495, 4905,  7089, -1499),
 "FY2023": (55154, 12016, 4130,  5708,  2178),
 "FY2024": (69592, 16120, 4722,  6449,  4949),
 "FY2025": (75793, 23050, 5715,  7646,  9689),
}
ttm = dict(rev=276092, gp=85211, sm=19732, ga=25945, ebit=39534)   # ILS k, gilat_q2_2026_full p.32 (FY2025 - H1 2025 + H1 2026)
EBIT_NORM = 11100; TTM_EBIT_ADJ = 33526                             # output.txt section 3

# ---- 1. What the base EBIT_norm needs: revenue R with EBIT = R*g - opex
g_pre2025 = sum(v[1]/v[0] for k, v in hist.items() if k != "FY2025") / 4     # mean gross margin FY2021-FY2024
g_ttm = ttm["gp"] / ttm["rev"]
opex_lean = (hist["FY2023"][2] + hist["FY2023"][3] + hist["FY2024"][2] + hist["FY2024"][3]) / 2 * FX   # FY2023-24 average S&M+G&A, in ILS at spot
opex_ttm = ttm["sm"] + ttm["ga"]
rev_window_mean = (sum(v[0] for v in hist.values()) * FX + ttm["rev"]) / 6   # the base window's mean revenue, USD years at spot
rev_routine = ttm["rev"] / 2   # CEO, Bizportal 4.3.2025 [BZ-20014148]: wartime turnover "about double" the normal period
print("1. Base EBIT_norm requirement")
print(f"   gross margin mean FY2021-24 {pct(g_pre2025)}; TTM {pct(g_ttm)}; opex FY2023-24 avg at spot {opex_lean:,.0f}; opex TTM {opex_ttm:,.0f}")
print(f"   window mean revenue {rev_window_mean:,.0f}; CEO 'routine' revenue (TTM/2) {rev_routine:,.0f}; TTM revenue {ttm['rev']:,.0f}")
for gname, g in (("pre-2025 margin", g_pre2025), ("TTM margin", g_ttm)):
    for oname, o in (("lean opex", opex_lean), ("TTM opex", opex_ttm)):
        need = (EBIT_NORM + o) / g
        at_routine = rev_routine * g - o
        print(f"   {gname:<16} {oname:<10}: revenue needed for EBIT_norm {need:>9,.0f} = {need/rev_routine:4.2f}x routine, {need/ttm['rev']:4.2f}x TTM;"
              f" EBIT at routine revenue {at_routine:>9,.0f}")
defence_routine = 0.30 * rev_routine          # CEO: defence ~30% of turnover in routine
gov_2025_ils = 48065 * FX                      # gilat_fy2025 p.181 (government segment 2025, USD k)
gov_2022_ils = 14771 * FX                      # gilat_fy2023 p.166-167 via business.md section 2
print(f"   CEO framing: routine defence revenue {defence_routine:,.0f} = {defence_routine/gov_2025_ils:.2f}x the 2025 government segment; 2022 (pre-war) segment {gov_2022_ils:,.0f}")

# ---- 2. Vodacom's weight in EBIT_norm
vod_rev = 12392; glob_rev = 19655; glob_res = 4106          # USD k: gilat_fy2025 p.55; p.181
vod_contrib = vod_rev * glob_res / glob_rev * FX            # at the 2025 global-segment margin (UNVERIFIED: contract margin not disclosed)
print("2. Vodacom")
print(f"   share of global segment {pct(vod_rev/glob_rev)}; segment margin {pct(glob_res/glob_rev)}; contribution at that margin {vod_contrib:,.0f} ILS k = {pct(vod_contrib/EBIT_NORM)} of EBIT_norm")

# ---- 3. Government backlog beyond 2026 (gilat_fy2025 p.32, USD k, at the report date 3.2026)
bl_2026 = 6179 + 5211 + 4653 + 4333; bl_after = 2116 + 79
print("3. Government backlog")
print(f"   2026 {bl_2026:,} = {pct(bl_2026/48065)} of 2025 segment revenue; 2027-2029 {bl_after:,} = {pct(bl_after/48065)}")

# ---- 4. ISP pricing against the line cost
arpu_q2 = 80.19; arpu_fy25 = 86.85; q_on_q = 0.096         # gilat_h1_2026 p.8 (ARPU "improved ~9.6% vs Q1 2026")
arpu_q1 = arpu_q2 / (1 + q_on_q)
line_cost = {"IRU-1 at 5% vendor rate": 55.6, "IRU-2 at 5% vendor rate": 50.5, "BSA regulated": 58.0}   # business.md section 1.6 (calc section 9); gilat_fy2025 p.40
print("4. ISP")
print(f"   derived Q1 2026 ARPU {arpu_q1:.1f} ({pct(arpu_q1/arpu_fy25-1)} vs FY2025 {arpu_fy25}); Q2 2026 {arpu_q2}")
for k, c in line_cost.items():
    print(f"   {k:<26} {c:5.1f}/month -> left for bandwidth, CPE, service, marketing, churn: Q1 {arpu_q1-c:5.1f}; Q2 {arpu_q2-c:5.1f}")

# ---- 5. IRU accounting against economic cost (per line-month, ILS)
c1, c2 = 4890.0, 160_000_000/36_000      # ILS per line: gilat_fy2025 p.153; p.183 (pulse 1 ~ILS 160M for 36,000 lines)
om = 0.04                                # O&M 4% of consideration a year, expensed (p.153, p.183)
booked = lambda c: c/300 + om*c/12       # policy: paid amounts (incl. interest) amortised over 25 years incl. two unexercised 5-year options (p.153)
pv = {"IRU-1": 5658, "IRU-2": 5142, "BSA": 5552}   # output.txt: PV per line at r = 10% over 15 years, contract terms (10 instalments at 5%) + O&M
econ10 = {k: 58.0 * v / pv["BSA"] for k, v in pv.items()}   # level monthly equivalent at the fund's r = 10%, scaled to BSA = 58
econ5 = {"IRU-1": 55.6, "IRU-2": 50.5}                     # at Bezeq's 5% vendor rate: 15-year annuity + O&M (business.md section 1.6, calc section 9)
L1, L2 = 18000, 3000                     # TTM line-years: IRU-1 fully used by end-2025 (gilat_fy2025 p.12); IRU-2 tranches Dec-25/Mar-26/Jun-26 of 3,000 (7+4+1 months) - assumption
om_ttm = om * (c1*L1 + c2*L2) / 1000     # modelled O&M in the TTM, ILS k
booked_policy = (booked(c1)*L1 + booked(c2)*L2) * 12 / 1000
booked_actual = 6955 + om_ttm            # TTM IRU amortisation 3,506 + 3,449 (gilat_q2_2026_full p.38) + modelled O&M
amort_actual_pm = 6955*1000/((L1+L2)*12)
print("5. IRU accounting (per line-month, ILS)")
print(f"   stated policy (25 years incl. unexercised options, interest capitalised): IRU-1 {booked(c1):.1f}, IRU-2 {booked(c2):.1f}")
print(f"   actual TTM amortisation {amort_actual_pm:.1f} per line-month (15-year straight line of IRU-1 would be {c1/180:.1f}; 25-year {c1/300:.1f}) + O&M -> booked {booked_actual*1000/((L1+L2)*12):.1f}")
print(f"   economic at Bezeq's 5%: IRU-1 {econ5['IRU-1']}, IRU-2 {econ5['IRU-2']}; at the fund's 10%: IRU-1 {econ10['IRU-1']:.1f}, IRU-2 {econ10['IRU-2']:.1f}; BSA regulated {econ10['BSA']:.1f}")
gaps = {}
for bname, b in (("actual amortisation", booked_actual), ("stated policy", booked_policy)):
    for ename, e in (("5%", econ5), ("10%", econ10)):
        ec = (e["IRU-1"]*L1 + e["IRU-2"]*L2) * 12 / 1000
        gaps[(bname, ename)] = ec - b
        print(f"   TTM: booked ({bname}) {b:,.0f} vs economic at {ename} {ec:,.0f} -> EBIT flattered by {ec-b:,.0f} ILS k = {pct((ec-b)/ttm['ebit'])} of TTM EBIT")
for ename, e in (("5%", econ5), ("10%", econ10)):
    gf = ((e["IRU-1"] - booked(c1)) * 18000 + (e["IRU-2"] - booked(c2)) * 36000) * 12 / 1000
    print(f"   at 54,000 lines on the stated policy, economic at {ename}: {gf:,.0f} ILS k a year = {gf/EBIT_NORM:.2f}x EBIT_norm")
gap_actual = gaps[("actual amortisation", "10%")]

# ---- 6. Buybacks against conversions, 2026
bb_sh = 2300000 + 2274810; bb_ils = 5988 + 4620      # June: gilat_q2_2026_full p.39 / gilat_h1_2026 p.37; October: market.md (UNVERIFIED vs Maya)
conv_par = 13151410 + 16032064; conv_sh = 9741785 + 16032064   # H1 2026 conversions: gilat_h1_2026 p.37
print("6. Buybacks vs conversions")
print(f"   average buyback price {bb_ils*1000/bb_sh:.3f} ILS; average H1 2026 conversion price {conv_par/conv_sh:.3f} ILS (par extinguished per share);"
      f" ratio {bb_ils*1000/bb_sh/(conv_par/conv_sh):.2f}x; bought back {pct(bb_sh/conv_sh)} of the H1 conversion shares")
print(f"   buyback prices vs team base 0.7888: June {5988/2300:.3f} = {5988/2300/0.7888:.1f}x; October {4620/2274.810:.3f} = {4620/2274.810/0.7888:.1f}x")

# ---- 7. Scenario weights and asymmetry (values: output.txt section 5)
vals = {"worst": 0.0, "conservative": 0.3563, "base": 0.7888, "optimistic": 1.9215}; price = 1.653
weights = {"team 10/25/45/20": (0.10, 0.25, 0.45, 0.20), "red team 15/30/45/10": (0.15, 0.30, 0.45, 0.10), "red team 20/30/40/10": (0.20, 0.30, 0.40, 0.10)}
print("7. Probability-weighted value")
for k, w in weights.items():
    pw = sum(wi*v for wi, v in zip(w, vals.values()))
    print(f"   {k:<22} {pw:.3f} ILS = {pct(pw/price-1)} vs price")
for k, v in vals.items():
    print(f"   {k:<13} {v:.3f} -> {pct(v/price-1)} from the price")
d_opt = gap_actual * (1-0.23) / 0.10 / 152177.660      # EPV effect per share, fully diluted count at the price (output.txt); approximate
print(f"   optimistic less the IRU accounting gap (actual-amortisation basis): about {vals['optimistic']-d_opt:.3f} ILS ({pct((vals['optimistic']-d_opt)/price-1)} vs price)")

# ---- 8. Fixed claims against cash (output.txt section 3; IRU unpaid UNVERIFIED)
cash = 86855; iru_unpaid = 223595; ser_d = 26338; leases = 33116; ncav = 37844
print("8. Claims vs cash")
print(f"   unpaid IRU + Series D par + leases = {iru_unpaid+ser_d+leases:,} = {(iru_unpaid+ser_d+leases)/cash:.2f}x pro forma cash; unpaid IRU = {iru_unpaid/ncav:.1f}x NCAV")

# ---- 9. 2021 control block [CAL-0217]: 41% sold for ~ILS 26M at a ILS 68M market value, after failed attempts to sell control
print("9. 2021 control block")
print(f"   implied 100% value {26/0.41:.1f}M vs market value 68M: {pct(26/0.41/68-1)} (no control premium)")

# ---- 10. December 2025 CEO options against the Bezeq addendum (closes, agorot: TASE series in web/history_data.json)
k_hi, k_lo = 110.15, 92.7                     # strikes, gilat_fy2025 p.206
close = {"28.10.2025 (board decision, no later than)": 84.1, "3.11.2025 (addendum signed)": 85.3,
         "4.11.2025 (addendum announced)": 91.6, "4.12.2025 (general meeting)": 114.0}
print("10. CEO options (4,000,000; strikes 110.15 / 92.7 agorot)")
for k, c in close.items():
    print(f"   {k:<44} close {c:6.1f}: strike 92.7 {pct(k_lo/c-1)}, strike 110.15 {pct(k_hi/c-1)} vs close")
print(f"   price move on the addendum announcement: {pct(91.6/85.3-1)}")
```
<!-- CALC-END -->

Printout (python3 -I on the block above, run 3.11.2026):

```text
1. Base EBIT_norm requirement
   gross margin mean FY2021-24 23.3%; TTM 30.9%; opex FY2023-24 avg at spot 33,163; opex TTM 45,677
   window mean revenue 201,420; CEO 'routine' revenue (TTM/2) 138,046; TTM revenue 276,092
   pre-2025 margin  lean opex : revenue needed for EBIT_norm   189,614 = 1.37x routine, 0.69x TTM; EBIT at routine revenue      -938
   pre-2025 margin  TTM opex  : revenue needed for EBIT_norm   243,223 = 1.76x routine, 0.88x TTM; EBIT at routine revenue   -13,452
   TTM margin       lean opex : revenue needed for EBIT_norm   143,416 = 1.04x routine, 0.52x TTM; EBIT at routine revenue     9,443
   TTM margin       TTM opex  : revenue needed for EBIT_norm   183,963 = 1.33x routine, 0.67x TTM; EBIT at routine revenue    -3,072
   CEO framing: routine defence revenue 41,414 = 0.27x the 2025 government segment; 2022 (pre-war) segment 46,632
2. Vodacom
   share of global segment 63.0%; segment margin 20.9%; contribution at that margin 8,173 ILS k = 73.6% of EBIT_norm
3. Government backlog
   2026 20,376 = 42.4% of 2025 segment revenue; 2027-2029 2,195 = 4.6%
4. ISP
   derived Q1 2026 ARPU 73.2 (-15.8% vs FY2025 86.85); Q2 2026 80.19
   IRU-1 at 5% vendor rate     55.6/month -> left for bandwidth, CPE, service, marketing, churn: Q1  17.6; Q2  24.6
   IRU-2 at 5% vendor rate     50.5/month -> left for bandwidth, CPE, service, marketing, churn: Q1  22.7; Q2  29.7
   BSA regulated               58.0/month -> left for bandwidth, CPE, service, marketing, churn: Q1  15.2; Q2  22.2
5. IRU accounting (per line-month, ILS)
   stated policy (25 years incl. unexercised options, interest capitalised): IRU-1 32.6, IRU-2 29.6
   actual TTM amortisation 27.6 per line-month (15-year straight line of IRU-1 would be 27.2; 25-year 16.3) + O&M -> booked 43.7
   economic at Bezeq's 5%: IRU-1 55.6, IRU-2 50.5; at the fund's 10%: IRU-1 59.1, IRU-2 53.7; BSA regulated 58.0
   TTM: booked (actual amortisation) 11,009 vs economic at 5% 13,828 -> EBIT flattered by 2,818 ILS k = 7.1% of TTM EBIT
   TTM: booked (actual amortisation) 11,009 vs economic at 10% 14,701 -> EBIT flattered by 3,692 ILS k = 9.3% of TTM EBIT
   TTM: booked (stated policy) 8,108 vs economic at 5% 13,828 -> EBIT flattered by 5,719 ILS k = 14.5% of TTM EBIT
   TTM: booked (stated policy) 8,108 vs economic at 10% 14,701 -> EBIT flattered by 6,593 ILS k = 16.7% of TTM EBIT
   at 54,000 lines on the stated policy, economic at 5%: 13,984 ILS k a year = 1.26x EBIT_norm
   at 54,000 lines on the stated policy, economic at 10%: 16,131 ILS k a year = 1.45x EBIT_norm
6. Buybacks vs conversions
   average buyback price 2.319 ILS; average H1 2026 conversion price 1.132 ILS (par extinguished per share); ratio 2.05x; bought back 17.7% of the H1 conversion shares
   buyback prices vs team base 0.7888: June 2.603 = 3.3x; October 2.031 = 2.6x
7. Probability-weighted value
   team 10/25/45/20       0.828 ILS = -49.9% vs price
   red team 15/30/45/10   0.654 ILS = -60.4% vs price
   red team 20/30/40/10   0.615 ILS = -62.8% vs price
   worst         0.000 -> -100.0% from the price
   conservative  0.356 -> -78.4% from the price
   base          0.789 -> -52.3% from the price
   optimistic    1.921 -> 16.2% from the price
   optimistic less the IRU accounting gap (actual-amortisation basis): about 1.735 ILS (4.9% vs price)
8. Claims vs cash
   unpaid IRU + Series D par + leases = 283,049 = 3.26x pro forma cash; unpaid IRU = 5.9x NCAV
9. 2021 control block
   implied 100% value 63.4M vs market value 68M: -6.7% (no control premium)
10. CEO options (4,000,000; strikes 110.15 / 92.7 agorot)
   28.10.2025 (board decision, no later than)   close   84.1: strike 92.7 10.2%, strike 110.15 31.0% vs close
   3.11.2025 (addendum signed)                  close   85.3: strike 92.7 8.7%, strike 110.15 29.1% vs close
   4.11.2025 (addendum announced)               close   91.6: strike 92.7 1.2%, strike 110.15 20.3% vs close
   4.12.2025 (general meeting)                  close  114.0: strike 92.7 -18.7%, strike 110.15 -3.4% vs close
   price move on the addendum announcement: 7.4%
```
