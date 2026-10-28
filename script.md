# Narration script: task 33g7c3d6 v3, take 3 (catalog search, pg_trgm GIN vs GiST, decision in Sheets)

Goes with [task-steps.md](task-steps.md) Phase H. About 38 to 42 minutes in total. The take-2 script is archived as
[script-take2.md](script-take2.md).

**Why take 3.** Review #1 sent take 2 back for two reasons. First, the narration failed the eyes-closed test: it said
"the yellow icon over here", "the save icon over here", "copy this" and "this walnut", and clicked pgAdmin in the
Dock and ran queries again and again without saying where anything was. Second, Used Apps was empty. This script
fixes the first problem: **every action says What + Where (+ Why), and every cursor movement is spoken.**

## How to use this script
- **Rehearse with it; don't read it on camera.** Recited narration sounds robotic. Learn the screen map and the
  pattern below, then say it in your own words. Only the intro sentence must be word for word.
- **Keep it off the screen while recording.** Use your phone, an iPad or a printout.
- `ACTION` = what your hands do. `SAY` = what you say while doing it. `{{…}}` = read the real number off the screen
  (the dry-run value is a guide; never say a number you didn't see).
- **Say every keyboard shortcut out loud** as you press it. Prefer clicking the toolbar button and saying where it is.
- **No gap over 45 seconds. No typing burst over 45 seconds.**

### The eyes-closed pattern (use it for every click)
> **"I'll move the cursor** [direction] **to** [named control], **the** [shape or colour] **in the** [screen area],
> **and click it** [to do what / why]**."** Then say what changed and where it shows.

Example from the reviewer: *"I will now move the cursor right towards the Dock, which is on the right of the screen,
and click on the Finder app, which is the very first app from the top of the Dock, to open it."*

### Banned words: say the name and the place instead
| Don't say | Say |
|---|---|
| "the yellow icon over here" | "the yellow Minimize button, the middle of the three circles at the top-left corner of the Chrome window" |
| "click pgAdmin" (no place) | "the pgAdmin 4 icon, the blue elephant, in the lower part of the Dock on the right edge of the screen" |
| "the save icon over here" | "the Save File button, the floppy-disk icon, second from the left in the toolbar above the editor" |
| "I have saved it" | "I'll click the blue Save button at the bottom-right of the dialog. The tab title at the top of the editor now reads search_measurements.sql, so it's saved." |
| "copy this" | "I'll triple-click line 1, the walnut query, to highlight the whole line, and press Command C to copy it" |
| "this walnut" | "on line 3, I'll double-click the word walnut inside the quotes" |
| "select this and click execute" | "I'll triple-click line 5 to highlight the Q X query, then move up to the toolbar and click Execute, the white play triangle just right of the square Stop button" |
| (running again in silence) | "Run two: I'll move back up to the Execute button, the play triangle in the toolbar, and click it again" |
| "it says here" | "in the status bar at the bottom-left of the results panel, next to Total rows, it says Query complete …" |

---

## Screen map (learn this before recording; check it once on the real screen)

Positions are from take 2. The Dock order changes when an app is quit, so look at the Dock once before Start.

**macOS**
- **Dock**: right edge of the screen. **Chrome** (red, yellow and green circle) and **pgAdmin 4** (blue elephant)
  are in the lower part, pgAdmin just below Chrome. TaskRecorder is just below pgAdmin.
- **Window buttons**: three circles at the **top-left corner** of every window: red Close (left), yellow Minimize
  (middle), green Zoom (right; hold it for the Tile menu).
- **Menu bar**: across the very top. The clock is at its right end.

**pgAdmin 4** (tiled to the left half)
- **Object Explorer**: the panel down the **left side**. The tree is Servers → Local Postgres 17 → Databases → catalog →
  Schemas → public → Tables → products → Indexes.
- **Tab row**: across the top of the right-hand area. The Query Tool tab is the **last tab, on the right**, and its title
  is the open file's name.
- **Query Tool toolbar**: the row of icons just under the tab row, **from left to right**:
  - Open File (folder);
  - **Save File** (floppy disk), with a small **down arrow** next to it that holds **Save As**;
  - Edit;
  - Filter;
  - the "No limit" box;
  - **Stop** (grey square);
  - **Execute** (white **play triangle**, F5);
  - a small down arrow;
  - Explain (letter E);
  - Explain Analyze;
  - Commit and Rollback;
  - Macros;
  - Help (question mark, far right).
- **Editor**: the middle of the right-hand area, with **line numbers down its left edge**.
- **Results panel**: the lower half. Its tabs **Data Output**, **Messages** and **Notifications** are at its
  **top-left**.
- **Status bar**: the bottom edge of the results panel. **Total rows** is at the **bottom-left**, and **Query
  complete** with the time is just to its right.

**Chrome / Google Sheets** (tiled to the right half)
- **Browser tabs** across the very top: **Goal Document** on the left, **search_benchmark** to its right.
- **Sheet title** at the top-left, with the **menu row** under it: File, Edit, View, Insert, Format, Data, Tools,
  Extensions, Help.
- **Name box**: the small box at the **left end of the formula bar**, under the toolbar. It shows the cell address,
  for example E2. The **formula bar** (fx) is to its right.
- **Column letters** run along the top of the grid, and **row numbers** run down its left edge.
- **Sheet1 tab**: at the **bottom-left**.
- **Download indicator**: after a download, a **download arrow icon** appears in Chrome's toolbar at the **top-right**,
  left of the profile button. Never use the Downloads stack in the Dock.

---

| Section | Target | Clock at end (about) |
|---|---|---|
| Intro | 0:20 | 0:20 |
| 1. Baseline searches | 4:30 | 4:50 |
| 2. Read the plans | 4:30 | 9:20 |
| 3. Time each term three times | 4:30 | 13:50 |
| 4. Sheets: baseline | 4:00 | 17:50 |
| 5. GIN index | 7:00 | 24:50 |
| 6. GiST index | 6:00 | 30:50 |
| 7. Sheets: compare and decide | 6:00 | 36:50 |
| Epilogue | 3:30 | 40:20 |

If you're past **47:00** at the epilogue, shorten it, but still cover all six points. The hard limit is 50:59.

---

## Intro (under 20 seconds, exact words)

ACTION: Goal document visible behind TaskRecorder. **Check Used Apps shows `pgAdmin 4` and `Google Sheets`.** Click
**Start Recording**, then minimize TaskRecorder at once.

SAY (exactly):
> "I will be beginning my task soon. Here is the workflow I have in mind."

ACTION: wait 2 to 3 seconds. Move to the top-left of the Chrome window → yellow Minimize button.
SAY:
> "I'll move the cursor up to the top-left corner of the Chrome window and click the yellow Minimize button, the
> middle of the three circles, to put the Goal document away."

---

## Step 1: baseline searches in pgAdmin 4

ACTION: cursor → Dock (right edge) → pgAdmin 4 elephant icon → click.
SAY:
> "Step 1. I'll move the cursor right to the Dock on the right edge of the screen. In the lower part of the Dock,
> just below the Chrome icon, is pgAdmin 4, the blue elephant icon. I'll click it to bring pgAdmin to the front. It's
> already connected to my local PostgreSQL 17 server."

ACTION: point down the Object Explorer tree to `products` → `Indexes` → the two indexes.
SAY:
> "On the left side of the window is the Object Explorer. I'll move the cursor down the tree: the catalog database,
> Schemas, public, Tables, then the products table. Under products I'll click the arrow next to Indexes to expand
> it. There are two indexes: products_pkey on the id column, and products_name_idx, a B-tree index on name that the
> team added earlier to speed up search."

ACTION: cursor → editor (centre right), trace the query on line 1.
SAY:
> "Now I'll move the cursor right to the Query Tool in the middle of the window. The tab at the top-right says
> catalog_search.sql, the query our product-search API runs. On line 1 it selects id, name and price from products
> where name ILIKE percent, the search term, percent, ordered by id, limited to 50 rows. ILIKE makes the match
> case-insensitive, and the percent signs on both sides mean the term can appear anywhere in the name."

SAY (first-use description of the prepared data; required; never name a tool):
> "The catalog is a synthetic test database of 500,000 generated product names, prepared before this session. It
> contains no real customer data and nothing copyrighted."

ACTION: toolbar → small down arrow right of the floppy disk → **Save As** → Where = `catalog-task` → name
`search_measurements.sql` → **Save**. Point at the tab title.
SAY:
> "Before I change anything, I'll save a working copy so the original file stays untouched. In the toolbar above
> the editor, the second icon from the left is the Save File button, a floppy disk. I'll click the small down arrow
> just to its right and choose Save As from the menu."
> "A save dialog opens in the middle of the screen. In the Save As box at the top I'll type search underscore
> measurements dot sql. In the Where drop-down below it I'll choose the catalog-task folder. Then I'll click the
> blue Save button at the bottom-right of the dialog."
> "The tab title at the top right of the editor now reads search_measurements.sql, so the working copy is saved and
> this file will hold my measurements."

SAY:
> "Users say search is slow, so I'll test three kinds of search term. A rare term, walnut, in only a handful of
> products. A common term, steel, in about a quarter of the catalog. And a very short term, the two letters Q X,
> because real users type short fragments."

ACTION: triple-click line 1 → ⌘C → click end of line 1 → Return → ⌘V → Return → ⌘V.
SAY:
> "I'll move the cursor to line 1 in the editor and triple-click it to highlight the whole walnut query, then press
> Command C to copy it. I'll click at the end of line 1, after the semicolon, press Return for a new line and press
> Command V to paste a copy on line 2, then Return and Command V again for a third copy on line 3."

ACTION: line 2 → double-click `walnut` → type `steel`; line 3 → double-click `walnut` → type `qx`.
SAY:
> "On line 2, I'll double-click the word walnut inside the quotes to select it and type steel. On line 3, I'll
> double-click walnut inside the quotes again and type Q X."

ACTION: triple-click line 1 → cursor up to the toolbar → **Execute** (play triangle) → point at the status bar.
SAY:
> "To run only the walnut query, I'll triple-click line 1 to highlight it. Then I'll move the cursor up to the
> toolbar and click Execute, the white play triangle just to the right of the square Stop button. Its shortcut is F5.
> Running only the highlighted line matters: with nothing highlighted, pgAdmin would run every statement in the
> file."
> "The rows appear in the Data Output tab in the lower half of the window. In the status bar at the bottom-left,
> Total rows says 50, and just to its right, Query complete says about {{70}} milliseconds."

ACTION: line 2 → triple-click → Execute; line 3 → triple-click → Execute.
SAY:
> "Next, steel. I'll triple-click line 2 and click the Execute play triangle in the toolbar again. Total rows at the
> bottom-left says 50, and Query complete is almost instant."
> "And Q X. I'll triple-click line 3 and click Execute in the toolbar. Total rows says only {{40}}, because fewer
> than 50 products contain Q X, and it takes about {{70}} milliseconds."
> "So the rare search and the short search are slow, and the common search is fast. That's the opposite of what you
> might expect, and the execution plans will show why."

ACTION (optional): type the `count(*)` line on line 4 → triple-click → Execute.
SAY:
> "To put a number on common, I'll add a count query on line 4, highlight it and click Execute. In Data Output,
> the count column shows {{125,000}} products contain steel."

---

## Step 2: read the plans

ACTION: click at the very start of line 1 → type `EXPLAIN (ANALYZE, BUFFERS) ` → triple-click line 1 → Execute.
SAY:
> "Step 2. I'll read the execution plan for walnut. I'll click at the very start of line 1, before the word SELECT,
> and type EXPLAIN, open bracket, ANALYZE, comma, BUFFERS, close bracket. EXPLAIN ANALYZE actually runs the query and
> reports what happened, and BUFFERS adds how many 8-kilobyte pages it touched."
> "I'll triple-click line 1 and click Execute, the play triangle in the toolbar."

ACTION: cursor → Data Output (lower half) → start at the most indented row and move upward.
SAY:
> "The plan appears in the Data Output tab in the lower half, one plan line per row. I'll move the cursor down to the
> most indented row near the bottom of the plan and read upwards. At the bottom is a Parallel Seq Scan on products.
> That means PostgreSQL reads every row, split across the main process and two workers. Moving up: a Sort on id,
> then Gather Merge, which combines the three sorted streams, and Limit at the top, which keeps the first 50."

ACTION: point at `loops=3`, `Rows Removed by Filter`, `Buffers`.
SAY:
> "On the Parallel Seq Scan row, at the right end, it says loops equals three, so the numbers are per process and I
> multiply by three. Two rows below, Rows Removed by Filter is about {{166,617}}, so roughly 499,850 rows were checked
> and thrown away to find 150 matches. The next row, Buffers shared hit {{4,896}}, is every page of the table, all
> from memory, so this is pure CPU work."

SAY (the key *why*):
> "Notice that products_name_idx doesn't appear anywhere in the plan. A B-tree keeps names sorted from the first
> character, like a phone book sorted by surname, so it's great for names that start with something. But walnut can
> appear anywhere in the name. With a wildcard at the front the sorted order doesn't help, so the planner ignores
> that index and reads the whole table."

ACTION: line 2 → add the prefix → triple-click → Execute → point at the top plan rows.
SAY:
> "For comparison, steel. I'll click at the start of line 2, type the same EXPLAIN prefix, triple-click the line and
> click Execute in the toolbar. In Data Output the second row is an Index Scan using products_pkey, the primary key,
> with the same filter. Because a quarter of the products contain steel, walking the table in id order finds 50
> matches after about 200 rows. A few rows down, Rows Removed by Filter is just {{150}} and Buffers just {{5}}. The
> LIMIT is doing the work."

---

## Step 3: time each term three times

ACTION: line 3 → add the prefix. Typing it is fine (short); say it.
SAY:
> "Step 3. One run on its own is noisy, so I'll run each search three times and compare medians. First I'll click at
> the start of line 3, the Q X query, and type the same EXPLAIN prefix."

ACTION: triple-click line 1 → Execute three times → point at the last row each time.
SAY:
> "Walnut. I'll triple-click line 1 and click Execute, the play triangle in the toolbar. I'll scroll to the bottom of
> Data Output: the last row, Execution Time, is the time spent inside the database, without drawing results on
> screen. Run one: {{…}} milliseconds."
> "Run two: I'll move back up to the Execute button in the toolbar and click it again. The last row in Data Output
> says {{…}}."
> "Run three: Execute again, at the top. {{…}} milliseconds."

ACTION: click the empty line under the queries → type `-- no index | walnut: __, __, __`.
SAY:
> "I'll click on the empty line below the queries, near the bottom of the editor, and type a comment with those three
> timings. The two dashes make it a comment, so it never runs."

ACTION: the same for steel (line 2) and qx (line 3), each with a comment line.
SAY (shorter now that the pattern is set, but still say where):
> "Now steel. I'll triple-click line 2 and click Execute in the toolbar three times, reading Execution Time on the
> last row of Data Output each time: {{…}}, {{…}} and {{…}}, well under a millisecond. I'll add a comment line under
> the walnut one."
> "And Q X. I'll triple-click line 3 and click Execute three times: {{…}}, {{…}} and {{…}}. As slow as walnut, because
> it's rare too, so it also reads the whole table. One more comment line."

ACTION: toolbar → Save File (floppy disk) click.
SAY:
> "To save my notes, I'll move up to the Save File button, the floppy disk second from the left in the toolbar, and
> click it. The star after the file name in the tab title disappears, which tells me it's saved."

---

## Step 4: Google Sheets, baseline

ACTION: Dock → Chrome → the `search_benchmark` tab.
SAY:
> "Step 4. I'll record these numbers in Google Sheets so I can compare all three setups side by side. I'll move the
> cursor right to the Dock and click the Chrome icon, the red, yellow and green circle, just above pgAdmin. Chrome
> opens on the right half of the screen. At the top of the window I'll click the second browser tab,
> search_benchmark, my blank sheet."

ACTION: click A1 → type headers with Tab: `Term`, `No index run 1`, `No index run 2`, `No index run 3`,
`No index median`.
SAY:
> "I'll click cell A1, the top-left cell of the grid, under column letter A. I'll type Term, then press Tab to move
> one cell right to B1, and type No index run 1. Tab again for C1, run 2, Tab for D1, run 3, and Tab for E1, No
> index median."

ACTION: click A2 → `walnut (rare)` Return `steel (common)` Return `qx (two-letter)`.
SAY:
> "I'll click cell A2, in column A one row down, and type walnut, rare. Return moves down to A3, steel, common. Return
> again for A4, Q X, two-letter."

ACTION: click B2 → enter nine numbers, reading from pgAdmin on the left.
SAY (between short bursts):
> "Now the timings from my notes. pgAdmin is still open on the left half, so I can read the comment lines in the
> editor. I'll click cell B2 and type walnut's three runs, pressing Tab between them: {{…}}, {{…}}, {{…}}. Then cell
> B3 for steel… and cell B4 for Q X…"

ACTION: click E2 → `=MEDIAN(B2:D2)` → Return → drag-select E2:E4 → ⌘D.
SAY:
> "I'll click cell E2, under No index median, and type equals MEDIAN, open bracket, B2 colon D2, close bracket, then
> press Return. To copy the formula down, I'll click E2 and drag down to E4 to highlight the three cells, then press
> Command D, which fills down. The medians with no index are walnut {{70}}, steel {{0.2}} and Q X {{68}}
> milliseconds. So the problem is rare terms, not every search."

---

## Step 5: GIN trigram index

ACTION: Dock → pgAdmin → click the empty line under the comments → type `CREATE EXTENSION pg_trgm;` →
triple-click → Execute → **Messages** tab.
SAY:
> "Step 5. I'll go back to pgAdmin to try the first fix. I'll move the cursor right to the Dock and click the
> pgAdmin elephant icon, below Chrome. In the editor I'll click the empty line under my comments and type CREATE
> EXTENSION pg underscore trgm."
> "Trigram indexes come from the pg_trgm extension, which ships with PostgreSQL but isn't enabled in this database
> yet. I'll triple-click that line and click Execute in the toolbar. Then I'll click the Messages tab at the top-left
> of the results panel, next to Data Output. It says CREATE EXTENSION, so it's enabled."

SAY (the concept):
> "pg_trgm splits text into three-character pieces called trigrams. For walnut those are W-A-L, A-L-N, L-N-U and
> N-U-T. If an index knows which rows contain each trigram, PostgreSQL can look up those four pieces and check only
> the rows that have all of them, instead of reading the whole table."
> "Two index types can store trigrams, GIN and GiST. Rather than guess, I'll build and measure both. First GIN, a
> generalized inverted index. It works like the index at the back of a book: for each trigram, a list of the rows
> that contain it."

ACTION: next line → type the GIN `CREATE INDEX` → triple-click → Execute → Messages tab.
SAY:
> "On the next line I'll type CREATE INDEX products underscore name underscore trgm underscore gin, on products,
> using gin, on the name column with gin underscore trgm underscore ops. That operator class tells it to index the
> name's trigrams, not the whole value. I'll triple-click the line and click Execute in the toolbar."
> "In the Messages tab at the top-left of the results panel, it says the query returned successfully in {{2}}
> seconds. That's the build time, so I'll add it as a comment at the end of the line."

ACTION: next line → `SELECT pg_size_pretty(pg_relation_size('products_name_trgm_gin'));` → triple-click → Execute →
Data Output.
SAY:
> "Next, the size. On the next line I'll type SELECT pg_size_pretty of pg_relation_size of the GIN index name, then
> triple-click it and click Execute. I'll click the Data Output tab at the top-left of the results panel: the single
> cell says {{26}} megabytes."

ACTION: triple-click line 1 (walnut EXPLAIN) → Execute.
SAY:
> "Now walnut again with the index in place. I'll scroll up to line 1 in the editor, triple-click it and click
> Execute. In Data Output, the plan now has a Bitmap Index Scan on products_name_trgm_gin, which finds the candidate
> rows, and above it a Bitmap Heap Scan that fetches only those rows. The Recheck Cond row matters: the index knows
> which rows contain all four trigrams, but not whether they're next to each other in the right order, so
> PostgreSQL checks each candidate against the real condition. The last row, Execution Time, is about {{0.7}}
> milliseconds, compared with {{70}} before."

ACTION: line 2 → Execute.
SAY:
> "Steel: I'll triple-click line 2 and click Execute. It still uses the primary-key Index Scan on the top rows, and
> that's the right call. With 125,000 matches, using the trigram index would cost more than walking the table until
> 50 turn up. The planner only uses an index when it's cheaper."

ACTION: line 3 → Execute.
SAY:
> "Q X: triple-click line 3, Execute. The bottom of the plan still shows a Parallel Seq Scan. Two letters don't make
> up a single trigram, so the index has nothing to look up, and the planner knows not to use it."

ACTION: each line three times (triple-click → Execute ×3) → `-- GIN |` comment lines.
SAY:
> "Now the three timed runs with GIN. Walnut: line 1, Execute in the toolbar, three times, reading Execution Time on
> the last row of Data Output: {{…}}, {{…}}, {{…}}. Steel: line 2, Execute three times: {{…}}… Q X: line 3, three
> more: {{…}}… I'll type them as GIN comment lines under the queries."

ACTION: `DROP INDEX products_name_trgm_gin;` → triple-click → Execute → Save File button.
SAY:
> "On a new line I'll type DROP INDEX products underscore name underscore trgm underscore gin, triple-click it and
> click Execute. I'm dropping it so it can't affect the GiST test. Messages says DROP INDEX. Then I'll click the Save
> File floppy disk, second from the left in the toolbar, to save my notes."

---

## Step 6: GiST trigram index

ACTION: next line → GiST `CREATE INDEX` → triple-click → Execute → Messages tab.
SAY (while it builds; use this time to talk):
> "Step 6. On a new line I'll type the same CREATE INDEX, but named products underscore name underscore trgm
> underscore gist, using gist, with gist underscore trgm underscore ops. I'll triple-click it and click Execute in the
> toolbar."
> "While it builds: GiST is a generalized search tree. Instead of a list per trigram, it stores a compressed
> signature of each name's trigrams in a balanced tree. Those signatures are lossy, so it usually needs more
> rechecking than GIN. But GiST can also order results by similarity, which would matter if we later added 'did you
> mean' style fuzzy search."
> "The Messages tab at the top-left of the results panel says {{3}} seconds, about one and a half times as long as
> GIN. I'll add that as a comment."

ACTION: size query for `products_name_trgm_gist` → Execute → Data Output.
SAY:
> "On the next line, the same size query with the GiST index name. Triple-click, Execute, then the Data Output tab at
> the top-left of the results: {{79}} megabytes, about three times the GIN index."

ACTION: line 1 → Execute.
SAY:
> "Walnut: line 1, Execute. In Data Output there's a Bitmap Index Scan on the GiST index, and the last row says about
> {{30}} milliseconds. Much better than {{70}} with no index, but much slower than GIN's {{0.7}}. A few rows up, Rows
> Removed by Index Recheck shows the lossy signatures at work."

ACTION: line 2 → Execute.
SAY:
> "Steel: line 2, Execute. The top rows show the same primary-key Index Scan as before."

ACTION: line 3 → Execute → point at `Rows Removed by Index Recheck`.
SAY (the key finding):
> "Q X: line 3, Execute. This is the interesting one. In Data Output, the planner did choose the GiST index this
> time, and the last row says {{170}} milliseconds, more than double the {{68}} with no index. I'll point at the
> Rows Removed by Index Recheck row: {{499,960}}. With no trigram to match, the index can't rule anything out, so it
> returned every row as a candidate and every row had to be rechecked. So this GiST index would make short searches
> slower."

ACTION: three timed runs per line → `-- GiST |` comment lines → `DROP INDEX products_name_trgm_gist;` → Execute →
Save File.
SAY:
> "Three timed runs with GiST. Line 1, Execute three times: {{…}}… line 2: {{…}}… line 3: {{…}}… I'll type them as GiST
> comment lines. Then on a new line, DROP INDEX for the GiST index, triple-click, Execute, and Messages says DROP INDEX.
> Finally, I'll click the Save File floppy disk in the toolbar."

---

## Step 7: Google Sheets, compare and decide

ACTION: Dock → Chrome.
SAY:
> "Step 7. I'll move right to the Dock and click the Chrome icon to go back to the sheet, compare all three setups
> and decide."

ACTION: click F1 → headers across to M1 with Tab: `GIN run 1`, `GIN run 2`, `GIN run 3`, `GIN median`,
`GiST run 1`, `GiST run 2`, `GiST run 3`, `GiST median`.
SAY:
> "I'll click cell F1, to the right of No index median in row 1, and type GIN run 1, then press Tab to move right.
> Run 2, Tab, run 3, Tab, GIN median, Tab. Then the same four headers for GiST, ending at M1."

ACTION: click F2 → GIN timings in F2:H4; click J2 → GiST timings in J2:L4.
SAY:
> "Now the timings from the comment lines in pgAdmin on the left. I'll click cell F2 and type GIN's three walnut
> runs with Tab between… then F3 for steel and F4 for Q X. Then I'll click cell J2 for the GiST runs…"

ACTION: drag-select E2:E4 → ⌘C → click I2 → ⌘V → click M2 → ⌘V.
SAY:
> "For the medians, I'll drag from E2 down to E4 to highlight the no-index median column and press Command C to copy
> it. Then I'll click cell I2, under GIN median, and press Command V to paste, and click cell M2, under GiST median,
> and press Command V again. Sheets moves the formula to the new columns by itself: clicking I2, the formula bar at
> the top shows MEDIAN of F2 to H2."

ACTION: N1 `GIN speedup (x)`, O1 `GiST speedup (x)`; N2 `=E2/I2`, O2 `=E2/M2` → drag-select N2:O4 → ⌘D.
SAY:
> "Speedup is the no-index median divided by the indexed median. I'll click cell N1 and type GIN speedup, Tab, and in
> O1, GiST speedup. In N2 I'll type equals E2 divided by I2, Tab, and in O2 equals E2 divided by M2, then Return. I'll
> drag from N2 to O4 to highlight both columns and press Command D to fill down."
> "Walnut is about {{100}} times faster with GIN and {{2}} times with GiST. Steel is about 1 with both, so no change.
> For Q X, GIN is about 1 and GiST is {{0.4}}. Below one means slower, so GiST makes short searches more than twice
> as slow."

ACTION: A6 `Index`, B6 `Size (MB)`, C6 `Build time (ms)`; A7 `GIN` + numbers; A8 `GiST` + numbers.
SAY:
> "Below the timings, a small cost table. I'll click cell A6 and type Index, Tab, Size in megabytes, Tab, Build time
> in milliseconds. In A7, GIN: {{26}} megabytes and {{2,000}} milliseconds. In A8, GiST: {{79}} megabytes and {{3,100}}
> milliseconds."

ACTION: A10 `Decision`, B10 your decision with the reason. A11 `Min search length`, B11 `3 characters`.
SAY (adapt to what you measured):
> "I'll click cell A10 and type Decision, then Tab to B10 and type my choice: {{GIN}}. It gave the fastest rare-term
> search, the smallest index and the fastest build. GiST's one advantage, similarity ranking, isn't something this
> search uses. In A11 I'll type Min search length, and in B11, 3 characters, because neither index helps two-letter
> searches and GiST makes them slower."

ACTION: File menu (top-left) → Download → Microsoft Excel (.xlsx) → point at the download arrow (top-right).
SAY:
> "To export the deliverable, I'll move the cursor up to the File menu at the top-left, under the sheet title, and
> click it. I'll hover over Download near the middle of the menu, and in the submenu that opens on the right, click
> Microsoft Excel, dot x l s x."
> "A download arrow icon appears in Chrome's toolbar at the top-right, just left of the profile button. I'll click it:
> it lists search_benchmark.xlsx, saved to my Downloads folder. That's the deliverable for my team's code review.
> I'll click on the sheet to close that list."

---

## Epilogue (about 3½ minutes, max 4:00; the mouse may rest, the sheet on screen)

SAY (in your own words; cover all six points, using your real numbers):

> **Completion.** "To wrap up: the task is complete. With the GIN trigram index, the rare-term search goes from about
> {{70}} milliseconds to {{0.7}}. I verified it three ways: the plan shows a Bitmap Index Scan on the trigram index,
> I compared medians of three runs rather than single timings, and the numbers in the sheet match my notes in
> pgAdmin. The main limitations are synthetic data on one laptop with a warm cache, and I haven't measured the extra
> cost the index adds to inserts and updates."

> **Approach.** "My approach was to diagnose before fixing. The plan showed that the existing B-tree couldn't help a
> leading-wildcard search, which pointed to trigram indexes. Then, instead of assuming GIN was better, I built both
> GIN and GiST and measured speed, size and build time against three kinds of term."

> **Challenges.** "The most surprising part was the two-letter search. With GiST, the planner chose the index and it
> ended up slower than having no index, because it had to recheck every row. It was also interesting that the common
> term never needed an index, because the LIMIT finds 50 matches almost immediately."

> **Quality.** "I'm confident in the choice for this workload: GIN was faster, smaller and quicker to build. The
> weaknesses are the extra storage and write overhead, and very short searches stay slow, which is why the
> recommendation includes a three-character minimum."

> **Next time.** "Next, I'd create the chosen index in production with CREATE INDEX CONCURRENTLY, so writes to the
> table aren't blocked while it builds, prove the search results are exactly the same as before, and measure insert
> and update performance with realistic search terms from real query logs."

> **Insight.** "The key lesson for anyone less experienced: an index doesn't help every query. A wildcard at the
> start defeats a normal B-tree, and very short terms defeat trigram indexes. So always read the execution plan, and
> test different kinds of input, not just the one search you were asked about."

SAY:
> "That completes the task. I'll move the cursor to the Dock on the right and click the TaskRecorder icon, just below
> pgAdmin, to stop the recording."

ACTION: TaskRecorder → **Stop Recording** → don't quit; wait for **Idle**.

---

## Bridge lines (use these instead of going silent)

- While an index builds: *"While that builds: the index has to read all 500,000 names and break each one into
  trigrams, so this is the slowest part."*
- While the sheet loads: *"While that loads, the thing I'm watching for is whether the planner actually picks the
  new index, not just whether the time goes down."*
- Before switching apps: *"I'll move to the Dock on the right and click {{Chrome / pgAdmin}} to {{record these
  numbers / try the next index}}."*

## If something goes wrong (say it, fix it, check it)

- Syntax error: *"The Messages tab says syntax error near {{…}}. I left out {{a comma / a bracket}}. I'll click
  after {{…}} on line {{n}}, fix it, triple-click the line and click Execute again… and now it succeeds."*
- **Nothing highlighted, so the whole file ran.** There are CREATE and DROP statements later in the file, so say so.
  In the Object Explorer on the left, right-click **Indexes** under products → **Refresh** to see what exists, drop
  anything that shouldn't be there, and rerun only the highlighted line. *"That ran the whole file instead of my
  selection. I'll check the Indexes folder in the Object Explorer and put it back the way it was."*
- `extension "pg_trgm" already exists`: *"The Messages tab says the extension is already enabled, so I'll carry on."*
- `relation "products_name_trgm_gin" already exists`: drop it, recreate it, and read the build time from the new run.
- Typo in the sheet: *"In cell {{C3}} I typed {{…}} instead of {{…}}. I'll click that cell, retype it and press Return,
  and the median in column E updates."*
- If anything shows your name, a personal account, Studio or Slack: **stop and re-record from the start.** Don't
  narrate over it.
