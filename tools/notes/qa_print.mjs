/**
 * Print-media QA: confirm the print stylesheet produces textbook pages.
 *
 * Checks the things that silently ruin a printed document: leftover dark
 * background, visible screen chrome, clipped code, and oversized content.
 */
export default async function run(page) {
  await page.emulateMedia({ media: 'print' });
  await page.waitForTimeout(400);

  return await page.evaluate(() => {
    const px = (v) => Math.round(v * 10) / 10;
    const isVisible = (el) => {
      if (!el) return false;
      const st = getComputedStyle(el);
      return st.display !== 'none' && st.visibility !== 'hidden' && st.opacity !== '0';
    };

    const chromeSel = ['.sidebar', '.save-pdf-btn', '.reading-progress', '.back-to-top',
      '.mobile-toc-toggle', '.copy-code', '.sidebar-backdrop'];
    const chrome = chromeSel.map((sel) => {
      const el = document.querySelector(sel);
      return { sel, exists: !!el, visible: isVisible(el) };
    });

    const section = document.querySelector('.section-card');
    const p = section.querySelector('p:not(.callout-title)');
    const pre = document.querySelector('.code-shell pre');
    const code = document.querySelector('.code-shell pre code');

    const clipped = [];
    document.querySelectorAll('.code-shell pre, .table-wrap').forEach((el) => {
      const st = getComputedStyle(el);
      if (el.scrollWidth > el.clientWidth + 2 && st.overflowX !== 'visible') {
        clipped.push({
          cls: String(el.className).slice(0, 40),
          scrollW: el.scrollWidth,
          clientW: el.clientWidth,
        });
      }
    });

    const contentW = document.querySelector('.content').getBoundingClientRect().width;
    const docW = document.documentElement.clientWidth;

    return {
      media: 'print',
      hiddenChrome: chrome,
      bodyBg: getComputedStyle(document.body).backgroundColor,
      cardBg: getComputedStyle(section).backgroundColor,
      codeShellBg: getComputedStyle(document.querySelector('.code-shell')).backgroundColor,
      preBg: getComputedStyle(pre).backgroundColor,
      codeColor: getComputedStyle(code).color,
      paragraphColor: getComputedStyle(p).color,
      bodyFontSize: getComputedStyle(section).fontSize,
      h2FontSize: getComputedStyle(document.querySelector('h2')).fontSize,
      codeFontSize: getComputedStyle(code).fontSize,
      contentWidth: px(contentW),
      docWidth: docW,
      overflowPage: contentW > docW + 1,
      clipped,
      h2BreakAfter: getComputedStyle(document.querySelector('h2')).breakAfter,
      calloutBreakInside: getComputedStyle(document.querySelector('.callout') || section).breakInside,
      codeShellBreakInside: getComputedStyle(document.querySelector('.code-shell')).breakInside,
      tocHidden: !isVisible(document.querySelector('.sidebar')),
    };
  });
}