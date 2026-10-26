# Task 33g7c3d6: end-to-end steps (catalog search, pg_trgm GIN vs GiST)

Idea: [idea-draft.md](idea-draft.md) (v2, **APPROVED**). Rules: [task-instructions.md](task-instructions.md).
Apps: **pgAdmin 4** + **Google Sheets**. Target recording: **about 40 minutes** (hard window 15:00–50:59).
Task files: [33g7c3d6/](33g7c3d6/) (inputs go in `33g7c3d6/inputs/`).

| Phase | What | Status |
|---|---|---|
| A | Get the idea approved | **DONE** |
| B | One-time Mac setup (Recorder user, Xcode/Inspector, TaskRecorder, Dock/clock) | **DONE** |
| C | Build the database and the two input files | **DONE** (inputs validated and loaded 2026-10-26; DB reset to the pre-recording state) |
| D | Set up pgAdmin 4 and Google Sheets | to do |
| E | Metadata.rtf, opening Goal doc, Studio pre-recording fields | to do (text ready below) |
| F | Dry run, then reset the database | to do |
| G | Pre-flight checklist (the 10 minutes before Start) | recording day |
| H | The recording (run sheet with SQL and narration cues) | recording |
| I | Stop and validate | after recording |
| J | Build Deliverables.zip | after recording |
| K | Upload, AutoQC, submit | after recording |

---

## Phase A: idea approved (DONE)

### The approved Goal: paste this exact text in three places
1. TaskRecorder → **Task Description**.
2. The opening Google Docs document (only this paragraph, no Approval ID).
3. Metadata.rtf → **Request**.

Before using it, compare it against the Goal in Studio's pre-filled **Prompt/Description**. If Studio's text
differs in any character, **Studio's version wins**: replace it here and everywhere else.

```
As a backend developer, I will fix a slow product-search query in a synthetic PostgreSQL catalog database using pgAdmin 4 and Google Sheets. The search matches any part of the product name with ILIKE '%term%', so the existing B-tree index on name cannot help. In pgAdmin 4, I will read the execution plans, then build and measure two trigram index options from the pg_trgm extension, GIN and GiST, against a rare term, a common term and a two-letter term, and confirm every search returns exactly the same rows as before. In Google Sheets, I will compare median timings, index sizes and build times to choose one index. I will deliver catalog_search_index.sql, with the chosen index, my measurements and a minimum search-length recommendation, and the benchmark spreadsheet for my team's code review.
```

### What the approval means for the rest of this file
- **Record exactly what was approved:** both apps, all three terms, both index types, the equality checks, and
  both deliverables. If anything has to change materially, use **Revise idea** and wait for re-approval
  *before* recording.
- **Never reuse or show the Approval ID** on screen.
- **The epilogue is required:** this idea was approved after Oct 19, 2026 6 PM PT.
- **Continue in the same Studio task.** It is now In Progress; don't create a new one.

---

## Phase B: one-time Mac setup

### B1. Create a separate "Recorder" macOS user (do this: your username is your full name)
Your login `amanverma` appears in Save/Open dialogs, file paths and the Finder sidebar. A full name is PII, and
one frame is enough for rejection. The guide's fix is a separate account:
1. System Settings → **Users & Groups** → **Add User** → **Administrator**, full name and account name
   `Recorder`, any password. **Don't** sign in to iCloud.
2. Keep your main account **logged in** (use fast user switching, not Log Out). Your Homebrew PostgreSQL
   (`postgresql@17`, a launch agent under `amanverma`) keeps running and is reachable from Recorder on
   `127.0.0.1:5432`.
3. Keep Studio, Slack, the guidelines and this folder in your **main** account. Do the recording in **Recorder**.

### B2. Inside the Recorder account (settings are per user, so redo them there)
- **Desktop:** empty, no widgets. **Wallpaper:** a built-in Apple one.
- **Do Not Disturb:** Focus → Do Not Disturb → People: None, Apps: None, Intelligent Breakthrough off.
- **Clock:** System Settings → Menu Bar → Clock Options → **Display the time with seconds** ON.
- **Dock:** System Settings → Desktop & Dock → Position **Left** (or Right), **Automatically hide** OFF,
  **Show indicators for open applications** ON.
