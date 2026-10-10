"""Enclose the actual low-eight native signed-pole head and source norm."""
from validate_rpb108_rc30_interval_metric import I,loctx,hictx
from validate_rpb108_rc29_atom_reduction import legendre
from validate_rpb108_rc31_trial_riesz import mm,tr,psd
from fractions import Fraction as F
from pathlib import Path
from math import factorial
import hashlib,json,sys

def outward(value,den=10**12):
    low=int(loctx.multiply(value.l,I(den).l).to_integral_value(rounding='ROUND_FLOOR'))
    high=int(hictx.multiply(value.h,I(den).h).to_integral_value(rounding='ROUND_CEILING'))
    return F(low,den),F(high,den)

def rational_interval(lo,hi):
    assert lo<=hi
    return I(I(lo).l,I(hi).h)

def run(path):
    raw=Path(path).read_bytes(); source=json.loads(raw)
    assert source['actual_low_native_Gram_certified']
    assert source['native_features_certified']==list(range(8))
    V=[[F(x) for x in row] for row in source['native_trial_coefficients']]
    P=[[F(x) for x in row] for row in source['physical_native_Gram']]
    beta=F(source['canonical_trial_error_physical_squared_upper'])
    rho=F(source['canonical_native_Gram_physical_upper_factor'])
    B=F(11,10); k=B/2; N=80
    # Entire exponential tail on |t|<=1: geometric ratio <= k/(N+2)<1/2.
    tail=2*k**(N+1)/factorial(N+1)
    assert k/F(N+2)<F(1,2) and tail<F(1,10**140)
    integrals=[]
    for i in range(32):
        p=legendre(i)
        value=sum((B*a*k**n*F(2,m+n+1)/factorial(n)
                   for m,a in enumerate(p) for n in range(N+1)
                   if (m+n)%2==0),F(0))
        integrals.append(value)
    trial=[sum((V[i][j]*integrals[i] for i in range(32)),F(0)) for j in range(8)]
    trial_tail=[2*B*tail*sum((abs(V[i][j]) for i in range(32)),F(0)) for j in range(8)]
    sinh=(I(B).exp()-I(-B).exp())/2
    even_norm=I(B)+sinh; odd_norm=sinh-I(B)
    assert even_norm.l>0 and odd_norm.l>0
    norm_upper=[outward(even_norm)[1],outward(odd_norm)[1]]
    rows=[]; u=[]; bounds=[]
    for j in range(8):
        # Reflection gives m_+(r_j)=<cosh(x/2),i r_j> for even j,
        # and <sinh(x/2),i r_j> for odd j. Use the smaller parity norm.
        rad=(I(rho*beta*P[j][j])*I(norm_upper[j%2])).sqrt()+I(trial_tail[j])
        lo,hi=outward(I(trial[j])+I(rad.h.copy_negate(),rad.h))
        tl,th=outward(I(trial[j])+rational_interval(-trial_tail[j],trial_tail[j]))
        rows.append(dict(j=j,trial_m_plus_lower=str(tl),trial_m_plus_upper=str(th),
                         actual_m_plus_lower=str(lo),actual_m_plus_upper=str(hi),
                         m_minus_parity_multiplier=str((-1)**j)))
        u.append(rational_interval(lo,hi))
        bounds.append((lo,hi))
    assert u[0].l>0 and u[1].l>0  # both signed parity blocks have rank one
    entries=[]
    for i in range(8):
        for j in range(i,8):
            if (i-j)%2:
                entries.append(dict(i=i,j=j,lower='0',upper='0',reason='exact parity'))
            else:
                if i==j:
                    a,b=bounds[i]
                    low_square=F(0) if a<=0<=b else min(a*a,b*b)
                    high_square=max(a*a,b*b)
                    lo,hi=(2*low_square,2*high_square) if i%2==0 else (-2*high_square,-2*low_square)
                else:
                    value=2*((-1)**i)*u[i]*u[j]
                    lo,hi=outward(value)
                entries.append(dict(i=i,j=j,lower=str(lo),upper=str(hi)))
    # Physical pole remainder is 2 |cosh><cosh| -2 |sinh><sinh|.
    # Its canonical lift is 2 |i^*cosh><i^*cosh| -2 |i^*sinh><i^*sinh|.
    # Reflection makes these two canonical images orthogonal.
    physical_norm_upper=2*norm_upper[0]
    canonical_norm_upper=rho*physical_norm_upper
    source_squared_upper=canonical_norm_upper**2
    # For actual source columns sigma_pole=A_pole R, sigma^*sigma<=K^2 M.
    assert canonical_norm_upper<F(24,5)
    return dict(milestone='RC42',status='PASS',
        source_certificate_sha256=hashlib.sha256(raw).hexdigest(),
        original_form_source_blob='e9a44661f94ee6750fc5ad1fbf7dc719fa3ba482',
        native_features_certified=list(range(8)),exponential_degree=N,
        exponential_uniform_remainder_upper=str(tail),
        cosh_physical_norm_squared_upper=str(norm_upper[0]),
        sinh_physical_norm_squared_upper=str(norm_upper[1]),
        actual_native_pole_moment_enclosures=rows,
        actual_native_signed_pole_head_entry_enclosures=entries,
        actual_native_signed_pole_head_rank=2,
        actual_native_signed_pole_head_inertia=[1,1,6],
        physical_signed_pole_operator_norm_upper=str(physical_norm_upper),
        canonical_signed_pole_operator_norm_upper=str(canonical_norm_upper),
        canonical_negative_pole_part_norm_upper=str(2*rho*norm_upper[1]),
        whole_actual_pole_source_Gram_relative_native_metric_upper=str(source_squared_upper),
        whole_actual_odd_pole_source_Gram_relative_native_metric_upper=str((2*rho*norm_upper[1])**2),
        actual_signed_pole_head_enclosed=True,actual_signed_pole_source_norm_enclosed=True,
        exact_actual_pole_source_Gram_evaluated=False,
        complete_native_Gram_certified=False,full_native_remainder_sources_certified=False,
        original_Weil_head_floor_certified=False,aperture_extended=False)

