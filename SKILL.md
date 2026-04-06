---
name: asyre-social
description: |
  Asyre 社媒内容创作系统。融合 AI 图片直出 + 精排版引擎 + 品牌管理。
  三种模式：Mode A (AI 信息图直出), Mode B (HTML 精排版), Mode C (混合)。
  12 种 AI 生图风格 × 8 布局 × 23+ 预设 + 6 种排版模具 + 客户品牌系统。
  触发词: /asyre-social, 社媒, 小红书, 做卡片, 排版, 信息图, XHS, RedNote, 内容卡片
user-invocable: true
---

# Asyre Social — 统一社媒内容创作系统

## 1. Overview + Quick Start

Asyre Social 把四个独立技能融合为一个统一入口：AI 图片生成、精排版引擎、品牌系统、内容润色。

三种输出模式：

| Mode | Engine | Best For | Output |
|------|--------|----------|--------|
| **A: AI 直出** | Gemini AI image generation | 封面、海报、简单信息图 | AI-generated PNG |
| **B: 精排版** | HTML/CSS → Playwright → PNG | 长文、深度内容、多页卡片 | 1080×1440 PNG pages |
| **C: 混合** | A + B combined | 系列内容（封面AI + 内容精排） | Mixed PNG series |

### Quick Start

```bash
/asyre-social [topic or content]                    # Auto-detect mode
/asyre-social article.md --mode=text                # Force text layout
/asyre-social --mode=ai --style=notion --preset=knowledge-card
/asyre-social --brand=tuisheng                      # Use brand
/asyre-social article.md --yes                      # Non-interactive, skip confirmations
```

### Options

| Flag | Values | Default | Description |
|------|--------|---------|-------------|
| `--mode` | `ai`, `text`, `hybrid`, `auto` | `auto` | 强制指定输出模式 |
| `--brand` | brand slug | project default | 使用指定品牌配置 |
| `--style` | 12 styles (see Section 5) | auto from analysis | AI 生图风格 |
| `--layout` | 8 layouts (see Section 5) | auto from analysis | AI 生图布局 |
| `--preset` | 23+ presets | none | 预设快捷方式（覆盖 style+layout） |
| `--mold` | `-m`, `-l`, `-i`, `-v`, `-c`, `-w` | `-m` | Mode B 排版模具 |
| `--yes` | flag | off | 非交互模式，跳过所有确认 |

---

## 2. Mode Routing Decision Tree ★ CRITICAL

**AI 必须先读本节再做任何事。** 所有请求先经过路由决策，确定输出模式。

```
STEP 1: Check explicit override
  --mode=ai     → Mode A
  --mode=text   → Mode B
  --mode=hybrid → Mode C
  --mode=auto   → continue to Step 2 (default)

STEP 2: Content signal analysis

  Compute these signals from input:
  - char_count        = total characters in source content
  - page_estimate     = char_count / 300
  - has_data          = content contains numbers/stats/percentages (bool)
  - is_visual_request = content mentions "封面", "海报", "cover", "poster" (bool)
  - text_density      = average chars per logical section
  - content_type      = inferred type (article/tutorial/list/visual/mixed)

  ROUTING TABLE:
  ┌──────────────────────────────────────────────┬────────┐
  │ Condition                                    │ Mode   │
  ├──────────────────────────────────────────────┼────────┤
  │ is_visual_request (封面/海报/单图)             │  A     │
  │ page_estimate ≤ 2 AND visual-first content   │  A     │
  │ page_estimate ≥ 4 AND text_density > 200     │  B     │
  │ content_type = long-form article             │  B     │
  │ content_type = tutorial AND pages ≥ 5        │  B     │
  │ page_estimate 3-5, mixed signals             │  C     │
  │ DEFAULT (ambiguous or short mixed content)   │  C     │
  └──────────────────────────────────────────────┴────────┘

STEP 3: Brand adjustment (optional)
  - If brand.json has ai_style.preferred_mode, treat as suggestion
  - Content signals ALWAYS override brand preference
  - Example: brand prefers Mode A, but 2000-char article → Mode B wins

STEP 4: Brief confirmation
  Output: "将以 [Mode X: 名称] 模式生成。确认？"
  If --yes flag → skip confirmation, proceed directly
```

