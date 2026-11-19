#!/usr/bin/env python3
"""Emit bounded Lean candidates for each original physical H/V entry row.

This is an exact SOURCE-CUSTODY COMPILATION PLAN, not a claim that any
original row gate is true. Each generated theorem has a real Boolean
conclusion discharged only by Lean's kernel evaluator; a false gate
must fail the build. Bank and payment symbols are explicit CLI inputs
so the emitter cannot introduce unverified data or silently swap frames.
"""
import argparse
import hashlib
import json
from pathlib import Path
from tempfile import TemporaryDirectory

N = 242
DEFAULT_BANK_MODULE = "WeilDefect.Generated.NF628.ChunkJoin"
DEFAULT_PAYMENT_MODULE = "WeilDefect.Generated.NF630.Data"
DEFAULT_BANK = "nf628Bank"
DEFAULT_PAYMENT = "nf630Inputs.payment"
GATE_MODULE = "WeilDefect.Arithmetic.ActualZetaOriginalPhysicalShardedEntryCustody"

def source_text(bank_module, payment_module, bank, payment, rows):
    imports = sorted({GATE_MODULE, bank_module, payment_module})
    body = "\n".join("import " + name for name in imports)
    body += "\n\nnamespace WeilDefect\n\n"
    body += "set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n"
    for i in rows:
        name = f"nf674OriginalRow{i:03d}"
        body += (
            f"/-- Original source index {i}; untrusted literal gate until Lean PASS. -/\n"
            f"theorem {name} :\n"
            f"    neutralNF674OriginalRowCheck\n"
            f"      (neutralNF624Lookup {bank} (neutralNF624Index {bank}))\n"
            f"      ({payment}) ({i} : Fin 242) = true := by\n"
            f"  decide +kernel\n\n"
            f"#print axioms {name}\n\n"
        )
    return body + "end WeilDefect\n"

def emit(out, start, end, chunk, bank_module, payment_module, bank, payment):
    assert 0 <= start < end <= N and 0 < chunk <= 242
    assert all(v and all(c.isalnum() or c in "._" for c in v)
               for v in (bank_module,payment_module,bank,payment))
    out.mkdir(parents=True,exist_ok=True)
    files=[]
    for first in range(start,end,chunk):
        last=min(first+chunk,end)
        path=out/f"Rows{first:03d}To{last-1:03d}.lean"
        code=source_text(bank_module,payment_module,bank,payment,range(first,last))
        path.write_text(code,encoding="utf8")
        files.append(dict(file=path.name,from_row=first,to_row=last-1,
                          sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
    manifest={
        "schema":"NF674-original-physical-row-kernel-proposals-v1",
        "coverage":{"first":start,"last_exclusive":end,"count":end-start},
        "per_row_gates":["H lower triangle","H exact rational center symmetry","all 4 V entries"],
        "bank_module":bank_module,"bank_symbol":bank,
        "payment_module":payment_module,"payment_symbol":payment,
        "files":files,
        "scope":"Untrusted Lean proposals only; NO rows passed by emission and no bank, coverage, cache or payment truth asserted",
    }
    (out/"manifest.json").write_text(json.dumps(manifest,indent=2)+"\n")
    return manifest

def self_test():
    with TemporaryDirectory() as d:
        out=Path(d)
        m=emit(out,0,5,2,DEFAULT_BANK_MODULE,DEFAULT_PAYMENT_MODULE,
               DEFAULT_BANK,DEFAULT_PAYMENT)
        assert len(m["files"])==3
        a=(out/"Rows000To001.lean").read_text()
        assert "nf674OriginalRow000" in a and "nf674OriginalRow001" in a
        assert "nf674OriginalRow002" not in a
        assert "nf630Inputs.payment" in a
        assert "decide +kernel" in a
        assert m["coverage"]["count"]==5
        for f in m["files"]:
            assert hashlib.sha256((out/f["file"]).read_bytes()).hexdigest()==f["sha256"]
    print("NF674 deterministic original-source row-gate emitter synthetic PASS; NO Lean data gate certified")

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",type=Path)
    p.add_argument("--start",type=int,default=0)
    p.add_argument("--end",type=int,default=N)
    p.add_argument("--chunk",type=int,default=1)
    p.add_argument("--bank-module",default=DEFAULT_BANK_MODULE)
    p.add_argument("--payment-module",default=DEFAULT_PAYMENT_MODULE)
    p.add_argument("--bank",default=DEFAULT_BANK)
    p.add_argument("--payment",default=DEFAULT_PAYMENT)
    p.add_argument("--self-test",action="store_true")
    a=p.parse_args()
    if a.self_test:
        self_test()
        return
    if a.output is None:
        p.error("--output is required except for --self-test")
    m=emit(a.output,a.start,a.end,a.chunk,a.bank_module,
           a.payment_module,a.bank,a.payment)
    print("NF674 emitted",m["coverage"]["count"],
          "unverified original physical row proposals across",len(m["files"]),"Lean files")

if __name__=="__main__":
    main()
