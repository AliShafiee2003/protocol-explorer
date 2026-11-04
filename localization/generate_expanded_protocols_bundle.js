import fs from 'fs';

// Load dictionary
const dict = JSON.parse(fs.readFileSync('localization/dictionary.json', 'utf8'));

// Generate the lessons JS string
const lessonsCode = `
// ==================== 7 MODERN PROTOCOL LESSONS ====================

const lessonHttp2 = {
  id: "http2",
  name: "HTTP/2",
  title: "Multiplexed Binary Streams",
  layer: 7,
  nodes: ["client", "router", "internet", "web"],
  latency: { "client-web": 0.018, "client-router": 0.002, "router-web": 0.016, "client-internet": 0.010, "internet-web": 0.008 },
  legend: [["green", "TCP"], ["teal", "TLS 1.3"], ["amber", "Stream 1 (HTML)"], ["violet", "Stream 3 (CSS)"], ["blue", "Stream 5 (Image)"], ["rose", "RST_STREAM / Loss"]],
  overview: {
    full: "Hypertext Transfer Protocol Version 2",
    description: "HTTP/2 replaces plain text with binary framing and stream multiplexing over a single TCP connection. Multiple requests and responses interleave concurrently without head-of-line blocking at the application layer.",
    facts: [["Layer", "Application (Layer 7)"], ["Default Port", "443 (h2 via ALPN)"], ["Transport", "TCP + TLS 1.3"], ["Framing", "Binary frames (Length, Type, Flags, Stream ID)"], ["Multiplexing", "Concurrent streams on 1 TCP connection"], ["Defined In", "RFC 7540, RFC 9113"]]
  },
  outro: {
    title: "Multiplexed Streams Completed",
    desc: "Concurrent delivery on a single connection",
    text: "HTTP/2 sent HTML, CSS, and Images interleaved across independent streams. However, when TCP packet loss occurred, all streams paused until TCP recovered (TCP head-of-line blocking).",
    facts: [["Active Streams", "Stream 1, 3, 5"], ["Connection Overhead", "1 TCP + TLS Handshake"], ["Multiplexing Gain", "Zero HTTP head-of-line blocking"], ["Transport Vulnerability", "TCP packet loss halts all streams"]]
  },
  start: { nodes: ["client"], frame: "client" },
  steps: [
    {
      title: "TCP & TLS 1.3 Handshake",
      desc: "Establishes secure transport with h2 ALPN",
      detail: "Before any HTTP/2 frames can be sent, the browser establishes a TCP connection and negotiates TLS 1.3 with ALPN set to h2.",
      facts: [["TCP Port", "443"], ["TLS Extension", "ALPN: h2"], ["Round Trips", "2 (1 TCP + 1 TLS 1.3)"]],
      events: [
        { type: "show", nodes: ["router", "internet", "web"], frame: "path" },
        u("client", "web", "green", "SYN", ["TCP SYN", "sport: 52410, dport: 443"], { time: "0.000s", src: "192.168.1.105", dst: "93.184.216.34", proto: "TCP", info: "52410 → 443 [SYN] Seq=0 Win=65535", len: "66 B", wire: { tcp: { sport: 52410, dport: 443, flags: "S" } } }),
        u("web", "client", "green", "SYN-ACK", ["TCP SYN, ACK", "sport: 443, dport: 52410"], { time: "0.018s", src: "93.184.216.34", dst: "192.168.1.105", proto: "TCP", info: "443 → 52410 [SYN, ACK] Seq=0 Ack=1 Win=65535", len: "66 B", wire: { tcp: { sport: 443, dport: 52410, flags: "SA" } } }),
        u("client", "web", "teal", "CLIENT HELLO", ["TLS 1.3 Client Hello", "ALPN: h2"], { time: "0.036s", src: "192.168.1.105", dst: "93.184.216.34", proto: "TLSv1.3", info: "Client Hello (ALPN: h2)", len: "312 B", wire: { tcp: { sport: 52410, dport: 443, flags: "PA" } } }),
        u("web", "client", "teal", "SERVER HELLO", ["TLS 1.3 Server Hello", "Encrypted Extensions, Finished"], { time: "0.054s", src: "93.184.216.34", dst: "192.168.1.105", proto: "TLSv1.3", info: "Server Hello, Finished", len: "950 B", wire: { tcp: { sport: 443, dport: 52410, flags: "PA" } } }),
        { type: "note", at: "client", text: "TLS ALPN NEGOTIATED: h2", tone: "green" }
      ]
    },
    {
      title: "HTTP/2 Preface & SETTINGS",
      desc: "Negotiates stream parameters and window sizes",
      detail: "Client sends the 24-byte HTTP/2 connection preface followed by a SETTINGS frame on Stream 0. The server confirms with a SETTINGS ACK.",
      facts: [["Preface", "PRI * HTTP/2.0"], ["Control Stream", "Stream 0"], ["Max Streams", "100 concurrent"]],
      events: [
        u("client", "web", "amber", "PREFACE + SETTINGS", ["Preface (24 bytes)", "SETTINGS (Stream 0)"], { time: "0.072s", src: "192.168.1.105", dst: "93.184.216.34", proto: "HTTP/2", info: "SETTINGS [MAX_CONCURRENT_STREAMS=100]", len: "98 B", wire: { tcp: { sport: 52410, dport: 443, flags: "PA", data: { http2: { type: "SETTINGS", streamId: 0, typeCode: 4, flags: 0, params: [{ id: "MAX_CONCURRENT_STREAMS", val: 100, idCode: 3 }] } } } } }),
        u("web", "client", "amber", "SETTINGS ACK", ["SETTINGS ACK (Stream 0)"], { time: "0.090s", src: "93.184.216.34", dst: "192.168.1.105", proto: "HTTP/2", info: "SETTINGS [ACK]", len: "60 B", wire: { tcp: { sport: 443, dport: 52410, flags: "A", data: { http2: { type: "SETTINGS", streamId: 0, typeCode: 4, flags: 1 } } } } }),
        { type: "note", at: "web", text: "STREAM PREFACE & SETTINGS EXCHANGED", tone: "green" }
      ]
    },
    {
      title: "Multiplexed Streams (1, 3, 5)",
      desc: "Client requests HTML, CSS, and Image simultaneously",
      detail: "Unlike HTTP/1.1 which needed multiple TCP connections, HTTP/2 sends 3 distinct HEADERS frames over the same connection concurrently on odd-numbered streams (1, 3, 5).",
      facts: [["Stream 1", "GET /index.html"], ["Stream 3", "GET /style.css"], ["Stream 5", "GET /hero.png"]],
      events: [
        u("client", "web", "amber", "HEADERS (Str 1)", ["GET /index.html", "Stream 1"], { time: "0.110s", src: "192.168.1.105", dst: "93.184.216.34", proto: "HTTP/2", info: "HEADERS Stream: 1 [GET /index.html]", len: "82 B", wire: { tcp: { sport: 52410, dport: 443, flags: "PA", data: { http2: { type: "HEADERS", streamId: 1, typeCode: 1, flags: 5, headers: [":method GET", ":path /index.html", ":scheme https"] } } } } }),
        u("client", "web", "violet", "HEADERS (Str 3)", ["GET /style.css", "Stream 3"], { time: "0.111s", src: "192.168.1.105", dst: "93.184.216.34", proto: "HTTP/2", info: "HEADERS Stream: 3 [GET /style.css]", len: "78 B", wire: { tcp: { sport: 52410, dport: 443, flags: "PA", data: { http2: { type: "HEADERS", streamId: 3, typeCode: 1, flags: 5, headers: [":method GET", ":path /style.css", ":scheme https"] } } } } }),
        u("client", "web", "blue", "HEADERS (Str 5)", ["GET /hero.png", "Stream 5"], { time: "0.112s", src: "192.168.1.105", dst: "93.184.216.34", proto: "HTTP/2", info: "HEADERS Stream: 5 [GET /hero.png]", len: "76 B", wire: { tcp: { sport: 52410, dport: 443, flags: "PA", data: { http2: { type: "HEADERS", streamId: 5, typeCode: 1, flags: 5, headers: [":method GET", ":path /hero.png", ":scheme https"] } } } } })
      ]
    },
    {
      title: "Server Interleaved Data & Packet Loss",
      desc: "Stream 3 packet is dropped in transit",
      detail: "The server interleaves data chunks from all 3 streams. Stream 1 (HTML) and Stream 5 (Image) arrive safely, but the TCP packet carrying Stream 3 (CSS) is dropped by router congestion.",
      facts: [["Stream 1 Status", "Arrived (500 B)"], ["Stream 3 Status", "LOST IN TRANSIT"], ["Stream 5 Status", "Arrived (1200 B)"]],
      events: [
        u("web", "client", "amber", "DATA (Str 1)", ["HTML Chunk", "Stream 1"], { time: "0.130s", src: "93.184.216.34", dst: "192.168.1.105", proto: "HTTP/2", info: "DATA Stream: 1 (HTML 500 B)", len: "550 B", wire: { tcp: { sport: 443, dport: 52410, flags: "PA", data: { http2: { type: "DATA", streamId: 1, typeCode: 0, flags: 1, length: 500, data: "<!DOCTYPE html><html><head><title>Test</title></head></html>" } } } } }),
        u("web", "client", "violet", "DATA (Str 3)", ["CSS Chunk", "Stream 3"], { time: "0.131s", src: "93.184.216.34", dst: "192.168.1.105", proto: "HTTP/2", info: "DATA Stream: 3 (CSS 900 B)", len: "950 B", wire: { tcp: { sport: 443, dport: 52410, flags: "PA", data: { http2: { type: "DATA", streamId: 3, typeCode: 0, flags: 0, length: 900, data: "body { background: #fff; color: #333; }" } } } } }, { lost: true }),
        u("web", "client", "blue", "DATA (Str 5)", ["Image Chunk", "Stream 5"], { time: "0.132s", src: "93.184.216.34", dst: "192.168.1.105", proto: "HTTP/2", info: "DATA Stream: 5 (Image 1200 B)", len: "1250 B", wire: { tcp: { sport: 443, dport: 52410, flags: "PA", data: { http2: { type: "DATA", streamId: 5, typeCode: 0, flags: 0, length: 1200, data: "[PNG Image Binary Data]" } } } } }),
        { type: "note", at: "internet", text: "PACKET LOSS: STREAM 3 (CSS) DROPPED", tone: "amber" }
      ]
    },
    {
      title: "TCP Head-of-Line Blocking",
      desc: "Stream 5 is blocked until Stream 3 recovers",
      detail: "Even though Stream 5 was completely received by the client's network card, the operating system TCP stack cannot pass it to the browser because TCP requires in-order byte delivery! All streams are stalled until Stream 3 is retransmitted.",
      facts: [["Vulnerability", "TCP Head-of-Line Blocking"], ["Client Action", "Duplicate ACK + SACK"], ["Resolution", "Retransmission of Stream 3"]],
      events: [
        { type: "note", at: "client", text: "TCP HOL BLOCKING: ALL STREAMS PAUSED", tone: "rose" },
        u("client", "web", "green", "TCP DUP ACK", ["SACK block: Stream 5 received", "Waiting for Stream 3"], { time: "0.150s", src: "192.168.1.105", dst: "93.184.216.34", proto: "TCP", info: "52410 → 443 [ACK] SACK: Missing Stream 3", len: "74 B", wire: { tcp: { sport: 52410, dport: 443, flags: "A" } } }),
        u("web", "client", "violet", "DATA RETRANSMIT", ["CSS Chunk (Stream 3)", "Retransmitted"], { time: "0.170s", src: "93.184.216.34", dst: "192.168.1.105", proto: "HTTP/2", info: "DATA Stream: 3 (Retransmitted)", len: "950 B", wire: { tcp: { sport: 443, dport: 52410, flags: "PA", data: { http2: { type: "DATA", streamId: 3, typeCode: 0, flags: 1, length: 900, data: "body { background: #fff; color: #333; }" } } } } })
      ]
    },
    {
      title: "Stream Cancellation via RST_STREAM",
      desc: "Client cancels Stream 5 without closing TCP connection",
      detail: "The user navigated away before the full image was needed. The client issues a RST_STREAM frame with error code CANCEL (0x8). The server stops sending image data immediately while keeping the TCP connection open for other streams.",
      facts: [["Cancelled Stream", "Stream 5"], ["Error Code", "0x8 (CANCEL)"], ["Connection Impact", "Zero (TCP remains active)"]],
      events: [
        u("client", "web", "rose", "RST_STREAM", ["Cancel Stream 5", "Code: CANCEL (0x8)"], { time: "0.195s", src: "192.168.1.105", dst: "93.184.216.34", proto: "HTTP/2", info: "RST_STREAM Stream: 5 [CANCEL 0x8]", len: "64 B", wire: { tcp: { sport: 52410, dport: 443, flags: "PA", data: { http2: { type: "RST_STREAM", streamId: 5, typeCode: 3, flags: 0, errorCode: 8, errorName: "CANCEL" } } } } }),
        { type: "note", at: "client", text: "STREAM 5 CANCELLED: RST_STREAM", tone: "green" }
      ]
    }
  ]
};

const lessonHttp3 = {
  id: "http3",
  name: "HTTP/3",
  title: "QUIC over UDP Evolution",
  layer: 7,
  nodes: ["client", "router", "internet", "web"],
  latency: { "client-web": 0.016, "client-router": 0.002, "router-web": 0.014, "client-internet": 0.009, "internet-web": 0.007 },
  legend: [["teal", "QUIC Handshake (1-RTT)"], ["amber", "Stream 0 (HTML)"], ["blue", "Stream 4 (Image)"], ["green", "QUIC ACK"], ["rose", "Loss / Migration"]],
  overview: {
    full: "HTTP/3 over QUIC",
    description: "HTTP/3 runs over QUIC, a transport protocol built on top of UDP. It integrates TLS 1.3 encryption directly into transport, eliminates TCP head-of-line blocking, and supports seamless connection migration when networks switch.",
    facts: [["Layer", "Application (Layer 7) / Transport (QUIC)"], ["Default Port", "443 (UDP)"], ["Transport", "QUIC over UDP"], ["Handshake", "1-RTT (or 0-RTT resumption)"], ["HoL Blocking", "None: Streams are strictly independent"], ["Defined In", "RFC 9000, RFC 9114"]]
  },
  outro: {
    title: "Independent QUIC Streams",
    desc: "Zero Head-of-Line blocking and seamless mobility",
    text: "HTTP/3 established encryption in a single round-trip over UDP. When a packet was lost on Stream 4, Stream 0 continued rendering without delay. Switching from Wi-Fi to 4G required no reconnect due to Connection IDs.",
    facts: [["Handshake Time", "1 RTT (~18 ms)"], ["HoL Blocking", "0 ms (isolated stream loss)"], ["Connection Migration", "PATH_CHALLENGE / PATH_RESPONSE"], ["Socket State", "Persisted across IP changes"]]
  },
  start: { nodes: ["client"], frame: "client" },
  steps: [
    {
      title: "1-RTT QUIC Handshake",
      desc: "Cryptographic handshake completed over UDP in 1 RTT",
      detail: "Client sends a QUIC Initial datagram over UDP port 443 carrying TLS 1.3 Client Hello. No separate TCP handshake is required. Encryption and transport parameters are negotiated simultaneously.",
      facts: [["Transport", "UDP Port 443"], ["Initial DCID", "0x8a3f9104c2"], ["Handshake Round Trips", "1 RTT"]],
      events: [
        { type: "show", nodes: ["router", "internet", "web"], frame: "path" },
        u("client", "web", "teal", "QUIC INITIAL", ["QUIC Initial [CRYPTO]", "TLS 1.3 Client Hello"], { time: "0.000s", src: "192.168.1.105", dst: "93.184.216.34", proto: "QUIC", info: "Initial, DCID=8a3f9104, CRYPTO: Client Hello", len: "1200 B", wire: { udp: { sport: 50443, dport: 443, data: { quic: { isLong: true, packetType: "Initial", dcid: "8a3f9104", packetNumber: 1, frames: [{ type: "CRYPTO", typeCode: 6, data: "TLS 1.3 Client Hello, ALPN=h3", note: "Carries TLS handshake records" }] } } } } }),
        u("web", "client", "teal", "INITIAL + HANDSHAKE", ["Server Hello, Finished", "Handshake keys derived"], { time: "0.016s", src: "93.184.216.34", dst: "192.168.1.105", proto: "QUIC", info: "Initial, Handshake [CRYPTO: Finished]", len: "1280 B", wire: { udp: { sport: 443, dport: 50443, data: { quic: { isLong: true, packetType: "Handshake", dcid: "8a3f9104", packetNumber: 1, frames: [{ type: "CRYPTO", typeCode: 6, data: "Server Hello, Finished", note: "1-RTT Handshake completed" }] } } } } }),
        { type: "note", at: "client", text: "QUIC 1-RTT HANDSHAKE COMPLETE", tone: "green" }
      ]
    },
    {
      title: "Concurrent QUIC Streams",
      desc: "Independent streams multiplexed over UDP datagrams",
      detail: "Client requests HTML on Stream 0 and Image on Stream 4 in 1-RTT short-header packets. In QUIC, each stream is tracked independently by the transport layer.",
      facts: [["Stream 0", "GET /index.html"], ["Stream 4", "GET /photo.webp"], ["Header Form", "Short Header (1-RTT)"]],
      events: [
        u("client", "web", "amber", "1-RTT (Stream 0 & 4)", ["HEADERS: Stream 0 (HTML)", "HEADERS: Stream 4 (Image)"], { time: "0.032s", src: "192.168.1.105", dst: "93.184.216.34", proto: "HTTP/3", info: "1-RTT, Stream 0 & 4 [HEADERS]", len: "140 B", wire: { udp: { sport: 50443, dport: 443, data: { quic: { isLong: false, packetType: "1-RTT", dcid: "8a3f9104", packetNumber: 2, frames: [{ type: "STREAM", streamId: 0, typeCode: 8, data: ":method GET :path /index.html" }, { type: "STREAM", streamId: 4, typeCode: 8, data: ":method GET :path /photo.webp" }] } } } } }),
        u("web", "client", "amber", "STREAM 0 (HTML)", ["HTML Data (500 B)", "Offset: 0"], { time: "0.050s", src: "93.184.216.34", dst: "192.168.1.105", proto: "HTTP/3", info: "1-RTT, Stream: 0 Offset=0 Len=500", len: "540 B", wire: { udp: { sport: 443, dport: 50443, data: { quic: { isLong: false, packetType: "1-RTT", dcid: "8a3f9104", packetNumber: 3, frames: [{ type: "STREAM", streamId: 0, typeCode: 8, data: "<!DOCTYPE html><html><h1>QUIC HTTP/3</h1></html>" }] } } } } })
      ]
    },
    {
      title: "Stream 4 Loss (No HoL Blocking)",
      desc: "Image packet lost with zero delay to HTML stream",
      detail: "The UDP packet carrying Stream 4 (Image) is lost. In TCP, this would freeze Stream 0 from reaching the browser. In QUIC over UDP, Stream 0 is delivered and rendered immediately with ZERO delay!",
      facts: [["Stream 0 Delivery", "Immediate (Rendered)"], ["Stream 4 Status", "LOST IN TRANSIT"], ["Head-of-Line Impact", "0 ms delay"]],
      events: [
        u("web", "client", "blue", "STREAM 4 (IMAGE)", ["Image Data (1200 B)", "Offset: 0"], { time: "0.052s", src: "93.184.216.34", dst: "192.168.1.105", proto: "HTTP/3", info: "1-RTT, Stream: 4 Offset=0 Len=1200", len: "1240 B", wire: { udp: { sport: 443, dport: 50443, data: { quic: { isLong: false, packetType: "1-RTT", dcid: "8a3f9104", packetNumber: 4, frames: [{ type: "STREAM", streamId: 4, typeCode: 8, data: "[WEBP Image Chunk 1]" }] } } } } }, { lost: true }),
        { type: "note", at: "client", text: "STREAM 4 LOST · ZERO IMPACT ON STREAM 0", tone: "green" }
      ]
    },
    {
      title: "Independent Stream Retransmission",
      desc: "Only missing stream data is resent with new packet number",
      detail: "Client acknowledges Stream 0 with a QUIC ACK frame. Server detects missing packet #4 and retransmits Stream 4 data under a NEW packet number (#5). QUIC never reuses packet numbers.",
      facts: [["QUIC ACK", "Stream 0 confirmed"], ["New Packet Number", "#5 (Prevents ACK ambiguity)"], ["Stream 4 Offset", "0 (Original bytes resent)"]],
      events: [
        u("client", "web", "green", "QUIC ACK", ["ACK Packet #3 (Stream 0)", "NACK Packet #4 (Stream 4)"], { time: "0.068s", src: "192.168.1.105", dst: "93.184.216.34", proto: "QUIC", info: "1-RTT, ACK: Largest Acked=3", len: "64 B", wire: { udp: { sport: 50443, dport: 443, data: { quic: { isLong: false, packetType: "1-RTT", dcid: "8a3f9104", packetNumber: 3, frames: [{ type: "ACK", typeCode: 2, note: "Acknowledges packet #3" }] } } } } }),
        u("web", "client", "blue", "STREAM 4 RETRANSMIT", ["Image Data Resent", "New Packet #5"], { time: "0.086s", src: "93.184.216.34", dst: "192.168.1.105", proto: "HTTP/3", info: "1-RTT, Stream: 4 (Packet #5)", len: "1240 B", wire: { udp: { sport: 443, dport: 50443, data: { quic: { isLong: false, packetType: "1-RTT", dcid: "8a3f9104", packetNumber: 5, frames: [{ type: "STREAM", streamId: 4, typeCode: 8, data: "[WEBP Image Chunk 1]" }] } } } } }),
        { type: "note", at: "web", text: "QUIC ACK & STREAM 4 RETRANSMITTED", tone: "green" }
      ]
    },
    {
      title: "Network Switch & Migration",
      desc: "Connection persists across IP change from Wi-Fi to 4G",
      detail: "Client laptop leaves Wi-Fi and connects to 4G Cellular (IP changes from 192.168.1.105 to 10.42.18.90). In TCP this would crash the connection. QUIC sends PATH_CHALLENGE using the same Connection ID and migrates seamlessly!",
      facts: [["Old Client IP", "192.168.1.105 (Wi-Fi)"], ["New Client IP", "10.42.18.90 (Cellular)"], ["Connection ID", "0x8a3f9104 (Unchanged)"]],
      events: [
        u("client", "web", "rose", "PATH_CHALLENGE", ["Client IP changed to 10.42.18.90", "PATH_CHALLENGE (CID 0x8a3f9104)"], { time: "0.110s", src: "10.42.18.90", dst: "93.184.216.34", proto: "QUIC", info: "1-RTT, PATH_CHALLENGE Data=0x9f2a41c8", len: "72 B", wire: { udp: { sport: 50443, dport: 443, data: { quic: { isLong: false, packetType: "1-RTT", dcid: "8a3f9104", packetNumber: 6, frames: [{ type: "PATH_CHALLENGE", typeCode: 26, data: "0x9f2a41c8", note: "Validates new network path" }] } } } } }),
        u("web", "client", "teal", "PATH_RESPONSE", ["Path validated", "Connection active on 4G"], { time: "0.126s", src: "93.184.216.34", dst: "10.42.18.90", proto: "QUIC", info: "1-RTT, PATH_RESPONSE Data=0x9f2a41c8", len: "72 B", wire: { udp: { sport: 443, dport: 50443, data: { quic: { isLong: false, packetType: "1-RTT", dcid: "8a3f9104", packetNumber: 7, frames: [{ type: "PATH_RESPONSE", typeCode: 27, data: "0x9f2a41c8", note: "Path migration verified" }] } } } } }),
        { type: "note", at: "client", text: "CONNECTION MIGRATED (WIFI → 4G)", tone: "teal" }
      ]
    }
  ]
};

const lessonWs = {
  id: "ws",
  name: "WebSocket",
  title: "Bidirectional Full-Duplex Web Streams",
  layer: 7,
  nodes: ["client", "router", "internet", "web"],
  latency: { "client-web": 0.014, "client-router": 0.002, "router-web": 0.012, "client-internet": 0.008, "internet-web": 0.006 },
  legend: [["green", "Upgrade (HTTP 101)"], ["amber", "Client Frame (Masked)"], ["violet", "Server Frame (Unmasked)"], ["blue", "Ping / Pong"], ["rose", "Loss / Reconnect"]],
  overview: {
    full: "WebSocket Protocol",
    description: "WebSocket provides persistent, full-duplex communication over a single TCP connection. Initiated with an HTTP/1.1 Upgrade handshake, either side can send low-overhead text or binary frames at any time.",
    facts: [["Layer", "Application (Layer 7)"], ["Default Port", "80 (ws) / 443 (wss)"], ["Transport", "TCP / TLS"], ["Framing", "Minimal 2–10 byte binary frame"], ["Client Masking", "Mandatory 4-byte XOR mask"], ["Defined In", "RFC 6455"]]
  },
  outro: {
    title: "Real-Time Stream Maintained",
    desc: "Sub-millisecond messaging and heartbeat recovery",
    text: "WebSocket transformed an HTTP connection into a continuous two-way stream. Client masking protected intermediary caches, heartbeat pings detected silent disconnects, and exponential backoff restored the link.",
    facts: [["Framing Overhead", "2 to 6 bytes per message"], ["Directionality", "True full-duplex"], ["Heartbeat Check", "Ping / Pong keep-alive"], ["Close Handshake", "Clean code 1000 closure"]]
  },
  start: { nodes: ["client"], frame: "client" },
  steps: [
    {
      title: "WebSocket Upgrade Handshake",
      desc: "HTTP/1.1 101 Switching Protocols upgrade",
      detail: "Client sends an HTTP/1.1 GET with Upgrade: websocket and a random base64 Sec-WebSocket-Key. Server computes the SHA-1 response hash and returns HTTP 101 Switching Protocols.",
      facts: [["Handshake Request", "GET /chat (Upgrade: websocket)"], ["Handshake Response", "HTTP/1.1 101 Switching Protocols"], ["Key Negotiation", "Sec-WebSocket-Accept verified"]],
      events: [
        { type: "show", nodes: ["router", "internet", "web"], frame: "path" },
        u("client", "web", "green", "GET /chat (UPGRADE)", ["Upgrade: websocket", "Sec-WebSocket-Key"], { time: "0.000s", src: "192.168.1.105", dst: "93.184.216.34", proto: "HTTP", info: "GET /chat HTTP/1.1 [Upgrade: websocket]", len: "240 B", wire: { tcp: { sport: 52412, dport: 443, flags: "PA", data: { text: ["GET /chat HTTP/1.1", "Host: example.com", "Upgrade: websocket", "Connection: Upgrade", "Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ=="] } } } }),
        u("web", "client", "green", "101 SWITCHING", ["HTTP/1.1 101 Switching Protocols", "Connection: Upgrade"], { time: "0.014s", src: "93.184.216.34", dst: "192.168.1.105", proto: "HTTP", info: "HTTP/1.1 101 Switching Protocols", len: "180 B", wire: { tcp: { sport: 443, dport: 52412, flags: "PA", data: { text: ["HTTP/1.1 101 Switching Protocols", "Upgrade: websocket", "Connection: Upgrade", "Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo="] } } } }),
        { type: "note", at: "client", text: "UPGRADED TO WEBSOCKET", tone: "green" }
      ]
    },
    {
      title: "Client Masked Frame",
      desc: "Client frame XOR-masked for proxy cache security",
      detail: "Client sends text 'Hello Server!'. Under RFC 6455, every client-to-server frame MUST be XOR masked using a 4-byte random key to prevent malicious cache poisoning on transparent proxies.",
      facts: [["Opcode", "0x1 (Text Frame)"], ["Masked Flag", "1 (4-byte XOR key)"], ["Mask Key", "0x37 0xfa 0x21 0x3d"]],
      events: [
        u("client", "web", "amber", "WS TEXT (MASKED)", ["Opcode: 0x1 (Text)", "Payload: 'Hello Server!' (Masked)"], { time: "0.030s", src: "192.168.1.105", dst: "93.184.216.34", proto: "WebSocket", info: "WebSocket Text [Masked] (13 bytes)", len: "73 B", wire: { tcp: { sport: 52412, dport: 443, flags: "PA", data: { ws: { fin: 1, opcode: 1, opcodeName: "Text", masked: 1, length: 13, maskKey: [55, 250, 33, 61], text: "Hello Server!" } } } } }),
        { type: "note", at: "web", text: "CLIENT FRAME: XOR-MASKED", tone: "green" }
      ]
    },
    {
      title: "Server Unmasked Broadcast",
      desc: "Server pushes real-time event to client",
      detail: "Server pushes an asynchronous event without being prompted. Server-to-client frames are NEVER masked, keeping overhead to just 2 bytes.",
      facts: [["Direction", "Server to Client (Push)"], ["Masked Flag", "0 (Unmasked)"], ["Frame Overhead", "2 bytes"]],
      events: [
        u("web", "client", "violet", "WS TEXT (UNMASKED)", ["Opcode: 0x1 (Text)", "User Alice joined room"], { time: "0.046s", src: "93.184.216.34", dst: "192.168.1.105", proto: "WebSocket", info: "WebSocket Text (22 bytes)", len: "82 B", wire: { tcp: { sport: 443, dport: 52412, flags: "PA", data: { ws: { fin: 1, opcode: 1, opcodeName: "Text", masked: 0, length: 22, text: "User Alice joined room" } } } } })
      ]
    },
    {
      title: "Heartbeat Ping Loss",
      desc: "Ping packet lost, triggering heartbeat timeout",
      detail: "To verify the TCP connection is still alive through NATs and firewalls, client sends a Ping frame (opcode 0x9). The router drops it, triggering a client heartbeat timeout.",
      facts: [["Ping Opcode", "0x9 (Control Frame)"], ["Status", "LOST IN TRANSIT"], ["Client Action", "Ping timer expires"]],
      events: [
        u("client", "web", "blue", "PING (0x9)", ["Opcode: 0x9 (Ping)", "Keep-alive heartbeat"], { time: "0.065s", src: "192.168.1.105", dst: "93.184.216.34", proto: "WebSocket", info: "WebSocket Ping [Masked]", len: "60 B", wire: { tcp: { sport: 52412, dport: 443, flags: "PA", data: { ws: { fin: 1, opcode: 9, opcodeName: "Ping", masked: 1, length: 0, maskKey: [18, 52, 86, 120] } } } } }, { lost: true }),
        { type: "note", at: "client", text: "PING LOST · HEARTBEAT TIMEOUT", tone: "rose" }
      ]
    },
    {
      title: "Backoff Reconnection & Clean Close",
      desc: "Auto-reconnect followed by opcode 8 clean closure",
      detail: "Client detects dead socket, applies exponential backoff, re-establishes WebSocket, and finally closes the session cleanly with a Close frame (opcode 0x8, code 1000).",
      facts: [["Reconnection", "Exponential backoff"], ["Close Opcode", "0x8 (Close)"], ["Status Code", "1000 (Normal Closure)"]],
      events: [
        u("client", "web", "rose", "CLOSE (1000)", ["Opcode: 0x8 (Close)", "Code: 1000 (Normal Closure)"], { time: "0.095s", src: "192.168.1.105", dst: "93.184.216.34", proto: "WebSocket", info: "WebSocket Close [Code 1000]", len: "62 B", wire: { tcp: { sport: 52412, dport: 443, flags: "PA", data: { ws: { fin: 1, opcode: 8, opcodeName: "Close", masked: 1, length: 2, maskKey: [10, 20, 30, 40], closeCode: 1000 } } } } }),
        { type: "note", at: "web", text: "RECONNECTED · CLEAN CLOSE (CODE 1000)", tone: "teal" }
      ]
    }
  ]
};

const lessonMqtt = {
  id: "mqtt",
  name: "MQTT",
  title: "Lightweight IoT Publish / Subscribe",
  layer: 7,
  nodes: ["client", "router", "internet", "web"],
  latency: { "client-web": 0.020, "client-router": 0.003, "router-web": 0.017, "client-internet": 0.011, "internet-web": 0.009 },
  legend: [["green", "CONNECT / CONNACK"], ["blue", "SUBSCRIBE / SUBACK"], ["amber", "PUBLISH (QoS 1)"], ["violet", "PUBACK"], ["rose", "Loss / Retransmit (DUP=1)"]],
  overview: {
    full: "Message Queuing Telemetry Transport",
    description: "MQTT is an ultra-lightweight publish/subscribe messaging protocol designed for battery-powered IoT devices and high-latency or constrained networks. It features a tiny 2-byte header, 3 QoS delivery guarantees, and a Last Will mechanism.",
    facts: [["Layer", "Application (Layer 7)"], ["Default Port", "1883 (plain) / 8883 (TLS)"], ["Transport", "TCP"], ["Pattern", "Publish / Subscribe via Broker"], ["QoS Levels", "0 (At most once), 1 (At least once), 2 (Exactly once)"], ["Defined In", "OASIS MQTT v3.1.1, v5.0"]]
  },
  outro: {
    title: "IoT Telemetry Stream Complete",
    desc: "Resilient telemetry with QoS 1 guarantees",
    text: "The IoT sensor connected with CleanSession=0 and published sensor readings. When PUBACK was lost, the client retransmitted with DUP=1 to guarantee delivery. Last Will and Testament ensured instant alert on broker disconnection.",
    facts: [["Header Overhead", "As low as 2 bytes"], ["Delivery Guarantee", "QoS 1 (PUBACK with DUP retry)"], ["State Persistence", "CleanSession=0 (Broker remembers state)"], ["Offline Alert", "LWT (Last Will and Testament)"]]
  },
  start: { nodes: ["client"], frame: "client" },
  steps: [
    {
      title: "MQTT CONNECT & CONNACK",
      desc: "Sensor connects with CleanSession=0 and Last Will",
      detail: "IoT sensor opens TCP connection to broker on port 1883. It sends CONNECT with CleanSession=0 (resumes saved subscriptions) and registers a Last Will and Testament (LWT) topic.",
      facts: [["Client ID", "sensor-node-01"], ["CleanSession", "0 (Persistent Session)"], ["Keep Alive", "60 seconds"]],
      events: [
        { type: "show", nodes: ["router", "internet", "web"], frame: "path" },
        u("client", "web", "green", "CONNECT", ["Client ID: sensor-node-01", "CleanSession: 0, Will: status/sensor-01"], { time: "0.000s", src: "192.168.1.105", dst: "93.184.216.34", proto: "MQTT", info: "Connect Command [sensor-node-01]", len: "92 B", wire: { tcp: { sport: 52414, dport: 1883, flags: "PA", data: { mqtt: { type: "CONNECT", typeCode: 1, flags: 0, remainingLength: 38, topic: "status/sensor-01", payload: "Client: sensor-node-01 (Will: offline)" } } } } }),
        u("web", "client", "green", "CONNACK", ["Connection Accepted", "Session Present: 1"], { time: "0.020s", src: "93.184.216.34", dst: "192.168.1.105", proto: "MQTT", info: "Connect Ack [Session Present: 1, Return: 0]", len: "64 B", wire: { tcp: { sport: 1883, dport: 52414, flags: "PA", data: { mqtt: { type: "CONNACK", typeCode: 2, flags: 0, remainingLength: 2, payload: "Return Code: 0 (Accepted)" } } } } }),
        { type: "note", at: "client", text: "MQTT CONNECTED: SESSION RESTORED", tone: "green" }
      ]
    },
    {
      title: "SUBSCRIBE to Commands",
      desc: "Subscribes with QoS 1 acknowledgment",
      detail: "Sensor subscribes to topic 'commands/node-01' with QoS 1. Broker responds with SUBACK granting QoS 1.",
      facts: [["Topic", "commands/node-01"], ["QoS Level", "1 (At least once)"], ["Packet ID", "1"]],
      events: [
        u("client", "web", "blue", "SUBSCRIBE", ["Topic: commands/node-01", "QoS: 1, Packet ID: 1"], { time: "0.042s", src: "192.168.1.105", dst: "93.184.216.34", proto: "MQTT", info: "Subscribe Request [commands/node-01 QoS: 1]", len: "78 B", wire: { tcp: { sport: 52414, dport: 1883, flags: "PA", data: { mqtt: { type: "SUBSCRIBE", typeCode: 8, flags: 2, remainingLength: 24, topic: "commands/node-01", packetId: 1, qos: 1 } } } } }),
        u("web", "client", "blue", "SUBACK", ["Packet ID: 1", "Granted QoS: 1"], { time: "0.062s", src: "93.184.216.34", dst: "192.168.1.105", proto: "MQTT", info: "Subscribe Ack [Packet ID: 1, QoS: 1]", len: "65 B", wire: { tcp: { sport: 1883, dport: 52414, flags: "PA", data: { mqtt: { type: "SUBACK", typeCode: 9, flags: 0, remainingLength: 3, packetId: 1, payload: "Granted QoS: [1]" } } } } })
      ]
    },
    {
      title: "QoS 1 PUBLISH & PUBACK Loss",
      desc: "Sensor reading published, PUBACK dropped in network",
      detail: "Sensor publishes telemetry (temp=24.5C). Under QoS 1, the broker sends a PUBACK, but the packet is dropped by cellular packet loss.",
      facts: [["Topic", "telemetry/temp"], ["Payload", "{'temp': 24.5, 'battery': 98}"], ["PUBACK Status", "LOST IN NETWORK"]],
      events: [
        u("client", "web", "amber", "PUBLISH (QoS 1)", ["Topic: telemetry/temp", "Packet ID: 42, QoS 1"], { time: "0.085s", src: "192.168.1.105", dst: "93.184.216.34", proto: "MQTT", info: "Publish Message [telemetry/temp QoS: 1]", len: "96 B", wire: { tcp: { sport: 52414, dport: 1883, flags: "PA", data: { mqtt: { type: "PUBLISH", typeCode: 3, flags: 2, qos: 1, remainingLength: 42, topic: "telemetry/temp", packetId: 42, payload: "{'temp': 24.5, 'battery': 98}" } } } } }),
        u("web", "client", "violet", "PUBACK (ID 42)", ["PUBACK Packet ID: 42", "Confirmation of receipt"], { time: "0.105s", src: "93.184.216.34", dst: "192.168.1.105", proto: "MQTT", info: "Publish Ack [Packet ID: 42]", len: "64 B", wire: { tcp: { sport: 1883, dport: 52414, flags: "PA", data: { mqtt: { type: "PUBACK", typeCode: 4, flags: 0, remainingLength: 2, packetId: 42 } } } } }, { lost: true }),
        { type: "note", at: "internet", text: "PUBACK DROPPED · ACK TIMEOUT", tone: "amber" }
      ]
    },
    {
      title: "DUP=1 Retransmission",
      desc: "Guaranteed delivery via retransmission with duplicate flag",
      detail: "Sensor's ACK timer expires. It retransmits the same PUBLISH message with DUP=1 set. The broker receives it and acknowledges with a fresh PUBACK.",
      facts: [["DUP Flag", "1 (Duplicate Retransmit)"], ["Packet ID", "42"], ["Result", "PUBACK safely received"]],
      events: [
        u("client", "web", "rose", "PUBLISH (DUP=1)", ["Retransmit with DUP=1", "Packet ID: 42"], { time: "0.140s", src: "192.168.1.105", dst: "93.184.216.34", proto: "MQTT", info: "Publish Message [DUP=1, ID: 42]", len: "96 B", wire: { tcp: { sport: 52414, dport: 1883, flags: "PA", data: { mqtt: { type: "PUBLISH", typeCode: 3, flags: 10, dup: true, qos: 1, remainingLength: 42, topic: "telemetry/temp", packetId: 42, payload: "{'temp': 24.5, 'battery': 98}" } } } } }),
        u("web", "client", "violet", "PUBACK (ID 42)", ["PUBACK Received", "Message Delivered"], { time: "0.160s", src: "93.184.216.34", dst: "192.168.1.105", proto: "MQTT", info: "Publish Ack [Packet ID: 42]", len: "64 B", wire: { tcp: { sport: 1883, dport: 52414, flags: "PA", data: { mqtt: { type: "PUBACK", typeCode: 4, flags: 0, remainingLength: 2, packetId: 42 } } } } }),
        { type: "note", at: "client", text: "PUBLISH RETRANSMITTED (DUP=1) · PUBACK RECEIVED", tone: "green" }
      ]
    },
    {
      title: "Broker Last Will Broadcast",
      desc: "Broker detects abrupt sensor failure and broadcasts LWT",
      detail: "Sensor battery dies abruptly. The broker notices missing PINGREQ keep-alives and broadcasts the sensor's registered Last Will ('offline') to all subscribers.",
      facts: [["Failure Cause", "Dead battery (Silent disconnect)"], ["LWT Topic", "status/sensor-01"], ["LWT Message", "'offline'"]],
      events: [
        { type: "note", at: "web", text: "BROKER BROADCASTS LAST WILL (LWT)", tone: "rose" }
      ]
    }
  ]
};

const lessonSse = {
  id: "sse",
  name: "SSE",
  title: "Server-Sent Events Streaming",
  layer: 7,
  nodes: ["client", "router", "internet", "web"],
  latency: { "client-web": 0.016, "client-router": 0.002, "router-web": 0.014, "client-internet": 0.009, "internet-web": 0.007 },
  legend: [["green", "HTTP Connection"], ["violet", "Event Stream Pushes"], ["amber", "Heartbeat Comment (:ping)"], ["rose", "Connection Drop / Auto-Resume"]],
  overview: {
    full: "Server-Sent Events",
    description: "Server-Sent Events (SSE) allows a server to push asynchronous text updates to the client over a persistent HTTP connection. Browsers use the built-in EventSource API, which includes automatic reconnection and stream resumption via Last-Event-ID.",
    facts: [["Layer", "Application (Layer 7)"], ["MIME Type", "text/event-stream"], ["Transport", "HTTP/1.1 or HTTP/2"], ["Direction", "Unidirectional (Server to Client)"], ["Resilience", "Native browser auto-reconnect with Last-Event-ID"], ["Standard", "HTML Living Standard / W3C"]]
  },
  outro: {
    title: "Event Stream Streamed & Resumed",
    desc: "Unidirectional event flow with zero-loss resumption",
    text: "The server pushed real-time ticker events over a single HTTP stream. When a middlebox dropped the idle connection, the browser EventSource reconnected after 3 seconds with Last-Event-ID: 101, recovering missed events automatically.",
    facts: [["Format", "text/event-stream lines (id, event, data)"], ["Directionality", "Unidirectional (server -> browser)"], ["Middlebox Keep-Alive", "Periodic colon comments (:keepalive)"], ["Recovery Mechanism", "Last-Event-ID HTTP header"]]
  },
  start: { nodes: ["client"], frame: "client" },
  steps: [
    {
      title: "SSE Stream Initiation",
      desc: "HTTP GET with text/event-stream response",
      detail: "Client invokes new EventSource('/events'). It sends an HTTP GET with Accept: text/event-stream. Server responds with 200 OK and Content-Type: text/event-stream.",
      facts: [["Accept", "text/event-stream"], ["Cache-Control", "no-cache"], ["Transfer-Encoding", "chunked"]],
      events: [
        { type: "show", nodes: ["router", "internet", "web"], frame: "path" },
        u("client", "web", "green", "GET /events", ["Accept: text/event-stream", "Cache-Control: no-cache"], { time: "0.000s", src: "192.168.1.105", dst: "93.184.216.34", proto: "HTTP", info: "GET /events HTTP/1.1 [Accept: text/event-stream]", len: "210 B", wire: { tcp: { sport: 52416, dport: 443, flags: "PA", data: { text: ["GET /events HTTP/1.1", "Host: example.com", "Accept: text/event-stream", "Cache-Control: no-cache"] } } } }),
        u("web", "client", "green", "200 OK (text/event-stream)", ["Content-Type: text/event-stream", "Connection: keep-alive"], { time: "0.016s", src: "93.184.216.34", dst: "192.168.1.105", proto: "HTTP", info: "HTTP/1.1 200 OK [Content-Type: text/event-stream]", len: "245 B", wire: { tcp: { sport: 443, dport: 52416, flags: "PA", data: { sse: { headers: ["HTTP/1.1 200 OK", "Content-Type: text/event-stream", "Cache-Control: no-cache", "Connection: keep-alive"] } } } } }),
        { type: "note", at: "client", text: "STREAM OPENED: text/event-stream", tone: "green" }
      ]
    },
    {
      title: "Real-Time Event Stream",
      desc: "Server pushes structured events with ID and data",
      detail: "Server pushes events formatted as lines (id, event, data) delimited by double newlines. Client browser fires onmessage handlers.",
      facts: [["Event 1 ID", "100 (Trade AAPL $198.50)"], ["Event 2 ID", "101 (Trade GOOG $175.20)"], ["Format", "Plain text lines"]],
      events: [
        u("web", "client", "violet", "EVENT id:100", ["id: 100", "event: trade", "data: AAPL $198.5"], { time: "0.035s", src: "93.184.216.34", dst: "192.168.1.105", proto: "SSE", info: "SSE Event id: 100 (trade)", len: "128 B", wire: { tcp: { sport: 443, dport: 52416, flags: "PA", data: { sse: { id: 100, event: "trade", data: "{'sym':'AAPL','p':198.5}" } } } } }),
        u("web", "client", "violet", "EVENT id:101", ["id: 101", "event: trade", "data: GOOG $175.2"], { time: "0.055s", src: "93.184.216.34", dst: "192.168.1.105", proto: "SSE", info: "SSE Event id: 101 (trade)", len: "128 B", wire: { tcp: { sport: 443, dport: 52416, flags: "PA", data: { sse: { id: 101, event: "trade", data: "{'sym':'GOOG','p':175.2}" } } } } })
      ]
    },
    {
      title: "Proxy Idle Drop",
      desc: "Middlebox drops idle connection",
      detail: "During a quiet trading period with no price changes, an intermediate proxy times out the idle TCP connection and drops the socket.",
      facts: [["Cause", "NAT / Firewall idle timeout"], ["Socket State", "Abruptly terminated"], ["Client State", "Detects connection drop"]],
      events: [
        { type: "note", at: "internet", text: "PROXY DROP: CONNECTION TERMINATED", tone: "rose" }
      ]
    },
    {
      title: "EventSource Auto-Resume",
      desc: "Native reconnect resuming from Last-Event-ID: 101",
      detail: "The browser's native EventSource automatically reconnects after a short backoff, attaching the HTTP header Last-Event-ID: 101. The server resumes immediately from ID: 102 with zero data loss!",
      facts: [["Header Sent", "Last-Event-ID: 101"], ["Resume Event", "ID: 102 (MSFT $420.10)"], ["Data Lost", "0 bytes"]],
      events: [
        u("client", "web", "green", "GET /events (RESUME)", ["Last-Event-ID: 101", "Automatic reconnect"], { time: "0.095s", src: "192.168.1.105", dst: "93.184.216.34", proto: "HTTP", info: "GET /events [Last-Event-ID: 101]", len: "235 B", wire: { tcp: { sport: 52416, dport: 443, flags: "PA", data: { text: ["GET /events HTTP/1.1", "Host: example.com", "Accept: text/event-stream", "Last-Event-ID: 101"] } } } }),
        u("web", "client", "violet", "EVENT id:102", ["id: 102", "event: trade", "data: MSFT $420.1"], { time: "0.115s", src: "93.184.216.34", dst: "192.168.1.105", proto: "SSE", info: "SSE Event id: 102 (trade)", len: "128 B", wire: { tcp: { sport: 443, dport: 52416, flags: "PA", data: { sse: { id: 102, event: "trade", data: "{'sym':'MSFT','p':420.1}" } } } } }),
        { type: "note", at: "client", text: "STREAM RESUMED FROM ID: 101", tone: "green" }
      ]
    }
  ]
};

const lessonChunked = {
  id: "chunked",
  name: "Chunked",
  title: "Dynamic Chunked Streaming",
  layer: 7,
  nodes: ["client", "router", "internet", "web"],
  latency: { "client-web": 0.018, "client-router": 0.002, "router-web": 0.016, "client-internet": 0.010, "internet-web": 0.008 },
  legend: [["amber", "HTTP Request"], ["violet", "Chunked Data (Hex Sizes)"], ["rose", "Loss / Mid-Stream Error"], ["green", "Terminal Chunk & Trailer"]],
  overview: {
    full: "HTTP Chunked Transfer Encoding",
    description: "Chunked transfer encoding is a streaming mechanism in HTTP/1.1 where data is sent as a series of size-prefixed chunks rather than needing an upfront Content-Length header. This enables immediate streaming for database results, file generation, and LLM responses.",
    facts: [["Layer", "Application (Layer 7)"], ["Header", "Transfer-Encoding: chunked"], ["Transport", "TCP"], ["Chunk Format", "<hex size>\\r\\n<data>\\r\\n"], ["Termination", "0\\r\\n\\r\\n (zero-length chunk)"], ["Defined In", "RFC 9112 (Section 7.1)"]]
  },
  outro: {
    title: "Dynamic Stream Completed",
    desc: "Streaming data without upfront Content-Length",
    text: "The server began transmitting immediately as data was generated. When an intermediate chunk was lost, TCP retransmitted to maintain stream integrity. The stream ended with a terminal zero-byte chunk and a trailing cryptographic checksum.",
    facts: [["Memory Buffer", "Zero: stream chunks as generated"], ["Delimiter", "Hex length + CRLF per chunk"], ["Trailer Support", "Post-stream checksums (X-SHA256)"], ["Failure Mode", "TCP connection teardown if stream aborts"]]
  },
  start: { nodes: ["client"], frame: "client" },
  steps: [
    {
      title: "Chunked Transfer Request",
      desc: "Response with Transfer-Encoding: chunked",
      detail: "Client requests an export of dynamically generated user records. Since the server does not know the final payload size, it responds with Transfer-Encoding: chunked instead of Content-Length.",
      facts: [["Method", "GET /export/records"], ["Encoding", "Transfer-Encoding: chunked"], ["Trailer Promised", "Trailer: X-Checksum-SHA256"]],
      events: [
        { type: "show", nodes: ["router", "internet", "web"], frame: "path" },
        u("client", "web", "amber", "GET /export/records", ["GET /export/records HTTP/1.1", "Host: example.com"], { time: "0.000s", src: "192.168.1.105", dst: "93.184.216.34", proto: "HTTP", info: "GET /export/records HTTP/1.1", len: "160 B", wire: { tcp: { sport: 52418, dport: 80, flags: "PA", data: { text: ["GET /export/records HTTP/1.1", "Host: example.com"] } } } }),
        u("web", "client", "green", "200 OK (chunked)", ["Transfer-Encoding: chunked", "Trailer: X-Checksum-SHA256"], { time: "0.018s", src: "93.184.216.34", dst: "192.168.1.105", proto: "HTTP", info: "HTTP/1.1 200 OK [Transfer-Encoding: chunked]", len: "215 B", wire: { tcp: { sport: 80, dport: 52418, flags: "PA", data: { text: ["HTTP/1.1 200 OK", "Transfer-Encoding: chunked", "Trailer: X-Checksum-SHA256"] } } } }),
        { type: "note", at: "client", text: "CHUNKED STREAM INITIATED", tone: "green" }
      ]
    },
    {
      title: "Hex-Sized Data Chunks",
      desc: "Server streams data without upfront Content-Length",
      detail: "The server sends the first 26 bytes of JSON preceded by hex size 1A (26 in decimal) and CRLF. The client parses chunk 1 immediately while the database query continues.",
      facts: [["Hex Size", "1A (26 bytes)"], ["Chunk Payload", "{'user':'Alice','score':95}"], ["Framing", "<hex>\\r\\n<data>\\r\\n"]],
      events: [
        u("web", "client", "violet", "CHUNK 1 (1A)", ["Chunk size: 1A (26 bytes)", "{'user':'Alice','score':95}"], { time: "0.038s", src: "93.184.216.34", dst: "192.168.1.105", proto: "HTTP", info: "HTTP Chunked: 1A bytes (26)", len: "90 B", wire: { tcp: { sport: 80, dport: 52418, flags: "PA", data: { chunked: { hexSize: "1A", byteCount: 26, data: "{'user':'Alice','score':95}" } } } } })
      ]
    },
    {
      title: "Intermediate Chunk Loss",
      desc: "Lost chunk recovered by TCP transport",
      detail: "Server sends Chunk 2 (size 24 hex = 36 bytes), but the packet is lost. The client TCP layer stalls the application stream, triggers a retransmission via SACK, and restores byte order.",
      facts: [["Chunk 2 Size", "24 (36 bytes)"], ["Status", "LOST IN TRANSIT"], ["Recovery", "TCP SACK retransmission"]],
      events: [
        u("web", "client", "violet", "CHUNK 2 (24)", ["Chunk size: 24 (36 bytes)", "{'user':'Bob','score':88}"], { time: "0.060s", src: "93.184.216.34", dst: "192.168.1.105", proto: "HTTP", info: "HTTP Chunked: 24 bytes (36)", len: "100 B", wire: { tcp: { sport: 80, dport: 52418, flags: "PA", data: { chunked: { hexSize: "24", byteCount: 36, data: "{'user':'Bob','score':88}" } } } } }, { lost: true }),
        { type: "note", at: "internet", text: "CHUNK 2 LOST · RETRANSMITTED", tone: "amber" },
        u("web", "client", "violet", "CHUNK 2 (RESENT)", ["Chunk 2 recovered", "Delivered to client"], { time: "0.090s", src: "93.184.216.34", dst: "192.168.1.105", proto: "HTTP", info: "HTTP Chunked: 24 bytes (Resent)", len: "100 B", wire: { tcp: { sport: 80, dport: 52418, flags: "PA", data: { chunked: { hexSize: "24", byteCount: 36, data: "{'user':'Bob','score':88}" } } } } })
      ]
    },
    {
      title: "Mid-Stream Database Abort",
      desc: "Server tears down connection on fatal streaming error",
      detail: "In chunked encoding, HTTP headers (200 OK) have already been sent! If the database crashes mid-stream, the server CANNOT change status to 500. It must abort the TCP connection with TCP RST to signal payload corruption.",
      facts: [["Limitation", "Headers already committed as 200 OK"], ["Error Mechanism", "TCP RST abruptly tears down stream"], ["Client Defense", "Recognizes truncated body"]],
      events: [
        { type: "note", at: "web", text: "DATABASE ABORT · TCP RST ERROR HANDLING", tone: "rose" }
      ]
    },
    {
      title: "Terminal Zero Chunk & Trailer",
      desc: "Stream ends with 0\\r\\n and cryptographic checksum",
      detail: "On successful completion, server emits chunk size 0\\r\\n followed by trailing headers containing a SHA-256 integrity hash of the streamed content.",
      facts: [["Terminal Chunk", "0\\r\\n"], ["Trailer Header", "X-Checksum-SHA256"], ["Integrity", "Cryptographic verification of streamed stream"]],
      events: [
        u("web", "client", "green", "CHUNK 0 + TRAILER", ["Terminal chunk: 0", "X-Checksum-SHA256: 4f9a2b..."], { time: "0.130s", src: "93.184.216.34", dst: "192.168.1.105", proto: "HTTP", info: "HTTP Chunked: 0 bytes + Trailers", len: "145 B", wire: { tcp: { sport: 80, dport: 52418, flags: "PA", data: { chunked: { hexSize: "0", byteCount: 0, trailers: ["X-Checksum-SHA256: 4f9a2b719c8d3e..."] } } } } }),
        { type: "note", at: "client", text: "STREAM TERMINATED · CHECKSUM VERIFIED", tone: "green" }
      ]
    }
  ]
};

const lessonGrpc = {
  id: "grpc",
  name: "gRPC",
  title: "High-Performance RPC over HTTP/2",
  layer: 7,
  nodes: ["client", "router", "internet", "web"],
  latency: { "client-web": 0.015, "client-router": 0.002, "router-web": 0.013, "client-internet": 0.008, "internet-web": 0.007 },
  legend: [["green", "Unary RPC Call"], ["violet", "gRPC Protobuf Response"], ["rose", "Trailers: Error Status 5 (NOT_FOUND)"], ["amber", "Deadline Exceeded (Timeout)"]],
  overview: {
    full: "gRPC Remote Procedure Calls",
    description: "gRPC is a high-performance open-source RPC framework created by Google. Built on HTTP/2 transport and Protocol Buffers (Protobuf) binary serialization, it provides strongly-typed contracts, streaming RPCs, deadlines, and status codes in HTTP/2 trailers.",
    facts: [["Layer", "Application (Layer 7)"], ["Default Port", "50051 (or 443)"], ["Transport", "HTTP/2 (Binary Framing)"], ["Serialization", "Protocol Buffers (proto3)"], ["Framing", "5-byte prefix (Compressed flag + Length)"], ["Status Codes", "16 canonical gRPC status codes in trailers"]]
  },
  outro: {
    title: "RPC Execution Complete",
    desc: "Typed remote procedure call with trailer status",
    text: "The client invoked a typed RPC over HTTP/2. gRPC serialized parameters with Protocol Buffers into compact binary bytes. When an error occurred, the server returned canonical status code 5 (NOT_FOUND) directly in HTTP/2 trailers without rebuilding headers.",
    facts: [["Serialization Efficiency", "Up to 10x smaller than JSON"], ["Error Propagation", "grpc-status & grpc-message in trailers"], ["Deadline Support", "grpc-timeout header with RST_STREAM cancel"], ["Streaming Capabilities", "Unary, Client/Server streaming, Bidirectional"]]
  },
  start: { nodes: ["client"], frame: "client" },
  steps: [
    {
      title: "Unary gRPC Request",
      desc: "POST /OrderService/GetOrder with Protobuf payload",
      detail: "Client invokes unary RPC GetOrder(order_id=1042). gRPC sends an HTTP/2 HEADERS frame with content-type: application/grpc and a DATA frame carrying the 5-byte length prefix and binary Protobuf payload.",
      facts: [["RPC Method", "POST /OrderService/GetOrder"], ["Content-Type", "application/grpc"], ["Protobuf Tag", "Field 1 (order_id: 1042)"]],
      events: [
        { type: "show", nodes: ["router", "internet", "web"], frame: "path" },
        u("client", "web", "green", "gRPC REQUEST", ["POST /OrderService/GetOrder", "order_id: 1042 (Protobuf)"], { time: "0.000s", src: "192.168.1.105", dst: "93.184.216.34", proto: "gRPC", info: "gRPC Call: /OrderService/GetOrder [order_id: 1042]", len: "115 B", wire: { tcp: { sport: 52420, dport: 50051, flags: "PA", data: { grpc: { service: "OrderService", method: "GetOrder", compressed: 0, length: 6, fields: [{ tag: 1, name: "order_id", wireType: 0, val: 1042 }] } } } } }),
        { type: "note", at: "client", text: "gRPC UNARY INVOCATION", tone: "green" }
      ]
    },
    {
      title: "Protobuf Response & Status OK",
      desc: "Typed response with grpc-status: 0 in trailers",
      detail: "Server processes request and returns HTTP/2 HEADERS (:status 200), DATA (Protobuf OrderResponse), and trailing HEADERS with grpc-status: 0 (OK).",
      facts: [["Order ID", "1042"], ["Status", "'SHIPPED'"], ["grpc-status", "0 (OK in trailers)"]],
      events: [
        u("web", "client", "violet", "gRPC RESPONSE (OK)", ["OrderResponse (Protobuf)", "grpc-status: 0 (OK)"], { time: "0.018s", src: "93.184.216.34", dst: "192.168.1.105", proto: "gRPC", info: "gRPC Reply: OK [grpc-status: 0]", len: "148 B", wire: { tcp: { sport: 50051, dport: 52420, flags: "PA", data: { grpc: { service: "OrderService", method: "GetOrder", compressed: 0, length: 18, fields: [{ tag: 1, name: "order_id", wireType: 0, val: 1042 }, { tag: 2, name: "status", wireType: 2, val: "SHIPPED" }], trailers: [{ name: "grpc-status", val: "0 (OK)" }] } } } } }),
        { type: "note", at: "client", text: "gRPC STATUS 0: OK", tone: "green" }
      ]
    },
    {
      title: "Error Status: NOT_FOUND",
      desc: "Canonical gRPC error code 5 returned in trailers",
      detail: "Client requests non-existent order #9999. In gRPC, the HTTP status is still 200 OK, but the trailing headers convey canonical status 5 (NOT_FOUND) with an error description.",
      facts: [["HTTP Status", "200 (Transport OK)"], ["grpc-status", "5 (NOT_FOUND)"], ["grpc-message", "order 9999 does not exist"]],
      events: [
        u("client", "web", "green", "GET ORDER #9999", ["POST /OrderService/GetOrder", "order_id: 9999"], { time: "0.040s", src: "192.168.1.105", dst: "93.184.216.34", proto: "gRPC", info: "gRPC Call: /OrderService/GetOrder [order_id: 9999]", len: "115 B", wire: { tcp: { sport: 52420, dport: 50051, flags: "PA", data: { grpc: { service: "OrderService", method: "GetOrder", compressed: 0, length: 6, fields: [{ tag: 1, name: "order_id", wireType: 0, val: 9999 }] } } } } }),
        u("web", "client", "rose", "gRPC STATUS 5", ["Trailers: grpc-status: 5", "NOT_FOUND: order not found"], { time: "0.058s", src: "93.184.216.34", dst: "192.168.1.105", proto: "gRPC", info: "gRPC Reply: 5 NOT_FOUND", len: "130 B", wire: { tcp: { sport: 50051, dport: 52420, flags: "PA", data: { grpc: { service: "OrderService", method: "GetOrder", compressed: 0, length: 0, trailers: [{ name: "grpc-status", val: "5 (NOT_FOUND)" }, { name: "grpc-message", val: "order 9999 does not exist" }] } } } } }),
        { type: "note", at: "client", text: "GRPC STATUS: 5 NOT_FOUND", tone: "rose" }
      ]
    },
    {
      title: "Strict Deadline Exceeded",
      desc: "Timeout triggers client RST_STREAM and code 4 status",
      detail: "Client sets a strict deadline with grpc-timeout: 20m (20 ms). When the database query takes too long, the client cancels the call by sending HTTP/2 RST_STREAM and raises DEADLINE_EXCEEDED (code 4).",
      facts: [["grpc-timeout", "20m (20 milliseconds)"], ["Cancellation", "RST_STREAM (CANCEL)"], ["Result Code", "4 (DEADLINE_EXCEEDED)"]],
      events: [
        u("client", "web", "amber", "RST_STREAM (TIMEOUT)", ["Deadline exceeded (20ms)", "RST_STREAM CANCEL"], { time: "0.115s", src: "192.168.1.105", dst: "93.184.216.34", proto: "HTTP/2", info: "RST_STREAM Stream: 1 [CANCEL]", len: "64 B", wire: { tcp: { sport: 52420, dport: 50051, flags: "PA", data: { http2: { type: "RST_STREAM", streamId: 1, typeCode: 3, flags: 0, errorCode: 8, errorName: "CANCEL" } } } } }),
        { type: "note", at: "client", text: "DEADLINE EXCEEDED · TIMEOUT", tone: "amber" }
      ]
    }
  ]
};
`;

console.log("Lessons code generated. Length:", lessonsCode.length);

export { lessonsCode };
