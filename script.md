# Narration script: payments refund list (pgAdmin 4 + Google Sheets, about 32 minutes)

Goes with [run-sheet.md](run-sheet.md) Phase G. The run sheet has the setup. This file is what you **do** and **say**,
with the real numbers from the loaded data.

## How to use this script
- **Rehearse with it; don't read it on camera.** Learn the flow and the *why* lines, then say them in your own words.
  Only the intro sentence must be word for word.
- **Keep it off the screen.** Use your phone, an iPad or a printout.
- `ACTION` = what your hands do. `SAY` = what you say while doing it. Numbers in **bold** are what the screen will show
  with this data. If the screen shows something else, say what you see.
- **Every click:** name the control, say where it is, and say the cursor movement. Never a bare "this" or "here".
- **Say every keyboard shortcut** as you press it ("Command S to save").
- **No silence over 45 seconds. No typing burst over 45 seconds:** type a query in two or three bursts and talk in
  between.
- **To run one query:** highlight the whole query, then click Execute. Triple-click a one-line query; drag from the
  first word to the semicolon for a longer one.

### The pattern for every click
> "I'll move the cursor [direction] to [named control], the [shape or colour] in the [screen area], and click it
> [to do what]."

| Don't say | Say |
|---|---|
| "click here" | "click Execute, the white play triangle in the toolbar above the editor" |
| "copy this" | "double-click the first order id in Data Output and press Command C" |
| "it says here" | "the Messages tab, at the top-left of the results panel, says SELECT 110" |
| "save it" | "Command S to save; the star after the file name in the tab title disappears" |

---

## Screen map (check it once on the real screen)

**macOS**
- **Dock** on the right edge. **Chrome** is the red, yellow and green circle; **pgAdmin 4** is the blue elephant just
  below it; **TaskRecorder** is just below pgAdmin.
- **Window buttons**: three circles at each window's top-left: red Close, **yellow Minimize**, green Zoom.

**pgAdmin 4**
- **Object Explorer**: the panel down the left side.
- **Query Tool toolbar**, the row of icons above the editor, from left to right:
  - Open File (folder);
  - **Save File** (floppy disk), with a **small down arrow** next to it that holds **Save As**;
  - Edit;
  - Filter;
  - the "No limit" box;
  - Stop (grey square);
  - **Execute** (white **play triangle**, F5).
- **Editor**: the middle area, with line numbers down its left edge.
- **Results panel**: the lower half, with the **Data Output** and **Messages** tabs at its top-left.
- **Status bar**: the bottom edge. **Total rows** is at the bottom-left, and **Query complete** with the time is to its
  right.
- **Save results to file**: in the small toolbar right above the result grid, the **down-arrow icon**, sixth from the
  left, just left of the zig-zag graph icon.

**Chrome / Google Sheets**
- **Tabs** across the top: **Goal Document**, then **refund_summary**.
- The **File, Edit, View, Insert, …** menus at the top-left, under the sheet title.
- The **sheet tabs** at the bottom-left. The **pivot table editor** opens as a panel on the right side.
- The **download arrow** in Chrome's toolbar at the top-right, after a download.

| Section | Target | Clock at end (about) |
|---|---|---|
| Intro | 0:20 | 0:20 |
| 1. Find the orders charged more than once | 4:00 | 4:20 |
| 2. The retry pattern on one order | 3:00 | 7:20 |
| 3. Build the refund list | 6:00 | 13:20 |
| 4. Check, total, export | 6:00 | 19:20 |
| 5. Sheets: import, pivot, cross-check | 7:00 | 26:20 |
| 6. Summary, download, stop check | 3:00 | 29:20 |
| Epilogue | 3:00 | 32:20 |

---

## Intro (under 20 seconds, exact words)

ACTION: the Goal Document is visible behind TaskRecorder. **Used Apps shows pgAdmin 4 and Google Sheets.** Click
**Start Recording**, then minimize TaskRecorder at once.

SAY (exactly):
> "I will be beginning my task soon. Here is the workflow I have in mind."

ACTION: wait 2 to 3 seconds. Cursor to Chrome's top-left → yellow Minimize.
SAY:
> "I'll move the cursor to the top-left corner of the Chrome window and click the yellow Minimize button, the middle
> of the three circles."

