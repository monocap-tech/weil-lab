"""RC60 exact mixed physical residual Gram for all 22 RC59 trials.

The additive generalized RC38 builder keeps Legendre targets until the
final exact Chebyshev congruence. Replay uses reflection-reduced moments.
"""
from fractions import Fraction as F
from pathlib import Path
from math import factorial
import json,sys,hashlib
from concurrent.futures import ProcessPoolExecutor
from validate_rpb108_rc35_enriched_residuals import I,PI,loctx,hictx,N,transformed,reflect,polyadd,scalar,integrate
from validate_rpb108_rc29_atom_reduction import legendre
from validate_rpb108_rc31_trial_riesz import mm,tr,inverse,psd
from validate_rpb108_rc47_correlated_native_transport import matrix,serialize,rows,root
from validate_rpb108_rc59_twenty_two_native_projection import nearest
from validate_rpb108_rc57_uniform_low_head_floor import rounded_bound

def build_forms(V):
    ntrial=len(V); ntarget=len(V[0]);assert (ntrial,ntarget)==(32,22)
    assert all(V[i][j]==0 for i in range(ntrial) for j in range(ntarget) if (i-j)%2)
    H=[sum((F(1,k) for k in range(1,n+1)),F(0)) for n in range(2*(N+ntrial+1)+1)]
    H2=[sum((F(1,k*k) for k in range(1,n+1)),F(0)) for n in range(len(H))]
    cmid=F(-3203794213-3203306050,2*10**9)
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

def pairing(f,g,m,R,replay):
    A,B,C=f;X,Y,Z=g
    if replay:
        # Same parity gives reflection partners equal; six terms combine.
        return I(R)*(integrate(A,X,m[0])+2*integrate(A,Y,m[1])+2*integrate(B,X,m[1])+2*integrate(B,Y,m[3])+2*integrate(B,Z,m[5]))
    return I(R)*(integrate(A,X,m[0])+integrate(A,Y,m[1])+integrate(B,X,m[1])+integrate(A,Z,m[2])+integrate(C,X,m[2])+integrate(B,Y,m[3])+integrate(C,Z,m[4])+integrate(B,Z,m[5])+integrate(C,Y,m[5]))

def init_worker(forms,mom,R,replay):
    global WORK
    WORK=(forms,mom,R,replay)

def gram_worker(ij):
    i,j=ij;forms,mom,R,replay=WORK
    return i,j,pairing(forms[i],forms[j],mom,R,replay)