**Edge cases:**
- Empty input (just a topic keyword) → Mode A (generate visual from topic)
- URL input → fetch content → re-analyze signals
- Image input → Mode A (use as reference)
- Markdown file → read file → analyze signals

Reference: `{skill_dir}/references/routing.md` for extended decision logic.

---

## 3. Brand System

### 3.1 Loading a Brand

```
Step 0.1: Check --brand flag → if present, use it
Step 0.2: If no flag, scan {skill_dir}/brands/ for project default (default.json)
Step 0.3: If no brand found → offer first-time brand setup (see 3.3)
Step 0.4: Read {skill_dir}/brands/{brand}/brand.json
Step 0.5: Apply brand to current mode:
  - Mode A: Read {skill_dir}/brands/{brand}/ai-style.md
            → inject color constraints + negative prompts into Gemini prompt
  - Mode B: Read {skill_dir}/brands/{brand}/base.css
            → inject into HTML template as {{CUSTOM_CSS}}
  - Mode C: Both of the above
```

### 3.2 brand.json Schema

```json
{
  "name": "brand-slug",
  "display_name": "Brand Display Name",
  "description": "One-line brand description",
  "palette": {
    "primary": "#HEX",
    "secondary": "#HEX",
    "accent": "#HEX",
    "background": "#HEX",
    "text": "#HEX",
    "muted": "#HEX"
  },
  "typography": {
    "heading_font": "font-family string",
    "body_font": "font-family string",
    "accent_font": "font-family string or null"
  },
  "ai_style": {
    "preferred_mode": "A|B|C|null",
    "default_style": "style slug",
    "default_layout": "layout slug",
    "color_keywords": ["dark", "gold", "cyan"],
    "negative_prompts": ["cartoon", "childish"],
    "texture_keywords": ["grain", "matte"]
  },
  "assets": {
    "avatar": "{skill_dir}/brands/{brand}/avatars/avatar.jpg",
    "backgrounds": "{skill_dir}/brands/{brand}/backgrounds/",
    "logo": "{skill_dir}/brands/{brand}/logo.png"
  },
  "defaults": {
    "author": "Author Name",
    "watermark": "Watermark Text",
    "tags_separator": " × "
  }
}
```

### 3.3 First-Time Brand Setup

When no brand exists for a client, ask 3 questions:

1. **受众是谁？** — Target audience (e.g., "25-35岁职场人", "技术从业者")
2. **品牌个性用3个词描述** — (e.g., "专业、温暖、有深度")
3. **美学方向** — 暗色 / 亮色 / 温暖 / 极简 / 赛博 / 自定义

Then:
1. Fork the nearest existing brand as template
2. Generate `brand.json` with adjusted palette + typography
3. Generate `base.css` with CSS variables matching palette
4. Generate `ai-style.md` with color constraints for Gemini
5. Save all to `{skill_dir}/brands/{client}/`
6. Set as project default

### 3.4 Available Brands

| Brand | Slug | Look | Best For |
|-------|------|------|----------|
| 推升 | `tuisheng` | 暗色+金/青，赛博学术，颗粒质感 | 深度知识分享，社群内容 |
| Asher | `asher` | 暖纸质感，米色+棕，手写温度 | 小红书个人号，朋友圈 |
| 启合 | `qihe` | 商务蓝+白，专业干净，几何线条 | 客户报告，方案交付 |

---

## 4. Shared Workflow

**所有模式共享 Step 0–4。Step 4 之后分流到各模式的专属流水线。**

### Step 0: Load Preferences + Brand ⛔ BLOCKING

加载顺序（优先级从高到低）：
1. 命令行参数 (`--brand`, `--style`, etc.)
2. 项目级 `EXTEND.md`（当前目录或 `.asyre/EXTEND.md`）
3. XDG config: `$XDG_CONFIG_HOME/asyre-social/EXTEND.md`
4. 用户级: `~/.asyre-social/EXTEND.md`

加载品牌（见 Section 3.1）。

