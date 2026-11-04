import fs from 'fs';

const js = fs.readFileSync('assets/index-4NePqLyW.js', 'utf8');
let pos = 0;
while ((pos = js.indexOf('strings[', pos + 1)) !== -1) {
  console.log('--- FOUND strings[ ---');
  console.log(js.substring(pos - 150, pos + 250));
}
