# -*- coding: utf-8 -*-
import json
import os

with open(r'D:\My_Script\NetWork-aap\chunk_2.json', 'r', encoding='utf-8') as f:
    chunk2 = json.load(f)

keys = list(chunk2.keys())
assert len(keys) == 260, f"Expected 260 keys, got {len(keys)}"

translations = {}

# 0-9
translations[keys[0]] = "دستور curl درخواست HTTP ۷۸ بایتی خود را ارسال می‌کند: بایت‌های ۱ تا ۷۸. شماره ACK سرور، ۷۹، بایت بعدی مورد انتظار آن است، به این معنی که تمام بایت‌های قبل از آن دریافت شده‌اند."
translations[keys[1]] = "ارسال شد"
translations[keys[2]] = "۷۹ = بایت بعدی مورد انتظار"
translations[keys[3]] = "دو سگمنت در پاسخ"
translations[keys[4]] = "یکی از آن‌ها گم می‌شود"
translations[keys[5]] = "سرور با ۲,۹۲۰ بایت پاسخ می‌دهد: دو سگمنت کاملِ ۱,۴۶۰ بایتی (حداکثر مقداری که در اینجا درون یک بسته جا می‌گیرد) که پشت سر هم ارسال می‌شوند. اولی در جایی از اینترنت دراپ (گم) می‌شود؛ دومی به مقصد می‌رسد."
translations[keys[6]] = "سگمنت ۱"
translations[keys[7]] = "بایت‌های ۱–۱۴۶۰ (از دست رفته)"
translations[keys[8]] = "سگمنت ۲"
translations[keys[9]] = "اندازه سگمنت"

# 10-19
translations[keys[10]] = "seq=1 و seq=1461"
translations[keys[11]] = "اولی از دست می‌رود"
translations[keys[12]] = "یک شکاف (داده مفقود) شناسایی شد"
translations[keys[13]] = "ACK تکراری همراه با SACK"
translations[keys[14]] = "بایت‌های ۱۴۶۱–۲۹۲۰ می‌رسند، اما ۱–۱۴۶۰ هرگز دریافت نشدند. یک ACK فقط می‌تواند بایت‌های دریافت شده به ترتیب را تأیید کند، بنابراین لپ‌تاپ بلافاصله ACK 1 را تکرار می‌کند و یک بلوک SACK اضافه می‌کند که نشان می‌دهد بایت‌های ۱۴۶۱–۲۹۲۰ را از قبل دریافت کرده است."
translations[keys[15]] = "۱ (همچنان در انتظار بایت ۱)"
translations[keys[16]] = "بایت‌های ۱۴۶۱–۲۹۲۰ را دارد"
translations[keys[17]] = "بلافاصله، بدون تأخیر"
translations[keys[18]] = "sack: شامل ۱۴۶۱–۲۹۲۰"
translations[keys[19]] = "ارسال مجدد شکاف (داده مفقود)"

# 20-29
translations[keys[20]] = "فقط بایت‌های مفقود"
translations[keys[21]] = "بلوک SACK دقیقاً به سرور اعلام می‌کند چه چیزی مفقود شده است، بنابراین سرور تنها سگمنت ۱ را مجدداً ارسال می‌کند و لپ‌تاپ همه داده‌ها را تأیید می‌نماید. اگر اصلاً هیچ ACKای دریافت نمی‌شد، تایمرها وارد عمل می‌شدند: یک پروب پس از حدود دو رفت‌وبرگشت (RTT)، و سپس مهلت زمانی بازترسالی یا RTO (حداقل ۲۰۰ میلی‌ثانیه در لینوکس)."
translations[keys[22]] = "مجدداً ارسال شد"
translations[keys[23]] = "فقط بایت‌های ۱–۱۴۶۰"
translations[keys[24]] = "ACK بعدی"
translations[keys[25]] = "۲۹۲۱ (همه بایت‌ها)"
translations[keys[26]] = "آنچه curl دریافت کرد"
translations[keys[27]] = "تمام بایت‌ها، مرتب و به ترتیب"
translations[keys[28]] = "فقط سگمنت مفقود"
translations[keys[29]] = "بستن اتصال"