- **Language:** English. **Cursor:** default size and color.
- **Mac name:** already neutral ("MacBook Pro"), so nothing to do.

### B3. Xcode and Accessibility Inspector
- Xcode is already in `/Applications`. In Recorder, open it once and finish any first-run prompts.
- Right-click Xcode in the Dock → **Open Developer Tool → Accessibility Inspector** → close its *window* with
  the red button. Don't quit or minimize the app. The blue icon must keep a **dot** under it.

### B4. TaskRecorder 2.4.4
1. Download `TaskRecorder2.4.4.dmg` (Apple silicon) from the Studio card **2. Set up your tech** (in your main
   account), and move the DMG to `/Users/Shared`.
2. In Recorder: open the DMG from `/Users/Shared` → drag TaskRecorder to **Applications** (choose Replace if
   asked).
3. Open it. If macOS can't verify the developer: **Done** → System Settings → Privacy & Security → **Open
   Anyway**. If it says *damaged* or *malware*, stop and post in #odin--helpdesk.
4. Grant **Accessibility, Screen Recording, Microphone**. All three must be **green** in TaskRecorder. If one
   won't stick: remove it with "−", re-add with "+", toggle on, then quit and reopen TaskRecorder.
5. **10-second test:** start, switch between two apps, open a Save dialog, stop, and wait for **Idle**. Open
   **Show Recordings** and check that `video.mp4` plays with audio, `screenshots/` has PNGs, and the
   `.jsonl` files exist.

### B5. Studio one-time checklist (main account)
Card **2. One-time setup checklist**: answer **Yes, I did this step** for all 5 (Xcode, Accessibility
Inspector, TaskRecorder 2.4.4, permissions, clock + Dock). Also answer the two **Before you start** dropdowns
(your Mac meets all three requirements; Insightful is installed and running).

### B6. Insightful
- Run it (Workpuls.app, Project Odin) only during your **3 paid setup hours**. After those, the first task is
  paid by milestones ($150 on submit, $250 at RFD), not hourly.
- If it runs while you record, it must be minimized and its window never shown.

### B7. Watch the required video
On the task page: **Watch: How to Narrate Well** (required before the first task). Also worth watching:
**During Recording** and the **Software & AI/ML** Golden Example.

---

## Phase C: database and input files (main account, Terminal)

### C1. Make the input files with Gemini
Input files must be **self-created**, or made with **Gemini** (the only AI allowed for inputs). Route chosen:
**Gemini**. Paste the prompt in [33g7c3d6/gemini-prompt.md](33g7c3d6/gemini-prompt.md) into Gemini (with your
@mercor.expert account) and save the outputs to `33g7c3d6/inputs/`. That makes them **AI-generated file**
inputs, and Final Notes must say exactly `AI-generated before recording`. The spec in C3 and C4 is what the
prompt asks for.

### C2. A neutral database login (so pgAdmin never shows `amanverma`): DONE 2026-10-26
Role `backend_dev` (LOGIN; local auth is trust, so no password) and database `catalog` (owned by it) exist.
Your PostgreSQL superuser is `amanverma`, and pgAdmin shows the login name in tab titles. Create a neutral
role and database, then build everything as that role:
```sql
-- psql -d postgres   (as amanverma, once)
CREATE ROLE backend_dev LOGIN PASSWORD 'pick-one';
CREATE DATABASE catalog OWNER backend_dev;
```

### C3. Input 1: `create_catalog_db.sql` (you write it)
Requirements:
- Runs in database `catalog` as `backend_dev`.
- Table `products`: `id bigint primary key`, `name text not null`, `price numeric(10,2)` (a category column is
  optional). About **500,000 rows**.
- Names follow a pattern like `<Adjective> <Material> <Item> <CODE-1234>`, built from small **generic word
  lists** with `generate_series` + `random()`. Call `setseed(...)` first so the data is reproducible. **No real
  brands, people or emails.**
- Plant the three test terms deliberately:
  - **Rare term** (e.g. one material): about 50 to 250 rows.
  - **Common term** (another material): about 20 to 30% of rows.
  - **Two-letter term**: a letter pair that appears in only a few rows (e.g. a rare model-code prefix). Check
    it doesn't occur inside other common words.
