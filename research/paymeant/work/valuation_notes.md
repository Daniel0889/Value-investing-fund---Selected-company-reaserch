# Paymeant (TASE 1180876): charter valuation, assumptions and reasoning

> **CIO gate, 3.11.2026: this note is superseded in part.**
> - **What changed.** The red team's objections were accepted except B11 (rejected); B2, O1, O4 and O8 were accepted
>   in part. The revised figures are in `research/paymeant/output.txt`.
> - **The revised figures.** Base value is 2.19 a diluted share, not 5.36. The shadow buy price is withdrawn. D3 fails.
>   The verdict is NO_THESIS.
> - **Where the decisions are.** `work/paymeant/gate.md` holds the decision on each objection; `work/paymeant/checklist.md`
>   holds the 60-item checklist.
> - **What below is out of date.** Sections 1-7 are the valuation team's first version, kept for the record. Their
>   normalisation (note 19e added back, TTM as a sixth year), base value, D3 "pass", implied growth of −4.7% and shadow
>   buy price no longer stand.

Written 3.11.2026 for the Rev 4 study. The code is
`/home/user/value-investing-fund---selected-company-reaserch/research/paymeant/valuation.py`. Its printout is
`/home/user/value-investing-fund---selected-company-reaserch/research/paymeant/output.txt`, cited below as "out §n".
Every number in this note is either printed by that code or is a filed figure with its page. Units are ILS
thousands unless stated; per-share values are in ILS (1 ILS = 100 agorot).

**Preliminary verdict: NO_THESIS.** No lane fits. Several VETO items fail on the funding structure and the moat,
not only on price. The stock is also below the charter's liquidity floor. For reference only, the price is 1.08x a
shadow Tier B buy price.

---

## 1. The key judgement: value a lender on its equity, and show the EV basis beside it

Paymeant is not a software company. It is a licensed consumer lender. It originates point-of-sale loans, holds
about 210M of them on on-call bank lines, and sells them to banks and to its own unconsolidated SPCs (business.md
§1). Its own P&L puts "financing expenses attributed to ongoing activity" above operating profit (paymeant_fy2023
p.82). That is why Mega's 88% "gross" and 41% "operating" margins are measured after interest.

- **The charter's own rule.** screen_spec 3.1 says that for financials "EBIT, EV and ROIC [are] meaningless", and
  routes lenders to the bank route (4.7). That route judges a lender on equity: ROE, P/TBV, normalised P/E. So the
  primary basis here is the **lender (equity) basis**:
  - EBIT is operating profit as reported, after funding cost.
  - Owner earnings are equity owner earnings.
  - The warehouse credit is the funding of the loan book. Its cost is already charged, so it is not deducted again
    in the equity bridge.
- **The cross-check.** framework d3 and d5 as written (the EV basis) are also computed: EBIT before funding, with
  the bank credit deducted at face.
- **How the two differ.** The EV basis gives 2.95 a share against 4.36 on the lender basis (out §3). The gap is
  exactly the warehouse leverage: debt at face (115,225) against its capitalised after-tax normalised cost (59,754).
  That difference is 55,471, or 1.41 a share, and the code reconciles it to the shekel.
- **Why this matters for the verdict.** At today's price the market pays about the no-leverage value: price / EPV
  on the EV basis is 1.07 (out §3). The whole discount to the lender-basis value is the value of leverage that is
  on-call and concentrated in one bank. The fund's rule 4 treats that kind of leverage as close to disqualifying,
  and framework f2 lists "dependent on refinancing markets (Delta Financial's warehouse lines)" on its avoid list.
  So the "cheapness" is the one thing the fund declines to pay for.

## 2. Step 1: lane and tier (out §1, §6)

