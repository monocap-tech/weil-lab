"""RC61: actual signed original Weil head on 22 native Riesz features.

No enlarged uniform head floor or projected-source threshold is asserted.
Replay changes the prime-overlap, pole-moment and arch-kernel formulas.
"""
from fractions import Fraction as F
from pathlib import Path
from math import comb,factorial
from concurrent.futures import ProcessPoolExecutor
import json,sys,hashlib
from validate_rpb108_rc30_interval_metric import I,endpoint
from validate_rpb108_rc29_atom_reduction import legendre
from validate_rpb108_rc31_trial_riesz import mm,tr,psd
from validate_rpb108_rc35_enriched_residuals import transformed
from validate_rpb108_rc42_native_signed_pole_head import outward,rational_interval
from validate_rpb108_rc43_native_prime_head import pairing
from validate_rpb108_rc46_native_archimedean_head import regular_coefficients
from validate_rpb108_rc47_correlated_native_transport import matrix,serialize,entries,rows,root,intersect,product
from validate_rpb108_rc56_precision_attached_head import C0,DC0

DIM=22;B=F(11,10);R=2*B;DEG=192

def init_worker(config):
    global WORK
    WORK=config

def arch_worker(ij):
    i,j=ij;polys,left,weighted,weights,W,H,T,V,replay=WORK
    if replay:
        # Direct triangle beta moments, without the convolved polynomial.
        kernel=2*R*R*sum((weights[p][m]*vm*weighted[i][p+m+1]
            for p in range(len(weights)) for m,vm in enumerate(polys[j]) if vm),F(0))
        end=W[i][j]
    else:
        kernel=2*R*sum((a*w for a,w in zip(left[j],weighted[i])),F(0))
        end=R*sum((a*b*(F(1,2*(k+l+1)**2)+H[k+l+1]/(2*(k+l+1)))
            for k,a in enumerate(polys[i]) for l,b in enumerate(polys[j])),F(0))
    harmonic=sum((H[n]*R/F(2*n+1)*V[n][i]*V[n][j] for n in range(32)),F(0))
    return i,j,outward(I(end+harmonic+C0*T[i][j]-kernel),10**20)

def exact_shift(p,x):
    return [sum((p[j]*comb(j,k)*x**(j-k) for j in range(k,len(p))),F(0)) for k in range(len(p))]

def prime_worker(ij):
    i,j=ij;polys,V,prime,replay=WORK;value=I(0)
    for row in prime['active_prime_powers']:
        n=row['n'];p=row['base_prime'];ell=I(n).log();c=I(p).log()/I(n).sqrt()
        if not replay:
            value=value-c*(pairing([I(x) for x in polys[i]],[I(x) for x in polys[j]],ell,B)+pairing([I(x) for x in polys[j]],[I(x) for x in polys[i]],ell,B))
        else:
            el,eh=F(row['translation_lower']),F(row['translation_upper']);cl,ch=F(row['coefficient_lower']),F(row['coefficient_upper'])
            assert I(el).l<=ell.l<=ell.h<=I(eh).h and I(cl).l<=c.l<=c.h<=I(ch).h
            e=(el+eh)/2;cm=(cl+ch)/2;length=2-e/B
            left=[exact_shift(polys[z],F(-1)) for z in [i,j]]
            right=[exact_shift(polys[z],-1+e/B) for z in [i,j]]
            moments=[B*length**(k+1)/F(k+1) for k in range(63)]
            integral=sum((a*b*moments[k+l] for u,v in [(0,1),(1,0)] for k,a in enumerate(left[u]) for l,b in enumerate(right[v])),F(0))
            A=[sum((abs(V[n][z]) for n in range(32)),F(0)) for z in [i,j]]
            D=[sum((abs(V[n][z])*F(n*(n+1),2) for n in range(32)),F(0)) for z in [i,j]]
            lip=2*A[0]*A[1]+2*(A[0]*D[1]+A[1]*D[0])
            error=(ch-cl)/2*2*R*A[0]*A[1]+ch*(eh-el)/2*lip
            value=value+I(-cm*integral)+rational_interval(-error,error)
    return i,j,outward(value,10**20)

