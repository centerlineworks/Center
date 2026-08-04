# CLAUDE.md — How we build web pages for Centerline Construction

This repo holds custom pages for **centerlineworks.com**, a Squarespace site owned by
Alfred Tudela (alfred@centerlineworks.com). Alfred is not a programmer — explain things
plainly, do the technical work for him, and always give copy-paste-ready output.

## Pages in this repo

- **Home** — `home.html` → `squarespace/home-part1-header-injection.html` +
  `home-part2-code-block.html`. Scope `#cl-home`. Responsive-first (no phone twin).
  Conversion-led structure from 2026 contractor-site research: above the fold it carries a
  specific offer, click-to-call, review count, free-estimate CTA and trust chips over the
  video hero; then services grid (links into `/services#<anchor>`, Commercial spans the row
  as a wide card), before/after featured work, values, 3-step process, Alfred, reviews,
  service-area chips (local SEO), FAQ, video CTA. Reuses `services-hero.*` and photos
  already live elsewhere, so it needs zero new uploads — note that swapping the Services
  video therefore also changes Home until it gets its own `home-hero.*`.
  Alfred's **Elfsight** All-in-One Reviews widget is embedded verbatim in the reviews
  section; three real reviews render behind it and hide via `.cl-elf-ready` once the widget
  paints (MutationObserver + height check + timed fallbacks), so the section is never empty
  and crawlers/AI still get review text. Preconnect to `elfsightcdn.com` sits in Part 1.
  Hero: centred, led by a LARGE logo (`/s/centerline-logo.png`, clamp up to 680px) over
  the video, then the slogan **"Measure twice. Build once."** Slogan history — do not
  regress: About's "Built on Faith / Finished with craftsmanship" is off limits here;
  a service list ("Bathrooms. Basements. Cabanas.") was rejected ("if I was a teacher I
  wouldn't say apples.books.teaching"); "Straight lines. Straight answers." was rejected as
  "a weird slogan for a construction company". Alfred wants trade-rooted, not clever.
  Services belong in the subhead, not the headline.
  Copy rules he's asked for: don't lead with "family-owned" up top (it's fine lower down);
  never imply a single crew ("One crew. Every room" was rejected as sounding understaffed —
  now "Every room. Inside and out."); the process section must not mirror "Three values.
  Zero shortcuts." or claim a fixed number of steps (now "Making it easy. No surprises."
  with non-numbered phase labels).
  Each "What we build" card can take an optional looping video via
  `window.CL_HOME_VIDEOS` (same keys as the photo config). The card's photo is always the
  fallback: the `<video>` layer sits above the photo at `opacity:0` and only gets
  `.is-playing` on the real `playing` event, so a broken/slow clip is invisible rather than
  a blank card. Videos are `preload="none"`, sources attached and played only when the card
  intersects (200px margin), paused when it leaves, and skipped entirely under
  `prefers-reduced-motion` or `connection.saveData`. `pointer-events:none` keeps the card
  clickable as a link.
  **Review counts are config-driven**: `window.CL_REVIEWS` at the top of Part 2 holds the
  rating plus a per-platform count (google/facebook/yelp/nextdoor). JS sums them and fills
  every `[data-rev-total]`, `[data-rev-rating]`, the `[data-rev-count]` stat counter and the
  platform badges, so bumping one platform updates the whole page. Never hardcode "43"
  in visible copy again.
  NEVER recreate the logo in CSS/SVG — Alfred called a CSS lockup "totally botched". Drop
  the real image in as-is; a plain dashed upload-reminder note is the only stand-in, and it
  disappears once the file loads. The owner section is video-led (`home-owner.*`, Alfred's
  own work-and-life reel) with a flat 3-photo strip, not About's portrait+cameo overlap.
  That reel is vertical phone footage, so the frame is portrait — `aspect-ratio: 4/5`,
  `max-width: 460px`, in the narrower grid column — and the cover crop that gives us also
  swallows the letterbox bars a few of the source shots carry.
  LESSON: footage Alfred sends may be a repost montage with **burned-in watermarks**
  (a TikTok logo + someone's handle, an Instagram repost tag). Always build a
  second-by-second contact sheet before encoding, flag them, and cut those shots out with
  a `trim`/`concat` filter graph rather than shipping them — a competitor's or a repost
  account's handle on the company homepage is worse than a shorter video. Phone exports
  are also often **HEVC/H.265**, which Chrome and Firefox won't reliably decode, so they
  always need a real H.264 + VP9 transcode, never a straight upload.
  LESSON: an absolutely-positioned card whose children are ALL absolute has no content to
  give it height — it collapses to ~0px unless you set an explicit `aspect-ratio`.
  LESSON: on phones the service/work rows become horizontal swipe rails, and cards parked
  off-screen to the right never intersect the viewport, so their lazy images stay unloaded
  until swiped. An IntersectionObserver on each rail promotes every image inside it to
  `loading="eager"` as soon as the rail scrolls into view vertically.
- **About** — `index.html` → `squarespace/part1-header-injection.html` +
  `part2-code-block.html` + `part3-phone-addon.html`. Desktop-first design with a bolted-on
  phone twin (see LESSON below on why that got complicated).
- **Services** — `services.html` → `squarespace/services-part1-header-injection.html` +
  `services-part2-code-block.html`. Built responsive-first instead — ONE file reshapes
  itself for phones via CSS media queries (galleries become swipeable strips, a sticky
  action bar appears) with no duplicated markup/JS twin. Prefer this pattern for any new
  page: only reach for an About-style Part 3 phone twin when a page already shipped
  desktop-only and a full rewrite isn't worth it.
  Seven service categories with a 4-photo gallery each: Bathrooms, Basements, Cabanas
  (custom cabanas/pavilions — swapped in for Kitchen Remodeling since there aren't enough
  kitchen photos yet), Additions, Decks & Outdoor, Siding & Exterior, Commercial.
  Has its OWN hero video (`assets/services-hero.mp4/.webm` + `-poster.jpg`) — a separate
  poolside cabana/pavilion clip, intentionally decoupled from the About page's
  `hero-loop.*` files so editing one page's video never risks the other's. Never reuse
  the About page's hero filenames for a different page's different footage.
- Each page has its own `<title>`/meta/JSON-LD but shares the same design tokens, fonts,
  and `#cl-<page>`-scoped CSS pattern — copy the foundation from the most recent page
  rather than reinventing it.

## The workflow (follow this for every new page)

1. **One fully standalone HTML file per page** (`index.html`, `services.html`, …). Each
   must open and work from a local file with zero build steps. Media lives in `assets/`
   with relative paths for local preview.
2. **Regenerate the Squarespace paste files after every edit** to a page's source file:
   - `squarespace/part1-header-injection.html` — everything from `<meta charset>` through
     `</style>` (minus the `<title>` line; the SEO title is set in Page Settings). Pasted
     into Page Settings → Advanced → Page Header Code Injection.
   - `squarespace/part2-code-block.html` — from the `YOUR PHOTOS` config `<script>` +
     `<main id="cl-about">` through the desktop IIFE's `</script>` (stop at the
     `<!-- PART3-START -->` marker). Pasted into one Code Block (type HTML).
   - `squarespace/part3-phone-addon.html` — the `<!-- PART3-START/END -->` block: a
     phone-only layout (`#cl-about-m`) pasted below Part 2 in the same Code Block.
     Width switch at 767px hides `#cl-about` on phones and `#cl-about-m` at ≥768px.
     Its JS runs only on phones: it strips the hidden desktop videos' sources (saves
     bandwidth), attaches its own hero video, and CLONES photos (`data-m-from` ←
     `data-cl-photo`), work cards, and all review cards from the desktop DOM — content
     is maintained in Part 2 only. On desktop it stays fully inert (no downloads).
     Signature mobile moves: sticky bottom action bar (Get Estimate / Call / Email,
     safe-area padding), scroll-snap swipe galleries, 100svh video hero.
     LESSON: the mobile hero does NOT have its own <video> — the phone JS MOVES the
     original desktop hero video element (the only one proven to play on Alfred's
     phone) into `.m-hero`. Never recreate that video element; adopt it.
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
  Squarespace's image CDN at unguessable URLs** — never hardcode guesses. Instead each page
  has its own `window.CL_PHOTOS` / `CL_SERVICES_PHOTOS` config near the top of Part 2:
  Alfred pastes each image's URL (get it via Image Block on a hidden page → right-click →
  Copy Image Address, OR upload as a File like the videos to get a predictable `/s/` URL
  with no copying at all); JS applies it to `<img data-cl-photo="...">` tags.
  LESSON (hard-won, cost Alfred a day of debugging): an `<img>` with no `src` yet renders a
  tiny broken icon, so photo slots need a "not loaded yet" state — but **never implement
  that state with `display: none` on the image, and never depend on inline
  `onload`/`onerror` attributes to undo it.** Two independent failure modes turn that into
  a permanent deadlock where photos never appear on the live site (while looking fine in
  the Squarespace editor): (1) a `display:none` or fully `clip-path`-clipped image with
  `loading="lazy"` is never fetched, so its load event never fires, so it's never revealed;
  (2) Squarespace's Code Block sanitizer can strip inline event-handler attributes.
  The robust pattern, now used on the Services page: hide with `opacity: 0` (image still
  loads and lays out), attach `load`/`error` listeners **in JS**, check
  `img.complete && img.naturalWidth > 0` immediately for the already-cached case, and run a
  `setTimeout`/`window.load` sweep as a safety net. Any image that is visually hidden or
  clipped in its resting state (e.g. the before/after comparison image) must be
  `loading="eager"` — lazy loading will never fetch it.
