"""Exact physical trial Gram by monomials versus shifted Legendre orthogonality.
Usage: python v10b30_trial_gram.py FROZEN_TRANSFORMED_JSON OUTPUT_JSON
Checks the trial Gram only, not the action/residual Gram or the analytic identity.
"""
from fractions import Fraction as Q
from math import lcm
from pathlib import Path
import hashlib,json,sys
src=Path(sys.argv[1]); raw=src.read_bytes(); digest=hashlib.sha256(raw).hexdigest()
assert digest=='1fea00167929e3f5312c16dcd680154a34ead4b8934a520c7a23fd60e79e8c5f'
d=json.loads(raw); a=d['physical_monomial_numerators']; b=d['legendre_numerators']; den=d['denominator']; assert den==2**48
assert len(a)==len(b)==16 and all(len(x)==160 for x in a+b)
assert all(v%(2**k)==0 for row in a for k,v in enumerate(row))
c=[[v//2**k for k,v in enumerate(row)] for row in a]
L=lcm(*range(1,320)); W=[L//(k+1) for k in range(319)]
G=[[None]*16 for _ in range(16)]
for i in range(16):
 for j in range(i,16):
  v=[0]*319
  for k,x in enumerate(c[i]):
   for h,y in enumerate(c[j]):v[k+h]+=x*y
  mono=Q(sum(x*w for x,w in zip(v,W)),2*den**2*L)
  leg=sum((Q(x*y,2*den**2*(2*k+1)) for k,(x,y) in enumerate(zip(b[i],b[j]))),Q(0))
  assert mono==leg,(i,j)
  G[i][j]=G[j][i]=mono
assert all(0<G[i][i]<=1 for i in range(16))
trace=sum(G[i][i] for i in range(16)); assert trace<=Q(4481662,1000000)
out={'parent_sha256':digest,'entries_checked':136,'diagonal_bounds_pass':16,'trace':str(trace),'gram':[[str(x) for x in row] for row in G]}
Path(sys.argv[2]).write_text(json.dumps(out,indent=2)+'\n')
assert hashlib.sha256(Path(sys.argv[2]).read_bytes()).hexdigest()=='f4b5a8b470bac912d3b3b946b7ef35b6581263f29fcdea83c1d341538f65d900'
print('136/136 exact trial Gram comparisons PASS; 16/16 physical norm squares <= 1')
print('trace approximate',float(trace))