`--yes` 模式：找不到配置就用默认值，跳过 setup 向导。

### Step 1: Analyze Content → analysis.md

按 `{skill_dir}/references/ai-gen/workflows/analysis-framework.md` 执行：

1. **内容分类** — article / tutorial / list / opinion / review / news / story
2. **Hook 分析** — 标题吸引力评分 (1-10)，改进建议
3. **目标受众** — 推断读者画像
4. **视觉机会点** — 哪些段落适合可视化、哪些数据适合图表
5. **关键信息提取** — 核心论点、金句、数据点
6. **自动推荐** — mode + strategy + style + layout + mold

保存到 `analysis.md`。

### Step 1.5: Fact-Check + Logic Gap Analysis

**主动检查用户原始内容中的问题：**

1. **事实核查** — 数据、引用、品牌名、价格、日期是否准确？
   - 可验证的声明：标注置信度 (✅ 确认 / ⚠️ 可疑 / ❌ 错误)
   - 不可验证的声明：标注"无法验证"
2. **逻辑漏洞** — 论证链条是否完整？有无跳跃、因果倒置、偷换概念？
3. **信息缺口** — 读者读完会不会有"然后呢？""怎么做？"的疑问？

Output format:
```
📋 内容理解确认
  主题：[topic]
  核心论点：[thesis]
  目标读者：[audience]

⚠️ 事实核查问题（如有）
  - [item]: [issue] → [suggestion]

🔗 逻辑补强建议（如有）
  - [gap]: [suggestion]

❓ 信息缺口（如有）
  - [question readers might have]
```

如果发现 ❌ 级别错误，**必须暂停**，通知用户修正后再继续。
⚠️ 级别：标注但继续。✅ 级别：无需提示。

### Step 2: Smart Confirm ⚠️ REQUIRED

**`--yes` 模式**: 跳过确认，使用 Step 1 的推荐方案直接执行。

**交互模式** — 展示推荐方案：

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 内容分析
  主题：[topic] | 类型：[content_type]
  字数：[char_count] | 预估页数：[page_estimate]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎨 推荐方案
  模式：[A/B/C]（[reason]）
  策略：[A/B/C] | 风格：[style] | 布局：[layout]
  品牌：[brand] | 模具：[mold]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ 事实核查：[N issues found / all clear]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

提供 3 个选项（AskUserQuestion）：
1. ✅ **确认，直接生成**（推荐）
2. 🎛️ **自定义调整** — 修改 mode/style/layout/brand/mold
3. 📋 **详细模式** — 生成 3 套大纲 → 用户选择

### Step 2.5: Humanize Content 🧹 (Optional)

**Purpose**: 用 humanizer-bilingual 润色，去AI味，加人味。

- **中文处理**：去官腔、去教科书病、去"值得注意的是"、加口语温度、保留专业度
- **英文处理**：去AI高频词 (delve, tapestry, landscape, leverage)、加 voice、varied sentence length
- **双语内容**：分别处理，保持各自语感

Rules:
- 保存润色结果到 `humanized.md`
- 原文 `source.md` 不动
- 如果用户内容本身已经很好（人味足），标注"无需润色"并跳过

### Step 2.6: Draft Confirmation ⚠️ BLOCKING

- 显示润色前后对比（diff 高亮关键变化）
- 用户满意 → 进入 Step 3
- 用户不满意 → 根据反馈修改 → 再次展示 → 循环
- **未确认前绝不进入 Step 3**
- `--yes` 模式：自动确认润色结果

### Step 3: Generate Outline

基于 `analysis.md` + `humanized.md`（定稿后文案），生成大纲。

三种策略可选：
- **Strategy A (Story-Driven)** — 叙事驱动，hook → conflict → insight → resolution
- **Strategy B (Information-Dense)** — 信息密集，模块化，每页一个核心点
- **Strategy C (Visual-First)** — 视觉优先，大图+少文字，冲击力导向

大纲包含：
- 每页的标题、核心内容、视觉方向
- 文字量估算（chars per page）
- Mode A 页面的 prompt 方向
- Mode B 页面的排版提示

