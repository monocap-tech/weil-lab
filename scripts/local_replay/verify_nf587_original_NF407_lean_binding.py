#!/usr/bin/env python3
"""NF587 lossless independent NF407 -> Lean table audit.

Only exact integers and rationals. Verifies the frozen source bytes,
all primitive coefficient midpoints/radii, selected node alignment,
and the full critical probe shape. Does not prove the original solve
is inside its archival coefficient intervals.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json
import re
import sys

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json"
LEAN = ROOT / "WeilDefect/Arithmetic"
SHA = "0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"

def dy(p):
    return F(int(p[0])) * F(2)**int(p[1])

def read_source():
    raw = SRC.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == SHA
    return json.loads(raw)

def check_source(j):
    a = j["original_exact_native_raw_selected_coefficients_mid_radius"]
    b = j["original_exact_native_original_four_critical_coefficients_mid_radius"]
    nodes = j["original_selected_generator_node_orders"]
    freqs = j["original_source_critical_sine_frequencies"]
    shapes = j["original_source_critical_sines_and_pole_coefficients"]
    assert len(a) == len(nodes) == 242
    assert len(b) == len(shapes) == 4
    assert len(freqs) == 32
    assert nodes[-1] == ["pole", None]
    assert all(len(s["sine_coefficients"]) == 32 for s in shapes)
    assert all(dy(r) >= 0 and abs(dy(m)) + dy(r) < 10**143 for m,r in a+b)
    assert all(F(0) < F(f) < 883 and 0 <= k <= 13 for f,k in nodes[:-1])
    assert all(F(0) < F(f) < 883 for f in freqs)
    assert all(abs(F(q)) <= 1 for s in shapes for q in
               s["sine_coefficients"]+[s["sinh_coefficient"]])
    assert len({(F(f),k) for f,k in nodes[:-1]} |
               {(F(f),0) for f in freqs}) == 273
    pat = re.compile(r"\(\((-?\d+), (-?\d+)\), \((-?\d+), (-?\d+)\)\)")
    def parse(s):
        return [((int(m),int(e)),(int(r),int(k))) for m,e,r,k in pat.findall(s)]
    def expected(rows):
        return [tuple(tuple(map(int,p)) for p in row) for row in rows]
    observed = []
    for k in range(4):
        observed += parse((LEAN / f"ActualZetaOriginalNF407DyadicChunk{k}.lean").read_text())
    assert observed == expected(a)
    data = (LEAN / "ActualZetaOriginalNF407FrozenData.lean").read_text()
    assert parse(data) == expected(b)
    def table(name, end):
        t = data.split("def "+name+" ",1)[1]
        return t.split(end,1)[0].split(":=",1)[1]
    rational = r"\((-?\d+(?:/\d+)?)\)"
    rowpat = re.compile(r"\(\((-?\d+(?:/\d+)?)\), (\d+)\)")
    assert [(F(f),int(k)) for f,k in rowpat.findall(
        table("neutralNF587FrozenNodes","]"))] == [(F(f),k) for f,k in nodes[:-1]]
    assert [F(x) for x in re.findall(rational,table(
        "neutralNF587CriticalFrequencies","]"))] == list(map(F,freqs))
    shape_text = table("neutralNF587CriticalSines","def neutralNF587CriticalPoles")
    shape_rows = re.findall(r"#\[([^\[\]]*)\]",shape_text)
    assert [[F(x) for x in re.findall(rational,row)] for row in shape_rows] == [
        list(map(F,s["sine_coefficients"])) for s in shapes]
    assert [F(x) for x in re.findall(rational,table(
        "neutralNF587CriticalPoles","]"))] == [F(s["sinh_coefficient"]) for s in shapes]
    signature = (LEAN / "ActualZetaOriginalJ242ExponentialSignature.lean").read_text()
    groups = re.findall(r"\(\(([0-9/]+) : ℚ\), (\d+)\)",signature)
    assert len(groups)==67
    assert [(F(f),k) for f,n in groups for k in range(int(n))] == [
       (F(f),k) for f,k in nodes[:-1]]
    # Exact rational closure of coarse complex-disc majorant:
    # |x|<2, |Im(2*pi*f*x)|<283, |sinh(x/2)|<3,
    # at most 242 + 4*(32+1) < 400 primitive summands.
    assert 242+4*(32+1) < 400
    assert F(2*4*883,25) < 283
    assert 400*10**143*2**13*3**283 < 10**400
    print("NF587 frozen NF407 byte/hash, 246 dyadic pairs, full probe shapes, 241 node alignment PASS")
    print("Uniform coefficient upper 10^143 and coarse Cauchy majorant arithmetic PASS")

if __name__ == "__main__":
    check_source(read_source())
