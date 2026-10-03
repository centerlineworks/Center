#!/usr/bin/env python3
"""Generate WordPress-ready paste files from the already-verified Squarespace
paste files in squarespace/.

Why start from squarespace/*.html instead of the page sources directly: those
files are the exact, already-tested "body to paste into a block" content —
re-deriving from home.html/index.html/etc. would risk reintroducing a bug
that's already been fixed once. This script only does the narrow, mechanical
changes WordPress actually needs:

  1. Every uploaded-file URL (https://www.centerlineworks.com/s/<file>) becomes
     a WordPress Media Library URL (https://www.centerlineworks.com/wp-content/
     uploads/<file>) — same filename, same domain, so it's a pure prefix swap.
     This assumes Alfred has turned OFF "organize uploads into month/year
     folders" in Settings -> Media BEFORE uploading (see WORDPRESS-DEPLOY.md) —
     otherwise WordPress nests files under /uploads/2026/10/ and the filenames
     alone won't resolve.
  2. The Schedule page's Squarespace Form Block bridge is retargeted to
     WPForms (the free plugin recommended in WORDPRESS-DEPLOY.md): selectors,
     function names and comments are swapped from Squarespace's
     .sqs-block-form/.form-item/.sqs-system-button to WPForms'
     .wpforms-container/.wpforms-field/.wpforms-submit. Nothing about the
     one-step logic, the work-order ticket, or the mailto fallback changes.
  3. The leading instructional comment on each file is rewritten for the
     WordPress workflow (Custom HTML block + WPCode, not Code Block + Page
     Header Code Injection).

images.squarespace-cdn.com photo URLs are intentionally left untouched — those
are real project photos Alfred uploaded to Squarespace's asset library, and
there is no mechanical way to know their new WordPress Media Library URLs
ahead of time. See WORDPRESS-DEPLOY.md for that manual (one-time) step.

Run: python3 tools/gen_wordpress.py
"""
import pathlib

ROOT = pathlib.Path("/home/user/Center")
SQ = ROOT / "squarespace"
WP = ROOT / "wordpress"
WP.mkdir(exist_ok=True)

MEDIA_OLD = "https://www.centerlineworks.com/s/"
MEDIA_NEW = "https://www.centerlineworks.com/wp-content/uploads/"


def sub_media(text):
    return text.replace(MEDIA_OLD, MEDIA_NEW)


