# Put the pages live on Squarespace — step by step

This repo has two pages: **About** (`index.html`) and **Services** (`services.html`), each
with its own pair of paste files in `squarespace/`. Steps 1–7 below cover the About page;
jump to **"Deploying the Services page"** at the bottom once that's live — it reuses the
same video files and skips most of the setup.

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
6. **Photos**: near the top of the code block is a **`YOUR SERVICE PHOTOS`** list — 4 spots
   per service (28 total). A few are already filled in with photos reused from the About
   page (bathrooms, basements, decks, siding, commercial); Cabanas and Additions, plus the
   remaining spots in every category, are waiting on photos. Same method as the About page:
   put each photo on a page with an Image Block, right-click → Copy Image Address, paste it
   into the matching line. An empty spot just shows a text label — nothing looks broken
   while you fill it in.
7. Click any real photo on the live page to open it full-size in a lightbox; click outside
   it, the × button, or press Escape to close.
8. Every "Explore Our Services" link on the About page already points here.
