#!/usr/bin/env python3
"""Reference entry point for the MSX research ppt v11 evidence-chain builder.

The full historical builder is included in the distributable package under
`dist/msx-research-ppt.zip.b64.part*`. Reconstruct it with:

    cat dist/msx-research-ppt.zip.b64.part* | base64 -d > msx-research-ppt.zip
    unzip msx-research-ppt.zip

Inside the reconstructed package, see:

    msx-research-ppt/scripts/v11_reference_builder.py

The extracted layout constants, narrative rules, figure hierarchy rules, and QA
checks are also available as editable source files under `references/` and
`scripts/audit_pptx.py` in this repository.
"""
from __future__ import annotations

from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    print("MSX research ppt reference builder")
    print("Editable rules:")
    for path in sorted((root / "references").glob("*.md")):
        print(f"- {path.relative_to(root)}")
    print("\nFull historical builder is stored in the distributable zip base64 parts under dist/.")


if __name__ == "__main__":
    main()
