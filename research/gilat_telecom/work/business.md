# Gilat Telecom Global (TASE 1080597): business and moat

Prepared 3.11.2026 for the fund's Revision 4 study. This is the business section of the study, not the valuation.

**Sources.** All four documents are the company's own filings to the ISA:
- `gilat_fy2023`: the 2023 annual report.
- `gilat_fy2024`: the 2024 annual report. The investor's file name says 2025, but the cover says 2024.
- `gilat_fy2025`: the 2025 annual report.
- `gilat_h1_2026`: the Q2 2026 report. It holds the directors' report and the company-only (solo) interim data. **The consolidated interim statements are not in it.**

Page numbers are PDF page indexes (p.1 is the first PDF page). I checked every table figure used here against the PDF page image.

**Derived figures.** Every ratio, sum, margin, share, scenario and conversion below comes from `business_calcs.py` in this folder. Its printed output is `business_calcs_output.txt`. I did no arithmetic by hand.

**Units.** 2021–2025 figures are in USD thousands, because USD was the functional currency to 31.12.2025. Figures for 2026, and the FY2025 and H1 2025 figures restated in the Q2 2026 report, are in ILS thousands, because ILS is the functional currency from 1.1.2026 (gilat_h1_2026 p.2). Conversions to the other currency use the spot rate given in the task, USD/ILS 3.157.

**Labels.**
- "UNVERIFIED": a figure I could not tie to a filing.
- "Analyst estimate": my own estimate, built from cited inputs.

---

## 0. Bottom line

1. **What it is.** Gilat is a small reseller and integrator of other companies' networks. It owns almost no network of its own. It leases satellite capacity and buys airtime from Iridium, Inmarsat, Thuraya, Intelsat and SES/O3b. It buys fibre lines from Bezeq. It packages these with terminals, integration, network management and support.
   - Bought-in capacity and airtime were 55–62% of revenue in 2023–2025. Cash paid on leases alone was 27–30% of revenue (calc §3).
   - The business needs almost no tangible capital. Operating working capital was negative or near zero in 2022–2025 (calc §8). The real commitments are leases and take-or-pay contracts.
2. **Where the money comes from now.** One unnamed Israeli customer buying mobile satellite solutions was **25.4% of 2025 revenue**. Vodacom DRC was **16.3%** (calc §5). The government segment was **63.4%** of 2025 revenue and ~99% Israeli (gilat_fy2025 p.31). It grew **3.59x** from 2021 to 2025 (calc §1), and the company itself attributes part of the growth to the wars (gilat_fy2025 p.97; gilat_h1_2026 p.12).
3. **Earnings power.** TTM to 30.6.2026 (ILS) is revenue 276,092, operating income 39,535 (14.3% margin) and net income 32,985 (calc §7; this matches the Mega figures). **This is near-peak, not normal.** Four things flatter it or put it at risk:
   - war-driven defence demand, including one-off equipment sales (gilat_h1_2026 p.12);
   - a one-off credit from a satellite supplier in 2025 (gilat_fy2025 p.96, p.160);
   - a 14% fall of the USD against the ILS. Revenue is now mostly in ILS while satellite costs are in USD (gilat_fy2025 p.90, p.136; gilat_h1_2026 p.12, p.18-19);
   - Vodacom, a contract that ends in March 2027 (gilat_fy2025 p.56).

   My normalised operating profit treats leases as operating costs (analyst estimate, calc §11). Base is **ILS 15.1M (USD 4.8M)**, 38% of TTM operating income. Bear is a **loss of ILS 11.9M**. Bull is ILS 38.6M. The 5-year average of lease-adjusted EBIT for 2021–2025 is only **USD 1.4M** (calc §1).
4. **Moat.** There is none in the Africa business or the ISP. In Israeli defence there is at most a narrow moat, built on Ministry of Communications licences, security-cleared staff and long relationships with Israeli defence buyers. The company itself says competition is mainly on price and its share is "not material" (gilat_fy2025 p.32). Segment margins were 26–28% in 2021–2024 and reached 35% only in 2025 (calc §1). High returns on capital come from supplier financing and leased capacity, not from a franchise (calc §8).
5. **Biggest new commitment.** Gilat has taken fibre-line rights (IRUs) from Bezeq for 54,000 lines, worth **ILS 248M of committed consideration** (calc §9). That is 0.95x FY2025 revenue. It is payable over up to 10 years and is mostly **not on the balance sheet**. The accounting spreads the cost over 25 years (gilat_fy2025 p.153).
   - Against the regulated wholesale price that Gilat can buy without limit (ILS 58/month), the new lines are 13% cheaper with Bezeq's 5% financing and 9% dearer at the fund's 10% hurdle (calc §9).
   - This is a bet on scale, not a cost moat.
6. **Circle of competence.** An outside owner can understand how the business works. He cannot predict it 5–10 years out:
   - Israeli defence ordering, war intensity, low-orbit satellites (Starlink), the Vodacom renewal and wholesale regulation all drive the result;
   - a quarter of revenue comes from a customer the company does not name.

   **Suggested treatment for the lead analyst:** the fund's "cheap" track. Grade **C**, plus about 5 points of extra margin for concentration, undisclosed key data and inconsistent figures. Value it on base or bear normalised earnings, never on TTM.

---

## 1. What Gilat sells, to whom, and how it makes money

### 1.1 The company
- Founded 20.10.1968 and listed on the TASE since 1994 (gilat_fy2025 p.6).
- Registered as a "small corporation" (תאגיד קטן) and has adopted the disclosure reliefs, except the one on quarterly reporting (gilat_fy2025 p.2, p.108).
- Has had no controlling shareholder since 17.2.2021 (gilat_fy2025 p.214).
- Subsidiaries: Gilat Telecom (Israel, the operating company), IP Planet, Israsat (inactive), Gilat Nigeria (inactive), Gilat Ghana, Gilat Uganda and G-Telecom Belgium (gilat_fy2025 p.8).
- Head office is leased in Petah Tikva to March 2028, with options to 2030 (gilat_fy2025 p.61).

### 1.2 The model
Gilat owns very little network. Its owned assets are hubs, a teleport on its Petah Tikva roof, antennas, routers and modems rented to customers, an in-house CRM and a cloud ERP (gilat_fy2025 p.60-61).

What it sells is capacity it buys from others:
- **Satellite capacity**: transponders and MHz bought from satellite operators on leases of 1–4 years and on shorter contracts (gilat_fy2025 p.64, p.159).
- **Airtime and terminals** of mobile satellite networks, under distribution agreements:
  - Iridium since 2003: one-year terms that renew automatically. Iridium can change prices on 30 days' notice (gilat_fy2025 p.66).
  - Inmarsat since 2018 (gilat_fy2025 p.67).
  - Thuraya since 2022, renewed to 7.2028 (gilat_fy2025 p.67).
- **Fibre access lines** bought from Bezeq under the IRU agreements (gilat_fy2025 p.41-42, p.152-153).

