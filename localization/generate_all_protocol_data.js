// Builder for 7 Modern Protocols Data, Decoders, and Multilingual Dictionary
import fs from 'fs';

// Helper for row creation
function makeRow(time, src, dst, proto, info, len, wire) {
  return { time, src, dst, proto, info, len, wire };
}

// 1. Decoder source code as string to inject into index-4NePqLyW.js
export const decodersCode = `
function decodeHttp2(t) {
  const s = new me("http2", "HTTP/2 · " + (t.type || "Frame") + " · Stream " + (t.streamId ?? 0));
  s.field("Length", (t.length ?? 0) + " bytes", () => s.u24(t.length ?? 0), { depth: 0, note: "Length of the frame payload in octets (24 bits)." });
  const typeMap = { 0: "DATA (0x0)", 1: "HEADERS (0x1)", 2: "PRIORITY (0x2)", 3: "RST_STREAM (0x3)", 4: "SETTINGS (0x4)", 5: "PUSH_PROMISE (0x5)", 6: "PING (0x6)", 7: "GOAWAY (0x7)", 8: "WINDOW_UPDATE (0x8)", 9: "CONTINUATION (0x9)" };
  s.field("Type", typeMap[t.typeCode ?? 0] || String(t.type), () => s.u8(t.typeCode ?? 0), { depth: 0, note: "Defines the frame format and semantics." });
  s.field("Flags", "0x" + (t.flags ?? 0).toString(16).padStart(2, "0"), () => s.u8(t.flags ?? 0), { depth: 0, note: "Flags specific to the frame type." });
  s.field("Stream Identifier", String(t.streamId ?? 0), () => s.u32((t.streamId ?? 0) & 0x7fffffff), { depth: 0, note: "Identifies the stream this frame belongs to (0 is control)." });
  if (t.headers) {
    t.headers.forEach(h => s.field("Header", h, () => s.ascii(h), { mono: true, depth: 1 }));
  }
  if (t.data) {
    s.field("Payload", String(t.data), () => s.ascii(String(t.data)), { mono: true, depth: 1 });
  }
  if (t.params) {
    t.params.forEach(p => s.field("Setting", p.id + " = " + p.val, () => s.u16(p.idCode ?? 1).u32(p.val), { depth: 1 }));
  }
  if (t.errorCode !== undefined) {
    s.field("Error Code", "0x" + t.errorCode.toString(16) + " (" + (t.errorName || "ERROR") + ")", () => s.u32(t.errorCode), { depth: 1, tone: "rose" });
  }
  return s;
}

function decodeQuic(t) {
  const s = new me("quic", "QUIC · " + (t.packetType || "Datagram") + " · DCID: " + (t.dcid || ""));
  s.field("Header Form", t.isLong ? "1 (Long Header)" : "0 (Short Header)", () => s.u8(t.isLong ? 0xc0 : 0x40), { note: "Long headers used during handshake; short headers for 1-RTT application data." });
  if (t.isLong) {
    s.field("Version", "0x00000001 (QUIC v1)", () => s.u32(1), { note: "QUIC Version 1 (RFC 9000)." });
  }
  s.field("Destination CID", String(t.dcid), () => s.ascii(String(t.dcid).slice(0, 8)), { mono: true, note: "Unique Connection ID enabling seamless connection migration." });
  s.field("Packet Number", "#" + t.packetNumber, () => s.u16(t.packetNumber), { note: "Monotonically increasing packet number (never reused)." });
  if (t.frames) {
    t.frames.forEach(f => {
      s.field("Frame", f.type + (f.streamId !== undefined ? " · Stream " + f.streamId : ""), () => {
        s.u8(f.typeCode ?? 8);
        if (f.data) s.ascii(String(f.data));
      }, { depth: 1, mono: true, note: f.note });
    });
  }
  return s;
}

function decodeWs(t) {
  const s = new me("ws", "WebSocket · " + (t.opcodeName || "Frame") + " · " + (t.length ?? 0) + " bytes");
  s.field("FIN", t.fin ? "1 (Final fragment)" : "0 (More fragments)", () => s.u8(0x80 | ((t.opcode ?? 1) & 0x0f)), { note: "Indicates whether this is the final fragment in a message." });
  s.field("Opcode", (t.opcode ?? 1) + " (" + (t.opcodeName || "Text") + ")", () => {}, { depth: 1, note: "0x1: Text, 0x2: Binary, 0x8: Close, 0x9: Ping, 0xA: Pong" });
  s.field("Masked", t.masked ? "1 (Client XOR masked)" : "0 (Unmasked)", () => s.u8((t.masked ? 0x80 : 0x00) | Math.min(125, t.length ?? 0)), { note: "Client-to-server frames MUST be masked to prevent proxy caching attacks." });
  s.field("Payload Length", (t.length ?? 0) + " bytes", () => {}, { depth: 1 });
  if (t.masked && t.maskKey) {
    s.field("Masking Key", t.maskKey.map(b => b.toString(16).padStart(2, "0")).join(" "), () => {
      t.maskKey.forEach(b => s.u8(b));
    }, { mono: true, note: "4-byte random key used to XOR payload." });
  }
  if (t.text) {
    s.field("Payload Data", String(t.text), () => s.ascii(String(t.text)), { mono: true, depth: 1 });
  }
  if (t.closeCode !== undefined) {
    s.field("Close Code", t.closeCode + " (Normal Closure)", () => s.u16(t.closeCode), { depth: 1 });
  }
  return s;
}

function decodeMqtt(t) {
  const s = new me("mqtt", "MQTT · " + (t.type || "Packet") + " · QoS " + (t.qos ?? 0));
  s.field("Control Packet Type", (t.typeCode ?? 1) + " (" + (t.type || "CONNECT") + ")", () => s.u8(((t.typeCode & 0x0f) << 4) | ((t.flags || 0) & 0x0f)), { note: "Identifies MQTT message type: 1=CONNECT, 3=PUBLISH, 4=PUBACK, etc." });
  s.field("Flags", "DUP=" + (t.dup ? 1 : 0) + ", QoS=" + (t.qos ?? 0) + ", RETAIN=" + (t.retain ? 1 : 0), () => {}, { depth: 1 });
  s.field("Remaining Length", (t.remainingLength ?? 0) + " bytes", () => s.u8(t.remainingLength ?? 0), { note: "Length of variable header + payload." });
  if (t.topic) {
    s.field("Topic", String(t.topic), () => s.u16(t.topic.length).ascii(String(t.topic)), { depth: 1, mono: true });
  }
  if (t.packetId !== undefined) {
    s.field("Packet Identifier", String(t.packetId), () => s.u16(t.packetId), { depth: 1, note: "Used for QoS 1 & 2 delivery acknowledgments." });
  }
  if (t.payload) {
    s.field("Payload", String(t.payload), () => s.ascii(String(t.payload)), { depth: 1, mono: true });
  }
  return s;
}

function decodeSse(t) {
  const s = new me("sse", "SSE · Event Stream · ID " + (t.id !== undefined ? t.id : "None"));
  if (t.headers) {
    t.headers.forEach(h => s.field("Header", h, () => s.ascii(h + "\\r\\n"), { mono: true }));
  }
  if (t.event) {
    s.field("event", t.event, () => s.ascii("event: " + t.event + "\\r\\n"), { mono: true, depth: 1 });
  }
  if (t.id !== undefined) {
    s.field("id", String(t.id), () => s.ascii("id: " + t.id + "\\r\\n"), { mono: true, depth: 1 });
  }
  if (t.data) {
    s.field("data", String(t.data), () => s.ascii("data: " + t.data + "\\r\\n\\r\\n"), { mono: true, depth: 1 });
  }
  return s;
}

function decodeChunked(t) {
  const s = new me("chunked", "HTTP Chunked · Size: " + (t.hexSize || "0"));
  s.field("Chunk Size (Hex)", (t.hexSize || "0") + " (" + (t.byteCount ?? 0) + " bytes)", () => s.ascii((t.hexSize || "0") + "\\r\\n"), { mono: true, note: "Hexadecimal length of the following data octets." });
  if (t.data) {
    s.field("Chunk Data", String(t.data), () => s.ascii(String(t.data) + "\\r\\n"), { mono: true, depth: 1 });
  }
  if (t.trailers) {
    t.trailers.forEach(tr => s.field("Trailer", tr, () => s.ascii(tr + "\\r\\n"), { mono: true, depth: 1, note: "Trailing headers sent after the zero chunk." }));
  }
  return s;
}

function decodeGrpc(t) {
  const s = new me("grpc", "gRPC · " + (t.service || "Service") + "/" + (t.method || "Method"));
  s.field("Compressed-Flag", (t.compressed ? 1 : 0) + " (" + (t.compressed ? "Compressed" : "Uncompressed") + ")", () => s.u8(t.compressed ? 1 : 0), { note: "1-byte flag indicating gzip/deflate compression." });
  s.field("Message-Length", (t.length ?? 0) + " bytes", () => s.u32(t.length ?? 0), { note: "4-byte big-endian length of the protobuf payload." });
  if (t.fields) {
    t.fields.forEach(f => s.field("Field " + f.tag + " (" + f.name + ")", String(f.val), () => s.u8((f.tag << 3) | (f.wireType ?? 0)).ascii(String(f.val)), { mono: true, depth: 1 }));
  }
  if (t.trailers) {
    t.trailers.forEach(tr => s.field("Trailer", tr.name + ": " + tr.val, () => s.ascii(tr.name + ": " + tr.val), { mono: true, depth: 1, note: "Delivered in HTTP/2 trailing HEADERS frame." }));
  }
  return s;
}
`;

console.log("Decoders code string prepared. Length:", decodersCode.length);