# ---------------------------------------------------------------------------
# Leading-comment rewrites (exact string swap of the file's opening <!-- --> )
# ---------------------------------------------------------------------------
# A couple of smaller, page-specific wording fixes that don't fit the bigger
# categories above — comments that explained a Squarespace-theme quirk and
# would be misleading left as-is on a WordPress page.
MISC_HEADER_SUBS = {
    "home-part1-header-injection.html": [
        (
            """  /* ---------- Logo: dropped in as-is, never recreated ----------
     The Squarespace theme likes to paint a background (and sometimes a border or
     radius) onto images inside code blocks, which shows up as a white slab behind
     a transparent PNG. Nothing here ever wants that, so it is forced off. */""",
            """  /* ---------- Logo: dropped in as-is, never recreated ----------
     Squarespace's theme used to paint a background (and sometimes a border or
     radius) onto images inside code blocks, which showed up as a white slab
     behind a transparent PNG — WordPress block themes don't do this, but the
     rule is harmless to keep as a safety net against a theme that does. */""",
        ),
    ],
    "home-part2-code-block.html": [
        (
            """  /* ---------- Photos ----------
     All load detection happens here in JS on purpose — never via inline
     onload/onerror attributes (Squarespace's code-block sanitizer can strip
     them) and never by hiding images with display:none (a hidden lazy image
     is never fetched, so it would never reveal itself). Images sit at
     opacity:0 until confirmed loaded. */""",
            """  /* ---------- Photos ----------
     All load detection happens here in JS on purpose — never via inline
     onload/onerror attributes (some page builders and security plugins strip
     them) and never by hiding images with display:none (a hidden lazy image
     is never fetched, so it would never reveal itself). Images sit at
     opacity:0 until confirmed loaded. */""",
        ),
        (
            """    /* Reading pixels back off a canvas is blocked for images the browser
       considers cross-origin. Squarespace may serve /s/ files from its own CDN
       host, which would silently kill the knockout — so if the direct attempt
       is refused, retry through a proper CORS request. The cache-buster matters:
       without it the browser can hand back the copy it already fetched without
       CORS headers, and that copy taints the canvas all over again. */""",
            """    /* Reading pixels back off a canvas is blocked for images the browser
       considers cross-origin. A CDN or caching/security plugin in front of
       your WordPress Media Library can serve files without the right CORS
       headers, which would silently kill the knockout — so if the direct
       attempt is refused, retry through a proper CORS request. The
       cache-buster matters: without it the browser can hand back the copy it
       already fetched without CORS headers, and that copy taints the canvas
       all over again. */""",
        ),
        (
            """      /* The logo is embedded as a WebP data URI. Every current browser reads
         those, but if one ever can't, fall back to the copy in your Squarespace
         file storage rather than showing nothing. */""",
            """      /* The logo is embedded as a WebP data URI. Every current browser reads
         those, but if one ever can't, fall back to the copy in your WordPress
         Media Library rather than showing nothing. */""",
        ),
    ],
    "services-part2-code-block.html": [
        (
            """     onload/onerror attributes on the <img> tags. Squarespace's code-block
     sanitizer can strip inline event handlers, and a hidden lazy-loaded image""",
            """     onload/onerror attributes on the <img> tags. Some page builders and
     security plugins strip inline event handlers, and a hidden lazy-loaded image""",
        ),
    ],
    "part2-code-block.html": [
        (
            """         EDIT ME (Squarespace): after uploading, replace both video src URLs and the
         poster URL with your hosted file URLs — see README "Hosting the video". -->""",
            """         EDIT ME: after uploading to the WordPress Media Library, replace both
         video src URLs and the poster URL with your hosted file URLs — see
         README "Hosting the video". -->""",
        ),
        (
            "<!-- EDIT ME: confirm the /schedule URL matches your Squarespace page slug -->",
            "<!-- EDIT ME: confirm the /schedule URL matches your WordPress page slug -->",
        ),
        (
            """         EDIT ME (Squarespace): replace src/poster with your hosted URLs. -->""",
            """         EDIT ME: replace src/poster with your WordPress Media Library URLs. -->""",
        ),
        (
            """   How to get a photo's address from Squarespace:
     1. Put the image on any page with a normal Image Block (a hidden/
        unlinked page is fine) and save.
     2. View that page on the live site, right-click the image, and choose
        "Copy Image Address".
     3. Paste it below between the quotes for the matching photo.
        (You can delete the temporary page afterward — the address keeps
        working.)""",
            """   How to get a photo's address on WordPress:
     1. Media -> Add New -> upload the photo.
     2. Click the uploaded photo in the Media Library and copy its
        "File URL" (also called "Copy URL") from the panel on the right.
     3. Paste it below between the quotes for the matching photo.""",
        ),
        (
            """        <!-- Photo: upload IMG_1704.JPG to Squarespace file storage (Link -> File -> Upload,
             keep the filename) so this URL resolves. If the photo doesn't appear, the
             filename differs - paste the file's exact URL instead. -->
        <figure class="cl-photo" data-tiltcard data-label="[ Photo: IMG_1704.JPG — upload to Squarespace file storage ]">""",
            """        <!-- Photo: upload IMG_1704.JPG to the WordPress Media Library and paste its
             File URL into CL_PHOTOS.story above — the baked-in address below still
             works for now, but points at Squarespace and should be swapped before
             Squarespace is turned off. -->
        <figure class="cl-photo" data-tiltcard data-label="[ Photo: IMG_1704.JPG — upload to WordPress Media Library ]">""",
        ),
        (
            """         EDIT ME: each card below has a photo slot. Upload a project photo to Squarespace
         and swap the placeholder div for:
         <img src="YOUR-IMAGE-URL" alt="Describe the project, e.g. Custom tile walk-in shower remodel in Canton GA"> -->
    <div class="cl-work-banner cl-reveal" data-delay="1">
      <!-- Photos load from Squarespace file storage (/s/<filename>). Upload each file via
           Link -> File -> Upload WITHOUT renaming. If one doesn't appear, its name or
           extension differs - swap in the file's exact URL. Cards with a wrong URL fall""",
            """         EDIT ME: each card below has a photo slot. Upload a project photo to the
         WordPress Media Library and swap the placeholder div for:
         <img src="YOUR-IMAGE-URL" alt="Describe the project, e.g. Custom tile walk-in shower remodel in Canton GA"> -->
    <div class="cl-work-banner cl-reveal" data-delay="1">
      <!-- Photos load from /wp-content/uploads/<filename>. Upload each file via
           Media -> Add New WITHOUT renaming (and with month/year folders turned
           off in Settings -> Media). If one doesn't appear, its name or
           extension differs - swap in the file's exact URL. Cards with a wrong URL fall""",
        ),
        (
            """        <!-- Main portrait: IMG_1661-EDIT (1) - if it doesn't appear, check the exact
             filename/extension in Squarespace and swap in the file's URL. -->
        <figure class="cl-photo" data-tiltcard data-label="[ Photo: IMG_1661-EDIT (1) — upload to Squarespace file storage ]">""",
            """        <!-- Main portrait: IMG_1661-EDIT (1) - if it doesn't appear, check the exact
             filename/extension in your WordPress Media Library and swap in the
             file's URL. The baked-in address below points at Squarespace and
             should be swapped before Squarespace is turned off. -->
        <figure class="cl-photo" data-tiltcard data-label="[ Photo: IMG_1661-EDIT (1) — upload to WordPress Media Library ]">""",
        ),
    ],
}

