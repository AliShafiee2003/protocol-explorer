import fs from 'fs';

const js = fs.readFileSync('localization/generate_expanded_protocols_bundle.js', 'utf8');
const lines = js.split('\n');
lines.forEach((l, idx) => {
  if (l.includes('\\"')) {
    console.log(`Line ${idx + 1}: ${l.trim()}`);
  }
});