# 30-39
translations[keys[30]] = "هر طرف پایان ارتباط را اعلام می‌کند"
translations[keys[31]] = "کار curl تمام شده است، بنابراین اتصال را می‌بندد. هر جهت به طور مستقل بسته می‌شود: لپ‌تاپ بسته FIN ارسال می‌کند و سرور آن را با ACK تأیید می‌نماید، سپس سرور بسته FIN خود را می‌فرستد و لپ‌تاپ آن را تأیید می‌کند. لپ‌تاپ جزئیات اتصال را برای مدتی نگه می‌دارد (TIME-WAIT)."
translations[keys[32]] = "بسته شده توسط"
translations[keys[33]] = "یک پیام FIN از هر طرف"
translations[keys[34]] = "ترتیب"
translations[keys[35]] = "سپس"
translations[keys[36]] = "لپ‌تاپ منتظر می‌ماند (TIME-WAIT)"
translations[keys[37]] = "داده‌ها"
translations[keys[38]] = "۱,۴۶۰ بایت: پاسخ HTTP، بایت‌های ۱–۱۴۶۰"
translations[keys[39]] = "۱,۴۶۰ بایت: پاسخ HTTP، بایت‌های ۱۴۶۱–۲۹۲۰"

# 40-49
translations[keys[40]] = "شامل ۱۴۶۱–۲۹۲۰ است"
translations[keys[41]] = "بایت‌هایی که بعد از شکاف رسیده‌اند، بنابراین فقط شکاف نیاز به ارسال مجدد دارد."
translations[keys[42]] = "دیتاگرام‌های سریع"
translations[keys[43]] = "صدای شما"
translations[keys[44]] = "صدای طرف مقابل"
translations[keys[45]] = "سرور مدیا (رسانه)"
translations[keys[46]] = "پروتکل UDP داده‌ها را در بسته‌های مستقلی به نام دیتاگرام (Datagram) ارسال می‌کند؛ بدون اتصال، بدون تأییدیه و بدون ارسال مجدد. این امر آن را سریع و سبک نگه می‌دارد: مناسب برای صوت، تصویر، بازی‌ها و DNS، جایی که پاسخی با تأخیر بدتر از پاسخی است که اصلاً نرسیده باشد."
translations[keys[47]] = "هیچ"
translations[keys[48]] = "هیچ (بدون ACK، بدون ارسال مجدد)"
translations[keys[49]] = "ترتیب بسته‌ها"

# 50-59
translations[keys[50]] = "تضمین نمی‌شود"
translations[keys[51]] = "تماس بدون وقفه جریان دارد"
translations[keys[52]] = "سریع، ساده، بدون تضمین"
translations[keys[53]] = "صدا با همان اولین پکت آغاز شد، هر دیتاگرام به طور مستقل مسیر را طی کرد، و آن بسته‌ای که گم شد به سادگی از دست رفت: UDP هرگز متوجه آن نشد. برنامه شکاف را جبران کرد و تماس ادامه یافت. برای مشاهده دوباره، دکمه بازپخش (REPLAY) را بزنید."
translations[keys[54]] = "دیتاگرام‌ها"
translations[keys[55]] = "۱۱ (۱ بسته گم شد، هرگز مجدداً ارسال نشد)"
translations[keys[56]] = "زمان راه‌اندازی"
translations[keys[57]] = "۰ میلی‌ثانیه (بدون دست‌تکانی)"
translations[keys[58]] = "نمایش داده شده"
translations[keys[59]] = "اولین ۰.۲ ثانیه از تماس"

