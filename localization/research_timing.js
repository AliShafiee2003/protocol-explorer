import fs from 'fs';

const js = fs.readFileSync('assets/index-4NePqLyW.js', 'utf8');

const idx = js.indexOf('function Er(');
console.log('Er function:');
console.log(js.substring(idx, idx + 1000));
