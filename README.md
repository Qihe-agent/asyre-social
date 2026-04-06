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

12 visual styles for AI-generated infographics:

| Style | Description | Best For |
|-------|-------------|----------|
| `cute` | Sweet, adorable, girly | Lifestyle, beauty |
| `fresh` | Clean, refreshing, natural | Wellness, organic |
| `warm` | Cozy, friendly, approachable | Personal stories |
| `bold` | High impact, attention-grabbing | Warnings, tips |
| `minimal` | Ultra-clean, sophisticated | Professional |
| `retro` | Vintage, nostalgic, trendy | Throwback content |
| `pop` | Vibrant, energetic, eye-catching | Fun facts |
| `notion` | Minimalist line art, intellectual | Knowledge cards |
| `chalkboard` | Chalk on blackboard, educational | Tutorials |
| `study-notes` | Handwritten photo style | Study guides |
| `screen-print` | Bold poster art, halftone textures | Opinion pieces, editorials |
| `tuisheng` | Dark cyber-academic, gold/teal highlights | Deep analysis, scholarly content |

Each style combines with 8 layouts (sparse, balanced, dense, list, comparison, flow, mindmap, quadrant) and 23+ presets for quick setup.

---

## Precision Layout Engine (Mode B)

6 rendering molds for pixel-perfect text output:

| Mold | Output | Best For |
|------|--------|----------|
| Multi-card (`-m`) | 1080×1440 per page | XHS series, social cards |
| Long image (`-l`) | 1080×auto | Single long card |
| Infograph (`-i`) | 1080×auto | Data visualization |
| Sketchnote (`-v`) | 1080×auto | Hand-drawn style |
| Comic (`-c`) | 1080×auto | Manga-style B&W |
| Whiteboard (`-w`) | 1080×auto | Structured diagrams |

Features: automatic tone detection, golden sentence highlighting, dropcap, overflow protection, brand-aware CSS injection.

---

## Brand System

Every client gets their own visual identity — covering both AI generation and HTML rendering.

### Built-in Brands

| Brand | Look | Best For |
|-------|------|----------|
| **tuisheng** | Dark + gold/teal, cyber-academic | Community knowledge sharing |
| **asher** | Warm paper texture, personal | Personal XHS, moments |
| **qihe** | Corporate blue, clean | Client reports, proposals |

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