HEADER_COMMENTS = {
    "home-part1-header-injection.html": (
        """<!-- Centerline HOME page - PART 1 of 2
     Paste into: Page Settings -> Advanced -> Page Header Code Injection
     for the HOME page.
     Set the page title in Page Settings -> SEO to:
      Centerline Construction | Remodeling Contractor in Holly Springs & Canton, GA -->""",
        """<!-- Centerline HOME page - WordPress header code
     Paste into a WPCode "Insert Headers and Footers" snippet, type HTML,
     insert location Head, scope "Specific Pages" -> Home only.
     Set the page title in your SEO plugin (Yoast / Rank Math / All in One
     SEO) to:
      Centerline Construction | Remodeling Contractor in Holly Springs & Canton, GA
     See WORDPRESS-DEPLOY.md for the full page-by-page walkthrough. -->""",
    ),
    "services-part1-header-injection.html": (
        """<!-- Centerline Services page - PART 1 of 2
     Paste into: Page Settings -> Advanced -> Page Header Code Injection
     for the SERVICES page (Squarespace header injection is set per-page,
     so this is separate from the About page's Part 1).
     Set the page title in Page Settings -> SEO to:
      Our Services | Bathrooms, Basements, Cabanas & More — Centerline Construction -->""",
        """<!-- Centerline Services page - WordPress header code
     Paste into a WPCode snippet, type HTML, insert location Head, scope
     "Specific Pages" -> Services only (WPCode scopes per page, same idea
     as Squarespace's per-page header injection).
     Set the page title in your SEO plugin to:
      Our Services | Bathrooms, Basements, Cabanas & More — Centerline Construction
     See WORDPRESS-DEPLOY.md for the full page-by-page walkthrough. -->""",
    ),
    "part1-header-injection.html": (
        """<!-- Centerline About page - PART 1 of 2
     Paste into: Page Settings -> Advanced -> Page Header Code Injection
     (Set the page title in Page Settings -> SEO to:
      About Centerline Construction | Alfred Tudela | Holly Springs & Canton, GA Remodeling Contractor) -->""",
        """<!-- Centerline About page - WordPress header code
     Paste into a WPCode snippet, type HTML, insert location Head, scope
     "Specific Pages" -> About only.
     Set the page title in your SEO plugin to:
      About Centerline Construction | Alfred Tudela | Holly Springs & Canton, GA Remodeling Contractor
     See WORDPRESS-DEPLOY.md for the full page-by-page walkthrough. -->""",
    ),
    "schedule-part1-header-injection.html": (
        """<!-- Centerline SCHEDULE page - PART 1 of 2
     Paste into: Page Settings -> Advanced -> Page Header Code Injection
     for the SCHEDULE page.
     Set the page title in Page Settings -> SEO to:
      Schedule a Free Estimate | Centerline Construction - Holly Springs & Canton, GA -->""",
        """<!-- Centerline SCHEDULE page - WordPress header code
     Paste into a WPCode snippet, type HTML, insert location Head, scope
     "Specific Pages" -> Schedule only. The slug MUST stay /schedule — every
     "Schedule an Estimate" button on the other pages points there.
     Set the page title in your SEO plugin to:
      Schedule a Free Estimate | Centerline Construction - Holly Springs & Canton, GA
     See WORDPRESS-DEPLOY.md for the full page-by-page walkthrough, including
     the free WPForms plugin that makes this page email+store requests
     automatically instead of just opening the visitor's email app. -->""",
    ),
}

