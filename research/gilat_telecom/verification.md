# Gilat Telecom Global (TASE 1080597): verification of the final record

**Record date: 3.11.2026.** The final edit ran on 4.11.2026 against the record as it stood on 3.11.2026. No price, rate or
date was updated, and no old rate was re-dated. Charter Revision 4 ("Text to paste") governs, with `framework.md`, the
constitution's `checklist.md`, `screen_spec.md` and `small_investor_and_israel.md`.

## Outcome

**The verdict is unchanged: NO_THESIS.** No confirmed defect changed the outcome of a decision rule: an investment-test
question, a VETO item's pass or fail, the lane or the price test.
- B7 moved from pass to "cannot assess here" and now fails closed, so one more VETO item fails.
- E7 is a FLAG item; it moved from "no" to "yes".
- WATCHLIST stays excluded: seven VETO items fail at any price.

**What moved.**

| Per share, ILS (3.11.2026) | At the gate | After the final edit | Why |
|---|---|---|---|
| Price | 1.653 | 1.653 | unchanged |
| Worst case | 0.000 | 0.000 | still nil; the unfilled-line PV is now dated (125,093 instead of 135,760) |
| Conservative | 0.000 | 0.000 | still nil (equity before Series D 20,451 against par 26,338) |
| **Base** | 0.4281 | **0.4737** | AR-1 alone gives 0.4602; AR-3 alone 0.4416; both 0.4737 (out §8) |
| Optimistic | 1.7177 | 1.7177 | unchanged (TTM add-back, no IRU expected cost) |
| Probability-weighted (15/30/45/10) | 0.3644 | 0.3849 | follows the base |
| Net-net reference line (not a buy price) | 0.0921 | 0.0921 | relabelled: the 30.6.2026 balance sheet per 3.11.2026 listed share; 0.094 per 30.6.2026 share |
| Price / base | 3.86 | 3.49 | |
| Implied growth, normalised | +16.5% | +15.7% | |
| Sensitivity grid | 0.297-0.523 | 0.336-0.573 | still below the price everywhere |
| Size | 0.0% of NAV | 0.0% of NAV | quarter-Kelly still binds: full Kelly 0% |

**Checklist tallies.**

| | Gate | Now |
|---|---|---|
| VETO (pass / fail / cannot assess) | 15 / 10 / 3 | 14 / 10 / 4 |
| FLAG (pass / fail / cannot assess) | 3 / 6 / 2 | 4 / 5 / 2 |

## What was checked, and by which lens

Three verifiers audited the gate's revisions and the memo independently. Their reports are in the scratchpad at
`verify/gilat_telecom/`: `arithmetic.md`, `charter.md` and `memo-facts.md`.

- **Arithmetic and inputs.**
  - An independent re-derivation of every headline from framework d1-d11, e2 and screen_spec 2.2-2.3.
  - The inputs traced to their filing pages, with page images where a table mattered.
  - A leak check against the pre-gate valuation.
  - Library functions checked against `framework.md`.
- **Charter compliance.**
  - The four questions, the lane, the tier and the margin.
  - The 60 checklist items: type, applicability and fail-closed handling.
  - The verdict category, the falsification conditions, the sell rule and the size.
  - The Israeli rules and the dated rates.
- **Memo facts.**
  - 1,094 numeric tokens in `thesis_he.md` traced to their sources, and 128 table cells matched.
  - 12 load-bearing facts confirmed on filing pages.
  - Every Hebrew sentence checked against the English record, and the section 14 contradictions classified.
- **Final edit (this file).**
  - Each finding confirmed or refuted against the files and the filings. Page images were rendered for gilat_fy2021
    p.146 and gilat_h1_2026 p.8; text pages were read for gilat_fy2021 p.120, p.132-133, p.145, p.152, p.198-199;
    gilat_fy2022 p.148, p.206-207; gilat_fy2023 p.7, p.91, p.141, p.151, p.183, p.193-194; gilat_fy2024 p.8, p.88-90,
    p.155, p.190, p.192, p.199-200; gilat_fy2025 p.32, p.50, p.63, p.72-74, p.81-82, p.90, p.94, p.140, p.150, p.173,
    p.182, p.205, p.207, p.214-215; gilat_h1_2026 p.14-15; and the company-site media list (cio_dl).
  - The confirmed defects fixed and propagated to every file that quotes them; `valuation.py` re-run.
  - Scripts, run with `python3 -I`, are in the scratchpad at `verify/gilat_telecom/fix_tools/`:
    `fix_financials.py` and `library_effects.py` (with `library_effects_out.txt`).

