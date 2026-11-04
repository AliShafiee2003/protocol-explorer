import fs from 'fs';

async function testExportVar() {
  const files = [
    { f: 'ar-SjO31DnI.js', v: 'T' },
    { f: 'de-HYTLkJDz.js', v: 'h' },
    { f: 'es-C9vklYn6.js', v: 'p' },
    { f: 'fr-QqmZdpVw.js', v: 'c' },
    { f: 'he-Dd-kXJJK.js', v: 'd' },
    { f: 'hi-Bnsh4qCD.js', v: 'i' },
    { f: 'id-CDETR5_t.js', v: 'o' },
    { f: 'ja-C4-8Cz_-.js', v: 'r' },
    { f: 'ko-DmUagyds.js', v: 'n' },
    { f: 'pt-J1dFf1-g.js', v: 'c' },
    { f: 'tr-EKtCvHjH.js', v: 'o' },
    { f: 'zh-DWvsr0s_.js', v: 'r' },
    { f: 'zh-TW-CmWpn3k9.js', v: 'r' }
  ];

  for (const item of files) {
    const mod = (await import(`../assets/${item.f}`)).default;
    console.log(`${item.f}: has strings? ${!!mod.strings} (count: ${Object.keys(mod.strings).length})`);
  }
}

testExportVar().catch(console.error);