| Test | Evidence | Result |
|---|---|---|
| Median pre-tax return on tangible capital, unlevered | FY2022-TTM year-end 8.4%, 13.7%, 16.8%, 16.1%, 15.7%. Median 15.7%, minimum 8.4%. On average capital: median 16.9%, minimum 15.3% | B's 12-20% band; fails A (median < 20%, a year < 10%) |
| Same, bank lens (pre-tax return on tangible equity) | Median 28.6%, minimum 16.0% | High, but levered: equity is 37.5% of assets |
| Net debt with leases / normalised EBIT | 112,942: 3.7x EBIT_norm before funding, 5.0x after | Fails A (1x) and B (2x): C2 VETO |
| Interest cover | 5.1x TTM | Fails C2's 8x |
| Funding concentration | Bank B 88.5% of drawn credit at 31.12.2025 (paymeant_fy2025 p.49); all lines on-call; take-outs to own SPCs funded by "a banking corporation" | E8 and C3 VETO fail |
| Moat, named by type | Claimed: underwriting data, merchant network, bank trust, licence. Merchants can cancel at will (paymeant_fy2025 p.41); nothing patented; the regulator is adding competitors (business.md §5, §11). No peer returns are available to show returns above peers | A3, A4 fail (the $1bn test fails easily) |
| Management record | Delivered 2025 growth and a ~50% payout; no buybacks at ~3 ILS while options went to the controllers; candour mixed (governance_risk.md §5, §7) | Not owner-oriented enough to offset the above |

- **Lane A or B.** Fails on the moat items (A3, A4) and on leverage and cover (C2), all VETO.
- **Lane C.** Not a net-net: market cap 124,794 against 2/3 of NCAV 46,869 and Dempster 43,215. No disclosed
  transaction gives a private-owner value; minority placements and block trades are not owner value (framework
  d7).
- **Lane D.** There is no A/B franchise underneath.
- **Lane E.** There is no announced deal.
- **Result: lane "none".** The tier used for the margin is a **shadow Tier B**, for reference only. B is the
  nearest tier on unlevered returns and the only one with a defined buy rule for this kind of business.
- **ROTC definition.** Capital is loan book + receivables + PP&E + ROU − operating payables. Cash, bank credit,
  leases, deferred tax and intangibles are excluded. This follows the charter's ROTC (NetPPE includes ROU under
  IFRS) and its tangible-capital rule (intangibles out). derived.txt included capitalised development and left out
  ROU, so its figures differ slightly. The tier conclusion is the same either way.
- **FY2021.** It has no balance sheet in the documents, so it is left out of the returns series.

## 3. Step 2: window, normalisation, owner earnings (out §2)

### The window
- FY2021-FY2025 plus TTM to 30.6.2026, as the brief directs: six points.
- TTM = FY2025 + H1 2026 − H1 2025, the charter's construction for semi-annual reporters.
- The Israeli window is at most six years (charter amendment 2), and this one contains no credit cycle, so the
  data flag `cycle_window_short` applies.
- FY2020 is not in the documents. The history gate (X4) and C6 cannot be assessed here.

### One-offs and EBIT_adj
- EBIT_adj is operating profit before other items. This removes note 19e (paymeant_fy2023 p.111):
  - IPO grants of 288 (2021), 751 (2022) and 228 (2023);
  - options that vested immediately at the IPO, 1,997 (2021);
  - one-off income of 1,188 (2022) when the engagement with acquiring corporation A ended.
- These are tied to one event, the IPO, and stopped after 2023. The line is nil in FY2024, FY2025 and H1 2026.
- They are not impairments or restructuring, so this is **not an endogenous add-back** (C5 passes; no +10).
- Removing them *lowers* the median margin: 37.52%, against 38.28% with them left in. But it decides the cyclical
  classification. Left in, the FY2021 loss of 769 makes the business "cyclical", and EBIT_norm falls to 14,447.
  That reading is used, in substance, in the conservative case.
- All recurring share-based pay stays expensed.
- The 2022 fair-value gains on unsold loans are not removed. They are how this lender recognises revenue, not a
  one-off, and the median is unchanged with or without them.

### Cyclical test and EBIT_norm
- The stdev of the margins is 8.37 points, against half the median of 18.76 points, and no EBIT_adj is ≤ 0. So the
  business is **not cyclical** by the charter's test.
