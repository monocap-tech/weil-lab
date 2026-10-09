#!/usr/bin/env python3
"""Exact scalar guards and transfer to NF24's exact H2 minimizers.
Analytic ||L_Q e_n||<200 for n112..115 is detailed in the DNE15 report.
C2<5 is the inherited CC60 original native bound.
"""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib,argparse,gzip,base64
from decimal import Decimal as D,Context,ROUND_HALF_EVEN
cx=Context(prec=100,rounding=ROUND_HALF_EVEN)
class Bound:
 def __init__(self,l,h):self.lo,self.hi=l,h
 def __truediv__(self,t):return Bound(self.lo/t.hi,self.hi/t.lo)
def dec(v):
 v=F(v);return cx.divide(D(v.numerator),D(v.denominator))
def log(v):
 z=dec(v);y=cx.ln(z);return Bound(F(cx.next_minus(y)),F(cx.next_plus(y)))
def sq(v):
 z=dec(v);y=cx.sqrt(z);return Bound(F(cx.next_minus(y)),F(cx.next_plus(y)))
A=F(53,50)
parser=argparse.ArgumentParser();parser.add_argument('--targets',required=True);parser.add_argument('--even',required=True);parser.add_argument('--odd',required=True)
args=parser.parse_args()

assert 2*A*F(550,19)<62
assert F(231,1)/(2*A)<121
assert sum((F(1,k) for k in range(1,116)),F(0))<6
assert log(2*A).lo>F(74,100) and log(2*A).hi<F(76,100)
assert 2*A*(4*F(26,100)**2+1)<4
assert log(7).hi<2 and log(2).lo>F(2,3)
for n in (2,3,4,5,7,8):
 assert (log(2 if n in (4,8) else n)/sq(n)).hi<1
assert 3+6+11+62+12+18<200
raw=Path(args.targets).read_bytes()
if args.targets.endswith('.gz.b64'):raw=gzip.decompress(base64.b64decode(raw))
assert hashlib.sha256(raw).hexdigest()=='6eee61fb4e58ac5be0e95f492f461b289da37ee13aeaa74bbf4acc06f6650c00'
targets=json.loads(raw);out=[]
for r in targets['authenticated_compensated_targets']:
 parity=r['parity'];c=json.loads(Path(args.even if parity=='even' else args.odd).read_text())
 delta=max(max(abs(F(v)-F(b)) for b in bounds) for v,bounds in zip(r['exact_rational_high_compensation'],r['true_H2_minimizer_enclosures']))
 assert delta<F(1,10**60)
 # two column source bound200 gives norm error <=400e-60.
 source_error=400*F(1,10**60)
 Pl,Pu=map(F,c['actual_full_F112_residual_square']);El,Eu=map(F,r['compensated_energy'])
 assert 0<Pl<Pu<F(1,10**30)
 # sqrt(Pu)<1e-15 makes this a rational norm-square perturbation guard.
 err2=source_error*(2*F(1,10**15)+source_error)
 assert err2<F(1,10**72)
 energy_error=5*2*F(1,10**120)
 assert energy_error<F(1,10**118)
 Pstar=(Pl-F(1,10**72),Pu+F(1,10**72))
 Estar=(El-F(1,10**118),Eu)
 ratio=(Pstar[0]/Estar[1],Pstar[1]/Estar[0])
 bounds=(F('0.35007'),F('0.35008')) if parity=='even' else (F('0.28028'),F('0.28029'))
 assert bounds[0]<ratio[0]<ratio[1]<bounds[1]
 assert Pstar[0]>F(207,1000)*Estar[1]
 out.append({'parity':parity,'high_coefficient_error_upper':str(delta),
 'conservative_source_L2_transfer_error':str(source_error),
 'source_square_transfer_error_upper':'1/10^72','energy_transfer_error_upper':'1/10^118',
 'exact_H2_residual_square_over_S2':[str(v) for v in ratio],
 'display_ratio_bounds':[str(v) for v in bounds],
 'exact_H2_scalar_floor_gate_failure_proved':True})
print(json.dumps({'stage':'DNE15','source_column_norm_bound':200,'CC60_C2_upper':5,'targets':out,'full_inverse_response_evaluated':False},indent=2))
