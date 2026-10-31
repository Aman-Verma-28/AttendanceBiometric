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
> "Step 1. I'm a payments backend engineer, and every day I check what our card processor settled against what our ledger captured. Before finance books the payout, every difference has to be explained to the cent.
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

This part is broken into single actions. Each step says **where** the control is, **what** to do, and what you'll
**see** afterwards. The positions come from your own screen in the payments take 2 recording, with Chrome on the
left of the screen and the Dock on the right.

**Before your practice run,** look at the finished layout in
[reference/settlement_reconciliation-reference.xlsx](reference/settlement_reconciliation-reference.xlsx). Open it
**only with Quick Look**: select it in Finder and press the space bar. Never open it in Google Sheets, because it's
Claude-made and must never touch the task.

### The Google Sheets window (learn this map once)
```
+-------------------------------------------------------------------------------------------+
| o o o  [Goal Document]  [settlement_reconciliation]                      <- Chrome tabs     |
| <  >  C   docs.google.com/spreadsheets/...          star  (download)  profile  ...          |
|                                                      ^ the download icon appears here,       |
|                                                        after a download                     |
| [green icon] settlement_reconciliation        clock  comments  camera  [Share]  (V)         |
|              File Edit View Insert Format Data Tools Extensions Help    <- MENUS             |
|  search undo redo print ... 100% ... B I ...                            <- toolbar           |
| [A1 v] fx ......                         <- Name box (the cell you're in) + formula bar       |
|        A      B      C      D      E      F      G      H      I      J   ...  <- COLUMNS  |
|    1                                                                                        |
|    2                                                                                        |
|    3          <- ROW NUMBERS run down the left edge                                         |
|   ...                                                                                       |
| [+] [=]  Sheet1 v   settlement_breaks v   Pivot Table 1 v               <- SHEET TABS       |
+-------------------------------------------------------------------------------------------+
```
- **Menus:** File is the first word under the sheet title, at the top-left. Insert is the 4th menu.
- **Cell address:** the column letter, then the row number. `I2` is column I, row 2, and `J3:J5` means J3, J4 and J5.
- **Typing in a cell:** click the cell, type, then press **Return**. Return saves it and moves one cell **down**.
- **Undo a slip:** press **⌘Z** and say "Command Z to undo".

---

### 5A. Open the blank sheet

**5.1** WHERE: the Dock on the right edge of the screen.
DO: move the cursor there and click **Chrome**, the red, yellow and green circle just above pgAdmin.
SEE: Chrome comes to the front, showing the Goal Document.

**5.2** WHERE: the tabs along the very top of the Chrome window.
DO: click the **second tab**, `settlement_reconciliation`.
SEE: an empty grid. At the bottom-left there's one sheet tab, **Sheet1**.
> "Step 5. Now I'll build the reconciliation for the finance operations team in Google Sheets. I'll move right to the
> Dock and click Chrome, the red, yellow and green circle just above pgAdmin. At the top of the window, I'll click the
> second tab, settlement_reconciliation, my blank sheet."

---

### 5B. Import the CSV (two small windows)

**5.3** WHERE: top-left, the first menu word under the sheet title.
DO: click **File**.
SEE: a long menu drops down: New, Open, **Import**, Make a copy, Share, Email, Download, and more.

**5.4** WHERE: the 3rd item in that menu.
DO: click **Import**.
SEE: a large **Import file** window in the middle of the screen. It opens on the **My Drive** tab, which may list old
files. **Ignore them.**
```
+-- Import file --------------------------------------------- [X] -+
|  [ Search in Drive or paste URL ]                                  |
|  My Drive    Shared with me    Recent    Upload   <- 4 tabs        |
|  ...files...                                                       |
+--------------------------------------------------------------------+
```

**5.5** WHERE: the row of four tabs near the top of that window. **Upload** is the 4th tab, the one furthest right.
DO: click **Upload**.
SEE: a dashed box with a cloud picture and a blue **Browse** button in the middle.

**5.6** WHERE: the middle of the dashed box.
DO: click the blue **Browse** button.
SEE: a Finder window.

**5.7** WHERE: the left sidebar of the Finder window.
DO: click **Downloads**.

