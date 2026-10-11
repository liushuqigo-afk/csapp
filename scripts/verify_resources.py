#!/usr/bin/env python3
"""Verify downloaded archives, PDFs, and supplementary trace data."""

import hashlib
import json
from pathlib import Path


def main():
    root = Path(__file__).resolve().parents[1]
    manifest = json.loads((root / "sources.json").read_text())
    failures = []
    for item in manifest["artifacts"]:
        path = root / item["path"]
        if not path.is_file():
            failures.append(f"缺少：{item['path']}")
            continue
        digest = hashlib.sha256()
        with path.open("rb") as source:
            for block in iter(lambda: source.read(1024 * 1024), b""):
                digest.update(block)
        if digest.hexdigest() != item["sha256"]:
            failures.append(f"校验不符：{item['path']}")
    if failures:
        print("\n".join(failures))
        return 1
    print(f"通过：{len(manifest['artifacts'])} 个原始资源的 SHA-256 均匹配。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
