import fs from 'fs';

const dict = JSON.parse(fs.readFileSync('translations_fa.json', 'utf8'));

const code = `import { a as d } from "./shared-CAKwAg2C.js";

const strings = ${JSON.stringify(dict, null, 2)};

const patterns = [
  [/^([\\d,]+) bytes$/, "$1 بایت"],
  [/^(Ethernet II|IPv4|UDP|TCP) · (\\d+) bytes$/, "$1 · $2 بایت"],
  [/^(Application Data|Handshake|Change Cipher Spec), ([\\d,]+) bytes?$/, "$1، $2 بایت"],
  [/^([\\d,]+) bytes: report\\.pdf, bytes (.+)$/, "$1 بایت: report.pdf، بایت‌های $2"],
  [/^(.+) h later$/, "$1 ساعت بعد"],
  [/^(.+) min later$/, "$1 دقیقه بعد"],
  [/^(.+) s later$/, "$1 ثانیه بعد"],
  [/^(\\S+) \\(relative\\)$/, "$1 (نسبی)"],
  [/^(\\d+) \\(ephemeral\\)$/, "$1 (موقت)"],
  [/^(\\d+) TCP segments$/, (t, e) => \`\${e} سگمنت TCP\`],
  [/^(\\d+) segments$/, (t, e) => \`\${e} سگمنت\`],
  [/^(.*), (\\d+) segments$/, (t, e, s) => \`\${e}، \${s} سگمنت\`],
  [/^TLS 1\\.3 · (\\d+) records? · bytes (.+) of (.+)$/, (t, e, s, r) => \`TLS 1.3 · \${e} رکورد · بایت‌های \${s} از \${r}\`],
  [/^TLS 1\\.3 · (\\d+) records?$/, (t, e) => \`TLS 1.3 · \${e} رکورد\`],
  [/^Ethernet padding · (\\d+) bytes$/, "پدینگ اترنت · $1 بایت"],
  [/^(\\d+) zero bytes, up to the 300-byte minimum$/, "$1 بایت صفر، تا حداقل ۳۰۰ بایت"],
  [/^(\\d+) zero bytes$/, "$1 بایت صفر"],
  [/^(\\d+) random bytes$/, "$1 بایت تصادفی"],
  [/^Seen as it leaves (.+)$/, "مشاهده شده هنگام خروج از $1"],
  [/^Option (\\d+)$/, "گزینه $1"],
  [/^value (\\d+), echo (\\d+)$/, "مقدار $1، بازتاب $2"],
  [/^20 bytes, plus (\\d+) of options\\.$/, "۲۰ بایت، به همراه $1 بایت گزینه‌ها."],
  [/^Windows starts at (\\d+)\\. Set to (\\d+) on purpose here\\.$/, "ویندوز از $1 شروع می‌کند. اینجا عمداً روی $2 تنظیم شده است."],
  [/^Started at (\\d+); (\\d+) routers? on the way each took 1\\.$/, (t, e, s) => s === "1" ? \`با \${e} شروع شد؛ تنها روتر در مسیر ۱ واحد کاهش داد.\` : \`با \${e} شروع شد؛ هر کدام از \${s} روتر در مسیر ۱ واحد کاهش دادند.\`],
  [/^all (\\d+) bytes of it$/, "تمام $1 بایت آن"],
  [/^The packet that caused this, as the reporting device received it \\(TTL (\\d+)\\), so the sender can tell which packet it was\\.$/, "پکتی که باعث این پیام شد، همان‌طور که توسط دستگاه گزارش‌دهنده دریافت گردید (TTL $1)، تا فرستنده تشخیص دهد کدام پکت بوده است."],
  [/^Port (\\d+), TLS from the start$/, "پورت $1، با TLS از ابتدا"],
  [/^(\\d+), TLS from the start$/, "$1، با TLS از ابتدا"]
];

const fa = {
  strings,
  patterns,
  post: d
};

export default fa;
`;

fs.writeFileSync('assets/fa.js', code, 'utf8');
console.log('assets/fa.js generated successfully. File size:', Buffer.byteLength(code, 'utf8'));