**5.8** WHERE: the file list in the middle of the Finder window.
DO: click **settlement_breaks.csv** once, then click the **Open** button at the bottom-right of the Finder window.
SEE: Finder closes and a **smaller** Import file window appears in the middle of the screen:
```
+-- Import file ------------------------------------- [X] -+
|  File:  settlement_breaks.csv                            |
|  Import location              Separator type             |
|  [ Create new spreadsheet v ]  [ Detect automatically v ] |
|  [x] Convert text to numbers, dates, and formulas        |
|                           [ Import data ]  [ Cancel ]    |
+----------------------------------------------------------+
```

**5.9** WHERE: the **left** box, under the words **Import location**. It says **Create new spreadsheet** by default.
DO: click that box.
SEE: a list of six options: Create new spreadsheet, **Insert new sheet(s)**, Replace spreadsheet, Replace current
sheet, Append to current sheet, Replace data at selected cell.

**5.10** WHERE: the 2nd option in that list.
DO: click **Insert new sheet(s)**.
SEE: the left box now says **Insert new sheet(s)**. This step matters: the default would make a separate
spreadsheet.

**5.11** WHERE: the right box (Separator type) and the checkbox below both boxes.
DO: nothing. Just check that the right box says **Detect automatically** and the checkbox **Convert text to numbers,
dates, and formulas** has a green tick.
> "I'll click the File menu at the top-left and choose Import. In the window, I'll click the Upload tab, the fourth
> tab on the right, then the blue Browse button. In Finder I'll choose Downloads in the sidebar, then
> settlement_breaks.csv, and click Open. For Import location I'll change Create new spreadsheet to Insert new sheet,
> so the data gets its own tab in this file. I'll keep Convert text to numbers ticked, so the differences become real
> numbers I can add up."

**5.12** WHERE: the bottom-right of the small window. The green button is left of Cancel.
DO: click the green **Import data** button.
SEE: after 2 or 3 seconds, a new sheet tab **settlement_breaks** at the bottom-left, already open. Columns A to E hold
processor_ref, currency, break_type, difference and fee_over.
> "While that loads: the file has one row per break, so the operations team can work through it line by line."

**5.13** WHERE: the bottom-middle of the sheet, where a small pop-up appears saying **Convert to table**.
DO: **don't click "Convert to table".** Click the small **x** at the right end of that pop-up to close it, or just
leave it alone.

**5.14** WHERE: anywhere over the grid.
DO: scroll down with the trackpad (two fingers) until you reach the last row. Point at its row number on the left
edge: **88**. Then scroll back up to the top.
> "A new tab, settlement_breaks, appears at the bottom-left. I'll scroll down: the last row is 88, so 87 breaks plus
> the header row, the same as the database."

---

### 5C. Build the pivot table

**5.15** WHERE: the top-left cell of the grid, column A row 1. It says **processor_ref**.
DO: click cell **A1**.
SEE: a blue outline around A1, and the Name box at the far left of the formula bar shows **A1**.

**5.16** WHERE: the menus at the top. **Insert** is the 4th menu: File, Edit, View, **Insert**.
DO: click **Insert**.
SEE: a menu: Cells, Rows, Columns, Sheet, Pre-built tables, Timeline, Chart, **Pivot table**, Image, and more.

**5.17** WHERE: the middle of that menu, just below **Chart**.
DO: click **Pivot table**.
SEE: a small **Create pivot table** window, a little right of the middle of the screen:
```
+-- Create pivot table ------------ [X] -+
|  Data range                            |
|  settlement_breaks!A1:E88         [#]  |
|  Insert to                             |
|  (o) New sheet                         |
|  ( ) Existing sheet                    |
|                  [ Cancel ] [ Create ] |
+----------------------------------------+
```

**5.18** WHERE: inside that small window.
DO: check that **Data range** says `settlement_breaks!A1:E88` and that **New sheet** has the filled circle. Don't
change anything.

**5.19** WHERE: the bottom-right of the small window. The green button is right of Cancel.
DO: click the green **Create** button.
SEE:
- A new sheet tab, **Pivot Table 1**, at the bottom-left.
- On the left, an empty pivot with the grey words Rows, Columns and Values.
- On the right, the **Pivot table editor** panel:
```
+-- Pivot table editor ---------------------------------- [X] -+  <- X = close the panel
|  [ settlement_breaks!A1:E88 ]       |  Search               |
|                       [Clear all]   |  processor_ref        |
|  Suggested    (ignore these)        |  currency             |  <- a list of the column
|   ( ) Sum of difference for each... |  break_type           |     names; don't drag from
|  Rows                     [ Add ]   |  difference           |     it, use the Add buttons
|  Columns                  [ Add ]   |  fee_over             |
|  Values                   [ Add ]   |                       |
|  Filters                  [ Add ]   |                       |
+--------------------------------------------------------------+
```
> "A pivot table groups and totals data without formulas. I clicked cell A1, then the Insert menu at the top, and
> Pivot table. The data range is the whole settlement_breaks tab, and I'll keep New sheet and click the green Create
> button. The pivot table editor opens on the right side."

