"""Actual low-eight archimedean head and complete original-head assembly."""
from validate_rpb108_rc30_interval_metric import I,hictx
from validate_rpb108_rc29_atom_reduction import legendre
from validate_rpb108_rc35_enriched_residuals import transformed
from validate_rpb108_rc31_trial_riesz import mm,tr
from validate_rpb108_rc42_native_signed_pole_head import outward,rational_interval
from fractions import Fraction as F
from pathlib import Path
from math import factorial
import hashlib,json,sys

def regular_coefficients(N):
    # r j(r)=exp(r/2)/(2(sinh(r)/r)). Formal series division is exact.
    a=[]
    for n in range(N+2):
        a.append(F(1,2**(n+1)*factorial(n))-
                 sum((a[n-k]/factorial(k+1) for k in range(2,n+1,2)),F(0)))
    assert a[0]==F(1,2) and a[1]==F(1,4) and a[2]==F(-1,48)
    return a[1:]

def run(metric_path,native_path,pole_path,prime_path):
    paths=[metric_path,native_path,pole_path,prime_path]
    raw=[Path(p).read_bytes() for p in paths];metric,native,pole,prime=[json.loads(x) for x in raw]
    hashes=[hashlib.sha256(x).hexdigest() for x in raw]
    assert native['metric_certificate_sha256']==hashes[0]
    assert pole['source_certificate_sha256']==prime['native_certificate_sha256']==hashes[1]
    assert metric['trial_dimension']==32 and native['native_features_certified']==list(range(8))
    V=[[F(x) for x in row] for row in native['native_trial_coefficients']]
    G=[[F(x) for x in row] for row in metric['metric_center']]
    P=[[F(x) for x in row] for row in native['physical_native_Gram']]
    mass=list(map(F,metric['physical_mass']));R=F(11,5);B=R/2;N=192
    T=mm(mm(tr(V),[[mass[i]*(i==j) for j in range(32)] for i in range(32)]),V)
    Hmetric=mm(mm(tr(V),G),V)
    harmonics=[sum((F(1,k) for k in range(1,n+1)),F(0)) for n in range(260)]
    reg=regular_coefficients(N)
    # Cauchy circle |z|=3: |sinh z|>1/10 and exp(Re z/2)<5,
    # giving |z j(z)|<75. Tail for j-1/(2z) on [0,11/5].
    sin3_lower=sum(((-1)**k*F(3)**(2*k+1)/factorial(2*k+1) for k in range(6)),F(0))
    assert sin3_lower>F(1,10)
    exp15=sum((F(3,2)**k/factorial(k) for k in range(101)),F(0))
    exp15+=F(3,2)**101/factorial(101)/(1-F(3,204))
    assert exp15<5
    tail=F(375,4)*F(11,15)**(N+1);assert tail<F(1,10**23)
    polys=[]
    for j in range(8):
        p=[F(0)]*32
        for n in range(32):
            for k,a in enumerate(transformed(legendre(n))): p[k]+=V[n][j]*a
        polys.append(p)
    fac=[factorial(n) for n in range(260)]
    left=[]
    for j in range(8):
        a=[F(0)]*(N+34)
        for p,rp in enumerate(reg):
            for m,vm in enumerate(polys[j]):
                a[p+m+1]+=R*rp*R**p*vm*F(fac[p]*fac[m],fac[p+m+1])
        left.append(a)
        print('archimedean polynomial convolution',j,'built',file=sys.stderr,flush=True)
    c_mid=F(-3203794213-3203306050,2*10**9);dc=F(488163,2*10**9)
    E=F(metric['mass_metric_error_upper']);beta=F(native['canonical_trial_error_physical_squared_upper']);rho=F(252,257)
    arch=[];rem=[];nominal=[[F(0)]*8 for _ in range(8)]
    Mentries={(r['i'],r['j']):r for r in native['canonical_native_Gram_entry_enclosures']}
    for i in range(8):
        for j in range(i,8):
            if (i-j)%2:
                arch.append(dict(i=i,j=j,lower='0',upper='0',reason='exact parity'))
                rem.append(dict(i=i,j=j,lower='0',upper='0'))
                continue
            endpoint=R*sum((a*b*(F(1,2*(k+l+1)**2)+harmonics[k+l+1]/(2*(k+l+1)))
                            for k,a in enumerate(polys[i]) for l,b in enumerate(polys[j])),F(0))
            t0=sum((harmonics[n]*mass[n]*V[n][i]*V[n][j] for n in range(32)),F(0))
            def left_pair(i,j):
                return R*sum((a*b/F(k+l+1) for k,a in enumerate(polys[i])
                              for l,b in enumerate(left[j])),F(0))
            kernel=2*left_pair(i,j)
            assert kernel==2*left_pair(j,i)
            q=endpoint+t0+c_mid*T[i][j]-kernel
            nominal[i][j]=nominal[j][i]=q
            rem_center=q-Hmetric[i][j]
            perturb=(I(E+dc+R*tail)*I(T[i][i]*T[j][j]).sqrt())
            trial_rem=I(rem_center)+I(perturb.h.copy_negate(),perturb.h)
            lo,hi=outward(trial_rem,10**20)
            rem.append(dict(i=i,j=j,lower=str(lo),upper=str(hi)))
            # The archimedean PHYSICAL bounded remainder has norm <8 (RC17/21).
            e_i=I(rho*beta*P[i][i]).sqrt();e_j=I(rho*beta*P[j][j]).sqrt()
            transfer=8*(e_i*I(T[j][j]).sqrt()+e_j*I(T[i][i]).sqrt()+e_i*e_j)
            mr=Mentries[(i,j)]
            actual=rational_interval(F(mr['lower']),F(mr['upper']))+trial_rem+I(transfer.h.copy_negate(),transfer.h)
            al,au=outward(actual)
            arch.append(dict(i=i,j=j,lower=str(al),upper=str(au)))
            print('actual archimedean head entry',i,j,'enclosed',file=sys.stderr,flush=True)
    prime_entries={(r['i'],r['j']):r for r in prime['actual_native_prime_head_entry_enclosures']}
    pole_entries={(r['i'],r['j']):r for r in pole['actual_native_signed_pole_head_entry_enclosures']}
    full=[]
    for row in arch:
        i,j=row['i'],row['j'];pr=prime_entries[(i,j)];po=pole_entries[(i,j)]
        lo=F(row['lower'])+F(pr['lower'])+F(po['lower'])
        hi=F(row['upper'])+F(pr['upper'])+F(po['upper'])
        full.append(dict(i=i,j=j,lower=str(lo),upper=str(hi)))
    assert F(full[0]['lower'])<0<F(full[0]['upper'])
    return dict(milestone='RC46',status='PASS',
        metric_certificate_sha256=hashes[0],native_certificate_sha256=hashes[1],
        pole_certificate_sha256=hashes[2],prime_certificate_sha256=hashes[3],
        native_features_certified=list(range(8)),regular_kernel_degree=N,
        regular_kernel_coefficients=list(map(str,reg)),regular_kernel_uniform_error_upper=str(tail),
        archimedean_trial_head_nominal=[[str(x) for x in row] for row in nominal],
        archimedean_trial_remainder_head_entry_enclosures=rem,
        actual_native_archimedean_head_entry_enclosures=arch,
        actual_original_Weil_low_head_entry_enclosures=full,
        physical_archimedean_remainder_norm_upper='8',
        canonical_archimedean_remainder_norm_upper=str(8*rho),
        whole_actual_archimedean_remainder_source_Gram_relative_native_metric_upper=str((8*rho)**2),
        actual_low_native_archimedean_head_enclosed=True,
        actual_original_Weil_low_head_enclosed=True,
        first_original_low_head_diagonal_interval_contains_zero=True,
        original_Weil_head_floor_certified=False,
        combined_native_source_covariance_evaluated=False,
        full_1250_native_projection_constructed=False,aperture_extended=False)

