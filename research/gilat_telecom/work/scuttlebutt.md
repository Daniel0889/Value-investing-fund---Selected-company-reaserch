# Gilat Telecom Global (TASE 1080597): public-document scuttlebutt and market microstructure

Workstream for the Rev 4 study: framework (c)4 "public-document scuttlebutt"; checklist B7, E3, E5, E9, F1 and F6.
Researched 3.11.2026. The web pages were read on 3.11.2026 between 21:53 and 22:22 Israel time (UTC+2); the
Sources table gives each URL and the time it was read. This is an input to the synthesis, not a verdict.

**How to read this file.**
- Every derived number comes from `scuttle_calc.py`; its output is saved in `scuttle_calc_output.txt` and cited as
  "calc §n".
- Figures from the company's filings cite the document id and PDF page, for example "gilat_fy2025 p.214". The
  filing figures used here were checked on the PDF page image (gilat_fy2023 p.118, p.195; gilat_fy2024 p.192,
  p.199; gilat_fy2025 p.127, p.205, p.216; gilat_h1_2026 p.6, p.15). Passages quoted from the text layer are
  narrative, not table figures.
- Items resting on a search-engine summary, a headline or a reader comment, with the page itself not read, are
  marked **UNVERIFIED**.
- Peer financials come from S&P Global Market Intelligence via StockAnalysis. They are Tier 2 data and were not
  checked against the peers' own filings. StockAnalysis misstates Gilat's own TTM revenue by 12.5% (calc §4), so
  treat the peer table as indicative.
- Other workstreams are cited by file: `business.md`, `governance_risk.md`, `market.md` (same folder).

**Blocked or out of reach (not retried):**
- maya.tase.co.il and Magna block scripted access (the brief). mayafiles.tase.co.il returned HTTP 403 on 3.11.2026.
- funder.co.il returned 403; engineeringnews.co.za served a Cloudflare check.
- The Globes interested-party feed (GTOFeeder) returned no rows for this instrument; only the server-rendered
  ten most recent buyers and sellers were readable.
- Court databases (Nevo, Takdin, Net HaMishpat), the class-action register, the Pledges Registrar by name and the
  Ministry of Defence's procurement records were not searchable here.

---

## 0. Bottom line

1. **Liquidity clears every charter line, but it is new.**
   - Over the 60 sessions to 3.11.2026 (4.8–3.11.2026), median daily turnover was **ILS 1,325,803** and the 25th
     percentile **ILS 1,001,604**. No session traded below ILS 100,000 (calc §1).
   - The median is 26.5 times the ILS 50,000 floor and 13.3 times the ILS 100,000 price-reliability line. The
     charter liquidity cap (20 days × 20% × p25) is **ILS 4,006,416**, 2.01% of the market cap (calc §1).
   - A year earlier the 60-session median was only ILS 211,291 (p25 ILS 113,160). The liquidity came with the
     2026 re-rating and the bond conversions.
   - The share is **not on the maintenance list**: the public holds 85.8–92.0%, worth ILS 171–183M, 34–37 times the
     NIS 5M floor (calc §2, §8). It sits in TA Tel-Tech (weight 2.46%), TA Growth (1.82%) and TA All-Share (0.27%).
2. **No controller, and the chain is short (F1).**
   - Control was dispersed on 17.2.2021, when the liquidators of Eurocom (Shaul Elovitch's former group) sold the
     41% block to institutions in 2–3% lots. The Ministry of Communications required Israeli buyers and no
     dominant holder [CAL-0217]; gilat_fy2025 p.214.
   - The largest holders today are the CEO (9,547,586 shares, 7.93%) and the Ayalon mutual funds (6.22%) (calc §2).
   - No pledge is disclosed. A pledge on the CEO's shares **cannot be assessed here** (open).
3. **Who sold and who bought in the last two years (E3).**
   - **Sellers.** Shidurit Telepage, the holder the Ministry presumed to be the controller in October 2024 (13.8%,
     approved to go to 26%; gilat_fy2024 p.199; [BZ-834978]), sold down to about 3% by 4.3.2026. Its priced sales
     were ILS 7.29M at an average 156.4 agorot (calc §3). Ayalon funds reported reductions of 4,632,270 shares in
     2026. Meitav funds sold 1,891,278 at 196 agorot on
     5.10.2026. Bondholders converted: of the 38.8M gross increase in listed shares over two years, 31.1M came from
     conversions and option exercises and 7.71M from the placement (calc §3, §8).
   - **Buyers.** The CEO bought 640,966 shares (ILS 1.21M, average 188.6 agorot) and sold none. The company
     bought 4,574,810 shares for ILS 10.61M, at 260.3 agorot in June and 203.1 in October; today's close is 36.5%
     and 18.6% below those prices. Pasternak Shoham and Mor bought 7.71M new shares at 88 agorot in July 2025
     (calc §3).
4. **Against peers, the TTM margin is high; the five-year record is not.**
   - Gilat's TTM operating margin of 14.3% ranks 4th of 15 against Israeli telecom groups (median 14.0%),
     satellite operators (median 4.0%) and satcom equipment and service firms (median 1.9%) (calc §4).
   - Its 2021–25 median operating margin was 3.9%, which would rank 10th (calc §4).
   - The CEO himself said the war roughly doubled turnover, and that defence is "about 30%" of turnover in
     routine against about 50% in wartime [BZ-20014148]. The 2025 government share was 63.4% (business.md §0).
5. **Two outside facts the filings do not put in front of the reader.**
   - **Bezeq's own report of the fibre deals** (4.11.2025) gives total consideration of about NIS 140M for the
     2024 deal and "over NIS 600 million" for the 2025 addendum, including maintenance, interest and linkage,
     "with the majority … paid over the first years" [BZQ-IRU]. That is more than NIS 740M, 3.72 times today's market
     cap. Gilat's filings present the one-time amounts (ILS 88M + ILS 160M firm, ILS 488M if every tranche is
     taken). The one-time figures agree with Bezeq's (calc §5).
   - **Vodacom, 16.3% of 2025 revenue (business.md §3) under a contract ending 31.3.2027, signed a pan-African Starlink backhaul
     and resale agreement on 12.11.2025** [SIA-VOD]. Starlink went live in the DRC in June 2025 [CA-DRC], and
     Vodacom agreed infrastructure sharing with Airtel in the DRC in August 2025 [DT-AIRTEL]. The FY2025 report
     (approved March 2026) and the Q2 2026 report do not mention the Starlink agreement. They say only that the
     company "is working to renew" (gilat_h1_2026 p.15).
6. **Moat from the outside: incumbency, not a franchise.**
   - Government procurement data show Gilat as the holder of the Accountant General's central satellite tender
     since 2012 [GOV-EXEMPT], and defence frameworks have been renewed [BZ-838877].
   - Licences are not exclusive. Spacecom received the same OneWeb approval on the same day [BZ-20013709]. Starlink
     has sold direct to Israelis since August 2025 [GL-STAR].
   - In the ISP, Gilat pays about what Partner pays Bezeq per line (+2.2% for the 2024 lines, −7.1% for the first
     2025 tranche) (calc §5). That is cost parity, not an advantage.
7. **B7: no record of misconduct, sanction or conviction** of the company, its directors or its officers in the
   sources checked: the Companies Registrar, government procurement data, and searches of the ISA, the Ministry
   of Communications and the press.
   - Chairman Ami Barlev was general counsel of the Elovitch group (Eurocom). He replaced Elovitch on the boards of
     Internet Gold and Bezeq in 2018 and later ran B Communications' debt settlement [WAL-0403]; [CAL-0109]. He was
     interim CEO of Vesttoo after its fraud came to light in 2023 [IJ-0815]. These were clean-up roles, and no
     allegation against him personally was found.
   - His FY2023 biography lists Vesttoo (gilat_fy2023 p.195); the FY2025 biography drops it (gilat_fy2025 p.216).
   - Court databases were not searchable, so B7 stays open on the courts.
