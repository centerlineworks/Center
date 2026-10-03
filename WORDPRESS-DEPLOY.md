# Moving centerlineworks.com to WordPress — step by step

This is the WordPress twin of `DEPLOY.md`. Same four pages, same design, same 3D drum — just
built for a different host. Written so you can keep Squarespace live while you build and test
this, and only switch over once everything checks out.

**The plan, in order:**

1. Set up WordPress + two free plugins (this page)
2. Upload your videos and photos
3. Build the four pages
4. Test everything on the new site, with Squarespace still live
5. Only then point your domain at WordPress

Don't skip to step 5. Keeping Squarespace running until WordPress is fully tested is what
makes this safe to do in a day or two instead of risking the live site.

---

## What ported over cleanly, and what needed rebuilding

Worth understanding before you start, so none of this feels like guesswork:

- **The pages themselves** — all the 3D effects, the review carousel, the drum, the live
  map — are plain HTML/CSS/JavaScript with no Squarespace-specific code in them. They paste
  into WordPress exactly the way they paste into Squarespace, just into a different kind of box
  (a "Custom HTML" block instead of a "Code" block).
- **Video and logo addresses** were automatically rewritten from Squarespace's file address
  (`/s/<filename>`) to WordPress's (`/wp-content/uploads/<filename>`) — same filenames, so once
  you upload the same files, these just work.
- **The Schedule page's "send it to my inbox automatically" piece** did need rebuilding. On
  Squarespace it looks for your Form Block and uses Squarespace's own Submit button. WordPress
  has no built-in form system, so this version looks for a form built with the free **WPForms**
  plugin instead (see Step 2 below). Without that plugin, it still works exactly like it does
  today — it opens the visitor's email with everything filled in.
- **Your project photos** are the one thing that didn't move automatically, and can't — they're
  not uploaded files, they're pictures living in Squarespace's own photo library at addresses
  only Squarespace knows. You'll re-upload these to WordPress's photo library and give me (or
  paste in yourself) the dozen new addresses. See Step 5.

---

## Step 1 — Get WordPress running

You said you don't have hosting yet, so here's what to look for — I'm not picking a company for
you, this is a real purchase and your call:

- Any host advertising **"1-click WordPress install"** or **"Managed WordPress"** works. Common
  ones people use: Hostinger, SiteGround, Bluehost, WP Engine — there are many others, and
  price/support matter more than the brand.
- You do **not** need a page-builder plan (Elementor, Divi, etc.) — everything here is built to
  work on the plain WordPress editor that comes free with any install.
- While you're choosing, ask whichever host you pick two questions: **"What's the file upload
  size limit?"** (your videos are a few MB each — anything above 32MB handles them fine) and
  **"Do you include a free SSL certificate?"** (say yes to it if offered — it's what makes the
  address start `https://`).
- **Don't point centerlineworks.com at it yet.** Every host gives you a temporary address to work
  with first (something like `yoursite.hostingcompanyname.com`) — build and test on that, and
  only move the real domain over in the final step.

Once WordPress is installed, log in to its dashboard (usually `yoursite.com/wp-admin`).

---

## Step 2 — Install two free plugins

In the dashboard: **Plugins → Add New Plugin**, search, **Install**, then **Activate**.

### WPCode (for the invisible per-page code — same job as Squarespace's "Page Header Code Injection")

Search for **"WPCode"** (sometimes listed as "Insert Headers and Footers"). This is where each
page's meta tags, search-engine data, and styling go.

### WPForms Lite (makes the Schedule page email + save requests automatically — optional but recommended)

Search for **"WPForms"**, install the **free "Lite"** version — you don't need to pay for
anything. This is the WordPress equivalent of the Squarespace Form Block you set up before.
Skip this if you're OK with the Schedule page falling back to opening the visitor's email app —
it still works fine without it, just one extra tap for the visitor.

---

## Step 3 — Turn off date folders, then upload your videos

WordPress normally files uploads into dated folders (`/wp-content/uploads/2026/10/`), which
would break the addresses already written into the code. One checkbox fixes that:

1. **Settings → Media**
2. Uncheck **"Organize my uploads into month- and year-based folders"**
3. **Save Changes**

Now every file you upload lives at a flat, predictable address:
`centerlineworks.com/wp-content/uploads/<exact filename>`.

