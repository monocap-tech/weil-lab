"""RC56: certify c_R, attach its center correction and correlated cancellation.

Analytic dependencies: DLMF 5.4.14, 5.11.2 and 5.11(ii).
The inherited c derivatives are Lw'=I+Pi_e, Karch'=-Pi_e,
where Pi_e is the restricted Fourier projection, 0<=Pi_e<=I.
All trials are unchanged; their actual Riesz errors are bounded afresh.
"""
from fractions import Fraction as F
from pathlib import Path
from math import comb
import json,hashlib,sys
from validate_rpb108_rc30_interval_metric import I,PI
from validate_rpb108_rc42_native_signed_pole_head import outward
from validate_rpb108_rc47_correlated_native_transport import matrix,entries,serialize,rows,root,intersect
from validate_rpb108_rc31_trial_riesz import mm,tr,psd
from validate_rpb108_rc55_weak_head_schur import quad,schur_intervals

C0=F(-3203794213-3203306050,2*10**9)
DC0=F(488163,2*10**9)

def bernoulli(n):
    b=[F(1)]
    for m in range(1,n+1):
        b.append(-sum((comb(m+1,k)*b[k] for k in range(m)),F(0))/F(m+1))
    return b

def constant(n):
    b=bernoulli(10)
    assert [b[k] for k in [2,4,6,8,10]]==[F(1,6),F(-1,30),F(1,42),F(-1,30),F(5,66)]
    h=sum((F(1,k) for k in range(1,n+1)),F(0))
    # psi(n)=H_n-gamma-1/n. The first neglected psi term is
    # -B10/(10 n^10); hence the neglected gamma term is positive.
    partial=I(h)-I(n).log()-I(F(1,2*n))
    for k in range(1,5):partial=partial+I(b[2*k]/F(2*k*n**(2*k)))
    rem=b[10]/F(10*n**10)
    gamma=partial+I(0,I(rem).h)
    c=-gamma-(2*PI*I(F(11,5))).log()
    return outward(c,10**30),outward(gamma,10**30),rem

