import fs from 'fs';

const files = fs.readdirSync('assets').filter(f => f.endsWith('.js') && !f.includes('index-') && !f.includes('shared-'));
console.log('Language files found:', files);

files.forEach(f => {
  const code = fs.readFileSync(`assets/${f}`, 'utf8');
  const hasStrings = code.includes('strings:');
  const lastExport = code.substring(code.lastIndexOf('export'));
  console.log(`- ${f}: has 'strings:'? ${hasStrings} | export: ${lastExport.trim()}`);
});
