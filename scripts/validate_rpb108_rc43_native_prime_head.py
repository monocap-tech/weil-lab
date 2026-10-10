"""Seven active prime powers: actual native low-eight head enclosures."""
from validate_rpb108_rc30_interval_metric import I,hictx,loctx
from validate_rpb108_rc29_atom_reduction import legendre
from validate_rpb108_rc31_trial_riesz import mm,tr,psd
from validate_rpb108_rc42_native_signed_pole_head import outward,rational_interval
from fractions import Fraction as F
from pathlib import Path
from math import comb
import hashlib,json,sys

def poly_value(p,x):
    value=I(0)
    for a in reversed(p): value=value*x+a
    return value

def shift(p,x):
    powers=[I(1)]
    for _ in range(len(p)-1): powers.append(powers[-1]*x)
    return [sum((p[j]*comb(j,k)*powers[j-k] for j in range(k,len(p))),I(0))
            for k in range(len(p))]

def pairing(p,q,ell,B):
    # x=B t, t in [-1,1-ell/B] for the positive translation.
    shifted=shift(q,ell/I(B)); product=[I(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(shifted): product[i+j]=product[i+j]+a*b
    primitive=[I(0)]+[a/(j+1) for j,a in enumerate(product)]
    return I(B)*(poly_value(primitive,1-ell/I(B))-poly_value(primitive,I(-1)))

def run(native_path,residual_path):
    raw=Path(native_path).read_bytes(); data=json.loads(raw)
    residual_raw=Path(residual_path).read_bytes(); residual=json.loads(residual_raw)
    assert data['metric_certificate_sha256']==residual['metric_certificate_sha256']
    assert data['actual_low_native_Gram_certified']
    V=[[F(x) for x in row] for row in data['native_trial_coefficients']]
    C=[[F(x) for x in row] for row in data['chebyshev_to_legendre']]
    P=[[F(x) for x in row] for row in data['physical_native_Gram']]
    TL=[[F(x) for x in row] for row in residual['trial_physical_Gram']]
    T=mm(mm(tr(C),TL),C)
    beta=F(data['canonical_trial_error_physical_squared_upper'])
    rho=F(data['canonical_native_Gram_physical_upper_factor'])
    tv=F(residual['trial_map_squared_upper'])
    assert psd([[tv*P[i][j]-T[i][j] for j in range(8)] for i in range(8)])
    B=F(11,10); R=2*B
    exponential=I(R).exp(); assert exponential.l>9 and exponential.h<10
    polynomials=[]
    for j in range(8):
        p=[F(0)]*32
        for n in range(32):
            for k,a in enumerate(legendre(n)): p[k]+=V[n][j]*a
        polynomials.append([I(x) for x in p])
    H=[[I(0)]*8 for _ in range(8)]
    prime_rows=[]; operator_upper=F(0)
    for n,p,m in [(2,2,3),(3,3,2),(4,2,1),(5,5,1),(7,7,1),(8,2,1),(9,3,1)]:
        ell=I(n).log(); coefficient=I(p).log()/I(n).sqrt()
        assert (m*ell).h<I(R).l and ((m+1)*ell).l>I(R).h
        # Fibers of x modulo ell are path chains of at most m+1 nodes.
        adjacency=(1+I(5).sqrt())/2 if m==3 else I(2).sqrt() if m==2 else I(1)
        adjacency_upper=outward(adjacency)[1]
        matrix=[[adjacency_upper*(i==j)-F(abs(i-j)==1) for j in range(m+1)] for i in range(m+1)]
        assert psd(matrix)
        c_lo,c_hi=outward(coefficient,10**40); e_lo,e_hi=outward(ell,10**40)
        operator_upper+=c_hi*adjacency_upper
        local=[]
        for i in range(8):
            for j in range(i,8):
                if (i-j)%2: continue
                value=-coefficient*(pairing(polynomials[i],polynomials[j],ell,B)+
                                    pairing(polynomials[j],polynomials[i],ell,B))
                lo,hi=outward(value,10**20)
                assert hi-lo<F(1,10**18)
                H[i][j]=H[j][i]=H[i][j]+rational_interval(lo,hi)
                local.append(dict(i=i,j=j,lower=str(lo),upper=str(hi)))
        prime_rows.append(dict(n=n,base_prime=p,translation_lower=str(e_lo),translation_upper=str(e_hi),
            coefficient_lower=str(c_lo),coefficient_upper=str(c_hi),
            maximum_chain_nodes=m+1,paired_translation_norm_upper=str(adjacency_upper),
            trial_head_entry_enclosures=local))
        print('prime power',n,'paired translations enclosed',file=sys.stderr,flush=True)
    canonical_upper=rho*operator_upper
    e=[(I(rho*beta*P[i][i])).sqrt() for i in range(8)]
    v=[I(T[i][i]).sqrt() for i in range(8)]
    entries=[]; trials=[]
    for i in range(8):
        for j in range(i,8):
            tl,tu=outward(H[i][j],10**20)
            trials.append(dict(i=i,j=j,lower=str(tl),upper=str(tu)))
            if (i-j)%2:
                entries.append(dict(i=i,j=j,lower='0',upper='0',reason='exact parity'))
            else:
                radius=I(operator_upper)*(e[i]*v[j]+e[j]*v[i]+e[i]*e[j])
                lo,hi=outward(H[i][j]+I(radius.h.copy_negate(),radius.h))
                entries.append(dict(i=i,j=j,lower=str(lo),upper=str(hi)))
    normalized=I(operator_upper)*(2*I(rho*beta*tv).sqrt()+I(rho*beta))
    center=[[F(0)]*8 for _ in range(8)]
    half=F(0)
    for row in trials:
        i,j=row['i'],row['j'];lo,hi=F(row['lower']),F(row['upper'])
        center[i][j]=center[j][i]=(lo+hi)/2
        half=max(half,(hi-lo)/2)
    # 8h I <=64h P by the checked Euclidean lower bound for P.
    assert psd([[P[i][j]-F(1,8)*(i==j) for j in range(8)] for i in range(8)])
    center_rounding_error=64*half
    error_upper=outward(normalized)[1]+center_rounding_error
    assert entries[0]['i']==entries[0]['j']==0 and F(entries[0]['upper'])<0
    assert F(next(row['lower'] for row in entries if row['i']==row['j']==1))>0
    return dict(milestone='RC43',status='PASS',
        native_certificate_sha256=hashlib.sha256(raw).hexdigest(),
        residual_certificate_sha256=hashlib.sha256(residual_raw).hexdigest(),
        original_form_source_blob='e9a44661f94ee6750fc5ad1fbf7dc719fa3ba482',
        native_features_certified=list(range(8)),active_prime_powers=prime_rows,
        complete_active_prime_set_certified=True,
        physical_native_Gram=[[str(x) for x in row] for row in P],
        physical_native_trial_Gram=[[str(x) for x in row] for row in T],
        full_paired_prime_physical_operator_norm_upper=str(operator_upper),
        full_paired_prime_canonical_operator_norm_upper=str(canonical_upper),
        whole_actual_prime_source_Gram_relative_native_metric_upper=str(canonical_upper**2),
        trial_prime_head_entry_enclosures=trials,
        trial_prime_head_rational_center=[[str(x) for x in row] for row in center],
        trial_center_physical_metric_rounding_error_upper=str(center_rounding_error),
        actual_native_prime_head_entry_enclosures=entries,
        actual_prime_head_trial_center_physical_metric_error_upper=str(error_upper),
        actual_low_native_prime_head_enclosed=True,
        actual_low_native_prime_head_indefinite_certified=True,
        exact_actual_prime_source_Gram_evaluated=False,
        full_native_remainder_sources_certified=False,
        original_Weil_head_floor_certified=False,aperture_extended=False)

def replay(certificate_path,native_path,residual_path):
    native_raw=Path(native_path).read_bytes(); residual_raw=Path(residual_path).read_bytes()
    native=json.loads(native_raw); residual=json.loads(residual_raw)
    cert=json.loads(Path(certificate_path).read_text())
    assert cert['native_certificate_sha256']==hashlib.sha256(native_raw).hexdigest()
    assert cert['residual_certificate_sha256']==hashlib.sha256(residual_raw).hexdigest()
    V=[[F(x) for x in row] for row in native['native_trial_coefficients']]
    B=F(11,10); R=2*B
    polys=[]
    for j in range(8):
        row=[F(0)]*32
        for n in range(32):
            for k,a in enumerate(legendre(n)): row[k]+=V[n][j]*a
        polys.append(row)
    def exact_shift(p,x):
        return [sum((p[j]*comb(j,k)*x**(j-k) for j in range(k,len(p))),F(0)) for k in range(len(p))]
    left=[exact_shift(p,F(-1)) for p in polys]
    A=[sum((abs(V[n][j]) for n in range(32)),F(0)) for j in range(8)]
    D=[sum((abs(V[n][j])*F(n*(n+1),2) for n in range(32)),F(0)) for j in range(8)]
    total_lower=[[F(0)]*8 for _ in range(8)]; total_upper=[[F(0)]*8 for _ in range(8)]
    norm=F(0)
    assert [r['n'] for r in cert['active_prime_powers']]==[2,3,4,5,7,8,9]
    assert I(R).exp().l>9 and I(R).exp().h<10
    for row in cert['active_prime_powers']:
        n=row['n'];p=row['base_prime'];m=row['maximum_chain_nodes']-1
        assert p in [2,3,5,7]
        assert n in [p**k for k in range(1,4)]
        el,eh=F(row['translation_lower']),F(row['translation_upper'])
        cl,ch=F(row['coefficient_lower']),F(row['coefficient_upper'])
        logarithm=I(n).log();coefficient=I(p).log()/I(n).sqrt()
        assert I(el).l<=logarithm.l<=logarithm.h<=I(eh).h
        assert I(cl).l<=coefficient.l<=coefficient.h<=I(ch).h
        assert m*eh<R<(m+1)*el
        adjacency=F(row['paired_translation_norm_upper'])
        assert psd([[adjacency*(i==j)-F(abs(i-j)==1) for j in range(m+1)] for i in range(m+1)])
        norm+=ch*adjacency
        ell=(el+eh)/2;c=(cl+ch)/2;length=2-ell/B
        right=[exact_shift(poly,-1+ell/B) for poly in polys]
        moments=[B*length**(k+1)/F(k+1) for k in range(63)]
        def integral(i,j):
            return sum((a*b*moments[k+l] for k,a in enumerate(left[i])
                        for l,b in enumerate(right[j])),F(0))
        assert integral(0,1)+integral(1,0)==0
        assert B*length==R-ell  # one constant-function translated overlap
        for entry in row['trial_head_entry_enclosures']:
            i,j=entry['i'],entry['j'];value=-c*(integral(i,j)+integral(j,i))
            # Translation derivative includes the moving endpoint and both
            # shifted polynomial derivatives. Legendre Markov bounds apply
            # throughout every enclosing physical overlap interval.
            lipschitz=2*A[i]*A[j]+2*(A[i]*D[j]+A[j]*D[i])
            error=(ch-cl)/2*2*R*A[i]*A[j]+ch*(eh-el)/2*lipschitz
            lo,hi=F(entry['lower']),F(entry['upper'])
            assert lo<=value-error<=value+error<=hi,(n,i,j)
            total_lower[i][j]=total_lower[j][i]=total_lower[i][j]+lo
            total_upper[i][j]=total_upper[j][i]=total_upper[i][j]+hi
        print('replayed rational prime overlaps',n,file=sys.stderr,flush=True)
    assert norm==F(cert['full_paired_prime_physical_operator_norm_upper'])
    rho=F(native['canonical_native_Gram_physical_upper_factor']); beta=F(native['canonical_trial_error_physical_squared_upper'])
    assert rho*norm==F(cert['full_paired_prime_canonical_operator_norm_upper'])
    assert (rho*norm)**2==F(cert['whole_actual_prime_source_Gram_relative_native_metric_upper'])
    P=[[F(x) for x in r] for r in cert['physical_native_Gram']]
    T=[[F(x) for x in r] for r in cert['physical_native_trial_Gram']]
    for entry in cert['trial_prime_head_entry_enclosures']:
        i,j=entry['i'],entry['j']
        assert F(entry['lower'])<=total_lower[i][j]<=total_upper[i][j]<=F(entry['upper'])
    for entry in cert['actual_native_prime_head_entry_enclosures']:
        i,j=entry['i'],entry['j'];lo,hi=F(entry['lower']),F(entry['upper'])
        if (i-j)%2: assert lo==hi==0
        else:
            radius=I(norm)*(I(rho*beta*P[i][i]*T[j][j]).sqrt()+
                           I(rho*beta*P[j][j]*T[i][i]).sqrt()+
                           I(rho*beta*P[i][i]).sqrt()*I(rho*beta*P[j][j]).sqrt())
            assert I(lo).h<=loctx.subtract(I(total_lower[i][j]).l,radius.h)
            assert I(hi).l>=hictx.add(I(total_upper[i][j]).h,radius.h)
    diagonals={entry['i']:entry for entry in cert['actual_native_prime_head_entry_enclosures'] if entry['i']==entry['j']}
    assert F(diagonals[0]['upper'])<0<F(diagonals[1]['lower'])
    center=[[F(x) for x in row] for row in cert['trial_prime_head_rational_center']]
    half=F(0)
    for entry in cert['trial_prime_head_entry_enclosures']:
        i,j=entry['i'],entry['j'];lo,hi=F(entry['lower']),F(entry['upper'])
        assert center[i][j]==center[j][i]==(lo+hi)/2
        half=max(half,(hi-lo)/2)
    assert psd([[P[i][j]-F(1,8)*(i==j) for j in range(8)] for i in range(8)])
    assert F(cert['trial_center_physical_metric_rounding_error_upper'])==64*half
    tv=F(residual['trial_map_squared_upper'])
    assert psd([[tv*P[i][j]-T[i][j] for j in range(8)] for i in range(8)])
    normalized=I(norm)*(2*I(rho*beta*tv).sqrt()+I(rho*beta))
    assert F(cert['actual_prime_head_trial_center_physical_metric_error_upper'])>=outward(normalized)[1]+64*half
    print('PASS: rational translated-overlap replay, active set, path bounds, all native entries, and whole-source budget')

if __name__=='__main__':
    root=Path(__file__).parent.parent/'certificates'
    if len(sys.argv)>1 and sys.argv[1]=='--replay':
        replay(sys.argv[2],sys.argv[3] if len(sys.argv)>3 else root/'rpb108_rc39_native_low_chebyshev_gram.json',
               sys.argv[4] if len(sys.argv)>4 else root/'rpb108_rc38_thirty_two_residuals.json')
    else:
        native=sys.argv[1] if len(sys.argv)>1 else root/'rpb108_rc39_native_low_chebyshev_gram.json'
        residual=sys.argv[2] if len(sys.argv)>2 else root/'rpb108_rc38_thirty_two_residuals.json'
        print(json.dumps(run(native,residual),indent=2))