It packages these with design, equipment, installation, project management, network management, a 24/7 support desk and SLAs, and bills the customer, mostly monthly.

The cost lines show the model (USD k, gilat_fy2025 p.173; calc §3):

| | 2023 | 2024 | 2025 |
|---|---|---|---|
| Bought-in capacity and airtime: satellite services, D&A in cost of revenue (mostly satellite-lease depreciation), fibre-IRU amortisation, mobile satellite airtime and telephony, other communication services | 32,616 | 43,054 | 41,753 |
| — as % of revenue | 59.1% | 61.9% | 55.1% |
| Cash paid on all leases, including short-term (gilat_fy2025 p.160) | 15,678 | 18,835 | 22,860 |
| — as % of revenue | 28.4% | 27.1% | 30.2% |
| Lease payments as % of operating cash flow (gilat_fy2023 p.86; gilat_fy2025 p.93) | 54.0% | 79.5% | 55.1% |

The company's own "Adjusted EBITDA" deducts satellite-lease depreciation, so it already treats capacity as an operating cost (gilat_fy2025 p.92). That is the right lens for an owner.

### 1.3 Segments
The segments changed in Q1 2026:
- **To 2025 there were three:** government/defence, Israel communications and internet (the ISP), and global business, which is mainly Africa (gilat_fy2025 p.6, p.11).
- **From Q1 2026 there are two** (gilat_h1_2026 p.3-4):
  - **commercial and government satellite**, 85.3% of H1 2026 revenue (calc §1);
  - **internet, communications and cloud**, 14.7%. This one includes Uganda.

### 1.4 Government and defence (63.4% of 2025 revenue)

**What it sells** (gilat_fy2025 p.29, p.31):
- mobile and fixed satellite voice and data, "anywhere on earth, at sea, in the air and on land";
- satellite phones, terminals and modems;
- fleet and vessel tracking;
- projects: consulting, design, shipping, implementation, on-site support, and leasing and configuring capacity.

**Who buys** (gilat_fy2025 p.30-31):
- government and municipal bodies, state and security organisations, telecom companies, integrators and distributors;
- in Israel it sells directly to end users; abroad it sells through agents and distributors;
- Israel was about 99% of the segment's revenue in 2023, 2024 and 2025 (gilat_fy2023 p.52; gilat_fy2024 p.49; gilat_fy2025 p.31).

**Contract structure: mostly 12-month orders and non-binding frameworks.** The company has reported these orders and agreements (gilat_fy2025 p.101-104; gilat_h1_2026 p.15-16):
- A 4-year contract worth ILS 39M from 1.10.2023, paid in equal instalments. The customer holds options for up to 11 more years. If all are exercised, the contract reaches up to ILS 139M over 15 years.
- An exclusive framework of up to ILS 36.5M to the end of 2029, signed 12.2024. ILS 36M of it was used by March 2026, and the customer then added ILS 43.5M. The framework is **non-binding**.
- Annual orders and renewals:
  - ILS 22M for the 12 months after 31.12.2024;
  - ILS 9.8M for 2025;
  - ILS 28M for 2025 plus ILS 3.5M for 2026 (April 2025);
  - **about ILS 110M, including VAT, for "the coming year"**, ordered in 12.2025–1.2026.
- The Ministry of Finance Accountant General's communications tender, held since 2012 and extended to June 2027.
- In 2026: an order of ILS 14.3M plus ILS 4.25M, and an integration job for a foreign defence customer worth ILS 4.3M.

**Revenue mix and margins.**
- Services were 84.9% of the segment's 2025 revenue and equipment 15.1%. In 2023 services were 66.8% and equipment 33.2% (calc §3, from gilat_fy2025 p.173).
- Company-wide equipment gross margin was 21.4% in 2023, 23.9% in 2024 and 31.3% in 2025 (calc §3).
- Segment margin was 26.4–28.4% in 2021–2024 and **34.6% in 2025** (calc §1).
- Variable costs were 52.8–56.5% of segment revenue in 2021–2023 and 43.7% in 2024 (calc §1; gilat_fy2023 p.10, gilat_fy2024 p.11). The published split stops at 2024.

**Unit economics.** Gilat earns a reseller and integrator spread on airtime and capacity it does not own. Its suppliers can reprice on 30 days' notice. Domestic satellite service under its licence must use Israeli (Spacecom) satellites unless Spacecom cannot supply the capacity (gilat_fy2025 p.70).

The segment is run by **6 sales staff**, against 8 in 2022 (gilat_fy2025 p.62; gilat_fy2023 p.57). That is USD 8.0M of segment revenue per salesperson in 2025 (calc §8). The business is about relationships and access, not volume selling.

### 1.5 Global business (25.9% of 2025 revenue; mainly Africa)

**What it sells:** managed connectivity to the internet backbone, private corporate networks (WAN/MPLS), network management, raw space segment, and O3b/mPOWER medium-orbit (MEO) capacity from SES (gilat_fy2025 p.54-55).

**Who buys:** mobile operators, ISPs, fixed-line carriers, enterprises, NGOs and humanitarian bodies (gilat_fy2025 p.55). Telecom operators were 75% of revenue in 2025, 70% in 2024 and 72% in 2023 (gilat_fy2025 p.56-57). The table is labelled "share of company revenue", but it sits in the global section and can only mean share of the segment's revenue.

**Contracts** (gilat_fy2025 p.57):
- usually one year, renewing automatically, billed monthly;
- service to small customers stops if they do not pay;
- SLAs promise 99.5–99.9% availability.

Gilat says it avoids long supplier contracts and keeps its supplier terms back-to-back with customer terms (gilat_fy2025 p.53). Capacity is fully sold: free capacity was 0–2.6% in 2023–2025 and 0–0.5% at 30.6.2026 (gilat_fy2025 p.93; gilat_h1_2026 p.7).

**Vodacom DRC is the anchor** (gilat_fy2025 p.55-56):
- It has averaged about USD 1M a month in 2023–2025.
- It was renewed in May 2024 to the end of March 2027, for an expected ~USD 45M over the term. The company calls it its largest service contract of the decade.
- The service is managed satellite capacity, backup and outsourcing of the customer's satellite operations, including SES mPOWER.
- The company "is working to renew" it (gilat_h1_2026 p.15).
- Satellite-transponder lease additions were USD 23,826k in 2024 (gilat_fy2025 p.159). In my reading this is capacity committed for the renewal (analyst inference).
- About USD 2.4M of Vodacom-deal costs were prepaid in Q2 2024, ~USD 1.8M of it for 2025–2027 (gilat_fy2024 p.83). Agent commissions rose with the renewal (gilat_fy2024 p.85).

### 1.6 The Israeli ISP (10.7% of 2025 revenue; "internet and cloud" from 2026)

**History.** Gilat entered the ISP market in March 2022. It served operators first, then businesses, and launched consumer service in April 2023 (gilat_fy2025 p.6, p.11).

