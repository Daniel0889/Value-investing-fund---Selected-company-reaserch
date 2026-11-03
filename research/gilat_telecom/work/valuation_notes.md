# Gilat Telecom Global (TASE 1080597): charter valuation, assumptions and reasons

> **Superseded at the CIO gate (3.11.2026).** The figures below are the team's pre-gate run. After the red-team
> objections the gate re-ran `valuation.py`: base 0.428 (not 0.789), conservative 0.000, optimistic 1.718,
> probability-weighted 0.364; the 0.316 "shadow" buy line is withdrawn (the only charter Tier C line is the net-net
> 0.092, not a live buy price). Use `research/gilat_telecom/output.txt`, `gate.md` and `checklist.md` in this folder.

Prepared 3.11.2026 under Charter Revision 4 (`constitution_zip/charter_rev4_draft.md`, "Text to paste"), applying
`framework.md` (c) steps 4-10, (d) d1-d11, (e2), (h), `checklist.md` by lane, and `small_investor_and_israel.md`
Part 2.9 and Part 3.

- Code: `/home/user/value-investing-fund---selected-company-reaserch/research/gilat_telecom/valuation.py`
- Printout: `/home/user/value-investing-fund---selected-company-reaserch/research/gilat_telecom/output.txt`

Every number below is copied from `output.txt`. These notes do no arithmetic of their own. The section numbers
match the printout.

## Bottom line

| | ILS per share | agorot | USD at 3.157 |
|---|---|---|---|
| Price, close 3.11.2026 | 1.653 | 165.3 | 0.524 |
| Worst case (ten years out) | 0.000 | 0.0 | 0.000 |
| Conservative | 0.356 | 35.6 | 0.113 |
| **Base** | **0.789** | **78.9** | **0.250** |
| Optimistic | 1.921 | 192.1 | 0.609 |
| Probability-weighted (10/25/45/20) | 0.828 | 82.8 | 0.262 |
| Buy price (shadow Tier C, 40% of base) | 0.316 | 31.6 | 0.100 |

- **Lane C, tier C.** The total margin is 60%: 50 points for the tier plus 10 points of data additions, which is the cap.
- **The price is 2.10 times base value and 5.24 times the buy price.**
- **What the price implies:** normalised owner earnings growing +11.4% a year for ten years, or TTM owner earnings
  falling only −2.5% a year.
- **Preliminary verdict: NO_THESIS.** This is not WATCHLIST, because price is not the only failure.
  - E1 fails: the worst case has a plausible path to all three impairment markers.
  - E3, B3, D5, H4 and H5 also fail.
  - Q1 (circle of competence) cannot be assessed here.

## 0. What I checked myself, and what changed from the team's inputs

**The consolidated H1 2026 statements exist.** The supplied `gilat_h1_2026` lacks them. `market.md` found the full
Q2 2026 report on the company's site and saved it as `web/pdf/company_site_q2_2026_full.pdf`. I cite it as
`gilat_q2_2026_full`.

I opened these pages as images and read every figure used from them:
- p.30-31: balance sheet;
- p.32: P&L;
- p.38-39: cash flow;
- p.46-48: segment note.

I read p.41-43 (inflation, functional currency, exchange rates) and p.49 (revenue split, events) on the text layer.
Pages 1-26 are the directors' report, page for page the same as `gilat_h1_2026` p.1-26.

**TTM reconciliation.** The TTM is FY2025 (translated by the company into ILS) − H1 2025 + H1 2026. Built from these
statements, it reproduces Mega exactly: operating income 39,534, net income 32,985, OCF 80,967.

**Estimates in `derived.txt` §3 that this replaces with filed figures (TTM, ILS k):**

| Item | Filed figure | `derived.txt` estimate |
|---|---|---|
| IRU amortisation | 6,955 | 3,766 |
| SBC | 1,270 | 327 |
| Bond interest paid, consolidated | 3,144 | 3,582, parent |
| Lease interest | 7,950 | 4,776 |
| Lease principal | 28,590 | 31,761 |

**Share count and price.**
- I replace the derived share counts (117.4M and 119.0M) with the TASE "registered capital for trading" on 3.11.2026:
  120,417,631 shares.
