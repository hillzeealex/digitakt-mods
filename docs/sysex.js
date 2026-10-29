// Lit un fichier OS Elektron (.syx) et vérifie qu'il est complet avant tout envoi :
// un message d'en-tête, les messages de données numérotés, un message de fin qui répète l'en-tête.

export const DEVICES = { 0x0a: 'Digitakt', 0x14: 'Digitakt II' };

// Pause entre deux messages. shortcut: valeur prudente, non mesurée sur une vraie machine
// (digikit utilise 2 ms en USB) ; à baisser une fois l'envoi confirmé sur Digitakt.
export const PACE_MS = 50;

const ELEKTRON = [0xf0, 0x00, 0x20, 0x3c];

export function parseOs(bytes) {
  const msgs = [];
  for (let i = 0; i < bytes.length; ) {
    if (bytes[i] !== 0xf0) throw new Error("ce n'est pas un fichier .syx");
    const end = bytes.indexOf(0xf7, i);
    if (end < 0) throw new Error('fichier coupé (téléchargement incomplet ?)');
    msgs.push(bytes.subarray(i, end + 1));
    i = end + 1;
  }
  if (msgs.length < 3) throw new Error("ce n'est pas un OS Elektron");
  const head = msgs[0], foot = msgs[msgs.length - 1];
  const framing = (m, kind) => m.length === 16 && ELEKTRON.every((b, k) => m[k] === b) && m[6] === 0x7f && m[7] === kind;
  if (!framing(head, 1) || !framing(foot, 2)) throw new Error("ce n'est pas un OS Elektron");
  for (let k = 8; k < 15; k++) if (head[k] !== foot[k]) throw new Error('début et fin du fichier ne correspondent pas');
  const device = DEVICES[head[4]];
  if (!device) throw new Error("ce fichier n'est pas pour une Digitakt");
  const num = (m, k) => (m[k] << 14) | (m[k + 1] << 7) | m[k + 2];
  const start = num(head, 9), count = num(head, 12), data = msgs.slice(1, -1);
  if (data.length !== count) throw new Error(`il manque des morceaux : ${data.length} sur ${count}`);
  data.forEach((m, n) => {
    if (m.length !== 128 || m[4] !== head[4] || m[6] !== 0x7e || num(m, 7) !== start + n)
      throw new Error(`morceau ${n + 1} abîmé`);
  });
  return { device, msgs, seconds: Math.ceil((msgs.length * PACE_MS) / 1000) };
}