8. **Smaller findings.**
   - Goldphone Ltd, approved in October 2024 to hold up to 13.4% (gilat_fy2024 p.199), is flagged a "violating
     company" by the Companies Registrar and has filed no annual report [ICA].
   - The Nexttel receivable (EUR 4.8M; gilat_fy2025 p.76) is caught in a shareholder war between Viettel and
     BestCam that began with the Gilat contract itself [CAMER].
   - The CEO said Gilat petitioned the High Court against the Ministry over wholesale prices and withdrew after the
     Bezeq deal [BZ-838877]. The docket was not found.

---

## 1. Competitors, and how their margins and returns compare (E5, E9)

### 1.1 Who competes

| Segment | Competitor | Evidence |
|---|---|---|
| Government and defence, Israel | **Spacecom (Space Communication, TASE: SCC)**, operator of the AMOS satellites | Domestic satellite service must use Spacecom transponders unless Spacecom cannot supply (gilat_fy2025 p.70). Spacecom got the Ministry's OneWeb LEO approval on the same day as Gilat, 19.2.2025 [BZ-20013709]. Its CEO Dan Zajicek [BZ-20013709] was Gilat Telecom's CEO in 2018 [ITW-NEXT]. Supplier and rival at once |
| | MX1 (formerly RR Media), Linkcom | Named by the company (gilat_fy2025 p.58) |
| | Applied Satellite Technology (AST, UK) | Won the 2013 Israeli government MSS contract (Inmarsat and Iridium) jointly with Gilat Satcom [SATTODAY-2013]. **UNVERIFIED**: search summary, page not read |
| | Starlink | Licensed by the Ministry in February 2024; consumer service from 8.8.2025 at NIS 230 a month and up, sold direct [GL-STAR]. The company calls it "a direct competitor" of its GEO VSAT products (gilat_fy2025 p.16). Gilat also holds the Director's instruction to provide access to the Starlink Israel network (gilat_fy2025 p.71-72) |
| | Elbit, Rafael | Described by the CEO as partners, not rivals [BZ-20014148] |
| Global, mainly Africa | Marlink, Speedcast, EMC; operators selling direct (SES with Intelsat, ABS, Spacecom, Starlink) | gilat_fy2025 p.58 |
| | **The customer itself.** Vodacom will resell Starlink to enterprises and use Starlink backhaul across its markets | [SIA-VOD] 12.11.2025; [TT-VOD]. Regulatory approval is needed market by market [CA-VOD] |
| | Mobile operators sharing infrastructure (Vodacom with Airtel in the DRC, Tanzania and Mozambique) | [DT-AIRTEL] 12.8.2025; subject to approvals |
| Israeli ISP | Bezeq, Partner, Cellcom, HOT (about 95% of private fibre); IBC/Unlimited as wholesaler | gilat_fy2025 p.34, p.45. Partner holds the template IRU: 120,000 lines for NIS 574M + VAT in five instalments, about NIS 1bn with 4% maintenance [GL-PTNR] |

### 1.2 Returns and multiples (TTM; StockAnalysis, read 3.11.2026 22:03–22:04; calc §4)

| Company | Currency | Revenue (m) | Operating income (m) | Op. margin | ROIC | ROE | P/E | EV/EBIT | Debt/equity |
|---|---|---|---|---|---|---|---|---|---|
| **Gilat Telecom, TTM to 30.6.2026 (filings)** | ILS | 276.1 | 39.5 | **14.3%** | — | — | — | — | — |
| **Gilat Telecom, 2021–25 median (filings)** | USD | — | — | **3.9%** | — | — | — | — | — |
| Bezeq | ILS | 8,670 | 1,960 | 22.6% | 16.5% | 42.9% | 15.4 | 13.3 | 3.27 |
| Partner | ILS | 3,150 | 441 | 14.0% | 11.3% | 15.7% | 19.7 | 16.5 | 0.56 |
| Cellcom | ILS | 4,150 | 404 | 9.8% | 7.2% | 22.0% | 9.1 | 16.8 | 0.71 |
| Spacecom (AMOS) | ILS | 242.3 | 79.5 | 32.8% | 13.3% | 47.6% | 1.8 | 6.2 | 1.95 |
| SES (with Intelsat) | EUR | 3,250 | 131 | 4.0% | 1.5% | −9.9% | n/a | 61.5 | 2.63 |
| Eutelsat (OneWeb) | EUR | 1,240 | −65.9 | −5.3% | −1.3% | −14.5% | n/a | n/a | 0.86 |
| Iridium | USD | 903 | 171.6 | 19.0% | 6.4% | 31.7% | 29.2 | 39.7 | 3.78 |
| Viasat (Inmarsat) | USD | 4,630 | 103.1 | 2.2% | 0.1% | 0.2% | n/a | 152.3 | 1.47 |
| Space42 (Thuraya) | AED | 2,240 | −364.6 | −16.3% | −9.0% | −5.8% | n/a | n/a | 0.28 |
| Globalstar | USD | 280.6 | 13.4 | 4.8% | 3.3% | −15.9% | n/a | 812.5 | 1.43 |
| Gilat Satellite Networks (a different company) | USD | 487.8 | 32.0 | 6.6% | 8.2% | 7.0% | 17.5 | 13.1 | 0.02 |
| KVH Industries | USD | 125.0 | −8.8 | −7.0% | −11.4% | −4.4% | n/a | n/a | 0.04 |
| Comtech | USD | 249.6 | −7.0 | −2.8% | −1.5% | −6.6% | n/a | n/a | 0.84 |
| Gogo | USD | 903.3 | 112.3 | 12.4% | −0.6% | −0.8% | n/a | 10.0 | 7.30 |

Gilat's margins by year were −5.3% (2021), −3.5% (2022), 3.9% (2023), 7.1% (2024) and 12.8% (2025)
(gilat_fy2023 p.118; gilat_fy2025 p.127; calc §4).

What the table says:
- **Group medians** (calc §4):
  - Israeli telecom groups 14.0%;
  - satellite operators 4.0%;
  - satcom equipment and service providers 1.9%.
- **The TTM margin is a peak.** Gilat's 14.3% puts it 4th of 15, level with Partner and above every satellite
  service peer. On its 2021–25 median of 3.9% it ranks 10th, with the satellite operators.
- **The capacity layer is earning little.**
  - SES, Eutelsat, Viasat and Space42 all show negative ROE or near-zero ROIC.
  - These are Gilat's suppliers: Intelsat and SES, Inmarsat and Thuraya, OneWeb.
  - Inference: suppliers under return pressure are more likely to raise prices on resellers or sell direct than
    to subsidise them.
- **The listed connectivity resellers lose money.** KVH and Comtech have negative operating margins.
- **Spacecom** shows a 32.8% operating margin but carries debt of 1.95 times equity, and its P/E of 1.8 points to
  one-off income in the TTM (not investigated).
- **Bezeq**, the only infrastructure owner, earns the highest ROIC (16.5%). Gilat's ISP rents Bezeq's network.

### 1.3 What the competitors' and suppliers' record shows

