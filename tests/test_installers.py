from pathlib import Path
import hashlib
import json
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class InstallerTests(unittest.TestCase):
    def run_installer(self, script, *arguments):
        return subprocess.run(['bash', str(ROOT/'scripts'/script), *map(str, arguments)], text=True, capture_output=True, timeout=20)

    def test_unknown_collection_rejects_without_creating_target(self):
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)/'missing target'
            result = self.run_installer('install-collection.sh', 'unknown-synthetic', target)
            self.assertEqual(result.returncode, 2, result.stderr)
            self.assertFalse(target.exists())

    def test_each_collection_matches_the_catalog_and_source_bytes(self):
        catalog = json.loads((ROOT/'catalog.json').read_text())['collections']
        originals = {p.parent.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in (ROOT/'skills').rglob('SKILL.md')}
        with tempfile.TemporaryDirectory() as temporary:
            for name, collection in catalog.items():
                with self.subTest(collection=name):
                    target = Path(temporary)/name
                    result = self.run_installer('install-collection.sh', name, target)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    actual = {p.parent.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in target.rglob('SKILL.md')}
                    self.assertEqual(actual, {name: originals[name] for name in collection['skills']})

    def test_install_all_preserves_each_relative_path_and_file(self):
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)/'all skills'
            result = self.run_installer('install.sh', target)
            self.assertEqual(result.returncode, 0, result.stderr)
            source = ROOT/'skills'
            expected = {p.relative_to(source).as_posix(): p.read_bytes() for p in source.rglob('*') if p.is_file()}
            actual = {p.relative_to(target).as_posix(): p.read_bytes() for p in target.rglob('*') if p.is_file()}
            self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
