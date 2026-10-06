"""Sharper rational constant from the unchanged exact 22/25 integrated bound."""
import json
from certify_native_legendre_small_window import F
from certify_native_prime5_integrated_complement84_088 import certificate as integrated_certificate


def certificate():
    result=integrated_certificate()
    assert F(result['physical_unrounded_lower'])>F(619,1000)
    result.update(status='certified refined actual 84-moment complement at 22/25',
        physical_lower='619/1000',complement_inverse_factor='1000/619',
        original_integrated_physical_lower_preserved='3/5',
        same_integrated_mass_and_cutoff=True)
    return result


if __name__=='__main__':print(json.dumps(certificate(),indent=2))
