import puppeteer from 'puppeteer';

async function testPacketInspector() {
  const browser = await puppeteer.launch({
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 1400, height: 900 });

  const errors = [];
  page.on('console', msg => {
    if (msg.type() === 'error') errors.push(msg.text());
  });
  page.on('pageerror', err => errors.push(err.message));

  console.log("Navigating to http://localhost:8000/ ...");
  await page.goto('http://localhost:8000/', { waitUntil: 'networkidle0' });
  await new Promise(r => setTimeout(r, 1000));

  const protocolsToTest = ['http2', 'http3', 'mqtt', 'grpc', 'ws'];

  for (const id of protocolsToTest) {
    console.log(`\nTesting packet inspector for ${id}:`);
    
    // Select protocol
    await page.evaluate((lid) => {
      document.querySelector(`.sidebar .proto[data-lesson="${lid}"] .proto-row`).click();
    }, id);
    await new Promise(r => setTimeout(r, 800));

    // Click on a packet row (e.g. row index 2 or 3)
    const clickedRow = await page.evaluate(() => {
      // Find packet table row
      const rows = Array.from(document.querySelectorAll('.pkt-row, tr[data-packet]'));
      if (rows.length > 2) {
        rows[2].click();
        return true;
      } else if (rows.length > 0) {
        rows[0].click();
        return true;
      }
      return false;
    });

    console.log(`  Clicked packet table row: ${clickedRow}`);
    await new Promise(r => setTimeout(r, 800));

    // Inspect the packet inspector panel
    const inspectorInfo = await page.evaluate(() => {
      const panel = document.querySelector('.inspector, .ins-card, .ins-layer, .packet-inspector');
      const title = document.querySelector('.ins-title, .ins-proto, .ins-name')?.textContent?.trim();
      const fields = Array.from(document.querySelectorAll('.ins-field, .ins-row')).map(f => f.textContent.replace(/\s+/g, ' ').trim()).slice(0, 5);
      const hex = document.querySelector('.ins-hex, .hexdump, .ins-bytes')?.textContent?.slice(0, 80);
      return { title, fields, hexSample: hex };
    });

    console.log(`  Inspector content:`, inspectorInfo);
    await page.screenshot({ path: `inspector_${id}.png` });
  }

  console.log("\nTotal errors during inspector testing:", errors.length);
  if (errors.length > 0) {
    console.error("Errors:", errors);
  }

  await browser.close();
}

testPacketInspector().catch(console.error);
