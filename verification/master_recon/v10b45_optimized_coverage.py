"""V10B45: reproduce custody and optimized row dominance from durable coordinates.
No original V10B19 ZIP custody, analytical attachment, or positivity adoption.
"""
from fractions import Fraction as Q
from math import comb, factorial
from pathlib import Path
import hashlib, json

here=Path(__file__).resolve().parent
d=json.loads((here/'v10b45_optimized_coordinates.json').read_text())
D=d['denominator']
V=d['legendre_numerators']
S=d['subtraction_numerators']
assert D==2**48
assert len(V)==len(S)==16
assert all(len(v)==160 for v in V) and all(len(s)==16 for s in S)
# Reproduce the full, previously authenticated derived V10B29 JSON.
P=[[2**k*sum(v[j]*(-1)**(j-k)*comb(j,k)*comb(j+k,k)
                 for j in range(k,160)) for k in range(160)] for v in V]
derived={'parent_sha256':d['parent_sha256'],'denominator':D,
         'coordinate':d['coordinate'],'physical_monomial_numerators':P,
         'legendre_numerators':V,'subtraction_numerators':S}
digest=hashlib.sha256((json.dumps(derived,indent=1)+'\n').encode()).hexdigest()
assert digest==d['derived_sha256']=='1fea00167929e3f5312c16dcd680154a34ead4b8934a520c7a23fd60e79e8c5f'
print('Derived V10B29 digest reproduced:',digest)
# Coordinate-scaled leading rows. For normalized constraint 15,
# higher odd terms have pairing ratio I_j/I_15, j>=17, and even terms vanish.
# Conditional on Rodrigues and w<=1/4:
# I_j/I_15 <= (1/16)^(j-15) * 15!/j! <= 1/256.
base=[Q(abs(V[i][i])-sum(abs(V[j][i]) for j in range(16) if i!=j),D)
      for i in range(16)]
high=[sum(abs(v[j]) for j in range(17,160,2)) for v in V]
assert min(base)>1
assert base[15]>2
assert sum(high)<7*D
coarse=Q(sum(high),256*D)
assert base[15]-coarse>2
assert min(base[:15]+[base[15]-coarse])>1
print('Leading rows 16/16 PASS; coarse high-row reserve:',float(coarse),
      'high-row margin:',float(base[15]-coarse))
# Reproduce the earlier tight finite pole-load row using both conventions.
def a(j,n):
    return sum((Q((2*j+1)*2**j*factorial(j+m),
                  8**(j+2*m)*factorial(m)*factorial(2*j+2*m+1))
                for m in range(n)),Q(0))
for n in (16,17):
    c=[a(j,n)/a(15,n) for j in range(15,34,2)]
    r=[sum((Q(31*v[j],(2*j+1)*D)*c[k]
            for k,j in enumerate(range(15,34,2))),Q(0)) for v in V]
    # L1(P_j)<=1 follows from diagonal orthogonality and Cauchy-Schwarz.
    reserve=Q(31*sum(sum(abs(x) for x in v) for v in V),D*10**25)
    highmargin=abs(r[15])-sum(abs(x) for x in r[:15])-reserve
    assert highmargin>Q(298,100)
    assert min(base[:15]+[highmargin])>Q(10675,10000)
    print(n,'terms: tight dominance PASS',float(highmargin),
          'minimum',float(min(base[:15]+[highmargin])))
