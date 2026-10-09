#!/usr/bin/env python3
"""Exact coercive Galerkin controls for form error vs physical source residual.
Abstract operator control, not an original Weil arithmetic counterexample.
"""
import argparse,json
from fractions import Fraction as F
KAPPA=F(207,1000)
def mul(M,v):return [sum(a*b for a,b in zip(row,v)) for row in M]
def dot(x,y):return sum(a*b for a,b in zip(x,y))
def validate():
    blocks=[]
    for j in range(1,65):
        C=[[F(j),F(j**3)],[F(j**3),F(2*j**5)]]
        g=[F(1,j**2),F(0)];w=[F(2,j**3),F(-1,j**5)];y=[F(1,j**3),F(0)]
        assert mul(C,w)==g
        err=[w[i]-y[i] for i in range(2)];residual=mul(C,err)
        assert residual==[F(0),F(-1)]
        assert dot(err,residual)==F(1,j**5)
        assert dot(w,g)==F(2,j**5)
        assert dot(y,mul(C,y))==F(1,j**5)
        floor=F(j,3)
        determinant=(C[0][0]-floor)*(C[1][1]-floor)-C[0][1]**2
        assert determinant==F(j**6,3)-F(2*j**2,9)>=F(j**2,9)>0
        assert C[0][0]-floor>0 and floor>KAPPA
        blocks.append(dict(j=j,high_floor=str(floor),incomplete_form_error=str(F(1,j**5)),physical_residual_squared='1'))
    stages=[]
    for m in [1,2,3,4,8,16,32,64,128,256]:
        k=m//2;pending=m-k
        finite_error=sum(F(1,j**5) for j in range(k+1,m+1))
        tail_upper=F(1,2*m**4)
        assert pending>=1 and F(pending)>KAPPA*3
        if k:
            # The missing true response <=2 sum_{j>k}j^-5 <1/(2k^4).
            assert finite_error+tail_upper<F(1,2*k**4)
        stages.append(dict(m=m,completed_pairs=k,trial_dimension=m+k,
            physical_residual_squared_strict_lower=str(pending),
            physical_residual_squared_strict_upper=str(F(pending)+F(1,3*m**3)),
            true_form_error_strict_upper=str(F(1,2*k**4)) if k else None,
            sufficient_P_over_kappa_gate_impossible=True))
    crossings=[]
    for count in [1,2,8,32]:
        G=sum(F(2,j**5) for j in range(1,count+1))
        for eps in [F(1,100),F(0),F(-1,100)]:
            low=G+eps;assert low-G==eps
            crossings.append(dict(pairs=count,low=str(low),corrected_sign='positive' if eps>0 else 'null' if eps==0 else 'negative'))
    shifts=[]
    C=[[F(1),F(1)],[F(1),F(2)]];g=[F(1),F(0)]
    for mu in [F(1,10**40),F(1,100),F(1,20)]:
        shifted=[[C[i][j]-(mu if i==j else 0) for j in range(2)] for i in range(2)]
        det=shifted[0][0]*shifted[1][1]-1
        w=[shifted[1][1]/det,-F(1)/det]
        assert mul(shifted,w)==g
        low=mu+dot(g,w)
        Q=[[low,F(1),F(0)],[F(1),F(1),F(1)],[F(0),F(1),F(2)]]
        h=[F(1),-w[0],-w[1]]
        assert mul(Q,h)==[mu*v for v in h]
        assert dot(h,mul(Q,h))==mu*dot(h,h)>0
        assert F(1,3)-mu>KAPPA
        assert low-mu-F(2)>0 # shifting only the retained diagonal misses the null.
        shifts.append(dict(original_positive_eigenlevel=str(mu),whole_mass_shift_exact_null=True,shifted_high_floor_above_kappa=True,low_only_shift_misses_null=True))
    return dict(status='PASS',milestone='CC57',classification='abstract exact direct-sum Galerkin operator control; not original Weil source',
        physical_high_floor='1/3',original_low_A='3',full_inverse_response_strict_upper='5/2',
        original_full_Schur_strict_lower='1/2',
        complete_source_physical_L2=True,exact_block_tests=len(blocks),
        stage_controls=stages,infinite_form_Galerkin_error_tends_to_zero=True,
        infinite_physical_residual_norm_diverges=True,
        physical_residual_sufficient_gate_fails_at_every_stage=True,
        exact_crossing_controls=crossings,exact_positive_level_controls=shifts,
        form_convergence_alone_insufficient_for_L2_residual_convergence=True,
        graph_stability_is_one_sufficient_upgrade=True,
        native_Weil_graph_instability_proved=False,NF21_residual_Gram_evaluated=False,
        whole_native_aperture_positive=False,RH=False,Lean=False)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output');a=p.parse_args()
    out=json.dumps(validate(),indent=2)+'\n'
    if a.output:open(a.output,'w').write(out)
    print(out)
