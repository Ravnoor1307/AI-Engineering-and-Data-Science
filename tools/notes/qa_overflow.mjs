export default async function run(page) {
  await page.setViewportSize({ width: 390, height: 900 });
  await page.waitForTimeout(300);

  return await page.evaluate(() => {
    const doc = document.documentElement;
    const before = doc.scrollWidth;

    // Measure the ambient background pseudo-elements, which use a negative
    // inset and can widen the scrollable area.
    const pre = getComputedStyle(document.body, '::before');
    const after = getComputedStyle(document.body, '::after');

    const suspects = {};

    // Turn off the decorative pseudo-elements and re-measure.
    const style = document.createElement('style');
    style.textContent = 'body::before, body::after { display: none !important; }';
    document.head.appendChild(style);
    suspects.withoutPseudo = doc.scrollWidth;
    style.remove();

    // Turn off the code shell overflow and re-measure.
    const style2 = document.createElement('style');
    style2.textContent = '.code-shell pre { overflow-x: visible !important; }';
    document.head.appendChild(style2);
    suspects.codeVisible = doc.scrollWidth;
    style2.remove();

    // Turn off tables.
    const style3 = document.createElement('style');
    style3.textContent = '.table-wrap { overflow-x: visible !important; }';
    document.head.appendChild(style3);
    suspects.tableVisible = doc.scrollWidth;
    style3.remove();

    // Turn off the drawer.
    const style4 = document.createElement('style');
    style4.textContent = '.sidebar { display: none !important; }';
    document.head.appendChild(style4);
    suspects.noSidebar = doc.scrollWidth;
    style4.remove();

    // Clip everything.
    const style5 = document.createElement('style');
    style5.textContent = 'html, body { overflow-x: hidden !important; }';
    document.head.appendChild(style5);
    suspects.htmlClip = doc.scrollWidth;
    style5.remove();

    return {
      docScrollW: before,
      docClientW: doc.clientWidth,
      pseudoBefore: { position: pre.position, inset: pre.inset, width: pre.width, left: pre.left },
      pseudoAfter: { position: after.position, inset: after.inset, width: after.width },
      bodyOverflowX: getComputedStyle(document.body).overflowX,
      htmlOverflowX: getComputedStyle(document.documentElement).overflowX,
      suspects,
    };
  });
}