- **Supplier consolidation has narrowed Gilat's options.**
  - SES completed the purchase of Intelsat on 17.7.2025 and targets about €370M of annual synergies [SES-H1].
    Intelsat has been Gilat's key supplier since 2006, with a history of overdue balances (business.md §7).
  - Inmarsat is now Viasat's, and Thuraya is Space42's.
  - Gilat calls the SES–Intelsat merger "a positive development" against LEO competition and says it has good
    working relations with the merged company (gilat_fy2025 p.16). That is management's view. The outside
    record is fewer GEO counterparties, each under return pressure.
- **Israeli defence satcom assets attract foreign strategic buyers, with conditions.**
  - Kratos agreed to buy Orbit Technologies, a TASE-listed maker of satcom terminals, for $356.3M in cash. Closing
    needed clearances for "the acquisition of an Israeli national security company by a foreign buyer" [CT-ORBIT].
  - Completion on 2.3.2026 rests on a search summary only (**UNVERIFIED**).
  - Gilat's licence requires the Minister's consent for any holding of 5% or more and an Israeli acquirer
    (gilat_fy2025 p.72-74; governance_risk.md §1.3). Its takeover optionality is narrower than Orbit's.
- **Defence demand is real and, for now, rising.**
  - Israel's 2026 defence budget was passed at about $44.8B, up about $9.48B, with a supplemental expected for the
    war with Iran (Operation Roaring Lion from 28.2.2026) [BD-0330].
  - The same source puts defence spending at about $17.65B in 2015–16 and roughly flat until 2022. The TTM rests
    on a spending level about 2.5 times the pre-war norm (2.54 times; calc §8).

### 1.4 Second-order effects (E5)

- **Supply response in capacity.** LEO capacity (Starlink, OneWeb, Kuiper) keeps cutting the price per megabit.
  The company itself expects "continued price erosion" (gilat_fy2025 p.50).
  - In Africa, that hits the managed GEO and MEO backhaul Gilat sells to Vodacom.
  - In Israel, it hits VSAT. MSS airtime (Iridium, Inmarsat) is less exposed.
- **Customers' reactions.**
  - Vodacom chose to partner with Starlink rather than only buy from integrators [SIA-VOD].
  - Starlink also sells direct to Israeli households and businesses [GL-STAR].
  - Both moves shorten the chain that Gilat's margin sits in.
- **Competitors' reactions in the ISP.**
  - The CEO says Bezeq signed the voluntary IRU deals partly to show the Ministry that price regulation is
    unnecessary, and to fill its network before Cellcom and HOT fill IBC's at "relatively aggressive" prices
    [BZ-838877].
  - The Ministry then fixed fibre BSA at ILS 58 a month for 2026–2031 and left small ISPs unlimited access
    (gilat_fy2025 p.39-40). That narrows the IRU's cost edge once the cost of money is counted (business.md §1.6).
- **Who else benefits.**
  - **Bezeq:** front-loaded cash, "the majority … over the first years" [BZQ-IRU].
  - **Partner:** an IRU on the same terms.
  - **Vodacom:** it resells Starlink.
  - **Converting bondholders:** they converted at ILS 1.00–1.35 while the share closed between ILS 1.26 and 2.83
    in 2026 (calc §8; market.md §1.4).
  - **Option holders:** the December 2025 grants (governance_risk.md §2).
- **Regulatory second order.**
  - Gilat's unified satellite licence runs to 31.12.2026 (gilat_fy2025 p.69-72); renewal is due within two months.
  - Uganda's regulator lists Gilat Telecom (U) Ltd's NPSP licence as running "1/7/2021 to 30/6/2026" [UCC]. The
    FY2024 report said 30.6.2025 (gilat_fy2024 p.66) and the FY2025 report says 30.6.2030 (gilat_fy2025 p.75).
  - The 2030 date could not be checked against a later regulator list.

---

## 2. Is the moat visible from outside?

| Test | Outside evidence | Reading |
|---|---|---|
| Incumbency with the state | Government Procurement Administration records: Gilat Telecom Ltd (511784498) supplied satellite communications equipment and services to ministries from 2012 to 2017 under an exemption for identical terms (ILS 18.3M). The central tender for satellite communications was extended in 2020–21 (ILS 1.5M a year). Smaller sole-supplier notices date from 2010–2011 [GOV-EXEMPT]; calc §6 | **Yes, in civil government.** The civil tender is small: the 2012–17 contract was ILS 3.66M a year, 1.53% of 2025 revenue (calc §6). The defence buyer behind Customer A (25.4% of 2025 revenue) does not appear in these civil records |
| Renewals by the defence customer | A three-year exclusive framework of up to ILS 40M with "a leading Israeli government customer" (January 2021) [CAL-0118]. A five-year exclusive framework of up to ILS 36.5M (December 2024) renewed one "fully used within 3 years" [BZ-838877]. A 10-month order of about ILS 52M in January 2026 [BZ-20025845] | **Relationship strength, not a contract moat.** The customer "is not obliged to buy" (company statement in [BZ-838877]) |
| Licences | Satellite, Iridium, OneWeb and Starlink-access permits (gilat_fy2025 p.69-72). Spacecom received the OneWeb approval on the same day [BZ-20013709]. An Iridium end-user licence requires an Iridium service-provider agreement ([GOV-IRIDIUM], search summary, **UNVERIFIED**) | **Low barrier.** Licences keep foreigners out and slow entrants, but the incumbent operator and Starlink have the same access |
| Cost position, ISP | Gilat's IRU price per line is within −7% to +2% of Partner's (calc §5). Bezeq ARPU is ILS 138 against Gilat's ILS 80 (business.md §1.6) | **No cost advantage.** It competes on price |
| Returns against peers | TTM margin 4th of 15; five-year median 10th (calc §4) | **Not proven through a cycle** |
| Customer captivity in Africa | Vodacom's Starlink agreement [SIA-VOD]; Starlink licensed in the DRC [CA-DRC] | **Weakening** |

**Verdict.** The outside record shows an incumbent relationship business in Israeli government and defence satcom,
sustained by security-cleared staff and repeated renewals. It shows no structural moat, and the African and
ISP businesses show none. This agrees with business.md §11: narrow at best in defence, none elsewhere.

---

## 3. What confirms, and what contradicts, management's account

**Confirmed from outside:**
- The Bezeq IRU deals and their one-time amounts. Bezeq's report gives about NIS 90M one-time for the 2024 deal
  and about NIS 400M one-time for the addendum, against Gilat's ILS 88.02M and ILS 400M (calc §5) [BZQ-IRU].
- The SES–Intelsat merger completed on 17.7.2025 [SES-H1], as stated in gilat_fy2025 p.16.
- The Accountant General's tender relationship since 2012 [GOV-EXEMPT], as stated in business.md §1.4.
- The OneWeb LEO permit of February 2025 [BZ-20013709], as stated in gilat_fy2025 p.71.
- The Nexttel dispute. Cameroonian press describes a shareholder war in which Viettel's side tried to cancel the
  Gilat contract in 2018 [CAMER]; [ITW-NEXT]. That matches the claim of about EUR 4.8M pursued in Cameroon since
  May 2021 (gilat_fy2025 p.76). It also suggests a low recovery.
- The July 2025 placement: 7.71M shares at 88 agorot, a 3% discount to the 98-agorot market price
  [BZ-20019103]; gilat_fy2025 p.8.
