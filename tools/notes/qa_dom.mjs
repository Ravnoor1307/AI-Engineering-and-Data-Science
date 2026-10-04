export default async function run(page) {
  return await page.evaluate(() => {
    const px = (v) => Math.round(v);
    const doc = document.documentElement;
    const layout = document.querySelector('.layout');
    const sidebar = document.querySelector('.sidebar');
    const main = document.querySelector('.main');

    // Identify real horizontal overflow sources, ignoring intentionally
    // scrollable containers and off-screen accessibility affordances.
    const offenders = [];
    const docW = doc.clientWidth;
    document.querySelectorAll('body *').forEach((el) => {
      const st = getComputedStyle(el);
      if (st.position === 'fixed' || st.display === 'none') return;
      const r = el.getBoundingClientRect();
      if (r.width === 0) return;
      if (r.right <= docW + 1 && r.left >= -1) return;
      let p = el.parentElement, scrollable = false, hidden = false;
      while (p) {
        const ps = getComputedStyle(p);
        if (ps.overflowX === 'auto' || ps.overflowX === 'scroll') scrollable = true;
        if (ps.overflowX === 'hidden' || ps.overflow === 'hidden') hidden = true;
        if (ps.position === 'fixed') break;
        p = p.parentElement;
      }
      if (scrollable) return;
      const cls = (el.className || '').toString();
      if (cls.includes('skip-link')) return; // intentionally off-canvas
      if (st.position === 'fixed') return;
      offenders.push({
        tag: el.tagName.toLowerCase(),
        cls: cls.slice(0, 50),
        left: px(r.left),
        right: px(r.right),
        width: px(r.width),
        parentOverflowHidden: hidden,
        text: (el.textContent || '').trim().slice(0, 40),
      });
    });

    return {
      viewport: { w: window.innerWidth, h: window.innerHeight },
      gridCols: getComputedStyle(layout).gridTemplateColumns,
      sidebarW: px(sidebar.getBoundingClientRect().width),
      sidebarPosition: getComputedStyle(sidebar).position,
      mainX: px(main.getBoundingClientRect().x),
      mainW: px(main.getBoundingClientRect().width),
      sidebarVar: getComputedStyle(doc).getPropertyValue('--sidebar-w').trim(),
      bodyBg: getComputedStyle(document.body).backgroundColor,
      sectionCardBg: getComputedStyle(document.querySelector('.section-card')).backgroundColor,
      hScroll: doc.scrollWidth > doc.clientWidth + 1,
      docScrollWidth: doc.scrollWidth,
      docClientWidth: doc.clientWidth,
      offenders: offenders.slice(0, 10),
      offenderCount: offenders.length,
      counts: {
        h2: document.querySelectorAll('h2').length,
        h3: document.querySelectorAll('h3').length,
        h4: document.querySelectorAll('h4').length,
        toc: document.querySelectorAll('.toc-link').length,
        code: document.querySelectorAll('.code-shell').length,
        callout: document.querySelectorAll('.callout').length,
        table: document.querySelectorAll('.table-wrap').length,
        glossary: document.querySelectorAll('.glossary-item').length,
        check: document.querySelectorAll('.checklist input').length,
        diagram: document.querySelectorAll('.diagram').length,
        remoteImg: document.querySelectorAll('img[src^="http"]').length,
        externalFig: document.querySelectorAll('.external-figure').length,
      },
    };
  });
}