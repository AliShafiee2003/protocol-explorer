import fs from 'fs';

const js = fs.readFileSync('assets/index-4NePqLyW.js', 'utf8');
let pos = 0;
while ((pos = js.indexOf('Xt.', pos + 1)) !== -1) {
  console.log(js.substring(pos - 30, pos + 200));
}
