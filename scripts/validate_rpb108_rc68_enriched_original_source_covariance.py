"""RC68: enriched complete original source covariance and rank-22 residual.

Fplus_nom=q+K_nom V; actual cancellation uses q+K_actual V.
Actual canonical source columns are i*(q+K_actual iR), not these trials.
"""
from fractions import Fraction as F
from pathlib import Path
from math import factorial,comb
from concurrent.futures import ProcessPoolExecutor
import json,sys,hashlib
from validate_rpb108_rc30_interval_metric import I,PI
from validate_rpb108_rc29_atom_reduction import legendre
from validate_rpb108_rc31_trial_riesz import mm,tr,psd,inverse
from validate_rpb108_rc35_enriched_residuals import transformed,polyadd,reflect,scalar,integrate
from validate_rpb108_rc60_twenty_two_mixed_residuals import build_forms,pairing
from validate_rpb108_rc42_native_signed_pole_head import outward,rational_interval
from validate_rpb108_rc43_native_prime_head import shift,poly_value
from validate_rpb108_rc48_prime_source_covariance import geometry,integrate_product
from validate_rpb108_rc49_prime_pole_covariance import exact_exponential_integral
from validate_rpb108_rc52_complete_source_covariance import primitives
from validate_rpb108_rc47_correlated_native_transport import matrix,serialize,entries,rows,root,intersect
from validate_rpb108_rc56_precision_attached_head import C0
from validate_rpb108_rc57_uniform_low_head_floor import rounded_bound

DIM=22;B=F(11,10);R=2*B;RHO=F(252,257)

def init_worker(data):
    global WORK
    WORK=data

def base_worker(ij):
    i,j=ij;forms,mom,replay=WORK
    return i,j,outward(pairing(forms[i],forms[j],mom,R,replay),10**20)

def prime_worker(ij):
    i,j=ij;segments,replay=WORK;value=I(0)
    for left,right,source,affine in segments:
        if replay:
            value=value+B*(right-left)*sum((a*b/F(k+l+1) for k,a in enumerate(affine[i]) for l,b in enumerate(affine[j])),I(0))
        else:value=value+integrate_product(source[i],source[j],left,right,B)
    return i,j,outward(value,10**20)

def cross_worker(i):
    forms,segment_data,replay=WORK;A,L,M=forms[i];out=[I(0)]*DIM
    for moments,sources in segment_data:
        weights=[]
        for l in range(64):
            a=sum((x*moments[0][k+l] for k,x in enumerate(A)),I(0))
            a=a+(2 if replay else 1)*sum((x*moments[1][k+l] for k,x in enumerate(L)),I(0))
            if not replay:a=a+sum((x*moments[2][k+l] for k,x in enumerate(M)),I(0))
            weights.append(R*a)
        for j in range(DIM):
            if (i-j)%2==0:out[j]=out[j]+sum((a*b for a,b in zip(weights,sources[j])),I(0))
    return i,out

def exponential_worker(j):
    forms,mom,Q,replay=WORK;A,L,M=forms[j];N=128
    ep=[I(B**n/factorial(n)) for n in range(N+1)];em=[I((-B)**n/factorial(n)) for n in range(N+1)]
    tail=2*B**129/factorial(129);assert B/130<F(1,2)
    value=integrate(A,ep,mom[0])+integrate(L,ep,mom[1])
    value=value+((-1)**j*I(B).exp()*integrate(L,em,mom[1]) if replay else integrate(M,ep,mom[2]))
    value=R*I(-B/2).exp()*value
    if replay:
        def l1(p):return sum((max(abs(F(x.l)),abs(F(x.h))) for x in p),F(0))
        radius=I(R*tail)*(I(l1(A))+I(l1(L))*(1+I(B).exp()))
    else:radius=I(tail*root(R*Q[j,j][1]))
    return j,outward(value+I(-radius.h,radius.h),10**20)

def prime_exponential_worker(j):
    segments,T,kp,replay=WORK;value=I(0);b=B/2;N=100
    for left,right,source,_ in segments:
        if replay:
            ep=[I(b**n/factorial(n)) for n in range(N+1)]
            value=value+integrate_product(source[j],ep,left,right,B)
        else:value=value+exact_exponential_integral(source[j],left,right)
    if replay:
        tail=2*b**101/factorial(101);radius=I(tail*kp*root(R*T[j][j]))
        value=value+I(-radius.h,radius.h)
    return j,outward(value,10**20)

from validate_rpb108_rc65_parity_projected_residual_refinement import add,scale,block,cong,relative

