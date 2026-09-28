#!/usr/bin/env python3
"""GERM-73: source-word repair and fourth-section elliptic-visit control.

Repairs the GERM-72 word assignment and proves the source-exclusion strip
3h-theta < e <= 3h-alpha, where alpha=tau-3theta. The part through
epsilon=gamma is re-certified, not assumed. All numerical proof tests are
outward rational tests; all domain tests are exact affine-polytope tests.
Run with assertions enabled. No full parent symbolic replay or large
determinant inventory is executed.
"""
from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import hashlib
import json
import sys

assert __debug__, "Assertions are part of this certificate; do not use -O."
ROOT = Path(__file__).resolve().parents[1]
PINS = {
 "tools/sz_second_section_self_overlap_audit.py":
 "d0e725cc800aee9564bf79877d851c3c0d49299a4681ab9302ce80c7d3c1e8ad",
 "tools/sz_overlapping_section_audit.py":
 "0283a3412d0ef9d029e690693b472ad656602ca817e3d730d7c48234361602e4",
 "tools/sz_multivisit_section_audit.py":
 "16517b40a62f46ec32e439a42fe70e6a52cf5d665138f0c93be0ed25a6c31bb7",
 "tools/sz_mixed_return_cone_audit.py":
 "f43eaf0e86e823a2f7ebeb6580b8ea12fcf4587ad405f708c3b66d6939b2a6c0",
 "notes/_recurrence67_audit.json":
 "db2dcd27d30ca3199c444e449d7a2b93b674a7fe2b2d4cc764b38a9a863e0b09",
 "notes/_recurrence71_audit.json":
 "f837da6405cce7a6aff2f67b381e00d9986dad4e41abf142b970dd21357d132b",
}
for path, digest in PINS.items():
    assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == digest, path
import sz_second_section_self_overlap_audit as parent

old = parent.old
mat, mm, product = old.mat, old.mm, parent.product
inverse, det = parent.inverse, parent.det
af, add, sub, val, vertices = (
    parent.af, parent.add, parent.sub, parent.value, parent.vertices)

# Negative rotations: + means nonwrap, - means wrap. Words are chronological.
# Residual beta/gamma below are lengths, NOT the prime coefficient symbols.
THIRD = {
 "A": ["01-", "11+", "10+"],
 "Q": ["01-", "11+", "11+"],
 "P": ["11-", "11+", "11+", "10+"],
 "D": ["01-", "11+", "11+", "10+"],
}
BAD72 = {
 "A": ["00-", "00+", "00+"],
 "D": ["00-", "00+", "00+", "00+"],
}
FOURTH = {
 "A": ["A", "D"],           # epsilon<w, gamma<w<beta
 "O": ["A", "D", "D"],      # epsilon<w<gamma
 "J": ["Q", "P", "D"],      # 0<w<min(epsilon,gamma)
 "E": ["Q", "P"],           # gamma<w<epsilon
}
PAIRS = [(s,n) for n in (4,5) for s in range(n)]
def fifth_word(s,n):
    return ["J"] + ["A"]*(n-s-1) + ["E"]*s

def expand_third(word):
    return [x for key in word for x in THIRD[key]]
def expand_fourth(word):
    return [x for key in word for x in FOURTH[key]]
def original_of_third(word):
    return parent.expand_original(expand_third(word))

def cone_test(b, chart, sign, lower):
    q = mm(mm(inverse(mat(chart)), b), mat(chart))
    pos = [[sign*x for x in row] for row in q]
    assert all(x.lo>0 for row in pos for x in row), old.display_matrix(pos)
    delta = det(pos)
    assert delta.lo>0 and delta.lo<=1<=delta.hi
    fw = min(pos[0][0].lo+pos[1][0].lo, pos[0][1].lo+pos[1][1].lo)
    bw = min(pos[1][1].lo+pos[1][0].lo, pos[0][1].lo+pos[0][0].lo)/delta.hi
    assert fw>lower and bw>lower
    return {
      "sign":sign, "positive_conjugate":old.display_matrix(pos),
      "determinant_enclosure":old.display_matrix([[delta]]),
      "forward_lower":old.outward_decimal(fw,10),
      "backward_lower":old.outward_decimal(bw,10)}