- EBIT_norm = TTM revenue 60,301 × m_norm 37.52% = **22,624**, which is 7.5% below the TTM figure. The median is used
  because TTM looks high-normal: arrears have risen and the credit charge is low (business.md §12; framework d2,
  "use the median, not the best year").
- A credit business with no credit cycle in its window could be cyclical in substance. The **conservative case**
  therefore forces the cyclical formula: 14,395.

### Tax
- 23% statutory (paymeant_fy2025 p.106). Effective rates were 22.4% (FY2023), 22.8% (FY2024), 23.5% (FY2025) and
  24.5% (TTM).

### Maintenance capex
- TTM capex is 2,897: PP&E, capitalised development including capitalised share-based pay, and ROU investment.
- The growth carve-out is 530.
- The **floor at total D&A, 3,278, binds**.
- Total D&A includes ROU depreciation and the amortisation of capitalised development. Using it as the floor keeps
  both the lease cost and the platform's upkeep inside owner earnings, as the fund's IFRS 16 rule requires. It is
  also the conservative reading: a floor at PP&E and ROU depreciation alone would leave owner earnings above net
  income (the H1 split of D&A by asset is not disclosed, so that variant is not computed).

### Owner earnings
- d1 TTM = 18,466, equal to net income.
- Normalised: EBIT_norm × (1 − 23%) = **17,421**. No finance line sits below operating profit, so this is also net
  income.

### dWC_maint = 0 in the EPV (assumed)
- The EPV holds *nominal* volume flat, so no extra loan book is needed.
- Inflation-driven and real growth of the book is charged in the DCF reinvestment term, so growth is never charged
  twice (framework d1, last bullet).
- Charging inflation working capital in the EPV as well would charge for volume the EPV does not credit.

### Cash proxy
- On reported OCF the proxy is 8,025 (43% of net income). That figure is not meaningful for a lender, because the
  loan book and its bank funding run through OCF.
- Before warehouse funding and loan-book growth, the proxy is 19,524 (106% of net income).
- C4, FY2023-FY2025 cumulative: 100%, which passes (≥ 80%).
- The adjustment removes the change in bank credit and in payables for credit transactions, and adds back the
  change in the loan book. These are balance-sheet deltas from verified statements.

### Excess cash, debt and other claims
- **Excess cash is 0.** Cash is 4,877, against two months of operating costs of 5,974. For a lender, operating
  costs include funding and credit costs.
- **Debt and other claims:**
  - bank credit 115,225: on-call, prime +0.5-0.8%, secured on the loans (paymeant_fy2025 p.49, p.99);
  - leases 2,594;
  - no NCI, preferred shares, bonds or long-term debt.
- **Leases in the bridge.** The lease liability is deducted in the bridge even though the floor already charges
  ROU depreciation. That is the charter-literal, conservative choice; out §2 prints its per-share size.

## 4. Step 3: methods (out §3)

- **EPV, lender basis.** 17,421 / 10% − leases 2,594 = **4.36**.
- **EPV, EV basis (cross-check).**
  - The unlevered normalised EBIT is 30,384, giving owner earnings of 23,396 after tax.
  - Dividing by r and deducting the bank credit and leases gives **2.95**.
  - The two bases are reconciled in §1 above.
- **Ten-year DCF, lender basis.**
  - The g1 cap is min(the per-share EPS record of 47.5%, retention 51.3% × ROIIC 22.2% = 11.4%, 10%), so 10%. The
    per-share record uses 3-year averages over five years, not ten (none exists for Israel), and does not bind.
  - **ROIIC = OE_norm / tangible equity, 22.2%.** This assumes growth at constant margins and a constant capital
    ratio. It is deliberately below the record's incremental ROTE of 34.0% (FY2023 to TTM), which was flattered by
    operating leverage and the shift to merchant fees.
  - **Base growth: 5% nominal (assumed).** That is about 2% CPI plus 3% real, and well inside the cap. Against it:
    the record, with originations from 356M (2022) to 535M (2025) (business.md §2; paymeant_fy2025 p.42) and the
    stated 600M pace (paymeant_h1_2026 p.5). For caution: H1 2026 net income +3.5%, the BNPL rules from 12.1.2027,
    rising arrears and funding concentration.
  - Terminal assumptions: gT 2.5%, and ROIIC_T = r (the library default), so terminal growth adds nothing.
  - The terminal value is 53% of the total, under the 75% warning.
  - Result: **5.36**.
