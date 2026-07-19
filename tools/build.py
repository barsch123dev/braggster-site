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

# Microsoft Clarity, pinned to cookieless mode.
#
# The consentv2 call is queued by the tag shim before the remote script loads, so
# Clarity sees "denied" before it can write anything: no _clck, no _clsk, no
# third-party cookie, and no cross-visit id. It gets a fresh id per page view
# instead, which is enough for heatmaps and scroll depth but deliberately gives up
# returning-visitor stitching. Because the signal is hard-coded rather than read
# from a banner, this does not depend on the project's dashboard cookie setting.
#
# This is still a third party receiving visitor data, so it is disclosed in the
# privacy policy under privacy_website_p in every locale. Do not add Clarity to a
# page without that disclosure.
CLARITY_ID = "xm8qnymj92"
CLARITY_HTML = (
    "<script>\n"
    "(function(c,l,a,r,i,t,y){\n"
    "    c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};\n"
    "    t=l.createElement(r);t.async=1;t.src=\"https://www.clarity.ms/tag/\"+i;\n"
    "    y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);\n"
    f'}})(window, document, "clarity", "script", "{CLARITY_ID}");\n'
    "window.clarity('consentv2', {ad_Storage: 'denied', analytics_Storage: 'denied'});\n"
    "</script>"
)

# English is canonical and sits at the root. Order drives the footer language nav.
LOCALES = ["en", "nl", "es", "fr", "de", "pt-BR", "it"]
DEFAULT_LOCALE = "en"

# Open Graph wants language_TERRITORY, which is not the same shape as our locale
# codes or as the BCP 47 tags hreflang uses.
OG_LOCALES = {
    "en": "en_US",
    "nl": "nl_NL",
    "es": "es_ES",
    "fr": "fr_FR",
    "de": "de_DE",
    "pt-BR": "pt_BR",
    "it": "it_IT",
}

# The share card is text-free and locale-independent: the headline a reader sees
# in WhatsApp comes from og:title below, not from the image. See tools/build_og.py.
OG_IMAGE = f"{SITE_URL}/assets/web/og-card.png"
OG_IMAGE_SIZE = (1200, 630)

# A representative slice of the games the app ships, spread across categories
# (card, dice, board, sports, puzzle) and countries. Proper nouns, so they are
# not translated. The "any board game" and "more" chips carry the rest.
# Chess, Backgammon and Sudoku are also playable in the app, not just scored.
GAME_NAMES = [
    "Klaverjassen",
    "Pesten",
    "Poker",
    "Chess",
    "Briscola",
    "Yahtzee",
    "Belote",
    "Backgammon",
    "Skat",
    "Darts",
    "Truco",
    "Sudoku",
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


def social_html(current: str, title: str, description: str, url: str) -> str:
    """Open Graph and Twitter card tags.

    Title and description are escaped here rather than by render(), because the
    whole block is substituted as raw _html.
    """
    title = html.escape(title, quote=True)
    description = html.escape(description, quote=True)
    width, height = OG_IMAGE_SIZE

    tags = [
        '<meta property="og:type" content="website">',
        '<meta property="og:site_name" content="braggster">',
        f'<meta property="og:title" content="{title}">',
        f'<meta property="og:description" content="{description}">',
        f'<meta property="og:url" content="{url}">',
        f'<meta property="og:image" content="{OG_IMAGE}">',
        f'<meta property="og:image:width" content="{width}">',
        f'<meta property="og:image:height" content="{height}">',
        '<meta property="og:image:alt" content="braggster">',
        f'<meta property="og:locale" content="{OG_LOCALES[current]}">',
    ]
    for code in LOCALES:
        if code != current:
            tags.append(f'<meta property="og:locale:alternate" content="{OG_LOCALES[code]}">')

    tags += [
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{title}">',
        f'<meta name="twitter:description" content="{description}">',
        f'<meta name="twitter:image" content="{OG_IMAGE}">',
        '<meta name="twitter:image:alt" content="braggster">',
    ]
    return "\n".join(tags)


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

    # The .ttf sources stay in the repo but are never served: styles.css asks for
    # the subset .woff2 that tools/build_fonts.py generates beside them. The OFL
    # ships, because the licence has to travel with the fonts.
    shutil.copytree(ROOT / "assets", DIST / "assets", ignore=shutil.ignore_patterns("*.ttf"))
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
            social_html=social_html(code, loc["meta_title"], loc["meta_description"], f"{SITE_URL}/{ldir}"),
            features_html=features_html(loc),
            chips_html=chips_html(loc),
            lang_links_html=lang_links_html(code, locales, root, ""),
            privacy_href=f"{root}{ldir}privacy/",
            contact_email=CONTACT_EMAIL,
            clarity_html=CLARITY_HTML,
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
            privacy_social_html=social_html(
                code,
                loc["privacy_meta_title"],
                loc["privacy_meta_description"],
                f"{SITE_URL}/{ldir}privacy/",
            ),
            privacy_lang_links_html=lang_links_html(code, locales, proot, "privacy/"),
            home_href=f"{proot}{ldir}",
            contact_email=CONTACT_EMAIL,
            clarity_html=CLARITY_HTML,
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
