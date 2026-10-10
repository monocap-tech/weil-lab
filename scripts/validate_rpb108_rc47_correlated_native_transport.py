"""RC47: transport the mixed RC38 residual Gram into native coordinates."""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import hashlib,json,sys
from validate_rpb108_rc31_trial_riesz import mm,tr,psd

def root(q,den=10**18):
    assert q>=0
    k=isqrt(q.numerator*den*den//q.denominator)
    if F(k*k,den*den)<q: k+=1
    return F(k,den)

def upper(q,den=10**20):
    scaled=q*den
    return F(-(-scaled.numerator//scaled.denominator),den)

def matrix(rows): return [[F(x) for x in row] for row in rows]
def entries(rows): return {(r['i'],r['j']):(F(r['lower']),F(r['upper'])) for r in rows}
def intersect(a,b):
    result=(max(a[0],b[0]),min(a[1],b[1]));assert result[0]<=result[1]
    return result
def product(a,b):
    vals=[x*y for x in a for y in b];return min(vals),max(vals)
def serialize(A): return [[str(x) for x in row] for row in A]
def rows(A): return [dict(i=i,j=j,lower=str(a),upper=str(b)) for (i,j),(a,b) in sorted(A.items())]

def run(paths):
    raw=[Path(p).read_bytes() for p in paths]
    metric,residual,native,pole,prime,arch=[json.loads(x) for x in raw]
    hashes=[hashlib.sha256(x).hexdigest() for x in raw]
    assert residual['metric_certificate_sha256']==native['metric_certificate_sha256']==hashes[0]
    assert pole['source_certificate_sha256']==prime['native_certificate_sha256']==arch['native_certificate_sha256']==hashes[2]
    assert prime['residual_certificate_sha256']==hashes[1]
    assert arch['metric_certificate_sha256']==hashes[0]
    assert arch['pole_certificate_sha256']==hashes[3] and arch['prime_certificate_sha256']==hashes[4]
    C=matrix(native['chebyshev_to_legendre']);V=matrix(native['native_trial_coefficients'])
    mass=list(map(F,metric['physical_mass']));P=matrix(native['physical_native_Gram'])
    T=matrix(prime['physical_native_trial_Gram']);G=matrix(metric['metric_center'])
    assert T==mm(mm(tr(V),[[mass[i]*(i==j) for j in range(32)] for i in range(32)]),V)
    Q=matrix(residual['nominal_Gram_center']);eta=F(residual['normalized_Gram_rounding_error_upper'])
    half=max((F(r['upper'])-F(r['lower']))/2 for r in residual['nominal_Gram_entry_enclosures'])
    assert eta==8*half/min(mass[:8])
    for r in residual['nominal_Gram_entry_enclosures']:
        assert Q[r['i']][r['j']]==(F(r['lower'])+F(r['upper']))/2
    # Nominal physical residual Gram <= Q+eta D. Congruence retains all
    # native correlations instead of replacing it by a scalar times P.
    Qup=mm(mm(tr(C),[[Q[i][j]+eta*mass[i]*(i==j) for j in range(8)] for i in range(8)]),C)
    assert psd(Qup)
    delta=upper(F(residual['source_operator_error_upper']));rho=F(252,257)
    # Fixed Young parameter supplies a whole-map bound, in addition to
    # sharper columnwise Minkowski bounds used below.
    B=[[F(33,32)*Qup[i][j]+33*delta*delta*T[i][j] for j in range(8)] for i in range(8)]
    d2=[(root(Qup[i][i])+delta*root(T[i][i]))**2 for i in range(8)]
    ec=[root(rho*x) for x in d2];ep=[root(rho*rho*x) for x in d2]
    v=[root(T[i][i]) for i in range(8)]
    oldphysical=F(residual['collective_physical_squared_upper'])
    assert all(d2[i]<oldphysical*P[i][i] for i in range(8))
    H=mm(mm(tr(V),G),V)
    # J_ij=<q_i,V_j>_physical. Exact Riesz identities give
    # M=J+J^*-H_actual+E^*E, preserving the canonical/physical distinction.
    J=mm(tr(C),[[mass[i]*V[i][j] for j in range(8)] for i in range(8)])
    Emetric=F(metric['mass_metric_error_upper'])
    oldM=entries(native['canonical_native_Gram_entry_enclosures'])
    oldA=entries(arch['actual_native_archimedean_head_entry_enclosures'])
    oldP=entries(prime['actual_native_prime_head_entry_enclosures'])
    oldO=entries(pole['actual_native_signed_pole_head_entry_enclosures'])
    oldW=entries(arch['actual_original_Weil_low_head_entry_enclosures'])
    rem=entries(arch['archimedean_trial_remainder_head_entry_enclosures'])
    trialprime=entries(prime['trial_prime_head_entry_enclosures'])
    polemom=[];actualmom=[]
    norms=[F(pole['cosh_physical_norm_squared_upper']),F(pole['sinh_physical_norm_squared_upper'])]
    for i,row in enumerate(pole['actual_native_pole_moment_enclosures']):
        assert row['j']==i
        a,b=F(row['trial_m_plus_lower']),F(row['trial_m_plus_upper'])
        rad=ep[i]*root(norms[i%2])
        polemom.append((a,b));actualmom.append((a-rad,b+rad))
    kp=F(prime['full_paired_prime_physical_operator_norm_upper'])
    matrices=[{} for _ in range(5)];newM,newA,newP,newO,newW=matrices
    ratios=[]
    for i in range(8):
        for j in range(i,8):
            key=(i,j)
            if (i-j)%2:
                for out in matrices:out[key]=(F(0),F(0))
                continue
            center=J[i][j]+J[j][i]-H[i][j]
            metricrad=Emetric*root(T[i][i]*T[j][j])
            if i==j:
                m=(center-metricrad,center+metricrad+rho*d2[i])
            else:
                rad=metricrad+ec[i]*ec[j];m=(center-rad,center+rad)
            newM[key]=intersect(m,oldM[key])
            transfer=ep[i]*v[j]+ep[j]*v[i]+ep[i]*ep[j]
            newA[key]=intersect((newM[key][0]+rem[key][0]-8*transfer,
                                newM[key][1]+rem[key][1]+8*transfer),oldA[key])
            newP[key]=intersect((trialprime[key][0]-kp*transfer,trialprime[key][1]+kp*transfer),oldP[key])
            if i==j:
                a,b=actualmom[i];sq=(F(0) if a<=0<=b else min(a*a,b*b),max(a*a,b*b))
                po=(2*sq[0],2*sq[1]) if i%2==0 else (-2*sq[1],-2*sq[0])
            else:
                po=product(actualmom[i],actualmom[j]);factor=2*(-1)**i
                po=(factor*po[0],factor*po[1]) if factor>0 else (factor*po[1],factor*po[0])
            newO[key]=intersect(po,oldO[key])
            total=(sum(out[key][0] for out in [newA,newP,newO]),sum(out[key][1] for out in [newA,newP,newO]))
            newW[key]=intersect(total,oldW[key])
            ratios.append((oldW[key][1]-oldW[key][0])/(newW[key][1]-newW[key][0]))
    assert len(newW)==36 and min(ratios)>F(11,4)
    return dict(milestone='RC47',status='PASS',input_sha256=hashes,
        native_features_certified=list(range(8)),
        source_operator_error_rational_upper=str(delta),
        nominal_native_residual_Gram_Loewner_upper=serialize(Qup),
        actual_physical_residual_Gram_Loewner_upper=serialize(B),
        actual_canonical_Riesz_error_Gram_Loewner_upper=serialize([[rho*x for x in row] for row in B]),
        actual_physical_Riesz_error_Gram_Loewner_upper=serialize([[rho*rho*x for x in row] for row in B]),
        actual_physical_residual_column_squared_upper=list(map(str,d2)),
        canonical_Riesz_error_column_norm_upper=list(map(str,ec)),
        physical_Riesz_error_column_norm_upper=list(map(str,ep)),
        trial_physical_column_norm_upper=list(map(str,v)),
        refined_actual_native_Gram_entry_enclosures=rows(newM),
        refined_actual_archimedean_head_entry_enclosures=rows(newA),
        refined_actual_prime_head_entry_enclosures=rows(newP),
        refined_actual_signed_pole_head_entry_enclosures=rows(newO),
        refined_actual_original_Weil_low_head_entry_enclosures=rows(newW),
        minimum_nonzero_entry_width_improvement_factor_lower=str(min(ratios)),
        all_original_head_diagonal_intervals_contain_zero=all(a<0<b for (i,j),(a,b) in newW.items() if i==j),
        original_Weil_head_floor_certified=False,
        combined_original_source_covariance_evaluated=False,
        full_1250_native_projection_constructed=False,aperture_extended=False)

def replay(path,inputs):
    cert=json.loads(Path(path).read_text());data=[json.loads(Path(p).read_text()) for p in inputs]
    metric,residual,native,pole,prime,arch=data
    assert cert['input_sha256']==[hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in inputs]
    # Independently convert entries by scalar double sums instead of matrix
    # multiplication, and verify norm bounds by exact squared inequalities.
    C=matrix(native['chebyshev_to_legendre']);Q=matrix(residual['nominal_Gram_center'])
    eta=F(residual['normalized_Gram_rounding_error_upper']);mass=list(map(F,metric['physical_mass']))
    Qup=matrix(cert['nominal_native_residual_Gram_Loewner_upper'])
    T=matrix(prime['physical_native_trial_Gram']);delta=F(cert['source_operator_error_rational_upper']);rho=F(252,257)
    assert 0<=delta-F(residual['source_operator_error_upper'])<F(1,10**20)
    B=matrix(cert['actual_physical_residual_Gram_Loewner_upper'])
    for i in range(8):
        for j in range(8):
            exact=sum((C[k][i]*C[l][j]*(Q[k][l]+eta*mass[k]*(k==l)) for k in range(8) for l in range(8)),F(0))
            assert exact==Qup[i][j]
            assert B[i][j]==F(33,32)*exact+33*delta*delta*T[i][j]
        # d_i >=sqrt(Qup_ii)+delta sqrt(T_ii), without irrational arithmetic.
        dsq=F(cert['actual_physical_residual_column_squared_upper'][i])
        slack=dsq-Qup[i][i]-delta*delta*T[i][i]
        assert slack>=0 and slack*slack>=4*delta*delta*Qup[i][i]*T[i][i]
        assert F(cert['canonical_Riesz_error_column_norm_upper'][i])**2>=rho*dsq
        assert F(cert['physical_Riesz_error_column_norm_upper'][i])**2>=rho*rho*dsq
        assert F(cert['trial_physical_column_norm_upper'][i])**2>=T[i][i]
    assert psd(B) and psd(Qup)
    # Replay all exact rational identity/transport/intersection calculations.
    rebuilt=run(inputs)
    assert rebuilt==cert
    assert not cert['original_Weil_head_floor_certified']
    print('PASS: scalar mixed-Gram conversion, squared norm inequalities, whole-map bounds, all 36 refined original entries and historical intersections')

if __name__=='__main__':
    base=Path(__file__).parent.parent/'certificates'
    defaults=[base/name for name in ['rpb108_rc38_thirty_two_metric.json','rpb108_rc38_thirty_two_residuals.json',
        'rpb108_rc39_native_low_chebyshev_gram.json','rpb108_rc42_native_signed_pole_head.json',
        'rpb108_rc43_native_prime_head.json','rpb108_rc46_native_archimedean_head.json']]
    if len(sys.argv)>1 and sys.argv[1]=='--replay':replay(sys.argv[2],sys.argv[3:] or defaults)
    else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