**What it sells.** Fibre internet under the "Gilat Telecom" brand, cloud connectivity, VoIP, integration for retail chains, and rental of routers and modems (gilat_fy2025 p.46-47). It sells through call centres, a self-service web store and resellers. It has **no material customers** in this segment (gilat_fy2025 p.46).

**Pricing and scale** (calc §9; gilat_fy2025 p.94; gilat_h1_2026 p.8):

| | 31.12.2024 | 30.6.2025 | 31.12.2025 | 30.6.2026 |
|---|---|---|---|---|
| Private subscribers | 6,566 | 10,294 | 17,929 | 25,045 |

| | FY2024 | Q2 2025 | FY2025 | Q2 2026 |
|---|---|---|---|---|
| Monthly ARPU (ILS) | 87.83 | 88.71 | 86.85 | 80.19 |

- Net additions were 3,728 in H1 2025, 7,635 in H2 2025 and 7,116 in H1 2026.
- ARPU in Q2 2026 was down 9.6% year on year, because new customers come in on promotions. The long-run target is ILS 90.
- Peer ARPUs: Partner about ILS 94, Cellcom ILS 99.6, Bezeq ILS 138 (gilat_fy2025 p.37-38). Gilat is 15–42% below them, so it competes on price.
- Customers reported in the text (gilat_fy2025 p.91; gilat_h1_2026 p.5):
  - March 2026: ~21,000 private, ~300 business, ~22,000 lines active on Bezeq;
  - August 2026: ~26,000 private, ~330 business, more than 27,600 lines.

**Line economics: the two Bezeq IRUs** (gilat_fy2025 p.41-42, p.152-153, p.183; gilat_fy2024 p.11):

| | IRU-1 (12.2024) | IRU-2, first pulse (11.2025) |
|---|---|---|
| Lines | 18,000 | 36,000, in 12 quarterly tranches of 3,000 |
| Consideration | ILS 88.02M + VAT | ~ILS 160M "assuming full exercise", CPI-linked |
| Price per line (calc) | ILS 4,890 | ILS 4,444 |
| Term | 15 years + 2×5-year options | 15 years |
| O&M fee | 4% a year | 4% a year |
| Payment | each pulse can be spread over 10 annual payments; 5% interest on pulse 1 | same |
| Monthly cost per fully used line, before financing (calc) | ILS 43.5 | ILS 39.5 |
| — at Bezeq's 5% financing | ILS 55.6 | ILS 50.5 |
| — at the fund's 10% hurdle | ILS 69.9 | ILS 63.5 |
| Against the regulated BSA price of ILS 58/month (before financing / 5% / 10%) | −25% / −4% / +20% | −32% / −13% / +9% |

Notes on the IRUs:
- Later pulses add 3 × 18,000 lines at ~ILS 80M each, in 2029, 2031 and 2033. Gilat is released from a pulse if line-growth targets are missed.
- The regulated price for fibre BSA up to 1 Gbps is ILS 58/month, fixed for 2026–2031. Small ISPs such as Gilat keep **unlimited** access to BSA at the regulated price; only the big four have quotas (gilat_fy2025 p.40).
- So on today's regulation the IRU saves Gilat little once the cost of money is counted. It is protection against wholesale prices rising after 2028–2031, and a bet on filling 54,000 lines.
- Gilat has to fill about 26,400 more committed lines by the end of 2028. That is 1.85 years of private net additions at the H1 2026 pace of 14,232 a year (calc §9).
- **ARPU minus line cost** at Bezeq's 5% financing is only ILS 25–30 a month (calc §9). That margin still has to pay for bandwidth, customer equipment, service, marketing and churn.
- Gilat's IRU cost is in line with Partner's Bezeq IRU, about ILS 42/month before financing (gilat_fy2025 p.35). Gilat has bought its way to cost parity with the big groups, not below them.

**The 'yes' wholesale contract.** Gilat supplied ISP services to the operator 'yes' from June 2022 to the end of 2025; yes is "Customer B", 11.6–13.5% of revenue in 2023–2024 (calc §5).
- From September 2024 yes bought the Bezeq lines directly. That pass-through revenue disappeared with no effect on profit, which is why segment revenue fell from 12,695 to 8,073 in 2025 (gilat_fy2025 p.97).
- The contract ended at the end of 2025 (gilat_fy2025 p.91).

### 1.7 Recurring versus one-off
- Revenue recognised over time (services) was 84.2% in 2023, 88.7% in 2024 and 89.3% in 2025. Equipment, recognised at a point in time, was 10.7–15.8% (calc §3).
- "Recurring" here does not mean "contracted". Government services run on 12-month orders and non-binding frameworks. Africa contracts run one year. Consumers can leave monthly.
- Backlog at year-end covered only **27.9% of 2024 revenue and 45.7% of 2025 revenue**. For the government segment it covered only 29.9% and 31.3% (calc §6).
- Most of each year's government revenue is therefore booked and billed within the year.

---

## 2. Segment revenue and profit, 2021 to H1 2026

USD k. Segment result is direct profit before shared salaries, S&M, G&A, finance and tax. To 2025 it is after lease interest (gilat_fy2025 p.181). Sources: gilat_fy2023 p.10, p.166-167; gilat_fy2024 p.11; gilat_fy2025 p.97-98, p.181-182. Margins, shares and growth are from calc §1.

| | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| **Government/defence revenue** | 13,385 | 14,771 | 22,213 | 36,949 | 48,065 |
| — growth | | +10.4% | +50.4% | +66.3% | +30.1% |
| — segment result | 3,533 | 4,189 | 5,865 | 10,398 | 16,620 |
| — margin | 26.4% | 28.4% | 26.4% | 28.1% | 34.6% |
| **Global (Africa) revenue** | 38,431 | 27,345 | 25,747 | 19,948 | 19,655 |
| — growth | | −28.8% | −5.8% | −22.5% | −1.5% |
| — segment result | 9,412 | 5,495 | 5,481 | 3,544 | 4,106 |
| — margin | 24.5% | 20.1% | 21.3% | 17.8% | 20.9% |
| **Israel ISP revenue** | – | 882 | 7,194 | 12,695 | 8,073 |
| — segment result | – | (342) | (418) | (37) | 524 |
| Sum of segment results | 12,945 | 9,342 | 10,928 | 13,905 | 21,250 |
| Central costs: unallocated cost of revenue, S&M and G&A | 17,025 | 11,546 | 8,991 | 10,580 | 13,197 |
| **Lease-adjusted EBIT** (segment results minus central costs) | (4,080) | (2,204) | 1,937 | 3,325 | 8,053 |
| Reported operating income (gilat_fy2023 p.118; gilat_fy2025 p.127) | (2,731) | (1,499) | 2,178 | 4,949 | 9,689 |
| Group revenue | 51,816 | 42,997 | 55,154 | 69,592 | 75,793 |
| Gross margin | 24.0% | 24.4% | 21.8% | 23.2% | 30.4% |
| Operating margin | −5.3% | −3.5% | 3.9% | 7.1% | 12.8% |
| Net income | (5,423) | (4,064) | 715 | 1,786 | 6,350 |