- The price is the 3.11.2026 close of 165.3 agorot. I checked both figures in the saved Bizportal snapshot
  `web/bizportal_generalview.html`, which also shows market cap ILS 199,050k and equity 132,371k.
- Mega's 14:03 snapshot implies 164.6 agorot (−0.4%). The charter wants the latest close (D7), so I use 165.3.

**Accounting identities (C7) pass at 30.6.2026.**
- Assets − liabilities − equity = 0.
- The H1 2026 cash flow foots to the change in cash: difference 0.
- NI / basic EPS = 108,088k, equal to the weighted basic share count.

**Annual-report figures.** Every figure I use was page-image-checked by the reconciliation (`recon/viewed_log.md`):
- gilat_fy2023 p.116-118, 122-123;
- gilat_fy2024 p.118-120;
- gilat_fy2025 p.92, 125-127, 131-132, 150, 163.

## 1. Currency and units

**Why ILS.** From 1.1.2026 the functional and presentation currency is the shekel (gilat_q2_2026_full p.42). A USD
TTM does not exist. I therefore value in ILS thousands.

**One rate for the USD history.** The audited USD window FY2021-FY2025 is converted at one dated rate: the Bank of
Israel representative rate of 3.157 on 3.11.2026. Per-share values are also shown in USD at that rate.

**Why this matches the task.** With a single rate, this is the same as "value in USD, then convert per share at
3.157".

**What it costs.** Converting at spot rather than at each year's average rate (about 3.2-3.7) makes the
2023-2025 positive years a little smaller in shekels. BoI annual average rates for 2021-2024 are not in the documents.
The ratio inputs (margins, the cyclical test) are unaffected.

**One-offs in H2 2025.** The H2 2025 one-off is removed at the company's own implied H2 2025 rate of 3.3023
(derived from its ILS and USD revenue), because that is the rate at which it sits inside the TTM.

## 2. Hurdle

- r = max(10%, y10 + 3 points), in the cash flows' currency.
- The Israel 10-year was 4.16% on 3.11.2026 (market.md §5), so r = 10%.
- The US 10-year (4.91%) + 3 points = 7.91%, also below 10%.
- No beta, no equity risk premium.

## 3. Lane and tier (framework d11; checklist A3, C2; screen_spec 2.3)

### Return on tangible capital

Pre-tax return on tangible capital, on the screen_spec definition:
`EBIT_adj / (NWC_op + net PP&E + ROU)`, where NWC_op = max(0, (CA − C) − (CL − short-term debt)).
- ROU assets count as capital because Gilat reports under IFRS.
- Short-term debt includes current leases and the conversion-option and warrant liabilities.

| | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | TTM |
|---|---|---|---|---|---|---|
| ROTC | −14.0% | −12.0% | 17.9% | 17.0% | 38.9% | 51.0% |

- The median is 17.5% and the minimum −14.0%.
- The FY2021 balance sheet is not in the documents. I used the 1.1.2022 opening PP&E and ROU with NWC_op = 0. EBIT
  was negative, so the sign is certain.

### Leverage

- **On the balance sheet:** net cash. Net debt with leases, with Series D at par, is −27,401 (−2.5x EBIT_norm).
- **With the Bezeq IRU instalments:** net debt is 7.1x EBIT_norm counting the unpaid consideration for the lines in
  service, and 17.7x counting everything committed. Both figures are UNVERIFIED (§7 below).
- **Interest cover TTM:** 3.0x.

### Moat by type

**Business by business** (`business.md` §11):
- **Licence:** Ministry of Communications licences and security clearances. A narrow advantage against foreigners in
  Israeli defence only.
- **No switching costs:** contracts run on 12-month orders and non-binding frameworks.
- **No scale or cost advantage:** a reseller of others' capacity; the IRU buys cost parity with Partner, not an
  advantage.
- **No share of mind:** the ISP prices 15-42% below the big four.

**The company's own words:** competition is "mainly on price" and its share is "not material" (gilat_fy2025 p.32).