**5.20** WHERE: in the editor, the line that says **Rows**, with a green-outlined **Add** button at its right end.
DO: click that **Add** button.
SEE: a small list drops down under it, with a search box at the top and the five column names below.

**5.21** WHERE: in that small list.
DO: click **currency**.
SEE: EUR, GBP and USD appear down column A, plus a Grand Total row. In the editor, a grey card named **currency**
appears under Rows, showing Order, Sort by and Show totals. **Leave those as they are.**
> "Next to Rows, I'll click the green Add button and choose currency, so each currency gets its own row."

**5.22** WHERE: in the editor, the line that says **Columns**, now a little lower because the currency card pushed
it down. **Add** is at its right end.
DO: click that **Add** button.

**5.23** WHERE: in the small list that drops down.
DO: click **break_type**.
SEE: the five break types appear across the top of the pivot, and a **break_type** card appears under Columns.
**Leave it as it is.**
> "Next to Columns, I'll click Add and choose break_type, so each kind of break gets its own column."

**5.24** WHERE: in the editor, the line that says **Values**, below the Columns card. **Add** is at its right end.
DO: click that **Add** button.
SEE: a list whose first item is **Calculated Field**, followed by the five column names. **Don't** click Calculated
Field.

**5.25** WHERE: in that list.
DO: click **difference**.
SEE: numbers fill the pivot. A **difference** card appears under Values, with **Summarize by: SUM**.

**5.26** WHERE: the difference card under Values, at its left: the box under **Summarize by**.
DO: check that it says **SUM**. If it says anything else, such as COUNTA, click the box and choose **SUM**.
> "Next to Values, I'll click Add and choose difference. Summarize by says SUM, so each cell adds up the money."

**5.27** WHERE: the pivot on the left of the screen. Compare it with the reference file:
```
        A                  B                 C               D         E          F          G
  1   SUM of difference  break_type
  2   currency           amount mismatch   fee overcharge  missing   timing     unknown    Grand Total
  3   EUR                4.59              0               341.08    2231.22    -140.08    2436.81
  4   GBP                6.67              0               425.01    1948.83    -48.95     2331.56
  5   USD                2.42              0               260.51    6216.79    -332.82    6146.9
  6   Grand Total        13.68             0               1026.6    10396.84   -521.85    10915.27
```
DO: point along the USD row, then up at **Grand Total** in **G2**.
**If Grand Total isn't in column G,** use the letter where it is in step 5.33.
> "Each cell is the money in one kind of break in one currency. In dollars, for example, timing is 6,216.79,
> missing is 260.51, and unknown is −332.82, negative because that's money the processor paid that our ledger
> doesn't have. The fee overcharge column is zero, because a fee doesn't change the gross amount. The Grand Total
> column on the right adds up each currency's breaks. I'll ignore the Grand Total row at the bottom, because it adds
> three currencies together."

**5.28** WHERE: the top-right corner of the **Pivot table editor** panel, the **X** on the same line as its title.
DO: click the **X**.
SEE: the panel closes and the grid fills the window. Columns **I** and **J** are now visible. They were hidden under
the panel.
> "I'll close the pivot table editor with the X at its top-right, so I can use the columns to the right of the
> pivot."

*If the panel opens again later, because you clicked inside the pivot, close it again with the same X.*

---

### 5D. The tie-out: is every cent explained?

**5.29** WHERE: column **I**, row **2**, one empty column to the right of Grand Total.
DO: click cell **I2**, type `DB gap` and press **Return**.
SEE: I2 says DB gap, and the blue outline jumps down to **I3**.

**5.30** WHERE: you're in I3 now.
DO: type `2436.81` and press **Return**. Type `2331.56` and press **Return**. Type `6146.90` and press **Return**.
SEE: I3, I4 and I5 hold the three gaps, on the same rows as EUR, GBP and USD. Sheets may show 6146.9, which is fine.
> "Now the tie-out. If my breaks explain everything, each currency's Grand Total must equal the gap I measured in the
> database. In cell I2, to the right of the pivot, I'll type DB gap, then the three gaps from my SQL comment in I3 to
> I5, in the same order as the pivot: euros, pounds, dollars."

