#!/usr/bin/env python3
"""F08-074 independent archive custody, not a second native compile."""
import hashlib,json,os,re,subprocess,sys,urllib.request,zipfile
from pathlib import Path,PurePosixPath
M=json.loads(Path(__file__).with_name("pins.json").read_text())
NAME="f08_073_original_fixedSupport_smooth_approx"
ALLOWED={"propext","Classical.choice","Quot.sound"}
def axioms(s):
    p=r"'WeilDefect\.(\w+)' depends on axioms: \[([^\]]*)\]"
    matches=list(re.finditer(p,s,re.S))
    assert len(matches)==1 and not re.sub(p,"",s,flags=re.S).strip()
    assert matches[0][1]==NAME
    a={x.strip() for x in matches[0][2].split(",") if x.strip()}
    assert a <= ALLOWED and a==ALLOWED
    return sorted(a)
def selftest():
    good="'WeilDefect."+NAME+"' depends on axioms: [propext, Classical.choice, Quot.sound]"
    assert axioms(good)==sorted(ALLOWED)
    for bad in (good.replace("propext","sorryAx"),good.replace(NAME,"other"),good+"\n"+good,good+"\nerror: failed"):
        try: axioms(bad)
        except AssertionError: continue
        raise AssertionError("invalid axiom log accepted")
    print("F08-074 selftest PASS 4/4")
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
    step=p["step"] if producer else "Download and independently audit actual entire original compiler archive"
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
    producer,research,out=map(Path,sys.argv[1:4])
    out.mkdir(parents=True,exist_ok=True)
    p=M["producer"]
    assert git(producer,"rev-parse","HEAD")==p["head"]
    assert git(research,"rev-parse","HEAD")==M["research_commit"]
    assert (research/"lean-toolchain").read_text().strip()=="leanprover/lean4:v4.34.0"
    for x in M["research"]:
        assert git(research,"hash-object",x["source"])==x["blob"]
    for x in M["pins"]:
        assert git(producer,"hash-object",x["source"])==x["blob"]
    preds=[metadata(x) for x in M["predecessors"]]
    m=metadata(p,True)
    raw=request("/actions/artifacts/"+str(p["artifact"])+"/zip")
    assert len(raw)==m["size"] and hashlib.sha256(raw).hexdigest()==p["digest"]
    zpath=out/"producer.zip"
    zpath.write_bytes(raw)
    with zipfile.ZipFile(zpath) as z:
        names=z.namelist()
        assert len(names)==39 and len(set(names))==39 and z.testzip() is None
        assert all(not PurePosixPath(n).is_absolute() and ".." not in PurePosixPath(n).parts and not n.endswith("/") for n in names)
        used=set()
        def read(s):
            hits=[n for n in names if n==s or n.endswith("/"+s)]
            assert len(hits)==1 and hits[0] not in used,(s,hits)
            used.add(hits[0])
            return z.read(hits[0])
        for x in M["pins"]:
            b=read(x["archive"])
            assert gitblob(b)==x["blob"] and b==(producer/x["source"]).read_bytes()
            assert not re.search(rb"\b(sorry|admit|unsafe)\b",b)
        build=read("f08-073-build.log").decode()
        a=axioms(read("f08-073-axioms.log").decode())
        assert set(names)==used
    assert "Build completed successfully (9068 jobs)." in build
    assert "Built WeilDefect.Generated.F08.TerminalOriginalFixedSupportSmoothDensity" in build
    assert not re.search(r"(^|\n)[^\n]*error:",build,re.I)
    receipt={"gate":"F08-074","producer":m,"predecessor_custody_metadata":preds,"archive_entries":39,"source_blobs":37,"original_research_blobs":6,"build_jobs":9068,"axioms":{NAME:a},"fixed_support_weighted_density_custody":True,"independent_native_recompile":False,"signed_Weil_transfer":False,"global_positivity":False,"RH":False}
    (out/"receipt.json").write_text(json.dumps(receipt,indent=2,sort_keys=True)+"\n")
    print("F08-074 independent terminal archive custody PASS")
if __name__=="__main__": main()