---

## Step 1: find the orders charged more than once (pgAdmin 4)

ACTION: cursor → Dock (right edge) → pgAdmin elephant → click.
SAY:
> "Step 1. Yesterday our payment gateway had timeouts, and support says some customers were charged twice. I'll move
> the cursor right to the Dock on the right edge of the screen and click pgAdmin 4, the blue elephant just below
> Chrome."

ACTION: Object Explorer: expand payments → Schemas → public → Tables → payments → Columns, and point down the columns.
SAY:
> "On the left side is the Object Explorer. I'll expand the payments database, then Schemas, public, Tables, and the
> payments table, then click the arrow next to Columns. Each row of this table is one capture attempt, which means one
> try at taking money from a card. The columns are the payment id, the order id, a customer code, the amount, the
> currency, a status of captured or failed, the idempotency key the checkout service sent, and the time."

SAY (first-use description of the input; required; never name a tool):
> "This is a synthetic test copy of one day of payments, about ten thousand rows prepared before this session. It
> contains no real customer data: customers are just codes, and there are no names or card numbers."

ACTION: right-click the **payments database** (not the table) → **Query Tool**.
SAY:
> "I'll move up the tree, right-click the payments database, and choose Query Tool from the menu. That opens an SQL
> editor in the middle of the window."

ACTION: toolbar → small down arrow right of the floppy disk → **Save As** → type `refund_investigation.sql` → Where:
`payments-task` → blue **Save**.
SAY:
> "Before I write anything, I'll save the file so all my queries are kept. In the toolbar above the editor, the second
> icon from the left is the Save File button, a floppy disk. I'll click the small down arrow just to its right and
> choose Save As. In the dialog, I'll type refund underscore investigation dot sql, choose the payments-task folder in
> the Where menu, and click the blue Save button at the bottom-right. The tab title at the top of the editor now reads
> refund_investigation.sql."

ACTION: type `SELECT count(*) AS attempts, count(DISTINCT order_id) AS orders FROM payments;` → triple-click → Execute.
SAY:
> "First, the size of the table. I'll type a count of all attempts and of distinct orders. I'll triple-click the line
> to highlight it, move up to the toolbar and click Execute, the white play triangle just right of the grey square Stop
> button."
> "In Data Output in the lower half: **10,107** attempts but only **9,850** orders. A few extra attempts are normal: a
> card gets declined and the customer tries again. The problem is the gateway timeout, which the incident report puts
> between 14:00 and 14:30 UTC on October 14th."

ACTION: type the window query in two bursts (lines 1–4, then 5–7) → drag-select it → Execute.
```sql
SELECT order_id, count(*) AS captures
FROM payments
WHERE status = 'captured'
  AND created_at >= '2026-10-14 14:00+00' AND created_at < '2026-10-14 14:30+00'
GROUP BY order_id
HAVING count(*) > 1
ORDER BY captures DESC, order_id;
```
SAY (while typing the first burst):
> "Now I'll count captures per order inside that window. I only count status captured, because a failed attempt never
> took any money."
SAY (second burst):
> "GROUP BY puts each order's rows together, and HAVING count greater than one keeps only the orders captured more than
> once. I'll sort the worst first."
SAY (after running):
> "I'll drag from SELECT down to the semicolon to highlight the query and click Execute in the toolbar. In the status
> bar at the bottom-left, Total rows says **100**. So a hundred orders were charged more than once. The first ten rows
> in Data Output show **3** captures: those customers were charged three times. The rest show 2."

ACTION: **⌘S**.
SAY:
> "Command S to save the file. The star after the name in the tab title goes away."

---

## Step 2: the retry pattern on one order

ACTION: Data Output → double-click the first order id (**2010091**) → ⌘C. In the editor, type the query, then paste the
id with ⌘V → drag-select → Execute.
```sql
SELECT id, order_id, status, amount, currency, idempotency_key, created_at
FROM payments
WHERE order_id = 2010091
ORDER BY created_at;
```
SAY:
> "Step 2. I want to see why the gateway let these through. In Data Output I'll double-click the first order id,
> 2010091, and press Command C to copy it. Back in the editor I'll write a query for every attempt of one order, and
> paste the id after order_id equals with Command V. Then I'll highlight the query and click Execute."
> "Data Output shows **three** rows, all captured, all **217.38 dollars**, at **14:15:13**, **14:15:28** and **14:15:46**:
> three charges in about half a minute."