- Headcount growth in tactical satcom and ISP support. On 3.11.2026 Drushim listed two openings through the
  agency Binat Samach: a Tactical SATCOM presales engineer (3–4 years' experience) and 24/7 technical-support
  representatives for private and business internet customers [DRUSHIM]. An earlier posting for ISP sales
  representatives with a ILS 10,000 joining bonus had been removed (HTTP 410). That earlier posting rests on a
  search summary (**UNVERIFIED**).

**Contradicted, or not explained by any filing read:**

| Item | Outside source | Filing position | Status |
|---|---|---|---|
| Size of the Bezeq commitment | Bezeq: about NIS 140M (2024 deal) and "over NIS 600 million" (addendum), including maintenance, interest and linkage, mostly paid in the first years [BZQ-IRU] | One-time amounts only; the unpaid instalments are not liabilities; the commitment is not a risk factor (governance_risk.md §4.5, §10) | **Material.** The all-in figure is about 1.5 times the one-time amount (calc §5). Read Bezeq's Hebrew original on Maya (the copy read is an unofficial translation) |
| The Vodacom renewal | Vodacom–Starlink agreement of 12.11.2025: backhaul plus enterprise resale [SIA-VOD]; [TT-VOD]. Starlink live in the DRC from June 2025 [CA-DRC] | "The company is working to renew the contract for further periods" (gilat_h1_2026 p.15). The FY2025 Africa section discusses Starlink generally and notes that about 75% of Congolese mobile operators use SES's cell-backhaul platform (gilat_fy2025 p.27), with no mention of the Vodacom agreement | **Open and material.** Vodacom revenue was about USD 12.4M in 2025, 19.6% of today's market cap in ILS (calc §7) |
| What "normal" looks like | CEO, March 2025: wartime turnover about double the normal; defence about 50% of turnover in wartime against about 30% in routine [BZ-20014148] | 2025 government segment 63.4% of revenue (business.md §0). No numeric guidance | **Confirms business.md:** the TTM is a wartime figure |
| Starlink's price in Israel | NIS 230 a month and up, aimed at heavy and business users [GL-STAR] | "Starlink sells far below industry norms" (gilat_fy2025 p.50) | Consistent abroad; in Israel Starlink is dearer than fibre, so the ISP is not the exposed line |
| The chairman's biography | Interim CEO of Vesttoo from August 2023 [IJ-0815]; [CT-0815] | FY2023 lists "Vesttoo Ltd (director and manager of the company in liquidation)" (gilat_fy2023 p.195). FY2025's five-year history omits it (gilat_fy2025 p.216) | **Minor candour point.** Reg. 26 asks for five years |
| The 2023 "premium" to the CEO | Bizportal (27.6.2023): the 30 agorot issue price was "the lowest price at which shares can be issued", while the company spoke of a 10% premium [BZ-815902] | gilat_fy2023 p.7, p.183 | Already in governance_risk.md §3. The same price went to all holders in the rights issue |
| Bezeq IRU and the regulator | CEO: Gilat petitioned the High Court against the Ministry over wholesale prices, then withdrew after the Bezeq deal [BZ-838877] | Not in the filings read | **Docket UNVERIFIED** |
| An "Orange contract in Africa" loss | Bizportal (9.10.2024) says investors were scared by the loss of "a significant contract with Orange" [BZ-834978] | The filings name Orange only as an example of African operators (gilat_fy2023 p.43; gilat_fy2024 p.40) | **UNVERIFIED.** Not found in the filings read |
| IPv4 address pool | An opinion piece puts it at about 85,000 IPv4 addresses, at USD 20–28 an address on the market [YNET-1021] | Not disclosed | **UNVERIFIED.** A possible hidden asset of about USD 1.7–2.4M, ILS 5.4–7.5M (calc §8) |

---

## 4. Misconduct, sanctions and convictions of the controller and officers (checklist B7, VETO)

There is no controller. People checked:
- the company, under its old names Satcom Systems and Gilat Satcom;
- Chairman Ami Barlev; CEO Itzik Ben Eliezer; CFO Orit Gal; COO Assaf Rozenhak; VP Government and Defence Ami
  Schneider; CTO Amir Cohen;
- directors Yahel Yaakov Shahar, Bina Rezinovsky-Sanker and Haran Levavot;
- the large holders: Shidurit Telepage (Shalom Dadush), Goldphone, and the former controller Eurocom.

The officer list is from gilat_fy2025 p.216-218.

| Source | Result |
|---|---|
| Companies Registrar (data.gov.il, company list and change file dated 3.11.2026) [ICA] | Gilat Telecom Global (520041674), Gilat Telecom Ltd (511784498), IP Planet Network (512726969), Israsat (511773624) and Shidurit Telepage (511408692) are active and not flagged "violating". **Goldphone Ltd (513709634) is flagged "מפרה" (violating)**, with no annual report filed, care of a Jerusalem lawyer |
| Government Procurement Administration exemption records [GOV-EXEMPT] | Gilat Telecom Ltd appears as an approved supplier. No exclusion was found |
| ISA enforcement; Ministry of Communications fines (עיצום כספי): web searches by company name, old names and officers | No hit. The Ministry's recent fines in the results concern HOT and others |
| Press on the chairman | Legal counsel of B Communications and the whole Eurocom group under Elovitch [CAL-0109]; the dates (2008–2014 or 2016) come from a MarketScreener profile, **UNVERIFIED**. Replaced Elovitch on the Internet Gold and Bezeq boards on 3.4.2018 [WAL-0403]. Led B Communications' debt settlement and was removed as its CEO by Searchlight in January 2020 [CAL-0109]. Interim CEO of Vesttoo after its collateral fraud, in Chapter 11 from August 2023 [IJ-0815]. Vesttoo's estate sued the former executives, Aon and China Construction Bank; no claim naming Barlev was found (search summary, **UNVERIFIED**) |
| Press on the CEO | Former Bezeq VP for technology and network and CEO of Bezeq Online (gilat_fy2025 p.217; [BZ-815902]). Earlier CEO of 018 Xphone and later a bidder for Xphone's mobile business (search summaries, **UNVERIFIED**). Nothing adverse found |
| The former controller | Shaul Elovitch's Eurocom group went into liquidation at Bank Hapoalim's initiative over about ILS 1bn of debt [CAL-0217]. Elovitch faced the Case 4000 proceedings (common knowledge; not re-verified here). **He has had no stake since 17.2.2021** |
| Court databases (Nevo, Takdin, Net HaMishpat) and the class-action register | **Not accessible here.** Web searches for "גילת טלקום" with class-action terms returned other companies (Golan Telecom, Gilat Satellite Networks) |

**B7 reading:** no record of personal misconduct, sanction or conviction in the sources checked. The chairman's
career runs through two collapsed groups, Eurocom and Vesttoo, but in post-crisis roles, and no allegation against
him was found. B7 **passes on the record checked and stays open on the courts**. The principal should run a
court search on the company, the subsidiary and the chairman.

---

## 5. Control chain and pledges (checklist F1, VETO)

| Layer | Fact | Source |
|---|---|---|
| Controller | None since 17.2.2021. Eurocom's liquidators sold 41% in 2–3% lots to institutions through the investment house Epsilon, for about ILS 26M at a ILS 68M valuation. The Ministry required Israeli buyers and no dominant party | gilat_fy2025 p.214; [CAL-0217] |
| Attempted re-concentration | September 2021: an investor group led by Einav Cohen bought about 15–20% in one session from the hedge funds Hatzavim and Denver [BZ-796082]. October 2024: the CEO (to 25%), Shidurit (to 26%) and Goldphone (to 13.4%) obtained Ministry permits. The Ministry presumed Shidurit, then the largest holder, to be the controller | gilat_fy2024 p.199; [BZ-834978] |
| Outcome | The permits lapsed. The CEO and Shidurit may each hold up to 15%. Shidurit sold down to about 3% (calc §3). Goldphone is not an interested party | gilat_fy2025 p.214; [GL-IP] |
| Largest holders now | CEO 9,547,586 (7.93%), held privately. Ayalon mutual funds 7,494,833 (6.22%). Chairman 44,555. Rozenhak 47,619 | [BZ-STAKE]; [GL-IP]; calc §2 |
| Below 5%, not reported | Meitav funds about 5.73M after 5.10.2026 (implied). Pasternak Shoham and Mor (7.71M placement shares in July 2025; current holding unknown). Shidurit (about 3.2M in March 2026, implied). Goldphone (unknown) | calc §3 |
| Stale register entries | Bizportal still lists "Ayalon Investment House" with 3,405,800 shares (17.2.2021), Phoenix nostro 1,112,438 (31.12.2021) and Psagot nostro 980,288 (30.6.2021). They look like 2021 dispersal buyers who fell below reporting thresholds | [BZ-STAKE] |
| Pledges of holders' shares | None disclosed. Reg. 21A lists no shareholder agreement (gilat_fy2024 p.199). The open Pledges Registrar data carries no names | **Cannot assess here** |
| The company's own charges | The operating subsidiary registered charge no. 33 (25.12.2025, removed 26.2.2026) and no. 34 (25.2.2026), and removed no. 32 (9.1.2026). This fits the pledged deposit of about ILS 3.5M behind guarantees (gilat_fy2025 p.158) | [ICA]. Chargee and amount are not in the open file |
| Licence limits | Holding 5% or more needs the Minister's consent and an "Israeli" holder. A lender enforcing on a block of 5% or more would face the same gate | gilat_fy2025 p.72-74 |

**F1 reading:** the chain is mapped. There is no controller, no pyramid and no disclosed pledge. The CEO is the
nearest thing to a control block at 7.9%. He paid cash in 2023 (ILS 1.84M [BZ-815902]) and has bought on the
market since. Whether his shares are pledged is **"cannot assess here"** and stays open. The principal should ask
the company and search the Pledges Registrar by name.

---

## 6. Who has been selling and buying, and why (checklist E3, VETO)

**Trades, 3.11.2024–3.11.2026** (calc §3; percentages as reported after each trade):

| Date | Party | Shares | Price (ILS) | Value | Holding after | Source |
|---|---|---|---|---|---|---|
| 8.7.2025 | Pasternak Shoham (about ILS 5.3M) and Mor (about ILS 1.5M): private placement | +7,710,000 | 0.88 | +6.78M | n/a | gilat_fy2025 p.8; [BZ-20019103] |
| 8.1.2026 | Shidurit Telepage | −1,160,771 | not reported | — | 8.21% | [GL-IP] |
| 3.2.2026 | Shidurit Telepage | −1,995,518 | 1.45 | −2.89M | 5.98% | [GL-IP] |
| 3–4.3.2026 | Shidurit Telepage | −2,677,372 | 1.65 (4.3) | −4.40M | 3.01% | [GL-IP]; calc §8 |
| 4.3.2026 | Ayalon mutual funds | −782,430 | 1.70 | −1.33M | 10.6% | [GL-IP] |
| 9.4, 30.6 and 7.10.2026 | Ayalon mutual funds | −3,849,840 | not reported | — | 6.13% | [GL-IP]; [BZ-FLOW]; calc §8 |
| 12–30.6.2026 | The company (buyback, board approval 11.6.2026) | +2,300,000 | 2.60 incl. fees | 5.99M | treasury | gilat_h1_2026 p.37; calc §3 |
| 1.10.2026 | CEO Itzik Ben Eliezer | +28,893 | 2.07 | +0.06M | 7.81% | [GL-IP] |
| 12 months to 3.11.2026 | CEO (all buys) | +640,966 | 1.886 average | +1.21M | 7.93% now | [BZ-FLOW]; calc §3 |
| 5.10.2026 | Meitav mutual funds | −1,891,278 | 1.96 | −3.71M | 4.69% | [GL-IP] |
| 7–21.10.2026 | The company (ILS 7M programme of 7.10.2026) | +2,274,810 | 2.031 average | 4.62M | treasury | [GL-IP]; calc §3 |
| 2025–2026 | Bondholders converting Series C (at 1.35) and Series D (at 1.00); option exercises | +31,112,917 listed shares in two years (the gross increase of 38,822,917 less the placement) | 1.00–1.35 | — | — | TASE series; calc §3, §8 |

**Reading, by group:**
- **Insiders.** The CEO is the only officer who traded in the period. He bought 640,966 shares in the last year at
  an average of 188.6 agorot and sold none (calc §3). He also holds 4M options from December 2025 (governance_risk.md §2). The
  chairman's 44,555 shares are unchanged since 2021.
  - On Klarman's question, the most informed seller is **not** management.
- **The would-be controller exited.**
  - Shidurit held about 11.9M shares (13.8%) in October 2024 and was cleared to go to 26% (calc §3;
    gilat_fy2024 p.199).
  - It sold about 8.7M shares by 4.3.2026, of which about 2.8M went before January 2026 and are not itemised in
    the feeds read (calc §3).
  - Its priced exit averaged 156.4 agorot. The company later bought back at 1.66 times (June) and 1.30 times
    (October) that price, and today's close is 1.06 times it (calc §3).
  - Why it sold is **UNVERIFIED**. The 26% permit lapsed after six months (gilat_fy2025 p.214), so the window to
    build control had closed. A holder in that position is a plausible profit-taker after the multi-fold rise
    since 2023.
- **Institutions.**
  - At 31.8.2026, 43 mutual funds held 19,704,370 shares, worth ILS 42.6M. Bizportal prints this as 16.36% on
    today's share count; it was 16.16% of the 31.8.2026 count (calc §3). By house: Ayalon 6.46%, Meitav 6.37%,
    Migdal 1.73%, Yelin Lapidot 1.60%, Kesem 0.09% [BZ-STAKE]. The snapshot's implied price equals the 31.8.2026
    close of 216.4 agorot, which dates it (calc §3).
  - In the 365 days to 3.11.2026, Ayalon sold 4.63M and bought 0.58M, and Meitav bought 7.63M and sold 1.89M
    [BZ-FLOW]. Both trimmed into the October fall.
  - Six Ayalon funds hold 2,428,004 par of Series D, 9.22% of it [BZ-BONDD].
  - The October fund holdings, due around mid-November, will show whether the funds sold after 5.10.
- **Supply from conversions.** TASE's listed count rose from 86,069,060 (3.11.2024) to 120,417,631 (net
  +34.3M). Daily increases sum to 38.8M, of which 7.71M was the July 2025 placement; buybacks took 4.5M out
  (calc §3, §8). About 26.3M Series D shares remain
  convertible at ILS 1.00 until 1.4.2028 (market.md §1.4).
  - Converters selling into the market are the largest and steadiest source of supply. Their reason is
    arbitrage, not information.
