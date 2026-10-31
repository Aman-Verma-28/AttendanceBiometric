# Narration script: settlement reconciliation (pgAdmin 4 + Google Sheets, about 25 minutes)

One simple flow, the same shape as the payments task:
- **pgAdmin 4:** look at the two tables, measure the gap, build the breaks table with one query, check it, and
  export it as a CSV.
- **Google Sheets:** import the CSV, build one pivot, add one check column, write a summary and download the file.

Every number in **bold** is what the screen shows with the loaded data; I tested it on 2026-10-31.

---

## How to use this script

- **Rehearse with it; don't read it on camera.** Learn the flow and the *why* lines, then say them in your own words.
  Only the intro sentence must be word for word.
- **Keep it off the screen.** Use your phone, an iPad or a printout. The numbers card at the end fits on one phone
  screen.
- `ACTION` = what your hands do. `SAY` = what you say while doing it. If the screen shows something different from
  the script, say what you see.
- **Every click: What + Where.** Name the control, say where it is on screen, and say where the cursor moves.
  Never say a bare "this" or "here".
- **Pattern for every click:** "I'll move the cursor [direction] to [named control], the [shape or colour] in the
  [screen area], and click it [to do what]."

## The five rules that sent the payments takes back

1. **The mouse is never still for more than about 20 seconds**, except in the epilogue. Use the type-and-point loop
   for every query:
   1. Type **one line**.
   2. Put your hand on the mouse, **point at that line** and say what it does.
   3. Click at the **end of the line** to put the caret back.
   4. Press Return and type the next line.
2. **While you explain a result, trace it with the cursor.** Point at each row or number as you say it, and pause about
   one second after each click. Don't circle the cursor aimlessly.
3. **Say every shortcut out loud** as you press it, for example "Command S to save".
4. **Use the exact file names from the Goal.** When pgAdmin offers `data-….csv`, select the whole name and replace it
   with `settlement_breaks.csv`. Name the Google Sheet `settlement_reconciliation`.
5. **Download the .xlsx on camera and click the download arrow before the epilogue.** The recording isn't finished
   until the download list shows the file.

---

## Screen map (check it once on the real screen)

**macOS**
- **Dock** on the right edge. **Chrome** is the red, yellow and green circle. **pgAdmin 4** is the blue elephant just
  below it. **TaskRecorder** is just below pgAdmin.
- **Window buttons:** the three circles at each window's top-left are red Close, **yellow Minimize** and green Zoom.

**pgAdmin 4**
- **Object Explorer:** the tree down the left side.
- **Query Tool toolbar:** the row of icons above the editor. From left to right:
  - Open File (folder).
  - **Save File** (floppy disk), with a **small down arrow** beside it that holds **Save As**.
  - Edit.
  - Filter.
  - The "No limit" box.
  - Stop (grey square).
  - **Execute** (white **play triangle**).
- **Editor:** the middle area, with line numbers down its left edge.
- **Results panel:** the lower half, with the **Data Output** and **Messages** tabs at its top-left.
- **Status bar:** the bottom edge, with **Total rows** at the bottom-left.
- **Save results to file:** the **down-arrow icon**, sixth from the left in the small toolbar right above the
  result grid, just left of the zig-zag graph icon.

**Chrome / Google Sheets**
- **Tabs** across the top: **Goal Document**, then **settlement_reconciliation**.
- **Menus:** File, Edit, View, Insert and the rest, at the top-left under the sheet title.
- **Sheet tabs:** at the bottom-left.
- **Pivot table editor:** a panel that opens on the right side.
- **Download arrow:** in Chrome's toolbar at the top-right, after a download.

## Timing

| Section | Target | Clock at end (about) |
|---|---|---|
| Intro | 0:20 | 0:20 |
| 1. The two tables and a clean settlement line | 4:30 | 4:50 |
| 2. The gap per currency | 3:00 | 7:50 |
| 3. The breaks table (one query) | 6:00 | 13:50 |
| 4. Check, walk through the breaks, export | 3:30 | 17:20 |
| 5. Sheets: import, pivot, tie-out | 4:30 | 21:50 |
| 6. Summary, download, stop check | 1:30 | 23:20 |
| Epilogue | 3:15 | 26:35 |

Anything from 20 to 28 minutes is fine; the allowed range is 15:00 to 50:59.

---

## Before you record (not recorded)