H1 2026 figures are in ILS k, on the new two-segment basis (gilat_h1_2026 p.6, p.12; calc §7):

| | H1 2025 | H1 2026 | FY2025 |
|---|---|---|---|
| Satellite (commercial and government) revenue | 106,360 | 119,422 (+12.3%) | 224,369 |
| — segment result | 23,440 (22.0%) | 39,769 (33.3%) | 69,057 (30.8%) |
| Internet, communications and cloud revenue | 17,874 | 20,569 (+15.1%) | 35,966 |
| — segment result | 1,423 (8.0%) | 2,613 (12.7%) | 3,541 (9.8%) |
| Revenue | 124,234 | 139,991 (+12.7%) | 260,335 |
| Gross profit | 35,978 (29.0%) | 42,251 (30.2%) (+17.4%) | 78,938 |
| Operating income | 12,841 (10.3%) | 19,395 (13.9%) (+51.0%) | 32,981 |
| Net income | 4,044 | 15,770 | 21,259 |

**Caution on the 2026 segment figures.** The restated H1 2025 segment costs are ILS 11,115k above cost of revenue. In H1 2026, segment costs roughly equal cost of revenue (a difference of −131). Derived H2 2025 shows −4,775 (calc §7). The restatement is therefore not on one consistent basis, and the +69.7% jump in satellite segment result (calc §7) overstates the real improvement. Use consolidated figures instead:
- gross profit +17.4%;
- operating income +51.0%;
- S&M plus G&A −1.2% (calc §7).

**Why each segment moved.**

*Government/defence.*
- **2022:** +10.4%, the pre-war pace.
- **2023:** "service revenue and one-off equipment revenue, with emphasis on Q4 2023 due to the outbreak of the war" (gilat_fy2023 p.88). Q4 2023 group revenue was 18,830, against 11,277–12,583 in Q1–Q3 (gilat_fy2023 p.86).
- **2024:** service and one-off equipment revenue, "inter alia due to the outbreak of the war" (gilat_fy2024 p.86).
- **2025:** "part of the growth was due to security events, although a general global trend of rising demand is evident" (gilat_fy2025 p.97). Customer A grew 2.10x, from 9,164 to 19,278 (gilat_fy2025 p.32; calc §7). Margin rose to 34.6%, helped by "high-profitability deals" and a credit from a satellite supplier (gilat_fy2025 p.96).
- **H1 2026:** satellite revenue +12.3%, with "one-off equipment revenue, inter alia due to the 'Roaring Lion' war". Segment costs fell "due to the decline in the dollar exchange rate" (gilat_h1_2026 p.12).

*Global (Africa).*
- **2022:** revenue −28.8% when a global contract with a DRC customer ended (gilat_fy2023 p.88).
- **2023:** −5.8% when an O3B services contract ended (gilat_fy2023 p.88).
- **2024:** −22.5%, "a decline in traditional satellite in Africa" (gilat_fy2024 p.86).
- Profit was defended by cutting costs. Fixed costs fell 47% between 2021 and 2024 (calc §1; gilat_fy2023 p.10, gilat_fy2024 p.11). The Vodacom renewal helped from 2024.
- At the end of 2025 Africa stopped being a division and became a lean sales unit (gilat_fy2025 p.90).

*ISP.*
- Losses in 2022–2024 while it scaled.
- It turned positive in 2025 "due to the strategic agreement with Bezeq", which cut line costs from 1.1.2025 (gilat_fy2025 p.98).
- Revenue fell only because the yes pass-through ended (gilat_fy2025 p.97).

*Central costs.* These are unallocated cost of revenue, S&M and G&A.
- They fell from 32.9% of revenue in 2021 to 15.2% in 2024, then rose to 17.4% in 2025 (calc §1).
- 2025 drivers: advertising for the ISP brand (USD 1,151k in 2025 against 46k in 2023), agent commissions and a weaker USD against ILS-denominated costs (gilat_fy2025 p.96, p.174).

---

## 3. Customer concentration

Calc §5; sources gilat_fy2025 p.32, p.55, p.182; gilat_fy2024 p.170; gilat_fy2023 p.168.

| Share of group revenue | 2021 | 2022 | 2023 | 2024 | 2025 | H1 2026 |
|---|---|---|---|---|---|---|
| Customer A: unnamed Israeli buyer of mobile satellite solutions (government segment) | n/a | n/a | <10% | 13.2% | **25.4%** | n/a |
| Vodacom (DRC; global segment) | n/a | n/a | 20.0% | 15.1% | 16.3% | n/a |
| Customer B: 'yes' wholesale (ISP; ended end-2025) | – | 2.0% | 11.6% | 13.5% | <10% | – |
| Israel | 24.0% | 33.2% | 54.4% | 72.1% | 74.5% | 76.7% |
| DR Congo | 44.4% | 31.4% | 22.6% | 16.0% | 17.1% | n/a |

- **The top two customers were 41.8% of 2025 revenue.** The top three were 41.7% of 2024 revenue.
- Customer A was 40.1% of the government segment in 2025. Vodacom was 63.0% of the global segment.
- The 2023 report shows one global-segment customer at about USD 11M in both 2022 and 2023 (gilat_fy2023 p.168). That is most likely Vodacom, which had USD 11,028k in 2023 (gilat_fy2025 p.55). The 2022 identity is not stated.
- Africa outside the DRC is spread over many small accounts (gilat_fy2025 p.80, p.106).
- The company does not name Customer A. Given the segment's customer list (gilat_fy2025 p.31) it is very likely an Israeli defence or security body. That is **UNVERIFIED**.

---

## 4. Backlog (צבר הזמנות)

USD k at 31 December. Sources: gilat_fy2023 p.31-32, p.47, p.52; gilat_fy2024 p.33, p.44, p.49-50; gilat_fy2025 p.32, p.48, p.57-58; gilat_h1_2026 p.3, p.14. Totals and coverage ratios are from calc §6.

| | 31.12.2022 | 31.12.2023 | 31.12.2024 | 31.12.2025 | Report date 8.2026 |
|---|---|---|---|---|---|
| Government/defence | 3,100 | 17,500 | 19,800 | 22,600 | |
| Global | 18,500 | 11,100 | 44,500 | 27,700 | |
| ISP | 1,500 | 1,900 | 3,200 | 2,080 | |
| **Total** | **23,100** | **30,500** | **67,500** | **52,380** | **ILS 158M (≈ USD 50.0M at 3.157)** |
| Part due in the next year | | 19,414 | 34,655 | 43,424 | |
| — as % of next year's actual revenue | | 27.9% (of 2024) | 45.7% (of 2025) | 57.3% of FY2025 revenue | |

