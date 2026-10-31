#!/usr/bin/env python3
"""NF414: rigorous SOURCE and seven-prime part of true continuous z at three original physical hotspot points.

Unchanged NF407 original 242 selected+four critical source, original NF408
continuous regularization and NF404 dyadic pole. 4096-bit Arb physical
source and real elementary functions, strict true log(n) seam decisions,
fully outward rational point enclosures + coefficient-radius charge.

This DOES NOT yet integrate remaining I0/I1 arch kernels and therefore
DOES NOT provide a true z pointwise enclosure, let alone cell sup or norm.
"""
import argparse,hashlib,json,sys
from pathlib import Path
from fractions import Fraction as F
from flint import arb,ctx
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
B=F(11,10)
X={3:F(7,20),6:F(9,10),7:F(26,25)}
WEIGHTS={2:2,3:3,4:2,5:5,7:7,8:2,9:3}
POLE=F(6677356497477490213,4611686018427387904)
def read(p):
 raw=Path(p).read_bytes()
 return json.loads(raw),hashlib.sha256(raw).hexdigest()
def dyad(v):
 n,e=int(v[0]),int(v[1])
 return F(n*(2**e)) if e>=0 else F(n,2**(-e))
def A(q):return arb(str(q))
def enclosed(z,n=60):
 m,r,e=z.mid_rad_10exp(n)
 # exact outward decimal interval, NOT rounded float display
 return [str(F((int(m)-int(r))*10**int(e)) if e>=0 else F(int(m)-int(r),10**(-int(e)))),
         str(F((int(m)+int(r))*10**int(e)) if e>=0 else F(int(m)+int(r),10**(-int(e))))]
def enlarge(interval,eps):
 return [str(F(interval[0])-eps),str(F(interval[1])+eps)]
def source_data(data):
 original={};pole=F(0);S0=F(0)
 def add(f,k,val):
  key=(f,k);original[key]=original.get(key,F(0))+val
 for (f,k),(mid,rad) in zip(data['original_selected_generator_node_orders'],
                            data['original_exact_native_raw_selected_coefficients_mid_radius']):
  val=dyad(mid);rr=abs(dyad(rad))
  if f=='pole':
   assert k is None
   pole+=val;S0+=rr
  else:
   f=F(f);add(f,k,val);S0+=rr*B**k
 for (mid,rad),shape in zip(data['original_exact_native_original_four_critical_coefficients_mid_radius'],
                             data['original_source_critical_sines_and_pole_coefficients']):
  alpha=dyad(mid);err=abs(dyad(rad))
  for f,q in zip(data['original_source_critical_sine_frequencies'],shape['sine_coefficients']):
   f=F(f);q=F(q);add(f,0,alpha*q);S0+=err*abs(q)
  q=F(shape['sinh_coefficient']);pole+=alpha*q;S0+=err*abs(q)
 assert len(data['original_selected_generator_node_orders'])==242
 assert len(data['original_source_critical_sine_frequencies'])==32
 assert S0<F(1,10**700),('coefficient radii too large',str(S0)[:150])
 return [(f,k,v) for (f,k),v in sorted(original.items()) if v],pole,S0
class Original:
 def __init__(self,s):
  self.terms,self.pole,self.S0=source_data(s)
  self.pi=arb.pi()
 def at(self,x):
  assert (A(-B)<x and x<A(B)) or x.overlaps(A(B)) or x.overlaps(A(-B)),('source eval outside physical support',str(x)[:90])
  z=A(self.pole)*(x/2).sinh()
  for f,k,v in self.terms:
   tr=A(2*f)*self.pi*x
   z+=A(v)*x**k*(tr.sin() if k%2==0 else tr.cos())
  return z
