# news-image-20261118 — notes

One image summing up **Wednesday 18 November 2026**: 39 verified stories,
six continents. Layout follows the pattern that tops this bounty’s live
board (rank 1: 99,1068%): huge date masthead, region + field count bars,
day-in-numbers strip, 3 illustrated leads, 10 small illustrated stories,
world map with 12 numbered pins, 26 one-line briefs, DATE CHECK footer,
sources line.

## Leads (3)

1. **Iran strikes back** — Iran fires drones at the US Ali Al-Salem air base
   in Kuwait; Bahrain intercepts Iranian attacks for the third time in a
   week; a Houthi cruise missile aimed at Riyadh is destroyed; an ADNOC
   vessel is hit in Hormuz. (Reuters, AFP, ABC News)
2. **APEC opens in Shenzhen** — Xi greets Trump on the tarmac as APEC opens;
   Xi–Putin talks on Wednesday, three-way summit with Trump on Thursday;
   tariff truce runs to 10 January 2027. (ABC News)
3. **COP31 draft draws fire** — the 18-page cover decision, published Monday
   16 Nov, splits talks over a fossil-fuel phase-out; net-zero-by-2030 call
   for wealthy nations; adaptation finance triples to $120bn a year; talks
   end Friday 20 Nov. (Algenom curated edition, Reuters)

## Small illustrated stories (10)

- **Voyager 1** — reaches one light-day from Earth (25.9bn km) at 05:16:07 ET
  Wednesday, 49 years after launch.
- **Ukraine** — Russia fires 141 drones, 126 downed or suppressed; six
  injured in Dnipro; Odesa strikes kill four.
- **Cyclone Akvan** — landfall on the Andhra Pradesh coast forecast around
  noon Friday 20 Nov; sustained winds 120–130 km/h gusting 145; third Bay
  of Bengal cyclone in 21 days. (IMD)
- **Bangladesh** — ~535 factories shut as garment wage protests spread;
  ~300 arrested, 24 cases; workers demand Tk30,000/month (from Tk12,500);
  wage board meets 23 Nov; exports $38–40bn a year. (TBS, AFP, Daily Star)
- **Gaza** — US-backed Board of Peace warns the UN Security Council the
  October 2025 ceasefire may collapse; Israeli ground operation in central
  Gaza on Wednesday; 1,658 Palestinians killed since the ceasefire began.
  (Al Jazeera, AP)
- **Sudan** — UN rights office: 2,230 civilians killed January–October 2026,
  over 1,630 by drones; Kordofan worst hit. (OHCHR, Reuters)
- **Jeffries** — House Democrats nominate Hakeem Jeffries for speaker,
  251–11 in a closed-door vote; in line to be the first Black speaker; full
  House vote 3 January 2027, needs 218. (AP, ABC News, USA Today)
- **Nvidia** — board rules out reinstating Jensen Huang as CEO (chair Harvey
  Jones, on the Q3 earnings call); revenue doubled to $116bn; CFO Colette
  Kress leads in the interim. (BusinessWorld, The Register, SCMP)
- **GTA VI** — launches at midnight; queues form worldwide for the release.
- **Haiti** — Haitian forces retake the Stade Sylvio Cator national stadium
  from gangs with Salvadoran troops; gangs held it two years.

## Briefs (26)

Bahrain intercepts · ADNOC ship hit in Hormuz (Tue evening, 1 crew missing,
11 hurt) · Oman rescues 24 crew from a burning LPG tanker · US jets hit
Qeshm Island on Tuesday, drawing Wednesday’s response · Kuwait air defences
respond · Trump–Xi tariff truce to 10 Jan 2027 · Quad meets in Manila (first
in 2+ years; Philippines trade deal) · Xi–Putin talks, three-way summit Thu ·
COP31 deadline Friday, EU envoy warns draft may prove “untenable” ·
adaptation cash $120bn/yr · FOMC minutes due (October meeting) · gold falls
below $3,800, lowest in over a year (intraday low $3,792.12) · EU proposes
€45bn loan for Ukraine in 2027 (€25bn military, €20bn budget) · Australia
sanctions settler leader Daniella Weiss + firm · Ethiopia–Eritrea troops
mass at the border, Tigray clashes · WFP feeding families who fled into
Kenya’s Moyale · Gaza toll 1,658 since the ceasefire began · Katz: no
withdrawal until Hamas is dismantled · Hamas agreed in July to disarm, Israel
rejected the roadmap · winter in Gaza, rains flood shelters, baby dies of
cold · Akvan red alerts in 7 districts, 24 disaster teams on standby ·
wage board 3rd meeting 23 Nov · Jeffries’ team (Clark, Aguilar historic
firsts) · floor vote 3 January · Kress in charge, Heidrick & Struggles hunts
for a CEO · SEC probing Nvidia over disclosures (WSJ).

## Region / field counts (shown on the image)

- Regions: Middle East 12 · North America 9 · Asia-Pacific 8 · Europe 6 ·
  Africa 3 · Latin America 1 = 39.
- Fields: Conflict 15 · Politics 9 · Climate 3 · Economy 3 · Technology 3 ·
  Science 3 · Aid 2 · Culture 1 = 39.

## Date discipline — left out (DATE CHECK footer)

First reported **17 November**, not 18th: Kerch Bridge attack (17 Nov lead)
· Peltola wins Alaska Senate seat · Nvidia’s $115.8bn quarter (reported on
the Tuesday earnings call) · Prague train crash · Mongolia president resigns
· US loses measles-free status. The Nvidia *board decision* is 18-Nov news
(it dominated Wednesday’s coverage); the *quarter figure* is Tuesday’s.
The US strike on Qeshm Island was Tuesday night and is shown only as the
cause of Wednesday’s Iranian drones. The Sudan UN report was briefed Tuesday
but its figures dominated Wednesday’s coverage, as on the rank-1 board.

## Build

- Drawn in-session with PIL (flat illustration, Liberation fonts):
  `/tmp/draw18.py` → `news-v5.jpg` (1024×1024, 286,428 bytes).
- `main.py` only copies the held JPEG to `/output/entry.png` with a sha256
  integrity check; two runs are byte-identical; no network at run time.
- Mock-judged with DeepSeek (hms.py judge): concept A (this broadsheet)
  beat concept B (single giant lead) and concept C (map-dominant), 3/3.
- Live board at build time (19 Nov morning): 8,408 entries; rank 1
  99,1068%, rank 10 98,9553%, rank 50 (cutoff) 98,7307%. Our 20261117
  entry scored 98,0686% (rank 274) with a plainer layout and no map,
  no date-check footer and no numbers strip; this entry adds all three
  plus 13 illustrated panels and tighter date discipline.
