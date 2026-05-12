---
title: "High-Resolution Audio: FLAC, DSD, and PCM Explained"
date: 2026-01-30
description: "What is hi-res audio, does it actually sound better than CD, and which formats are worth caring about? The technical facts without the marketing hype."
categories: ["Guides"]
tags: ["digital audio", "high resolution", "flac", "dsd", "streaming"]
image: "/images/articles/streaming.svg"
---

High-resolution audio is one of the most marketed and least clearly defined terms in consumer audio. Definitions vary by retailer and format, claims range from modestly plausible to demonstrably false, and the debate about audibility has been running for two decades without resolution. This guide explains what the formats actually are, what the research suggests about audibility, and what matters in practice.

{{< ad id="in-article-hires1" >}}

## The Foundation: How Digital Audio Works

Digital audio captures an analog waveform by measuring its amplitude at regular intervals. Two parameters define the quality of this capture:

**Sample rate** (measured in kHz) determines how many times per second the signal is sampled. CD uses 44.1 kHz — 44,100 samples per second. According to the Nyquist theorem, this is sufficient to perfectly reconstruct frequencies up to 22,050 Hz, well above the generally accepted upper limit of human hearing (around 20,000 Hz for young listeners).

**Bit depth** determines how precisely each sample is measured. CD uses 16 bits, allowing 65,536 discrete amplitude levels and a theoretical dynamic range of 96 dB. 24-bit audio uses over 16 million levels and theoretically achieves 144 dB of dynamic range.

## What "Hi-Res Audio" Actually Means

The Consumer Technology Association defines high-resolution audio as files exceeding the CD standard of 44.1kHz/16-bit — so 88.2kHz/24-bit and above. Common hi-res formats include:

- 88.2kHz/24-bit and 96kHz/24-bit (the practical sweet spots)
- 176.4kHz/24-bit and 192kHz/24-bit
- DSD64, DSD128, DSD256 (the Direct Stream Digital formats used in SACDs)

## PCM: The Standard Architecture

PCM (Pulse Code Modulation) is the basis of CD audio and nearly all high-resolution audio. It samples the waveform at regular intervals and stores each sample as a binary number. FLAC (Free Lossless Audio Codec) is the most common lossless container for PCM hi-res files — it compresses without any quality loss, unlike MP3 or AAC.

AIFF and WAV are uncompressed PCM containers that some prefer for compatibility, though lossless FLAC is bit-for-bit identical to the uncompressed original.

{{< ad id="in-article-hires2" >}}

## DSD: A Different Architecture

DSD (Direct Stream Digital) takes a fundamentally different approach. Instead of multi-bit samples at regular intervals, DSD uses single-bit samples at extremely high rates — 2.8 MHz (DSD64) or 5.6 MHz (DSD128). This is the format used on SACDs.

DSD proponents argue it has a more analog-like quality, avoiding the reconstruction filters required by PCM. Critics note that DSD has a high ultrasonic noise floor and that most modern recording, mixing, and mastering is done in PCM, making DSD releases of modern material simply converted from PCM masters.

Native DSD recordings — those recorded, mixed, and mastered entirely in DSD — are a different matter and are genuinely popular with audiophiles who prefer the format.

## Does Hi-Res Audio Actually Sound Better?

The honest answer is nuanced.

**The case that it can:** Some listeners reliably prefer high-resolution versions of specific recordings in informal and semi-controlled listening. When a hi-res file comes from a different (often earlier, less compressed) master than the CD release, it can sound dramatically better — but that's mastering, not resolution.

**The case that the format itself rarely matters:** Rigorous double-blind testing has consistently failed to demonstrate reliable audibility of sample rate above 44.1kHz among trained listeners. The audible difference, when present, almost always traces back to mastering differences rather than sample rate.

The 24-bit advantage is more defensible: 24-bit audio provides genuine benefits in the recording and mixing process (headroom, flexibility), and playback at 24-bit eliminates any dithering noise that 16-bit playback introduces. Whether this is audible in practice is debated.

## What Actually Matters

1. **Get lossless audio.** The difference between lossless (FLAC, ALAC, WAV) and a high-bitrate lossy file (320kbps MP3, AAC) can be audible on quality equipment. This is a real and meaningful distinction.

2. **Care about mastering.** The quality of the master recording — the choices made in mixing and mastering — has far more impact on what you hear than whether the file is 44.1kHz or 96kHz.

3. **Your DAC matters.** A quality DAC that properly implements the reconstruction filter and analog output stage will sound better with standard-resolution audio than a poor DAC playing hi-res files.

{{< amazon name="iFi Audio NEO iDSD 2 DAC" asin="B0BQZRJB6W" price="~$399" desc="Supports PCM up to 768kHz, DSD512, and MQA. A versatile, well-measured DAC/headphone amp that handles every format you're likely to encounter." >}}

If a streaming service offers 16-bit/44.1kHz lossless, that is genuinely excellent audio. Hi-res above that is worth exploring — particularly if you find masterings you prefer — but it isn't the dramatic leap some marketing suggests.
