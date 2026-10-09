#!/usr/bin/env python3
"""Native observed lower bound for collective retained high-source loading.

Fixed rational preconditioners select an inverse; outward rational
congruence and Neumann checks alone certify it. No numerical proof data.
"""
import argparse,gzip,hashlib,json
from fractions import Fraction as F
from pathlib import Path
import certify_native_retained_coupling_nf27_106 as c
from certify_seed_assembly_cc69 import sqrt_bounds

def det3(A):
    return A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])-A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])+A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0])

def run(targets,nf26,nf27,native,boundary):
    I=c.I;n=c.n;k=F(207,1000);rows=[]
    for t,z,f in zip(targets['authenticated_compensated_targets'],nf26['parity_certificates'],nf27['parity_certificates']):
        assert t['parity']==z['parity']==f['parity']
        ids=t['retained_indices'];x=list(map(F,t['retained_coefficients']))
        A=[[I(*map(F,native[f'{min(i,j)},{max(i,j)}']['full'])) for j in ids] for i in ids]
        W=[[F(0)]*55 for i in range(56)]
        for j in range(55):W[0][j]=-x[j+1]/x[0];W[j+1][j]=F(1)
        assert all(sum(x[i]*W[i][j] for i in range(56))==0 for j in range(55))
        AW=[[c.dot(row,col) for col in zip(*W)] for row in A]
        CW=[[c.dot(col,row) for row in zip(*AW)] for col in zip(*W)]
        inv,proof=c.inverse(CW)
        assert proof==f['constrained_inverse_verification']
        h=112 if t['parity']=='even' else 113
        g=[I(*map(F,boundary[f'{i},{h}']['full'])) for i in ids]
        gw=[c.dot(col,g) for col in zip(*W)]
        observed=c.dot(gw,c.matvec(inv,gw))/k
        assert observed.l>n.SCALE
        # theta = ||P_F L W A_W^(-1/2)||^2/kappa. A single unit
        # high test gives theta >= g_W^* A_W^-1 g_W/kappa.
        p=F(z['coarse_response_over_corrected_energy'][1])
        reaction=F(f['retained_reaction_over_corrected_energy'][1])
        assert p+reaction<1
        theta=F(1,100) if t['parity']=='even' else F(4,25)
        _,rootup=sqrt_bounds(p*theta*reaction)
        slack=1-p-reaction-theta-2*rootup
        assert slack>0
        # The true C-weighted loading also has a native lower bound:
        # <z,C^-1 z> >= |<e_h,z>|^2/Q(e_h). This follows by
        # optimizing the high-form variational principle on span(e_h).
        highq=I(*map(F,boundary[f'{h},{h}']['full']))
        assert highq.l>0
        true_loading_lower=F(observed.l,n.SCALE)*k/F(highq.h,n.SCALE)
        rootlo,_=sqrt_bounds(p*reaction*true_loading_lower)
        true_gate_excess=p+reaction+true_loading_lower+2*rootlo-1
        assert true_gate_excess>0
        # The displayed robust threshold is diagnostic only; rational
        # target/slack checks above provide the proof.
        rows.append(dict(parity=t['parity'],original_observed_high_degree=h,
            constrained_inverse_verification=proof,
            native_observed_loading_interval=observed.ends(),
            complete_loading_at_least_observed_lower=True,
            original_unlifted_background_scalar_floor_gate_rejected=True,
            source_ratio_upper=str(p),finite_reaction_ratio_upper=str(reaction),
            hypothetical_sufficient_collective_loading_target=str(theta),
            hypothetical_robust_gate_slack_lower=str(slack),
            native_true_response_loading_lower=str(true_loading_lower),
            robust_true_response_gate_excess_using_unchanged_seed_bound=str(true_gate_excess),
            robust_true_response_gate_with_unchanged_seed_bound_rejected=True,
            loading_target_certified=False,whole_aperture_positive=False))
    crossings=[]
    for s in [F(7,9)-F(1,100),F(7,9),F(7,9)+F(1,100)]:
        M=[[F(1),F(1,3),F(1,3)],[F(1,3),F(1),-s],[F(1,3),-s,F(1)]]
        d=det3(M)
        assert d==1-F(2,9)-s*s-F(2,9)*s
        assert 1-s*s>0 and F(8,9)>0
        expected=1 if s<F(7,9) else -1 if s>F(7,9) else 0
        assert (d>0)-(d<0)==expected
        crossings.append(dict(high_background_coupling=str(s),determinant=str(d),
            finite_restriction_positive=True,seed_high_Schur_positive=True,
            seed_score_minus_finite_reaction=str(F(7,9)),whole_sign=expected))
    levels=[]
    for level in [F(1,1000),F(1,10),F(2)]:
        M=[[1+level,F(1,3),F(1,3)],[F(1,3),1+level,-F(7,9)],[F(1,3),-F(7,9),1+level]]
        assert det3(M)>0 and (1+level)**2-F(1,9)>0
        # Crossing matrix is PSD with rank two, so its whole-mass
        # shift has exact smallest physical eigenvalue level.
        levels.append(dict(whole_mass_shift=str(level),ground_level=str(level),determinant=str(det3(M))))
    return dict(milestone='CC70',aperture='53/50',native_finite_lifted_dimension=112,
        parity_rows=rows,genuine_three_block_crossings=crossings,positive_whole_mass_levels=levels,
        robust_gate='p+t+theta+2*sqrt(p*t*theta)<1',
        full_collective_Schur_certified=False,uniform_defect_relative_frame=False,
        full_Weil_nonimplication_claimed=False,whole_aperture_positive=False,RH=False,F4=False,Lean=False)

if __name__=='__main__':
    p=argparse.ArgumentParser()
    for a in ['targets','nf26','nf27','native','boundary']:p.add_argument(a)
    p.add_argument('--output',required=True);a=p.parse_args()
    raw=[Path(v).read_bytes() for v in [a.targets,a.nf26,a.nf27]]
    raw += [gzip.decompress(Path(v).read_bytes()) for v in [a.native,a.boundary]]
    hashes=[hashlib.sha256(v).hexdigest() for v in raw]
    assert hashes==['6eee61fb4e58ac5be0e95f492f461b289da37ee13aeaa74bbf4acc06f6650c00','f2010510bacac64c45ef1825cd5e2c41e395519417815a43530e44e6cfdbf930','2110e07c7a7e39d2b454cff364c0863f6f3e3ff151cf72309999130f5e17fe42','f69019a895cd675e304989cbb8209c90f033264e0aef589d4b1aa3be09cf4c81','da5fe692dc0d3a0820ccaf68217628776f08718661696dddad54012f4f3841ee']
    ds=list(map(json.loads,raw));result=run(*ds[:3],ds[3]['complete_form'],ds[4]['original_full_source']);result['input_sha256']=hashes
    Path(a.output).write_text(json.dumps(result,indent=2)+'\n')
    for r in result['parity_rows']:print(r['parity'],'loading lower',float(F(r['native_observed_loading_interval'][0])),'hypothetical target',r['hypothetical_sufficient_collective_loading_target'])
