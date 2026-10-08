"""Exact three-retained mixed parity controls and actual certificate checks."""
from validate_native_two_retained_block_cc9 import mm,tr,minus
from validate_native_two_trial_solve_cc8 import F,solve
from pathlib import Path
import json

def det(A):
    if len(A)==1:return A[0][0]
    return sum(((-1)**j*A[0][j]*det([row[:j]+row[j+1:] for row in A[1:]]) for j in range(len(A))),F(0))

def psd3(A):
    for i in range(3):
        if A[i][i]<0:return False
        for j in range(i):
            if A[i][i]*A[j][j]-A[i][j]**2<0:return False
    return det(A)>=0

def run():
    cases=0
    # Two even complement coordinates and one odd: same original operator.
    for c in (F(1,2),F(699,1000),F(2)):
        C=[[c+1,F(1,4),F(0)],[F(1,4),c+2,F(0)],[F(0),F(0),c+3]]
        for epsilon in (F(0),F(1,100),F(-1,100)):
            B=[[F(1),F(2),F(0)],[F(-1),F(1),F(0)],[epsilon,F(0),F(1)]]
            for T in ([[F(1,10),F(1,20),F(0)],[F(-1,20),F(1,10),F(0)],[F(0),F(0),F(0)]],
                      [[F(0)]*3 for _ in range(3)]):
                CB=mm(C,T);R=minus(B,CB)
                bu=mm(tr(B),T);ub=mm(tr(T),B);uc=mm(tr(T),CB);rr=mm(tr(R),R)
                upper=[[bu[i][j]+ub[i][j]-uc[i][j]+rr[i][j]/c for j in range(3)] for i in range(3)]
                exact=mm(tr(B),tr([solve(C,list(col)) for col in zip(*B)]))
                assert psd3(minus(upper,exact))
                assert upper[1][2]==0
                assert upper[0][2]==epsilon/c
                # Keep the genuine odd mixed residual; it cannot be deleted.
                assert upper[2][2]==F(1)/c
                cases+=1
    assert not psd3([[F(1),F(0),F(2)],[F(0),F(1),F(0)],[F(2),F(0),F(1)]])
    root=Path(__file__).resolve().parents[1]/'notes/data'
    d=json.loads((root/'RPB108_ODD_ENLARGEMENT_CC10_CERTIFICATE_20261008.json').read_text())
    old=json.loads((root/'RPB108_TWO_RETAINED_BLOCK_CC9_CERTIFICATE_20261008.json').read_text())
    assert [row[:2] for row in d['original_completed_schur_lower_block'][:2]]==old['original_completed_schur_lower_block']
    assert d['odd_native_pairing_audits']==56 and d['odd_native_self_overlap_audit']
    assert d['source_reflection_parity']==-1 and d['both_signed_pole_slots']
    assert d['all_original_prime_powers']==[2,3,4,5,7,8]
    # Independently evaluate a conservative endpoint Sylvester test.
    block=d['original_completed_schur_lower_block']
    alo,ahi=map(F,block[0][0]);dlo,dhi=map(F,block[1][1]);qlo,qhi=map(F,block[2][2])
    bmax=max(map(abs,map(F,block[0][1])));xmax=max(map(abs,map(F,block[0][2])))
    independent_det2=alo*dlo-bmax*bmax
    independent_det3=qlo*independent_det2-dhi*xmax*xmax
    assert alo>0 and qlo>0 and independent_det2>0 and independent_det3>0
    assert d['three_retained_plane_positive'] and F(d['lower_determinant'][0])>0
    assert F(d['lower_determinant'][0])>F(6,10**35) and qlo>F(1227,10000)
    assert d['protected_slice_codimension']==109
    assert F(d['whole_infinite_slice_physical_margin'])>F(1,10**35)
    assert F(d['whole_infinite_slice_canonical_margin'])>F(4,10**38)
    assert not d['full_112_retained_sign'] and not d['whole_aperture_positive']
    return dict(passed=True,genuine_mixed_parity_operator_cases=cases,
        mixed_term_deletion_countercontrol_rejected=True,actual_odd_native_overlaps=57,
        historical_cc9_block_preserved=True,three_retained_plane_positive=True,
        protected_slice_codimension=109,whole_aperture_positive_claimed=False)

if __name__=='__main__':print(json.dumps(run(),indent=2))
