# Payments refund task: setup and recording run sheet

Idea: [../idea-payments-simple.md](../idea-payments-simple.md) (approved 2026-10-29). Rules: [../task-instructions.md](../task-instructions.md).
Apps: **pgAdmin 4** and **Google Sheets**. Target: **about 30 minutes** (hard window 15:00–50:59).

Files and folders:
- Input prompt: [gemini-prompt.md](gemini-prompt.md). The input lands in `payments/inputs/create_payments_db.sql`.
- Database: `payments`, owner `backend_dev`, timezone UTC. It's created and empty, waiting for the input.
- Shared folder (any macOS account can write to it): `/Users/Shared/payments-task/`. The working SQL file and the CSV
  are saved here on camera.
- After recording: `payments/outputs/` (Metadata.rtf, Deliverables.zip).

Lessons carried over from the catalog task (all four takes):
- **Used Apps** filled in TaskRecorder, and checked again right before Start.
- **What + Where narration on every click.** Name the control, say where it is, and say the cursor movement. Never use
  a bare "this" or "here".
- **Save on camera.** Press Command S after every step. Export the CSV and the .xlsx **before** the epilogue, then do
  the stop check.
- Don't paste SQL or notes into the sheet.

| Phase | What | Who | Status |
|---|---|---|---|
| A | Idea approved; check Studio's Goal | you | approved |
| B | Input file with Gemini; load and validate | you, then me | **DONE 2026-10-29: loaded, all checks pass** |
| C | Recorder account: pgAdmin, Sheets, Goal doc, practice | you | after B |
| D | Metadata.rtf, Studio fields | me + you | after B |
| E | Dry run, then reset | you, then me | before recording |
| F | Pre-flight | you | recording day |
| G | The recording | you | |
| H | Validate, Deliverables.zip, upload | me, then you | after recording |

---

## Phase A: the approved Goal

Compare Studio's approved Goal with the block below. **If it differs by even one character, Studio's version wins.**
Use it in all three places: TaskRecorder's Task Description, the Goal document, and the Metadata.rtf Request.
```
As a payments backend engineer, I will find the orders that were charged more than once during a gateway timeout in a synthetic PostgreSQL payments database and prepare their refund list using pgAdmin 4 and Google Sheets. The checkout service retried captures with new idempotency keys, so the gateway did not block the duplicates. In pgAdmin 4, I will find the affected orders, build a refund list that keeps each order's first successful capture and skips failed retries, check that every affected order keeps exactly one capture, and export the list as duplicate_refunds.csv. In Google Sheets, I will total the refunds by currency, check the totals against the database, and deliver refund_summary.xlsx for the payments operations team.
```

---

## Phase B: the input file (main account)

**B1 (you).** Open [gemini-prompt.md](gemini-prompt.md) and copy everything inside the box. In Gemini, signed in with
@mercor.expert, paste it and send. Save the SQL it returns as `Mercor/Odin/payments/inputs/create_payments_db.sql`.
Don't hand-edit it.

**B2 (me).** I load it into `payments` as `backend_dev`.

**B3 (me).** These must match exactly. A throwaway copy built to the same spec gave these numbers.

| Check | Expected |
|---|---|
| Rows / distinct orders / failed rows | 10,107 / 9,850 / 147 |
| Orders with 2+ captures, 14:00–14:30 UTC | 100 (10 with 3 captures: order ids 2010091–2010100) |
| Refund list (keep the earliest capture) | 110 refunds, 100 orders |
| Refunds per currency | EUR 30 · GBP 18 · USD 62. **Real file: EUR 4849.79 · GBP 2323.47 · USD 9942.11** |
| Exactly-one check | 0 rows |
| Number first, filter after (the trap) | 232 |

If anything is off, ask Gemini to fix that group, telling it which count is wrong. Save the new file and I'll check
again.

---

## Phase C: the Recorder account

### C1. pgAdmin 4
1. In the Object Explorer, right-click **Local Postgres 17** → **Disconnect Server**. Then right-click it again →
   **Properties** → **Advanced** tab → **DB restriction**: replace `catalog` with `payments` → **Save** → reconnect.
   The tree should now show only `payments`.
2. **Downloads prompt** (so you can name the CSV): **pgAdmin 4 menu → Settings** (or Preferences) → **Miscellaneous →
   File Downloads**. Turn on **Prompt for the download location?** and turn off **Automatically open downloaded file?**
   → Save.