BLOCK_COMMENTS = {
    "home-part2-code-block.html": (
        """<!-- Centerline HOME page - PART 2 of 2
     Paste into a single Code Block (type: HTML) on the Home page.
     Three easy-edit lists sit at the very top:
       YOUR REVIEW COUNTS    - change a platform number, every mention updates
       OPTIONAL VIDEOS       - one clip per 'What we build' card (photo is the fallback)
       YOUR HOME PAGE PHOTOS - logo + photo addresses -->""",
        """<!-- Centerline HOME page - WordPress Custom HTML block
     Paste into a "Custom HTML" block on the Home page (Gutenberg: the "/"
     menu -> Custom HTML).
     Three easy-edit lists sit at the very top:
       YOUR REVIEW COUNTS    - change a platform number, every mention updates
       OPTIONAL VIDEOS       - one clip per 'What we build' card (photo is the fallback)
       YOUR HOME PAGE PHOTOS - logo + photo addresses
     Video/poster addresses already point at /wp-content/uploads/<filename> —
     upload each file in assets/ with Settings -> Media -> "organize uploads
     into month- and year-based folders" turned OFF first, so the filename
     alone is the address. Photo addresses still say images.squarespace-cdn.com
     — re-upload those to WordPress and swap the URLs; see WORDPRESS-DEPLOY.md. -->""",
    ),
    "services-part2-code-block.html": (
        """<!-- Centerline Services page - PART 2 of 2
     Paste into a single Code Block (type: HTML) on the Services page.
     Fully responsive; the YOUR SERVICE PHOTOS list near the top is where
     you add photos, including optional before/after pairs. -->""",
        """<!-- Centerline Services page - WordPress Custom HTML block
     Paste into a "Custom HTML" block on the Services page.
     Fully responsive; the YOUR SERVICE PHOTOS list near the top is where
     you add photos, including optional before/after pairs. Photo addresses
     still say images.squarespace-cdn.com — re-upload those to WordPress and
     swap the URLs; see WORDPRESS-DEPLOY.md. The hero video address already
     points at /wp-content/uploads/<filename>. -->""",
    ),
    "part2-code-block.html": (
        """<!-- Centerline About page - PART 2 of 2
     Paste into a single Code Block (type: HTML) on the About page.
     All photos are pre-wired; the YOUR PHOTOS list is only for future swaps. -->""",
        """<!-- Centerline About page - WordPress Custom HTML block
     Paste into a "Custom HTML" block on the About page.
     All photos are pre-wired; the YOUR PHOTOS list is only for future swaps —
     those addresses still say images.squarespace-cdn.com, re-upload to
     WordPress and swap the URLs; see WORDPRESS-DEPLOY.md. Hero video
     addresses already point at /wp-content/uploads/<filename>. -->""",
    ),
    "schedule-part2-code-block.html": (
        """<!-- Centerline SCHEDULE page - PART 2 of 2
     Paste into a single Code Block (type: HTML) on the Schedule page.
     The short list at the very top is the only thing you would ever edit:
     the email address estimate requests are sent to, and your phone number. -->""",
        """<!-- Centerline SCHEDULE page - WordPress Custom HTML block
     Paste into a "Custom HTML" block on the Schedule page.
     The short list at the very top is the only thing you would ever edit:
     the email address estimate requests are sent to, and your phone number.
     Add the free WPForms plugin and a form on this page (see
     WORDPRESS-DEPLOY.md) to have requests stored and emailed automatically —
     without it, this still works via the visitor's own email app. -->""",
    ),
}