### A. One-time setup in the Recorder account
1. **pgAdmin:** right-click the server in the tree → **Properties** → **Advanced** tab → **DB restriction**. Remove
   `payments`, add `settlement`, then **Save**. Right-click the server → **Refresh**. The tree should show only
   **settlement**, and under **Tables** only `ledger_captures` and `settlement_lines`.
2. **Goal Document** (in Chrome, signed in with the @mercor.expert account): replace the text with the new Goal, word
   for word from Studio.
3. **Google Sheets:** create a blank spreadsheet and title it `settlement_reconciliation`. Leave it empty.
4. **One UI change** from the payments recordings, for example a new wallpaper.

### B. Practice once (not recorded)
Run Steps 1 to 6 once, without the epilogue, timing it with the menu-bar clock. Then:
- **Tell me.** I'll run `DROP TABLE settlement_breaks;` so the database is clean again.
- **Delete** the practice `reconciliation.sql`, `settlement_breaks.csv` and `settlement_reconciliation.xlsx` from
  Downloads.
- **Clear the practice spreadsheet:** delete it, create a new blank one titled `settlement_reconciliation`, and empty
  Drive's trash.

### C. Pre-flight (the 10 minutes before Start)
Main account: Studio, Slack, the guidelines, Metadata.rtf and this file are closed. Switch to the Recorder account.
- [ ] Mac on power, quiet room, **Do Not Disturb on**.
- [ ] Dock on the right, menu-bar clock with seconds, default cursor.
- [ ] **Accessibility Inspector** running with its window closed. **Xcode** quit.
- [ ] ⌘Tab shows only pgAdmin 4, Chrome, TaskRecorder and Accessibility Inspector.
- [ ] **pgAdmin:** connected, the tree open at `settlement → Schemas → public → Tables` (no `settlement_breaks`), no
  Query Tool open, window minimized.
- [ ] **Chrome:** the Goal Document tab and the blank `settlement_reconciliation` tab, with the Goal Document in front.
- [ ] **Downloads:** no `reconciliation*`, `settlement*` or `data-*` files.
- [ ] **TaskRecorder:** Task Description = the Goal. **Used Apps = `pgAdmin 4`, `Google Sheets`.** Check Used Apps
  again as the very last thing before Start.

---

## Intro (under 20 seconds, exact words)

ACTION: the Goal Document is visible behind TaskRecorder. Click **Start Recording**, then minimize TaskRecorder at
once.

SAY (exactly):
> "I will be beginning my task soon. Here is the workflow I have in mind."

ACTION: wait 2 to 3 seconds, then move the cursor to Chrome's top-left and click the yellow Minimize button.
SAY:
> "I'll move the cursor to the top-left corner of the Chrome window and click the yellow Minimize button, the middle
> of the three circles."

---

## Step 1: the two tables and a clean settlement line (pgAdmin 4, about 4.5 min)

ACTION: cursor → the Dock (right edge) → the pgAdmin elephant → click.
SAY:
> "Step 1. I'm a payments backend engineer, and one of the jobs my team owns is the daily settlement
> reconciliation. Every day, our card processor pays us for the card payments it settled, minus its fees. Before
> finance books that payout, we check it against our own ledger, which is our record of every capture our system
> made. If the two don't agree, we have to explain exactly why, to the cent, before anyone signs off.
> I'll move the cursor right to the Dock on the right edge of the screen and click pgAdmin 4, the blue elephant just
> below Chrome."

ACTION: in the Object Explorer, expand **settlement → Schemas → public → Tables**. Point at the two tables.
SAY:
> "On the left is the Object Explorer. I'll expand the settlement database, then Schemas, public and Tables. There are
> two tables. ledger_captures is our side: what our system captured today. settlement_lines is the processor's side:
> its settlement report for the same day."

ACTION: click the arrow next to **ledger_captures**, then the arrow next to **Columns**, and move the cursor down the
column names one at a time.
SAY:
> "In ledger_captures, each row is one card capture: a capture id, the order id, the processor reference, which is
> the id the processor gave this payment, then the amount, the currency, and the time we captured it."

ACTION: click the arrow next to **settlement_lines**, then its **Columns**, and move down the names.
SAY:
> "In settlement_lines, each row is one payment the processor settled: the same processor reference, the gross
> amount, the fee the processor kept, the net amount it paid us, and the currency. The processor reference is the
> one field both sides share, so that's what I'll match on."

