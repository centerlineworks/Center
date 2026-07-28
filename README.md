# Centerline Construction — Website Pages

Custom pages for [centerlineworks.com](https://www.centerlineworks.com), built to drop into
Squarespace with zero build tools. Two pages so far:

- **`index.html`** — the About page, with 3D scroll effects and a phone-only twin (Part 3).
- **`services.html`** — the Services page: every service with its own photo gallery, in one
  fully responsive file (see "The Services page" section below).

## What's inside

- **Looping drone video backgrounds** — the crew-framing-an-addition drone clip
  (`assets/hero-loop.mp4`, compressed from 6.6MB to 1.7MB for fast loading, with a poster
  image fallback) plays silently behind the hero and again behind the closing call-to-action.
  It pauses automatically for reduced-motion visitors.
- **3D scroll experience** — a wireframe house that rotates and grows as visitors scroll, a
  perspective blueprint grid that drifts under the hero, parallax headline layers, sections that
  flip up in 3D as they enter the screen, and value cards that tilt toward the mouse on desktop.
- **Action buttons throughout** — "Schedule an Estimate" (`/schedule`), "Contact Us"
  (`/contact`), "Explore Our Services" (`/services`), and click-to-call, placed in the hero,
  story, work showcase, owner section, and closing CTA.
- **Our Story** — the "centerline" founding story: faith, integrity, craftsmanship, founded 2020,
  18+ years of experience, with animated stat counters.
- **Services** — bathrooms, basements, kitchens, home additions, decks & railing, siding, wood rot
  repair, cabinetry, exterior repairs, commercial.
- **Our Work showcase** — an auto-scrolling horizontal banner of project categories (Bathrooms,
  Basements, Additions, Kitchens, Decks & Outdoor, Siding & Exterior), each with a photo slot for
  a real project shot. It glides on its own, pauses on hover/touch, and becomes a normal
  swipeable strip for reduced-motion visitors.
- **Real reviews** — a 3D carousel of all 43 five-star reviews (39 cards after removing
  cross-platform duplicates) from Google, Facebook, Yelp, and Nextdoor, each attributed by
  name with a source badge. It auto-rotates, and visitors can drag, swipe, or use the arrows.
  A "5.0 across 43 reviews" scoreboard sits above it.
- **Meet the Owner** — Alfred Tudela: founder & CEO, husband and father, family-owned company,
  and **Youth Director at Rising Hills Church** in Canton, GA.
- **FAQ + call-to-action** — click-to-call (678) 372-1274 with business hours.
- **Accessible & mobile-friendly** — semantic HTML, ARIA labels, fully responsive, and all motion
  is disabled automatically for visitors with "reduce motion" turned on.

## SEO & AI-answer (GEO) optimization

The page is built so both Google **and** AI assistants (ChatGPT, Claude, Perplexity, Gemini) can
confidently point people to Centerline:

- **JSON-LD structured data** for `HomeAndConstructionBusiness` (services, hours, phone, service
  area, Facebook/LinkedIn profiles), a `Person` record for Alfred Tudela (including the Rising
  Hills Church affiliation), and an `FAQPage` — the exact format answer engines parse.
- **On-page FAQ section** that mirrors the structured data, so quotable plain-language answers
  ("Who owns Centerline Construction?", "What areas do you serve?") exist in the visible content.
- Title tag, meta description, canonical URL, Open Graph / Twitter cards, semantic heading
  hierarchy, and location keywords (Holly Springs, Canton, Woodstock, Cherokee County, North
  Georgia) woven naturally into the copy.

## How to install on Squarespace

> **Start with [DEPLOY.md](DEPLOY.md)** — a copy-paste checklist using the ready-made snippet
> files in the `squarespace/` folder (`part1-header-injection.html` and
> `part2-code-block.html`), with the video URLs already pointed at Squarespace's file storage.
> Code Blocks with JavaScript require the Squarespace **Business plan or higher**.

Prefer to work from the source? `index.html` is split into two clearly marked parts:

1. **Create the page.** In Squarespace: Pages → `+` → **Blank Page**. Name it "About".
2. **Part 1 → Page Header Code Injection.** Open `index.html`, copy everything between the
   `PART 1` markers (the meta tags, the `<script type="application/ld+json">` block, the font
   links, and the `<style>` block). Paste it into **Page Settings → Advanced → Page Header Code
   Injection** for the About page. (Skip the `<title>` line — set the page title in Page
   Settings → SEO instead, using the same text.)
3. **Part 2 → Code Block.** Edit the page, add a single **Code Block** (type: HTML, "Display
   Source" off), and paste everything between the `PART 2` markers (the `<main id="cl-about">`
   element and the `<script>` after it).
4. **Set the page URL** to `/about` so it matches the canonical URL in the code (or update the
   canonical + JSON-LD URLs to your chosen slug).
5. **Save and preview** — scroll the page to see the 3D house, parallax, and reveals in action.

To preview locally first, download the whole repository ("Code" → "Download ZIP" on GitHub),
unzip it, and open `index.html` in any browser — keep the `assets` folder next to it so the
videos play.

### Hosting the video

The code references the video as `assets/hero-loop.mp4`, which works for local preview. On
Squarespace you need the video at a public URL. Easiest options:

1. **Squarespace CDN**: in any Squarespace editor, add a link to something, choose
   "File" → upload `assets/hero-loop.mp4`, save, then copy the file's URL (it will look like
   `/s/hero-loop.mp4` — use the full `https://www.centerlineworks.com/s/hero-loop.mp4`).
   Do the same for `assets/hero-poster.jpg`.