- **The October–November fall** from 200.3 to 165.3 coincided with the 27.10.2026 election and a market-wide
  sell-off (market.md §1.1; on Globes, "the stock exchange in panic", 28.10.2026). No company news was found.
- **Volume.** In two years 315.4M shares changed hands on exchange, 2.62 times today's listed shares; 1.85 times
  in the last year (calc §3). The price went from 69.5 agorot (3.11.2024) to a peak of 282.8 (12.6.2026) and
  165.3 now, 2.38 times over two years and 41.5% below the peak (calc §3).

**E3 reading (facts for the synthesis).**
- What explains a P/E of 6.0 on TTM earnings (market.md §1.3) is largely known and observable:
  - wartime defence revenue, by the CEO's own description [BZ-20014148];
  - a Vodacom renewal now facing Starlink [SIA-VOD];
  - an all-in Bezeq commitment of more than NIS 740M, 3.72 times the market cap (calc §5);
  - a convertible overhang (market.md §1.4);
  - a customer concentration the company does not name.
- Under the Petco rule, a thesis must show why these facts are wrong or temporary. The outside record supplies
  no such evidence. The insider evidence (CEO buying, company buybacks) is positive but small, and the buybacks
  were done at higher prices.

---

## 7. Liquidity, maintenance list and index membership (checklist F6, FLAG)

