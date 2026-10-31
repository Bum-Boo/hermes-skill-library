"""Synthetic reproductions for skills/research/grounded-citations/scripts/sources.py.

Run: python3 -m unittest discover -s review -p "test_*.py" -v   (from repo root)
Tests named test_defect_* assert the CURRENT (defective) behaviour so they pass
today and document the bug; flip the assertion once fixed.
No network: URLs are example.* strings only, ledger lives in a temp dir.
"""
import contextlib
import importlib.util
import io
import os
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "skills/research/grounded-citations/scripts/sources.py"
spec = importlib.util.spec_from_file_location("sources_under_review", SCRIPT)
src = importlib.util.module_from_spec(spec)
spec.loader.exec_module(src)


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)
        self.ledger = str(self.dir / "ledger.json")

    def tearDown(self):
        self.tmp.cleanup()

    def run_cli(self, *argv):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            try:
                rc = src.main(["--ledger", self.ledger, *argv])
            except SystemExit as e:
                rc = e.code
        return rc, out.getvalue(), err.getvalue()

    def draft(self, text):
        p = self.dir / "draft.md"
        p.write_text(text, encoding="utf-8")
        return p


class Covered(Base):
    def test_add_idempotent_and_normalized(self):
        self.run_cli("add", "https://example.com/a")
        rc, out, _ = self.run_cli("add", "https://example.com/a/#frag")
        self.assertEqual(out.strip(), "[1] https://example.com/a")

    def test_render_replace_in_markdown_is_idempotent(self):
        self.run_cli("add", "https://example.com/a")
        d = self.draft("Claim one is here.[1]\n")
        self.run_cli("render", "--replace-in", str(d))
        first = d.read_text()
        self.run_cli("render", "--replace-in", str(d))
        self.assertEqual(first, d.read_text())
        self.assertEqual(self.run_cli("verify", str(d))[0], 0)

    def test_quote_rejects_paraphrase(self):
        self.run_cli("add", "https://example.com/a")
        ev = self.dir / "page.txt"
        ev.write_text("Ice is about nine percent less dense than water.")
        rc, _, _ = self.run_cli("quote", "1", "--text", "ice is much lighter than water", "--from", str(ev))
        self.assertNotEqual(rc, 0)


class Defects(Base):
    def test_defect_replace_in_deletes_content_after_sources_block(self):
        self.run_cli("add", "https://example.com/a")
        d = self.draft("Claim one is here.[1]\n\n## Sources\n\n[1] https://example.com/a\n\n"
                       "## Appendix\n\nIrreplaceable appendix text.\n")
        self.run_cli("render", "--replace-in", str(d))
        self.assertNotIn("Irreplaceable appendix text.", d.read_text())  # silently lost

    def test_defect_sources_line_in_code_fence_truncates_draft(self):
        self.run_cli("add", "https://example.com/a")
        d = self.draft("Intro claim is here.[1]\n\n```text\nSources:\n```\n\nLater body text stays here.[1]\n")
        self.run_cli("render", "--replace-in", str(d))
        text = d.read_text()
        self.assertNotIn("Later body text stays here.", text)  # cut at fenced 'Sources:'

    def test_defect_footnotes_replace_in_not_idempotent(self):
        self.run_cli("add", "https://example.com/a")
        d = self.draft("Claim one is here.[1]\n")
        for _ in range(3):
            self.run_cli("render", "--style", "footnotes", "--replace-in", str(d))
        self.assertEqual(d.read_text().count("[^1]: https://example.com/a"), 3)  # stacked

    def test_defect_url_with_parentheses_fails_own_render(self):
        url = "https://en.example.org/wiki/Python_(language)"
        self.run_cli("add", url)
        d = self.draft("Python is a programming language.[1]\n")
        self.run_cli("render", "--replace-in", str(d))
        rc, _, err = self.run_cli("verify", str(d))
        self.assertEqual(rc, 1)
        self.assertIn("does not match the ledger", err)

    def test_defect_bad_only_range_tracebacks(self):
        self.run_cli("add", "https://example.com/a")
        with self.assertRaises(ValueError):
            src.main(["--ledger", self.ledger, "render", "--only", "1-"])

    def test_defect_lock_stolen_from_live_holder(self):
        path = Path(self.ledger)
        holder = src._LedgerLock(path).__enter__()      # live holder
        second = src._LedgerLock(path, timeout=0.1).__enter__()  # should wait, instead steals
        self.assertIsNotNone(second.fd)                 # both 'hold' the lock now
        second.__exit__(None, None, None)
        holder.__exit__(None, None, None)


if __name__ == "__main__":
    unittest.main()
