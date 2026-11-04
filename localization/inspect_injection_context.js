import fs from 'fs';

const js = fs.readFileSync('assets/index-4NePqLyW.js', 'utf8');
const idx = js.indexOf('Xt=[');
console.log('After Xt=[');
console.log(js.substring(idx + 1000, idx + 1600));