- Create the B-tree index the team added earlier: `CREATE INDEX products_name_idx ON products (name);`
- End with `VACUUM ANALYZE products;`
- **Don't** create `pg_trgm`. `CREATE EXTENSION` happens on camera.

Run it: `psql -h 127.0.0.1 -U backend_dev -d catalog -f create_catalog_db.sql`

### C4. Input 2: `catalog_search.sql` (you write it)
The search API's query exactly as the idea describes it: a case-insensitive partial match on the name, first
50 matches by id. It has this shape, with one sample term in it:
`SELECT id, name, price FROM products WHERE name ILIKE '%<term>%' ORDER BY id LIMIT 50;`

### C5. Verify the data behaves (these are checks, not input files)
```sql
SELECT count(*) FROM products;                                  -- ≈ 500000
SELECT count(*) FROM products WHERE name ILIKE '%<rare>%';      -- ≈ 50–250
SELECT count(*) FROM products WHERE name ILIKE '%<common>%';    -- ≈ 20–30%
SELECT count(*) FROM products WHERE name ILIKE '%<xy>%';        -- small
EXPLAIN (ANALYZE, BUFFERS) <catalog_search query with the rare term>;  -- note Execution Time
```
- The rare-term search should be clearly slow (tens to hundreds of ms). If not, add rows.
- Note what the baseline plan looks like. With `ORDER BY id LIMIT 50` PostgreSQL may walk the primary key and
  filter, or do a Seq Scan + Sort. Either way it reads nearly the whole table for the rare term, and it never
  uses `products_name_idx`. Narrate whichever you actually see.