保存到 `outline.md`。

### Step 4: Confirm Outline + Mode + Style

展示大纲概览，确认后分流：
- **Mode A** → Section 5
- **Mode B** → Section 6
- **Mode C** → Section 7

---

## 5. Mode A — AI Image Generation

### 5.1 Style Gallery (12 Styles)

| # | Style | Slug | Look | Best For |
|---|-------|------|------|----------|
| 1 | Notion 风格 | `notion` | 极简线条+柔和色块 | 知识卡片、教程 |
| 2 | 杂志排版 | `magazine` | 大字标题+留白+高级感 | 观点文、金句 |
| 3 | 手绘风 | `sketch` | 铅笔/马克笔手绘质感 | 教程、笔记 |
| 4 | 赛博朋克 | `cyberpunk` | 霓虹+暗色+故障效果 | 科技、未来 |
| 5 | 学术海报 | `academic` | 论文排版风+数据图表 | 研究、数据 |
| 6 | 复古胶片 | `retro` | 胶片色调+颗粒+褪色 | 故事、回忆 |
| 7 | 扁平插画 | `flat` | 几何色块+扁平人物 | 产品介绍、列表 |
| 8 | 水彩风 | `watercolor` | 水彩晕染+手写字 | 文艺、生活方式 |
| 9 | 暗黑极简 | `dark-minimal` | 纯黑底+白字+一点亮色 | 高端、商务 |
| 10 | 纸质温暖 | `paper-warm` | 米色纸张+手写+印章 | 个人分享、朋友圈 |
| 11 | 3D 渲染 | `3d-render` | 3D物体+柔和光影 | 产品、概念 |
| 12 | 推升定制 | `tuisheng` | 暗色+金/青+学术+赛博 | 推升社群内容 |

### 5.2 Layout Gallery (8 Layouts)

| # | Layout | Slug | Structure | Best For |
|---|--------|------|-----------|----------|
| 1 | 中心标题 | `center-title` | 大标题居中+副标题+底部信息 | 封面 |
| 2 | 左右分栏 | `split` | 左文右图或左图右文 | 对比、产品 |
| 3 | 上图下文 | `top-image` | 60%图+40%文字 | 场景+说明 |
| 4 | 网格 | `grid` | 2×2 或 3×3 网格 | 多项列表 |
| 5 | 时间线 | `timeline` | 纵向时间轴+节点 | 流程、历史 |
| 6 | 数据仪表盘 | `dashboard` | 数字+图表+指标 | 数据展示 |
| 7 | 引用卡 | `quote` | 大引号+金句+署名 | 金句、观点 |
| 8 | 全出血 | `full-bleed` | 全幅背景图+叠加文字 | 封面、海报 |

### 5.3 Preset Gallery

23+ 预设快捷方式，每个预设 = style + layout + 特定提示词组合。

Reference: `{skill_dir}/references/ai-gen/style-presets.md`

常用预设：

| Preset | Style | Layout | Use Case |
|--------|-------|--------|----------|
| `knowledge-card` | notion | center-title | 知识点卡片 |
| `data-story` | academic | dashboard | 数据故事 |
| `quote-poster` | magazine | quote | 金句海报 |
| `tech-breakdown` | cyberpunk | grid | 技术拆解 |
| `warm-share` | paper-warm | top-image | 个人分享 |
| `tuisheng-cover` | tuisheng | full-bleed | 推升封面 |

### 5.4 Generation Process

1. **Image 1 (cover)**: Generate without `--ref`，建立视觉基调
2. **Images 2+**: Generate with `--ref <image-01>`，确保视觉一致性
3. **Session ID**: `social-{slug}-{timestamp}`，同 session 所有图片共享

Generation per image:
```
1. Assemble prompt from: outline + style definition + layout template + brand constraints
2. Add text overlay instructions (exact text, position, size)
3. Send to Gemini image generation
4. Validate output: text legibility, layout compliance, color accuracy
5. If validation fails → adjust prompt → retry (max 2 retries)
6. Save to output directory with sequential naming
```

### 5.5 Brand Color Injection

