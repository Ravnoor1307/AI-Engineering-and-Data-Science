export default async function run(page) {
  const out = {};
  for (const w of [390, 700, 1000, 1280, 1600]) {
    await page.setViewportSize({ width: w, height: 900 });
    await page.waitForTimeout(350);
    out[w] = await page.evaluate(() => {
      const doc = document.documentElement;
      const docW = doc.clientWidth;
      const offenders = [];
      document.querySelectorAll('body *').forEach((el) => {
        const st = getComputedStyle(el);
        if (st.display === 'none' || st.visibility === 'hidden') return;
        const r = el.getBoundingClientRect();
        if (r.width === 0) return;
        if (r.right <= docW + 1 && r.left >= -1) return;
        const cls = (el.className || '').toString();
        if (cls.includes('skip-link') || st.position === 'fixed') return;
        // walk up for scroll containers or clipping
        let p = el.parentElement, scrollable = false;
        while (p) {
          const ps = getComputedStyle(p);
          if (['auto', 'scroll', 'hidden', 'clip'].includes(ps.overflowX)) { scrollable = true; break; }
          p = p.parentElement;
        }
        if (scrollable) return;
        offenders.push({
          tag: el.tagName.toLowerCase(),
          cls: cls.slice(0, 44),
          left: Math.round(r.left),
          right: Math.round(r.right),
          width: Math.round(r.width),
          text: (el.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 50),
        });
      });
      return {
        docScrollW: doc.scrollWidth,
        docClientW: doc.clientWidth,
        hScroll: doc.scrollWidth > doc.clientWidth + 1,
        offenders: offenders.slice(0, 6),
        count: offenders.length,
      };
    });
  }
  return out;
}