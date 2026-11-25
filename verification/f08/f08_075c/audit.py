#!/usr/bin/env python3
"""F08-075C independent archive custody, not a second native compile."""
import hashlib,json,os,re,subprocess,sys,urllib.request,zipfile
from pathlib import Path,PurePosixPath
M=json.loads(Path(__file__).with_name("pins.json").read_text())
NAMES={"f08_075_originalSchwartzHilbert_approx","f08_075_originalHilbert_eq_of_physical_eq"}
ALLOWED={"propext","Classical.choice","Quot.sound"}
def axioms(s):
    p=r"'WeilDefect\.(\w+)' depends on axioms: \[([^\]]*)\]"
    matches=list(re.finditer(p,s,re.S))
    assert len(matches)==2 and not re.sub(p,"",s,flags=re.S).strip()
    assert {m[1] for m in matches}==NAMES
    out={}
    for m in matches:
        a={x.strip() for x in m[2].split(",") if x.strip()}
        assert a==ALLOWED
        out[m[1]]=sorted(a)
    return out
def selftest():
    good="\n".join("'WeilDefect."+n+"' depends on axioms: [propext, Classical.choice, Quot.sound]" for n in sorted(NAMES))
    assert set(axioms(good))==NAMES
    for bad in (good.replace("propext","sorryAx"),good.replace(sorted(NAMES)[0],"other"),good+"\n"+good,good+"\nerror: failed",good.splitlines()[0]):
        try: axioms(bad)
        except AssertionError: continue
        raise AssertionError("invalid axiom log accepted")
    print("F08-075C selftest PASS 5/5")
def git(cwd,*args):
    return subprocess.check_output(["git","-C",str(cwd),*args],text=True).strip()
def gitblob(b):
    return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def request(path):
    url=os.environ["GITHUB_API_URL"]+"/repos/"+os.environ["GITHUB_REPOSITORY"]+path
    headers={"Authorization":"Bearer "+os.environ["GH_TOKEN"],"Accept":"application/vnd.github+json","X-GitHub-Api-Version":"2022-11-28"}
    with urllib.request.urlopen(urllib.request.Request(url,headers=headers),timeout=90) as r:
        return r.read()
def metadata(p,producer=False):
    r=json.loads(request("/actions/runs/"+str(p["run"])))
    assert r["status"]=="completed" and r["conclusion"]=="success" and r["head_sha"]==p["head"]
    assert r["head_repository"]["full_name"]=="monocap-tech/weil-lab"
    j=json.loads(request("/actions/runs/"+str(p["run"])+"/jobs"))["jobs"]
    step=p["step"]
    assert any(x["conclusion"]=="success" and any(s["name"]==step and s["conclusion"]=="success" for s in x["steps"]) for x in j)
    a=json.loads(request("/actions/artifacts/"+str(p["artifact"])))
    assert a["workflow_run"]["id"]==p["run"] and a["workflow_run"]["head_sha"]==p["head"]
    assert a["digest"]=="sha256:"+p["digest"] and not a["expired"] and a["size_in_bytes"]>0
    if producer:
        assert r["name"]==p["workflow"] and a["name"]==p["name"]
    return {"run":p["run"],"head":p["head"],"artifact":p["artifact"],"digest":p["digest"],"size":a["size_in_bytes"]}
def main():
    selftest()
    if "--selftest" in sys.argv: return
    producer,upstream,research,out=map(Path,sys.argv[1:5])
    out.mkdir(parents=True,exist_ok=True)
    p=M["producer"]
    assert git(producer,"rev-parse","HEAD")==p["head"]
    assert git(upstream,"rev-parse","HEAD")==M["upstream"]
    roots={"producer":producer,"upstream":upstream}
    assert git(research,"rev-parse","HEAD")==M["research_commit"]
    assert (research/"lean-toolchain").read_text().strip()=="leanprover/lean4:v4.34.0"
    for x in M["research"]:
        assert git(research,"hash-object",x["source"])==x["blob"]
    for x in M["pins"]:
        assert git(roots[x["checkout"]],"hash-object",x["source"])==x["blob"]
    preds=[metadata(x) for x in M["predecessors"]]
    m=metadata(p,True)
    # curl does not forward Authorization to the cross-origin signed storage URL.
    # Retain the exact ZIP size and digest checks below.
    url=os.environ["GITHUB_API_URL"]+"/repos/"+os.environ["GITHUB_REPOSITORY"]+"/actions/artifacts/"+str(p["artifact"])+"/zip"
    raw=subprocess.check_output(["curl","--fail","--silent","--show-error","--location","--retry","3","--max-time","120","--proto","=https","--proto-redir","=https","-H","Authorization: Bearer "+os.environ["GH_TOKEN"],url])
    assert len(raw)==m["size"] and hashlib.sha256(raw).hexdigest()==p["digest"]
    zpath=out/"producer.zip"
    zpath.write_bytes(raw)
    with zipfile.ZipFile(zpath) as z:
        names=z.namelist()
        assert len(names)==40 and len(set(names))==40 and z.testzip() is None
        assert all(not PurePosixPath(n).is_absolute() and ".." not in PurePosixPath(n).parts and not n.endswith("/") for n in names)
        used=set()
        def read(s):
            hits=[n for n in names if n==s or n.endswith("/"+s)]
            assert len(hits)==1 and hits[0] not in used,(s,hits)
            used.add(hits[0])
            return z.read(hits[0])
        for x in M["pins"]:
            b=read(x["archive"])
            assert gitblob(b)==x["blob"] and b==(roots[x["checkout"]]/x["source"]).read_bytes()
            assert not re.search(rb"\b(sorry|admit|unsafe)\b",b)
        build=read("f08-075-build.log").decode()
        a=axioms(read("f08-075-axioms.log").decode())
        assert set(names)==used
    assert "Build completed successfully (9069 jobs)." in build
    assert "Built WeilDefect.Generated.F08.OriginalSchwartzHilbertCore" in build
    assert not re.search(r"(^|\n)[^\n]*error:",build,re.I)
    receipt={"gate":"F08-075C","producer":m,"predecessor_custody_metadata":preds,"archive_entries":40,"source_blobs":38,"original_research_blobs":6,"build_jobs":9069,"axioms":a,"schwartz_hilbert_core_custody":True,"independent_native_recompile":False,"signed_Weil_transfer":False,"global_positivity":False,"RH":False}
    (out/"receipt.json").write_text(json.dumps(receipt,indent=2,sort_keys=True)+"\n")
    print("F08-075C independent Schwartz Hilbert core archive custody PASS")
if __name__=="__main__": main()
