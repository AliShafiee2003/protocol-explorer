import fs from 'fs';
import { decodersCode } from './generate_all_protocol_data.js';
import { lessonsCode } from './generate_expanded_protocols_bundle.js';

// Restore clean original
let indexJs = fs.readFileSync('assets/index-4NePqLyW.js.orig', 'utf8');

// 1. Inject decoders check into ed(e, t)
const edOld = 'if(t.rtp)return id(t.rtp);throw new Error(`unknown payload for ${e.info}`)';
const edNew = `if(t.rtp)return id(t.rtp);
if(t.http2)return decodeHttp2(t.http2);
if(t.quic)return decodeQuic(t.quic);
if(t.ws)return decodeWs(t.ws);
if(t.mqtt)return decodeMqtt(t.mqtt);
if(t.sse)return decodeSse(t.sse);
if(t.chunked)return decodeChunked(t.chunked);
if(t.grpc)return decodeGrpc(t.grpc);
throw new Error(\`unknown payload for \${e.info}\`)`;

if (!indexJs.includes(edOld)) {
  throw new Error("Could not find target in ed(e, t)");
}
indexJs = indexJs.replace(edOld, edNew);
console.log("1. Replaced ed payload router.");

// 2. Extend Xt catalog
const xtTarget = '{id:"tls",name:"TLS/SSL",full:"Transport Layer Security",group:"security"}]';
const xtReplacement = '{id:"tls",name:"TLS/SSL",full:"Transport Layer Security",group:"security"},{id:"http2",name:"HTTP/2",full:"Hypertext Transfer Protocol Version 2",group:"application"},{id:"http3",name:"HTTP/3",full:"HTTP/3 over QUIC",group:"application"},{id:"ws",name:"WebSocket",full:"WebSocket Protocol",group:"application"},{id:"mqtt",name:"MQTT",full:"Message Queuing Telemetry Transport",group:"application"},{id:"sse",name:"SSE",full:"Server-Sent Events",group:"application"},{id:"chunked",name:"Chunked",full:"HTTP Chunked Transfer Encoding",group:"application"},{id:"grpc",name:"gRPC",full:"gRPC Remote Procedure Calls",group:"application"}]';

if (!indexJs.includes(xtTarget)) {
  throw new Error("Could not find target in Xt catalog");
}
indexJs = indexJs.replace(xtTarget, xtReplacement);
console.log("2. Replaced Xt catalog.");

// 3. Split the const chain before cs and inject decoders + lessons
const csTarget = ',cs={http:pi,https:hi,tcp:ui,udp:fi,ip:mi,dns:wi,dhcp:Si,icmp:Ti,smtp:_i,pop3:Ki,imap:Xi,ftp:Zi,ssh:ul,tls:wl}';
if (!indexJs.includes(csTarget)) {
  throw new Error("Could not find target in cs map");
}

const marker = '// === EXPANDED_PROTOCOLS_CODE ===';
const csReplacement = `;
${marker}
${decodersCode}
${lessonsCode}
const cs={http:pi,https:hi,tcp:ui,udp:fi,ip:mi,dns:wi,dhcp:Si,icmp:Ti,smtp:_i,pop3:Ki,imap:Xi,ftp:Zi,ssh:ul,tls:wl,http2:lessonHttp2,http3:lessonHttp3,ws:lessonWs,mqtt:lessonMqtt,sse:lessonSse,chunked:lessonChunked,grpc:lessonGrpc}`;

indexJs = indexJs.replace(csTarget, csReplacement);
console.log("3. Injected decoders, lessons, and extended cs with const declaration.");

fs.writeFileSync('assets/index-4NePqLyW.js', indexJs, 'utf8');
console.log("Successfully saved assets/index-4NePqLyW.js!");
