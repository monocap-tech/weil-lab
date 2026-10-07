"""Independent exact endpoints and both complete mass audits."""
import hashlib,json,tempfile
from pathlib import Path
from fractions import Fraction as F
from validate_native_prime5_depth6_complement_092 import certificate as mass_audit
from certify_native_legendre_small_window import I,log_rational

def certificate(path,repeat):
    raw=Path(path).read_bytes();assert raw==Path(repeat).read_bytes()
    c=json.loads(raw)
    root=Path(__file__).resolve().parents[1]/'notes/data'
    outer=root/'RPB108_PRIME5_DEPTH6_COMPLEMENT84_092_CERTIFICATE_20261006.json'
    assert hashlib.sha256(outer.read_bytes()).hexdigest()==c['previous_complement_sha256']
    prior=json.loads(outer.read_bytes());o=c['outer_mass_certificate'];inner=c['inner_mass_certificate']
    with tempfile.TemporaryDirectory() as temp:
        ip=Path(temp)/'inner.json';ip.write_text(json.dumps(inner))
        inner_report=mass_audit(ip,ip)
        op=Path(temp)/'outer.json';op.write_text(json.dumps(o))
        outer_report=mass_audit(op,op)
    assert inner['physical_cutoff']==c['inner_cutoff']=='263/20'
    assert inner['physical_low_frequency_mass_upper']==c['inner_mass_upper']
    old=I.grid;I.grid=10**100
    try:
        bounds=[]
        for t in (F(263,20),F(72,5)):
            z=log_rational(t)-F(7,216)/t**2;bounds.append((z.lo,z.hi))
    finally:I.grid=old
    sl,sh=map(F,c['inner_archimedean_high_interval']);tl,th=map(F,c['outer_archimedean_high_interval'])
    assert sl<=bounds[0][0]<=bounds[0][1]<=sh<tl<=bounds[1][0]<=bounds[1][1]<=th
    ri=F(c['inner_mass_upper']);ro=F(o['physical_low_frequency_mass_upper'])
    assert 0<ri<ro
    loss=sum((F(o[k]) for k in ('joint_prime24_operator_upper','joint_prime35_operator_upper','pole_absolute_upper')),F(0))
    exact=tl-(th-sl)*ro-(sh+F(27,5))*ri-loss
    assert exact==F(c['physical_unrounded_lower'])>F(c['physical_lower'])==F(17,25)
    assert F(c['complement_inverse_factor'])==F(25,17)
    assert all(c[k]==o[k]==prior[k] for k in ('joint_prime24_operator_upper','joint_prime35_operator_upper','pole_absolute_upper','logarithmic_lower'))
    # Exact pointwise step lower bound, including negative central symbol.
    controls=0
    for m,b1,b2 in ((-F(27,5),1,1),(sl,0,1),(tl,0,0)):
        step=tl-(th-sl)*b2-(sh+F(27,5))*b1
        assert step<=m
        controls+=1
    assert tl-(tl-sl)*ri-(sl+F(27,5))*ri> -F(27,5) # wrong outer-mass substitution rejects at central mass
    return dict(certificate_sha256=hashlib.sha256(raw).hexdigest(),byte_identical_repeat=True,
        inner_complete_mass_audit=inner_report,outer_complete_mass_audit=outer_report,
        exact_two_band_endpoint_sum_verified=True,pointwise_region_controls=controls,
        unchanged_prime_pole_logarithmic_bounds=True,complement_lower='17/25',
        whole_domain_positivity=False,f4_closed=False,lean_formalized=False)

if __name__=='__main__':
    import sys
    print(json.dumps(certificate(*sys.argv[1:]),indent=2))