SAY (first-use description of the input; required; never name a tool):
> "This is a synthetic test database I prepared before this session: one day of about 7,900 captures and the
> matching settlement report. It's made-up data created for this exercise, so it's free to use, with no license
> restrictions. It contains no real customer or card data, only generated reference codes."

ACTION: right-click **settlement_lines** → **View/Edit Data** → **First 100 Rows**. A new tab opens with a grid.
Point at the first row, one cell at a time.
SAY:
> "Before I write any SQL, I want to see what a clean line looks like. I'll right-click settlement_lines and choose
> View/Edit Data, then First 100 Rows. A grid opens in a new tab. The first row is PR-0000001: gross **248.44**
> dollars, fee **7.50**, net **240.94**.
> Our contract with the processor is 2.9% of the gross plus 30 cents per payment. 2.9% of 248.44 is about 7.20, and
> plus 30 cents that makes 7.50, exactly the fee here. The net, 240.94, is the gross minus the fee. That's a clean
> line. Anything that doesn't look like this is what I'm hunting for."

ACTION: close that data tab with the small **x** on its tab title at the top.
SAY:
> "I'll close this data tab with the small x on its tab title at the top."

ACTION: right-click the **settlement database** (not a table) → **Query Tool**.
SAY:
> "Now I'll right-click the settlement database in the tree and choose Query Tool. That opens an SQL editor in the
> middle of the window."

ACTION: toolbar → the small down arrow right of the floppy disk → **Save As** → type `reconciliation.sql` → Where:
**Downloads** → the blue **Save** button.
SAY:
> "Before I write anything, I'll save the file so every query is kept. In the toolbar above the editor, the second
> icon is the Save File button, a floppy disk. I'll click the small down arrow just to its right and choose Save As.
> I'll name it reconciliation dot sql, keep Downloads in the Where menu, and click the blue Save button at the
> bottom-right. The tab title at the top of the editor now reads reconciliation.sql."

---

## Step 2: the gap per currency (about 3 min)

SAY (before typing, cursor in the editor):
> "Step 2. First I want the size of the problem: per currency, how much we captured, how much the processor settled,
> and the difference. I keep each currency separate, because euros, pounds and dollars can't be added together."

ACTION: type with the loop, one line at a time, pointing at each line after you type it.
```sql
SELECT currency, l.total AS ledger_total, s.total AS settled_total, l.total - s.total AS gap
FROM (SELECT currency, sum(amount) AS total FROM ledger_captures GROUP BY currency) l
JOIN (SELECT currency, sum(gross_amount) AS total FROM settlement_lines GROUP BY currency) s USING (currency)
ORDER BY currency;
```
| Line | Point at it and say |
|---|---|
| 1 | "The output: for each currency, our total, the processor's total, and the gap between them." |
| 2 | "Our side: the sum of the captured amounts per currency. I call it l, for ledger." |
| 3 | "The processor's side: the sum of the settled gross amounts per currency, called s, joined to ours on the currency." |
| 4 | "Sorted by currency." |

ACTION: drag from **SELECT** down to the semicolon → **Execute** (the white play triangle).
SAY:
> "I'll drag from SELECT down to the semicolon to highlight the query, move up to the toolbar and click Execute, the
> white play triangle just right of the grey square Stop button."

EXPECT, in Data Output (point at each number as you read it):

| currency | ledger_total | settled_total | gap |
|---|---|---|---|
| EUR | **294708.65** | **292271.84** | **2436.81** |
| GBP | **181968.83** | **179637.27** | **2331.56** |
| USD | **725183.83** | **719036.93** | **6146.90** |

SAY:
> "Three rows in Data Output. Euros: we captured 294,708.65, and the processor settled 292,271.84, so the gap is
> 2,436.81. Pounds: a gap of 2,331.56. Dollars: a gap of 6,146.90. In every currency we captured more than the
> processor paid for. Some of that is normal and some of it isn't, and my job is to say which, for every cent."

ACTION: click at the end of the last line, press Return twice, and type the comment line. Then **⌘S**.
```sql
-- gap: EUR 2436.81 | GBP 2331.56 | USD 6146.90
```
SAY:
> "I'll note the three gaps as a comment, so I can check the spreadsheet against them later. The two dashes make it a
> comment, so it never runs. Command S to save. The star after the file name in the tab title goes away."

---

## Step 3: the breaks table, one query (about 6 min)

