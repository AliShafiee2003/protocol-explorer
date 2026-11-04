import fs from 'fs';

let css = fs.readFileSync('assets/index-D7FMEo1m.css', 'utf8');

// Make existing font URLs relative: /assets/ -> ./
css = css.replace(/url\(\/assets\//g, 'url(./');

const vazirRules = `
@font-face{font-family:'Vazirmatn';font-weight:400;font-style:normal;font-display:swap;src:url(./Vazirmatn-Regular.woff2) format('woff2')}
@font-face{font-family:'Vazirmatn';font-weight:500;font-style:normal;font-display:swap;src:url(./Vazirmatn-Medium.woff2) format('woff2')}
@font-face{font-family:'Vazirmatn';font-weight:700;font-style:normal;font-display:swap;src:url(./Vazirmatn-Bold.woff2) format('woff2')}
[lang|=fa],[lang="fa"]{font-family:'Vazirmatn',Iosevka,-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
[lang|=fa] pre,[lang|=fa] code,[lang|=fa] .mono,[lang|=fa] .packet-byte,[lang|=fa] .wire-cell,[lang|=fa] .f-hex,[lang|=fa] .f-dec{font-family:Iosevka,'Vazirmatn',monospace}
`;

css += '\n' + vazirRules;

fs.writeFileSync('assets/index-D7FMEo1m.css', css, 'utf8');
console.log('assets/index-D7FMEo1m.css updated with Vazirmatn font rules.');