**Does the moat show in the numbers?** No. There were operating losses in FY2021-FY2022, so A3 fails for A, B and D.

### Management record

From `governance_risk.md`:
- **No controlling holder.** Related-party dealings are pay only. The CEO bought about 10% of the company with his
  own cash in 2023.
- **Serial dilution.** Listed shares are ×2.06 since 31.12.2022 (21% a year), with Series D adding 22% more.
- **Pay-setting.** The bonus cap was raised in December 2025, and the CEO's options were in the money at grant.
- **Buybacks.** Made at ILS 2.60 (June 2026) and about 2.03 (October 2026), both above every value computed here.

### Tier and lane

**Tier A** fails: it needs a median of at least 20% and never below 10%.

**Tier B**'s 12-20% band holds on the median only. It fails on the moat (A3 VETO). Lane D needs an A/B franchise.
Lane E has no deal.

**Lane C is the only lane whose valuation basis fits.** This is a contract- and war-driven, cyclical business with
no moat, valued on normalised earnings and assets. This matches the task's own rule: cyclical, project or contract →
the cheap track, grade C. Today it is not a C bargain:
- market cap is 5.3x NCAV;
- TTM EBIT_adj is 3.0x EBIT_norm (`ttm_above_norm`): a peak, not depressed earnings;
- there is no disclosed transaction to evidence a private-owner value.

**Why "C" and not "none".** I declare lane C rather than "none" because C is the lane whose rules would govern any
future purchase:
- the C buy line;
- the C sell rule;
- items H1-H6.

A sibling study (paymeant) chose "none" in a different situation: a levered lender with no fitting lane at all.

## 4. Window, one-offs, cyclical test, EBIT_norm (d2)

### The window

- **Base window:** FY2021-FY2025 plus TTM to 30.6.2026, six observations, as the task specifies.
- **Overlap:** the TTM overlaps FY2025 by six months (H2 2025 counts twice). I state this; I do not hide it.
- **Shorter than a cycle:** the Israeli window is at most six years and shorter than one defence or war cycle
  (`cycle_window_short`).

### One-offs removed (gains only, sign-aware)

**1. The 2025 satellite-supplier credit.** The credit is named (gilat_fy2025 p.96, p.160) but its amount is not
disclosed.
- The estimate is Q4 2025 gross profit above the Q1-Q3 2025 gross margin (28.53%) = USD 1,423k (gilat_fy2025 p.92).
- That is ILS 4,700k at 3.3023 inside the TTM.
- UNVERIFIED. The Q4 spike may also contain "high-profitability deals". Taking all of it as one-off is conservative.

**2. The H1 2026 one-off war equipment revenue.** It is named (gilat_h1_2026 p.12) but the amount is not disclosed.
- The estimate is the rise in satellite-segment equipment revenue: +4,179 (gilat_q2_2026_full p.49).
- At the 2025 equipment gross margin of 31.3% (gilat_fy2025 p.173 via business_calcs §3), that is 1,308 of profit.
- UNVERIFIED. The revenue is also removed from TTM revenue for the margin.

### Not added back: no endogenous add-back is used

- **FY2021 doubtful debts of USD 3,191k** (gilat_fy2023 p.158): a credit loss in the business, which would be an
  endogenous add-back. Left in.
- **The FY2023 revenue de-recognition (USD 401k)** and **the USD 100k legal settlement**: small, and the year it was
  booked is unclear. Left in.

### Non-operating items

Non-operating items are not in EBIT:
- the FX gain on cash (7,185 TTM);
- the option and warrant revaluation (1,029 TTM);
- the DTA tax benefit.

They are removed from the d1 owner earnings and from Graham's NI_norm.

### Cyclical test

The test is true: operating losses in FY2021-FY2022. The charter formula therefore applies:

**EBIT_norm = min(mean, median, mean revenue × m_norm) = min(11,461; 11,250; 11,100) = 11,100.** That is 33% of TTM
EBIT_adj (33,526). Here m_norm is 5.53%.

The fiscal-years-only variant, which drops the TTM peak, gives 6,876 (m_norm 3.95%). It is shown as a variant.

### Margin expansion