The trend:
- Backlog peaked at the end of 2024 on the Vodacom renewal and has been running off since.
- Government backlog is short: **90.2% of the end-2025 government backlog falls due within 2026** (calc §6).
- The jump from 3,100 to 17,500 at the end of 2023 coincides with the 4-year ILS 39M contract and ILS 16M of Q4 2023 orders (gilat_fy2023 p.84).

Headline backlog figures move between dates and horizons:
- **FY2023 report:** about USD 30.5M to 2027 at publication (gilat_fy2023 p.83).
- **FY2024 report:** about USD 67M to 2028 at the report date (gilat_fy2024 p.80, p.127), and about USD 61M to 2028 at publication (gilat_fy2024 p.92).
- **FY2025 report:** about USD 52.3M to 2029 at the report date (gilat_fy2025 p.89), and about USD 58.3M to 2028 at publication (gilat_fy2025 p.102).

The segment tables add up to the report-date figures. Treat the publication-date figures as indicative only.

---

## 5. Competition and market structure

**Government/defence.**
- In the company's words: "many large, medium and small players, some of them far larger than the group; competition focuses mainly on price and the ability to offer a full solution; the group's share is not material" (gilat_fy2025 p.32).
- Named satellite rivals in Israel: MX1 (formerly RR Media) and Linkcom (gilat_fy2025 p.58).
- Starlink is "a direct competitor of the company's GEO-based VSAT products". It sells direct to end users at prices far below industry norms (gilat_fy2025 p.15-16, p.50-51).
- The state is building sovereign capacity. The national satellite Dror-1 was launched in July 2025. Gilat expects it to add to the market rather than replace existing services (gilat_fy2025 p.19-20).
- Gilat holds Israeli authorisations to provide OneWeb and Starlink Israel access (gilat_fy2025 p.71-72). It treats Eutelsat-OneWeb and Amazon Kuiper as possible partners (gilat_fy2025 p.16).

**Global (Africa).**
- Rivals: EMC, Marlink and Speedcast, and satellite operators selling direct, such as SES/New Skies, Intelsat, ABS, Spacecom and Starlink (gilat_fy2025 p.58).
- Substitutes: undersea and land fibre (every country where Gilat operates now has undersea fibre), mobile operators' own 4G/LTE, and microwave backhaul (gilat_fy2025 p.25-26, p.53-54).
- The price per megabit keeps falling. Consumption rises, so revenue stays "relatively stable" (gilat_fy2025 p.52).
- The company calls its outlook in Africa "a challenging horizon for significant growth" (gilat_fy2025 p.27).

**Israeli ISP.**
- Four groups dominate: Bezeq, Partner, Cellcom and HOT hold about 95% of private fibre internet, and Bezeq alone holds more than 80% of the business market (gilat_fy2025 p.34, p.45). Bezeq's retail share is about 30–35%; the others hold 15–25% each (gilat_fy2025 p.14).
- Only Bezeq and IBC own nationwide fixed infrastructure. Partner has its own fibre to about 1M homes (gilat_fy2025 p.13).
- Small ISPs without infrastructure "have disappeared". Gilat calls itself almost the only challenger. It says retail prices are similar across the big groups, "relatively high" and give them high profits (gilat_fy2025 p.45).
- Entry barriers for an ISP without infrastructure are "low": a general-permit registration is enough. The company argues critical mass is still needed, and that it has reached it (gilat_fy2025 p.45).
- Gilat's market share is "still relatively small" (gilat_fy2025 p.35). In the FY2023 report it was "negligible" (gilat_fy2023 p.32).
- Wholesale prices are "determined mainly by the regulator" (gilat_fy2025 p.38).

---

## 6. Regulation and licences

**Ministry of Communications licences** (gilat_fy2025 p.69-72):

| Licence or permit | Valid to | Notes |
|---|---|---|
| Unified satellite licence: VSAT, video and audio transmission, international transmission | **31.12.2026** | |
| Iridium terminal licence | 31.12.2026 | also covers Judea and Samaria |
| Trade licence | 31.12.2026 | also covers Judea and Samaria |
| OneWeb terminal licence | 31.12.2026 | |
| ISP general permit | 31.3.2028 | renewed every 2 years |
| Radiation permit for the teleport | 19.5.2029 | |

**Licence conditions** (gilat_fy2025 p.72-74):
- The company must be "Israeli": incorporated in Israel, managed from Israel, with its centre of business there.
- Any holding of 10% or more, and any transfer of control, needs the Minister's prior approval.
- Holding 25% or more is presumed to give "significant influence".
- At least a third of the directors, and at least two, must have security clearance. There must be a security committee.
- The Ministry may place an observer on the board.
- These rules protect incumbents against foreign entrants, but they also limit who could buy the company.

**Domestic satellite service must use Spacecom transponders** unless Spacecom cannot supply them (gilat_fy2025 p.70).

**Abroad.** Uganda NPSP licence to 30.6.2030 (gilat_fy2025 p.75). In other countries, local licensing is the customer's responsibility under the contracts.

**Wholesale fixed-line regulation.** The Minister's decision of 26.2.2026 sets (gilat_fy2025 p.39-40):
- fibre BSA up to 1 Gbps at ILS 58/month, fixed for 2026–2031;
- quotas for the big four, with the regulated price applying to their quota until 31.8.2028;
- unlimited regulated BSA for small ISPs such as Gilat.

The text is ambiguous on whether the 31.8.2028 end of regulated pricing also applies to small ISPs.

Hearings from 18.2.2026 propose prior approval for agreements between infrastructure owners and large operators (gilat_fy2025 p.40-41).

**Other.** 5G frequencies overlap satellite C-band reception, which needs coordination and filters (gilat_fy2025 p.82). Consumer-protection and privacy law apply, including Amendment 13 from August 2025 (gilat_fy2025 p.75-76).

**Litigation.** Gilat is pursuing Nextel Cameroon and its parent for about EUR 4.8M of unpaid debt. The case is at an early stage and the outcome cannot be assessed (gilat_fy2025 p.76).

---

## 7. Suppliers and dependencies

**Satellite capacity.**
- Gilat leases from "several main suppliers" on terms from a few months to 3 years. Its liability cover towards customers is not fully back-to-back (gilat_fy2025 p.64).
- Management says it has **no dependence** on any one supplier. It also admits that losing a main supplier would hurt sales in the short term, and that moving customers is costly and may lose some of them (gilat_fy2025 p.66).