Read `{skill_dir}/brands/{brand}/ai-style.md` → extract:
- **Color constraints**: "use #1A1A2E as background, #D4A520 as accent"
- **Negative prompts**: "avoid bright colors, no cartoon style"
- **Texture keywords**: "add film grain, matte finish"

Inject into Gemini prompt as hard constraints (placed before content-specific instructions).

### 5.6 Multi-Panel Stitch Mode

当风格为 tuisheng 或文字密度高时，自动切换到拼接模式：

1. 生成 3 张横向面板 (3:2 比例) 而非 1 张竖向图 (3:4)
2. 每张面板承载 ~1/3 内容 → 文字更清晰
3. 拼接命令：
```bash
convert panel-1.png panel-2.png panel-3.png -append combined.png
```

Auto-detection rules:
- `tuisheng` style → 默认启用拼接
- Other styles → 仅当 total text > 100 chars 时启用
- 可通过 `--no-stitch` 强制关闭

### 5.7 Image Generation Skill

优先使用 `image-gen` skill（如果可用）。Fallback 到 `nano-banana-pro`。

所有图片使用相同 Session ID，确保风格一致。

---

## 6. Mode B — Precision Text Layout

### 6.1 Rendering Pipeline

```
Markdown
  → Parse blocks: title / subtitle / paragraph / callout / image / highlight / divider / list
  → Detect tone (see 6.3)
  → Apply brand CSS from {skill_dir}/brands/{brand}/base.css
  → Generate HTML: template + content blocks + CSS variables
  → Playwright screenshot → 1080×1440 PNG (or auto-height for long/infograph)
```

### 6.2 Six Molds

| Mold | Flag | Dimensions | Best For |
|------|------|------------|----------|
| 多卡 (Multi-Card) | `-m` | 1080×1440 per page | 小红书系列卡片 **(DEFAULT)** |
| 长图 (Long Image) | `-l` | 1080×auto | 单张长图，朋友圈 |
| 信息图 (Infograph) | `-i` | 1080×auto | 数据可视化，流程图 |
| 视觉笔记 (Visual Note) | `-v` | 1080×auto | 手绘风格笔记 |
| 漫画 (Comic) | `-c` | 1080×auto | 黑白漫画分格 |
| 白板 (Whiteboard) | `-w` | 1080×auto | 结构化框图，思维导图 |

Auto-selection (when no `--mold` specified):
- 小红书系列内容 → `-m` (multi-card)
- 单张知识卡片 → `-l` (long)
- 数据密集型内容 → `-i` (infograph)
- 教程/步骤类 → `-v` (visual note) or `-w` (whiteboard)
- 故事/对话类 → `-c` (comic)

### 6.3 Tone Detection

Keyword scan → weighted scoring → highest tone wins (threshold ≥ 3 keyword hits):

| Tone | Accent Color | Secondary Color | Signal Keywords |
|------|-------------|-----------------|-----------------|
| strategic | `#D4A520` gold | `#2D6A4F` green | 战略、投资、市场、增长、ROI、商业模式 |
| tech | `#40B8B8` teal | `#3D5A80` blue | 架构、AI、代码、算法、系统、API、部署 |
| philosophical | `#C4A55A` warm gold | `#8B5E3C` brown | 认知、思维、本质、悖论、第一性原理 |
| literary | `#C08050` ochre | `#6B4E3D` umber | 故事、写作、文字、叙事、隐喻、意象 |

If no tone reaches threshold → default to brand's primary accent color.

Tone colors are injected as CSS variables:
```css
:root {
  --tone-accent: #D4A520;
  --tone-secondary: #2D6A4F;
}
```

Reference: `{skill_dir}/references/text-render/tone-detection.md`

### 6.4 Typography Rules

**Body text**: ≥ 38px (mobile readable, non-negotiable)

**Dropcap**: First page, first paragraph only
- Size: 128px
- Color: tone accent color
- Font: brand heading font
- Span: 3 lines of body text

**Golden sentence auto-highlight**:
- Detection: standalone sentence ≤ 25 characters, not a heading
- Style: gold left border (4px) + faint background (accent color at 8% opacity)
- Max 2 per page to avoid over-decoration

