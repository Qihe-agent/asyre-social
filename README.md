<div align="center">

# Asyre Social

**Unified social media content creation — AI image generation + precision text layout + brand management.**

![License](https://img.shields.io/badge/License-MIT-blue)
![Styles](https://img.shields.io/badge/AI%20Styles-12-brightgreen)
![Layouts](https://img.shields.io/badge/Layouts-8-orange)
![Brands](https://img.shields.io/badge/Brands-3%2B-blueviolet)

[**中文版**](README_CN.md)

</div>

---

## Three Modes, One Skill

| Mode | Engine | Best For | Output |
|------|--------|----------|--------|
| **A: AI Direct** | Gemini image generation | Covers, posters, infographics | AI-generated PNG |
| **B: Precision Layout** | HTML/CSS → Playwright → PNG | Long-form, text-heavy, multi-page | 1080×1440 PNG pages |
| **C: Hybrid** | A + B combined | Content series (AI cover + text pages) | Mixed PNG series |

The AI automatically selects the best mode based on your content — or you can override with `--mode=ai`, `--mode=text`, or `--mode=hybrid`.

---

## AI Style Gallery (Mode A)

12 visual styles for AI-generated infographics. Same topic — *"AI Transforms Business"* — rendered in every style:

| | |
|---|---|
| ![cute](assets/styles/cute-ai-business.png) | ![fresh](assets/styles/fresh-ai-business.png) |
| **cute** — Sweet, adorable, girly | **fresh** — Clean, refreshing, natural |
| ![warm](assets/styles/warm-ai-business.png) | ![bold](assets/styles/bold-ai-business.png) |
| **warm** — Cozy, friendly, approachable | **bold** — High impact, attention-grabbing |
| ![minimal](assets/styles/minimal-ai-business.png) | ![retro](assets/styles/retro-ai-business.png) |
| **minimal** — Ultra-clean, sophisticated | **retro** — Vintage, nostalgic, trendy |
| ![pop](assets/styles/pop-ai-business.png) | ![notion](assets/styles/notion-ai-business.png) |
| **pop** — Vibrant, energetic, eye-catching | **notion** — Minimalist line art, intellectual |
| ![chalkboard](assets/styles/chalkboard-ai-business.png) | ![study-notes](assets/styles/study-notes-ai-business.png) |
| **chalkboard** — Chalk on blackboard, educational | **study-notes** — Handwritten photo style |
| ![screen-print](assets/styles/screen-print-ai-business.png) | ![tuisheng](assets/styles/tuisheng-ai-business.png) |
| **screen-print** — Bold poster art, halftone textures | **tuisheng** — Dark cyber-academic, gold/teal |

Each style combines with 8 layouts (sparse, balanced, dense, list, comparison, flow, mindmap, quadrant) and 23+ presets for quick setup.

### Preset Examples

Presets = style + layout in one flag. Three popular presets on the same topic:

| | |
|---|---|
| ![knowledge-card](assets/presets/preset-knowledge-card.png) | ![tutorial](assets/presets/preset-tutorial.png) |
| **knowledge-card** — notion + dense | **tutorial** — chalkboard + flow |

![poster](assets/presets/preset-poster.png)

*poster — screen-print + sparse*

---

## Infographic Engine (21 Layouts × 20 Styles)

High-density information visualization — single-image infographics with structured layouts. Shown in *technical-schematic* style:

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

**Same 21 layouts in craft-handmade Chinese style:**

| | | |
|---|---|---|
| ![](assets/infographic-cn/bento-grid.png) | ![](assets/infographic-cn/bridge.png) | ![](assets/infographic-cn/circular-flow.png) |
| ![](assets/infographic-cn/funnel.png) | ![](assets/infographic-cn/iceberg.png) | ![](assets/infographic-cn/hierarchical-layers.png) |
| ![](assets/infographic-cn/hub-spoke.png) | ![](assets/infographic-cn/dashboard.png) | ![](assets/infographic-cn/tree-branching.png) |
| ![](assets/infographic-cn/venn-diagram.png) | ![](assets/infographic-cn/jigsaw.png) | ![](assets/infographic-cn/winding-roadmap.png) |

**Same 21 layouts in golden particle dark concept art style:**

| | | |
|---|---|---|
| ![](assets/infographic-gold/bento-grid.png) | ![](assets/infographic-gold/bridge.png) | ![](assets/infographic-gold/circular-flow.png) |
| ![](assets/infographic-gold/funnel.png) | ![](assets/infographic-gold/iceberg.png) | ![](assets/infographic-gold/hierarchical-layers.png) |
| ![](assets/infographic-gold/hub-spoke.png) | ![](assets/infographic-gold/dashboard.png) | ![](assets/infographic-gold/tree-branching.png) |
| ![](assets/infographic-gold/venn-diagram.png) | ![](assets/infographic-gold/jigsaw.png) | ![](assets/infographic-gold/winding-roadmap.png) |

Each layout combines with 20 visual styles: craft-handmade, aged-academia, claymation, cyberpunk-neon, ikea-manual, origami, pixel-art, technical-schematic, and more.

---

## Precision Layout Engine (Mode B)

Pixel-perfect text rendering — HTML/CSS + Playwright → 1080×1440 PNG. No AI text distortion, data cards, comparison tables, numbered action lists — all rendered with crisp typography.

### Five Brands × Six Densities

Same content, *"AI Transforms Business"*, rendered across all brand/density combinations:

**墨金 (Dark Cyber-Academic)**

| | | | | | |
|---|---|---|---|---|---|
| ![](assets/mode-b/mojin-sparse.png) | ![](assets/mode-b/mojin-light.png) | ![](assets/mode-b/mojin-balanced.png) | ![](assets/mode-b/mojin-medium.png) | ![](assets/mode-b/mojin-dense.png) | ![](assets/mode-b/mojin-ultra.png) |
| Sparse | Light | Balanced | Medium | Dense | Ultra |

**素启 (Corporate Professional)**

| | | | | | |
|---|---|---|---|---|---|
| ![](assets/mode-b/suqi-sparse.png) | ![](assets/mode-b/suqi-light.png) | ![](assets/mode-b/suqi-balanced.png) | ![](assets/mode-b/suqi-medium.png) | ![](assets/mode-b/suqi-dense.png) | ![](assets/mode-b/suqi-ultra.png) |
| Sparse | Light | Balanced | Medium | Dense | Ultra |

**暖荷 (Warm Personal)**

| | | | | | |
|---|---|---|---|---|---|
| ![](assets/mode-b/nuanhe-sparse.png) | ![](assets/mode-b/nuanhe-light.png) | ![](assets/mode-b/nuanhe-balanced.png) | ![](assets/mode-b/nuanhe-medium.png) | ![](assets/mode-b/nuanhe-dense.png) | ![](assets/mode-b/nuanhe-ultra.png) |
| Sparse | Light | Balanced | Medium | Dense | Ultra |

**朱砂 (Bold Cinnabar)**

| | | | | | |
|---|---|---|---|---|---|
| ![](assets/mode-b/zhusa-sparse.png) | ![](assets/mode-b/zhusa-light.png) | ![](assets/mode-b/zhusa-balanced.png) | ![](assets/mode-b/zhusa-medium.png) | ![](assets/mode-b/zhusa-dense.png) | ![](assets/mode-b/zhusa-ultra.png) |
| Sparse | Light | Balanced | Medium | Dense | Ultra |

**青瓷 (Celadon Elegance)**

| | | | | | |
|---|---|---|---|---|---|
| ![](assets/mode-b/qingci-sparse.png) | ![](assets/mode-b/qingci-light.png) | ![](assets/mode-b/qingci-balanced.png) | ![](assets/mode-b/qingci-medium.png) | ![](assets/mode-b/qingci-dense.png) | ![](assets/mode-b/qingci-ultra.png) |
| Sparse | Light | Balanced | Medium | Dense | Ultra |

Content density is auto-selected. Dense/Ultra pages are always filled with actual content — never stretched spacing.

### 6 Rendering Molds

| Mold | Output | Best For |
|------|--------|----------|
| Multi-card (`-m`) | 1080×1440 per page | XHS series, social cards |
| Long image (`-l`) | 1080×auto | Single long card |
| Infograph (`-i`) | 1080×auto | Data visualization |
| Sketchnote (`-v`) | 1080×auto | Hand-drawn style |
| Comic (`-c`) | 1080×auto | Manga-style B&W |
| Whiteboard (`-w`) | 1080×auto | Structured diagrams |

Features: automatic tone detection, data cards, comparison tables, golden sentence highlighting, dropcap, vertical centering, brand-aware CSS injection.

---

## Hybrid Mode (Mode C)

AI-generated cover for visual impact + precision layout for text-heavy content pages. Best of both worlds.

| | |
|---|---|
| ![cover](assets/mode-c/mode-c-cover.png) | ![content](assets/mode-c/content-01.png) |
| **Page 1: AI cover** (Gemini Pro) | **Page 2: Text layout** (Playwright) |

*Cover uses concept art with golden hammer metaphor. Content pages use the same tuisheng brand colors for visual consistency across AI and HTML rendering.*

---

## Brand System

Every client gets their own visual identity — covering both AI generation and HTML rendering.

### Built-in Brands

| Brand | Look | Best For |
|-------|------|----------|
| **墨金** | Dark + gold/teal, cyber-academic | Community knowledge, deep analysis |
| **素启** | Corporate light, green accents | Client reports, proposals |
| **暖荷** | Warm paper texture, personal | Personal XHS, moments |
| **朱砂** | Dark + cinnabar red, dramatic | Bold statements, impact content |
| **青瓷** | Light celadon, elegant green | Lifestyle, aesthetic sharing |

### Create Your Own Brand

First time use triggers a 3-question setup:
1. Target audience
2. Brand personality (3 words)
3. Aesthetic direction (dark/light/warm/minimal)

This generates `brand.json` + `base.css` + `ai-style.md` — a complete visual system for your client.

---

## Installation

### Claude Code

```bash
git clone https://github.com/Qihe-agent/asyre-social ~/.claude/skills/asyre-social
```

Then use:
```
/asyre-social
```

### OpenClaw

```bash
clawhub install asyre-social
```

### Other AI Tools

Use `SKILL.md` as a system prompt and reference the supporting files.

---

## Usage

```bash
/asyre-social [topic or content]                     # Auto-detect mode
/asyre-social article.md --mode=text                 # Force text layout
/asyre-social --mode=ai --preset=knowledge-card      # AI with preset
/asyre-social --brand=tuisheng                       # Use specific brand
/asyre-social article.md --yes                       # Non-interactive
```

---

## File Structure

```
asyre-social/
├── SKILL.md                         # Core workflow (AI reads this)
├── openclaw.plugin.json             # OpenClaw plugin config
├── brands/
│   ├── _template/brand-template.json  # Template for new brands
│   ├── tuisheng/                    # Dark cyber-academic brand
│   │   ├── brand.json / base.css / ai-style.md
│   ├── asher/                       # Warm personal brand
│   │   ├── brand.json / base.css / ai-style.md
│   └── qihe/                        # Corporate professional brand
│       ├── brand.json / base.css / ai-style.md
├── references/
│   ├── routing.md                   # Mode routing decision tree
│   ├── taste.md                     # Anti-AI-slop quality gates
│   ├── ai-gen/                      # AI generation references
│   │   ├── presets/                 # 12 style definitions
│   │   ├── elements/               # Canvas, decorations, effects, typography
│   │   ├── workflows/              # Analysis, outline, prompt assembly
│   │   └── style-presets.md        # 23+ preset shortcuts
│   ├── text-render/                 # Text layout references
│   │   ├── engine.md / tone-detection.md / typography.md
│   └── config/
│       ├── first-time-setup.md / preferences-schema.md
├── scripts/
│   ├── capture.js                   # Playwright screenshot engine
│   ├── render_pages.py              # Multi-page renderer
│   └── render_single.py            # Single-page renderer
└── templates/
    └── page.html                    # HTML page template
```

## Credits

- **[baoyu-xhs-images](https://github.com/JimLiu/baoyu-skills)** by JimLiu — XHS infographic generation engine
- **Asyre Design System** — brand management and anti-AI-slop quality gates

## License

MIT License. See [LICENSE](LICENSE).

---

<div align="center">

**Stop making generic content. Start making branded impressions.**

![Asyre](https://img.shields.io/badge/Asyre-Social-black?style=for-the-badge)

Powered by [**Asyre**](https://github.com/Qihe-agent)

</div>
