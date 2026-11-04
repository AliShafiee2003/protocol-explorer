import fs from 'fs';

let js = fs.readFileSync('assets/index-4NePqLyW.js', 'utf8');

const target1 = 'Ht=[{code:"en",name:"English",short:"EN",html:"en"},';
const repl1 = 'Ht=[{code:"fa",name:"فارسی",short:"FA",html:"fa",dir:"rtl",load:()=>Oe(()=>import("./fa.js"),[])},{code:"en",name:"English",short:"EN",html:"en"},';

if (!js.includes(target1)) {
  console.error('Target 1 not found!');
  process.exit(1);
}

js = js.replace(target1, repl1);
console.log('Target 1 replaced successfully.');

const target2 = 'async function Ol(){let e=null;try{e=localStorage.getItem(mr)}catch{}e&&e!=="en"&&await wr(e,!1).catch(()=>{})}';
const repl2 = 'async function Ol(){let e="fa";try{e=localStorage.getItem(mr)||"fa"}catch{}e&&await wr(e,!1).catch(()=>{})}';

if (!js.includes(target2)) {
  console.error('Target 2 not found!');
  process.exit(1);
}

js = js.replace(target2, repl2);
console.log('Target 2 replaced successfully.');

fs.writeFileSync('assets/index-4NePqLyW.js', js, 'utf8');
console.log('assets/index-4NePqLyW.js updated successfully.');
