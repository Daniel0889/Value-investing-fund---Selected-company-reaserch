# Paymeant Financial Technologies (TASE 1180876): final verification

**Date: 3.11.2026**, the study date. The record was verified as it stood on that date. The editing was done on
4.11.2026, and no price, rate or date was updated: the price is the 3.11.2026 close of 3.173 ILS, and the y10 used is
the 3.11.2026 reading that the record's own market workstream already held.

**Verdict: NO_THESIS, unchanged.** The lane is none, there is no buy price, and the size is 0% of NAV.
- No confirmed defect changes the outcome of a decision rule that the verdict rests on.
- One VETO answer changed (D1, now "no"). It adds a failure and removes none.

## 1. What was checked, and by which lens

The CIO gate's revisions and the Hebrew memo were checked by three independent verifiers. Their full reports are in
the scratchpad workspace (`verify/paymeant/arithmetic.md`, `charter.md`, `memo-facts.md`).

| Lens | Scope | Findings |
|---|---|---|
| Arithmetic and inputs | Re-derived every headline from financials.json and framework d1-d11, e2. Traced the value-moving inputs to the filing pages | F1-F7, library L1-L3 |
| Charter | Charter Revision 4 ("Text to paste"), framework, checklist, screen_spec, Israeli rules: the four questions, the lane, the 60 items, sizing, the hurdle | C-1 to C-7, five library notes |
| Memo facts | Every number in thesis_he.md against the record, the 12 facts the verdict rests on against the pages, and the Hebrew against the English | MF-1 to MF-11 |

**The final editor's own checks:**
- confirmed or refuted every finding against the files and the filing pages;
- re-read the disputed pages as images at 110 dpi:
  - paymeant_fy2025 p.49, p.68, p.99, p.105, p.109 and p.112;
  - paymeant_h1_2026 p.18 and p.23;
- read the text layer of fy2025 p.97, p.108-111 and p.114, and of h1_2026 p.25 and p.33;
- measured each fix's effect with read-only probes of `valuation.py`.

The scripts are in the scratchpad workspace under `verify/paymeant/fix_tools/`:
- `probe.py` prints the headline values;
- `probe_0_baseline.txt` to `probe_4_final.txt` record them before and after each fix;
- `check_f2.py` covers implied growth;
- `number_trace.py` traces every number in the documents to a record file.

## 2. Headline values (out §4-§6, per diluted share, ILS)

| Value | Before verification | After | What moved it |
|---|---|---|---|
| Price (3.11.2026 close) | 3.173 | 3.173 | — |
| Worst case, low end (sizing) | 0.5921 | 0.6391 | F1 +0.0485, F3 −0.0015 |
| Worst case, high end (Dempster) | 1.0916 | 1.0891 | F3 |
| Conservative | 1.7472 | 1.7431 | F3 |
| **Base** (DCF, lender basis) | **2.1857** | **2.2232** | F3 −0.0050, F5 +0.0425 |
| EPV | 2.1521 | 2.1841 | F3, F5 |
| Optimistic | 4.6821 | 4.7220 | F3, F5 |
| Probability-weighted | 2.3363 | 2.3653 | F1, F3, F5 |
| Sensitivity grid | 1.95-2.55 | 1.98-2.60 | F3, F5 |
| Reference lines: Tier C / bank route | 1.09 / 2.28 | 1.09 / 2.27 | F3 |
| Dilutive shares at the price | 309,797 | 401,732 | F3 |
| L_worst / permanent-loss budget | 81.3% / 6.1% | 79.9% / 6.3% | F1 |
| Implied growth: today's scale / free | −3.2% / +5.3% | −3.3% / +5.0% | F5 |
| Buy price | none | none | — |
| Size | 0% of NAV | 0% of NAV | quarter-Kelly binds at 0 |

The price is above every value except the optimistic case, as before.

## 3. Findings and dispositions

Severity uses the task's rubric. Where the final editor graded a finding differently from its verifier, both grades
are shown as "verifier → editor".