ACTION: point along the **idempotency_key** column, row by row.
SAY (the key *why*):
> "Now the idempotency_key column. Every attempt has a **different** key. An idempotency key is a unique id the checkout
> service sends with a payment, so if it ever sends the same request twice, the gateway recognises the key and charges
> only once. But when the gateway timed out, the retry code generated a new key each time. To the gateway these looked
> like three separate payments, so it charged all three. The root cause is the retry creating a new key instead of
> reusing the original one. That's a code fix for later. Today's job is refunding the extra charges."

ACTION: **⌘S**.

---

## Step 3: build the refund list

SAY (before typing, cursor resting in the editor):
> "Step 3. The rule for the refunds: for each order, number its successful captures in time order. Number one is the
> charge the customer meant to make, so we keep it. Numbers two and three are duplicates, so we refund them. The order
> of operations matters: I'll filter to captured rows first and number them second."

ACTION: type the real query in three bursts → drag-select → Execute → click the **Messages** tab.
```sql
CREATE TABLE refund_list AS
SELECT id AS payment_id, order_id, customer_id, amount, currency
FROM (
  SELECT p.*, ROW_NUMBER() OVER (PARTITION BY order_id ORDER BY created_at, id) AS rn
  FROM payments p
  WHERE status = 'captured'
) c
WHERE rn > 1;
```
SAY (bursts):
> "Now the right way. The inner query keeps only captured rows. Then ROW_NUMBER, partitioned by order_id, restarts the
> numbering for every order, ordered by time. The id breaks a tie if two captures share the same second."
> "The outer query keeps row number two and above, the duplicates, and saves them as a new table called refund_list."
SAY (after running):
> "I'll highlight from CREATE down to the semicolon and click Execute. Then I'll click the Messages tab at the top-left
> of the results panel, next to Data Output. It says **SELECT 110**: one refund for each of the 90 orders charged twice,
> and two refunds for each of the 10 orders charged three times. 90 plus 20 is 110."

ACTION: **⌘S**.

---

## Step 4: check, total, export

ACTION: type the check in two bursts → drag-select → Execute.
```sql
SELECT p.order_id, count(*) - count(r.payment_id) AS captures_left
FROM payments p
LEFT JOIN refund_list r ON r.payment_id = p.id
WHERE p.status = 'captured'
  AND p.order_id IN (SELECT order_id FROM refund_list)
GROUP BY p.order_id
HAVING count(*) - count(r.payment_id) <> 1;
```
SAY:
> "Step 4. Before anything is refunded, I'll prove each customer ends up paying exactly once. For every affected order,
> I take its captures and subtract the ones in the refund list. That must leave exactly one. The LEFT JOIN matches each
> capture to the refund list if it's there, and count of r.payment_id counts only the matched ones. This query lists
> any order where the result isn't one."
> "Highlight, Execute. Data Output is **empty** and Total rows at the bottom-left says **zero**. No order is left with
> zero charges or two charges, so every customer pays exactly once."

ACTION: type the totals → drag-select → Execute.
```sql
SELECT currency, count(*) AS refunds, sum(amount) AS refund_total
FROM refund_list
GROUP BY currency
ORDER BY currency;
```
SAY:
> "Now the totals per currency. Euros, pounds and dollars can't be added together, so I group by currency. Highlight,
> Execute. Data Output shows **EUR 30 refunds, 4,849.79**; **GBP 18, 2,323.47**; and **USD 62, 9,942.11**. That's 110
> refunds."

ACTION: type the comment line `-- DB totals: EUR 4849.79 | GBP 2323.47 | USD 9942.11` → **⌘S**.
SAY:
> "I'll note these totals as a comment at the bottom of the file, so I can check the spreadsheet against them later.
> The two dashes make it a comment, so it never runs. Command S to save."

