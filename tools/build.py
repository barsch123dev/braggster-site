#!/usr/bin/env python3
"""Render the Braggster marketing site from src/ into dist/.

One template per page, one JSON file per locale. English lives at the site root;
every other locale lives under its own directory. Asset and page links are
relative, so the output works from a subpath (the github.io preview URL) as well
as from the apex domain.
"""

from __future__ import annotations

import html
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
DIST = ROOT / "dist"

SITE_URL = "https://braggster.com"
CONTACT_EMAIL = "hello@braggster.com"

# English is canonical and sits at the root. Order drives the footer language nav.
LOCALES = ["en", "nl", "es", "fr", "de", "pt-BR", "it"]
DEFAULT_LOCALE = "en"

# A representative slice of the games the app ships, spread across categories
# (card, dice, board, sports) and countries. Proper nouns, so they are not
# translated. The "any board game" and "more" chips carry the rest.
GAME_NAMES = [
    "Klaverjassen",
    "Poker",
    "Bridge",
    "Hearts",
    "Briscola",
    "Belote",
    "Skat",
    "Truco",
    "Yahtzee",
    "Dudo",
    "Darts",
    "Rummikub",
]

TOKEN = re.compile(r"\{\{(\w+)\}\}")

# Feature glyphs, rebuilt as inline SVG from the prototype's div geometry.
GLYPH_DICE = (
    '<svg width="26" height="26" viewBox="0 0 26 26" aria-hidden="true" focusable="false">'
    '<rect x="0" y="0" width="16" height="16" rx="5" fill="#16243D" transform="rotate(-8 8 8)"/>'
    '<rect x="10" y="10" width="16" height="16" rx="5" fill="#F08A24" transform="rotate(7 18 18)"/>'
    "</svg>"
)
GLYPH_BARS = (
    '<svg width="24" height="24" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
    '<rect x="0" y="12" width="6" height="12" rx="3" fill="#2D6BE4"/>'
    '<rect x="9" y="0" width="6" height="24" rx="3" fill="#2D6BE4"/>'
    '<rect x="18" y="7" width="6" height="17" rx="3" fill="#2D6BE4"/>'
    "</svg>"
)
GLYPH_PASS = (
    '<svg width="26" height="16" viewBox="0 0 26 16" aria-hidden="true" focusable="false">'
    '<circle cx="8" cy="8" r="8" fill="#F08A24"/>'
    '<circle cx="18" cy="8" r="8" fill="#16243D"/>'
    "</svg>"
)

FEATURES = [
    ("f1", "#FDEBD6", -6, GLYPH_DICE),
    ("f2", "#E3ECFC", 5, GLYPH_BARS),
    ("f3", "#FDEBD6", -5, GLYPH_PASS),
]


def locale_dir(code: str) -> str:
    """Directory for a locale, relative to the site root. English is the root."""
    return "" if code == DEFAULT_LOCALE else f"{code.lower()}/"


def render(template: str, values: dict[str, str]) -> str:
    """Substitute {{key}}. Keys ending in _html are raw; everything else is escaped."""

    def sub(match: re.Match[str]) -> str:
        key = match.group(1)
        if key not in values:
            raise KeyError(f"template key not provided: {key}")
        value = values[key]
        return value if key.endswith("_html") else html.escape(value, quote=True)

    return TOKEN.sub(sub, template)


def features_html(loc: dict[str, str]) -> str:
    cards = []
    for key, tile_bg, tilt, glyph in FEATURES:
        cards.append(
            f'        <article class="card">\n'
            f'          <div class="card__tile" style="background: {tile_bg}; transform: rotate({tilt}deg);">{glyph}</div>\n'
            f"          <h3>{html.escape(loc[f'{key}_title'])}</h3>\n"
            f"          <p>{html.escape(loc[f'{key}_body'])}</p>\n"
            f"        </article>"
        )
    return "\n".join(cards)


