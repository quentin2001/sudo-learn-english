# 📚 sudo-learn-english

> **An $i+1$ Comprehensible Input Knowledge-Base** – 原汁原味英文原著泛读、苏格拉底式 AI 启发内化与个人语块沉淀体系。

---

[![Playbook](https://img.shields.io/badge/Master_Playbook-SLA_OS-brightgreen)](playbook.md)
[![Learning Log](https://img.shields.io/badge/Learning_Log-Sprint_01-blueviolet)](journal.md)
[![Reading Stage](https://img.shields.io/badge/Current_Stage-Phase_1_(Flow_&_Confidence)-blue)](engine/skills/esheep-pick-enbooks/SKILL.md)
[![Books Read](https://img.shields.io/badge/Books_Completed-1-orange)](books/corpus/ebooks/)
[![Words Absorbed](https://img.shields.io/badge/Words_Absorbed-~25%2C000+-purple)](books/corpus/notes/)
[![License](https://img.shields.io/badge/license-MIT-lightgrey)](LICENSE)

---

## 🎯 核心理念与体系 (Core Philosophy)

本项目基于**斯蒂芬·克拉申（Stephen Krashen）的 $i+1$ 可理解性输入假说（Comprehensible Input）** 构建：

1. **零查词心流阅读（Flow Input）**：精选 95%+ 容易理解的原著，阅读中不查生词，靠上下文猜义，建立英文直接理解回路。
2. **苏格拉底式启发对话（Socratic AI Dialogue）**：读完后与 AI 针对情节和哲理用英文碰撞思想，每轮实现“观点共鸣 + 1~2个地道语块升级 + 延伸追问”。
3. **一书一档深度沉淀（Book Archives）**：提炼高价值语块（Collocations），通过“个人生活微造句”将消极词汇转化为终身积极能力。

> 🧠 **个人方法论总纲**：详见 [《个人英语习得底层操作系统 (Master Playbook)》](playbook.md)  
> 📅 **学习与打卡日志**：详见 [《个人学习实战与成长日志 (Learning Journal)》](journal.md)  
> 📖 **工具书精读拆解**：详见 [《把你的英语用起来！精读指南与学习蓝图》](books/toolbooks/notes/01-把你的英语用起来.md)

---

## 📊 阅读里程碑看板 (Milestone Dashboard)

| 统计指标 (Metric) | 当前数据 (Current Value) | 目标 / 说明 (Target & Level) |
| :--- | :--- | :--- |
| **已完本书籍 (Books Finished)** | **1 本** | 🎯 短期目标：5 本经典入门原著 |
| **在读书籍 (Currently Reading)** | **1 本** (进度 ~50%) | 《Who Moved My Cheese?》 |
| **累计吸收字数 (Words Absorbed)** | **~25,000+ words** | 🎯 第一阶段目标：100,000 words |
| **当前所处阶梯 (Stage)** | **Phase 1: 建立心流与语感** | 寓言/儿童文学/极简自控类 |
| **当前冲刺周期 (Current Sprint)** | **Sprint 01 (语音筑基与心流)** | 详见 [`journal.md`](journal.md) |

---

## 📚 原图书架索引 (Bookshelf Index)

| 序号 | 书籍名称 (Title) | 体裁与分类 | 词数 (Words) | $i+1$ 难度 | 状态 (Status) | 资源与档案 (Links) |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: |
| 01 | **The Little Prince** (小王子) | 哲学童话 / 文学寓言 | ~15,000 | ⭐⭐⭐ | `Completed` ✅ | [📖 全彩插图版 PDF](books/corpus/ebooks/01-the-little-prince.pdf) · [📝 读后档案](books/corpus/notes/01-the-little-prince.md) |
| 02 | **Who Moved My Cheese?** (谁动了我的奶酪) | 职场寓言 / 个人成长 | ~10,000 | ⭐⭐ | `Reading` ⏳ | [📖 插图版 PDF](books/corpus/ebooks/02-who-moved-my-cheese.pdf) · [📝 在读打卡](books/corpus/notes/02-who-moved-my-cheese.md) |
| - | *新书档案模板* | - | - | - | `Template` | [使用模板](books/corpus/notes/_template.md) |

---

## 📂 仓库结构目录 (Directory Structure)

```
.
├── 🧠 playbook.md        # 📘【个人方法论总纲】我的英语习得底层操作系统（融会贯通）
├── 📅 journal.md         # 📝【实战学习日志】全周期时间投入、每日打卡流水与冲刺复盘
│
├─ books/                 # 📚 核心图书与笔记大库
│   ├─ corpus/            # 📖 英文原版原著区（英语阅读实践）
│   │   ├─ ebooks/        # 高清插图版原著 PDF（《小王子》全彩原版、《谁动了我的奶酪》）
│   │   └─ notes/         # 一书一档读后精读与语块档案（01-小王子.md、02-奶酪.md）
│   └─ toolbooks/         # 🛠️ 英语学习工具书与方法论区（认知与心法）
│       ├─ ebooks/        # 高清工具书 PDF（《把你的英语用起来.pdf》）
│       └─ notes/         # 工具书全本精读与行动指南（01-把你的英语用起来.md）
│
├─ engine/                # ⚙️ 后台技术与数据引擎
│   ├─ skills/            # 🧠 智能工具技能（esheep-pick-enbooks 选书 Skill）
│   ├─ scripts/           # 💻 语料分析与词汇追踪工具（直接分析 PDF）
│   │   ├─ learner.py     # 词频与 CEFR 难度分析 CLI
│   │   ├─ build_lexicon.py # 词库拓展构建脚本
│   │   └─ init_data.py   # 数据初始化脚本
│   └── data/             # 📊 词汇图谱与用户画像数据库
│
├─ README.md              # 知识库主页与动态看板
└─ .gitignore             # 过滤过程与临时构建文件
```

---

## 🚀 极简阅读工作流 (Quick Workflow)

```
[选书] -> [读插图 PDF] -> [与 AI 对话] -> [建立档案/微造句] -> [更新主页]
```

1. **选书**：使用 [`engine/skills/esheep-pick-enbooks/SKILL.md`](engine/skills/esheep-pick-enbooks/SKILL.md) 评估或根据 [100本原著难度表](books/toolbooks/notes/01-把你的英语用起来.md#附录-22经典畅销英文原著-100-本难度全览表) 挑选一本 95% 以上词汇都认识的书。
2. **通读**：打开 `books/corpus/ebooks/` 中的**插图版 PDF**，遵循 **3 秒法则**，全程不查词典，一口气读完，保护心流。
3. **内化对话**：读完后对 AI 说：`“我刚刚读完了《书名》，我们来进行启发式内化探讨吧！”`
4. **归档**：复制 `books/corpus/notes/_template.md`，记录本次探讨感悟与 5~10 个核心语块的场景微造句。

---

## 💻 The Runtime Environment

```bash
$ user@brain:~$ echo $LANG
zh_CN.UTF-8

$ user@brain:~$ sudo apt-get install i+1-comprehensible-input
[sudo] password for user: **********
> Authenticating...
> Downloading: The Little Prince [COMPLETED - 15,000 words]
> Downloading: Who Moved My Cheese? [IN PROGRESS - 50%]
> Unpacking fluency-engine-v2.0...
> Neural pathways compiling without dictionary lag... [OK]
> Comprehension rate: 95%+
> Status: Flow state unlocked. Ready for the next chapter.
```