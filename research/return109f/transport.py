#!/usr/bin/env python3
"""Authenticated transport adapter for the unchanged F6R generator."""
import hashlib, importlib.util, json, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parent
CANONICAL = "3ffc6dfb7d3ec42a050fff2c1e2f858ff6c85c79"
BUNDLES = {
    "bundle-1.json": "639ca7ae719c6f01465528979f79af530c85b5b0",
    "bundle-2.json": "5b7e22a0f392530ebc253042b23a791e1a171344",
    "bundle-3.json": "51890d2f9ac650571f562ccebd82bebc1b6160af",
}
SCRIPTS = {
    "prepare_f_assembly.py": "62febd704f73cb842c184ed2eb1b6588b8725631",
    "audit_f_stage.py": "d0a36b619ca4fb77dfcbfcb024b56ae05e836936",
    "test_f6r.py": "73fe3934d514f970380b364c0086d5dc6945ea8b",
}
def digest(b):
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()

def verified_files(root):
    files = {}
    for name, sha in BUNDLES.items():
        raw = (root / name).read_bytes()
        assert digest(raw) == sha, name
        obj = json.loads(raw)
        assert obj["canonical"] == CANONICAL
        for path, entry in obj["files"].items():
            assert path not in files, path
            b = entry["content"].encode("utf-8")
            assert digest(b) == entry["blob"], path
            files[path] = b
    assert len(files) == 20
    for name, sha in SCRIPTS.items():
        assert digest((root / name).read_bytes()) == sha, name
    return files

def main():
    if not __debug__:
        raise RuntimeError("verification requires assertions enabled")
    assert len(sys.argv) == 4, "usage: transport.py BASE_ASSEMBLER OUTPUT PLAN_OUTPUT"
    base, out, plan = map(pathlib.Path, sys.argv[1:])
    files = verified_files(ROOT)
    spec = importlib.util.spec_from_file_location("pinned_generator", ROOT / "prepare_f_assembly.py")
    gen = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gen)
    assert gen.CANONICAL == CANONICAL
    used = set()
    def read(c, p, sha):
        key = str(p)
        assert key in files and key not in used, key
        b = files[key]
        assert digest(b) == sha, key
        used.add(key)
        return b
    gen.read = read
    plan_key = "research/master-return-109f/F6_STAGED_AUDIT.json"
    plan_bytes = read(ROOT, plan_key, "734de9581c2c23a37cdbd92895606d9681294911")
    sys.argv = ["prepare_f_assembly.py", str(base), str(ROOT), str(out)]
    gen.main()
    assert used == set(files), sorted(set(files)-used)
    plan.write_bytes(plan_bytes)
    print("RETURN109-F transport PASS: 20 exact canonical inputs; original generator unchanged")

if __name__ == "__main__":
    main()