Go to **Media → Add New**, and upload these files from the `assets/` folder in the GitHub repo,
**keeping the exact filenames**:

| Upload this file | What it is |
| --- | --- |
| `hero-loop.mp4` + `hero-loop.webm` + `hero-poster.jpg` | About page's looping crew footage |
| `home-owner.mp4` + `home-owner.webm` + `home-owner-poster.jpg` | Home page's "Meet the Owner" video |
| `services-hero.mp4` + `services-hero.webm` + `services-hero-poster.jpg` | Services + Schedule pages' hero video |
| `centerline-logo-transparent.png` | **Rename this to `centerline-logo.png` before uploading** — it's the fallback image if a visitor's browser can't show the built-in logo (rare, but free to cover) |

That's 10 files. Nothing else needs uploading yet — your actual logo is already built into the
page code itself (no upload needed, same as it is on Squarespace today).

---

## Step 4 — Build the four pages

For each page below: **Pages → Add New**, give it the exact title and slug shown, then:

1. Click the **(+)** block inserter, search **"Custom HTML"**, add the block, and paste in the
   matching `wordpress/*-block.html` file from the repo (and `about-phone-addon.html` too, for
   About — paste it into a **second** Custom HTML block right after the first one)
2. **Publish** the page
3. Open **Code Snippets → Add New** (WPCode's menu) *or* use WPCode's "Header" panel if it
   offers one, paste in the matching `wordpress/*-header.html` file, set **Insert Location** to
   **Head**, set **Scope / Where** to **Specific Pages** and pick this one page, then **Save**
   and make sure it's toggled **Active**

| Page | Title | Slug (URL) | Paste these files |
| --- | --- | --- | --- |
| Home | Home | `/` (your site's front page — see note below) | `wordpress/home-header.html` + `wordpress/home-block.html` |
| About | About | `/about` | `wordpress/about-header.html` + `wordpress/about-block.html` + `wordpress/about-phone-addon.html` |
| Services | Services | `/services` | `wordpress/services-header.html` + `wordpress/services-block.html` |
| Schedule | Schedule | `/schedule` | `wordpress/schedule-header.html` + `wordpress/schedule-block.html` |

**The slugs matter.** Every "Schedule an Estimate" button, every internal link, and your Google
rankings all depend on these exact addresses — `/about`, `/services`, `/schedule`. Don't let
WordPress auto-generate something like `/about-2`.

**Making Home your front page:** after publishing it, go to **Settings → Reading**, choose **"A
static page"**, and set **Homepage** to your Home page.

**SEO title:** your theme usually turns the page's **Title** field (the one at the very top of
the editor) into the clickable blue link in Google results. Set it to match what's already in
`README.md`'s SEO section for each page (e.g. for Home: `Centerline Construction | Remodeling
Contractor in Holly Springs & Canton, GA`). If you want finer control later, a free SEO plugin
like **Yoast SEO** or **Rank Math** adds a dedicated box for this on every page — not required
to launch, worth adding eventually.

---

## Step 5 — Swap in your real project photos

Everything above gets your pages fully working with placeholder-free video, your real logo, and
every bit of the design — except a dozen project photos, which are still pointing at
Squarespace's photo library. They'll keep working for now (as long as Squarespace stays active),
but need to move before you turn Squarespace off for good.

1. **Media → Add New**, upload each photo below (any filename is fine this time — write down
   the new address it gives you, found by clicking the uploaded photo and copying its **File
   URL** / **Copy URL** link)
2. Send me the 12 new addresses (paste them in chat, or commit them to the repo on GitHub the
   way you've done before) and I'll swap every one into the right spot across all three pages in
   one pass — these exact same photos are reused between Home, Services and About, so it's one
   clean update, not twelve separate ones.

| Current filename | Appears on |
| --- | --- |
| `IMG_2657.jpg` | Home, Services (Bathrooms) |
| `IMG_2415.JPG` | Home, Services, About (Bathrooms before-photo) |
| `basement333.jpg` | Home (Basements) |
| `5123309364774959038.jpg` | Services, About (Basements) |
| `dji_fly_20260212_094138_86_...jpg` | Home, Services, About (Decks) |
| `dji_fly_20260604_094024_92_...jpg` | Home, Services, About (Siding) |
| `IMG_8669.JPG` | Home, Services, About (Commercial) |
| `IMG_1661-EDIT (1).jpg` | Home, About (Alfred's portrait) |
| `IMG_1176.JPG` | Home (Alfred, cedar project) |
| `IMG_1704.JPG` | Home, About (crew photo) |
| `dji_fly_20260612_195606_114_...jpg` | About only |
| `PXL_20250226_233210463.jpg` | About only |

Until you do this, nothing is broken — these photos simply keep loading from Squarespace in the
background, same as they do on the live site today.

---

## Step 6 — Set up WPForms on the Schedule page (optional but recommended)

Without this, the Schedule page still works — pressing Submit opens the visitor's email app
with everything filled in. With it, requests are saved inside WordPress and emailed to you
automatically, the same as the Squarespace version does.

1. **WPForms → Add New**, start from a **blank form**, name it "Estimate Request"
2. Add these fields, in this order:
   - **Name** field — either "Simple" (one box) or "First/Last" (two boxes), both work
   - **Phone** field
   - **Email** field
   - **Paragraph Text** field, labeled "Tell us about your project"
3. **Settings → Notifications** — confirm it's set to email `Info@centerlineworks.com`
4. **Settings → Confirmations** — leave as default (the visitor never actually sees this screen;
   our page submits on their behalf and shows its own "sent" message)
5. **Save**, then **Embed** the form onto the **Schedule page** — add a normal WordPress block
   (not Custom HTML) anywhere on the page, search **"WPForms"**, pick your new form
6. **Update** the page

The Schedule page's own script finds this form automatically, lifts it onto the last card of
the drum, fills it in from everything the visitor already answered, and the big gold button
becomes **"Submit My Request"** — pressing it submits the real WPForms form behind the scenes.
If you ever remove the form, the page quietly falls back to the email hand-off — it can't break.

---

## Step 7 — llms.txt

The `llms.txt` file (see `README.md`) needs re-adding here too — WordPress doesn't have a
Squarespace-style settings toggle for it, but it's actually simpler: install a small plugin
like **"WP File Manager"** or ask your host for FTP access, and upload `llms.txt` from this repo
straight into the site's root folder, so it's reachable at `centerlineworks.com/llms.txt`.

---

## Step 8 — Test everything before touching your domain

With the site live on its temporary address, go through this list:

- [ ] All four pages load, videos play, the logo shows with no white box behind it
- [ ] Phone view: open each page on your actual phone (use the temporary address)
- [ ] Reviews carousel scrolls and the counter works on Home and About
- [ ] Schedule page: the drum turns, the map pin lands on the right town, the work order fills
      in as you answer
- [ ] Press Submit on the Schedule page (use a real email you check) and confirm you get it
- [ ] Every "Schedule an Estimate" / "Call" / phone number link works
- [ ] View each page's source (right-click → "View Page Source") and confirm you see the meta
      tags and the big `<script type="application/ld+json">` block near the top — if it's
      missing, the WPCode snippet for that page isn't active

Only move to Step 9 once every box is checked.

---

## Step 9 — Point your domain at WordPress

This is the one truly irreversible-feeling step, so do it carefully and keep Squarespace paid
and running for at least a week or two afterward as a safety net.

1. In your new WordPress host's dashboard, find where it tells you to point your domain (it'll
   say something like "add your domain" or give you nameservers / an IP address to use)
2. Log in to wherever centerlineworks.com's domain is currently managed (this might be
   Squarespace Domains, or a separate registrar like GoDaddy/Namecheap) and update the DNS
   records to point at your new WordPress host, following their instructions exactly
3. DNS changes can take anywhere from a few minutes to about 24 hours to fully take effect
   everywhere — this is normal, not a sign anything broke
4. Once centerlineworks.com is showing the WordPress site, **do not cancel Squarespace yet.**
   Keep it active for a week or two. If anything looks wrong on WordPress, you can switch the
   DNS back in minutes while we fix it
5. **Keeping the same URLs (`/`, `/about`, `/services`, `/schedule`) is what protects your
   Google ranking through this move** — since the addresses don't change, Google treats it as
   the same site on a new host, not a new site to rank from scratch

Once you're confident everything's solid, add Bing/Google Search Console verification for the
new host if it asks, and you're done.