**Intelsat, the key supplier since 2006** (gilat_fy2025 p.64), has a history of overdue balances:
- **March 2020:** about USD 6M overdue was rescheduled over 24 months. Intelsat granted a USD 2M credit tied to the Vodacom renewal. The balance was repaid in February 2022 (gilat_fy2023 p.146).
- **2023:** about USD 4.1M was overdue. In May 2023 Intelsat demanded payment and **warned it would suspend service** (gilat_fy2023 p.146).
- **End-2024:** about USD 4.46M was open (gilat_fy2024 p.150).
- **End-2025:** about USD 4.5M was open, described as "the ordinary course of business" (gilat_fy2025 p.160).
- An agreement signed in 2024 gives competitive capacity pricing. In return Gilat commits to future purchases, backed by customer orders, and Intelsat commits to **one-off credits** and infrastructure investment (gilat_fy2024 p.150; gilat_fy2025 p.160).
- Part of Gilat's negative working capital is therefore credit from Intelsat. The Vodacom economics depend on Intelsat's pricing and credits.

**SES/O3b.** Framework since 2016, renewed in 2019 (gilat_fy2025 p.65-66). SES/O3b MEO capacity, including mPOWER, is central to the Vodacom service.

**Mobile satellite networks.** Iridium (since 2003), Inmarsat (since 2018) and Thuraya (to 7.2028). The company calls these agreements the main entry barrier to the business. They are short, renew automatically, and Iridium can change prices on 30 days' notice (gilat_fy2025 p.66-67).

**Fibre.** Bezeq, through the IRUs (§1.6). This is a structural dependence for the ISP. Gilat also leases fibre segments for 17–23 years (gilat_fy2025 p.159).

**Equipment.** It comes from many vendors. No supplier other than the satellite and fibre suppliers is above 10% of purchases (gilat_fy2025 p.67).

---

## 8. Employees

Sources: gilat_fy2023 p.57; gilat_fy2025 p.61-62.

| At 31 December | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|
| Total | 88 | 100 | 104 | 117 |
| — ISP support, service and sales (includes part-time shift staff) | 15 | 27 | 29 | 41 |
| — Israel communications sales | 10 | 12 | 15 | 23 |
| — Government/defence sales | 8 | 7 | 6 | 6 |
| — Global sales | 10 | 9 | 7 | 2 |
| — Uganda | 10 | 9 | 11 | 7 |

- Revenue per employee was USD 648k in 2025 (calc §8).
- The report says total payroll fell even as headcount rose, because most new hires are part-time (gilat_fy2025 p.62). **Its own notes contradict this.** Salaries across cost of revenue, S&M and G&A were USD 7,090k in 2023, 7,923k in 2024 and 9,560k in 2025: +20.7% in 2025 and +34.8% since 2023 (gilat_fy2025 p.173-174; calc §3). The same sentence appears in the 2023 and 2024 reports (gilat_fy2023 p.57; gilat_fy2024 p.54), so it reads as boilerplate.
- Staff are employed on personal contracts (gilat_fy2025 p.63).
- In December 2025 the company granted options over 4.665M shares to 32 employees, 4 of them officers, and over 4.0M shares to the CEO. Exercise prices are 92.7 and 110.15 agorot (gilat_fy2025 p.62-63).

---

## 9. Seasonality

The company reports no seasonality in Africa, and none so far in the ISP (gilat_fy2025 p.48, p.59).

Quarterly revenue moves with events, not seasons (calc §4; gilat_fy2023 p.86, gilat_fy2024 p.82, gilat_fy2025 p.92). USD k:

| | Q1 | Q2 | Q3 | Q4 |
|---|---|---|---|---|
| 2023 revenue | 11,277 | 12,583 | 12,464 | 18,830 |
| 2024 revenue | 15,483 | 18,123 | 19,276 | 16,710 |
| 2025 revenue | 15,994 | 18,585 | 20,075 | 21,139 |
| 2025 gross margin | 28.3% | 29.6% | 27.8% | **35.3%** |

- Q4 2023 is the outbreak of war.
- Q4 2025 is a margin spike. The 2025 satellite-supplier credit may explain part of it; neither its amount nor its quarter is disclosed.

---

## 10. Strategy across the three reports, and what was delivered

**FY2023 report (approved 26.3.2024).** The strategy adopted in 2022 had three legs (gilat_fy2023 p.72-74):
1. Build the ISP into a growing revenue and profit division.
2. Fixed satellite: run for profit and avoid high-risk projects.
3. Mobile satellite and HLS-D: grow, invest in sales, add territories and complex projects.

For government, the plan was to expand into Asia, Africa and Central and South America and to move to full solutions. Management's framing (gilat_fy2023 p.83-84):
- 2023 was "a turning point";
- the Africa division "reinvented itself" as a lean unit;
- the ISP had been launched "without significant expenses";
- the 2023 profit came "partly from one-off effects".

**FY2024 report (27.3.2025).** The strategy was restated as "reduce Africa exposure, focus on government/defence, launch a new business line" (gilat_fy2024 p.6). A fourth leg was added: investments and acquisitions in adjacent fields to raise shareholder return (gilat_fy2024 p.7). The Bezeq IRU "meets the business-plan target" of the segment (gilat_fy2024 p.11). ILS 45M of Series D convertibles were raised in 2.2025 for growth engines and "synergistic strategic deals" (gilat_fy2024 p.80).

**FY2025 report (25.3.2026).** Five legs (gilat_fy2025 p.7):
1. Internet and cloud: build the brand, grow households, run business customers for profit.
2. Mobile satellite and HLS-D: growth.
3. Commercial satellite: profit.
4. Investments and acquisitions.
5. Financing: a "net financial asset", conversions of debt into equity, and studying ways to return value. Dividends "may be considered" (gilat_fy2025 p.10).

Organisation and accounting changes:
- Africa became a sales unit and integration was merged into one unit (gilat_fy2025 p.90).
- The functional currency moved to ILS from 1.1.2026 (gilat_fy2025 p.90).

**Q2 2026 report (19.8.2026).**
- New two-segment reporting (gilat_h1_2026 p.3-4).
- Growth in combined integration and government projects (gilat_h1_2026 p.4).
- An ILS 6M buyback in June 2026: 2.3M shares (gilat_h1_2026 p.3).
- A long-run ARPU target of ILS 90 (gilat_h1_2026 p.8).

**Delivery scorecard.** Figures are from calc §1, §2, §5 and §9.

| Stated aim | What happened | Verdict |
|---|---|---|
| Reduce exposure to Africa | Africa revenue fell 51% between 2021 and 2025, from 73.7% to 24.8% of group revenue. Much of the fall was lost contracts (O3B, a DRC global contract), not choice, and the segment now depends on Vodacom (63.0% of it) | Delivered, partly by default |
| Grow government/defence | 3.59x between 2021 and 2025. The company itself attributes part to the wars | Delivered, with the war's help |
| Expand government sales abroad (Asia, Africa, Latin America) | Israel is still about 99% of the segment (gilat_fy2025 p.31) | **Not delivered** |
| Build a profitable ISP "without significant investment" | Profitable from 2025, with 25,045 subscribers. But it now carries ILS 248M of Bezeq commitments, its ARPU is below peers and falling in 2026, and its reported profit benefits from 25-year amortisation | Delivered on growth; the "low investment" claim no longer holds |
| Acquisitions and investments in adjacent fields | None reported to H1 2026 | Not executed. That is better than a bad deal |
| Strong balance sheet, "not leveraged" (gilat_fy2025 p.90) | Net financial asset of ILS 66M at 30.6.2026 (gilat_h1_2026 p.3), but the IRU instalments are off balance sheet. Weighted shares rose 53.6% between 2022 and 2025 (gilat_fy2023 p.118; gilat_fy2025 p.127), and conversions continue in 2026 | Mixed |
| Profit | From losses in 2021–2022 to USD 6,350k of net income in 2025 and ILS 15,770k in H1 2026 | Delivered, on war demand |

