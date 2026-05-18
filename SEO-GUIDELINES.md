# SEO Guidelines — Deep Groove HiFi

Reference document for title tags and meta descriptions across deepgroovehifi.com.
Update this file whenever a page is added, renamed, or its meta copy changes.

---

## Character Limits

| Field | Target | Hard Limit | Notes |
|---|---|---|---|
| `<title>` tag | 50–60 chars | 60 chars | Hugo appends ` \| Deep Groove HiFi` automatically — write the page title portion only |
| `description:` (articles) | 145–155 chars | 155 chars | Front matter field in markdown |
| `<meta name="description">` (calculators) | 145–155 chars | 155 chars | In `static/calculators/*/index.html` |

> **Why 155 and not 160?** Google's truncation point varies slightly by device and result type. A 5-character buffer prevents clipping on narrower renders without sacrificing meaningful copy.

---

## Quick Rules for New Pages

1. **Write the description first, count second.** Paste into any character counter before committing.
2. **One specific promise per description.** State what the reader will get, not what the page is about.
3. **End with value, not brand.** "Free tool from Deep Groove HiFi" is fine as a closer but must fit within the 155-char budget.
4. **No keyword stuffing.** Descriptions don't affect ranking directly — write for the click, not the crawler.
5. **Calculator files are standalone HTML.** They do not inherit meta from Hugo front matter. Update `<meta name="description">` directly in `static/calculators/*/index.html`.

---

## Current Page Inventory

### Articles — `content/articles/*.md`

| File | Title | Meta Description | Chars |
|---|---|---|---|
| `speaker-placement-guide.md` | Speaker Placement: The Free Hi-Fi Upgrade | Speaker placement matters more than almost any upgrade you could buy. Here's how to find the positions that unlock what your speakers can actually do. | 150 |
| `amplifier-classes-explained.md` | Amplifier Classes: A, AB, and D Explained | Class A runs hot and expensive. Class D runs cool and efficient. Class AB sits between. Here's what each means for sound quality and your electricity bill. | 154 |
| `open-back-vs-closed-back-headphones.md` | Open-Back vs. Closed-Back Headphones | Open-back headphones sound more spacious, but closed-back designs have real advantages. Here's how to choose the right type for how and where you listen. | 153 |
| `streaming-vs-local-files.md` | Streaming vs. Local Files: Does It Matter? | Tidal and Qobuz offer lossless hi-res streaming. Does it sound as good as your local FLAC library? The honest answer is more interesting than you'd expect. | 155 |
| `bookshelf-vs-floorstanding.md` | Bookshelf vs. Floorstanding: How to Choose | Bigger isn't always better. The case for bookshelf speakers is stronger than many audiophiles admit. Here's how to match speaker size to your room. | 147 |
| `the-preamplifier.md` | Preamplifiers Explained: Do You Need One? | A preamp handles source selection and volume control. Not every system needs one, and the wrong preamp can hurt more than help. Here's how to decide. | 149 |
| `phono-preamp-basics.md` | Phono Preamp Basics: MM vs. MC Cartridges | Your turntable cartridge signal is too small and too colored for a line-level input. A phono preamp fixes both — here's how it works and what to look for. | 154 |
| `room-acoustics-guide.md` | Room Acoustics: Practical HiFi Improvements | Your room shapes sound more than almost any component change. Here's how to fix acoustic problems without making your room an isolation chamber. | 143 |

### Calculators — `static/calculators/*/index.html`

| File | Title | Meta Description | Chars |
|---|---|---|---|
| `speaker-impedance/index.html` | Speaker Impedance Calculator | Check whether your speakers are compatible with your amplifier. Calculate impedance for single or multi-speaker wiring. Free tool from Deep Groove HiFi. | 152 |
| `amplifier-power/index.html` | Amplifier Power & Speaker SPL Calculator | Find how many watts your speakers need — or what SPL your amplifier can deliver at your listening position. Free calculator from Deep Groove HiFi. | 146 |
| `phono-stage-gain/index.html` | Phono Stage Gain Calculator | Find how much gain your phono stage needs for your MM or MC cartridge. Includes step-up transformer recommendations. Free calculator from Deep Groove HiFi. | 155 |
| `room-acoustics/index.html` | Room Acoustics Calculator | Find your room's resonant frequencies, mode coincidences, and Schroeder frequency. Know where to focus your acoustic treatment. Free from Deep Groove HiFi. | 155 |
| `listening-room-size/index.html` | Listening Room Size Calculator | Find ideal speaker placement and listening position for your room. Get exact distances for your speakers, chair, and first reflection points. Free tool. | 152 |

---

## Title Tag Reference

Hugo constructs the full `<title>` tag as:

```
[page title] | Deep Groove HiFi
```

The ` | Deep Groove HiFi` suffix adds 18 characters. Keep the page title portion at **42 characters or fewer** to stay under the 60-char total.

| Page | Title Portion | Title Portion Chars | Full Tag Chars |
|---|---|---|---|
| Speaker Placement Guide | Speaker Placement: The Free Hi-Fi Upgrade | 42 | 60 |
| Amplifier Classes | Amplifier Classes: A, AB, and D Explained | 42 | 60 |
| Open-Back vs. Closed-Back | Open-Back vs. Closed-Back Headphones | 37 | 55 |
| Streaming vs. Local Files | Streaming vs. Local Files: Does It Matter? | 42 | 60 ✅ |
| Bookshelf vs. Floorstanding | Bookshelf vs. Floorstanding: How to Choose | 42 | 60 ✅ |
| The Preamplifier | Preamplifiers Explained: Do You Need One? | 41 | 59 |
| Phono Preamp Basics | Phono Preamp Basics: MM vs. MC Cartridges | 42 | 60 |
| Room Acoustics Guide | Room Acoustics: Practical HiFi Improvements | 44 | 62 |
| Speaker Impedance Calculator | Speaker Impedance Calculator | 29 | 47 |
| Amplifier Power Calculator | Amplifier Power & Speaker SPL Calculator | 41 | 59 |
| Phono Stage Gain Calculator | Phono Stage Gain Calculator | 28 | 46 |
| Room Acoustics Calculator | Room Acoustics Calculator | 26 | 44 |
| Listening Room Size Calculator | Listening Room Size Calculator | 31 | 49 |

> All current pages are within the 60-character title limit.

---

*Last updated: May 2026*
