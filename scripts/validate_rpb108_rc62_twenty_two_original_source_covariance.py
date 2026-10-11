"""RC62: complete signed original physical source covariance on 22 trials.

Fplus_nom=q+K_nom V; actual cancellation uses q+K_actual V.
Actual canonical source columns are i*(q+K_actual iR), not these trials.
"""
from fractions import Fraction as F
from pathlib import Path
from math import factorial,comb
from concurrent.futures import ProcessPoolExecutor
import json,sys,hashlib
from validate_rpb108_rc30_interval_metric import I
from validate_rpb108_rc29_atom_reduction import legendre
from validate_rpb108_rc31_trial_riesz import mm,tr,psd
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

def source_forms(native,arch):
    V=matrix(native['native_trial_coefficients']);C=matrix(native['chebyshev_to_legendre'])
    aux,mom,_,_=build_forms(V)
    # Auxiliary forms have Legendre targets; those targets are removed
    # exactly before the actual native q_j is added to the bounded source.
    LP=[transformed(legendre(n)) for n in range(32)]
    H=[sum((F(1,k) for k in range(1,n+1)),F(0)) for n in range(32)]
    reg=list(map(F,arch['regular_kernel_coefficients']))
    weights=[[R*rp*R**p*F(factorial(p)*factorial(m),factorial(p+m+1)) for m in range(32)] for p,rp in enumerate(reg)]
    forms=[];trials=[];targets=[]
    for j in range(DIM):
        v=[sum((V[n][j]*(LP[n][k] if k<=n else 0) for n in range(32)),F(0)) for k in range(32)]
        tv=[sum((H[n]*V[n][j]*(LP[n][k] if k<=n else 0) for n in range(32)),F(0)) for k in range(32)]
        q=[sum((C[n][j]*(LP[n][k] if k<=n else 0) for n in range(DIM)),F(0)) for k in range(DIM)]
        A,L,M=aux[j]
        A=polyadd(A,[I(tv[k]+C0*v[k]-(LP[j][k] if k<=j else 0)) for k in range(32)])
        L=polyadd(L,[I(x/2) for x in v],-1);M=polyadd(M,[I(x/2) for x in v],-1)
        left=[F(0)]*225
        for p in range(len(weights)):
            for m,vm in enumerate(v):left[p+m+1]+=weights[p][m]*vm
        regular=polyadd([I(x) for x in left],reflect([I(x) for x in left]),(-1)**j)
        A=polyadd(polyadd(A,regular,-1),[I(x) for x in q])
        forms.append((A,L,M));trials.append(v);targets.append(q)
        print('original source log form',j,'built',file=sys.stderr,flush=True)
    return forms,mom,trials,targets

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
        for l in range(32):
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

def relative_upper(A,P):
    def accepts(t):return psd([[t*P[i][j]-A[i][j] for j in range(DIM)] for i in range(DIM)])
    lo=F(0);hi=F(1)
    while not accepts(hi):hi*=2
    for _ in range(24):
        mid=(lo+hi)/2
        if accepts(mid):hi=mid
        else:lo=mid
    assert accepts(hi);return hi

