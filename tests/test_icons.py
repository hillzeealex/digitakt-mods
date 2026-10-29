import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class IconsTest(unittest.TestCase):
    def test_every_mod_has_an_icon(self):
        for m in json.loads((ROOT / 'mods.json').read_text())['mods']:
            name = m['id'] if m['device'] == 'digitakt-mk1' else '%s-dt2' % m['id']
            self.assertTrue((ROOT / 'docs' / 'icons' / ('%s.svg' % name)).is_file(), name)

    def test_every_image_the_docs_use_exists(self):
        import re
        for doc in [ROOT / 'README.md', *sorted((ROOT / 'docs').glob('*.md'))]:
            for src in re.findall(r'(?:src="|\]\()([^")#]+\.svg)', doc.read_text()):
                self.assertTrue((doc.parent / src).is_file(), '%s: %s' % (doc.name, src))


if __name__ == '__main__':
    unittest.main()
