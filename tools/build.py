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

# No country code in the path: Apple routes a visitor to their own storefront,
# and this page is served in seven languages to whoever turns up. A /nl/ link
# would send everyone through the Dutch store.
APP_STORE_URL = "https://apps.apple.com/app/id6789661787"

# Google Play has no per-storefront routing concern to match the comment above:
# the listing id is the same for every visitor regardless of language or country.
PLAY_STORE_URL = "https://play.google.com/store/apps/details?id=com.braggster.app"

CONTACT_EMAIL = "hello@braggster.com"
SUPPORT_EMAIL = "support@braggster.com"

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

# The catalogue has one home: src/games.json, extracted from the app's game
# definitions. Everything the games page and the home chips render is derived
# from it, so the site cannot drift from the app the way a hand-kept list did.
GAMES = json.loads((SRC / "games.json").read_text("utf-8"))["games"]

# Category order on the games page. Mirrors the app's GameCategory, except that
# the blank scorecard is split out of "other" into its own "free" bucket: it is
# the one game that is always free, which is worth saying plainly.
CATEGORIES = ["card", "dice", "board", "sports", "free"]

# The home page keeps a short teaser rather than all 53 names. This is a
# curated slice, spread across categories and countries, but the names
# themselves still come from games.json, so a rename in the app travels here.
HOME_CHIP_IDS = [
    "klaverjassen",
    "pesten",
    "poker",
    "chess",
    "briscola",
    "yahtzee",
    "belote",
    "backgammon",
    "skat",
    "darts",
    "truco",
    "sudoku",
    "rummikub",
]

TOKEN = re.compile(r"\{\{(\w+)\}\}")

# The catalogue's own numbers, substituted into the copy rather than written out
# in seven languages. They were spelled out until the app shipped its 54th game
# and every locale had to be chased; now they cannot go stale.
COUNTS = {
    "{n}": str(len(GAMES)),
    "{play}": str(sum(1 for g in GAMES if g["playInApp"])),
    "{low}": str(sum(1 for g in GAMES if g["lowestWins"])),
}

# The screenshots tools/build_screenshots.py writes, in the order the gallery
# shows them. The hero takes the first; the rest are the gallery.
SHOTS = ["home", "games", "yahtzee", "sudoku"]
SHOT_WIDTH, SHOT_HEIGHT = 320, 695

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


def counted(text: str) -> str:
    """Fill in the catalogue's own numbers."""
    for token, value in COUNTS.items():
        text = text.replace(token, value)
    return text


def screenshot_html(root: str, locale: str, shot: str, *, hero: bool) -> str:
    """One phone screenshot, at 1x and 2x. The hero's is eager and the gallery's
    is lazy: the hero is the largest thing above the fold, and the gallery is
    three more of it that nobody has scrolled to yet."""
    base = f"{root}assets/screenshots/{locale}/{shot}"
    loading = 'fetchpriority="high"' if hero else 'loading="lazy"'
    return (
        f'<img src="{base}.webp" srcset="{base}.webp 1x, {base}@2x.webp 2x" '
        f'alt="{{alt}}" width="{SHOT_WIDTH}" height="{SHOT_HEIGHT}" {loading} decoding="async">'
    )


def shots_html(loc: dict[str, str], root: str, locale: str) -> str:
    """The gallery: every shot but the one already in the hero."""
    figures = []
    for shot in SHOTS[1:]:
        image = screenshot_html(root, locale, shot, hero=False).replace(
            "{alt}", html.escape(loc[f"shot_{shot}_alt"], quote=True)
        )
        figures.append(
            f'        <figure class="shot">\n'
            f'          <div class="phone">{image}</div>\n'
            f"          <figcaption>{html.escape(loc[f'shot_{shot}_cap'])}</figcaption>\n"
            f"        </figure>"
        )
    return "\n".join(figures)


def render(template: str, values: dict[str, str]) -> str:
    """Substitute {{key}}. Keys ending in _html are raw; everything else is escaped."""

    def sub(match: re.Match[str]) -> str:
        key = match.group(1)
        if key not in values:
            raise KeyError(f"template key not provided: {key}")
        value = counted(values[key])
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


def chips_html(loc: dict[str, str], games_href: str) -> str:
    """The home teaser. The last chip is a link through to the full catalogue,
    which is where the "more" chip used to sit before there was a page to send
    people to."""
    by_id = {g["id"]: g for g in GAMES}
    names = [by_id[i]["name"] for i in HOME_CHIP_IDS]
    chips = [f'        <span class="chip">{html.escape(n)}</span>' for n in names]
    chips.append(f'        <span class="chip">{html.escape(loc["chip_generic"])}</span>')
    more = counted(loc["games_more_link"])
    chips.append(f'        <a class="chip chip--more" href="{games_href}">{html.escape(more)}</a>')
    return "\n".join(chips)


