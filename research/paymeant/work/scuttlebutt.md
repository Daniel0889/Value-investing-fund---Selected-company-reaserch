# Paymeant Financial Technologies (TASE 1180876): public-document scuttlebutt and market microstructure

Workstream for the Rev 4 study: framework (c)4 "public-document scuttlebutt"; checklist B7, E3, E5, E9, F1 and F6.
Researched 3.11.2026. All web pages were read on 3.11.2026, Israel time (UTC+2). The Sources table gives each URL
and the time it was read.

**How to read this file.**
- Every derived number comes from `scuttle_calc.py`; its output is saved in `scuttle_calc_output.txt` and cited as
  "calc §n".
- Figures from the company's filings cite the document id and PDF page, for example "fy2025 p.17". Table figures
  were checked on the PDF page image.
- Items that rest on a search-engine summary, a headline or a reader comment, with the page itself not read, are
  marked **UNVERIFIED**.
- Peer financials come from S&P Global Market Intelligence via StockAnalysis. They are Tier 2 data and were not
  checked against the peers' own filings.

**Blocked or out of reach (not retried):**
- maya.tase.co.il and www.tase.co.il block scripted access (the brief, and an HTTP 403 earlier on 3.11.2026).
- funder.co.il returned 403 to curl and does not resolve for WebFetch.
- mako.co.il served a Radware bot page.
- The company website (payment-pay.co.il, the address in the filings) served a Cloudflare check.
- The court databases (Nevo, Takdin, Net HaMishpat) and the class-action register were not searchable here.

---

## 0. Bottom line

1. **Liquidity fails the charter floor by a wide margin.**
   - Over the 60 sessions to 3.11.2026, median daily turnover was **19,125 ILS** and the 25th percentile
     **2,590 ILS**. The floor is 50,000 ILS.
   - 45 of the 60 sessions traded below 50,000 ILS, and 89.8% of the 60-session turnover came in the 10 sessions of
     the October fall (calc §1).
   - The charter's liquidity cap (20 days × 20% × the 25th percentile) is **10,361 ILS** (calc §1, §7). The share is
     not on the maintenance list (§7).
2. **The low P/E is a lender's multiple, not an anomaly.**
   - Profitable Israeli specialist lenders trade at a median P/E of 7.67 (range 6.59–10.59) and P/B 1.37. Their
     median TTM ROE is 17.5% (calc §5).
   - Paymeant is at P/E 6.93, P/B 1.44 and ROE 22.6%. That is 9.6% cheaper than the median on P/E, with 5.1 points
     more ROE (calc §5).
   - Synchrony, owner of the largest US healthcare and aesthetics point-of-sale lender (CareCredit), is at 7.9x.
   - Against a lender peer group, the "P/E 6.6" headline explains most of the discount (§1.2).
3. **The nearest listed rival is losing.**
   - Blender, the only other listed Israeli BNPL lender, lost 72.5M ILS in 2021–2025 (calc §5). It closed its P2P
     platform in January 2026.
   - Its partner bank, Hapoalim, is selling out of the joint BNPL venture because it "prefers direct credit"
     (Calcalist, 11.1.2026 and 21.7.2026).
   - Bank Leumi bought Paymeant's loans in 2023 and Blender's in 2026.
   - So banks want the loans, not the platform. Paymeant's relative profitability is the one outside sign of an edge.
     It is not a moat that stops a bank or card issuer that decides to compete (§2).
4. **Management's account is confirmed on the basics.** Questions remain on four post-period items (§3):
   - **UNVERIFIED:** an anonymous reader comment (28.10.2026) alleges a class action over a merchant that turned its
     customers into Paymeant debtors. The FY2025 report widened its wording to "no *material* legal proceedings"
     (fy2025 p.54).
   - The Companies Registrar shows a **share transfer in the SPC Paymeant Series 1 on 10.9.2026**, with an officer
     change and an articles change, and new charges on 23.9 and 28.9.2026.
   - The licensed lending subsidiary registered **8 charges between 4.12.2025 and 4.10.2026** (calc §6).
   - A fourth subsidiary, Paymeant Clearance Ltd (incorporated 8.5.2025), is not named in the FY2025 report
     (fy2025 p.4).
