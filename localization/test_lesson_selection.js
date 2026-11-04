import puppeteer from 'puppeteer';

async function testLessonSelection() {
  const browser = await puppeteer.launch({
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 1400, height: 900 });

  page.on('console', msg => console.log('[BROWSER]', msg.text()));
  page.on('pageerror', err => console.error('[PAGE ERROR]', err.message));

  console.log("Navigating to http://localhost:8000/ ...");
  await page.goto('http://localhost:8000/', { waitUntil: 'networkidle0' });
  await new Promise(r => setTimeout(r, 1200));

  const targets = ['http2', 'http3', 'ws', 'mqtt', 'sse', 'chunked', 'grpc'];

  for (const id of targets) {
    console.log(`\nTesting lesson switch to: ${id}`);
    
    // Select via sidebar click
    const clicked = await page.evaluate((lessonId) => {
      const btn = document.querySelector(`.sidebar .proto[data-lesson="${lessonId}"] .proto-row`);
      if (btn) {
        btn.click();
        return true;
      }
      return false;
    }, id);
    console.log(`  Clicked .sidebar .proto[data-lesson="${id}"] .proto-row: ${clicked}`);

    await new Promise(r => setTimeout(r, 1000));

    // Read the overview title, badge, and first step narrative
    const info = await page.evaluate(() => {
      const title = document.querySelector('.overview-title, .overview h1, .overview h2, .overview')?.textContent?.replace(/\s+/g, ' ').slice(0, 100);
      const activeLesson = document.querySelector('.sidebar .proto.is-active, .proto.is-open')?.getAttribute('data-lesson');
      const stepHeader = document.querySelector('.step-nav-title, .narrative-title, .step.is-active')?.textContent?.replace(/\s+/g, ' ');
      const rows = document.querySelectorAll('.pkt-row, .packets tbody tr, .packets-row').length;
      return { title, activeLesson, stepHeader, rows };
    });

    console.log(`  Current UI state:`, info);

    await page.screenshot({ path: `lesson_${id}.png` });
  }

  await browser.close();
}

testLessonSelection().catch(console.error);
