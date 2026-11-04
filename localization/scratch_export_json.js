import fs from 'fs';

async function main() {
  const ar = (await import('./assets/ar-SjO31DnI.js')).default;
  fs.writeFileSync('translations_en_ar.json', JSON.stringify(ar.strings, null, 2), 'utf8');
  console.log('Saved translations_en_ar.json with', Object.keys(ar.strings).length, 'keys');
}

main().catch(console.error);