**Overflow protection** (critical for multi-card):
1. **Measure**: Calculate rendered height of all content blocks
2. **Bin**: Distribute blocks across pages with 1440px budget per page
3. **Verify**: Playwright renders → check actual height
4. **Rollback**: If overflow detected → re-bin with tighter budget → re-render

Reference: `{skill_dir}/references/text-render/typography.md`

### 6.5 AI Images in Text Layout (Optional)

Mode B can embed AI-generated concept images inline:

1. Identify key sections that benefit from visual metaphor
2. Use Mode A engine to generate concept art (same brand constraints)
3. Insert into Markdown as `![metaphor description](path/to/generated.png)`
4. `render_pages.py` embeds images as base64 → renders inline in HTML
5. Image sizing: max 60% page width, centered, with 16px margin

This is **optional** and only triggered when:
- User requests it explicitly
- Analysis identifies high-impact visual opportunities
- `--no-inline-images` to disable

### 6.6 Rendering Commands

**Multi-card (default for Mode B):**
```bash
python3 {skill_dir}/scripts/render_pages.py \
  --input humanized.md \
  --output ./pages/ \
  --background {skill_dir}/brands/{brand}/backgrounds/texture.png \
  --avatar {skill_dir}/brands/{brand}/avatars/avatar.jpg \
  --author "Author Name" \
  --date "2026-04-06" \
  --tags "Tag1 × Tag2" \
  --watermark "Brand" \
  --tone auto
```

**Single long image:**
```bash
python3 {skill_dir}/scripts/render_single.py \
  --input humanized.md \
  --output ./output/ \
  --mold long \
  --background {skill_dir}/brands/{brand}/backgrounds/texture.png \
  --avatar {skill_dir}/brands/{brand}/avatars/avatar.jpg \
  --author "Author Name"
```

**Playwright capture (for content-card molds):**
```bash
node {skill_dir}/scripts/capture.js <html-file> <output-png> 1080 1440
```

**Infograph / Visual Note / Comic / Whiteboard:**
```bash
python3 {skill_dir}/scripts/render_single.py \
  --input humanized.md \
  --output ./output/ \
  --mold [infograph|visual-note|comic|whiteboard]
```

---

## 7. Mode C — Hybrid

### 7.1 Structure

| Page | Mode | Engine | Why |
|------|------|--------|-----|
| Cover (P1) | A | Gemini AI | 视觉冲击力，抓眼球 |
| Content (P2–Pn) | B | HTML/Playwright | 精确排版，文字可读 |
| Ending (last) | A or B | Depends | A = 视觉收尾; B = CTA 文字 |

Decision for ending page:
- If ending has call-to-action text → Mode B
- If ending is a visual summary/mood → Mode A
- Default: Mode A (visual closure)

### 7.2 Color Consistency Rules

**This is the core value of Mode C** — unified visual language across AI and HTML pages.

- Brand colors used for **BOTH** AI generation **AND** HTML rendering
- AI cover: `brands/{brand}/ai-style.md` color constraints → Gemini prompt
- Text pages: `brands/{brand}/base.css` → matching CSS variables
- Tone detection colors are also aligned with brand palette
- Result: 翻页时颜色不跳，从封面到正文到结尾是一体的

### 7.3 Workflow

1. Generate outline with page-level mode assignments (from Step 3)
2. Render Mode A pages first (cover + any visual pages)
3. Extract dominant colors from AI output → verify against brand palette
4. Render Mode B pages with brand CSS (already aligned)
5. Assemble final sequence with consistent file naming

### 7.4 File Naming

```
output/
├── 01-cover-[slug].png          # Mode A generated
├── 02-content-[slug].png        # Mode B rendered
├── 03-content-[slug].png        # Mode B rendered
├── 04-content-[slug].png        # Mode B rendered
├── ...
└── NN-ending-[slug].png         # Mode A or B
```

Sequential numbering ensures correct order on all platforms.

---

## 8. Output + Delivery

### 8.1 Output Directory Structure

