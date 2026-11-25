#!/usr/bin/env python3
"""UOI046 finite arithmetic sanity check; NOT a proof of the infinite-stage theorem."""
from pathlib import Path
from fractions import Fraction
from decimal import Decimal, getcontext
import json, hashlib

base=Path(__file__).resolve().parent
orig=base.parent/'uoi044'/'UOI044_stage10_exact_arithmetic_receipt.json'
src=json.loads(orig.read_text(encoding='utf-8'))
b=src['matrix_upper_microgrid_int']; M=10**6
assert len(b)==10 and all(len(row)==10 for row in b)
assert all(b[j][k]==b[k][j] for j in range(10) for k in range(10))
assert all(b[j][j]==0 for j in range(10))
cols=[]
for k in range(1,10):
    value=sum((Fraction(b[j][k],M)**2 for j in range(k)),Fraction(0))
    ratio=value/(k+1)
    cols.append({'k':k,'sum_of_squared_upper_edges':str(value),
                 'ratio_to_k_plus_1':str(ratio),'ratio_approx':float(ratio)})
assert max(Fraction(x['ratio_to_k_plus_1']) for x in cols)<Fraction(1,25)
getcontext().prec=48
q=Decimal(8)
D=Decimal(1)/Decimal(1000)
low_const_without_Cpsi=(Decimal(8)*Decimal('3.14159265358979323846264338327950288419716939937510')*(Decimal(2)/Decimal(3)).sqrt()*D**Decimal('1.5')/(q**Decimal('.25')-1))
# A strong geometric sanity check of the frequency-slice exponent:
# sqrt(N) * delta_k^(3/2) * (sqrt(N))^(3/2)
# = delta^(3/2) * 8^(-3j/2) * 8^(-(k-j)/4).
for j in range(0,5):
 for k in range(j+1,10):
    d=k-j
    L=q**(Decimal(d)/2)*(D*q**(-k))**(Decimal(3)/2)*(q**(Decimal(d)/2))**(Decimal(3)/2)
    R=D**(Decimal(3)/2)*q**(-Decimal(3*j)/2-Decimal(d)/4)
    assert abs(L-R)/R < Decimal('1e-40')
out={'schema':'UOI046-finite-slice-sanity-v1','status':'finite exact-arithmetic checks only, NOT Lean and NOT infinite proof',
     'source_stage10_sha256':hashlib.sha256(orig.read_bytes()).hexdigest(),
     'stage10_squared_column_upper_bounds':cols,
     'max_column_ratio_to_k_plus_1':str(max(Fraction(x['ratio_to_k_plus_1']) for x in cols)),
     'small_low_band_convolution_coefficient_without_Cpsi':str(low_const_without_Cpsi),
     'infinite_main_theorem_checked':False,
     'unverified_analytic_inputs':['original signed Gamma localization','Brun–Titchmarsh short intervals','Chebyshev bound','functional-analytic completion']}
path=base/'UOI046_finite_sanity_receipt.json';path.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print('PASS: finite exact squared-column certificate, Fourier scaling, geometric identity')
print('Max finite column bound / (k+1):',out['max_column_ratio_to_k_plus_1'])
print('Output:',path)
