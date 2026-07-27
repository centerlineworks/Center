# Put the About page live on Squarespace — step by step

Total time: about 15 minutes. You need the **Squarespace Business plan or higher**
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
