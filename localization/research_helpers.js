import fs from 'fs';

const js = fs.readFileSync('assets/index-4NePqLyW.js', 'utf8');

// Find function u definition
const uIdx = js.indexOf('function u(');
if (uIdx !== -1) {
  console.log('function u:\n', js.substring(uIdx, uIdx + 400));
} else {
  const m = js.match(/.{0,30}u\s*=\s*\([^)]*\)\s*=>.{0,100}/g);
  console.log('Arrow function u matches:\n', m ? m.slice(0, 5) : 'None');
}

// Find function N definition (time formatter)
const nIdx = js.indexOf('function N(');
if (nIdx !== -1) {
  console.log('\nfunction N:\n', js.substring(nIdx, nIdx + 300));
} else {
  const m = js.match(/.{0,20}N\s*=\s*e\s*=>.{0,60}/g);
  console.log('Arrow function N matches:\n', m ? m.slice(0, 5) : 'None');
}

// Find O definition (TCP wire builder)
const oIdx = js.indexOf('function O(');
if (oIdx !== -1) {
  console.log('\nfunction O:\n', js.substring(oIdx, oIdx + 400));
} else {
  const m = js.match(/.{0,20}O\s*=\s*\([^)]*\)\s*=>.{0,100}/g);
  console.log('Arrow function O matches:\n', m ? m.slice(0, 5) : 'None');
}
