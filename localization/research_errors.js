import fs from 'fs';

const js = fs.readFileSync('assets/index-4NePqLyW.js', 'utf8');

// Search for note event rendering
const noteIdx = js.indexOf('type:"note"');
if (noteIdx !== -1) {
  console.log('type:"note" context:');
  console.log(js.substring(Math.max(0, noteIdx - 100), noteIdx + 500));
}

// Search for how lost packets are flagged or rendered
const lostIdx = js.indexOf('lost:!0');
if (lostIdx !== -1) {
  console.log('\nlost:!0 context:');
  console.log(js.substring(Math.max(0, lostIdx - 100), lostIdx + 400));
}
