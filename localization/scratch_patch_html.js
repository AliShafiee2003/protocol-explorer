import fs from 'fs';

let html = fs.readFileSync('index.html', 'utf8');

// Replace html tag
html = html.replace('<html lang="en">', '<html lang="fa" dir="rtl">');

// Remove strict CSP meta tag
html = html.replace(/<meta http-equiv="Content-Security-Policy"[^>]*>/i, '');

// Update title
html = html.replace(/<title>.*?<\/title>/i, '<title>کاوشگر پروتکل‌ها (Protocol Explorer) — آموزش نحوه کارکرد اینترنت</title>');

// Make asset links relative
html = html.replace(/href="\/assets\//g, 'href="./assets/');
html = html.replace(/src="\/assets\//g, 'src="./assets/');
html = html.replace(/href="\/favicon/g, 'href="./favicon');
html = html.replace(/href="\/apple-touch-icon/g, 'href="./apple-touch-icon');
html = html.replace(/href="\/site.webmanifest"/g, 'href="./site.webmanifest"');

fs.writeFileSync('index.html', html, 'utf8');
console.log('index.html updated successfully.');
