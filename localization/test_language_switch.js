import puppeteer from 'puppeteer';

async function testLangSwitch() {
  const browser = await puppeteer.launch({
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 1400, height: 900 });

  console.log("Loading http://localhost:8000/ ...");
  await page.goto('http://localhost:8000/', { waitUntil: 'networkidle0' });
  await new Promise(r => setTimeout(r, 1000));

  // Function to switch language via select element
  const testLangs = ['fa', 'en', 'ar', 'es', 'ja', 'zh'];

  for (const lang of testLangs) {
    console.log(`\nTesting language switch to: ${lang}`);
    await page.evaluate((l) => {
      const select = document.querySelector('select.lang-select, select[aria-label="Language"], select');
      if (select) {
        select.value = l;
        select.dispatchEvent(new Event('change', { bubbles: true }));
      }
    }, lang);

    await new Promise(r => setTimeout(r, 1200));

    // Read HTTP/2 and HTTP/3 row titles in sidebar
    const labels = await page.evaluate(() => {
      const h2 = document.querySelector('.sidebar .proto[data-lesson="http2"]')?.textContent?.replace(/\s+/g, ' ').trim();
      const h3 = document.querySelector('.sidebar .proto[data-lesson="http3"]')?.textContent?.replace(/\s+/g, ' ').trim();
      const ws = document.querySelector('.sidebar .proto[data-lesson="ws"]')?.textContent?.replace(/\s+/g, ' ').trim();
      return { h2, h3, ws };
    });

    console.log(`  Sidebar labels in ${lang}:`, labels);
    await page.screenshot({ path: `lang_${lang}.png` });
  }

  await browser.close();
}

testLangSwitch().catch(console.error);