def replay(certificate_path,source_path):
    """Positive Rodrigues-series replay, independent of power-basis cancellation."""
    raw=Path(source_path).read_bytes(); source=json.loads(raw)
    cert=json.loads(Path(certificate_path).read_text())
    assert cert['source_certificate_sha256']==hashlib.sha256(raw).hexdigest()
    V=[[F(x) for x in row] for row in source['native_trial_coefficients']]
    P=[[F(x) for x in row] for row in source['physical_native_Gram']]
    beta=F(source['canonical_trial_error_physical_squared_upper'])
    rho=F(source['canonical_native_Gram_physical_upper_factor'])
    B=F(11,10); k=B/2; integrals=[]
    # Rodrigues + n integrations by parts gives the positive series
    # integral exp(kt) P_n(t) dt =sum_l 2^(n+1) k^(n+2l)
    #                              (l+n)!/[l!(2l+2n+1)!].
    for n in range(32):
        def term(l): return F(2**(n+1)*factorial(l+n),factorial(l)*factorial(2*l+2*n+1))*k**(n+2*l)
        lower=B*sum((term(l) for l in range(41)),F(0))
        ratio=k*k/F(2*42*(2*41+2*n+3))
        assert 0<ratio<F(1,2)
        upper=lower+2*B*term(41)
        integrals.append((lower,upper))
    sinh_low=sum((B**n/factorial(n) for n in range(1,81,2)),F(0))
    sinh_high=sinh_low+2*B**81/factorial(81)
    norms=[F(cert['cosh_physical_norm_squared_upper']),F(cert['sinh_physical_norm_squared_upper'])]
    assert norms[0]>=B+sinh_high and norms[1]>=sinh_high-B>0
    bounds=[]
    for row in cert['actual_native_pole_moment_enclosures']:
        j=row['j']; tl=F(0);tu=F(0)
        for i in range(32):
            a,b=integrals[i]; coefficient=V[i][j]
            tl+=coefficient*(a if coefficient>=0 else b)
            tu+=coefficient*(b if coefficient>=0 else a)
        assert F(row['trial_m_plus_lower'])<=tl<=tu<=F(row['trial_m_plus_upper'])
        lo=F(row['actual_m_plus_lower']); hi=F(row['actual_m_plus_upper'])
        radius_squared=rho*beta*P[j][j]*norms[j%2]
        assert tl>lo and hi>tu
        assert (tl-lo)**2>=radius_squared and (hi-tu)**2>=radius_squared
        assert row['m_minus_parity_multiplier']==str((-1)**j)
        bounds.append((lo,hi))
    assert bounds[0][0]>0 and bounds[1][0]>0
    for row in cert['actual_native_signed_pole_head_entry_enclosures']:
        i=row['i'];j=row['j'];lo=F(row['lower']);hi=F(row['upper'])
        if (i-j)%2: assert lo==hi==0
        elif i==j:
            a,b=bounds[i]; low=F(0) if a<=0<=b else min(a*a,b*b); high=max(a*a,b*b)
            expected=(2*low,2*high) if i%2==0 else (-2*high,-2*low)
            assert lo<=expected[0]<=expected[1]<=hi
        else:
            products=[2*((-1)**i)*a*b for a in bounds[i] for b in bounds[j]]
            assert lo<=min(products)<=max(products)<=hi
    assert F(cert['canonical_signed_pole_operator_norm_upper'])==2*rho*norms[0]
    assert F(cert['canonical_negative_pole_part_norm_upper'])==2*rho*norms[1]
    assert F(cert['whole_actual_pole_source_Gram_relative_native_metric_upper'])==(2*rho*norms[0])**2
    assert F(cert['whole_actual_odd_pole_source_Gram_relative_native_metric_upper'])==(2*rho*norms[1])**2
    assert cert['actual_native_signed_pole_head_rank']==2
    assert cert['actual_native_signed_pole_head_inertia']==[1,1,6]
    print('PASS: positive Rodrigues-series replay, all moment/head entries, signed rank, and whole-source bound')

if __name__=='__main__':
    root=Path(__file__).parent.parent/'certificates'
    if len(sys.argv)>1 and sys.argv[1]=='--replay':
        replay(sys.argv[2],sys.argv[3] if len(sys.argv)>3 else root/'rpb108_rc39_native_low_chebyshev_gram.json')
    else:
        path=sys.argv[1] if len(sys.argv)>1 else root/'rpb108_rc39_native_low_chebyshev_gram.json'
        print(json.dumps(run(path),indent=2))
