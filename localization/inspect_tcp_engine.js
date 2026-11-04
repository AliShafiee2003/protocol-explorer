import fs from 'fs';

const js = fs.readFileSync('assets/index-4NePqLyW.js', 'utf8');
const idx = js.indexOf('d=this.tcp(');
if (idx !== -1) {
  console.log(js.substring(idx - 200, idx + 400));
}

// Find tcp method in class
const tcpMethodIdx = js.indexOf('tcp(t,s,a,n,o,r){') !== -1 ? js.indexOf('tcp(t,s,a,n,o,r){') : js.indexOf('tcp(');
console.log('tcpMethodIdx:', tcpMethodIdx);
if (tcpMethodIdx !== -1) {
  console.log(js.substring(tcpMethodIdx, tcpMethodIdx + 800));
}