**Data.**
- Daily on-exchange proceeds in ILS come from Bizportal's history call, which ends 2.11.2026. The 3.11.2026
  session (ILS 1,727,998) comes from the general view [BZ-GV].
- **Cross-check against the TASE series** embedded in the company's IR page (to 29.10.2026; market workstream
  copy) (calc §1):
  - the two series agree on 1,226 sessions, with a largest difference of ILS 999, from TASE's rounding to
    thousands;
  - Bizportal has three dates the TASE copy lacks: 16.2.2024, and 30.10 and 2.11.2026, which fall after the copy
    was taken;
  - the TASE copy has two dates before Bizportal's series starts;
  - no session in the last 250 had zero turnover.
- lib/liquidity.py is not available. Percentiles use linear interpolation, with the nearest rank printed as a
  check; the cap uses `charter_valuation.position_size` (calc §1).

| Window | Median (ILS) | 25th pct (ILS) | Mean (ILS) | Sessions < 50k | Sessions < 100k | Liquidity cap 20×20%×p25 (ILS) |
|---|---|---|---|---|---|---|
| **60 sessions to 3.11.2026** | **1,325,803** | **1,001,604** | 1,772,960 | 0 | 0 | **4,006,416** |
| 20 sessions to 3.11.2026 | 1,675,131 | 1,182,498 | 1,940,857 | 0 | 0 | 4,729,990 |
| 120 sessions to 3.11.2026 | 1,473,484 | 1,080,351 | 2,227,505 | 0 | 0 | 4,321,403 |
| 250 sessions to 3.11.2026 | 1,227,188 | 631,441 | 1,763,967 | 2 | 10 | 2,525,764 |
| 60 sessions to 23.10.2026 (before the election-week fall) | 1,319,604 | 975,424 | — | — | — | — |
| 60 sessions to 3.11.2025 (a year earlier) | 211,291 | 113,160 | — | 4 | 12 | — |

- **Published cross-check.** Bizportal's published 90-day average on 3.11.2026 is ILS 1,773,721; the 60-session
  mean here is ILS 1,772,960 (calc §1).
- **ILS 50,000 floor: PASSES**, with the median at 26.5 times the floor.
- **ILS 100,000 price-reliability line: PASSES**, at 13.3 times. The price-reliability block is not mandatory.
- **Position building.**
  - At 20% of the 60-session median, ILS 1M takes 3.8 sessions, ILS 2M 7.5 and ILS 5M 18.9 (calc §1).
  - Mean daily turnover is 0.89% of the market cap.
  - The charter cap is ILS 4.0M (USD 1.27M at 3.157), 2.01% of the market cap.
- **How durable is it?** In the 60 sessions to 3.11.2025 the median was ILS 211,291 and four sessions traded under
  ILS 50,000. The liquidity rose with the 2026 re-rating and the conversions. If the price and the conversion
  flow fade, turnover could fall back toward 2025 levels, which still clear the floor on the median but not on
  every day.
- **Maintenance list: NOT on it.**
  - TASE's rules, per its notice of 11.7.2024 [TASE-MAINT]: a company is non-compliant if the public's holdings
    are worth less than NIS 5M, or if the public holds under 5%, or under 15% while worth less than NIS 15M.
    Market-maker exemptions apply at NIS 4M and 12.5%.
  - Gilat's public holds 85.77% excluding every reported interested party, or 91.99% if the institutional holder
    counts as public. That is worth ILS 170.7M or 183.1M: 34.1 or 36.6 times the NIS 5M floor (calc §2).
  - These are the 2024 thresholds; the current ones are **UNVERIFIED**.
- **Index membership** (Bizportal, 3.11.2026): TA Tel-Tech 2.46%, TA Growth 1.82%, TA All-Share 0.27%, Trade &
  Services 0.15%, Yeter 0.09%, Yeter and convertibles 0.09%, General 0.01%, General and convertibles 0.01%
  [BZ-GV]. Index membership is consistent with continuous trading.
- **Short interest:** 1.18% of public holdings on 23.10.2026, 1.6 days to cover (deeptase, via market.md §2.1).
  The Globes short-selling tab carried only 2024 data.
- **Other F6 items:**
  - Not a TA-35 heavyweight and not dual-listed. Do not confuse it with Gilat Satellite Networks (Nasdaq and TASE:
    GILT), a different company with a similar name.
  - The Israeli window is at most six years: `cycle_window_short` applies.
  - The TASE 30% cap is the principal's to check; holdings and NAV are not available here.

---

## 8. Li Lu's four categories, for the outside record (checklist E9, FLAG)

| Category | Items |
|---|---|
| **What we know** | No controller since 2021 and how control was dispersed (§5); who sold and who bought for two years (§6); liquidity and maintenance status (§7); peer margins and the gap between Gilat's TTM and five-year margins (§1.2); Bezeq's all-in IRU figures (§3); Vodacom's Starlink agreement and Starlink's DRC licence (§1.1, §3); supplier consolidation (§1.3); incumbency in the civil government tender (§2) |
| **What we do not know** | Whether Vodacom will renew after 31.3.2027, and on what terms; who Customer A is (a defence body is likely but **UNVERIFIED**); Shidurit's and Goldphone's current holdings and motives; whether the CEO's shares are pledged; the chargee of the subsidiary's 2026 charge; the outcome of the satellite licence renewal due 31.12.2026; any court cases |
| **What we do not need to know** | Global satellite market size; Starlink's subscriber numbers in Israel (it is dearer than fibre); Gilat Satellite Networks' affairs (a different company) |
| **What could be unknown to us** | Terms of the Intelsat/SES purchase commitments (undisclosed amount, gilat_fy2025 p.160); post-war defence ordering; anything in Maya immediate reports, which were not readable; any change in the Ministry's wholesale regime after 2028–2031 |

---

## 9. Checklist status from this workstream

| Item | Status | Basis |
|---|---|---|
| **B7** (VETO) no misconduct record | **PASS on the record checked; OPEN on the courts** | §4. The chairman's links to Eurocom and Vesttoo are noted, with no allegation found against him |
| **E3** (VETO) mispricing and who is selling | **Facts supplied. The visible discount is explained by known facts** | §6. Sellers: the would-be controller, funds, converters. Buyers: the CEO and the company. The verdict belongs to the synthesis |
| **E5** (FLAG) second-order effects | **Done** | §1.3–1.4 |
| **E9** (FLAG) four categories and outside scuttlebutt | **Done for the outside record** | §8. Covers competitors, customers (Vodacom), suppliers (Bezeq, SES), regulators (Ministry, UCC, procurement), registry, jobs and press. Courts and Maya are the gap |
| **F1** (VETO) control chain and pledges | **Chain mapped; pledge "cannot assess here" (open)** | §5 |
| **F6** (FLAG) maintenance list, liquidity, window, TASE cap | **Liquidity and maintenance PASS**; `cycle_window_short` applies; TASE cap not assessable here | §7 |

