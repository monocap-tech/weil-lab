"""Complete prime-prime trial source covariance and actual source transport."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,sys
from math import comb
from validate_rpb108_rc30_interval_metric import I
from validate_rpb108_rc29_atom_reduction import legendre
from validate_rpb108_rc31_trial_riesz import psd
from validate_rpb108_rc42_native_signed_pole_head import outward
from validate_rpb108_rc43_native_prime_head import shift,poly_value
from validate_rpb108_rc47_correlated_native_transport import root,matrix,entries,intersect,serialize,rows

def polynomials(native):
    V=matrix(native['native_trial_coefficients']);out=[]
    for j in range(8):
        p=[F(0)]*32
        for n in range(32):
            for k,a in enumerate(legendre(n)):p[k]+=V[n][j]*a
        out.append(p)
    return out

def geometry(prime):
    B=F(11,10);terms=[];knots=[('left',I(-1)),('right',I(1))]
    for row in prime['active_prime_powers']:
        n=row['n'];p=row['base_prime'];ell=I(n).log()/B;c=I(p).log()/I(n).sqrt()
        for sign in [1,-1]:
            low=I(-1) if sign==1 else -1+ell
            high=1-ell if sign==1 else I(1)
            terms.append(dict(n=n,sign=sign,offset=sign*ell,coefficient=-c,low=low,high=high))
            knots.append((str(n)+('+' if sign==1 else '-'),high if sign==1 else low))
    knots.sort(key=lambda x:x[1].l)
    assert len(knots)==16
    for (_,left),(_,right) in zip(knots,knots[1:]):assert left.h<right.l
    segments=[]
    for (ln,left),(rn,right) in zip(knots,knots[1:]):
        middle=(left+right)/2
        active=[]
        for k,term in enumerate(terms):
            inside=middle.l>term['low'].h and middle.h<term['high'].l
            outside=middle.h<term['low'].l or middle.l>term['high'].h
            assert inside or outside
            if inside:active.append(k)
        segments.append((ln,rn,left,right,active))
    return terms,segments

def integrate_product(p,q,left,right,B):
    product=[I(0)]*(len(p)+len(q)-1)
    for k,a in enumerate(p):
        for l,b in enumerate(q):product[k+l]=product[k+l]+a*b
    primitive=[I(0)]+[a/(k+1) for k,a in enumerate(product)]
    return B*(poly_value(primitive,right)-poly_value(primitive,left))

def assemble(polys,terms,segments,replay=False):
    B=F(11,10);U=[[I(0)]*8 for _ in range(8)];H=[[I(0)]*8 for _ in range(8)]
    shifted=[[shift([I(a) for a in poly],term['offset']) for poly in polys] for term in terms] if not replay else None
    for _,_,left,right,active in segments:
        source=[]
        if replay:
            # Independent integration on u in [0,1], x/B=left+(right-left)u.
            length=right-left
            trial=[]
            for j,poly in enumerate(polys):
                source_j=[I(0)]*32
                for k in active:
                    term=terms[k];offset=left+term['offset'];power=[I(1)]
                    for _ in range(31):power.append(power[-1]*offset)
                    scale=I(1)
                    for m in range(32):
                        a=sum((I(poly[n]*comb(n,m))*power[n-m] for n in range(m,32)),I(0))
                        source_j[m]=source_j[m]+term['coefficient']*a*scale
                        scale=scale*length
                source.append(source_j)
                shifted_trial=shift([I(a) for a in poly],left);scale=I(1);tp=[]
                for a in shifted_trial:tp.append(a*scale);scale=scale*length
                trial.append(tp)
            for i in range(8):
                for j in range(i,8):
                    if (i-j)%2:continue
                    u=B*length*sum((a*b/F(k+l+1) for k,a in enumerate(source[i]) for l,b in enumerate(source[j])),I(0))
                    h=B*length*sum((a*b/F(k+l+1) for k,a in enumerate(trial[i]) for l,b in enumerate(source[j])),I(0))
                    U[i][j]=U[j][i]=U[i][j]+u;H[i][j]=H[j][i]=H[i][j]+h
        else:
            for j in range(8):source.append([sum((terms[k]['coefficient']*shifted[k][j][m] for k in active),I(0)) for m in range(32)])
            for i in range(8):
                for j in range(i,8):
                    if (i-j)%2:continue
                    u=integrate_product(source[i],source[j],left,right,B)
                    h=integrate_product([I(a) for a in polys[i]],source[j],left,right,B)
                    U[i][j]=U[j][i]=U[i][j]+u;H[i][j]=H[j][i]=H[i][j]+h
    return U,H

def run(paths):
    raw=[Path(p).read_bytes() for p in paths];native,prime,transport=[json.loads(x) for x in raw]
    hashes=[hashlib.sha256(x).hexdigest() for x in raw]
    assert prime['native_certificate_sha256']==hashes[0]
    assert transport['input_sha256'][2]==hashes[0] and transport['input_sha256'][4]==hashes[1]
    assert [r['n'] for r in prime['active_prime_powers']]==[2,3,4,5,7,8,9]
    polys=polynomials(native);terms,segments=geometry(prime);U,H=assemble(polys,terms,segments)
    oldtrials=entries(prime['trial_prime_head_entry_enclosures'])
    trialsource={};trialhead={};center=[[F(0)]*8 for _ in range(8)];half=F(0)
    for i in range(8):
        for j in range(i,8):
            key=(i,j)
            if (i-j)%2:lo=hi=F(0);hl=hh=F(0)
            else:
                lo,hi=outward(U[i][j],10**25);hl,hh=outward(H[i][j],10**25)
                assert hi-lo<F(1,10**23)
                assert oldtrials[key][0]<=hl<=hh<=oldtrials[key][1]
            trialsource[key]=(lo,hi);trialhead[key]=(hl,hh)
            center[i][j]=center[j][i]=(lo+hi)/2;half=max(half,(hi-lo)/2)
    P=matrix(native['physical_native_Gram']);assert psd([[P[i][j]-F(1,8)*(i==j) for j in range(8)] for i in range(8)])
    Uup=[[center[i][j]+64*half*P[i][j] for j in range(8)] for i in range(8)]
    assert psd(Uup)
    s=[root(trialsource[(i,i)][1]) for i in range(8)]
    ep=list(map(F,transport['physical_Riesz_error_column_norm_upper']))
    kp=F(prime['full_paired_prime_physical_operator_norm_upper']);rho=F(252,257)
    T=matrix(prime['physical_native_trial_Gram']);assert all(s[i]**2<kp*kp*T[i][i] for i in range(8))
    priorprime=entries(transport['refined_actual_prime_head_entry_enclosures'])
    priorWeil=entries(transport['refined_actual_original_Weil_low_head_entry_enclosures'])
    arch=entries(transport['refined_actual_archimedean_head_entry_enclosures'])
    pole=entries(transport['refined_actual_signed_pole_head_entry_enclosures'])
    actualprime={};actualsource={};actualWeil={};ratios=[]
    for i in range(8):
        for j in range(i,8):
            key=(i,j)
            if (i-j)%2:actualprime[key]=actualsource[key]=actualWeil[key]=(F(0),F(0));continue
            radius=ep[i]*s[j]+ep[j]*s[i]+kp*ep[i]*ep[j]
            a,b=trialhead[key]
            actualprime[key]=intersect((a-radius,b+radius),priorprime[key])
            # This is the actual PHYSICAL prime source Gram, not i^*-lifted covariance.
            rad=kp*(ep[i]*s[j]+ep[j]*s[i])+kp*kp*ep[i]*ep[j]
            a,b=trialsource[key]
            actualsource[key]=(max(F(0),a-rad) if i==j else a-rad,b+rad)
            a,b=actualprime[key]
            actualWeil[key]=intersect((a+arch[key][0]+pole[key][0],b+arch[key][1]+pole[key][1]),priorWeil[key])
            ratios.append((priorprime[key][1]-priorprime[key][0])/(b-a))
    # Whole canonical actual source covariance bound, with every cross-prime
    # trial term included and the physical Riesz error paid as a whole map.
    Berr=matrix(transport['actual_physical_Riesz_error_Gram_Loewner_upper'])
    # An exact scalar bisection checks lambda P-S directly; no eigensolver.
    def relative_upper(A):
        def accepts(q):return psd([[q*P[i][j]-A[i][j] for j in range(8)] for i in range(8)])
        low=F(0);high=F(1)
        while not accepts(high):high*=2
        for _ in range(32):
            mid=(low+high)/2
            if accepts(mid):high=mid
            else:low=mid
        assert accepts(high);return high
    candidates=[]
    for t in [F(1,32),F(1,16),F(1,8),F(1,4),F(1,2),F(1)]:
        A=[[rho*((1+t)*Uup[i][j]+(1+1/t)*kp*kp*Berr[i][j]) for j in range(8)] for i in range(8)]
        candidates.append((relative_upper(A),t,A))
    lam,t,A=min(candidates,key=lambda x:x[0]);alpha=F(native['canonical_native_Gram_physical_lower_factor'])
    refined=lam/alpha;old=F(prime['whole_actual_prime_source_Gram_relative_native_metric_upper'])
    assert refined<old and refined<F(4107,500)
    assert min(ratios)>F(37,20)
    return dict(milestone='RC48',status='PASS',input_sha256=hashes,
        native_features_certified=list(range(8)),source_bound_feature_scope='native features 0 through 7 only',
        active_prime_powers=[2,3,4,5,7,8,9],oriented_source_terms=14,
        physical_source_partition=[dict(left=a,right=b,active_terms=active) for a,b,_,_,active in segments],
        trial_physical_prime_source_Gram_entry_enclosures=rows(trialsource),
        trial_prime_head_entry_enclosures=rows(trialhead),
        trial_physical_prime_source_Gram_Loewner_upper=serialize(Uup),
        trial_prime_source_column_norm_upper=list(map(str,s)),
        actual_physical_prime_source_Gram_entry_enclosures=rows(actualsource),
        actual_native_prime_head_entry_enclosures=rows(actualprime),
        actual_original_Weil_low_head_entry_enclosures=rows(actualWeil),
        actual_canonical_prime_source_Gram_Loewner_upper=serialize(A),
        actual_canonical_prime_source_Gram_relative_physical_native_Gram_upper=str(lam),
        whole_actual_prime_source_Gram_relative_native_metric_upper=str(refined),
        previous_whole_actual_prime_source_Gram_relative_native_metric_upper=str(old),
        source_transport_Young_parameter=str(t),
        minimum_prime_head_width_improvement_factor_lower=str(min(ratios)),
        all_complete_head_diagonal_intervals_contain_zero=all(a<0<b for (i,j),(a,b) in actualWeil.items() if i==j),
        all_prime_prime_trial_source_correlations_evaluated=True,
        exact_actual_canonical_prime_source_Gram_evaluated=False,
        complete_archimedean_prime_pole_covariance_evaluated=False,
        original_Weil_head_floor_certified=False,full_1250_native_projection_constructed=False,aperture_extended=False)

def replay(path,paths):
    cert=json.loads(Path(path).read_text());native,prime,transport=[json.loads(Path(p).read_text()) for p in paths]
    assert cert['input_sha256']==[hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in paths]
    terms,segments=geometry(prime);U,H=assemble(polynomials(native),terms,segments,replay=True)
    for name,A in [('trial_physical_prime_source_Gram_entry_enclosures',U),('trial_prime_head_entry_enclosures',H)]:
        for row in cert[name]:
            i,j=row['i'],row['j'];lo,hi=F(row['lower']),F(row['upper'])
            if (i-j)%2:assert lo==hi==0
            else:assert I(lo).h<=A[i][j].l<=A[i][j].h<=I(hi).l
    # Deterministic rational replay of all source/head transport and PSD checks.
    assert run(paths)==cert
    print('PASS: independent affine-segment integration, all prime-prime trial correlations, actual source/head transport, and exact whole-source Loewner bound')

if __name__=='__main__':
    base=Path(__file__).parent.parent/'certificates'
    defaults=[base/name for name in ['rpb108_rc39_native_low_chebyshev_gram.json',
        'rpb108_rc43_native_prime_head.json','rpb108_rc47_correlated_native_transport.json']]
    if len(sys.argv)>1 and sys.argv[1]=='--replay':replay(sys.argv[2],sys.argv[3:] or defaults)
    else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
