#!/usr/bin/env python3
"""Authenticated transport adapter for the unchanged F6R generator."""
import hashlib, importlib.util, json, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parent
CANONICAL = "cd8d611e494e2e1e49a466603be3c2bc7b9b3f48"
BUNDLES = {
    "bundle-1.json": "14a7cfad34be79b497dba88c677cfa4f58518fc9",
    "bundle-2.json": "17e815554ac56dc379819c805151398c2877bc2f",
    "bundle-3.json": "081f23f01e52dae734ef696ca49817509e1f9d8e",
}
SCRIPTS = {
    "prepare_f_assembly.py": "695f04e1bf24d812f55eab4dd62ec703646667f2",
    "audit_f_stage.py": "2b545942dab479d7c3cec0f774ec16c0abd39ea9",
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
    plan_bytes = read(ROOT, plan_key, "49ba17ce959659f8ac458865346ff2a0340f3df9")
    sys.argv = ["prepare_f_assembly.py", str(base), str(ROOT), str(out)]
    gen.main()
    assert used == set(files), sorted(set(files)-used)
    plan.write_bytes(plan_bytes)
    print("RETURN109-F transport PASS: 20 exact canonical inputs; original generator unchanged")

if __name__ == "__main__":
    main()
