#!/usr/bin/env python3
"""Authenticated transport adapter for the unchanged F6R generator."""
import hashlib, importlib.util, json, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parent
CANONICAL = "3ee0cc9b3a169fc82b95561f91974457cbf524b9"
BUNDLES = {
    "bundle-1.json": "e7512e748cdc31a0a986077d3b3f59cb00c3be3a",
    "bundle-2.json": "1284be32c8494dc131068bd68dcaea9848aed95a",
    "bundle-3.json": "ce2f28cee921195a3f9c8464117b61f55df04e0f",
}
SCRIPTS = {
    "prepare_f_assembly.py": "b2fd179cac28cee3dccd8a359febe9d0ded026fa",
    "audit_f_stage.py": "d6229908afb44b91d3c1e1ae1a1c47dde7ad7d68",
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
    plan_bytes = read(ROOT, plan_key, "b1f9b37e663fc01face78baa404b1ab1b97be5e9")
    sys.argv = ["prepare_f_assembly.py", str(base), str(ROOT), str(out)]
    gen.main()
    assert used == set(files), sorted(set(files)-used)
    plan.write_bytes(plan_bytes)
    print("RETURN109-F transport PASS: 20 exact canonical inputs; original generator unchanged")

if __name__ == "__main__":
    main()
