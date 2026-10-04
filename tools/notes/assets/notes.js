(function () {
  'use strict';

  /* ---------- Save as PDF ---------- */
  var saveBtn = document.getElementById('savePdfBtn');
  if (saveBtn) {
    saveBtn.addEventListener('click', function () { window.print(); });
  }

  /* ---------- Back to top ---------- */
  var topBtn = document.getElementById('backToTop');
  if (topBtn) {
    topBtn.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  /* ---------- Reading progress ---------- */
  var bar = document.querySelector('.reading-progress');
  var ticking = false;

  function updateProgress() {
    if (!bar) return;
    var doc = document.documentElement;
    var scrollTop = window.pageYOffset || doc.scrollTop;
    var scrollHeight = doc.scrollHeight - window.innerHeight;
    var pct = scrollHeight > 0 ? (scrollTop / scrollHeight) * 100 : 0;
    bar.style.width = Math.min(100, Math.max(0, pct)) + '%';

    if (topBtn) {
      topBtn.classList.toggle('visible', window.pageYOffset > 600);
    }
    ticking = false;
  }

  if (bar) {
    window.addEventListener('scroll', function () {
      if (!ticking) {
        window.requestAnimationFrame(updateProgress);
        ticking = true;
      }
    }, { passive: true });
    updateProgress();
  } else {
    window.addEventListener('scroll', function () {
      if (topBtn) topBtn.classList.toggle('visible', window.pageYOffset > 600);
    }, { passive: true });
  }

  /* ---------- Copy code ---------- */
  document.querySelectorAll('.copy-code').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var shell = btn.closest('.code-shell');
      var code = shell ? shell.querySelector('pre code') : null;
      if (!code) return;

      var text = code.innerText;
      var done = function () {
        btn.classList.add('copied');
        var label = btn.querySelector('span');
        if (label) label.textContent = 'Copied';
        setTimeout(function () {
          btn.classList.remove('copied');
          if (label) label.textContent = 'Copy';
        }, 1800);
      };

      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done).catch(function () { fallbackCopy(text, done); });
      } else {
        fallbackCopy(text, done);
      }
    });
  });

  function fallbackCopy(text, cb) {
    var ta = document.createElement('textarea');
    ta.value = text;
    ta.setAttribute('readonly', '');
    ta.style.position = 'absolute';
    ta.style.left = '-9999px';
    document.body.appendChild(ta);
    ta.select();
    try { document.execCommand('copy'); cb(); } catch (e) { /* noop */ }
    document.body.removeChild(ta);
  }

  /* ---------- Mobile TOC drawer ---------- */
  var toggle = document.querySelector('.mobile-toc-toggle');
  var sidebar = document.querySelector('.sidebar');
  var backdrop = document.querySelector('.sidebar-backdrop');

  function closeSidebar() {
    if (sidebar) sidebar.classList.remove('open');
    if (backdrop) backdrop.classList.remove('visible');
  }

  if (toggle && sidebar) {
    toggle.addEventListener('click', function () {
      sidebar.classList.toggle('open');
      if (backdrop) backdrop.classList.toggle('visible', sidebar.classList.contains('open'));
    });
  }

  if (backdrop) {
    backdrop.addEventListener('click', closeSidebar);
  }

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeSidebar();
  });

  /* ---------- Active TOC section ---------- */
  var links = Array.prototype.slice.call(document.querySelectorAll('.toc-link'));
  if (links.length && 'IntersectionObserver' in window) {
    var map = {};
    var targets = [];

    links.forEach(function (link) {
      var id = link.getAttribute('href');
      if (!id || id.charAt(0) !== '#') return;
      var el = document.querySelector(id);
      if (el) {
        map[id.slice(1)] = link;
        targets.push(el);
      }
    });

    var visible = {};

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        visible[entry.target.id] = entry.isIntersecting ? entry.intersectionRatio : 0;
      });

      var bestId = null;
      var bestRatio = 0;
      targets.forEach(function (t) {
        var r = visible[t.id] || 0;
        if (r > bestRatio) { bestRatio = r; bestId = t.id; }
      });

      if (!bestId) {
        // fall back to the last heading above the fold
        var offset = window.pageYOffset + 120;
        for (var i = 0; i < targets.length; i++) {
          if (targets[i].offsetTop <= offset) bestId = targets[i].id;
        }
      }

      links.forEach(function (l) { l.classList.remove('active'); });
      if (bestId && map[bestId]) map[bestId].classList.add('active');
    }, {
      rootMargin: '-80px 0px -55% 0px',
      threshold: [0, 0.15, 0.4, 0.75, 1]
    });

    targets.forEach(function (t) { observer.observe(t); });
  }
})();