| ID | Lens | Severity | Disposition | Evidence (one line) |
|---|---|---|---|---|
| F1 | Arithmetic | high | **fixed** | fy2025 p.105 (note 15d, image): the gross DTL is intangible 1,681 + loans held for sale 1,934; h1_2026 p.23 (image): net DTL 1,919 inside total liabilities of 145,031. The run-off removes both assets, so `runoff_low` now deducts TL − 1,919. Worst low 0.5921 → 0.6406 alone (+8.2%) |
| F2 | Arithmetic | medium | **fixed** (record); library part under L1 | `check_f2.py`: at the solved +13.85%, g/ROIIC = 1.24, so lib's `min(g/roiic, 1)` leaves growth above ROIIC free. The line no longer says "charged"; it prints the value at full internal reinvestment, 102,001 against 127,388 (98,502 before the fixes). Uncapped d4 needs +21.8% (+23.9% before the fixes; computed outside the library, so the record does not print it) |
| F3 | Arithmetic | medium | **fixed** | fy2025 p.109-110: the 31.7.2023 and 25.2.2024 grants vest nothing before 1.8.2025 and 1.4.2026. p.112 (image): 2,737,750 − 1,920,000 − 510,000 − 46,835 = 260,915 at 0.01. With that, 1,000,000 + 418,960 + 510,000 + 260,915 = 2,189,875 exactly, and note 17's 4.02 is the average without the 0.01 options (4.02; 3.54 with them). The 5.89 plug is gone; the 85,000 shares issued in 2026 are netted (h1_2026 p.25). Dilutive shares at the price 309,797 → 401,732 |
| F4 | Arithmetic | low → medium | **fixed** | fy2025 p.99 and h1_2026 p.33 (images): (a) is "מסך כל המאזן (או המאזן המוחשי)"; the company reports 34% and 33%-34% (h1_2026 p.18). Both denominators are now printed; the total balance sheet binds: 40,318 / 37,675, not 42,385 / 39,742 |
| F5 | Arithmetic | low → medium | **fixed** | fy2025 p.97: lease interest 191 sits in the funding-cost line (finance expense 4,711, p.114; financials.json caveat 7), while the 2,594 liability is also deducted. The interest is now added back after tax (d3 treats leases as debt), and the sentence on the floor is corrected: 3,514 > 3,278. OE_norm 8,779 → 8,926; base +1.9% |
| F6 | Arithmetic | low → medium | **fixed** (with C-2) | The tier medians counted TTM beside FY2025 and left out FY2021. Now taken over fiscal years: 13.6% with FY2021, 14.8% on FY2022-FY2025, minimum negative |
| F7 | Arithmetic | low | **fixed** | fy2025 p.49 and p.99 (images): line D has 89,000 unused of 100,000, so 11,000 is drawn. gate O10, memo O10 and out §1b now say "unused on lines A and D 189,000 (A undrawn; D 11,000 drawn)" |
| C-1 | Charter | high | **fixed** | Constitution checklist l.78: D1 asks "Was value estimated before looking at the price". The record's own note says the price was in the brief, and a "don't know" counts as "no". D1 is now "no"; VETO 7 / 24 / 6 / 3; gate §3, §13 and memo §9 updated |
| C-2 | Charter | medium | **fixed** | W is the fiscal years (gate B3), and FY2021's EBIT before funding cost is −679. out §1a now gives the window statistics with FY2021 as a loss year and TTM shown but not counted. A3 and memo §3, §5, §6 and §9 restated; still Tier B's band |
| C-3 | Charter | medium | **fixed**; primary-source part deferred | market.md §5 (l.244-249) gives the generic 10-year, 4.162%, and the 0537 bond only as a cross-check; screen_spec defines y10 as the 10-year yield; Gilat's study of the same date uses 4.16%. Y10 is now 0.04162. r stays 10%; Graham's required yield 8.6% → 8.3%; a 2-point rise still leaves r at 10% (printed) |
| C-4 | Charter | low | **fixed** | framework h6 and small_investor rule 10 make the price-reliability block mandatory below 100,000. out §6 now carries it: 352,392 ILS, 111,691 shares, 46 trades, 18.4x the median; 10 sessions under 1,000 ILS. F6 is restated: the TASE room is the only open part, so it becomes "cannot assess here"; X5 is noted separately. FLAG 7 / 8 / 4 / 1 |
| C-5 | Charter | low | **fixed** | screen_spec §3: X4's rule for missing data is "Fail". gate §11 item 8, checklist C6, memo §14 item 9 and out §1b now record X4 as failed closed until the FY2020 comparatives are read |
| C-6 | Charter | low | **fixed** | out §5 prints only "51% below base" (50% before the fixes); "מרווח כולל 0.5006" was printed nowhere and misused d11's term. Memo §1 now says the Tier C line is min(2/3 NCAV, Dempster) = 1.09, not a margin and not a buy price |
| C-7 | Charter | low | **fixed** (same as F7) | See F7 |
| MF-1 | Memo facts | medium | **fixed** | gate §4 ("if one is met, the file reopens"), gate §10 ("only when conditions 1 and 2 are met and §11 is closed") and memo §14 disagreed. §10's rule is adopted in gate §4 and memo §12 and §14; condition 3 alone does not reopen the file |
| MF-2 | Memo facts | medium | **fixed** | fy2025 p.99 and h1_2026 p.33 (images): (b) reads "ההון העצמי ... לא יפחת מסך של 25 מיליוני ש"ח"; only the directors' report (fy2025 p.68, h1_2026 p.18) says tangible. Memo §14 item 3 is rewritten as a company inconsistency; the covenant table, gate B6, the valuation.py comment and out §4 show both readings (53,643 / 51,000 on TE; 61,912 on equity) |
| MF-3 | Memo facts | low | **fixed** (same as F7) | See F7 |
| MF-4 | Memo facts | low | **fixed** | h1_2026 p.31: 9,515 is the pre-tax step-up, and 78,643 − 71,316 = 7,327 after tax. out §3 now prints both; memo §7 and §11 (B8) and gate B8 read "9,515 pre-tax; 7,327 after tax" |
| MF-5 | Memo facts | low | **fixed** (same as C-6) | See C-6 |
| MF-6 | Memo facts | low | **fixed** | out §0 prints P/E 6.76; 6.6 is the brief's Mega headline (6.64, sources.md). The memo §1 heading now reads "P/E של 6.76 (כ-6.6 בכותרת התדריך)" |
| MF-7 | Memo facts | low | **refuted in part; header fixed** | financials.json holds the three figures as fractions: `kpis` gross_margin 0.8842 and pretax_margin 0.4056, and related_parties 0.273 ("2 x 2,484 / net income 18,188"). The citations are right. The header's list of number sources left out the work files cited inline; it now includes them |
| MF-8 | Memo facts | low | **fixed** | The repository has no `work/paymeant/`. `research/paymeant/work/*` is byte-identical to the scratchpad copies (cmp), and gate_tools is not committed. Paths fixed in thesis_he.md, gate.md, checklist.md, sources.md and the valuation.py comments |
| MF-9 | Memo facts | low | **fixed** | fy2025 p.49 (image): every cell reads "פריים +0.5% – פריים +0.8%". The six `bank_credit_short_term` notes in financials.json now read "prime+0.5% to prime+0.8%". No figure changed: a leaf-by-leaf comparison shows only these six strings differ |
| MF-10 | Memo facts | low | **fixed** | fy2025 p.112: the plan was approved on 13.11.2024 "לתקופה של שנתיים החל מיום 18 בנובמבר 2024". Checklist B2 now reads "approved on 13.11.2024 for 18.11.2024-18.11.2026" |
| MF-11 | Memo facts | low | **fixed** | charter l.263 and lib `position_size()` put Tier B's cap at 10%. gate §8 and memo §12 now state the 10% and that tier B also gives 0.0% |

