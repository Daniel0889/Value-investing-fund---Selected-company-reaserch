#!/usr/bin/env python3
"""Build research/tase_studies_20261103.xlsx, the data workbook of the two November 2026 TASE studies
(Paymeant Financial Technologies, TASE 1180876, and Gilat Telecom Global, TASE 1080597).

Nothing in the workbook is retyped. Every figure comes from the study's own files:
  - research/<slug>/financials.json  the reconciled dataset from the filings; each value cell carries its
                                      document id and PDF page (and any note or status) as a cell comment;
  - research/<slug>/valuation.py     run here, so the valuation sheets hold exactly the figures output.txt
                                      prints (the script refuses to build if the run does not reproduce
                                      output.txt);
  - research/<slug>/checklist.md     the 60-item checklist of the CIO gate.
The base-case chain (normalised EBIT -> owner earnings -> value of operations -> equity -> value per
share) is rebuilt as live formulas. The "בדיקות" sheet compares each formula result with valuation.py.

Colours: blue = an input taken from the files; black = a formula; green = a link to another sheet;
yellow fill = a key assumption; orange fill = a value the dataset marks UNVERIFIED or as an estimate.

Run from the repository root, then recalculate the formulas (LibreOffice or Excel):
    python3 -I research/build_workbook.py
"""
from __future__ import annotations

import contextlib
import io
import json
import pathlib
import re
import runpy
import statistics

from openpyxl import Workbook
from openpyxl.comments import Comment
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.properties import PageSetupProperties

ROOT = pathlib.Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "research"
OUT = RESEARCH / "tase_studies_20261103.xlsx"

FONT = "Arial"
BLUE, BLACK, GREEN, WHITE = "0000FF", "000000", "008000", "FFFFFF"
FILL_TITLE = PatternFill("solid", fgColor="1F4E78")
FILL_HEAD = PatternFill("solid", fgColor="DDEBF7")
FILL_SECTION = PatternFill("solid", fgColor="EDEDED")
FILL_KEY = PatternFill("solid", fgColor="FFFF00")
FILL_SOFT = PatternFill("solid", fgColor="FCE4D6")

NF_K = '#,##0;(#,##0);"-"'
NF_K1 = '#,##0.0;(#,##0.0);"-"'
NF_PS = '0.000;-0.000;0.000'
NF_PCT = '0.0%;-0.0%;0.0%'
NF_PCT2 = '0.00%;-0.00%;0.00%'
NF_X = '0.00"x"'
NF_INT = '#,##0'
NF_FX = '0.000'

MAX_GROWTH, MAX_TERMINAL_GROWTH = 0.10, 0.025      # lib/charter_valuation.py (framework d4)
HURDLE_FLOOR, HURDLE_SPREAD = 0.10, 0.03            # r = max(10%, y10 + 3 points)


# =====================================================================================================
# loading
# =====================================================================================================
def run_valuation(slug: str) -> dict:
    """Run research/<slug>/valuation.py and return its globals; refuse if it does not reproduce output.txt."""
    path = RESEARCH / slug / "valuation.py"
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        g = runpy.run_path(str(path), run_name="__main__")
    printed = [ln.rstrip() for ln in buf.getvalue().splitlines()]
    saved = [ln.rstrip() for ln in (RESEARCH / slug / "output.txt").read_text(encoding="utf-8").splitlines()]
    if printed != saved:
        raise SystemExit(f"{slug}: valuation.py does not reproduce output.txt; re-run it before building the workbook")
    return g


def load_fin(slug: str) -> dict:
    return json.loads((RESEARCH / slug / "financials.json").read_text(encoding="utf-8"))


