# i+1 English Reading & Deep Internalization Framework Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Establish the $i+1$ English reading, Socratic AI dialogue, and "一书一档" knowledge archiving system in the repository.

**Architecture:** A lightweight, pure-Markdown and Git-driven system composed of a comprehensive methodology handbook (`docs/methodology-guide.md`), a standardized archive template (`books/_template.md`), pre-populated records for first two books (`books/01-the-little-prince.md` and `books/02-who-moved-my-cheese.md`), and an aggregated bookshelf dashboard (`README.md`).

**Tech Stack:** Markdown (GitHub Flavored), Git

## Global Constraints

- Absolute clarity, high readability, and strict adherence to SLA (Second Language Acquisition) $i+1$ principles.
- Clean file links using Markdown format.
- Zero external runtime dependencies required for basic usage.

---

### Task 1: Create the Comprehensive Methodology Handbook (`docs/methodology-guide.md`)

**Files:**
- Create: `docs/methodology-guide.md`

**Interfaces:**
- Consumed by: Learner / User & AI agents when preparing Socratic discussions and reading logs.
- Produces: The core theoretical and practical reference for the entire repository.

- [ ] **Step 1: Write `docs/methodology-guide.md`**
  Write full content covering:
  1. Krashen's $i+1$ Comprehensible Input & Affective Filter Hypothesis.
  2. Incidental Vocabulary Acquisition & The 7-12 Encounters Rule.
  3. The 3-Second Rule for Unknown Words (Flow Protection).
  4. Socratic AI Dialogue SOP (Thought Resonance + 1-2 Collocation Upgrades + Deepening Question).
  5. The "Chunk + Context + Micro-Transfer (生活微造句)" Internalization Formula.
  6. 3-Phase Progression Roadmap (Level 1 Children's/Fables -> Level 2 YA Fiction & Non-Fiction -> Level 3 Complex Literature).

- [ ] **Step 2: Commit**
  ```bash
  git add docs/methodology-guide.md
  git commit -m "docs: add comprehensive i+1 reading and internalization methodology guide"
  ```

---

### Task 2: Create Standard Book Archive Template (`books/_template.md`)

**Files:**
- Create: `books/_template.md`

**Interfaces:**
- Consumed by: Every new book record initialized in `books/`.
- Produces: Standardized schema (Frontmatter/Metadata, Core Resonance, Socratic Highlights, Active Collocations, Review & Ratings).

- [ ] **Step 1: Write `books/_template.md`**
  Provide standardized template with clear section markers, comments, and placeholder format for:
  - Metadata (Title, Author, Difficulty 1-5, Words, Reading Time, Average WPM, Status, Dates).
  - Part 1: Core Plot & Philosophical Resonance.
  - Part 2: AI Socratic Dialogue Highlights (1-2 Turns).
  - Part 3: Active Collocations & Micro-Transfer Cards (5-10 items).
  - Part 4: Post-Reading Review & Flow Rating.

- [ ] **Step 2: Commit**
  ```bash
  git add books/_template.md
  git commit -m "feat: add standardized book archive template"
  ```

---

### Task 3: Create Initial Book Records for *The Little Prince* and *Who Moved My Cheese?*

**Files:**
- Create: `books/01-the-little-prince.md`
- Create: `books/02-who-moved-my-cheese.md`

**Interfaces:**
- Consumes: `books/_template.md`
- Produces: Concrete live records reflecting the user's completed first book and in-progress second book.

- [ ] **Step 1: Write `books/01-the-little-prince.md`**
  - Metadata: Completed, ~15,000 words, Difficulty: ⭐⭐⭐.
  - Core philosophy: "What is essential is invisible to the eye" & "Taming as establishing ties".
  - High-yield collocations prepared for review: `establish ties`, `matter of consequence`, `in the blink of an eye`, `unique in all the world`, `look with the heart`.
  - Prepared Socratic question ready for live interaction.

- [ ] **Step 2: Write `books/02-who-moved-my-cheese.md`**
  - Metadata: In Progress (~50%), ~10,000 words, Difficulty: ⭐⭐.
  - Reading session tracking log with WPM calculation formula.
  - Key thematic themes (anticipating change, letting go of fear, enjoying new cheese).

- [ ] **Step 3: Commit**
  ```bash
  git add books/01-the-little-prince.md books/02-who-moved-my-cheese.md
  git commit -m "feat: add initial book archives for The Little Prince and Who Moved My Cheese"
  ```

---

### Task 4: Modernize Root `README.md` into an $i+1$ Reading Dashboard

**Files:**
- Modify: `README.md`

**Interfaces:**
- Consumes: `books/*.md`, `docs/methodology-guide.md`
- Produces: Inspiring landing page, live bookshelf table, statistics & milestones, and quickstart instructions.

- [ ] **Step 1: Update `README.md`**
  - Modern header and project vision.
  - Real-time Stats & Milestone badges (Total Books, Total Words Read, Current Level).
  - Visual Bookshelf Table indexing all books with links.
  - Methodology overview and quick workflow steps.
  - Maintain clean navigation to existing supplementary notes if desired.

- [ ] **Step 2: Commit**
  ```bash
  git add README.md
  git commit -m "docs: modernize README with i+1 dashboard, bookshelf index, and milestone tracker"
  ```

---

### Task 5: Verification & Self-Review

**Files:**
- Verify: All files in repository.

- [ ] **Step 1: Check link integrity and markdown rendering**
  - Verify all relative and absolute markdown links (`docs/methodology-guide.md`, `books/01-the-little-prince.md`, `books/02-who-moved-my-cheese.md`, `books/_template.md`).
- [ ] **Step 2: Commit any cleanups if needed**
