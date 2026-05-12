# Deep Groove HiFi — Site Setup Guide

## Overview
A Hugo static site pre-configured for:
- Google AdSense monetization
- Amazon Associates (tag: `audiochainhif-20`)
- Netlify deployment from GitHub
- 20 original audiophile articles at launch

---

## Quick Start (First Deploy)

### 1. Install Hugo
```bash
# macOS
brew install hugo

# Windows (via Chocolatey)
choco install hugo-extended

# Verify
hugo version  # needs 0.120+
```

### 2. Clone / Initialize GitHub Repo
```bash
cd audiochainhifi
git init
git add .
git commit -m "Initial site launch"
git remote add origin https://github.com/YOUR_USERNAME/deepgroovehifi.git
git push -u origin main
```

### 3. Connect to Netlify
1. Log in at netlify.com
2. "Add new site" → "Import an existing project" → GitHub
3. Select your repo
4. Build command: `hugo --minify`
5. Publish directory: `public`
6. Click Deploy

Netlify auto-deploys every time you push to GitHub.

---

## Activating Google AdSense

1. Apply at **adsense.google.com** with your deepgroovehifi.com domain
2. Once approved, copy your Publisher ID (format: `ca-pub-XXXXXXXXXXXXXXXXXX`)
3. Open `hugo.toml` and update:
   ```toml
   adsenseID = "ca-pub-XXXXXXXXXXXXXXXXXX"
   ```
4. Open `static/ads.txt` and update:
   ```
   google.com, ca-pub-XXXXXXXXXXXXXXXXXX, DIRECT, f08c47fec0942fa0
   ```
5. In `themes/audiophile/layouts/_default/baseof.html`, uncomment the AdSense script block
6. Push to GitHub — Netlify auto-deploys

---

## Adding a New Article

Create a file in `content/articles/` using this template:

```markdown
---
title: "Your Article Title Here"
date: 2026-06-01
description: "A 150-character description for SEO."
categories: ["Guides"]   # Options: Guides, Gear, Reviews, Features
tags: ["dac", "amplifiers", "vinyl"]
image: "/images/articles/dac.svg"  # Pick existing or add new SVG
---

Your article content here in Markdown...

{{</* ad id="in-article-1" */>}}

More content...

{{</* amazon name="Product Name" asin="B0XXXXXXXX" price="~$299" desc="Product description." */>}}
```

Then `git add . && git commit -m "Add article" && git push`.

---

## Article Image Options (SVGs included)
| File | Use for |
|---|---|
| `/images/articles/dac.svg` | DACs, digital audio |
| `/images/articles/amp.svg` | Amplifiers, tubes |
| `/images/articles/vinyl.svg` | Vinyl culture, records |
| `/images/articles/turntable.svg` | Turntables, setup guides |
| `/images/articles/phono.svg` | Phono stages, cartridges |
| `/images/articles/cdplayer.svg` | CD players, transports |
| `/images/articles/streaming.svg` | Streamers, digital |
| `/images/articles/speakers.svg` | Speakers |
| `/images/articles/cables.svg` | Cables, connections |
| `/images/articles/room.svg` | Acoustics, room setup |

---

## Re-Theming the Site

All color and font variables are in ONE place:
`themes/audiophile/static/css/main.css` — top of file under `/* THEME VARIABLES */`

To change the accent color from gold to blue:
```css
--accent:       #4a8db5;
--accent-hover: #6aafd5;
```

To change fonts, swap the Google Fonts link in `baseof.html` and update:
```css
--font-head: 'Your Heading Font', serif;
--font-body: 'Your Body Font', sans-serif;
```

---

## Amazon Associates Links

Use the `{{</* amazon */>}}` shortcode in any article:

```markdown
{{</* amazon
    name="Product Name"
    asin="B0XXXXXXXXX"
    price="~$299"
    desc="Short product description."
*/>}}
```

Your affiliate tag (`audiochainhif-20`) is automatically appended to every link.

---

## AdSense Checklist for Approval
- [x] Privacy Policy at /privacy-policy/
- [x] About page at /about/
- [x] Contact page at /contact/ with working Netlify Form
- [x] ads.txt at root
- [x] Cookie consent banner
- [x] 20 original articles (800–1,100 words each)
- [x] Mobile responsive design
- [x] robots.txt with sitemap reference
- [ ] Update ads.txt with your Publisher ID (after approval)
- [ ] Uncomment AdSense script in baseof.html (after approval)
- [ ] Update adsenseID in hugo.toml (after approval)

---

## Local Development

```bash
cd audiochainhifi
hugo server -D
# Open http://localhost:1313
```
