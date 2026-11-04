import fs from 'fs';

const js = fs.readFileSync('assets/index-4NePqLyW.js', 'utf8');
const idx = js.indexOf('function tc(');
console.log(js.substring(idx, idx + 800));