SAY (before typing; point at each gap figure in Data Output as you name the break types):
> "Step 3. A difference between the ledger and the settlement report can be one of four things, and each needs a
> different action.
> One: timing. The processor closes its business day at 22:00 UTC. Anything we captured after 22:00 settles in
> tomorrow's report. That's expected, not an error, so we just carry it forward.
> Two: missing. We captured it before the cut-off, but it's not in the report. That's money we may never receive, so
> we raise it with the processor.
> Three: unknown. The processor settled it, but our ledger has no record of it. That usually means our system lost a
> capture, so we investigate on our side.
> Four: an amount mismatch. Both sides have it, but the processor settled a different amount.
> And separately, even when the amounts agree, I check the fee against our contract, 2.9% plus 30 cents, and flag
> any fee more than one cent over, so finance can claim it back.
> I'll put all of these in one table called settlement_breaks, with one row per problem record."

ACTION: type with the loop. Type one line, point at it, say the line below, click at the line's end, and continue.
Pause and point after every one or two lines; never type more than about 20 seconds without pointing.
```sql
CREATE TABLE settlement_breaks AS
SELECT coalesce(l.processor_ref, s.processor_ref) AS processor_ref,
       coalesce(l.currency, s.currency) AS currency,
       CASE
         WHEN s.processor_ref IS NULL AND l.captured_at >= '2026-10-20 22:00+00' THEN 'timing'
         WHEN s.processor_ref IS NULL THEN 'missing'
         WHEN l.processor_ref IS NULL THEN 'unknown'
         WHEN l.amount <> s.gross_amount THEN 'amount mismatch'
         ELSE 'fee overcharge'
       END AS break_type,
       coalesce(l.amount, 0) - coalesce(s.gross_amount, 0) AS difference,
       s.fee - round(s.gross_amount * 0.029 + 0.30, 2) AS fee_over
FROM ledger_captures l
FULL OUTER JOIN settlement_lines s ON s.processor_ref = l.processor_ref
WHERE l.processor_ref IS NULL OR s.processor_ref IS NULL
   OR l.amount <> s.gross_amount
   OR s.fee > round(s.gross_amount * 0.029 + 0.30, 2) + 0.01;
```
| Line(s) | Point at it and say |
|---|---|
| CREATE TABLE | "This saves the result as a new table, settlement_breaks, so I can check it and export it." |
| coalesce … processor_ref | "Coalesce takes the first value that isn't empty. A missing capture has no settlement side, and an unknown line has no ledger side, so I take the reference from whichever side exists." |
| coalesce … currency | "The same for the currency." |
| CASE, first WHEN | "Now the break type, checked in order. No settlement line, and captured at or after 22:00: timing." |
| second WHEN | "No settlement line but captured before the cut-off: missing." |
| third WHEN | "No ledger capture: unknown." |
| fourth WHEN | "Both sides exist but the amounts differ: amount mismatch." |
| ELSE … END | "Anything else that reaches this list can only be here for its fee: fee overcharge." |
| difference | "The difference is our amount minus the processor's gross. An empty side counts as zero. This is each break's share of the gap." |
| fee_over | "fee_over is the fee charged minus the contract fee: 2.9% of the gross plus 30 cents, rounded to the cent." |
| FROM / FULL OUTER JOIN | "A FULL OUTER JOIN on the processor reference keeps rows from both sides, including the ones with no match. A normal join would silently drop exactly the records I'm looking for." |
| WHERE, first line | "Keep a row if either side is missing…" |
| OR amount | "…or the amounts differ…" |
| OR fee | "…or the fee is more than one cent above the contract. Every other row is a clean match and stays out." |

ACTION: drag from **CREATE** down to the final semicolon → **Execute** → click the **Messages** tab.
SAY:
> "I'll drag from CREATE down to the semicolon on the last line and click Execute in the toolbar. Then I'll click the
> Messages tab at the top-left of the results panel, next to Data Output. It says **SELECT 87**: 87 records need
> attention out of about 7,900."

ACTION: **⌘S**.
SAY:
> "Command S to save the file."

---

## Step 4: check, walk through the breaks, export (about 3.5 min)

