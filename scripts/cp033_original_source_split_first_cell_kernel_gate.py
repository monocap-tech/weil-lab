#!/usr/bin/env python3
"""CP033 strict original Zeta v4.35 CP032 finite split + n=1 kernel gate.

A source-only PASS means ONLY that the exact four theorem candidates and
their four print-axioms requests are frozen. A KERNEL PASS requires the
fresh original v4.35 compiler, actual .olean, both actual logs, and every
standard-only #print axioms line. Fails closed on missing evidence.

No external CP032/31 cells are imported as axioms; the original n=1
complex power is the ONLY real source-term cell tested in this leaf.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PKG=ROOT/"cp011_zeta_v435"
SRC=PKG/"CP032OriginalTermSplit.lean"
PIN="75024762ea2f9fff12f1d6205af652ce9d21f747"
ORIGINAL_ZETA="c06b4e13d9c847e50a32c3d738271cbad62ae9f3"
TOOLCHAIN="leanprover/lean4:v4.35.0"
IMPORTS=["Zeta.EulerMaclaurin.Continuation","Zeta.Zeros.HardyZ"]
TARGETS=["original_M6N256_finite_expansion","component_sum_interval",
         "dirichlet_one","dirichlet_one_exact_cells"]
AXIOMS=PKG/"cp033-CP032-original-four-genuine-axioms.log"
BUILD=PKG/"cp033-CP032-original-actual-build.log"
OLEAN=PKG/".lake/build/lib/lean/CP032OriginalTermSplit.olean"
STANDARD={"propext","Classical.choice","Quot.sound"}

def blob(p:Path)->str:
    b=p.read_bytes()
    return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()

def sha256(p:Path)->str:
    return hashlib.sha256(p.read_bytes()).hexdigest()

def source_check():
    if blob(SRC)!=PIN:
        raise ValueError("source changed from frozen CP033 four-proof original source candidate")
    src=SRC.read_text("utf8")
    imports=re.findall(r"(?m)^public import\s+(.+)",src)
    thms=re.findall(r"(?m)^theorem\s+([A-Za-z0-9_']+)",src)
    printed=re.findall(r"(?m)^#print axioms\s+CP032OriginalTermSplit\.([A-Za-z0-9_']+)",src)
    if imports!=IMPORTS or thms!=TARGETS or printed!=TARGETS:
        raise ValueError("upstream-only import/four genuine theorem/four axiom roster mismatch")
    if re.search(r"(?m)^\s*(?:axiom|sorry|admit|opaque|unsafe|constant)\b",src):
        raise ValueError("new admitted or unsafe source declaration")
    for key in ("zetaApproximant (point t) 6 256",
                "Finset.Ico 1 256","Finset.Icc 1 6",
                "dirichletTerm t 1 = 1",
                "cellMembership (dirichletTerm t 1).re 1000000000000000 1000000000000000"):
        if key not in src:
            raise ValueError("true original source decomposition / exact n=1 cell drift: "+key)
    if (PKG/"lean-toolchain").read_text("utf8").strip()!=TOOLCHAIN:
        raise ValueError("original Lean toolchain drift")
    if 'git = "https://github.com/smmercuri/zeta"' not in (PKG/"lakefile.toml").read_text("utf8"):
        raise ValueError("upstream original Zeta package pin changed")
    if not (PKG/"lakefile.toml").read_text("utf8").count('rev = "v1-1e6"')==1:
        raise ValueError("original Zeta revision tag mismatch")
    print("CP033 PINNED ORIGINAL ZETA435 FOUR SOURCES + FOUR AXIOM REQUESTS PASS — NOT LEAN")

def parse_original_axioms(ax: str) -> dict[str,list[str]]:
    # Lean's actual v4.35 build output prefixes #print axioms with
    # "info: path:line:column:" and may wrap bracket contents across lines.
    # Require exactly the expected theorem labels, uniquely; tolerate
    # prefix/line wrapping but never an extra declaration or axiom.
    observed=re.findall(
        r"'CP032OriginalTermSplit\.([A-Za-z0-9_']+)'\s+"
        r"(?:depends on axioms:|does not depend on any axioms)", ax)
    if sorted(observed)!=sorted(TARGETS):
        raise ValueError("not exactly four genuine source-axiom declarations: "+repr(observed))
    result={}
    for theorem in TARGETS:
        tag=re.escape("'CP032OriginalTermSplit."+theorem+"'")
        regexp=rf"{tag}\s+(?:depends on axioms:\s*\[([^\]]*)\]|does not depend on any axioms)"
        hits=re.findall(regexp,ax)
        if len(hits)!=1:
            raise ValueError("missing or duplicate original v4.35 #print axioms: "+theorem)
        symbols={item.strip() for item in hits[0].split(",") if item.strip()}
        if not symbols<=STANDARD:
            raise ValueError("nonstandard axiom for "+theorem+": "+repr(symbols-STANDARD))
        result[theorem]=sorted(symbols)
    return result

def parser_self_test():
    lines=[]
    for i,name in enumerate(TARGETS):
        lines.append(
            f"info: CP032OriginalTermSplit.lean:{83+i}:0: "
            f"'CP032OriginalTermSplit.{name}' depends on axioms: "
            "[propext,\n Classical.choice,\n Quot.sound]")
    good="\n".join(lines)
    got=parse_original_axioms(good)
    if set(got)!=set(TARGETS):
        raise ValueError("self-test dropped a genuine four-axiom item")
    for bad in (
        good.replace("propext,", "sorryAx,", 1),
        good.replace("Quot.sound]", "Invented.axiom]", 1),
        good.replace(lines[-1], "", 1),
        good+"\n"+lines[-1]
    ):
        try: parse_original_axioms(bad)
        except ValueError: continue
        raise ValueError("the strict source axiom parser admitted a negative control")
    print("CP034 ACTUAL v4.35 PREFIX/MULTILINE FOUR AXIOM PARSER + FOUR NEGATIVE CONTROLS: PASS NOT LEAN")

def kernel_check():
    source_check()
    if not OLEAN.exists() or OLEAN.stat().st_size==0:
        raise ValueError("original Lean v4.35 .olean absent or empty")
    if not BUILD.exists() or not AXIOMS.exists():
        raise ValueError("genuine compiler/axiom logs missing")
    bs=BUILD.read_text("utf8",errors="replace")
    ax=AXIOMS.read_text("utf8",errors="replace")
    if not bs.strip() or not ax.strip():
        raise ValueError("empty genuine v4.35 compiler/axiom log")
    for label,log in (("build",bs),("axioms",ax)):
        if re.search(r"(?i)(?:^|\n)[^\n]*(?:error:|unsolved goals|sorryAx|declaration uses 'sorry'|admit)",log):
            raise ValueError(label+" original source v4.35 compiler reports failure or admitted proof")
    result=parse_original_axioms(ax)
    print("CP033 ORIGINAL-ZETA435 CP032 SOURCE SPLIT + FIRST UNIT CELL 4/4 ACTUAL LEAN KERNEL+AXIOM PASS")
    return result

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--source-check",action="store_true")
    p.add_argument("--parser-self-test",action="store_true")
    p.add_argument("--kernel-audit",action="store_true")
    p.add_argument("--receipt",type=Path)
    a=p.parse_args()
    if a.source_check: source_check()
    if a.parser_self_test: parser_self_test()
    evidence=kernel_check() if a.kernel_audit else None
    if a.receipt:
        if evidence is None:
            raise ValueError("fail closed: no receipt without genuine v4.35 .olean + logs + standard axioms")
        receipt={
            "status":"CP033_ORIGINAL_ZETA435_CP032_SOURCE_SPLIT_AND_UNIT_CELL_ACTUAL_LEAN_KERNEL_PASS",
            "source_git_blob":blob(SRC),
            "source_sha256":sha256(SRC),
            "source_original_Zeta_commit":ORIGINAL_ZETA,
            "original_lean_toolchain":TOOLCHAIN,
            "actual_original_olean_sha256":sha256(OLEAN),
            "actual_build_log_sha256":sha256(BUILD),
            "actual_axioms_log_sha256":sha256(AXIOMS),
            "genuine_four_standard_axiom_theorems":evidence,
            "original_M6N256_source_decomposition_kernel_pass":True,
            "original_first_n1_complex_source_cell_kernel_pass":True,
            "all_other_525_original_complex_term_memberships_Lean_paid":False,
            "original_theta_sine_cosine_memberships_Lean_paid":False,
            "CP029_original_pointwise_Borwein_Lean_pass":False,
            "original_critical_line_zero_unconditional_Lean_pass":False,
            "source_ordinal53_or_uniqueness":False,
            "global_signed_Weil_positivity_or_RH":False,
        }
        a.receipt.write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf8")
        print(receipt["status"])
    if not (a.source_check or a.kernel_audit or a.parser_self_test): p.print_help()

if __name__=="__main__":
    try:main()
    except (OSError,ValueError,AssertionError,UnicodeError) as ex:
        raise SystemExit("CP033 NOT LEAN KERNEL CERTIFIED: "+str(ex))
