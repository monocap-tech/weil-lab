"""RC81: direct mixed operator residuals for the existing 64-mode Riesz trials.

Recenter the nominal residual at RC56's certified constant. Independently
replay all interval entries through reflection-reduced logarithmic moments.
"""
from fractions import Fraction as F
from pathlib import Path
from math import factorial
import json,sys,hashlib
from concurrent.futures import ProcessPoolExecutor
from validate_rpb108_rc35_enriched_residuals import I,PI,loctx,hictx,N,transformed,reflect,polyadd,scalar,integrate
from validate_rpb108_rc29_atom_reduction import legendre
from validate_rpb108_rc31_trial_riesz import mm,tr,inverse,psd
from validate_rpb108_rc47_correlated_native_transport import matrix,serialize,rows
from validate_rpb108_rc57_uniform_low_head_floor import rounded_bound
from validate_rpb108_rc60_twenty_two_mixed_residuals import init_worker,gram_worker

def build_forms(V,cmid):
    ntrial=len(V); ntarget=len(V[0]);assert (ntrial,ntarget)==(64,22)
    assert all(V[i][j]==0 for i in range(ntrial) for j in range(ntarget) if (i-j)%2)
    H=[sum((F(1,k) for k in range(1,n+1)),F(0)) for n in range(2*(N+ntrial+1)+1)]
    H2=[sum((F(1,k*k) for k in range(1,n+1)),F(0)) for n in range(len(H))]
    R=F(11,5);Z=I(1).exp()*2*PI*I(R);assert Z.h<42
    q=[I(0)]*N;l=[I(0)]*N;power=I(1)
    for n in range(1,N+1):
        power=power*Z/n
        if n%2==0:q[n-1]=(-1)**(n//2+1)*power/2
        else:
            sign=(-1)**((n-1)//2)
            q[n-1]=sign*power*I(H[n]+cmid-1)/PI
            l[n-1]=-sign*power/PI
    eps=F(4,3)*(N+ntrial)*F(42)**(N+1)/factorial(N+1);assert eps<F(1,10**40)
    moments=[[],[],[],[],[],[]];zeta=PI*PI/6
    for k in range(2*(N+ntrial)+1):
        a=k+1;ha=H[a];hb=H2[a]
        for value,arr in zip([I(F(1,a)),I(-F(1,a*a)),I(-ha/a),I(F(2,a**3)),I((ha*ha+hb)/a),I(ha/F(a*a)+hb/a)-zeta/a],moments):arr.append(value)
    P=[transformed(legendre(i)) for i in range(ntrial)];forms=[]
    for j in range(ntarget):
        v=[F(0)]*ntrial;tv=[F(0)]*ntrial
        for i in range(ntrial):
            for m,x in enumerate(P[i]):v[m]+=V[i][j]*x;tv[m]+=H[i]*V[i][j]*x
        al=[I(0)]*(N+ntrial);bl=[I(0)]*(N+ntrial)
        for p in range(N):
            for m,vm in enumerate(v):
                if vm==0:continue
                d=p+m+1;beta=F(factorial(p)*factorial(m),factorial(d))
                bl[d]=bl[d]+l[p]*I(vm*beta)
                al[d]=al[d]+(q[p]+l[p]*I(H[p]-H[d]))*I(vm*beta)
        ka=polyadd(al,reflect(al),(-1)**j)
        base=polyadd([I(x) for x in P[j]],[I(tv[m]+cmid*v[m]) for m in range(ntrial)],-1)
        forms.append((polyadd(base,ka,-1),polyadd([I(x/2) for x in v],bl,-1),polyadd([I(x/2) for x in v],scalar(reflect(bl),(-1)**j),-1)))
        print('form',j,'built',file=sys.stderr,flush=True)
    return forms,moments,R,eps

def run(paths,replay=False,saved=None):
    raw=[Path(p).read_bytes() for p in paths];boundary,prior,enriched,native,precision=map(json.loads,raw)
    hashes=[hashlib.sha256(x).hexdigest() for x in raw]
    assert boundary['input_sha256'][:3]==[hashes[i] for i in [1,3,2]]
    assert enriched['input_sha256'][1]==hashes[3] and enriched['input_sha256'][3]==hashes[4]
    assert prior['input_sha256'][3]==hashes[2] and prior['input_sha256'][5]==hashes[3]
    C=matrix(native['chebyshev_to_legendre']);Vn=matrix(enriched['enriched_native_trial_coefficients'])
    V=mm(Vn,inverse(C));assert mm(V,C)==Vn
    cmid=F(precision['constant_midpoint']);crad=F(precision['constant_radius'])
    forms,mom,R,eps=build_forms(V,cmid)
    Q=[[F(0)]*22 for _ in range(22)];E={};allow=[F(0)]*22
    old={} if saved is None else {(e['i'],e['j']):(F(e['lower']),F(e['upper'])) for e in saved['nominal_Legendre_residual_Gram_entry_enclosures']}
    for i in range(22):
        for j in range(i,22):
            if (i-j)%2:E[i,j]=(F(0),F(0))
    jobs=[(i,j) for i in range(22) for j in range(i,22) if (i-j)%2==0]
    with ProcessPoolExecutor(max_workers=8,initializer=init_worker,initargs=(forms,mom,R,replay)) as pool:
        for i,j,value in pool.map(gram_worker,jobs):
            assert hictx.subtract(value.h,value.l)<I(F(1,10**20)).h
            den=10**20
            low=F(int(loctx.multiply(value.l,I(den).l).to_integral_value(rounding='ROUND_FLOOR')),den)
            high=F(int(hictx.multiply(value.h,I(den).h).to_integral_value(rounding='ROUND_CEILING')),den)
            if saved is not None:
                low,high=old[i,j];assert I(low).l<=value.l<=value.h<=I(high).h
            E[i,j]=(low,high);Q[i][j]=Q[j][i]=(low+high)/2
            half=(high-low)/2;allow[i]+=half
            if i!=j:allow[j]+=half
            print('Gram',i,j,'enclosed',file=sys.stderr,flush=True)
    Qu=[[Q[i][j]+(i==j)*allow[i] for j in range(22)] for i in range(22)]
    Qn=mm(mm(tr(C),Qu),C);assert psd(Qu) and psd(Qn)
    mass=list(map(F,enriched['physical_mass']));D=[[mass[i]*F(i==j) for j in range(64)] for i in range(64)]
    if replay:T=[[sum((mass[q]*Vn[q][i]*Vn[q][j] for q in range(64)),F(0)) for j in range(22)] for i in range(22)]
    else:T=mm(mm(tr(Vn),D),Vn)
    delta=2*crad+eps;t=F(1,65536);rho=F(252,257)
    B=[[(1+t)*Qn[i][j]+(1+1/t)*delta**2*T[i][j] for j in range(22)] for i in range(22)]
    B,br=rounded_bound(B,1,10**24)
    Ec=[[rho*x for x in row] for row in B];Ep=[[rho*x for x in row] for row in Ec]
    oldEc=matrix(enriched['enriched_actual_canonical_Riesz_error_Gram_Loewner_upper'])
    assert psd(Ec) and psd([[oldEc[i][j]-Ec[i][j] for j in range(22)] for i in range(22)])
    comparisons=[dict(feature=j,prior_canonical_error_squared_upper=str(oldEc[j][j]),direct_canonical_error_squared_upper=str(Ec[j][j]),diagonal_upper_bound_improvement_factor=str(oldEc[j][j]/Ec[j][j])) for j in range(22)]
    result=dict(milestone='RC81',status='PASS',input_sha256=hashes,trial_dimension=64,target_dimension=22,
      recentered_nominal_constant_midpoint=str(cmid),kernel_degree=N,kernel_remainder_upper=str(eps),
      nominal_Legendre_residual_Gram_center=serialize(Q),nominal_Legendre_residual_Gram_entry_enclosures=rows(E),nominal_rounding_diagonal_allowances=list(map(str,allow)),
      nominal_native_physical_residual_Gram_Loewner_upper=serialize(Qn),actual_operator_correction_norm_upper=str(delta),Young_parameter=str(t),
      actual_physical_operator_residual_Gram_Loewner_upper=serialize(B),actual_canonical_Riesz_error_Gram_Loewner_upper=serialize(Ec),actual_physical_Riesz_error_Gram_Loewner_upper=serialize(Ep),
      transport_rounding_diagonal_allowances=list(map(str,br)),whole_matrix_Riesz_error_improves_RC67=True,diagonal_error_bound_comparisons=comparisons,
      enriched_trial_coefficients_unchanged=True,actual_Riesz_errors_evaluated_exactly=False,new_error_enclosure_propagated_into_original_source_bound=False,
      prior_RC79_actual_source_relative_upper=prior['actual_rank_38_relative_bound_for_existing_22_source_inputs'],
      required_scalar_source_budget_certified=False,actual_rank_38_scalar_budget_failure_proved=False,thirty_eight_source_input_covariance_evaluated=False,
      enlarged_Weil_floor_certified=False,whole_aperture_positivity_extended=False,RH=False,F4=False)
    if saved is not None:assert result==saved
    return result

if __name__=='__main__':
    base=Path(__file__).parent.parent/'certificates'
    defaults=[base/n for n in ['rpb108_rc80_two_allowance_boundary.json','rpb108_rc79_uniform_adjoint_tail_transport.json','rpb108_rc67_sixty_four_riesz_enrichment.json','rpb108_rc59_twenty_two_native_projection.json','rpb108_rc56_precision_attached_head.json']]
    if len(sys.argv)>1 and sys.argv[1]=='--replay':
        run(sys.argv[3:] or defaults,True,json.loads(Path(sys.argv[2]).read_text()))
        print('PASS: reflection-reduced mixed residual moments, exact native congruence and direct enriched Riesz-error comparison')
    else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))