3. **Practise the CSV export once** (this takes a minute; delete the test file afterwards):
   - Open a Query Tool on `payments`. Run `SELECT * FROM payments LIMIT 5;`.
   - In the toolbar just above the result grid, click **Save results to file**: the down-arrow icon, sixth from the
     left, just left of the zig-zag graph icon.
   - A save dialog should open. Name the file `test.csv`, choose `payments-task` (add `/Users/Shared/payments-task` to
     the Finder sidebar first, so it shows in the **Where** menu) → **Save**.
   - Open the file: the first line should be the column names. Delete `test.csv`.
   - **If no dialog opens** and the file lands in Downloads under another name, tell me before recording.
4. Close the Query Tool (choose **Don't save**). Collapse the tree to `payments → Schemas → public → Tables` → minimize.

### C2. Google Sheets (Chrome, @mercor.expert)
1. Reuse the **Goal Document** Google Doc: replace its text with the Goal from Phase A, and nothing else.
2. Create a new **blank** sheet and click "Untitled spreadsheet" at its top-left. Type `refund_summary` and press
   Return. The tab must read **refund_summary - Google Sheets**.
3. Practise, in a separate scratch sheet that you delete afterwards:
   - **File → Import → Upload → Browse**, then pick any CSV. Set **Import location: Insert new sheet(s)** and
     **Separator: Detect automatically**, and keep **Convert text to numbers** ticked → **Import data**.
   - Click a data cell → **Insert → Pivot table** → **New sheet** → **Create**. In the editor on the right:
     - **Rows → Add**: currency.
     - **Values → Add**: amount, summarized by SUM.
     - **Values → Add** again: payment_id, summarized by COUNTA.
   - **File → Download → Microsoft Excel (.xlsx)**, and watch for the download arrow at the top-right.
4. Delete the scratch sheet and empty Drive's trash. In Finder → Downloads, delete any old `search_*`, `test*` and
   `refund_*` files.
5. Chrome should have **two tabs only**: Goal Document and refund_summary. Close the "Continue where you left off" bar.

---

## Phase D: Metadata.rtf and Studio fields

- **Metadata.rtf (me, DONE):** it's at `payments/outputs/Metadata.rtf`:
  - Request = the Goal;
  - Topology `pgAdmin 4 (CREATE) -> Google Sheets (CREATE)`;
  - six task-description lines.

  I'll update the Topology after recording if the app order changes. It's never shown on screen and never goes in the
  zip.
- **Studio (you):**
  - Before Recording (Task Plan): tick it.
  - **Inputs Used: AI-generated file**.
  - Display: the built-in display at your recording resolution.
  - Final Notes later: `AI-generated before recording`.

---

## Phase E: dry run, then reset

1. Do Phase G once, unrecorded, timing it with the menu-bar clock. If it runs much over 35 minutes, trim the talk, not
   the steps.
2. Tell me. I'll run `DROP TABLE IF EXISTS refund_list;` and empty `/Users/Shared/payments-task/`.
3. You: delete the dry-run sheet's contents. The easiest way is to delete the sheet, create a new one and title it
   `refund_summary` again. Empty Drive's trash and clear Downloads.

---

## Phase F: pre-flight (the 10 minutes before Start)

Main account: Studio, Slack, the guidelines, Metadata.rtf and this file are closed. Switch to Recorder.

Recorder account:
- [ ] Mac on power, quiet room, **Do Not Disturb ON**.
- [ ] **One UI change** compared with the catalog recordings, for example a new wallpaper (they all used the Golden
  Gate one) or a different accent colour.
- [ ] Dock on the right side, indicators on, clock with seconds, default cursor.
- [ ] **Accessibility Inspector** running with its window closed. **Xcode quit.**
- [ ] ⌘Tab shows only pgAdmin 4, Chrome, TaskRecorder and Accessibility Inspector.
- [ ] **pgAdmin 4**: connected, tree at `payments → … → Tables` (only `payments`, **no** `refund_list`), no Query Tool
  open → minimized.
- [ ] **Chrome**: Goal Document tab + `refund_summary` tab (blank, titled) → the Goal Document tab in front.
- [ ] `/Users/Shared/payments-task/` is empty. Downloads has no `refund_*` or `duplicate_*` files.
- [ ] **TaskRecorder**: Task Description = the Goal; **Used Apps = `pgAdmin 4`, `Google Sheets`**. Look at Used Apps
  again as the very last thing before Start.

---

## Phase G: the recording (about 30 minutes)

**Screen map** (the same layout as the catalog task):
- **Dock** on the right edge. **Chrome** is the red, yellow and green circle; **pgAdmin 4** is the blue elephant just
  below it; **TaskRecorder** is just below pgAdmin.
- **Window buttons**: three circles at each window's top-left. Yellow (the middle one) is Minimize.
- **pgAdmin**:
  - **Object Explorer** down the left side.
  - **Query Tool toolbar** above the editor. The **floppy disk** (Save File), second from left, has a small down
    arrow beside it with **Save As**. **Execute** is the **white play triangle**, just right of the grey square Stop
    button.
  - **Results panel** in the lower half, with the **Data Output / Messages** tabs at its top-left. The status bar at
    the bottom shows **Total rows** and **Query complete**.
  - **Save results to file**: the down-arrow icon, sixth from the left in the toolbar right above the result grid.
- **Sheets**:
  - Title and the **File / Edit / … / Insert** menus at the top-left.
  - The **Name box** at the left end of the formula bar.
  - Sheet tabs at the bottom-left.
  - The **download arrow** in Chrome's toolbar at the top-right, after a download.

**Pattern for every click:** "I'll move the cursor [direction] to [control], the [shape or colour] in the [area], and
click it to [why]."

### Intro (under 20 s)
Goal Document visible. Click **Start Recording**, then minimize TaskRecorder.
> "I will be beginning my task soon. Here is the workflow I have in mind."

Minimize Chrome: *"I'll move to the top-left corner of the Chrome window and click the yellow Minimize button, the
middle of the three circles."*

### Step 1: find the orders charged more than once (pgAdmin, about 4 min)

DO:
1. Dock → pgAdmin.
   > "Step 1. I'll move the cursor right to the Dock on the right edge of the screen and click pgAdmin 4, the blue
   > elephant just below Chrome."
2. Object Explorer: expand `payments → Schemas → public → Tables → payments → Columns`, and move the cursor down the
   columns.
   > "On the left in the Object Explorer, I'll expand the payments database down to Tables, then the payments table and
   > its Columns. Each row is one capture attempt: an order id, a customer code, the amount and currency, a status of
   > captured or failed, the idempotency key the checkout service sent, and the time."
   > "This is a synthetic test copy of our payments table with about ten thousand rows, prepared before this session.
   > There's no real customer data in it."
3. Right-click the `payments` **database** → **Query Tool**. Then use the down arrow next to the floppy disk → **Save
   As**: name `refund_investigation.sql`, Where = `payments-task` → the blue **Save** button.
   > "I'll right-click the payments database in the tree and choose Query Tool to open an SQL editor. Before I write
   > anything, I'll save it: in the toolbar above the editor, I'll click the small down arrow right of the floppy-disk
   > Save button, choose Save As, name it refund underscore investigation dot sql, pick the payments-task folder in the
   > Where menu, and click the blue Save button at the bottom-right. The tab title at the top now shows the file name."
4. Type and run. **To run one query:** highlight the whole query, then click **Execute** and say where it is.
   For a one-line query, triple-click the line. For a longer one, drag from its first word to the semicolon. With
   nothing highlighted, pgAdmin runs the whole file, including the CREATE TABLE.
```sql
SELECT count(*) AS attempts, count(DISTINCT order_id) AS orders FROM payments;
```
EXPECT: **10,107 attempts, 9,850 orders**.
> "There are more attempts than orders. A few extra are normal, when a card is declined and the customer tries again.
> The problem is the gateway timeout between 14:00 and 14:30 UTC, so I'll look inside that window."
5. Type in two bursts, then run:
```sql
SELECT order_id, count(*) AS captures
FROM payments
WHERE status = 'captured'
  AND created_at >= '2026-10-14 14:00+00' AND created_at < '2026-10-14 14:30+00'
GROUP BY order_id
HAVING count(*) > 1
ORDER BY captures DESC, order_id;
```
EXPECT: **Total rows 100** at the bottom-left. The first 10 rows (2010091–2010100) show **3** captures; the rest show 2.
> "I count only captured rows, because a failed attempt never took money. In the status bar at the bottom-left,
> Total rows says 100: a hundred orders were charged more than once, and the first ten rows in Data Output were charged
> three times."

**⌘S** (*"Command S to save the file"*).

### Step 2: show the retry pattern on one order (about 3 min)

DO: double-click the first order id in Data Output (2010091) → ⌘C. Type, paste the id and run:
```sql
SELECT id, order_id, status, amount, currency, idempotency_key, created_at
FROM payments
WHERE order_id = 2010091
ORDER BY created_at;
```
EXPECT: **3 captured rows**, the same amount, seconds apart, **three different idempotency keys**.
> "I'll double-click the first order id in Data Output and press Command C to copy it, then paste it into the WHERE
> line with Command V. Three captures of the same order, 217.38 dollars each, within about half a minute. Now the
> idempotency_key column: every attempt has a different key. The gateway only blocks a repeat that reuses a key, so it
> treated these as three separate payments. The root cause is the retry creating a new key instead of reusing the
> original. Today's job is the cleanup."

**⌘S**.

### Step 3: build the refund list (about 6 min)

SAY before typing:
> "Step 3. The rule: number each order's successful captures by time with ROW_NUMBER, keep number one, the first
> capture, and refund number two and above. I filter to captured rows first and number them second. If I numbered every
> attempt, a failed first attempt would take number one, and I'd refund the customer's only real charge."

DO (optional, about 30 s, shows why the order matters):
```sql
SELECT count(*) AS would_refund
FROM (SELECT p.*, ROW_NUMBER() OVER (PARTITION BY order_id ORDER BY created_at, id) AS rn
      FROM payments p) c
WHERE rn > 1 AND status = 'captured';
```
EXPECT: **232**.
> "Numbering first would refund 232 payments instead of 110. The extra 122 are customers whose first attempt failed,
> and each of them would end up paying nothing."

DO: type in 2–3 bursts, run:
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
EXPECT: click the **Messages** tab at the top-left of the results panel: **SELECT 110**.
> "The Messages tab, top-left of the results panel, says SELECT 110: one refund for each of the 90 double charges and
> two for each of the 10 triple charges. The id breaks ties if two captures share a timestamp."

**⌘S**.

### Step 4: check, total, export (about 5 min)

DO:
1. Type and run the check:
```sql
SELECT p.order_id, count(*) - count(r.payment_id) AS captures_left
FROM payments p
LEFT JOIN refund_list r ON r.payment_id = p.id
WHERE p.status = 'captured'
  AND p.order_id IN (SELECT order_id FROM refund_list)
GROUP BY p.order_id
HAVING count(*) - count(r.payment_id) <> 1;
```
EXPECT: **0 rows**.
> "For every affected order, its captures minus its planned refunds must be exactly one. This query lists any order
> where that isn't true. Data Output is empty and Total rows says zero, so every customer ends up paying exactly once."
2. Totals:
```sql
SELECT currency, count(*) AS refunds, sum(amount) AS refund_total
FROM refund_list
GROUP BY currency
ORDER BY currency;
```
EXPECT: EUR 30, GBP 18, USD 62 refunds, with your amounts.
> "I total per currency, because euros, pounds and dollars can't be added together."

Type a comment line under it with the numbers on screen. With this data they are `-- DB totals: EUR 4849.79 | GBP 2323.47 | USD 9942.11`.
Then **⌘S**.
3. Export:
```sql
SELECT * FROM refund_list ORDER BY order_id, payment_id;
```
EXPECT: Total rows **110**. Then click **Save results to file** in the toolbar right above the grid (down arrow, sixth
from left) → name `duplicate_refunds.csv`, Where = `payments-task` → **Save**.
> "I'll move the cursor to the toolbar just above the result grid and click Save results to file, the down-arrow icon,
> sixth from the left. In the save dialog I'll name it duplicate underscore refunds dot csv, choose the payments-task
> folder in the Where menu, and click Save at the bottom-right. That's the file operations will feed to the refund
> tool."

**⌘S** once more, then minimize pgAdmin (yellow button, top-left of its window).

### Step 5: Google Sheets, import, pivot, cross-check (about 7 min)

DO:
1. Dock → Chrome → the `refund_summary` tab at the top.
   > "Step 5. I'll move right to the Dock and click Chrome, the red, yellow and green circle just above pgAdmin. At the
   > top of the window I'll click the second tab, refund_summary, my blank sheet."
2. **File** (top-left) → **Import** → the **Upload** tab → blue **Browse** button → `payments-task` →
   `duplicate_refunds.csv` → **Open**. Set **Import location: Insert new sheet(s)** and keep **Convert text to
   numbers** ticked → the green **Import data** button.
   EXPECT: a new tab `duplicate_refunds` at the bottom-left, with **111 rows** (a header plus 110).
   > "Row 111 is the last one: 110 refunds plus the header, the same as the database."
3. Click A1 → **Insert** menu → **Pivot table** → **New sheet** → **Create**. In the pivot editor on the right:
   **Rows → Add → currency**; **Values → Add → amount** (SUM); **Values → Add → payment_id** (COUNTA).
   EXPECT: EUR / GBP / USD rows with SUM and COUNTA, plus a Grand Total row.
   > "In the pivot table editor on the right side, under Rows I'll click Add and pick currency. Under Values I'll add
   > amount, summarized by SUM, then payment_id, summarized by COUNTA."
4. Cross-check: E1 `DB total`, then E2:E4 typed from your comment line (in the pivot's order: EUR, GBP, USD). F1
   `Difference`, F2 `=ROUND(B2-E2,2)` → select F2:F4 → **⌘D**. (Rounding hides tiny leftovers like 1E-12, which
   Sheets can show when it subtracts decimal numbers.)
   EXPECT: **0** in all three.
   > "Each currency's total in the sheet minus the database total. All three are zero, so nothing was lost in the export.
   > I ignore the Grand Total row because it mixes currencies."

### Step 6: summary and download (about 2 min)

DO:
1. A7 `Summary`, B7 `100 affected orders; refunds EUR 4849.79 (30), GBP 2323.47 (18), USD 9942.11 (62)`.
   Optional: right-click the empty **Sheet1** tab → **Delete**. Reference layout:
   [reference/refund_summary-reference.xlsx](reference/refund_summary-reference.xlsx). It's Claude-made, so never
   import it. All the queries in order: [queries-in-order.sql](queries-in-order.sql).
2. **File → Download → Microsoft Excel (.xlsx)** → point at the download arrow at the top-right → click it to show
   `refund_summary.xlsx`.
   > "I'll move up to the File menu at the top-left, hover over Download and click Microsoft Excel. The download arrow
   > at the top-right of Chrome now lists refund_summary.xlsx."

**STOP CHECK (say it, point at each one):**
> "Before I wrap up, I'll check the deliverables. The sheet tab at the top says refund_summary, and the download list
> shows refund_summary.xlsx. duplicate_refunds.csv and refund_investigation.sql are saved in the payments-task folder,
> and the SQL file was saved with Command S, so its tab title has no star."

### Epilogue (about 3 min, max 4:00; the mouse may rest)
In your own words, covering all six points with your real numbers:
1. **Completion:** 110 refunds for 100 orders. Every affected order keeps exactly one capture (0 rows), and the sheet
   matches the database per currency. Limitations: synthetic data, and not reconciled with the processor's
   settlement report.
2. **Approach:** I found the affected orders first, read one order's attempts to understand the cause, then wrote the
   rule.
3. **Challenges:** the order of operations. Numbering before filtering would have refunded 122 customers' only payment.
4. **Quality:** I'm confident, because the check is independent of the query that built the list. The weak spot is
   refunds made outside this table.
5. **Next time:** fix the retry so it reuses the idempotency key, add an alert for an order with two captures, and
   reconcile with the processor.
6. **Insight:** deduplicate on the business key (the order), filter before you number, and prove each customer pays
   exactly once before refunding.

> "That completes the task. I'll move to the Dock on the right and click TaskRecorder, just below pgAdmin, to stop the
> recording."

Click **Stop Recording**. Don't quit; wait for **Idle**.

### If something goes wrong (say it, fix it, check it)
- A typo error: *"The Messages tab says syntax error near …; I'll fix the spelling on line … and run it again."*
- The check returns rows: read them aloud. The list query is different from the one above. Fix it, run
  `DROP TABLE refund_list;`, recreate it and rerun the check.
- `relation "refund_list" already exists`: run `DROP TABLE refund_list;` and recreate it.

---

## Phase H: after recording
1. Wait for Idle → **Show Recordings** → copy the newest `recording_…` folder and `.zip`, unchanged, into
   `/Users/Shared/payments-task/`. Copy `refund_summary.xlsx` from Downloads into `/Users/Shared/payments-task/` too.
2. Tell me. I check everything as I did for the catalog take 4, then build `payments/outputs/Deliverables.zip` and
   finalize Metadata.rtf. The zip holds:
   - `input 1.sql` (create_payments_db.sql);
   - `artifact 1.sql` (refund_investigation.sql);
   - `artifact 2.csv` (duplicate_refunds.csv);
   - `final output 1.xlsx` (refund_summary.xlsx).
3. You upload Metadata.rtf, video.mp4, the recording zip (unmodified) and Deliverables.zip. Run both AutoQCs, do the
   checks, set Final Notes to `AI-generated before recording`, and submit.
