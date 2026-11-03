# Red team: accounting, data and valuation mechanics — Gilat Telecom Global (TASE 1080597)

Prepared 3.11.2026 as charter step 8 (red team), lens: checklist C1-C7, D1-D8, F3, F4. The charter text in force is
`constitution_zip/charter_rev4_draft.md` ("Text to paste"), with `framework.md` (d) and `checklist.md`.
Reviewed: `research/gilat_telecom/valuation.py`, `output.txt`, `work/gilat_telecom/valuation_notes.md`.
Every number below comes from the recalculation script in the appendix (it imports the team's `valuation.py`
read-only and `lib/charter_valuation.py`); its output is reproduced verbatim. Page numbers are PDF page indexes.

## Bottom line

- **The filed inputs check out.** Every statement figure I re-opened as a page image matches `valuation.py`
  (list below). The TTM build reproduces Mega. The identities (C7) pass on the consolidated statements.
- **The mechanics do not all follow the charter.** The largest departure: the cyclical normalisation adds the TTM as
  a sixth "window" observation, so H2 2025 counts twice. On the charter's window (fiscal years) the base is
  **0.520 ILS, not 0.789**; the shadow buy line is **0.208, not 0.316**; probability-weighted **0.640, not 0.828**.
- **F4 (VETO) is missing from the checklist record and fails.** "No CPI-linked debt" omits ~ILS 224M of half
  CPI-linked Bezeq commitments; the balance-sheet FX exposure is left out of the stress.
- **E1's printed evidence is the wrong test** (cash and Dempster against undiscounted ten-year commitments). A
  dated cash runway still fails E1, so the verdict holds, but the evidence must be replaced.
- **Nothing here overturns NO_THESIS.** B3, D2, E3, H4 and H5 fail on their own. Every correction moves value down,
  except the lease-interest split, which only moves interest cover.

## Pages re-opened as images (figures confirmed)

| Document | Pages | What was confirmed |
|---|---|---|
| gilat_q2_2026_full | 30-32, 38-39, 46-49 | balance sheet 30.6.2026 / 30.6.2025 / 31.12.2025; P&L; cash flow; segment note; revenue note; events after the date (conversions) |
| gilat_fy2025 | 106-107, 125-127, 131-132, 147, 152-153, 183 | linkage table 31.12.2025; BS, P&L, CF 2023-2025; receivables note; IRU note 9 and addendum note 22 |
| gilat_fy2023 | 118, 122-123 | P&L and CF 2021-2023 (EBIT, NI, OCF, SBC, capex, lease principal and interest, interest paid) |
| gilat_h1_2026 | 12, 19, 24 | directors' report segment table; linkage table 30.6.2026 and forwards; Series D terms |

Text layer only (no figure relied on without an identity): gilat_fy2025 p.35, 96, 99, 123-124, 150-151, 160,
163-166, 172-173, 177; gilat_h1_2026 p.5, 14, 18; gilat_fy2024 p.119; gilat_q2_2026_full p.40-45.

## Objections

### O1 (high). The base EBIT_norm is not the charter's normalised earnings — D1, D2, D5, H5

- **Claim.** framework.md d2 defines the cyclical window W as fiscal years: "in Israel ... W is FY2020 to the latest
  year, at most six years". `valuation.py` line 355 feeds `normalised_ebit()` five fiscal years **plus the TTM to
  30.6.2026**. H2 2025 (EBIT 20,139 ILS k, gilat_q2_2026_full p.32) therefore sits in both the FY2025 and the TTM
  observation, and the war-peak H1 2026 is added on top. FY2020, which the charter's W includes, was not obtained.
- **Effect (R1).** On fiscal years FY2021-FY2025, EBIT_norm is 6,876, not 11,100 (−38%). Base value per share is
  0.5203, not 0.7888: the team's base is 52% above the charter formula. Price/base becomes 3.18, not 2.10. The shadow
  buy price is 0.2081, not 0.3155. The conservative case is 0.0862 and the probability-weighted value 0.6400.
- **Why it matters although the verdict stands.** The base and the dated buy line are the numbers the fund carries
  into the re-examination triggers. A later re-run that clears E1 would be priced against a line half again too high.
- **Required change.**
  - Make the fiscal-year EBIT_norm (`norm5`) the BASE. Show the TTM-augmented figure as a sensitivity only.
  - Re-run every downstream figure.
  - Obtain FY2020 (comparatives in the FY2021 annual report, on Maya or the company site) so that W = FY2020-FY2025.
    Otherwise record W as five years and say why.

### O2 (medium). F4 is unrecorded and fails; the currency and CPI facts are incomplete — F4, D1, C1

- **The record.** F4 is a VETO for every lane except E. It appears in neither the pass/fail lists of `output.txt` §7
  nor `valuation_notes.md` §13.
- **Currency.** The team's own stress cuts the base 61% (0.306) for USD/ILS +10%. That stress uses a hedge-size proxy
  and ignores the balance sheet. The filed linkage table at 30.6.2026 (gilat_h1_2026 p.19) shows:
  - USD liabilities of 90,430 against USD monetary assets of 24,967 (ILS k);
  - 91% of current leases and suppliers in USD, against 21% of customers.

  With the remeasurement, +10% gives a base of 0.2156 (0.2733 if the forwards on the remaining USD 22M, whose
  strike is undisclosed, gain fully). +20% gives zero. USD/ILS moved −18.3% from 31.12.2024 to 30.6.2026
  (gilat_q2_2026_full p.43; R3), so a 20% reversal is within the range already seen.
- **CPI.** The line "high CPI: no CPI-linked debt" is wrong in substance:
  - the Bezeq IRU instalments and the 4% O&M fee carry 50% CPI linkage (gilat_fy2025 p.153);
  - the addendum consideration is stated as CPI-linked (p.183).

  CPI of 5% instead of 2% adds 17,637 ILS k pre-tax of PV to the committed IRU cash, or 0.113 ILS/share after tax (R5).
