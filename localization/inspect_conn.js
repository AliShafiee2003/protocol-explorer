import fs from 'fs';

const js = fs.readFileSync('assets/index-4NePqLyW.js', 'utf8');
const idx = js.indexOf('conn(t,s){');
if (idx !== -1) {
  console.log(js.substring(idx, idx + 600));
}