- **Asset values.**
  - NCAV: 1.79.
  - Dempster: 1.10. Loans and receivables are counted at 85%; PP&E, ROU and the platform at nil; every liability,
    including deferred tax, at 100%. All loans and receivables are financial assets (paymeant_h1_2026 p.31), so none
    is treated as prepaid.
  - Tangible book: 2.00, of which the fair-value step-up is 12.1%.
- **Private-owner value.** None exists (no disclosed control transaction).
- **d5 pre-tax multiple.** EV / EBIT_norm is 5.42x on the lender basis and 7.82x on the EV basis. 10x is the d5
  fair price for **Tier A** only. Translated into value it gives 5.81 / 4.85, used as a sanity check, not as a
  method.
- **d9 Graham's yardstick.** Passes: an earnings yield of 14.8% against 8.6%, and a P/E of 6.76 against 10. It is
  labelled [I], looser than Graham's, because it uses the shekel government yield, not an AA corporate yield.
- **d8 implied growth.**
  - Lender basis: **−4.7% a year for ten years** (−5.6% on TTM owner earnings).
  - EV basis: +2.8% at an unlevered ROIIC of 12.1%, which is about the no-leverage value.
- **Bank route.**
  - Passes: F.2 (ROE median 22.5%, ROA 9.0%) and F.3 (equity 37.5% of assets).
  - Fails F.1: the FY2021 loss, with FY2020 absent.
  - Fails F.4 on P/TBV: 1.59 against 1.2. The bank-route price would be **2.40** (1.2x tangible book).
- **The method spread is 168%.** The charter says a spread above 30% is resolved first:
  1. **Lender basis against EV basis.** Explained to the shekel by leverage (§1). The EV basis is invalid for a
     lender (screen_spec 3.1) and is kept as the no-leverage sensitivity.
  2. **Earnings against assets.** EPV / tangible book = 2.18, which is the normalised return on tangible equity
     (22.2%) over r (10%), less leases. The gap is the capitalised excess return. It stands only if that return is
     durable, which is the moat question. Four profitable years with no credit cycle cannot settle it.
  - So the spread is explained but not closed, and that is itself why no A/B lane fits.

## 5. Step 4: the range (out §4)

| Point | Per share | Reason |
|---|---|---|
| Worst case | **1.10** (110 ag) | Funding withdrawn or a credit shock: origination stops and the 30.6.2026 book runs off at Dempster value. Estimated on today's balance sheet because a run-off can come at any time in ten years; retained earnings before then would raise it. It excludes the SPC indemnities and the 360 payment-guarantee exposure, which are not disclosed, so it is **not held with high confidence (A2 fails)** |
| Conservative | **2.75** (275 ag) | EPV on the forced-cyclical EBIT_norm of 14,395 (net 11,084): credit and the 2027 rules bite, no growth |
| Base | **5.36** (536 ag) | DCF on OE_norm 17,421, g 5%, ROIIC 22.2%, r 10% |
| Optimistic | **7.32** (732 ag) | DCF on TTM owner earnings 18,466, g 10% (the cap), ROIIC 23.5% |

**Probabilities.** 10% / 25% / 45% / 20% (assumed; model judgements, uncalibrated) give a probability-weighted
value of **4.67**.

**Impairment markers in the worst case.**
1. *Covenant breach or maturity leading to dilution: a plausible path.*
   - The lines are on-call.
   - The 20% tangible-equity covenant breaks at a loss of 42,385.
   - The Dempster run-off loss is 35,428, which is 84% of that, before the undisclosed exposures.
2. *Going-concern doubt: a plausible path* if the funders withdraw and origination stops.
3. *Assets worth less than debt: no.* Loans and receivables at 85%, 183,369, exceed all liabilities, 145,031.