# 60-69
translations[keys[60]] = "ارسال بلافاصله"
translations[keys[61]] = "بدون دست‌تکانی، داده‌ها ابتدا ارسال می‌شوند"
translations[keys[62]] = "برنامه تماس از زمان ورود به سیستم، آدرس و پورت سرور رسانه را می‌داند. بنابراین اتصالی برقرار نمی‌کند: اولین دیتاگرام بلافاصله حامل ۲۰ میلی‌ثانیه از صدای شما در پسِ یک هدر ۸ بایتی UDP است."
translations[keys[63]] = "راه‌اندازی"
translations[keys[64]] = "پورت‌ها"
translations[keys[65]] = "۹۲ بایت صوت، بدون راه‌اندازی"
translations[keys[66]] = "جریانی از دیتاگرام‌ها"
translations[keys[67]] = "هر ۲۰ میلی‌ثانیه یک بسته، هرکدام مستقل"
translations[keys[68]] = "برنامه در هر ۲۰ میلی‌ثانیه به ارسال یک دیتاگرام ادامه می‌دهد. هر کدام با هدر اختصاصی خود مستقل بوده و اتصالی به بقیه ندارد. پروتکل UDP آن‌ها را شماره‌گذاری نمی‌کند و هیچ پاسخی برای تأیید رسیدن آن‌ها بازنمی‌گردد."
translations[keys[69]] = "نرخ"

# 70-79
translations[keys[70]] = "۱ دیتاگرام در هر ۲۰ میلی‌ثانیه"
translations[keys[71]] = "شماره‌گذاری"
translations[keys[72]] = "در خود UDP وجود ندارد"
translations[keys[73]] = "تأییدیه"
translations[keys[74]] = "ندارد (بدون ACK)"
translations[keys[75]] = "فریم‌های صوتی ۲–۵"
translations[keys[76]] = "هرکدام با هدر ۸ بایتی اختصاصی خود"
translations[keys[77]] = "گم‌شده در مسیر"
translations[keys[78]] = "کسی آن را دوباره نمی‌فرستد"
translations[keys[79]] = "فریم ۷ در جایی از اینترنت دراپ (گم) می‌شود. سرور مدیا هرگز تقاضای آن را نمی‌کند و UDP نیز به لپ‌تاپ چیزی نمی‌گوید: هیچ تأییدیه‌ای وجود ندارد که منتظرش باشند. دیتاگرام‌های بعد از آن طبق روال عادی می‌رسند."

# 80-89
translations[keys[80]] = "گم‌شده (از دست رفته)"
translations[keys[81]] = "فریم صوتی شماره ۷"
translations[keys[82]] = "هرگز (بدون ACK)"
translations[keys[83]] = "مفقود"
translations[keys[84]] = "۲۰ میلی‌ثانیه صوت"
translations[keys[85]] = "فریم‌های صوتی ۶–۸"
translations[keys[86]] = "فریم ۷ گم شده است"
translations[keys[87]] = "پاسخ‌ها بازمی‌گردند"
translations[keys[88]] = "صدای طرف مقابل بازمی‌گردد"
translations[keys[89]] = "صدای مخاطب نیز به همان صورت، در قالب دیتاگرام‌های مجزا به پورت ۵۰۰۰۰ می‌رسد. بسته‌ها وارد می‌شوند چون روتر شما هنگام ترجمه آدرس شما (NAT)، پورت خروجی را در حافظه ثبت کرده است."

# 90-99
translations[keys[90]] = "جهت"
translations[keys[91]] = "مستقل از جهت ما"
translations[keys[92]] = "از طریق NAT"
translations[keys[93]] = "روتر پورت را به یاد دارد"
translations[keys[94]] = "صدای طرف مقابل"
translations[keys[95]] = "ارسال شده به پورت ۵۰۰۰۰"
translations[keys[96]] = "برنامه تصمیم می‌گیرد"
translations[keys[97]] = "قابلیت اطمینان بر عهده برنامه است"
translations[keys[98]] = "برنامه تماس فریم‌های خود را شماره‌گذاری می‌کند (پروتکل RTP این کار را انجام می‌دهد)، بنابراین متوجه می‌شود که فریم ۷ مفقود شده و به جای منتظر ماندن، وقفه ۲۰ میلی‌ثانیه‌ای را پنهان و هموار می‌کند. انتظار برای ارسال مجدد کل مکالمه را با تأخیر مواجه می‌کرد."
translations[keys[99]] = "وظیفه برنامه (مانند RTP)"