- **Reducing upload friction**: when Alfred has a batch of photos ready, he can attach them
  directly in the chat — reuse the video pipeline's instinct (rename/organize/compress for
  web) and hand back the exact filenames before he uploads. Steer him toward uploading
  photos as **Files** (same as the videos) rather than through the asset library whenever
  possible — it skips the "Image Block + copy address" step entirely and gives a
  predictable `/s/<filename>` URL we can write into the code directly.
- **The site theme bleeds into code blocks** (it set our headings white-on-white once, and
  separately left chip/pill `<span>` text with no explicit color so it could inherit an
  invisible white-on-cream from the theme). Guard broadly — include `span`/`div`/`b`/`strong`
  in the `:is(...)` inherit rule, not just headings/paragraphs, and give every "pill" style
  (chips, badges) its own explicit `color` too, never rely on inheritance alone:
  `#cl-<page> :is(h1,h2,h3,h4,p,blockquote,summary,cite,small,li,figcaption,span,div,b,strong)
  { color: inherit; }`. Scope ALL CSS under the page's `#cl-<page>` id.
  LESSON: white-on-cream isn't always theme bleed — an alternating-background rule like
  `.cl-svc:nth-of-type(even)` can outrank a section's own intentional dark-background rule
  on CSS specificity alone (extra class-level selector from `:nth-of-type()`), silently
  flipping a dark CTA section to a light background while its light text stays light.
  Any section with its own hardcoded background (CTA, etc.) needs `:not(.cl-cta)` added to
  the alternating-background selector, not just an inherit guard.
