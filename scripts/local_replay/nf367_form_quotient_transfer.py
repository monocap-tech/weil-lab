#!/usr/bin/env python3
"""NF367 exact original PR355 native-interval transfer to Astar form topology.
Inherits native Arb accuracy and original signed exterior PSD; NOT a fresh
native computation, strong L2 action certificate or global sign theorem.
"""
import argparse
import hashlib
import io
import json
import zipfile
from fractions import Fraction as Q
from nf366_negative_quotient_transfer import dyad, fetch_archive, ZIP_SHA, JSON_SHA

def trace_upper(matrix):
    assert len(matrix)==4 and all(len(row)==4 for row in matrix)
    t=Q(0)
    for i in range(4):
        mid=dyad(matrix[i][i][0]);rad=dyad(matrix[i][i][1])
        assert rad>0 and mid>rad
        t+=mid+rad
    return t

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--offline',help='PR355 SHA-pinned original native archive ZIP')
    args=p.parse_args()
    blob=fetch_archive(args.offline)
    assert hashlib.sha256(blob).hexdigest()==ZIP_SHA
    with zipfile.ZipFile(io.BytesIO(blob)) as z:
        raw=z.read('original_exterior_scalar_floor_stop.json')
    assert hashlib.sha256(raw).hexdigest()==JSON_SHA
    d=json.loads(raw)
    assert d['selected_rank']==242 and d['existing_critical_witness_count']==4
    assert d['global_infinite_Schur_sign_certified'] is False
    S=trace_upper(d['physical_quotient_Gram_native'])
    C=trace_upper(d['actual_exterior_signed_Gram_native'])
    # PSD of both original complete physical/signed quotient Grams inherited
    # from PR355's native original exterior-form acceptance.
    E=C+17*S
    kappa=Q(33621,10**9)
    weak_signed_squared=2*(E+289*S/kappa)
    assert S < Q(1,2**604)
    assert E < Q(1,2**600)
    assert weak_signed_squared < Q(1,2**580)
    print('PASS NF367 original PR355 native archive+JSON SHA256')
    print('PASS source quotient Astar form energy < 2^-600 ||z||^2')
    print('PASS complete signed weak form-dual squared < 2^-580 ||z||^2')
    print('approx trace(S)=',float(S),'trace(C)=',float(C))
    print('approx energy bound=',float(E),'signed weak dual bound²=',float(weak_signed_squared))
    print('NO strong Astar*q, exterior solve, full Schur or RH sign conclusion')

if __name__=='__main__':
    main()
