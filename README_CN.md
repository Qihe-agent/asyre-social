<div align="center">

# Asyre Social

**统一社媒内容创作 — AI 图片生成 + 精排版引擎 + 品牌管理。**

![License](https://img.shields.io/badge/License-MIT-blue)
![Styles](https://img.shields.io/badge/AI%20Styles-12-brightgreen)
![Layouts](https://img.shields.io/badge/Layouts-8-orange)
![Brands](https://img.shields.io/badge/Brands-3%2B-blueviolet)

[**English**](README.md)

</div>

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

12 种视觉风格，同一主题「AI 改变商业」的不同演绎：

| | |
|---|---|
| ![cute](assets/styles/cute-ai-business.png) | ![fresh](assets/styles/fresh-ai-business.png) |
| **cute** — 甜美可爱少女风 | **fresh** — 清新自然 |
| ![warm](assets/styles/warm-ai-business.png) | ![bold](assets/styles/bold-ai-business.png) |
| **warm** — 温暖亲切 | **bold** — 高冲击力 |
| ![minimal](assets/styles/minimal-ai-business.png) | ![retro](assets/styles/retro-ai-business.png) |
| **minimal** — 极简高级 | **retro** — 复古怀旧 |
| ![pop](assets/styles/pop-ai-business.png) | ![notion](assets/styles/notion-ai-business.png) |
| **pop** — 活力四射 | **notion** — 极简线条画，知性 |
| ![chalkboard](assets/styles/chalkboard-ai-business.png) | ![study-notes](assets/styles/study-notes-ai-business.png) |
| **chalkboard** — 粉笔黑板风 | **study-notes** — 手写笔记照片风 |
| ![screen-print](assets/styles/screen-print-ai-business.png) | ![tuisheng](assets/styles/tuisheng-ai-business.png) |
| **screen-print** — 丝网印刷海报风 | **tuisheng** — 暗色赛博学术风 |

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

**同样 21 种布局，手绘中文版：**

| | | |
|---|---|---|
| ![](assets/infographic-cn/bento-grid.png) | ![](assets/infographic-cn/bridge.png) | ![](assets/infographic-cn/circular-flow.png) |
| ![](assets/infographic-cn/funnel.png) | ![](assets/infographic-cn/iceberg.png) | ![](assets/infographic-cn/hierarchical-layers.png) |
| ![](assets/infographic-cn/hub-spoke.png) | ![](assets/infographic-cn/dashboard.png) | ![](assets/infographic-cn/tree-branching.png) |
| ![](assets/infographic-cn/venn-diagram.png) | ![](assets/infographic-cn/jigsaw.png) | ![](assets/infographic-cn/winding-roadmap.png) |

**同样 21 种布局，金色粒子暗黑概念艺术风：**

| | | |
|---|---|---|
| ![](assets/infographic-gold/bento-grid.png) | ![](assets/infographic-gold/bridge.png) | ![](assets/infographic-gold/circular-flow.png) |
| ![](assets/infographic-gold/funnel.png) | ![](assets/infographic-gold/iceberg.png) | ![](assets/infographic-gold/hierarchical-layers.png) |
| ![](assets/infographic-gold/hub-spoke.png) | ![](assets/infographic-gold/dashboard.png) | ![](assets/infographic-gold/tree-branching.png) |
| ![](assets/infographic-gold/venn-diagram.png) | ![](assets/infographic-gold/jigsaw.png) | ![](assets/infographic-gold/winding-roadmap.png) |

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

## 致谢

- **[baoyu-xhs-images](https://github.com/JimLiu/baoyu-skills)** by JimLiu — 小红书信息图生成引擎
- **Asyre Design System** — 品牌管理与反 AI slop 质量体系

## License

MIT License. 详见 [LICENSE](LICENSE)。

---

<div align="center">

**别再做千篇一律的内容。做有品牌感的东西。**

![Asyre](https://img.shields.io/badge/Asyre-Social-black?style=for-the-badge)

Powered by [**Asyre**](https://github.com/Qihe-agent)

</div>