# ---------------------------------------------------------------------------
# Schedule page: retarget the Squarespace Form Block bridge to WPForms
# ---------------------------------------------------------------------------
SCHEDULE_BLOCK_SUBS = [
    (
        """                <!-- If a Squarespace Form Block exists on this page, the script
                     lifts it in here and fills it in from the answers above, so
                     the visitor just presses Submit and it lands in your inbox.
                     With no form block on the page this stays empty and the
                     send button falls back to opening their email app. -->""",
        """                <!-- If a WPForms form exists on this page, the script lifts it
                     in here and fills it in from the answers above, so the
                     visitor just presses Submit and it lands in your inbox.
                     With no form on the page this stays empty and the send
                     button falls back to opening their email app. -->""",
    ),
    (
        "Load detection in JS on purpose — Squarespace's code-block sanitiser can\n"
        "     strip inline onload/onerror attributes.",
        "Load detection in JS on purpose, same as every other page in this\n"
        "     project — keeps this file identical in spirit to the Squarespace\n"
        "     version it was ported from.",
    ),
    (
        "with a real form on the last face, Squarespace validates its own */",
        "with a real form on the last face, WPForms validates its own */",
    ),
    (
        "Squarespace validates and sends */",
        "WPForms validates and sends */",
    ),
    (
        """  /* =====================================================================
     SQUARESPACE FORM BRIDGE
     If a Form Block exists anywhere on this page, lift it onto the last face
     and fill it in from the answers. The visitor then presses Squarespace's
     own Submit button, so the submission is stored in Form Submissions and
     emailed to whichever address the block is set to — no third-party service,
     nothing faked. If there is no form block, everything falls back to the
     pre-written email exactly as before.
     ===================================================================== */
  var formSlot = root.querySelector("[data-form-slot]");
  var noFormNote = root.querySelector("[data-no-form]");
  var sqForm = null;

  function findSquarespaceForm() {
    var block = document.querySelector(
      ".sqs-block-form, .form-block, [data-block-type='9']");
    if (!block || root.contains(block)) return null;
    return block;
  }""",
        """  /* =====================================================================
     WPFORMS BRIDGE
     If a WPForms form exists anywhere on this page, lift it onto the last
     face and fill it in from the answers. The visitor then presses WPForms'
     own Submit button, so the submission is stored in WPForms' entries and
     emailed to whichever address the form's notification is set to — no
     third-party service, nothing faked. If there is no form, everything
     falls back to the pre-written email exactly as before.
     ===================================================================== */
  var formSlot = root.querySelector("[data-form-slot]");
  var noFormNote = root.querySelector("[data-no-form]");
  var sqForm = null;

  function findSquarespaceForm() {
    var block = document.querySelector(".wpforms-container");
    if (!block || root.contains(block)) return null;
    return block;
  }""",
    ),
    (
        'var items = sqForm.querySelectorAll(".form-item, .field, fieldset");',
        'var items = sqForm.querySelectorAll(".form-item, .field, fieldset, .wpforms-field");',
    ),
    (
        'sqForm.querySelectorAll(".form-item, .field, fieldset").forEach(function (item) {',
        'sqForm.querySelectorAll(".form-item, .field, fieldset, .wpforms-field").forEach(function (item) {',
    ),
    (
        """    /* our big gold button becomes the Submit — Squarespace's own is hidden and
       clicked on their behalf, so the real submission still goes through it */
    sendBtn.textContent = "Submit My Request";
    var realSubmit = sqForm.querySelector("input[type=submit], button[type=submit], .sqs-system-button");""",
        """    /* our big gold button becomes the Submit — WPForms' own is hidden and
       clicked on their behalf, so the real submission still goes through it */
    sendBtn.textContent = "Submit My Request";
    var realSubmit = sqForm.querySelector("input[type=submit], button[type=submit], .wpforms-submit");""",
    ),
    (
        'var submit = sqForm.querySelector("input[type=submit], button[type=submit], .sqs-system-button");',
        'var submit = sqForm.querySelector("input[type=submit], button[type=submit], .wpforms-submit");',
    ),
    # Identifier renames last, so the longer strings above (which contain these
    # substrings) are matched against their original spelling first.
    ("sqForm", "wpForm"),
    ("findSquarespaceForm", "findWPForm"),
    ("fillSquarespaceForm", "fillWPForm"),
    ("mountSquarespaceForm", "mountWPForm"),
]

