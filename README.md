# Centerline Construction — About Page

An eye-catching About page for [centerlineworks.com](https://www.centerlineworks.com) with 3D
scroll effects, built to drop into Squarespace. Everything lives in one file: **`index.html`**.

## What's inside

- **Looping drone video backgrounds** — the crew-framing-an-addition drone clip
  (`assets/hero-loop.mp4`, compressed from 6.6MB to 1.7MB for fast loading, with a poster
  image fallback) plays silently behind the hero and again behind the closing call-to-action.
  It pauses automatically for reduced-motion visitors.
- **3D scroll experience** — a wireframe house that rotates and grows as visitors scroll, a
  perspective blueprint grid that drifts under the hero, parallax headline layers, sections that
  flip up in 3D as they enter the screen, and value cards that tilt toward the mouse on desktop.
- **Action buttons throughout** — "Schedule an Estimate" (`/schedule`), "Contact Us"
  (`/contact`), "Explore Our Services" (`/newservices`), and click-to-call, placed in the hero,
  story, work showcase, owner section, and closing CTA.
- **Our Story** — the "centerline" founding story: faith, integrity, craftsmanship, founded 2020,
  18+ years of experience, with animated stat counters.
- **Services** — bathrooms, basements, kitchens, home additions, decks & railing, siding, wood rot
  repair, cabinetry, exterior repairs, commercial.
- **Our Work showcase** — an auto-scrolling horizontal banner of project categories (Bathrooms,
  Basements, Additions, Kitchens, Decks & Outdoor, Siding & Exterior), each with a photo slot for
  a real project shot. It glides on its own, pauses on hover/touch, and becomes a normal
  swipeable strip for reduced-motion visitors.
- **Real reviews** — three actual client quotes attributed by name ("— Joni Dunnington · Google
  Review" style), with links to both Google Reviews and Facebook.
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

> Code Blocks with JavaScript require the Squarespace **Business plan or higher**.

`index.html` is split into two clearly marked parts:

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

- **Photos**: eight placeholder frames are marked in the code — a team/project photo in the story
  section, six project-category cards in the Our Work banner (shower/bathroom, basement, addition,
  kitchen, deck, siding), and a photo of Alfred (or the whole family) in the owner section. Upload
  images to Squarespace and swap in the `<img>` tags per the comments.
- **Family details**: the owner section says "devoted husband and father" — add names and any
  personal details you'd like to share.
- **Reviewer names**: the review cards are attributed "— Joni Dunnington · Google Review" style;
  verify each name matches the person who actually wrote that quote, and fill in the two
  `[ Customer name ]` placeholders from your Google/Facebook reviews.
- **Google review link**: swap the generic Google search link in the reviews section for your
  Google Business Profile review link (Google Business Profile → "Ask for reviews").
- **Button links**: buttons point to `/schedule`, `/contact`, and `/newservices` on
  centerlineworks.com — confirm those match your actual page slugs.
- **Social share image**: replace the `og:image` URL in Part 1 with a real uploaded photo.
- **Stats**: 18+ years, founded 2020, and 100% Facebook recommendation — adjust if anything
  changes.
