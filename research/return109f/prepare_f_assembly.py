#!/usr/bin/env python3
"""Generate a standalone F closure assembler from the admitted E6 base.
No execution of Lean, workflow activation, or admission occurs here.
Usage: python prepare_f_assembly.py BASE_ASSEMBLER CANONICAL_CHECKOUT OUTPUT
Canonical checkout must contain the pinned F manifest revision.
Rebase deliberately if E6 is superseded; never silently consume a later repair.
"""
import hashlib, json, pathlib, re, subprocess, sys

BASE_BLOB = "b25ed55d1ab8511a784cf3863aa630db9bb84a55"
CANONICAL = "cd8d611e494e2e1e49a466603be3c2bc7b9b3f48"
E_BLOB = "67fc9656ae64efc72b084634e5ecee10b54aa2c8"
DIR = pathlib.Path("research/master-return-109f")
MANIFEST_BLOB = "dbdd76a2b5b065549255e507852505f286a8c605"
ROOTS_BLOB = "9ae4efda9bad8a024ef2db5ddff4e2299035d564"
DISCOVERY_BLOB = "e3c3cf6237eb7cb2e9a23193efc80376ab04fc8e"

def digest(b):
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()

def read(c, p, sha):
    b = subprocess.check_output(["git", "-C", str(c), "show", CANONICAL + ":" + str(p)])
    assert digest(b) == sha, (p, digest(b), sha)
    return b

def main():
    if not __debug__:
        raise RuntimeError("verification requires assertions enabled")
    assert len(sys.argv) == 4, __doc__
    base, c, out = map(pathlib.Path, sys.argv[1:])
    data = base.read_bytes()
    assert digest(data) == BASE_BLOB, "E6 assembler drift"
    f = json.loads(read(c, DIR / "F_NAMED_AUDIT_MANIFEST.json", MANIFEST_BLOB))
    roots = json.loads(read(c, DIR / "F_SUPPLIER_ROOTS.json", ROOTS_BLOB))
    d = json.loads(read(c, DIR / "F_CLOSURE_DISCOVERY.json", DISCOVERY_BLOB))
    assert not d["pending"] and len(d["added"]) == 31
    assert roots["base_manifest_count"] == d["base_count"] == 283
    assert roots["IV"] == d["IV"] and roots["RECON"] == d["RECON"]
    assert len(f["modules"]) == 16 and f["total"] == f["unique"] == 111
    additions = {p: e["blob"] for p, e in d["added"].items()}
    new_roots = {e["path"]: e["blob"] for e in roots["roots"] if not e["inE2"]}
    assert len(new_roots) == 4
    # The inherited visitor performs comment-aware import traversal, exact git
    # blob checks and dual-lineage conflict rejection. Pin its observed delta.
    block = f"""
# RETURN109-F6: exact IV supplier delta, before any source writes.
assert len(manifest) == 283, len(manifest)
f_before = set(manifest)
f_roots = {new_roots!r}
f_expected = {additions!r}
for p, sha in f_roots.items():
    visit(p, "IV")
    assert manifest[p]["blob"] == sha, p
assert set(manifest) - f_before == set(f_expected), (sorted(set(manifest)-f_before), sorted(set(f_expected)-set(manifest)))
for p, sha in f_expected.items():
    assert manifest[p]["blob"] == sha and manifest[p]["required_by"] == ["IV"], p
print("RETURN109-F6 supplier delta authenticated:", len(f_expected))
"""
    src = data.decode("utf-8")
    assert E_BLOB in src, "admitted E6 attachment missing"
    marker = "# No source files are written until the entire selected closure passes."
    assert src.count(marker) == 1
    src = src.replace(marker, block + marker)
    src = 'if not __debug__: raise RuntimeError("verification requires assertions enabled")\n' + src
    # Append exact staged source bytes, never regenerate theorem text.
    src += f"""\nassert digest(pathlib.Path('WeilDefect/MasterReturn/LogCarrierBoundedAnalysis.lean').read_bytes()) == {E_BLOB!r}\nassert len(manifest) == 314\n"""
    names = set()
    staged = {}
    for e in f["modules"]:
        p = pathlib.Path(e["path"])
        b = read(c, p, e["blob"])
        source = b.decode("utf-8")
        found = re.findall(r"^#print axioms (.+)$", source, re.M)
        assert found == e["names"] and not names.intersection(found), p
        names.update(found)
        im = re.findall(r"^import (.+)$", source, re.M)
        assert im == e["imports"], p
        target = "WeilDefect/MasterReturn/" + p.name
        assert target not in staged
        staged[target] = {"blob": e["blob"], "names": found, "imports": im}
        src += f"""
f_path = pathlib.Path({target!r})
assert not f_path.exists(), f_path
f_data = {b!r}
assert digest(f_data) == {e["blob"]!r}
f_path.write_bytes(f_data)
assert digest(f_path.read_bytes()) == {e["blob"]!r}
"""
    assert len(names) == 111
    src += f"""
f_result = {{"canonical": {CANONICAL!r}, "base_assembler_blob": {BASE_BLOB!r},
    "supplier_delta": f_expected, "staged": {staged!r},
    "admitted_E_blob": {E_BLOB!r}, "supplier_count": 314,
    "named_targets": 111, "status": "source assembly only; native audit pending"}}
pathlib.Path("return109f-closure.json").write_text(json.dumps(f_result, indent=2, sort_keys=True)+"\\n")
print("RETURN109-F6 staged source assembly PASS 16 modules / 111 names")
"""
    compile(src, str(out), "exec")
    out.write_text(src, encoding="utf-8")
    print("Generated assembler SHA256:", hashlib.sha256(out.read_bytes()).hexdigest())

if __name__ == "__main__":
    main()