def players_label(loc: dict[str, str], players: dict[str, int]) -> str:
    """Human player count for one game, from the app's sideStructure numbers."""
    lo, hi, per_side = players["min"], players["max"], players["perSide"]
    if per_side > 1:
        # Every partnership game in the catalogue is exactly two teams of two.
        # If that ever stops being true, this needs a real plural rule.
        assert lo == hi == 2 and per_side == 2, f"unexpected team shape: {players}"
        return loc["games_players_teams"]
    if lo == hi == 1:
        return loc["games_players_solo"]
    if lo == hi:
        return loc["games_players_exact"].replace("{n}", str(lo))
    return loc["games_players_range"].replace("{min}", str(lo)).replace("{max}", str(hi))


def games_filters_html(loc: dict[str, str]) -> str:
    """Radio group for the category filter, plus the play-in-app checkbox.

    The controls are plain form inputs with no JavaScript behind them: the
    filtering is done by the CSS in games_css(), which reads their :checked
    state through :has(). Where :has() is unsupported the inputs simply do
    nothing and every game stays visible, which is the right fallback.
    """
    rows = [
        '        <fieldset class="filters">',
        f'          <legend class="filters__legend">{html.escape(loc["games_filter_category"])}</legend>',
        '          <input type="radio" name="cat" id="f-all" class="filters__input" checked>',
        f'          <label for="f-all" class="filters__chip">{html.escape(loc["games_cat_all"])}</label>',
    ]
    for cat in CATEGORIES:
        label = html.escape(loc[f"games_cat_{cat}"])
        rows.append(f'          <input type="radio" name="cat" id="f-{cat}" class="filters__input">')
        rows.append(f'          <label for="f-{cat}" class="filters__chip">{label}</label>')
    rows.append("        </fieldset>")
    rows.append('        <div class="filters filters--toggle">')
    rows.append('          <input type="checkbox" id="f-app" class="filters__input">')
    rows.append(
        f'          <label for="f-app" class="filters__chip">{html.escape(loc["games_badge_app"])}</label>'
    )
    rows.append("        </div>")
    return "\n".join(rows)


def games_grid_html(loc: dict[str, str]) -> str:
    """One card per game. Tag words are rendered as real text, not attributes,
    because they exist to be found: by a search engine, and by a reader looking
    for the name their family uses."""
    items = []
    for game in GAMES:
        badges = []
        if game["playInApp"]:
            badges.append(("game__badge game__badge--app", loc["games_badge_app"]))
        if game["lowestWins"]:
            badges.append(("game__badge game__badge--low", loc["games_badge_lowest"]))
        badge_html = "".join(
            f'<span class="{cls}">{html.escape(text)}</span>' for cls, text in badges
        )
        app_attr = " data-app" if game["playInApp"] else ""
        category_label = loc["games_cat_" + game["category"]]
        meta = f"{players_label(loc, game['players'])} · {category_label}"
        items.append(
            f'          <li class="game" data-cat="{game["category"]}"{app_attr}>\n'
            f'            <h2 class="game__name">{html.escape(game["name"])}</h2>\n'
            f'            <p class="game__meta">{html.escape(meta)}</p>\n'
            + (f'            <p class="game__badges">{badge_html}</p>\n' if badge_html else "")
            + f'            <p class="game__tags"><span class="sr-only">{html.escape(loc["games_tags_label"])} </span>'
            f'{html.escape(", ".join(game["tags"]))}</p>\n'
            f"          </li>"
        )
    return "\n".join(items)


