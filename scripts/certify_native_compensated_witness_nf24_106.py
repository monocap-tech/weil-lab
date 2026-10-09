#!/usr/bin/env python3
"""NF24: authenticated NF18 rational directions, two-mode original native
compensation, exact finite energy and low source-coordinate ledger.

The complete physical residual square is NOT computed. NF22's regular
kernel certificate extends to every supported polynomial with operator
error <=2a*epsilon, since the interior/boundary p(x) terms cancel.
"""
from fractions import Fraction as F
import argparse,json,gzip,hashlib
import certify_native_source_square_prime_pole_nf21_106 as base
base.G=10**180
I=base.I
A=F(53,50)
SHA=['f69019a895cd675e304989cbb8209c90f033264e0aef589d4b1aa3be09cf4c81',
     'da5fe692dc0d3a0820ccaf68217628776f08718661696dddad54012f4f3841ee',
     '0a8f4ebd0778fa5c90209b3021d22791bdb0d9b73e0f19df608e04ed9ba2bcad',
     'b3e23133db4562c1b28816e922f9c085899818399dcfcee74a323b4f6da10d5c']

def read(path,expected):
    b=open(path,'rb').read()
    if path.endswith('.gz'):b=gzip.decompress(b)
    assert hashlib.sha256(b).hexdigest()==expected
    return json.loads(b)

def square(v):
    if v.l<=0<=v.h:return I(0,max(v.l*v.l,v.h*v.h))
    return I(min(v.l*v.l,v.h*v.h),max(v.l*v.l,v.h*v.h))

def certify(paths):
    old,first,second,witness=[read(p,s) for p,s in zip(paths,SHA)]
    assert old['aperture']==first['aperture']==second['aperture']==witness['aperture']=='53/50'
    assert first['parent_sha256']==SHA[0]
    assert second['parent_E112_SHA256']==SHA[0] and second['parent_first_boundary_SHA256']==SHA[1]
    assert witness['parent_source']==SHA[0]
    assert int(witness['coefficient_denominator'])==10**55
    source={**old['complete_form'],**first['original_full_source'],**second['original_full_source']}
    assert len(source)==3422
    def Q(i,j):return I(*map(F,source[f'{min(i,j)},{max(i,j)}']['full']))
    eps=4*F(106,125)**320/(1-F(106,125))
    norm_error=2*A*eps
    assert norm_error<F(7,10**22)
    results=[]
    for parity,start in [('even',0),('odd',1)]:
        w=witness['witnesses'][parity]
        ids=w['indices'];assert ids==list(range(start,112,2))
        x=[F(int(v),10**55) for v in w['numerators']]
        high=[112+start,114+start]
        q=sum((x[i]*x[j]*Q(u,v) for i,u in enumerate(ids) for j,v in enumerate(ids)),I(0))
        t=[sum((z*Q(i,h) for i,z in zip(ids,x)),I(0)) for h in high]
        c00=Q(high[0],high[0]);c01=Q(high[0],high[1]);c11=Q(high[1],high[1])
        det=c00*c11-square(c01);assert det.l>0
        lam=[-(c11*t[0]-c01*t[1])/det,-(c00*t[1]-c01*t[0])/det]
        # Exact minimizer is enclosed. Freeze a nearby EXACT RATIONAL vector
        # so the new physical-source target is unambiguous and reproducible.
        denom=10**80
        coeff=[F((((z.l+z.h)/2)*denom).__floor__(),denom) for z in lam]
        v=x+coeff;allids=ids+high
        energy=q+2*sum((z*tj for z,tj in zip(coeff,t)),I(0))+sum(
            (coeff[i]*coeff[j]*Q(hi,hj) for i,hi in enumerate(high) for j,hj in enumerate(high)),I(0))
        assert energy.l>0
        reaction=q-energy
        assert reaction.l>0
        ratio=reaction/q
        assert ratio.l>0 and ratio.h<1
        norm_sq=sum(z*z for z in v)
        assert norm_sq<F(1001,1000)
        # Full native source pairings into E112 and measured H2; physical
        # orthonormality makes these actual source coordinates.
        lowcoords=[sum((z*Q(k,i) for i,z in zip(allids,v)),I(0)) for k in ids]
        highcoords=[sum((z*Q(k,i) for i,z in zip(allids,v)),I(0)) for k in high]
        low_sq=sum((square(z) for z in lowcoords),I(0))
        high_sq=sum((square(z) for z in highcoords),I(0))
        assert high_sq.h<F(1,10**150)
        # ||p||<1001/1000 safely dominates the certified squared norm.
        source_error=norm_error*F(1001,1000)
        assert source_error<F(1,10**21)
        # The physical F112 residual subtracts the complete E112 source
        # coordinates; its source approximation error remains unchanged.
        # A directional sufficient test is ||P_F112 L p||²<kappa*Q(p,p).
        target=F(207,1000)*energy
        root=base.sqrt(target.l)
        assert root.l>source_error
        approximant_budget=(root.l-source_error)**2
        assert approximant_budget>F(999,1000)*target.l
        results.append(dict(parity=parity,retained_indices=ids,
            retained_coefficients=[str(z) for z in x],high_indices=high,
            exact_rational_high_compensation=[str(z) for z in coeff],
            true_H2_minimizer_enclosures=[z.asstr() for z in lam],
            compensated_norm_squared=str(norm_sq),old_energy=q.asstr(),
            compensated_energy=energy.asstr(),two_mode_reaction=reaction.asstr(),
            two_mode_reaction_over_old_energy=ratio.asstr(),
            low_source_coordinates=[z.asstr() for z in lowcoords],
            measured_high_source_coordinates=[z.asstr() for z in highcoords],
            low_source_projection_squared=low_sq.asstr(),
            measured_high_source_projection_squared=high_sq.asstr(),
            arch_source_approximation_L2_error_upper=str(source_error),
            directional_residual_square_sufficient_threshold=target.asstr(),
            reconstructed_residual_square_sufficient_upper=str(approximant_budget),
            source_error_fraction_of_threshold_norm_upper=str(source_error/root.l),
            complete_source_square_computed=False,directional_residual_gate_certified=False))
    return dict(milestone='NF24',aperture='53/50',input_sha256=SHA,
        interval_grid=str(base.G),kernel_degree=320,
        all_polynomial_arch_operator_error_upper=str(norm_error),
        uniform_error_has_no_polynomial_degree_factor=True,
        source_error_identity='L_arch(p)-L_arch,N(p)=-integral (r-r_N)(abs(x-y))*p(y)dy',
        authenticated_compensated_targets=results,
        full_residual_Gram=False,whole_aperture_positive=False,RH=False,Lean=False)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('e112');p.add_argument('first');p.add_argument('second');p.add_argument('witness')
    p.add_argument('--output');a=p.parse_args()
    result=json.dumps(certify([a.e112,a.first,a.second,a.witness]),indent=2)+'\n'
    if a.output:open(a.output,'w').write(result)
    else:print(result,end='')