### C6. Put the inputs where Recorder can open them
Copy both files into `/Users/Shared/catalog-task/` (or Recorder's Documents). Keep the originals for
Deliverables.zip.

---

## Phase D: pgAdmin 4 and Google Sheets (Recorder account)

### D1. pgAdmin 4
1. Install it: the DMG from pgadmin.org, or `brew install --cask pgadmin4` from the main account. It goes in
   `/Applications`. The license (PostgreSQL License) allows commercial use.
2. Open it in Recorder and set a master password if asked.
3. **Register → Server**:
   - General: Name `Local PostgreSQL 17`.
   - Connection: Host `127.0.0.1`, Port `5432`, Maintenance DB `catalog`, Username `backend_dev`, Save
     password on.
   - **Advanced → DB restriction: `catalog`** hides your `postgres`/`techops_*` databases from the tree.
4. Expand catalog → Schemas → public → Tables → products → Indexes, and confirm only `products_pkey` and
   `products_name_idx` exist.
5. Practise, and confirm in your pgAdmin version:
   - **Query Tool** (right-click `catalog` → Query Tool), **Open File**, **Execute** (▶ / F5), running only the
     **selected** text, and **Save** / **Save As**.
   - **Explain Analyze** button (Shift+F7). In its options dropdown turn on **Buffers**. Results appear in
     the **Explain** tab → **Graphical** / **Analysis** / **Statistics**.
   - Where build time shows: the **Messages** tab ("Query returned successfully in … msec").
   - For exact timings, the typed `EXPLAIN (ANALYZE, BUFFERS) …` prints **Execution Time** on its last row in
     Data Output.

### D2. Google Sheets
1. In Recorder, use a **fresh browser** (Safari, or install Firefox) with no imported data. Sign in to Google
   with your **@mercor.expert** account only.
2. Check the top-right account corner: it should show only your @mercor.expert identity (first name and initial
   are fine).
3. Practise in a scratch sheet:
   - `=MEDIAN()`.
   - **Insert → Chart** → Column chart, with a series per configuration. Under **Customize → Vertical axis**,
     tick **Log scale**: no-index and GIN times differ by orders of magnitude, and a linear axis hides the small
     bars.
   - **File → Download → Microsoft Excel (.xlsx)**.

---

## Phase E: Metadata.rtf, opening doc, Studio fields (do now: the idea is approved)

### E1. Metadata.rtf (TextEdit is allowed only for this file)
Download the template (https://drive.google.com/file/d/1_WThzOJgZzk_WcUdDtqO1QR4qYG1tbGa/view), open it in
TextEdit, fill the three sections, **delete everything from "PLEASE DELETE THIS SECTION" down**, and save as
`Metadata.rtf` in your main account.

```
Topology: pgAdmin 4 (LOOKUP) -> Google Sheets (CREATE) -> pgAdmin 4 (MODIFY) -> Google Sheets (MODIFY) -> pgAdmin 4 (CREATE)

Request: As a backend developer, I will fix a slow product-search query in a synthetic PostgreSQL catalog database using pgAdmin 4 and Google Sheets. The search matches any part of the product name with ILIKE '%term%', so the existing B-tree index on name cannot help. In pgAdmin 4, I will read the execution plans, then build and measure two trigram index options from the pg_trgm extension, GIN and GiST, against a rare term, a common term and a two-letter term, and confirm every search returns exactly the same rows as before. In Google Sheets, I will compare median timings, index sizes and build times to choose one index. I will deliver catalog_search_index.sql, with the chosen index, my measurements and a minimum search-length recommendation, and the benchmark spreadsheet for my team's code review.

Task Description:
1. Run the catalog search query in pgAdmin 4 with a rare, a common and a two-letter term and record the baseline row counts and timings.
2. Read the EXPLAIN ANALYZE plans to show the B-tree index on name is not used for a leading-wildcard ILIKE search, and save baseline results for each term.
3. Record the baseline timings in a Google Sheets benchmark and calculate the medians.
4. Enable pg_trgm in pgAdmin 4, build and measure a GIN trigram index, then a GiST trigram index (build time, size, plans, three timings per term).
5. Compare medians, sizes and build times in Google Sheets, chart them, choose an index and download search_benchmark.xlsx.
6. Re-create the chosen index with CREATE INDEX CONCURRENTLY in pgAdmin 4, prove every term returns the same rows as the baseline with EXCEPT checks, and save catalog_search_index.sql with the measurements, decision and three-character minimum recommendation.
```
The Topology must match the **actual** order you record. If you add an app visit, add it here too. Never show
Metadata.rtf on screen.

### E2. Opening Goal document
A **Google Docs** document (in its own browser window in Recorder) containing **only the approved Goal
paragraph** (the block in Phase A): no Approval ID, no other approval text. Name it something neutral like
`Search index task`. Not Notes.app or TextEdit. Google Docs doesn't count as a
task app, because it's only used for the opening.

### E3. Studio pre-recording fields (main account)
- **Before Recording (Task Plan)**: tick the confirm box when Metadata.rtf is ready, the Request matches the
  Goal, and the inputs are clean.
- **Inputs Used**: **AI-generated file** (made with Gemini before recording).
- **Before Recording (Prepare)** → **Display**: choose the display and resolution you'll record on (the
  built-in display) and keep it the same.

---

## Phase F: dry run, then reset

1. Do the whole of Phase H once **without recording** (or as a throwaway test recording), timing yourself with
   the menu-bar clock. If it's over 45 minutes, shorten the narration, not the steps.
2. Check that the plans behave as expected:
   - GIN gives a **Bitmap Index Scan** for the rare term.
   - The common term keeps a plan without the trigram index.
   - The two-letter term gets no benefit.
   If not, adjust the data in C3 and redo C5.
3. **Reset before the real take** (main account or pgAdmin):
```sql
DROP INDEX IF EXISTS products_name_trgm_gin;
DROP INDEX IF EXISTS products_name_trgm_gist;
DROP TABLE IF EXISTS baseline_rare, baseline_common, baseline_short;
DROP EXTENSION IF EXISTS pg_trgm;
VACUUM ANALYZE products;
```
4. Delete any dry-run `catalog_search_index.sql`, empty the practice sheet (keep one **blank** spreadsheet), and
   clear browser history and downloads in the Recorder browser.

---

## Phase G: pre-flight (the 10 minutes before Start Recording)

Main account:
- [ ] Studio, Slack, the guidelines, Metadata.rtf and this folder are closed or at least not visible in Recorder.
  Switch to Recorder.

Recorder account:
- [ ] Mac on **power**; at least 35 GB free; quiet room; **Do Not Disturb ON**.
- [ ] **UI change for this recording:** e.g. turn on **Dark Mode** or change the accent color (at least one, every
  recording).
- [ ] Dock left/right with indicators; clock with seconds; default cursor.
- [ ] **Accessibility Inspector** running, window closed, dot under its icon.
- [ ] Quit everything else (⌘Q). ⌘Tab should show only pgAdmin 4, the browser, TaskRecorder and Accessibility
  Inspector.
- [ ] **pgAdmin 4**: connected to `Local PostgreSQL 17`, tree expanded to `products → Indexes`, Query Tool open
  with `catalog_search.sql` loaded (not run), window positioned → **minimize**.
- [ ] **Browser**: blank Google Sheet open, titled `search_benchmark` (so the download is named right),
  @mercor.expert account, no other tabs → **minimize**.
- [ ] **Opening doc**: the Google Docs window with only the Goal, visible behind TaskRecorder.
- [ ] Check the account corner of every visible app; no personal name, photo or email anywhere.
- [ ] **TaskRecorder**: permissions green; mic selected and the level bar goes green on a test sentence; correct
  display; **Task Description** = the approved Goal from Phase A (pasted exactly, no link or path); **Used Apps** = `pgAdmin 4`,
  `Google Sheets` (exactly as in Studio). Clear anything left from earlier tests.
  *If TaskRecorder only lets you pick installed apps and Google Sheets isn't one, ask @Maven in #odin--helpdesk
  how to list a browser-based app before recording.*

---

## Phase H: the recording (run sheet)

Golden rules for the whole take:
- **Narrate what + where + why**, with the cursor on what you name.
- **Pause about 1 second after each click.**
- **Say every keyboard shortcut out loud.**
- **No silence over 45 seconds**: the GiST build may take a while, so explain trigrams while it runs.
- **No typing burst over 45 seconds; total typing ≤ 35%.**
- **Never show** Studio, Slack, Insightful or Metadata.rtf. **No AI of any kind.**
- **Windows:** one window in ordinary Fill, or two side by side. Never Full Screen. Don't let overlap cover the
  work.

### 0:00–0:20 Intro
- Click **Start Recording** → **minimize TaskRecorder immediately**.
- With the Goal doc visible, say only: *"I will be beginning my task soon. Here is the workflow I have in mind."*
- Minimize the Goal doc window.

### Step 1: baseline searches in pgAdmin 4 (about 4 min)
- Bring up pgAdmin 4 from the Dock.
- Walk the tree: point at `products` → **Indexes** → `products_name_idx`. *"The team already added a B-tree
  index on name."*
- In the Query Tool, read `catalog_search.sql` aloud in plain terms. On first use, say what the prepared data
  is, without naming any AI tool or inventing a source: *"The catalog database is a synthetic test copy of
  500,000 product names that I prepared for this test. It contains no real customer data and no copyrighted
  material."*
- Make three copies of the query, one each for the **rare**, **common** and **two-letter** terms. Say why you
  picked each one: a selective search, a broad search, and a term too short for trigrams.
- Select each query and click **Execute**. Point at the row count and the "Query complete" time.

### Step 2: read the plans (about 4 min)
- Select the rare-term query → **Explain Analyze** button (Buffers on) → **Explain** tab → **Graphical**.
- Hover each node and name it. Expect **Limit → Gather Merge → Sort → Parallel Seq Scan** (2 workers),
  with "Rows Removed by Filter" around 166k per worker. Show that `products_name_idx` is **not** used.
- **Why:** *"A B-tree is sorted by the start of the string. `ILIKE '%walnut%'` can start anywhere, so the index
  can't narrow the search, and PostgreSQL reads the whole table and filters every row."*
- Point at the **Buffers** and actual-rows numbers.
- Repeat briefly for the common term: *"Fast already, because 50 matches turn up early."*

### Step 3: save baselines and time them (about 5 min)
```sql
CREATE TABLE baseline_rare   AS <rare query>;
CREATE TABLE baseline_common AS <common query>;
CREATE TABLE baseline_short  AS <two-letter query>;
```
- *"These saved results let me prove the index doesn't change what users see."*
- Time each term 3 times with `EXPLAIN (ANALYZE, BUFFERS) <query>`, reading **Execution Time** on the last row.
  Say each number aloud, because you'll type it into the sheet next.
- Mention cache effects: *"The first run can be slower because pages aren't cached yet, which is why I'll use
  the median."*

### Step 4: Google Sheets benchmark (about 3 min)
- Bring up the browser and the blank `search_benchmark` sheet. Arrange it side by side with pgAdmin if
  that's useful.
- Layout:
  - Column A: `Term` (rare / common / two-letter).
  - Columns B–D: `No index run 1–3`, then E: `No index median`.
  - The same pattern later for GIN (F–I) and GiST (J–M).
  - A small table below for **Index | Size | Build time**.
- Enter the 9 baseline timings in short bursts. In E, use `=MEDIAN(B2:D2)` and fill it down by dragging the
  handle.

### Step 5: GIN trigram index (about 6 min)
```sql
CREATE EXTENSION pg_trgm;
CREATE INDEX products_name_trgm_gin ON products USING gin (name gin_trgm_ops);
SELECT pg_size_pretty(pg_relation_size('products_name_trgm_gin'));
```
- **Explain:** *"pg_trgm breaks text into three-character pieces, so 'walnut' becomes 'wal', 'aln', 'lnu' and
  so on. GIN is an inverted index from each trigram to the rows containing it, so a substring search can look up
  the pieces instead of reading every row."*
- Point at the **Messages** tab for the build time, then the size result.
- Explain Analyze each term:
  - **Rare:** Bitmap Index Scan on `products_name_trgm_gin` → Bitmap Heap Scan (with **Recheck**, because the
    index finds candidates and PostgreSQL confirms the real match).
  - **Common:** the planner keeps a plan without the index (*"too many matches; walking the table finds 50
    quickly"*).
  - **Two-letter:** no benefit (*"two letters can't form a trigram, so the index has nothing to look up"*).
- Time each term 3 times, then `DROP INDEX products_name_trgm_gin;`

### Step 6: GiST trigram index (about 5 min)
```sql
CREATE INDEX products_name_trgm_gist ON products USING gist (name gist_trgm_ops);
SELECT pg_size_pretty(pg_relation_size('products_name_trgm_gist'));
```
- Narrate during the build: *"GiST stores compressed trigram signatures in a balanced tree. It's lossy, so it
  needs more rechecking, but it also supports similarity ordering, which GIN can't."*
- Do the same measurements as Step 5: build time, size, plans, 3 timings per term. Then
  `DROP INDEX products_name_trgm_gist;`
- **Watch the two-letter term here (the dry run showed this):** with GiST, the planner *does* use the index for
  `qx`, and it's **slower than having no index**. The Bitmap Index Scan returns all 500,000 rows and
  **Rows Removed by Index Recheck ≈ 499,960**. Point at that line. It's the strongest evidence for the
  three-character minimum, and a real difference between GIN (whose planner avoided the index) and GiST.

### Step 7: compare and decide in Google Sheets (about 5 min)
- Enter the GIN and GiST timings, medians, sizes and build times.
- Add `Speedup = No-index median / GIN median` (and the GiST equivalent) for the rare term.
- **Insert → Chart** → Column chart of the three median columns by term → **Customize → Vertical axis → Log
  scale**. Explain why you chose log scale.
- Write a **Decision** cell based on **your measured numbers** (e.g. faster rare-term search vs size and build
  cost, and whether you need similarity ranking). Don't decide in advance.
- **File → Download → Microsoft Excel (.xlsx)** gives `search_benchmark.xlsx`. Say where it was saved, and don't
  click the Dock's Downloads stack.

### Step 8: final index, equality proof, deliverable SQL (about 6 min)
```sql
CREATE INDEX CONCURRENTLY products_name_trgm_gin ON products USING gin (name gin_trgm_ops);  -- or the GiST form if that won
```
- *"In production I'd build it CONCURRENTLY so writes to products aren't blocked while it builds."*
- Equality check for each term (must return **0**):
```sql
SELECT count(*) FROM (
  (SELECT * FROM baseline_rare EXCEPT (<rare query>))
  UNION ALL
  ((<rare query>) EXCEPT SELECT * FROM baseline_rare)
) diff;
```
  Repeat for `baseline_common` and `baseline_short`. *"Zero rows in both directions means the index changed the
  speed, not the results."*
- **Save As** the Query Tool contents as `catalog_search_index.sql`. Write it in short bursts, as comment
  sections with **your** numbers:
  1. The search query.
  2. The baseline plan summary + median per term.
  3. GIN: build time, size, plan per term, medians.
  4. GiST: the same.
  5. Decision + reasoning.
  6. Recommendation: require at least 3 characters in the search box (the two-letter term evidence).
  7. Final `CREATE INDEX CONCURRENTLY` statement.
  8. The three equality checks + "returned 0".
- Save. Scroll through the saved file once on camera and point at each section.

### Step 9: finish and epilogue (target 3–4 min, max 4:00; the mouse may rest)
- Show the saved `catalog_search_index.sql` and the downloaded `search_benchmark.xlsx`, and confirm the results.
- Epilogue, in your own words:
  1. **Completion:** how you verified it (zero-row EXCEPT checks, plan shows the trigram index, medians);
     limitations (synthetic data, a single machine, warm cache).
  2. **Approach:** why you measured both GIN and GiST instead of guessing.
  3. **Challenges:** what surprised you (e.g. the common term not using the index).
  4. **Quality:** how solid the result is; weaknesses (index size, slower writes).
  5. **Next time:** test write and insert overhead, more terms, production-like data.
  6. **Insight:** *"Indexes don't help every query. A leading wildcard defeats a B-tree, and very short
     search terms defeat trigrams, so check the plan, not just the timing."*
- Say *"That completes the task."* → bring up TaskRecorder → **Stop Recording**.

---

## Phase I: stop and validate

1. After **Stop Recording**, don't quit. Wait for **Stopping → Archiving → Idle**.
2. **Show Recordings** → the newest `recording_TIMESTAMP` folder and `recording_TIMESTAMP.zip`. **Don't rename,
   edit or re-zip.**
3. The folder must contain `screenshots/` (PNGs), `video.mp4`, `frames.jsonl`, `ax.jsonl`, `input.jsonl`,
   `processes.jsonl` and `recording.log`.
4. Open `video.mp4` in QuickTime and check the start, middle and end: picture OK, narration audible, nothing
   cut off. Length must be **15:00–50:59**.
5. **Screenshot ratio:** the PNG count divided by the video seconds must be **> 0.5**. In Terminal:
   `ls <folder>/screenshots | wc -l` and `mdls -name kMDItemDurationSeconds <folder>/video.mp4`.
6. Watch for PII (names, paths, account corners), Studio/Slack/Insightful/Metadata on screen, silences over 45
   seconds, and swearing. **If any of these happened, re-record. Never edit the video.**

---

## Phase J: Deliverables.zip

1. Make a folder containing (keep the extensions):
   - `input 1 - create_catalog_db.sql`
   - `input 2 - catalog_search.sql`
   - `final output 1 - catalog_search_index.sql`
   - `final output 2 - search_benchmark.xlsx`
   *(The guide asks for "input 1 / final output 1" labels. Keeping the original name after the label keeps them
   matching the approved idea.)*
2. Select the files → right-click → **Compress** → rename the result to `Deliverables.zip`.
3. Open the zip and check all 4 files are there and open. **Metadata.rtf must not be inside.**

---

## Phase K: upload and submit (main account, Studio task 33g7c3d6)

1. Upload **Metadata.rtf** (its own field), **video.mp4** (the separate copy from the recording folder),
   **recording_TIMESTAMP.zip** (unmodified) and **Deliverables.zip**.
2. Run both AutoQCs: **Files & Recording** and **Narration**.
   - **Major** flags block submission: fix them (for a file problem, re-upload the corrected file; no
     re-record) or **Dispute** with a reason and timestamps.
   - **Minor** flags are advice.
3. Do the manual checks one by one, and tick the **Task Checklist + PII** confirmation after opening both links.
4. Tick the **epilogue** checkbox (you recorded one).
5. **Final Notes**: exactly `AI-generated before recording` (for create_catalog_db.sql and catalog_search.sql).
   Fill in **Source of Data** if Studio shows it.
6. Tick **Final Confirmation** → **Submit for Review**. The status should become **Ready for Review**.
7. Afterwards, keep the recording folders until review passes, then delete them and empty the Trash.
