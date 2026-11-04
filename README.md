# Value investing fund — selected company research

Valuations of individual companies under the fund's Revision 4 constitution
(10% hurdle, margin of safety by business grade, no leverage).

- `lib/charter_valuation.py` — the Charter Revision 4 arithmetic (framework sections d1-d11 and
  e2): maintenance capex floored at depreciation, owner earnings, normalised EBIT with the
  cyclical test, EPV with the equity bridge, the ten-year DCF with the reinvestment charged and
  terminal growth of at most 2.5%, implied growth, NCAV and Dempster value, Graham's yardstick,
  the tier margin with capped data additions, the sensitivity grid and position sizing.
  Research from November 2026 on uses it.
- `lib/rev4_value.py` — the earlier, simpler methods (owner earnings, EPV, conservative DCF with
  a 15x terminal multiple, 10x pre-tax test, reverse DCF, buy line by grade), used by the
  October 2026 studies (Alphabet, Samsung, Aluma, Thor).
- `research/` — per-company inputs, sources and outputs. The November 2026 studies (Paymeant, Gilat
  Telecom) also carry the reconciled `financials.json`, the 60-item `checklist.md`, the Hebrew investment
  memo `thesis_he.md`, `verification.md` (an independent three-lens check of the final record: every finding,
  its disposition and the fix), and under `work/` the analysts' notes, the red-team objections and the CIO gate
  (`gate.md`). Gilat Telecom's `thesis_numbers.py` computes the memo's few figures that `valuation.py` does not print. Memos cite those notes as `work/<company>/...`, which is `research/<company>/work/...`
  here. The company filings themselves are not in the repository.
- `research/tase_studies_20261103.xlsx` — the Excel workbook of the November 2026 studies: a summary of both
  companies, each company's filings data by period (every value carries its document and page as a cell
  comment), the valuation with the base-case chain as live formulas, and the 60-item checklists. A checks
  sheet compares every formula result with `valuation.py`. `research/build_workbook.py` builds it from the
  study files (`python3 -I research/build_workbook.py`, then recalculate in LibreOffice or Excel).
