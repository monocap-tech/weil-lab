"""Exact mixed matrix-credit controls and audit of the actual CC9 block."""
from fractions import Fraction as F
from pathlib import Path
import json
from validate_native_two_trial_solve_cc8 import dot,action,solve

def mm(A,B):return [[dot(row,col) for col in zip(*B)] for row in A]
def tr(A):return [list(row) for row in zip(*A)]
def minus(A,B):return [[a-b for a,b in zip(ar,br)] for ar,br in zip(A,B)]
def psd(A):return A[0][0]>=0 and A[1][1]>=0 and A[0][0]*A[1][1]-A[0][1]*A[1][0]>=0

def run():
    controls=0
    for c in (F(1,2),F(699,1000),F(2)):
        for v in ([F(1),F(2),F(-1)],[F(-2),F(1),F(3)]):
            C=[[(c+1 if i==j else F(0))+v[i]*v[j] for j in range(3)] for i in range(3)]
            Z=[[F(1),F(0)],[F(0),F(1)],[F(0),F(0)]]
            for B in ([[F(1),F(2)],[F(-1),F(1)],[F(2),F(-2)]],
                      [[F(2),F(-1)],[F(3),F(2)],[F(1),F(4)]]):
                CZ=mm(C,Z);Q=mm(tr(Z),CZ);G=mm(tr(CZ),CZ)
                V=mm(tr(CZ),B);b=mm(tr(Z),B);GR=mm(tr(B),B)
                J=[[G[i][j]/c-Q[i][j] for j in range(2)] for i in range(2)]
                a=[[V[i][j]/c-b[i][j] for j in range(2)] for i in range(2)]
                cols=[solve(J,[a[i][j] for i in range(2)]) for j in range(2)]
                T=tr(cols)
                at=mm(tr(a),T);ta=mm(tr(T),a);tjt=mm(tr(T),mm(J,T))
                credit=[[at[i][j]+ta[i][j]-tjt[i][j] for j in range(2)] for i in range(2)]
                U=mm(Z,T);R=minus(B,mm(C,U))
                upper=[[GR[i][j]/c-credit[i][j] for j in range(2)] for i in range(2)]
                literal=mm(tr(B),U);literal2=mm(tr(U),B);cu=mm(tr(U),mm(C,U));rr=mm(tr(R),R)
                identity=[[literal[i][j]+literal2[i][j]-cu[i][j]+rr[i][j]/c for j in range(2)] for i in range(2)]
                assert identity==upper
                inverse_cols=[solve(C,list(col)) for col in zip(*B)]
                exact=mm(tr(B),tr(inverse_cols))
                assert psd(minus(upper,exact)) and psd(credit)
                controls+=1
    assert not psd([[F(1),F(2)],[F(2),F(1)]])
    root=Path(__file__).resolve().parents[1]/'notes/data'
    data=json.loads((root/'RPB108_TWO_RETAINED_BLOCK_CC9_CERTIFICATE_20261008.json').read_text())
    old=json.loads((root/'RPB108_TWO_TRIAL_SOLVE_CC8_CERTIFICATE_20261008.json').read_text())
    def overlap(a,b):return max(F(a[0]),F(b[0]))<=min(F(a[1]),F(b[1]))
    audits=[]
    for i in range(2):
        audits.append(overlap(data['mixed_trial_native'][i][0],old['source_native_cross'][i]))
        audits.append(overlap(data['mixed_trial_action'][i][0],old['source_cross_action'][i]))
        for j in range(2):
            audits.append(overlap(data['trial_native_gram'][i][j],old['original_native_trial_gram'][i][j]))
            audits.append(overlap(data['trial_action_gram'][i][j],old['actual_action_gram'][i][j]))
    assert all(audits)
    assert data['two_retained_plane_positive']
    assert F(data['lower_block_determinant'][0])>F(5,10**34)
    assert F(data['slice_retained_physical_margin'])>F(35,10**34)
    assert F(data['whole_infinite_slice_physical_margin'])>F(13,10**36)
    assert F(data['whole_infinite_slice_canonical_margin'])>F(5,10**38)
    assert data['protected_slice_codimension']==110
    return {'passed':True,'genuine_mixed_matrix_credit_cases':controls,
            'positive_diagonals_insufficient_control_rejected':True,
            'independent_actual_cc8_pairing_overlap_audits':len(audits),
            'actual_two_retained_plane_positive':data['two_retained_plane_positive'],
            'whole_infinite_slice_physical_strict_lower':'13/10^36',
            'whole_infinite_slice_canonical_strict_lower':'5/10^38',
            'protected_slice_codimension':110,
            'full_112_retained_sign_claimed':False}

if __name__=='__main__':print(json.dumps(run(),indent=2))