**Candour.** The reports are promotional. The ISP is said to be "shattering market forecasts" (gilat_fy2025 p.90), and every year is called a record.
- The headline "free cash flow excluding prepaid expenses" adds back real costs: the Vodacom-deal prepayment and the Bezeq IRU instalments (gilat_fy2024 p.83; gilat_fy2025 p.93, p.95).
- Several figures disagree within the same report (§14).
- Against that, the risks are disclosed: Intelsat's suspension warning, the identity of Vodacom, and the role of the war.

---

## 11. Moat: source, durability, evidence

**Sources the company claims:**
- licences and security clearances, and the distribution agreements;
- integration and engineering know-how, and long customer relationships (gilat_fy2025 p.33, p.54, p.59);
- a lower line cost in the ISP through the Bezeq IRU (gilat_fy2025 p.35, p.39).

**Assessment by business.**
- **Government/defence: narrow at best.**
  - *What is real.* There are licensing and security barriers that keep foreigners out (§6). Incumbency with Israeli defence buyers comes from the exclusive framework to 2029 and the 4-year contract with options for up to 11 more years (gilat_fy2025 p.103). Integration skill matters in a crisis.
  - *What limits it.* Competition is on price, there are many rivals and Gilat's share is "not material" (gilat_fy2025 p.32). The distribution rights are short and its suppliers can reprice (gilat_fy2025 p.66-67). Low-orbit operators sell direct (gilat_fy2025 p.16). The state is building its own capacity (Dror-1). One customer is 40.1% of the segment (calc §5).
  - *Margin evidence.* 26.4–28.4% in 2021–2024 and 34.6% only in 2025 (calc §1). That looks like scarcity pricing during a war, not a durable advantage.
- **Global/Africa: no moat.** Revenue fell 49% between 2021 and 2025. Margins ranged 17.8–24.5% (calc §1). The price per megabit keeps falling, and fibre and low-orbit satellites replace it (gilat_fy2025 p.52-54). The goodwill test values the segment at USD 44,970k against a carrying amount of USD 18,063k, using a 20% pre-tax discount rate and 2.5% terminal growth (gilat_fy2025 p.109). That is management's own model, not evidence of a moat.
- **ISP: no moat.**
  - It is a challenger in a regulated oligopoly, with entry barriers the company calls "low" for an ISP without infrastructure (gilat_fy2025 p.45).
  - The IRU gives cost parity with Partner's Bezeq deal, not an advantage (§1.6).
  - It prices 15–42% below peers (calc §9).
  - Its edge is service and brand at a lower price. That can win share. It is not a franchise.

**Returns on capital and margins over time** (calc §2 and §8; gilat_fy2023 p.116-118; gilat_fy2025 p.125-127):

| | 2021 | 2022 | 2023 | 2024 | 2025 | TTM 6.2026 |
|---|---|---|---|---|---|---|
| Gross margin | 24.0% | 24.4% | 21.8% | 23.2% | 30.4% | 30.9% |
| Operating margin | −5.3% | −3.5% | 3.9% | 7.1% | 12.8% | 14.3% |
| Adjusted EBITDA margin (satellite leases as costs) | 4.4% | 7.0% | 10.6% | 12.5% | 19.5% | 21.3% |
| Operating working capital + PP&E (leases as operating costs) | n/a | (5,221) | (3,757) | 2,513 | 5,015 | n/a |
| Pre-tax return on that capital | n/a | n/m (capital < 0) | n/m (capital < 0) | 132% | 161% | n/a |
| EBIT ÷ capital including right-of-use assets | n/a | −38% | 58% | 19% | 44% | n/a |
| ROE on average equity | n/a | n/a | 6.7% | 13.1% | 31.6% | n/a |

- In 2022–2023 the business had negative tangible capital. Suppliers and customers financed it. In good years returns look extraordinary, in bad years they are negative.
- **Returns on capital tell us the model is asset-light. They do not show a moat.** The test of a moat is whether margins hold through a cycle, and the only pre-war years available, 2021–2022, show operating losses.
- **Durability: low to moderate.** Each of the four engines depends on a third party's decision:
  - Israeli defence budgets and wars;
  - Vodacom's renewal in 2027;
  - Intelsat and SES pricing;
  - Bezeq and the regulator.

---

## 12. Is TTM-to-June-2026 earnings power representative? Normalised earnings

**TTM to 30.6.2026, ILS k** (FY2025 − H1 2025 + H1 2026; calc §7). It matches the Mega export.

| Item | TTM |
|---|---|
| Revenue | 276,092 |
| Gross profit | 85,211 (30.9%) |
| Operating income | 39,535 (14.3%) |
| Adjusted EBITDA | 58,787 |
| Net income | 32,985 |
| Operating cash flow | 80,967 |
| Operating cash flow − capex − lease payments | 34,271, still after the IRU prepayments |
| Operating income in USD at spot | 12,523 |

**Verdict: TTM is near-peak.** Five things flatter it or put it at risk:

| # | Factor | Effect on TTM |
|---|---|---|
| 1 | **Defence demand from the wars**: "Swords of Iron" from 10.2023, "Am KeLavi" in 6.2025 and "Roaring Lion" from 28.2.2026 (gilat_fy2025 p.9). The company itself links the growth to the wars (gilat_fy2023 p.88; gilat_fy2024 p.86; gilat_fy2025 p.97; gilat_h1_2026 p.12) | Israeli satellite revenue (proxy: satellite segment minus all Africa) is ILS 176,246k TTM, 63.8% of revenue (calc §7). Government revenue in 2025 was 3.25x 2022 (calc §1) |
| 2 | **One-off equipment revenue** in H1 2026 (gilat_h1_2026 p.12) | Amount not disclosed: **UNVERIFIED** |
| 3 | **One-off credit from a satellite supplier** in 2025 (gilat_fy2025 p.96, p.160) | Amount not disclosed. Q4 2025 gross profit was USD 1,423k (ILS 4,700k) above the Q1–Q3 margin of 28.53% (calc §4). I use that as the allowance (analyst estimate) |
| 4 | **Currency.** The USD fell 14.23% against the ILS in 2025 (gilat_fy2025 p.136). Revenue is now mostly ILS, but satellite costs are USD: Gilat hedges USD 2M a month to 12.2026 and USD 1.5M a month in 2027 (gilat_h1_2026 p.18-19). The 2026 fall in satellite segment costs is attributed to the weaker USD (gilat_h1_2026 p.12) | A 10% rebound in USD/ILS from spot costs about **ILS 7,577k a year, 19% of TTM operating income** (calc §10) |
| 5 | **Vodacom runs to 3.2027.** Renewal is "being worked on" (gilat_h1_2026 p.15) | At spot it is worth ILS 39,122k of revenue (calc §11) |