2. **Any file host** you already use (Cloudinary, S3, etc.).

Then replace the two `src="assets/hero-loop.mp4"` and two `poster="assets/hero-poster.jpg"`
references in the code (one pair in the hero, one pair in the CTA section) with your hosted
URLs — they're marked with `EDIT ME` comments.

## Before you publish — personalize these (search the file for `EDIT ME`)

- **Photos**: most cards are wired to real filenames served from Squarespace file storage
  (see DEPLOY.md step 2 for the upload list). Still open: the **Additions** and **Kitchens**
  work cards have no photo yet, and three guessed `.jpg` extensions may need correcting.
- **Family details**: the owner section says "devoted husband and father" — add names and any
  personal details you'd like to share.
- **Google review link**: swap the generic Google search link in the reviews section for your
  Google Business Profile review link (Google Business Profile → "Ask for reviews").
- **Button links**: confirm the `/schedule` and `/services` page slugs; the Contact Us
  buttons use tel/mailto links (call at the top, Info@centerlineworks.com at the bottom).
- **Stats**: 18+ years, founded 2020, 43 five-star reviews — adjust as the numbers grow.

## The Services page (`services.html`)

A combined services-and-portfolio page — every service explained alongside real project
photos, instead of splitting "Services" and "Portfolio" into separate pages.

- **Seven services**, each with a description, a chip list of what's included, and a
  **4-photo gallery**: Bathrooms, Basements, Cabanas, Additions, Decks & Outdoor, Siding &
  Exterior, and Commercial.
- **Its own hero video** — a poolside cabana/pavilion project (`assets/services-hero.mp4`)
  — kept completely separate from the About page's video so each page can show different
  footage independently.
- **Fully responsive in one file** — no separate phone version. Galleries become swipeable
  strips and a sticky Get Estimate / Call / Email bar appears automatically on phones; the
  same content and code serve every screen size.
- **3D effects to match the About page** — parallax hero text, sections that flip up in 3D
  as they scroll into view, and mouse-tilt on the "How It Works" cards (desktop only; all
  disabled under reduced motion).
- **Before/after comparison reveal** — hover any gallery photo that has a matching "before"
  photo configured and it slides open to compare, tracking your mouse left-right in real
  time; move off and it closes back to just the finished photo. Squares without a before
  photo keep a simple hover zoom instead. Currently wired up on the first bathroom photo
  (IMG_2415 before → IMG_2657 after); every other photo slot has an empty, ready-to-fill
  `_before` counterpart.
- **Sticky anchor nav** below the hero jumps to any service and highlights the one in view.
- **Lightbox** — click any real (non-comparison) photo to view it full-size; click outside,
  the × button, or press Escape to close. Empty photo spots aren't clickable.
- **"How It Works"** 3-step process section (Consultation → Plan & Quote → Build &
  Walkthrough) and a trust strip linking to the About page's reviews.
- **Photos**: a `window.CL_SERVICES_PHOTOS` list at the top of the code block, 4 "after"
  slots per service (28 total) plus a matching optional `_before` slot for each (56 lines
  total) — same "paste the image address" workflow as the About page. A few "after" slots
  are pre-filled with photos already gathered for the About page (bathrooms, basements,
  decks, siding, commercial); Cabanas, Additions, and the remaining slots in every category
  are open. An empty slot shows a text label, never a broken image; an empty `_before` slot
  just means that square has no comparison, nothing more.
- **SEO/GEO**: its own `HomeAndConstructionBusiness` + `BreadcrumbList` + a `Service` entity
  per offering in JSON-LD, plus title/meta/OG tags specific to Services.
- See **[DEPLOY.md](DEPLOY.md#deploying-the-services-page)** for install steps, including
  uploading its own video files.
