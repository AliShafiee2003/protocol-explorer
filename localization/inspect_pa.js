import fs from 'fs';

const js = fs.readFileSync('assets/index-4NePqLyW.js', 'utf8');
const idx = js.indexOf('Pa=');
console.log(js.substring(idx - 50, idx + 100));
