"""Independent three-band step arithmetic and all three complete mass audits."""
import hashlib,json,tempfile
from pathlib import Path
from fractions import Fraction as F
from certify_native_legendre_small_window import I,log_rational
from validate_native_prime5_depth6_complement_097 import certificate as mass_audit
from validate_native_prime5_weighted_schur_097 import certificate as joint_audit
from validate_native_prime5_baseline_097 import certificate as baseline_audit

def certificate(path,repeat):
    raw=Path(path).read_bytes();assert raw==Path(repeat).read_bytes();c=json.loads(raw)
    root=Path(__file__).resolve().parents[1]/'notes/data'
    names=list(c['input_sha256']);assert len(names)==2
    def read(n):
        p=root/n
        return p.read_bytes() if p.exists() else __import__('gzip').decompress(p.with_suffix('.json.gz').read_bytes())
    for n in names:assert hashlib.sha256(read(n)).hexdigest()==c['input_sha256'][n]
    base,joint=[json.loads(read(n)) for n in names]
    assert c['aperture']==base['aperture']==joint['aperture']=='97/100'
    ba=baseline_audit(root/names[0],root/names[0])
    with tempfile.TemporaryDirectory() as directory:
        jp=Path(directory)/'joint.json';jp.write_bytes(read(names[1]));ja=joint_audit(jp,jp)
    cuts=list(map(F,c['cutoffs']));assert cuts==[F(64,5),F(67,5),F(69,5)]
    old=I.grid;I.grid=10**100
    try:high=[log_rational(t)-F(7,216)/t**2 for t in cuts]
    finally:I.grid=old
    stored=[tuple(map(F,p)) for p in c['archimedean_high_intervals']]
    assert all(lo<=h.lo<=h.hi<=hi for (lo,hi),h in zip(stored,high))
    assert all(0<x[0]<=x[1]<y[0] for x,y in zip(stored,stored[1:]))
    masses=list(map(F,c['frequency_masses_upper']));assert 0<masses[0]<masses[1]<masses[2]
    from certify_native_iterated_damped_mass_depth6 import integrated_iterated_mass
    try:integrated_iterated_mass(F(97,100),84,F(14),depth=6)
    except ValueError:pass
    else:raise AssertionError('Invalid outer cutoff accepted')
    reports=[]
    with tempfile.TemporaryDirectory() as directory:
        for i,m in enumerate(c['complete_mass_certificates']):
            assert F(m['physical_cutoff'])==cuts[i] and F(m['physical_low_frequency_mass_upper'])==masses[i]
            assert m['single_band_positive_lower_claimed'] is False
            for k in ('joint_prime24_operator_upper','joint_prime35_operator_upper','pole_absolute_upper','logarithmic_lower'):
                assert m[k]==base[k]
            p=Path(directory)/f'mass{i}.json';p.write_text(json.dumps(m));reports.append(mass_audit(p,p))
    arch=stored[-1][0]-(stored[0][1]+F(27,5))*masses[0]
    for i in range(1,3):arch-=(stored[i][1]-stored[i-1][0])*masses[i]
    assert arch==F(c['three_band_archimedean_lower'])
    norm=F(joint['joint_prime_operator_norm_upper']);assert norm==F(c['combined_prime_upper'])==F(444727,250000)
    pole=F(base['pole_absolute_upper']);assert pole==F(c['pole_absolute_upper'])
    exact=arch-norm-pole
    assert exact==F(c['physical_unrounded_lower'])>F(c['physical_lower'])==F(4,5)
    assert F(c['complement_inverse_factor'])==F(5,4)
    assert c['logarithmic_lower']==base['logarithmic_lower']=='9/100'
    for region in range(4):
        flags=[int(region<=i) for i in range(3)]
        step=stored[-1][0]-(stored[0][1]+F(27,5))*flags[0]
        for i in range(1,3):step-=(stored[i][1]-stored[i-1][0])*flags[i]
        symbol=-F(27,5) if region==0 else stored[region-1][0]
        assert step<=symbol
    return dict(aperture='97/100',certificate_sha256=hashlib.sha256(raw).hexdigest(),
        byte_identical_repeat=True,all_three_complete_mass_audits=reports,
        independent_logarithmic_baseline_audit=ba,independent_weighted_prime_audit=ja,
        exact_three_band_endpoint_sum_verified=True,pointwise_region_controls=4,obsolete_outer_cutoff_14_rejected=True,
        single_band_intermediates_not_used_as_positive_lower_claims=True,
        physical_lower='4/5',physical_lower_display=float(exact),logarithmic_lower='9/100',
        whole_domain_positivity=False,f4_entry_closed=False,lean_formalized=False)

if __name__=='__main__':
    import sys
    print(json.dumps(certificate(*sys.argv[1:]),indent=2))