---

## 10. Open items for the principal (Maya and registries)

1. **Bezeq's Hebrew report of 4.11.2025** (and that of 15.12.2024), to confirm the all-in consideration and the
   payment schedule behind "the majority … paid over the first years". The copy read was an unofficial
   translation.
2. **Vodacom.** Ask management directly about the Starlink agreement's effect on the DRC contract and the renewal
   timetable. Read Vodacom Group's FY2026 annual report (year to 31.3.2026) for DRC capex and backhaul plans.
3. **Ministry of Communications.** Check the renewal of the unified satellite licence (expires 31.12.2026) and the
   Uganda licence (UCC lists 30.6.2026; the company says 30.6.2030).
4. **Court search and class-action register** for Gilat Telecom Global (520041674), Gilat Telecom Ltd (511784498)
   and the chairman. Also the High Court petition on wholesale prices that the CEO described.
5. **Pledges Registrar by name** for Itzik Ben Eliezer; the registrar extract for charge no. 34 of 511784498.
6. **Maya interested-party reports, 2024–2026**, for Shidurit's 2025 sales (about 2.8M shares not itemised), for
   Goldphone and its owners, and for Pasternak Shoham's current holding.
7. **October 2026 fund holdings** (Ayalon, Meitav, Migdal, Yelin Lapidot), due around mid-November.
8. **The Q3 2026 report**, expected late November 2026 (market.md §3).

---

## Sources

All read on 3.11.2026, Israel time (UTC+2), unless stated. Raw copies are saved under `scuttle/raw/` (see Files).