def games_css() -> str:
    """The filter behaviour, generated from the data rather than hand-written.

    Two kinds of rule. The first hides everything outside the chosen category,
    or everything without in-app play. The second turns on the empty state, and
    it only fires for combinations that genuinely have no games: asking for
    dice, sports or the blank scorecard *and* play-in-app matches nothing. Both
    are derived here so they cannot drift from games.json.
    """
    lines = [
        "  .games:has(#f-app:checked) .game:not([data-app]) { display: none; }",
    ]
    for cat in CATEGORIES:
        lines.append(
            f'  .games:has(#f-{cat}:checked) .game:not([data-cat="{cat}"]) {{ display: none; }}'
        )

    empty = [
        f"  .games:has(#f-app:checked):has(#f-{cat}:checked) .games__empty"
        for cat in CATEGORIES
        if not any(g["category"] == cat and g["playInApp"] for g in GAMES)
    ]
    if empty:
        lines.append(",\n".join(empty) + " { display: block; }")
    return "\n".join(lines)


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
    games_tpl = (SRC / "games.html").read_text("utf-8")
    support_tpl = (SRC / "support.html").read_text("utf-8")

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
            social_html=social_html(
                code, counted(loc["meta_title"]), counted(loc["meta_description"]), f"{SITE_URL}/{ldir}"
            ),
            features_html=features_html(loc),
            hero_shot_html=screenshot_html(root, code, SHOTS[0], hero=True).replace(
                "{alt}", html.escape(loc["phone_alt"], quote=True)
            ),
            shots_html=shots_html(loc, root, code),
            chips_html=chips_html(loc, f"{root}{ldir}games/"),
            lang_links_html=lang_links_html(code, locales, root, ""),
            games_href=f"{root}{ldir}games/",
            privacy_href=f"{root}{ldir}privacy/",
            support_href=f"{root}{ldir}support/",
            store_href=APP_STORE_URL,
            play_store_href=PLAY_STORE_URL,
            contact_email=CONTACT_EMAIL,
            support_email=SUPPORT_EMAIL,
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
                counted(loc["privacy_meta_title"]),
                counted(loc["privacy_meta_description"]),
                f"{SITE_URL}/{ldir}privacy/",
            ),
            privacy_lang_links_html=lang_links_html(code, locales, proot, "privacy/"),
            home_href=f"{proot}{ldir}",
            privacy_href=f"{proot}{ldir}privacy/",
            support_href=f"{proot}{ldir}support/",
            contact_email=CONTACT_EMAIL,
            support_email=SUPPORT_EMAIL,
            clarity_html=CLARITY_HTML,
        )
        pout = DIST / ldir / "privacy" / "index.html"
        pout.parent.mkdir(parents=True, exist_ok=True)
        pout.write_text(render(privacy_tpl, pvalues), "utf-8")
        written.append(str(pout.relative_to(DIST)))

        # ---- Games: <root>/<ldir>games/index.html
        groot = "../" * (depth + 1)
        gvalues = dict(loc)
        gvalues.update(
            root=groot,
            games_canonical=f"{SITE_URL}/{ldir}games/",
            games_hreflang_html=hreflang_html("games/"),
            games_social_html=social_html(
                code,
                counted(loc["games_meta_title"]),
                counted(loc["games_meta_description"]),
                f"{SITE_URL}/{ldir}games/",
            ),
            games_lang_links_html=lang_links_html(code, locales, groot, "games/"),
            games_filters_html=games_filters_html(loc),
            games_grid_html=games_grid_html(loc),
            games_css_html=games_css(),
            home_href=f"{groot}{ldir}",
            games_href=f"{groot}{ldir}games/",
            privacy_href=f"{groot}{ldir}privacy/",
            support_href=f"{groot}{ldir}support/",
            store_href=APP_STORE_URL,
            contact_email=CONTACT_EMAIL,
            support_email=SUPPORT_EMAIL,
            clarity_html=CLARITY_HTML,
        )
        gout = DIST / ldir / "games" / "index.html"
        gout.parent.mkdir(parents=True, exist_ok=True)
        gout.write_text(render(games_tpl, gvalues), "utf-8")
        written.append(str(gout.relative_to(DIST)))

        # ---- Support: <root>/<ldir>support/index.html
        sdepth = depth + 1
        sroot = "../" * sdepth
        svalues = dict(loc)
        svalues.update(
            root=sroot,
            support_canonical=f"{SITE_URL}/{ldir}support/",
            support_hreflang_html=hreflang_html("support/"),
            support_social_html=social_html(
                code,
                counted(loc["support_meta_title"]),
                counted(loc["support_meta_description"]),
                f"{SITE_URL}/{ldir}support/",
            ),
            support_lang_links_html=lang_links_html(code, locales, sroot, "support/"),
            home_href=f"{sroot}{ldir}",
            privacy_href=f"{sroot}{ldir}privacy/",
            support_href=f"{sroot}{ldir}support/",
            contact_email=CONTACT_EMAIL,
            support_email=SUPPORT_EMAIL,
            clarity_html=CLARITY_HTML,
        )
        sout = DIST / ldir / "support" / "index.html"
        sout.parent.mkdir(parents=True, exist_ok=True)
        sout.write_text(render(support_tpl, svalues), "utf-8")
        written.append(str(sout.relative_to(DIST)))

    urls = [f"{SITE_URL}/{locale_dir(c)}{s}" for s in ("", "games/", "privacy/", "support/") for c in LOCALES]
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