# 100-109
translations[keys[100]] = "اتلاف بسته (Loss)"
translations[keys[101]] = "توسط برنامه جبران (پنهان) می‌شود"
translations[keys[102]] = "همچنین بر بستر UDP"
translations[keys[103]] = "DNS، بازی‌ها، QUIC"
translations[keys[104]] = "نسخه و موارد دیگر"
translations[keys[105]] = "۲، بدون padding، بدون افزونه، بدون CSRC"
translations[keys[106]] = "مارکر (نشانگر)، نوع پی‌لود (Payload Type)"
translations[keys[107]] = "۱، ۱۱۱ (Opus، توافق‌شده هنگام راه‌اندازی تماس)"
translations[keys[108]] = "به ازای هر پکت یک شماره بالا می‌رود تا برنامه بتواند پکت‌های مفقود یا با تأخیر را تشخیص دهد."
translations[keys[109]] = "برچسب زمانی (Timestamp)"

# 110-119
translations[keys[110]] = "کلاک صوتی در ۴۸,۰۰۰ هرتز (در ثانیه): افزایش ۹۶۰ تیک به ازای هر فریم ۲۰ میلی‌ثانیه‌ای."
translations[keys[111]] = "این جریان صوتی را شناسایی می‌کند."
translations[keys[112]] = "صوت"
translations[keys[113]] = "۸۰ بایت صدای فشرده Opus (۲۰ میلی‌ثانیه)"
translations[keys[114]] = "۰، ۱۱۱ (Opus، توافق‌شده هنگام راه‌اندازی تماس)"
translations[keys[115]] = "آدرس‌دهی و مسیریابی"
translations[keys[116]] = "پکت خروجی"
translations[keys[117]] = "پاسخ"
translations[keys[118]] = "پروتکل IP به هر دستگاه یک آدرس می‌دهد و پکت‌ها را از شبکه‌ای به شبکه دیگر منتقل می‌کند. هر روتر تنها به آدرس مقصد نگاه می‌کند تا گام بعدی (Next Hop) را انتخاب نماید. پروتکل IP از نوع بهترین تلاش (Best-effort) است: هیچ قولی برای تحویل یا حفظ ترتیب نمی‌دهد؛ پروتکل TCP این قابلیت‌ها را روی آن اضافه می‌کند."
translations[keys[119]] = "شبکه (لایه ۳)"

# 120-129
translations[keys[120]] = "آدرس"
translations[keys[121]] = "در هر روتر ۱ واحد کاهش می‌یابد"
translations[keys[122]] = "تحویل"
translations[keys[123]] = "بهترین تلاش (Best-effort)"
translations[keys[124]] = "مسیر رفت و برگشت"
translations[keys[125]] = "۱۲ روتر در هر مسیر"
translations[keys[126]] = "لپ‌تاپ پکت را به روتر خود فرستاد و روتر آدرس عمومی خود را جایگزین آن کرد. در مجموع دوازده روتر تنها بر اساس آدرس مقصد بسته را هدایت کردند و پاسخ نیز به همین ترتیب مسیر برگشت را یافت. برای مشاهده دوباره، دکمه بازپخش (REPLAY) را فشار دهید."
translations[keys[127]] = "روترها"
translations[keys[128]] = "۱۲ روتر در هر مسیر (۱ روتر خانگی + ۱۱ روتر)"
translations[keys[129]] = "مقدار TTL در سرور"