| Key | What was used | URL | Read |
|---|---|---|---|
| [BZ-RT] | Daily close, volume and on-exchange proceeds (ILS), 2.11.2021–2.11.2026 | https://www.bizportal.co.il/ajax/biz_papers_helper.ashx?action=get_paper_yearly_graph&request_type=1&paper_id=1080597&period=6 (the quote page's own history call, with the cookie from a plain visit to the quote page) | 21:53 |
| [BZ-GV] | 3.11.2026: close 165.3, daily proceeds 1,727,998, 90-day average 1,773,721, 120,417,631 listed shares, index weights | https://www.bizportal.co.il/capitalmarket/quote/generalview/1080597 | 21:53 |
| [TASE-H] | TASE daily series embedded in the company's IR page (used to cross-check and for listed share counts) | https://satcom-gilat.co.il/גרף-מניה/ (market workstream copy `web/history_data.json`, as of 30.10.2026 17:34) | 17:49 (market workstream) |
| [BZ-STAKE] | Interested-party register; fund snapshot (31.8.2026) by manager | https://www.bizportal.co.il/capitalmarket/quote/stakeholders/1080597 | 21:57 |
| [BZ-FLOW] | 365-day interested-party flows (CEO +640,966 / ILS 1,209K; Ayalon; Meitav) | https://www.bizportal.co.il/ajax/biz_papers_helper.ashx?action=get_holding_flow_summary_data_json&paperId=1080597&period=y | 21:57 |
| [BZ-BONDD] | Series D: 6 Ayalon funds hold 2,428,004 par | https://www.bizportal.co.il/bonds/quote/stakeholders/1218205 | 22:09 |
| [GL-IP] | Globes interested parties: holdings (CEO 7.93%, chairman 0.04%, public 92.03%) and the ten latest buyers and sellers; the page's news list ("הבורסה בפאניקה", 28.10.2026) | https://www.globes.co.il/portal/instrument.aspx?instrumentid=949&mode=company | 21:56 |
| [BZ-NEWS] | Bizportal headline list for the share, 2022–2026 | https://www.bizportal.co.il/ajax/biz_papers_helper.ashx?action=get_paper_news_page&paper_id=1080597&page_number=1 (pages 1–5) | 22:11 |
| [BZ-815902] | "מנכ"ל גילת טלקום קונה 9.5% ממניות החברה במחיר המינימום האפשרי בשוק", Itzik Yitzhaki, 27.6.2023 | https://www.bizportal.co.il/capitalmarket/news/article/815902 | 22:12 |
| [BZ-834978] | Ministry permits for the CEO, Shidurit and Goldphone; "lost a significant contract with Orange", 9.10.2024 | https://www.bizportal.co.il/capitalmarket/news/article/834978 | 22:12 |
| [BZ-838877] | Defence framework of up to ILS 36.5M; CEO interview (High Court petition, Bezeq's motives), 29.12.2024 | https://www.bizportal.co.il/capitalmarket/news/article/838877 | 22:12 |
| [BZ-20013709] | Gilat and Spacecom receive OneWeb LEO approvals, 19.2.2025 | https://www.bizportal.co.il/capitalmarket/news/article/20013709 | 22:12 |
| [BZ-20014148] | CEO and Ami Schneider interview: wartime turnover about double; defence about 30% of turnover in routine, 4.3.2025 | https://www.bizportal.co.il/capitalmarket/news/article/20014148 | 22:12 |
| [BZ-20019103] | Placement: 7.7M shares at 88 agorot to Pasternak Shoham and Mor, 8.7.2025 | https://www.bizportal.co.il/capitalmarket/news/article/20019103 | 22:12 |
| [BZ-20025845] | ILS 52M, 10-month order from an Israeli customer, 5.1.2026 | https://www.bizportal.co.il/capitalmarket/news/article/20025845 | 22:12 |
| [BZ-20039673] | Q2 2026 results; ARPU eroded year on year, 20.8.2026 | https://www.bizportal.co.il/capitalmarket/news/article/20039673 | 22:12 |
| [BZ-796082] | "מאבק שליטה בסאטקום?", Itay Pat-Yah, 9.9.2021: Eurocom history; Einav Cohen group | https://www.bizportal.co.il/capitalmarket/news/article/796082 | 22:00 |
| [CAL-0217] | Eurocom liquidators disperse the 41% control block, 17.2.2021 | https://www.calcalist.co.il/articles/0,7340,L-3894358,00.html | 22:16 |
| [CAL-0118] | ILS 40M government framework; Rozenhak named CEO, 18.1.2021 | https://www.calcalist.co.il/articles/0,7340,L-3888431,00.html | 22:00 |
| [CAL-0109] | "בר-לב הודח - סרצ'לייט ממנה את תומר ראב"ד למנכ"ל בי-קום", 9.1.2020 | https://www.calcalist.co.il/articles/0,7340,L-3777427,00.html | 22:02 |
| [WAL-0403] | Ami Bar-Lev, Eurocom's legal counsel, replaces Elovitch at Internet Gold and Bezeq, 3.4.2018 | https://finance.walla.co.il/item/3147514 | 22:02 |
| [IJ-0815] | "Fintech Vesttoo Seeks Chapter 11 Bankruptcy Protection": "interim CEO Ami Barlev", 15.8.2023 | https://www.insurancejournal.com/news/international/2023/08/15/735355.htm | 22:03 |
| [CT-0815] | Ctech, "Vesttoo seeks Chapter 11 bankruptcy protection", 15.8.2023; also https://www.calcalistech.com/ctechnews/article/rj2htx92h (16.8.2023) | https://www.calcalistech.com/ctechnews/article/bys4stohn | 22:03 |
| [BZQ-IRU] | Bezeq immediate report, 4.11.2025: addendum with Gilat, 90,000 lines, consideration "over NIS 600 million" (unofficial English translation) | https://cdn.financialreports.eu/financialreports/media/filings/6676/2025/RNS/6676_rns_2025-11-04_e1aa6820-2af2-43ba-8ca3-38e73d48d81b.pdf | 21:59 |
| [GL-PTNR] | "Partner signs NIS 1b Bezeq fiber optic deal", 22.12.2022 | https://en.globes.co.il/en/article-1001433549 | 22:16 |
| [SES-H1] | SES H1 2025 results; Intelsat acquisition completed 17.7.2025; synergies | https://www.ses.com/press-release/ses-delivers-solid-h1-2025-results-completes-intelsat-acquisition | 22:05 |
| [GL-STAR] | "Elon Musk's Starlink launches Israel Internet services", 8.8.2025 | https://en.globes.co.il/en/article-elon-musks-starlink-launches-israel-internet-services-1001518509 | 22:05 |
| [SIA-VOD] | "Vodacom Group and Starlink Partners to Transform Connectivity Across Africa", 12.11.2025 | https://spaceinafrica.com/2025/11/12/vodacom-group-and-starlink-partners-to-transform-connectivity-across-africa/ | 22:05 |
| [CA-VOD] | Connecting Africa, "ATF 2025: Vodacom, Starlink partner to connect Africa", 13.11.2025 | https://www.connectingafrica.com/partnerships/atf-2025-vodacom-starlink-partner-to-connect-africa | 22:05 |
| [TT-VOD] | Total Telecom, "Vodacom taps Starlink for mobile backhaul across Africa", 12.11.2025 | https://totaltele.com/vodacom-taps-starlink-for-mobile-backhaul-across-africa/ | 22:05 |
| [CA-DRC] | "Starlink live in DRC", 4.6.2025 | https://www.connectingafrica.com/connectivity/starlink-live-in-drc | 22:07 |
| [DT-AIRTEL] | "Airtel Africa, Vodacom to share infrastructure in African markets", 12.8.2025 | https://developingtelecoms.com/telecom-business/operator-news/18907-airtel-africa-vodacom-to-share-infrastructure-in-african-markets.html | 22:07 |
| [ITW-NEXT] | "Nexttel leverages Gilat to deploy 4G in Cameroon" (CEO Dan Zajicek quoted), 31.8.2018 | https://itweb.africa/article/nexttel-leverages-gilat-to-deploy-4g-in-cameroon/P3gQ2MGxjmrqnRD1 | 22:09 |
| [CAMER] | "Affaire Nexttel : Baba Danpullo de retour sur la table des négociations", 22.10.2019 | https://www.camer.be/77331/12:1/cameroun-affaire-nexttel-baba-danpullo-de-retour-sur-la-table-des-negociations-cameroon.html | 22:09 |
| [UCC] | Uganda Communications Commission, licensed operators as at 30.12.2024 (row 27, Gilat Telecom (U) Ltd) | https://ucc.co.ug/wp-content/uploads/2025/02/LICENSED-TELECOM-OPERATORS-AS-AT-30TH-DECEMBER-2024.pdf | 22:14 |
| [ICA] | Companies Registrar: company list (resource f004176c-…) and change file (28780ab5-…, one year back, dated 3.11.2026) | https://data.gov.il/api/3/action/datastore_search?resource_id=f004176c-b85f-4542-8901-7b3176f9a054&q=גילת טלקום ; …&q=שידורית ; …&q=גולדפון ; https://data.gov.il/api/3/action/datastore_search?resource_id=28780ab5-3ef1-44c7-8377-da82c0aa6781&q=511784498 | 21:55–21:56 |
| [GOV-EXEMPT] | Government Procurement Administration, "דוח התקשרויות בפטור והליכים תחרותיים" (resource 65c8fced-…) | https://data.gov.il/api/3/action/datastore_search?resource_id=65c8fced-c50c-400e-94fb-ef1a208c43e5&q=גילת טלקום | 22:07–22:08 |
| [TASE-MAINT] | TASE notice to members, "Non-Compliance with the Maintenance Rules Based on Data as of June 30, 2024", 11.7.2024 (republished by a listed issuer) | https://cdn.financialreports.eu/financialreports/media/filings/6813/2024/RNS/6813_rns_2024-07-11_b3e0303e-65be-41da-bc5e-a6403413d89a.pdf | 22:10 |
| [SA] | StockAnalysis TTM statistics: GLTL, SCC, BEZQ, PTNR, CEL (tlv); GILT, KVHI, IRDM, VSAT, GSAT, CMTL, GOGO (US); SESG, ETL (epa); SPACE42 (adx) | https://stockanalysis.com/quote/tlv/SCC/statistics/ (same path per ticker; US: https://stockanalysis.com/stocks/irdm/statistics/ etc.) | 22:03–22:04 |
| [CT-ORBIT] | "U.S. defense firm Kratos to acquire Israel's Orbit in $356 million deal", 5.11.2025 | https://www.calcalistech.com/ctechnews/article/byzgiud1zg | 22:22 |
| [BD-0330] | "Israel approves $45B defense budget as Iran war rages", 30.3.2026 | https://breakingdefense.com/2026/03/israel-approves-45b-defense-budget-as-iran-war-rages/ | 22:19 |
| [DRUSHIM] | Drushim search "גילת טלקום": 2 openings (Tactical SATCOM presales; 24/7 technical support), via Binat Samach | https://www.drushim.co.il/jobs/search/גילת%20טלקום/ | 22:11 |
| [YNET-1021] | Ynet Capital opinion piece, "ניתוח טכני: האם האסטרטגייה החדשה של גילת טלקום תוכיח את עצמה", 21.10.2025 (IPv4 pool, CEO's ISP target) | https://www.ynet.co.il/capital/article/bygon24ree | 22:13 |
| [SATTODAY-2013] | Gilat Satcom and AST chosen to provide MSS services to the Israeli government, 11.11.2013 | https://www.satellitetoday.com/government-military/2013/11/11/gilat-satcom-and-ast-chosen-to-provide-mss-services-to-the-israeli-government/ | search summary only (UNVERIFIED) |
| [GOV-IRIDIUM] | gov.il service page: Iridium end-user licence requires an Iridium service-provider agreement | https://www.gov.il/en/service/satellites-iridium-operators | search summary only (UNVERIFIED) |

Read but not used for figures:
- The Globes short-selling tab (data to 2024 only).
- The Globes financial-reports tab.
- Walla 1031058 (an undated item on Gilat Satcom under Zvika Barinboim's WorldGroup, about 2007).
- The Funder article 120487 (HTTP 403).

Search-engine summaries used only as leads, and marked UNVERIFIED where repeated:
- MarketScreener's dates for the chairman's Eurocom role.
- The Vesttoo litigation defendants.
- The Kratos–Orbit completion date.
- Gilat Satcom's 2013 MSS award with AST.
- The earlier Drushim sales posting.

---

## Files

All paths are absolute under the scratchpad work folder:
`/tmp/claude-0/-home-user-value-investing-fund---selected-company-reaserch/8e9bb9a6-b39f-5c24-a635-b21606f1c8ae/scratchpad/work/gilat_telecom/`

- `scuttle_calc.py` and `scuttle_calc_output.txt`: every derived figure.
- `scuttle/raw/`: raw copies of the pages and data used:
  - Bizportal series, register, flows and articles (`biz_*`);
  - Globes pages (`globes_*`);
  - registrar and procurement JSON (`ica_*`, `gov_*`);
  - Bezeq, TASE and UCC PDFs with their text;
  - press pages.
- `scuttle/raw/sa/`: StockAnalysis pages and `sa_stats.json`.
- `scuttle/tools/`: `parse_biz_rt1.py`, `parse_sa_stats.py`, `article_text.py`.
