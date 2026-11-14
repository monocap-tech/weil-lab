#!/usr/bin/env python3
"""NF508 exact source-pinned screening of original one-pair and k-pair support additions.

No individual physical cell energy or Gram is claimed evaluated. The theorem
uses only the certified whole-exterior Schur interval and selected dimension.
"""
import argparse, hashlib, json
from fractions import Fraction as Q
from pathlib import Path
SRC='0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce'
SEAM='c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675'
NATIVE='ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec'
AUDIT='0fd77189a8b49106ca634bda33173e8adae91126144e33ba740e437f831b9a28'
N,M,THETA=242,4096,Q(27,29)

def load(path):
    raw=Path(path).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()
def dot(a,b):return sum((x*y for x,y in zip(a,b)),Q(0))
def solve(A,b):
    t=[list(row)+[bi] for row,bi in zip(A,b)];n=len(b)
    for j in range(n):
        p=next((i for i in range(j,n) if t[i][j]),None)
        assert p is not None
        t[j],t[p]=t[p],t[j];v=t[j][j];t[j]=[x/v for x in t[j]]
        for i in range(n):
            if i!=j:
                v=t[i][j];t[i]=[x-v*y for x,y in zip(t[i],t[j])]
    return [row[-1] for row in t]

def controls(m,shift):
    xs=[Q(s*(j+1),m+1) for j in range(m) for s in (-1,1)]
    J=[(Q(1),x) for x in xs]
    W=[x**3+x**5/7+shift[0]+shift[1]*x for x in xs]
    def gram(indices):return [[sum((J[i][a]*J[i][b] for i in indices),Q(0)) for b in range(2)] for a in range(2)]
    def moments(indices):return [sum((J[i][a]*W[i] for i in indices),Q(0)) for a in range(2)]
    O=list(range(2*m));G=gram(O);a=solve(G,moments(O))
    r=[W[i]-dot(J[i],a) for i in O];R=dot(r,r);assert R>0
    inverse=[[solve(G,[Q(int(j==k)) for j in range(2)])[i] for k in range(2)] for i in range(2)]
    trace_total=energy_total=Q(0);bad_t=bad_e=0
    theta=Q(1,2);gamma=R/100;threshold=(1-theta)*(R-gamma)
    for j in range(m):
        D=(2*j,2*j+1);out=[i for i in O if i not in D]
        C=gram(D);tau=sum((inverse[i][k]*C[k][i] for i in range(2) for k in range(2)),Q(0))
        e=sum((r[i]**2 for i in D),Q(0))
        k=[sum((J[i][a]*r[i] for i in D),Q(0)) for a in range(2)]
        gain=e+dot(k,solve(gram(out),k))
        new=sum((W[i]**2 for i in out),Q(0))-dot(moments(out),solve(gram(out),moments(out)))
        assert R-new==gain and gain>=e>=0 and tau>=0
        if tau<1: assert gain<=e/(1-tau)
        if tau<theta and e<threshold: assert new>gamma
        trace_total+=tau;energy_total+=e
        bad_t+=int(tau>=theta);bad_e+=int(e>=threshold)
    assert trace_total==2 and energy_total==R
    assert bad_t<=2//theta and bad_e<=R//threshold
    assert m-bad_t-bad_e>=m-(2//theta)-(R//threshold)
    return m

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--native',required=True);ap.add_argument('--audit',required=True);ap.add_argument('--output',required=True)
    o=ap.parse_args();n,sh=load(o.native);a,ah=load(o.audit)
    assert (sh,ah)==(NATIVE,AUDIT)
    assert n['pass']=='NF504-native' and a['pass']=='NF505'
    assert a['original_nf504_original_entire_242_exterior_4096bit_native_json_sha256']==sh
    assert n['source_original_NF407_sha256']==a['original_nf407_source_sha256']==SRC
    assert n['source_original_NF406_sha256']==a['original_nf406_seams_sha256']==SEAM
    assert n['original_selected_J_dimension']==a['original_selected_true_J_dimension']==N
    assert n['original_exterior_center_radius']=='549/500'
    assert n['original_support_saturated_physical_Hilbert_gate']==a['original_original_S_support_saturated_physical_Hilbert_verdict']=='CERTIFIED_PHYSICAL_SUPPORT_NO_GO'
    assert n['original_weil_multiplier_source_image_domain']=='OPEN'
    lo,hi=map(Q,n['original_original_saturated_exterior_residual_outward']);gamma=Q(n['original_original_gamma_squared'])
    assert gamma==Q(a['original_original_gamma_squared']) and 0<gamma<lo<=hi
    reduction=lo-gamma;E=(1-THETA)*reduction
    leverage_bad=N//THETA;energy_bad=hi//E;safe=M-int(leverage_bad)-int(energy_bad)
    assert (leverage_bad,energy_bad,safe)==(259,14,3823)
    bad_expected=Q(N)/THETA+hi/E
    fractions={str(k):str(1-Q(k,M)*bad_expected) for k in (1,2,4,8,14)}
    assert all(Q(v)>0 for v in fractions.values()) and 1-Q(15,M)*bad_expected<0
    tested=sum(controls(m,shift) for m in (12,14,16) for shift in ((Q(0),Q(0)),(Q(13,19),Q(-8,23)),(Q(10**11),-Q(10**17))))
    assert tested==126
    out={'pass':'NF508-exact-source-aggregate-screen','scope':'At least 3823 of 4096 single mirrored interior-pair support enlargements fail unchanged NF404; identities unknown; source/domain and RH OPEN',
      'native_sha256':sh,'nf505_audit_sha256':ah,'original_source_sha256':SRC,'original_seams_sha256':SEAM,
      'selected_rank':N,'mirror_pair_cells':M,'pair_total_physical_width':str(Q(2)*Q(549,500)/M),
      'old_exterior_schur_interval':[str(lo),str(hi)],'fixed_nf404_gamma_squared':str(gamma),
      'theta_trace_leverage':str(THETA),'threshold_local_residual_energy':str(E),
      'max_high_leverage_cells':int(leverage_bad),'max_high_energy_cells':int(energy_bad),
      'certified_at_least_single_pair_no_go':safe,'not_excluded_single_pairs_at_most':M-safe,
      'fraction_of_all_k_pair_subsets_certified_no_go_lower':fractions,'largest_tested_k_with_positive_lower':14,
      'toy_exact_rational_controls':tested,'individual_cell_indices_located':False,
      'original_per_cell_source_integrals_completed':False,'Weil_multiplier_image_graph_domain':'OPEN','W_ODD_NEG':'OPEN','RH':'OPEN'}
    Path(o.output).write_text(json.dumps(out,indent=2)+'\n')
    print('NF508 exact rational source-custody + 126 finite-dimensional controls PASS')
    print('At least',safe,'of',M,'single mirrored pair local additions fail unchanged NF404; at most',M-safe,'unexcluded')
    print('No physical cell identities or Weil-source/domain admissibility established')
if __name__=='__main__':main()
