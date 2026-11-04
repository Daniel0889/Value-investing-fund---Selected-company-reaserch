# Paymeant (TASE 1180876): red team on accounting, data and valuation mechanics

Charter step 8, written 3.11.2026. Lens: checklist C1-C7, D1-D8, F3 and F4. I argue against the valuation team's
`research/paymeant/valuation.py`, `research/paymeant/output.txt` and `work/paymeant/valuation_notes.md`.

- **Units.** ILS thousands unless stated; per-share figures in ILS on 39,330,034 shares.
- **Sources.** Every number below is either a filed figure with its PDF page, opened as an image, or is printed by the
  script in section D. The script imports `lib/charter_valuation.py` and is reproduced verbatim with its output. "calc §n"
  points to that output.
- **No file of the team was edited.**

---

## Bottom line

1. **The verdict stands, on firmer ground than the team claims.** NO_THESIS is right. But the value range is too high,
   and two VETO answers the file reports as passing do not pass on the charter's own arithmetic: D3 and C5.
2. **The base value of 5.36 rests on adding back share-based pay.**
   - The team's EBIT_adj removes note 19e's IPO grants and immediately vested options: 2,285 in FY2021, 751 in FY2022
     and 228 in FY2023 (paymeant_fy2023 p.111).
   - screen_spec 2.3 does not allow that, and framework d1 forbids adding back stock pay.
   - Kept in, FY2021 is an operating loss, so d2 classifies the business as **cyclical**. EBIT_norm falls from 22,624 to
     14,249, or 11,707 on fiscal years alone.
   - On the team's own lender basis, the EPV becomes 2.72 (2.23) and the five-percent DCF 3.05 (2.35). That is at or below
     the 3.173 price.
   - The D3 grid runs from 2.59 to 3.74, so D3 fails.
   - Implied growth turns from −4.7% to **+6.5%** (+13.6%). On this basis the price assumes growth, not decline (calc §1).
3. **The EV basis fails D3 too.** Framework d3 and d4 as written deduct the bank credit. On that basis, even with the
   team's normalisation, the EPV is 2.95, the five-percent DCF 3.37 and the grid 2.52 to 4.70 (calc §2).
4. **Earnings quality is weaker than the file says.**
   - Before net capitalisation of development costs, H1 2026 pre-tax profit **fell 4.2%**; the reported change is +6.7%.
   - Part of the controlling holders' pay is capitalised.
   - Provision coverage of the amortised-cost book fell from 64.0% to 16.3% while defaults trebled.
   - The F4 rate stress leaves out the sale-price channel that the company itself names.
   - A net-income covenant of 1M a year and a change-of-control trigger are missing from the code (calc §3-§9).
5. **Some key figures cannot be verified.** These are the Level 2 fair-value marks, the gains on sale to the company's own
   unconsolidated SPCs, the SPC and "360" guarantee exposures, and the economic credit cost (B8).

---

## A. The inputs of valuation.py, re-checked on the page images

| Input group in valuation.py | Pages opened as images | Result |
|---|---|---|
| P&L FY2021-FY2023 (revenue, funding cost, operating profit before other items, other items, tax, NI, EPS) | paymeant_fy2023 p.82 | All agree |
| Other items, split into IPO grant/SBP 288/751/228, options vested immediately 1,997 and termination income (1,188) | paymeant_fy2023 p.111 (note 19e) | Agree; see B1 for their treatment |
| P&L FY2024; quarterly FY2024 | paymeant_fy2024 p.81, p.117 | Agree |
| P&L FY2025; H1 2025 and H1 2026; quarterly FY2025 | paymeant_fy2025 p.83, p.117; paymeant_h1_2026 p.24 | Agree; TTM revenue 60,301, pre-tax 24,460, NI 18,466 |
| Cash flow FY2023-FY2025, H1 (D&A, SBC, OCF, capex lines, lease principal, dividends) | paymeant_fy2025 p.85; paymeant_h1_2026 p.28 | Agree |
| Balance sheets 31.12.2022 to 30.6.2026 | paymeant_fy2023 p.81; paymeant_fy2024 p.80; paymeant_fy2025 p.82; paymeant_h1_2026 p.23 | Agree, including the restated 2023 cash of 16,922 |
| FY2021 total assets 32,944 and equity 22,163 | paymeant_fy2023 p.19, p.83 | Agree |
| Statutory tax 23% | paymeant_fy2025 p.104, p.106 | Agrees, but the effective rate is higher (B11) |
| Covenant 20%; rate sensitivity 1,152; CPI sensitivity 1,981; FV step-up 9,515 | paymeant_h1_2026 p.18, p.9, p.8, p.31 | Agree; three covenants are left out (B6) |
| Lines 340,000; bank B drawn 92,000 of 104,000 | paymeant_fy2025 p.49, p.99 | Agree |
| Arrears at 30.6.2026 | paymeant_h1_2026 p.15 | Agree |
| Options 2,189,875 at 4.02; 512,000 at 5.74; shares 39,245,034 | paymeant_fy2025 p.112, p.108; paymeant_h1_2026 p.33 | Agree; the count conflicts with Reg. 24A (B10) |
| Originations 535 (2025), 258 (H1 2026, +18) | paymeant_fy2025 p.42; paymeant_h1_2026 p.15 | Agree |

**No transcription error was found in valuation.py.** The objections are about treatment, coverage and mechanics.

---

## B. Objections

### B1 (high). The "stable" classification and EBIT_norm of 22,624 rest on an add-back of share-based pay

**The claim.** valuation.py sets `EBIT_ADJ = OP`, operating profit before other items. That removes all of note 19e:
- "IPO grant to senior officers and share-based payment": 288 (2021), 751 (2022) and 228 (2023);
- "share-based payment – options vested immediately": 1,997 (2021);
- the one-off termination income of 1,188 (2022).

All are on paymeant_fy2023 p.111. The FY2021 P&L shows operating profit before other expenses of 1,516, other expenses
of (2,285) and a loss before tax of (769) (paymeant_fy2023 p.82).

**Why it is wrong under the charter.**
- **The definition.** framework.md's notation defines EBIT_adj by screen_spec §2.3. That definition removes impairments,
  restructuring, disposal and litigation items, and for IFRS filers investment-property revaluation gains and other
  operating income where EBIT exceeds gross profit. Compensation is not on the list.
- **d1.** "Stock-based compensation is a cost and is never added back."
- **The cyclical test.** d2 and screen_spec 2.3 say a business is cyclical if "any EBIT_adj_y ≤ 0 in W".
- **Recurrence.** The IPO grant line recurred in three consecutive years. Removing it is therefore at best a recurring
  add-back, which C5 puts on the analyst to justify. valuation_notes.md §3 instead states "C5 passes; no +10".
- **The only removable item** is the 1,188 termination income, which is like a settlement gain.

**The effect, all on the team's own lender basis (calc §1).**

