import fs from 'fs';

const js = fs.readFileSync('assets/index-4NePqLyW.js', 'utf8');
const idx = js.indexOf('fi={id:"udp"');
const stepsIdx = js.indexOf('steps:[', idx);
console.log(js.substring(stepsIdx, stepsIdx + 1200));
