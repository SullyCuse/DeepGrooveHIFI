#!/usr/bin/env python3
"""
Fix calculator pages nav/footer to match the Hugo theme.
Run from your repo root:  python3 fix_calculators.py
"""

import re, os

FILES = [
    'static/calculators/amplifier-power/index.html',
    'static/calculators/speaker-impedance/index.html',
    'static/calculators/phono-stage-gain/index.html',
    'static/calculators/room-acoustics/index.html',
    'static/calculators/listening-room-size/index.html',
]

# ── Replacement blocks ────────────────────────────────────────────────────────

NEW_NAV_CSS = """\
    /* ── NAV ── */
    .nav { position: sticky; top: 0; z-index: 100; background: var(--bg-nav); border-bottom: 1px solid var(--border); height: 68px; }
    .nav__inner { max-width: 1200px; margin: 0 auto; padding: 0 1.5rem; height: 100%; display: flex; align-items: center; justify-content: space-between; gap: 2rem; }
    .nav__logo { display: flex; align-items: center; gap: .75rem; text-decoration: none; flex-shrink: 0; }
    .nav__logo-text { font-family: var(--serif); font-size: 1.25rem; color: #ffffff; letter-spacing: .01em; white-space: nowrap; }
    .nav__logo-text span { color: var(--gold); }
    .nav__links { display: flex; align-items: center; gap: 1.75rem; list-style: none; }
    .nav__links a { font-size: 15px; font-weight: 500; letter-spacing: .05em; text-transform: uppercase; color: rgba(255,255,255,0.8); text-decoration: none; transition: color .15s; }
    .nav__links a:hover { color: var(--gold); }
    .nav__toggle { display: none; background: none; border: none; cursor: pointer; padding: .5rem; flex-direction: column; gap: 5px; }
    .nav__toggle span { display: block; width: 24px; height: 2px; background: #ffffff; transition: all .3s; }
    @media (max-width: 768px) {
      .nav__toggle { display: flex; }
      .nav__links { display: none; position: absolute; top: 68px; left: 0; right: 0; background: var(--bg-nav); flex-direction: column; padding: 1.5rem; border-bottom: 1px solid var(--border); gap: 1.25rem; align-items: flex-start; }
      .nav__links.is-open { display: flex; }
    }

    """

NEW_FOOTER_CSS = """\
    /* ── FOOTER ── */
    .footer { background: var(--bg-nav); border-top: 1px solid var(--border); padding: 3rem 0 2rem; margin-top: 4rem; }
    .footer__inner { max-width: 1200px; margin: 0 auto; padding: 0 1.5rem; }
    .footer__grid { display: grid; grid-template-columns: 2fr 1fr 1fr 1fr 1fr; gap: 3rem; margin-bottom: 3rem; }
    @media (max-width: 900px) { .footer__grid { grid-template-columns: 1fr 1fr; gap: 2rem; } }
    @media (max-width: 500px) { .footer__grid { grid-template-columns: 1fr; } }
    .footer__brand p { font-size: 15px; color: var(--text-muted); line-height: 1.7; margin-top: .75rem; max-width: 300px; }
    .footer__logo-text { font-family: var(--serif); font-size: 1.2rem; color: #ffffff; }
    .footer__logo-text span { color: var(--gold); }
    .footer__col h4 { font-size: 12px; font-weight: 700; letter-spacing: .12em; text-transform: uppercase; color: #ffffff; margin-bottom: 1rem; }
    .footer__col ul { list-style: none; }
    .footer__col li { margin-bottom: .6rem; }
    .footer__col a { font-size: 15px; color: var(--text-muted); transition: color .2s; }
    .footer__col a:hover { color: var(--gold); }
    .footer__bottom { padding-top: 2rem; border-top: 1px solid var(--border); display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; }
    .footer__copy { font-size: 13px; color: var(--text-muted); }
  </style>
"""

NEW_NAV_HTML = """\

  <!-- NETWORK BAR -->
  <div class="network-bar">
    <div class="network-bar__inner">
      <span class="network-bar__label">Also from our network:</span>
      <a href="https://audiochainhifi.com" target="_blank" rel="noopener">AudioChainHiFi.com</a>
      <span class="network-bar__dot">·</span>
      <a href="https://audioscopehifi.com" target="_blank" rel="noopener">AudioScopeHiFi.com</a>
    </div>
  </div>

  <!-- NAV -->
  <header class="nav">
    <div class="nav__inner">
      <a href="https://deepgroovehifi.com/" class="nav__logo" aria-label="Deep Groove HiFi home">
        <svg width="36" height="36" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
          <circle cx="18" cy="18" r="17" stroke="#c9a84c" stroke-width="2"/>
          <circle cx="18" cy="18" r="5" fill="#c9a84c"/>
          <path d="M6 18 Q9 11 12 18 Q15 25 18 18 Q21 11 24 18 Q27 25 30 18" stroke="#c9a84c" stroke-width="1.75" fill="none" stroke-linecap="round"/>
        </svg>
        <span class="nav__logo-text">Deep Groove <span>HiFi</span></span>
      </a>
      <ul class="nav__links" id="nav-links">
        <li><a href="https://deepgroovehifi.com/categories/guides/">Guides</a></li>
        <li><a href="https://deepgroovehifi.com/calculators/" class="active">Calculators</a></li>
        <li><a href="https://deepgroovehifi.com/categories/features/">Features</a></li>
        <li><a href="https://deepgroovehifi.com/about/">About</a></li>
        <li><a href="https://deepgroovehifi.com/contact/">Contact</a></li>
      </ul>
      <button class="nav__toggle" aria-label="Toggle navigation" aria-expanded="false">
        <span></span>
        <span></span>
        <span></span>
      </button>
    </div>
  </header>
"""