def chips_html(loc: dict[str, str]) -> str:
    chips = [f'        <span class="chip">{html.escape(g)}</span>' for g in GAME_NAMES]
    chips.append(f'        <span class="chip">{html.escape(loc["chip_generic"])}</span>')
    chips.append(f'        <span class="chip chip--soon">{html.escape(loc["chip_soon"])}</span>')
    return "\n".join(chips)


def lang_links_html(current: str, locales: dict[str, dict], root: str, suffix: str) -> str:
    links = []
    for code in LOCALES:
        href = f"{root}{locale_dir(code)}{suffix}" or "./"
        current_attr = ' aria-current="true"' if code == current else ""
        name = html.escape(locales[code]["name"])
        links.append(f'      <a href="{href}" hreflang="{code}" lang="{code}"{current_attr}>{name}</a>')
    return "\n".join(links)


def hreflang_html(suffix: str) -> str:
    tags = []
    for code in LOCALES:
        url = f"{SITE_URL}/{locale_dir(code)}{suffix}"
        tags.append(f'<link rel="alternate" hreflang="{code}" href="{url}">')
    tags.append(f'<link rel="alternate" hreflang="x-default" href="{SITE_URL}/{suffix}">')
    return "\n".join(tags)


def build() -> None:
    locales = {c: json.loads((SRC / "locales" / f"{c}.json").read_text("utf-8")) for c in LOCALES}
    home_tpl = (SRC / "home.html").read_text("utf-8")
    privacy_tpl = (SRC / "privacy.html").read_text("utf-8")

    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True)

    shutil.copytree(ROOT / "assets", DIST / "assets")
    shutil.copy2(SRC / "styles.css", DIST / "styles.css")
    shutil.copy2(ROOT / "CNAME", DIST / "CNAME")
    (DIST / ".nojekyll").write_text("")

    written: list[str] = []

    for code in LOCALES:
        loc = dict(locales[code])
        ldir = locale_dir(code)

        # ---- Home: <root>/<ldir>index.html
        depth = ldir.count("/")
        root = "../" * depth
        values = dict(loc)
        values.update(
            root=root,
            canonical=f"{SITE_URL}/{ldir}",
            hreflang_html=hreflang_html(""),
            features_html=features_html(loc),
            chips_html=chips_html(loc),
            lang_links_html=lang_links_html(code, locales, root, ""),
            privacy_href=f"{root}{ldir}privacy/",
            contact_email=CONTACT_EMAIL,
        )
        out = DIST / ldir / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render(home_tpl, values), "utf-8")
        written.append(str(out.relative_to(DIST)))

        # ---- Privacy: <root>/<ldir>privacy/index.html
        pdepth = depth + 1
        proot = "../" * pdepth
        pvalues = dict(loc)
        pvalues.update(
            root=proot,
            privacy_canonical=f"{SITE_URL}/{ldir}privacy/",
            privacy_hreflang_html=hreflang_html("privacy/"),
            privacy_lang_links_html=lang_links_html(code, locales, proot, "privacy/"),
            home_href=f"{proot}{ldir}",
            contact_email=CONTACT_EMAIL,
        )
        pout = DIST / ldir / "privacy" / "index.html"
        pout.parent.mkdir(parents=True, exist_ok=True)
        pout.write_text(render(privacy_tpl, pvalues), "utf-8")
        written.append(str(pout.relative_to(DIST)))

    urls = [f"{SITE_URL}/{locale_dir(c)}{s}" for s in ("", "privacy/") for c in LOCALES]
    sitemap = "\n".join(f"  <url><loc>{u}</loc></url>" for u in urls)
    (DIST / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{sitemap}\n</urlset>\n",
        "utf-8",
    )
    (DIST / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")

    print(f"built {len(written)} pages into {DIST}")
    for page in written:
        print(f"  {page}")


if __name__ == "__main__":
    build()