def rational_audit():
    # The physical matrices are recalculated, not rounded fixture inputs.
    returns, pivots = parent.parent.recalculate_returns()
    first = {k:product(w,returns) for k,w in parent.FIRST.items()}
    second = {k:product(w,first) for k,w in parent.SECOND.items()}
    fixture = json.loads((ROOT/"notes/_recurrence71_audit.json").read_text())
    boxes = fixture["audit"]["rational_audit"]["second_section_maps"]
    for key,b in second.items():
        for i in range(2):
            for j in range(2):
                lo,hi = map(F,boxes[key][i][j])
                assert lo <= b[i][j].lo <= b[i][j].hi <= hi
    third = {k:product(w,second) for k,w in THIRD.items()}
    fourth = {k:product(w,third) for k,w in FOURTH.items()}
    repaired = {}
    for key,sign in (("A",-1),("O",1),("J",1)):
        repaired[key] = cone_test(fourth[key],[[1,1],[1,3]],sign,F(5,2))
        word = original_of_third(FOURTH[key])
        assert parent.determinant_exponent(word)==0
    wrong_chart = mat([[1,1],[F(3,5),F(1,5)]])
    wrong_j = mm(mm(inverse(wrong_chart),fourth["J"]),wrong_chart)
    assert all(x.lo>0 for x in wrong_j[0]) and all(x.hi<0 for x in wrong_j[1])
    # E is the correctly retained elliptic two-step word, not repaired away.
    trace = fourth["E"][0][0]+fourth["E"][1][1]
    disc = trace*trace-4*det(fourth["E"])
    assert disc.hi<0
    new = {}
    for s,n in PAIRS:
        word = fifth_word(s,n)
        b = product(word,fourth)
        sign = (-1)**(n+1) * (1 if s<=1 else -1)
        result = cone_test(b,[[1,-1],[6,-10]],sign,F(2))
        third_word = expand_fourth(word)
        original = original_of_third(third_word)
        assert len(third_word)==2*n+1
        assert len(original)==297*n+169
        assert parent.determinant_exponent(original)==0
        result.update({
          "fourth_word":word,
          "third_step_count":len(third_word),
          "original_step_count":len(original),
          "original_word_sha256":hashlib.sha256(
            json.dumps(original,separators=(",",":")).encode()).hexdigest()})
        new[f"{s}/{n}"] = result
    return {
      "physical_source_maps":"FRESH OUTWARD RATIONAL PAIRED-SOURCE SOLVES",
      "second_map_regression":"CONTAINED IN BYTE-PINNED GERM-71 BOXES",
      "layer_pivots":pivots,
      "withdrawn_72_chart_corrected_J":old.display_matrix(wrong_j),
      "withdrawn_72_chart_test":"OPPOSITE ROW SIGNS; NO OVERALL SIGN PRESERVES C+",
      "repaired_72_chart":[["1","1"],["1","3"]],
      "repaired_72_factor":"5/2", "repaired_three_words":repaired,
      "elliptic_fourth_word":FOURTH["E"],
      "elliptic_trace":old.display_matrix([[trace]]),
      "elliptic_discriminant":old.display_matrix([[disc]]),
      "new_chart":[["1","-1"],["6","-10"]],
      "new_factor":"2", "nine_fifth_returns":new}

# Exact geometry in gamma units: variables (r=beta/gamma, epsilon, seed).
def scale(c,x): return tuple(c*t for t in x)
zero,one = af(),af(1)
r,eps,seed = af(r=1),af(eta=1),af(z=1)
beta = r
alpha = add(r,one)
theta = add(scale(2,r),one)
tau = add(scale(7,r),af(4))
zeta = add(sub(tau,theta),eps)
RANGE = (sub(r,af(F(49,10))),sub(af(5),r))

def audit_margins(margins, vv):
    assert vv, "Empty certificate cell."
    weak = []
    for name,a in margins:
        values = [val(a,v) for v in vv]
        assert min(values)>=0,(name,a,min(values))
        if max(values)==0:
            assert name.endswith("global_scope"),(name,a)
            weak.append(name)
    return {"vertices":len(vv),"checked_margins":len(margins),"weak_global":weak}

@lru_cache(None)
def second_template(key):
    return parent.lift_second(key,parent.af(z=1))

def second_lift(key,y):
    # Scale every parent affine margin out of theta-normalized coordinates.
    def subst(a):
        return add(add(scale(a[0],theta),scale(a[1],tau)),
                   add(scale(a[2],zeta),scale(a[3],y)))
    target,margins = second_template(key)
    return subst(target),[(name,subst(a)) for name,a in margins]

