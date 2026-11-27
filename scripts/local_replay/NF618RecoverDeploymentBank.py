#!/usr/bin/env python3
"""Recover the exact NF618 frozen bank from repository-held chunks; no native workflow."""
import hashlib
import json
import pathlib
import sys
import zipfile

def main():
    root = pathlib.Path(__file__).resolve().parents[2]
    manifest = json.loads((root / "notes/provisional/NF618ReflexiveDeploymentBank.manifest.json").read_text())
    target = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path(manifest["archive"])
    digest = hashlib.sha256()
    with target.open("wb") as output:
        for entry in manifest["chunks"]:
            data = (root / entry["path"]).read_bytes()
            blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
            if len(data) != entry["bytes"] or blob != entry["git_blob"]:
                raise ValueError("Chunk identity mismatch: " + entry["path"])
            output.write(data)
            digest.update(data)
    if target.stat().st_size != manifest["bytes"] or digest.hexdigest() != manifest["sha256"]:
        target.unlink(missing_ok=True)
        raise ValueError("Archive identity mismatch")
    with zipfile.ZipFile(target) as archive:
        bad = archive.testzip()
        if bad is not None:
            target.unlink(missing_ok=True)
            raise ValueError("ZIP member failed CRC: " + bad)
    print(f"PASS {target} {manifest['bytes']} bytes {digest.hexdigest()}")

if __name__ == "__main__":
    main()
