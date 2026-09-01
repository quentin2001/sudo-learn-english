# 📚 sudo-learn-english

> **An $i+1$ Comprehensible Input Knowledge-Base** – 原汁原味英文原著泛读、苏格拉底式 AI 启发内化与个人语块沉淀体系。

---

[![Methodology](https://img.shields.io/badge/SLA_Theory-Krashen_i%2B1-brightgreen)](docs/methodology-guide.md)
[![Reading Stage](https://img.shields.io/badge/Current_Stage-Phase_1_(Flow_&_Confidence)-blue)](docs/methodology-guide.md#三-进阶选书阶梯-the-3-phase-roadmap)
[![Books Read](https://img.shields.io/badge/Books_Completed-1-orange)](books/)
[![Words Absorbed](https://img.shields.io/badge/Words_Absorbed-~25%2C000+-purple)](books/)
[![License](https://img.shields.io/badge/license-MIT-lightgrey)](LICENSE)

---

## 🎯 核心理念与体系 (Core Philosophy)

本项目基于**斯蒂芬·克拉申（Stephen Krashen）的 $i+1$ 可理解性输入假说（Comprehensible Input）** 构建：

1. **零查词心流阅读（Flow Input）**：精选 95%+ 容易理解的原著，阅读中不查生词，靠上下文猜义，建立英文直接理解回路。
2. **苏格拉底式启发对话（Socratic AI Dialogue）**：读完后与 AI 针对情节和哲理用英文碰撞思想，每轮实现“观点共鸣 + 1~2个地道语块升级 + 延伸追问”。
3. **一书一档深度沉淀（Book Archives）**：提炼高价值语块（Collocations），通过“个人生活微造句”将消极词汇转化为终身积极能力。

> 📖 **完整方法论手册**：详见 [《i+1 英文原著阅读与深度内化方法论指南》](docs/methodology-guide.md)

---

## 📊 阅读里程碑看板 (Milestone Dashboard)

| 统计指标 (Metric) | 当前数据 (Current Value) | 目标 / 说明 (Target & Level) |
| :--- | :--- | :--- |
| **已完本书籍 (Books Finished)** | **1 本** | 🎯 短期目标：5 本经典入门原著 |
| **在读书籍 (Currently Reading)** | **1 本** (进度 ~50%) | 《Who Moved My Cheese?》 |
| **累计吸收字数 (Words Absorbed)** | **~25,000+ words** | 🎯 第一阶段目标：100,000 words |
| **当前所处阶梯 (Stage)** | **Phase 1: 建立心流与语感** | 寓言/儿童文学/极简自控类 |
| **平均阅读速度 (Avg WPM)** | **~120 - 150+ WPM** | 提速明显，语流感显著增强 |

---

## 📚 原图书架索引 (Bookshelf Index)

| 序号 | 书籍名称 (Title) | 体裁与分类 | 词数 (Words) | $i+1$ 难度 | 状态 (Status) | 档案链接 (Archive) |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: |
| 01 | **The Little Prince** (小王子) | 哲学童话 / 文学寓言 | ~15,000 | ⭐⭐⭐ | `Completed` ✅ | [查看档案](books/01-the-little-prince.md) |
| 02 | **Who Moved My Cheese?** (谁动了我的奶酪) | 职场寓言 / 个人成长 | ~10,000 | ⭐⭐ | `Reading` ⏳ | [查看档案](books/02-who-moved-my-cheese.md) |
| - | *新书档案模板* | - | - | - | `Template` | [使用模板](books/_template.md) |

---

## 📂 仓库结构目录 (Directory Structure)

```
.
├─ docs/
│   ├─ methodology-guide.md   # 核心指南：i+1 理论、阅读守则与内化 SOP
│   └─ 把你的英语用起来.pdf     # 经典方法论电子书原著
├─ toolbooks/
│   └─ 01-把你的英语用起来.md   # 方法论精读与实战指南（全书拆解）
├─ skills/
│   └─ esheep-pick-enbooks/   # 智能选书 Skill（量化标准与决策卡片）
├─ books/
│   ├─ _template.md           # 标准一书一档模板
│   ├─ 01-the-little-prince.md # 第 1 本书：《小王子》完本与语块档案
│   └─ 02-who-moved-my-cheese.md # 第 2 本书：《谁动了我的奶酪》在读与打卡
├─ ESLPOD.md                  # 听力与日常训练笔记（历史归档）
├─ speak.md                   # 口语与连读节奏笔记（历史归档）
├─ README.md                  # 知识库主页与动态看板
└─ .gitignore                 # 过滤过程与临时构建文件
```

---

## 🚀 极简阅读工作流 (Quick Workflow)

```
[选书] -> [零查词通读] -> [与 AI 对话] -> [建立档案/微造句] -> [更新主页]
```

1. **选书**：根据 [选书阶梯](docs/methodology-guide.md#三-进阶选书阶梯-the-3-phase-roadmap) 挑选一本 95% 以上词汇都认识的书。
2. **通读**：遵循 **3 秒法则**，全程不查词典，一口气读完，保护心流。
3. **内化对话**：读完后对 AI 说：`“我刚刚读完了《书名》，我们来进行启发式内化探讨吧！”`
4. **归档**：复制 `books/_template.md`，记录本次探讨感悟与 5~10 个核心语块的场景微造句。

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