def third_lift(key,v):
    wrap = key in ("P","D")
    n = 4 if wrap else 3
    target = add(v,beta) if wrap else sub(v,alpha)
    source_inside = key=="P"
    target_inside = key=="Q"
    points = [add(sub(tau,theta),v)]+[add(v,scale(j,theta)) for j in range(n)]
    assert points[-1] == add(sub(tau,theta),target)
    bits = [int(source_inside)]+[1]*(n-1)+[int(target_inside)]
    expected = [f"{bits[j]}{bits[j+1]}"+("-" if j==0 else "+") for j in range(n)]
    assert expected == THIRD[key]
    margins = [
      ("v>0",v),("v<theta",sub(theta,v)),
      ("target>0",target),("target<theta",sub(theta,target)),
      ("source_overlap",sub(eps,v) if source_inside else sub(v,eps)),
      ("target_overlap",sub(eps,target) if target_inside else sub(target,eps)),
      ("third_cut",sub(alpha,v) if wrap else sub(v,alpha)),
      ("four_type_global_scope",sub(beta,eps))]
    for j,key2 in enumerate(expected):
        yy,lower = second_lift(key2,points[j])
        assert yy==points[j+1]
        margins.extend((f"{j}:{name}",a) for name,a in lower)
        p = points[j+1]
        margins.append((f"no_earlier_third{j}",
          sub(sub(tau,theta),p) if j<n-1 else sub(p,sub(tau,theta))))
    return target,margins

def fourth_lift(key,w):
    word = FOURTH[key]
    n = len(word)
    points = [add(alpha,w),w,add(w,beta)]
    if n==3: points.append(add(w,scale(2,beta)))
    target = sub(w,one) if n==2 else add(w,sub(beta,one))
    assert points[-1] == add(alpha,target)
    margins = [("w>0",w),("w<beta",sub(beta,w)),
       ("fourth_return_cut",sub(w,one) if n==2 else sub(one,w)),
       ("first_target_overlap",sub(eps,w) if key in ("J","E") else sub(w,eps))]
    for j,k in enumerate(word):
        vv,lower = third_lift(k,points[j])
        assert vv==points[j+1]
        margins.extend((f"{j}:{name}",a) for name,a in lower)
        margins.append((f"no_earlier_fourth{j}",
          sub(alpha,vv) if j<n-1 else sub(vv,alpha)))
    return target,margins

def geometry_audit():
    # Prime-log vectors in old helper's (q,j,k) coordinates.
    hv,kv=old.H,old.KAP
    tv=old.sub(hv,old.mul(5,kv))
    thv=old.sub(kv,old.mul(8,tv))
    av=old.sub(tv,old.mul(3,thv))
    bv=old.sub(thv,av)
    gv=old.sub(av,bv)
    fixed = {
      "gamma_positive":gv,
      "10beta_gt_49gamma":old.sub(old.mul(10,bv),old.mul(49,gv)),
      "beta_lt_5gamma":old.sub(old.mul(5,gv),bv)}
    assert all(old.prime_sign(v[:3])>0 for v in fixed.values())
    # Counterexamples are exact affine intervals, not sampled topology.
    witnesses={}
    for key,v in (("A",scale(F(3,4),theta)),("D",scale(F(1,2),alpha))):
        _,margins=third_lift(key,v)
        vv=[(rr,F(1,2),F(0)) for rr in (F(49,10),F(5))]
        assert THIRD[key]!=BAD72[key]
        witnesses[key]=audit_margins(margins,vv)
        witnesses[key].update({"rejected":BAD72[key],"required":THIRD[key]})
    # Certify all four species through epsilon=beta.
    third_cells={}
    for key in THIRD:
        _,margins = third_lift(key,seed)
        cond = RANGE+(eps,sub(beta,eps),seed,sub(theta,seed))
        cond += tuple(a for name,a in margins if ":" not in name and
                      name in ("third_cut","source_overlap","target_overlap"))
        third_cells[key]=audit_margins(margins,vertices(cond))
    # Full fourth library across both the repair and continuation strips.
    fourth_cells={}
    for key in FOURTH:
        _,margins=fourth_lift(key,seed)
        inside = key in ("J","E")
        two = len(FOURTH[key])==2
        cond=RANGE+(eps,sub(beta,eps),seed,sub(beta,seed),
          sub(seed,one) if two else sub(one,seed),
          sub(eps,seed) if inside else sub(seed,eps))
        fourth_cells[key]=audit_margins(margins,vertices(cond))
    # Repaired GERM-72 endpoint epsilon=gamma, actual source inequalities remain strict.
    for key in ("A","J"):
        _,margins=fourth_lift(key,seed)
        cond=RANGE+(eps,sub(one,eps),sub(eps,one),seed,sub(beta,seed),
          sub(seed,one) if key=="A" else sub(one,seed))
        fourth_cells[key]["repair_endpoint_face"]=audit_margins(margins,vertices(cond))
    fifth={}
    for s,n in PAIRS:
        word=fifth_word(s,n)
        points=[seed]+[add(seed,sub(beta,af(j))) for j in range(1,n+1)]
        q=points[-1]
        cond=RANGE+(sub(eps,one),sub(beta,eps),seed,sub(one,seed),q,sub(one,q))
        cond += (sub(add(q,one),eps),) if s==0 else (
            sub(eps,add(q,af(s))),sub(add(q,af(s+1)),eps))
        margins=[("fifth_global_scope",sub(beta,eps))]
        for j,key in enumerate(word):
            target,lower=fourth_lift(key,points[j])
            assert target==points[j+1]
            margins.extend((f"{j}:{name}",a) for name,a in lower)
            margins.append((f"no_earlier_fifth{j}",
              sub(target,one) if j<n-1 else sub(one,target)))
        item=audit_margins(margins,vertices(cond))
        if s==n-1:
            face=cond+(sub(eps,beta),)
            item["epsilon_equals_beta_face"]=audit_margins(margins,vertices(face))
        fifth[f"{s}/{n}"]=item
    # Exact first-return image tiling. xi=5gamma-beta.
    xi=sub(af(5),beta)
    assert add(xi,sub(beta,af(4)))==one
    assert add(xi,sub(beta,af(5)))==zero
    # Above beta a new third inside-to-inside wrap appears: v<epsilon-beta.
    # Directly lift it from the already valid second-section system.
    delta=sub(eps,beta)
    guard_cond=RANGE+(delta,sub(one,delta),seed,sub(delta,seed))
    points=[add(sub(tau,theta),seed)]+[add(seed,scale(j,theta)) for j in range(4)]
    guard_word=["11-","11+","11+","11+"]
    margins=[]
    for j,key in enumerate(guard_word):
        target,lower=second_lift(key,points[j]);assert target==points[j+1]
        margins.extend((f"{j}:{name}",a) for name,a in lower)
    guard=audit_margins(margins,vertices(guard_cond))
    return {
      "normalization":"gamma=1; 49/10<beta/gamma<5; variables (r,epsilon,seed)",
      "exact_prime_power_checks":{k:"PASS" for k in fixed},
      "GERM72_source_word_counterexamples":witnesses,
      "four_retyped_third_cells":third_cells,"fourth_cells":fourth_cells,
      "fifth_section":"0<w<gamma inside H=(alpha,theta)",
      "physical_fifth_section":"h-beta<t<h-beta+gamma",
      "fifth_return_times":"4 for z<5gamma-beta; 5 for z>5gamma-beta",
      "fifth_map":"z -> z+(beta-4gamma) mod gamma",
      "image_tiling":"(beta-4gamma,gamma) and (0,beta-4gamma)",
      "nine_fifth_cells":fifth,
      "above_scope_guard":guard,
      "above_scope_domain":"epsilon=beta+delta; 0<v<delta<gamma",
      "above_scope_second_word":guard_word,
      "sampled_topology_in_certificate":False}

