"""Actual 52-source enclosures at aperture 4/5."""
import json
from certify_native_prime3_source36 import compute,quantize
from certify_native_legendre_small_window import F,I

def certificate():
    old=I.grid;I.grid=10**200
    try:return quantize(compute(degree=51,a=F(4,5)))
    finally:I.grid=old

if __name__=='__main__':
    print(json.dumps(certificate(),indent=2))
