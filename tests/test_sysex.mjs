import { test } from 'node:test';
import assert from 'node:assert/strict';
import { parseOs } from '../docs/sysex.js';

// Un faux OS Digitakt au même format que celui d'Elektron : en-tête, n données numérotées, fin.
function fakeOs(n, dev = 0x0a) {
  const num = (v) => [(v >> 14) & 0x7f, (v >> 7) & 0x7f, v & 0x7f];
  const frame = (kind) => [0xf0, 0x00, 0x20, 0x3c, dev, 0x00, 0x7f, kind, 0x05, ...num(242), ...num(n), 0xf7];
  const data = (i) => [0xf0, 0x00, 0x20, 0x3c, dev, 0x00, 0x7e, ...num(242 + i), ...new Array(117).fill(0), 0xf7];
  return [frame(1), ...Array.from({ length: n }, (_, i) => data(i)), frame(2)];
}
const bytes = (msgs) => new Uint8Array(msgs.flat());

test('un OS complet est accepté', () => {
  assert.equal(parseOs(bytes(fakeOs(5))).device, 'Digitakt');
  assert.equal(parseOs(bytes(fakeOs(5, 0x14))).device, 'Digitakt II');
  assert.equal(parseOs(bytes(fakeOs(5))).msgs.length, 7);
});

test('un message manquant est refusé', () => {
  const m = fakeOs(5);
  m.splice(3, 1);
  assert.throws(() => parseOs(bytes(m)), /il manque/);
});

test('des messages dans le désordre sont refusés', () => {
  const m = fakeOs(5);
  [m[2], m[3]] = [m[3], m[2]];
  assert.throws(() => parseOs(bytes(m)), /abîmé/);
});

test("un fichier coupé, d'une autre machine ou pas un .syx est refusé", () => {
  assert.throws(() => parseOs(bytes(fakeOs(5)).subarray(0, 300)), /coupé/);
  assert.throws(() => parseOs(bytes(fakeOs(5, 0x0c))), /pas pour une Digitakt/);
  assert.throws(() => parseOs(new TextEncoder().encode('{"mods": []}')), /pas un fichier/);
});