With plausible paths to markers 1 and 2, E1 fails closed. The charter rejects a bear case with an impairment path
"regardless of expected value".

**F4 stresses.** Revenue, costs and debt are all in shekels, and FX exposure is not material (paymeant_fy2025
p.101).
- **+2 points on prime.** Pre-tax profit falls by 2,304 a year (paymeant_h1_2026 p.9), giving an EPV of 3.91 and a
  base value of 4.72. The fair-value effect of higher discount rates on the fixed-rate loans is not disclosed
  (UNVERIFIED).
- **CPI −1 point.** A one-off of 0.039 a share after tax (paymeant_h1_2026 p.8).
- **High CPI.** It helps while funding stays unlinked, until the rate rise follows.

**Sensitivity grid (D3).** r ± 1 point and g ± 2 points around the base. The minimum is 4.41 (r 11%, g 3%), above
the 3.173 price at every point, so D3 passes on the base. It does not rescue the lane.

## 6. Step 5: margin and buy price (out §5)

- **Shadow Tier B.** 35% + data additions capped at 10%, with no endogenous addition, gives a total of 45%. The buy
  line is 55% of base: **2.95 ILS (295 ag)**. Price / buy price is **1.08**, so D2 fails even in the shadow tier.
- **The three data flags.** The cap means only 10 points count:
  1. `cycle_window_short`.
  2. `derived_tier2_field`:
     - the TTM flows are derived;
     - the 30.6.2026 share count is not filed (39,330,034 is the TASE count of 3.11.2026, which the Mega cap
       reproduces exactly);
     - FY2021 has no balance sheet.
  3. `microcap_field_unavailable`:
     - the SPC terms and maximum loss;
     - the 360 guarantee exposure;
     - the loss curves;
     - the Reg. 24 holdings and pledge report;
     - the Maya immediate reports since 30.6.2026.
- **Tier C.** A 50% margin of private-owner value, but no such value exists, so there is no Tier C buy price.
- **Price used.** The **official close of 3.11.2026, 3.173 ILS** (D7: the latest close, dated; market.md §0). The
  Mega snapshot of 3.18 at 14:04 differs by 0.22% (market.md §0) and changes nothing.
- **Shares and dilution.** 39,330,034 basic. The option overhang at base value is about 1.4% by the treasury method
  (out §5 memo). It is not deducted; it would lower every per-share value by about that much.
- **Hurdle.** The Israel 10-year was 4.29% on 3.11.2026 (the 0537 bond; the generic quote is 4.162%), so r = max(10%,
  7.29%) = 10%.

## 7. Step 6: preliminary verdict (out §6)

### The four questions
1. **Inside the circle?**
   - Cannot be assessed here: theses/CIRCLE.md is not available, so this fails closed and goes to the principal.
   - The model is the avoid list's "dependent on refinancing markets" pattern.
2. **A good business by its lane?** No lane fits.
3. **Price well below value?**
   - On the lender basis, yes: price / base is 0.59.
   - On the no-leverage basis, no: price / EPV is 1.07.
   - Shadow D2 fails.
4. **What does the price assume, and why is that wrong?**
   - On the lender basis, owner earnings shrinking 4.7% a year for ten years, against +13.4% TTM net income and a
     32.9% CAGR for FY2023-FY2025.
   - The causes are known facts the filings do not refute:
     - on-call funding concentrated in one bank;
     - arrears up: default 4,395 and 1-90 days 5,198 on a 209,853 book at 30.6.2026 (paymeant_h1_2026 p.15);
     - the BNPL circular from 12.1.2027, which may shift merchant non-delivery risk to the lender;
     - the credit-data amendment.
   - Under the Petco rule, a discount fully explained by a known fact you cannot refute is priced.
   - **Who sold.** Between 21 and 28 October, 8.6% of the company changed hands and the share fell 46.8% with no
     company news. No interested party reported a sale, and the company said nothing unusual had happened
     (market.md §2-§3). The seller is UNVERIFIED. A forced block seller is a valid answer to the "who is selling"
     part, but it does not answer why the market is wrong about the funding risk.

