import fs from 'fs';

const js = fs.readFileSync('assets/index-4NePqLyW.js', 'utf8');
let pos = 0;
while ((pos = js.indexOf('"fa"', pos + 1)) !== -1) {
  console.log(js.substring(pos - 50, pos + 120));
}