On the other side:
- the ISP is still ramping;
- the non-cash option revaluations stopped in 2026 (gilat_h1_2026 p.6).

**Normalised operating earnings.** These treat leases as operating costs: TTM operating income less a lease-interest proxy of ILS 5,642k (FY2025 lease interest USD 1,787k at spot). They are analyst estimates (calc §11). Lost revenue is taken at the FY2025 government segment margin of 34.6%.

**Bear: a loss of ILS 11,921k (USD −3,776k).** Assumptions:
- Israeli satellite revenue falls to 46.2% of TTM, the 2023/2025 ratio;
- the one-off allowance is removed;
- Vodacom is lost, at the global segment's 20.9% margin;
- the ISP earns zero;
- central costs are cut by 10%.

If the USD also rebounds 10%, the loss is ILS 19,497k.

**Base: ILS 15,099k (USD 4,783k), 38% of TTM operating income.** Assumptions:
- Israeli satellite revenue at 76.9% of TTM, the 2024/2025 ratio;
- the one-off allowance is removed;
- Vodacom is renewed;
- the ISP stays at its TTM result.

**Bull: ILS 38,624k (USD 12,235k), 98% of TTM operating income.** Assumptions:
- TTM demand persists;
- the ISP result doubles as lines fill.

**Probability-weighted** (bear 25%, base 50%, bull 25%): ILS 14,226k (USD 4,506k).

For comparison:
- TTM "as is", leases as costs, is ILS 33,893k.
- History of lease-adjusted EBIT, USD k: 2021 (4,080), 2022 (2,204), 2023 1,937, 2024 3,325, 2025 8,053.
- The 5-year average is USD 1,406k. The 2024–2025 average is USD 5,689k.

Recommendation to the valuation:
1. **Use the base, about ILS 15M of pre-tax operating profit with leases as costs, as normalised earnings power.** It sits between 2024 and 2025 actual results. Do not capitalise TTM.
2. Because lease interest is already charged, do not deduct lease liabilities again from net cash.
3. **Treat the unpaid Bezeq IRU instalments as a debt-like obligation, or charge the 15-year economic cost.** At full delivery the 25-year accounting understates the annual cost by about ILS 6,614k (calc §9).

Taxes are left to the valuation section.

---

## 13. Circle-of-competence verdict

**Understandable: yes.** The mechanics are simple. Gilat buys capacity, airtime and fibre lines, adds integration and service, resells them monthly with a spread, and sells equipment on top. The cost structure, the contracts and the main risks are disclosed in plain terms.

**Predictable 5–10 years out: no.** The things that decide the result are outside an owner's view and outside the company's control:
- (a) How long Israel's defence establishment keeps paying for satellite redundancy at war-time levels. A quarter of revenue comes from one unnamed customer, ordering 12 months at a time.
- (b) The Vodacom renewal in 2027 and the steady erosion of satellite in Africa by fibre and low-orbit satellites.
- (c) Starlink, Kuiper and OneWeb selling direct.
- (d) Whether Gilat can fill 54,000 committed Bezeq lines at an adequate ARPU against four entrenched groups and a regulator that sets wholesale prices.
- (e) The USD/ILS rate.

Li Lu's test is to know the business better than the market. Here no outsider can know Customer A's plans. Buffett's test asks whether we can be confident of earnings 10 years out; we cannot.

**Fit with the fund.** This is not TOO_HARD in the fund's sense: the business is understandable and most key figures are verifiable. It is a **contract-driven, event-cyclical business with no durable moat**. It belongs in the cheap track: grade **C, plus about 5 points** for concentration, an undisclosed key customer and data inconsistencies. It can only be bought at a price that works on base or bear normalised earnings and on a balance sheet that counts the IRU obligations.

*Inversion: what would kill it?* Peace or a cut in defence budgets, together with:
- loss of Vodacom;
- an ISP price war that leaves the committed IRU lines empty;
- a stronger USD.

Each has a plausible path, and the bear case is a loss like 2021–2022.

---

## 14. Data issues and UNVERIFIED items

1. **Consolidated interim statements** for H1 2026 are not in the supplied document. The TTM uses directors'-report tables (gilat_h1_2026 p.6-14).
2. **Satellite-supplier credit (2025)** and **one-off equipment revenue (H1 2026)**: neither amount is disclosed. Both are UNVERIFIED. The Q4 2025 margin allowance is an estimate.
3. **Customer A's identity** is not disclosed. UNVERIFIED.
4. **Backlog** headlines change between report date and publication date, with different horizons: 67M against 61M in the FY2024 report, and 52.3M (to 2029) against 58.3M (to 2028) in the FY2025 report (gilat_fy2024 p.80, p.92; gilat_fy2025 p.89, p.102).
5. **2026 segment restatement is inconsistent across periods** (calc §7). Segment profit growth in H1 2026 is overstated. Use consolidated figures.
6. **H1 2025 revenue:** P&L ILS 124,234k against the regional total of 124,324k (gilat_h1_2026 p.6-7; calc §5). The text cites satellite revenue of ILS 119,847k against 119,422k in the table (gilat_h1_2026 p.14, p.12).
7. **Government 2023 "fixed costs"** are printed as 2,531. The table's own totals imply 3,794 (gilat_fy2023 p.10; gilat_fy2024 p.11; calc §1).
8. **FY2023 segment note:** total segment results are printed "810,92" (that is, 10,928), and pre-tax is 972 against the P&L's 944 (gilat_fy2023 p.166, p.118).
9. **FY2025 within-report differences:**
   - EBITDA 23,869 against 23,893, and adjusted EBITDA 14,786 against 14,810 (gilat_fy2025 p.92, p.96);
   - operating cash flow 20,530 against 20,611 (gilat_fy2025 p.93, p.98).
10. **The IRU amortisation charged in 2025** (USD 1,079k against USD 3,902k capitalised; gilat_fy2025 p.152, p.173) cannot be reconciled with the stated 25-year policy from the disclosures. The unpaid IRU instalments are not shown as a liability. UNVERIFIED; ask the company.
11. **Hedged USD costs** (USD 24M a year) are used as a proxy for the net USD cost exposure. The true net exposure is UNVERIFIED.
12. **Payroll statement:** "total salary expenses decreased" (gilat_fy2025 p.62) against salaries up 20.7% in the notes (gilat_fy2025 p.173-174; calc §3). It is boilerplate repeated from earlier reports.
