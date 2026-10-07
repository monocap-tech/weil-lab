"""Exact replacement of separated prime loss by the combined tenth-power bound."""
import json,hashlib
from pathlib import Path
from fractions import Fraction as F
EXPECTED = {'RPB108_PRIME5_TWOBAND_COMPLEMENT84_095_CERTIFICATE_20261007.json': '13aaaac081b8eef76d6f9cb3d0bcfe1dcd33fcd80d5b65b9f4f565c10b7c5ca8', 'RPB108_PRIME5_JOINT_POWER10_095_CERTIFICATE_20261007.json': 'fb15f25db70b1720ed190a6fa2a7a5077217caa15eb81c0c78cbc43161d99223'}

def certificate():
    root=Path(__file__).resolve().parents[1]/'notes/data'
    def read(n):
        p=root/n
        return p.read_bytes() if p.exists() else __import__('gzip').decompress(p.with_suffix('.json.gz').read_bytes())
    raw={n:read(n) for n in EXPECTED}
    assert {n:hashlib.sha256(v).hexdigest() for n,v in raw.items()}==EXPECTED
    parent,joint=[json.loads(raw[n]) for n in EXPECTED]
    assert parent['aperture']==joint['aperture']=='19/20'
    norm=F(joint['joint_prime_operator_norm_upper']);assert norm==F(919,500)
    assert F(joint['maximum_tenth_power_row_mass_upper'])<norm**10
    separated=F(parent['joint_prime24_operator_upper'])+F(parent['joint_prime35_operator_upper'])
    lower=F(parent['physical_unrounded_lower'])+separated-norm
    c=F(399,500);assert lower>c>0
    return dict(aperture='19/20',input_sha256=EXPECTED,physical_lower=str(c),
        physical_unrounded_lower=str(lower),physical_lower_display=float(lower),
        previous_separated_prime_upper=str(separated),combined_prime_upper=str(norm),
        exact_improvement=str(separated-norm),logarithmic_lower=parent['logarithmic_lower'],
        same_archimedean_mass_pole_and_projection=True,whole_domain_positivity=False,
        f4_entry_closed=False,lean_formalized=False)

if __name__=='__main__':print(json.dumps(certificate(),indent=2))
