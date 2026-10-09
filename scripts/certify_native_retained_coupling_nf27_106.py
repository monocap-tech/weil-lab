#!/usr/bin/env python3
"""NF27: original finite retained complement reaction to NF26 trials.
Not a whole-domain certificate: the full high response remains coupled.
"""
import argparse,gzip,json,hashlib
from fractions import Fraction as F
import certify_native_correlated_sources_nf25_106 as n

I=n.I
def dot(a,b):return sum((x*y for x,y in zip(a,b)),I(0))
def matvec(A,x):return [dot(row,x) for row in A]
def inverse(A):
    from decimal import Decimal as D,localcontext
    m=len(A)
    def dec(v):v=F(v);return D(v.numerator)/D(v.denominator)
    with localcontext() as ctx:
        ctx.prec=200
        M=[[dec(v.mid()) for v in row] for row in A]
        L=[[D(int(i==j)) for j in range(m)] for i in range(m)];d=[]
        for i in range(m):
            v=M[i][i]-sum((L[i][k]**2*d[k] for k in range(i)),D(0));assert v>0;d.append(v)
            for j in range(i+1,m):L[j][i]=(M[j][i]-sum((L[j][k]*L[i][k]*d[k] for k in range(i)),D(0)))/v
        J=[]
        for i in range(m):
            row=[D(0)]*m;row[i]=D(1)
            for k in reversed(range(i)):row[k]=-sum((row[j]*L[j][k] for j in range(k+1,i+1)),D(0))
            J.append([F(v) for v in row])
        B=[]
        for i in range(m):B.append([F(sum((dec(J[k][i])*dec(J[k][j])/d[k] for k in range(max(i,j),m)),D(0))) for j in range(m)])
    # Decimal values choose fixed rational preconditioners only. Positive
    # definiteness is proved by rational congruence and Gershgorin below.
    T0=[[dot(J[i],col) for col in zip(*A)] for i in range(m)]
    T=[[dot(T0[i],J[j]) for j in range(m)] for i in range(m)]
    gaps=[F(T[i][i].l,n.SCALE)-sum((T[i][j].absupper() for j in range(m) if j!=i),F(0)) for i in range(m)]
    assert min(gaps)>0
    # Residual certification of the approximate inverse, in row-sum norm.
    residual=[[I(int(i==j))-dot(B[i],col) for j,col in enumerate(zip(*A))] for i in range(m)]
    rho=max(sum((v.absupper() for v in row),F(0)) for row in residual);assert rho<1
    bnorm=max(sum(map(abs,row)) for row in B)
    error=bnorm*rho/(1-rho)
    return [[I(v-error,v+error) for v in row] for row in B],dict(congruence_Gershgorin_lower=str(min(gaps)),inverse_residual_row_norm=str(rho),inverse_entry_error_upper=str(error))