### VETO items that fail
- A3 and A4 (moat).
- A2 (worst case not held with confidence).
- C2 (leverage and cover).
- C3 (on-call funding must stay open).
- E1 (plausible paths to markers 1 and 2).
- E8 (one bank; take-outs to own SPCs funded by one bank).
- D2 (price above even the shadow buy line).
- D8 (Maya immediate reports since 30.6.2026 not read; only headlines via Globes).
- A0 cannot be assessed.

### Liquidity
- The median daily turnover over the 60 sessions to 3.11.2026 is **17,757 ILS**, against the **50,000 floor**. It
  was 11,060 before the October fall, and the 25th percentile is 1,735.
- The e2 liquidity maximum is 6,940 ILS at cost.
- Turnover is approximated as volume × close from the S&P / StockAnalysis series, with the 3.11 session from
  Bizportal.

### e2 sizing (informational; a NO_THESIS means no position)
- Kelly is at its 100% bound under the assumed probabilities: the expected value is positive.
- Quarter-Kelly 25%, the tier cap 10%, and the permanent-loss budget 7.6% (L_worst 65%).
- Liquidity binds by orders of magnitude.

### Output
**NO_THESIS, not TOO_HARD and not WATCHLIST.**
- Not TOO_HARD: the rejection rests on knowable facts (the funding structure, leverage, moat and liquidity), not on
  data we cannot verify. If every unverifiable item resolved favourably, the verdict would not change.
- Not WATCHLIST: price is not the only failure.

### What would make it worth re-examining
These are dated and observable; none is a buy signal.
1. The FY2026 annual report (due about February 2027) shows **committed** funding of at least two years from at
   least two unrelated funders, with no bank above 50% of drawn credit. It also quantifies the SPC and 360
   guarantee maximum exposures.
2. The same report shows non-current loans back at or below 2.6% of the on-balance-sheet book (the 31.12.2025 level,
   governance_risk.md §9.3), after the BNPL circular has been in force for at least one quarter.
3. The 60-session median turnover is at least 50,000 ILS, and the price is at or below the bank-route 2.40 (1.2x
   tangible book), or at or below 55% of the base value recomputed then.

## 8. Data notes and UNVERIFIED items

- **Primary figures read on the page images:**
  - paymeant_fy2023 p.81, p.82, p.96, p.97, p.111;
  - paymeant_fy2024 p.80, p.81, p.117;
  - paymeant_fy2025 p.42, p.49, p.82, p.83, p.85, p.105, p.106, p.108, p.112;
  - paymeant_h1_2026 p.8, p.9, p.15, p.18, p.23, p.24, p.28, p.31.
- **Figures cited from the reconciled team files**, whose pages the team checked on the images:
  - FY2021 total assets, paymeant_fy2023 p.19;
  - FY2021 equity, p.83;
  - FY2021 PP&E and ROU, p.96-97 (seen in the 1.1.2022 opening balances);
  - originations, paymeant_fy2025 p.42 and paymeant_h1_2026 p.15;
  - FX "not material", paymeant_fy2025 p.101.
- **UNVERIFIED:**
  - the SPC terms, lender identity and maximum loss;
  - the 360 payment-guarantee exposure;
  - pledges of the controllers' shares (the Reg. 24 report is not available);
  - the identity of the October 2026 seller;
  - the content of the 23.9.2026 portfolio-assignment report (headline only);
  - the fair-value sensitivity to discount rates;
  - the 30.6.2026 share count;
  - the turnover series, which is volume × close, an approximation.
- **Not available here:** theses/CIRCLE.md, lib/valuation.py, lib/liquidity.py, the calibration ledger, the fund's
  holdings and NAV, and tax_params. A0, D6, G1's sector and TASE rooms, G3 and the after-tax items cannot be
  assessed here, and go to the principal.
- **Known limitations.**
  - The scenario probabilities are model judgements, not calibrated forecasts.
  - Israeli history is at most six years.
  - This is research, not advice.