| Case | Cyclical | EBIT_norm | EPV | DCF at g 5% | D3 grid | Implied g |
|---|---|---|---|---|---|---|
| A. Team (other items removed; window FY2021-FY2025 + TTM) | no | 22,624 | 4.36 | 5.36 | 4.41-6.74, passes | −4.7% |
| C. screen_spec 2.3 EBIT_adj, same window | **yes** | 14,249 | **2.72** | **3.05** | 2.59-3.74, **fails** | **+6.5%** |
| D. screen_spec 2.3 EBIT_adj, fiscal years only (B3) | **yes** | 11,707 | **2.23** | **2.35** | 2.04-2.83, **fails** | **+13.6%** |

- **The team's "conservative" case is in substance this base.** It forces the cyclical formula: EBIT_norm 14,395 and
  EPV 2.75.
- **The investment test changes.** On the charter-literal normalisation:
  - Q3: the price is not below value;
  - Q4 (E3): the price already assumes owner earnings grow 6.5-13.6% a year for ten years.
- **The "market assumes decline" reading is an artefact** of the add-back.

**Required change.**
1. Rebuild EBIT_adj by screen_spec 2.3, removing only the 1,188 termination income. Classify the business as cyclical
   and use the cyclical EBIT_norm as base. Recompute the range, the D3 grid, the probability-weighted value and d8.
   Report D3 as failing.
2. If the team keeps the add-back, it must:
   - declare it an endogenous, recurring add-back: +10 points outside the cap;
   - carry C5's burden of proof;
   - restate the shadow buy line as 2.41, not 2.95 (calc §1).
3. Either way, C5 cannot be reported as "passes".

**Checklist items:** C5, B5, D1, D2, D3, D4, E3.

### B2 (medium). The lender basis is used for every headline number; the charter-literal EV basis fails D3

**The claim.** The range, the sensitivity grid ("D3: True"), the probability-weighted 4.67, "price / base 0.59" and the
implied growth of −4.7% are all on a "lender basis". That basis keeps the 115,225 of on-call warehouse credit out of the
bridge and capitalises the spread it earns.

**Why it is wrong under the charter.**
- **framework d3 deducts the debt.** It defines EPV_equity = OE_unlevered / r + excess cash − D − leases. d4 bridges the
  same way.
- **The bank route has no DCF.** screen_spec 3.1 sends lenders to the bank route (4.7). That route is a set of gates:
  P/TBV ≤ 1.2 and pe_norm ≤ 10. Paymeant fails F.1 and F.4 there, and the route's price is 2.40 (output §3).