d2 asks whether a higher margin is permanent, answered from the filings. The filings attribute the rise to:
- the wars (gilat_fy2023 p.88; gilat_fy2025 p.97; gilat_h1_2026 p.12; gilat_q2_2026_full p.41: "a positive effect and
  increased demand in the government-defence segment due to the war situations");
- one-off equipment;
- a supplier credit;
- the weaker dollar.

None of these is shown to be permanent. The median-based figure stands.

## 5. Maintenance capex, owner earnings, cash proxy, tax

### Maintenance capex (d1)

maintenance_capex() is floored at Dep:
- **Dep** = PP&E + ROU depreciation + licence amortisation + IRU amortisation = 46,361 TTM.
- **CapEx** (10,159) + IRU payments (13,714), less growth capex (5-year NetPPE/revenue of 7.62% × revenue growth),
  is far below the floor.
- **The floor binds.** That is what keeps leases a cost: ROU depreciation stays charged, which is the fund rule that
  lease principal must not escape owner earnings.
- The customer-relations amortisation (USD 809k a year, gilat_fy2025 p.150) is Amort_acq: added back and taxed in
  full, per d3.

### Owner earnings, d1, TTM on a reported basis

29,383. SBC (1,270) stays expensed. NI includes a tax benefit.

### Cash proxy (C4)

- **Formula:** OCF − lease and other interest − SBC − maintenance capex on owned assets − lease principal. Gilat books
  lease and bond interest in financing, so both are deducted.
- **IRU payments** stay inside OCF and are fully charged (conservative).
- **The maintenance-capex depreciation base for TTM** (PP&E + licences) is an UNVERIFIED split of TTM D&A. It does
  not bind.

| | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| Cash proxy, USD k | −5,763 | −2,435 | 876 | −390 | 5,971 |

- **TTM:** 31,055 ILS k, 94% of NI.
- **C4 (FLAG):** the window sum over positive NI is −20%; FY2023-FY2025 is 73%. Both are below 80%: fails.

### Tax

- **Rate used:** the statutory 23% (gilat_fy2025 p.164).
- **Effective TTM:** −5.3%. This is a DTA recognition, and H1 2026 shows 1.2% because of losses carried forward.
- **Losses carried forward:** unrecognised tax losses of USD 19.0M at 31.12.2025 (gilat_fy2025 p.163). Their shield
  is not valued: which entity holds them is not disclosed, and leaving it out is conservative. It is upside.

## 6. Cash and claims (d3 equity bridge)

**Cash, pro forma 3.11.2026: 86,855.** This starts from 92,955 at 30.6.2026 and deducts:
- the October 2026 buyback: 4,620 (2,274,810 shares at about 203.1 agorot; Globes feed and TASE counts, market.md
  calc §3; UNVERIFIED against Maya);
- the Series C final redemption on 1.9.2026: 741 (public par less the about 192K shares converted after 19.8, plus
  the last coupon; derived);
- the Series D coupon of 1.10.2026: 738 (derived).

Two further points:
- Q3 operating cash flow is unknown and **not** added, which is conservative.
- Restricted cash of 3,500 is pledged for guarantees (gilat_fy2025 p.158) and excluded.

**Excess cash (d3) = cash − two months of cash operating costs = 49,491.** Cash operating costs are 224,183: operating
costs less D&A and IRU amortisation, plus lease payments. They include lease payments because those are cash costs
outside "operating costs" under IFRS 16.

**Leases: 33,116** (gilat_q2_2026_full p.31), deducted in every bridge. EBIT is after ROU depreciation and before
lease interest, so deducting the liability charges the financing part. This is the charter's d3 bridge.

**Series D.** 26,337,927 par outstanding on 3.11.2026, derived: the next coupon of ILS 724,293 is 2.75% of par
(Bizportal; market.md §1.4). It converts 1:1 until 1.4.2028 (gilat_h1_2026 p.24).
- Holders convert only when that is worth more than par. Shareholders then get min(value as converted, value with
  Series D at par).
- Proof sketch: E/(S + D) < (E − D)/S exactly when E/(S + D) > 1, that is, when conversion is worth more than par.
- Where equity is below the Series D claim, equity is nil.
- In the base (0.789 < 1.00), Series D stays debt at par. In the optimistic case it converts.

**Options: net exercise** at the computed per-share value (fixed point):
- the four December/November 2025 packages (gilat_fy2025 p.166);
- 3,428,500 older options at a weighted strike of USD 0.23 × 3.19 = ILS 0.734 (gilat_fy2025 p.172). This count is an
  upper bound, since some were exercised in H1 2026.

**Nothing else to deduct:** no bank debt, no NCI, no preferred.

## 7. The Bezeq IRU: the decisive balance-sheet item

### Terms

From gilat_fy2025 p.40-42, p.152-153 and p.183:
- **IRU-1:** 18,000 lines at ILS 4,890 a line for 15 years (ILS 88.02M).
- **IRU-2 pulse 1:** 36,000 lines in quarterly tranches, December 2025-2028, about ILS 160M "assuming full exercise".
- **O&M:** 4% of consideration a year.
- **Payment:** each pulse can be paid in 10 annual instalments with interest (5% for pulse 1).
- **Release clause:** Gilat is released only from a *later* pulse if its growth target is missed.

**Accounting.** Only amounts paid are on the balance sheet, as deferred expenses. The 25-year amortisation stated
(p.153) cannot be reconciled with the charge actually booked (business.md §14 item 10).

### Derived amounts (UNVERIFIED; the filings do not state the unpaid balance)

| | ILS k |
|---|---|
| Committed | 248,020 |
| Paid to 30.6.2026 (ILS 13,752 in FY2025 + 10,673 in H1 2026, gilat_q2_2026_full p.38) | 24,425 |
| Unpaid | 223,595 |
| — of which for the ~27,600 lines in service at 19.8.2026 (gilat_h1_2026 p.5) | 106,262 |

Committed lines not yet filled: 26,400.

### Economics against the alternative

Small ISPs can rent unlimited fibre BSA at ILS 58 a month, fixed for 2026-2031 (gilat_fy2025 p.40). PV at r over 15
years, on the contract terms:

| | PV per line |
|---|---|
| IRU-1 | 5,658 |
| IRU-2 | 5,142 |
| BSA | 5,552 |

Assumptions: 10 payments from delivery at 5% vendor interest (assumed 5% for IRU-2, where Bezeq's bond yield is not
disclosed), plus 4% O&M. **If every line is filled, the IRU beats BSA by +12,850 pre-tax.**

### Treatment by scenario

**Base:** the committed lines are filled and **NPV-neutral**. There is no deduction, and no credit for the +12,850.
This assumes the ISP keeps adding lines at roughly its H1 2026 pace (7,116 private net additions,
gilat_h1_2026 p.8) and that ARPU above the line cost covers the other ISP costs.

**Conservative:** half of the 26,400 unfilled lines are never used but are paid for. Dead cost 52,268 after tax, at
the PV of an unused IRU-2 line.

**Worst:** all 26,400 are unused. Dead cost 135,760, pre-tax because a loss-making business gets no tax shield.

**Leverage view (C2, H5):** the unpaid instalments are fixed obligations, so they count as debt-like whatever their
NPV.

**Variant:** base earnings with the ISP stalled at today's lines gives **0.000**. If the ISP stops growing, the
committed lines alone are enough to wipe out the equity on base earnings.

## 8. Methods and the method spread

| Method | ILS per share | Note |
|---|---|---|
| **d3 EPV** | **0.789** | OE_unlevered = (EBIT_norm + Amort_acq) × (1 − 23%) + Dep − maintenance (= 0) = 10,514; / r = 105,139; + excess cash − leases = 121,514 before Series D |
| **d4 DCF** | 0.789 | Base g1 = 0. See below |
| d4 DCF at revenue/share −2.3% | 0.664 | Diagnostic only: dilution outran growth |
| d5 10x EBIT_norm + excess cash − leases | 0.836 | |
| **d7 tangible book**, 30.6.2026 | **0.940** | Holds ROU 43,241 and IRU prepayments 16,229 that are tied to obligations |
| d6 NCAV | 0.321 | Market cap is 5.3x NCAV; net-net test fails |
| d6 Dempster | 0.094 | PP&E, ROU and IRU at nil |
| d7 private-owner value | none | No control transaction is disclosed. The placements at 0.30 and 0.88, conversions at 1.00/1.35 and buybacks at 2.60/2.03 are minority trades |

**Why the base DCF uses g1 = 0.** The per-share EPS record has no rate: the 3-year averages run −0.0507 → +0.0350 USD,
from a negative base, over an Israeli window that is not ten years. ROIIC is set to r because there is no moat.
Growth therefore adds no value, and the DCF equals EPV by the library's construction. The cap is 10%.

**d5 multiples.** EV is 188,848 (as-converted market cap + leases − cash):
- EV/EBIT_norm is 17.0x, against the about 10x that d5 treats as fair for Tier A;
- EV/TTM EBIT_adj is 5.6x.

The stock looks cheap on peak earnings and expensive on normalised earnings.

**d9 Graham's yardstick.** This is the looser [I] version, using the ILS government yield. NI_norm_ttm is 14,746.

| | Gilat | Test |
|---|---|---|
| Earnings yield | 7.4% | at least 8.32% |
| P/E | 13.5 | at most 10 |

Result: fails.

**d8 implied growth at the price.** The operations value is 235,174: fully diluted shares × price, plus leases, less
excess cash.
- That is 22.4x normalised OE, which needs **+11.4% a year for ten years**. No reinvestment is charged, which is the
  generous reading.
- Or it is 8.5x TTM OE, which needs only **−2.5% a year**.

**Method spread: 19%,** below 30%. EPV, DCF and 10x pre-tax are one earnings view; tangible book is the independent
asset view. EPV/TBV = 0.84 because normalised NOPAT on tangible equity is 9.5%, below r.

## 9. Scenarios and probabilities

The probabilities are model judgements, uncalibrated: the ledger is not available.

| Scenario | ILS | Probability | Reason |
|---|---|---|---|
| Worst | 0.000 | 10% | Ten years out: pre-war defence demand, Vodacom lost in 3.2027, ISP stalls. Today's liquidation value is already below the claims (see below). Without the IRU the liquidation floor would be 0.043. The worst case is held with confidence as a floor |
| Conservative | 0.356 | 25% | Base earnings; the largest company-specific risk (the IRU) at half strength. Variants below |
| Base | 0.789 | 45% | Charter EBIT_norm, IRU NPV-neutral, no growth (ROIIC = r) |
| Optimistic | 1.921 | 20% | TTM EBIT_adj persists: war-era demand, the 2026 shekel, Vodacom renewed, ISP filling its lines |

- **Worst-case liquidation:** Dempster value before Series D is 31,508. Less the 26,400 unused lines (135,760), the
  claims exceed the value, and FY2021-2022-style losses only widen the gap.
- **Conservative variants:** fiscal-year EBIT_norm with the lines filled gives 0.520; both pessimisms together give
  0.086.
- **Probability-weighted value:** 0.828.

## 10. Impairment markers, stresses, sensitivity

### E1 (VETO, all lanes) fails

A plausible worst-case path exists to all three markers.

**1. A maturity or covenant breach that leads to dilution.**
- Below ILS 1.00, Series D stays debt, with 25% a year due 1.4.2028-2031.
- The Bezeq instalments run about ten years.
- The company's own record shows this path: the 2023 rights issue and CEO placement at 0.30, and the 2024
  bond-for-share exchange, came under Series C maturity pressure.

**2. A going-concern doubt.** Cash of 86,855 stands against 223,595 of unpaid IRU commitments, plus operating losses
like FY2021-2022.

**3. Assets worth less than debt.** Dempster value of 11,095 against the IRU commitments.

### F4 stresses on base

| Stress | Base value per share | Note |
|---|---|---|
| USD/ILS +10% | 0.306 | Pre-tax −7,577 a year, using USD 24M of hedged costs as the proxy for net USD costs (gilat_h1_2026 p.19), UNVERIFIED |
| USD/ILS −10% | 1.202 | |
| +2 points on rates | no hit | No floating debt; r stays 10% |
| High CPI | small hit | No CPI-linked debt (gilat_q2_2026_full p.41); Bezeq principal half-linked until each pulse starts; wages in ILS |

The dollar is already +6.0% above the 30.6.2026 balance-sheet rate of 2.978.

### Sensitivity grid around base (D3)

r ± 1 point, g ± 2 points around 0%, ROIIC held at 10%:

| r \ g | −2% | 0% | +2% |
|---|---|---|---|
| 9% | 0.761 | 0.883 | 0.913 |
| 10% | 0.681 | 0.789 | 0.789 |
| 11% | 0.614 | 0.711 | 0.700 |

The minimum is 0.614 and the maximum 0.913. **Base is below the price of 1.653 everywhere.**

## 11. Margin and buy price

`required_margin("C", [...])` gives:
- Tier C: 50 points.
- Data additions:
  - `cycle_window_short`: an Israeli window shorter than a cycle; no FY2021 balance sheet.
  - `derived_tier2_field`: the TTM is built from three columns; the one-off removals, the pro forma cash, Series D
    par and the IRU unpaid balance are all derived.
  - `microcap_field_unavailable`: undisclosed amounts (the supplier credit, the war equipment, the IRU schedule and
    Customer A's identity) at a market cap of about USD 63M.
  - +5 points each; `required_margin()` caps the total at +10.
- No endogenous add-back.
- **Total margin: 60%. Buy at 40% of base = 0.316 ILS (31.6 agorot; USD 0.100).**

**Why the buy price is a shadow.** The charter's evidenced Tier C routes are:
- the net-net route (at most 2/3 of NCAV and at most Dempster), which gives 0.092 ILS;
- 50% of a private-owner value evidenced by disclosed transactions, which do not exist here.

So 0.316 is labelled a **shadow** C line on the normalised-earnings base. It is reference only.

**The team's suggested extra +5 points** (business.md, governance_risk.md, from the older fund rules) **are not
applied.** The charter allows only the capped data additions and the endogenous +10. It handles governance and
uncertainty through VETO items and the worst case, not through extra margin.

**Reference only.** The analyst's segment normalisation (business.md §12: 15,099 after lease interest) would give
1.237 ILS. The price is 1.34 times even that.

## 12. Liquidity and sizing (e2)

**Liquidity (TASE series to 29.10.2026, market.md calc §9).**
- The 60-session median is ILS 1,303,000: above the ILS 50,000 floor and above ILS 100,000, so no price-reliability
  block is needed.
- The 25th percentile is ILS 960,250. The liquidity maximum (20 days × 20% × p25) is ILS 3,841,000 at cost.

**Sizing.**
- Full Kelly is 0%: every outcome except the optimistic one sits below the price.
- L_worst is 100%, so the permanent-loss budget is 5%.
- The tier cap is 5%.
- **Size: 0%.**

**Not available here:** fund NAV, holdings and the calibration ledger. The liquidity cap is therefore given as an
amount, and the probabilities are uncalibrated.

**Ownership cap.** The licence requires Ministry approval to hold 5% or more of the company (gilat_fy2025 p.73-74).

## 13. Checklist items that bind Lane C (yes = pass)

**VETO items that fail:**
- **B3** dilution: ×2.06 listed shares since 2022, 21% a year, issued at 0.30-1.35.
- **D2** price at most the buy price: 5.24x.
- **D5** expected return clears r: price/base 2.10.
- **E1** impairment path.
- **E3** mispricing: the price already pays for the war-era earnings; no pessimism to refute.
- **H4** catalyst or basket: none.
- **H5** cyclical: no low-cost position; net debt once the IRU is counted.

**VETO items that are open (they fail closed):**
- **A0/Q1** circle: `theses/CIRCLE.md` is not available here.
- **B5** accounts and candour: the headline adjusted EBITDA and "FCF before prepaid expenses" exclude the recurring
  IRU cost, and the unpaid IRU balance is not disclosed.
- **D8** filings since 30.6.2026: the Q2 report was read in full and immediate reports via the company site and news
  feeds; Maya is not reachable and Q3 is not yet published (expected late November 2026).

**VETO items that pass:**
- **B7** misconduct: none found; Maya not checked.
- **C1** survives flat revenue and a 30% EBIT fall: covenants at −24% net financial debt/assets and 48% equity/assets,
  against limits of 60% and 12%.
- **C3** no maturity in 24 months that needs refinancing: Series C repaid; Series D's first 25% is due 1.4.2028 and is
  covered by cash.
- **C5** no endogenous add-back.
- **C7** identities.
- **D1** two methods with a range, in code.
- **D7** dated close.
- **F1** control chain: no controller, no pledges.
- **F2** related parties: pay only.
- **F3** consolidated statements; currency read.
- **H1** plain explanation.
- **H2** asset value from one balance-sheet date, identity-checked.
- **H3** the floor is not burned: OCF positive in every year.

**FLAG items:**
- **C4** fails (73%).
- **E5 and E9:** see business.md and the scuttlebutt files.

**Not applicable to Lane C:** A1-A8, B1, B4, B6, C2, D3, D4, E6, E8 and H6. Notes on two of them:
- **D3** would fail anyway.
- **D4:** implied growth is above any per-share record.

## 14. The investment test

| Question | Answer |
|---|---|
| Q1 inside the circle? | Cannot be assessed here: open |
| Q2 a good business by its lane? | No. Not a C bargain today: no net-net, peak earnings, no catalyst |
| Q3 price well below value? | No. Price/base 2.10; even the analyst segment base is 1.34x below the price |
| Q4 what the price assumes | +11.4% a year from normalised earnings, or −2.5% a year from TTM. It assumes the war-era earnings largely persist. The filings give no ground to call that too pessimistic |

**Who is selling, and to whom.** Mutual funds trimmed after a +93.8% one-year rise (market.md calc §8): Meitav sold
1.89M shares at 1.96 on 5.10.2026, and Ayalon reduced its holding. The buyer was the company itself, at prices above every value here.

## 15. Preliminary verdict and re-examination triggers

**NO_THESIS.** This is not WATCHLIST: E1 fails at any price until the IRU exposure is disclosed, and E3, B3, H4 and
H5 fail too.

Re-examine if:
1. **Vodacom DRC** (16.3% of 2025 revenue) is renewed by 31.3.2027 at USD 1M a month or more, or is lost.
2. **The Bezeq IRU:** the FY2026 annual report (due by 31.3.2027) states the unpaid IRU balance and whether pulse-1
   tranches can be declined; and lines in service reach 54,000 by 31.12.2028.
3. **The war premium:** satellite-segment revenue in H1 2027 is below 75% of H1 2026 (ILS 119,422k), which confirms
   the normalisation; or it holds at or above that level for a second year after the April 2026 ceasefire, which calls
   for re-underwriting EBIT_norm.

Then re-run `valuation.py` against the dated buy price.

## 16. UNVERIFIED items and what is not available here

**UNVERIFIED:**
- the one-off amounts (supplier credit; war equipment);
- the IRU unpaid balance, the delivery schedule and whether pulse-1 tranches can be declined;
- the vendor rate for IRU-2;
- the October buyback amount, the Series C final cash, the Series D coupon and Series D par (derived from market data);
- the older-option count after H1 2026 exercises;
- the TTM split of D&A between owned assets and ROU (used only in the cash proxy);
- the net USD cost exposure (the hedged-cost proxy);
- the FY2025 lease-interest split in the ILS restatement. It is 9,584 against USD 1,788 × the average rate, while the
  lease total is consistent. It inflates the TTM lease interest used for interest cover and the cash proxy, which is
  conservative.

**Not available in this environment:**
- `theses/CIRCLE.md`: Q1/A0 is open.
- `lib/valuation.py`: `lib/charter_valuation.py` was used instead.
- `lib/liquidity.py`: the charter formula was computed from the TASE series.
- the calibration ledger: the probabilities are uncalibrated.
- the fund's holdings and NAV: sizing is given as fractions and amounts, and D6/G6 cannot be assessed.
- `tax_params`: after-tax swap and G8 cannot be assessed.
