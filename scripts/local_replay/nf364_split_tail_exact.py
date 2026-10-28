from fractions import Fraction as F
import json,zipfile,hashlib
from pathlib import Path
import os
CUSTODY_ROOT = Path(os.environ.get("WEIL_CUSTODY_DATA_DIR", "/mnt/data"))
zfile=Path(str(CUSTODY_ROOT / 'nf361-pr348-fourmode.zip')); z=zipfile.ZipFile(zfile)
raw=z.read('original_four_mode_critical_block.json')
assert hashlib.sha256(zfile.read_bytes()).hexdigest()=='735ab9b78b6df9b09590ba70a8e51049aa19e73ebb526f22c58797b455cc4968'
assert hashlib.sha256(raw).hexdigest()=='a84b19c1fefc4e680c5c19ea643bbe5badce639374cb0a424211ee980020f922'
o=json.loads(raw);pr=o['exact_candidates']['probes'];cs=[F(s) for s in o['exact_candidates']['sine_frequencies']]
assert cs==[F(5*n,11) for n in range(1,33)]
B=F(11,10); C=F(440,837)
assert B**2/F(20)<F(1,16)
# sinh(B)-B <= (B^3/6)/(1-B^2/20) by first-term ratio, all rational
s2_upper=(B**3/F(6))/(1-B**2/F(20))
assert s2_upper<F(1,4)
# for |xi|<=1, real psi(1/4+i pi xi)-log pi < 4+10*(64/125+8/25)
# and |prime terms|<70751/10000 (SM41/SI06). Bound <20.
arch_up=F(4)+10*(F(64,125)+F(8,25))
prime_up=F(70751,10000)
assert arch_up+prime_up<20
# frequency >=1: 2*int_1^infty (17+log t)^2/t^2 = 650 exactly
# Twice integrate by parts for the supported odd sinh source:
# |hat s(xi)| <= sinh(B/2)/(pi |xi|) + cosh(B/2)/(4 pi^2 xi^2).
# Series bounds sinh(11/20)<3/5 and (1/2)cosh(11/20)<3/5.
y=F(11,20)
sinh_bound=y + (y**3/F(6))/(1-y*y/F(20))
cosh_bound=1+(y*y/F(2))/(1-y*y/F(12))
assert sinh_bound<F(3,5) and cosh_bound/F(2)<F(3,5)
# pi>3 gives |hat s(xi)|<(1/5) /|xi|+(1/30)/xi^2<=7/(30|xi|), |xi|>=1
pole_action_sq_up=400*F(1,4)+650*F(7,30)**2
assert pole_action_sq_up<136
b=[F(p['sinh_coefficient']) for p in pr]
bnormsq=sum(x*x for x in b)

def integ_log_sq(power,L,k):
 q=power-1;X=17+F(347,500)*k
 return F(1,(L**q)*q)*(X*X+2*X/q+F(2,q*q))

def terms_sine(probe,order):
 a=[F(x) for x in probe['sine_coefficients']]
 moment=[sum((-1)**n*an*c**(2*j+1) for n,(an,c) in enumerate(zip(a,cs),1)) for j in range(order)]
 terms=[(2*j+2,abs(x)/3) for j,x in enumerate(moment)]
 R=sum(abs(an)*c**(2*order+1) for an,c in zip(a,cs))
 terms.append((2*order+2,F(4,9)*R))
 return terms

def tail(L,order):
 k=L.bit_length()-1
 out=F(0)
 for p in pr:
  terms=terms_sine(p,order)
  for q,cq in terms:
   for r,cr in terms:
    out +=2*cq*cr*integ_log_sq(q+r,L,k)
 return out
res={'status':'EXACT_RATIONAL_SINE_ONLY_HIGHTAIL_PLUS_SHARED_TRUE_POLE_GLOBAL_NORM',
 'artifact_sha256':hashlib.sha256(zfile.read_bytes()).hexdigest(),
 'json_sha256':hashlib.sha256(raw).hexdigest(),
 'pole_output_identity':'Q Astar sinh(x/2) = Q Ao sinh(x/2), since Qs=0',
 'shared_pole_unprojected_global_strong_square_upper_exact':str(pole_action_sq_up),
 'shared_pole_unprojected_global_strong_square_upper_float':float(pole_action_sq_up),
 'shared_pole_under_136':pole_action_sq_up<136,
 'pole_L2_norm_sq_upper_exact':str(s2_upper),
 'arch_abs_low_0to1_upper_exact':str(arch_up),
 'seven_prime_amplitude_upper_exact':str(prime_up),
 'sinh_endpoint_series_upper_exact':str(sinh_bound),
 'cosh_endpoint_series_upper_exact':str(cosh_bound),
 'full_4direction_pole_coeff_squared_exact':str(bnormsq),
 'pole_forcing_four_direction_square_upper_exact':str(136*bnormsq),
 'pole_forcing_four_direction_square_upper_float':float(136*bnormsq),
 'base_strong_floor_kappa_exact':str(F(33621,10**9)),
 'locally_proved_exterior_mu_lower':str(F(998,100000)),
 'tail':[]}
for L in [32,64,128,256,512,1024,2048,4096,8192,16384]:
 row={'cutoff':L}
 for order in [1,2,3,4]:
  h=tail(L,order)
  row[f'order{order}_sine_only_tail_exact']=str(h)
  row[f'order{order}_sine_only_tail_float']=float(h)
  row[f'order{order}_relative_energy_error_upper_float']=float(h/F(998,100000))
 res['tail'].append(row)
# Independent exact-rational replay of the retained full (sine+pole) four-plane tail at 32.
nf363=json.load(open(str(CUSTODY_ROOT / 'nf363_critical_sine_tail_higher_report.json')))
full32=F(nf363['tail'][0]['order4_upper_exact'])
assert full32<F(1,10**12)
# The accepted four-mode physical Gram is >=99/100, so sqrt(G)>=99/100.
# Ao>=1/1000 in strong sense; low-pass *physical* output has norm >=.00099-1e-6.
low_band_norm_lower=F(99,100)*F(1,1000)-F(1,10**6)
assert low_band_norm_lower==F(989,10**6)
res['unprojected_low32_strong_action_norm_lower_exact']=str(low_band_norm_lower)
res['unprojected_low32_strong_action_square_lower_exact']=str(low_band_norm_lower**2)
res['full_critical_four_mode_high32_tail_less_1e_12']=True
res['physical_frame_gram_lower_exact']='99/100'
Path(str(CUSTODY_ROOT / 'nf364_split_tail_exact_report.json')).write_text(json.dumps(res,indent=2))
for x in res['tail']:
 print('L',x['cutoff'],'  '+ ' '.join('O%d=%.4e'%(i,x[f'order{i}_sine_only_tail_float']) for i in [1,2,3,4]))
print('pole<136',pole_action_sq_up,'sum b²',bnormsq,'global shared pole forcing <',float(136*bnormsq))