NEW_FOOTER_AND_END = """\

  <!-- FOOTER -->
  <footer class="footer">
    <div class="footer__inner">
      <div class="footer__grid">

        <div class="footer__brand">
          <div class="footer__logo-text">Deep Groove <span>HiFi</span></div>
          <p>Expert audiophile coverage for enthusiasts who care about the signal chain — from source to speaker.</p>
        </div>

        <div class="footer__col">
          <h4>Topics</h4>
          <ul>
            <li><a href="https://deepgroovehifi.com/categories/guides/">Guides</a></li>
            <li><a href="https://deepgroovehifi.com/categories/reviews/">Reviews</a></li>
            <li><a href="https://deepgroovehifi.com/categories/features/">Features</a></li>
            <li><a href="https://deepgroovehifi.com/articles/">All Articles</a></li>
          </ul>
        </div>

        <div class="footer__col">
          <h4>Gear Types</h4>
          <ul>
            <li><a href="https://deepgroovehifi.com/tags/dac/">DACs</a></li>
            <li><a href="https://deepgroovehifi.com/tags/amplifiers/">Amplifiers</a></li>
            <li><a href="https://deepgroovehifi.com/tags/turntables/">Turntables</a></li>
            <li><a href="https://deepgroovehifi.com/tags/speakers/">Speakers</a></li>
            <li><a href="https://deepgroovehifi.com/tags/streamers/">Streamers</a></li>
          </ul>
        </div>

        <div class="footer__col">
          <h4>Site</h4>
          <ul>
            <li><a href="https://deepgroovehifi.com/about/">About</a></li>
            <li><a href="https://deepgroovehifi.com/contact/">Contact</a></li>
            <li><a href="https://deepgroovehifi.com/privacy-policy/">Privacy Policy</a></li>
            <li><a href="https://deepgroovehifi.com/affiliate-disclosure/">Affiliate Disclosure</a></li>
          </ul>
        </div>

        <div class="footer__col">
          <h4>Sister Sites</h4>
          <ul>
            <li><a href="https://audiochainhifi.com" target="_blank" rel="noopener">AudioChainHiFi.com</a></li>
            <li><a href="https://audioscopehifi.com" target="_blank" rel="noopener">AudioScopeHiFi.com</a></li>
          </ul>
        </div>

      </div>
      <div class="footer__bottom">
        <p class="footer__copy">&copy; 2026 Deep Groove HiFi. All rights reserved.</p>
      </div>
    </div>
  </footer>

  <script>
    const toggle = document.querySelector('.nav__toggle');
    const links  = document.querySelector('.nav__links');
    toggle.addEventListener('click', () => {
      const open = links.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', open);
    });
  </script>

</body>
</html>"""


# ── Per-file transformation ───────────────────────────────────────────────────

def fix_file(filepath):
    if not os.path.exists(filepath):
        print(f'  ✗ Not found: {filepath}')
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. html font-size (handles both "html { scroll-behavior..." and multi-line)
    content = re.sub(
        r'(html\s*\{[^}]*?)scroll-behavior:\s*smooth',
        lambda m: m.group(0) if 'font-size' in m.group(1)
                  else m.group(1) + 'font-size: 18px; scroll-behavior: smooth',
        content
    )

    # 2. network-bar__inner max-width 1100 → 1200 (handles one-liners and multi-line)
    content = re.sub(
        r'(\.network-bar__inner\s*\{[^}]*?)max-width:\s*1100px',
        r'\1max-width: 1200px',
        content,
        flags=re.DOTALL
    )

    # 3. network-bar__label color #9a9a9a → #7A6A58
    content = re.sub(
        r'(\.network-bar__label\s*\{[^}]*?)color:\s*#9a9a9a',
        r'\1color: #7A6A58',
        content,
        flags=re.DOTALL
    )

    # 4. network-bar__dot font-size 10px → 11px
    content = re.sub(
        r'(\.network-bar__dot\s*\{[^}]*?)font-size:\s*10px',
        r'\1font-size: 11px',
        content,
        flags=re.DOTALL
    )

    # 5. Nav CSS: replace from /* ── NAV ── */ up to (not including) /* ── HERO ── */
    content = re.sub(
        r'/\*\s*──\s*NAV\s*──\s*\*/.*?(?=/\*\s*──\s*HERO)',
        NEW_NAV_CSS,
        content,
        flags=re.DOTALL
    )

    # 6. Footer CSS: replace from /* ── FOOTER ── */ through </style>
    content = re.sub(
        r'/\*\s*──\s*FOOTER\s*──\s*\*/.*?</style>',
        NEW_FOOTER_CSS,
        content,
        flags=re.DOTALL
    )

    # 7. Nav HTML: replace from <!-- NETWORK BAR --> through closing </nav> or </header>
    content = re.sub(
        r'<!--\s*NETWORK BAR\s*-->.*?</(?:nav|header)>',
        NEW_NAV_HTML,
        content,
        flags=re.DOTALL
    )

    # 8. Footer + end-of-file: replace from <!-- FOOTER --> to end
    content = re.sub(
        r'<!--\s*FOOTER\s*-->.*',
        NEW_FOOTER_AND_END,
        content,
        flags=re.DOTALL
    )

    if content == original:
        print(f'  ⚠ No changes detected in: {filepath}')
        print(f'    (Check that comment markers like <!-- NETWORK BAR --> exist in the file)')
        return False

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f'  ✓ {filepath}')
    return True


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    print('Fixing calculator nav/footer to match Hugo theme...\n')
    ok = sum(fix_file(f) for f in FILES)
    print(f'\nDone: {ok}/{len(FILES)} files updated.')
    if ok < len(FILES):
        print('See warnings above — those files may need a manual check.')

if __name__ == '__main__':
    main()
