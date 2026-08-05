# Translation brief for the braggster.com blog

Applies to every locale under `src/blog/<locale>/`. English at `src/blog/en/` is canonical.

## Filenames and slugs

**Keep the English filename.** `how-to-score-klaverjassen.md` stays `how-to-score-klaverjassen.md` in
every locale, and the `slug:` field keeps its English value. The URL becomes
`/<locale>/blog/<slug>/`. One slug per article across all seven languages keeps hreflang, the
renderer and the internal links simple, and the slug is a minor ranking factor next to the title and
the body.

## Frontmatter

| Field | What to do |
|---|---|
| `title` | Translate. This is the H1 and it must match the `# ` heading in the body exactly |
| `slug` | Leave unchanged |
| `locale` | Set to this file's locale code |
| `type`, `category`, `game_id`, `priority`, `schema`, `internal_links` | Leave unchanged |
| `meta_title` | Translate. **Hard limit 60 characters** |
| `meta_description` | Translate. **110 to 160 characters**, never over |
| `primary_keyword` | **Re-target, do not translate.** See below |
| `secondary_keywords` | Re-target for the language |
| `search_intent` | Leave unchanged |
| `trademark_note` | Translate where it is not null |

## Keywords are re-targeted, not translated

The point of the keyword fields is what people actually type into a search box in that language. A
literal translation of the English phrase is usually not it.

- Dutch Klaverjassen: `klaverjassen puntentelling`, not "klaverjassen scoring"
- German Yahtzee: `kniffel punkte`, not "yahtzee scoring"
- French Yahtzee: `yams regles`
- Spanish Solitaire: `solitario reglas puntuacion`
- Italian Briscola style games: use the Italian name people search for
- Portuguese (BR) Backgammon: `gamao regras`

Several of these already appear in the English drafts' `secondary_keywords`, so the target is known
rather than guessed. Where you are unsure, pick the phrase a native speaker would type, not the one
that mirrors the English.

## Game names are never translated

They are proper nouns. Klaverjassen stays Klaverjassen in Italian. Yahtzee stays Yahtzee in French,
with Yams introduced in the body as the local name where the English text already does that. This
matches `src/games.json`, which never translates a game name.

## Copy rules

- **No em dashes and no en dashes.** Neither `—` nor `–`, anywhere, including inside frontmatter.
  This is gated by `tools/check_copy.py` and it fails the build.
- **No wagering vocabulary.** Nothing may say bet, stake, chip, pot, ante, payout or their
  equivalents in your language, except in the sentences that explicitly say the app has none of them.
- Keep the markdown structure identical: same headings, same tables with the same rows, same FAQ
  questions, same closing link block.
- Do not translate link paths. `/blog/how-to-score-hearts/` and `/games/` stay exactly as written.
- Write natural prose in the target language. A translation that reads like English with the words
  swapped is worse than a looser one that reads like it was written in that language.
- Numbers, scoring tables and rules must survive exactly. If the English says 162 card points, the
  translation says 162.

## Voice

Match `src/locales/<locale>.json`, which holds the site's existing copy in your language. That file
is the reference for tone, for how the product is described, and for terminology already chosen
(what "score sheet" is called, how the app is introduced).
