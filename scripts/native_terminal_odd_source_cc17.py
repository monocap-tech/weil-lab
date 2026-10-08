"""Original odd source with the parity rules of SOURCE112 engine105.

The reflected kernel-difference term changes sign and the pole term is
-Mplus*expplus+Mplus*expminus. All source terms and error bounds remain.
"""
import inspect
from fractions import Fraction as F
import certify_native_coupled_trial_cc3 as original
from native_rich_action_fast_source_cc14 import SOURCE,OLD,fast_left,controls as convolution_controls
REPLACEMENTS={
 'def source(':'def odd_source(',
 'All inputs here are even under t -> 1-t.':'All inputs here are odd under t -> 1-t.',
 'assert exact_reflect(p)==p':'assert exact_reflect(p)==[-x for x in p]',
 OLD:'    left=fast_left(p,A)\n',
 'add(left,exact_reflect(left))':'add(left,[-c for c in exact_reflect(left)])',
 'mp*(ep[k]+em[k])':'mp*(-ep[k]+em[k])',
}
CODE=SOURCE
for before,after in REPLACEMENTS.items():
 assert CODE.count(before)==1
 CODE=CODE.replace(before,after,1)
scope={**original.__dict__,'fast_left':fast_left}
exec(compile(CODE,__file__,'exec'),scope)
odd_source=scope['odd_source']

def controls():
 checks=convolution_controls()
 for n in (1,3,5,7):
  p=original.shifted_legendre(n)[n]
  assert original.exact_reflect(p)==[-x for x in p];checks+=1
  A=[F((-1)**k,k+1) for k in range(9)]
  slow=[F(0)]*(len(p)+len(A)-1)
  for j,c in enumerate(p):
   for k,a in enumerate(A):slow[j+k]+=c*a*original.regular_difference_factor(j,k)
  fast=fast_left(p,A)
  assert original.add(fast,[-x for x in original.exact_reflect(fast)])==original.add(slow,[-x for x in original.exact_reflect(slow)]);checks+=1
  ep=original.compose([F(1,k+1) for k in range(9)],F(-1,2));em=original.exact_reflect(ep)
  mp=original.D*sum((x/F(k+1) for k,x in enumerate(original.mul(p,ep))),F(0))
  mm=original.D*sum((x/F(k+1) for k,x in enumerate(original.mul(p,em))),F(0))
  assert mm==-mp;checks+=1
  poles=original.add([-mp*x for x in ep],[mp*x for x in em])
  assert original.exact_reflect(poles)==[-x for x in poles];checks+=1
 return checks

if __name__=='__main__':print({'exact_original_odd_source_controls':controls()})
