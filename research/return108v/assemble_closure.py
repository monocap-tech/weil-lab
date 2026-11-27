#!/usr/bin/env python3
"""Build the minimal literal bridge overlay, with fail-closed source custody."""
import hashlib, json, pathlib, re, subprocess
I = "f2e8ec89ae4bf8687a652b299b730d6d1baa43f7"
R = "8866d05c4d795bf153027b0b076a323262b0c71a"
ROOT = "WeilDefect/MasterReturn/LogCarrierBridge.lean"
def git(*args):
    return subprocess.check_output(["git", *args])
def inventory(ref):
    result = {}
    for row in git("ls-tree", "-r", "-z", ref).split(b"\0"):
        if not row: continue
        meta, path = row.split(b"\t", 1)
        mode, kind, sha = meta.decode().split()
        if kind == "blob": result[path.decode()] = (mode, sha)
    return result
def digest(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
trees = {"IV": inventory(I), "RECON": inventory(R)}
refs = {"IV": I, "RECON": R}
for p in ("lean-toolchain", "lakefile.toml"):
    assert trees["IV"][p] == trees["RECON"][p], p
    assert digest(pathlib.Path(p).read_bytes()) == trees["IV"][p][1], p
seen, manifest, external = set(), {}, set()
IV_ENTRY = "WeilDefect/Morphology/NeutralLogHilbertCarrier.lean"
assert git("rev-parse", "HEAD").decode().strip() == I
def visit(p, preferred):
    if (p, preferred) in seen: return
    seen.add((p, preferred))
    side = preferred
    if p not in trees[side]:
        raise SystemExit("MISSING PROJECT SOURCE IN " + side + ": " + p)
    # Only compare versions actually required by the selected import graph.
    a, b = trees["IV"].get(p), trees["RECON"].get(p)
    if p in manifest and manifest[p]["blob"] != trees[side][p][1]:
        raise SystemExit("DUAL-LINEAGE SOURCE CONFLICT: " + p + " " + str((a,b)))
    if side == "RECON" and a and a != b:
        raise SystemExit("RECON SOURCE WOULD OVERWRITE IV BASE: " + p)
    mode, sha = trees[side][p]
    assert mode == "100644", (p, mode)
    data = git("show", refs[side] + ":" + p)
    assert digest(data) == sha, p
    entry = manifest.setdefault(p, {"blob":sha,"origin":"IV" if a else "RECON","imports":[],"required_by":[]})
    if side not in entry["required_by"]: entry["required_by"].append(side)
    # Remove nested Lean block comments, preserving line boundaries.
    source = data.decode()
    clean = []
    depth = 0
    pos = 0
    while pos < len(source):
        if source.startswith("/-", pos):
            depth += 1; pos += 2
        elif depth and source.startswith("-/", pos):
            depth -= 1; pos += 2
        elif not depth and source.startswith("--", pos):
            end = source.find("\n", pos)
            pos = len(source) if end < 0 else end
        else:
            if not depth or source[pos] == "\n": clean.append(source[pos])
            pos += 1
    assert depth == 0, p
    for line in "".join(clean).splitlines():
        m = re.match(r"^\s*(?:(?:public|private|meta)\s+)*import\s+(.+?)\s*$", line)
        if not m: continue
        for module in m.group(1).split():
            if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_'.]*", module):
                raise SystemExit("UNPARSED IMPORT: " + p + ": " + line)
            target = module.replace(".", "/") + ".lean"
            if target in trees["IV"] or target in trees["RECON"] or module == "WeilDefect" or module.startswith("WeilDefect."):
                if target not in entry["imports"]: entry["imports"].append(target)
                visit(target, "IV" if p == ROOT and target == IV_ENTRY else side)
            else: external.add(module)
visit(ROOT, "RECON")
# No source files are written until the entire selected closure passes.
for p, e in sorted(manifest.items()):
    dst = pathlib.Path(p)
    if e["origin"] == "IV":
        assert digest(dst.read_bytes()) == e["blob"], p
    else:
        assert not dst.exists(), p
        data = git("show", R + ":" + p)
        assert digest(data) == e["blob"], p
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_bytes(data)
    assert digest(dst.read_bytes()) == e["blob"], p
assert manifest[IV_ENTRY]["required_by"] == ["IV"]
assert manifest[ROOT]["blob"] == "268105f19fd9bb8e1401219268b6bf5d42fef05d"
neutral = "WeilDefect/Morphology/Neutral.lean"
assert manifest[neutral]["blob"] == "9c446407e5f9ecfada57d2dee5e1d85b7d8a5753"
assert manifest[neutral]["required_by"] == ["IV"]
result = {"IV":I,"RECON":R,"root":ROOT,"entries":manifest,"external_imports":sorted(external),"explicit_cross_edge":[ROOT,IV_ENTRY]}
pathlib.Path("return108v-closure.json").write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
print("Authenticated closure:", len(manifest), "modules;", sum(e["origin"]=="RECON" for e in manifest.values()), "overlay modules")
print("No differing shared path required by both lineages; IV morphology retained.")