```
{output_root}/asyre-social/{topic-slug}/
├── source.md                    # Original content (untouched)
├── humanized.md                 # Humanized draft (if modified)
├── analysis.md                  # Content analysis results
├── outline.md                   # Selected outline
├── prompts/                     # AI generation prompts (Mode A/C only)
│   ├── 01-cover-[slug].md
│   ├── 02-[slug].md
│   └── ...
├── 01-cover-[slug].png          # Final output images
├── 02-content-[slug].png
├── 03-content-[slug].png
└── ...
```

`{output_root}` defaults to current working directory. Override with `--output`.

### 8.2 Completion Report

生成完成后输出：

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Asyre Social Complete!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Topic:    [topic]
  Mode:     [A/B/C] ([mode name])
  Brand:    [brand]
  Strategy: [A/B/C] ([strategy name])
  Style:    [style] | Layout: [layout]
  Mold:     [mold] (Mode B only)
  Images:   N total
  Location: [absolute path]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 8.3 Image Modification

生成后的修改操作：

| Action | Steps |
|--------|-------|
| **Edit single image** | 1. Update prompt (Mode A) or markdown section (Mode B) → 2. Regenerate that image only → 3. Replace in output |
| **Add image** | 1. Specify insertion position → 2. Create prompt/content → 3. Generate → 4. Renumber all subsequent files |
| **Delete image** | 1. Remove file → 2. Renumber remaining → 3. Update outline.md |
| **Regenerate all** | 1. Re-run from Step 4 with same outline → 2. Overwrite output |
| **Change style** | 1. Update style → 2. Regenerate all Mode A images → 3. Mode B unaffected unless brand changes |

---

## 9. Reference Index

### AI Generation References
- `{skill_dir}/references/ai-gen/presets/` — 12 style definition files
- `{skill_dir}/references/ai-gen/elements/canvas.md` — canvas sizing, aspect ratios
- `{skill_dir}/references/ai-gen/elements/decorations.md` — borders, corners, badges
- `{skill_dir}/references/ai-gen/elements/image-effects.md` — grain, blur, glow
- `{skill_dir}/references/ai-gen/elements/typography.md` — AI text rendering rules
- `{skill_dir}/references/ai-gen/workflows/analysis-framework.md` — content analysis
- `{skill_dir}/references/ai-gen/workflows/outline-strategies.md` — 3 outline strategies
- `{skill_dir}/references/ai-gen/workflows/prompt-assembly.md` — prompt construction
- `{skill_dir}/references/ai-gen/style-presets.md` — 23+ preset definitions

### Text Rendering References
- `{skill_dir}/references/text-render/engine.md` — Playwright rendering pipeline
- `{skill_dir}/references/text-render/tone-detection.md` — tone scoring + color mapping
- `{skill_dir}/references/text-render/typography.md` — font sizes, dropcap, golden sentences, overflow

### Quality
- `{skill_dir}/references/taste.md` — Anti-AI-slop quality gates, visual taste rules

### Config
- `{skill_dir}/references/config/first-time-setup.md` — Brand setup wizard flow
- `{skill_dir}/references/config/preferences-schema.md` — EXTEND.md schema definition

### Brands
- `{skill_dir}/brands/{brand}/brand.json` — Visual identity config
- `{skill_dir}/brands/{brand}/base.css` — HTML rendering styles
- `{skill_dir}/brands/{brand}/ai-style.md` — AI generation color/style constraints
- `{skill_dir}/brands/{brand}/avatars/` — Avatar images
- `{skill_dir}/brands/{brand}/backgrounds/` — Background textures

---

## Notes

- **Portable paths**: Always use `{skill_dir}` prefix for file references within this skill
- **Image generation**: Prefer `image-gen` skill; fallback to `nano-banana-pro`
- **Environment**: `GEMINI_API_KEY` required for Mode A and Mode C
- **Playwright**: Required for Mode B; depends on content-card `node_modules`
- **ImageMagick**: Required for multi-panel stitch (`convert` command)
- **Font loading**: Ensure CJK fonts (Noto Sans CJK, LXGW WenKai) are installed on render host
- **Output size**: Target ≤ 500KB per PNG for social platform upload limits
