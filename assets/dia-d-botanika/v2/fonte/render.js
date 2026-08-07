const { chromium } = require('playwright-core');
const path = require('path');

(async () => {
  const [htmlRel, wStr, hStr, outRel, scaleStr, transparent, vpHStr] = process.argv.slice(2);
  const width = parseInt(wStr, 10), height = parseInt(hStr, 10);
  const vpHeight = vpHStr ? parseInt(vpHStr, 10) : height;
  const scale = scaleStr ? parseFloat(scaleStr) : 2;
  const htmlPath = path.resolve(htmlRel);
  const outPath = path.resolve(outRel);
  const browser = await chromium.launch({
    executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
    args: ['--no-sandbox', '--force-color-profile=srgb']
  });
  const page = await browser.newPage({
    viewport: { width, height: vpHeight },
    deviceScaleFactor: scale
  });
  await page.goto('file://' + htmlPath, { waitUntil: 'load', timeout: 60000 });
  try {
    await page.evaluate(() => Promise.race([
      document.fonts.ready,
      new Promise(r => setTimeout(r, 4000))
    ]));
  } catch (e) { /* best-effort font wait */ }
  await page.waitForTimeout(400);
  await page.screenshot({
    path: outPath,
    clip: { x: 0, y: 0, width, height },
    omitBackground: transparent === 'transparent'
  });
  await browser.close();
  console.log('rendered', outPath, `${width}x${height}@${scale}x`);
})();
