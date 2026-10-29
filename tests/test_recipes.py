import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class RecipesTest(unittest.TestCase):
    def test_every_recipe_line_is_in_the_manifest_and_one_os(self):
        known = {m['path']: m for m in json.loads((ROOT / 'mods.json').read_text())['mods']}
        recipes = sorted((ROOT / 'recipes').glob('*/*.txt'))
        self.assertTrue(recipes)
        for r in recipes:
            lines = [l.strip() for l in r.read_text().splitlines() if l.strip() and not l.startswith('#')]
            for l in lines:
                self.assertIn(l, known, '%s: %s' % (r.name, l))
            self.assertEqual(len({(known[l]['device'], known[l]['os']) for l in lines}), 1, r.name)


if __name__ == '__main__':
    unittest.main()
