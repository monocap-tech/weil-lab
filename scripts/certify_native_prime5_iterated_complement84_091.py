"""Actual fresh 91/100 complement with its certified depth-three parameters."""
import json
from certify_native_legendre_small_window import F
from certify_native_prime5_iterated_preflight import certificate as preflight


def certificate():
    return preflight(F(91,100))


if __name__=='__main__':print(json.dumps(certificate(),indent=2))
