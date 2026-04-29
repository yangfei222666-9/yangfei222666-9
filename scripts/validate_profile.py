#!/usr/bin/env python3
"""Validate the GitHub profile README and local visual asset.

The profile repo is mostly documentation, so this check intentionally stays
local and deterministic. It verifies that the public entrypoints and proof-card
asset are present without depending on third-party network availability.
"""

from __future__ import annotations

import argparse
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


REQUIRED_README_SNIPPETS = (
    "Building Reliable Agent Infrastructure",
    "self-improving-loop v0.1.1",
    "zhuge-crystals",
    "No polished CV needed",
    "GitHub issues preferred",
)

REQUIRED_LINKS = (
    "../taiji",
    "../self-improving-loop",
    "../zhuge-skill",
    "../zhuge-crystals",
)

FORBIDDEN_README_SNIPPETS = (
    f"{'Yang'} {'Fei'}",
    "yang" + "fei" + "222666-9",
)

LOCAL_ASSET_RE = re.compile(r'<img[^>]+src="(?P<src>\./assets/taijios-proof-card\.svg)"', re.IGNORECASE)


def validate_readme(readme_path: Path) -> list[str]:
    errors: list[str] = []
    if not readme_path.exists():
        return [f"{readme_path}: missing"]

    text = readme_path.read_text(encoding="utf-8")
    if len(text.strip()) < 1000:
        errors.append("README.md is unexpectedly short")

    for snippet in REQUIRED_README_SNIPPETS:
        if snippet not in text:
            errors.append(f"README.md missing required snippet: {snippet}")

    for link in REQUIRED_LINKS:
        if link not in text:
            errors.append(f"README.md missing required link: {link}")

    for snippet in FORBIDDEN_README_SNIPPETS:
        if snippet in text:
            errors.append(f"README.md contains forbidden privacy snippet: {snippet}")

    if not LOCAL_ASSET_RE.search(text):
        errors.append("README.md must reference ./assets/taijios-proof-card.svg")

    return errors


def validate_svg(svg_path: Path) -> list[str]:
    errors: list[str] = []
    if not svg_path.exists():
        return [f"{svg_path}: missing"]

    try:
        root = ET.parse(svg_path).getroot()
    except ET.ParseError as exc:
        return [f"{svg_path}: invalid SVG XML: {exc}"]

    if not root.tag.endswith("svg"):
        errors.append(f"{svg_path}: root element is not svg")
    if not root.attrib.get("width") or not root.attrib.get("height"):
        errors.append(f"{svg_path}: width and height are required")

    title_found = any(child.tag.endswith("title") for child in root.iter())
    desc_found = any(child.tag.endswith("desc") for child in root.iter())
    if not title_found:
        errors.append(f"{svg_path}: missing title element")
    if not desc_found:
        errors.append(f"{svg_path}: missing desc element")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate profile README and local assets.")
    parser.add_argument("--readme", default="README.md")
    parser.add_argument("--svg", default="assets/taijios-proof-card.svg")
    args = parser.parse_args()

    errors = [
        *validate_readme(Path(args.readme)),
        *validate_svg(Path(args.svg)),
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
