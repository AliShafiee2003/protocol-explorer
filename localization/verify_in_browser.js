import puppeteer from 'puppeteer';

async function testProtocols() {
  const browser = await puppeteer.launch({
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 1400, height: 900 });

  page.on('console', msg => console.log('[BROWSER]', msg.text()));
  page.on('pageerror', err => console.error('[PAGE ERROR]', err.message));

  console.log("Loading http://localhost:8000/ ...");
  await page.goto('http://localhost:8000/', { waitUntil: 'networkidle0' });
  await new Promise(r => setTimeout(r, 1000));

  // Inspect all data-lesson elements
  const lessons = await page.evaluate(() => {
    const items = Array.from(document.querySelectorAll('[data-lesson]'));
    return items.map(el => ({
      lesson: el.getAttribute('data-lesson'),
      text: el.textContent.replace(/\s+/g, ' ').trim()
    }));
  });

  console.log("Total [data-lesson] elements found:", lessons.length);
  lessons.forEach(l => console.log(`  - ${l.lesson}: ${l.text.slice(0, 50)}`));

  const targets = ['http2', 'http3', 'ws', 'mqtt', 'sse', 'chunked', 'grpc'];

  for (const id of targets) {
    console.log(`\n================ Testing ${id} ================`);
    const success = await page.evaluate((lessonId) => {
      const el = document.querySelector(`[data-lesson="${lessonId}"] .proto-row, [data-lesson="${lessonId}"] button, [data-lesson="${lessonId}"]`);
      if (el) {
        el.click();
        return true;
      }
      return false;
    }, id);

    console.log(`Clicked on ${id}: ${success}`);
    await new Promise(r => setTimeout(r, 1000));

    // Get current lesson header and step info
    const state = await page.evaluate(() => {
      const name = document.querySelector('.header-title, .title, h1, .lesson-title')?.textContent?.trim();
      const currentStep = document.querySelector('.step-title, .step.is-active, .narrative-title')?.textContent?.trim();
      const packetCount = document.querySelectorAll('.seq-arrow, .packet').length;
      return { name, currentStep, packetCount };
    });
    console.log(`State for ${id}:`, state);

    // Click next step button if present
    const stepClicked = await page.evaluate(() => {
      const btn = document.querySelector('button.next, button[title="Next step"], .step-nav button:last-child');
      if (btn && !btn.disabled) {
        btn.click();
        return true;
      }
      return false;
    });
    console.log(`Clicked next step for ${id}: ${stepClicked}`);
    await new Promise(r => setTimeout(r, 800));

    await page.screenshot({ path: `test_${id}.png` });
  }

  await browser.close();
}

testProtocols().catch(console.error);