ACTION: type `SELECT * FROM refund_list ORDER BY order_id, payment_id;` → triple-click → Execute.
SAY:
> "Now the export. I'll select every row of refund_list, sorted by order. Triple-click, Execute. Total rows says
> **110**."

ACTION: cursor → the toolbar right above the grid → **Save results to file** (down arrow, sixth from left) → name
`duplicate_refunds.csv`, Where: `payments-task` → **Save**.
SAY:
> "I'll move the cursor down to the small toolbar right above the result grid and click Save results to file, the
> down-arrow icon, sixth from the left, just left of the zig-zag graph icon. In the save dialog I'll name it duplicate
> underscore refunds dot csv, choose the payments-task folder in the Where menu, and click Save at the bottom-right. The
> payments operations team will load this file into the refund tool."

ACTION: **⌘S** → yellow Minimize at pgAdmin's top-left.
SAY:
> "One more Command S to save my SQL file, and I'll minimize pgAdmin with the yellow button at its top-left."

---

## Step 5: Google Sheets: import, pivot, cross-check

ACTION: Dock → Chrome → the **refund_summary** tab.
SAY:
> "Step 5. Now I'll build the summary for operations in Google Sheets. I'll move right to the Dock and click Chrome,
> the red, yellow and green circle just above pgAdmin. At the top of the window I'll click the second tab,
> refund_summary, my blank sheet."

ACTION: **File** (top-left) → **Import** → **Upload** tab → blue **Browse** → payments-task → duplicate_refunds.csv →
**Open** → Import location **Insert new sheet(s)**, keep **Convert text to numbers** ticked → green **Import data**.
SAY:
> "I'll click the File menu at the top-left and choose Import. In the dialog I'll click the Upload tab, then the blue
> Browse button. In the Finder window I'll choose payments-task in the sidebar, then duplicate_refunds.csv, and click
> Open. For Import location I'll pick Insert new sheet, so the data gets its own tab, and keep Convert text to numbers
> ticked so the amounts become numbers. Then the green Import data button."
> "A new tab, duplicate_refunds, appears at the bottom-left. I'll scroll down: the last row is **111**, so 110 refunds
> plus the header row, the same as the database."

ACTION: click **A1** → **Insert** → **Pivot table** → **New sheet** → **Create**. Editor on the right: **Rows → Add →
currency**; **Values → Add → amount** (SUM); **Values → Add → payment_id** (COUNTA).
SAY:
> "A pivot table groups and totals data without formulas. I'll click cell A1, then the Insert menu at the top and Pivot
> table. In the dialog I'll keep New sheet and click Create."
> "The pivot table editor opens on the right side. Next to Rows I'll click Add and choose currency. Next to Values I'll
> click Add and choose amount, summarized by SUM. Then Add again for payment_id, summarized by COUNTA, which counts the
> refunds."
> "The table shows **EUR 4,849.79 from 30 refunds, GBP 2,323.47 from 18, and USD 9,942.11 from 62**. I'll ignore the
> Grand Total row, because it adds three currencies together."

ACTION: click **E1** → `DB total`; E2:E4 → `4849.79`, `2323.47`, `9942.11`. **F1** → `Difference`; F2 →
`=ROUND(B2-E2,2)` → select F2:F4 → **⌘D**.
SAY:
> "Now the cross-check. In cell E1, to the right of the pivot, I'll type DB total, then the three totals from my SQL
> comment in E2 to E4, in the same order as the pivot: euros, pounds, dollars."
> "In F1 I'll type Difference, and in F2, equals ROUND of B2 minus E2, to two decimals. I round to cents because
> spreadsheets store decimals in binary and can show a tiny leftover like 0.0000000001. I'll select F2 to F4 and press
> Command D to fill down. All three are **0**: the sheet matches the database to the cent, so nothing was lost or
> changed in the export."

---

## Step 6: summary, download, stop check

ACTION: click **A7** → `Summary` → Tab → B7: `100 affected orders; refunds EUR 4849.79 (30), GBP 2323.47 (18), USD 9942.11 (62)`.
SAY:
> "Step 6. A one-line summary for operations. In cell A7 I'll type Summary, press Tab to move to B7, and type: 100
> affected orders, and the refunds per currency with their counts."