# 130-139
translations[keys[130]] = "۱۱۶ (با مقدار اولیه ۱۲۸ ارسال شده بود)"
translations[keys[131]] = "بازنویسی‌شده توسط NAT"
translations[keys[132]] = "آدرس مبدأ در رفت، آدرس مقصد در برگشت"
translations[keys[133]] = "IPv4 (عملکرد IPv6 نیز مشابه است)"
translations[keys[134]] = "محلی یا غیرمحلی؟"
translations[keys[135]] = "مقایسه آدرس با ماسک زیرشبکه (ساب‌نت)"
translations[keys[136]] = "آدرس لپ‌تاپ 192.168.1.10 با ماسک 24/ است، بنابراین شبکه محلی آن از 192.168.1.0 تا 192.168.1.255 است. سرور با آدرس 203.0.113.10 خارج از این محدوده است، بنابراین پکت باید به گیت‌وی پیش‌فرض ارسال شود: روتر خانگی."
translations[keys[137]] = "لپ‌تاپ"
translations[keys[138]] = "محدوده محلی"
translations[keys[139]] = "گیت‌وی (Gateway)"

# 140-149
translations[keys[140]] = "یافتن روتر"
translations[keys[141]] = "پروتکل ARP آدرس IP را به MAC تبدیل می‌کند"
translations[keys[142]] = "در شبکه محلی، فریم‌ها بر اساس آدرس MAC تحویل داده می‌شوند. اگر مک‌آدرسِ روتر در کش ARP لپ‌تاپ نباشد، پیام همگانی (برودکست) «چه کسی 192.168.1.1 را دارد؟» ارسال می‌کند و روتر با آدرس MAC خود پاسخ می‌دهد."
translations[keys[143]] = "می‌پرسد"
translations[keys[144]] = "چه کسی 192.168.1.1 را دارد؟"
translations[keys[145]] = "ارسال شده به"
translations[keys[146]] = "همه (برودکست)"
translations[keys[147]] = "دریافت می‌کند (می‌آموزد)"
translations[keys[148]] = "آدرس MAC روتر"
translations[keys[149]] = "چه کسی 192.168.1.1 را دارد؟"

# 150-159
translations[keys[150]] = "به 192.168.1.10 اعلام کن"
translations[keys[151]] = "ارسال پکت"
translations[keys[152]] = "آدرس‌ها، TTL و پروتکل"
translations[keys[153]] = "هدر IP حاوی آدرس‌های مبدأ و مقصد، مقدار TTL و نوع پروتکل درون آن است. در اینجا حامل پیام TCP SYN به پورت ۴۴۳ است. ویندوز مقدار TTL را از ۱۲۸ آغاز می‌کند (لینوکس و macOS از ۶۴ استفاده می‌کنند)."
translations[keys[154]] = "مبدأ ← مقصد"
translations[keys[155]] = "مقدار TTL برابر ۱۲۸ · پروتکل TCP"
translations[keys[156]] = "ابتدا NAT، سپس گام به گام"
translations[keys[157]] = "روتر بازنویسی کرده و ارسال می‌کند"
translations[keys[158]] = "روتر آدرس خصوصی مبدأ را با آدرس عمومی خود 198.51.100.7 جایگزین می‌کند (و در اینجا پورت ۴۰۱۱۲ را به جای ۵۲۳۴۴ قرار می‌دهد)، این نگاشت را ذخیره کرده و TTL را به ۱۲۷ کاهش می‌دهد. سپس ۱۱ روتر در اینترنت، هرکدام گام بعدی را بر اساس آدرس مقصد انتخاب کرده و مجدداً یک واحد از TTL کم می‌کنند."
translations[keys[159]] = "مبدأ جدید"

