"""Actual 48-source enclosures at aperture 3/4."""
import json
from certify_native_prime3_source36 import compute,quantize
from certify_native_legendre_small_window import F,I

def certificate():
    old=I.grid;I.grid=10**200
    try:return quantize(compute(degree=47,a=F(3,4)))
    finally:I.grid=old

if __name__=='__main__':
    print(json.dumps(certificate(),indent=2))
