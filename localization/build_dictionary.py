# -*- coding: utf-8 -*-
import json

# Complete multilingual dictionary generator for all 15 languages:
# en, fa, ar, es, fr, de, tr, pt, id, ja, zh, zh-TW, ko, hi, he

def get_full_translations():
    t = {}

    def add(en, fa, ar, es, fr, de, tr, pt, id_, ja, zh, zh_tw, ko, hi, he):
        t[en] = {
            "fa": fa, "ar": ar, "es": es, "fr": fr, "de": de, "tr": tr,
            "pt": pt, "id": id_, "ja": ja, "zh": zh, "zh-TW": zh_tw,
            "ko": ko, "hi": hi, "he": he
        }

    # Protocol Names & Titles
    add("Hypertext Transfer Protocol Version 2",
        "پروتکل انتقال ابرمتن نسخه ۲ (HTTP/2)", "بروتوكول نقل النص التشعبي الإصدار 2",
        "Protocolo de transferencia de hipertexto versión 2", "Protocole de transfert hypertexte version 2",
        "Hypertext Transfer Protocol Version 2", "Hiper Metin Transfer Protokolü Versiyon 2",
        "Protocolo de Transferência de Hipertexto Versão 2", "Protokol Transfer Hiperteks Versi 2",
        "ハイパーテキスト転送プロトコル バージョン2", "超文本传输协议第2版", "超文本傳輸協定第2版",
        "하이퍼텍스트 전송 프로토콜 버전 2", "हाइपरटेक्स्ट ट्रांसफर प्रोटोकॉल संस्करण 2", "פרוטוקול העברת היפרטקסט גרסה 2")

    add("Multiplexed Binary Streams",
        "جریان‌های باینری چندگانه (Multiplexed)", "تدفقات ثنائية متعددة الإرسال",
        "Flujos binarios multiplexados", "Flux binaires multiplexés",
        "Multiplexierte Binär-Streams", "Çoklamalı İkili Akışlar",
        "Fluxos binários multiplexados", "Aliran Biner Termultipleks",
        "多重化されたバイナリストリーム", "多路复用二进制流", "多路複用二進位串流",
        "다중화된 바이너리 스트림", "मल्टीप्लेक्स बाइनरी स्ट्रीम्स", "ערוצים בינאריים מרובי ערוצים")

    add("HTTP/3 over QUIC",
        "پروتکل HTTP/3 بر بستر QUIC", "HTTP/3 عبر QUIC",
        "HTTP/3 sobre QUIC", "HTTP/3 sur QUIC",
        "HTTP/3 über QUIC", "QUIC üzerinden HTTP/3",
        "HTTP/3 sobre QUIC", "HTTP/3 melalui QUIC",
        "QUIC上のHTTP/3", "基于QUIC的HTTP/3", "基於QUIC的HTTP/3",
        "QUIC 기반 HTTP/3", "QUIC पर HTTP/3", "HTTP/3 על גבי QUIC")

    add("QUIC over UDP Evolution",
        "تکامل QUIC بر بستر UDP", "تطور QUIC عبر UDP",
        "Evolución de QUIC sobre UDP", "Évolution de QUIC sur UDP",
        "QUIC über UDP Evolution", "UDP üzerinden QUIC Evrimi",
        "Evolução do QUIC sobre UDP", "Evolusi QUIC melalui UDP",
        "UDP上のQUICの進化", "基于UDP的QUIC演进", "基於UDP的QUIC演進",
        "UDP 기반 QUIC의 진화", "UDP पर QUIC का विकास", "התפתחות QUIC על גבי UDP")

    add("WebSocket Protocol",
        "پروتکل وب‌سوکت (WebSocket)", "بروتوكول ويب سوكت",
        "Protocolo WebSocket", "Protocole WebSocket",
        "WebSocket-Protokoll", "WebSocket Protokolü",
        "Protocolo WebSocket", "Protokol WebSocket",
        "WebSocketプロトコル", "WebSocket协议", "WebSocket協定",
        "웹소켓 프로토콜", "वेबसॉकेट प्रोटोकॉल", "פרוטוקול ווב-סוקט")

    add("Bidirectional Full-Duplex Web Streams",
        "جریان‌های وب تمام دوطرفه (Full-Duplex)", "تدفقات ويب مزدوجة كاملة ثنائية الاتجاه",
        "Flujos web bidireccionales completos", "Flux web bidirectionnels simultanés",
        "Bidirektionale Voll-Duplex-Web-Streams", "Çift Yönlü Tam Çift Akışlar",
        "Fluxos web bidirecionais full-duplex", "Aliran Web Dua Arah Penuh",
        "双方向全二重Webストリーム", "双向全双工Web流", "雙向全雙工Web串流",
        "양방향 전이중 웹 스트림", "द्वि-दिशात्मक फुल-डुप्लेक्स वेब स्ट्रीम", "ערוצי רשת דו-כיווניים מלאים")

    add("Message Queuing Telemetry Transport",
        "پروتکل پیام‌رسانی تله‌متری اینترنت اشیاء (MQTT)", "بروتوكول نقل القياس عن بعد في قائمة انتظار الرسائل",
        "Transporte de telemetría de cola de mensajes", "Transport télémétrique de file d'attente de messages",
        "Message Queuing Telemetry Transport", "Mesaj Kuyruğu Telemetri Aktarımı",
        "Transporte de telemetria de enfileiramento de mensagens", "Message Queuing Telemetry Transport",
        "メッセージキューテレメトリトランスポート", "消息队列遥测传输", "訊息佇列遙測傳輸",
        "메시지 큐잉 텔레메트리 트랜스포트", "मैसेज कतार टेलीमेट्री ट्रांसपोर्ट", "פרוטוקול תור הודעות טלמטריה")

    add("Lightweight IoT Publish / Subscribe",
        "انتشار / اشتراک سبک اینترنت اشیاء", "نشر / اشتراك خفيف لإنترنت الأشياء",
        "Publicar / Suscribir ligero para IoT", "Publication / Abonnement léger pour l'IoT",
        "Leichtgewichtiges IoT Publish / Subscribe", "Hafif IoT Yayınla / Abone Ol",
        "Publicação / Assinatura leve para IoT", "Publikasi / Berlangganan IoT Ringan",
        "軽量なIoTパブリッシュ / サブスクライブ", "轻量级物联网发布/订阅", "輕量級物聯網發佈/訂閱",
        "경량 IoT 발행 / 구독", "हल्का IoT पब्लिश / सब्सक्राइब", "פרסום / מנוי קל משקל לאינטרנט של הדברים")

    add("Server-Sent Events",
        "رویدادهای ارسال‌شده از سرور (SSE)", "الأحداث المرسلة من الخادم",
        "Eventos enviados por el servidor", "Événements envoyés par le serveur",
        "Server-Sent Events", "Sunucu Tarafından Gönderilen Olaylar",
        "Eventos enviados pelo servidor", "Peristiwa yang Dikirim Server",
        "サーバー送信イベント", "服务器发送事件", "伺服器發送事件",
        "서버 전송 이벤트", "सर्वर-सेंट इवेंट्स", "אירועים שנשלחו מהשרת")

    add("Server-Sent Events Streaming",
        "استریم رویدادهای زنده از سمت سرور", "تدفق الأحداث المرسلة من الخادم",
        "Transmisión de eventos enviados por el servidor", "Diffusion d'événements envoyés par le serveur",
        "Server-Sent Events Streaming", "Sunucu Gönderimli Olay Akışı",
        "Transmissão de eventos enviados pelo servidor", "Streaming Peristiwa yang Dikirim Server",
        "サーバー送信イベントのストリーミング", "服务器发送事件流式传输", "伺服器發送事件串流傳輸",
        "서버 전송 이벤트 스트리밍", "सर्वर-सेंट इवेंट्स स्ट्रीमिंग", "הזרמת אירועים שנשלחו מהשרת")

    add("HTTP Chunked Transfer Encoding",
        "کدگذاری انتقال تکه‌تکه در HTTP (Chunked)", "ترميز النقل المجزأ في HTTP",
        "Codificación de transferencia fragmentada HTTP", "Codage de transfert fractionné HTTP",
        "HTTP Chunked Transfer Encoding", "HTTP Parçalı Transfer Kodlaması",
        "Codificação de transferência em pedaços HTTP", "Pengkodean Transfer Terpotong HTTP",
        "HTTPチャンク転送エンコーディング", "HTTP分块传输编码", "HTTP分塊傳輸編碼",
        "HTTP 청크 분할 전송 인코딩", "HTTP चंक्ड ट्रांसफर एन्कोडिंग", "קידוד העברה במקטעים ב-HTTP")

    add("Dynamic Chunked Streaming",
        "استریم پویا با تکه‌های داده", "تدفق مجزأ ديناميكي",
        "Transmisión dinámica por fragmentos", "Diffusion fractionnée dynamique",
        "Dynamisches Chunk-Streaming", "Dinamik Parçalı Akış",
        "Transmissão dinâmica em pedaços", "Streaming Potongan Dinamis",
        "動的チャンクストリーミング", "动态分块流传输", "動態分塊串流傳輸",
        "동적 청크 스트리밍", "गतिशील चंक्ड स्ट्रीमिंग", "הזרמת מקטעים דינמית")

    add("gRPC Remote Procedure Calls",
        "فراخوانی رویه از راه دور (gRPC)", "استدعاءات الإجراءات البعيدة gRPC",
        "Llamadas a procedimiento remoto gRPC", "Appels de procédure à distance gRPC",
        "gRPC Remote Procedure Calls", "gRPC Uzaktan Prosedür Çağrıları",
        "Chamadas de procedimento remoto gRPC", "Panggilan Prosedur Jarak Jauh gRPC",
        "gRPCリモートプロシージャコール", "gRPC远程过程调用", "gRPC遠端程序呼叫",
        "gRPC 원격 프로시저 호출", "gRPC रिमोट प्रक्रिया कॉल", "קריאות פרוצדורה מרוחקות gRPC")

    add("High-Performance RPC over HTTP/2",
        "ارتباط پرسرعت RPC بر بستر HTTP/2", "اتصال RPC عالي الأداء عبر HTTP/2",
        "RPC de alto rendimiento sobre HTTP/2", "RPC haute performance sur HTTP/2",
        "Hochleistungs-RPC über HTTP/2", "HTTP/2 üzerinden Yüksek Performanslı RPC",
        "RPC de alto desempenho sobre HTTP/2", "RPC Kinerja Tinggi melalui HTTP/2",
        "HTTP/2上の高性能RPC", "基于HTTP/2的高性能RPC", "基於HTTP/2的高效能RPC",
        "HTTP/2 기반 고성능 RPC", "HTTP/2 पर उच्च प्रदर्शन RPC", "קישוריות RPC עתירת ביצועים על גבי HTTP/2")

    # Step Titles & Subtitles
    add("TCP & TLS 1.3 Handshake",
        "دست‌تکانی TCP و TLS 1.3 با ALPN", "مصافحة TCP و TLS 1.3 مع ALPN",
        "Apretón de manos TCP y TLS 1.3 con ALPN", "Poignée de main TCP et TLS 1.3 avec ALPN",
        "TCP & TLS 1.3 Handshake mit ALPN", "ALPN ile TCP ve TLS 1.3 Tokalaşması",
        "Handshake TCP e TLS 1.3 com ALPN", "Jabat Tangan TCP & TLS 1.3 dengan ALPN",
        "ALPNを使用したTCP & TLS 1.3ハンドシェイク", "包含ALPN的TCP与TLS 1.3握手", "包含ALPN的TCP與TLS 1.3交握",
        "ALPN 기반 TCP 및 TLS 1.3 핸드셰이크", "ALPN के साथ TCP और TLS 1.3 हैंडशेक", "לחיצת יד TCP ו-TLS 1.3 עם ALPN")

    add("Establishes secure transport with h2 ALPN",
        "برقراری ارتباط امن با شناسه پروتکل h2", "إنشاء اتصال آمن مع تفاوض h2",
        "Establece transporte seguro con ALPN h2", "Établit un transport sécurisé avec h2 ALPN",
        "Sicherer Transport mit h2 ALPN", "h2 ALPN ile güvenli aktarım kurulur",
        "Estabelece transporte seguro com ALPN h2", "Membentuk transport aman dengan h2 ALPN",
        "h2 ALPNによる安全なトランスポート確立", "通过h2 ALPN协商建立安全传输", "透過h2 ALPN協商建立安全傳輸",
        "h2 ALPN을 통한 보안 전송 수립", "h2 ALPN के साथ सुरक्षित ट्रांसपोर्ट स्थापित", "הקמת תעבורה מאובטחת עם h2 ALPN")

    add("HTTP/2 Preface & SETTINGS",
        "دیباچه اتصال و فریم تنظیمات (SETTINGS)", "مقدمة اتصال HTTP/2 وإعدادات SETTINGS",
        "Prefacio de conexión y marco SETTINGS", "Préface de connexion et trame SETTINGS",
        "HTTP/2 Preface & SETTINGS-Frame", "HTTP/2 Ön Ek ve SETTINGS Çerçevesi",
        "Prefácio HTTP/2 e quadro SETTINGS", "Pembuka HTTP/2 & Frame SETTINGS",
        "HTTP/2プレフィックスとSETTINGSフレーム", "HTTP/2连接前缀与SETTINGS帧", "HTTP/2連線前綴與SETTINGS訊框",
        "HTTP/2 연결 서문 및 SETTINGS 프레임", "HTTP/2 प्रस्तावना और SETTINGS फ़्रेम", "פתיח חיבור ומסגרת SETTINGS ב-HTTP/2")

    add("Negotiates stream parameters and window sizes",
        "مذاکره پارامترهای استریم و اندازه پنجره‌ها", "التفاوض على معلمات التدفق وحجم النوافذ",
        "Negocia parámetros de flujo y tamaños de ventana", "Négocie les paramètres de flux et tailles de fenêtre",
        "Verhandelt Stream-Parameter und Fenstergrößen", "Akış parametrelerini ve pencere boyutlarını müzakere eder",
        "Negocia parâmetros de fluxo e tamanho das janelas", "Menegosiasikan parameter aliran dan ukuran jendela",
        "ストリームパラメータとウィンドウサイズをネゴシエーション", "协商流参数与窗口大小", "協商串流參數與視窗大小",
        "스트림 매개변수 및 윈도우 크기 협상", "स्ट्रीम पैरामीटर और विंडो आकार पर बातचीत", "משא ומתן על פרמטרי ערוץ וגודל חלונות")

    add("Multiplexed Streams (1, 3, 5)",
        "ارسال همزمان استریم‌های ۱، ۳ و ۵", "تدفقات متعددة متزامنة (1، 3، 5)",
        "Flujos multiplexados (1, 3, 5)", "Flux multiplexés (1, 3, 5)",
        "Multiplexierte Streams (1, 3, 5)", "Çoklamalı Akışlar (1, 3, 5)",
        "Fluxos multiplexados (1, 3, 5)", "Aliran Termultipleks (1, 3, 5)",
        "多重化ストリーム (1, 3, 5)", "多路复用流 (1, 3, 5)", "多路複用串流 (1, 3, 5)",
        "다중화된 스트림 (1, 3, 5)", "मल्टीप्लेक्स स्ट्रीम्स (1, 3, 5)", "ערוצים מרובים במקביל (1, 3, 5)")

    add("Client requests HTML, CSS, and Image simultaneously",
        "درخواست همزمان HTML، CSS و تصویر روی یک کانکشن", "العميل يطلب HTML و CSS وصورة في وقت واحد",
        "El cliente solicita HTML, CSS e imagen simultáneamente", "Le client demande HTML, CSS et image simultanément",
        "Client fordert HTML, CSS und Bild gleichzeitig an", "İstemci HTML, CSS ve Resmi aynı anda ister",
        "O cliente solicita HTML, CSS e imagem simultaneamente", "Klien meminta HTML, CSS, dan Gambar secara bersamaan",
        "クライアントがHTML、CSS、画像を同時にリクエスト", "客户端同时请求HTML、CSS与图片", "用戶端同時請求HTML、CSS與圖片",
        "클라이언트가 HTML, CSS 및 이미지를 동시에 요청", "क्लाइंट एक साथ HTML, CSS और इमेज का अनुरोध करता है", "הלקוח מבקש HTML, CSS ותמונה בו-זמנית")

    add("Server Interleaved Data & Packet Loss",
        "تداخل داده‌ها در سرور و گم‌شدن پکت استریم ۳", "تداخل بيانات الخادم وفقدان حزمة التدفق 3",
        "Datos intercalados del servidor y pérdida de paquetes", "Données entrelacées du serveur et perte de paquets",
        "Verschachtelte Serverdaten & Paketverlust", "Sunucu Araya Eklenen Veri ve Paket Kaybı",
        "Dados intercalados do servidor e perda de pacotes", "Data Terjalin Server & Kehilangan Paket",
        "サーバーのインターリーブデータとパケット損失", "服务端交错数据与数据包丢失", "伺服端交錯資料與封包遺失",
        "서버 인터리브 데이터 및 패킷 유실", "सर्वर इंटरलीव्ड डेटा और पैकेट हानि", "שילוב נתונים בשרת ואובדן חבילות")

    add("Stream 3 packet is dropped in transit",
        "بسته استریم ۳ (CSS) در طول مسیر شبکه گم می‌شود", "تم إسقاط حزمة التدفق 3 في مسار الشبكة",
        "El paquete del flujo 3 se descarta en tránsito", "Le paquet du flux 3 est abandonné en transit",
        "Paket von Stream 3 geht bei der Übertragung verloren", "Akış 3 paketi aktarım sırasında düştü",
        "O pacote do fluxo 3 é descartado em trânsito", "Paket aliran 3 hilang dalam perjalanan",
        "ストリーム3のパケットが転送中に喪失", "流3的数据包在传输中丢失", "串流3的封包在傳輸中遺失",
        "스트림 3 패킷이 전송 중 유실됨", "स्ट्रीम 3 का पैकेट रास्ते में छूट जाता है", "חבילת ערוץ 3 אובדת בדרך")

    add("TCP Head-of-Line Blocking",
        "مسدود شدن سر خط در TCP (Head-of-Line)", "حظر رأس الخط في بروتوكول TCP",
        "Bloqueo de cabeza de línea en TCP", "Blocage en tête de ligne TCP",
        "TCP Head-of-Line-Blocking", "TCP Sıra Başı Engellemesi (HoL)",
        "Bloqueio de início de fila TCP (HoL)", "Pemblokiran Head-of-Line TCP",
        "TCPヘッドオブラインブロッキング", "TCP队头阻塞 (Head-of-Line Blocking)", "TCP隊頭阻塞 (Head-of-Line Blocking)",
        "TCP 헤드 오브 라인 블로킹 (HoL)", "TCP हेड-ऑफ-लाइन ब्लॉकिंग", "חסימת ראש התור ב-TCP")

    add("Stream 5 is blocked until Stream 3 recovers",
        "استریم ۵ متوقف می‌ماند تا قطعه گمشده استریم ۳ بازیابی شود", "التدفق 5 محظور حتى يتعافى التدفق 3",
        "El flujo 5 se bloquea hasta que el flujo 3 se recupera", "Le flux 5 est bloqué jusqu'à récupération du flux 3",
        "Stream 5 ist blockiert, bis Stream 3 wiederhergestellt ist", "Akış 3 kurtarılana kadar Akış 5 engellenir",
        "O fluxo 5 fica bloqueado até o fluxo 3 se recuperar", "Aliran 5 diblokir hingga Aliran 3 pulih",
        "ストリーム3が回復するまでストリーム5がブロックされる", "流5被阻塞直到流3恢复", "串流5被阻塞直到串流3復原",
        "스트림 3이 복구될 때까지 스트림 5가 차단됨", "स्ट्रीम 3 के ठीक होने तक स्ट्रीम 5 अवरुद्ध रहता है", "ערוץ 5 נחסם עד לשחזור ערוץ 3")

    add("Stream Cancellation via RST_STREAM",
        "لغو فوری استریم با فریم RST_STREAM", "إلغاء التدفق عبر RST_STREAM",
        "Cancelación de flujo mediante RST_STREAM", "Annulation de flux via RST_STREAM",
        "Stream-Abbruch über RST_STREAM", "RST_STREAM ile Akış İptali",
        "Cancelamento de fluxo via RST_STREAM", "Pembatalan Aliran melalui RST_STREAM",
        "RST_STREAMによるストリームのキャンセル", "通过RST_STREAM取消流", "透過RST_STREAM取消串流",
        "RST_STREAM을 통한 스트림 취소", "RST_STREAM के माध्यम से स्ट्रीम रद्दीकरण", "ביטול ערוץ באמצעות RST_STREAM")

    add("Client cancels Stream 5 without closing TCP connection",
        "کلاینت بدون بستن اتصال TCP، استریم ۵ را متوقف می‌کند", "العميل يلغي التدفق 5 دون إغلاق اتصال TCP",
        "El cliente cancela el flujo 5 sin cerrar la conexión TCP", "Le client annule le flux 5 sans fermer la connexion TCP",
        "Client bricht Stream 5 ab, ohne die TCP-Verbindung zu schließen", "İstemci, TCP bağlantısını kapatmadan Akış 5'i iptal eder",
        "O cliente cancela o fluxo 5 sem fechar a conexão TCP", "Klien membatalkan Aliran 5 tanpa menutup koneksi TCP",
        "クライアントはTCP接続を閉じずにストリーム5をキャンセル", "客户端取消流5而无需关闭TCP连接", "用戶端取消串流5而無需關閉TCP連線",
        "클라이언트가 TCP 연결을 닫지 않고 스트림 5를 취소함", "क्लाइंट TCP कनेक्शन बंद किए बिना स्ट्रीम 5 रद्द करता है", "הלקוח מבטל את ערוץ 5 מבלי לסגור את חיבור ה-TCP")

    add("1-RTT QUIC Handshake",
        "دست‌تکانی ۱ دور گردشی (1-RTT) در QUIC", "مصافحة QUIC في 1-RTT",
        "Apretón de manos QUIC de 1-RTT", "Poignée de main QUIC en 1-RTT",
        "1-RTT QUIC-Handshake", "1-RTT QUIC Tokalaşması",
        "Handshake QUIC de 1-RTT", "Jabat Tangan QUIC 1-RTT",
        "1-RTT QUICハンドシェイク", "1-RTT QUIC握手", "1-RTT QUIC交握",
        "1-RTT QUIC 핸드셰이크", "1-RTT QUIC हैंडशेक", "לחיצת יד QUIC של 1-RTT")

    add("Cryptographic handshake completed over UDP in 1 RTT",
        "دست‌تکانی رمزنگاری بر بستر UDP تنها در یک رفت و برگشت", "اكتملت المصافحة المشفرة عبر UDP في رحلة واحدة",
        "Apretón criptográfico completado sobre UDP en 1 RTT", "Poignée de main cryptographique sur UDP en 1 RTT",
        "Kryptografischer Handshake über UDP in 1 RTT abgeschlossen", "Şifreli tokalaşma UDP üzerinden 1 RTT'de tamamlandı",
        "Handshake criptográfico concluído sobre UDP em 1 RTT", "Jabat tangan kriptografi selesai melalui UDP dalam 1 RTT",
        "暗号化ハンドシェイクがUDP上で1 RTTで完了", "基于UDP的加密握手在1-RTT内完成", "基於UDP的加密交握在1-RTT內完成",
        "UDP 기반 암호화 핸드셰이크가 1 RTT 만에 완료됨", "UDP पर 1 RTT में क्रिप्टोग्राफ़िक हैंडशेक पूरा", "לחיצת יד קריפטוגרפית הושלמה על גבי UDP ב-1 RTT")

    add("Concurrent QUIC Streams",
        "جریان‌های مستقل و موازی در QUIC", "تدفقات QUIC متزامنة ومستقلة",
        "Flujos QUIC concurrentes e independientes", "Flux QUIC simultanés et indépendants",
        "Gleichzeitige QUIC-Streams", "Eşzamanlı QUIC Akışları",
        "Fluxos QUIC simultâneos", "Aliran QUIC Simultan",
        "並行QUICストリーム", "并发QUIC数据流", "並發QUIC資料串流",
        "동시 QUIC 스트림", "समवर्ती QUIC स्ट्रीम्स", "ערוצי QUIC במקביל")

    add("Independent streams multiplexed over UDP datagrams",
        "جریان‌های کاملاً مستقل روی دیتagram‌های مجزای UDP", "تدفقات مستقلة مجمعة عبر مخططات بيانات UDP",
        "Flujos independientes multiplexados sobre datagramas UDP", "Flux indépendants multiplexés sur des datagrammes UDP",
        "Unabhängige Streams multiplexiert über UDP-Datagramme", "UDP datagramları üzerinden çoklanan bağımsız akışlar",
        "Fluxos independentes multiplexados sobre datagramas UDP", "Aliran independen termultipleks melalui datagram UDP",
        "UDPデータグラム上で多重化された独立ストリーム", "通过UDP数据报多路复用的独立数据流", "透過UDP資料報多路複用的獨立資料串流",
        "UDP 데이터그램을 통해 다중화된 독립 스트림", "UDP डेटाग्राम पर मल्टीप्लेक्स स्वतंत्र स्ट्रीम्स", "ערוצים עצמאיים על גבי חבילות נתונים של UDP")

    add("Stream 4 Loss (No HoL Blocking)",
        "گم‌شدن استریم ۴ (بدون مسدودی سر خط!)", "فقدان التدفق 4 (بدون حظر رأس الخط!)",
        "Pérdida del flujo 4 (¡Sin bloqueo HoL!)", "Perte du flux 4 (Aucun blocage HoL !)",
        "Verlust von Stream 4 (Kein HoL-Blocking!)", "Akış 4 Kaybı (HoL Engellemesi Yok!)",
        "Perda do fluxo 4 (Sem bloqueio HoL!)", "Kehilangan Aliran 4 (Tanpa Pemblokiran HoL!)",
        "ストリーム4喪失 (HoLブロッキングなし！)", "流4丢失 (无队头阻塞！)", "串流4遺失 (無隊頭阻塞！)",
        "스트림 4 유실 (HoL 차단 없음!)", "स्ट्रीम 4 हानि (कोई HoL ब्लॉकिंग नहीं!)", "אובדן ערוץ 4 (ללא חסימת ראש תור!)")

    add("Image packet lost with zero delay to HTML stream",
        "پکت تصویر گم شد اما استریم HTML بدون هیچ تاخیری پردازش می‌شود", "فقدت حزمة الصورة دون أي تأخير لتدفق HTML",
        "Paquete de imagen perdido con cero retraso en el flujo HTML", "Paquet d'image perdu sans aucun retard pour le flux HTML",
        "Bildpaket ging verloren ohne Verzögerung für den HTML-Stream", "Resim paketi kayboldu, HTML akışında sıfır gecikme",
        "Pacote de imagem perdido com atraso zero no fluxo HTML", "Paket gambar hilang tanpa penundaan untuk aliran HTML",
        "画像パケットが喪失してもHTMLストリームに遅延ゼロ", "图片数据包丢失但对HTML流零延迟", "圖片封包遺失但對HTML串流零延遲",
        "이미지 패킷이 유실되어도 HTML 스트림에는 지연 없음", "इमेज पैकेट खो गया पर HTML स्ट्रीम में शून्य देरी", "חבילת תמונה אבדה ללא עיכוב בערוץ ה-HTML")

    add("Independent Stream Retransmission",
        "ارسال مجدد مستقل استریم گمشده", "إعادة إرسال مستقلة للتدفق المفقود",
        "Retransmisión independiente del flujo", "Retransmission indépendante du flux",
        "Unabhängige Stream-Wiederholung", "Bağımsız Akış Yeniden Aktarımı",
        "Retransmissão independente de fluxo", "Transmisi Ulang Aliran Independen",
        "独立したストリームの再送信", "独立数据流重传", "獨立資料串流重傳",
        "독립적인 스트림 재전송", "स्वतंत्र स्ट्रीम पुनः प्रसारण", "שידור חוזר של ערוץ עצמאי")

    add("Only missing stream data is resent with new packet number",
        "فقط داده‌های گمشده با شماره پکت جدید دوباره ارسال می‌شوند", "يتم فقط إعادة إرسال بيانات التدفق المفقودة برقم حزمة جديد",
        "Solo los datos perdidos se reenvían con nuevo número de paquete", "Seules les données manquantes sont renvoyées avec un nouveau numéro",
        "Nur fehlende Daten werden mit neuer Paketnummer erneut gesendet", "Yalnızca eksik veri yeni bir paket numarasıyla yeniden gönderilir",
        "Apenas os dados ausentes são reenviados com novo número de pacote", "Hanya data hilang yang dikirim ulang dengan nomor paket baru",
        "欠落したストリームデータのみが新しいパケット番号で再送される", "仅丢失的数据使用新的包编号重新发送", "僅遺失的資料使用新的封包編號重新發送",
        "누락된 스트림 데이터만 새 패킷 번호로 다시 전송됨", "केवल छूटा हुआ डेटा नए पैकेट नंबर के साथ भेजा जाता है", "רק הנתונים החסרים נשלחים מחדש עם מספר חבילה חדש")

    add("Network Switch & Migration",
        "مهاجرت کانکشن هنگام تغییر شبکه (وای‌فای به 4G)", "تبديل الشبكة وترحيل الاتصال (Wi-Fi إلى 4G)",
        "Cambio de red y migración de conexión (Wi-Fi a 4G)", "Changement de réseau et migration (Wi-Fi vers 4G)",
        "Netzwerkwechsel & Verbindungsmigration", "Ağ Değişimi ve Bağlantı Taşıma (Wi-Fi'dan 4G'ye)",
        "Troca de rede e migração de conexão (Wi-Fi para 4G)", "Peralihan Jaringan & Migrasi Koneksi (Wi-Fi ke 4G)",
        "ネットワーク切り替えとコネクションマイグレーション", "网络切换与连接迁移 (Wi-Fi转4G)", "網路切換與連線遷移 (Wi-Fi轉4G)",
        "네트워크 전환 및 연결 마이그레이션 (Wi-Fi에서 4G로)", "नेटवर्क स्विच और कनेक्शन माइग्रेशन (Wi-Fi से 4G)", "החלפת רשת ונדידת חיבור (Wi-Fi ל-4G)")

    add("Connection persists across IP change from Wi-Fi to 4G",
        "اتصال با وجود تغییر IP بدون قطع ارتباط ادامه می‌یابد", "يستمر الاتصال عبر تغيير IP من Wi-Fi إلى 4G دون انقطاع",
        "La conexión persiste tras el cambio de IP de Wi-Fi a 4G", "La connexion persiste malgré le changement d'IP (Wi-Fi vers 4G)",
        "Verbindung bleibt trotz IP-Wechsel von Wi-Fi zu 4G bestehen", "Bağlantı, Wi-Fi'dan 4G'ye IP değişikliğine rağmen devam eder",
        "A conexão persiste através da alteração de IP do Wi-Fi para 4G", "Koneksi bertahan saat IP berubah dari Wi-Fi ke 4G",
        "Wi-Fiから4GへのIP変更時もコネクションが持続", "Wi-Fi切换至4G改变IP但连接依然保持", "Wi-Fi切換至4G改變IP但連線依然保持",
        "Wi-Fi에서 4G로 IP가 바뀌어도 연결이 끊기지 않고 유지됨", "Wi-Fi से 4G पर IP बदलने पर भी कनेक्शन बना रहता है", "החיבור נשמר בעת שינוי IP מ-Wi-Fi ל-4G")

    # WebSocket Steps
    add("WebSocket Upgrade Handshake",
        "دست‌تکانی ارتقا به وب‌سوکت", "مصافحة ترقية WebSocket",
        "Apretón de actualización de WebSocket", "Poignée de main de mise à niveau WebSocket",
        "WebSocket Upgrade-Handshake", "WebSocket Yükseltme Tokalaşması",
        "Handshake de atualização do WebSocket", "Jabat Tangan Peningkatan WebSocket",
        "WebSocketアップグレードハンドシェイク", "WebSocket升级握手", "WebSocket升級交握",
        "웹소켓 업그레이드 핸드셰이크", "वेबसॉकेट अपग्रेड हैंडशेक", "לחיצת יד שדרוג ל-WebSocket")

    add("HTTP/1.1 101 Switching Protocols upgrade",
        "ارتقای پروتکل با کد وضعیت ۱۰۱ سوئیچینگ", "ترقية البروتوكول مع كود الحالة 101",
        "Actualización con código de estado 101", "Mise à niveau avec le statut 101",
        "Upgrade über HTTP/1.1 101 Switching Protocols", "HTTP/1.1 101 Protokol Değişimi ile yükseltme",
        "Atualização HTTP/1.1 101 Switching Protocols", "Peningkatan HTTP/1.1 101 Switching Protocols",
        "HTTP/1.1 101 Switching Protocolsによるアップグレード", "HTTP/1.1 101 Switching Protocols协议升级", "HTTP/1.1 101 Switching Protocols協定升級",
        "HTTP/1.1 101 Switching Protocols 프로토콜 전환 업그레이드", "HTTP/1.1 101 स्विचिंग प्रोटोकॉल अपग्रेड", "שדרוג פרוטוקול עם קוד סטטוס 101")

    add("Client Masked Frame",
        "ارسال فریم ماسک‌شده از کلاینت", "إطار العميل المقنع بمفتاح",
        "Marco enmascarado del cliente", "Trame masquée du client",
        "Maskierter Client-Frame", "İstemci Maskeli Çerçevesi",
        "Quadro mascarado do cliente", "Frame Klien Termasker",
        "クライアントのマスクされたフレーム", "客户端掩码数据帧", "用戶端遮罩資料訊框",
        "클라이언트 마스킹 프레임", "क्लाइंट का मास्क किया गया फ़्रेम", "מסגרת לקוח ממוסכת")

    add("Client frame XOR-masked for proxy cache security",
        "ماسک کردن داده کلاینت با XOR جهت امنیت پراکسی‌ها", "تشفير بيانات العميل بواسطة XOR لأمان البروكسي",
        "Marco del cliente enmascarado con XOR para seguridad de proxy", "Trame du client masquée par XOR pour la sécurité du proxy",
        "Client-Frame mit XOR maskiert für Proxy-Sicherheit", "Proxy güvenliği için istemci çerçevesi XOR ile maskelenir",
        "Quadro do cliente mascarado com XOR para segurança do proxy", "Frame klien dimaskerkan XOR untuk keamanan cache proxy",
        "プロキシキャッシュセキュリティのためXORマスクされたフレーム", "客户端数据帧经XOR掩码以保障代理缓存安全", "用戶端資料訊框經XOR遮罩以保障代理快取安全",
        "프록시 캐시 보안을 위해 클라이언트 프레임에 XOR 마스킹 적용", "प्रॉक्सी सुरक्षा के लिए क्लाइंट फ़्रेम XOR-मास्क किया गया", "מסגרת הלקוח ממוסכת ב-XOR לאבטחת זיכרון מטמון")

    add("Server Unmasked Broadcast",
        "ارسال بدون ماسک داده از سمت سرور", "بث بيانات الخادم غير المقنعة",
        "Transmisión no enmascarada del servidor", "Diffusion non masquée du serveur",
        "Unmaskierter Server-Broadcast", "Sunucu Maskesiz Yayını",
        "Transmissão não mascarada do servidor", "Siaran Server Tanpa Masker",
        "サーバーの非マスクブロードキャスト", "服务端非掩码广播数据", "伺服端非遮罩廣播資料",
        "서버의 비마스킹 브로드캐스트", "सर्वर का अनमास्क प्रसारण", "שידור לא ממוסך מהשרת")

    add("Server pushes real-time event to client",
        "سرور رویداد بلادرنگ را بدون نیاز به درخواست به کلاینت می‌فرستد", "الخادم يرسل حدثًا فوريًا إلى العميل",
        "El servidor envía eventos en tiempo real al cliente", "Le serveur transmet des événements en direct au client",
        "Server sendet Echtzeit-Ereignisse an den Client", "Sunucu istemciye gerçek zamanlı olay gönderir",
        "O servidor envia eventos em tempo real para o cliente", "Server mendorong peristiwa waktu-nyata ke klien",
        "サーバーがクライアントへリアルタイムイベントをプッシュ", "服务器直接向客户端推送实时事件", "伺服器直接向用戶端推送即時事件",
        "서버가 클라이언트에게 실시간 이벤트를 직접 푸시", "सर्वर क्लाइंट को रीयल-टाइम इवेंट भेजता है", "השרת שולח אירוע בזמן אמת ללקוח")

    add("Heartbeat Ping Loss",
        "گم‌شدن پکت پینگ در بررسی سلامت اتصال", "فقدان حزمة Ping لفحص نبضات القلب",
        "Pérdida de ping en latido", "Perte du ping de battement de cœur",
        "Heartbeat Ping-Verlust", "Heartbeat Ping Kaybı",
        "Perda de ping do heartbeat", "Kehilangan Ping Detak Jantung",
        "ハートビートPing喪失", "心跳Ping包丢失", "心跳Ping封包遺失",
        "하트비트 Ping 유실", "दिल की धड़कन पिंग हानि", "אובדן חבילת פינג בדופק חיים")

    add("Ping packet lost, triggering heartbeat timeout",
        "پکت پینگ در مسیر گم شده و تایم‌اوت فعال می‌شود", "فقدت حزمة Ping مما تسبب في انتهاء المهلة",
        "El paquete ping se pierde y activa el tiempo de espera", "Paquet ping perdu déclenchant l'expiration du délai",
        "Ping-Paket verloren, löst Heartbeat-Timeout aus", "Ping paketi kayboldu, heartbeat zaman aşımını tetikledi",
        "Pacote ping perdido, disparando o tempo limite do heartbeat", "Paket ping hilang, memicu batas waktu detak jantung",
        "Pingパケットが喪失し、ハートビートタイムアウトが発生", "Ping数据包丢失，触发心跳超时检测", "Ping資料封包遺失，觸發心跳逾時檢測",
        "Ping 패킷이 유실되어 하트비트 타임아웃이 트리거됨", "पिंग पैकेट खो गया, जिससे टाइमआउट ट्रिगर हुआ", "חבילת פינג אבדה והפעילה פסק זמן")

    add("Backoff Reconnection & Clean Close",
        "تلاش مجدد هوشمند و بستن تمیز ارتباط", "إعادة الاتصال التلقائي والإغلاق النظيف",
        "Reconexión con retroceso y cierre limpio", "Reconnexion exponentielle et fermeture propre",
        "Backoff-Wiederverbindung & sauberer Abschluss", "Geri Çekilmeli Yeniden Bağlantı ve Temiz Kapanış",
        "Reconexão com recuo e fechamento limpo", "Koneksi Ulang Backoff & Penutupan Bersih",
        "バックオフ再接続と正常クローズ", "退避重连与正常关闭连接", "退避重連與正常關閉連線",
        "지수 백오프 재연결 및 정상 종료", "बैकऑफ़ पुनः कनेक्शन और सामान्य समापन", "חיבור מחדש מדורג וסגירה תקינה")

    add("Auto-reconnect followed by opcode 8 clean closure",
        "اتصال مجدد خودکار و پایان کار با کد ۱۰۰۰", "إعادة اتصال تلقائية ثم إغلاق نظيف بالرمز 1000",
        "Reconexión automática seguida de cierre limpio con código 1000", "Reconnexion automatique suivie d'une fermeture propre (code 1000)",
        "Automatische Wiederverbindung gefolgt von sauberem Schließen (Code 1000)", "Otomatik yeniden bağlanma ve ardından kod 1000 ile temiz kapanış",
        "Reconexão automática seguida de fechamento limpo com código 1000", "Koneksi ulang otomatis diikuti penutupan bersih opcode 8 (kode 1000)",
        "自動再接続とコード1000による正常終了", "自动重连后通过操作码8正常关闭 (代码1000)", "自動重連後透過操作碼8正常關閉 (代碼1000)",
        "자동 재연결 후 조작 코드 8(코드 1000)로 정상 종료", "ऑटो-पुनः कनेक्ट के बाद सामान्य समापन (कोड 1000)", "חיבור אוטומטי מחדש וסגירה תקינה עם קוד 1000")

    # MQTT Steps
    add("MQTT CONNECT & CONNACK",
        "اتصال حسگر و تاییدیه با بازیابی نشست", "اتصال الحساس وتأكيد الاتصال في MQTT",
        "CONNECT y CONNACK en MQTT", "CONNECT et CONNACK MQTT",
        "MQTT CONNECT & CONNACK", "MQTT CONNECT ve CONNACK",
        "MQTT CONNECT e CONNACK", "MQTT CONNECT & CONNACK",
        "MQTT CONNECTとCONNACK", "MQTT CONNECT与CONNACK", "MQTT CONNECT與CONNACK",
        "MQTT CONNECT 및 CONNACK", "MQTT CONNECT और CONNACK", "חיבור ואישור CONNECT ו-CONNACK ב-MQTT")

    add("Sensor connects with CleanSession=0 and Last Will",
        "حسگر با CleanSession=0 و پیام وصیت‌نامه متصل می‌شود", "الحساس يتصل مع CleanSession=0 والوصية الأخيرة",
        "El sensor se conecta con CleanSession=0 y última voluntad", "Le capteur se connecte avec CleanSession=0 et testament",
        "Sensor verbindet sich mit CleanSession=0 und Last Will", "Sensör CleanSession=0 ve Son Vasiyet ile bağlanır",
        "O sensor se conecta com CleanSession=0 e último testamento", "Sensor terhubung dengan CleanSession=0 dan Wasiat Terakhir",
        "センサーがCleanSession=0と遺言メッセージで接続", "传感器通过CleanSession=0与遗嘱消息发起连接", "感測器透過CleanSession=0與遺囑訊息發起連線",
        "센서가 CleanSession=0 및 유언 메시지와 함께 연결됨", "सेंसर CleanSession=0 और अंतिम वसीयत के साथ कनेक्ट होता है", "החיישן מתחבר עם CleanSession=0 וצוואה אחרונה")

    add("SUBSCRIBE to Commands",
        "اشتراک در موضوع دریافت دستورات", "الاشتراك في موضوع الأوامر",
        "SUSCRIBIRSE a comandos", "Abonnement aux commandes",
        "SUBSCRIBE auf Befehle", "Komutlara SUBSCRIBE",
        "SUBSCREVER para comandos", "BERLANGGANAN Perintah",
        "コマンドへのSUBSCRIBE", "订阅控制指令主题", "訂閱控制指令主題",
        "제어 명령 토픽 구독 (SUBSCRIBE)", "कमांड की सदस्यता लें", "הרשמה לקבלת פקודות (SUBSCRIBE)")

    add("Subscribes with QoS 1 acknowledgment",
        "اشتراک در سطح تضمین تحویل QoS 1", "الاشتراك مع تأكيد QoS 1",
        "Suscripción con confirmación de QoS 1", "Abonnement avec accusé de réception QoS 1",
        "Abonniert mit QoS 1 Bestätigung", "QoS 1 onayı ile abone olur",
        "Assina com confirmação de QoS 1", "Berlangganan dengan konfirmasi QoS 1",
        "QoS 1確認付きでサブスクライブ", "以QoS 1服务质量等级订阅并确认", "以QoS 1服務品質等級訂閱並確認",
        "QoS 1 확인 응답과 함께 구독 완료", "QoS 1 पावती के साथ सदस्यता", "הרשמה עם אישור QoS 1")

    add("QoS 1 PUBLISH & PUBACK Loss",
        "ارسال داده حسگر و گم‌شدن تاییدیه PUBACK", "نشر QoS 1 وفقدان تأكيد PUBACK",
        "PUBLICAR QoS 1 y pérdida de PUBACK", "PUBLISH QoS 1 et perte de PUBACK",
        "QoS 1 PUBLISH & PUBACK-Verlust", "QoS 1 PUBLISH ve PUBACK Kaybı",
        "PUBLICAR QoS 1 e perda de PUBACK", "PUBLISH QoS 1 & Kehilangan PUBACK",
        "QoS 1 PUBLISHとPUBACK喪失", "QoS 1发布与PUBACK丢失", "QoS 1發佈與PUBACK遺失",
        "QoS 1 발행 (PUBLISH) 및 PUBACK 유실", "QoS 1 PUBLISH और PUBACK हानि", "פרסום QoS 1 ואובדן אישור PUBACK")

    add("Sensor reading published, PUBACK dropped in network",
        "داده دما ارسال شد اما پاسخ تاییدیه در شبکه افتاد", "تم نشر قراءة الحساس وسقطت حزمة التأكيد",
        "Lectura del sensor publicada, PUBACK descartado en la red", "Relevé du capteur publié, PUBACK perdu sur le réseau",
        "Sensordaten gesendet, PUBACK im Netzwerk verloren", "Sensör verisi yayınlandı, ağda PUBACK düştü",
        "Leitura do sensor publicada, PUBACK descartado na rede", "Data sensor diterbitkan, PUBACK hilang di jaringan",
        "センサー測定値を送信したが、PUBACKがネットワークで欠落", "传感器遥测数据已发布，但PUBACK确认在网络中丢弃", "感測器遙測資料已發佈，但PUBACK確認在網路中丟棄",
        "센서 데이터를 발행했으나 네트워크에서 PUBACK이 드롭됨", "सेंसर डेटा भेजा गया, नेटवर्क में PUBACK छूट गया", "קריאת החיישן פורסמה, אישור PUBACK נשמט ברשת")

    add("DUP=1 Retransmission",
        "ارسال مجدد با فلگ پیام تکراری (DUP=1)", "إعادة الإرسال مع علامة DUP=1",
        "Retransmisión con DUP=1", "Retransmission avec DUP=1",
        "DUP=1 Wiederholung", "DUP=1 ile Yeniden Gönderim",
        "Retransmissão com DUP=1", "Transmisi Ulang DUP=1",
        "DUP=1による再送信", "携带DUP=1标志重新发送", "攜帶DUP=1標誌重新發送",
        "DUP=1 플래그를 통한 재전송", "DUP=1 पुनः प्रसारण", "שידור חוזר עם דגל DUP=1")

    add("Guaranteed delivery via retransmission with duplicate flag",
        "تضمین قطعی تحویل پیام با علامت‌گذاری بسته تکراری", "ضمان التسليم عبر إعادة الإرسال مع علامة التكرار",
        "Entrega garantizada mediante retransmisión con indicador de duplicado", "Livraison garantie par retransmission avec indicateur de doublon",
        "Garantierte Zustellung durch Wiederholung mit Duplikat-Flag", "Yinelenen bayrağıyla yeniden aktarım sayesinde garantili teslimat",
        "Entrega garantida via retransmissão com flag de duplicata", "Pengiriman terjamin melalui transmisi ulang dengan flag duplikat",
        "重複フラグ付き再送信による確実な配信保証", "通过附带重复标志的重发机制确保消息至少送达一次", "透過附帶重複標誌的重發機制確保訊息至少送達一次",
        "중복 플래그를 포함한 재전송으로 신뢰성 있는 메시지 전달 보장", "डुप्लिकेट फ़्लैग के साथ पुनः प्रसारण द्वारा डिलीवरी की गारंटी", "מסירה מובטחת באמצעות שידור חוזר עם דגל כפילות")

    add("Broker Last Will Broadcast",
        "انتشار پیام وصیت‌نامه توسط بروکر", "بث الوصية الأخيرة من الوسيط",
        "Transmisión de última voluntad del broker", "Diffusion du testament par le courtier",
        "Broker sendet Last Will", "Aracı Son Vasiyeti Yayınlar",
        "Transmissão do último testamento pelo broker", "Siaran Wasiat Terakhir oleh Broker",
        "ブローカーによる遺言メッセージ配信", "代理服务器广播遗言消息", "代理伺服器廣播遺言訊息",
        "브로커의 유언 메시지 (LWT) 브로드캐스트", "ब्रोकर द्वारा अंतिम वसीयत प्रसारण", "שידור צוואה אחרונה על ידי המתווך")

    add("Broker detects abrupt sensor failure and broadcasts LWT",
        "بروکر با قطعی ناگهانی حسگر، وصیت آن را به مشترکین می‌فرستد", "الوسيط يكتشف انقطاع الحساس المفاجئ ويبث وصيته",
        "El broker detecta desconexión abrupta y transmite LWT", "Le courtier détecte la déconnexion brutale et diffuse le LWT",
        "Broker bemerkt plötzlichen Ausfall und sendet LWT", "Aracı sensörün aniden koptuğunu algılar ve LWT yayınlar",
        "O broker detecta falha abrupta e transmite o LWT", "Broker mendeteksi kegagalan sensor dan menyiarkan LWT",
        "ブローカーがセンサーの突然の切断を検知しLWTを配信", "代理服务器检测到传感器异常掉线并向订阅者广播遗言", "代理伺服器檢測到感測器異常斷線並向訂閱者廣播遺言",
        "브로커가 센서의 비정상적 연결 끊김을 감지하고 LWT를 발행", "ब्रोकर अचानक विफलता का पता लगाता है और LWT प्रसारित करता है", "המתווך מזהה ניתוק פתאומי של החיישן ומפיץ את הצוואה")

    # SSE Steps
    add("SSE Stream Initiation",
        "برقراری ارتباط استریم رویدادها (SSE)", "بدء تدفق أحداث SSE",
        "Inicio de transmisión SSE", "Initialisation du flux SSE",
        "SSE-Stream-Initialisierung", "SSE Akış Başlatma",
        "Iniciação de fluxo SSE", "Inisiasi Aliran SSE",
        "SSEストリームの初期化", "SSE事件流建立", "SSE事件串流建立",
        "SSE 이벤트 스트림 연결 시작", "SSE स्ट्रीम की शुरुआत", "הקמת ערוץ אירועים של SSE")

    add("HTTP GET with text/event-stream response",
        "درخواست با هدر text/event-stream و پاسخ ۲۰۰", "طلب HTTP GET مع استجابة text/event-stream",
        "HTTP GET con respuesta text/event-stream", "HTTP GET avec réponse text/event-stream",
        "HTTP GET mit text/event-stream Antwort", "text/event-stream yanıtı ile HTTP GET",
        "HTTP GET com resposta text/event-stream", "HTTP GET dengan respons text/event-stream",
        "text/event-streamレスポンス伴うHTTP GET", "带有text/event-stream响应的HTTP GET", "帶有text/event-stream回應的HTTP GET",
        "text/event-stream 응답을 수신하는 HTTP GET 요청", "text/event-stream प्रतिक्रिया के साथ HTTP GET", "בקשת HTTP GET עם תגובת text/event-stream")

    add("Real-Time Event Stream",
        "استریم بلادرنگ داده‌های رویداد", "تدفق الأحداث الفوري",
        "Flujo de eventos en tiempo real", "Flux d'événements en direct",
        "Echtzeit-Ereignis-Stream", "Gerçek Zamanlı Olay Akışı",
        "Fluxo de eventos em tempo real", "Aliran Peristiwa Real-Time",
        "リアルタイムイベントストリーム", "实时事件流传输", "即時事件串流傳輸",
        "실시간 이벤트 스트림", "रीयल-टाइम इवेंट स्ट्रीम", "ערוץ אירועים בזמן אמת")

    add("Server pushes structured events with ID and data",
        "سرور رویدادهای ساختاریافته شامل شناسه و داده می‌فرستد", "الخادم يرسل أحداثًا منظمة مع المعرف والبيانات",
        "El servidor envía eventos estructurados con ID y datos", "Le serveur envoie des événements structurés avec ID et données",
        "Server sendet strukturierte Ereignisse mit ID und Daten", "Sunucu kimlik ve veri içeren yapılandırılmış olaylar gönderir",
        "O servidor envia eventos estruturados com ID e dados", "Server mendorong peristiwa terstruktur dengan ID dan data",
        "サーバーがIDとデータを持つ構造化イベントを送信", "服务器向客户端持续推送包含ID与数据体的结构化事件", "伺服器向用戶端持續推送包含ID與資料體的結構化事件",
        "서버가 ID와 데이터가 포함된 구조화된 이벤트를 연속 푸시", "सर्वर आईडी और डेटा के साथ संरचित इवेंट भेजता है", "השרת שולח אירועים מובנים עם מזהה ונתונים")

    add("Proxy Idle Drop",
        "قطع اتصال ساکت توسط پراکسی میانی", "قطع الاتصال الخامل عبر البروكسي",
        "Caída por inactividad del proxy", "Coupure de proxy pour inactivité",
        "Proxy-Leerlaufabbruch", "Ara Sunucu Boşta Kalma Kesintisi",
        "Queda por inatividade do proxy", "Pemutusan Sambungan Diam Proxy",
        "プロキシによるアイドル切断", "代理服务器空闲超时中断", "代理伺服器閒置逾時中斷",
        "프록시 유휴 상태 타임아웃 연결 끊김", "प्रॉक्सी निष्क्रिय ड्रॉप", "ניתוק חיבור לא פעיל על ידי פרוקסי")

    add("Middlebox drops idle connection",
        "تجهیزات میانی شبکه کانکشن بدون تبادل را می‌بندند", "الجهاز الوسيط يسقط الاتصال الخامل",
        "El intermediario descarta la conexión inactiva", "L'équipement intermédiaire abandonne la connexion inactive",
        "Middlebox trennt inaktive Verbindung", "Ağ aygıtı boşta duran bağlantıyı sonlandırır",
        "O intermediário descarta a conexão inativa", "Perangkat perantara memutuskan koneksi yang menganggur",
        "中間ネットワーク機器がアイドル接続を切断", "网络中间件主动断开空闲超时的长连接", "網路中介軟體主動斷開閒置逾時的長連線",
        "네트워크 중간 장비가 유휴 상태인 연결을 강제 종료", "मिडिलबॉक्स निष्क्रिय कनेक्शन समाप्त करता है", "רכיב רשת סוגר חיבור לא פעיל")

    add("EventSource Auto-Resume",
        "بازیابی هوشمند و خودکار با شناسه رویداد", "استئناف تلقائي عبر EventSource",
        "Reanudación automática con EventSource", "Reprise automatique avec EventSource",
        "Automatisches Fortsetzen mit EventSource", "EventSource Otomatik Devam Etme",
        "Retomada automática com EventSource", "Lanjutan Otomatis EventSource",
        "EventSourceによる自動再開", "EventSource自动断点续传", "EventSource自動斷點續傳",
        "EventSource 자동 재개 및 복구", "EventSource स्वचालित पुनरारंभ", "חידוש אוטומטי באמצעות EventSource")

    add("Native reconnect resuming from Last-Event-ID: 101",
        "اتصال مجدد خودکار مرورگر از آخرین شناسه دریافت شده", "إعادة اتصال تلقائية واستئناف من Last-Event-ID: 101",
        "Reconexión nativa reanudando desde Last-Event-ID: 101", "Reconnexion native reprenant à Last-Event-ID : 101",
        "Automatische Wiederverbindung ab Last-Event-ID: 101", "Last-Event-ID: 101 ile yerel otomatik yeniden bağlanma",
        "Reconexão nativa retomando a partir de Last-Event-ID: 101", "Koneksi ulang native melanjutkan dari Last-Event-ID: 101",
        "Last-Event-ID: 101からブラウザが自動再開", "浏览器原生重连并携带Last-Event-ID: 101恢复传输", "瀏覽器原生重連並攜帶Last-Event-ID: 101恢復傳輸",
        "브라우저가 Last-Event-ID: 101 헤더와 함께 자동으로 연결 복구", "Last-Event-ID: 101 से मूल पुनः कनेक्शन", "חידוש אוטומטי בדפדפן ממזהה Last-Event-ID: 101")

    # Chunked Steps
    add("Chunked Transfer Request",
        "درخواست دریافت محتوا با تکه‌بندی پویا", "طلب نقل البيانات المجزأة",
        "Solicitud de transferencia fragmentada", "Demande de transfert fractionné",
        "Chunked-Transfer-Anfrage", "Parçalı Transfer Talebi",
        "Requisição de transferência em pedaços", "Permintaan Transfer Terpotong",
        "チャンク転送リクエスト", "分块传输请求", "分塊傳輸請求",
        "청크 분할 전송 요청", "चंक्ड ट्रांसफर अनुरोध", "בקשת העברה במקטעים")

    add("Response with Transfer-Encoding: chunked",
        "پاسخ سرور با مشخصه Transfer-Encoding: chunked", "استجابة الخادم مع Transfer-Encoding: chunked",
        "Respuesta con Transfer-Encoding: chunked", "Réponse avec Transfer-Encoding : chunked",
        "Antwort mit Transfer-Encoding: chunked", "Transfer-Encoding: chunked içeren yanıt",
        "Resposta com Transfer-Encoding: chunked", "Respons dengan Transfer-Encoding: chunked",
        "Transfer-Encoding: chunkedを含むレスポンス", "带有Transfer-Encoding: chunked响应头", "帶有Transfer-Encoding: chunked回應標頭",
        "Transfer-Encoding: chunked 헤더가 포함된 서버 응답", "Transfer-Encoding: chunked के साथ उत्तर", "תגובה עם Transfer-Encoding: chunked")

    add("Hex-Sized Data Chunks",
        "ارسال تکه‌های داده با طول هگزادسیمال", "إرسال أجزاء البيانات بالأحجام السداسية",
        "Fragmentos de datos con tamaño hexadecimal", "Morceaux de données dimensionnés en hexadécimal",
        "Hex-formatierte Daten-Chunks", "Onaltılık Boyutlu Veri Parçaları",
        "Blocos de dados com tamanho hexadecimal", "Potongan Data Berukuran Heksadesimal",
        "16進数サイズ指定のデータチャンク", "十六进制长度标记的数据块", "十六進位長度標記的資料塊",
        "16진수 크기 표기 데이터 청크 전송", "हेक्स-आकार के डेटा चंक्स", "מקטעי נתונים בגודל הקסדצימלי")

    add("Server streams data without upfront Content-Length",
        "سرور داده‌ها را بدون مشخص بودن حجم کل استریم می‌کند", "الخادم يرسل البيانات دون معرفة الحجم الكلي مسبقًا",
        "El servidor transmite sin Content-Length previo", "Le serveur transmet sans Content-Length préalable",
        "Server streamt Daten ohne vorab bekanntes Content-Length", "Sunucu önceden Content-Length olmadan veri akışı sağlar",
        "O servidor transmite dados sem Content-Length prévio", "Server mengalirkan data tanpa Content-Length di awal",
        "サーバーは事前のContent-Lengthなしでデータをストリーミング", "服务端在未知Content-Length的情况下即时流式输出数据", "伺服端在未知Content-Length的情況下即時串流輸出資料",
        "서버가 전체 크기를 미리 알지 못해도 데이터를 실시간 스트리밍", "सर्वर बिना Content-Length के डेटा स्ट्रीम करता है", "השרת מזרים נתונים ללא הגדרת Content-Length מראש")

    add("Intermediate Chunk Loss",
        "گم‌شدن تکه‌ای از داده در میانه راه", "فقدان جزء من البيانات في المنتصف",
        "Pérdida de fragmento intermedio", "Perte d'un morceau intermédiaire",
        "Zwischenzeitlicher Chunk-Verlust", "Ara Parça Kaybı",
        "Perda de bloco intermediário", "Kehilangan Potongan Menengah",
        "中間チャンクの喪失", "传输途中中间数据块丢失", "傳輸途中中間資料塊遺失",
        "중간 데이터 청크 유실", "मध्यवर्ती चंक् हानि", "אובדן מקטע נתונים באמצע הדרך")

    add("Lost chunk recovered by TCP transport",
        "قطعه گمشده با ارسال مجدد در لایه TCP بازیابی می‌شود", "استعادة الجزء المفقود عبر طبقة نقل TCP",
        "Fragmento perdido recuperado por transporte TCP", "Morceau perdu récupéré par la couche de transport TCP",
        "Verlorener Chunk durch TCP wiederhergestellt", "Kaybolan parça TCP aktarımı ile kurtarıldı",
        "Bloco perdido recuperado pelo transporte TCP", "Potongan hilang dipulihkan oleh transport TCP",
        "喪失したチャンクがTCPトランスポートによって復旧", "丢失的数据块通过TCP传输层自动重传恢复", "遺失的資料塊透過TCP傳輸層自動重傳復原",
        "유실된 청크가 TCP 전송 계층 재전송을 통해 복구됨", "छूटा हुआ चंक् TCP द्वारा पुनर्प्राप्त", "המקטע שאבד שוחזר באמצעות תעבורת TCP")

    add("Mid-Stream Database Abort",
        "توقف ناگهانی استریم در پی خطای پایگاه‌داده", "انقطاع البث في المنتصف بسبب خطأ قاعدة البيانات",
        "Aborto de flujo por error de base de datos", "Interruption du flux pour erreur de base de données",
        "Abbruch mitten im Stream bei Datenbankfehler", "Veritabanı Hatasıyla Akışın Kesilmesi",
        "Interrupção no meio do fluxo por erro no banco de dados", "Pembatalan Tengah Aliran Akibat Database",
        "データベースエラーによるストリーム中断", "数据库致命错误引发中途连接重置", "資料庫嚴重錯誤引發中途連線重設",
        "데이터베이스 치명적 에러로 인한 중간 스트림 중단", "डेटाबेस त्रुटि के कारण बीच में स्ट्रीम रद्द", "ביטול באמצע הזרמה בשל שגיאת מסד נתונים")

    add("Server tears down connection on fatal streaming error",
        "سرور با ارسال TCP RST ارتباط را بلافاصله ابطال می‌کند", "الخادم ينهي الاتصال عبر TCP RST عند حدوث خطأ فادح",
        "El servidor corta la conexión con TCP RST ante error fatal", "Le serveur interrompt la connexion avec TCP RST en cas d'erreur fatale",
        "Server beendet Verbindung mit TCP RST bei schwerem Fehler", "Sunucu kritik akış hatasında TCP RST ile bağlantıyı keser",
        "O servidor encerra a conexão com TCP RST em caso de erro fatal", "Server memutuskan koneksi dengan TCP RST saat terjadi kesalahan fatal",
        "致命的なエラー時にサーバーがTCP RSTで接続を強制切断", "遇到不可恢复异常时服务端主动发送TCP RST中断通信", "遇到不可復原異常時伺服端主動發送TCP RST中斷通訊",
        "복구 불가능한 에러 발생 시 서버가 TCP RST로 연결을 강제 리셋", "गंभीर त्रुटि पर सर्वर TCP RST भेजकर कनेक्शन समाप्त करता है", "השרת מנתק את החיבור עם TCP RST בעת שגיאה קריטית")

    add("Terminal Zero Chunk & Trailer",
        "پایان استریم با قطعه صفر و هدرهای پایانی", "الجزء الصفري النهائي ورؤوس المقطورة",
        "Fragmento cero terminal y encabezados finales", "Morceau terminal zéro et en-têtes finaux",
        "Terminaler Null-Chunk & Trailer", "Son Sıfır Parçası ve Artbilgi",
        "Bloco zero terminal e cabeçalhos finais", "Potongan Nol Akhir & Trailer",
        "終端ゼロチャンクとトレイラーヘッダー", "终止零块与尾部校验标头", "終止零塊與尾部校驗標頭",
        "종료 알림 0 청크 및 트레일러 헤더", "टर्मिनल शून्य चंक् और ट्रेलर", "מקטע אפס סופי וכותרות סיום")

    add("Stream ends with 0\\r\\n and cryptographic checksum",
        "پایان جریان با 0\\r\\n و چکسام رمزنگاری SHA256", "انتهاء التدفق مع 0\\r\\n والمجموع الاختباري المشفر",
        "El flujo finaliza con 0\\r\\n y suma de verificación criptográfica", "Le flux se termine par 0\\r\\n et somme de contrôle cryptographique",
        "Stream endet mit 0\\r\\n und kryptografischer Prüfsumme", "Akış 0\\r\\n ve kriptografik sağlama toplamı ile biter",
        "O fluxo termina com 0\\r\\n e soma de verificação criptográfica", "Aliran berakhir dengan 0\\r\\n dan checksum kriptografi",
        "0\\r\\nと暗号化チェックサムでストリーム完了", "数据流以0\\r\\n终止并附带SHA256加密校验和", "資料串流以0\\r\\n終止並附帶SHA256加密校驗和",
        "스트림이 0\\r\\n 및 SHA256 암호화 체크섬과 함께 완전히 종료됨", "स्ट्रीम 0\\r\\n और क्रिप्टोग्राफ़िक चेकसम के साथ समाप्त होती है", "הזרמה מסתיימת ב-0\\r\\n ובדיקת סיכום קריפטוגרפית")

    # gRPC Steps
    add("Unary gRPC Request",
        "درخواست فراخوانی تکی روش در gRPC", "طلب gRPC أحادي",
        "Solicitud gRPC unaria", "Requête gRPC unitaire",
        "Unäre gRPC-Anfrage", "Tekil gRPC Talebi (Unary)",
        "Requisição gRPC unária", "Permintaan gRPC Tunggal",
        "単一gRPCリクエスト (Unary RPC)", "gRPC一元调用请求", "gRPC一元呼叫請求",
        "gRPC 단일 호출 요청 (Unary RPC)", "एकल gRPC अनुरोध", "בקשת gRPC יחידה (Unary)")

    add("POST /OrderService/GetOrder with Protobuf payload",
        "ارسال متد با پی‌لود باینری پروتکل بافرز (Protobuf)", "إرسال الطلب مع حمولة ثنائية Protocol Buffers",
        "POST /OrderService/GetOrder con carga binaria Protobuf", "POST /OrderService/GetOrder avec charge utile binaire Protobuf",
        "POST /OrderService/GetOrder mit Protobuf-Nutzlast", "Protobuf yükü ile POST /OrderService/GetOrder",
        "POST /OrderService/GetOrder com payload binário Protobuf", "POST /OrderService/GetOrder dengan muatan Protobuf",
        "Protobufペイロードを伴うPOST /OrderService/GetOrder", "携带Protobuf二进制载荷的POST调用", "攜帶Protobuf二進位載荷的POST呼叫",
        "Protobuf 바이너리 페이로드를 전달하는 POST 호출", "Protobuf पेलोड के साथ POST अनुरोध", "קריאת POST עם נתוני Protobuf בינאריים")

    add("Protobuf Response & Status OK",
        "پاسخ باینری و وضعیت موفقیت‌آمیز در تریلر", "استجابة Protobuf مع حالة نجاح 0",
        "Respuesta Protobuf y estado 0 OK", "Réponse Protobuf et statut 0 OK",
        "Protobuf-Antwort & Status 0 OK", "Protobuf Yanıtı ve Durum 0 OK",
        "Resposta Protobuf e status 0 OK", "Respons Protobuf & Status 0 OK",
        "Protobufレスポンスとステータス 0 OK", "Protobuf响应体与状态码 0 OK", "Protobuf回應體與狀態碼 0 OK",
        "Protobuf 응답 및 상태 코드 0 OK", "Protobuf प्रतिक्रिया और स्थिति 0 OK", "תגובת Protobuf וסטטוס תקין (0 OK)")

    add("Typed response with grpc-status: 0 in trailers",
        "پاسخ داده دارای نوع با grpc-status: 0 در هدرهای پایانی", "استجابة قوية مع grpc-status: 0 في المقطورات",
        "Respuesta tipada con grpc-status: 0 en trailers", "Réponse typée avec grpc-status : 0 dans les en-têtes finaux",
        "Typisierte Antwort mit grpc-status: 0 in Trailern", "Artbilgilerde grpc-status: 0 içeren türü belirtilmiş yanıt",
        "Resposta tipada com grpc-status: 0 nos trailers", "Respons bertipe dengan grpc-status: 0 di trailer",
        "トレイラー内のgrpc-status: 0を伴う型付きレスポンス", "尾部帧附带grpc-status: 0状态码的强类型响应", "尾部訊框附帶grpc-status: 0狀態碼的強型別回應",
        "트레일러에 grpc-status: 0이 포함된 강력한 타입의 응답", "ट्रेलर में grpc-status: 0 के साथ टाइप किया गया उत्तर", "תגובה מוגדרת עם grpc-status: 0 בכותרות הסיום")

    add("Error Status: NOT_FOUND",
        "خطای استاندارد: پیدا نشدن منبع (کد ۵)", "حالة الخطأ: غير موجود (الرمز 5)",
        "Estado de error: NOT_FOUND (código 5)", "Statut d'erreur : NOT_FOUND (code 5)",
        "Fehlerstatus: NOT_FOUND (Code 5)", "Hata Durumu: Bulunamadı (Kod 5)",
        "Status de erro: NOT_FOUND (código 5)", "Status Error: TIDAK_DITEMUKAN (Kode 5)",
        "エラーステータス: NOT_FOUND (コード 5)", "错误状态: 未找到 (NOT_FOUND, 代码5)", "錯誤狀態: 找不到 (NOT_FOUND, 代碼5)",
        "에러 상태: 찾을 수 없음 (NOT_FOUND, 코드 5)", "त्रुटि स्थिति: नहीं मिला (कोड 5)", "סטטוס שגיאה: לא נמצא (קוד 5)")

    add("Canonical gRPC error code 5 returned in trailers",
        "بازگشت کد استاندارد ۵ در تریلر بدون نیاز به بدنه خطا", "إرجاع كود الخطأ القياسي 5 في المقطورات",
        "Código canónico de gRPC 5 devuelto en trailers", "Code d'erreur canonique 5 renvoyé dans les trailers",
        "Kanonischer gRPC-Fehlercode 5 in Trailern zurückgegeben", "Artbilgilerde standart gRPC hata kodu 5 döndürüldü",
        "Código canônico de gRPC 5 retornado em trailers", "Kode kesalahan standar gRPC 5 dikembalikan di trailer",
        "トレイラー内で返却される標準gRPCエラーコード5", "通过HTTP/2尾部帧直接返回标准gRPC错误码5", "透過HTTP/2尾部訊框直接返回標準gRPC錯誤碼5",
        "HTTP/2 트레일러를 통해 표준 gRPC 에러 코드 5가 즉시 반환됨", "ट्रेलर में मानक gRPC त्रुटि कोड 5 लौटा", "קוד שגיאה תקני 5 מוחזר בכותרות הסיום")

    add("Strict Deadline Exceeded",
        "انقضای مهلت پاسخگویی و لغو استریم", "تجاوز الموعد النهائي المحدد وإلغاء الاستدعاء",
        "Plazo estricto excedido y cancelación", "Délai strict dépassé et annulation",
        "Strikte Frist überschritten & Abbruch", "Kesin Zaman Sınırı Aşıldı ve İptal",
        "Prazo rigoroso excedido e cancelamento", "Batas Waktu Ketat Terlampaui",
        "厳格なデッドライン超過とキャンセル", "严格截止期限超时触发取消", "嚴格截止期限超時觸發取消",
        "엄격한 마감 시간 초과 및 스트림 취소", "कड़ी समय सीमा समाप्त और रद्दीकरण", "חריגה ממועד יעד סופי וביטול הקריאה")

    add("Timeout triggers client RST_STREAM and code 4 status",
        "پایان مهلت زمانی کلاینت را به ارسال RST_STREAM و دریافت کد ۴ وا می‌دارد", "انتهاء المهلة يدفع العميل لإرسال RST_STREAM واستلام الرمز 4",
        "El tiempo de espera activa RST_STREAM y código de error 4", "L'expiration déclenche RST_STREAM et le code de statut 4",
        "Timeout löst clientseitiges RST_STREAM und Statuscode 4 aus", "Zaman aşımı istemcinin RST_STREAM göndermesini ve kod 4 almasını tetikler",
        "O tempo limite aciona RST_STREAM do cliente e status código 4", "Timeout memicu RST_STREAM klien dan status kode 4",
        "タイムアウトによりクライアントがRST_STREAMを送信しコード4を受信", "超时促使客户端立即发出RST_STREAM并接收状态码4", "超時促使用戶端立即發出RST_STREAM並接收狀態碼4",
        "타임아웃 발생으로 클라이언트가 즉시 RST_STREAM을 전송하고 코드 4를 수신", "समय सीमा समाप्त होने पर क्लाइंट RST_STREAM भेजता है और कोड 4 मिलता है", "פסק זמן מפעיל שליחת RST_STREAM וקבלת קוד סטטוס 4")

    # Facts Keys & Common Labels
    add("Active Streams", "استریم‌های فعال", "التدفقات النشطة", "Flujos activos", "Flux actifs",
        "Aktive Streams", "Aktif Akışlar", "Fluxos ativos", "Aliran Aktif", "アクティブストリーム",
        "活跃流", "活躍串流", "활성 스트림", "सक्रिय स्ट्रीम्स", "ערוצים פעילים")

    add("Connection Overhead", "سربار اتصال اولیه", "العبء الأولي للاتصال", "Sobrecarga de conexión", "Surcharge de connexion",
        "Verbindungs-Overhead", "Bağlantı Ek Yükü", "Sobrecarga de conexão", "Overhead Koneksi", "接続オーバーヘッド",
        "连接开销", "連線開銷", "연결 오버헤드", "कनेक्शन ओवरहेड", "תקורה של החיבור")

    add("Multiplexing Gain", "مزیت مالتی‌پلکسینگ", "مكسب مضاعفة الإرسال", "Ganancia de multiplexación", "Gain de multiplexage",
        "Multiplexing-Vorteil", "Çoklama Kazanımı", "Ganho de multiplexação", "Keuntungan Multipleksing", "多重化の利点",
        "多路复用收益", "多路複用效益", "다중화 이점", "मल्टीप्लेक्सिंग लाभ", "יתרון ריבוי ערוצים")

    add("Transport Vulnerability", "آسیب‌پذیری لایه انتقال", "نقطة ضعف طبقة النقل", "Vulnerabilidad de transporte", "Vulnérabilité de transport",
        "Transportschwäche", "Aktarım Zafiyeti", "Vulnerabilidade de transporte", "Kerentanan Transport", "トランスポート層の弱点",
        "传输层脆弱点", "傳輸層脆弱點", "전송 계층 취약점", "ट्रांसपोर्ट भेद्यता", "פגיעות שכבת התעבורה")

    add("Handshake Time", "مدت زمان دست‌تکانی", "وقت المصافحة", "Tiempo de apretón", "Temps de négociation",
        "Handshake-Dauer", "Tokalaşma Süresi", "Tempo de handshake", "Waktu Jabat Tangan", "ハンドシェイク時間",
        "握手耗时", "交握耗時", "핸드셰이크 소요 시간", "हैंडशेक समय", "זמן לחיצת יד")

    add("Connection Migration", "مهاجرت کانکشن", "ترحيل الاتصال", "Migración de conexión", "Migration de connexion",
        "Verbindungsmigration", "Bağlantı Taşıma", "Migração de conexão", "Migrasi Koneksi", "コネクションマイグレーション",
        "连接平滑迁移", "連線平滑遷移", "연결 마이그레이션", "कनेक्शन माइग्रेशन", "נדידת חיבור")

    add("Socket State", "وضعیت سوکت شبکه", "حالة المقبس", "Estado del socket", "État du socket",
        "Socket-Zustand", "Soket Durumu", "Estado do socket", "Status Soket", "ソケット状態",
        "套接字状态", "通訊端狀態", "소켓 상태", "सॉकेट स्थिति", "מצב שקע הרשת")

    add("Framing Overhead", "سربار فریم‌بندی", "عبء تأطير البيانات", "Sobrecarga de tramas", "Surcharge de trames",
        "Framing-Overhead", "Çerçeveleme Ek Yükü", "Sobrecarga de quadros", "Overhead Pembingkaian", "フレームオーバーヘッド",
        "帧开销", "訊框開銷", "프레이밍 오버헤드", "फ़्रेमिंग ओवरहेड", "תקורת מסגור")

    add("Directionality", "جهت انتقال داده", "اتجاهية البيانات", "Direccionalidad", "Directionnalité",
        "Richtung", "Yönlülük", "Direcionalidade", "Arah Aliran", "方向性",
        "双向传输能力", "雙向傳輸能力", "방향성", "दिशात्मकता", "כיווניות")

    add("Heartbeat Check", "بررسی زنده بودن اتصال", "فحص نبضات القلب", "Comprobación de latido", "Contrôle de battement",
        "Heartbeat-Prüfung", "Heartbeat Kontrolü", "Verificação de heartbeat", "Pemeriksaan Detak Jantung", "ハートビート監視",
        "心跳保活检测", "心跳保活檢測", "하트비트 감시", "हार्टबीट जाँच", "בדיקת דופק חיים")

    add("Close Handshake", "دست‌تکانی پایان ارتباط", "مصافحة الإغلاق", "Apretón de cierre", "Fermeture négociée",
        "Schließen-Handshake", "Kapanış Tokalaşması", "Handshake de encerramento", "Jabat Tangan Penutupan", "クローズハンドシェイク",
        "挥手断开机制", "揮手斷開機制", "종료 핸드셰이크", "क्लोज़ हैंडशेक", "לחיצת יד לסגירה")

    add("Header Overhead", "سربار هدر پروتکل", "حجم رؤوس البروتوكول", "Sobrecarga de encabezados", "Surcharge d'en-tête",
        "Header-Overhead", "Başlık Ek Yükü", "Sobrecarga de cabeçalho", "Overhead Header", "ヘッダーオーバーヘッド",
        "报头开销", "標頭開銷", "헤더 오버헤드", "हेडर ओवरहेड", "תקורת כותרת")

    add("Delivery Guarantee", "تضمین تحویل پیام", "ضمان تسليم الرسالة", "Garantía de entrega", "Garantie de livraison",
        "Zustellgarantie", "Teslimat Garantisi", "Garantia de entrega", "Jaminan Pengiriman", "配信保証レベル",
        "消息投递保证", "訊息投遞保證", "메시지 전달 보장", "वितरण गारंटी", "אחריות מסירה")

    add("State Persistence", "ماندگاری وضعیت نشست", "استمرارية حالة الجلسة", "Persistencia de estado", "Persistance d'état",
        "Zustandspersistenz", "Durum Kalıcılığı", "Persistência de estado", "Persistensi Status", "状態永続化",
        "会话状态持久化", "工作階段狀態持久化", "상태 지속성", "स्थिति दृढ़ता", "התמדת מצב")

    add("Offline Alert", "هشدار آفلاین شدن", "تنبيه عدم الاتصال", "Alerta de desconexión", "Alerte hors ligne",
        "Offline-Alarm", "Çevrimdışı Uyarısı", "Alerta offline", "Peringatan Offline", "オフライン通知",
        "离线遗嘱预警", "離線遺囑預警", "오프라인 알림", "ऑफ़लाइन चेतावनी", "התראת ניתוק")

    add("Memory Buffer", "بافر حافظه مورد نیاز", "ذاكرة التخزين المؤقت", "Búfer de memoria", "Tampon mémoire",
        "Speicherpuffer", "Bellek Arabelleği", "Buffer de memória", "Buffer Memori", "必要なメモリバッファ",
        "内存缓冲开销", "記憶體緩衝開銷", "메모리 버퍼링", "मेमोरी बफर", "חוצץ זיכרון")

    add("Delimiter", "جداکننده قطعات داده", "محدد الأجزاء", "Delimitador", "Délimiteur",
        "Trennzeichen", "Sınırlayıcı", "Delimitador", "Pemisah", "区切り文字",
        "块分隔标识", "塊分隔標識", "구분자", "सीमांकक", "תו מפריד")

    add("Trailer Support", "پشتیبانی از هدرهای پایانی", "دعم الرؤوس الختامية", "Soporte de trailers", "Prise en charge des trailers",
        "Trailer-Unterstützung", "Artbilgi Desteği", "Suporte a trailers", "Dukungan Trailer", "トレイラーサポート",
        "尾部标头支持", "尾部標頭支援", "트레일러 지원", "ट्रेलर समर्थन", "תמיכה בכותרות סיום")

    add("Failure Mode", "نحوه مواجهه با خطا", "سلوك معالجة الخطأ", "Modo de falla", "Comportement en échec",
        "Fehlermodus", "Hata Davranışı", "Modo de falha", "Mode Kegagalan", "障害発生時の動作",
        "故障降级行为", "故障降級行為", "장애 대응 방식", "विफलता मोड", "אופן טיפול בכשל")

    add("Serialization Efficiency", "بهره‌وری سریال‌سازی داده", "كفاءة تسلسل البيانات", "Eficiencia de serialización", "Efficacité de sérialisation",
        "Serialisierungseffizienz", "Serileştirme Verimliliği", "Eficiência de serialização", "Efisiensi Serialisasi", "シリアライズ効率",
        "序列化效率", "序列化效率", "직렬화 효율성", "क्रमांकन दक्षता", "יעילות סריאליזציה")

    add("Error Propagation", "نحوه انتقال خطا", "نقل تفاصيل الأخطاء", "Propagación de errores", "Propagation d'erreur",
        "Fehlerübertragung", "Hata Yayılımı", "Propagação de erros", "Propagasi Error", "エラー伝播方式",
        "错误传递机制", "錯誤傳遞機制", "에러 전파 방식", "त्रुटि प्रसार", "הפצת שגיאות")

    add("Deadline Support", "پشتیبانی از مهلت پاسخگویی", "دعم المهل الزمنية", "Soporte de plazos", "Gestion des délais",
        "Frist-Unterstützung", "Zaman Sınırı Desteği", "Suporte a prazos", "Dukungan Batas Waktu", "デッドライン制御",
        "截止期限控制", "截止期限控制", "마감 시간 (데드라인) 제어", "समय सीमा समर्थन", "תמיכה במועדי יעד")

    add("Streaming Capabilities", "انواع پشتیبانی از استریم", "أنماط التدفق المدعومة", "Capacidades de transmisión", "Capacités de streaming",
        "Streaming-Fähigkeiten", "Akış Yetenekleri", "Capacidades de streaming", "Kemampuan Streaming", "ストリーミング機能",
        "流式RPC模式", "串流RPC模式", "스트리밍 기능", "स्ट्रीमिंग क्षमताएं", "יכולות הזרמה")

    return t

if __name__ == '__main__':
    data = get_full_translations()
    with open('localization/dictionary.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Successfully generated dictionary.json with {len(data)} multi-lingual entries across all 15 languages!")