def pole_moments(V,replay):
    integrals=[];tail=2*(B/2)**81/factorial(81)
    for n in range(32):
        if replay:
            def term(l):return F(2**(n+1)*factorial(l+n),factorial(l)*factorial(2*l+2*n+1))*(B/2)**(n+2*l)
            a=B*sum((term(l) for l in range(41)),F(0));b=a+2*B*term(41)
            assert (B/2)**2/F(2*42*(2*41+2*n+3))<F(1,2)
            integrals.append((a,b))
        else:
            a=sum((B*x*(B/2)**k*F(2,m+k+1)/factorial(k) for m,x in enumerate(legendre(n)) for k in range(81) if (m+k)%2==0),F(0))
            integrals.append((a-2*B*tail,a+2*B*tail))
    out=[]
    for j in range(DIM):
        a=b=F(0)
        for n in range(32):
            lo,hi=integrals[n];c=V[n][j];a+=c*(lo if c>=0 else hi);b+=c*(hi if c>=0 else lo)
        out.append(outward(rational_interval(a,b),10**20))
    return out

def run(paths,replay=False,saved=None):
    raw=[Path(p).read_bytes() for p in paths]
    metric,native,residual,precision,prime,pole,arch=[json.loads(x) for x in raw]
    hashes=[hashlib.sha256(x).hexdigest() for x in raw]
    assert residual['input_sha256']==[hashes[k] for k in [0,3,1]]
    assert native['input_sha256'][0]==hashes[0] and native['input_sha256'][2]==hashes[3]
    assert precision['input_sha256'][4]==hashes[4] and precision['input_sha256'][5]==hashes[6]
    assert arch['pole_certificate_sha256']==hashes[5] and arch['prime_certificate_sha256']==hashes[4]
    V=matrix(native['native_trial_coefficients']);C=matrix(native['chebyshev_to_legendre']);G=matrix(metric['metric_center'])
    T=matrix(native['physical_native_trial_Gram']);P=matrix(native['physical_native_Gram']);GT=mm(mm(tr(V),G),V)
    masses=list(map(F,metric['physical_mass']))
    assert T==mm(mm(tr(V),[[masses[i]*(i==j) for j in range(32)] for i in range(32)]),V)
    J=mm(tr([[masses[i]*C[i][j] if i<DIM else F(0) for j in range(DIM)] for i in range(32)]),V)
    H=[sum((F(1,k) for k in range(1,n+1)),F(0)) for n in range(260)]
    reg=regular_coefficients(DEG)
    if replay:
        a=[]
        for n in range(DEG+2):a.append(F(1,2)*F(-1,2)**n/factorial(n)-sum((a[n-k]*F(-2)**k/factorial(k+1) for k in range(1,n+1)),F(0)))
        assert a[1:]==reg
    assert list(map(F,arch['regular_kernel_coefficients']))==reg
    tail=F(375,4)*F(11,15)**193;assert tail==F(arch['regular_kernel_uniform_error_upper'])
    polys=[];xp=[];LP=[legendre(n) for n in range(32)];YP=[transformed(p) for p in LP]
    for j in range(DIM):
        polys.append([sum((V[n][j]*(LP[n][k] if k<=n else 0) for n in range(32)),F(0)) for k in range(32)])
        xp.append([sum((V[n][j]*(YP[n][k] if k<=n else 0) for n in range(32)),F(0)) for k in range(32)])
    weights=[[rp*R**p*F(factorial(p)*factorial(m),factorial(p+m+1)) for m in range(32)] for p,rp in enumerate(reg)]
    left=[]
    for poly in xp:
        row=[F(0)]*226
        if not replay:
            for p in range(len(weights)):
                for m,vm in enumerate(poly):row[p+m+1]+=R*weights[p][m]*vm
        left.append(row)
    weighted=[[sum((x/F(k+d+1) for k,x in enumerate(poly)),F(0)) for d in range(226)] for poly in xp]
    W=mm(mm(tr(V),[[endpoint(i,j) if (i-j)%2==0 else F(0) for j in range(32)] for i in range(32)]),V) if replay else None
    jobs=[(i,j) for i in range(DIM) for j in range(i,DIM) if (i-j)%2==0]
    AH={};PH={};zero={(i,j):(F(0),F(0)) for i in range(DIM) for j in range(i,DIM) if (i-j)%2}
    for func,config,out,label in [(arch_worker,(xp,left,weighted,weights,W,H,T,V,replay),AH,'arch'),(prime_worker,(polys,V,prime,replay),PH,'prime')]:
        with ProcessPoolExecutor(max_workers=8,initializer=init_worker,initargs=(config,)) as pool:
            for i,j,value in pool.map(func,jobs):
                if saved is not None:
                    prior=entries(saved['nominal_'+label+'_trial_head_entry_enclosures'])[i,j]
                    assert prior[0]<=value[0]<=value[1]<=prior[1],(label,i,j)
                    value=prior
                out[i,j]=value
                print(label,i,j,'attached',file=sys.stderr,flush=True)
        out.update(zero)
    moments=pole_moments(V,replay)
    if saved is not None:
        prior=[tuple(map(F,r)) for r in saved['nominal_trial_pole_moment_enclosures']]
        assert all(a<=c<=d<=b for (a,b),(c,d) in zip(prior,moments));moments=prior
    norms=[F(pole['cosh_physical_norm_squared_upper']),F(pole['sinh_physical_norm_squared_upper'])]
    s=(I(B).exp()-I(-B).exp())/2
    assert I(norms[0]).l>=(I(B)+s).h and I(norms[1]).l>=(s-I(B)).h
    kp=F(prime['full_paired_prime_physical_operator_norm_upper']);total=F(0)
    assert [r['n'] for r in prime['active_prime_powers']]==[2,3,4,5,7,8,9]
    assert 9<I(R).exp().l and I(R).exp().h<10
    for r in prime['active_prime_powers']:
        m=r['maximum_chain_nodes']-1;ell=I(r['n']).log();assert (m*ell).h<I(R).l and ((m+1)*ell).l>I(R).h
        adj=F(r['paired_translation_norm_upper']);assert psd([[adj*(i==j)-F(abs(i-j)==1) for j in range(m+1)] for i in range(m+1)])
        total+=F(r['coefficient_upper'])*adj
    assert total==kp
    Ep=matrix(residual['actual_physical_Riesz_error_Gram_Loewner_upper']);Ec=matrix(residual['actual_canonical_Riesz_error_Gram_Loewner_upper'])
    ep=[root(Ep[i][i]) for i in range(DIM)];ec=[root(Ec[i][i]) for i in range(DIM)];v=[root(T[i][i]) for i in range(DIM)]
    actualmom=[(a-ep[j]*root(norms[j%2]),b+ep[j]*root(norms[j%2])) for j,(a,b) in enumerate(moments)]
    assert actualmom[0][0]>0 and actualmom[1][0]>0
    deltaG=F(native['actual_metric_error_upper_used']);shift=F(precision['constant_center_shift']);dc=F(precision['constant_radius'])
    epsG=F(metric['mass_metric_error_upper'])-2*DC0;assert epsG>0
    deltaS=abs(shift)+dc+epsG+R*tail
    M0=entries(native['actual_native_Gram_entry_enclosures']);M8=entries(precision['refined_actual_native_Gram_entry_enclosures']);Q8=entries(precision['actual_original_Weil_low_head_entry_enclosures'])
    MM={};AA={};PP={};OO={};QQ={};QT={}
    for i in range(DIM):
        for j in range(i,DIM):
            key=i,j
            if (i-j)%2:
                for out in [MM,AA,PP,OO,QQ,QT]:out[key]=(F(0),F(0))
                continue
            c=J[i][j]+J[j][i]-GT[i][j];mr=deltaG*root(T[i][i]*T[j][j])
            m=(c-mr,c+mr+Ec[i][i]) if i==j else (c-mr-ec[i]*ec[j],c+mr+ec[i]*ec[j])
            MM[key]=intersect(m,M0[key])
            if j<8:MM[key]=intersect(MM[key],M8[key])
            transfer=ep[i]*v[j]+ep[j]*v[i]+ep[i]*ep[j]
            ar=deltaS*root(T[i][i]*T[j][j])+8*transfer
            AA[key]=(MM[key][0]+AH[key][0]-GT[i][j]-ar,MM[key][1]+AH[key][1]-GT[i][j]+ar)
            PP[key]=(PH[key][0]-kp*transfer,PH[key][1]+kp*transfer)
            def pole_entry(ms):
                if i==j:
                    a,b=ms[i];lo=F(0) if a<=0<=b else min(a*a,b*b);hi=max(a*a,b*b)
                    return (2*lo,2*hi) if i%2==0 else (-2*hi,-2*lo)
                a,b=product(ms[i],ms[j]);return (2*a,2*b) if i%2==0 else (-2*b,-2*a)
            OO[key]=pole_entry(actualmom);po=pole_entry(moments)
            qt=(AH[key][0]+PH[key][0]+po[0]+shift*T[i][j],AH[key][1]+PH[key][1]+po[1]+shift*T[i][j])
            rad=(dc+epsG+R*tail)*root(T[i][i]*T[j][j]);QT[key]=(qt[0]-rad,qt[1]+rad)
            QQ[key]=(sum(out[key][0] for out in [AA,PP,OO]),sum(out[key][1] for out in [AA,PP,OO]))
            if j<8:QQ[key]=intersect(QQ[key],Q8[key])
    # Compact rational endpoints; pay this final serialization rounding
    # explicitly rather than retain kernel factorial denominators in rows.
    den=10**24
    for out in [MM,AA,PP,OO,QQ,QT]:
        for key,(a,b) in out.items():
            lo=a*den;hi=b*den
            out[key]=(F(lo.numerator//lo.denominator,den),F(-(-hi.numerator//hi.denominator),den))
    positive=[i for i in range(DIM) if QQ[i,i][0]>0]
    return dict(milestone='RC61',status='PASS',input_sha256=hashes,native_features_certified=list(range(DIM)),trial_dimension=32,
        nominal_arch_trial_head_entry_enclosures=rows(AH),nominal_prime_trial_head_entry_enclosures=rows(PH),
        nominal_trial_pole_moment_enclosures=[list(map(str,r)) for r in moments],actual_pole_moment_enclosures=[list(map(str,r)) for r in actualmom],
        corrected_arch_trial_remainder_operator_error_upper=str(deltaS),physical_prime_operator_norm_upper=str(kp),
        refined_actual_native_Gram_entry_enclosures=rows(MM),actual_archimedean_head_entry_enclosures=rows(AA),
        actual_prime_head_entry_enclosures=rows(PP),actual_signed_pole_head_entry_enclosures=rows(OO),
        actual_original_Weil_head_entry_enclosures=rows(QQ),actual_original_trial_Weil_head_entry_enclosures=rows(QT),
        certified_positive_actual_original_head_diagonal_features=positive,actual_signed_pole_head_rank=2,actual_signed_pole_head_inertia=[1,1,20],
        all_253_actual_original_head_entries_enclosed=True,retained_low_eight_enclosures_intersected=True,
        uniform_twenty_two_original_head_floor_certified=False,complete_twenty_two_source_covariance_evaluated=False,
        enlarged_projected_source_threshold_certified=False,whole_aperture_positivity_extended=False,RH=False,F4=False)

if __name__=='__main__':
    base=Path(__file__).parent.parent/'certificates'
    defaults=[base/n for n in ['rpb108_rc38_thirty_two_metric.json','rpb108_rc59_twenty_two_native_projection.json','rpb108_rc60_twenty_two_mixed_residuals.json','rpb108_rc56_precision_attached_head.json','rpb108_rc43_native_prime_head.json','rpb108_rc42_native_signed_pole_head.json','rpb108_rc46_native_archimedean_head.json']]
    if len(sys.argv)>1 and sys.argv[1]=='--replay':
        saved=json.loads(Path(sys.argv[2]).read_text());assert run(sys.argv[3:] or defaults,True,saved)==saved
        print('PASS: alternate arch division, direct triangle moments and Legendre endpoints, rational translated prime overlaps, positive Rodrigues pole moments, all 253 actual signed-head entries')
    else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