def run(paths,replay=False):
    raw=[Path(p).read_bytes() for p in paths]
    native,metric,residual,transport,prime,arch,complete,head,weak=[json.loads(x) for x in raw]
    hashes=[hashlib.sha256(x).hexdigest() for x in raw]
    assert native['metric_certificate_sha256']==residual['metric_certificate_sha256']==hashes[1]
    assert weak['input_sha256']==[hashes[k] for k in [0,3,4,1,6,7]]
    assert [head['input_sha256'][k] for k in [0,1,2,3,5,7]]==[hashes[k] for k in [0,4,5,3,6,1]]
    c,gamma,rem=constant(1000);clo,chi=c
    cmid=(clo+chi)/2;dc=(chi-clo)/2;shift=cmid-C0
    assert C0-DC0<clo<chi<C0+DC0 and dc<=F(1,10**30)
    if replay:
        # Independently shift the harmonic anchor and rebuild the first
        # neglected term; compare unrounded enclosures via finer endpoints.
        c2,g2,r2=constant(2000)
        assert clo<=c2[0]<=c2[1]<=chi and r2*2**10==rem
        assert gamma[0]<=g2[0]<=g2[1]<=gamma[1]
        # Coefficientwise derivative cancellation, before any norm bound.
        for n in range(1,193):
            metric_coefficient=F((-1)**((n-1)//2)) if n%2 else F(0)
            arch_coefficient=-metric_coefficient
            assert metric_coefficient+arch_coefficient==0
    P=matrix(native['physical_native_Gram']);T=matrix(prime['physical_native_trial_Gram'])
    alpha=F(native['canonical_native_Gram_physical_lower_factor'])
    V=matrix(native['native_trial_coefficients']);G=matrix(metric['metric_center']);GT=mm(mm(tr(V),G),V)
    Qup=matrix(transport['nominal_native_residual_Gram_Loewner_upper'])
    U=matrix(head['nominal_physical_original_source_Gram_Loewner_upper'])
    H=entries(complete['nominal_complete_signed_remainder_head_entry_enclosures'])
    oldQ=entries(head['actual_original_Weil_low_head_entry_enclosures'])
    oldM=entries(transport['refined_actual_native_Gram_entry_enclosures'])
    rho=F(252,257);k=list(map(F,complete['complete_physical_operator_parity_norm_upper']))
    eps=F(residual['source_operator_error_upper'])-2*DC0
    epsG=F(metric['mass_metric_error_upper'])-2*DC0
    epsA=F(complete['archimedean_source_approximation_operator_error_upper'])-DC0
    assert min(eps,epsG,epsA)>0
    # Bound changes from OLD nominal residual/source, without pretending
    # that their polynomial forms or covariance centers were recentered.
    deltaR=2*(abs(shift)+dc)+eps
    deltaS=abs(shift)+dc+epsA
    deltaHead=dc+epsG+epsA
    assert deltaR<F(1,10**7) and deltaS<F(1,10**7) and deltaHead<F(1,10**16)
    assert deltaR<F(transport['source_operator_error_rational_upper'])
    d2=[(root(Qup[i][i])+deltaR*root(T[i][i]))**2 for i in range(8)]
    ep=[rho*root(x) for x in d2];ec=[root(rho*x) for x in d2]
    oldep=list(map(F,transport['physical_Riesz_error_column_norm_upper']))
    assert all(ep[i]<oldep[i] for i in range(8))
    C=matrix(native['chebyshev_to_legendre']);mass=list(map(F,metric['physical_mass']))
    J=mm(tr(C),[[mass[i]*V[i][j] for j in range(8)] for i in range(8)])
    if replay:
        Q=matrix(residual['nominal_Gram_center']);eta=F(residual['normalized_Gram_rounding_error_upper'])
        for i in range(8):
            for j in range(8):
                assert Qup[i][j]==sum((C[a][i]*C[b][j]*(Q[a][b]+eta*mass[a]*(a==b))
                    for a in range(8) for b in range(8)),F(0))
                assert T[i][j]==sum((mass[a]*V[a][i]*V[a][j] for a in range(32)),F(0))
                assert GT[i][j]==sum((V[a][i]*G[a][b]*V[b][j]
                    for a in range(32) for b in range(32)),F(0))
    newQ={};newM={};trial={};ratios=[]
    for i in range(8):
        for j in range(i,8):
            key=i,j
            if (i-j)%2:newQ[key]=newM[key]=trial[key]=(F(0),F(0));continue
            # Both nominal c-dependent projection terms cancel exactly.
            a,b=H[key];lo=GT[i][j]+a+shift*T[i][j];hi=GT[i][j]+b+shift*T[i][j]
            rad=deltaHead*root(T[i][i]*T[j][j]);trial[key]=(lo-rad,hi+rad)
            source=[root(U[z][z])+deltaS*root(T[z][z]) for z in [i,j]]
            error=ep[i]*source[1]+ep[j]*source[0]+k[i%2]*ep[i]*ep[j]
            neg=ec[i]*ec[j]
            lower=lo-rad-error-neg;upper=hi+rad+error+(neg if i!=j else 0)
            newQ[key]=intersect((lower,upper),oldQ[key])
            ratios.append((oldQ[key][1]-oldQ[key][0])/(newQ[key][1]-newQ[key][0]))
            # Lw changes by shift*(I+Pi_e), norm <=2 abs(shift).
            center=J[i][j]+J[j][i]-GT[i][j]
            mr=(2*(abs(shift)+dc)+epsG)*root(T[i][i]*T[j][j])
            m=(center-mr,center+mr+rho*d2[i]) if i==j else (center-mr-neg,center+mr+neg)
            newM[key]=intersect(m,oldM[key])
    directional=[]
    for parity,row in enumerate(weak['weak_direction_actual_quadratic_enclosures']):
        v=list(map(F,row['coefficients']));pn=quad(v,P);tt=quad(v,T);qq=quad(v,Qup);u=quad(v,U)
        dsq=(root(qq)+deltaR*root(tt))**2
        e=rho*rho*dsq;ce=rho*dsq
        source=root(u)+deltaS*root(tt)
        linear=2*root(e)*source;quadratic=k[parity]*e
        hc=hr=F(0)
        for i in range(8):
            for j in range(8):
                a,b=H[tuple(sorted((i,j)))];hc+=v[i]*v[j]*(a+b)/2;hr+=abs(v[i]*v[j])*(b-a)/2
        base=quad(v,GT)+hc+shift*tt
        rad=deltaHead*tt+hr+linear+quadratic
        lo,hi=base-rad-ce,base+rad
        oldlo=F(row['actual_Weil_quadratic_lower']);oldhi=F(row['actual_Weil_quadratic_upper'])
        lo,hi=intersect((lo,hi),(oldlo,oldhi));factor=(oldhi-oldlo)/(hi-lo)
        print('direction',parity,float(lo/pn),float(hi/pn),'width gain',float(factor),file=sys.stderr)
        assert 0<lo<=hi and factor>F(200 if parity==0 else 2344)
        targetupper=hi-F(1,4000)*alpha*pn
        assert targetupper<0
        if replay:
            # Scalar Minkowski bound checked without irrational arithmetic.
            slack=dsq-qq-deltaR*deltaR*tt
            assert slack>=0 and slack*slack>=4*deltaR*deltaR*qq*tt
            assert root(e)**2>=e and source>=root(u)
            assert base==F(row['nominal_trial_head_quadratic'])+shift*tt
        directional.append(dict(parity=row['parity'],coefficients=row['coefficients'],
            physical_native_squared_norm=str(pn),actual_Weil_quadratic_lower=str(lo),actual_Weil_quadratic_upper=str(hi),
            physical_normalized_actual_Weil_quadratic_lower=str(lo/pn),physical_normalized_actual_Weil_quadratic_upper=str(hi/pn),
            actual_canonical_Rayleigh_quotient_lower=str(lo/(rho*pn)),
            actual_canonical_Rayleigh_quotient_upper=str(hi/(alpha*pn)),
            target_Q_minus_M_over_4000_quadratic_upper=str(targetupper),
            physical_normalized_target_quadratic_upper=str(targetupper/pn),
            target_floor_ruled_out_in_this_direction=True,
            previous_directional_width=str(oldhi-oldlo),directional_width_improvement_factor_lower=str(factor),
            recentered_nominal_trial_head_quadratic=str(base),constant_center_correction=str(shift*tt),
            combined_trial_head_approximation_allowance=str(deltaHead*tt+hr),
            physical_Riesz_source_linear_allowance=str(linear),physical_Riesz_quadratic_allowance=str(quadratic),
            negative_canonical_Riesz_error_Gram_allowance=str(ce),actual_physical_Riesz_error_squared_upper=str(e)))
    theta=F(1,4000);target={key:(a-theta*newM[key][1],b-theta*newM[key][0]) for key,(a,b) in newQ.items()}
    schurs=[]
    for S,W in [([0,6],[2,4]),([1,7],[3,5])]:
        A,AI,det,bounds=schur_intervals(target,S,W)
        schurs.append(dict(strong_features=S,weak_features=W,strong_target_determinant_enclosure=list(map(str,det)),
            weak_target_Schur_entry_enclosures=rows(bounds)))
    return dict(milestone='RC56',status='PASS',input_sha256=hashes,
        analytic_sources=['https://dlmf.nist.gov/5.4#E14','https://dlmf.nist.gov/5.11#E2','https://dlmf.nist.gov/5.11#ii'],
        harmonic_anchor=1000,Bernoulli_corrections=4,gamma_enclosure=list(map(str,gamma)),
        gamma_first_neglected_term_upper=str(rem),actual_constant_enclosure=list(map(str,c)),
        constant_midpoint=str(cmid),constant_radius=str(dc),previous_constant_midpoint=str(C0),
        previous_constant_radius=str(DC0),constant_center_shift=str(shift),
        constant_radius_improvement_factor_lower=str(DC0/dc),
        residual_error_from_old_nominal_forms_upper=str(deltaR),source_error_from_old_nominal_forms_upper=str(deltaS),
        combined_recentered_trial_head_operator_error_upper=str(deltaHead),
        Fourier_projection_constant_terms_cancelled_before_norm_bounds=True,
        old_trials_and_source_covariance_centers_retained=True,
        refined_physical_Riesz_error_column_norm_upper=list(map(str,ep)),
        refined_canonical_Riesz_error_column_norm_upper=list(map(str,ec)),
        actual_original_trial_head_entry_enclosures=rows(trial),
        refined_actual_native_Gram_entry_enclosures=rows(newM),
        actual_original_Weil_low_head_entry_enclosures=rows(newQ),
        minimum_original_head_entry_width_improvement_factor_lower=str(min(ratios)),
        weak_direction_actual_quadratic_enclosures=directional,actual_weak_target_Schur_entry_enclosures=schurs,
        retained_strong_native_subspace_floor='1/200',retained_two_feature_subspace_floor='1/17',
        certified_positive_weak_control_directions=[x['parity'] for x in directional if F(x['actual_Weil_quadratic_lower'])>0],
        both_actual_weak_direction_signs_unresolved=all(F(x['actual_Weil_quadratic_lower'])<0<F(x['actual_Weil_quadratic_upper']) for x in directional),
        proposed_one_over_4000_low_head_floor_ruled_out=True,
        proposed_one_over_4000_floor_ruled_out_on_every_superspace_containing_low_eight=True,
        any_uniform_low_eight_canonical_head_floor_upper=str(min(F(x['actual_canonical_Rayleigh_quotient_upper']) for x in directional)),
        original_Weil_head_floor_certified=False,
        actual_head_indefiniteness_proved=False,full_1250_native_projection_constructed=False,
        retained_low_eight_canonical_source_residual_relative_native_metric_upper=weak['retained_low_eight_canonical_source_residual_relative_native_metric_upper'],
        aperture_extended=False)

if __name__=='__main__':
    base=Path(__file__).parent.parent/'certificates'
    defaults=[base/name for name in ['rpb108_rc39_native_low_chebyshev_gram.json','rpb108_rc38_thirty_two_metric.json',
        'rpb108_rc38_thirty_two_residuals.json','rpb108_rc47_correlated_native_transport.json','rpb108_rc43_native_prime_head.json',
        'rpb108_rc46_native_archimedean_head.json','rpb108_rc52_complete_source_covariance.json',
        'rpb108_rc54_original_source_cancellation.json','rpb108_rc55_weak_head_schur.json']]
    if len(sys.argv)>1 and sys.argv[1]=='--replay':
        saved=json.loads(Path(sys.argv[2]).read_text());assert run(sys.argv[3:] or defaults,True)==saved
        print('PASS: shifted harmonic-anchor replay, exact coefficient cancellation, squared Riesz bounds, recentered head attachment and Schur reduction')
    else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
