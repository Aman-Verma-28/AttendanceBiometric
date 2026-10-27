# Narration script: task 33g7c3d6 v3 (catalog search, pg_trgm GIN vs GiST, decision in Sheets)

Goes with [task-steps.md](task-steps.md) Phase H. About 34 minutes in total. The SQL is in the run sheet and in the
"queries in order" block; this file is what you say. v2's script is archived as [script-v2.md](script-v2.md).

## How to use this script
- **Rehearse with it; don't read it on camera.** Reviewers reject narration that sounds recited or robotic. Learn
  the flow and the *why* lines, then say them in your own words. Only the intro sentence must be word for word.
- **Keep it off the screen while recording** (it mentions the project). Use your phone, an iPad or a printout.
- `ACTION` = what your hands do. `SAY` = what you say while doing it. `{{…}}` = read the real number off the
  screen (the dry-run value is shown as a guide; never say a number you didn't see).
- Keep the cursor on whatever you're naming. Pause about 1 second after each click.
- **Say every keyboard shortcut out loud** as you press it.
- **No gap over 45 seconds.** If something is loading, use a bridge line (end of this file).
- **Typing:** no burst over 45 seconds. Talk between bursts.

| Section | Target | Clock at end (about) |
|---|---|---|
| Intro | 0:20 | 0:20 |
| 1. Baseline searches | 3:30 | 3:50 |
| 2. Read the plans | 4:00 | 7:50 |
| 3. Time each term three times | 3:30 | 11:20 |
| 4. Sheets: baseline | 3:30 | 14:50 |
| 5. GIN index | 6:00 | 20:50 |
| 6. GiST index | 5:00 | 25:50 |
| 7. Sheets: compare and decide | 5:00 | 30:50 |
| Epilogue | 3:30 | 34:20 |

If you're past **47:00** when you reach the epilogue, shorten it (it must still cover all six points). The hard
limit is 50:59.

---

## Intro (under 20 seconds, exact words)

ACTION: Goal document visible. Click **Start Recording** in TaskRecorder, then minimize TaskRecorder immediately.

SAY (exactly):
> "I will be beginning my task soon. Here is the workflow I have in mind."

ACTION: wait 2–3 seconds, then minimize the Goal document window. **Don't read or explain the Goal.**

---

## Step 1: baseline searches in pgAdmin 4

ACTION: click the **pgAdmin 4** icon in the Dock.
SAY:
> "Step 1. I'm opening pgAdmin 4, which is already connected to my local PostgreSQL 17 server."

ACTION: point at the Object Explorer, then at `products` → **Indexes**.
SAY:
> "On the left, in the Object Explorer, I have the catalog database open. Under Schemas, public, Tables, I'll
> expand products and then its Indexes folder. There are two indexes: products_pkey on the id column, and
> products_name_idx, a B-tree index on name that the team added earlier to speed up search."

ACTION: point at the Query Tool editor with `catalog_search.sql`.
SAY:
> "In the Query Tool I've opened catalog_search.sql, the query our product-search API runs. It selects id, name and
> price from products where name ILIKE percent, the search term, percent, ordered by id, limited to 50 rows. ILIKE
> makes the match case-insensitive, and the percent signs on both sides mean the term can appear anywhere in the
> name."

SAY (the first-use description of the prepared data; required, and never name a tool):
> "The catalog itself is a synthetic test database of 500,000 generated product names, prepared before this
> session. It contains no real customer data and nothing copyrighted."

ACTION: open the **Save** dropdown in the toolbar → **Save As** → `/Users/Shared/catalog-task` → `search_measurements.sql` → Save.
SAY:
> "Before I change anything, I'll open the save menu in the toolbar, choose Save As, and save a working copy as
> search_measurements.sql. The original query file stays untouched, and this file will hold my measurements."

SAY:
> "Users say search is slow, so I'll test three kinds of search term. A rare term, walnut, which appears in only a
> handful of products. A common term, steel, which is in about a quarter of the catalog. And a very short term, the
> two letters Q X, because real users type short fragments and I need to know how any fix handles them."

ACTION: select the query line → ⌘C → click at the end → Return → ⌘V → Return → ⌘V. Change the terms to `steel`
and `qx`.
SAY:
> "I'll select the query line and press Command C, then Return and Command V twice to paste two copies. In the
> second I'll double-click walnut and type steel, and in the third, Q X."

ACTION: highlight the walnut line → **F5**. Then steel, then qx.
SAY:
> "I'll highlight just the walnut query and press F5, so only that statement runs. Data Output shows 50 rows, and
> the status bar says about {{80}} milliseconds."
> "Steel: 50 rows again, almost instant."
> "Q X: only {{40}} rows, because fewer than 50 products contain it, and about {{80}} milliseconds."
> "So the rare search and the short search are the slow ones, and the common search is fast. That's the opposite of
> what you might expect, and the plans will show why."

ACTION (optional): the two `count(*)` lines.
SAY:
> "To put numbers on rare and common: walnut is in {{150}} products, steel in {{125,000}}."

---

## Step 2: read the plans

ACTION: type `EXPLAIN (ANALYZE, BUFFERS) ` in front of the walnut line → highlight it → **F5**.
SAY:
> "Step 2. I'll read the execution plan. EXPLAIN ANALYZE actually runs the query and reports what happened, and
> BUFFERS adds how many 8 kilobyte pages it touched."

ACTION: Data Output → scroll to the top rows, then move the cursor up from the deepest-indented line.
SAY:
> "The plan reads from the most indented line upwards. At the bottom, a Parallel Seq Scan on products. That means
> PostgreSQL reads every row, split across the main process and two workers. Above it, a Sort on id, then Gather
> Merge combines the three sorted streams, and Limit keeps the first 50."

ACTION: point at `loops=3`, `Rows Removed by Filter`, `Buffers`.
SAY:
> "Loops equals three, so these numbers are per process and I multiply by three. Rows Removed by Filter is about
> {{166,617}}, so roughly 499,850 rows were checked and thrown away to find 150 matches. Buffers, shared hit
> {{4,896}}: that's every page of the table, and all of them came from memory, so this is pure CPU work."

SAY (the key *why*):
> "Notice that products_name_idx doesn't appear anywhere. A B-tree keeps names sorted from the first character, like
> a phone book sorted by surname, so it's great for names that start with something. But walnut can appear anywhere
> in the name. With a wildcard at the front, the sorted order doesn't help, so the planner ignores that index and
> reads the whole table."

ACTION: the same for steel.
SAY:
> "For comparison, steel. This is an Index Scan using products_pkey, the primary key, with the same filter. Because a
> quarter of the products contain steel, walking the table in id order finds 50 matches after about 200 rows. Rows
> Removed by Filter is just {{150}}, Buffers just {{5}}, and it's done in {{0.08}} milliseconds. The LIMIT is doing
> the work."

---

## Step 3: time each term three times

ACTION: put the same prefix on the steel and qx lines (copy the prefix with ⌘C, paste with ⌘V).
SAY:
> "Step 3. One run on its own is noisy, so I'll run each search three times and compare medians. I'll copy the
> EXPLAIN prefix with Command C and paste it onto the other two lines with Command V."

ACTION: highlight the walnut EXPLAIN line → **F5** three times, reading the last row each time.
SAY:
> "The last row, Execution Time, is the time spent in the database, without drawing results on screen. Walnut, run
> one: {{…}} milliseconds. Run two: {{…}}. Run three: {{…}}."

ACTION: type a comment at the bottom: `-- no index | walnut: __, __, __`.
SAY:
> "I'll note those in a comment at the bottom of my working file."

ACTION: the same for steel and qx, each with a comment line. Then **⌘S**.
SAY:
> "Steel: {{…}}, {{…}}, {{…}}, well under a millisecond. Q X: {{…}}, {{…}}, {{…}}, as slow as walnut, because it's
> rare too, so it also reads the whole table."
> "Command S to save the working file."

---

## Step 4: Google Sheets, baseline

ACTION: click the browser in the Dock (the blank `search_benchmark` sheet). Optional tile: green button → **Tile
Window to Right of Screen**, pgAdmin on the left.
SAY:
> "Step 4. I'll record these in Google Sheets so I can compare all three setups side by side. I'll tile the browser
> to the right, with pgAdmin on the left, so I can read my notes while I type."

ACTION: A1:E1 `Term`, `No index run 1`, `No index run 2`, `No index run 3`, `No index median` (Tab between). A2:A4
`walnut (rare)`, `steel (common)`, `qx (two-letter)` (Return between).
SAY (between bursts):
> "One row per search term, one group of columns per configuration. Tab moves to the next column. Rows two to four
> are walnut, steel and Q X."

ACTION: enter the nine numbers, one row at a time.
SAY:
> "Now the timings from my notes. Walnut: {{…}}, {{…}}, {{…}}…"

ACTION: E2 `=MEDIAN(B2:D2)` → Return → select E2:E4 → **⌘D**.
SAY:
> "In E2, equals MEDIAN of B2 to D2. Then I'll select E2 to E4 and press Command D to fill it down. Median times with
> no index: walnut {{48}}, steel {{0.08}}, and Q X {{45}} milliseconds. So the problem is rare terms, not every
> search."

---

## Step 5: GIN trigram index

ACTION: click **pgAdmin 4**. Under the comments, type `CREATE EXTENSION pg_trgm;` → highlight → **F5**.
SAY:
> "Step 5. Back to pgAdmin to try the first fix. Trigram indexes come from the pg_trgm extension, which ships with
> PostgreSQL but isn't enabled in this database yet. The Messages tab says CREATE EXTENSION."

SAY (the concept):
> "pg_trgm splits text into three-character pieces called trigrams. For walnut those are W-A-L, A-L-N, L-N-U and
> N-U-T. If an index knows which rows contain each trigram, PostgreSQL can look up those four pieces and check only
> the rows that have all of them, instead of reading the whole table."
> "Two index types can store trigrams, GIN and GiST. Rather than guess, I'll build and measure both. First GIN, a
> generalized inverted index. It works like the index at the back of a book: for each trigram, a list of the rows
> that contain it."

ACTION: type the GIN `CREATE INDEX` → **F5** → **Messages** tab.
SAY:
> "The gin underscore trgm underscore ops operator class tells it to index the name's trigrams, not the whole value.
> In the Messages tab, the query returned successfully in {{1.9}} seconds. That's the build time."

ACTION: the `pg_size_pretty` query → **F5**.
SAY:
> "And the GIN index takes {{26}} megabytes."

ACTION: paste a copy of the three EXPLAIN lines under the GIN section. Walnut → **F5**.
SAY:
> "Walnut again. Now the plan has a Bitmap Index Scan on products_name_trgm_gin, which found the candidate rows, then a
> Bitmap Heap Scan that fetches only those. The Recheck Cond line matters: the index knows which rows contain all
> four trigrams, but not whether they're next to each other in the right order, so PostgreSQL checks each candidate
> against the real condition. About {{0.3}} milliseconds, compared with {{48}} before."

ACTION: steel → **F5**.
SAY:
> "Steel still uses the primary-key scan, and that's the right call. With 125,000 matches, going through the index
> would cost more than walking the table until 50 turn up. The planner only uses an index when it's cheaper."

ACTION: qx → **F5**.
SAY:
> "Q X still does a full parallel scan. Two letters don't make up a single trigram, so the index has nothing to
> look up, and the planner knows not to use it."

ACTION: run each line three times → write the `-- GIN |` comment lines → `DROP INDEX products_name_trgm_gin;` → **F5** → **⌘S**.
SAY:
> "Timing with GIN. Walnut: {{…}}, {{…}}, {{…}}. Steel: {{…}}… Q X: {{…}}…"
> "I'll drop the GIN index so it doesn't affect the GiST test, and press Command S to save my notes."

---

## Step 6: GiST trigram index

ACTION: type the GiST `CREATE INDEX` → **F5**.
SAY (while it builds):
> "Step 6. The second option is GiST, a generalized search tree. Instead of a list per trigram, it stores a
> compressed signature of each name's trigrams in a balanced tree. Those signatures are lossy, so it usually needs
> more rechecking than GIN. But GiST can also order results by similarity, which would matter if we later added
> 'did you mean' style fuzzy search."
> "Messages says the build took {{3.7}} seconds, about twice as long as GIN."

ACTION: the size query for `products_name_trgm_gist`.
SAY:
> "And it's {{79}} megabytes, about three times the size of the GIN index."

ACTION: paste the three EXPLAIN lines under the GiST section. Walnut → **F5**.
SAY:
> "Walnut uses a Bitmap Index Scan on the GiST index, in about {{11}} milliseconds. Much better than {{48}} with no
> index, but slower than GIN's {{0.3}}. Rows Removed by Index Recheck shows the lossy signatures at work."

ACTION: steel → **F5**.
SAY:
> "Steel: {{the same primary-key scan as before}}."

ACTION: qx → **F5** → point at `Rows Removed by Index Recheck`.
SAY (the key finding):
> "Q X is the interesting one. With GiST, the planner did choose the index, and it took {{146}} milliseconds, about
> three times the {{45}} with no index at all. Rows Removed by Index Recheck: {{499,960}}. With no trigram to match,
> the index can't rule anything out, so it returned every row as a candidate, and every row had to be rechecked. So
> this GiST index would make short searches slower."

ACTION: run each line three times → `-- GiST |` comment lines → `DROP INDEX products_name_trgm_gist;` → **F5** → **⌘S**.
SAY:
> "Timing with GiST. Walnut: {{…}}… Steel: {{…}}… Q X: {{…}}… Then I'll drop the GiST index and press Command S."

---

## Step 7: Google Sheets, compare and decide

ACTION: click the browser.
SAY:
> "Step 7. Back to the sheet to compare all three setups and decide."

ACTION: F1:M1 `GIN run 1`, `GIN run 2`, `GIN run 3`, `GIN median`, `GiST run 1`, `GiST run 2`, `GiST run 3`,
`GiST median`. Enter the GIN timings in F2:H4 and the GiST timings in J2:L4.
SAY:
> "Columns F to I are the GIN runs and median, and J to M are GiST. I'll enter the timings from my notes."

ACTION: select E2:E4 → **⌘C** → click I2 → **⌘V** → click M2 → **⌘V**.
SAY:
> "For the medians, I'll copy the no-index median column with Command C and paste it with Command V into I2 and M2.
> Sheets shifts the formula to the new columns by itself."

ACTION: N1 `GIN speedup (×)`, O1 `GiST speedup (×)`; N2 `=E2/I2`, O2 `=E2/M2` → select N2:O4 → **⌘D**.
SAY:
> "Speedup is the no-index median divided by the indexed median. For walnut that's about {{160}} times with GIN and
> {{4}} times with GiST. Steel is about 1 with both, so no change. For Q X, GIN is 1 and GiST is {{0.31}}: below one
> means slower, so GiST makes short searches about three times slower."

ACTION: A6 `Index`, B6 `Size (MB)`, C6 `Build time (ms)`; A7 `GIN` + numbers; A8 `GiST` + numbers.
SAY:
> "Below, a small cost table. GIN is {{26}} megabytes and built in {{1,900}} milliseconds. GiST is {{79}} megabytes
> and {{3,700}} milliseconds."

ACTION: A10 `Decision`, B10 **your** decision. A11 `Min search length`, B11 `3 characters (two-letter terms get no
benefit; GiST made qx slower)`.
SAY (adapt to what you measured):
> "My decision: {{GIN}}. It gave the fastest rare-term search, the smallest index and the fastest build. GiST's one
> advantage, similarity ranking, isn't something this search uses. And since neither index helps two-letter
> searches, and GiST makes them worse, I recommend the search box requires at least three characters."

ACTION: **File → Download → Microsoft Excel (.xlsx)**. Point at the download indicator.
SAY:
> "File menu, Download, Microsoft Excel. The download indicator at the top right shows search_benchmark.xlsx has been
> saved to my Downloads folder. That's the deliverable for my team's code review."

---

## Epilogue (about 3½ minutes, max 4:00; the mouse may rest, the sheet on screen)

SAY (in your own words; cover all six points, using your real numbers):

> **Completion.** "To wrap up: the task is complete. With the GIN trigram index, the rare-term search goes from about
> {{48}} milliseconds to {{0.3}}. I verified it three ways: the plan shows a Bitmap Index Scan on the trigram index,
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
> "That completes the task."

ACTION: bring TaskRecorder up from the Dock → **Stop Recording** → don't quit; wait for **Idle**.

---

## Bridge lines (use these instead of going silent)

- While an index builds: *"While that builds: the index has to read all 500,000 names and break each one into
  trigrams, so this is the slowest part."*
- While the sheet loads: *"While that loads, the thing I'm watching for is whether the planner actually picks the
  new index, not just whether the time goes down."*
- Before switching apps: *"I'll switch to {{the sheet / pgAdmin}} to {{record these numbers / try the next index}}."*

## If something goes wrong (say it, fix it, check it)

- Syntax error: *"I've got a syntax error near {{…}}. I left out {{a comma / a bracket}}. I'll fix it and run it
  again… and now it succeeds."*
- **Nothing highlighted, so the whole file ran.** Later in the file there are CREATE and DROP statements, so say so,
  right-click **Indexes** → **Refresh** to see what exists, drop anything that shouldn't be there, and rerun just the
  highlighted statement. *"That ran the whole file instead of my selection. I'll check the Indexes folder and put it
  back the way it was."*
- `extension "pg_trgm" already exists`: *"The extension is already enabled, so I'll carry on."*
- `relation "products_name_trgm_gin" already exists`: drop it, recreate it, and read the build time from the new run.
- Typo in the sheet: *"I typed {{…}} instead of {{…}}. I'll click the cell and correct it, and the median updates."*
- If anything shows your name, a personal account, Studio or Slack: **stop and re-record from the start.** Don't
  narrate over it.