def run(paths,replay=False,saved=None):
    raw=[Path(p).read_bytes() for p in paths];metric,native,residual,head,precision,prime,pole,arch=[json.loads(x) for x in raw]
    hashes=[hashlib.sha256(x).hexdigest() for x in raw]
    assert head['input_sha256']==[hashes[k] for k in [0,1,2,4,5,6,7]]
    assert residual['input_sha256']==[hashes[k] for k in [0,4,1]]
    assert precision['input_sha256'][4]==hashes[5] and precision['input_sha256'][5]==hashes[7]
    forms,mom,trials,targets=source_forms(native,arch)
    V=matrix(native['native_trial_coefficients']);T=matrix(native['physical_native_trial_Gram']);P=matrix(native['physical_native_Gram'])
    LP=[legendre(n) for n in range(32)]
    polys=[[sum((V[n][j]*(LP[n][k] if k<=n else 0) for n in range(32)),F(0)) for k in range(32)] for j in range(DIM)]
    terms,geometry_segments=geometry(prime);assert len(geometry_segments)==15
    shifted=[[shift([I(a) for a in poly],term['offset']) for poly in polys] for term in terms]
    translated=[[ [a*2**k for k,a in enumerate(shift([I(x) for x in poly],term['offset']-1))] for poly in polys] for term in terms]
    segs=[];cross_data=[];cache={}
    for ln,rn,left,right,active in geometry_segments:
        source=[[sum((terms[h]['coefficient']*shifted[h][j][k] for h in active),I(0)) for k in range(32)] for j in range(DIM)]
        affine=[]
        if replay:
            for poly in source:
                sh=shift(poly,left);powers=[I(1)]
                for _ in range(31):powers.append(powers[-1]*(right-left))
                affine.append([a*s for a,s in zip(sh,powers)])
        segs.append((left,right,source,affine))
        for name,t in [(ln,left),(rn,right)]:
            if name not in cache:cache[name]=primitives((t+1)/2,255,0 if name=='left' else 1 if name=='right' else None)
        moments=[[cache[rn][kind][k]-cache[ln][kind][k] for k in range(256)] for kind in range(3)]
        sy=[[sum((terms[h]['coefficient']*translated[h][j][k] for h in active),I(0)) for k in range(32)] for j in range(DIM)]
        cross_data.append((moments,sy))
    jobs=[(i,j) for i in range(DIM) for j in range(i,DIM) if (i-j)%2==0]
    zero={(i,j):(F(0),F(0)) for i in range(DIM) for j in range(i,DIM) if (i-j)%2}
    U0={};UP={}
    def accept(name,key,value):
        if saved is None:return value
        old=entries(saved[name])[key];assert old[0]<=value[0]<=value[1]<=old[1],(name,key);return old
    for worker,config,out,name in [(base_worker,(forms,mom,replay),U0,'nominal_q_plus_arch_source_Gram_entries'),(prime_worker,(segs,replay),UP,'nominal_prime_source_Gram_entries')]:
        with ProcessPoolExecutor(max_workers=8,initializer=init_worker,initargs=(config,)) as pool:
            for i,j,value in pool.map(worker,jobs):
                out[i,j]=accept(name,(i,j),value);print(name,i,j,'checked',file=sys.stderr,flush=True)
        out.update(zero)
    ordered={}
    with ProcessPoolExecutor(max_workers=8,initializer=init_worker,initargs=((forms,cross_data,replay),)) as pool:
        for i,value in pool.map(cross_worker,range(DIM)):
            ordered[i]=value;print('mixed original-arch prime row',i,'checked',file=sys.stderr,flush=True)
    cross={}
    for i,j in jobs:cross[i,j]=accept('nominal_symmetrized_q_plus_arch_prime_cross_entries',(i,j),outward(ordered[i][j]+ordered[j][i],10**20))
    cross.update(zero)
    kp=F(prime['full_paired_prime_physical_operator_norm_upper']);z0=[];zp=[]
    for worker,config,out,name in [(exponential_worker,(forms,mom,U0,replay),z0,'nominal_q_plus_arch_exponential_moments'),(prime_exponential_worker,(segs,T,kp,replay),zp,'nominal_prime_exponential_moments')]:
        with ProcessPoolExecutor(max_workers=8,initializer=init_worker,initargs=(config,)) as pool:
            for j,value in pool.map(worker,range(DIM)):
                if saved is not None:
                    old=tuple(map(F,saved[name][j]));assert old[0]<=value[0]<=value[1]<=old[1],(name,j);value=old
                out.append(value);print(name,j,'checked',file=sys.stderr,flush=True)
    moments=[rational_interval(*map(F,r)) for r in head['nominal_trial_pole_moment_enclosures']]
    s=(I(B).exp()-I(-B).exp())/2;norm=[I(B)+s,s-I(B)]
    U={};PO={};XPO={}
    for i,j in jobs:
        sign=(-1)**i;mi,mj=moments[i],moments[j]
        o=4*mi*mj*norm[i%2]
        x=2*sign*(mj*rational_interval(*z0[i])+mi*rational_interval(*z0[j])+mj*rational_interval(*zp[i])+mi*rational_interval(*zp[j]))
        PO[i,j]=outward(o,10**20);XPO[i,j]=outward(x,10**20)
        U[i,j]=outward(rational_interval(*U0[i,j])+rational_interval(*UP[i,j])+rational_interval(*cross[i,j])+o+x,10**20)
        if saved is not None:U[i,j]=accept('nominal_complete_original_source_Gram_entries',(i,j),U[i,j])
    for out in [U,PO,XPO]:out.update(zero)
    center=[[F(0)]*DIM for _ in range(DIM)];allow=[F(0)]*DIM
    for (i,j),(a,b) in U.items():
        center[i][j]=center[j][i]=(a+b)/2;h=(b-a)/2;allow[i]+=h
        if i!=j:allow[j]+=h
    Uup=[[center[i][j]+(i==j)*allow[i] for j in range(DIM)] for i in range(DIM)];assert psd(Uup)
    delta=F(head['corrected_arch_trial_remainder_operator_error_upper'])
    assert delta>=abs(F(precision['constant_center_shift']))+F(precision['constant_radius'])+F(residual['kernel_remainder_upper'])+R*F(arch['regular_kernel_uniform_error_upper'])
    Ep=matrix(residual['actual_physical_Riesz_error_Gram_Loewner_upper']);Ec=matrix(residual['actual_canonical_Riesz_error_Gram_Loewner_upper'])
    assert all(Ep[i][j]==0 for i in range(DIM) for j in range(DIM) if (i-j)%2)
    k=[8+kp+2*F(pole[name]) for name in ['cosh_physical_norm_squared_upper','sinh_physical_norm_squared_upper']]
    u=F(1,32);t=F(1,16)
    Err=[[(1+u)*k[i%2]*k[j%2]*Ep[i][j]+(1+1/u)*delta**2*T[i][j] for j in range(DIM)] for i in range(DIM)]
    S=[[RHO*((1+t)*Uup[i][j]+(1+1/t)*Err[i][j]) for j in range(DIM)] for i in range(DIM)]
    S,sround=rounded_bound(S,1,10**24);assert psd(S)
    relative=relative_upper(S,P)/F(native['actual_canonical_native_Gram_physical_lower_factor'])
    ep=[root(Ep[i][i]) for i in range(DIM)];ec=[root(Ec[i][i]) for i in range(DIM)]
    sn=[root(U[i,i][1])+delta*root(T[i][i]) for i in range(DIM)]
    QT=entries(head['actual_original_trial_Weil_head_entry_enclosures']);oldQ=entries(head['actual_original_Weil_head_entry_enclosures']);Q={};gains=[]
    for i in range(DIM):
        for j in range(i,DIM):
            key=i,j
            if (i-j)%2:Q[key]=(F(0),F(0));continue
            linear=ep[i]*sn[j]+ep[j]*sn[i];quad=k[i%2]*ep[i]*ep[j]
            a,b=QT[key];new=(a-linear-quad-ec[i]*ec[j],b+linear+quad+(ec[i]*ec[j] if i!=j else 0))
            new=intersect(new,oldQ[key]);a,b=new;den=10**24
            aa=a*den;bb=b*den;Q[key]=(F(aa.numerator//aa.denominator,den),F(-(-bb.numerator//bb.denominator),den))
            gains.append((oldQ[key][1]-oldQ[key][0])/(Q[key][1]-Q[key][0]))
    return dict(milestone='RC62',status='PASS',input_sha256=hashes,native_features_certified=list(range(DIM)),trial_dimension=32,
        original_source_definition='Fplus_nom=q+K_nom V; actual canonical source is i_star(q+K_actual iR)',
        physical_source_partition_segments=15,nominal_q_plus_arch_source_Gram_entries=rows(U0),nominal_prime_source_Gram_entries=rows(UP),
        nominal_symmetrized_q_plus_arch_prime_cross_entries=rows(cross),nominal_q_plus_arch_exponential_moments=[list(map(str,r)) for r in z0],
        nominal_prime_exponential_moments=[list(map(str,r)) for r in zp],nominal_pole_source_Gram_entries=rows(PO),
        nominal_symmetrized_all_pole_cross_entries=rows(XPO),nominal_complete_original_source_Gram_entries=rows(U),
        nominal_complete_original_source_Gram_Loewner_upper=serialize(Uup),Gram_rounding_diagonal_allowances=list(map(str,allow)),
        complete_physical_operator_parity_norm_upper=list(map(str,k)),actual_source_approximation_operator_error_upper=str(delta),
        source_error_Young_parameter=str(u),source_transport_Young_parameter=str(t),actual_complete_original_canonical_source_Gram_Loewner_upper=serialize(S),
        actual_complete_original_canonical_source_Gram_relative_actual_native_metric_upper=str(relative),
        actual_source_rounding_diagonal_allowances=list(map(str,sround)),refined_actual_original_Weil_head_entries=rows(Q),
        certified_positive_actual_original_head_diagonal_features=[i for i in range(DIM) if Q[i,i][0]>0],
        minimum_head_entry_width_improvement_factor_lower=str(min(gains)),all_signed_nominal_original_source_covariances_evaluated=True,
        original_source_cancellation_attached_to_actual_head=True,uniform_twenty_two_original_head_floor_certified=False,
        actual_twenty_two_projected_source_residual_evaluated=False,enlarged_projected_source_threshold_certified=False,
        whole_aperture_positivity_extended=False,RH=False,F4=False)

if __name__=='__main__':
    base=Path(__file__).parent.parent/'certificates'
    defaults=[base/n for n in ['rpb108_rc38_thirty_two_metric.json','rpb108_rc59_twenty_two_native_projection.json','rpb108_rc60_twenty_two_mixed_residuals.json','rpb108_rc61_twenty_two_signed_head.json','rpb108_rc56_precision_attached_head.json','rpb108_rc43_native_prime_head.json','rpb108_rc42_native_signed_pole_head.json','rpb108_rc46_native_archimedean_head.json']]
    if len(sys.argv)>1 and sys.argv[1]=='--replay':
        saved=json.loads(Path(sys.argv[2]).read_text());assert run(sys.argv[3:] or defaults,True,saved)==saved
        print('PASS: reflected log covariance, affine prime segments, reflected mixed logs, independent exponential integrations, signed original source assembly, actual transport and head cancellation')
    else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
