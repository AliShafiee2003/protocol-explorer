import fs from 'fs';

const dict = JSON.parse(fs.readFileSync('translations_en_ar.json', 'utf8'));
const entries = Object.entries(dict);
console.log('Total entries:', entries.length);

const chunkSize = 260;
for (let i = 0; i < entries.length; i += chunkSize) {
  const chunk = Object.fromEntries(entries.slice(i, i + chunkSize));
  const chunkIndex = Math.floor(i / chunkSize) + 1;
  fs.writeFileSync(`chunk_${chunkIndex}.json`, JSON.stringify(chunk, null, 2), 'utf8');
  console.log(`Saved chunk_${chunkIndex}.json with ${Object.keys(chunk).length} items`);
}