# 160-169
translations[keys[160]] = "خروج از شبکه خانگی"
translations[keys[161]] = "در سمت سرور"
translations[keys[162]] = "مقدار TTL برابر ۱۱۶ (۱۱ گام دیگر)"
translations[keys[163]] = "مقدار TTL برابر ۱۲۷ · پس از NAT"
translations[keys[164]] = "پاسخ بازمی‌گردد"
translations[keys[165]] = "سرویس NAT آن را برای لپ‌تاپ ترجمه می‌کند"
translations[keys[166]] = "سرور به آدرسی که دریافت کرده پاسخ می‌دهد: 198.51.100.7:40112. روتر آن را در جدول NAT خود جستجو کرده، آدرس مقصد را مجدداً به 192.168.1.10:52344 تغییر می‌دهد و آن را هدایت می‌کند. پاسخ با TTL اولیه ۶۴ شروع شد و با مقدار ۵۲ می‌رسد."
translations[keys[167]] = "تحویل داده شد به"
translations[keys[168]] = "مقدار TTL برابر ۵۲ · پس از NAT"
translations[keys[169]] = "مقدار TTL برابر ۱۲۷ · 40112 → 443 [SYN] (پس از NAT)"

# 170-179
translations[keys[170]] = "مقدار TTL برابر ۵۲ · 443 → 52344 [SYN, ACK] (پس از NAT)"
translations[keys[171]] = "درخواست ARP · ۲۸ بایت"
translations[keys[172]] = "برودکست: تمام دستگاه‌های موجود در شبکه آن را دریافت می‌کنند."
translations[keys[173]] = "کارت شبکه فرستنده."
translations[keys[174]] = "نوع سخت‌افزار"
translations[keys[175]] = "نوع پروتکل"
translations[keys[176]] = "اندازه آدرس‌ها"
translations[keys[177]] = "عملیات (Operation)"
translations[keys[178]] = "۱ (درخواست: چه کسی ... را دارد؟)"
translations[keys[179]] = "آدرس MAC فرستنده"

# 180-189
translations[keys[180]] = "آدرس IP فرستنده"
translations[keys[181]] = "آدرس MAC هدف"
translations[keys[182]] = "تماماً صفر: این مقداری است که این درخواست به دنبال یافتن آن است."
translations[keys[183]] = "آدرس IP هدف"
translations[keys[184]] = "پاسخ ARP · ۲۸ بایت"
translations[keys[185]] = "مستقیماً به سمت دستگاهی که درخواست کرده بود بازمی‌گردد."
translations[keys[186]] = "۲ (پاسخ: ... در ... است)"
translations[keys[187]] = "همان‌طور که در حال خروج از سمت اینترنت روتر دیده می‌شود"
translations[keys[188]] = "روتر ارائه‌دهنده خدمات اینترنت (ISP)، گام بعدی."
translations[keys[189]] = "پورت روتر متصل به سمت اینترنت."

# 190-199
translations[keys[190]] = "طبق وضعیت ارسال: مقدار اولیه در این سیستم از ۶۴ شروع می‌شود."
translations[keys[191]] = "سرویس NAT روتر پورت خود را جایگزین پورت لپ‌تاپ کرده است."
translations[keys[192]] = "روتر بعدی فرستنده؛ هر گام بسته را درون یک فریم جدید قرار می‌دهد."
translations[keys[193]] = "تفکیک نام دامنه (Name Resolution)"
translations[keys[194]] = "پرس‌وجو (Query)"
translations[keys[195]] = "ارجاع (Referral)"
translations[keys[196]] = "در اینجا DNSSEC درخواست نشده است"
translations[keys[197]] = "سامانه DNS نام‌هایی مانند www.example.com را به آدرس‌های IP که کامپیوترها برای دسترسی به یکدیگر نیاز دارند تبدیل می‌کند. هیچ سرور واحدی تمام نام‌ها را نمی‌داند: این سیستم ساختاری سلسله‌مراتبی از سرورها دارد و پاسخ‌ها در طول مسیر کش می‌شوند تا اکثر جستجوها نیاز به رفتن به مسافت‌های دور نداشته باشند."
translations[keys[198]] = "پورت ۵۳، پروتکل UDP (در صورت بزرگی بسته، TCP)"
translations[keys[199]] = "تبدیل می‌کند"

