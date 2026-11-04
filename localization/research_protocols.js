import fs from 'fs';

const js = fs.readFileSync('assets/index-4NePqLyW.js', 'utf8');

const idx = js.indexOf('function Lo(');
console.log('Function Lo definition:');
console.log(js.substring(idx, idx + 2000));