def replay(certificate_path,metric_path,native_path,pole_path,prime_path):
    raw=[Path(p).read_bytes() for p in [metric_path,native_path,pole_path,prime_path]]
    metric,native,pole,prime=[json.loads(x) for x in raw]
    cert=json.loads(Path(certificate_path).read_text())
    for name,value in zip(['metric_certificate_sha256','native_certificate_sha256','pole_certificate_sha256','prime_certificate_sha256'],raw):
        assert cert[name]==hashlib.sha256(value).hexdigest()
    N=cert['regular_kernel_degree'];R=F(11,5);reg=list(map(F,cert['regular_kernel_coefficients']))
    # Alternative exact division: r j(r)=(1/2)exp(-r/2)/D(r),
    # D(r)=(1-exp(-2r))/(2r), rather than exp(r/2)/(2 sinh(r)/r).
    a=[]
    for n in range(N+2):
        a.append(F(1,2)*F(-1,2)**n/factorial(n)-
                 sum((a[n-k]*F(-2)**k/factorial(k+1) for k in range(1,n+1)),F(0)))
    assert a[0]==F(1,2) and a[1:]==reg
    tail=F(375,4)*F(11,15)**(N+1)
    assert tail==F(cert['regular_kernel_uniform_error_upper'])<F(1,10**23)
    V=[[F(x) for x in row] for row in native['native_trial_coefficients']]
    mass=list(map(F,metric['physical_mass']))
    G=[[F(x) for x in row] for row in metric['metric_center']]
    T=mm(mm(tr(V),[[mass[i]*(i==j) for j in range(32)] for i in range(32)]),V)
    Hmetric=mm(mm(tr(V),G),V)
    from validate_rpb108_rc30_interval_metric import endpoint
    endpoints=[[endpoint(i,j) if (i-j)%2==0 else F(0) for j in range(32)] for i in range(32)]
    W=mm(mm(tr(V),endpoints),V)
    polys=[]
    for j in range(8):
        p=[F(0)]*32
        for n in range(32):
            for k,x in enumerate(transformed(legendre(n))): p[k]+=V[n][j]*x
        polys.append(p)
    # Direct triangle moments, without constructing the convolved polynomial.
    weighted=[[sum((x/F(k+d+1) for k,x in enumerate(poly)),F(0))
               for d in range(N+34)] for poly in polys]
    beta_table=[[F(factorial(p)*factorial(m),factorial(p+m+1)) for m in range(32)] for p in range(N+1)]
    H=[sum((F(1,k) for k in range(1,n+1)),F(0)) for n in range(32)]
    mid=F(-3203794213-3203306050,2*10**9);dc=F(488163,2*10**9)
    E=F(metric['mass_metric_error_upper']);rho=F(252,257);beta=F(native['canonical_trial_error_physical_squared_upper'])
    P=[[F(x) for x in row] for row in native['physical_native_Gram']]
    nominal=[[F(x) for x in row] for row in cert['archimedean_trial_head_nominal']]
    Mentries={(r['i'],r['j']):r for r in native['canonical_native_Gram_entry_enclosures']}
    rem={(r['i'],r['j']):r for r in cert['archimedean_trial_remainder_head_entry_enclosures']}
    for row in cert['actual_native_archimedean_head_entry_enclosures']:
        i,j=row['i'],row['j'];lo,hi=F(row['lower']),F(row['upper'])
        if (i-j)%2: assert lo==hi==nominal[i][j]==0;continue
        kernel=2*R*R*sum((rp*R**p*vm*beta_table[p][m]*weighted[i][p+m+1]
                          for p,rp in enumerate(reg) for m,vm in enumerate(polys[j])),F(0))
        t0=sum((H[n]*mass[n]*V[n][i]*V[n][j] for n in range(32)),F(0))
        q=W[i][j]+t0+mid*T[i][j]-kernel
        assert q==nominal[i][j]==nominal[j][i]
        error=I(E+dc+R*tail)*I(T[i][i]*T[j][j]).sqrt()
        trial=I(q-Hmetric[i][j])+I(error.h.copy_negate(),error.h)
        rr=rem[(i,j)]
        assert I(F(rr['lower'])).h<=trial.l and I(F(rr['upper'])).l>=trial.h
        transfer=8*(I(rho*beta*P[i][i]*T[j][j]).sqrt()+I(rho*beta*P[j][j]*T[i][i]).sqrt()+
                    I(rho*beta*P[i][i]).sqrt()*I(rho*beta*P[j][j]).sqrt())
        mr=Mentries[(i,j)]
        actual=rational_interval(F(mr['lower']),F(mr['upper']))+trial+I(transfer.h.copy_negate(),transfer.h)
        assert I(lo).h<=actual.l and I(hi).l>=actual.h
        print('replayed archimedean head',i,j,file=sys.stderr,flush=True)
    maps=[{(r['i'],r['j']):r for r in rows} for rows in [cert['actual_native_archimedean_head_entry_enclosures'],
           pole['actual_native_signed_pole_head_entry_enclosures'],prime['actual_native_prime_head_entry_enclosures']]]
    for row in cert['actual_original_Weil_low_head_entry_enclosures']:
        key=(row['i'],row['j'])
        assert F(row['lower'])==sum((F(m[key]['lower']) for m in maps),F(0))
        assert F(row['upper'])==sum((F(m[key]['upper']) for m in maps),F(0))
    assert F(cert['whole_actual_archimedean_remainder_source_Gram_relative_native_metric_upper'])==(8*rho)**2
    assert not cert['original_Weil_head_floor_certified']
    print('PASS: alternate regular-kernel series, Legendre endpoint integrals, direct triangle moments, all actual entries, and complete assembly')

if __name__=='__main__':
    root=Path(__file__).parent.parent/'certificates'
    defaults=[root/'rpb108_rc38_thirty_two_metric.json',root/'rpb108_rc39_native_low_chebyshev_gram.json',
              root/'rpb108_rc42_native_signed_pole_head.json',root/'rpb108_rc43_native_prime_head.json']
    if len(sys.argv)>1 and sys.argv[1]=='--replay':
        replay(sys.argv[2],*(sys.argv[3:] or defaults))
    else:
        print(json.dumps(run(*(sys.argv[1:] or defaults)),indent=2))