def main():
 p=argparse.ArgumentParser()
 p.add_argument('--source',default='notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
 p.add_argument('--seams',default='notes/data/provisional/NF406_original_prime_support_partition_exact.json')
 p.add_argument('--continuous',default='notes/data/provisional/NF408_original_continuous_action_exact.json')
 p.add_argument('--nf413',default='notes/data/provisional/NF413_original_full_246_source_curvature_native.json')
 p.add_argument('--output',required=True)
 args=p.parse_args()
 source,ssha=read(args.source);seams,seamsha=read(args.seams)
 continuous,csha=read(args.continuous);nf413,gsha=read(args.nf413)
 assert continuous['original_nf407_true_coefficient_native_sha256']==ssha
 assert continuous['original_nf406_seam_partition_sha256']==seamsha
 assert nf413['original_nf407_full_native_source_sha256']==ssha
 assert nf413['original_true_full_u4_second_derivative_L2_upper_integer']=='256'
 assert all(z['W_ODD_NEG']==z['RH']=='OPEN' for z in (source,seams,continuous,nf413))
 ctx.prec=4096
 src=Original(source)
 v=src.at(A(B))
 assert v<0
 centers=[]
 for cell,xrat in X.items():
  x=A(xrat);d=A(B)-x;t1=2*d;t2=2*(A(B)+x)
  u=src.at(x);L=(A(B)/d).log()
  pi=arb.pi()
  # NF408 exact stable continuous arch, before I0+I1.
  e=(-d/2).exp()
  phi=((d/A(B))*(d/4).cosh()/(d/4).sinh()).log()+2*e.atan()
  ztail=(-t2/4).exp()
  J2=2*(ztail.atanh()+ztail.atan())
  c0=(arb(1)/4).digamma()-pi.log()
  multiplier=c0+(J2+phi)/2
  arch_known=multiplier*u+L*(u-v)/2
  # All original 7 signed primes, true seam branches verified directly
  # on 4096-bit outward intervals for log(n), never inferred from decimal.
  primes=arb(0);entries=[];wtotal=arb(0)
  for n,power in WEIGHTS.items():
   h=arb(n).log()
   w=arb(power).log()/arb(n).sqrt()
   seam=abs(A(B)-h)
   assert x<seam or x>seam,('seam uncertainty',cell,n)
   if h<A(B) and x<seam:
    xp=x+h;xm=x-h
    assert xp<A(B) and xm>A(-B)
    part=-w*(src.at(xp)+src.at(xm))
    branch='both'
   elif h>A(B) and x<seam:
    part=arb(0);branch='neither'
   else:
    xm=x-h
    assert A(-B)<xm<A(B)
    part=-w*(src.at(xm)+v)
    branch='post-seam'
   primes+=part
   wtotal+=w
   entries.append({'n':n,'branch':branch,'prime_minus_r_native_arb':str(part)[:150]})
  finite=arch_known+primes-A(POLE)*(x/2).sinh()
  # Source uncertainty for *finite* part ONLY: each u-at-point and v
  # at most S0, |L|<10, |multiplier|<10, all weights sum<10.
  # So arch coefficient charge <20 S0; seven prime contributions
  # charge <20 S0. Use generous exact 100*S0.
  assert abs(L)<arb(10) and abs(multiplier)<arb(10)
  assert wtotal<arb(10)
  eps=100*src.S0
  arch_iv=enlarge(enclosed(arch_known),eps)
  prime_iv=enlarge(enclosed(primes),eps)
  finite_iv=enlarge(enclosed(finite),eps)
  assert F(finite_iv[0])<F(finite_iv[1])
  centers.append({
   'cell':cell,'rational_physical_x':str(xrat),
   'true_original_source_u_x_native':str(u)[:200],
   'true_original_source_endpoint_v_native':str(v)[:200],
   'NF408_arch_finite_without_I0_I1_source_paid_rational_interval':arch_iv,
   'seven_true_prime_continuous_contribution_source_paid_rational_interval':prime_iv,
   'original_z_finite_known_part_source_paid_rational_interval':finite_iv,
   'source_coefficient_uncertainty_rational_per_finite_total':str(eps),
   'all_seven_true_prime_branches':entries,
   'I0_I1_nested_arch_integrals_certified':False,
   'true_continuous_original_z_pointwise_certified':False
  })
 out={
  'pass':'NF414',
  'standing':'SOURCE-NATIVE RIGOROUS FINITE ORIGINAL z PIECES AT PHYSICAL CELL 6,3,7 RATIONAL INTERIORS; REMAINING ORIGINAL I0/I1 NOT CERTIFIED',
  'original_nf407_source_sha256':ssha,'original_nf406_seams_sha256':seamsha,
  'original_nf408_continuous_formula_sha256':csha,
  'original_nf413_source_curvature_sha256':gsha,
  'same_original_246_source_generator_custody':True,
  'original_physical_source_coefficient_uniform_error_exact':str(src.S0),
  'source_full_original_seven_prime_true_branch_pieces_certified':True,
  'arch_finite_continuous_part_at_three_hotspot_interiors_certified':True,
  'hotspot_points':centers,
  'original_remaining_arch_I0_I1_integrated':False,
  'actual_true_continuous_z_on_any_hotspot_cell_certified':False,
  'original_signed_z_principal_cross_certified':False,
  'full_original_centered_scalar_certified':False,
  'NF404_gate_decided':False,
  'new_signed_source_cells':0,'W_ODD_NEG':'OPEN','RH':'OPEN'
 }
 dst=Path(args.output);dst.parent.mkdir(parents=True,exist_ok=True)
 dst.write_text(json.dumps(out,indent=2)+'\n')
 for c in centers:
  print('NF414 cell',c['cell'],'physical x',c['rational_physical_x'],
        'original z KNOWN FINITE numerator',*[str(F(v).numerator)[:14] for v in c['original_z_finite_known_part_source_paid_rational_interval']],flush=True)
 print('NF414 original true remaining I0+I1 and whole scalar OPEN')
if __name__=='__main__':main()
