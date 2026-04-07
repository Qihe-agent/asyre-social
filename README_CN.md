<div align="center">

# Asyre Graphic

**统一社媒内容创作 — AI 图片生成 + 精排版引擎 + 品牌管理。**

*好内容值得好画面。28 万种视觉组合，一键出图。*

*内容决定深度，配图决定触达。*

*写完文章的那一刻，配图就该准备好了。*

![License](https://img.shields.io/badge/License-MIT-blue)
![AI Styles](https://img.shields.io/badge/AI%20%E9%A3%8E%E6%A0%BC-20-brightgreen)
![Infographic Layouts](https://img.shields.io/badge/%E4%BF%A1%E6%81%AF%E5%9B%BE%E5%B8%83%E5%B1%80-23-yellow)
![Infographic Styles](https://img.shields.io/badge/%E4%BF%A1%E6%81%AF%E5%9B%BE%E9%A3%8E%E6%A0%BC-20-orange)
![Text Molds](https://img.shields.io/badge/%E6%8E%92%E7%89%88%E6%A8%A1%E5%85%B7-6-red)
![Density](https://img.shields.io/badge/%E5%AF%86%E5%BA%A6-6%20%E6%A1%A3-purple)
![Brands](https://img.shields.io/badge/%E5%93%81%E7%89%8C-5%20%E5%9B%BD%E9%A3%8E-blueviolet)
![Embed](https://img.shields.io/badge/%E5%B5%8C%E5%85%A5%E6%8A%80%E6%B3%95-10-teal)
![Claude Code](https://img.shields.io/badge/Claude%20Code-Ready-black)
![OpenClaw](https://img.shields.io/badge/OpenClaw-%E5%85%BC%E5%AE%B9-green)

[**English**](README.md)

</div>

---

## 为什么好内容需要好配图

一篇深度文章如果只是白底黑字发到社交媒体，没有人会停下来看。

**内容决定深度，配图决定触达。** 同样的洞察，用一张精心设计的视觉卡片呈现，阅读完成率可以提升 3-5 倍。但传统做法需要设计师、工具链、反复沟通——这个成本让大多数内容创作者望而却步。

Asyre Social 的目标很简单：**你只管写好内容，配图的事交给系统。**

### 这套系统能产生多少种视觉组合？

| 维度 | 选项数 | 说明 |
|------|--------|------|
| AI 生图风格 | 20 | cute, notion, cyberpunk 等 |
| XHS 卡片布局 | 8 | sparse, dense, flow, mindmap 等 |
| 信息图布局 | 23 | funnel, iceberg, bridge, SWOT 等 |
| 信息图风格 | 20 | 手绘、像素、黏土、蓝图等 |
| 排版模具 | 6 | 多卡、长图、信息图、漫画等 |
| 内容密度 | 6 | 稀疏 → 极密 |
| 品牌 | 5+ | 墨金、素启、暖荷、朱砂、青瓷 + 自定义 |
| 嵌入技法 | 10 | Hero、裁切、网格、滤镜、叠加等 |

**数学组合**：

- **Mode A 单图**：20 风格 × 8 布局 = **160 种** XHS 卡片组合
- **Mode A 信息图**：23 布局 × 20 风格 = **460 种**信息图组合
- **Mode B 排版**：6 模具 × 6 密度 × 5 品牌 = **180 种**排版组合
- **Mode C 混合**：160 封面选项 × 180 内容页选项 × 10 嵌入技法 = **288,000+ 种**混合组合

> **总计：超过 28 万种不同的视觉组合。**

而且这还只是预设选项。AI 可以根据你的具体内容**即兴生成完全定制的风格** —— 不在这 28 万种之内的、独一无二的视觉方案。你描述你想要的感觉，系统就能做出来。

每新增一个品牌、一个风格、一种布局，组合数都是乘法增长。这就是模块化设计的威力。

---

## 三种模式，一个技能

| 模式 | 引擎 | 适用场景 | 输出 |
|------|------|---------|------|
| **A: AI 直出** | Gemini 图片生成 | 封面、海报、信息图 | AI 生成 PNG |
| **B: 精排版** | HTML/CSS → Playwright → PNG | 长文、深度内容、多页卡片 | 1080×1440 分页 PNG |
| **C: 混合** | A + B 结合 | 系列内容（AI封面 + 文字内容页） | 混合 PNG 系列 |

AI 根据内容自动选择最佳模式 — 也可以用 `--mode=ai`、`--mode=text`、`--mode=hybrid` 手动指定。

---

## AI 风格库（Mode A）

20 种视觉风格，同一主题「AI 改变商业」的不同演绎：

| | | | |
|---|---|---|---|
| ![](assets/styles/cute-ai-business.png) | ![](assets/styles/fresh-ai-business.png) | ![](assets/styles/warm-ai-business.png) | ![](assets/styles/bold-ai-business.png) |
| **cute** 甜美 | **fresh** 清新 | **warm** 温暖 | **bold** 冲击 |
| ![](assets/styles/minimal-ai-business.png) | ![](assets/styles/retro-ai-business.png) | ![](assets/styles/pop-ai-business.png) | ![](assets/styles/notion-ai-business.png) |
| **minimal** 极简 | **retro** 复古 | **pop** 活力 | **notion** 知性 |
| ![](assets/styles/chalkboard-ai-business.png) | ![](assets/styles/study-notes-ai-business.png) | ![](assets/styles/screen-print-ai-business.png) | ![](assets/styles/tuisheng-ai-business.png) |
| **chalkboard** 黑板 | **study-notes** 笔记 | **screen-print** 海报 | **tuisheng** 墨金 |
| ![](assets/styles/kawaii.png) | ![](assets/styles/pixel-art.png) | ![](assets/styles/claymation.png) | ![](assets/styles/origami.png) |
| **kawaii** 卡通 | **pixel-art** 像素 | **claymation** 黏土 | **origami** 折纸 |
| ![](assets/styles/cyberpunk-neon.png) | ![](assets/styles/storybook-watercolor.png) | ![](assets/styles/ikea-manual.png) | ![](assets/styles/morandi-journal.png) |
| **cyberpunk** 霓虹 | **watercolor** 水彩 | **ikea** 说明书 | **morandi** 莫兰迪 |

每种风格可与 8 种布局（稀疏、平衡、密集、列表、对比、流程、脑图、象限）自由组合，另有 23+ 场景预设。

### 预设示例

预设 = 风格 + 布局一键组合。同一主题的三种预设效果：

| | |
|---|---|
| ![knowledge-card](assets/presets/preset-knowledge-card.png) | ![tutorial](assets/presets/preset-tutorial.png) |
| **knowledge-card** — notion + dense（知识卡） | **tutorial** — chalkboard + flow（教程） |

![poster](assets/presets/preset-poster.png)

*poster — screen-print + sparse（海报）*

---

## 信息图引擎（21 种布局 × 20 种风格）

高密度信息可视化 — 单张结构化信息图。以 *technical-schematic* 科技蓝图风展示：

| | | |
|---|---|---|
| ![](assets/infographic-layouts/bento-grid.png) | ![](assets/infographic-layouts/bridge.png) | ![](assets/infographic-layouts/circular-flow.png) |
| **bento-grid** | **bridge** | **circular-flow** |
| ![](assets/infographic-layouts/comparison-table.png) | ![](assets/infographic-layouts/binary-comparison.png) | ![](assets/infographic-layouts/comparison-matrix.png) |
| **comparison-table** | **binary-comparison** | **comparison-matrix** |
| ![](assets/infographic-layouts/funnel.png) | ![](assets/infographic-layouts/iceberg.png) | ![](assets/infographic-layouts/hierarchical-layers.png) |
| **funnel** | **iceberg** | **hierarchical-layers** |
| ![](assets/infographic-layouts/hub-spoke.png) | ![](assets/infographic-layouts/tree-branching.png) | ![](assets/infographic-layouts/linear-progression.png) |
| **hub-spoke** | **tree-branching** | **linear-progression** |
| ![](assets/infographic-layouts/dashboard.png) | ![](assets/infographic-layouts/isometric-map.png) | ![](assets/infographic-layouts/periodic-table.png) |
| **dashboard** | **isometric-map** | **periodic-table** |
| ![](assets/infographic-layouts/venn-diagram.png) | ![](assets/infographic-layouts/jigsaw.png) | ![](assets/infographic-layouts/winding-roadmap.png) |
| **venn-diagram** | **jigsaw** | **winding-roadmap** |
| ![](assets/infographic-layouts/comic-strip.png) | ![](assets/infographic-layouts/story-mountain.png) | ![](assets/infographic-layouts/dense-modules.png) |
| **comic-strip** | **story-mountain** | **dense-modules** |
| ![](assets/infographic-layouts/structural-breakdown.png) | ![](assets/infographic-layouts/swot-analysis.png) | ![](assets/infographic-layouts/radar-chart.png) |
| **structural-breakdown** | **swot-analysis** | **radar-chart** |

**同样布局，手绘中文版：**

| | | |
|---|---|---|
| ![](assets/infographic-cn/bento-grid.png) | ![](assets/infographic-cn/bridge.png) | ![](assets/infographic-cn/circular-flow.png) |
| **bento-grid** | **bridge** | **circular-flow** |
| ![](assets/infographic-cn/funnel.png) | ![](assets/infographic-cn/iceberg.png) | ![](assets/infographic-cn/hierarchical-layers.png) |
| **funnel** | **iceberg** | **hierarchical-layers** |
| ![](assets/infographic-cn/hub-spoke.png) | ![](assets/infographic-cn/dashboard.png) | ![](assets/infographic-cn/tree-branching.png) |
| **hub-spoke** | **dashboard** | **tree-branching** |
| ![](assets/infographic-cn/venn-diagram.png) | ![](assets/infographic-cn/jigsaw.png) | ![](assets/infographic-cn/winding-roadmap.png) |
| **venn-diagram** | **jigsaw** | **winding-roadmap** |

**同样布局，金色粒子暗黑概念艺术风：**

| | | |
|---|---|---|
| ![](assets/infographic-gold/bento-grid.png) | ![](assets/infographic-gold/bridge.png) | ![](assets/infographic-gold/circular-flow.png) |
| **bento-grid** | **bridge** | **circular-flow** |
| ![](assets/infographic-gold/funnel.png) | ![](assets/infographic-gold/iceberg.png) | ![](assets/infographic-gold/hierarchical-layers.png) |
| **funnel** | **iceberg** | **hierarchical-layers** |
| ![](assets/infographic-gold/hub-spoke.png) | ![](assets/infographic-gold/dashboard.png) | ![](assets/infographic-gold/tree-branching.png) |
| **hub-spoke** | **dashboard** | **tree-branching** |
| ![](assets/infographic-gold/venn-diagram.png) | ![](assets/infographic-gold/jigsaw.png) | ![](assets/infographic-gold/winding-roadmap.png) |
| **venn-diagram** | **jigsaw** | **winding-roadmap** |

每种布局可搭配 20 种视觉风格：手工质感、古典学术、黏土动画、赛博霓虹、宜家说明书、折纸、像素艺术、技术蓝图等。

---

## 精排版引擎（Mode B）

像素级精准的文字渲染 — HTML/CSS + Playwright → 1080×1440 PNG。没有 AI 文字扭曲，数据卡片、对比表格、编号行动清单——全部用清晰字体渲染。

### 五个品牌 × 六种密度

同一内容「AI 改变商业」，在所有品牌/密度组合下的效果：

**墨金（暗色赛博学术）**

| | | | | | |
|---|---|---|---|---|---|
| ![](assets/mode-b/mojin-sparse.png) | ![](assets/mode-b/mojin-light.png) | ![](assets/mode-b/mojin-balanced.png) | ![](assets/mode-b/mojin-medium.png) | ![](assets/mode-b/mojin-dense.png) | ![](assets/mode-b/mojin-ultra.png) |
| 稀疏 | 轻量 | 平衡 | 微密 | 密集 | 极密 |

**素启（商务专业）**

| | | | | | |
|---|---|---|---|---|---|
| ![](assets/mode-b/suqi-sparse.png) | ![](assets/mode-b/suqi-light.png) | ![](assets/mode-b/suqi-balanced.png) | ![](assets/mode-b/suqi-medium.png) | ![](assets/mode-b/suqi-dense.png) | ![](assets/mode-b/suqi-ultra.png) |
| 稀疏 | 轻量 | 平衡 | 微密 | 密集 | 极密 |

**暖荷（暖色个人）**

| | | | | | |
|---|---|---|---|---|---|
| ![](assets/mode-b/nuanhe-sparse.png) | ![](assets/mode-b/nuanhe-light.png) | ![](assets/mode-b/nuanhe-balanced.png) | ![](assets/mode-b/nuanhe-medium.png) | ![](assets/mode-b/nuanhe-dense.png) | ![](assets/mode-b/nuanhe-ultra.png) |
| 稀疏 | 轻量 | 平衡 | 微密 | 密集 | 极密 |

**朱砂（大胆冲击）**

| | | | | | |
|---|---|---|---|---|---|
| ![](assets/mode-b/zhusa-sparse.png) | ![](assets/mode-b/zhusa-light.png) | ![](assets/mode-b/zhusa-balanced.png) | ![](assets/mode-b/zhusa-medium.png) | ![](assets/mode-b/zhusa-dense.png) | ![](assets/mode-b/zhusa-ultra.png) |
| 稀疏 | 轻量 | 平衡 | 微密 | 密集 | 极密 |

**青瓷（雅致清新）**

| | | | | | |
|---|---|---|---|---|---|
| ![](assets/mode-b/qingci-sparse.png) | ![](assets/mode-b/qingci-light.png) | ![](assets/mode-b/qingci-balanced.png) | ![](assets/mode-b/qingci-medium.png) | ![](assets/mode-b/qingci-dense.png) | ![](assets/mode-b/qingci-ultra.png) |
| 稀疏 | 轻量 | 平衡 | 微密 | 密集 | 极密 |

密度由 AI 根据内容量自动选择。密集/极密模式必须用实际内容填满整页，不靠拉伸间距凑数。

### 6 种渲染模具

| 模具 | 输出 | 适用场景 |
|------|------|---------|
| 多卡 (`-m`) | 每页 1080×1440 | 小红书系列、社媒卡片 |
| 长图 (`-l`) | 1080×自适应高度 | 单张长卡片 |
| 信息图 (`-i`) | 1080×自适应高度 | 数据可视化 |
| 视觉笔记 (`-v`) | 1080×自适应高度 | 手绘风格 |
| 漫画 (`-c`) | 1080×自适应高度 | 黑白漫画 |
| 白板 (`-w`) | 1080×自适应高度 | 结构化框图 |

特性：自动色调感知、数据卡片、对比表格、金句高亮、首字下沉、垂直居中、品牌 CSS 注入。

---

## 混合模式（Mode C）— AI 概念图 × HTML 精排版

AI 生成的概念艺术直接嵌入像素级精准的 HTML 卡片。10 种嵌入技法，完全融合品牌系统。

| | |
|---|---|
| ![dark](assets/mode-c/embed-showcase-dark.png) | ![light](assets/mode-c/embed-showcase-light.png) |
| **墨金 暗色主题** | **素启 亮色主题** |

![original](assets/mode-c/embed-showcase-original.png)

*10 种技法：Hero 背景图、异形裁切、图片网格、CSS 滤镜、文字叠加、内联 SVG、渐变边框、内联配图、圆形头像、浮动卡片。全部通过 Playwright 渲染，AI 图片以 base64 内嵌。*

---

## 品牌系统

每个客户拥有自己的视觉身份 — 覆盖 AI 生图和 HTML 排版两条路径。

### 内置品牌

| 品牌 | 视觉风格 | 适用场景 |
|------|---------|---------|
| **墨金** | 暗色 + 金/青，赛博学术 | 社群知识、深度分析 |
| **素启** | 商务亮色，墨绿强调 | 客户报告、方案交付 |
| **暖荷** | 暖纸质感，赭色温度 | 个人小红书、朋友圈 |
| **朱砂** | 暗红 + 朱红，大胆冲击 | 强观点、高冲击内容 |
| **青瓷** | 淡青 + 翠绿，雅致清新 | 生活方式、美学分享 |

### 创建你的品牌

首次使用时回答 3 个问题：
1. 目标受众
2. 品牌个性（3个词）
3. 美学方向（暗色/亮色/温暖/极简）

系统自动生成 `brand.json` + `base.css` + `ai-style.md` — 一套完整的视觉系统。

---

## 安装

### Claude Code

```bash
git clone https://github.com/Qihe-agent/asyre-social ~/.claude/skills/asyre-social
```

使用：
```
/asyre-social
```

### OpenClaw

```bash
clawhub install asyre-social
```

### 其他 AI 工具

将 `SKILL.md` 作为 system prompt，引用支持文件即可。

---

## 使用方法

```bash
/asyre-social [主题或内容]                           # 自动检测模式
/asyre-social article.md --mode=text                 # 强制精排版
/asyre-social --mode=ai --preset=knowledge-card      # AI + 预设
/asyre-social --brand=tuisheng                       # 指定品牌
/asyre-social article.md --yes                       # 非交互模式
```

---

## 文件结构

```
asyre-social/
├── SKILL.md                         # 核心工作流（AI 读取这个文件）
├── openclaw.plugin.json             # OpenClaw 插件配置
├── brands/
│   ├── _template/brand-template.json  # 新品牌模板
│   ├── tuisheng/                    # 暗色赛博学术品牌
│   ├── asher/                       # 暖色个人品牌
│   └── qihe/                        # 商务专业品牌
├── references/
│   ├── routing.md                   # 模式路由决策树
│   ├── taste.md                     # 反 AI slop 品味准则
│   ├── ai-gen/                      # AI 生图参考
│   ├── text-render/                 # 精排版参考
│   └── config/                      # 配置参考
├── scripts/                         # 渲染脚本
└── templates/                       # HTML 模板
```

## 使用流程

**第一步：创建品牌** — 回答 3 个问题（受众、个性、美学方向），自动生成完整视觉系统：配色、字体、AI 生图约束、HTML 渲染 CSS。

**第二步：提供内容** — 文章、数据、要点，或者只给一个主题。AI 分析内容密度，推荐最佳模式。

**第三步：拿到结果** — Mode A 生成 AI 信息图，Mode B 渲染精排版卡片，Mode C 两者结合。全部自动套用你的品牌视觉。

## 30 个使用场景

内容为王。有了好内容 + 品牌系统，任何场景都能出专业级视觉：

### 个人品牌 & 小红书

| # | 场景 | 模式 | 说明 |
|---|------|------|------|
| 1 | 知识分享卡片 | B | 把洞察变成多页卡片系列，数据卡+金句高亮 |
| 2 | 个人品牌封面 | A | AI 生成品牌风格封面图 |
| 3 | 干货长图 | B | 单张长图知识卡，排版精美+图表 |
| 4 | 避坑指南 | A+B | 冲击力封面 + 详细文字拆解 |
| 5 | 读书笔记 | B | 笔记风格，高亮+批注 |
| 6 | 个人故事系列 | C | AI 氛围封面 + 暖色文字内容页 |

### 商务 & 客户交付

| # | 场景 | 模式 | 说明 |
|---|------|------|------|
| 7 | 客户提案封面 | A | 企业品牌风格的专业信息图 |
| 8 | 商业计划摘要 | B | 密集卡片：数据卡+对比表+行动清单 |
| 9 | 竞品分析 | A | 二元对比或 SWOT 信息图 |
| 10 | 季度报告卡片 | B | 仪表盘风格指标展示 |
| 11 | 产品发布海报 | A | 海报风或大胆风格 |
| 12 | 投资者简报 | C | AI 概念封面 + 数据密集内容页 |

### 教育 & 教程

| # | 场景 | 模式 | 说明 |
|---|------|------|------|
| 13 | 教程步骤图 | A | 黑板风或流程布局信息图 |
| 14 | 知识地图 | A | 中心辐射或树状分支布局 |
| 15 | 课程笔记卡 | B | 笔记密度+金句检测 |
| 16 | 考试复习卡 | B | 极密模式，所有要点塞满一页 |
| 17 | 概念解释图 | A | 冰山或桥梁布局做概念可视化 |
| 18 | 学习路线图 | A | 蜿蜒路线或时间线布局 |

### 营销 & 社媒

| # | 场景 | 模式 | 说明 |
|---|------|------|------|
| 19 | 产品对比图 | A | 对比表或二元对比布局 |
| 20 | 活动宣传海报 | A | 大胆风或赛博霓虹风格 |
| 21 | 数据驱动故事 | C | AI 数据可视化 + 文字分析 |
| 22 | 用户证言卡 | B | 引用卡片+圆形头像嵌入 |
| 23 | 品牌价值观 | B | 稀疏居中金句，品牌风格 |
| 24 | 社媒内容日历 | A | 元素周期表布局做内容规划 |

### 深度内容 & 思想领导力

| # | 场景 | 模式 | 说明 |
|---|------|------|------|
| 25 | 深度分析文章 | B | 多页密集卡片，完整长文排版 |
| 26 | 行业趋势报告 | C | AI 概念艺术 + 数据表 + 行动清单 |
| 27 | 框架/模型图 | A | 层级金字塔或结构分解布局 |
| 28 | 观点输出卡 | B | 微密密度+高亮引用 |
| 29 | 圆桌讨论摘要 | B | 多卡片，不同发言者分区 |
| 30 | 年度复盘 | C | AI 封面 + 时间线 + 指标 + 反思 |

### 完整工作流示例

```
1. /asyre-social --brand=mojin
   → 加载墨金品牌（暗金赛博风）

2. 粘贴你的文章或数据
   → AI 分析内容：2000字深度文章 → 推荐 Mode B

3. 确认方案
   → 策略 B (信息密集) / 密度 Dense / 品牌 墨金

4. 生成 4 页卡片
   → 01.png 标题页（稀疏）
   → 02.png 数据页（平衡 + 数据卡片）
   → 03.png 对比页（微密 + 对比表）
   → 04.png 行动页（密集 + 行动清单）

5. 发布到小红书
```

## License

MIT License. 详见 [LICENSE](LICENSE)。

---

<div align="center">

**别再做千篇一律的内容。做有品牌感的东西。**

![Asyre](https://img.shields.io/badge/Asyre-Social-black?style=for-the-badge)

</div>