def run(paths,replay=False,saved=None):
    raw=[Path(p).read_bytes() for p in paths];metric,precision,previous=[json.loads(x) for x in raw]
    hashes=[hashlib.sha256(x).hexdigest() for x in raw]
    assert previous['input_sha256'][0]==hashes[0] and previous['input_sha256'][2]==hashes[1]
    G=matrix(metric['metric_center']);mass=list(map(F,metric['physical_mass']));C=matrix(previous['chebyshev_to_legendre'])
    GI=inverse(G);rhs=[[mass[i]*(i==j) for j in range(22)] for i in range(32)]
    V=[[nearest(x,10**30) for x in row] for row in mm(GI,rhs)]
    assert mm(V,C)==matrix(previous['native_trial_coefficients'])
    assert [r[:8] for r in V]==matrix(metric['coefficients'])
    forms,mom,R,eps=build_forms(V);Q=[[F(0)]*22 for _ in range(22)];E={};allow=[F(0)]*22
    old_entries={} if saved is None else {(e['i'],e['j']):(F(e['lower']),F(e['upper'])) for e in saved['nominal_Legendre_residual_Gram_entry_enclosures']}
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
                low,high=old_entries[i,j];assert I(low).l<=value.l<=value.h<=I(high).h
            E[i,j]=(low,high);Q[i][j]=Q[j][i]=(low+high)/2
            half=(high-low)/2;allow[i]+=half
            if i!=j:allow[j]+=half
            print('Gram',i,j,'enclosed',file=sys.stderr,flush=True)
    Qu=[[Q[i][j]+(i==j)*allow[i] for j in range(22)] for i in range(22)]
    Qn=mm(mm(tr(C),Qu),C);assert psd(Qu) and psd(Qn)
    T=matrix(previous['physical_native_trial_Gram']);rho=F(252,257)
    delta=2*(abs(F(precision['constant_center_shift']))+F(precision['constant_radius']))+eps
    # Young on (nominal residual)+(actual constant/series correction).
    t=F(1,1024)
    B=[[(1+t)*Qn[i][j]+(1+1/t)*delta**2*T[i][j] for j in range(22)] for i in range(22)]
    B,br=rounded_bound(B,1,10**24)
    Ec=[[rho*x for x in row] for row in B];Ep=[[rho*x for x in row] for row in Ec]
    oldEc=matrix(previous['actual_canonical_Riesz_error_Gram_Loewner_upper'])
    # Whole-matrix improvement, proved by exact rational LDL.
    assert psd([[oldEc[i][j]-Ec[i][j] for j in range(22)] for i in range(22)])
    Vn=mm(V,C);D=[[mass[i]*(i==j) for j in range(32)] for i in range(32)]
    GT=mm(mm(tr(Vn),G),Vn);X=mm(tr([[mass[i]*C[i][j] if i<22 else F(0) for j in range(22)] for i in range(32)]),Vn)
    dm=F(previous['actual_metric_error_upper_used'])
    # M=J+J*-GTactual+Ecanonical; retain RC59 lower bound.
    newup=[[X[i][j]+X[j][i]-GT[i][j]+dm*T[i][j]+Ec[i][j] for j in range(22)] for i in range(22)]
    Mlo=matrix(previous['actual_canonical_native_Gram_Loewner_lower'])
    assert psd([[newup[i][j]-Mlo[i][j] for j in range(22)] for i in range(22)])
    result=dict(milestone='RC60',status='PASS',input_sha256=hashes,trial_dimension=32,target_dimension=22,
        kernel_degree=N,kernel_remainder_upper=str(eps),nominal_Legendre_residual_Gram_center=serialize(Q),
        nominal_Legendre_residual_Gram_entry_enclosures=rows(E),nominal_rounding_diagonal_allowances=list(map(str,allow)),
        nominal_native_physical_residual_Gram_Loewner_upper=serialize(Qn),corrected_residual_operator_error_upper=str(delta),
        Young_parameter=str(t),actual_physical_operator_residual_Gram_Loewner_upper=serialize(B),
        actual_canonical_Riesz_error_Gram_Loewner_upper=serialize(Ec),actual_physical_Riesz_error_Gram_Loewner_upper=serialize(Ep),
        transport_rounding_diagonal_allowances=list(map(str,br)),refined_actual_native_Gram_Loewner_upper=serialize(newup),
        whole_matrix_Riesz_error_improves_RC59=True,original_eight_trial_columns_preserved_exactly=True,
        enlarged_original_Weil_head_floor_certified=False,enlarged_projected_source_threshold_certified=False,
        whole_aperture_positivity_extended=False,RH=False,F4=False)
    if saved is not None:assert result==saved
    return result

if __name__=='__main__':
    base=Path(__file__).parent.parent/'certificates'
    defaults=[base/n for n in ['rpb108_rc38_thirty_two_metric.json','rpb108_rc56_precision_attached_head.json','rpb108_rc59_twenty_two_native_projection.json']]
    if len(sys.argv)>1 and sys.argv[1]=='--replay':
        run(sys.argv[3:] or defaults,True,json.loads(Path(sys.argv[2]).read_text()))
        print('PASS: reflection-reduced log moments, exact 22-feature congruence, corrected Riesz error transport and whole-matrix RC59 improvement')
    else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
