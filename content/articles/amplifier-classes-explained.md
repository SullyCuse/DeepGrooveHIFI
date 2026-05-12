---
title: "Amplifier Classes Explained: Class A, AB, and D"
date: 2026-04-22
description: "Class A runs hot and expensive. Class D runs cool and efficient. Class AB sits in between. Here's what each means for sound quality, heat, and your electricity bill."
categories: ["Guides"]
tags: ["amplifiers", "class a", "class d", "beginners"]
image: "/images/articles/amp.svg"
---

When you start shopping for amplifiers, you'll quickly encounter the terms Class A, Class AB, and Class D. These aren't marketing grades — they describe the fundamental operating principle of the amplifier circuit, determining how the output transistors or tubes conduct current. Each approach involves genuine tradeoffs between efficiency, heat, cost, and sonic character.

Here's what each class actually means.

{{< ad id="in-article-amp1" >}}

## What Amplifier Class Refers To

Every amplifier takes a small input signal and produces a larger output signal. The "class" describes how the amplifying devices — transistors, MOSFETs, or vacuum tubes — conduct current during the audio waveform cycle.

A full audio waveform cycle has a positive half and a negative half. The amplifier class determines what fraction of that cycle each device is active and conducting.

## Class A: Always On, Always Hot

In a Class A amplifier, the output devices conduct for the *entire* 360 degrees of the audio waveform. Both the positive and negative halves of the cycle are handled by the same devices running continuously, regardless of whether there's any signal.

**The advantage:** Because the output devices never switch off and never cross zero, there are no crossover distortion artifacts. The amplifier also tends to produce predominantly lower-order harmonic distortions — primarily second and third harmonics — which many listeners find more natural and musical than the higher-order distortions sometimes produced by other classes.

**The disadvantages:** Class A is dramatically inefficient. At best, around 25–30% of the power drawn from the wall becomes audio output. The remainder becomes heat. A 20-watt Class A amplifier may draw 80 watts continuously from the wall, even at idle. This means Class A amplifiers run hot, require substantial heatsinking, and cost more to run. High-power Class A designs are expensive, large, and heavy.

Class A is common in high-end stereo amplification, often at modest power levels (10–30 watts) where the heat penalty is manageable. It's the preferred topology of many audiophiles who prioritize naturalness and harmonic texture over raw power.

## Class AB: The Practical Compromise

Class AB is by far the most common amplifier class in hi-fi equipment. It's a hybrid approach that runs in Class A at low power levels — where most music actually lives — and transitions toward Class B behavior at higher output levels.

In Class AB, output transistors are biased to conduct for slightly more than 180 degrees each. The positive and negative halves of the waveform are handled by separate transistors (or pairs of transistors). At low signal levels, both sides conduct simultaneously, giving Class A behavior. At higher levels, each side handles its respective half of the cycle with a small overlap region.

**The advantage:** Much higher efficiency than Class A — typically 50–70% — while still achieving low distortion across most of the power range where music is reproduced. A 100-watt Class AB amplifier runs warm but not dangerously hot, and doesn't require huge heatsinks.

**The disadvantages:** There is a crossover region as each device hands off to the other, which can produce a small amount of crossover distortion if not carefully managed through biasing. Good Class AB designs minimize this through careful bias adjustment and high loop feedback.

The vast majority of excellent stereo amplifiers — including many at high price points — are Class AB. It's not a compromise in the pejorative sense; it's simply the topology that offers the best balance of performance, cost, heat, and practicality for most applications.

{{< ad id="in-article-amp2" >}}

## Class D: Efficient and Misunderstood

Class D amplifiers — sometimes called digital amplifiers or switching amplifiers — operate on an entirely different principle. Rather than varying the current through output devices continuously, Class D amplifiers switch the output transistors rapidly between fully on and fully off states. The output is a pulse-width modulated (PWM) signal that, after passing through a low-pass filter, reconstructs the original audio waveform.

**The advantage:** Because the transistors are either fully on or fully off, they spend almost no time in the inefficient middle ground where power dissipates as heat. Class D amplifiers routinely achieve 90% or higher efficiency. This means a 200-watt Class D amplifier barely gets warm, runs from a compact power supply, and can be built into a chassis a fraction of the size of an equivalent Class AB or Class A design.

**The disadvantages:** Early Class D amplifiers had a deserved reputation for hardness and grain — the switching artifacts and output filter choices created audible coloration, particularly at high frequencies. This reputation has lingered even as the technology has dramatically improved.

Modern Class D designs from companies like Hypex (NCore and Eigentakt modules), Purifi Audio, and Pascal have largely closed the sonic gap. Benchmark-quality measurements and very low distortion are now achievable from Class D. Many audiophiles who spent years dismissing switching amplifiers have revised their positions after hearing the latest generation.

Class D is now common in powered speakers, subwoofer amplifiers, and increasingly in high-end stereo amplifiers. It's the dominant technology in any application where power and efficiency matter — home theater, professional audio, automotive.

## Other Classes Worth Knowing

**Class H** takes a Class AB output stage and dynamically varies the power supply voltage to track the audio signal. It's more efficient than straight Class AB without switching artifacts, and is common in professional amplification.

**Class G** is similar to Class H but uses multiple fixed supply voltages rather than a continuously variable one.

**Class T** was a proprietary marketing name used by Tripath for a specific Class D implementation. Tripath is now defunct, but many well-regarded budget Class D products used their chips.

## Which Class Should You Choose?

The class matters less than the quality of execution. A mediocre Class A amplifier will sound worse than an excellent Class AB design. A poorly implemented Class D will disappoint next to a well-built Class AB.

That said, if sonic character matters to you and you've heard specific descriptions of warmth, naturalness, or tube-like qualities that appeal to you, a Class A or Class A-biased design is worth seeking out. If efficiency, compact size, and maximum power within a budget are priorities, modern Class D is entirely respectable. And if you want reliability, broad compatibility, and proven performance across all music types, Class AB remains the most versatile choice.

The best amplifier for your system is the one that drives your specific speakers to your preferred listening levels without running out of headroom, while sounding the way you like and fitting your budget.

{{< amazon name="Schiit Ragnarok 2 Integrated Amplifier" asin="B083CLBSXZ" price="~$1,499" desc="A Class A/AB switchable integrated amp from Schiit Audio. Run it in pure Class A at 24W or Class AB at 60W — a rare chance to compare both topologies in one chassis." >}}