5. **No record of misconduct, sanctions or convictions (B7)** was found for the company, the controllers or the
   officers.
   - Sources checked: the CMA sanctions tables for 2023, 2024 and 2025; the Companies Registrar (not a "violating
     company"); and press and web searches.
   - Court databases could not be searched, so B7 passes on the record checked, with the court check open (§4).
6. **Control chain (F1).**
   - Two founders hold 29.54% directly, as individuals, with no pyramid. Their voting agreement lapses below 25%, which
     leaves 4.54 points (1,784,758 shares) of headroom (calc §2).
   - No pledge is disclosed in any filing. The open Pledges Registrar data carries no names, so a pledge cannot be
     tested here (§5).
7. **Who sells and who buys (E3).** Over two years:
   - The informed insiders were **net sellers only**: the founders and the former chairman sold 1,019,374 shares for
     6.64M ILS and bought nothing (calc §3). The largest of these sales was the founders' 6.0M ILS block on
     13.3.2026 at 6.90, three weeks after the results-day high.
   - The 2022 institutional anchor, Mor (about 10% then), has left the interested-party register.
   - Two outside block holders, Alon Gonen (a Plus500 co-founder) and Udi Dor, were net buyers of 695,900 shares
     (calc §3).
   - The October 2026 seller is **unidentified**. No holder above 5% has reported a sale since 3.8.2026, and the
     October volume was 1.22 times the mutual funds' entire end-August holding (calc §4).

---

## 1. Competitors, and how their margins and returns compare (E5, E9)

### 1.1 Who competes

| Competitor | Where it competes | Evidence |
|---|---|---|
| Banks and credit-card companies | Instalment credit at the till; the merchant's own card instalment plan is the closest substitute | fy2025 p.38, p.43-44 |
| Direct Finance (Mimun Yashir, TASE: DIFI); car importers' finance arms (Colmobil, Lubinski group, Meir group); Blender; institutional lenders | Specialist consumer credit, for example cars and apartments | Named by the company, fy2025 p.44 (read on the PDF page): "Mimun Yashir and car importers (Colmobil, Lubinski group, Blender, Meir group and others) and institutional bodies". The company says its share is "small" |
| blenderPay BNPL (Blender 80%, Bank Hapoalim 20%) | Point-of-sale and e-commerce instalments, up to 48–60 payments, through electronics chains (KSP, Bug, iStore, Machsanei Chashmal), mostly to students | [BZ-813171] 28.3.2023: started on a 40M ILS Hapoalim line, at more than 1,000 points of sale. [ICE-974528] 1.8.2023: line raised to 82M. [CAL-0721] 21.7.2026: initial line 120M, later expanded; Hapoalim is selling its 20% to the Aviv family or a new investor, because the bank "prefers to focus on direct credit and less on point-of-sale credit" |
| Isracard (TASE: ISCD) | BNPL launched with private partners in 2021. Its advantage is presence at every terminal as Israel's largest acquirer | [BZ-797516] 3.11.2021 (Kobi Segev; the photo is captioned "Ayalim") |
| ERN | Named as an Israeli BNPL player in 2022 | [BZ-804121] 3.5.2022. No later trace found |
| Bank Leumi (as loan buyer, not originator) | Bought a 60M ILS consumer-loan portfolio from Paymeant to "increase its share in point-of-sale credit"; bought Blender's 38M ILS P2P portfolio in June 2026 | [ICE-969002] 26.6.2023; [CAL-0721] 21.7.2026 |

The ICE piece of 26.6.2023 puts Paymeant's average deal at 35k ILS, mostly dental and aesthetic treatment, against
Blender's smaller consumer-electronics tickets. That matches the filings: the average loan was 35,327 ILS in 2023
(business.md §1.4, from fy2025 p.42). **Paymeant and blenderPay barely overlap.** Paymeant is high-ticket and
medical or aesthetic; Blender is retail and student-heavy.

### 1.2 Returns and multiples (TTM; S&P Global via StockAnalysis, read 3.11.2026 21:29; calc §5)

| Company | Currency | Revenue (m) | Pre-tax (m) | Net (m) | ROE | ROA | P/E | P/B | Debt/equity |
|---|---|---|---|---|---|---|---|---|---|
| **Paymeant** | ILS | 60.3 | 24.5 | 18.5 | **22.6%** | 9.8% | **6.93** | 1.44 | 1.58 |
| Blender | ILS | 32.5 | 1.8 | −0.7 | 1.4% | 0.3% | n/a | 1.03 | 2.55 |
| Direct Finance (Mimun Yashir) | ILS | 759.2 | 354.8 | 201.5 | 15.3% | 2.2% | 7.97 | 1.08 | 5.94 |
| Menif | ILS | 319.7 | 263.1 | 202.4 | 29.9% | 5.3% | 6.59 | 1.80 | 4.32 |
| Michlol Finance | ILS | 247.9 | 80.5 | 61.4 | 15.8% | 5.3% | 10.59 | 1.52 | 4.83 |
| Jacob Finance | ILS | 125.3 | 114.6 | 87.4 | 19.4% | 2.9% | 7.67 | 1.37 | 5.93 |
| Opal Balance | ILS | 88.2 | 54.6 | 41.7 | 17.5% | 7.2% | 7.66 | 1.30 | 1.70 |
| Luzon Credit | ILS | 24.1 | 2.6 | 0.7 | 0.9% | −4.8% | 184.7 | 1.64 | 0.00 |
| Isracard | ILS | 3,290 | 308 | 228 | 7.2% | 0.8% | 22.46 | 1.13 | 1.26 |
| Synchrony (CareCredit) | USD | 9,780 | 4,366 | 3,242 | 19.8% | 2.8% | 7.89 | 1.61 | 1.03 |
| Affirm | USD | 4,260 | 493 | 1,930 | 45.1%* | 1.9% | 13.1* | 4.52 | 1.83 |
| Sezzle | USD | 532 | 201 | 161 | 88.9% | 48.8% | 27.6 | 18.5 | 0.52 |
| Klarna | USD | 4,040 | −61 | −142 | −4.3% | −0.1% | n/a | 2.08 | 0.66 |
| Zip Co | AUD | 1,340 | 145 | 116 | 16.8% | 9.4% | 21.1 | 3.53 | 4.09 |
| Humm Group | AUD | 253 | 20 | 16 | 3.0% | 0.3% | 15.3 | 0.45 | 8.32 |

\* Affirm's net income exceeds its pre-tax income, so its TTM includes a tax benefit. Its ROE and P/E are not
comparable (calc §5).

What the table says:
- **Against the profitable Israeli specialist lenders** (Direct Finance, Menif, Michlol, Jacob, Opal):
  - medians are ROE 17.46%, P/E 7.67 and P/B 1.37;
  - Paymeant's P/E is 9.6% below that median, its P/B 5.3% above it, and its ROE 5.13 points higher (calc §5);
  - its P/E ranks 2nd-cheapest of 8 profitable Israeli lenders, and its ROE 2nd-highest of 9.
- **How Paymeant earns its return.** It earns its ROE with less leverage than the bond-funded lenders (debt/equity
  1.58 against 1.70–5.94). Its ROA of 9.8% is above every core lender's (2.2%–7.2%). The reason is that it sells most
  loans and books gain-on-sale and fees. Those profits depend on buyers' appetite (business.md §1.6, §7).
- **Revenue definitions differ across lenders.** Gross, net-of-interest and net-of-buyer-share figures are mixed, so
  pre-tax margins do not compare. Paymeant's 40.6% "margin" is on revenue already net of the buyers' share
  (business.md §0). ROE, ROA, P/E and P/B are the comparable columns.
- **Foreign BNPL names** trade at higher multiples only where growth is fast (Sezzle, Zip). Synchrony, the
  closest functional analogue (CareCredit finances dental and cosmetic treatment), is at 7.9x. The market prices
  point-of-sale consumer credit at single-digit multiples on both sides of the Atlantic.

### 1.3 What the competitors' record shows

- **Blender (closest listed rival).**
  - Annual net losses 2021–2025 of 20.9M, 17.2M, 16.0M, 14.2M and 4.2M ILS, a cumulative −72.5M (StockAnalysis
    income statement, read 3.11.2026; calc §5). TTM net is −0.66M.
  - On 11.1.2026 Calcalist reported that Blender was closing its P2P platform (a 409M ILS book, run off).
  - Its P2P system carried a **3.5% credit-loss rate** at a **17% real borrower rate** (H1 2025) [CAL-0111].
  - Its share is down about 85% since the January 2021 IPO [CAL-0111].
  - Paymeant reports defaults of 2.1% of on-balance-sheet loans at 30.6.2026 and claims about 1% "verified by the
    buyers" (governance_risk.md §7, from h1_2026 p.15 and fy2025 p.60). The loss rates are not computed the same way,
    so the comparison is indicative only.
- **Tarya (the former P2P leader)** froze withdrawals after rates rose. Its book peaked at 3.3bn ILS in 2021 and is
  1.7bn now; the crisis ended only in December 2025 with the sale of a mortgage book above 400M [CAL-0111].
- **Unet Credit**, a listed non-bank lender, collapsed in 2022 after money went missing; executives were arrested
  and Giza took control [ICE-869052] 12.7.2022; [ICE-863358] 14.6.2022.

The pattern for Israeli non-bank lenders is that **funding breaks before credit does.** That is Paymeant's own first
risk: on-call bank lines, one bank supplying 88.5% of drawn credit at 31.12.2025, and take-outs through its own SPCs
(governance_risk.md §13).

### 1.4 Second-order effects (E5)

- **Supply response from banks: they buy, they do not build.** Leumi buys portfolios (Paymeant 2023, Blender 2026),
  and Hapoalim is leaving the platform it co-owned. That supports Paymeant's originate-and-sell model while bank
  appetite lasts, but it leaves Paymeant a price-taker on the spread.
- **Competitors' reactions.** The BNPL circular (in force 12.1.2027) and the shorter retention of negative credit
  data both raise costs for every lender.
  - The circular makes lenders bear part of merchant non-delivery risk (Gornitzky note, 29.7.2026, [GNY-BNPL]).
  - A precedent exists: when the Smile Clinic dental practice in Rishon LeZion closed, patients were left owing on
    treatment loans, and the lender, **Blender**, refused to cancel them. Source: N12/Mako, Q1 2026, read through a
    search summary only because the site blocked access. **UNVERIFIED** in detail.
  - Weaker players may exit, which would help Paymeant. But the same rule hits Paymeant's clinic-heavy book.
- **Who else benefits.**
  - Merchants: immediate payment and higher tickets, a company claim (fy2025 p.59).
  - Loan buyers and the SPC lender keep the spread after sale (business.md §1.5).
  - The founders' bonus is a share of pre-tax profit (governance_risk.md §0).
- **Regulatory opening for the "360" guarantee product.** On 9.3.2026 the Knesset Economics Committee approved
  opening the guarantees market. Extended-licence lenders may issue guarantees once the CMA approves them
  (Gornitzky, 11.3.2026, [GNY-GUAR]).
  - Paymeant's "payment guarantee" is part of the fee growth (business.md §1.3).
  - Whether the product needs that approval is **UNVERIFIED**.
  - A search summary also mentions a CMA draft licensing track for guarantee credit dated 26.7.2026. **UNVERIFIED**;
    the document was not read.

---

## 2. Is the moat visible from outside?

| Test | Outside evidence | Reading |
|---|---|---|
| Returns above peers | ROE 22.6% against a 17.5% core median; ROA 9.8% against 2.2–7.2% (calc §5). Blender lost money every year 2021–2025 | **Yes, on returns.** In the one head-to-head listed comparison, Paymeant's high-ticket medical niche works and Blender's retail BNPL does not |
| Durability | Hapoalim chose to exit point-of-sale credit [CAL-0721]; banks prefer buying portfolios [ICE-969002]; card issuers sit at every terminal [BZ-797516] | **Neutral to negative.** No outside party shows a barrier. The giants have stayed out by choice, not because they cannot enter |
| Pricing power | Not observable from outside. The filings show the borrower rate falling 187 basis points in 2023–2025 while merchant fees rose (business.md §11) | **Not shown** |
| Customer captivity | No merchant disclosures found. Agreements are cancellable at any time (fy2025 p.41) | **Not shown** |
| Market judgement | Anonymous reader (29.10.2026): "the only company in Israel that knows how to do BNPL profitably" [SP] | A reader opinion; noted only because it matches the peer data |

**Verdict.** The visible edge is relative execution in a niche: high tickets, medical and aesthetic merchants,
underwriting, and the sale relationship with banks. It is not a structural moat. The outside record agrees with
business.md §11: narrow at best, unproven through a credit cycle.

---

## 3. What confirms, and what contradicts, management's account

**Confirmed from outside:**
- Business model and average ticket: ICE (26.6.2023) reports a 35k average deal in medical treatment and loans sold
  on, consistent with fy2025 p.42 and business.md §1.4.
- Bank appetite for the loans: Leumi bought the June 2023 60M portfolio [ICE-969002]. The filings record that pool
  as sold to the SPC Paymeant Series 1 with "a banking corporation" financing it (business.md §7). **Leumi is
  therefore the likely SPC funder in 2023 (press-sourced; the company does not name the bank).**
- Loan-pool assignments, the licence renewal and results dates match the Maya headline feed as shown on Globes:
  - 60M (26.6.2023);
  - 90M to Series 1 (22.2.2024);
  - 80M (23.1.2025);
  - 84M (27.10.2025);
  - 80M (23.2.2026);
  - about 100M (agreement 23.9.2026, completed 29.9.2026);
  - licence renewed for five years (27.9.2023).

  Source: [GL-MAYA], read 3.11.2026 17:35.
- Interested-party sales match the filings: the founders' sales and Gonen's trades in fy2025 p.17, as shown on
  Globes and Bizportal (§6).
- Headcount: Drushim lists the company at "51-100 employees" (3.11.2026), consistent with 52 at February 2026
  (fy2025 p.46).

**Contradicted, or not yet explained by any filing we hold:**

| Item | Outside source | Filing position | Status |
|---|---|---|---|
| A class action over a merchant that "apparently deceived its customers and turned them, without their knowledge, into debtors of Paymeant", with "almost nothing" provided in the 2025 accounts | Anonymous reader comment "yair3", 28.10.2026 19:30, under the Sponser article [SP] | "Not party to any material legal proceedings" (fy2025 p.54). FY2023 and FY2024 said "not party to legal proceedings" (governance_risk.md §7). No contingent-liabilities note | **UNVERIFIED.** No court record, article or Maya report found. Check the class-action register and Maya. Material for B5 and E1 if true |
| Share transfer in the SPC **Paymeant Series 1** (10.9.2026), officer change (6.9.2026), articles change (15.9.2026), new charges (23.9 and 28.9.2026) | Companies Registrar change file on data.gov.il, dated 3.11.2026 (calc §6) | The SPC was a 100%-owned, unconsolidated subsidiary at 30.6.2026 (fy2025 p.4; h1_2026 p.6-7) | **Open.** The dates coincide with the ~100M assignment of 23.9.2026. If the shares left the group, the SPC's ownership, the deferred consideration (4.9M at 31.12.2025) and the servicing role may have changed. Read the September 2026 Maya reports |
| Eight charges registered by the licensed lender Paymeant Financing Solutions between 4.12.2025 and 4.10.2026, three of them in Sept-Oct 2026; four by the parent | Registrar change file (calc §6) | Charges on the company's assets are referred to h1_2026 p.19 §5.7 and the notes | Consistent with new secured bank lines. **Chargees and amounts UNVERIFIED** (the open file carries neither) |
| Paymeant Clearance Ltd (פיימנט סליקה בע"מ, 517159760), incorporated 8.5.2025, active, in Herzliya | Companies Registrar (ica_companies) | Not among the defined subsidiaries in fy2025 p.4 (read on the PDF page), which lists only Financing Solutions, Series 1 and Series 2 | **Open**, probably dormant or immaterial. It fits the "card clearing" item in the cash-flow suite (fy2025 p.39-40) |
| Headline of 27.10.2025: "פמנט-בהסכם עם מאוחדת להמחאת הלוואות... כ84מ'ש" (in agreement with a "consolidated [company]") | [GL-MAYA] | That pool went to Series 1 (fy2025 p.108), which the statements call "a structured entity that is not consolidated" (fy2025 p.4) | Headline wording only. **UNVERIFIED** whether it was a drafting slip |
| Strategy drift toward business credit | Drushim, 3.11.2026: five open roles, including a **business-credit underwriter** (3–4 years' experience), a client manager pitched at "business credit", a collections and service representative, and a credit back-office representative | FY2025 describes a B2B "cash-flow suite": advances, working capital, voucher discounting (fy2025 p.39-40) | Consistent, but a shift from consumer to merchant credit adds credit risk the filings do not size. Recruiting for collections fits the rising arrears (governance_risk.md §0 item 6) |

---

## 4. Misconduct, sanctions and convictions of the controllers and officers (checklist B7, VETO)

People checked: the company (and its old name, Credit Shop); Yaniv Gilor (CEO, controller); Guy Yochanan (CTO,
controller); chairman Shimon Hadad; former chairman Uri Kaduri Shoker; CFO Daniel Mastorov; VP Sales Oz Gabai; VP
Clearing and Risk Sahar Taliaz; VP R&D Aviv Yeshua; VP Collections Niv Ard; internal auditor Nir Gimpelvich. The
officer list is from fy2025 p.129, read on the PDF page.

| Source | Result |
|---|---|
| CMA sanctions, 2025 (FOI reply 2026-331, 18.3.2026) [CMA-FOI] | 18 entities sanctioned. Paymeant is not among them |
| CMA annual review 2024, chapter 2 (sanctions table) [CMA-2024] | No match for Paymeant, Credit Shop or the controllers |
| CMA annual review 2023, chapter 2 [CMA-2023] | No match |
| Companies Registrar (data.gov.il, ica_companies, file of 3.11.2026) | Paymeant is active, a public company, incorporated 9.12.2014, annual report for 2025 filed, and **not flagged "מפרה" (violating company)**. The same holds for its four subsidiaries |
| ISA enforcement: web search for the company and founders with "רשות ניירות ערך" and "אכיפה" | No hit |
| Press and web searches on the founders (Hebrew and English) | Nothing adverse. Only MarketScreener insider pages (Gilor's net worth put at about $14M on 29.6.2026, search snippet, UNVERIFIED) |
| Chairman Shimon Hadad | Career as described in search summaries of Funder and Walla items (pages not read): Isracard SVP, business customers, left about January 2022; CEO of Shufersal Finance from April 2023. Nothing adverse found |
| Former chairman Uri Shoker | Nothing found |
| Court databases (Nevo, Takdin, Net HaMishpat) and the class-action register | **Not accessible here.** Web searches for "פיימנט" and "קרדיט שופ" with court terms found nothing. See the class-action allegation in §3 |

**B7 reading:** no record of personal misconduct, sanction or conviction in the sources checked. The check is not
exhaustive, because the court databases are not available. It stays **open on the court and class-action search**
and goes to the principal.

---

## 5. Control chain and pledges (checklist F1, VETO)

| Layer | Fact | Source |
|---|---|---|
| Controllers | Yaniv Gilor 6,907,886 shares (17.56%) and Guy Yochanan 4,709,381 (11.97%), together **29.54%** | Globes JSON and Bizportal register, 3.11.2026; calc §2 |
| Holding form | Directly, as individuals: Bizportal type "פרטי" (private), Globes "אינו מוסדי" (not institutional). **No pyramid or holding company** | [BZ-STAKE]; [GL-INS] |
| Voting agreement | On director appointments and votes, while they hold more than 25% together | fy2025 p.123 |
| Headroom | 4.54 points, 1,784,758 shares, above the 25% floor. Their stake was 33.60% before the March 2026 sale and the August release (calc §2) | calc §2 |
| Pledges | None disclosed. Reg. 21A lists only the shareholders' agreement (fy2025 p.123); the H1 2026 pledges section refers only to the company's own assets (h1_2026 p.19 §5.7). The open Pledges Registrar dataset (8,458,542 records) carries only ids, dates and statuses, no names, so it cannot test a pledge of the founders' shares | data.gov.il "רשם המשכונות", read 3.11.2026 |
| Controllers' own leverage | Not disclosed. Indirect signs: they sold for cash, 3.85M ILS in January 2024 and 6.0M in March 2026 (calc §1, §3), and sold nothing during the October fall | Globes; fy2025 p.17 |
| Bank lines | Restrict changes of control (fy2025 p.99). The founders' departure or sale is therefore tied to the funding | governance_risk.md §1.1 |
| Nominee shares | The founders held shares "for the benefit of another shareholder in the company" (fy2025 p.118 notes 2-3). On 3.8.2026 they delivered 727,804 shares for no consideration, and Pini Yaakobi received 696,349 the same day. The other 31,455 presumably went to holders below 5% (UNVERIFIED; calc §2) | Globes JSON |
| What the nominee release implies | Yaakobi's direct stake before 3.8.2026 was 1,681,800 (4.28%) (calc §2). If the nominee shares were his, he held about 6% beneficially before being reported as an interested party. **UNVERIFIED**: the filings do not name the beneficiary | calc §2 |

**Other holders above 5%** (shares from the registers; percentages on 39,330,034 shares; calc §2):

| Holder | Stake | Notes |
|---|---|---|
| Alon Gonen | 9.48% | Plus500 co-founder, described as a billionaire [ICE-1133336], 12.10.2026 |
| Udi Dor | 8.47% | |
| Pini Yaakobi | 6.05% | |
| Shalom Bar Chen | 5.90% | Unchanged since 5.1.2023 |
| "Baldi" (בלדי) | 5.65% | 2,223,000 shares received from Erez Dahbani for no consideration on 30.6.2026. Nature UNVERIFIED |
| David Edri | 4.38% | Listed by Bizportal only; unchanged since 12.10.2021 |

- Bizportal's percentage column is stale for three holders, because it divides by each holder's last-report share
  count (calc §2).
- No institution is an interested party (Bizportal: "מוסדים 0").

**F1 reading:** the chain is mapped and simple: two individuals, no layers, no disclosed pledge. **Pledge
verification is "cannot assess here"** and stays open. Ask the company, or search the Pledges Registrar by name.

---

## 6. Who has been selling and buying, and why (checklist E3, VETO)

**Interested-party and officer trades, 3.11.2024 to 3.11.2026 (calc §3):**

| Date | Party | Shares | Price (ILS) | Value | Venue / source |
|---|---|---|---|---|---|
| 11–19.8.2025 | Uri Shoker (chairman until 15.9.2025) | −149,810 | ~4.27 | −0.64M | On exchange; fy2025 p.17 |
| 2025 (last action 31.12.2025) | Udi Dor | +284,056 | n/a | n/a | Bizportal 365-day flows; the filings show no off-exchange trade |
| 24.12.2025 | Alon Gonen | +1,581,844 | 4.98 | +7.88M | Off exchange; fy2025 p.17 |
| 6.1.2026 | Alon Gonen | −1,170,000 | 5.25 | −6.14M | Off exchange; fy2025 p.17 |
| 13.3.2026 | Yaniv Gilor | −434,783 | 6.90 | −3.00M | Off exchange ("מכירה בתמורה מחוץ לבורסה"); Globes JSON |
| 13.3.2026 | Guy Yochanan | −434,781 | 6.90 | −3.00M | Same |
| 30.6.2026 | Erez Dahbani → "Baldi" | 2,223,000 | 0 | — | Transfer for no consideration; Globes JSON |
| 3.8.2026 | Founders → nominee release; Yaakobi receives 696,349 | −727,804 | 0 | — | Transfers for no consideration; Globes JSON |
| 4.8–3.11.2026 | No interested-party transaction reported | — | — | — | Globes register as of 3.11.2026 18:02; Bizportal 90-day flows empty |

- **Insiders.** Officers and controllers sold 1,019,374 shares (2.59% of the company) for 6.64M ILS and bought
  none (calc §3).
  - The most informed sale, the founders' 6.0M ILS at 6.90 on 13.3.2026, came three weeks after the FY2025 results
    and the 52-week high (market.md §2), and before the August report that cut the run-rate from 640M to 600M
    (business.md §4).
  - Today's close is 54.0% below that sale price (calc §3).
  - Klarman's question has an uncomfortable answer: the people who know the most sold near the top.
  - The 5M ILS buyback was never used and expires on 18.11.2026 (market.md §3).
- **Outside block holders.** Gonen and Dor were net buyers of 695,900 shares; Gonen's net cash invested was 1.735M
  ILS (calc §3). Gonen buys and sells blocks: Bizportal totals his turnover at 2,751,844 shares in 13 days, 24.12.2025 to 6.1.2026 [BZ-FLOW].
- **Institutions.**
  - Mor Gemel & Pension led the August 2022 placement at 5.05 ILS and held about 10% on 31.10.2022 ([BZ-807179]
    9.8.2022; [BZ-809379] 31.10.2022) and 10.3% in June 2023 [ICE-969002].
  - By January 2025 it had "significantly reduced" its position, which "created massive pressure" on the price
    ([BZ-AK] 2.1.2025). It is no longer an interested party.
  - Mutual funds held 7.29% (2,866,124 shares, 49 funds) at **31.8.2026**: Sigma 3.58%, Ayalim 2.33%, Migdal 1.04%,
    Ayalon 0.22% ([BZ-STAKE]). The snapshot's value equals the 31.8.2026 close of 528.6 agorot, which dates it
    (calc §4).
  - One Sigma fund (Sigma Value Equities, Bizportal 5141650) holds 40,577 shares, 2.67% of a fund of about 8M ILS.
- **The October 2026 seller.**
  - From 20.10 to 3.11.2026, 3,485,393 shares traded: 8.86% of the company and 25.4% of the public float (calc §4).
  - That is 1.22 times the funds' end-August holding. On 28.10 alone, 1,742,446 shares traded, the day the TA-90
    fell about 4.5% after the election (market.md §3).
  - No holder above 5% reported a sale, so the seller held under 5%, or several sellers did. Mutual funds, a
    margin-called account or the class-action rumour (§3) are possibilities, all **UNVERIFIED**.
  - ICE (28.10.2026 18:25) offers only "a rapid exit of a prominent investor or forced liquidation by brokers of
    leveraged positions" [ICE-1135574]. Sponser (28.10.2026) reports market players asking "whether a large body
    decided to exit" [SP]. The company said it knew of no unusual event.
  - The October fund holdings, published around mid-November, will show whether funds sold.
- **Index money.** The share sits in TA-Software (weight 0.26%), TA-Growth (0.10%), TA Global-BlueTech (0.06%),
  Yeter (0.05%), TA All-Share (0.01%) and TA Tech-Elite (0.01%) [BZ-TRANS].
  - TASE classes it as "Software & Internet" [BZ-GV], so tech-index and tech-screen money owns a lender.
  - Passive weights are small. Mis-classification is a plausible source of disappointed holders, but **UNVERIFIED**
    as a cause.

**E3 reading (facts for the synthesis).**
- The scuttlebutt finds **no discount relative to what the business is.** As a lender, Paymeant is priced 9.6%
  below the core-lender median P/E with higher ROE (§1.2).
- The remaining gap is explained by known, observable facts: illiquidity, the founders' and Mor's selling, the
  October event, and funding concentration.
- On the Petco rule, a thesis would need to show why those facts are wrong or temporary. The outside record does
  not supply that.

---

## 7. Liquidity, maintenance list and index membership (checklist F6, FLAG)

**Data.**
- Daily on-exchange proceeds in ILS come from Bizportal's history call: 1,229 sessions, 2.11.2021–2.11.2026.
- The 3.11.2026 session (352,392 ILS; 111,691 shares in 46 trades) comes from the general view [BZ-GV], [BZ-TRANS].
- The series excludes off-exchange blocks: on 13.3.2026 it shows 33,166 ILS, while the founders sold 6.0M off
  exchange (calc §1).
- Compared with Bank Leumi's series, no session is missing, so no zero-turnover days are hidden. The 16 weekday gaps
  in 2026 are exchange holidays and election day (calc §1).
- lib/liquidity.py is not available, so percentiles use linear interpolation, with the nearest rank printed as a
  check (calc §1).

| Window | Median (ILS) | 25th pct (ILS) | Mean (ILS) | Sessions < 50k | Sessions < 100k | Liquidity cap 20×20%×p25 (ILS) |
|---|---|---|---|---|---|---|
| **60 sessions to 3.11.2026** | **19,125** | **2,590** | 191,213 | 45 of 60 | 49 of 60 | **10,361** |
| 60 sessions to 2.11.2026 | 17,757 | 2,277 | 185,351 | 46 | 50 | 9,109 |
| 60 sessions to 19.10.2026 (before the fall) | 12,250 | 1,374 | 23,488 | 52 | 58 | 5,496 |
| 120 sessions to 3.11.2026 | 19,125 | 4,928 | 120,903 | 87 of 120 | 100 of 120 | 19,714 |
| 250 sessions to 3.11.2026 | 39,703 | 14,170 | 116,313 | 136 of 250 | 181 of 250 | 56,680 |

(calc §1. The 60-session cap equals `charter_valuation.position_size`'s liquidity term.)

- **ILS 50,000 floor: FAILS.** The median of 19,125 is 38% of the floor (calc §1), and it fails in every window
  tested.
  Before the October fall the median was 12,250.
- **ILS 100,000 price-reliability line: FAILS.** If the name were pursued at all, the price-reliability block and
  the control and related-party section would be mandatory. Sections §5–§6 here and governance_risk.md supply the
  control material.
- **Concentration of trading.** 89.8% of the 60-session proceeds came in the 10 sessions from 20.10.2026
  (calc §1). Ten sessions in the window traded under 1,000 ILS; the lowest was 14 ILS.
- **What it means for a position.**
  - The charter cap is 10,361 ILS, 0.0083% of the market cap (calc §7).
  - At 20% of the 60-session median, building 1M ILS takes 261 sessions; at the pre-fall median, 408 (calc §7).
  - The only practical route is an off-exchange block. Blocks of 1–1.6M shares have changed hands in 2023–2026
    (fy2025 p.17), but the sellers in such blocks have been the most informed holders (§6).
- **Maintenance list: NOT on it, with a wide cushion.**
  - TASE's rules, per its notice of 11.7.2024 to members [TASE-MAINT]: a company is non-compliant if the public's
    holdings are worth less than NIS 5M, or if the public holds under 5%, or under 15% while worth less than NIS 15M.
    Reviews use 30 June and 31 December data, with market-maker exemptions at NIS 4M and 12.5%.
  - Paymeant's public holds 34.91% (Globes basis, 43.6M ILS at 317.3 agorot) or 30.53% (Bizportal basis, 38.1M ILS).
    That is 8.7x and 7.6x the NIS 5M floor and 2.33x and 2.04x the 15% line (calc §2).
  - Corroboration: Bizportal lists it as a member of ten TASE indices, among them TA-Software, TA-Growth and
    TA Tech-Elite [BZ-TRANS].
  - StockAnalysis tags 16 TASE tickers with ".M", apparently the maintenance list, and PMNT is not one of them. The
    meaning of the tag is an inference.
  - TASE's own list could not be read (403).
  - The 2024 thresholds are the latest found; current thresholds are **UNVERIFIED**.
- **Other F6 items:**
  - Not a TA-35 or dual-listed name: no edge problem.
  - The Israeli window is at most six years: `cycle_window_short` applies (charter amendment 2).
  - The TASE 30% cap is the principal's to check; holdings and NAV are not available here.

---

## 8. Li Lu's four categories, for the outside record (checklist E9, FLAG)

| Category | Items |
|---|---|
| **What we know** | Peer returns and multiples (§1.2); Blender's losses and Hapoalim's exit (§1.3); Leumi bought the loans in 2023 (§3); insider and institutional selling and the 2-year trade record (§6); liquidity statistics and maintenance status (§7); the registry facts, entities and charges (§3); no sanction records at the CMA 2023–2025 (§4) |
| **What we do not know** | Who sold in October 2026; whether a class action exists; why shares in Paymeant Series 1 were transferred on 10.9.2026 and to whom; who holds the charges registered in 2025–2026 and for how much; whether the founders' shares are pledged; the identity of the bank behind 88.5% of drawn credit at end-2025; the end-September and October fund holdings |
| **What we do not need to know** | The global BNPL market size (no Israeli figure is published); foreign BNPL growth rates (Paymeant does not compete abroad); Isracard's BNPL volumes |
| **What could be unknown to us** | Merchant-level losses under the "360" guarantee; claims from clinics that closed, under the BNPL circular after 12.1.2027; terms in the September 2026 SPC transaction; anything in Maya immediate reports, which were not readable |

---

## 9. Checklist status from this workstream

| Item | Status | Basis |
|---|---|---|
| **B7** (VETO) no misconduct record | **PASS on the record checked; OPEN on the courts** | §4. Court and class-action databases not accessible; one anonymous allegation (§3) |
| **E3** (VETO) mispricing and who is selling | **Facts supplied; points to NO_THESIS on mispricing** | §6. Priced like an Israeli specialist lender; the sellers were informed holders. The final verdict belongs to the synthesis |
| **E5** (FLAG) second-order effects | **Done** | §1.4 |
| **E9** (FLAG) four categories and outside scuttlebutt | **Done for the outside record** | §8; competitors, buyers, regulators, registry, jobs and press covered. Courts are the gap |
| **F1** (VETO) control chain and pledges | **Chain mapped; pledge "cannot assess here" (open)** | §5 |
| **F6** (FLAG) maintenance list, liquidity, window, TASE cap | **FLAG raised.** Fails the 50k floor and the 100k line; not on the maintenance list; `cycle_window_short`; TASE cap not assessable | §7 |

---

## 10. Open items for the principal (Maya and registries)

1. **Maya, September–October 2026:**
   - the 23.9 and 29.9.2026 assignment reports, and why shares in Paymeant Series 1 changed hands on 10.9.2026
     (buyer, price, effect on the deferred consideration and on servicing);
   - any report of an exchange inquiry around 28.10.2026;
   - interested-party reports filed late.
2. **Class-action register and court search** for "פיימנט טכנולוגיות פיננסיות" (515166544), its subsidiaries and the
   founders. This tests the reader-comment allegation (§3).
3. **Companies Registrar extracts (paid)** for 515166544, 516943644, 516789849 and 517081733: chargees, secured
   amounts, and the holder of Series 1 shares after 10.9.2026.
4. **Pledges Registrar search by name** for Yaniv Gilor and Guy Yochanan (F1).
5. **The October 2026 monthly fund holdings** (Sigma, Ayalim, Migdal), due around mid-November 2026, to identify the
   October seller.
6. **The Q3 2026 report**, expected around 17.11.2026, with the buyback plan expiring on 18.11.2026.

---

## Sources

All read on 3.11.2026, Israel time (UTC+2). Raw copies are saved under `scuttle/` (see Files).

| Key | What was used | URL | Read |
|---|---|---|---|
| [BZ-RT] | Daily close, volume and on-exchange proceeds (ILS), 2.11.2021–2.11.2026 | https://www.bizportal.co.il/ajax/biz_papers_helper.ashx?action=get_paper_yearly_graph&request_type=1&paper_id=1180876&period=6 (the quote page's own history call; plain request with the site's session cookie from a visit to the quote page) | 21:15 (identical to the 17:59 copy) |
| [BZ-RT-L] | The same series for Bank Leumi, used only as the session calendar | same call with paper_id=604611 | 18:01 |
| [BZ-GV] | 3.11.2026 proceeds 352,392 ILS; 39,330,034 shares; sector "Software & Internet" | https://www.bizportal.co.il/capitalmarket/quote/generalview/1180876 | 21:15 |
| [BZ-TRANS] | 3.11.2026: 111,691 shares, 46 trades, range 307.5–319; index memberships and weights | https://www.bizportal.co.il/capitalmarket/quote/transactions/1180876 | 18:01 |
| [BZ-STAKE] | 8 interested parties; mutual-fund snapshot (31.8.2026) by manager | https://www.bizportal.co.il/capitalmarket/quote/stakeholders/1180876 | 17:27 |
| [BZ-FLOW] | 365-day interested-party flows (Dor +284,056; Gonen ±; Yaakobi; Baldi); longer periods return nothing | https://www.bizportal.co.il/ajax/biz_papers_helper.ashx?action=get_holding_flow_summary_data_json&paperId=1180876&period=y | 21:25 |
| [BZ-FUND] | Sigma Value Equities holdings (Paymeant 40,577 shares, 2.67%) | https://www.bizportal.co.il/mutualfunds/quote/holdings/5141650 | 21:25 |
| [GL-INS] | Interested parties and their transactions (AsOfDate 3.11.2026 18:02) | https://www.globes.co.il/portal/instrument.aspx?instrumentid=370226&mode=company (data from POST /portal/Handlers/GTOFeeder.ashx, mode=interestedParties) | 18:02 |
| [GL-MAYA] | Maya headline feed 2023–2026 | https://www.globes.co.il/portal/instrument.aspx?instrumentid=370226&mode=reports | 17:34 |
| [ICE-1135574] | "מניית הפינטק הישראלית התרסקה ביותר מ-40%: החברה בהודעה חריגה לבורסה", ice editorial, 28.10.2026 18:25 | https://www.ice.co.il/finance/news/article/1135574 | 21:18 |
| [SP] | Sponser, 28.10.2026: "השלימה התרסקות של 50% בחודש ללא סיבה"; reader comments of 28.10 19:30 ("yair3") and 29.10 14:48 | https://www.sponser.co.il/Article.aspx?ArticleId=123772 | 17:39 (saved by the market workstream) |
| [ICE-969002] | "בנק לאומי רוכש תיק הלוואות צרכניות של 60 מיליון שקל", Nitzan Cohen, 26.6.2023 19:03 | https://www.ice.co.il/finance/news/article/969002 | 21:35 |
| [ICE-1052117] | FY2024 results write-up, 19.2.2025 14:15 | https://www.ice.co.il/finance/news/article/1052117 | 21:21 |
| [ICE-1133336] | Alon Gonen profile (Plus500 co-founder), 12.10.2026 22:01 | https://www.ice.co.il/financial-gossip/news/article/1133336 | 21:23 |
| [ICE-1107971] | Alon Gonen interview, Roy Shainman, 7.4.2026 10:58 | https://www.ice.co.il/finance/news/article/1107971 | 21:23 |
| [ICE-869052] / [ICE-863358] | Unet Credit arrests (12.7.2022) and Giza takeover (14.6.2022) | https://www.ice.co.il/law/news/article/869052 ; https://www.ice.co.il/finance/news/article/863358 | 21:21 |
| [ICE-974528] | Hapoalim line to blenderPay raised to 82M, 1.8.2023 | https://www.ice.co.il/finance/news/article/974528 | 21:27 |
| [ICE-851788] | blenderPay at iStore; Competition Authority approval of the Hapoalim–Blender venture (link title), 13.4.2022 | https://www.ice.co.il/consumerism/news/article/851788 | 21:27 |
| [BZ-813171] | blenderPay starts lending on a 40M Hapoalim line, 28.3.2023 | https://www.bizportal.co.il/capitalmarket/news/article/813171 | 21:27 |
| [BZ-804121] | "BNPL – מה זה", names Blender, ERN, Isracard and Paymeant, 3.5.2022 | https://www.bizportal.co.il/financialconsumerism/news/article/804121 | 21:27 |
| [BZ-797516] | Kobi Segev (photo captioned "Ayalim"): Blender, Isracard and Paymeant enter BNPL, 3.11.2021 | https://www.bizportal.co.il/capitalmarket/news/article/797516 | 21:35 |
| [BZ-807179] | 24M ILS placement led by Mor, 4.7M shares at 5.05, 9.8.2022 | https://www.bizportal.co.il/capitalmarket/news/article/807179 | 21:24 |
| [BZ-809379] | Q3 2022 results; Mor holds about 10%, 31.10.2022 | https://www.bizportal.co.il/capitalmarket/news/article/809379 | 21:24 |
| [BZ-AK] | Yaakov Akilov column (Mor reduced its stake; buyback unused), 2.1.2025 | https://www.bizportal.co.il/capitalmarket/news/article/20011989 | 17:44 (market workstream copy) |
| [CAL-0111] | "ענף הולך ונעלם: בלנדר סוגרת את פעילות פלטפורמת ה־P2P שלה", 11.1.2026 | https://www.calcalist.co.il/market/article/ryc7afxbwl | 21:32 |
| [CAL-0721] | "בנק הפועלים יוצא מבלנדר פיי: מוכר את החזקותיו למשפחת אביב", 21.7.2026 | https://www.calcalist.co.il/market/article/ry3vltoeze | 21:32 |
| [SA-STATS] | TTM statistics pages for PMNT, BLND, DIFI, MNIF, MCLL, JCFN, OPAL, LUZC, ISCD (tlv), ZIP, HUM (asx), AFRM, SEZL, KLAR, SYF; Blender annual income statement | https://stockanalysis.com/quote/tlv/PMNT/statistics/ (and the same path per ticker; US: https://stockanalysis.com/stocks/syf/statistics/ etc.); https://stockanalysis.com/quote/tlv/BLND/financials/ | 21:29 |
| [SA-LIST] | TASE ticker list (".M" suffixes) | https://stockanalysis.com/list/tel-aviv-stock-exchange/ | 21:28 |
| [CMA-FOI] | CMA FOI reply 2026-331 of 18.3.2026: 2025 sanctions table | https://www.gov.il/BlobFolder/dynamiccollectorresultitem/knas/he/repository-of-answers_capital-market-authority_knas.pdf | 21:22 |
| [CMA-2024] | CMA annual review 2024, chapter 2 | https://www.gov.il/BlobFolder/reports/report_0010/he/Commisioner%20Report%20Design%20B_chapter2%20ver6_digital.pdf | 21:22 |
| [CMA-2023] | CMA annual review 2023, chapter 2 | https://www.gov.il/BlobFolder/reports/report_0006/he/The_Commissioner's_Report_Chapter_2%20(1).pdf | 21:22 |
| [ICA] | Companies Registrar: company list (resource f004176c-b85f-4542-8901-7b3176f9a054) and change file (28780ab5-3ef1-44c7-8377-da82c0aa6781, one year back, dated 3.11.2026) | https://data.gov.il/api/3/action/datastore_search?resource_id=f004176c-b85f-4542-8901-7b3176f9a054&q=515166544 ; https://data.gov.il/api/3/action/datastore_search?resource_id=28780ab5-3ef1-44c7-8377-da82c0aa6781&q=515166544 | 21:33 |
| [PLEDGE] | Pledges Registrar open data (no names) | https://data.gov.il/api/3/action/datastore_search?resource_id=e7266a9c-fed6-40e4-a28e-8cddc9f44842 | 21:34 |
| [TASE-MAINT] | TASE notice to members, "Non-Compliance with the Maintenance Rules Based on Data as of June 30, 2024", 11.7.2024 (republished by a listed issuer) | https://cdn.financialreports.eu/financialreports/media/filings/6813/2024/RNS/6813_rns_2024-07-11_b3e0303e-65be-41da-bc5e-a6403413d89a.pdf | 21:29 |
| [GNY-BNPL] | Gornitzky client update on the BNPL circular, 29.7.2026 | https://www.gornitzky.co.il/wp-content/uploads/pdf/post/31940_bnpl-buy-n.pdf | market workstream copy |
| [GNY-GUAR] | Gornitzky, guarantees-market reform, 11.3.2026 | https://www.gornitzky.co.il/wp-content/uploads/pdf/post/30672_----------.pdf | 21:40 |
| [DRUSHIM] | Employer page: 5 open roles, "51-100 employees" | https://www.drushim.co.il/דרושים-3628319-פיימנט-טכנולוגיות-פיננסיות/ | 21:31 |
| [N12] | Smile Clinic closure, lender Blender (search summary only; site blocked) | https://www.mako.co.il/news-money/consumer/Article-3c4356104a2eb91026.htm | UNVERIFIED |

Search-engine summaries used only as leads, and marked UNVERIFIED where repeated:
- Chairman Hadad's career (Funder 147355, Walla 3482353).
- MarketScreener's figure for Gilor's net worth.
- The CMA draft guarantee licensing track of 26.7.2026.

---

## Files

All paths are absolute under the scratchpad work folder:
`/tmp/claude-0/-home-user-value-investing-fund---selected-company-reaserch/8e9bb9a6-b39f-5c24-a635-b21606f1c8ae/scratchpad/work/paymeant/`

- `scuttle_calc.py` and `scuttle_calc_output.txt`: every derived figure.
- `scuttle/raw2/`: Bizportal series refetch (`rt1_refetch.json`), general view, flows.
- `scuttle/raw3/`: ICE pages, CMA PDFs and their text, Mor reports.
- `scuttle/raw4/`:
  - StockAnalysis pages (`sa_stats/`), Calcalist and ICE competitor articles;
  - Companies Registrar JSON (`ica_*.json`) and Pledges Registrar sample;
  - the TASE maintenance notice, the Gornitzky guarantees note and the Drushim page.
- `scuttle/web/`: earlier copies (Globes interested-party JSON, Bizportal series, Leumi calendar).
