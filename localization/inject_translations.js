import fs from 'fs';

const dict = JSON.parse(fs.readFileSync('localization/dictionary.json', 'utf8'));

const langFiles = [
  { file: 'assets/ar-SjO31DnI.js', varName: 'T', code: 'ar' },
  { file: 'assets/de-HYTLkJDz.js', varName: 'h', code: 'de' },
  { file: 'assets/es-C9vklYn6.js', varName: 'p', code: 'es' },
  { file: 'assets/fa.js', varName: 'fa', code: 'fa' },
  { file: 'assets/fr-QqmZdpVw.js', varName: 'c', code: 'fr' },
  { file: 'assets/he-Dd-kXJJK.js', varName: 'd', code: 'he' },
  { file: 'assets/hi-Bnsh4qCD.js', varName: 'i', code: 'hi' },
  { file: 'assets/id-CDETR5_t.js', varName: 'o', code: 'id' },
  { file: 'assets/ja-C4-8Cz_-.js', varName: 'r', code: 'ja' },
  { file: 'assets/ko-DmUagyds.js', varName: 'n', code: 'ko' },
  { file: 'assets/pt-J1dFf1-g.js', varName: 'c', code: 'pt' },
  { file: 'assets/tr-EKtCvHjH.js', varName: 'o', code: 'tr' },
  { file: 'assets/zh-DWvsr0s_.js', varName: 'r', code: 'zh' },
  { file: 'assets/zh-TW-CmWpn3k9.js', varName: 'r', code: 'zh-TW' }
];

for (const target of langFiles) {
  let content = fs.readFileSync(target.file, 'utf8');
  
  // Extract translations for this specific language
  const langTranslations = {};
  for (const [englishKey, translations] of Object.entries(dict)) {
    if (translations[target.code]) {
      langTranslations[englishKey] = translations[target.code];
    }
  }

  // Remove previous injection if any
  const marker = '// === EXPANDED_PROTOCOLS_TRANSLATIONS ===';
  if (content.includes(marker)) {
    content = content.substring(0, content.indexOf(marker)).trim() + '\n';
  }

  // Find the export statement
  let exportStmt = '';
  if (target.file === 'assets/fa.js') {
    exportStmt = 'export default fa;';
    content = content.replace('export default fa;', '').trim();
  } else {
    const exportRegex = new RegExp(`export\\s*\\{\\s*${target.varName}\\s+as\\s+default\\s*\\};?`);
    content = content.replace(exportRegex, '').trim();
    exportStmt = `export{${target.varName} as default};`;
  }

  const jsonPayload = JSON.stringify(langTranslations);
  const patch = `
${marker}
Object.assign(${target.varName}.strings, ${jsonPayload});
${exportStmt}
`;

  fs.writeFileSync(target.file, content + patch, 'utf8');
  console.log(`Updated ${target.file} (${target.code}) with ${Object.keys(langTranslations).length} translated keys.`);
}
