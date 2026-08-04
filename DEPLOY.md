# Put the pages live on Squarespace — step by step

This repo has three pages: **Home** (`home.html`), **About** (`index.html`) and
**Services** (`services.html`), each with its own pair of paste files in `squarespace/`.
Steps 1–7 below cover the About page; the **Services** and **Home** sections at the bottom
cover those.

Total time: about 15 minutes per page. You need the **Squarespace Business plan or higher**
(code blocks with JavaScript don't run on the Personal plan).

## Step 1 — Download the files from GitHub

1. Go to **github.com/centerlineworks/Center**
2. Click the green **Code** button → **Download ZIP**
3. Unzip it. You'll use:
   - `squarespace/part1-header-injection.html`
   - `squarespace/part2-code-block.html`
   - `assets/hero-loop.mp4`, `assets/hero-loop.webm`, `assets/hero-poster.jpg`

## Step 2 — Upload the three video files to Squarespace

The page expects the videos at `centerlineworks.com/s/hero-loop.mp4` (etc.), which is
exactly where Squarespace serves uploaded **files** — as long as you don't rename them.

1. In Squarespace, edit any page and add a text block, type a word, highlight it, and click
   the **link** icon
2. In the link editor choose **File** → **Upload file** → upload `hero-loop.mp4`
3. Repeat for `hero-loop.webm` and `hero-poster.jpg` (from the `assets` folder)
4. Delete the temporary text block (the uploaded files stay in your file storage)
5. Check it worked: visit `https://www.centerlineworks.com/s/hero-loop.mp4` — the video
   should play in your browser

## Step 2b — Hook up your photos (asset-library friendly)

Photos in the Squarespace **asset library** live at Squarespace's own image-CDN addresses,
so the page can't guess them. Instead, the very top of the code block has a clearly marked
**`YOUR PHOTOS` list** — you paste each picture's address between the quotes, once.

To get a photo's address:

1. Put the image on any page with a normal **Image Block** (a hidden "not linked" page is
   fine) and save
2. View that page on the live site, **right-click the image → "Copy Image Address"**
3. Paste it into the matching line of the `YOUR PHOTOS` list in the code block
   (e.g. `story: "https://images.squarespace-cdn.com/...",`)
4. Repeat for each photo, then save the page. You can delete the temporary page afterward —
   the addresses keep working.

A spot with no working address shows a small text label instead of a broken image, so
nothing ever looks broken while you work through the list.

## Step 3 — Create the About page

1. **Pages** → click **+** → **Blank Page**, name it **About**
2. In **Page Settings → General**, set the URL slug to `/about`
3. In **Page Settings → SEO**, set the SEO title to:
   `About Centerline Construction | Alfred Tudela | Holly Springs & Canton, GA Remodeling Contractor`

## Step 4 — Paste Part 1 (the invisible plumbing)

1. Open `squarespace/part1-header-injection.html` in any text editor (Notepad/TextEdit),
   select all, copy
2. In Squarespace: **Page Settings → Advanced → Page Header Code Injection** → paste → Save

## Step 5 — Paste Part 2 (the visible page)

1. Open `squarespace/part2-code-block.html`, select all, copy
2. Edit the About page, add a **Code** block (type: HTML, "Display Source" OFF), paste, Save
3. If the page section adds white padding around the block, set the section's spacing/padding
   to minimum so the design runs edge to edge

## Step 5b — Optional: the phone-only version (Part 3)

`squarespace/part3-phone-addon.html` is a separate, app-style layout just for phones —
sticky Get Estimate / Call / Email buttons at the bottom, swipeable work gallery and
review cards, a full-screen video hero. Computers and tablets keep the original design.

1. Open `part3-phone-addon.html`, select all, copy
2. Edit the About page's Code Block and paste it **below** the existing Part 2 code
   (don't change Part 2 itself), then Save

That's it — the code decides by screen width: 767px and narrower gets the phone version,
768px and wider gets the original. The phone version borrows every photo and review from
Part 2 automatically, so future content edits only ever happen in one place.

## Step 6 — Look at it!

Open the page on your phone and computer. You should see the drone video playing behind the
headline, the 3D house rotating as you scroll, and the work banner gliding.

## Step 7 — Finish the personal touches (whenever you're ready)

Search the code block for `EDIT ME`:

- Add photos for the two work cards still waiting on one: **Additions** and **Kitchens**
- Swap the generic Google link in the reviews section for your Google Business Profile
  review link
- Confirm the `/schedule` and `/services` page slugs ("Contact Us" buttons now call
  (678) 372-1274 at the top and email Info@centerlineworks.com at the bottom)
- Add family names/details to the owner section if you'd like

## If something looks off

- **No video playing** → Step 2's URL check failed; re-upload without renaming the files
- **Photos show text labels** → their addresses aren't filled in yet; see Step 2b
- **Black empty area between the last section and the footer** → make sure you re-pasted
  the latest Part 1 (it collapses the host section automatically). If a sliver remains,
  edit the page, click the section containing the code block → pencil icon → set **Section
  Height** to Small and **Padding** to 0
- **Page looks like plain text** → the Code block type isn't set to HTML, or you're on the
  Personal plan (JavaScript blocked)
- **Fonts look plain** → hard-refresh (Ctrl+Shift+R); the Google Fonts link is in Part 1
- Still stuck? Come back to this chat and tell me what you're seeing.

---

## Deploying the Services page

The Services page shows every service (Bathrooms, Basements, Cabanas, Additions, Decks &
Outdoor, Siding & Exterior, Commercial) with its own photo gallery — a combined
"services + portfolio" page. It's **fully responsive in one file** — no separate phone
version to paste; the same code reshapes itself into swipeable galleries and a sticky
Get Estimate / Call / Email bar automatically on phones.

It has **its own hero video** (a poolside cabana/pavilion project) — separate from the
About page's video, so both pages can show different footage without one affecting the
other.

1. **Pages** → **+** → **Blank Page**, name it **Services**, set its URL slug to `/services`
2. Set the SEO title (Page Settings → SEO) to:
   `Our Services | Bathrooms, Basements, Cabanas & More — Centerline Construction`
3. Upload the Services page's own video files the same way as the About page's (Link
   editor → **File** → **Upload file**, keep the filenames exactly): `services-hero.mp4`,
   `services-hero.webm`, `services-hero-poster.jpg` (all in the `assets` folder). Confirm
   it worked by visiting `https://www.centerlineworks.com/s/services-hero.mp4` directly.
4. Open `squarespace/services-part1-header-injection.html`, select all, copy → paste into
   **Page Settings → Advanced → Page Header Code Injection** → Save
5. Open `squarespace/services-part2-code-block.html`, select all, copy → add a **Code**
   block (type: HTML) to the page, paste, Save
6. **Photos**: near the top of the code block is a **`YOUR SERVICE PHOTOS`** list — 4 "after"
   spots per service (28 total). A few are already filled in with photos reused from the
   About page (bathrooms, basements, decks, siding, commercial); Cabanas and Additions, plus
   the remaining spots in every category, are waiting on photos. Same method as the About
   page: put each photo on a page with an Image Block, right-click → Copy Image Address,
   paste it into the matching line. An empty spot just shows a text label — nothing looks
   broken while you fill it in.
7. **Before/after photos (optional)**: every spot in that same list also has a matching
   `_before` line right below it. Fill one in and hovering that square on the live page
   slides open the before photo as you move your mouse across it, closing back to just the
   after photo when you move away — no code changes needed, just paste the address. One
   pair is already set up (the first bathroom photo) as a working example. Leave a
   `_before` line blank and that square stays a normal photo with a gentle hover zoom.
8. Click any real photo on the live page to open it full-size in a lightbox — a photo with
   a before pair opens a zoomed-in side-by-side before/after instead; click outside it, the
   × button, or press Escape to close.
9. Every "Explore Our Services" link on the About page already points here.

### If the Services page video isn't playing

This page uses its **own** video files (`services-hero.mp4/.webm/-poster.jpg`) — separate
from the About page's `hero-loop.*` files, uploaded in Step 3 above. If nothing plays:

- Double check those 3 files were actually uploaded — visit
  `https://www.centerlineworks.com/s/services-hero.mp4` directly in your browser; if it
  doesn't play there either, they either weren't uploaded or got renamed on upload
- If the About page's video works but this one doesn't, that almost always means Step 3
  was skipped (easy to miss since it's easy to assume "I already uploaded a video" from
  setting up About) — go back and upload these 3 specific files
- Make sure you re-pasted the **current** `services-part1` and `services-part2` files from
  GitHub — an older paste from before the video existed won't reference it at all


---

## Deploying the Home page

The home page is the one that has to land the client, so it leads with the video hero, the
5.0 / 43-review trust chips and a free-estimate button above the fold, then walks visitors
through services, real before/after work, why Centerline, the 3-step process, Alfred,
reviews, service area and FAQ. Fully responsive in one file — on phones the service and
work rows become swipe rails and a sticky **Free Estimate / Call / Email** bar sits in the
thumb zone.

1. In Squarespace open your existing **Home** page (or create a Blank Page and set it as
   your homepage under Pages → ⋯ → *Set as Homepage*)
2. Set the SEO title (Page Settings → SEO) to:
   `Centerline Construction | Remodeling Contractor in Holly Springs & Canton, GA`
3. Paste `squarespace/home-part1-header-injection.html` into
   **Page Settings → Advanced → Page Header Code Injection** → Save
4. Add a **Code** block (type: HTML) to the page, paste
   `squarespace/home-part2-code-block.html`, Save
5. **Upload your logo** (one new file). Same method as the videos: Link editor → **File**
   → **Upload file**, and name it exactly **`centerline-logo.png`**. Use the version with
   **white "CONSTRUCTION" lettering on a transparent background** — the hero behind it is
   dark. Until it's uploaded the page shows a styled stand-in lockup, so nothing looks
   broken; the real logo takes over automatically the moment the file exists.
6. **Upload the Meet the Owner video** (3 files, same Link editor → **File** → **Upload
   file** method, keep the names exactly): `home-owner.mp4`, `home-owner.webm`,
   `home-owner-poster.jpg` from the `assets` folder. That's your own work-and-life reel.
   The hero still reuses `services-hero.*`, which is already on your site.
7. **Reviews are built in** — no widget, nothing to configure. A "5.0 · 43 reviews"
   scoreboard sits above a carousel holding all 39 of your real reviews. Visitors can use
   the arrows, drag it, swipe it on a phone, or just let it advance on its own. To add a
   new review later, find the review carousel in the code block, copy any
   `<article class="cl-rev-card">` block, and change the quote, the name and the platform.
8. **Review counts**: the `YOUR REVIEW COUNTS` list at the very top of the code block holds
   your rating and a count per platform. When Google gains a review, change that one number
   and the hero chip, the stat counter, the reviews headline and the platform badges all
   update themselves.
9. **Optional videos on the "What we build" cards**: the `OPTIONAL VIDEOS` list at the top
   of the code block has one line per card. Upload a short silent clip as a File and paste
   its address; it fades in over that card's photo once it's actually playing. The photo
   always loads first and stays as the fallback, so a slow or missing video never leaves a
   blank card. Clips only load when the card scrolls into view, pause when it scrolls away,
   and are skipped for visitors using reduce-motion or data saver.
10. **Photos**: the `YOUR HOME PAGE PHOTOS` list at the top of the code block. Cabanas and
   Additions are the two waiting on a photo; everything else is pre-filled. Any `*_before`
   line is optional — fill one in and that photo becomes a hover before/after comparison.

### Want the home page to have its own hero video?

Right now Home and Services share `services-hero.*`, so replacing that file changes both.
If you'd rather they be independent, send me new footage and I'll encode it as
`home-hero.*` — then only the home page changes when you swap it.