ACTION: click at the end of the file, press Return twice, and type the check. Triple-click the line → **Execute**.
```sql
SELECT count(*) AS breaks, count(DISTINCT processor_ref) AS refs FROM settlement_breaks;
```
SAY:
> "Step 4. Before I export anything, I'll check that no record is listed twice. This counts the rows and the distinct
> processor references. I'll triple-click the line to highlight it and click Execute."
> "Data Output shows breaks **87** and refs **87**. The two counts are equal, so every reference appears exactly once.
> No record was counted under two break types."

ACTION: Return twice, type the export query, triple-click it → **Execute**.
```sql
SELECT * FROM settlement_breaks ORDER BY break_type, processor_ref;
```
SAY:
> "Now the rows I'll export, sorted by break type. Triple-click, Execute. Total rows at the bottom-left says **87**."

ACTION: walk through the grid with the cursor, group by group, scrolling as you go. Point at each example row.
SAY (one group at a time):
> "The first five rows are **amount mismatches**. For example PR-0000811 in dollars: the processor settled **2.42**
> less than we captured."
> "Next, twelve **fee overcharges**. Their difference is zero, because the amounts agree, but the fee_over column shows
> what they charged above the contract. PR-0000649 was charged **1.12** too much."
> "Then six **missing** captures, two in each currency. PR-0000505, **193.99** dollars, was captured at 1:24 in the
> morning, long before the cut-off, so it should have been in today's report. These go to the processor."
> "Then sixty **timing** rows, all captured after 22:00. They'll settle tomorrow, so no action except checking
> tomorrow's report."
> "And the last four are **unknown**. Their difference is negative, because the processor settled money our ledger
> doesn't know about, for example PR-9000001 for **80.08** dollars. These are ours to investigate."

ACTION: cursor → the small toolbar right above the grid → **Save results to file** (the down arrow, sixth from the
left). In the save dialog, select the whole name → type `settlement_breaks.csv` → Where: **Downloads** → **Save**.
SAY:
> "Now I'll export these 87 rows. I'll move the cursor to the small toolbar right above the result grid and click
> Save results to file, the down-arrow icon, sixth from the left, just left of the zig-zag graph icon. The save
> dialog suggests a name starting with data. I'll select all of it and type settlement underscore breaks dot csv,
> keep Downloads in the Where menu, and click Save at the bottom-right."

ACTION: **⌘S** → the yellow Minimize button at pgAdmin's top-left.
SAY:
> "Command S once more to save my SQL file, and I'll minimize pgAdmin with the yellow button at the top-left of its
> window."

---

## Step 5: Google Sheets: import, pivot, tie-out (about 4.5 min)

ACTION: Dock → Chrome → the **settlement_reconciliation** tab.
SAY:
> "Step 5. Now I'll build the reconciliation for the finance operations team in Google Sheets. I'll move right to the
> Dock and click Chrome, the red, yellow and green circle just above pgAdmin. At the top of the window, I'll click the
> second tab, settlement_reconciliation, my blank sheet."

ACTION: **File** (top-left) → **Import** → **Upload** tab → blue **Browse** → **Downloads** in the sidebar →
`settlement_breaks.csv` → **Open**. Import location: **Insert new sheet(s)**. Keep **Convert text to numbers**
ticked → the green **Import data** button.
SAY:
> "I'll click the File menu at the top-left and choose Import. In the dialog, I'll click the Upload tab, then the blue
> Browse button. In the Finder window I'll choose Downloads in the sidebar, then settlement_breaks.csv, and click
> Open. For Import location I'll pick Insert new sheet, so the data gets its own tab. I'll keep Convert text to
> numbers ticked so the differences become numbers. Then I'll click the green Import data button."
> "A new tab, settlement_breaks, appears at the bottom-left. I'll scroll down: the last row is **88**, so 87 breaks
> plus the header row, the same as the database."

ACTION: click **A1** → **Insert** → **Pivot table** → keep **New sheet** → **Create**. In the editor on the right:
**Rows → Add → currency**, then **Columns → Add → break_type**, then **Values → Add → difference** (summarize by
**SUM**).
SAY:
> "A pivot table groups and totals data without formulas. I'll click cell A1, then the Insert menu at the top, and
> Pivot table. In the dialog I'll keep New sheet and click Create."
> "The pivot table editor opens on the right side. Next to Rows I'll click Add and choose currency. Next to Columns
> I'll click Add and choose break_type. Next to Values I'll click Add and choose difference, summarized by SUM."