# 200-209
translations[keys[200]] = "نام‌ها به آدرس‌های IP"
translations[keys[201]] = "سلسله‌مراتب"
translations[keys[202]] = "ریشه (Root) ← دامنه سطح‌بالا (TLD) ← معتبر (Authoritative)"
translations[keys[203]] = "کش کردن (ذخیره‌سازی موقت)"
translations[keys[204]] = "به مدت زمان TTL هر رکورد"
translations[keys[205]] = "نام تفکیک شد"
translations[keys[206]] = "و به مدت یک ساعت به یاد سپرده شد"
translations[keys[207]] = "ریزولور کار خود را با کش خالی شروع کرد و از ریشه (Root) به سمت com. و سپس به سرور اختصاصی example.com رفت و پاسخ را به لپ‌تاپ تحویل داد. تا زمانی که TTL منقضی نشود، جستجوی بعدی برای این نام مستقیماً از کش پاسخ داده می‌شود. برای مشاهده مجدد، دکمه بازپخش (REPLAY) را فشار دهید."
translations[keys[208]] = "پرس‌وجوها"
translations[keys[209]] = "۴ (لپ‌تاپ ۱، ریزولور ۳)"

# 210-219
translations[keys[210]] = "مدت ذخیره در کش"
translations[keys[211]] = "پرسش از ریزولور"
translations[keys[212]] = "لپ‌تاپ سؤال را واگذار می‌کند"
translations[keys[213]] = "مرورگر به آدرس IP سایت www.example.com نیاز دارد و نه مرورگر و نه ویندوز آن را در کش ندارند. لپ‌تاپ یک پرسش به ریزولور بازگشتی اختصاص‌یافته یعنی 8.8.8.8 ارسال می‌کند و از آن می‌خواهد کل جستجو را انجام دهد (Recursion Desired)."
translations[keys[214]] = "www.example.com، رکورد نوع A"
translations[keys[215]] = "مورد پرسش"
translations[keys[216]] = "8.8.8.8 (بازگشتی / Recursive)"
translations[keys[217]] = "RD (درخواست جستجوی بازگشتی)"
translations[keys[218]] = "پرچم‌ها: RD"
translations[keys[219]] = "مسیر com. را نشان می‌دهد"

# 220-229
translations[keys[220]] = "کش ریزولور خالی است (به تازگی راه‌اندازی شده)، بنابراین از بالاترین سطح شروع می‌کند. سرور ریشه آدرس IP را نمی‌داند، اما می‌داند کدام سرورها com. را مدیریت می‌کنند و با یک ارجاع پاسخ می‌دهد. بسیاری از ریزولورها فقط \"com\" را برای آن می‌فرستند، نه نام کامل را."
translations[keys[221]] = "سرورهای ریشه (Root Servers)"
translations[keys[222]] = "۱۳ نام سرور، بیش از ۱,۰۰۰ سایت Anycast"
translations[keys[223]] = "ارجاع (۱۳ سرور برای com.)"
translations[keys[224]] = "بدون پاسخ: از com. بپرسید"
translations[keys[225]] = "مسیر example.com را نشان می‌دهد"
translations[keys[226]] = "ریزولور از یکی از سرورهای com. می‌پرسد. آن‌ها نیز آدرس هر سایتی را در خود ندارند، اما می‌دانند هر دامنه com. از چه نیم‌سرورهایی استفاده می‌کند، بنابراین این پاسخ یک ارجاع دیگر است که آدرس آن سرورها (رکوردهای Glue) نیز پیوست آن شده است."
translations[keys[227]] = "می‌داند"
translations[keys[228]] = "نیم‌سرورهای دامنه‌های com."
translations[keys[229]] = "ارجاع + آدرس‌های چسبنده (Glue)"

