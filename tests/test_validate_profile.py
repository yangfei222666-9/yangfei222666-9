from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_profile import (  # noqa: E402
    REQUIRED_URLS,
    validate_legacy_asset_absent,
    validate_readme,
)


class ProfileValidationTests(unittest.TestCase):
    def validate_text(self, text: str) -> list[str]:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "README.md"
            path.write_text(text, encoding="utf-8")
            return validate_readme(path)

    def test_current_readme_passes(self) -> None:
        self.assertEqual(validate_readme(ROOT / "README.md"), [])

    def test_relative_repository_link_is_rejected(self) -> None:
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        errors = self.validate_text(text + "\n[broken](../taiji)\n")
        self.assertTrue(any("forbidden snippet: ../" in error for error in errors))
        self.assertTrue(any("absolute HTTP(S) URL" in error for error in errors))

    def test_contact_details_are_rejected(self) -> None:
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        errors = self.validate_text(text + "\ncontact: person@example.com, +60 1234 5678\n")
        self.assertIn("README.md contains a literal email address", errors)
        self.assertIn("README.md contains a phone-like value", errors)

    def test_required_url_as_plain_text_does_not_satisfy_link_contract(self) -> None:
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        required = REQUIRED_URLS[0]
        text = text.replace(f"]({required})", "](https://github.com/)", 1)
        errors = self.validate_text(text + f"\n{required}\n")
        self.assertIn(
            f"README.md missing required Markdown link target: {required}",
            errors,
        )

    def test_raw_html_link_is_rejected(self) -> None:
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        errors = self.validate_text(text + '\n<a href="javascript:alert(1)">bad</a>\n')
        self.assertIn("README.md contains a raw HTML link", errors)

    def test_legacy_proof_card_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "taijios-proof-card.svg"
            path.write_text("<svg/>", encoding="utf-8")
            errors = validate_legacy_asset_absent(path)
        self.assertEqual(len(errors), 1)
        self.assertIn("legacy proof-card asset", errors[0])

    def test_unverified_external_authority_phrases_are_rejected(self) -> None:
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        errors = self.validate_text(text + "\nmerged upstream after maintainer review\n")
        self.assertIn("README.md contains forbidden snippet: merged upstream", errors)
        self.assertIn("README.md contains forbidden snippet: maintainer review", errors)


if __name__ == "__main__":
    unittest.main()