EXPECT: currencies down the side (EUR, GBP, USD in rows 3 to 5), the five break types across the top, and a
**Grand Total** column, normally **G**. Point along each row as you speak.
SAY:
> "Each cell is the money in one kind of break in one currency. In dollars, for example, timing is **6,216.79**,
> missing is **260.51**, and unknown is **−332.82**, negative because that's money the processor paid that our ledger
> doesn't have. The fee overcharge column is zero, because a fee doesn't change the gross amount. The Grand Total
> column on the right adds up each currency's breaks."

ACTION:
1. Click **I2** → type `DB gap`.
2. In **I3, I4 and I5**, type `2436.81`, `2331.56` and `6146.90` (EUR, GBP, USD, the same order as the pivot).
3. Click **J2** → type `Check`.
4. Click **J3** → type `=ROUND(G3-I3,2)` → Return.
5. Select **J3:J5** → **⌘D**.

(If the Grand Total isn't in column G, use the letter where it is.)
SAY:
> "Now the tie-out. If my breaks explain everything, each currency's Grand Total must equal the gap I measured in the
> database. In cell I2, to the right of the pivot, I'll type DB gap, then the three gaps from my SQL comment in I3 to
> I5, in the same order as the pivot: euros, pounds, dollars."
> "In J2 I'll type Check, and in J3, equals ROUND of G3 minus I3, to two decimals. I round to cents because
> spreadsheets store decimals in binary and can leave a tiny leftover like 0.0000000001. I'll select J3 to J5 and
> press Command D to fill down."
> "All three are **0**. The breaks explain the full gap in every currency, to the cent. Nothing is unexplained."

---

## Step 6: summary, download, stop check (about 1.5 min)

ACTION: click **A8** and type the summary. Before typing each count, point at that column in the pivot.
```
Summary: 87 breaks explain the full gap in EUR, GBP and USD. Raise 6 missing and 4 unknown with the processor, carry 60 timing items to tomorrow, claim back 12 fee overcharges.
```
SAY:
> "Step 6. A one-line summary for finance operations. In cell A8 I'll type the conclusion: 87 breaks explain the full
> gap in all three currencies. Six missing captures and four unknown lines need a ticket with the processor. Sixty
> timing items carry over to tomorrow. And twelve fee overcharges go back to the processor as a fee claim."

ACTION: **File** (top-left) → hover **Download** → **Microsoft Excel (.xlsx)**. Then move to the **download arrow**
in Chrome's toolbar at the top-right and click it.
SAY:
> "To deliver it, I'll click the File menu at the top-left, hover over Download near the middle of the menu, and click
> Microsoft Excel in the submenu on the right. A download arrow appears in Chrome's toolbar at the top-right. I'll
> click it: it lists **settlement_reconciliation.xlsx**, saved to Downloads."

**STOP CHECK: don't start the epilogue until all three are true.**
- The download list shows **settlement_reconciliation.xlsx**.
- **settlement_breaks.csv** was saved to Downloads in Step 4.
- The SQL file was saved with ⌘S, so its tab title had no star.

SAY:
> "Before I wrap up, I'll check the deliverables. The download list shows settlement_reconciliation.xlsx.
> settlement_breaks.csv and reconciliation.sql are both in Downloads, and I saved the SQL file with Command S before
> I left pgAdmin."

---

## Epilogue (about 3 to 3.5 min, max 4:00; the mouse may rest, the sheet stays on screen)

SAY in your own words, covering all five points. About 3 minutes at a calm pace:

> **Completion and outcome.** "To wrap up: the reconciliation is complete. The ledger and the settlement report
> differed by 2,436.81 euros, 2,331.56 pounds and 6,146.90 dollars, and all of it is explained by 87 breaks. I
> verified it two ways. In the database, no record is listed twice. In the sheet, the breaks in each currency add up
> to the database gap exactly, to the cent. The limitation is that this is one synthetic day. In production, I'd also
> compare the net payout with the actual bank deposit."

> **Approach and key decision.** "My approach was a FULL OUTER JOIN on the processor reference, so nothing on either
> side could silently drop out. Then I gave every difference a type that tells someone what to do with it. The key
> decision was the 22:00 cut-off. Sixty-six of our captures weren't in the report, but sixty of them were simply
> after the cut-off and will settle tomorrow. If I'd raised all sixty-six with the processor, I'd have wasted their
> time and ours. Only six are real."

> **Challenges.** "The tricky part was making sure each record lands in exactly one category. A record can be both
> unmatched and suspicious, so the order of the checks in the CASE matters: missing sides first, then amounts, then
> fees. The 87-equals-87 check proved there were no double counts. Fees were the other subtle point: the processor's
> fee can differ from my formula by a rounding cent, so I only flag fees more than one cent over."

> **Quality.** "I'm confident in the result, because the tie-out in the sheet is independent of the query that built
> the list. If I'd missed a break or counted one twice, the check column wouldn't be zero. The weak spots are things
> this data doesn't have: same-day refunds, chargebacks and partial captures would each need their own break type."

> **Reflection.** "With more time, I'd run this automatically every night, carry today's 60 timing items forward
> and confirm they appear in tomorrow's report, and alert the team whenever a missing or unknown break shows up. For
> someone less experienced, the lesson is: match on a shared reference rather than on amounts, keep currencies
> separate, and don't trust a reconciliation until the breaks add up to the gap."

SAY:
> "That completes the task. I'll move the cursor to the Dock on the right and click TaskRecorder, just below pgAdmin,
> to stop the recording."

ACTION: TaskRecorder → **Stop Recording**. Don't quit; wait for **Idle**.

---

## Bridge lines (use these instead of going silent)

- **While typing a long query,** point at the line you just typed: *"This line takes the reference from whichever
  side exists; next, the break type…"*
- **While the import runs:** *"While that loads: the CSV has one row per break, so the operations team can work
  through it line by line."*
- **Before switching apps:** *"I'll move to the Dock on the right and click {{Chrome / pgAdmin}} to {{build the
  reconciliation / check the numbers}}."*

