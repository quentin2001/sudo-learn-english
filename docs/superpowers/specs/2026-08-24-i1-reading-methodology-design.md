# System Design: i+1 English Reading & Deep Internalization Framework

## 1. Context & Motivation

The user has recently completed their first full English book (*The Little Prince*) completely without looking up unknown words in a dictionary, relying purely on context, enjoying the story, and achieving a high level of comprehension. They have also started their second book (*Who Moved My Cheese?*) and noticed a visible increase in reading speed.

This project reconstructs the `sudo-learn-english` repository around **Stephen Krashen's $i+1$ Comprehensible Input Theory (可理解性输入)** and **Deep Semantic Internalization (深度语义内化)**. The goal is to provide a complete, low-friction, scientifically grounded system for reading English books, discussing them with AI to transform passive vocabulary into active usage, and archiving reading progress and key linguistic collocations.

---

## 2. Core Architecture: The 3-Phase Closed Loop

```
┌─────────────────────────────────────────────────────────────┐
│                 Phase 1: 纯粹心流输入 (Flow Input)             │
│   • 严格遵循 i+1 选书原则（95%+ 理解度，如《小王子》《奶酪》）         │
│   • 全程不查词典、不中断阅读，依靠上下文自然猜义与建立语流感           │
└──────────────────────────────┬──────────────────────────────┘
                               │ 读完章节 / 完本书籍
                               ▼
┌─────────────────────────────────────────────────────────────┐
│             Phase 2: 苏格拉底式启发对话 (Socratic AI)          │
│   • 观点与故事驱动：围绕情节、人物抉择、哲学寓意展开讨论            │
│   • 每轮机制：【思想共鸣】 + 【1~2个原书地道语块升级】 + 【延伸追问】│
│   • 目标：将“消极认知识别”转化为“积极表达与思考”                    │
└──────────────────────────────┬──────────────────────────────┘
                               │ 对话结束 / 提炼沉淀
                               ▼
┌─────────────────────────────────────────────────────────────┐
│               Phase 3: 一书一档沉淀 (Book Archives)          │
│   • `books/NN-book-name.md`                                 │
│   • 包含：阅读元数据（字数/耗时/难度）、思想感悟、5~10个核心语块卡片 │
│   • `README.md` 聚合看板：总字数、书架看板、进阶里程碑               │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. Detailed Specifications

### 3.1 `docs/methodology-guide.md` ($i+1$ 阅读与内化方法论指南)

This document serves as the permanent philosophical and practical handbook of the repository:
1. **二语习得核心理论 (SLA Theoretical Foundations)**:
   - **Krashen's $i+1$ Hypothesis**: Why input must be comprehensible ($i+1$) rather than overwhelming ($i+3$).
   - **Affective Filter Hypothesis**: Why zero-anxiety and reading pleasure maximize language acquisition.
   - **Incidental Vocabulary Acquisition (附带词汇习得)**: Why words stick after encountering them 7-12 times in context versus rote memorization.
   - **Narrow Reading Strategy (窄读策略)**: Why reading similar difficulty/genre books builds compound interest.
2. **阅读实操守则 (Reading Practice Rules)**:
   - "3-Second Rule" for unknown words: Guess or skip within 3 seconds; never pause to check a dictionary unless a word recurs $\ge 5$ times and completely blocks plot understanding.
   - 95% Comprehension Rule for book selection.
3. **读后内化标准作业程序 (Post-Reading Internalization SOP)**:
   - How to initiate Socratic Dialogue with AI.
   - The "Chunk + Collocation + Micro-Transfer" formula for active vocabulary.
   - Periodic review and mental compounding.

---

### 3.2 `books/_template.md` (标准书籍档案模板)

Every book will have its own dedicated markdown file under `books/` using this template:
- **Header & Metadata**:
  - Book Title, Author, Release Year, Genre.
  - Difficulty Rating: $\text{⭐}$ to $\text{⭐⭐⭐⭐⭐}$ (Subjective $i+1$ level).
  - Word Count, Estimated Total Reading Time, Calculated Average WPM (Words Per Minute).
  - Reading Status: `Reading` / `Completed` / `Shelved`.
  - Date Started & Date Finished.
- **Part 1: 核心故事与哲学梗概 (Core Plot & Philosophy)**:
  - 1-2 sentence core message.
  - Personal resonance (What touched you the most).
- **Part 2: AI 苏格拉底式启发对话精选 (Key Dialogue & Reflections)**:
  - 1-2 highlight Q&A turns where user expressed personal perspectives and AI refined phrasing.
- **Part 3: 核心语块与场景微迁移库 (Active Collocations & Micro-Transfer)**:
  - 5~10 high-value linguistic chunks extracted from the book.
  - Format per chunk:
    ```markdown
    #### 1. [Chunk / Collocation]
    - **释义/语感**：...
    - **原书例句**：> "..."
    - **个人生活微造句 (Micro-Transfer)**：*...*
    ```
- **Part 4: 读后复盘与评分 (Post-Reading Review)**:
  - Comprehension rate estimate (e.g. 95%).
  - Reading speed & flow score.

---

### 3.3 Initial Book Records

1. **`books/01-the-little-prince.md`**:
   - Status: `Completed`.
   - Word count: ~15,000 words.
   - Pre-populated with structured metadata, core themes (taming, essential matters, childlike wonder), and starter collocations ready for the upcoming interactive discussion.
2. **`books/02-who-moved-my-cheese.md`**:
   - Status: `Reading` (~50% progress).
   - Word count: ~10,000 words.
   - Ready for tracking today's reading session and subsequent completion debrief.

---

### 3.4 `README.md` (知识库主页与动态看板)

Modernize the root `README.md` into an inspiring, clean dashboard:
1. **Status & Milestones Dashboard**:
   - Total Books Finished: `1 / ∞`
   - Total Words Absorbed: `~15,000 words`
   - Current Level: `Phase 1 (Flow & Confidence Building)`
2. **Bookshelf Index (原图书架)**:
   - Table linking each book title to its `books/NN-*.md` file with genre, words, difficulty, status, and completion date.
3. **Quick Start & Workflow Guide**:
   - How to pick next book.
   - How to launch post-reading AI discussion.
   - How to record and update stats.

---

## 4. Spec Review & Non-Functional Requirements

- **Zero Friction**: Clean markdown structure without requiring complex runtime dependencies.
- **Extensible**: Designed so future CLI / Python automation scripts (e.g. automatic WPM calculators, badge generators) can easily parse the frontmatter/metadata of `books/*.md`.
- **Pure Pedagogy Alignment**: Fully adheres to SLA comprehensible input and Socratic feedback loops.
