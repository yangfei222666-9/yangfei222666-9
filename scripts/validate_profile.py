#!/usr/bin/env python3
"""Validate the public GitHub profile README contract."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit


REQUIRED_README_SNIPPETS = (
    "Agent Reliability · Evals · Developer Tools",
    "does the closeout include an explicit evidence pointer",
    "memory-auditor",
    "Agent Reliability proof",
    "External evidence",
    "Reviewed and merged contribution",
    "Issue-to-fix trace",
    "Feedback and collaboration",
    "AI tools assist research, implementation, testing, translation, and review",
)

REQUIRED_URLS = (
    "https://github.com/yangfei222666-9/memory-auditor",
    "https://github.com/yangfei222666-9/memory-auditor/releases/tag/repro-v0-v5",
    "https://github.com/yangfei222666-9/taiji/blob/main/docs/portfolio/agent-reliability-proof.md",
    "https://github.com/creativedswork/dsh-expmem/pull/2",
    "https://github.com/tt-a1i/archify/issues/76",
    "https://github.com/tt-a1i/archify/pull/80",
    "https://github.com/deepseek-ai/deepseek-harness/discussions/4911",
    "https://github.com/0xsline/awesome-deepseek-harness/pull/406",
)

FORBIDDEN_README_SNIPPETS = (
    "../",
    "taijios-product-spine-roadmap",
    "No polished CV needed",
    "14 production modules",
    "70,748 LoC",
    "12 providers",
    "industry-standard",
    "merged upstream",
    "maintainer review",
)

EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
PHONE_RE = re.compile(r"(?<!\w)(?:\+?\d[\d ()-]{7,}\d)(?!\w)")
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
HTML_HREF_RE = re.compile(r"<a\b[^>]*\bhref\s*=", re.IGNORECASE)


def validate_readme(readme_path: Path) -> list[str]:
    if not readme_path.exists():
        return [f"{readme_path}: missing"]

    text = readme_path.read_text(encoding="utf-8")
    errors: list[str] = []

    if len(text.strip()) < 1500:
        errors.append("README.md is unexpectedly short")

    for snippet in REQUIRED_README_SNIPPETS:
        if snippet not in text:
            errors.append(f"README.md missing required snippet: {snippet}")

    for snippet in FORBIDDEN_README_SNIPPETS:
        if snippet in text:
            errors.append(f"README.md contains forbidden snippet: {snippet}")

    if EMAIL_RE.search(text):
        errors.append("README.md contains a literal email address")
    if PHONE_RE.search(text):
        errors.append("README.md contains a phone-like value")

    targets = set(MARKDOWN_LINK_RE.findall(text))
    for url in REQUIRED_URLS:
        if url not in targets:
            errors.append(f"README.md missing required Markdown link target: {url}")

    if HTML_HREF_RE.search(text):
        errors.append("README.md contains a raw HTML link")

    for target in targets:
        parsed = urlsplit(target)
        if parsed.scheme not in {"http", "https"}:
            errors.append(f"README.md link must use an absolute HTTP(S) URL: {target}")

    return errors


def validate_legacy_asset_absent(path: Path) -> list[str]:
    if path.exists():
        return [f"legacy proof-card asset must be removed or revalidated: {path}"]
    return []


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the public profile README.")
    parser.add_argument("--readme", default="README.md")
    parser.add_argument("--legacy-proof-card", default="assets/taijios-proof-card.svg")
    args = parser.parse_args()

    errors = [
        *validate_readme(Path(args.readme)),
        *validate_legacy_asset_absent(Path(args.legacy_proof_card)),
    ]
    if errors:
        print("profile validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("profile validation ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
