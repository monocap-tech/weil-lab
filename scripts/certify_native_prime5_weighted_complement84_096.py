"""Exact replacement of separated prime loss by the positive weighted Schur bound."""
import json,hashlib
from pathlib import Path
from fractions import Fraction as F
EXPECTED = {'RPB108_PRIME5_TWOBAND_COMPLEMENT84_096_CERTIFICATE_20261007.json': '13aaaac081b8eef76d6f9cb3d0bcfe1dcd33fcd80d5b65b9f4f565c10b7c5ca8', 'RPB108_PRIME5_WEIGHTED_SCHUR_096_CERTIFICATE_20261007.json': '73391b10f021a0eb4e93ca9d939c9583dd310ee62df577ba468e24fa849a1b43'}
EXPECTED = {'RPB108_PRIME5_TWOBAND_COMPLEMENT84_096_CERTIFICATE_20261007.json': 'be03cd04387d21cc38c6c91c0654a40728ac2e3c7de6a0b6e866e154c11e9cce', 'RPB108_PRIME5_WEIGHTED_POINTWISE_096_CERTIFICATE_20261007.json': 'fb6897a38884f488fc2e154ad21e9ab33328c12e246a7ec95d92647c57a0efa6'}
def certificate():
    root=Path(__file__).resolve().parents[1]/'notes/data'
    def read(n):
        p=root/n
        return p.read_bytes() if p.exists() else __import__('gzip').decompress(p.with_suffix('.json.gz').read_bytes())
    raw={n:read(n) for n in EXPECTED}
    assert {n:hashlib.sha256(v).hexdigest() for n,v in raw.items()}==EXPECTED
    parent,joint=[json.loads(raw[n]) for n in EXPECTED]
    assert parent['aperture']==joint['aperture']=='24/25'
    norm=F(joint['joint_prime_operator_norm_upper']);assert norm==F(882017,500000)
    assert F(joint['maximum_weighted_row_ratio'])<=norm and F(joint['weight_lower'])>0
    separated=F(parent['joint_prime24_operator_upper'])+F(parent['joint_prime35_operator_upper'])
    lower=F(parent['physical_unrounded_lower'])+separated-norm
    c=F(107,125);assert lower>c>0
    return dict(aperture='24/25',input_sha256=EXPECTED,physical_lower=str(c),
        physical_unrounded_lower=str(lower),physical_lower_display=float(lower),
        previous_separated_prime_upper=str(separated),combined_prime_upper=str(norm),
        exact_improvement=str(separated-norm),logarithmic_lower=parent['logarithmic_lower'],
        same_archimedean_mass_pole_and_projection=True,whole_domain_positivity=False,
        f4_entry_closed=False,lean_formalized=False)

if __name__=='__main__':print(json.dumps(certificate(),indent=2))
