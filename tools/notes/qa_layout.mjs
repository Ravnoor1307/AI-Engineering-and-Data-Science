export default async function run(page, ui) {
  const probe = async () => {
    return await page.evaluate(() => {
      const px = (v) => Math.round(v * 10) / 10;
      const cs = (sel, prop) => {
        const el = document.querySelector(sel);
        return el ? getComputedStyle(el)[prop] : null;
      };
      const rect = (sel) => {
        const el = document.querySelector(sel);
        if (!el) return null;
        const r = el.getBoundingClientRect();
        return { x: px(r.x), y: px(r.y), w: px(r.width), h: px(r.height) };
      };

      // Find elements that overflow the document width horizontally.
      const overflowers = [];
      const docW = document.documentElement.clientWidth;
      document.querySelectorAll('body *').forEach((el) => {
        const r = el.getBoundingClientRect();
        if (r.width > 0 && (r.right > docW + 2 || r.left < -2)) {
          const style = getComputedStyle(el);
          // ignore intentionally scrollable containers
          if (style.overflowX === 'auto' || style.overflowX === 'scroll') return;
          let p = el.parentElement, scrollable = false;
          while (p) {
            const ps = getComputedStyle(p);
            if (ps.overflowX === 'auto' || ps.overflowX === 'scroll') { scrollable = true; break; }
            p = p.parentElement;
          }
          if (scrollable) return;
          overflowers.push({
            tag: el.tagName.toLowerCase(),
            cls: (el.className || '').toString().slice(0, 60),
            right: px(r.right),
            left: px(r.left),
          });
        }
      });

      // Relative luminance contrast check on the main text colours.
      const lum = (rgb) => {
        const [r, g, b] = rgb.map((v) => {
          v = v / 255;
          return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
        });
        return 0.2126 * r + 0.7152 * g + 0.0722 * b;
      };
      const parse = (s) => (s.match(/[\d.]+/g) || []).slice(0, 3).map(Number);
      const ratio = (a, b) => {
        const l1 = lum(a), l2 = lum(b);
        return px(Math.round(((Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05)) * 100) / 100);
      };

      const bodyBg = parse(getComputedStyle(document.body).backgroundColor);
      const pEl = document.querySelector('.section-card p:not(.callout-title)');
      const pColor = pEl ? parse(getComputedStyle(pEl).color) : null;
      const h2El = document.querySelector('h2');
      const h2Color = h2El ? parse(getComputedStyle(h2El).color) : null;
      const tocEl = document.querySelector('.toc-link');
      const tocColor = tocEl ? parse(getComputedStyle(tocEl).color) : null;

      // Do headings inherit the dark background correctly (no white card)?
      const cardBg = cs('.section-card', 'backgroundColor');

      const saveBtn = document.querySelector('#savePdfBtn');
      const saveRect = saveBtn ? saveBtn.getBoundingClientRect() : null;

      return {
        viewport: { w: window.innerWidth, h: window.innerHeight },
        docScrollWidth: document.documentElement.scrollWidth,
        docClientWidth: document.documentElement.clientWidth,
        horizontalScroll: document.documentElement.scrollWidth > document.documentElement.clientWidth + 1,
        sidebar: rect('.sidebar'),
        main: rect('.main'),
        content: rect('.content'),
        hero: rect('.hero'),
        sectionCard: rect('.section-card'),
        codeShell: rect('.code-shell'),
        tocLink: rect('.toc-link'),
        saveBtn: saveRect ? { x: px(saveRect.x), y: px(saveRect.y), w: px(saveRect.width), h: px(saveRect.height) } : null,
        sidebarPosition: cs('.sidebar', 'position'),
        sidebarOverflowY: cs('.sidebar', 'overflowY'),
        mobileToggleDisplay: cs('.mobile-toc-toggle', 'display'),
        bodyBg: getComputedStyle(document.body).backgroundColor,
        sectionCardBg: cardBg,
        fontSize: cs('.section-card', 'fontSize'),
        lineHeight: cs('.section-card', 'lineHeight'),
        contrast: {
          paragraph: pColor ? ratio(pColor, bodyBg) : null,
          h2: h2Color ? ratio(h2Color, bodyBg) : null,
          tocLink: tocColor ? ratio(tocColor, bodyBg) : null,
        },
        overflowers: overflowers.slice(0, 12),
        overflowCount: overflowers.length,
        h2Count: document.querySelectorAll('h2').length,
        codeCount: document.querySelectorAll('.code-shell').length,
        calloutCount: document.querySelectorAll('.callout').length,
        tableCount: document.querySelectorAll('.table-wrap table').length,
        tocCount: document.querySelectorAll('.toc-link').length,
        glossaryCount: document.querySelectorAll('.glossary-item').length,
        checklistCount: document.querySelectorAll('.checklist input').length,
        hasPrintBtn: !!saveBtn,
        externalAssets: [...document.querySelectorAll('link[href],script[src],img[src]')]
          .map((e) => e.getAttribute('href') || e.getAttribute('src'))
          .filter((u) => /^https?:|^\/\//.test(u)),
      };
    });
  };

  const desktop = await probe();

  // Exercise the interactive layer.
  const interactions = {};
  await page.locator('.copy-code').first().click();
  await page.waitForTimeout(200);
  interactions.copyLabel = await page.locator('.copy-code').first().innerText();

  await page.locator('#backToTop').click().catch(() => {});
  interactions.scrollTopAfterBackToTop = await page.evaluate(() => window.pageYOffset);

  await page.evaluate(() => window.scrollTo(0, 3000));
  await page.waitForTimeout(300);
  interactions.progressWidth = await page.evaluate(() => {
    const b = document.querySelector('.reading-progress');
    return b ? b.style.width : null;
  });
  interactions.backToTopVisible = await page.evaluate(() =>
    document.querySelector('#backToTop').classList.contains('visible'));
  interactions.activeToc = await page.evaluate(() => {
    const a = document.querySelector('.toc-link.active');
    return a ? a.getAttribute('href') : null;
  });

  // Mobile viewport.
  await page.setViewportSize({ width: 390, height: 844 });
  await page.waitForTimeout(400);
  const mobile = await probe();
  const drawer = {};
  drawer.toggleVisible = await page.evaluate(() =>
    getComputedStyle(document.querySelector('.mobile-toc-toggle')).display);
  await page.locator('.mobile-toc-toggle').click();
  await page.waitForTimeout(500);
  drawer.sidebarOpen = await page.evaluate(() =>
    document.querySelector('.sidebar').classList.contains('open'));
  drawer.sidebarRect = await page.evaluate(() => {
    const r = document.querySelector('.sidebar').getBoundingClientRect();
    return { x: Math.round(r.x), w: Math.round(r.width) };
  });
  drawer.backdropVisible = await page.evaluate(() =>
    document.querySelector('.sidebar-backdrop').classList.contains('visible'));
  await page.evaluate(() => {
    document.querySelector('.sidebar-backdrop').click();
  });
  await page.waitForTimeout(400);
  drawer.closedAfterBackdrop = await page.evaluate(() =>
    !document.querySelector('.sidebar').classList.contains('open'));

  // Escape key must also close the drawer.
  await page.locator('.mobile-toc-toggle').click();
  await page.waitForTimeout(300);
  drawer.reopened = await page.evaluate(() =>
    document.querySelector('.sidebar').classList.contains('open'));
  await page.keyboard.press('Escape');
  await page.waitForTimeout(300);
  drawer.closedAfterEscape = await page.evaluate(() =>
    !document.querySelector('.sidebar').classList.contains('open'));

  return { desktop, interactions, mobile, drawer };
}