ACTION (optional, 10 s): right-click the empty **Sheet1** tab at the bottom-left → **Delete**.
SAY:
> "The first tab, Sheet1 at the bottom-left, is empty, so I'll right-click it and choose Delete. That leaves just the
> refund list and the summary."

ACTION: **File** (top-left) → hover **Download** → **Microsoft Excel (.xlsx)** → click the download arrow (top-right).
SAY:
> "To deliver it, I'll move up to the File menu at the top-left and click it, hover over Download near the middle of
> the menu, and click Microsoft Excel in the submenu on the right. A download arrow appears in Chrome's toolbar at the
> top-right. I'll click it: it lists **refund_summary.xlsx**, saved to Downloads."

**STOP CHECK: don't start the epilogue until all three are true:**
- the download list shows **refund_summary.xlsx**;
- **duplicate_refunds.csv** was saved to payments-task in Step 4;
- the SQL file was saved with ⌘S, so its tab title has no star.

SAY:
> "Before I wrap up, I'll check the deliverables. The download list shows refund_summary.xlsx. duplicate_refunds.csv
> and refund_investigation.sql are saved in the payments-task folder, and I saved the SQL file with Command S before I
> left pgAdmin."

---

## Epilogue (about 3 minutes, max 4:00; the mouse may rest, the sheet on screen)

SAY (in your own words; cover all six points):

> **Completion.** "To wrap up: the task is complete. The refund list has 110 refunds for 100 orders: 4,849.79 euros,
> 2,323.47 pounds and 9,942.11 dollars. I verified it two ways. In the database, every affected order keeps exactly one
> capture. In the sheet, the totals per currency match the database to the cent. The limitations are that this is
> synthetic data, and I haven't reconciled it with the payment processor's settlement report."

> **Approach.** "My approach was to understand before fixing. I found the affected orders, then read one order's
> attempts to see the cause, the new idempotency key on every retry, and only then wrote the refund rule."

> **Challenges.** "The tricky part was the order of operations. If I had numbered every attempt before filtering out
> failed ones, a failed first attempt would have taken number one, and the customer's only real payment would have
> been refunded."

> **Quality.** "I'm confident in the list because the check is separate from the query that built it, and the
> spreadsheet matches the database. The weak spot is anything outside this table, such as a refund someone already
> made by hand in the processor's dashboard."

> **Next time.** "Next, I'd fix the retry code so it reuses the original idempotency key, add an alert when any order
> gets two captures, and reconcile these refunds against the processor's report before sending them."

> **Insight.** "The lesson for someone less experienced: find duplicates by the business key, here the order, not by
> similar amounts. Filter before you number. And prove every customer pays exactly once before you refund anything."

SAY:
> "That completes the task. I'll move the cursor to the Dock on the right and click TaskRecorder, just below pgAdmin, to
> stop the recording."

ACTION: TaskRecorder → **Stop Recording**. Don't quit; wait for **Idle**.

---

## Bridge lines (use these instead of going silent)
- While typing a long query: *"This part filters to captured payments; next I group by order…"*
- While the import runs: *"While that loads: the CSV has one row per refund, so the operations tool can process it
  line by line."*
- Before switching apps: *"I'll move to the Dock on the right and click {{Chrome / pgAdmin}} to {{build the summary /
  check the numbers}}."*

## If something goes wrong (say it, fix it, check it)
- Syntax error: *"The Messages tab says syntax error near …; I left out {{a comma / a bracket}}. I'll fix it on line …,
  highlight the query and click Execute again… and now it works."*
- **Nothing highlighted, so the whole file ran:** *"That ran the whole file instead of my selection."* If it says
  `relation "refund_list" already exists`, say so, run `DROP TABLE refund_list;`, then rerun the CREATE TABLE on its
  own.
- The check returns rows: read them aloud, fix the list query, `DROP TABLE refund_list;`, recreate it and rerun the
  check.
- Typo in the sheet: *"In cell {{E3}} I typed {{…}}. I'll click it, retype it and press Return, and the difference in
  column F updates."*
- Anything personal, Studio or Slack on screen: **stop and re-record from the start.** Don't narrate over it.
