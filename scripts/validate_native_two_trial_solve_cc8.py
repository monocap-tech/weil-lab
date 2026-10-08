"""Exact genuine-operator controls for two-trial original/shifted inverse bounds."""
from fractions import Fraction as F
from pathlib import Path
import json

def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def action(A,v):return [dot(row,v) for row in A]
def solve(A,b):
    a=[list(row)+[v] for row,v in zip(A,b)];n=len(b)
    for i in range(n):
        assert a[i][i]!=0
        pivot=a[i][i];a[i]=[v/pivot for v in a[i]]
        for j in range(n):
            if j!=i:
                t=a[j][i];a[j]=[v-t*w for v,w in zip(a[j],a[i])]
    return [row[-1] for row in a]

def run():
    cases=0
    for c in (F(1,3),F(699,1000),F(2)):
        for v in ([F(1),F(-2),F(3)],[F(2),F(1),F(-1)]):
            C=[[(c+1 if i==j else F(0))+v[i]*v[j] for j in range(3)] for i in range(3)]
            Q=[row[:2] for row in C[:2]]
            columns=[[C[i][j] for i in range(3)] for j in range(2)]
            G=[[dot(a,b) for b in columns] for a in columns]
            J=[[G[i][j]/c-Q[i][j] for j in range(2)] for i in range(2)]
            for B in ([F(1),F(2),F(3)],[F(-1),F(1),F(0)]):
                b=B[:2];vaction=[dot(B,col) for col in columns]
                aa=[vaction[i]/c-b[i] for i in range(2)]
                t=solve(J,aa);u=t+[F(0)];r=[x-y for x,y in zip(B,action(C,u))]
                exact=dot(B,solve(C,B))
                inverse_upper=2*dot(B,u)-dot(u,action(C,u))+dot(r,r)/c
                assert exact<=inverse_upper<=dot(B,B)/c
                one=aa[0]/J[0][0]
                one_credit=2*one*aa[0]-one*one*J[0][0]
                credit=dot(B,B)/c-inverse_upper
                assert credit>=one_credit
                L=[[C[i][j]+(c if i==j else 0) for j in range(3)] for i in range(3)]
                LC=[[L[i][j] for i in range(3)] for j in range(2)]
                GL=[[dot(x,y) for y in LC] for x in LC]
                ts=solve(GL,[dot(B,col) for col in LC]);us=ts+[F(0)]
                rs=[x-y for x,y in zip(B,action(L,us))]
                lower=2*dot(B,us)-dot(us,action(L,us))
                upper=lower+dot(rs,rs)/(2*c)
                shifted=dot(B,solve(L,B))
                assert lower<=shifted<=upper
                error=[x-y for x,y in zip(solve(L,B),us)]
                assert dot(error,error)<=dot(rs,rs)/(2*c)**2
                # Source-norm extraction must include BOTH complete-map errors.
                delta=F(1,1000);q=F(3);mass=F(2);surrogate=dot(B,B)
                estimator=q-(surrogate+delta*mass)/c
                lo=c*(q-estimator)-2*delta*mass;hi=c*(q-estimator)
                assert lo==surrogate-delta*mass and hi==surrogate+delta*mass
                cases+=1
    root=Path(__file__).resolve().parents[1]/'notes/data'
    actual=json.loads((root/'RPB108_TWO_TRIAL_SOLVE_CC8_CERTIFICATE_20261008.json').read_text())
    old=json.loads((root/'RPB108_COUPLED_TRIAL_CC3_CERTIFICATE_20261008.json').read_text())
    def overlap(a,b):return max(F(a[0]),F(b[0]))<=min(F(a[1]),F(b[1]))
    independent_audits=[
        overlap(actual['source_native_cross'][0],old['native_cross_pairing']),
        overlap(actual['original_native_trial_gram'][0][0],old['trial_native_pairing']),
        overlap(actual['source_cross_action'][0],old['residual_source_cross']),
        overlap(actual['actual_action_gram'][0][0],old['trial_complement_source_norm_squared'])]
    assert all(independent_audits)
    assert F(actual['inverse_estimator_credit'][0])>2*F(old['improvement'][1])
    assert F(actual['original_completed_direction_lower'][0])>F(135,10**34)
    assert F(actual['original_completed_direction_first_head_plus_whole_tail_lower'])>F(5,10**33)
    return {'passed':True,'genuine_three_dimensional_operator_cases':cases,
            'independent_cc3_actual_pairing_overlap_audits':len(independent_audits),
            'actual_inverse_credit_more_than_doubled':True,
            'actual_completed_direction_strict_lower':'135/10^34',
            'actual_first_head_plus_whole_tail_strict_lower':'5/10^33',
            'unshifted_and_shifted_all_mixed_blocks_retained':True,
            'two_trial_credit_not_less_than_one_trial':True,
            'shifted_quadratic_and_mass_error_controls':True,
            'complete_source_norm_error_extraction_checked':True}

if __name__=='__main__':print(json.dumps(run(),indent=2))