- **The host section adds a big empty (black) gap** below the block on every page. Part 1
  CSS collapses it per page: `.page-section:has(#cl-<page>) { padding:0!important;
  min-height:0!important; }` plus `.content-wrapper` / `.sqs-block` equivalents. Manual
  fallback: Section Height Small, padding 0.
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
- Portfolio/gallery pages (Services): a simple lightbox (click a real photo → full-size
  overlay, close via ×/backdrop/Escape) reused wherever a page shows a photo grid; a sticky
  anchor nav with scrollspy (`IntersectionObserver` + `rootMargin` trick) for jumping
  between long sections.
- **Before/after comparison reveal** (Services gallery): each photo slot has an optional
  matching `_before` config key. A shot with one gets `.has-before` and two stacked
  `<img>`s (`.cl-shot-after`, `.cl-shot-before` clipped via `clip-path: inset(0 X% 0 0)`,
  X driven live off cursor-x-within-card on `mousemove`, no transition while tracking so it
  feels directly connected to the mouse); `mouseleave` re-adds a transition and animates
  the clip back to fully hidden. A thin gold handle line follows the same X. Shots without
  a `_before` photo keep the plain hover-zoom instead — never show an inert handle/tag.
  Clicking a `.has-before` shot opens the lightbox in a side-by-side compare mode (two
  larger images) instead of the single-photo mode.
  LESSON: a `position: sticky` element (the anchor nav) that has scrolled to its "stuck"
  state can get its own compositing layer painted ABOVE a later `position: fixed` sibling
  (the lightbox) despite a much higher z-index — happens specifically after the page has
  scrolled, not on a fresh load, so it's easy to miss testing at scrollY 0. `transform:
  translateZ(0)` / `isolation: isolate` on the fixed element did NOT fix it. The reliable
  fix: toggle the sticky element to `position: static` for as long as the modal covering it
  is open (add a class on open, remove on close) — it's hidden behind the modal anyway, so
  there's no visual cost, and it sidesteps the layer-ordering bug entirely.

## Media pipeline

- Playwright's bundled ffmpeg is stripped (VP8/webm only). Use the full static binary:
  `pip install imageio-ffmpeg` →
  `/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-*`.
- A hero background loop only needs a few seconds — trim long source clips (`-t 8` or so)
  before encoding. Detailed/busy footage (foliage, water) costs much more per second than
  simple footage at the same crf; if a first-pass encode comes out heavy (e.g. rich pool/
  landscaping footage vs. plain framing footage), trim tighter and/or raise crf rather than
  shipping an oversized background video.
- **Each page's hero video gets its own filename** (e.g. `hero-loop.*` for About,
  `services-hero.*` for Services) even if both happen to need re-encoding in the same
  session — never let two pages share one filename, or replacing one page's footage
  silently changes the other's.
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
- All 11 photo spots are baked into `index.html` as real
  `images.squarespace-cdn.com/content/v1/6671a6d51ae36c17f36be63b/...` URLs (Alfred
  supplied them by editing part2 on GitHub — watch for his direct GitHub edits and
  integrate them into index.html before regenerating). The `CL_PHOTOS` list remains as an
  easy override for future photo swaps.