## Findings and dispositions

28 findings: 27 fixed, 1 refuted (CH-3). Two pairs were the same defect, AR-4 = MF-3 and CH-4 = MF-1; both members of
each pair are marked fixed. No finding was deferred.

| ID | Lens | Severity | Disposition | Evidence (one line) |
|---|---|---|---|---|
| AR-1 | arithmetic | high | **fixed** | gilat_fy2021 p.146 (image): the contract backlog (5,698) is amortised 949 in 2020, net nil, in one purchase price allocation with goodwill and customer relations. d1, d3 and the charter add acquired amortisation back. EBIT_norm, the W mean, carried USD 968k a year of it against 809 added back. The d3 add-back is now the W mean, 3,056: base 0.428 → 0.460 (AR-1 alone). C5 still passes; the 949 was mislabelled "endogenous" |
| AR-2 | arithmetic | medium | **fixed** | gilat_fy2021 p.145 (= gilat_fy2022 p.148): FY2021 PP&E depreciation is 3,353 (41,198 → 44,551). The record's 3,729 was a residual of 18,340 − 13,661 − 950 that holds 376 of other amortisation. C4 −38% → −34%; pre-war core −9,807 → −9,214; end-2028 14,029 → 15,216. The years below the floor and below zero (2028, 2029) are unchanged |
| AR-3 | arithmetic | medium | **fixed** | `pv_iru_line` is a PV at delivery. 25,250 of the 26,400 unfilled lines sit in tranches delivered after 3.11.2026, to 9.2028 (`IRU_TRANCHES`). Each PV is now dated to 3.11.2026, and the unused half is the latest delivered (factor 0.876; 0.921 for all lines). Expected cost 13,067 → 11,442; AR-3 alone 0.442 |
| AR-4 | arithmetic | low | **fixed** (relabelled; = MF-3) | 11,095 / 120,417,631 = 0.092 (line) against 11,095 / 118,063,162 = 0.094 (Dempster per share). Kept 0.092, the price at which today's market cap passes the aggregate D2 test, and stated its share basis wherever it is cited; out §4 prints both |
| AR-5 | arithmetic | low | **fixed** | Re-run: the filed remeasurement alone leaves the base at 0.416 (+10%) and 0.358 (+20%), which passes the record's own F4 test; the UNVERIFIED flow proxy carries the failure. Break-even USD 8.9M a year; cross-check gilat_fy2025 p.173 (11,220 + 12,614 + 5,559), p.132 (lease cash 11,309), p.181 (19,655) ≈ USD 21.0M. Now in out §5, gate A-O2, checklist F4 and memo §9-10 |
| CH-1 | charter | high | **fixed** | Constitution checklist: a "don't know" counts as "no". scuttlebutt.md §4 and §9: courts "not accessible", B7 "open on the courts". Gate §8 itself listed B7 as fail-closed. B7 → cannot assess (fails closed), VETO 14/10/4. Gate §8 now separates fail-closed items from reads that gate nothing (F1: no controller; F2: passes on the filings) |
| CH-2 | charter | medium | **fixed** | Constitution checklist "Recording the result": only a watchlist name gets a dated buy price. out §6 already named B3, E3, F4, H4 and H5 as failing at any price, while gate and memo said "not live while H2, B5 and E1 fail". Charter Q1 has no net-net exception. 0.092 is relabelled a reference line, not a buy price; the full list is stated; "except as a net-net" dropped from Q1 |
| CH-3 | charter | medium | **refuted** | The charter ("y10 dated", in the cash flows' currency), framework (b)-3 and e4, and screen_spec ("10-year government yield in the statements' currency") do not define y10 as a single bond's YTM. 4.16% is the dated 3.11.2026 generic 10-year shekel government yield; Shekel 0537 (10.58 years to run) is one bond. r = 10% and Graham fails on either (8.32% or 8.58% required against an EY of 5.4%). The Paymeant study's working copy has since moved to the same generic series (4.162%) |
| CH-4 | charter | low | **fixed** (= MF-1) | D2, D5 and E3 depend on the price; seven VETO items fail at any price |
| CH-5 | charter | low | **fixed** | Charter Q2 for Lane C asks for a firm asset value not burned and a catalyst or a basket; Q3 applies the tier table. The record cited price/NCAV and the D3 grid. Q2 now rests on H2, H4 and H3; Q3 on the Tier C test, with price/EPV as context (gate, out §7, checklist, memo §8) |
| CH-6 | charter | low | **fixed** | E7 asks "Have I checked for the misjudgment tendencies"; the record's own explanation shows the check was run and the fund uses none of management's metrics. E7 → yes; FLAG 4/5/2; management's bias stays under B4/B5 |
| CH-7 | charter | low | **fixed** | Reg. 21A and 22: no controller since 17.2.2021 and no controller transactions in 2021-2025 (gilat_fy2021 p.198-199; gilat_fy2022 p.206-207; gilat_fy2023 p.193-194; gilat_fy2024 p.199-200; gilat_fy2025 p.214-215). Now cited in F2, gate B-O8 and memo §4 |
| CH-8 | charter | low | **fixed** | out §7's trigger 2 lacked the gate's runway test. out §7 now prints gate §3's three conditions; the risk-factor and amortisation item, ISP additions and licences are monitoring triggers in both |
| MF-1 | memo-facts | medium | **fixed** | D2 and D5 are price tests and E3's implied growth moves with the price. Gate, memo §1 and §9, out §6-7 and the checklist now name the seven that fail at any price (B3, B5, E1, F4, H2, H4, H5) |
| MF-2 | memo-facts | low | **fixed** | Memo §1 rows "מחיר קנייה" and "מחיר / מחיר קנייה" and out §6 "buy line ... price/buy price" relabelled as the net-net reference line and price / line |
| MF-3 | memo-facts | low | **fixed** (= AR-4) | Share basis stated in memo §7 and §14 item 3 |
| MF-4 | memo-facts | low | **fixed** | gilat_fy2025 p.182 says "לקוח אחד" and "לקוח שני", with no letters; p.32 calls the government & defence customer "לקוח א'" (19,278). The letters are financials.json's own. Fixed in memo §14 item 1, sources.md and financials.json concentration[7], [8] |
| MF-5 | memo-facts | low | **fixed** | gilat_fy2023 p.7, p.91, p.183 and gilat_fy2024 p.8, p.90, p.190 print 6,134,442 for ILS 1,840,333, and the bridge to 68,629,480 is exact; 6,148,754 appears only in the equity notes. Memo §4 and §14 item 7, sources.md, financials.json (`shares_alt`) |
| MF-6 | memo-facts | low | **fixed** | gilat_fy2025 p.73 §3(c): 5% or more, 10% for an institutional investor, needs the Minister's prior written consent. Memo §4 and §12, gate §7, sources.md |
| MF-7 | memo-facts | low | **fixed** | gilat_h1_2026 p.8 (image): 80.19 against 88.71 (−9.6% y/y), attributed to "a sharp rise in recruiting new customers"; +9.6% against Q1 2026. Memo §2, checklist A7 |
| MF-8 | memo-facts | low | **fixed** | Bizportal 20014148 (saved copy): "about double the normal period" answers a question on the defence activity. The memo, gate, out §7 and checklist E3 quote it and state the ambiguity; out §5 keeps both readings. Price/base is 3.5, so neither reading changes a decision |
| MF-9 | memo-facts | low | **fixed** | gilat_fy2025 p.50 ("סטארלינק משנה את התעשייה באופן קיצוני"), p.90, p.32; gilat_fy2024 p.89 ("קיטון משמעותי של החוב"). "Largest commitment" attributed to governance_risk.md §4.5; Customer A is "an Israeli customer" in the government & defence segment. Quotes are now verbatim in the memo, and the truncated "mainly on price" is also fixed in the checklist, out §7 and gate §5 |
| MF-10 | memo-facts | low | **fixed** | The ~ILS 110M is on gilat_h1_2026 p.14; chapter 27 is gilat_fy2025 p.82-87; 586,737 is on gilat_fy2024 p.192. Fixed in memo §2 and §14, checklist B5, gate B-O1, sources.md and the financials.json ref |
| MF-11 | memo-facts | low | **fixed** | gilat_fy2025 p.63 prints 13.3.2024, p.207 prints 14.3.2024, and the company site has "אסיפה שזומנה ליום 13.3.24 נדחית ליום 14.3.24". Checklist F2, gate B-O8, memo §4 and §11 |
| MF-12 | memo-facts | low | **fixed** | financials.json caveats [0], [4] and [19] marked RESOLVED with evidence; [12] and [20], of the same kind, too |
| MF-13 | memo-facts | low | **fixed** | out §5: the dollar fell 18.3% from 31.12.2024. Memo §2 now dates the weak dollar from 2025 |
| MF-14 | memo-facts | low | **fixed** | Checklist C3: the 1.4.2028 Series D instalment falls inside the 24 months and is covered by cash. Memo §9 now says so |
| MF-15 | memo-facts | low | **fixed** | `thesis_numbers.py` (path made relative) and its output are now in `research/gilat_telecom/`, and the output is identical. The memo header cites market.md §1.3 and repository paths. Committed with the record after the CIO's review |

## Library issues (`lib/charter_valuation.py`; not edited)

| # | Function (lines) | Against | Issue | Effect on Gilat |
|---|---|---|---|---|
| L1 | `is_cyclical` (l.78-86) | framework d2 as made operational in screen_spec 2.3 | Sample `statistics.stdev` instead of the population SD, and `m < 0` instead of EBIT_adj ≤ 0 | None: cyclical on the FY2021-22 losses; sample SD 6.33%, population SD 5.78%, median 5.06% |
| L2 | `dcf_operations` (l.175-212) | framework d4 | The reinvestment charge is dated: year-1 growth is paid at t = 0 and year 10 at gT/ROIIC_T. d4 writes FCF_t = OE_t − g/ROIIC × OE_t for t = 1..10. The docstring documents it, and it keeps ROIIC = r growth value-neutral, as d3 requires | Only the grid's +2% column: 0.573 / 0.474 / 0.403 in the library against 0.587 / 0.487 / 0.410 on the literal d4. The base (g = 0) is unaffected |
| L3 | `implied_growth` (l.251-282) | framework d8 and its own "most generous reading" docstring | With `roiic=None`, g > 0 takes a no-reinvestment path but g ≤ 0 falls through to `dcf_operations`, which charges gT/ROIIC_T in year 10, a step of 0.096 × OE0 at g = 0 | TTM implied growth −1.54% (printed −1.5%) against −1.67% on a consistent path; the normalised +15.7% is unaffected |
| L4 | `required_margin` (l.328-366) | framework d11, the ceiling | The ceiling tests the tier base only and leaves out the endogenous +10, which d11 says is not a data addition. A Tier D name on a B franchise with an endogenous add-back (55%) is not flagged NO_THESIS | None (Tier C) |
| L5 | `ValueRange.buy_price` (l.459-460) | framework d11 Tier C | It always returns base × (1 − margin). For Tier C, d11 sets ≤ 2/3 NCAV and ≤ Dempster for net-nets, or ≤ 50% of private-owner value, so a caller whose base is EPV gets a line the charter does not define | None: the study overrides it in `CioValueRange` |
| L6 | `position_size` (l.415-443) | framework e2, "the smallest of" six limits | The TASE cap is dropped when `tase_room` is None, and the liquidity cap leaves the minimum when `nav` is None: it fails open | None: quarter-Kelly 0% binds and `tase_room` = 0.30 was passed |

## Checks that passed

- **Reproducibility.** `valuation.py` reproduced the committed `output.txt` byte for byte before the edit. After the edit
  it reproduces the new `output.txt` byte for byte (run from the repository root with `python3 -I`).
- **The corrected base, by hand.**
  - OE_unlevered 8,238 = (7,643 + 3,056) × 0.77; EPV 82,382.
  - Equity before Series D: 82,382 + 49,491 − 33,116 − 3,935 − 11,442 = 83,381; base 0.4737 with Series D at par.
  - The new code reproduces the gate's 0.4281 when both corrections are switched off (out §8).
- **Inputs.**
  - The FY2020 inputs match gilat_fy2022 p.119 and p.123-124 and gilat_fy2021 p.114-116 and p.145-146.
  - The FY2020-25 window, the EBIT_adj series and the cyclical test hold; EBIT_norm is 7,643 (the mean binds).
  - The TTM reproduces Mega: operating income 39,534, net income 32,985, OCF 80,967.
  - The 30.6.2026 identities pass.
- **Bridge, scenarios and size.**
  - Bridge: pro forma cash 86,855; excess cash 49,491; leases 33,116; FX restatement 3,935. Series D is treated as debt
    at par unless conversion is worth more. The share count of 120,417,631 reconciles.
  - The worst and conservative cases stay nil, and the optimistic case is unchanged at 1.718.
  - Size is 0% (full Kelly 0); the tier cap is 5% and the loss budget 5%; the liquidity maximum is ILS 4,006,416.
- **Valuation tests.**
  - The net-net test fails: market cap is 5.3x NCAV and 17.9x Dempster. H2 fails: the unpaid Bezeq consideration is
    5.9x NCAV.
  - The Tier C margin is 60%, with no endogenous add-back; no private-owner value is evidenced.
  - Graham's yardstick fails at either ILS y10.
- **F4 and E1.** F4 still fails after the corrections: +10% and +20% give nil, and the break-even flow is USD 8.9M
  against a cross-check of about USD 21.0M. The E1 runway still needs new money by 2029 on the pre-war and zero cores.
- **The checklist.** All 60 items are present, and their types and Lane C applicability match the constitution. The
  tallies were recounted from the table rows by script: VETO 14/10/4 with 12 n/a; FLAG 4/5/2 with 9 n/a (VETO 13/11/4
  after the CIO's review below).
- **The verdict.**
  - NO_THESIS is the right category.
  - WATCHLIST is excluded: seven VETO items fail at any price.
  - TOO_HARD is excluded: without the unverified IRU cost the base is 0.569 (out §5), still far below the price of 1.653.
- **The memo.**
  - Every number quoted in `gate.md`, `checklist.md` and `thesis_he.md` that changed is printed in `output.txt`
    (checked by script).
  - The memo keeps its 15 sections in Hebrew, and section 14 marks each resolved contradiction "תוקן".
- **The record around the verdict.**
  - The 12 load-bearing facts were confirmed on their filing pages (memo-facts lens).
  - The three falsification conditions are specific, observable and dated, and are now worded the same in out §7 and
    gate §3.
  - The Lane C cyclical sell rule is the charter's.
  - Rates are dated: y10 on 3.11.2026, the US 10-year on 2.11.2026, FX on 3.11.2026.
- **financials.json.** Its formatting is preserved, because a JSON round trip reproduced the file byte for byte before
  the edit. Its reconciled figures are unchanged, except FY2021 PP&E depreciation, which a filing page proves (AR-2).

## CIO review of this verification (3.11.2026 record; no price, rate or date changed)

- **D1 is now "no".** The Paymeant study's charter lens found that D1's first clause ("Was value estimated before
  looking at the price") fails closed when the price is in the valuation brief (its C-1). The same pipeline ran both
  studies, and the market workstream's price fed this study's valuation brief too, so D1 is answered alike in both:
  "no" here as well. No value input uses the price, so no number moves. VETO tally 13 yes / 11 no / 4 cannot assess
  (12 n/a). The VETO list in out §7, the gate's verdict section, the checklist and memo §1, §9 and §14 are updated.
- Whether a future run keeps the price out of the valuation brief, so that D1 can pass, is the principal's call.

## Files changed

- `research/gilat_telecom/valuation.py`, `research/gilat_telecom/output.txt`
- `research/gilat_telecom/work/gate.md`, `research/gilat_telecom/checklist.md`, `research/gilat_telecom/thesis_he.md`
- `research/gilat_telecom/sources.md`, `research/gilat_telecom/financials.json`
- New: `research/gilat_telecom/thesis_numbers.py`, `research/gilat_telecom/thesis_numbers_output.txt`, this file