## If something goes wrong (say it, fix it, check it)

- **Syntax error:** *"The Messages tab says syntax error near …; I left out {{a comma / a bracket}}. I'll fix it on
  line …, highlight the query and click Execute again… and now it works."*
- **Nothing was highlighted, so the whole file ran:** *"That ran the whole file instead of my selection."* If it says
  `relation "settlement_breaks" already exists`, say so. Run `DROP TABLE settlement_breaks;` (type it, triple-click,
  Execute), then highlight the CREATE TABLE query and run it again.
- **SELECT is not 87, or the check isn't 87 | 87:** read the number aloud. Find the typo in the query, `DROP TABLE
  settlement_breaks;`, then recreate the table and rerun the check.
- **A Check cell isn't 0:** click the I cell for that currency and compare it with your comment line. Retype it and
  press Return. The check updates.
- **The pivot shows COUNTA instead of SUM:** in the editor on the right, under Values, change Summarize by to SUM.
- **Anything personal, Studio or Slack appears on screen:** stop and re-record from the start. Don't narrate over it.

---

## Numbers card (for your phone)

| What | Value |
|---|---|
| Clean line example | PR-0000001: gross 248.44, fee 7.50 (= 2.9% + 0.30), net 240.94, USD |
| Gap EUR | ledger 294708.65, settled 292271.84, **gap 2436.81** |
| Gap GBP | ledger 181968.83, settled 179637.27, **gap 2331.56** |
| Gap USD | ledger 725183.83, settled 719036.93, **gap 6146.90** |
| CREATE TABLE | Messages: **SELECT 87** |
| Duplicate check | **87 / 87** |
| Breaks by type | amount mismatch 5, fee overcharge 12, missing 6, timing 60, unknown 4 |
| Examples | mismatch PR-0000811 2.42 · fee PR-0000649 1.12 over · missing PR-0000505 193.99 (01:24) · unknown PR-9000001 −80.08 |
| Pivot USD row | timing 6216.79 · missing 260.51 · unknown −332.82 · mismatch 2.42 · fee 0 · total 6146.90 |
| Sheet | last row 88 · I3:I5 = 2436.81 / 2331.56 / 6146.90 · J3:J5 = 0 |
| Fee overcharge to claim | EUR 2.60 · GBP 1.70 · USD 6.08 (total 12 lines) |

## After recording

1. Wait for **Idle** → **Show Recordings**. Copy the newest `recording_…` folder and its `.zip`, unchanged, into
   `/Users/Shared/payments-task/`.
2. Copy `reconciliation.sql`, `settlement_breaks.csv` and `settlement_reconciliation.xlsx` from Downloads into
   `/Users/Shared/payments-task/` too.
3. Tell me. I'll check the take (mouse, typing, silence, overlap, screen, files) and build Deliverables.zip.