**Deferred (for the principal).**
- **C-3, primary source.** The Bank of Israel or Ministry of Finance 10-year benchmark for 3.11.2026 was not read; no
  network was used. The record uses the generic 10-year that its market workstream recorded that day. r is 10% on
  any of these readings.
- **C-1, process.** The pipeline puts the price in the valuation brief. Whether D1's first clause can then ever pass is
  the principal's call: ratify an agent-workflow reading ("no value input uses the price"), or keep the price out of the
  brief. The Gilat Telecom study (`research/gilat_telecom/checklist.md`) had answered D1 the same way; at the CIO's review
  of this verification it was made "no" there too, so both studies now read D1 alike.

## 4. Library issues (lib/charter_valuation.py against framework.md; not edited)

| # | Formula | Issue | Effect on Paymeant |
|---|---|---|---|
| L1 | d4 / d8 | `dcf_operations` sets `reinvest = min(g1 / roiic, 1.0)` (l.197). `implied_growth` calls it with `cap_growth=False` (l.268-269), so the cap still applies. Above g = ROIIC, part of the growth is then free. d4 charges g / ROIIC × OE with no cap | lib +13.7% against +21.8% uncapped. The record now reports the 100%-reinvestment value instead (F2) |
| L2 | d4, timing | The reinvestment is charged at t = 0 (OE_0 × g1 / ROIIC) and at gT / ROIIC_T in year 10 (l.200-207). d4 writes FCF_t = OE_t × (1 − g / ROIIC) for t = 1..10. The docstring says the departure is deliberate, so that ROIIC = r is worth exactly EPV (d3) | Base about +2.2% on d4 as literally written. The price stays above the grid either way |
| L3 | d2 / screen_spec 2.3 | `is_cyclical` uses the sample standard deviation and `m < 0` (l.81-86). screen_spec 2.3 defines op_margin_sd as the population SD and cyclical as any EBIT_adj ≤ 0. valuation.py prints the sample figure, 21.34%, to match lib; the population SD is 19.09% | None: FY2021 is a loss year, and both figures exceed 17.23% |
| L4 | d11, ceiling | `required_margin` tests the 50% ceiling on the tier base only (l.361-362). d11 says an endogenous add-back "is not a data penalty", so it belongs in the margin before data additions. Tier D on B with an add-back needs 55% and should be NO_THESIS; lib returns `no_thesis=False` | None |
| L5 | e2 | `position_size` includes the liquidity cap only when `nav` is passed, and the TASE cap only when `tase_room` is passed (l.431-437). So `size` can exceed the liquidity maximum, whereas e2 takes the smallest of all limits | None: the size is 0%, and the ILS cap is stated separately |
| L6 | d11, Tier C | `ValueRange.buy_price()` applies the tier's buy fraction to `base` for every tier (l.459-460). For Tier C, d11 uses 2/3 NCAV and Dempster (net-nets), or 50% of private-owner value | None: valuation.py builds `vr` with a Tier C margin but never prints `buy_price()` |