def run(targets,certificate,source):
    results=[]
    for row,cert in zip(targets['authenticated_compensated_targets'],certificate['parity_certificates']):
        assert row['parity']==cert['parity']
        ids=row['retained_indices'];x=list(map(F,row['retained_coefficients']));assert len(ids)==56
        A=[[I(*map(F,source[f'{min(i,j)},{max(i,j)}']['full'])) for j in ids] for i in ids]
        # Fixed rational basis W_j=e_j-(x_j/x_0)e_0 of x-perp.
        assert x[0]!=0
        W=[[F(0)]*55 for i in range(56)]
        for j in range(55):W[0][j]=-x[j+1]/x[0];W[j+1][j]=F(1)
        AW=[[dot(row,col) for col in zip(*W)] for row in A]
        CW=[[dot(col,row) for row in zip(*AW)] for col in zip(*W)]
        Bi,inverse_proof=inverse(CW)
        WB=[[dot(row,col) for col in zip(*Bi)] for row in W]
        K=[[dot(row,col) for col in W] for row in WB]
        trace=sum((K[i][i] for i in range(56)),I(0));assert trace.l>0
        # K is positive semidefinite algebraically: the constrained inverse
        # of the verified positive constrained form. trace(K) bounds its
        # physical operator norm without treating W as orthonormal.
        low=[I(*map(F,v)) for v in row['low_source_coordinates']]
        ylow=[I(*map(F,v)) for v in cert['retained_approximant_Ly_coordinates']]
        b=[p-y for p,y in zip(low,ylow)]
        m=F(cert['correction_norm_upper']);eps=4*F(106,125)**320/(1-F(106,125))
        from math import factorial
        eta_unit=2*n.A*eps+16*(n.A/2)**41/F(factorial(41))
        # Both uncertainties are physical balls. Pay them after the
        # quadratic form, not as independent uncertain coordinates.
        bcenter=[v.mid() for v in b]
        bhat=[I(v) for v in bcenter]
        rr=dot(bhat,matvec(K,bhat));assert rr.l>0
        radius=8*max(F(v.h-v.l,2*n.SCALE) for v in b)+m*eta_unit
        root_trace=F(n.sqrt_r(F(trace.h,n.SCALE)).h,n.SCALE)
        err=radius*root_trace
        lowerroot=max(F(0),F(n.sqrt_r(F(rr.l,n.SCALE)).l,n.SCALE)-err)
        upperroot=F(n.sqrt_r(F(rr.h,n.SCALE)).h,n.SCALE)+err
        reaction=I(lowerroot**2,upperroot**2)
        q=I(*map(F,cert['corrected_native_energy']));margin=I(*map(F,cert['sufficient_directional_Schur_lower']))
        print(row['parity'],'reaction / q',float(F((reaction/q).l,n.SCALE)),float(F((reaction/q).h,n.SCALE)),flush=True)
        w=matvec(K,bhat);frozen=[F((z.mid()*10**100).__floor__(),10**100) for z in w]
        # Enforce exact physical orthogonality by a rational rank-one correction.
        inner=sum(u*v for u,v in zip(x,frozen));mass=sum(u*u for u in x)
        frozen=[v-inner/mass*u for u,v in zip(x,frozen)]
        assert sum(u*v for u,v in zip(x,frozen))==0
        # Independently evaluate finite energy removed by THIS exact vector.
        native_gain=2*dot(frozen,b)-dot(frozen,matvec(A,frozen))
        fmass=sum(z*z for z in frozen)
        en=native_gain+I(-m*eta_unit*F(n.sqrt_r(fmass).h,n.SCALE)*2,m*eta_unit*F(n.sqrt_r(fmass).h,n.SCALE)*2)
        assert en.l>0
        assert reaction.l<=en.l<=en.h<=reaction.h
        assert (q-reaction).l>0 and (margin-reaction).l>0
        results.append(dict(parity=row['parity'],original_native_retained_complement_positive=True,constrained_inverse_verification=inverse_proof,
            constrained_inverse_trace_upper=str(F(trace.h,n.SCALE)),approximate_constrained_reaction=rr.ends(),
            physical_retained_complement_gap_lower=str(1/F(trace.h,n.SCALE)),
            retained_source_coordinate_ball_radius=str(radius),reaction_sqrt_error_upper=str(err),
            original_finite_retained_complement_reaction=reaction.ends(),retained_reaction_over_corrected_energy=(reaction/q).ends(),
            retained_reaction_over_NF26_directional_margin=(reaction/margin).ends(),
            corrected_energy_after_finite_retained_elimination=(q-reaction).ends(),
            arithmetic_score_minus_finite_reaction_NOT_collective_Schur_bound=(margin-reaction).ends(),
            exact_rational_retained_response=frozen_strings(frozen),exact_response_orthogonal_to_seed=True,
            exact_response_norm_squared=str(fmass),exact_response_native_energy_gain=en.ends(),
            native_finite_lifted_restriction_positive=True,
            high_response_on_retained_complement_certified=False,whole_aperture_positive=False))
    return dict(milestone='NF27',status='finite retained complement reaction certified',aperture='53/50',parity_certificates=results,
        full_original_Schur_couplings_computed=False,whole_aperture_positive=False,RH=False,F4=False,Lean=False)
def frozen_strings(v):return list(map(str,v))
if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('targets');a.add_argument('nf26');a.add_argument('native');a.add_argument('--output',required=True);a=a.parse_args()
    raws=[open(a.targets,'rb').read(),open(a.nf26,'rb').read(),gzip.decompress(open(a.native,'rb').read())]
    assert hashlib.sha256(raws[0]).hexdigest()=='6eee61fb4e58ac5be0e95f492f461b289da37ee13aeaa74bbf4acc06f6650c00'
    assert hashlib.sha256(raws[1]).hexdigest()=='f2010510bacac64c45ef1825cd5e2c41e395519417815a43530e44e6cfdbf930'
    assert hashlib.sha256(raws[2]).hexdigest()=='f69019a895cd675e304989cbb8209c90f033264e0aef589d4b1aa3be09cf4c81'
    r=run(json.loads(raws[0]),json.loads(raws[1]),json.loads(raws[2])['complete_form']);r['input_sha256']=[hashlib.sha256(b).hexdigest() for b in raws]
    open(a.output,'w').write(json.dumps(r,indent=2)+'\n')
