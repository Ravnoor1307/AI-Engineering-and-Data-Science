/**
 * Render study-notes HTML to PDF with Chromium via Playwright (patchright).
 *
 * `page.pdf()` accepts a displayHeaderFooter with templates, so page numbers
 * and a running unit header can be produced. The plain Chrome CLI flag cannot
 * express those, which is why this path is preferred.
 *
 * Usage: node render_pdf.mjs <htmlPath> <pdfPath> [unitTitle]
 */
import { createRequire } from 'node:module';
import { existsSync } from 'node:fs';
import path from 'node:path';

const STANDALONE =
  'C:\\Users\\RAVNOOR SINGH\\.vscode\\extensions\\danielsanmedium.dscodegpt-3.24.76\\standalone';

const require = createRequire(path.join(STANDALONE, 'noop.js'));

function loadPlaywright() {
  const candidates = ['patchright', 'playwright-core', 'playwright'];
  for (const name of candidates) {
    try {
      return require(name);
    } catch {
      /* try next */
    }
  }
  throw new Error('no playwright/patchright module available');
}

const esc = (s) =>
  String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

function headerTemplate(title) {
  return `<div style="font-size:7px;width:100%;padding:0 15mm;color:#94a3b8;
    font-family:Helvetica,Arial,sans-serif;display:flex;justify-content:space-between;
    align-items:center;">
    <span style="letter-spacing:.06em;text-transform:uppercase;">${esc(title)}</span>
  </div>`;
}

function footerTemplate() {
  return `<div style="font-size:7.5px;width:100%;padding:0 15mm;color:#94a3b8;
    font-family:Helvetica,Arial,sans-serif;display:flex;justify-content:space-between;
    align-items:center;">
    <span>AI Engineering Foundations</span>
    <span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span>
  </div>`;
}

async function main() {
  const [htmlArg, pdfArg, titleArg] = process.argv.slice(2);
  if (!htmlArg || !pdfArg) {
    console.error('usage: node render_pdf.mjs <htmlPath> <pdfPath> [unitTitle]');
    process.exit(2);
  }

  const htmlPath = path.resolve(htmlArg);
  const pdfPath = path.resolve(pdfArg);
  const unitTitle = titleArg && titleArg !== '-' ? titleArg : 'AI Engineering Foundations';

  if (!existsSync(htmlPath)) {
    console.error(`html not found: ${htmlPath}`);
    process.exit(2);
  }

const { chromium } = loadPlaywright();

// Prefer a system Chrome/Edge so no browser download is required.
const CHROME_PATHS = [
  'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
  'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe',
  'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe',
  'C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe',
];
const executablePath = CHROME_PATHS.find((p) => existsSync(p));

const browser = await chromium.launch({
  headless: true,
  ...(executablePath ? { executablePath } : {}),
  args: ['--no-sandbox', '--disable-dev-shm-usage'],
});

  try {
    const page = await browser.newPage();
    await page.goto(`file:///${htmlPath.replace(/\\/g, '/')}`, {
      waitUntil: 'load',
      timeout: 120000,
    });

    // Fonts and the ambient background need a frame before printing.
    await page.evaluate(() => document.fonts && document.fonts.ready);
    await page.waitForTimeout(600);

    await page.pdf({
      path: pdfPath,
      format: 'A4',
      printBackground: true,
      displayHeaderFooter: true,
      headerTemplate: headerTemplate(unitTitle),
      footerTemplate: footerTemplate(),
      margin: { top: '14mm', bottom: '14mm', left: '0', right: '0' },
      preferCSSPageSize: false,
    });

    const { size } = await import('node:fs').then((m) => m.statSync(pdfPath));
    console.log(JSON.stringify({ ok: true, bytes: size, path: pdfPath }));
  } catch (err) {
    console.error(JSON.stringify({ ok: false, error: String(err && err.message ? err.message : err) }));
    process.exitCode = 1;
  } finally {
    await browser.close();
  }
}

main();