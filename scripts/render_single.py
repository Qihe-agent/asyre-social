#!/usr/bin/env python3
"""
Asyre XHS — Single-page renderer.
Renders entire Markdown article as ONE image (1080px width, adaptive height).
Top: avatar + author + date + tags
Bottom: watermark
Content: auto-fits vertically, no pagination.

Usage:
  python3 render_single.py \
    --input article.md \
    --output ./output/ \
    --background bg.png \
    --avatar avatar.jpg \
    --author "Asher 修荷" \
    --date "2026-03-19" \
    --tags "标签1 × 标签2" \
    --watermark "修荷 · 蜕升学院"
"""

import argparse
import base64
import os
import re
from pathlib import Path

from playwright.sync_api import sync_playwright

# Import parse_markdown from render_pages.py (reuse parsing logic)
import sys
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from render_pages import parse_markdown

# ── Constants ──────────────────────────────────────────────────────
PAGE_W = 1080
PAD_X = 65
PAD_TOP = 50
PAD_BOT = 70

SKILL_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = SKILL_DIR / "templates"


# ── Inline markup ──────────────────────────────────────────────────

def inline_markup(text: str) -> str:
    """Convert **bold** to gold, ^^text^^ to teal."""
    text = re.sub(r'\*\*(.+?)\*\*', r'<span style="color:#D4A520">\1</span>', text)
    text = re.sub(r'\^\^(.+?)\^\^', r'<span style="color:#40B8B8">\1</span>', text)
    return text


# ── Image base64 ──────────────────────────────────────────────────

def img_to_base64(path: str) -> str:
    if not path or not os.path.exists(path):
        return ''
    ext = Path(path).suffix.lower().lstrip('.')
    mime = {'jpg': 'jpeg', 'jpeg': 'jpeg', 'png': 'png', 'gif': 'gif', 'webp': 'webp'}.get(ext, 'png')
    with open(path, 'rb') as f:
        b64 = base64.b64encode(f.read()).decode()
    return f'data:image/{mime};base64,{b64}'


# ── Block → HTML ──────────────────────────────────────────────────

def block_to_html(block: dict) -> str:
    t = block['type']
    if t == 'title':
        return f'<h1>{inline_markup(block["text"])}</h1>'
    elif t == 'subtitle':
        return f'<h2>{inline_markup(block["text"])}</h2>'
    elif t == 'section':
        return f'<h3>{inline_markup(block["text"])}</h3>'
    elif t == 'para':
        lines = block['text'].split('\n')
        text = '<br>'.join(inline_markup(l) for l in lines)
        return f'<p>{text}</p>'
    elif t == 'callout':
        return f'<blockquote class="callout-red">{inline_markup(block["text"])}</blockquote>'
    elif t == 'callout-gold':
        return f'<blockquote class="callout-gold">{inline_markup(block["text"])}</blockquote>'
    elif t == 'divider':
        return '<hr>'
    elif t == 'image':
        b64 = img_to_base64(block['path'])
        if b64:
            return f'<div class="article-image"><img src="{b64}"></div>'
        return ''
    return ''