# =====================================================================================================
# a sheet with a few writing helpers
# =====================================================================================================
class Sheet:
    def __init__(self, wb: Workbook, title: str, widths: list[float], rtl: bool = True, fit_width: bool = True):
        self.ws = wb.create_sheet(title)
        self.title = title
        self.ws.sheet_view.rightToLeft = rtl
        for i, w in enumerate(widths, start=1):
            self.ws.column_dimensions[get_column_letter(i)].width = w
        self.ws.page_setup.orientation = "landscape"
        self.ws.page_setup.paperSize = self.ws.PAPERSIZE_A4
        if fit_width:   # print every column on one page width
            self.ws.sheet_properties.pageSetUpPr = PageSetupProperties(fitToPage=True)
            self.ws.page_setup.fitToWidth = 1
            self.ws.page_setup.fitToHeight = 0
        self.row = 1

    def ref(self, cell: str) -> str:
        col = "".join(ch for ch in cell if ch.isalpha())
        rw = "".join(ch for ch in cell if ch.isdigit())
        return f"'{self.title}'!${col}${rw}"

    def put(self, cell: str, value, *, nf: str | None = None, color: str | None = None, bold: bool = False,
            fill: PatternFill | None = None, comment: str | None = None, wrap: bool = False, italic: bool = False,
            size: int = 10, halign: str | None = None):
        c = self.ws[cell]
        c.value = value
        if color is None:
            if isinstance(value, str) and value.startswith("="):
                color = GREEN if "!" in value else BLACK
            elif isinstance(value, bool) or isinstance(value, (int, float)):
                color = BLUE
            else:
                color = BLACK
        c.font = Font(name=FONT, size=size, bold=bold, italic=italic, color=color)
        if nf:
            c.number_format = nf
        if fill:
            c.fill = fill
        if wrap or halign:
            c.alignment = Alignment(wrap_text=wrap, vertical="top", horizontal=halign)
        if comment:
            text = comment if len(comment) <= 1500 else comment[:1497] + "..."
            cm = Comment(text, "research")
            cm.width = 360
            cm.height = min(60 + 15 * (len(text) // 55 + text.count("\n")), 420)
            c.comment = cm
        return c

    def title_rows(self, title: str, subtitle: str | None = None, span: int = 6):
        self.put("A1", title, bold=True, size=14, color=WHITE, fill=FILL_TITLE)
        for i in range(2, span + 1):
            self.ws.cell(row=1, column=i).fill = FILL_TITLE
        if subtitle:
            self.put("A2", subtitle, italic=True)
        self.row = 4

    def section(self, text: str, span: int = 6):
        r = self.row
        self.put(f"A{r}", text, bold=True, fill=FILL_SECTION)
        for i in range(2, span + 1):
            self.ws.cell(row=r, column=i).fill = FILL_SECTION
        self.row += 1

    def line(self, label: str, value, *, nf: str | None = None, note: str | None = None, comment: str | None = None,
             fill: PatternFill | None = None, color: str | None = None, bold: bool = False) -> str:
        """label in A, value in B, note in C; returns the value cell address."""
        r = self.row
        self.put(f"A{r}", label, bold=bold)
        self.put(f"B{r}", value, nf=nf, comment=comment, fill=fill, color=color, bold=bold)
        if note:
            self.put(f"C{r}", note, italic=True, wrap=False)
        self.row += 1
        return f"B{r}"

    def blank(self, n: int = 1):
        self.row += n


# =====================================================================================================
# financial data sheets (financials.json)
# =====================================================================================================
HE = {
    "revenue": "הכנסות", "cost_of_revenue": "עלות ההכנסות", "gross_profit": "רווח גולמי",
    "sm_expense": "הוצאות מכירה ושיווק", "selling_marketing": "הוצאות מכירה ושיווק",
    "rd_expense": "הוצאות מחקר ופיתוח", "rnd": "הוצאות מחקר ופיתוח",
    "ga_expense": "הוצאות הנהלה וכלליות", "general_admin": "הוצאות הנהלה וכלליות",
    "total_opex": "סך הוצאות התפעול", "operating_income": "רווח תפעולי",
    "other_income_expense": "הכנסות (הוצאות) אחרות", "finance_expense": "הוצאות מימון",
    "finance_income": "הכנסות מימון", "finance_net": "מימון, נטו",
    "finance_expense_operating": "הוצאות מימון תפעוליות (עלות מימון התיק)",
    "credit_loss_expense": "הוצאות בגין הפסדי אשראי", "share_of_associates": "חלק ברווחי חברות כלולות",
    "pretax_income": "רווח לפני מסים", "tax_expense": "מסים על ההכנסה", "net_income": "רווח נקי",
    "net_income_total": "רווח נקי", "net_income_owners": "רווח נקי לבעלי המניות",
    "nci_share": "חלק הזכויות שאינן מקנות שליטה", "eps_basic_ils": "רווח בסיסי למניה (ש\"ח)",
    "eps_diluted_ils": "רווח מדולל למניה (ש\"ח)", "eps_basic_usd": "רווח בסיסי למניה (דולר)",
    "eps_diluted_usd": "רווח מדולל למניה (דולר)", "da_total_cf": "פחת והפחתות (דוח התזרים)",
    "sbp_expense": "תשלום מבוסס מניות", "sbc": "תשלום מבוסס מניות",
    "adjusted_ebitda_company": "Adjusted EBITDA (לפי החברה)", "adj_ebitda_company": "Adjusted EBITDA (לפי החברה)",
    "ebitda_company": "EBITDA (לפי החברה)", "operating_cash_flow": "תזרים מפעילות שוטפת",
    "ocf": "תזרים מפעילות שוטפת", "investing_cash_flow": "תזרים מפעילות השקעה",
    "investing_cf": "תזרים מפעילות השקעה", "financing_cash_flow": "תזרים מפעילות מימון",
    "financing_cf": "תזרים מפעילות מימון", "capex_ppe": "השקעה ברכוש קבוע",
    "lease_principal_repaid": "פירעון קרן חכירות", "lease_principal_paid": "פירעון קרן חכירות",
    "dividends_paid_owners": "דיבידנד לבעלי המניות", "dividends_owners": "דיבידנד לבעלי המניות",
    "buybacks": "רכישה עצמית של מניות", "buybacks_shares": "רכישה עצמית של מניות", "tax_paid": "מסים ששולמו",
    "interest_paid": "ריבית ששולמה", "interest_received": "ריבית שהתקבלה", "total_assets": "סך הנכסים",
    "total_liabilities": "סך ההתחייבויות", "equity_owners": "הון עצמי לבעלי המניות",
    "cash_and_equivalents": "מזומנים ושווי מזומנים", "cash": "מזומנים ושווי מזומנים",
    "restricted_cash": "מזומן מוגבל", "trade_receivables": "לקוחות", "inventory": "מלאי",
    "total_current_assets": "סך הנכסים השוטפים", "total_current_liabilities": "סך ההתחייבויות השוטפות",
    "trade_payables": "ספקים ונותני שירותים", "ppe_net": "רכוש קבוע, נטו",
    "right_of_use_asset": "נכסי זכות שימוש", "rou_assets": "נכסי זכות שימוש",
    "intangible_assets": "נכסים בלתי מוחשיים", "intangibles_net": "נכסים בלתי מוחשיים, נטו", "goodwill": "מוניטין",
    "lease_liabilities_total": "התחייבויות בגין חכירות", "bank_credit_short_term": "אשראי בנקאי לזמן קצר",
    "loans_held_for_sale_fv": "הלוואות המוחזקות למכירה (שווי הוגן)",
    "loan_book_total_on_balance_sheet": "תיק ההלוואות במאזן", "tangible_equity": "הון מוחשי",
    "shares_outstanding_end": "מניות במחזור, סוף התקופה", "shares_weighted_basic": "ממוצע משוקלל של מניות (בסיסי)",
    "shares_weighted_diluted": "ממוצע משוקלל של מניות (מדולל)", "employees_end": "עובדים", "employees": "עובדים",
    "originations_ils_m": "היקף העמדת הלוואות (מיליוני ש\"ח)", "bonds_nonconvertible": "אג\"ח שאינן המירות",
    "convertibles_total": "אג\"ח המירות, סך הכול", "fcf_company": "FCF (לפי החברה)", "nci": "זכויות שאינן מקנות שליטה",
    "wc_change": "שינוי בהון החוזר", "wc_change_total_reported": "שינוי בהון החוזר (כפי שדווח)",
    "capex_intangibles": "השקעה בנכסים בלתי מוחשיים", "net_change_in_cash": "שינוי במזומנים",
    "share_capital": "הון מניות", "share_premium": "פרמיה על מניות", "retained_earnings": "עודפים",
    "trade_receivables_gross": "לקוחות, ברוטו", "other_payables": "זכאים ויתרות זכות", "other_receivables": "חייבים ויתרות חובה",
}

SECTIONS = [("PL", "דוח רווח והפסד והערות"), ("CF", "דוח תזרים המזומנים"), ("BS", "מאזן (יתרות לסוף התקופה)"),
            ("OT", "נתונים תפעוליים, מניות ואחר")]

BS_EXACT = {
    "cash", "nci", "goodwill", "inventory", "bonds", "restricted_cash", "st_deposits", "marketable_securities",
    "total_assets", "total_liabilities", "total_current_assets", "total_current_liabilities",
    "total_noncurrent_liabilities", "equity_owners", "equity_owners_opening", "share_capital", "share_premium",
    "other_capital_reserves", "retained_earnings", "tangible_equity", "net_bank_debt", "ppe_net", "right_of_use_asset",
    "rou_assets", "intangible_assets", "intangibles_net", "trade_receivables", "trade_payables", "other_payables",
    "other_receivables", "taxes_payable", "contract_assets", "contract_liabilities", "deferred_tax_asset",
    "deferred_tax_assets", "deferred_tax_liability", "loan_book_total_on_balance_sheet", "credit_loss_allowance",
    "accrued_income_receivable", "current_tax_assets", "current_tax_liabilities", "other_lt_assets",
    "prepaid_expenses_company", "employee_benefit_assets", "lt_supplier_liabilities", "working_capital_company",
    "interest_payable_bonds", "financial_debt_excl_leases", "short_term_credit", "bank_credit_short_term",
    "state_guaranteed_loan", "loans_total", "loans_short", "loans_long", "bonds_series_B", "bonds_nonconvertible",
    "convertibles", "convertibles_total", "option_liabilities_total", "mgmt_warrants_liability",
    "warrant_option_liabilities", "amounts_payable_credit_transactions", "longterm_credit_balance_credit_providers",
    "credit_balance_acquiring_corp_A", "of_which_cash", "of_which_deposits", "cash_incl_designated",
    "cash_and_equivalents", "short_term_deposits_separate_line", "other_longterm_receivables",
    "trade_receivables_gross", "fx_hedge_options_liability", "convertible_series_C", "intangibles_licences_net",
    "intangibles_customer_relations_net", "loans_borrowings_long_term", "deferred_expenses_iru_current",
    "deferred_expenses_iru_noncurrent", "contract_costs_capitalised_noncurrent", "contract_costs_current",
    "state_guaranteed_loan_current", "state_guaranteed_loan_noncurrent", "loans_amortised_cost_net_total",
}
BS_PREFIX = ("cash_by_currency", "lease_liabilities", "loans_amortised", "loans_held", "loans_fv",
             "convertible_series", "conversion_option_liability", "equity_components", "wc_components",
             "original_presentation")
CF_PREFIX = ("ocf", "operating_cash_flow", "wc_change", "wc_delta", "interest_paid", "interest_received", "tax_paid",
             "capex", "acquisitions", "investing", "financing", "proceeds_", "restricted_cash_released",
             "restricted_cash_placed", "lease_principal", "lease_cash_outflow", "lease_total_cash_outflow",
             "lease_payments", "lease_interest_paid", "dividends", "buybacks", "bond_buyback", "share_issue_proceeds",
             "option_exercise_proceeds", "bond_issue", "bond_conversion_component", "series_B_principal",
             "series_F_convertible_principal", "bond_principal", "bond_interest_paid", "short_term_loan",
             "long_term_loan", "state_loan_repaid", "st_deposit_placed", "st_deposit_repaid", "warrants_issued_proceeds",
             "fx_effect_on_cash", "net_change_in_cash", "cash_end_per_cf", "rou_recognised_noncash", "noncash_", "fcf",
             "iru_deferred_expenses_paid", "finance_items_in_ocf", "option_revaluation_cf_lines",
             "capitalised_contract_costs", "contract_costs_capitalised", "capitalised_development_total",
             "rou_additions_note")
PL_PREFIX = ("revenue", "rev_", "cost_of_revenue", "gross_profit", "sm_", "rd_", "ga_", "selling_marketing",
             "general_admin", "rnd", "total_opex", "operating_income", "other_income_expense", "finance_expense",
             "finance_income", "finance_net", "share_of_associates", "pretax_income", "tax_expense", "tax_current",
             "tax_deferred", "net_income", "nci_share", "eps_", "oci", "total_comprehensive_income", "credit_loss_expense",
             "credit_losses_in_ga", "receivables_impairment_loss", "goodwill_impairment", "impairments", "da_", "sbp_",
             "sbc", "adjusted_ebitda", "adj_ebitda", "ebitda", "short_term_lease_expense", "satellite_lease_depreciation",
             "option_revaluation_loss", "loss_on_bond_exchange", "non_gaap_net_income", "lease_interest")


def classify(key: str) -> str:
    k = key.split(".")[0]
    if k in BS_EXACT or k.startswith(BS_PREFIX):
        return "BS"
    if k.startswith(CF_PREFIX):
        return "CF"
    if k.startswith(PL_PREFIX):
        return "PL"
    return "OT"


ABBR = {"ils": "ILS", "usd": "USD", "pct": "%", "fv": "FV", "rou": "ROU", "ppe": "PP&E", "sbp": "SBP", "sbc": "SBC",
        "da": "D&A", "ocf": "OCF", "fcf": "FCF", "cf": "CF", "nci": "NCI", "eps": "EPS", "iru": "IRU", "ebitda": "EBITDA",
        "oci": "OCI", "fx": "FX", "rd": "R&D", "sm": "S&M", "ga": "G&A", "st": "ST", "lt": "LT", "wc": "WC", "spc": "SPC",
        "fvoci": "FVOCI", "cpi": "CPI", "ttm": "TTM", "isp": "ISP", "bsa": "BSA", "m": "M"}


def humanize(key: str) -> str:
    parts = []
    for seg in key.split("."):
        words = [ABBR.get(w.lower(), w) for w in seg.split("_")]
        parts.append(" ".join(words))
    s = " / ".join(parts)
    return s[:1].upper() + s[1:]


def flatten_period(p: dict) -> dict:
    """field -> {'v', 'ref', ...}; nested dicts become 'parent.child' fields."""
    out = {}
    for key, val in p.items():
        if key == "_meta":
            continue
        if isinstance(val, dict) and "v" in val:
            out[key] = val
        elif isinstance(val, dict):
            for ck, cv in val.items():
                if isinstance(cv, dict) and "v" in cv:
                    out[f"{key}.{ck}"] = cv
                elif isinstance(cv, (int, float)) and not isinstance(cv, bool):
                    out[f"{key}.{ck}"] = {"v": cv, "ref": val.get("ref", ""), "note": val.get("note", "")}
    return out


def cell_comment(val: dict) -> str:
    bits = []
    if val.get("ref"):
        bits.append(f"Source: {val['ref']}")
    for k in ("status", "source", "calc", "note"):
        if val.get(k):
            bits.append(f"{k}: {val[k]}")
    for alt in val.get("alt", []) or []:
        if isinstance(alt, dict):
            bits.append(f"alt: {alt.get('v')} ({alt.get('ref', '')}{'; ' + alt['note'] if alt.get('note') else ''})")
    return "\n".join(str(b) for b in bits)


def soft(val: dict) -> bool:
    s = " ".join(str(val.get(k, "")) for k in ("status", "note")).upper()
    return "UNVERIFIED" in s or "ESTIMATE" in s


FY2020_MAP = {  # Gilat: financials.json field -> valuation.py global that also carries FY2020 (validated below)
    "revenue": "REV_USD", "gross_profit": "GP_USD", "operating_income": "EBIT_USD", "net_income": "NI_USD",
    "ocf": "OCF_USD", "sbc": "SBC_USD", "capex_ppe": "CAPEX_PPE_USD", "capex_intangibles": "CAPEX_INT_USD",
    "da_ppe": "DEP_PPE_USD", "da_licences": "AMORT_LIC_USD", "lease_principal_paid": "LEASE_PRIN_USD",
    "lease_interest_paid": "LEASE_INT_USD", "ppe_net": "NETPPE_USD", "rou_assets": "ROU_USD",
    "total_current_liabilities": "CL_USD",
    # not CA_USD or C_USD: their FY2020 entries are adjusted (current assets less the Wiocc stake; cash plus deposits)
}


def source_note_2020(src: str, name: str) -> str:
    """The comment on the FY2020 entry of a valuation.py dict (or on the dict's line)."""
    m = re.search(rf"^{name}\s*=\s*\{{(.*?)\}}([^\n]*)", src, flags=re.M | re.S)
    if not m:
        return "see valuation.py"
    for ln in m.group(1).splitlines():
        if "2020" in ln and "#" in ln:
            return ln.split("#", 1)[1].strip()
    if "#" in m.group(2):
        return m.group(2).split("#", 1)[1].strip()
    return "see valuation.py"


def fy2020_column(fin: dict, g: dict) -> tuple[dict, list[str]]:
    """FY2020 figures for Gilat from valuation.py, kept only where the same series equals financials.json in
    every FY2021-FY2025 year present in both (so the FY2020 value is the same line item)."""
    col, log = {}, []
    src = (RESEARCH / "gilat_telecom" / "valuation.py").read_text(encoding="utf-8")
    for field, name in FY2020_MAP.items():
        series = g.get(name)
        if not isinstance(series, dict) or 2020 not in series:
            continue
        same, n = True, 0
        for y in range(2021, 2026):
            jv = fin["periods"].get(f"FY{y}", {}).get(field)
            if y in series and isinstance(jv, dict) and isinstance(jv.get("v"), (int, float)):
                n += 1
                if abs(series[y] - jv["v"]) > 0.5:
                    same = False
        if same and n >= 2:
            where = source_note_2020(src, name)
            col[field] = {"v": series[2020], "ref": f"valuation.py {name} (FY2020 from the company's FY2021/FY2022 "
                          f"reports, downloaded from its website by the CIO gate): {where}"}
            log.append(f"FY2020 {field} <- {name}: kept ({n} years match)")
        else:
            log.append(f"FY2020 {field} <- {name}: skipped (series is defined differently from financials.json)")
    return col, log


def build_data_sheet(wb: Workbook, title: str, company: str, fin: dict, extra_cols: dict | None = None,
                     extra_first: str | None = None) -> tuple[Sheet, dict]:
    periods = list(fin["periods"].keys())
    flat = {p: flatten_period(fin["periods"][p]) for p in periods}
    if extra_cols:
        periods = [extra_first] + periods
        flat[extra_first] = extra_cols
    fields: dict[str, None] = {}
    for p in periods:
        for f in flat[p]:
            fields.setdefault(f, None)
    by_sec = {s: [f for f in fields if classify(f) == s] for s, _ in SECTIONS}

    S = Sheet(wb, title, [44, 34, 30] + [13] * len(periods), fit_width=False)
    S.title_rows(f"{company}: נתונים כספיים מהדוחות (המאגר המתואם, financials.json)",
                 "כחול = נתון מהדוחות; הערת התא מציינת מסמך ועמוד PDF. כתום = UNVERIFIED או הערכה. "
                 "שחור = נוסחה. " + str(fin.get("units", "")), span=3 + len(periods))
    S.put("A3", "מטבע: " + (fin["currency"] if isinstance(fin.get("currency"), str) else json.dumps(fin.get("currency"), ensure_ascii=False)),
          italic=True)
    hdr = S.row
    for i, h in enumerate(["Item", "פריט", "key"] + periods, start=1):
        S.put(f"{get_column_letter(i)}{hdr}", h, bold=True, fill=FILL_HEAD)
    S.row += 1
    cur = S.row
    for i, p in enumerate(periods, start=4):
        meta = fin["periods"].get(p, {}).get("_meta", {}) if p in fin["periods"] else {"currency": "USD"}
        S.put(f"{get_column_letter(i)}{cur}", meta.get("currency", fin.get("currency") if isinstance(fin.get("currency"), str) else ""),
              italic=True)
    S.put(f"A{cur}", "מטבע התקופה", italic=True)
    S.row += 1
    S.ws.freeze_panes = S.ws[f"D{S.row}"]

    # key ratios first (formulas on the rows below; their row numbers are fixed in advance)
    ratio_rows = 7
    first_data_row = S.row + 1 + ratio_rows + 1
    rows_of: dict[str, int] = {}
    r = first_data_row
    for sec, _ in SECTIONS:
        if by_sec[sec]:
            r += 1
            for f in by_sec[sec]:
                rows_of[f] = r
                r += 1
    S.section("יחסים מרכזיים (נוסחאות על השורות שלמטה)", span=3 + len(periods))
    rev = rows_of.get("revenue")
    ni_key = "net_income_total" if "net_income_total" in rows_of else "net_income"
    ocf_key = "operating_cash_flow" if "operating_cash_flow" in rows_of else "ocf"
    ratios = [("Gross margin", "מרווח גולמי", "gross_profit"), ("Operating margin", "מרווח תפעולי", "operating_income"),
              ("Pre-tax margin", "מרווח לפני מס", "pretax_income"), ("Net margin", "מרווח נקי", ni_key)]
    for en, he, key in ratios:
        rr = S.row
        S.put(f"A{rr}", en)
        S.put(f"B{rr}", he)
        S.put(f"C{rr}", f"{key} / revenue", italic=True)
        for i, p in enumerate(periods, start=4):
            col = get_column_letter(i)
            if key in rows_of and rev and key in flat[p] and "revenue" in flat[p]:
                S.put(f"{col}{rr}", f'=IFERROR({col}{rows_of[key]}/{col}{rev},"")', nf=NF_PCT)
        S.row += 1
    rr = S.row
    S.put(f"A{rr}", "OCF / net income")
    S.put(f"B{rr}", "תזרים שוטף / רווח נקי")
    S.put(f"C{rr}", f"{ocf_key} / {ni_key}", italic=True)
    for i, p in enumerate(periods, start=4):
        col = get_column_letter(i)
        if ocf_key in flat[p] and ni_key in flat[p]:
            S.put(f"{col}{rr}", f'=IFERROR({col}{rows_of[ocf_key]}/{col}{rows_of[ni_key]},"")', nf=NF_X)
    S.row += 1
    rr = S.row
    S.put(f"A{rr}", "Revenue growth (fiscal year on fiscal year)")
    S.put(f"B{rr}", "צמיחה בהכנסות (שנה על שנה)")
    fys = [p for p in periods if re.fullmatch(r"FY\d{4}", p)]
    for a, b in zip(fys, fys[1:]):
        ca, cb = get_column_letter(4 + periods.index(a)), get_column_letter(4 + periods.index(b))
        if "revenue" in flat[a] and "revenue" in flat[b]:
            S.put(f"{cb}{rr}", f'=IFERROR({cb}{rev}/{ca}{rev}-1,"")', nf=NF_PCT)
    S.row += 1
    S.put(f"A{S.row}", "הערה: יחס בכל עמודה מחושב במטבע של אותה תקופה.", italic=True)
    S.row = first_data_row

    for sec, sec_he in SECTIONS:
        if not by_sec[sec]:
            continue
        S.section(sec_he, span=3 + len(periods))
        for f in by_sec[sec]:
            rr = rows_of[f]
            assert rr == S.row, (f, rr, S.row)
            S.put(f"A{rr}", humanize(f))
            S.put(f"B{rr}", HE.get(f, ""))
            S.put(f"C{rr}", f, italic=True)
            for i, p in enumerate(periods, start=4):
                val = flat[p].get(f)
                if val is None:
                    continue
                v = val.get("v")
                if isinstance(v, bool) or v is None:
                    continue
                cell = f"{get_column_letter(i)}{rr}"
                if isinstance(v, (int, float)):
                    nf = NF_PS if (abs(v) < 10 and not float(v).is_integer()) else NF_K
                    if f.startswith(("eps_", "options_wavg", "average_deal", "series_D_implied")) or "_pct" in f or \
                            f in ("default_rate", "net_margin", "pretax_margin", "gross_margin", "equity_to_assets"):
                        nf = '0.0000' if abs(v) < 1 else NF_K1
                    S.put(cell, v, nf=nf, comment=cell_comment(val), fill=FILL_SOFT if soft(val) else None)
                else:
                    S.put(cell, str(v), comment=cell_comment(val), color=BLUE, fill=FILL_SOFT if soft(val) else None)
            S.row += 1
    return S, {"rows": rows_of, "periods": periods}


# =====================================================================================================
# per-share value by the treasury method, as formulas (closed form for the in-the-money set, iterated)
# =====================================================================================================
def treasury_rows(S: Sheet, label: str, equity_k: str, shares: str, n_rng: str, k_rng: str, iters: int = 5) -> str:
    """v0 = E/shares; v(i+1) = (E + sum over K < v(i) of n x K) / (shares + sum over K < v(i) of n).
    This is the fixed point of v = E / (shares + sum n x max(0, 1 - K / v)) that valuation.py iterates."""
    prev = S.line(f"{label}: איטרציה 0 (לפני דילול)", f"=IF({equity_k}<=0,0,{equity_k}*1000/{shares})", nf=NF_PS)
    for i in range(1, iters + 1):
        prev = S.line(f"{label}: איטרציה {i}",
                      f"=IF({equity_k}<=0,0,({equity_k}*1000+SUMPRODUCT(({k_rng}<{prev})*{n_rng}*{k_rng}))/"
                      f"({shares}+SUMPRODUCT(({k_rng}<{prev})*{n_rng})))", nf=NF_PS)
    return prev


def instruments_table(S: Sheet, items: list[tuple[str, float, float, str]]) -> tuple[str, str]:
    r0 = S.row
    S.put(f"A{r0}", "מכשיר", bold=True, fill=FILL_HEAD)
    S.put(f"B{r0}", "כמות", bold=True, fill=FILL_HEAD)
    S.put(f"C{r0}", "מחיר מימוש (ש\"ח)", bold=True, fill=FILL_HEAD)
    S.put(f"D{r0}", "מקור", bold=True, fill=FILL_HEAD)
    S.row += 1
    first = S.row
    for name, n, k, src in items:
        r = S.row
        S.put(f"A{r}", name)
        S.put(f"B{r}", n, nf=NF_INT)
        S.put(f"C{r}", k, nf='0.0000')
        S.put(f"D{r}", src, italic=True)
        S.row += 1
    last = S.row - 1
    return f"$B${first}:$B${last}", f"$C${first}:$C${last}"


def window_table(S: Sheet, years: list[str], rev: list, ebit: list, rev_src: str, ebit_src: str,
                 fx_cell: str | None = None) -> tuple[str, str, str]:
    """rows: period | revenue | EBIT_adj | margin (or USD, ILS = USD x FX when fx_cell is given)."""
    r0 = S.row
    heads = ["תקופה", "הכנסות", "EBIT_adj", "מרווח"] if not fx_cell else \
        ["תקופה", "הכנסות (אלפי דולר)", "EBIT_adj (אלפי דולר)", "הכנסות (אלפי ש\"ח)", "EBIT_adj (אלפי ש\"ח)", "מרווח"]
    for i, h in enumerate(heads, start=1):
        S.put(f"{get_column_letter(i)}{r0}", h, bold=True, fill=FILL_HEAD)
    S.row += 1
    first = S.row
    for y, rv, eb in zip(years, rev, ebit):
        r = S.row
        S.put(f"A{r}", str(y))
        S.put(f"B{r}", rv, nf=NF_K, comment=rev_src)
        S.put(f"C{r}", eb, nf=NF_K1 if not float(eb).is_integer() else NF_K, comment=ebit_src)
        if fx_cell:
            S.put(f"D{r}", f"=B{r}*{fx_cell}", nf=NF_K1)
            S.put(f"E{r}", f"=C{r}*{fx_cell}", nf=NF_K1)
            S.put(f"F{r}", f"=E{r}/D{r}", nf=NF_PCT2)
        else:
            S.put(f"D{r}", f"=C{r}/B{r}", nf=NF_PCT2)
        S.row += 1
    last = S.row - 1
    if fx_cell:
        return f"D{first}:D{last}", f"E{first}:E{last}", f"F{first}:F{last}"
    return f"B{first}:B{last}", f"C{first}:C{last}", f"D{first}:D{last}"


def normalisation_rows(S: Sheet, rev_rng: str, ebit_rng: str, m_rng: str, rev_ttm, rev_ttm_src: str) -> dict:
    out = {}
    out["m_norm"] = S.line("מרווח מנורמל m_norm (חציון המרווחים)", f"=MEDIAN({m_rng})", nf=NF_PCT2)
    out["cyc"] = S.line("מחזורי? (הפסד בחלון, או סטיית תקן של המרווח > חצי מהחציון)",
                        f"=OR(MIN({m_rng})<0,STDEV({m_rng})>0.5*MEDIAN({m_rng}))",
                        note="framework d2; lib is_cyclical (סטיית תקן מדגמית)")
    out["mean"] = S.line("ממוצע EBIT_adj בחלון", f"=AVERAGE({ebit_rng})", nf=NF_K1)
    out["median"] = S.line("חציון EBIT_adj בחלון", f"=MEDIAN({ebit_rng})", nf=NF_K1)
    out["meanrev"] = S.line("ממוצע הכנסות × m_norm", f"=AVERAGE({rev_rng})*{out['m_norm']}", nf=NF_K1)
    out["rev_ttm"] = S.line("הכנסות TTM (לנוסחה היציבה בלבד)", rev_ttm, nf=NF_K, comment=rev_ttm_src)
    out["ebit_norm"] = S.line("EBIT מנורמל (EBIT_norm)",
                              f"=IF({out['cyc']},MIN({out['mean']},{out['median']},{out['meanrev']}),"
                              f"{out['rev_ttm']}*{out['m_norm']})", nf=NF_K1, bold=True,
                              note="מחזורי: המינימום של שלושת המועמדים; יציב: הכנסות TTM × m_norm")
    return out


def hurdle_rows(S: Sheet, y10: float, y10_note: str) -> dict:
    out = {}
    out["y10"] = S.line("תשואת אג\"ח ממשלתית ל-10 שנים (y10), 3.11.2026", y10, nf=NF_PCT2, comment=y10_note)
    out["floor"] = S.line("רצפת שיעור ההיוון", HURDLE_FLOOR, nf=NF_PCT, note="חוקה: r = max(10%, y10 + 3 נקודות)")
    out["spread"] = S.line("תוספת מעל y10", HURDLE_SPREAD, nf=NF_PCT)
    out["r"] = S.line("שיעור ההיוון r", f"=MAX({out['floor']},{out['y10']}+{out['spread']})", nf=NF_PCT, bold=True)
    return out


def scenario_rows(S: Sheet, rows: list[tuple[str, object, float, str]], price: str) -> dict:
    r0 = S.row
    for i, h in enumerate(["תרחיש", "שווי למניה (ש\"ח)", "הסתברות", "תיאור"], start=1):
        S.put(f"{get_column_letter(i)}{r0}", h, bold=True, fill=FILL_HEAD)
    S.row += 1
    first = S.row
    out = {}
    for name, value, prob, desc in rows:
        r = S.row
        S.put(f"A{r}", name)
        S.put(f"B{r}", value, nf=NF_PS)
        S.put(f"C{r}", prob, nf=NF_PCT, fill=FILL_KEY)
        S.put(f"D{r}", desc, italic=True)
        out[name] = f"B{r}"
        S.row += 1
    last = S.row - 1
    out["sum_p"] = S.line("סכום ההסתברויות", f"=SUM(C{first}:C{last})", nf=NF_PCT)
    out["pw"] = S.line("שווי משוקלל הסתברות", f"=SUMPRODUCT(B{first}:B{last},C{first}:C{last})", nf=NF_PS, bold=True)
    out["p_base"] = S.line("מחיר / שווי בסיס", f"={price}/{out[rows[2][0]]}", nf=NF_X)
    out["p_pw"] = S.line("מחיר / שווי משוקלל", f"={price}/{out['pw']}", nf=NF_X)
    out["upside"] = S.line("מרחק המחיר משווי הבסיס (שלילי = המחיר גבוה מהשווי)", f"={out[rows[2][0]]}/{price}-1", nf=NF_PCT)
    return out


def grid_rows(S: Sheet, grid: dict, price: str, note: str) -> dict:
    rs = sorted({k[0] for k in grid})
    gs = sorted({k[1] for k in grid})
    r0 = S.row
    S.put(f"A{r0}", "r \\ g", bold=True, fill=FILL_HEAD)
    for j, gv in enumerate(gs):
        S.put(f"{get_column_letter(2 + j)}{r0}", gv, nf=NF_PCT, bold=True, fill=FILL_HEAD, color=BLACK)
    S.row += 1
    first = S.row
    for rv in rs:
        r = S.row
        S.put(f"A{r}", rv, nf=NF_PCT, bold=True, color=BLACK)
        for j, gv in enumerate(gs):
            S.put(f"{get_column_letter(2 + j)}{r}", grid[(rv, gv)], nf=NF_PS, comment=note if j == 0 and rv == rs[0] else None)
        S.row += 1
    rng = f"B{first}:{get_column_letter(1 + len(gs))}{S.row - 1}"
    out = {"min": S.line("מינימום ברשת", f"=MIN({rng})", nf=NF_PS),
           "max": S.line("מקסימום ברשת", f"=MAX({rng})", nf=NF_PS)}
    out["d3"] = S.line("שווי הבסיס מעל המחיר בכל הרשת? (D3)", f"={out['min']}>{price}")
    return out


# =====================================================================================================
# valuation sheets
# =====================================================================================================
def build_val_paymeant(wb: Workbook, g: dict) -> tuple[Sheet, dict, list]:
    S = Sheet(wb, "פיימנט - הערכה", [62, 16, 18, 16, 16, 16], rtl=True)
    S.title_rows("פיימנט (1180876): הערכת שווי לפי החוקה, בנוסחאות",
                 "אלפי ש\"ח אלא אם צוין; למניה: ש\"ח למניה מדוללת. כחול = קלט מ-valuation.py; שחור = נוסחה; "
                 "צהוב = הנחת מפתח. בסיס מלווה: עלות המימון היא עלות תפעולית (screen_spec 3.1).")
    C = {}
    checks = []
    S.section("1. קלטי שוק")
    C["price"] = S.line("מחיר (ש\"ח), נעילה 3.11.2026", g["PRICE"], nf=NF_PS, comment="valuation.py PRICE; output.txt §0")
    C["shares"] = S.line("מניות רגילות (בסיסי)", g["SHARES"], nf=NF_INT, comment="valuation.py SHARES (מספר המניות בבורסה)")
    C["mcap"] = S.line("שווי שוק (אלפי ש\"ח)", f"={C['price']}*{C['shares']}/1000", nf=NF_K1)
    checks.append(("פיימנט", "שווי שוק", C["mcap"], g["MCAP"]))
    C.update({f"h_{k}": v for k, v in hurdle_rows(S, g["Y10_ILS"], "valuation.py Y10_ILS: 4.29% YTM on ממשל שקלית 0537 "
                                                    "(TheMarker, 3.11.2026); generic 4.162% (Trading Economics)").items()})
    checks.append(("פיימנט", "שיעור היוון r", C["h_r"], g["R"]))
    C["tax"] = S.line("שיעור מס סטטוטורי", g["T_STATUTORY"], nf=NF_PCT, comment="valuation.py T_STATUTORY (paymeant_fy2025 p.106)")
    S.blank()

    S.section("2. נרמול EBIT: חלון השנים FY2021-FY2025 (framework d2; screen_spec 2.2-2.3)")
    fy = g["FY"]
    rev_rng, ebit_rng, m_rng = window_table(
        S, fy, [g["REV"][y] for y in fy], [g["EBIT_ADJ"][y] for y in fy],
        "valuation.py REV (from financials.json; see 'פיימנט - נתונים')",
        "valuation.py EBIT_ADJ: operating profit before other items; the IPO share-based pay of note 19e stays a cost; "
        "the 1,188 termination gain of 2022 is removed (screen_spec 2.3)")
    n = normalisation_rows(S, rev_rng, ebit_rng, m_rng, g["REV"]["TTM"], "valuation.py REV['TTM'] (FY2025 + H1 2026 - H1 2025)")
    C.update({f"n_{k}": v for k, v in n.items()})
    checks += [("פיימנט", "m_norm", n["m_norm"], g["n_base"].m_norm), ("פיימנט", "מחזורי", n["cyc"], g["n_base"].cyclical),
               ("פיימנט", "EBIT_norm", n["ebit_norm"], g["n_base"].ebit_norm)]
    S.blank()

    S.section("3. רווחי בעלים מנורמלים (framework d1)")
    C["nopat"] = S.line("EBIT_norm × (1 - מס)", f"={n['ebit_norm']}*(1-{C['tax']})", nf=NF_K1)
    C["da"] = S.line("פחת והפחתות TTM", g["DA"]["TTM"], nf=NF_K, comment="valuation.py DA['TTM'], including ROU depreciation and the amortisation of capitalised development")
    C["maint"] = S.line("השקעה תחזוקתית (Maint CapEx)", g["maint"], nf=NF_K1,
                        comment="valuation.py maint = max(CapEx at the H1 2026 run-rate - growth CapEx, D&A); never below D&A")
    C["oe"] = S.line("רווחי בעלים מנורמלים (OE_norm)", f"={C['nopat']}+{C['da']}-{C['maint']}", nf=NF_K1, bold=True,
                     note="אין החזרה של תשלום מבוסס מניות")
    checks.append(("פיימנט", "OE_norm", C["oe"], g["oe_norm"]))
    S.blank()

    S.section("4. שווי הפעילות: DCF ל-10 שנים, בסיס מלווה (framework d4)")
    C["g"] = S.line("צמיחה בבסיס g", g["G_BASE"], nf=NF_PCT, fill=FILL_KEY, comment="valuation.py G_BASE: assumed, CPI-level nominal growth")
    C["gcap"] = S.line("תקרת צמיחה", MAX_GROWTH, nf=NF_PCT, note="framework d4")
    C["g1"] = S.line("g1 = min(g, תקרה)", f"=MIN({C['g']},{C['gcap']})", nf=NF_PCT)
    C["roiic"] = S.line("ROIIC (תשואה על הון מושקע חדש)", g["roiic"], nf=NF_PCT2, fill=FILL_KEY,
                        comment="valuation.py roiic = OE_norm / tangible equity")
    C["reinv"] = S.line("שיעור ההשקעה מחדש = g1 / ROIIC", f"=IF({C['g1']}>0,MIN({C['g1']}/{C['roiic']},1),0)", nf=NF_PCT2)
    C["gT_in"] = S.line("צמיחה טרמינלית (קלט)", MAX_TERMINAL_GROWTH, nf=NF_PCT)
    C["gT"] = S.line("gT = min(קלט, 2.5%)", f"=MIN({C['gT_in']},{MAX_TERMINAL_GROWTH})", nf=NF_PCT)
    C["roiicT"] = S.line("ROIIC טרמינלי = max(r, r)", f"=MAX({C['h_r']},{C['h_r']})", nf=NF_PCT)
    C["reinvT"] = S.line("שיעור השקעה טרמינלי = gT / ROIIC_T", f"=MAX({C['gT']},0)/{C['roiicT']}", nf=NF_PCT2)
    r0 = S.row
    for i, h in enumerate(["שנה", "רווחי בעלים", "שיעור השקעה", "תזרים חופשי", "מקדם היוון", "ערך נוכחי"], start=1):
        S.put(f"{get_column_letter(i)}{r0}", h, bold=True, fill=FILL_HEAD)
    S.row += 1
    t0 = S.row
    S.put(f"A{t0}", 0, color=BLACK)
    S.put(f"B{t0}", f"={C['oe']}", nf=NF_K1)
    S.put(f"C{t0}", f"={C['reinv']}", nf=NF_PCT2)
    S.put(f"D{t0}", f"=-B{t0}*C{t0}", nf=NF_K1)
    S.put(f"E{t0}", 1, nf='0.0000', color=BLACK)
    S.put(f"F{t0}", f"=D{t0}*E{t0}", nf=NF_K1)
    S.row += 1
    for t in range(1, 11):
        r = S.row
        S.put(f"A{r}", t, color=BLACK)
        S.put(f"B{r}", f"=B{r - 1}*(1+{C['g1']})", nf=NF_K1)
        S.put(f"C{r}", f"={C['reinv']}" if t < 10 else f"={C['reinvT']}", nf=NF_PCT2)
        S.put(f"D{r}", f"=B{r}*(1-C{r})", nf=NF_K1)
        S.put(f"E{r}", f"=1/(1+{C['h_r']})^A{r}", nf='0.0000')
        S.put(f"F{r}", f"=D{r}*E{r}", nf=NF_K1)
        S.row += 1
    t10 = S.row - 1
    C["tv"] = S.line("ערך טרמינלי (בשנה 10)", f"=B{t10}*(1+{C['gT']})*(1-{C['gT']}/{C['roiicT']})/({C['h_r']}-{C['gT']})", nf=NF_K1)
    C["pv_tv"] = S.line("ערך נוכחי של הערך הטרמינלי", f"={C['tv']}/(1+{C['h_r']})^10", nf=NF_K1)
    C["ops"] = S.line("שווי הפעילות (DCF)", f"=SUM(F{t0}:F{t10})+{C['pv_tv']}", nf=NF_K1, bold=True)
    C["tv_share"] = S.line("חלק הערך הטרמינלי", f"={C['pv_tv']}/{C['ops']}", nf=NF_PCT)
    checks.append(("פיימנט", "שווי הפעילות (DCF)", C["ops"], g["dcf_b"].operations_value))
    S.blank()

    S.section("5. מהשווי של הפעילות להון (framework d3, גשר ההון)")
    lease = g["dcf_b"].operations_value - g["dcf_base"]
    assert abs(lease - g["LEASES"]["2026-06-30"]) < 1e-6, "Paymeant bridge is no longer 'operations - leases'"
    C["xs"] = S.line("+ מזומן עודף (מעל חודשיים של עלויות)", g["xs_cash"], nf=NF_K, comment="valuation.py xs_cash")
    C["lease"] = S.line("- התחייבויות חכירה, 30.6.2026", g["LEASES"]["2026-06-30"], nf=NF_K, comment="valuation.py LEASES (paymeant_h1_2026)")
    C["debt"] = S.line("- חוב פיננסי", 0, nf=NF_K, comment="Lender basis: the warehouse credit funds the loan book; its cost is already "
                                                          "inside EBIT, so it is not deducted again (screen_spec 3.1, 4.7)")
    C["nci"] = S.line("- זכויות שאינן מקנות שליטה ומניות בכורה", g["NCI"] + g["PREFERRED"], nf=NF_K)
    C["eq"] = S.line("הון לבעלי המניות", f"={C['ops']}+{C['xs']}-{C['lease']}-{C['debt']}-{C['nci']}", nf=NF_K1, bold=True)
    checks.append(("פיימנט", "הון בבסיס", C["eq"], g["dcf_base"]))
    C["eq_epv"] = S.line("לייחוס: הון לפי EPV (OE_norm / r, בניכוי חכירות)", f"={C['oe']}/{C['h_r']}+{C['xs']}-{C['lease']}-{C['debt']}-{C['nci']}", nf=NF_K1)
    checks.append(("פיימנט", "הון לפי EPV", C["eq_epv"], g["epv_l"]))
    S.blank()

    S.section("6. למניה מדוללת (שיטת האוצר, מכשיר אחר מכשיר)")
    items = [(o[0], o[1], o[2], o[3]) for o in g["OPTIONS"]] + \
            [("שארית אופציות ביאור 17 שלא זוהו (נגזר)", g["RES_N"], g["RES_K"], "valuation.py residual_note17 (paymeant_fy2025 p.112)")]
    n_rng, k_rng = instruments_table(S, items)
    v = treasury_rows(S, "בסיס", C["eq"], C["shares"], n_rng, k_rng)
    C["base"] = S.line("שווי בסיס למניה מדוללת (ש\"ח)", f"={v}", nf=NF_PS, bold=True)
    checks.append(("פיימנט", "שווי בסיס למניה", C["base"], g["base"]))
    v_epv = treasury_rows(S, "EPV", C["eq_epv"], C["shares"], n_rng, k_rng)
    C["epv_ps"] = S.line("לייחוס: EPV למניה מדוללת", f"={v_epv}", nf=NF_PS)
    checks.append(("פיימנט", "EPV למניה", C["epv_ps"], g["vr"].methods["EPV, lender basis (d3)"]))
    S.blank()

    S.section("7. תרחישים (output.txt §4)")
    sc = scenario_rows(S, [
        ("גרוע", g["worst_low"], g["SCENARIO_P"]["worst"], f"run-off of the 30.6.2026 book (low end; high end {g['worst_high']:.3f}); excludes SPC indemnities and the 360 guarantee"),
        ("שמרני", g["conservative"], g["SCENARIO_P"]["conservative"], "no moat: tangible book at amortised cost less the UNVERIFIED provision shortfall"),
        ("בסיס", f"={C['base']}", g["SCENARIO_P"]["base"], "the DCF above (g 2%, cyclical EBIT_norm)"),
        ("אופטימי", g["optimistic"], g["SCENARIO_P"]["optimistic"], "today's scale holds: TTM revenue x m_norm, g 5%"),
    ], C["price"])
    C.update({f"sc_{k}": v for k, v in sc.items()})
    checks.append(("פיימנט", "שווי משוקלל", sc["pw"], g["pw"]))
    S.blank()

    S.section("8. שיטות (output.txt §5)")
    for k, val in g["vr"].methods.items():
        S.line(k, val, nf=NF_PS, comment="valuation.py vr.methods")
    S.blank()

    S.section("9. רשת רגישות: שווי הבסיס למניה (r ± 1 נקודה, g ± 2 נקודות)")
    gr = grid_rows(S, g["grid"]["grid"], C["price"], "valuation.py grid (sensitivity_grid on the lender-basis DCF)")
    C.update({f"grid_{k}": v for k, v in gr.items()})
    S.blank()

    S.section("10. מחיר קנייה וקווי ייחוס (output.txt §5)")
    S.line("מסלול (lane)", "אין: שום מסלול לא מתאים, ולכן אין מחיר קנייה", bold=True)
    C["ncav"] = S.line("NCAV, 30.6.2026", g["ncav_v"], nf=NF_K, comment="valuation.py ncav_v")
    C["dempster"] = S.line("שווי Dempster, 30.6.2026", g["dempster"], nf=NF_K1, comment="valuation.py dempster")
    C["nn_k"] = S.line("min(2/3 NCAV, Dempster)", f"=MIN(2/3*{C['ncav']},{C['dempster']})", nf=NF_K1)
    vl = treasury_rows(S, "קו Tier C", C["nn_k"], C["shares"], n_rng, k_rng, iters=4)
    C["line_c"] = S.line("קו ה-net-net של Tier C (ייחוס בלבד, לא מחיר קנייה)", f"={vl}", nf=NF_PS, bold=True)
    checks.append(("פיימנט", "קו Tier C", C["line_c"], g["tier_c_line"]))
    C["line_c_margin"] = S.line("המרחק של הקו משווי הבסיס", f"=1-{C['line_c']}/{C['base']}", nf=NF_PCT2)
    C["price_line"] = S.line("מחיר / קו Tier C", f"={C['price']}/{C['line_c']}", nf=NF_X)
    C["te"] = S.line("הון מוחשי, 30.6.2026", g["TE_J26"], nf=NF_K, comment="valuation.py TE_J26")
    C["bank_k"] = S.line("מסלול הבנקים: min(1.2 × הון מוחשי, 10 × רווח נקי מנורמל)",
                         f"=MIN(1.2*{C['te']},10*{C['nopat']})", nf=NF_K1, comment="valuation.py bank_line (screen_spec 4.7)")
    vb = treasury_rows(S, "קו הבנקים", C["bank_k"], C["shares"], n_rng, k_rng, iters=4)
    C["line_bank"] = S.line("קו מסלול הבנקים למניה (ייחוס בלבד, לא מחיר קנייה)", f"={vb}", nf=NF_PS)
    checks.append(("פיימנט", "קו מסלול הבנקים", C["line_bank"], g["ps"](g["bank_line"])))
    S.line("תוספות נתונים (+5 כל אחת, תקרה +10)", ", ".join(g["DATA_FLAGS"]))
    S.blank()

    S.section("11. נזילות וגודל (framework e2; screen_spec X5)")
    C["med"] = S.line("מחזור יומי חציוני, 60 ימי מסחר (ש\"ח)", g["med"], nf=NF_INT, comment="valuation.py med (Bizportal, 4.8-3.11.2026)")
    C["p25"] = S.line("אחוזון 25 של המחזור היומי (ש\"ח)", g["p25"], nf=NF_K1, comment="valuation.py p25")
    C["liq"] = S.line("תקרת נזילות = 20 ימים × 20% × אחוזון 25 (ש\"ח)", f"=20*0.2*{C['p25']}", nf=NF_INT)
    checks.append(("פיימנט", "תקרת נזילות", C["liq"], g["size"]["liquidity_amount"]))
    C["floor"] = S.line("רצפת נזילות (חציון, ש\"ח)", g["LIQ_FLOOR"], nf=NF_INT)
    S.line("עובר את הרצפה?", f"={C['med']}>={C['floor']}")
    S.line("קלי מלא", g["size"]["kelly_full"], nf=NF_PCT)
    for k, val in g["size"]["limits"].items():
        S.line(f"מגבלה: {k}", val, nf=NF_PCT)
    C["size"] = S.line("גודל מוצע (מהנכסים)", g["size"]["size"], nf=NF_PCT, bold=True, comment=f"binding: {g['size']['binding']}")
    S.blank()

    S.section("12. מה המחיר מגלם (framework d8)")
    S.line("צמיחה שנתית ל-10 שנים על OE_norm, עם השקעה", g["g_impl"], nf=NF_PCT)
    S.line("כנ\"ל, אילו הצמיחה הייתה חינם", g["g_impl_free"], nf=NF_PCT)
    S.line("על קנה המידה של היום (OE אופטימי)", g["g_impl_opt"], nf=NF_PCT)
    return S, C, checks


def build_val_gilat(wb: Workbook, g: dict) -> tuple[Sheet, dict, list]:
    S = Sheet(wb, "גילת - הערכה", [62, 16, 18, 16, 16, 16], rtl=True)
    S.title_rows("גילת טלקום (1080597): הערכת שווי לפי החוקה, בנוסחאות",
                 "אלפי ש\"ח אלא אם צוין; למניה: ש\"ח. חלון השנים בדולרים הומר בשער אחד, 3.157 (בנק ישראל, 3.11.2026). "
                 "כחול = קלט מ-valuation.py; שחור = נוסחה; צהוב = הנחת מפתח.")
    C = {}
    checks = []
    S.section("1. קלטי שוק")
    C["price"] = S.line("מחיר (ש\"ח), נעילה 3.11.2026", g["PRICE"], nf=NF_PS, comment="valuation.py PRICE; output.txt §0")
    C["shares"] = S.line("מניות רשומות למסחר, 3.11.2026", g["SHARES_LISTED"], nf=NF_INT, comment="valuation.py SHARES_LISTED")
    C["mcap"] = S.line("שווי שוק (אלפי ש\"ח)", f"={C['price']}*{C['shares']}/1000", nf=NF_K1)
    checks.append(("גילת", "שווי שוק", C["mcap"], g["MCAP"]))
    C["fx"] = S.line("שער דולר-שקל (יציג, 3.11.2026)", g["FX"], nf=NF_FX, comment="valuation.py FX (Bank of Israel)")
    C.update({f"h_{k}": v for k, v in hurdle_rows(S, g["Y10_IL"], "valuation.py Y10_IL: Israel 10-year 4.16% (Trading Economics, 3.11.2026); US 4.91%").items()})
    checks.append(("גילת", "שיעור היוון r", C["h_r"], g["R"]))
    C["tax"] = S.line("שיעור מס סטטוטורי", g["TAX"], nf=NF_PCT, comment="valuation.py TAX")
    S.blank()

    S.section("2. נרמול EBIT: חלון FY2020-FY2025, שנים מלאות (framework d2)")
    years = list(g["YEARS"])
    rev_rng, ebit_rng, m_rng = window_table(
        S, [f"FY{y}" for y in years], [g["REV_USD"][y] for y in years], [g["EBIT_ADJ_USD"][y] for y in years],
        "valuation.py REV_USD (FY2020 from the company's FY2022 report; FY2021-FY2025 from financials.json)",
        "valuation.py EBIT_ADJ_USD: operating profit less other income (FY2020) and less the 2025 satellite-supplier credit "
        "(USD 1,423k, an upper-bound estimate, UNVERIFIED)", fx_cell=C["fx"])
    n = normalisation_rows(S, rev_rng, ebit_rng, m_rng, g["REV_ADJ_TTM"], "valuation.py REV_ADJ_TTM (TTM revenue less the one-off war equipment)")
    C.update({f"n_{k}": v for k, v in n.items()})
    checks += [("גילת", "m_norm", n["m_norm"], g["norm_w"].m_norm), ("גילת", "מחזורי", n["cyc"], g["norm_w"].cyclical),
               ("גילת", "EBIT_norm", n["ebit_norm"], g["EBIT_NORM"])]
    S.line("לייחוס: EBIT_adj ב-TTM", g["EBIT_ADJ_TTM"], nf=NF_K1, comment="valuation.py EBIT_ADJ_TTM")
    S.line("TTM / EBIT_norm", f"=B{S.row - 1}/{n['ebit_norm']}", nf=NF_X)
    S.blank()

    S.section("3. רווחי בעלים מנורמלים (framework d1)")
    C["amort"] = S.line("הפחתת נכסים שנרכשו (אלפי ש\"ח)", g["AMORT_ACQ"], nf=NF_K1, comment="valuation.py AMORT_ACQ = USD 809k x 3.157")
    C["dep"] = S.line("פחת והפחתות TTM, כולל ROU ו-IRU", g["DEP_TTM"], nf=NF_K1, comment="valuation.py DEP_TTM")
    C["maint"] = S.line("השקעה תחזוקתית (לא פחות מהפחת)", g["MAINT_TTM"], nf=NF_K1, comment="valuation.py MAINT_TTM: floored at depreciation, so leases stay a cost")
    C["oe"] = S.line("רווחי בעלים מנורמלים (OE_norm)", f"=({n['ebit_norm']}+{C['amort']})*(1-{C['tax']})+{C['dep']}-{C['maint']}", nf=NF_K1, bold=True)
    checks.append(("גילת", "OE_norm", C["oe"], g["OE_NORM"]))
    S.blank()

    S.section("4. שווי הפעילות: EPV (שווה ל-DCF כשהצמיחה 0% או ROIIC = r)")
    C["ops"] = S.line("שווי הפעילות = OE_norm / r", f"={C['oe']}/{C['h_r']}", nf=NF_K1, bold=True)
    checks.append(("גילת", "שווי הפעילות", C["ops"], g["dcf_base"].operations_value))
    S.blank()

    S.section("5. גשר ההון (framework d3)")
    C["cash_pf"] = S.line("מזומן פרו פורמה, 3.11.2026", g["CASH_PF"], nf=NF_K1, comment="valuation.py CASH_PF")
    C["opex"] = S.line("עלויות תפעול במזומן, TTM (כולל תשלומי חכירה)", g["CASH_OPEX_TTM"], nf=NF_K, comment="valuation.py CASH_OPEX_TTM")
    C["xs"] = S.line("+ מזומן עודף = מזומן - חודשיים של עלויות", f"=MAX({C['cash_pf']}-{C['opex']}*2/12,0)", nf=NF_K1)
    checks.append(("גילת", "מזומן עודף", C["xs"], g["EXCESS"]))
    C["lease"] = S.line("- התחייבויות חכירה", g["LEASES"], nf=NF_K, comment="valuation.py LEASES")
    C["iru"] = S.line("- עלות צפויה של קווי IRU שלא ינוצלו (25% מהמקרה החצי-מת, אחרי מס)", g["IRU_EXP_BASE"], nf=NF_K1,
                      fill=FILL_SOFT, comment="valuation.py IRU_EXP_BASE; the IRU schedule is UNVERIFIED")
    C["fxadj"] = S.line("- תיקון הגשר לשער 3.157 (התחייבויות דולריות נטו)", g["FX_BRIDGE_ADJ"], nf=NF_K1, comment="valuation.py FX_BRIDGE_ADJ")
    C["eq"] = S.line("הון לפני סדרה ד'", f"={C['ops']}+{C['xs']}-{C['lease']}-{C['iru']}-{C['fxadj']}", nf=NF_K1, bold=True)
    checks.append(("גילת", "הון לפני סדרה ד'", C["eq"], g["e_base"]))
    S.blank()

    S.section("6. למניה: סדרה ד' ממירה רק אם זה שווה יותר מהערך הנקוב (ש\"ח 1 ערך נקוב = מניה אחת)")
    C["sd_par"] = S.line("סדרה ד': ערך נקוב (ש\"ח)", g["SERIES_D_PAR"], nf=NF_INT, comment="valuation.py SERIES_D_PAR")
    C["sd_px"] = S.line("מחיר המרה (ש\"ח)", g["SERIES_D_CONV_PRICE"], nf='0.00')
    items = [(f"אופציות/כתבי אופציה #{i + 1}", nn, k, "valuation.py OPTIONS") for i, (nn, k) in enumerate(g["OPTIONS"])]
    n_rng, k_rng = instruments_table(S, items)
    C["eq_debt"] = S.line("הון למניות אם סדרה ד' נשארת חוב (בניכוי הערך הנקוב)", f"={C['eq']}-{C['sd_par']}/1000", nf=NF_K1)
    C["sh_conv"] = S.line("מניות אם סדרה ד' ממירה", f"={C['shares']}+{C['sd_par']}/{C['sd_px']}", nf=NF_INT)
    vd = treasury_rows(S, "חוב", C["eq_debt"], C["shares"], n_rng, k_rng, iters=4)
    vc = treasury_rows(S, "המרה", C["eq"], C["sh_conv"], n_rng, k_rng, iters=4)
    C["base"] = S.line("שווי בסיס למניה (ש\"ח) = max(0, min(המרה, חוב))", f"=MAX(0,MIN({vc},{vd}))", nf=NF_PS, bold=True)
    checks.append(("גילת", "שווי בסיס למניה", C["base"], g["v_base"]))
    S.blank()

    S.section("7. תרחישים (output.txt §5)")
    sc = scenario_rows(S, [
        ("גרוע", g["VALS"]["worst"], g["PROBS"]["worst"], "worst case ten years out: claims exceed value"),
        ("שמרני", g["VALS"]["conservative"], g["PROBS"]["conservative"], "Vodacom is not renewed"),
        ("בסיס", f"={C['base']}", g["PROBS"]["base"], "the EPV above (EBIT_norm over FY2020-FY2025)"),
        ("אופטימי", g["VALS"]["optimistic"], g["PROBS"]["optimistic"], "the TTM run-rate persists, net of the IRU accounting gap"),
    ], C["price"])
    C.update({f"sc_{k}": v for k, v in sc.items()})
    checks.append(("גילת", "שווי משוקלל", sc["pw"], g["v_pw"]))
    S.blank()

    S.section("8. שיטות (output.txt §6)")
    for k, val in g["methods"].items():
        S.line(k, val, nf=NF_PS, comment="valuation.py methods")
    for k, val in g["asset_ps"].items():
        S.line(f"רצפת נכסים: {k}", val, nf=NF_PS, comment="valuation.py asset_ps")
    S.blank()

    S.section("9. רשת רגישות: שווי הבסיס למניה (r ± 1 נקודה, g ± 2 נקודות)")
    gr = grid_rows(S, g["grid"]["grid"], C["price"], "valuation.py grid (sensitivity_grid)")
    C.update({f"grid_{k}": v for k, v in gr.items()})
    S.blank()

    S.section("10. מרווח ביטחון וקו ה-net-net (Tier C)")
    m = g["margin"]
    S.line("מסלול", "C (מציאה, תת-כלל מחזורי). אף מסלול אינו מתקיים היום", bold=True)
    S.line("מרווח בסיס של Tier C", m.base_margin, nf=NF_PCT)
    S.line("תוספות נתונים (" + ", ".join(g["DATA_FLAGS"]) + ")", m.data_addition, nf=NF_PCT)
    S.line("מרווח כולל", f"=B{S.row - 2}+B{S.row - 1}", nf=NF_PCT)
    C["ncav"] = S.line("NCAV, 30.6.2026", g["NCAV"], nf=NF_K, comment="valuation.py NCAV")
    C["dempster"] = S.line("שווי Dempster, 30.6.2026", g["DEMPSTER"], nf=NF_K1, comment="valuation.py DEMPSTER")
    C["line_c"] = S.line("קו ה-net-net = min(2/3 NCAV, Dempster) למניה (אינו מחיר קנייה חי)",
                         f"=MIN(2/3*{C['ncav']},{C['dempster']})*1000/{C['shares']}", nf=NF_PS, bold=True)
    checks.append(("גילת", "קו net-net", C["line_c"], g["NETNET_LINE"]))
    C["price_line"] = S.line("מחיר / קו net-net", f"={C['price']}/{C['line_c']}", nf=NF_X)
    S.line("קו net-net פרו פורמה, 3.11.2026", g["NETNET_LINE_PF"], nf=NF_PS, comment="valuation.py NETNET_LINE_PF")
    S.blank()

    S.section("11. נזילות וגודל (framework e2)")
    C["med"] = S.line("מחזור יומי חציוני, 60 ימי מסחר (ש\"ח)", g["TURNOVER_MEDIAN_60"], nf=NF_INT, comment="valuation.py TURNOVER_MEDIAN_60")
    C["p25"] = S.line("אחוזון 25 של המחזור היומי (ש\"ח)", g["TURNOVER_P25_60"], nf=NF_INT, comment="valuation.py TURNOVER_P25_60")
    C["liq"] = S.line("תקרת נזילות = 20 ימים × 20% × אחוזון 25 (ש\"ח)", f"=20*0.2*{C['p25']}", nf=NF_INT)
    checks.append(("גילת", "תקרת נזילות", C["liq"], g["size"]["liquidity_amount"]))
    S.line("קלי מלא", g["size"]["kelly_full"], nf=NF_PCT)
    for k, val in g["size"]["limits"].items():
        S.line(f"מגבלה: {k}", val, nf=NF_PCT)
    C["size"] = S.line("גודל מוצע (מהנכסים)", g["size"]["size"], nf=NF_PCT, bold=True, comment=f"binding: {g['size']['binding']}")
    S.blank()

    S.section("12. מה המחיר מגלם, והתחייבות בזק")
    S.line("צמיחה שנתית ל-10 שנים על OE_norm", g["IG_NORM"], nf=NF_PCT)
    S.line("כנ\"ל על רווחי ה-TTM", g["IG_TTM"], nf=NF_PCT)
    S.line("IRU לבזק: תמורה מחויבת", g["IRU_COMMITTED"], nf=NF_K, fill=FILL_SOFT, comment="valuation.py IRU_COMMITTED (UNVERIFIED schedule)")
    S.line("IRU לבזק: לא שולם", g["IRU_UNPAID_ALL"], nf=NF_K, fill=FILL_SOFT, comment="valuation.py IRU_UNPAID_ALL (UNVERIFIED)")
    S.line("IRU לבזק: לא שולם, על קווים שכבר בשירות", g["IRU_UNPAID_IN_SERVICE"], nf=NF_K, fill=FILL_SOFT, comment="valuation.py IRU_UNPAID_IN_SERVICE (UNVERIFIED)")
    S.line("שנה שבה נדרש כסף חדש במקרה הגרוע", g["NEW_MONEY_YEAR"], nf='0', comment="valuation.py NEW_MONEY_YEAR (E1 runway)")
    return S, C, checks


# =====================================================================================================
# checklist sheets
# =====================================================================================================
def parse_checklist(path: pathlib.Path) -> list[dict]:
    rows, section, header = [], None, None
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^##\s+([A-H])\.\s+(.*)$", line)
        if m:
            section, header = f"{m.group(1)}. {re.sub(r'\s*\(\d+\)$', '', m.group(2))}", None
            continue
        if line.startswith("## "):
            section, header = None, None
            continue
        if section and line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if header is None:
                header = cells
                continue
            if set("".join(cells)) <= set("-: "):
                continue
            if len(cells) > len(header):
                cells = cells[:len(header) - 1] + [" | ".join(cells[len(header) - 1:])]
            rec = dict(zip(header, cells))
            clean = {k: re.sub(r"\*\*|`", "", v) for k, v in rec.items()}
            rows.append({"section": section, **clean})
    return rows


def outcome(ans: str) -> str:
    a = ans.lower().strip()
    if a.startswith("n/a"):
        return "n/a"
    if a.startswith("cannot"):
        return "cannot assess"
    if a.startswith(("yes", "pass")):
        return "pass"
    if a.startswith(("no", "fail")):
        return "fail"
    return "other"


def build_checklist_sheet(wb: Workbook, title: str, company: str, rows: list[dict]) -> dict:
    S = Sheet(wb, title, [8, 26, 60, 9, 22, 22, 90])
    S.title_rows(f"{company}: רשימת הבדיקה של שער ה-CIO (60 פריטים)", "מתוך checklist.md. 'cannot assess here' נחשב כישלון.", span=7)
    hdr = S.row
    for i, h in enumerate(["#", "קבוצה", "שאלה", "סוג", "חל על / נבדק כ", "תשובה", "ראיות"], start=1):
        S.put(f"{get_column_letter(i)}{hdr}", h, bold=True, fill=FILL_HEAD)
    S.ws.freeze_panes = S.ws[f"A{hdr + 1}"]
    S.row += 1
    counts: dict = {}
    fails, cannot = [], []
    for rec in rows:
        r = S.row
        q = next((v for k, v in rec.items() if k.startswith("Question")), "")
        ev = next((v for k, v in rec.items() if k.startswith("Evidence")), "")
        applies = rec.get("Applies / run as", "")
        typ, ans = rec.get("Type", ""), rec.get("Answer", "")
        res = outcome(ans)
        counts[(typ, res)] = counts.get((typ, res), 0) + 1
        if typ == "VETO" and res == "fail":
            fails.append(rec["#"])
        if typ == "VETO" and res == "cannot assess":
            cannot.append(rec["#"])
        fill = FILL_SOFT if res in ("fail", "cannot assess") else None
        for i, val in enumerate([rec.get("#", ""), rec["section"], q, typ, applies, ans, ev], start=1):
            S.put(f"{get_column_letter(i)}{r}", val, wrap=i in (3, 7), fill=fill if i == 6 else None, color=BLACK)
        S.row += 1
    return {"counts": counts, "veto_fail": fails, "veto_cannot": cannot, "n": len(rows)}


# =====================================================================================================
# summary, checks and sources
# =====================================================================================================
FALSIFY = {
    "paymeant": [
        "מימון: בדוח השנתי 2026 (עד 31.3.2027) מסגרות מחויבות ל-24 חודשים לפחות משני מממנים לא קשורים, שמכסות את "
        "האשראי המנוצל; אף בנק אינו מחזיק יותר מ-50% מהאשראי המנוצל; והחשיפות לשיפויי ה-SPC ולערבות 360 מכומתות",
        "אשראי: בדוח הרבעון הראשון 2027 (עד 31.5.2027) פיגורים של 1-90 יום ועוד הלוואות בכשל עד 2.65% מהתיק במאזן, "
        "וכיסוי הפרשה של 50% לפחות",
        "קנה מידה: בדוח השנתי 2026 ובדוח החציוני 2027 (עד 31.8.2027) רווח לפני מס, לפני היוון פיתוח נטו, של 24,460 "
        "אלפי ש\"ח לפחות (רמת ה-TTM), כשהחוזר בתוקף",
    ],
    "gilat_telecom": [
        "פרמיית המלחמה: עד 31.1.2027 הזמנות 2027 מלקוחות ביטחוניים וממשלתיים בישראל בהיקף של כ-110 מיליון ש\"ח "
        "כולל מע\"מ לפחות (רמת 2026)",
        "בזק: בדוח השנתי 2026 (עד 31.3.2027) גילוי יתרת תמורת ה-IRU ולוח התשלומים, והרצה מחדש שמראה מזומן מעל "
        "חודשיים של עלויות עד 2031 עם ליבה אפסית",
        "Vodacom: עד 31.3.2027 חידוש חוזה Vodacom DRC ל-24 חודשים לפחות, במיליון דולר לחודש לפחות",
    ],
}


def build_summary(wb: Workbook, P: dict, G: dict, gp: dict, gg: dict, ckp: dict, ckg: dict) -> Sheet:
    S = Sheet(wb, "סיכום", [52, 42, 42, 60])
    S.title_rows("שתי חברות בבורסת תל אביב לפי חוקת הקרן (מהדורה 4): סיכום, 3.11.2026",
                 "שחור = נוסחה; ירוק = קישור לגיליון אחר; כחול = קלט מקובצי המחקר. המזכרים המלאים: research/<חברה>/thesis_he.md",
                 span=4)
    hdr = S.row
    for i, h in enumerate(["פריט", "פיימנט", "גילת טלקום", "הערה"], start=1):
        S.put(f"{get_column_letter(i)}{hdr}", h, bold=True, fill=FILL_HEAD)
    S.row += 1
    Pv, Gv = P["sheet"], G["sheet"]

    def row(label, a, b, nf=None, note=None, bold=False, wrap=False):
        r = S.row
        S.put(f"A{r}", label, bold=bold)
        S.put(f"B{r}", a, nf=nf, bold=bold, wrap=wrap)
        S.put(f"C{r}", b, nf=nf, bold=bold, wrap=wrap)
        if note:
            S.put(f"D{r}", note, italic=True, wrap=True)
        S.row += 1
        return r

    def link(sheet: Sheet, cell: str) -> str:
        return f"={sheet.ref(cell)}"

    row("חברה", "פיימנט טכנולוגיות פיננסיות בע\"מ", "גילת טלקום גלובל בע\"מ")
    row("מספר נייר ערך", 1180876, 1080597, nf='0')
    row("מה העסק", "מלווה צרכני בנקודת המכירה (BNPL), במימון מסגרות בנקאיות לפי דרישה ומכירת תיקים",
        "משווקת קיבולת לוויינית וקווי סיבים של אחרים; ביטחון, ספקית אינטרנט ואפריקה", wrap=True)
    row("פסק דין", "NO_THESIS (אין תזה)", "NO_THESIS (אין תזה)", bold=True)
    row("מסלול (lane)", "אין: שום מסלול לא מתאים", "C (מחזורי); אף מסלול אינו מתקיים היום", wrap=True)
    row("תאריך המחיר", "3.11.2026 (נעילה)", "3.11.2026 (נעילה)")
    r_price = row("מחיר (ש\"ח)", link(Pv, P["price"]), link(Gv, G["price"]), nf=NF_PS, bold=True)
    r_mcap = row("שווי שוק (אלפי ש\"ח)", link(Pv, P["mcap"]), link(Gv, G["mcap"]), nf=NF_K)
    row("שיעור היוון r", link(Pv, P["h_r"]), link(Gv, G["h_r"]), nf=NF_PCT)
    row("y10 ששימש", link(Pv, P["h_y10"]), link(Gv, G["h_y10"]), nf=NF_PCT2,
        note="שני מכשירים שונים באותו יום: אג\"ח שקלית 0537 (פיימנט) מול התשואה הכללית ל-10 שנים (גילת). r = 10% בשניהם")
    row("שווי במקרה הגרוע (ש\"ח למניה)", link(Pv, P["sc_גרוע"]), link(Gv, G["sc_גרוע"]), nf=NF_PS)
    row("שווי שמרני", link(Pv, P["sc_שמרני"]), link(Gv, G["sc_שמרני"]), nf=NF_PS)
    r_base = row("שווי בסיס", link(Pv, P["base"]), link(Gv, G["base"]), nf=NF_PS, bold=True)
    row("שווי אופטימי", link(Pv, P["sc_אופטימי"]), link(Gv, G["sc_אופטימי"]), nf=NF_PS)
    row("שווי משוקלל הסתברות", link(Pv, P["sc_pw"]), link(Gv, G["sc_pw"]), nf=NF_PS)
    row("מחיר / שווי בסיס", f"=B{r_price}/B{r_base}", f"=C{r_price}/C{r_base}", nf=NF_X, bold=True)
    row("מרחק המחיר משווי הבסיס", f"=B{r_base}/B{r_price}-1", f"=C{r_base}/C{r_price}-1", nf=NF_PCT,
        note="שלילי = המחיר גבוה מהשווי")
    row("רשת הרגישות: מינימום", link(Pv, P["grid_min"]), link(Gv, G["grid_min"]), nf=NF_PS)
    row("רשת הרגישות: מקסימום", link(Pv, P["grid_max"]), link(Gv, G["grid_max"]), nf=NF_PS)
    row("מחיר קנייה", "אין", "אין מחיר קנייה חי", bold=True)
    row("קו ייחוס של Tier C (net-net; אינו מחיר קנייה)", link(Pv, P["line_c"]), link(Gv, G["line_c"]), nf=NF_PS)
    row("מחיר / קו הייחוס", link(Pv, P["price_line"]), link(Gv, G["price_line"]), nf=NF_X)
    row("גודל פוזיציה מוצע", link(Pv, P["size"]), link(Gv, G["size"]), nf=NF_PCT, bold=True)
    row("מחזור יומי חציוני, 60 ימים (ש\"ח)", link(Pv, P["med"]), link(Gv, G["med"]), nf=NF_INT, note="רצפת החוקה: 50,000 ש\"ח")
    row("תקרת נזילות לפוזיציה (ש\"ח)", link(Pv, P["liq"]), link(Gv, G["liq"]), nf=NF_INT)
    row("צמיחה שנתית שהמחיר מגלם (על הרווח המנורמל, 10 שנים)", gp["g_impl"], gg["IG_NORM"], nf=NF_PCT)
    r_ni = row("רווח נקי TTM (אלפי ש\"ח)", gp["NI"]["TTM"], gg["NI_TTM"], nf=NF_K,
               note="12 החודשים עד 30.6.2026 (valuation.py NI['TTM'], NI_TTM)")
    row("P/E על מחיר 3.11.2026 (חישוב)", f"=B{r_mcap}/B{r_ni}", f"=C{r_mcap}/C{r_ni}", nf='0.00',
        note="Mega מחשבת P/E על נתוניה ועל מחיר אחר, ולכן המספר שם יכול להיות שונה מעט")
    row("פריטי וטו שנכשלו", ", ".join(ckp["veto_fail"]), ", ".join(ckg["veto_fail"]), wrap=True)
    row("פריטי וטו שלא ניתן להעריך כאן (נכשלים)", ", ".join(ckp["veto_cannot"]), ", ".join(ckg["veto_cannot"]), wrap=True)
    for i in range(3):
        row(f"תנאי הפרכה {i + 1}", FALSIFY["paymeant"][i], FALSIFY["gilat_telecom"][i], wrap=True)
    row("הקבצים", "research/paymeant/", "research/gilat_telecom/",
        note="thesis_he.md (מזכר), output.txt, checklist.md, sources.md, work/gate.md")
    for r in range(hdr + 1, S.row):
        S.ws.row_dimensions[r].height = None
    return S


def build_checks(wb: Workbook, items: list[tuple[str, str, str, object]]) -> Sheet:
    S = Sheet(wb, "בדיקות", [14, 34, 18, 18, 14, 10])
    S.title_rows("בדיקות: הנוסחאות בחוברת מול valuation.py", "כל שורה משווה תוצאת נוסחה בחוברת עם הערך ש-valuation.py מדפיס. "
                 "TRUE = זהים (סטייה יחסית עד 1e-9).", span=6)
    hdr = S.row
    for i, h in enumerate(["חברה", "פריט", "בחוברת (נוסחה)", "valuation.py", "סטייה", "תקין?"], start=1):
        S.put(f"{get_column_letter(i)}{hdr}", h, bold=True, fill=FILL_HEAD)
    S.row += 1
    first = S.row
    for comp, name, ref, expected in items:
        r = S.row
        S.put(f"A{r}", comp)
        S.put(f"B{r}", name)
        S.put(f"C{r}", f"={ref}", nf='0.000000')
        if isinstance(expected, bool):
            S.put(f"D{r}", expected)
            S.put(f"E{r}", f"=IF(C{r}=D{r},0,1)")
            S.put(f"F{r}", f"=C{r}=D{r}")
        else:
            S.put(f"D{r}", float(expected), nf='0.000000')
            S.put(f"E{r}", f"=C{r}-D{r}", nf='0.0E+00')
            S.put(f"F{r}", f"=ABS(C{r}-D{r})<=1E-9*MAX(1,ABS(D{r}))")
        S.row += 1
    S.line("הכול תקין?", f"=AND(F{first}:F{S.row - 1})", bold=True)
    return S


def build_sources(wb: Workbook, fins: dict, logs: list[str], ck: dict) -> Sheet:
    S = Sheet(wb, "מקורות והערות", [130])
    S.title_rows("מקורות, הערות ואיך החוברת נבנתה", span=1)
    lines = [
        ("איך נבנתה", True),
        ("research/build_workbook.py בונה את החוברת מקובצי המחקר בלי להקליד אף מספר: financials.json (נתוני הדוחות), "
         "valuation.py (שרץ בזמן הבנייה, ומסרב לבנות אם הריצה אינה משחזרת את output.txt) ו-checklist.md.", False),
        ("שרשרת הבסיס (EBIT מנורמל, רווחי בעלים, שווי הפעילות, גשר ההון, שווי למניה) בנויה בנוסחאות חיות; גיליון 'בדיקות' "
         "משווה כל תוצאה ל-valuation.py. שאר הערכים (תרחישים אחרים, רשת הרגישות, שיטות) הם קלטים מ-valuation.py.", False),
        ("צבעים: כחול = קלט מהקבצים; שחור = נוסחה; ירוק = קישור לגיליון אחר; צהוב = הנחת מפתח; כתום = UNVERIFIED או הערכה, "
         "או פריט בדיקה שנכשל.", False),
        ("מערכת הרשומה היא valuation.py ו-output.txt. שינוי הנחה בחוברת (r, g, ROIIC, הסתברויות) מראה את ההשפעה על שרשרת "
         "הבסיס בלבד; הוא אינו מעדכן את התרחישים האחרים או את רשת הרגישות.", False),
        ("", False),
        ("הנתונים מהדוחות", True),
    ]
    for slug, fin in fins.items():
        lines.append((f"{fin.get('company', slug)}: יחידות: {fin.get('units', '')}", False))
        docs = fin.get("documents", {})
        for k, v in (docs.items() if isinstance(docs, dict) else []):
            lines.append((f"  {k}: {v}", False))
        for cv in fin.get("caveats", []) or []:
            lines.append((f"  caveat: {cv}", False))
        lines.append(("", False))
    lines.append(("גילת: עמודת FY2020 בגיליון הנתונים", True))
    lines += [(f"  {ln}", False) for ln in logs]
    lines.append(("", False))
    lines.append(("רשימות הבדיקה: ספירת התשובות (סוג, תוצאה)", True))
    for slug, c in ck.items():
        lines.append((f"  {slug}: " + "; ".join(f"{t} {res}: {n}" for (t, res), n in sorted(c['counts'].items())), False))
    lines.append(("", False))
    lines.append(("זה מחקר, לא ייעוץ השקעות. ההסתברויות הן שיקול דעת ואינן מכוילות.", False))
    for text, bold in lines:
        S.put(f"A{S.row}", text, bold=bold, wrap=True)
        S.row += 1
    return S


# =====================================================================================================
def main() -> None:
    gp = run_valuation("paymeant")
    gg = run_valuation("gilat_telecom")
    fp = load_fin("paymeant")
    fg = load_fin("gilat_telecom")

    wb = Workbook()
    wb.remove(wb.active)

    Pv, P, chk_p = build_val_paymeant(wb, gp)
    Gv, G, chk_g = build_val_gilat(wb, gg)
    P["sheet"], G["sheet"] = Pv, Gv

    build_data_sheet(wb, "פיימנט - נתונים", "פיימנט טכנולוגיות פיננסיות (1180876)", fp)
    col2020, log2020 = fy2020_column(fg, gg)
    build_data_sheet(wb, "גילת - נתונים", "גילת טלקום גלובל (1080597)", fg, extra_cols=col2020, extra_first="FY2020")

    ck_p_rows = parse_checklist(RESEARCH / "paymeant" / "checklist.md")
    ck_g_rows = parse_checklist(RESEARCH / "gilat_telecom" / "checklist.md")
    ckp = build_checklist_sheet(wb, "פיימנט - רשימת בדיקה", "פיימנט", ck_p_rows)
    ckg = build_checklist_sheet(wb, "גילת - רשימת בדיקה", "גילת טלקום", ck_g_rows)

    build_summary(wb, P, G, gp, gg, ckp, ckg)
    build_checks(wb, [(a, b, Pv.ref(c) if a == "פיימנט" else Gv.ref(c), e) for a, b, c, e in chk_p + chk_g])
    build_sources(wb, {"paymeant": fp, "gilat_telecom": fg}, log2020, {"paymeant": ckp, "gilat_telecom": ckg})

    order = ["סיכום", "פיימנט - הערכה", "פיימנט - נתונים", "פיימנט - רשימת בדיקה", "גילת - הערכה", "גילת - נתונים",
             "גילת - רשימת בדיקה", "בדיקות", "מקורות והערות"]
    wb._sheets = [wb[n] for n in order]
    wb.active = 0
    wb.calculation.fullCalcOnLoad = True
    wb.save(OUT)
    print(f"wrote {OUT.relative_to(ROOT)}")
    print(f"checklists: paymeant {ckp['n']} items, VETO fails {ckp['veto_fail']}, cannot {ckp['veto_cannot']}")
    print(f"            gilat    {ckg['n']} items, VETO fails {ckg['veto_fail']}, cannot {ckg['veto_cannot']}")
    for ln in log2020:
        print(ln)
    print(f"checks: {len(chk_p) + len(chk_g)} formula results compared with valuation.py on the 'בדיקות' sheet")


if __name__ == "__main__":
    main()