## 5. Checks that passed

1. Before any edit, `valuation.py` re-ran to a byte-identical `output.txt`.
2. Every headline value reproduced to its printed precision under all three lenses, and in the final editor's probe:
   base 2.1857, EPV 2.1521, conservative 1.7472, worst 0.5921-1.0916, optimistic 4.6821, weighted 2.3363, grid
   1.9505-2.5545.
3. The 30.6.2026 balance sheet matches the page image (h1_2026 p.23):
   - cash 4,877; loans at fair value 203,167; loans at amortised cost 3,632 + 3,054; receivables 3,658 + 2,217;
   - right-of-use 2,392; PP&E 677; intangibles 8,269; total assets 231,943;
   - bank credit 115,225; payables for credit transactions 19,273; deferred tax 1,919; leases 781 + 1,813;
     equity 86,912.
4. The lines, covenants and pledges (fy2025 p.99) and the line table (p.49) match the record: 340,000 of lines,
   104,000 drawn, bank B 92,000 (88.5%), on-call.
5. Note 17's 2025 roll-forward totals reconcile: 2,737,750 + 1,519,000 − 1,966,835 − 100,040 = 2,189,875.
6. The gate revisions B1-B12 and O1-O11 are implemented as gate §1 says. The first-pass quantities feed only lines
   labelled first version or superseded.