def source_forms(enriched,native,arch,precision):
    V=matrix(enriched['enriched_native_trial_coefficients']);C=matrix(native['chebyshev_to_legendre']);ntrial=64;N=192
    H=[sum((F(1,k) for k in range(1,n+1)),F(0)) for n in range(2*(N+ntrial)+2)]
    H2=[sum((F(1,k*k) for k in range(1,n+1)),F(0)) for n in range(len(H))]
    cmid=F(precision['constant_midpoint']);Z=I(1).exp()*2*PI*I(R);assert Z.h<42
    q=[];l=[];power=I(1)
    for n in range(1,N+1):
        power=power*Z/n
        if n%2==0:q.append((-1)**(n//2+1)*power/2);l.append(I(0))
        else:
            sign=(-1)**((n-1)//2);q.append(sign*power*I(H[n]+cmid-1)/PI);l.append(-sign*power/PI)
    moments=[[],[],[],[],[],[]];zeta=PI*PI/6
    for k in range(2*(N+ntrial)+1):
        a=k+1;ha=H[a];hb=H2[a]
        for value,arr in zip([I(F(1,a)),I(-F(1,a*a)),I(-ha/a),I(F(2,a**3)),I((ha*ha+hb)/a),I(ha/F(a*a)+hb/a)-zeta/a],moments):arr.append(value)
    LP=[transformed(legendre(n)) for n in range(ntrial)]
    reg=list(map(F,arch['regular_kernel_coefficients']));forms=[];trials=[];targets=[]
    for j in range(DIM):
        v=[sum((V[n][j]*(LP[n][k] if k<=n else 0) for n in range(ntrial)),F(0)) for k in range(ntrial)]
        target=[sum((C[n][j]*(LP[n][k] if k<=n else 0) for n in range(DIM)),F(0)) for k in range(DIM)]
        al=[I(0)]*(N+ntrial);bl=[I(0)]*(N+ntrial);regular=[F(0)]*(N+ntrial+1)
        for p in range(N):
            for m,vm in enumerate(v):
                if vm==0:continue
                d=p+m+1;beta=F(factorial(p)*factorial(m),factorial(d))
                bl[d]+=l[p]*I(vm*beta)
                al[d]+=(q[p]+l[p]*I(H[p]-H[d]))*I(vm*beta)
                regular[d]+=R*reg[p]*R**p*vm*beta
        A=polyadd([I(x) for x in target],polyadd(al,reflect(al),(-1)**j),-1)
        A=polyadd(A,polyadd([I(x) for x in regular],reflect([I(x) for x in regular]),(-1)**j),-1)
        forms.append((A,scalar(bl,-1),scalar(reflect(bl),-(-1)**j)));trials.append(v);targets.append(target)
        print('enriched original source form',j,'built',file=sys.stderr,flush=True)
    return forms,moments,trials,targets

def head_worker(ij):
    i,j=ij;forms,trials,mom,segs,polys,replay=WORK
    A,L,M=forms[j];v=[I(x) for x in trials[i]]
    value=R*(integrate(v,A,mom[0])+2*integrate(v,L,mom[1])) if replay else R*(integrate(v,A,mom[0])+integrate(v,L,mom[1])+integrate(v,M,mom[2]))
    prime=I(0)
    for left,right,source,_ in segs:
        if replay:
            length=right-left;v0=shift([I(x) for x in polys[i]],left);s0=shift(source[j],left);powers=[I(1)]
            for _ in range(63):powers.append(powers[-1]*length)
            prime+=B*length*sum((a*powers[k]*b*powers[l]/F(k+l+1) for k,a in enumerate(v0) for l,b in enumerate(s0)),I(0))
        else:prime+=integrate_product([I(x) for x in polys[i]],source[j],left,right,B)
    return i,j,outward(value+prime,10**20)

def run(paths,replay=False,saved=None):
    raw=[Path(p).read_bytes() for p in paths];enriched,native,precision,prime,pole,arch,transport=[json.loads(x) for x in raw]
    hashes=[hashlib.sha256(x).hexdigest() for x in raw]
    assert enriched['input_sha256'][1:]==[hashes[1],transport['input_sha256'][1],hashes[2]]
    assert transport['input_sha256'][0]==hashes[1] and transport['input_sha256'][5]==hashes[2]
    assert transport['certified_physical_archimedean_remainder_norm_upper']=='643/100'
    assert [precision['input_sha256'][k] for k in [4,5]]==[hashes[k] for k in [3,5]]
    assert prime['native_certificate_sha256']==pole['source_certificate_sha256']
    forms,mom,trials,targets=source_forms(enriched,native,arch,precision)
    V=matrix(enriched['enriched_native_trial_coefficients']);mass=list(map(F,enriched['physical_mass']))
    D=[[mass[i]*(i==j) for j in range(64)] for i in range(64)];T=mm(mm(tr(V),D),V)
    G=matrix(enriched['recentered_nominal_metric_center']);GT=mm(mm(tr(V),G),V)
    C=matrix(native['chebyshev_to_legendre']);X=[[mass[i]*C[i][j] if i<DIM else F(0) for j in range(DIM)] for i in range(64)];J=mm(tr(X),V)
    LP=[legendre(n) for n in range(64)];polys=[[sum((V[n][j]*(LP[n][k] if k<=n else 0) for n in range(64)),F(0)) for k in range(64)] for j in range(DIM)]
    terms,geometry_segments=geometry(prime);assert len(geometry_segments)==15
    shifted=[[shift([I(a) for a in poly],term['offset']) for poly in polys] for term in terms]
    translated=[[[a*2**k for k,a in enumerate(shift([I(x) for x in poly],term['offset']-1))] for poly in polys] for term in terms]
    segs=[];cross_data=[];cache={}
    for ln,rn,left,right,active in geometry_segments:
        source=[[sum((terms[h]['coefficient']*shifted[h][j][k] for h in active),I(0)) for k in range(64)] for j in range(DIM)];affine=[]
        if replay:
            for poly in source:
                sh=shift(poly,left);powers=[I(1)]
                for _ in range(63):powers.append(powers[-1]*(right-left))
                affine.append([a*s for a,s in zip(sh,powers)])
        segs.append((left,right,source,affine))
        for name,t in [(ln,left),(rn,right)]:
            if name not in cache:cache[name]=primitives((t+1)/2,319,0 if name=='left' else 1 if name=='right' else None)
        moments=[[cache[rn][kind][k]-cache[ln][kind][k] for k in range(320)] for kind in range(3)]
        sy=[[sum((terms[h]['coefficient']*translated[h][j][k] for h in active),I(0)) for k in range(64)] for j in range(DIM)];cross_data.append((moments,sy))
    jobs=[(i,j) for i in range(DIM) for j in range(i,DIM) if (i-j)%2==0];zero={(i,j):(F(0),F(0)) for i in range(DIM) for j in range(i,DIM) if (i-j)%2}
    def accept(name,key,value):
        if saved is None:return value
        old=entries(saved[name])[key];assert old[0]<=value[0]<=value[1]<=old[1],(name,key);return old
    U0={};UP={};HP={}
    for worker,config,out,name in [(base_worker,(forms,mom,replay),U0,'nominal_q_plus_arch_source_Gram_entries'),(prime_worker,(segs,replay),UP,'nominal_prime_source_Gram_entries'),(head_worker,(forms,trials,mom,segs,polys,replay),HP,'nominal_q_plus_arch_plus_prime_trial_pairings')]:
        with ProcessPoolExecutor(max_workers=8,initializer=init_worker,initargs=(config,)) as pool:
            for i,j,value in pool.map(worker,jobs):out[i,j]=accept(name,(i,j),value);print(name,i,j,'checked',file=sys.stderr,flush=True)
        out.update(zero)
    ordered={}
    with ProcessPoolExecutor(max_workers=8,initializer=init_worker,initargs=((forms,cross_data,replay),)) as pool:
        for i,value in pool.map(cross_worker,range(DIM)):ordered[i]=value;print('enriched mixed source row',i,'checked',file=sys.stderr,flush=True)
    cross={}
    for i,j in jobs:cross[i,j]=accept('nominal_symmetrized_q_plus_arch_prime_cross_entries',(i,j),outward(ordered[i][j]+ordered[j][i],10**20))
    cross.update(zero);kp=F(prime['full_paired_prime_physical_operator_norm_upper']);z0=[];zp=[]
    for worker,config,out,name in [(exponential_worker,(forms,mom,U0,replay),z0,'nominal_q_plus_arch_exponential_moments'),(prime_exponential_worker,(segs,T,kp,replay),zp,'nominal_prime_exponential_moments')]:
        with ProcessPoolExecutor(max_workers=8,initializer=init_worker,initargs=(config,)) as pool:
            for j,value in pool.map(worker,range(DIM)):
                if saved is not None:
                    old=tuple(map(F,saved[name][j]));assert old[0]<=value[0]<=value[1]<=old[1],(name,j);value=old
                out.append(value)
    trialmom=[]
    for j in range(DIM):
        if replay:
            ep=[I((B/2)**n/factorial(n)) for n in range(101)];val=integrate_product([I(x) for x in polys[j]],ep,I(-1),I(1),B)
            tail=2*(B/2)**101/factorial(101);radius=I(tail*root(R*T[j][j]));val+=I(-radius.h,radius.h)
        else:val=exact_exponential_integral([I(x) for x in polys[j]],I(-1),I(1))
        value=outward(val,10**20)
        if saved is not None:
            old=tuple(map(F,saved['nominal_trial_exponential_moments'][j]));assert old[0]<=value[0]<=value[1]<=old[1];value=old
        trialmom.append(value)
    moments=[rational_interval(*r) for r in trialmom];s=(I(B).exp()-I(-B).exp())/2;norm=[I(B)+s,s-I(B)]
    U={};PO={};XPO={};H0=[[F(0)]*DIM for _ in range(DIM)];Rh=[[F(0)]*DIM for _ in range(DIM)]
    for i,j in jobs:
        sign=(-1)**i;mi,mj=moments[i],moments[j];o=4*mi*mj*norm[i%2]
        x=2*sign*(mj*rational_interval(*z0[i])+mi*rational_interval(*z0[j])+mj*rational_interval(*zp[i])+mi*rational_interval(*zp[j]))
        PO[i,j]=outward(o,10**20);XPO[i,j]=outward(x,10**20)
        U[i,j]=accept('nominal_complete_original_source_Gram_entries',(i,j),outward(rational_interval(*U0[i,j])+rational_interval(*UP[i,j])+rational_interval(*cross[i,j])+o+x,10**20))
        h=rational_interval(*HP[i,j])+2*sign*mi*mj;a,b=outward(h,10**20)
        H0[i][j]=(a+b)/2;Rh[i][j]=(b-a)/2
        H0[j][i]=H0[i][j]+J[i][j]-J[j][i];Rh[j][i]=Rh[i][j]
    for out in [U,PO,XPO]:out.update(zero)
    center=[[F(0)]*DIM for _ in range(DIM)];allow=[F(0)]*DIM
    for (i,j),(a,b) in U.items():
        center[i][j]=center[j][i]=(a+b)/2;half=(b-a)/2;allow[i]+=half
        if i!=j:allow[j]+=half
    Uup=[[center[i][j]+(i==j)*allow[i] for j in range(DIM)] for i in range(DIM)];assert psd(Uup)
    # Pay every finite pairing-center rounding in its interval radius.
    for i in range(DIM):
        for j in range(DIM):
            v=H0[i][j]*10**24;new=F(round(v),10**24);rr=(Rh[i][j]+abs(H0[i][j]-new))*10**24
            H0[i][j]=new;Rh[i][j]=F(-(-rr.numerator//rr.denominator),10**24)
    Gup=rounded_bound(add(GT,T,F(enriched['actual_recentered_metric_mass_error_upper'])),1,10**24)[0];GI=inverse(Gup)
    L=[[F(round(x*10**24),10**24) for x in row] for row in mm(GI,H0)]
    Z=[[abs(x) for x in row] for row in L];b1=mm(tr(Z),Rh);b2=mm(tr(Rh),Z)
    rounding=[[sum((b1[i][j]+b2[i][j] for j in range(DIM)),F(0))*(i==k) for k in range(DIM)] for i in range(DIM)]
    if replay:
        Lopt=mm(GI,H0);diff=add(L,Lopt,-1);Y=add(add(scale(Uup,RHO),mm(mm(tr(H0),GI),H0),-1),mm(mm(tr(diff),Gup),diff))
    else:
        HL=mm(tr(H0),L);Y=add(add(add(scale(Uup,RHO),HL,-1),tr(HL),-1),mm(mm(tr(L),Gup),L))
    Y=rounded_bound(add(Y,rounding),1,10**24)[0];assert psd(Y)
    # The nominal regular kernel includes degrees 0..191. Pay the
    # omitted degree-192 coefficient in addition to RC46's tail.
    omitted=abs(F(arch['regular_kernel_coefficients'][192]))*R**192
    delta=F(precision['constant_radius'])+F(4,3)*(192+64)*F(42)**193/factorial(193)+R*(F(arch['regular_kernel_uniform_error_upper'])+omitted)
    z=delta*10**30;delta=F(-(-z.numerator//z.denominator),10**30)
    Ep=matrix(enriched['enriched_actual_physical_Riesz_error_Gram_Loewner_upper']);Ec=matrix(enriched['enriched_actual_canonical_Riesz_error_Gram_Loewner_upper']);k=list(map(F,transport['complete_physical_operator_parity_norm_upper']))
    v=F(1,65536);u=F(1,16);ts=[F(2),F(3,2)]
    phys=rounded_bound([[(1+v)*k[i%2]*k[j%2]*Ep[i][j]+(1+1/v)*delta**2*T[i][j] for j in range(DIM)] for i in range(DIM)],1,10**24)[0]
    EL=rounded_bound(mm(mm(tr(L),Ec),L),1,10**24)[0];error=rounded_bound(add(scale(phys,RHO*(1+u)),EL,1+1/u),1,10**24)[0]
    A=rounded_bound([[(1+ts[i%2])*Y[i][j]+(1+1/ts[i%2])*error[i][j] for j in range(DIM)] for i in range(DIM)],1,10**24)[0]
    assert all(psd(x) for x in [phys,EL,error,A])
    Mlo=matrix(enriched['enriched_actual_native_Gram_Loewner_lower']);parity=[]
    for p in range(2):
        lam=relative(block(A,p),block(Mlo,p))
        if replay:
            CI=inverse(block(C,p));assert psd(cong(CI,add(scale(block(Mlo,p),lam),block(A,p),-1)))
        parity.append(dict(parity='even' if p==0 else 'odd',actual_projected_residual_relative_canonical_Gram_upper=str(lam)))
    bound=max(F(r['actual_projected_residual_relative_canonical_Gram_upper']) for r in parity);prior=F(transport['actual_rank_22_projected_source_relative_canonical_native_Gram_upper'])
    return dict(milestone='RC68',status='PASS',input_sha256=hashes,trial_dimension=64,native_features_certified=list(range(DIM)),
        original_source_definition='enriched Fplus_nom=q+K_nom V64; actual canonical source=i_star(q+K_actual iR)',
        nominal_q_plus_arch_source_Gram_entries=rows(U0),nominal_prime_source_Gram_entries=rows(UP),nominal_q_plus_arch_plus_prime_trial_pairings=rows(HP),
        nominal_symmetrized_q_plus_arch_prime_cross_entries=rows(cross),nominal_q_plus_arch_exponential_moments=[list(map(str,r)) for r in z0],nominal_prime_exponential_moments=[list(map(str,r)) for r in zp],nominal_trial_exponential_moments=[list(map(str,r)) for r in trialmom],
        nominal_pole_source_Gram_entries=rows(PO),nominal_symmetrized_all_pole_cross_entries=rows(XPO),nominal_complete_original_source_Gram_entries=rows(U),nominal_complete_original_source_Gram_Loewner_upper=serialize(Uup),
        nominal_original_trial_source_pairing_center=serialize(H0),nominal_original_trial_source_pairing_halfwidths=serialize(Rh),exact_rational_variational_coefficients=serialize(L),
        enriched_nominal_variational_residual_Gram_Loewner_upper=serialize(Y),actual_source_approximation_operator_error_upper=str(delta),enriched_source_transfer_physical_Gram_Loewner_upper=serialize(phys),enriched_canonical_representative_coefficient_error_Gram_Loewner_upper=serialize(EL),enriched_actual_projected_source_residual_Gram_Loewner_upper=serialize(A),
        parity_residual_certificates=parity,enriched_actual_rank_22_projected_source_relative_canonical_native_Gram_upper=str(bound),prior_RC66_projected_source_upper=str(prior),uniform_bound_fractional_reduction=str(1-bound/prior),
        all_signed_enriched_original_source_covariances_evaluated=True,actual_rank_22_projected_source_upper_certified=True,
        exact_actual_projection_coefficients_evaluated=False,required_projected_source_budget_certified=False,actual_projected_source_budget_failure_proved=False,
        uniform_twenty_two_positive_Weil_floor_certified=False,whole_aperture_positivity_extended=False,RH=False,F4=False)
if __name__=='__main__':
    base=Path(__file__).parent.parent/'certificates'
    defaults=[base/n for n in ['rpb108_rc67_sixty_four_riesz_enrichment.json','rpb108_rc59_twenty_two_native_projection.json','rpb108_rc56_precision_attached_head.json','rpb108_rc43_native_prime_head.json','rpb108_rc42_native_signed_pole_head.json','rpb108_rc46_native_archimedean_head.json','rpb108_rc66_arch_multiplier_transport.json']]
    if len(sys.argv)>1 and sys.argv[1]=='--replay':
        saved=json.loads(Path(sys.argv[2]).read_text());assert run(sys.argv[3:] or defaults,True,saved)==saved
        print('PASS: enriched reflected log covariance, affine prime integrals, independent exponential moments, variational square completion and exact canonical parity comparisons')
    else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