SCHEDULE_HEADER_SUBS = [
    (
        """  /* ---------- Squarespace's own Form Block, lifted onto the last face ----------
     We only restyle it and fill it in — the visitor presses Squarespace's real
     Submit button, so the submission goes through Squarespace exactly as if the
     form were sitting on the page by itself. */
  #cl-sched .cl-formslot:empty { display: none; }
  #cl-sched .cl-formslot .sqs-block,
  #cl-sched .cl-formslot .sqs-block-content { padding: 0 !important; margin: 0 !important; }
  #cl-sched .cl-formslot .form-item { margin: 0 0 9px !important; padding: 0 !important; }
  #cl-sched .cl-formslot :is(label, .title, .description) {
    font-size: 10.5px !important; font-weight: 800 !important; letter-spacing: .13em !important;
    text-transform: uppercase !important; color: rgba(18,16,12,.55) !important; margin-bottom: 4px !important;
  }
  #cl-sched .cl-formslot :is(input[type="text"], input[type="tel"], input[type="email"], input[type="number"], textarea, select) {
    font-family: inherit !important; font-size: 14.5px !important; color: var(--ink) !important;
    background: #fff !important; border: 2px solid rgba(18,16,12,.1) !important; border-radius: 10px !important;
    padding: 10px 12px !important; width: 100% !important; box-shadow: none !important;
  }
  #cl-sched .cl-formslot :is(input, textarea):focus {
    outline: none !important; border-color: var(--gold) !important; box-shadow: 0 0 0 4px rgba(217,164,65,.2) !important;
  }
  #cl-sched .cl-formslot textarea { min-height: 70px !important; resize: none !important; }
  /* Squarespace's own Submit is kept in the page — it is what actually sends —
     but tucked out of sight, because it sat below the fold inside the face's
     scroll area where nobody found it. The big gold button under the drum
     becomes "Submit" instead and clicks this one for them. */
  #cl-sched .cl-formslot .form-button-wrapper {
    position: absolute !important; width: 1px !important; height: 1px !important;
    padding: 0 !important; margin: -1px !important; overflow: hidden !important;
    clip-path: inset(50%) !important; border: 0 !important;
  }
  #cl-sched .cl-formslot .field-list > .field:not(:last-child) { margin-bottom: 9px; }""",
        """  /* ---------- WPForms' own form, lifted onto the last face ----------
     We only restyle it and fill it in — the visitor presses WPForms' real
     Submit button, so the submission goes through WPForms exactly as if the
     form were sitting on the page by itself. */
  #cl-sched .cl-formslot:empty { display: none; }
  #cl-sched .cl-formslot .wpforms-container { padding: 0 !important; margin: 0 !important; }
  #cl-sched .cl-formslot .wpforms-field { margin: 0 0 9px !important; padding: 0 !important; }
  #cl-sched .cl-formslot :is(label, .wpforms-field-label, .wpforms-field-description) {
    font-size: 10.5px !important; font-weight: 800 !important; letter-spacing: .13em !important;
    text-transform: uppercase !important; color: rgba(18,16,12,.55) !important; margin-bottom: 4px !important;
  }
  #cl-sched .cl-formslot :is(input[type="text"], input[type="tel"], input[type="email"], input[type="number"], textarea, select) {
    font-family: inherit !important; font-size: 14.5px !important; color: var(--ink) !important;
    background: #fff !important; border: 2px solid rgba(18,16,12,.1) !important; border-radius: 10px !important;
    padding: 10px 12px !important; width: 100% !important; box-shadow: none !important;
  }
  #cl-sched .cl-formslot :is(input, textarea):focus {
    outline: none !important; border-color: var(--gold) !important; box-shadow: 0 0 0 4px rgba(217,164,65,.2) !important;
  }
  #cl-sched .cl-formslot textarea { min-height: 70px !important; resize: none !important; }
  /* WPForms' own Submit is kept in the page — it is what actually sends — but
     tucked out of sight, because it sat below the fold inside the face's
     scroll area where nobody found it. The big gold button under the drum
     becomes "Submit" instead and clicks this one for them. */
  #cl-sched .cl-formslot .wpforms-submit-container {
    position: absolute !important; width: 1px !important; height: 1px !important;
    padding: 0 !important; margin: -1px !important; overflow: hidden !important;
    clip-path: inset(50%) !important; border: 0 !important;
  }""",
    ),
]


