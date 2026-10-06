#!/usr/bin/env python3
"""Tighten norm conversion using inherited certified Schur inputs; no Gram rerun."""
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

PINNED = {
    'notes/REFLECTED_PACKET_BRIDGE_108_PRIME5_84_SCHUR_081_20261005.md':
        '6669733a39388821f3d5c26eeec933f454c6ea24',
    'notes/REFLECTED_PACKET_BRIDGE_108_ENDPOINT_BRIDGE_AUDIT_20261005.md':
        '5202104f002a673ced842b655a4d222353e7d574',
    'notes/data/RPB108_PRIME5_84_SCHUR_081_VALIDATION_20261005.json':
        '95a36b76f5aa017cf3a8726658e9848d90eb56e2',
}


def conversion(tau, c, lift):
    if tau <= 0 or c <= 0 or lift < 0:
        raise ValueError('Invalid coercivity or lift input')
    mu = tau*c/(tau+c*(1+lift*lift))
    a = tau-mu*(1+lift*lift)
    b = -mu*lift
    d = c-mu
    determinant = a*d-b*b
    assert a >= 0 and d >= 0 and determinant == mu*mu > 0
    return mu, (a, b, d), determinant


def certificate(root):
    custody = {}
    texts = {}
    for name, expected in PINNED.items():
        raw = (root/name).read_bytes()
        blob = hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        if blob != expected:
            raise ValueError('Pinned inherited input changed: '+name)
        custody[name] = {'git_blob_sha': blob, 'sha256': hashlib.sha256(raw).hexdigest()}
        texts[name] = raw.decode()
    audit = json.loads(texts['notes/data/RPB108_PRIME5_84_SCHUR_081_VALIDATION_20261005.json'])
    assert audit['whole_domain_positivity'] and audit['sign_and_lift_margin_fields_verified']
    assert audit['certificate_sha256'] == '32f664f3e4a686dd220755c18f8aa38b790955b9c6b1a08e99fb8c5ac3a1615c'
    tau, c, lift = F(1, 10**29), F(51, 100), F(10)
    mu, matrix, determinant = conversion(tau, c, lift)
    old = F(1, 202*10**29)
    assert old < mu < 2*old
    kappa = mu/(10*(mu+23))
    old_kappa = F(1, 10+46460*10**29)
    assert old_kappa < kappa < 2*old_kappa
    weight = mu/(mu+23)
    assert (1-weight)*mu-weight*23 == 0
    assert weight/10 == kappa
    oversized = 2*mu
    broken = (tau-oversized*(1+lift*lift))*(c-oversized)-(oversized*lift)**2
    assert broken < 0
    controls = 0
    for t in (F(1,1000), F(1,10), F(2)):
        for comp in (F(1,2), F(1), F(3)):
            for ell in (F(0), F(1,2), F(2), F(10)):
                conversion(t, comp, ell)
                controls += 1
    return {
        'status': 'stronger whole-domain norm conversion from inherited certified Schur inputs',
        'aperture': '81/100', 'inherited_input_custody': custody,
        'inherited_full_gram_sha256': audit['certificate_sha256'],
        'full_gram_retrieved_or_recomputed_this_pass': False,
        'corrected_schur_margin': str(tau), 'physical_complement_lower': str(c),
        'lift_operator_norm_upper': str(lift),
        'whole_domain_physical_coercivity_lower': str(mu),
        'previous_whole_domain_physical_coercivity_lower': str(old),
        'physical_improvement_factor': str(mu/old),
        'two_by_two_psd_entries': list(map(str, matrix)),
        'two_by_two_determinant': str(determinant),
        'logarithmic_coercivity_lower': str(kappa),
        'previous_logarithmic_coercivity_lower': str(old_kappa),
        'logarithmic_mass_loss_ceiling': 23, 'logarithmic_blend_weight': str(weight),
        'generic_rational_conversion_controls': controls,
        'doubled_conversion_control_rejected': True,
        'doubled_conversion_control_determinant': str(broken),
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'corrected_schur_matrix_margin_updated': False,
        'finite_restriction_margin_used': False, 'numerical_aperture_frontier': '81/100',
        'global_endpoint_excluded': False, 'f4_entry_closed': False,
        'full_transport_closed': False, 'lean_formalized': False,
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    result = certificate(args.root)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ('whole_domain_physical_coercivity_lower',
                                           'logarithmic_coercivity_lower',
                                           'generic_rational_conversion_controls')}))