def main():
    # alpha=tau-3theta=665h-128k; 3h-alpha=128k-662h.
    final=F(16,3)*F(81,80)**3
    kap_arg=F(16,15)/F(81,80)**5
    tau_arg=F(81,80)/kap_arg**5
    theta_arg=kap_arg/tau_arg**8
    alpha_arg=tau_arg/theta_arg**3
    beta_arg=theta_arg/alpha_arg
    gamma_arg=alpha_arg/beta_arg
    l71=final/theta_arg
    l72=final/theta_arg*gamma_arg
    endpoint=final/alpha_arg
    assert l72==F(3**7373,2**8384*5**1421)
    assert endpoint==F(2**3164*5**534,3**2777)
    assert l71<l72<endpoint<final
    out={
      "pass":"SZ-KERNEL-EDGE-GERM-73","standing":"UNRATIFIED",
      "entry_commit":"e7ea1faf0a4c77439523b480b6d3f0c650c2bf99",
      "inherited_formula_scope":"2h<e<=3h",
      "repair_scope":"3h-theta<e<=3h-theta+gamma",
      "new_exclusion_scope":"3h-theta+gamma<e<=3h-alpha",
      "experimental_endpoint":"log(2^3164*5^534/3^2777)",
      "GERM72_factor_40":"WITHDRAWN: TWO SOURCE WORDS HAD WRONG INTERMEDIATE BITS",
      "source_proof_scope":"Inherited GERM-71 reductions; new word/domain and L2 proof",
      "dependency_sha256":PINS,
      "third_word_dictionary":THIRD,"fourth_word_dictionary":FOURTH,
      "original_expansion":"THIRD -> parent.SECOND -> parent.FIRST",
      "rational_audit":rational_audit(),"exact_geometry":geometry_audit(),
      "full_parent_symbolic_suites_rerun":False,"large_determinants_rerun":False,
      "canonical_cursor":"SZ-CROSS-COLLAR-3","canonical_effect":"NONE"}
    print(json.dumps(out,indent=2))

if __name__=="__main__":
    main()