# ── Main ──────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='Asyre XHS single-page renderer')
    parser.add_argument('--input', '-i', required=True, help='Markdown file')
    parser.add_argument('--output', '-o', required=True, help='Output directory')
    parser.add_argument('--background', '-bg', help='Background image path')
    parser.add_argument('--avatar', help='Author avatar path')
    parser.add_argument('--author', default='Asher 修荷', help='Author name')
    parser.add_argument('--date', default='', help='Date string')
    parser.add_argument('--tags', default='', help='Tags (× separated)')
    parser.add_argument('--watermark', default='修荷 · 蜕升学院', help='Watermark text')
    args = parser.parse_args()

    md_text = Path(args.input).read_text()
    blocks = parse_markdown(md_text)

    out_dir = Path(args.output)
    out_dir.mkdir(parents=True, exist_ok=True)

    bg_b64 = img_to_base64(args.background)
    avatar_b64 = img_to_base64(args.avatar)

    # Build author header
    author_html = ''
    if avatar_b64:
        tags_html = f'<div class="tags">{args.tags}</div>' if args.tags else ''
        date_html = f'<div class="author-date">{args.date}</div>' if args.date else ''
        author_html = (f'<div class="author-header">'
                       f'<img src="{avatar_b64}">'
                       f'<div>'
                       f'<div class="author-name">{args.author}</div>'
                       f'{date_html}{tags_html}'
                       f'</div></div>')

    # Build content blocks
    content_parts = []
    for block in blocks:
        if block['type'] == 'divider':
            continue  # skip dividers in single-page mode
        content_parts.append(block_to_html(block))
    content_html = '\n'.join(content_parts)

    # Build watermark
    watermark_html = f'<div class="watermark">{args.watermark}</div>'

    # Full HTML
    html = f'''<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;700;900&display=swap');
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{
  width: {PAGE_W}px;
  margin: 0 auto;
  font-family: 'Noto Serif SC', serif;
  color: #E8E0D0;
  background: #0D0D0F;
  position: relative;
}}
.bg {{
  position: fixed; top:0; left:0; right:0; bottom:0;
  background-image: url('{bg_b64}');
  background-size: 100% auto;
  background-repeat: repeat-y;
  opacity: 0.45; z-index: 0;
}}
.content {{
  position: relative; z-index: 10;
  padding: {PAD_TOP}px {PAD_X}px {PAD_BOT}px {PAD_X}px;
}}
.author-header {{
  display: flex; align-items: center; gap: 20px;
  margin-bottom: 32px; padding-bottom: 24px;
  border-bottom: 2px solid rgba(212,165,32,0.3);
}}
.author-header img {{
  width: 90px; height: 90px; border-radius: 50%;
  border: 3px solid rgba(212,165,32,0.6);
  object-fit: cover;
}}
.author-name {{ font-size: 26px; font-weight: 700; color: #D4A520; }}
.author-date {{ font-size: 16px; color: rgba(232,224,208,0.4); margin-top: 3px; }}
.tags {{ font-size: 14px; color: rgba(64,184,184,0.6); margin-top: 3px; }}

h1 {{ font-size: 28px; color: #D4A520; margin-bottom: 6px; line-height: 1.4; }}
h2 {{ font-size: 19px; color: #40B8B8; font-style: italic; margin-bottom: 22px; font-weight: 400; }}
h3 {{ font-size: 24px; color: #D4A520; margin-top: 20px; margin-bottom: 12px; font-weight: 700; }}
p {{ font-size: 22px; line-height: 1.9; margin-bottom: 14px; }}
hr {{ border: none; border-top: 1px solid rgba(212,165,32,0.25); margin: 18px 0; }}
blockquote {{
  padding: 14px 18px;
  margin: 16px 0;
  border-radius: 0 8px 8px 0;
  font-style: italic;
  font-size: 22px;
  line-height: 1.9;
}}
blockquote.callout-red {{
  border-left: 4px solid #C0392B;
  background: rgba(192,57,43,0.08);
}}
blockquote.callout-gold {{
  border-left: 4px solid #D4A520;
  background: rgba(212,165,32,0.08);
}}
blockquote p {{ margin-bottom: 0; }}
.article-image {{
  text-align: center;
  margin: 20px 0;
}}
.article-image img {{
  max-width: 100%;
  max-height: 800px;
  object-fit: contain;
  border-radius: 8px;
}}
.watermark {{
  text-align: right; font-size: 14px;
  color: rgba(212,165,32,0.15); letter-spacing: 6px;
  margin-top: 24px;
}}
</style></head>
<body>
<div class="bg"></div>
<div class="content">
{author_html}
{content_html}
{watermark_html}
</div>
</body></html>'''

    out_path = out_dir / 'single.png'

    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page(viewport={'width': PAGE_W, 'height': 1440})
        page.set_content(html)
        page.wait_for_load_state('networkidle')

        # Measure content height
        content_h = page.evaluate('document.querySelector(".content").scrollHeight + 120')
        final_h = max(content_h, 800)

        # Set viewport to final height
        page.set_viewport_size({'width': PAGE_W, 'height': final_h})

        # Screenshot
        page.screenshot(path=str(out_path), clip={'x': 0, 'y': 0, 'width': PAGE_W, 'height': final_h})
        browser.close()

    print(f'✅ {out_path} ({final_h}px height)')
    print(f'\nDone! Single-page image → {out_path}')


if __name__ == '__main__':
    main()