# ---------------------------------------------------------------------------
# "Host section" padding fixes — Squarespace wraps every Code Block in its own
# .page-section/.sqs-block, which added an unwanted empty gap below the page
# and needed collapsing. WordPress's block editor wraps a Custom HTML block in
# .wp-block-html instead (same class on every block theme, unlike the rest of
# a theme's markup) and most themes don't add the Squarespace-style gap in the
# first place, so these become a smaller, WordPress-flavoured safety net
# rather than a required fix.
# ---------------------------------------------------------------------------
HOST_SECTION_SUBS = {
    "home-part1-header-injection.html": (
        """  /* ---------- Squarespace host-page fixes ---------- */
  .page-section:has(#cl-home) { padding: 0 !important; min-height: 0 !important; }
  .page-section:has(#cl-home) > .content-wrapper { padding: 0 !important; max-width: none !important; width: 100% !important; }
  .sqs-block:has(#cl-home) { padding: 0 !important; }
  .sqs-block:has(#cl-home) .sqs-block-content { margin: 0 !important; }""",
        """  /* ---------- WordPress host-block safety net ----------
     Most block themes add no extra padding around a Custom HTML block, so
     this usually does nothing. If your theme leaves a gap above/below the
     page, this collapses the block's own wrapper (every WP block theme uses
     .wp-block-html for a Custom HTML block, unlike Squarespace's per-theme
     .sqs-block). See WORDPRESS-DEPLOY.md if a gap remains after this. */
  .wp-block-html:has(#cl-home) { padding: 0 !important; margin: 0 !important; }""",
    ),
    "services-part1-header-injection.html": (
        """  /* ---------- Squarespace host-page fixes ---------- */
  .page-section:has(#cl-services) { padding: 0 !important; min-height: 0 !important; }
  .page-section:has(#cl-services) > .content-wrapper { padding: 0 !important; max-width: none !important; width: 100% !important; }
  .sqs-block:has(#cl-services) { padding: 0 !important; }""",
        """  /* ---------- WordPress host-block safety net ----------
     Most block themes add no extra padding around a Custom HTML block, so
     this usually does nothing. If your theme leaves a gap above/below the
     page, this collapses the block's own wrapper. See WORDPRESS-DEPLOY.md
     if a gap remains after this. */
  .wp-block-html:has(#cl-services) { padding: 0 !important; margin: 0 !important; }""",
    ),
    "part1-header-injection.html": (
        """  /* ---------- Squarespace host-page fixes ----------
     Collapse the section that hosts this code block: no min-height, no padding,
     full-bleed width. This removes the tall empty (black) area between our final
     call-to-action and the Squarespace footer, and lets the design run edge to edge. */
  .page-section:has(#cl-about) { padding: 0 !important; min-height: 0 !important; }
  .page-section:has(#cl-about) > .content-wrapper { padding: 0 !important; max-width: none !important; width: 100% !important; }
  .sqs-block:has(#cl-about), .sqs-block-code:has(#cl-about) { padding: 0 !important; }
  .sqs-block:has(#cl-about) .sqs-block-content { margin: 0 !important; }""",
        """  /* ---------- WordPress host-block safety net ----------
     Most block themes add no extra padding around a Custom HTML block, so
     this usually does nothing. If your theme leaves a gap above/below the
     page, this collapses the block's own wrapper. See WORDPRESS-DEPLOY.md
     if a gap remains after this. */
  .wp-block-html:has(#cl-about) { padding: 0 !important; margin: 0 !important; }""",
    ),
    "schedule-part1-header-injection.html": (
        """  /* ---------- Collapse the host Squarespace section ---------- */
  .page-section:has(#cl-sched) { padding: 0 !important; min-height: 0 !important; }
  .page-section:has(#cl-sched) > .content-wrapper { padding: 0 !important; max-width: none !important; width: 100% !important; }
  .sqs-block:has(#cl-sched) { padding: 0 !important; }
  .sqs-block:has(#cl-sched) .sqs-block-content { margin: 0 !important; }""",
        """  /* ---------- WordPress host-block safety net ----------
     Most block themes add no extra padding around a Custom HTML block, so
     this usually does nothing. If your theme leaves a gap above/below the
     page, this collapses the block's own wrapper. See WORDPRESS-DEPLOY.md
     if a gap remains after this. */
  .wp-block-html:has(#cl-sched) { padding: 0 !important; margin: 0 !important; }""",
    ),
}


