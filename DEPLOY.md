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

The page expects the video files at `centerlineworks.com/s/hero-loop.mp4` (etc.), which is
exactly where Squarespace puts uploaded files **as long as you don't rename them**.

1. In Squarespace, edit any page and add a text block, type a word, highlight it, and click
   the **link** icon
2. In the link editor choose **File** → **Upload file** → upload `hero-loop.mp4`
3. Repeat for `hero-loop.webm` and `hero-poster.jpg`
4. Delete the temporary text block (the uploaded files stay in your file storage)
5. Check it worked: visit `https://www.centerlineworks.com/s/hero-loop.mp4` — the video
   should play in your browser

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

- Swap the 8 photo placeholders for real photos (story, six work cards, you/family)
- Fill in the two `[ Customer name ]` review attributions and verify Joni's quote is hers
- Swap the generic Google link for your Google Business Profile review link
- Confirm the button links: `/schedule`, `/contact`, `/newservices`
- Add family names/details to the owner section if you'd like
- Replace the `og:image` URL in Part 1 with a real photo for nice link previews

## If something looks off

- **No video playing** → Step 2's URL check failed; re-upload without renaming the files
- **Page looks like plain text** → the Code block type isn't set to HTML, or you're on the
  Personal plan (JavaScript blocked)
- **Fonts look plain** → hard-refresh (Ctrl+Shift+R); the Google Fonts link is in Part 1
- Still stuck? Come back to this chat and tell me what you're seeing.
