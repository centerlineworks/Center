# CLAUDE.md — How we build web pages for Centerline Construction

This repo holds custom pages for **centerlineworks.com**, a Squarespace site owned by
Alfred Tudela (alfred@centerlineworks.com). Alfred is not a programmer — explain things
plainly, do the technical work for him, and always give copy-paste-ready output.

## The workflow (follow this for every new page)

1. **`index.html` is the source of truth** — one fully standalone file per page
   (currently the About page). It must open and work from a local file with zero build
   steps. Media lives in `assets/` with relative paths for local preview.
2. **Regenerate the Squarespace paste files after every edit** to `index.html`:
   - `squarespace/part1-header-injection.html` — everything from `<meta charset>` through
     `</style>` (minus the `<title>` line; the SEO title is set in Page Settings). Pasted
     into Page Settings → Advanced → Page Header Code Injection.
   - `squarespace/part2-code-block.html` — from the `YOUR PHOTOS` config `<script>` +
     `<main id="cl-about">` through the final `</script>`. Pasted into one Code Block
     (type HTML).
   - In both, rewrite `assets/...` video/poster paths to
     `https://www.centerlineworks.com/s/<filename>` (Squarespace file-storage URLs).
   - The regeneration is done with a small Python script (see git history) — keep the
     split markers stable.
3. **Verify in a real browser before pushing**: Playwright with the preinstalled Chromium
   (`executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'`, flags
   `--no-sandbox --autoplay-policy=no-user-gesture-required`). Screenshot desktop (1280px)
   and mobile (390px), validate the JSON-LD parses, check for JS errors. NOTE: this
   Chromium cannot decode H.264, so MP4-only video shows as not playing — that's why every
   video has a WebM source too; test with the WebM.
4. **Publish a preview Artifact** for Alfred (same file path each time keeps the URL:
   claude.ai/code/artifact/84d79132-3461-419b-a87e-4df837442ed9, favicon 🏠). Embed the
   small videos/poster as base64 data URIs (CSP blocks external hosts). Remind him that
   photos hosted on Squarespace won't display in the preview — labels show instead.
5. **Commit and push** to the designated branch; keep `DEPLOY.md` and `README.md` in sync
   with any workflow-visible change.

## Squarespace constraints (learned the hard way)

- **JavaScript Code Blocks need the Business plan or higher.**
- **Files vs. images**: files uploaded via Link editor → File → Upload are served at
  `/s/<exact-filename>` — good for videos. Photos in the **asset library live on
  Squarespace's image CDN at unguessable URLs** — never hardcode guesses. Instead the page
  has a `window.CL_PHOTOS` config at the top of Part 2: Alfred pastes each image's URL
  (get it via Image Block on a hidden page → right-click → Copy Image Address); JS applies
  it to `<img data-cl-photo="...">` tags. Every photo spot needs `data-cl-photo`,
  a `data-label` fallback, and `onerror` → `.cl-noimg` so a bad URL shows a text label,
  never a broken image.
- **The site theme bleeds into code blocks** (it set our headings white-on-white once).
  Guard: `#cl-about :is(h1,h2,h3,h4,p,blockquote,summary,cite,small,li,figcaption)
  { color: inherit; }` and scope ALL CSS under the `#cl-about` id.
- **The host section adds a big empty (black) gap** below the block. Part 1 CSS collapses
  it: `.page-section:has(#cl-about) { padding:0!important; min-height:0!important; }` plus
  `.content-wrapper` / `.sqs-block` equivalents. Manual fallback: Section Height Small,
  padding 0.
- Buttons: "Schedule an Estimate" → `/schedule`, "Explore Our Services" → `/services`
  (NOT `/newservices`), Contact Us → `tel:+16783721274` (top) or
  `mailto:Info@centerlineworks.com` (bottom/owner).

## Design system (reuse for visual consistency)

- Tokens on `#cl-about`: ink `#12100c`, paper `#f7f4ee`, paper-2 `#efe9df`, gold
  `#d9a441`, gold-deep `#b07f22`, dark sections `#17161c→#0f0e13`, radius 18px, ease
  `cubic-bezier(.16,1,.3,1)`.
- Fonts: Archivo (headings/body, 800–900 for display) + Fraunces italic (serif accents),
  via Google Fonts link in Part 1.
- Signature moves: video hero with dark scrim + 3D blueprint grid + CSS wireframe house
  rotated by scroll; `.cl-reveal` 3D flip-up on IntersectionObserver; auto-drifting
  marquee (Our Work); 3D coverflow review carousel (drag/swipe/arrows/auto-rotate);
  mouse-tilt cards; animated stat counters; before/after crossfade photo cards.
- All motion respects `prefers-reduced-motion` (reveals shown, videos paused on poster,
  marquee becomes a swipeable strip, carousel keeps manual nav only).
- Everything is vanilla JS in one IIFE — no libraries, no build step.

## Media pipeline

- Playwright's bundled ffmpeg is stripped (VP8/webm only). Use the full static binary:
  `pip install imageio-ffmpeg` →
  `/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-*`.
- Per video, produce: `-an` MP4 (H.264, scale 1600w, crf 27, `+faststart`), WebM (VP9,
  crf 38), poster JPG, plus ~960w "small" versions (crf 32/44) for data-URI embedding in
  the preview Artifact. WebM source listed before MP4 in `<video>`.

## SEO / GEO (AI answer engines)

- JSON-LD `@graph` in Part 1: `HomeAndConstructionBusiness` (+`Person` Alfred Tudela with
  `image` array, +`FAQPage` mirroring the visible FAQ). Keep visible FAQ and schema in
  sync. Do NOT add `aggregateRating` from third-party reviews (against Google guidelines).
- Meta/OG/Twitter tags + canonical in Part 1; og:image = Alfred's portrait.
- Photos of Alfred get alt text naming him fully ("Alfred Tudela, founder and CEO of
  Centerline Construction…") to build his Google Images association.

## Business facts (verified July 2026)

- Centerline Construction Company, LLC — Holly Springs, GA; founded 2020; Alfred has 18+
  years construction experience (don't call him "working CEO"). Christ-centered,
  family-owned; emphasize the whole crew, not just Alfred.
- Phone (678) 372-1274 · Info@centerlineworks.com · Mon–Sat 7am–6pm, Sun 2–6pm.
- Services: bathrooms, basements, kitchens, home additions, decks & railing, siding, wood
  rot repair, cabinetry, exterior repairs, commercial.
- 43 five-star reviews (5.0) across Google 29 / Facebook 10 / Yelp 2 / Nextdoor 2 — full
  text baked into the review carousel (39 cards after dropping cross-platform duplicates).
- Alfred is Youth Director at Rising Hills Church in **Canton, GA** (not Woodstock).
- Photo filenames Alfred uses: story IMG_1704, bathroom before/after IMG_2415→IMG_2688,
  basement PXL_20250226_233210463, decks exported_A3C876F6-…, siding dji_fly_20260604_…,
  commercial IMG_8669, portrait "IMG_1661-EDIT (1)", cedar-beam IMG_1176. Additions and
  Kitchens cards still need photos.