7. The four questions run in the charter's order. Q1 is "don't know", and Q2, Q3 and Q4 are "no", so the result is
   NO_THESIS. WATCHLIST and TOO_HARD are rejected for the stated reasons.
8. The lane is none, so no tier margin and no buy price apply. Both reference lines are labelled "not a buy price".
   The data additions are capped at +10, with no endogenous add-back.
9. All 60 checklist items are present, and their VETO and FLAG types match the constitution. The tallies reconcile
   row by row: VETO 7 / 24 / 6 / 3 and FLAG 7 / 8 / 4 / 1.
10. Sizing follows e2: full Kelly 0 because the weighted 2.37 is below 3.173; quarter-Kelly binds at 0%; the liquidity
    maximum is 20 × 20% × 2,590 = 10,361 ILS; X5 fails (median 19,125).
11. There are three falsification conditions, each dated and observable. Their inputs reproduce: the 2.65% arrears
    baseline is 5,071 / 191,493 (fy2025 p.66), and the circular takes force on 12.1.2027 (h1_2026 p.8).
12. Facts confirmed on the pages:
    - defaults 1,481 → 4,395, and "שינוי בשיעור זניח";
    - provision coverage 64.0% → 16.3%;
    - "רשאים להפסיק ... באופן חד צדדי";
    - SPC indemnities "בגין מקרים נוספים";
    - Adjusted EBITDA adds back share-based pay;
    - the 2025 exercises at a weighted 2.02;
    - FY2021's loss came from the IPO share-based items;
    - merchants may cancel at any time.
13. The tax rate holds: the statutory 23% against a cumulative FY2023-FY2025 effective rate of 23.01% (fy2025 p.106).
    B11's rejection stands.
14. The memo's numbers hold after the edits:
    - its §2 and §5 tables still match financials.json cell by cell (the memo-facts lens's `memo_tables.py`, re-run on
      the edited memo: 0 mismatches);
    - its §9 lists match checklist.md item by item (30 VETO failed, 7 passed, 3 n/a; FLAG 7 / 8 / 4 / 1);
    - every number in thesis_he.md, gate.md and checklist.md traces to output.txt, financials.json or a committed work
      file (`number_trace.py`). The only exceptions are the deliberate before-and-after values in gate §13 and the
      memo's verification note.
15. The memo is still in Hebrew and keeps its 15 sections.
16. financials.json's reconciled figures are unchanged. Only six note strings differ (MF-9).
17. After the edits, `valuation.py` re-runs to a byte-identical `output.txt` (§7).

## 6. Files changed

All are under `research/paymeant/`:
- `valuation.py`: F1, F2, F3, F4, F5, C-2/F6, C-3, C-4, C-5, MF-2, MF-4, F7; comments and docstring for MF-8;
- `output.txt`: regenerated;
- `work/gate.md`: numbers restated, MF-1, MF-11, F7, MF-2, C-1, C-5 and MF-8, plus a new §13;
- `checklist.md`: D1, F6, C6, A2, A3, A6, B2, D2-D5, E3 and H2; tallies; header and paths;
- `thesis_he.md`: numbers restated in §1-§14, C-6, MF-1, MF-2, MF-4, MF-6, the header, the §14 contradictions marked
  תוקן, a verification note, and the §15 paths;
- `sources.md`: y10, covenants, options, lease interest, deferred tax, the price-reliability source, and paths;
- `financials.json`: six note strings (MF-9);
- `verification.md`: this file.

Nothing outside `research/paymeant/` was edited. `lib/charter_valuation.py` and the Gilat Telecom files are untouched.

## 7. Reproduction

```
cd /home/user/value-investing-fund---selected-company-reaserch
python3 -I research/paymeant/valuation.py > research/paymeant/output.txt
```

Re-run after the last edit: the output is byte-identical to `output.txt` (diff empty).
