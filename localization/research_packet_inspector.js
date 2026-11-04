import fs from 'fs';

const js = fs.readFileSync('assets/index-4NePqLyW.js', 'utf8');

const meIdx = js.indexOf('class me{');
console.log('Class me definition:');
console.log(js.substring(meIdx, meIdx + 1200));
