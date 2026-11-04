import puppeteer from 'puppeteer';

async function testLanguageSwitchingDirect() {
  const browser = await puppeteer.launch({
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 1400, height: 900 });

  console.log("Navigating to http://localhost:8000/ ...");
  await page.goto('http://localhost:8000/', { waitUntil: 'networkidle0' });
  await new Promise(r => setTimeout(r, 1000));

  const testLangs = [
    { code: 'fa', name: 'Persian' },
    { code: 'en', name: 'English' },
    { code: 'ar', name: 'Arabic' },
    { code: 'es', name: 'Spanish' },
    { code: 'fr', name: 'French' },
    { code: 'de', name: 'German' },
    { code: 'zh', name: 'Chinese' },
    { code: 'ja', name: 'Japanese' }
  ];

  for (const lang of testLangs) {
    console.log(`\nSwitching language to ${lang.name} (${lang.code})...`);
    
    // Switch via window / localStorage and trigger reload or UI update
    await page.evaluate(async (lcode) => {
      localStorage.setItem('protocol-explorer:lang', lcode);
    }, lang.code);

    await page.goto('http://localhost:8000/', { waitUntil: 'networkidle0' });
    await new Promise(r => setTimeout(r, 1000));

    // Read HTTP/2 and WebSocket title in the sidebar
    const titles = await page.evaluate(() => {
      const h2 = document.querySelector('.sidebar .proto[data-lesson="http2"]')?.textContent?.replace(/\s+/g, ' ').trim();
      const ws = document.querySelector('.sidebar .proto[data-lesson="ws"]')?.textContent?.replace(/\s+/g, ' ').trim();
      const sse = document.querySelector('.sidebar .proto[data-lesson="sse"]')?.textContent?.replace(/\s+/g, ' ').trim();
      return { h2: h2?.slice(0, 70), ws: ws?.slice(0, 70), sse: sse?.slice(0, 70) };
    });

    console.log(`  Titles in ${lang.name}:`, titles);
    await page.screenshot({ path: `lang_verified_${lang.code}.png` });
  }

  await browser.close();
  console.log("\nLanguage switching verification completed successfully!");
}

testLanguageSwitchingDirect().catch(console.error);