- **The fund declines to pay for this leverage.** Rule 4 and the f2 avoid list ("dependent on refinancing markets ...
  Delta Financial's warehouse lines") say so. The team itself shows that the whole gap between the bases is the
  warehouse leverage (output §3).

**The effect (calc §2), on the EV basis with the team's normalisation.**
- EPV 2.95.
- Five-percent DCF 3.37, at an unlevered ROIIC of 12.1%, about r.
- Grid 2.52 to 4.70, so **D3 fails**.
- Implied growth +2.8%: the price pays about the no-leverage value.
- With the screen_spec 2.3 normalisation the EV-basis EPV is 0.63.

**The method spread.** It is 168% (output §5). The charter says such a spread "is resolved first". The file explains it
but does not close it, so D1 is open, not passed.

**Required change.**
1. Show both bases in the range, the D3 grid, the probability-weighted value and d8.
2. Answer D3, Q3 and Q4 on the more conservative charter-literal basis.
3. Replace "D3: True" with "fails", or "n/a, no lane binds D3".
4. Q3 should read "no". Q4 should read "+2.8% on the EV basis", not "−4.7%".
5. Do not publish a shadow buy price for a lane-less name. If one is kept, compute it on the charter-literal base: 1.68
   (calc §1).
6. Re-examination condition 3 in valuation_notes.md §7 ("55% of the base value recomputed then") must name the basis.

**Checklist items:** D1, D2, D3, D4, E3, C2.

### B3 (low). The window counts TTM as a sixth year

**The claim.** W is "FY2021-FY2025 plus TTM". That counts H2 2025 twice: it sits in FY2025 and again in the TTM.
framework d2 and screen_spec 2.2 define W as fiscal years: "FY2020 through the latest FY". TTM supplies only Rev_ttm in
the stable formula.

**The effect (calc §1, case B).** With the team's own EBIT_adj, the fiscal-year window gives:
- m_norm 35.04%, against 37.52%;
- EBIT_norm 21,131;
- EPV 4.07 and DCF 4.95.

With the screen_spec EBIT_adj it is case D above.

**Required change.** Compute m_norm, the cyclical test and the cyclical candidates on fiscal years only.

**Checklist items:** D1, D3.

### B4 (medium). Capitalised development flatters the trend, the "record" and the TTM

**The facts.**
- **Capitalisation nearly trebled.** Additions to the platform asset were 1,994 in H1 2026 (cash 1,902 + capitalised SBP
  92), against 697 in H1 2025 (paymeant_h1_2026 p.28). The capitalised share of gross R&D rose from 14% to 34% (calc §9).
- **The directors say so.** R&D expense fell 5% in the half and 16% in Q2, "mainly from capitalisation for additional
  developments" (paymeant_h1_2026 p.13).
- **Net of amortisation, the swing is large.** Net capitalisation (additions − amortisation) was +962 in H1 2026, against
  −163 in H1 2025, and +512 in the TTM. Before it, **H1 2026 pre-tax profit fell 4.2% y/y**; the reported change is +6.7%
  (calc §9).
- **Controller pay is capitalised.** Pay to key management personnel who are interested parties, i.e. the two
  controlling holders, was capitalised into the intangible asset: 1,363 (2023), 751 (2024) and 500 (2025)
  (paymeant_fy2025 p.115). That is a related-party flow into the balance sheet.
- **The window years were flattered.** Net capitalisation was +2,021, +2,250, +2,666 and +983 in FY2021-FY2024
  (paymeant_fy2023 p.98, p.110; paymeant_fy2025 p.98).
- **TTM revenue holds an unrealised gain.** It includes the +1,216 growth of the fair-value step-up on a held book that
  grew from 131,460 to 203,167 (paymeant_h1_2026 p.31, p.23). With net capitalisation that is 1,728, or 7.1% of TTM
  pre-tax (calc §9).
- **The latest quarters are weaker.**
  - Revenue was 16,210 and 15,579 in Q3-Q4 2025, against 14,440 and 14,072 in Q1-Q2 2026.
  - Net income was 5,013 and 5,168, against 4,100 and 4,185 (paymeant_fy2025 p.117; paymeant_h1_2026 p.24).
  - H1 2026 pre-tax, annualised, is 21,920, below the EBIT_norm of 22,624. This is partly seasonal: H2 beat H1 in 2024
    and 2025.
- **Capex runs above the floor.** H1 2026 capex alone was 2,022, or 4,044 annualised, against the TTM D&A of 3,278 used as
  the maintenance floor (calc §10).

**Why it matters.** The "record" in Q4 and d8 rests on growth flattered by capitalisation: TTM NI +13.4%, H1 +3.5%,
FY2023-FY2025 CAGR +32.9%. So does the base growth of 5%. framework d says base inputs are "realistic, erring
conservative".

**Required change.**
1. Restate the growth record before net capitalisation and before the step-up growth.
2. Justify the 5% base against −4.2% underlying growth, or set it at or below CPI.
3. Charge maintenance capex at the H1 2026 run-rate, or show the effect.
4. Record C4 (capitalised expenses) and B5 (capitalised related-party pay) as FLAG items with written explanations.

**Checklist items:** C4, B5, D4, E3, D1.

### B5 (medium). The credit cost is not visible, and provisioning weakened as defaults trebled

**The facts.**
- **The P&L line covers only the small book.** The credit-loss line covers the amortised-cost book only. Expected losses
  on the 203,167 fair-value book sit inside revenue (paymeant_h1_2026 p.13; paymeant_fy2025 p.64).
- **Coverage fell.** Provision coverage of the amortised-cost book was 46.3% (2022), 39.2% (2023), 64.0% (2024) and 16.3%
  (2025) (paymeant_fy2023 p.95; paymeant_fy2024 p.95; paymeant_fy2025 p.95).
- **Write-offs ran ahead of the charge.** Write-offs were 833 in 2024 and 1,680 in 2025, against a 2025 charge of 783
  (calc §8, §10).
- **Defaults trebled in six months.** From 31.12.2025 to 30.6.2026 (paymeant_fy2025 p.66; paymeant_h1_2026 p.15):
  - defaults rose from 1,481 to 4,395 (×2.97);
  - 1-90-day arrears rose 45%;
  - arrears rose from 2.65% to 4.57% of the book.
  The H1 2026 charge was 670 (paymeant_h1_2026 p.24).
- **The interim hides the gross figures.** It gives only the net amortised-cost book, 6,686, with no gross amount or
  provision (paymeant_h1_2026 p.31).
- **The directors' text does not match the table.** It says there is no increase in arrears "except a negligible change
  relative to the volume of loans originated" (paymeant_h1_2026 p.15).
- **If the defaulted loans sit in the amortised-cost book,** coverage of 50-70% would need 2,791-8,651 more provision:
  11-35% of TTM pre-tax (calc §8). The location of those loans is not disclosed: **UNVERIFIED**.
- **The stresses run so far miss the binding risk.**
  - The window holds no credit cycle.
  - framework f3's Wells Fargo stress was not run. Run here, 19.4% of the on-balance-sheet book can default at 60%
    severity before pre-tax profit reaches zero (calc §8). So the held book is not the binding risk; the origination
    engine is (B6).
  - The team's "conservative" case comes from a formula that penalises growth. It is not a credit stress.

**Required change.**
1. Label the credit cost UNVERIFIED.
2. Add an explicit normalised credit cost, or a credit-stress conservative case.
3. Run the f3 stress.
4. Value defaulted loans at a recovery rate in the worst case.
5. Obtain the gross amortised-cost book and provision from the Q3 2026 report before any re-examination.

**Checklist items:** C1, C4, B5, A2, E1, D1.

### B6 (medium). Three covenants and a change-of-control clause are missing, and C1 is unanswered

**The facts.**
- **There are four covenants, not one.** Note 11a(6) lists them (paymeant_fy2025 p.99), and paymeant_h1_2026 p.18 and
  p.33 repeat them:
  - tangible equity of at least 20% of the balance sheet;
  - tangible equity of at least 25M;
  - senior debt of at most 80% of loans;
  - **annual net profit of at least 1M.**
- **Change of control is a trigger.** The line agreements restrict any change of control in the company and its
  controlling holders, and list causes for immediate repayment (paymeant_fy2025 p.99).
- **The code models only one.** valuation.py models only `COV_TE_RATIO`. Output §4, marker (1), cites only the loss of
  42,385 that breaks it.
- **The profit covenant is the nearest (calc §6).**
  - It breaks after a fall in pre-tax profit of 23,161, which is 94.7% of TTM.
  - Revenue that depends on new originations (fees plus loan sales and fair value) was 45,617 in the TTM, against opex of
    28,857.
  - With opex flat, an origination fall of 50.8% reaches the covenant. An origination stop breaches it within the year.
- **C1 is VETO for every lane,** yet it is missing from the team's list of answered VETO items. C1 asks for survival
  "without new money". With on-call lines, that holds only if the banks keep rolling them.
- **The change-of-control clause ties the funding to the controllers' stake.** Their shareholders' agreement lapses
  below 25% jointly (paymeant_fy2025 p.123; market.md §3).

**Required change.**
1. Add all four covenants and the change-of-control trigger to valuation.py.
2. Restate E1 marker (1): the first covenant to break is the profit covenant, at an origination fall of about half, not
   a 42M loss.
3. Answer C1 explicitly. It is "no / don't know", which fails closed.

**Checklist items:** C1, C3, E1, F1.

### B7 (medium). The F4 rate stress leaves out the channel the company itself names

**The claim.** The +2-point stress charges only the warehouse: 2,304 a year (output §4), from the 1,152 per point that the
company gives for its bank credit (paymeant_h1_2026 p.9). It calls the fair-value effect "not disclosed".

**What the filings say.**
- Portfolio sale prices discount cash flows at a rate "derived from government bonds of similar duration plus a
  margin" (paymeant_fy2025 p.51).
- A rate rise has an indirect effect, "mainly a decrease ... in the consideration in loan-portfolio assignment
  transactions", which repricing of new loans moderates (paymeant_h1_2026 p.10).
- Loan duration is 14 months, and 60% of 2025 credit was sold (paymeant_fy2025 p.42).

**The effect (calc §7).**
- A one-off fair-value loss on the held book of 2,438-4,741.
- Sale-price compression of 7,742 a year until loans are repriced.
- A first-year pre-tax hit of 12,484-14,787, which is 51-60% of TTM. The team has 2,304.
- If the annual parts were never repriced, the lender EPV would be 2.40, against the team's stressed 3.91.

**A mitigating fact.** In the 2022-2023 rate rise the company held more loans and repriced: 40% sold in 2023, at a
nominal rate of 9.83% (paymeant_fy2025 p.42).

**Required change.**
1. Model all three channels with a stated repricing lag.
2. Test the net-profit covenant under the stress.
3. Keep F4 open until the held book's discount-rate sensitivity is sourced.

**Checklist items:** F4, C1, D3.

### B8 (medium). Revenue recognition, Level 2 marks, SPC derecognition and the "360" guarantee: key figures cannot be verified

**The marks are set against the company's own vehicles.**
- Loans held for sale are carried at fair value through profit or loss and classified **Level 2** (paymeant_fy2025
  p.91).
- They are measured with "dedicated calculators that reflect the commercial terms closed with the purchasing parties"
  (paymeant_fy2025 p.103). The pricing formula fixes the expected default rate in advance (paymeant_fy2025 p.51).
- The FY2025 full-sale table lists only **Paymeant Series 1 and Series 2** (paymeant_fy2025 p.51-53). Both are the
  company's own 100%-held, unconsolidated SPCs, funded by a bank (paymeant_fy2025 p.94, p.106-108).
- So the "observable" prices behind the Level 2 marks and the gains on sale come from deals with the company's own
  vehicles.

**The company keeps exposure after the sale.**
- Deferred consideration is held in the SPCs' bank deposits and released as the sold portfolio repays
  (paymeant_fy2025 p.108, note 16a9).
- Receivables of 5,875 are mostly accrued income from assignments and these deferred amounts (paymeant_h1_2026 p.11,
  p.31; paymeant_fy2025 p.62, p.95).
- The company indemnifies the SPCs "for breach of representations and other cases" (paymeant_h1_2026 p.33).
- No table of the maximum exposure to loss is given.

**The 360 guarantee carries no visible liability.**
- Fees, 15,699 of 28,512 in H1 2026, are recognised when the transaction completes in the system (paymeant_fy2025 p.88;
  paymeant_h1_2026 p.32).
- The "360" operation and payment-guarantee product leaves deferred income inside "amounts payable for credit
  transactions" (paymeant_fy2025 p.62; paymeant_h1_2026 p.11). No guarantee liability, expected loss or exposure is
  disclosed.
- Operating income rose from 665 to 1,984 (paymeant_h1_2026 p.32).

**The marks feed several figures.** The 9,515 step-up (paymeant_h1_2026 p.31) enters tangible book, P/TBV, the bank-route
price and Dempster value.

**Required change.**
1. List as UNVERIFIED key figures: the fair-value marks, the SPC gains, the retained SPC exposure, the 360 exposure and
   the economic credit cost.
2. Haircut the fair-value and sale revenue and the 360 income in the conservative case.
3. Show leverage with the SPC debt consolidated, or state that it cannot be computed.
4. Record that the TOO_HARD key-figure test is met in part.

**Checklist items:** F3, C7, B5, A2, E8, D1.

### B9 (low). The worst case is overstated

**The claim.** Dempster value counts at 85%:
- the 4,395 of defaulted loans (paymeant_h1_2026 p.15);
- the 5,875 of receivables that are mostly SPC deferred consideration and accrued income (B8).

It charges no wind-down cost.

**The effect (calc §5).**

| Variant | Value | L_worst | Permanent-loss budget |
|---|---|---|---|
| Team | 1.10 | 65.4% | 7.6% |
| Defaults at 30%, SPC receivables at 50% | 0.99 | 69.0% | 7.3% |
| The same, after a six-month wind-down at half of TTM opex | 0.80 | 74.7% | 6.7% |
| The same on amortised cost, without the step-up | 0.60 | 81.2% | 6.2% |

**Required change.** Report the worst case as a range of 0.60-1.10 and size off the low end. State that the off-balance
-sheet SPC and guarantee exposures are excluded.

**Checklist items:** A2, E1, G1, D1.

### B10 (low). Dilution is understated, and B3 is not answered

**The facts.**
- **The memo.** It shows 546,742 shares (1.4%). It applies one weighted strike of 4.02 to all 2,189,875 options
  (paymeant_fy2025 p.112) and leaves out the 175,000 RSUs (paymeant_fy2025 p.110, p.123).
- **Instrument by instrument (calc §4),** the overhang is 805,224 shares (2.05%) at the team's base value and 309,797
  shares (0.79%) at the price. The instruments are:
  - 1,000,000 options to the controllers at 3.01 (paymeant_fy2025 p.111);
  - 519,000 employee options at 3.97, less 100,040 forfeited (paymeant_fy2025 p.111, p.112);
  - the 0.01-strike employee options;
  - the RSUs;
  - Amitim's 255,000 at 6.05, to 12.1.2027;
  - 512,000 options at 5.74 (paymeant_h1_2026 p.33).
- **The counts conflict.** Reg. 24A shows 1,136,125 options, against 2,189,875 in note 17 (paymeant_fy2025 p.123, p.112).
  They are not reconciled.
- **Diluted EPS confirms dilution.** It was 0.20 in H1 2026, against basic 0.21 (paymeant_h1_2026 p.24). That implies at
  least 40,414,634 diluted shares at H1 prices.
- **B3 is unanswered.** The share count rose 19.4% in 2022 and 5.3% in 2025 (derived.txt). Most of 2025's rise was
  1,920,000 third-party warrants exercised for about 4M (paymeant_fy2025 p.112).

**Required change.**
1. Compute per-share values on a diluted count wherever the options are in the money at the value computed.
2. Reconcile note 17 with Reg. 24A.
3. Answer B3: dilution was above 2% a year in 2022 and 2025.

**Checklist items:** B3, C7, D1.

### B11 (low). The tax rate is the statutory one, though the filing's own reconciliation runs higher

**The facts.**
- Effective rates were 24.51% for the TTM, 24.41% for H1 2026 and 23.49% for FY2025 (calc §3).
- The FY2025 reconciliation adds an unexplained "other" of 116 to the 23% (paymeant_fy2025 p.106). Share-based pay
  under section 102 (paymeant_fy2025 p.110) is a likely source.
- framework's notation asks for the statutory rate "checked against the filing's own rate reconciliation".

**The effect (calc §3).** At 24%, the EPV is 4.31 and the DCF 5.28, against 4.36 and 5.36.

**Required change.** Use 24%, or state why 23% holds.

**Checklist items:** D1, C7.

### B12 (low). Some identities and single-source figures do not hold

**The facts.**
- **The H1 2025 cash flow is inconsistent** (paymeant_h1_2026 p.28; reconcile.md §B M9 and §C). Its lines enter every
  TTM cash figure, including the TTM OCF of 12,963 and the "cash proxy" of 19,524.
  - It shows no tax paid, although taxes payable fell from 5,707 to 1,066 in the half (paymeant_h1_2026 p.23;
    paymeant_fy2025 p.82); the team estimates about 6.6M was paid.
  - Q2 2025 shows no interest received, against 2,340 of interest income (paymeant_h1_2026 p.28, p.32).
  - The customer-credit line does not reconcile with the change in the loan book less interest received. The gap is
    2,912 in H1 2025 and nil in H1 2026 (calc §10).
- **Bank credit sits in two places.** It is presented in operating cash flow (paymeant_fy2025 p.85) but listed among
  liabilities from financing activities (note 13f, paymeant_fy2025 p.104). So Mega's "cash_flow_operations 12,963"
  includes 51,875 of new bank borrowing (output §2).
- **The company's covenant figures do not reconcile.** Its "tangible equity" was 82M at 31.12.2025 and 76M at 30.6.2026
  (paymeant_fy2025 p.68; paymeant_h1_2026 p.18). Equity less intangibles was 74,891 and 78,643 (calc §10). It gives the
  tangible-balance-sheet ratio as a range of 32%-40%.

**Required change.**
1. Treat the TTM cash-flow figures and the company's covenant ratios as unreconciled: C7 is open on them.
2. Do not cite the TTM cash proxy as evidence.
3. Compute covenant headroom on both definitions.

**Checklist items:** C7, F3, C4.

---

## C. Checked, with no objection

- **Currency.** The company reports in ILS. The USD rate is used for display only (F3).
- **Consolidation.** The H1 2026 statements are consolidated. NCI and preferred are nil (paymeant_h1_2026 p.23).
- **IFRS 16.** Maintenance capex is floored at total D&A, including ROU depreciation, and the lease liability is also
  deducted in the bridge. That charges leases twice, which is conservative.
- **SBC in owner earnings.** It is never added back there. B1 is about EBIT_adj, not about owner earnings.
- **Cash.** The 4,877 is not free: it sits in pledged dedicated accounts (paymeant_fy2025 p.99, note 11b) and is owed
  onward through payables for credit transactions. The team's excess cash of 0 is right.
- **Loan-book build-up (C4's inventory test).** Loans held for sale equal 4.41 months of TTM originations at 30.6.2026,
  against 4.19-5.14 at the 2023-2025 year-ends. There is no abnormal build-up; the 3.43 at 30.6.2025 followed two SPC
  sales (calc §10). The team's constructed "100%" C4 figure is not needed to reach that answer.
- **Identities at 30.6.2026 (C7).** The balance sheet balances, the H1 2026 cash flow foots to the closing cash of 4,877,
  and NI / EPS agrees with the share count (calc §10).
- **Price, shares and hurdle (D5, D7).** The 3.173 close, the 39,330,034 shares and r = 10% are right. The 1,188
  termination income is correctly removed. The 20% covenant's break-loss of 42,385 reproduces.
- **D8.** The team marks it failing. I agree: the ~100M assignment of 23.9.2026 and the Series 1 SPC share transfer of
  10.9.2026 (scuttlebutt.md) could change both the derecognition picture and the Q3 TTM.

---

## D. Calculation script and output

Run by extracting the block below and piping it to `python3 -I -`. It reads nothing but `lib/charter_valuation.py` and
writes nothing.

```python redteam-calc
# redteam-calc: Paymeant red team (accounting, data and valuation mechanics), 3.11.2026
import sys
sys.dont_write_bytecode = True
sys.path.insert(0, "/home/user/value-investing-fund---selected-company-reaserch/lib")
import charter_valuation as cv

SH, PRICE = 39_330_034, 3.173          # TASE count 3.11.2026; official close (as the valuation team)
R, T = cv.hurdle(0.0429), 0.23          # r = 10%; statutory tax (fy2025 p.104, p.106)
ps = lambda k: k * 1000 / SH
# ---- filed inputs, ILS k (pages opened as images: fy2023 p.82, p.111; fy2024 p.81; fy2025 p.83; h1_2026 p.24)
REV  = {"FY2021": 7850, "FY2022": 23874, "FY2023": 38524, "FY2024": 43046, "FY2025": 56616, "H1_2025": 24827, "H1_2026": 28512}
FUND = {"FY2021": 90, "FY2022": 1982, "FY2023": 7750, "FY2024": 5224, "FY2025": 4711, "H1_2025": 1477, "H1_2026": 2738}
OPB  = {"FY2021": 1516, "FY2022": 8295, "FY2023": 13500, "FY2024": 17216, "FY2025": 23772, "H1_2025": 10272, "H1_2026": 10960}
PBT  = {"FY2021": -769, "FY2022": 8732, "FY2023": 13272, "FY2024": 17216, "FY2025": 23772, "H1_2025": 10272, "H1_2026": 10960}
GAIN = {"FY2022": 1188}                 # note 19e (fy2023 p.111): income on ending the engagement with acquiring corporation A
TAX  = {"FY2025": 5584, "H1_2025": 2265, "H1_2026": 2675}
ttm = lambda d: d["FY2025"] + d["H1_2026"] - d["H1_2025"]
for d in (REV, FUND, OPB, PBT, TAX):
    d["TTM"] = ttm(d)
FY = ["FY2021", "FY2022", "FY2023", "FY2024", "FY2025"]
W6 = FY + ["TTM"]
TE, LEASES, BANK = 86912 - 8269, 2594, 115225          # h1_2026 p.23
TOC_J26 = 193504                                        # team's tangible operating capital, 30.6.2026 (reproduced)

print("== 1. Normalisation (framework d2, screen_spec 2.3), lender (equity) basis, g 5%, ROIIC = OE_norm / TE")
team = {p: OPB[p] for p in W6}                          # team: every 'other' item removed (incl. IPO share-based pay)
lit = {p: PBT[p] - GAIN.get(p, 0) for p in W6}           # screen_spec 2.3: only the 1,188 gain removed; stock pay stays
res = {}
for e, W, lab in ((team, W6, "A team: other items removed, W = FY21-25 + TTM"),
                  (team, FY, "B team EBIT_adj, W = fiscal years only"),
                  (lit, W6, "C screen_spec 2.3 EBIT_adj, W + TTM"),
                  (lit, FY, "D screen_spec 2.3 EBIT_adj, fiscal years")):
    n = cv.normalised_ebit(REV["TTM"], [e[x] for x in W], [REV[x] for x in W])
    oe = n.ebit_norm * (1 - T)
    roiic = oe / TE
    epv = ps(cv.equity_bridge(cv.epv_operations(oe, R), 0, 0, 0, LEASES))
    dcf = ps(cv.dcf_operations(oe, R, 0.05, roiic).operations_value - LEASES)
    grid = cv.sensitivity_grid(lambda rr, gg: ps(cv.dcf_operations(oe, rr, gg, roiic).operations_value - LEASES), R, 0.05)
    gi = cv.implied_growth(PRICE * SH / 1000 + LEASES, oe, R, roiic)
    res[lab[0]] = (n, oe, epv, dcf, grid)
    print(f"  {lab:<46} m_norm {n.m_norm:6.2%} cyclical {str(n.cyclical):5} EBIT_norm {n.ebit_norm:7,.0f} OE {oe:7,.0f}"
          f" | EPV {epv:4.2f} DCF {dcf:4.2f} grid {grid['min']:4.2f}-{grid['max']:4.2f} (D3 {grid['min'] > PRICE}) | implied g {gi:+.1%}")
print("  screen_spec 2.3 EBIT_adj by period:", lit)
print("  shadow Tier B buy price on C: 45% margin", round(res["C"][3] * 0.55, 2), "| with the add-back kept as endogenous (+10):",
      round(res["A"][3] * 0.45, 2))

print("== 2. EV basis as framework d3/d4 are written (funding added back; bank credit and leases deducted)")
for e, W, lab in ((team, W6, "team EBIT_adj, W + TTM"), (lit, W6, "screen_spec 2.3 EBIT_adj, W + TTM")):
    unl = {p: e[p] + FUND[p] for p in W6}
    n = cv.normalised_ebit(REV["TTM"], [unl[x] for x in W], [REV[x] for x in W])
    oeu = n.ebit_norm * (1 - T)
    ru = oeu / TOC_J26
    epv = ps(cv.equity_bridge(cv.epv_operations(oeu, R), 0, 0, BANK, LEASES))
    dcf = ps(cv.equity_bridge(cv.dcf_operations(oeu, R, 0.05, ru).operations_value, 0, 0, BANK, LEASES))
    grid = cv.sensitivity_grid(lambda rr, gg: ps(cv.equity_bridge(cv.dcf_operations(oeu, rr, gg, ru).operations_value, 0, 0, BANK, LEASES)), R, 0.05)
    gi = cv.implied_growth(PRICE * SH / 1000 + BANK + LEASES, oeu, R, ru)
    print(f"  {lab:<36} cyclical {str(n.cyclical):5} EBIT_norm {n.ebit_norm:7,.0f} OE_unl {oeu:7,.0f} ROIIC_unl {ru:5.1%}"
          f" | EPV {epv:5.2f} DCF {dcf:5.2f} grid {grid['min']:5.2f} to {grid['max']:5.2f} (D3 {grid['min'] > PRICE}) | implied g {gi:+.1%}")

print("== 3. Tax: TTM effective", f"{TAX['TTM'] / PBT['TTM']:.2%}", "| H1 2026", f"{2675 / 10960:.2%}", "| FY2025", f"{5584 / 23772:.2%}",
      "| 'other' in the FY2025 reconciliation 116 =", f"{116 / 23772:.2%} of PBT")
oe_a = res["A"][1] / (1 - T)
for t in (0.24, TAX["TTM"] / PBT["TTM"]):
    oe = oe_a * (1 - t)
    print(f"  t {t:.2%}: OE_norm {oe:,.0f} EPV {ps(oe / R - LEASES):.2f} DCF {ps(cv.dcf_operations(oe, R, 0.05, oe / TE).operations_value - LEASES):.2f} (team 4.36 / 5.36)")

print("== 4. Dilution, instrument by instrument (fy2025 p.108-112, p.123; h1_2026 p.33), treasury method")
inst = [(1_000_000, 3.01), (519_000 - 100_040, 3.97), (255_000, 6.05), (313_000 + 75_000 - 257_475 - 46_835, 0.01),
        (175_000, 0.0), (512_000, 5.74)]
known = sum(n for n, _ in inst[:4]) + 255_000            # note-17 count also held the expired Amitim tranche at 31.12.2025
resid = 2_189_875 - known
resid_k = (2_189_875 * 4.02 - sum(n * k for n, k in inst[:4]) - 255_000 * 6.05) / resid
inst.append((resid, resid_k))
for pv in (PRICE, 5.3576):
    s = sum(n * max(0.0, 1 - k / pv) for n, k in inst)
    print(f"  at {pv:.4f}: {s:,.0f} dilutive shares = {s / SH:.2%} (team memo 546,742 = 1.4% at 5.3576, one weighted strike, no RSUs)")
print(f"  residual note-17 options {resid:,} at an implied strike of {resid_k:.2f}; H1 2026 diluted EPS 0.20 vs basic 0.21 implies >= {8_285_000 / 0.205:,.0f} diluted shares")

print("== 5. Worst case: Dempster at 30.6.2026 (h1_2026 p.15, p.23, p.31)")
cash, fv, fv_ac, ac, recv, tl, dflt = 4877, 203167, 193652, 6686, 5875, 145031, 4395
team_d = cv.dempster_value(cash, fv + ac + recv, 0, 0, 0, tl)
v1 = cash + 0.85 * (fv + ac - dflt) + 0.30 * dflt + 0.50 * recv - tl
v2 = cash + 0.85 * (fv_ac + ac - dflt) + 0.30 * dflt + 0.50 * recv - tl
wind = 0.25 * (27350 + 14144 - 12637)
for lab, v in (("team (85% on every loan and receivable)", team_d), ("defaults 30%, SPC/accrued receivables 50%", v1),
               ("same, less a six-month wind-down at half of TTM opex", v1 - wind), ("same on amortised cost (no FV step-up), less wind-down", v2 - wind)):
    lw = (PRICE - ps(v)) / PRICE
    print(f"  {lab:<58} {ps(v):5.2f} | L_worst {lw:5.1%} | permanent-loss budget {0.05 / lw:4.1%} of NAV")

print("== 6. Covenants (fy2025 p.99 note 11a(6); h1_2026 p.18, p.33)")
pre = PBT["TTM"]
need = pre - 1000 / (1 - T)
orig_rev = (27278 + 15699 - 11154) + (16301 + 6068 - 8575)   # fees + loan sales/FV, TTM (fy2025 p.113; h1_2026 p.32)
print(f"  NI >= 1M breaks after a pre-tax fall of {need:,.0f} ({need / pre:.1%} of TTM); TE-ratio 20% after a loss of 42,385 (team);"
      f" TE >= 25M after {TE - 25000:,}")
print(f"  origination-driven revenue TTM {orig_rev:,} vs opex TTM {27350 + 14144 - 12637:,}; with opex flat the NI covenant is reached"
      f" at an origination fall of {need / orig_rev:.1%}")

print("== 7. F4: +2 points through the warehouse, the held book's fair value and the sale price (fy2025 p.42, p.51; h1_2026 p.9, p.10)")
dur_new = 14 / 12                                       # loan duration 14 months (fy2025 p.42)
sold = 553000 * 0.60 * 0.02 * dur_new                   # TTM originations 553M x 60% sold (fy2025 p.42) x 2 points x duration
wh = 2 * 1152
for dur_book in (0.6, dur_new):
    fvh = 203167 * 0.02 * dur_book
    print(f"  held-book duration {dur_book:.2f}y: one-off FV loss {fvh:,.0f}; sale-price compression {sold:,.0f}/yr until repriced;"
          f" warehouse {wh:,}; first-year pre-tax hit {fvh + sold + wh:,.0f} ({(fvh + sold + wh) / pre:.0%} of TTM; team 2,304)")
oe_s = (res["A"][0].ebit_norm - wh - sold) * (1 - T)
print(f"  if the annual parts were never repriced: lender EPV {ps(oe_s / R - LEASES):.2f} (team stress 3.91)")

print("== 8. Credit: amortised-cost book (fy2023 p.95; fy2024 p.95; fy2025 p.95), arrears (fy2025 p.66; h1_2026 p.15)")
prov = {"2022": (1410, 653), "2023": (3604, 1411), "2024": (2859, 1831), "2025": (5731, 934)}
chg = {"2023": 758, "2024": 1253, "2025": 783}
print("  coverage:", {y: f"{p / g:.1%}" for y, (g, p) in prov.items()},
      "| write-offs:", {y: prov[str(int(y) - 1)][1] + chg[y] - prov[y][1] for y in chg})
print(f"  defaults 1,481 -> 4,395 (x{4395 / 1481:.2f}); 1-90 days 3,590 -> 5,198 ({5198 / 3590 - 1:+.0%}); arrears/book {(3590 + 1481) / 191493:.2%} -> {(5198 + 4395) / 209853:.2%}; H1 2026 charge 670")
for c in (0.5, 0.7):
    p_need = c / (1 - c) * dflt
    print(f"  IF the defaulted loans sit in the amortised-cost book at {c:.0%} coverage: provision {p_need:,.0f} vs at most {934 + 670:,} -> shortfall {p_need - 1604:,.0f} ({(p_need - 1604) / pre:.0%} of TTM pre-tax) [UNVERIFIED]")
print(f"  f3 Wells Fargo stress: defaults on the 209,853 on-balance-sheet book at 60% severity that take pre-tax to zero {pre / (0.6 * 209853):.1%}; to the NI covenant {need / (0.6 * 209853):.1%}")

print("== 9. Capitalised development (fy2023 p.98, p.110; fy2025 p.98, p.114; h1_2026 p.23, p.28)")
add = {"FY2021": 2021, "FY2022": 2377, "FY2023": 2892, "FY2024": 2356, "FY2025": 1279, "H1_2025": 642 + 55, "H1_2026": 1902 + 92}
amo = {"FY2021": 0, "FY2022": 127, "FY2023": 226, "FY2024": 1373, "FY2025": 1892, "H1_2025": 7920 + 697 - 7757, "H1_2026": 7307 + 1994 - 8269}
net = {k: add[k] - amo[k] for k in add}
net["TTM"] = ttm(net)
print("  net capitalisation (additions - amortisation):", net)
print(f"  H1 pre-tax growth: reported {10960 / 10272 - 1:+.1%}; before net capitalisation {(10960 - net['H1_2026']) / (10272 - net['H1_2025']) - 1:+.1%}")
print(f"  capitalised share of gross R&D: H1 2025 {add['H1_2025'] / (4177 + add['H1_2025']):.0%}, H1 2026 {add['H1_2026'] / (3950 + add['H1_2026']):.0%}")
print(f"  FV step-up growth inside TTM revenue: {9515 - 8299:,} (h1_2026 p.31); with net capitalisation {9515 - 8299 + net['TTM']:,} = {(9515 - 8299 + net['TTM']) / pre:.1%} of TTM pre-tax")
q = {"Q3_2025": (16210, 5013), "Q4_2025": (15579, 5168), "Q1_2026": (28512 - 14072, 8285 - 4185), "Q2_2026": (14072, 4185)}
print("  quarters (revenue, NI), fy2025 p.117 and h1_2026 p.24:", q, f"| H1 2026 annualised pre-tax {2 * 10960:,} vs EBIT_norm 22,624")

print("== 10. Identities, inventory test, covenant equity, capex run-rate (fy2024 p.42; fy2025 p.45, p.82, p.113; h1_2026 p.5, p.23, p.24, p.28)")
print(f"  balance sheet 30.6.2026: liabilities + equity {141299 + 3732 + 86912:,} vs assets 231,943;"
      f" H1 2026 cash flow {5236 - 1930 - 4367:,} -> closing cash {5938 + 5236 - 1930 - 4367:,} (filed 4,877)")
print(f"  NI / basic EPS: FY2025 {18188 / 0.47 * 1000:,.0f} vs weighted 38,723,775 (fy2025 p.113); H1 2026 {8285 / 0.21 * 1000:,.0f} vs {SH:,}")
orig = {"31.12.2023": 365, "31.12.2024": 389, "31.12.2025": 535, "30.6.2025": 389 - (82 + 87) + (127 + 113),
        "30.6.2026": 535 - (127 + 113) + (258)}
held = {"31.12.2023": 156490, "31.12.2024": 141714, "31.12.2025": 186696, "30.6.2025": 131460, "30.6.2026": 203167}
print("  loans held for sale / monthly TTM originations (months):", {k: round(held[k] / (orig[k] * 1000 / 12), 2) for k in held})
print(f"  equity less intangibles: 31.12.2025 {82198 - 7307:,} (company's covenant figure 82M, fy2025 p.68);"
      f" 30.6.2026 {86912 - 8269:,} (company 76M, h1_2026 p.18)")
cap_h1 = 28 + 1902 + 92
print(f"  H1 2026 capex (PP&E 28 + development 1,902 + capitalised SBP 92) {cap_h1:,}; annualised {2 * cap_h1:,} vs TTM D&A floor 3,278")
print(f"  2025 write-offs 1,680 vs charge 783: x{1680 / 783:.2f}")
id25 = -((131460 + 4233) - (141714 + 1028)) - 2093     # -(change in loan book) - interest received, H1 2025
id26 = -((203167 + 6686) - (186696 + 4797)) - 4761     # same, H1 2026
print(f"  customer-credit line vs -(change in loan book) - interest received: H1 2025 7,868 vs {id25:,} (gap {7868 - id25:,});"
      f" H1 2026 -23,121 vs {id26:,} (gap {-23121 - id26:,})")
```

Output:

```
== 1. Normalisation (framework d2, screen_spec 2.3), lender (equity) basis, g 5%, ROIIC = OE_norm / TE
  A team: other items removed, W = FY21-25 + TTM m_norm 37.52% cyclical False EBIT_norm  22,624 OE  17,421 | EPV 4.36 DCF 5.36 grid 4.41-6.74 (D3 True) | implied g -4.7%
  B team EBIT_adj, W = fiscal years only         m_norm 35.04% cyclical False EBIT_norm  21,131 OE  16,271 | EPV 4.07 DCF 4.95 grid 4.08-6.21 (D3 True) | implied g -3.7%
  C screen_spec 2.3 EBIT_adj, W + TTM            m_norm 37.22% cyclical True  EBIT_norm  14,249 OE  10,972 | EPV 2.72 DCF 3.05 grid 2.59-3.74 (D3 False) | implied g +6.5%
  D screen_spec 2.3 EBIT_adj, fiscal years       m_norm 34.45% cyclical True  EBIT_norm  11,707 OE   9,015 | EPV 2.23 DCF 2.35 grid 2.04-2.83 (D3 False) | implied g +13.6%
  screen_spec 2.3 EBIT_adj by period: {'FY2021': -769, 'FY2022': 7544, 'FY2023': 13272, 'FY2024': 17216, 'FY2025': 23772, 'TTM': 24460}
  shadow Tier B buy price on C: 45% margin 1.68 | with the add-back kept as endogenous (+10): 2.41
== 2. EV basis as framework d3/d4 are written (funding added back; bank credit and leases deducted)
  team EBIT_adj, W + TTM               cyclical False EBIT_norm  30,384 OE_unl  23,396 ROIIC_unl 12.1% | EPV  2.95 DCF  3.37 grid  2.52 to  4.70 (D3 False) | implied g +2.8%
  screen_spec 2.3 EBIT_adj, W + TTM    cyclical True  EBIT_norm  18,537 OE_unl  14,274 ROIIC_unl  7.4% | EPV  0.63 DCF  0.11 grid -0.66 to  0.83 (D3 False) | implied g +15.6%
== 3. Tax: TTM effective 24.51% | H1 2026 24.41% | FY2025 23.49% | 'other' in the FY2025 reconciliation 116 = 0.49% of PBT
  t 24.00%: OE_norm 17,194 EPV 4.31 DCF 5.28 (team 4.36 / 5.36)
  t 24.51%: OE_norm 17,080 EPV 4.28 DCF 5.24 (team 4.36 / 5.36)
== 4. Dilution, instrument by instrument (fy2025 p.108-112, p.123; h1_2026 p.33), treasury method
  at 3.1730: 309,797 dilutive shares = 0.79% (team memo 546,742 = 1.4% at 5.3576, one weighted strike, no RSUs)
  at 5.3576: 805,224 dilutive shares = 2.05% (team memo 546,742 = 1.4% at 5.3576, one weighted strike, no RSUs)
  residual note-17 options 177,225 at an implied strike of 5.89; H1 2026 diluted EPS 0.20 vs basic 0.21 implies >= 40,414,634 diluted shares
== 5. Worst case: Dempster at 30.6.2026 (h1_2026 p.15, p.23, p.31)
  team (85% on every loan and receivable)                     1.10 | L_worst 65.4% | permanent-loss budget 7.6% of NAV
  defaults 30%, SPC/accrued receivables 50%                   0.99 | L_worst 69.0% | permanent-loss budget 7.3% of NAV
  same, less a six-month wind-down at half of TTM opex        0.80 | L_worst 74.7% | permanent-loss budget 6.7% of NAV
  same on amortised cost (no FV step-up), less wind-down      0.60 | L_worst 81.2% | permanent-loss budget 6.2% of NAV
== 6. Covenants (fy2025 p.99 note 11a(6); h1_2026 p.18, p.33)
  NI >= 1M breaks after a pre-tax fall of 23,161 (94.7% of TTM); TE-ratio 20% after a loss of 42,385 (team); TE >= 25M after 53,643
  origination-driven revenue TTM 45,617 vs opex TTM 28,857; with opex flat the NI covenant is reached at an origination fall of 50.8%
== 7. F4: +2 points through the warehouse, the held book's fair value and the sale price (fy2025 p.42, p.51; h1_2026 p.9, p.10)
  held-book duration 0.60y: one-off FV loss 2,438; sale-price compression 7,742/yr until repriced; warehouse 2,304; first-year pre-tax hit 12,484 (51% of TTM; team 2,304)
  held-book duration 1.17y: one-off FV loss 4,741; sale-price compression 7,742/yr until repriced; warehouse 2,304; first-year pre-tax hit 14,787 (60% of TTM; team 2,304)
  if the annual parts were never repriced: lender EPV 2.40 (team stress 3.91)
== 8. Credit: amortised-cost book (fy2023 p.95; fy2024 p.95; fy2025 p.95), arrears (fy2025 p.66; h1_2026 p.15)
  coverage: {'2022': '46.3%', '2023': '39.2%', '2024': '64.0%', '2025': '16.3%'} | write-offs: {'2023': 0, '2024': 833, '2025': 1680}
  defaults 1,481 -> 4,395 (x2.97); 1-90 days 3,590 -> 5,198 (+45%); arrears/book 2.65% -> 4.57%; H1 2026 charge 670
  IF the defaulted loans sit in the amortised-cost book at 50% coverage: provision 4,395 vs at most 1,604 -> shortfall 2,791 (11% of TTM pre-tax) [UNVERIFIED]
  IF the defaulted loans sit in the amortised-cost book at 70% coverage: provision 10,255 vs at most 1,604 -> shortfall 8,651 (35% of TTM pre-tax) [UNVERIFIED]
  f3 Wells Fargo stress: defaults on the 209,853 on-balance-sheet book at 60% severity that take pre-tax to zero 19.4%; to the NI covenant 18.4%
== 9. Capitalised development (fy2023 p.98, p.110; fy2025 p.98, p.114; h1_2026 p.23, p.28)
  net capitalisation (additions - amortisation): {'FY2021': 2021, 'FY2022': 2250, 'FY2023': 2666, 'FY2024': 983, 'FY2025': -613, 'H1_2025': -163, 'H1_2026': 962, 'TTM': 512}
  H1 pre-tax growth: reported +6.7%; before net capitalisation -4.2%
  capitalised share of gross R&D: H1 2025 14%, H1 2026 34%
  FV step-up growth inside TTM revenue: 1,216 (h1_2026 p.31); with net capitalisation 1,728 = 7.1% of TTM pre-tax
  quarters (revenue, NI), fy2025 p.117 and h1_2026 p.24: {'Q3_2025': (16210, 5013), 'Q4_2025': (15579, 5168), 'Q1_2026': (14440, 4100), 'Q2_2026': (14072, 4185)} | H1 2026 annualised pre-tax 21,920 vs EBIT_norm 22,624
== 10. Identities, inventory test, covenant equity, capex run-rate (fy2024 p.42; fy2025 p.45, p.82, p.113; h1_2026 p.5, p.23, p.24, p.28)
  balance sheet 30.6.2026: liabilities + equity 231,943 vs assets 231,943; H1 2026 cash flow -1,061 -> closing cash 4,877 (filed 4,877)
  NI / basic EPS: FY2025 38,697,872 vs weighted 38,723,775 (fy2025 p.113); H1 2026 39,452,381 vs 39,330,034
  loans held for sale / monthly TTM originations (months): {'31.12.2023': 5.14, '31.12.2024': 4.37, '31.12.2025': 4.19, '30.6.2025': 3.43, '30.6.2026': 4.41}
  equity less intangibles: 31.12.2025 74,891 (company's covenant figure 82M, fy2025 p.68); 30.6.2026 78,643 (company 76M, h1_2026 p.18)
  H1 2026 capex (PP&E 28 + development 1,902 + capitalised SBP 92) 2,022; annualised 4,044 vs TTM D&A floor 3,278
  2025 write-offs 1,680 vs charge 783: x2.15
  customer-credit line vs -(change in loan book) - interest received: H1 2025 7,868 vs 4,956 (gap 2,912); H1 2026 -23,121 vs -23,121 (gap 0)
```
