"""Independent exact step-symbol arithmetic with complete inherited mass audits."""
import json,hashlib
from pathlib import Path
from fractions import Fraction as F
from validate_native_prime5_twoband_complement_093 import certificate as audit_parent
from validate_native_prime5_joint_power4_093 import certificate as audit_joint

def certificate(path,repeat):
    raw=Path(path).read_bytes();assert raw==Path(repeat).read_bytes();c=json.loads(raw)
    root=Path(__file__).resolve().parents[1]/'notes/data'
    names=list(c['input_sha256']);assert len(names)==2
    parent_path,joint_path=[root/n for n in names]
    for n in names:assert hashlib.sha256((root/n).read_bytes()).hexdigest()==c['input_sha256'][n]
    p=json.loads(parent_path.read_bytes());j=json.loads(joint_path.read_bytes())
    pa=audit_parent(parent_path,parent_path);ja=audit_joint(joint_path,joint_path)
    sl,sh=map(F,p['inner_archimedean_high_interval']);tl,th=map(F,p['outer_archimedean_high_interval'])
    inner=F(p['inner_mass_upper']);outer=F(p['outer_mass_certificate']['physical_low_frequency_mass_upper'])
    norm=F(j['joint_prime_operator_norm_upper']);assert norm==F(15,8)
    direct=tl-(th-sl)*outer-(sh+F(27,5))*inner-F(p['pole_absolute_upper'])-norm
    assert direct==F(c['physical_unrounded_lower'])>F(c['physical_lower'])==F(77,100)
    assert F(c['logarithmic_lower'])==F(p['logarithmic_lower'])==F(9,100)
    assert direct-F(p['physical_unrounded_lower'])==F(c['exact_improvement'])
    return dict(certificate_sha256=hashlib.sha256(raw).hexdigest(),byte_identical_repeat=True,
        parent_complete_mass_and_endpoint_audit=pa,joint_exhaustive_path_audit=ja,
        independent_direct_lower_sum_verified=True,physical_lower='77/100',
        physical_unrounded_display=float(direct),whole_domain_positivity=False,f4_closed=False,lean_formalized=False)

if __name__=='__main__':
    import sys
    print(json.dumps(certificate(*sys.argv[1:]),indent=2))
