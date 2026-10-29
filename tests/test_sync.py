import hashlib
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'tools'))
import sync  # noqa: E402


class VerifyTest(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp())
        (self.root / 'elemods').mkdir()
        (self.root / 'elemods' / 'a.elemod').write_bytes(b'{}')
        self.entry = {'path': 'elemods/a.elemod', 'url': 'unused',
                      'sha256': hashlib.sha256(b'{}').hexdigest()}

    def test_good_file_passes(self):
        self.assertEqual(sync.check(self.root, {'mods': [self.entry]}), [])

    def test_changed_or_missing_file_fails(self):
        (self.root / 'elemods' / 'a.elemod').write_bytes(b'{"x":1}')
        missing = dict(self.entry, path='elemods/b.elemod')
        self.assertEqual(len(sync.check(self.root, {'mods': [self.entry, missing]})), 2)

    def test_path_outside_elemods_refused(self):
        bad = dict(self.entry, path='../evil.elemod')
        self.assertIn('hors de elemods', sync.check(self.root, {'mods': [bad]})[0])


if __name__ == '__main__':
    unittest.main()
