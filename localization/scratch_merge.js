import fs from 'fs';

const orig = JSON.parse(fs.readFileSync('translations_en_ar.json', 'utf8'));
const origKeys = Object.keys(orig);

const c1 = JSON.parse(fs.readFileSync('chunk_1_fa.json', 'utf8'));
const c2 = JSON.parse(fs.readFileSync('chunk_2_fa.json', 'utf8'));
const c3 = JSON.parse(fs.readFileSync('chunk_3_fa.json', 'utf8'));
const c4 = JSON.parse(fs.readFileSync('chunk_4_fa.json', 'utf8'));
const c5 = JSON.parse(fs.readFileSync('chunk_5_fa.json', 'utf8'));

const merged = { ...c1, ...c2, ...c3, ...c4, ...c5 };
const mergedKeys = Object.keys(merged);

console.log('Original keys count:', origKeys.length);
console.log('Merged keys count:', mergedKeys.length);

const missing = origKeys.filter(k => !(k in merged));
console.log('Missing keys:', missing.length);
if (missing.length > 0) {
  console.log('First 5 missing:', missing.slice(0, 5));
}

fs.writeFileSync('translations_fa.json', JSON.stringify(merged, null, 2), 'utf8');
console.log('Wrote translations_fa.json successfully');
