(function () {
  const THEME_STORAGE_KEY = 'reference_sheets_theme';

  function getEventTargetFallback() {
    try {
      // Inline onclick handlers often have a global `event`.
      // This will be undefined for programmatic calls.
      // eslint-disable-next-line no-undef
      return typeof event !== 'undefined' ? event.target : null;
    } catch {
      return null;
    }
  }

  window.show = function show(id, el) {
    document.querySelectorAll('.section').forEach((s) => s.classList.remove('active'));

    const next = document.getElementById(id);
    if (next) next.classList.add('active');

    const nav = document.getElementById('nav');
    if (!nav) return;

    nav.querySelectorAll('button').forEach((b) => b.classList.remove('active'));

    const raw = el || getEventTargetFallback();
    const btn = raw && raw.closest ? raw.closest('button') : null;
    if (btn) btn.classList.add('active');
  };

  window.setTheme = function setTheme(el) {
    const theme = el && el.dataset ? el.dataset.p : null;
    if (!theme) return;

    document.body.setAttribute('data-theme', theme);
    try {
      localStorage.setItem(THEME_STORAGE_KEY, theme);
    } catch {
      // ignore (privacy mode / disabled storage)
    }

    document.querySelectorAll('.swatch').forEach((s) => s.classList.remove('active'));
    el.classList.add('active');
  };

  function initThemeFromStorage() {
    const body = document.body;
    if (!body || !body.hasAttribute('data-theme')) return;

    let theme = null;
    try {
      theme = localStorage.getItem(THEME_STORAGE_KEY);
    } catch {
      theme = null;
    }
    if (!theme) return;

    body.setAttribute('data-theme', theme);

    const swatch = document.querySelector(`.swatch[data-p="${theme}"]`);
    if (!swatch) return;

    document.querySelectorAll('.swatch').forEach((s) => s.classList.remove('active'));
    swatch.classList.add('active');
  }

  document.addEventListener('DOMContentLoaded', () => {
    initThemeFromStorage();
  });
})();