def apply_subs(text, subs):
    for old, new in subs:
        if old not in text:
            raise SystemExit(f"Expected substring not found (file drifted?):\n{old[:120]}...")
        text = text.replace(old, new)
    return text


def write(src_name, dest_name, comment_map):
    text = (SQ / src_name).read_text(encoding="utf-8")
    text = sub_media(text)
    if src_name in comment_map:
        old, new = comment_map[src_name]
        if old not in text:
            raise SystemExit(f"Leading comment not found in {src_name} (file drifted?)")
        text = text.replace(old, new, 1)
    if src_name == "schedule-part2-code-block.html":
        text = apply_subs(text, SCHEDULE_BLOCK_SUBS)
    if src_name == "schedule-part1-header-injection.html":
        text = apply_subs(text, SCHEDULE_HEADER_SUBS)
    if src_name in HOST_SECTION_SUBS:
        old, new = HOST_SECTION_SUBS[src_name]
        if old not in text:
            raise SystemExit(f"Host-section block not found in {src_name} (file drifted?)")
        text = text.replace(old, new, 1)
    if src_name in MISC_HEADER_SUBS:
        text = apply_subs(text, MISC_HEADER_SUBS[src_name])
    remaining = [l for l in text.split("\n") if "Squarespace" in l or ".sqs-" in l]
    allowed = (
        "compared", "ported from", "unlike Squarespace", "per-page header injection",
        "used to paint", "points at Squarespace", "Squarespace is turned off",
    )
    bad = [l for l in remaining if not any(a in l for a in allowed)]
    if bad:
        print(f"  !! unreviewed Squarespace mention(s) in {dest_name}:")
        for l in bad:
            print(f"       {l.strip()[:100]}")
    (WP / dest_name).write_text(text, encoding="utf-8")
    print(f"wrote wordpress/{dest_name}  ({len(text)//1024} KB)")


write("home-part1-header-injection.html", "home-header.html", HEADER_COMMENTS)
write("home-part2-code-block.html", "home-block.html", BLOCK_COMMENTS)
write("services-part1-header-injection.html", "services-header.html", HEADER_COMMENTS)
write("services-part2-code-block.html", "services-block.html", BLOCK_COMMENTS)
write("part1-header-injection.html", "about-header.html", HEADER_COMMENTS)
write("part2-code-block.html", "about-block.html", BLOCK_COMMENTS)
write("part3-phone-addon.html", "about-phone-addon.html", {})
write("schedule-part1-header-injection.html", "schedule-header.html", HEADER_COMMENTS)
write("schedule-part2-code-block.html", "schedule-block.html", BLOCK_COMMENTS)

print("\nDone. Remember: images.squarespace-cdn.com photo URLs inside these files")
print("still need re-uploading + swapping by hand (or send Claude the new URLs).")
