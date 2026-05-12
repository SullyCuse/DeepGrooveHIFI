/* Audio Chain HiFi — main.js */

// ── Mobile navigation toggle ──────────────────────────────────────────────────
const toggle = document.querySelector('.nav__toggle');
const navLinks = document.querySelector('.nav__links');

if (toggle && navLinks) {
  toggle.addEventListener('click', () => {
    navLinks.classList.toggle('is-open');
  });

  // Close menu when a link is clicked
  navLinks.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => navLinks.classList.remove('is-open'));
  });
}

// ── Cookie consent banner ─────────────────────────────────────────────────────
const COOKIE_KEY = 'achifi_cookie_consent';
const banner = document.querySelector('.cookie-banner');
const acceptBtn = document.querySelector('#cookie-accept');
const declineBtn = document.querySelector('#cookie-decline');

function showBanner() {
  if (banner && !localStorage.getItem(COOKIE_KEY)) {
    // Small delay so the page loads first
    setTimeout(() => banner.classList.add('is-visible'), 800);
  }
}

function dismissBanner(accepted) {
  localStorage.setItem(COOKIE_KEY, accepted ? 'accepted' : 'declined');
  if (banner) {
    banner.classList.remove('is-visible');
    setTimeout(() => banner.remove(), 400);
  }
}

if (acceptBtn)  acceptBtn.addEventListener('click',  () => dismissBanner(true));
if (declineBtn) declineBtn.addEventListener('click', () => dismissBanner(false));

showBanner();

// ── Reading progress bar (optional enhancement) ───────────────────────────────
const progressBar = document.querySelector('.reading-progress');
if (progressBar) {
  window.addEventListener('scroll', () => {
    const scrollTop    = document.documentElement.scrollTop;
    const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const progress     = scrollHeight > 0 ? (scrollTop / scrollHeight) * 100 : 0;
    progressBar.style.width = progress + '%';
  }, { passive: true });
}