# 230-239
translations[keys[230]] = "بدون پاسخ: از example.com بپرسید"
translations[keys[231]] = "پاسخ واقعی را ارائه می‌دهد"
translations[keys[232]] = "در نهایت ریزولور از نیم‌سرور اختصاصی example.com که رکوردهای دامنه را در اختیار دارد می‌پرسد. این سرور با رکورد A پاسخ می‌دهد و پاسخ را معتبر (Authoritative) علامت می‌زند. مالک دامنه مشخص می‌کند پاسخ چه مدت در کش بماند: در اینجا ۳۶۰۰ ثانیه."
translations[keys[233]] = "AA (معتبر)، TTL 3600"
translations[keys[234]] = "مقدار TTL برابر ۳۶۰۰ · پرچم AA"
translations[keys[235]] = "پاسخ و ذخیره در کش"
translations[keys[236]] = "لپ‌تاپ آدرس مورد نظر را دریافت می‌کند"
translations[keys[237]] = "ریزولور پاسخ را به لپ‌تاپ بازمی‌گرداند و یک نسخه را نگه می‌دارد. تا یک ساعت بعد می‌تواند به این نام بلافاصله پاسخ دهد، به همین دلیل جستجو در درس HTTP تنها ۲۴ میلی‌ثانیه طول کشید. لپ‌تاپ نیز آن را کش می‌کند."
translations[keys[238]] = "RD، RA (قابلیت بازگشتی در دسترس است)"
translations[keys[239]] = "کش‌شده توسط"

# 240-249
translations[keys[240]] = "ریزولور و لپ‌تاپ"
translations[keys[241]] = "پرچم‌ها: RD RA"
translations[keys[242]] = "ارجاع: 13× com. NS (با رکورد glue)"
translations[keys[243]] = "ارجاع: 2× example.com. NS (با رکورد glue)"
translations[keys[244]] = "پاسخ: رکورد A با آدرس 203.0.113.10 (معتبر / Authoritative)"
translations[keys[245]] = "طبق وضعیت ارسال: مقدار اولیه در این سیستم از ۱۲۸ شروع می‌شود."
translations[keys[246]] = "0x0000: پرس‌وجو (Query)"
translations[keys[247]] = "اندازه UDP برابر ۱۲۳۲، DNSSEC OK = 0"
translations[keys[248]] = "مشخص می‌کند که حداکثر اندازه پاسخ UDP چقدر می‌تواند باشد. برای کوتاه ماندن درس، در اینجا امضاهای DNSSEC درخواست نشده‌اند؛ اما یک ریزولور اعتبارسنج مانند 8.8.8.8 آن‌ها را درخواست می‌کند."
translations[keys[249]] = "0x8000: پاسخ (Response)"

# 250-259
translations[keys[250]] = "مرجعیت (Authority)"
translations[keys[251]] = "اطلاعات اضافی (Additional)"
translations[keys[252]] = "0x8400: پاسخ، با پرچم AA (معتبر / Authoritative)"
translations[keys[253]] = "دریافت آدرس IP"
translations[keys[254]] = "از طرف لپ‌تاپ"
translations[keys[255]] = "از طرف سرور DHCP"
translations[keys[256]] = "پروتکل پیکربندی پویای میزبان (DHCP)"
translations[keys[257]] = "پروتکل DHCP هر آنچه را که یک دستگاه برای استفاده از شبکه نیاز دارد در اختیارش می‌گذارد: یک آدرس IP، ماسک زیرشبکه (Subnet Mask)، روتر مسیر عبور ترافیک (Default Gateway)، و سرورهای DNS برای پاسخ‌گویی به پرس‌وجوها. آدرس‌ها برای مدت معینی اجاره داده می‌شوند (Lease) و مادامی که دستگاه در شبکه حضور داشته باشد، تمدید می‌شوند."
translations[keys[258]] = "پروتکل UDP پورت ۶۷ (سرور)، پورت ۶۸ (کلاینت)"
translations[keys[259]] = "تخصیص می‌دهد"

assert len(translations) == 260, f"Expected 260 translated items, got {len(translations)}"

# Check that keys match exactly
for i, k in enumerate(keys):
    assert k in translations, f"Missing key index {i}: {k}"

out_path = r'D:\My_Script\NetWork-aap\chunk_2_fa.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(translations, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {out_path} with {len(translations)} items.")