- **Required change.**
  - Record F4 = FAIL.
  - Replace the proxy with the filed linkage table, covering both the flow and the remeasurement, at +10% and +20%.
  - Add the CPI stress on the IRU commitments.
  - Reword the CPI line to "no CPI-linked financial debt; about ILS 224M of half-CPI-linked IRU commitments
    (UNVERIFIED balance)".

### O3 (medium). E1's printed evidence is the wrong test; a dated runway still fails E1 — E1, C1, C3

- **What is printed.** `output.txt` §5 prints marker (2) as "cash 86,855 against unpaid IRU 223,595" and marker (3)
  as "Dempster 11,095 vs IRU commitments 223,595 -> yes". Three things are wrong with this:
  - Both compare a balance on one date with **undiscounted ten-year commitments**.
  - 106,262 of those commitments (UNVERIFIED) pays for lines already earning revenue.
  - The worst case itself uses a PV of only the unfilled lines (135,760), so the two are inconsistent.

  Neither printed comparison is a charter marker, which must be filed. The FY2025 auditor's report is unqualified,
  with one key audit matter on contract revenue and no going-concern emphasis (gilat_fy2025 p.123-124). The Q2 2026
  directors' report states no warning signs at 30.6.2026 (gilat_h1_2026 p.14).
- **The runway (R4).** On a ten-instalment schedule with 5% vendor interest (gilat_fy2025 p.153, p.183; UNVERIFIED
  terms):
  - committed IRU cash rises to 30.0M (2027), 38.0M (2028) and 39.1M (2029), in ILS;
  - with today's ISP cash margin (12.1M a year, from the H1 2026 segment result plus IRU amortisation,
    gilat_q2_2026_full p.46) and a pre-war or zero core, cash falls below two months' costs in 2028 and below zero
    in 2029;
  - with the FY2023-25 core it falls below zero in 2031;
  - in every case new money is needed while the Series D still amortises 25% a year in 2028-2031 (gilat_h1_2026
    p.24).

  Marker (1) is therefore reachable, and E1 fails on correct evidence. The worst-case value of 0.000 rests on two
  UNVERIFIED inputs: the unpaid balance, and whether pulse-1 tranches can be declined (p.183 "assuming full
  exercise"). The filed 2025 payments (13,752) run ahead of the modelled 7,079.
- **Required change.** Replace the marker (2)/(3) lines with the runway, computed in code. Cite marker (1) with the
  year new money is needed. Label the instalment schedule UNVERIFIED.

### O4 (medium). The equity bridge is not at the valuation-date rate — D1, D7, F4, C7

- **The mismatch.** The bridge uses 30.6.2026 balances translated at 2.978 but is dated 3.11.2026 at 3.157 (+6.0%).
  "A rate carries its date."
- **Effect (R2).** Net USD monetary liabilities are 65,463 ILS k (USD 22.0M) at 30.6.2026 (gilat_h1_2026 p.19). At
  3.157 they are 3,935 ILS k larger, and the base falls from 0.7888 to 0.7570 (−4.0%). With O1 as well the base is
  0.4876. The 2026-27 forwards partly offset this, but their mark-to-market is not disclosed (no derivative line on
  gilat_q2_2026_full p.30-31).
- **The linkage table itself does not foot** on the asset side:
  - the cash row reads 84,007 + 8,984 = 92,991 against 92,955;
  - the printed column totals are 138,321 and 25,110, against rows summing to 138,235 and 24,967.
- **Required change.** Restate the USD monetary items in the bridge at 3.157, or present the 30.6.2026-rate figure
  as dated 30.6.2026. Record the footing errors as a C7 flag and use the row figures.

### O5 (low). C4's build-up clause and B5 have evidence the team did not record — C4, B5, C7

- **Receivables.** Gross customers rose 27.7% in FY2025 against revenue +8.9%. The company's own customer days went
  from 62 to 69 (gilat_fy2025 p.147). The allowance is 6,767 USD k, 29% of gross. The 30.6-to-30.6 comparison is
  benign (−2.5% against revenue +12.7%).
- **Deferred IRU asset.** It grew from 0 (31.12.2024) to USD 2,823k (31.12.2025, p.152) to ILS 16,229k (30.6.2026).
  TTM cash paid was 13,714 against a charge of 6,955 (gilat_q2_2026_full p.38).
- **The policy cannot be reconciled with the charge.** The stated policy amortises paid amounts plus capitalised
  vendor interest over 25 years, including two unexercised 5-year options (p.153). The charge is 27.7% of cost in
  year one and 14.9% of cumulative cost in H1 2026, which implies a life of about 3.4 years. The company's FY2025
  EBITDA of USD 23,893 (gilat_fy2025 p.96) equals EBIT + D&A + IRU amortisation within 26 (R10): the headline adds
  back the IRU charge while the USD 3,902 of payments sit in working capital (p.131).
- **Revenue recognition** of new and modified contracts is the auditor's key audit matter (p.123).
- **Required change.** Record C4 as failing on the build-up clause as well as the cash ratio. Record B5 as FAIL with
  this evidence, rather than "open".

### O6 (low). The ILS restatement's lease-interest split is used unquestioned — C6, C4, C7

- The FY2025 ILS cash flow shows 24.6% of lease cash as interest (9,584). The audited USD statement shows 15.8%
  (1,788 of 11,309, gilat_fy2025 p.132). The implied H2 2025 share is 31.3%.
- **Effect (R6).** On the audited split, TTM lease interest is 4,524, not 7,950, and interest cover is 4.4x, not 3.0x.
  The team calls the higher figure "conservative", but it misstates interest cover and the C4 cash proxy.
- **Required change.** Use the audited split, or carry both figures and flag the restatement.

### O7 (low). C6 is missing from the checklist record — C6

C6 is a FLAG for every lane except E. EBIT over interest paid is −1.1x in FY2021 and −0.9x in FY2022, the designated
stress year (gilat_fy2023 p.118, p.123). FY2020 is not in the documents. **Required change:** record C6 = no, with
these figures and a written explanation.

### O8 (low). Lane C base, method spread and the tangible-book basis — D1, D2, H2

- **Lane C has no EPV base.** For Lane C the charter's value bases are NCAV, Dempster or private-owner value.
  Price/NCAV is 5.16 and price/Dempster 17.6. EPV against NCAV is 146% apart.
- **The "19% spread" mixes dates and assets.**
  - Tangible book is taken on 30.6.2026 equity and shares (0.940), while EPV uses 3.11.2026 shares and pro forma cash.
  - On the 3.11.2026 basis tangible book is 0.920.
  - Without the IRU prepayments (16,229) and the DTA (2,403) it is 0.765 (R9).
- **Required change.**
  - State the spread against the asset methods of the declared lane.
  - Put tangible book on the 3.11.2026 basis.
  - Say in the re-examination step that the only charter Tier C line is 0.092 (net-net), and that the shadow 0.316
    (or 0.208 after O1) must not be used as a dated buy price.

### O9 (low). The TTM ROTC uses end-of-period capital — tier evidence (A3 binds A/B/D)

ROU fell from 71,085 to 43,241 over the TTM. On average capital the TTM ROTC is 42.9%, not 51.0%; adding the
long-term IRU prepayment, which is tangible operating capital, gives 39.1% (R8). The median of 17.5% is unchanged, so
the tier conclusion holds. **Required change:** use average capital and include the IRU prepayment.

### O10 (low). One-offs and non-operating items left in the TTM — C5, D1, E1

- **The supplier credit.** The estimate assigns the whole Q4 2025 gross-margin spike to the Intelsat credit.
  gilat_fy2025 p.96 names three causes: high-margin government deals, the IRU, and the credit.
- **The Intelsat agreement** (p.160) provides "one-off credits" in the plural, and future purchase commitments of an
  undisclosed amount:
  - any 2026 credit inside H1 2026 is not removed;
  - the commitment is outside the "net cash" and E1 analyses.
- **FX gains.** About 5,080 ILS k pre-tax of H1 2026 FX gains on USD liabilities remain inside NI_norm_ttm (only the
  cash line was removed; R12). This affects Graham and the d1 TTM figure, not EPV.
- **Required change.** Label the credit estimate as an upper bound. List the Intelsat commitment as UNVERIFIED in E1
  and C1. Strip the FX on non-cash items from NI_norm_ttm.

### O11 (low). Two versions of the same comparative segment results — C7, F3

The H1 2025 segment results are 24,863 in the directors' report (gilat_h1_2026 p.12) and 30,777 in the
financial-statement note (gilat_q2_2026_full p.46), a gap of 5,914 (R11). The analyst's reference-only segment
normalisation (1.237) must say which source it uses. Only the note reconciles to pre-tax profit.
**Required change:** cite the FS note and flag the directors' report table.

## Checked and agreed (no objection)

- **Market inputs.** Price 1.653 (close 3.11.2026), 120,417,631 listed shares, Series D par 26,337,927
  (29,134,661 at 19.8.2026, gilat_h1_2026 p.24, less 2,796,734 later conversions). The June buyback of 2,300,000
  shares at 260.36 agorot (gilat_q2_2026_full p.41). The options per gilat_fy2025 p.166, p.172.
- **Identities and the TTM.** The TTM build equals Mega (EBIT 39,534; NI 32,985; OCF 80,967). The 30.6.2026 identities
  pass.
- **Series D.** The min(as converted, at par) rule for shareholders is correct.
- **Window inputs.** Every FY2021-FY2025 window figure matches its page.
- **Restricted cash and IFRS 16.** Restricted cash is excluded. The lease treatment (EBIT after ROU depreciation, with
  the lease liability deducted) is no more generous than charging lease payments as opex: R0 reproduces the team.
- **No NCI, no preferred, no bank debt** (gilat_q2_2026_full p.31-32).
- **Data flags and margin** are applied as `required_margin` requires (cap +10).
- **Implied growth** is on a fully diluted basis consistent with the bridge.
- **The sensitivity grid** is computed as D3 asks (n/a for C).
- **D8 open** (Q3 2026 not yet filed; Maya unreachable) is the right call.

## UNVERIFIED / could not verify here

- FY2020 figures (outside the supplied documents).
- The IRU payment schedule and vendor rate for the addendum.
- Whether pulse-1 tranches can be declined.
- The strike and mark-to-market of the 2026-27 forwards.
- The amount of the Intelsat purchase commitment.
- The split of H1 2026 finance income.
- The ISP cash margin (segment result plus amortisation) as a proxy for the stalled-ISP case.

## Appendix A — recalculation script (run with python3; imports the team's model read-only)

```python
"""Red-team (accounting/data/valuation mechanics) recalculations for Gilat Telecom, 3.11.2026.
Imports the team's valuation.py read-only (its inputs and helpers) and lib/charter_valuation.py.
Every new input carries its source: document id + PDF page (p.N = PDF page index)."""
import importlib.util, statistics

VAL = "/home/user/value-investing-fund---selected-company-reaserch/research/gilat_telecom/valuation.py"
spec = importlib.util.spec_from_file_location("gv", VAL)
gv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gv)          # runs the team's model; prints nothing unless __main__
from charter_valuation import (unlevered_owner_earnings, epv_operations, equity_bridge, required_margin,
                               normalised_ebit, dcf_operations)

P = print
def ps(eq):  # per-share value with the team's Series D / option logic
    return gv.per_share(eq)[0]

P("== R0. Team figures reproduced")
P(f"  base {gv.v_base:.4f}  cons {gv.v_cons:.4f}  opt {gv.v_opt:.4f}  worst {gv.v_worst:.4f}  pw {gv.v_pw:.4f}  buy {gv.BUY:.4f}")
P(f"  EBIT_norm base (FY21-25 + TTM) {gv.EBIT_NORM:,.0f}; fiscal-years-only {gv.EBIT_NORM_CONS:,.0f}")

# ---------------------------------------------------------------- R1. charter d2 window = fiscal years
P("\n== R1. d2 window: W = fiscal years (charter: 'FY2020 to the latest year'); TTM is not a W observation")
oe_fy = unlevered_owner_earnings(gv.EBIT_NORM_CONS, gv.AMORT_ACQ, gv.TAX, gv.DEP_TTM, gv.MAINT_TTM)
v_fy = ps(gv.equity_value(oe_fy))
m = required_margin("C", gv.DATA_FLAGS)
P(f"  EBIT_norm FY2021-25 {gv.EBIT_NORM_CONS:,.0f} (vs {gv.EBIT_NORM:,.0f}: {gv.EBIT_NORM_CONS/gv.EBIT_NORM-1:+.0%}); OE {oe_fy:,.0f}")
P(f"  base per share {v_fy:.4f} (team {gv.v_base:.4f}, {v_fy/gv.v_base-1:+.0%}); shadow buy {v_fy*m.buy_fraction:.4f} (team {gv.BUY:.4f})")
P(f"  price/base {gv.PRICE/v_fy:.2f} (team {gv.PRICE/gv.v_base:.2f})")
# how much of the six-observation mean is H2 2025 counted twice
h2_25_ebit = gv.EBIT_ILS['FY25'] - gv.EBIT_ILS['H1_25']
P(f"  H2 2025 EBIT {h2_25_ebit:,.0f} ILS k sits in both the FY2025 and the TTM observation")
dead_half = gv.DEAD_CONS
v_fy_cons = ps(gv.equity_value(oe_fy, dead_cost=dead_half))
pw_fy = 0.10*gv.v_worst + 0.25*v_fy_cons + 0.45*v_fy + 0.20*gv.v_opt
P(f"  with W = fiscal years: conservative {v_fy_cons:.4f}; probability-weighted {pw_fy:.4f} (team {gv.v_pw:.4f})")

# ---------------------------------------------------------------- R2. bridge at the valuation-date FX rate
P("\n== R2. Equity bridge at the 3.11.2026 rate: USD monetary items at 30.6.2026 (gilat_h1_2026 p.19)")
usd_assets_rows = 8_984 + 13_023 + 2_960          # cash, customers, other receivables (rows)
usd_assets_printed = 25_110                         # printed column total (does not foot to its rows)
usd_liab = 24_275 + 60_188 + 3_347 + 116 + 2_504    # current leases, suppliers, payables, tax, LT leases (= printed 90,430)
net_usd = usd_liab - usd_assets_rows
fx_adj = net_usd * (gv.FX / gv.FX_30JUN26 - 1)
P(f"  USD assets rows {usd_assets_rows:,} (printed total {usd_assets_printed:,}: column does not foot, diff {usd_assets_printed-usd_assets_rows:,}); USD liabilities {usd_liab:,}")
P(f"  net USD monetary liabilities {net_usd:,} ILS k at {gv.FX_30JUN26} = USD {net_usd/gv.FX_30JUN26/1000:,.1f}M; at {gv.FX}: +{fx_adj:,.0f} ILS k")
v_fx = ps(gv.equity_value(gv.OE_NORM, dead_cost=fx_adj))
v_fx_fy = ps(gv.equity_value(oe_fy, dead_cost=fx_adj))
P(f"  base {gv.v_base:.4f} -> {v_fx:.4f} ({v_fx/gv.v_base-1:+.1%}); with R1 as well {v_fx_fy:.4f}")
share_usd_cl = (24_275 + 60_188) / (26_232 + 66_532)
share_usd_cust = 13_023 / 63_411
P(f"  currency of trade items: {share_usd_cl:.0%} of current leases + suppliers in USD; {share_usd_cust:.0%} of customers in USD")

# ---------------------------------------------------------------- R3. F4 stresses with the filed exposure
P("\n== R3. F4: USD/ILS +10% and +20% on base (team flow proxy USD 24M/yr = the company's own hedge size, gilat_h1_2026 p.19)")
move = (1 - 0.1253) * (gv.FX_30JUN26 / gv.FX_31DEC25) - 1          # USD/ILS -12.53% in 2025, then 3.19 -> 2.978 (gilat_q2_2026_full p.43)
P(f"  recent move: 31.12.2024 -> 30.6.2026 USD/ILS {move:+.1%} (so a 20% reversal is within the observed range)")
for shock in (0.10, 0.20):
    flow = shock * gv.USD_COST_PROXY * gv.FX
    bs = net_usd * gv.FX / gv.FX_30JUN26 * shock
    oe_s = unlevered_owner_earnings(gv.EBIT_NORM - flow, gv.AMORT_ACQ, gv.TAX, gv.DEP_TTM, gv.MAINT_TTM)
    v_s = ps(gv.equity_value(oe_s, dead_cost=fx_adj + bs))
    P(f"  +{shock:.0%}: flow -{flow:,.0f}/yr pre-tax; balance-sheet remeasurement -{bs:,.0f} one-off -> base {v_s:.4f}"
      f" ({v_s/gv.v_base-1:+.0%}); EBIT_norm after flow {gv.EBIT_NORM-flow:,.0f}")
    hedge = shock * (4_000 + 12 * 1_500) * gv.FX          # forwards left at 3.11.2026: USD 2M x Nov-Dec 2026 + 1.5M x 12 (2027), strike undisclosed
    v_h = ps(gv.equity_value(oe_s, dead_cost=fx_adj + bs - hedge))
    P(f"        if the remaining forwards (USD 22M notional) gain fully: +{hedge:,.0f} -> {v_h:.4f} (team F4 {gv.v_fx_up:.4f} has neither the remeasurement nor R2)")

# ---------------------------------------------------------------- R4. IRU cash schedule and E1 runway
P("\n== R4. E1 tested as a dated cash runway (not cash vs. undiscounted ten-year commitments)")
# tranches (start as year fraction, consideration ILS k): gilat_fy2025 p.152-153 (IRU-1), p.183 (IRU-2 pulse 1)
T = [(2025.00, 39_120)]                                             # IRU-1 pulse 1, 8,000 lines
T += [(2025.25 + 0.25*i, 24_450/4) for i in range(4)]               # pulse 2, 4 tranches 1.4.2025-1.1.2026
T += [(2026.25 + 0.25*i, 24_450/4) for i in range(4)]               # pulse 3, 4 tranches 1.4.2026-1.1.2027
T += [(2025.92 + 0.25*i, 160_000/12) for i in range(12)]            # IRU-2 pulse 1, 12 quarterly tranches from 12.2025
assert abs(sum(c for _, c in T) - gv.IRU_COMMITTED) < 1
VR, OM, N, LIFE = gv.IRU_VENDOR_RATE, gv.IRU_OM_RATE, gv.IRU_INSTALMENTS, gv.IRU_TERM
def schedule(cpi=0.0, link=0.5, om_from=2026.5):
    """Calendar-year cash: 10 annual instalments from each tranche start with vendor interest on the unpaid
    balance (pv_iru_line terms), plus 4% O&M on tranches starting after om_from (O&M on earlier tranches is
    already inside the TTM cost base). link x CPI escalation on both (gilat_fy2025 p.153: '50% of CPI differences')."""
    out = {}
    for start, c in T:
        for k in range(N):
            t = start + k
            amt = c / N + (VR * c * (1 - k / N) if k > 0 else 0.0)
            amt *= (1 + link * cpi) ** (t - 2026.5)
            out[int(t)] = out.get(int(t), 0.0) + amt
        if start > om_from:
            for q in range(LIFE * 4):
                t = start + q / 4
                out[int(t)] = out.get(int(t), 0.0) + OM * c / 4 * (1 + link * cpi) ** (t - 2026.5)
    return out
sch = schedule()
P("  committed IRU cash by year (principal + vendor interest; O&M only on tranches from 7.2026), ILS k:")
P("    " + "  ".join(f"{y}:{sch.get(y,0):,.0f}" for y in range(2025, 2037)))
P(f"  modelled 2025 + H1 2026 principal+interest vs filed payments to 30.6.2026 ({gv.IRU_PAID_TO_30JUN:,}): "
  f"{sch.get(2025,0):,.0f} in 2025 vs filed 13,752 (gilat_q2_2026_full p.38): the filed payments run ahead of the ten-instalment schedule (UNVERIFIED terms)")
# ISP cash margin before IRU principal/interest, today's lines: H1 2026 segment result + segment D&A (= IRU amortisation)
isp_cash = 2 * (2_613 + 3_449)                       # gilat_q2_2026_full p.46 (segment note), annualised
pre_war = statistics.mean([gv.cash_oe[2021], gv.cash_oe[2022]]) * gv.FX       # team cash proxy, USD k -> ILS k
mid = statistics.mean([gv.cash_oe[2023], gv.cash_oe[2024], gv.cash_oe[2025] + 3_902]) * gv.FX   # FY2025 IRU paid added back (gilat_fy2025 p.131)
sd_par = gv.SERIES_D_PAR / 1000
def runway(core):
    cash, par, rows = gv.CASH_PF, sd_par, []
    for y in range(2027, 2037):
        coupon = 0.055 * par
        principal = sd_par / 4 if 2028 <= y <= 2031 else 0.0
        par -= principal
        cash += core + isp_cash - sch.get(y, 0.0) - coupon - principal
        rows.append((y, cash))
    return rows
for label, core in (("pre-war core (FY2021-22 cash proxy)", pre_war), ("core = 0", 0.0), ("FY2023-25 core ex-IRU", mid)):
    rows = runway(core)
    neg = next((y for y, c in rows if c < 0), None)
    floor = next((y for y, c in rows if c < gv.CASH_OPEX_TTM / 6), None)
    P(f"  {label:<38} core {core:>8,.0f}/yr + ISP {isp_cash:,}/yr: cash below 2 months' costs in {floor}, below zero in {neg}; "
      f"cash end-2028 {dict(rows)[2028]:,.0f}")
P("  -> marker (1) (maturity -> new money -> dilution) is reachable in the pre-war case within the Series D life; markers (2)/(3) as printed")
P(f"     compare cash {gv.CASH_PF:,.0f} or Dempster {gv.DEMPSTER:,.0f} with undiscounted ten-year commitments {gv.IRU_UNPAID_ALL:,.0f}, of which")
P(f"     {gv.IRU_UNPAID_IN_SERVICE:,.0f} buys lines already earning revenue: neither is the charter's filed marker")

# CPI stress on the IRU (F4 high CPI): PV at r of the remaining schedule, CPI 2% vs 5% a year, 50% linkage
def pv(s, r=gv.R, t0=2026.84):
    return sum(v / (1 + r) ** max(0.0, (y + 0.5) - t0) for y, v in s.items() if y >= 2027)
d_cpi = pv(schedule(cpi=0.05)) - pv(schedule(cpi=0.02))
P(f"\n== R5. F4 high CPI: IRU instalments and O&M are half CPI-linked (gilat_fy2025 p.153, p.183); PV at r of committed cash from 2027,"
  f" CPI 5% vs 2%: +{d_cpi:,.0f} ILS k pre-tax = {d_cpi*(1-gv.TAX)*1000/gv.SHARES_LISTED:.3f} ILS/share after tax;"
  f" the printout's 'no CPI-linked debt' omits {gv.IRU_UNPAID_ALL:,.0f} of CPI-linked commitments")

# ---------------------------------------------------------------- R6. lease-interest split, interest cover
P("\n== R6. FY2025 lease interest in the ILS restatement (gilat_q2_2026_full p.39) vs audited USD split (gilat_fy2025 p.132)")
ils_total = gv.LEASE_PRIN_ILS['FY25'] + gv.LEASE_INT_ILS['FY25']
ils_int_usd_split = ils_total * gv.LEASE_INT_USD[2025] / (gv.LEASE_INT_USD[2025] + gv.LEASE_PRIN_USD[2025])
h2_share_ils = (gv.LEASE_INT_ILS['FY25'] - gv.LEASE_INT_ILS['H1_25']) / (ils_total - gv.LEASE_PRIN_ILS['H1_25'] - gv.LEASE_INT_ILS['H1_25'])
ttm_int = ils_int_usd_split - gv.LEASE_INT_ILS['H1_25'] + gv.LEASE_INT_ILS['H1_26']
P(f"  interest share of lease cash: USD FY2025 {gv.LEASE_INT_USD[2025]/(gv.LEASE_INT_USD[2025]+gv.LEASE_PRIN_USD[2025]):.1%}; ILS FY2025 {gv.LEASE_INT_ILS['FY25']/ils_total:.1%}; ILS H2 2025 implied {h2_share_ils:.1%}")
P(f"  FY2025 lease interest on the audited split {ils_int_usd_split:,.0f} (vs {gv.LEASE_INT_ILS['FY25']:,}); TTM {ttm_int:,.0f} (vs {gv.LEASE_INT_TTM:,.0f});"
  f" interest cover {gv.EBIT_ADJ_TTM/(ttm_int+gv.BOND_INT_TTM):.1f}x (vs {gv.EBIT_ADJ_TTM/(gv.LEASE_INT_TTM+gv.BOND_INT_TTM):.1f}x)")

# ---------------------------------------------------------------- R7. C6 (FLAG, all lanes except E): stress-year interest cover
P("\n== R7. C6 stress-year cover (FY2022 is a designated stress year; FY2020 not in the documents)")
for y in (2021, 2022):
    P(f"  FY{y}: EBIT {gv.EBIT_USD[y]:,} / (lease interest {gv.LEASE_INT_USD[y]:,} + other interest {gv.OTHER_INT_USD[y]:,}) = {gv.EBIT_USD[y]/(gv.LEASE_INT_USD[y]+gv.OTHER_INT_USD[y]):.1f}x  (gilat_fy2023 p.118, p.123)")

# ---------------------------------------------------------------- R8. ROTC TTM capital basis
P("\n== R8. TTM ROTC on average capital and with the long-term IRU prepayment (tangible operating capital)")
# 30.6.2025 balance sheet, gilat_q2_2026_full p.30-31
ca25, c25, cl25 = 149_039, 66_702, 183_167
std25 = 19_480 + 35_305 + 31_228 + 482 + 145 + 1_234 + 16_071
cap25 = max(0, (ca25 - c25) - (cl25 - std25)) + 16_447 + 71_085
cap26 = gv.cap_ttm
avg_cap = (cap25 + cap26) / 2
avg_iru_lt = (5_776 + gv.DEFERRED_LT) / 2
P(f"  capital 30.6.2025 {cap25:,} (ROU 71,085), 30.6.2026 {cap26:,.0f} (ROU 43,241); TTM ROTC end-capital {gv.rotc['TTM']:.1%},"
  f" average {gv.EBIT_ADJ_TTM/avg_cap:.1%}, average + LT IRU prepayment {gv.EBIT_ADJ_TTM/(avg_cap+avg_iru_lt):.1%}")
vals = [gv.rotc[y] for y in gv.YEARS] + [gv.EBIT_ADJ_TTM / avg_cap]
P(f"  median {statistics.median(vals):.1%} (unchanged tier conclusion)")

# ---------------------------------------------------------------- R9. method spread with the Lane C asset methods
P("\n== R9. Method spread when the Lane C asset methods are included")
ncav_ps = gv.NCAV * 1000 / gv.SHARES_30JUN
dem_ps = gv.DEMPSTER * 1000 / gv.SHARES_30JUN
meths = {"EPV": gv.v_epv, "TBV": gv.v_tbv, "NCAV": ncav_ps}
P(f"  EPV {gv.v_epv:.3f} / NCAV {ncav_ps:.3f} - 1 = {gv.v_epv/ncav_ps-1:.0%}; spread over EPV, TBV, NCAV {max(meths.values())/min(meths.values())-1:.0%}"
  f" (team, earnings methods + TBV: {gv.vr.method_spread():.0%}); price/NCAV {gv.PRICE/ncav_ps:.2f}; price/Dempster {gv.PRICE/dem_ps:.1f}")
# TBV at 3.11.2026 on the same basis as EPV (shares and cash pro forma); conversions after 30.6 from note 8 (gilat_q2_2026_full p.49) and market.md
sd_conv_par = 705_275 + 2_796_734
sd_par_30jun = 29_134_661 + 705_275                  # gilat_h1_2026 p.24 (par at 19.8.2026) + conversions 1.7-19.8
sc_conv = 1_240_026 + 192_435 * 1.35
eq_pf = gv.EQUITY - gv.OCT_BUYBACK + gv.SERIES_D_LIAB * sd_conv_par / sd_par_30jun + gv.SERIES_C_LIAB * sc_conv / (sc_conv + 725_180)
tbv_pf = (eq_pf - gv.INTANGIBLES) * 1000 / gv.SHARES_LISTED
tbv_hard = (eq_pf - gv.INTANGIBLES - gv.DEFERRED_ST - gv.DEFERRED_LT - 2_403) * 1000 / gv.SHARES_LISTED
P(f"  TBV pro forma 3.11.2026 {tbv_pf:.3f} (team 30.6 basis {gv.v_tbv:.3f}); excluding IRU prepayments 16,229 and DTA 2,403: {tbv_hard:.3f}")

# ---------------------------------------------------------------- R10. C4 build-up evidence
P("\n== R10. C4: build-up of receivables and deferred assets (gilat_fy2025 p.125, p.147, p.152; gilat_q2_2026_full p.30)")
gross24, gross25 = 17_995, 22_977
P(f"  gross customers FY2025 {gross25/gross24-1:+.1%} vs revenue {gv.REV_USD[2025]/gv.REV_USD[2024]-1:+.1%}; net {16_210/11_871-1:+.1%}; company customer days 62 -> 69 (p.147);"
  f" allowance 6,767 = {6_767/gross25:.0%} of gross")
ebitda_rebuilt = gv.EBIT_USD[2025] + 13_099 + 1_079     # EBIT + D&A + IRU amortisation, USD k (gilat_fy2025 p.127, p.131)
P(f"  company EBITDA 2025 USD 23,893 (gilat_fy2025 p.96) vs EBIT + D&A + IRU amortisation {ebitda_rebuilt:,}: the headline adds back the IRU charge"
  f" (difference {23_893-ebitda_rebuilt:,}); the IRU payments (USD 3,902) sit in working capital (p.131)")
P(f"  30.6.2026 vs 30.6.2025 customers {63_411/65_046-1:+.1%} vs H1 revenue {139_991/124_234-1:+.1%} (seasonal comparison is benign)")
P(f"  IRU deferred expense: 0 (31.12.2024) -> USD 2,823 (31.12.2025) -> ILS 16,229 (30.6.2026); TTM cash {gv.IRU_PAID_TTM:,} vs charge {gv.IRU_AMORT_TTM:,} (gilat_q2_2026_full p.38);"
  f" stated life 25 years incl. two unexercised 5-year options, vendor interest capitalised (p.153)")
cum_cost = 3_902 * gv.FX_31DEC25 + gv.IRU_PAID_ILS['H1_26']      # cumulative IRU cost in ILS at 30.6.2026 (USD cost at the 31.12.2025 rate)
P(f"  charge vs cost: FY2025 {1_079/3_902:.1%} of cost in year one; H1 2026 {3_449/cum_cost:.1%} of cumulative cost {cum_cost:,.0f} in six months"
  f" -> implied life about {cum_cost/(2*3_449):.1f} years, not 25: the policy and the charge cannot both be right (B5)")

# ---------------------------------------------------------------- R11. single-source checks (C7)
P("\n== R11. C7 single-source checks inside the Q2 2026 filing")
P(f"  H1 2025 segment results: directors' report (gilat_h1_2026 p.12) satellite 23,440 + ISP 1,423 = {23_440+1_423:,};"
  f" financial-statement note (gilat_q2_2026_full p.46) 27,886 + 2,891 = {27_886+2_891:,}; gap {27_886+2_891-23_440-1_423:,}")
P(f"  linkage table (gilat_h1_2026 p.19): cash row 84,007 + 8,984 = {84_007+8_984:,} vs 92,955; asset column totals 138,321 / 25,110 vs rows"
  f" {84_007+3_500+50_388+66+274:,} / {usd_assets_rows:,}; liabilities side foots ({usd_liab:,})")
# ---------------------------------------------------------------- R12. FX left inside TTM pre-tax (affects NI_norm_ttm / Graham only)
usd_noncash_net = 29_314 - (6_219 - 866)                 # USD liabilities - USD non-cash monetary assets, 31.12.2025 (gilat_fy2025 p.106), USD k
fx_gain_h1 = usd_noncash_net * (gv.FX_31DEC25 - gv.FX_30JUN26)
P(f"\n== R12. FX in H1 2026 finance items (ILS functional): USD liabilities less USD non-cash monetary assets at 1.1.2026 USD {usd_noncash_net:,}k"
  f" x (3.19 - 2.978) = gain ~{fx_gain_h1:,.0f} ILS k pre-tax, ~{fx_gain_h1*(1-gv.TAX):,.0f} after tax, left inside NI_norm_ttm {gv.NI_NORM_TTM:,.0f}"
  " (only the cash line was removed); H2 2025 (USD functional) carries FX losses on ILS liabilities in the other direction: net UNVERIFIED")
```

## Appendix B — output of the script (3.11.2026)

```
== R0. Team figures reproduced
  base 0.7888  cons 0.3563  opt 1.9215  worst 0.0000  pw 0.8283  buy 0.3155
  EBIT_norm base (FY21-25 + TTM) 11,100; fiscal-years-only 6,876

== R1. d2 window: W = fiscal years (charter: 'FY2020 to the latest year'); TTM is not a W observation
  EBIT_norm FY2021-25 6,876 (vs 11,100: -38%); OE 7,261
  base per share 0.5203 (team 0.7888, -34%); shadow buy 0.2081 (team 0.3155)
  price/base 3.18 (team 2.10)
  H2 2025 EBIT 20,139 ILS k sits in both the FY2025 and the TTM observation
  with W = fiscal years: conservative 0.0862; probability-weighted 0.6400 (team 0.8283)

== R2. Equity bridge at the 3.11.2026 rate: USD monetary items at 30.6.2026 (gilat_h1_2026 p.19)
  USD assets rows 24,967 (printed total 25,110: column does not foot, diff 143); USD liabilities 90,430
  net USD monetary liabilities 65,463 ILS k at 2.978 = USD 22.0M; at 3.157: +3,935 ILS k
  base 0.7888 -> 0.7570 (-4.0%); with R1 as well 0.4876
  currency of trade items: 91% of current leases + suppliers in USD; 21% of customers in USD

== R3. F4: USD/ILS +10% and +20% on base (team flow proxy USD 24M/yr = the company's own hedge size, gilat_h1_2026 p.19)
  recent move: 31.12.2024 -> 30.6.2026 USD/ILS -18.3% (so a 20% reversal is within the observed range)
  +10%: flow -7,577/yr pre-tax; balance-sheet remeasurement -6,940 one-off -> base 0.2156 (-73%); EBIT_norm after flow 3,524
        if the remaining forwards (USD 22M notional) gain fully: +6,945 -> 0.2733 (team F4 0.3059 has neither the remeasurement nor R2)
  +20%: flow -15,154/yr pre-tax; balance-sheet remeasurement -13,880 one-off -> base 0.0000 (-100%); EBIT_norm after flow -4,053
        if the remaining forwards (USD 22M notional) gain fully: +13,891 -> 0.0000 (team F4 0.3059 has neither the remeasurement nor R2)

== R4. E1 tested as a dated cash runway (not cash vs. undiscounted ten-year commitments)
  committed IRU cash by year (principal + vendor interest; O&M only on tranches from 7.2026), ILS k:
    2025:7,079  2026:18,504  2027:30,023  2028:37,955  2029:39,115  2030:37,875  2031:36,635  2032:35,395  2033:34,155  2034:32,914  2035:24,595  2036:15,931
  modelled 2025 + H1 2026 principal+interest vs filed payments to 30.6.2026 (24,425): 7,079 in 2025 vs filed 13,752 (gilat_q2_2026_full p.38): the filed payments run ahead of the ten-instalment schedule (UNVERIFIED terms)
  pre-war core (FY2021-22 cash proxy)    core  -12,941/yr + ISP 12,124/yr: cash below 2 months' costs in 2028, below zero in 2029; cash end-2028 7,763
  core = 0                               core        0/yr + ISP 12,124/yr: cash below 2 months' costs in 2028, below zero in 2029; cash end-2028 33,644
  FY2023-25 core ex-IRU                  core   10,901/yr + ISP 12,124/yr: cash below 2 months' costs in 2029, below zero in 2031; cash end-2028 55,445
  -> marker (1) (maturity -> new money -> dilution) is reachable in the pre-war case within the Series D life; markers (2)/(3) as printed
     compare cash 86,855 or Dempster 11,095 with undiscounted ten-year commitments 223,595, of which
     106,262 buys lines already earning revenue: neither is the charter's filed marker

== R5. F4 high CPI: IRU instalments and O&M are half CPI-linked (gilat_fy2025 p.153, p.183); PV at r of committed cash from 2027, CPI 5% vs 2%: +17,637 ILS k pre-tax = 0.113 ILS/share after tax; the printout's 'no CPI-linked debt' omits 223,595 of CPI-linked commitments

== R6. FY2025 lease interest in the ILS restatement (gilat_q2_2026_full p.39) vs audited USD split (gilat_fy2025 p.132)
  interest share of lease cash: USD FY2025 15.8%; ILS FY2025 24.6%; ILS H2 2025 implied 31.3%
  FY2025 lease interest on the audited split 6,158 (vs 9,584); TTM 4,524 (vs 7,950); interest cover 4.4x (vs 3.0x)

== R7. C6 stress-year cover (FY2022 is a designated stress year; FY2020 not in the documents)
  FY2021: EBIT -2,731 / (lease interest 1,396 + other interest 1,075) = -1.1x  (gilat_fy2023 p.118, p.123)
  FY2022: EBIT -1,499 / (lease interest 724 + other interest 910) = -0.9x  (gilat_fy2023 p.118, p.123)

== R8. TTM ROTC on average capital and with the long-term IRU prepayment (tangible operating capital)
  capital 30.6.2025 90,647 (ROU 71,085), 30.6.2026 65,776 (ROU 43,241); TTM ROTC end-capital 51.0%, average 42.9%, average + LT IRU prepayment 39.1%
  median 17.5% (unchanged tier conclusion)

== R9. Method spread when the Lane C asset methods are included
  EPV 0.789 / NCAV 0.321 - 1 = 146%; spread over EPV, TBV, NCAV 193% (team, earnings methods + TBV: 19%); price/NCAV 5.16; price/Dempster 17.6
  TBV pro forma 3.11.2026 0.920 (team 30.6 basis 0.940); excluding IRU prepayments 16,229 and DTA 2,403: 0.765

== R10. C4: build-up of receivables and deferred assets (gilat_fy2025 p.125, p.147, p.152; gilat_q2_2026_full p.30)
  gross customers FY2025 +27.7% vs revenue +8.9%; net +36.6%; company customer days 62 -> 69 (p.147); allowance 6,767 = 29% of gross
  company EBITDA 2025 USD 23,893 (gilat_fy2025 p.96) vs EBIT + D&A + IRU amortisation 23,867: the headline adds back the IRU charge (difference 26); the IRU payments (USD 3,902) sit in working capital (p.131)
  30.6.2026 vs 30.6.2025 customers -2.5% vs H1 revenue +12.7% (seasonal comparison is benign)
  IRU deferred expense: 0 (31.12.2024) -> USD 2,823 (31.12.2025) -> ILS 16,229 (30.6.2026); TTM cash 13,714 vs charge 6,955 (gilat_q2_2026_full p.38); stated life 25 years incl. two unexercised 5-year options, vendor interest capitalised (p.153)
  charge vs cost: FY2025 27.7% of cost in year one; H1 2026 14.9% of cumulative cost 23,120 in six months -> implied life about 3.4 years, not 25: the policy and the charge cannot both be right (B5)

== R11. C7 single-source checks inside the Q2 2026 filing
  H1 2025 segment results: directors' report (gilat_h1_2026 p.12) satellite 23,440 + ISP 1,423 = 24,863; financial-statement note (gilat_q2_2026_full p.46) 27,886 + 2,891 = 30,777; gap 5,914
  linkage table (gilat_h1_2026 p.19): cash row 84,007 + 8,984 = 92,991 vs 92,955; asset column totals 138,321 / 25,110 vs rows 138,235 / 24,967; liabilities side foots (90,430)

== R12. FX in H1 2026 finance items (ILS functional): USD liabilities less USD non-cash monetary assets at 1.1.2026 USD 23,961k x (3.19 - 2.978) = gain ~5,080 ILS k pre-tax, ~3,911 after tax, left inside NI_norm_ttm 14,746 (only the cash line was removed); H2 2025 (USD functional) carries FX losses on ILS liabilities in the other direction: net UNVERIFIED
```