**5.31** WHERE: column **J**, row **2**, just right of I2.
DO: click cell **J2**, type `Check` and press **Return**.
SEE: the outline jumps down to **J3**.

**5.32** WHERE: you're in J3 now.
DO: type `=ROUND(G3-I3,2)` exactly. It starts with an equals sign and has no spaces. A small grey help box about
ROUND pops up while you type; ignore it.

**5.33** DO: press **Return**.
SEE: **J3 shows 0**.
> "In J2 I'll type Check, and in J3, equals ROUND of G3 minus I3, to two decimals. That's the pivot's total minus the
> database gap for euros. I round to cents because spreadsheets store decimals in binary and can leave a tiny leftover
> like 0.0000000001."

**5.34** WHERE: cell J3.
DO: click **J3**. Hold **Shift** and click **J5**.
SEE: a blue box around J3, J4 and J5.

**5.35** DO: hold **Command** and press **D**, and say "Command D to fill down".
SEE: **J4 and J5 also show 0.**
> "I'll select J3 to J5 and press Command D to fill the formula down to the other two currencies."

**5.36** DO: point at each 0 in turn.
> "All three are 0. The breaks explain the full gap in every currency, to the cent. Nothing is unexplained."

**Don'ts in Sheets:**
- **Don't type inside the pivot** (A1 to G6). Sheets won't let you change pivot cells.
- **Don't click the Suggested options** in the editor, or Convert to table.
- **Don't sort, drag or move columns.**
- **If you typed in the wrong cell,** press **⌘Z** (say "Command Z to undo"), then click the right cell.

---

## Step 6: summary, download, stop check (about 1.5 min)

**6.1** WHERE: column **A**, row **8**, two empty rows below the pivot's Grand Total row.
DO: click cell **A8**. Type the line below, pointing at the pivot before each number, then press **Return**.
```
Summary: 87 breaks explain the full gap in EUR, GBP and USD. Raise 6 missing and 4 unknown with the processor, carry 60 timing items to tomorrow, claim back 12 fee overcharges.
```
SEE: the text runs across the empty cells to the right of A8. That's normal; it's all in A8.
> "Step 6. A one-line summary for finance operations. In cell A8 I'll type the conclusion: 87 breaks explain the full
> gap in all three currencies. Six missing captures and four unknown lines need a ticket with the processor. Sixty
> timing items carry over to tomorrow. And twelve fee overcharges go back to the processor as a fee claim."

**6.2** WHERE: top-left, the first menu word under the sheet title.
DO: click **File**.

**6.3** WHERE: the 7th item in the File menu, **Download**. It has a small arrow at its right end.
DO: move the cursor onto **Download** and rest it there. Don't click.
SEE: a second menu opens to the right: Microsoft Excel (.xlsx), OpenDocument (.ods), PDF, and more.

**6.4** WHERE: the first item of that second menu.
DO: move the cursor straight right into it and click **Microsoft Excel (.xlsx)**.

**6.5** WHERE: Chrome's toolbar at the top-right, next to the address bar. A **download icon**, a down arrow, appears
between the star and the profile icon. A small list may open under it by itself for a few seconds.
DO: move the cursor up to the download icon and click it.
SEE: the list shows **settlement_reconciliation.xlsx**. Point at it. Then click an empty cell in the sheet to close
the list.
> "To deliver it, I'll click the File menu at the top-left, rest on Download near the middle of the menu, and click
> Microsoft Excel in the submenu on the right. A download icon appears in Chrome's toolbar at the top-right. I'll
> click it: it lists settlement_reconciliation.xlsx, saved to Downloads."

**6.6** WHERE: the sheet tabs at the bottom-left.
DO: make sure **Pivot Table 1** is the open tab, so the result stays on screen during the epilogue.

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
- **The import made a separate spreadsheet** (Import location was left on Create new spreadsheet): say *"That
  created a separate file; I wanted a new tab in this one."* Close that browser tab, go back to the
  settlement_reconciliation tab and import again from step 5.3, choosing Insert new sheet(s).
- **The pivot editor disappeared before you finished:** click any cell inside the pivot (A1 to G6) and it comes back.
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
