# sudo-learn-english

个人英语学习知识库与进度记录仓库。包含学习方法论、学习日志、原著与工具书笔记、语法总结以及配套的词汇分析工具。

---

## 目录结构

```text
.
├── playbook.md          # 英语学习方法论与各专项执行规划
├── journal.md           # 学习打卡与阶段复盘日志
│
├── books/               # 图书与学习资料
│   ├── corpus/          # 英文原著
│   │   ├── notes/       # 原著阅读笔记与读后归档
│   │   └── ebooks/      # 原著电子书（本地存放，不上传）
│   ├── toolbooks/       # 学习工具书与教材
│   │   ├── notes/       # 工具书学习笔记（音标、发音、学习方法等）
│   │   └── ebooks/      # 工具书电子书（本地存放，不上传）
│   └── nce/             # 新概念英语资料（本地存放，不上传）
│
├── grammar/             # 语法专项
│   └── tenses.md        # 英语时态归纳与用法解析
│
├── engine/              # 辅助学习工具与数据
│   ├── scripts/         # 词汇提取、分级与统计脚本
│   ├── data/            # CEFR 词汇库与个人词汇表数据
│   └── skills/          # 选书评估规则与技能配置
│
└── README.md            # 仓库说明文档
```

---

## 内容概览

### 1. 核心规划与日志
* **[playbook.md](playbook.md)**：个人英语学习方法论体系，包含二语习得理念（可理解性输入 $i+1$）、学习方法、逆向回译质检流程以及发音、语法、阅读等各专项学习路线与资料索引。
* **[journal.md](journal.md)**：日常学习记录，包含 Sprint 阶段目标、每日打卡用时、练习内容与复盘。

### 2. 图书与教材笔记 (`books/`)
* **英文原著阅读笔记 (`books/corpus/notes/`)**：
  * [The Little Prince (小王子)](books/corpus/notes/01-the-little-prince.md)
  * [Who Moved My Cheese? (谁动了我的奶酪)](books/corpus/notes/02-who-moved-my-cheese.md)
  * [阅读笔记模板](books/corpus/notes/_template.md)
* **工具书精读笔记 (`books/toolbooks/notes/`)**：
  * [把你的英语用起来！](books/toolbooks/notes/01-把你的英语用起来.md)
  * [赖世雄美语音标](books/toolbooks/notes/02-赖世雄美语音标.md)
  * [Mastering the American Accent](books/toolbooks/notes/03-Mastering%20the%20American%20Accent.md)
  * [American Accent Training](books/toolbooks/notes/04-American%20Accent%20Training.md)

### 3. 语法专项 (`grammar/`)
* **[tenses.md](grammar/tenses.md)**：12 大英语时态的构成规则、核心概念与典型用法归纳。

### 4. 工具与数据 (`engine/`)
* **`engine/scripts/`**：包含 `learner.py`、`build_lexicon.py` 等脚本，用于文本分词、CEFR 词汇等级分析及生词提取。
* **`engine/data/`**：存放 Oxford 3000/5000 CEFR 词汇表及个人词汇数据库。
* **`engine/skills/`**：包含原著选书与文本难度评估的技能配置。

---

## 说明
* 电子书教材及大文件（如各 `ebooks/` 目录及 `books/nce/`）仅在本地保留，已加入 `.gitignore`，不提交至 Git 仓库。