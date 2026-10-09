#!/usr/bin/env python3
"""Complete projected-source diagonal of a fixed DNE32 remainder column.

Complete original source moments; analytic logs and directed arithmetic.
The high probe is a physical normalized Legendre mode in F112.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,base64,gzip,hashlib,json,sys,time
from math import isqrt
from materialize_dne32_normalized_sources import run as materialize

def read(p):
 b=Path(p).read_bytes()
 if p.endswith('.gz.b64'):b=gzip.decompress(base64.b64decode(b))
 return json.loads(b),hashlib.sha256(b).hexdigest()

def compact(out):
 grid=10**100
 def ceil(x):return F((x*grid).__ceil__(),grid)
 e=ceil(F(out['uniform_original_source_operator_error_upper'])*F(out['norm_upper'])+F(out['polynomial_rounding_source_L2_error_upper']))
 out['coordinate_error_payment']=str(e)
 for x in out['high_source_probes']:
  lo,hi=map(F,x['truncated_coordinate']);lo-=e;hi+=e;x['original_coordinate']=[str(lo),str(hi)];x['squared_coordinate_lower']=str(max(F(0),lo,-hi)**2)
 total=sum(F(x['squared_coordinate_lower']) for x in out['high_source_probes']);out['finite_Bessel_source_squared_lower']=str(total)
 best=max(out['high_source_probes'],key=lambda x:F(x['squared_coordinate_lower']));out['strongest_single_probe']=best['index'];out['single_probe_failure_proved']=F(best['squared_coordinate_lower'])>F(out['proposed_source_budget_upper']);out['source_matrix_bound_failure_proved']=total>F(out['proposed_source_budget_upper']);out['uniform_floor_source_comparison_failure_proved']=total>F(out['uniform_floor_budget_upper'])
 lo,hi=map(F,out['complete_rounded_source_norm_squared'])
 for box in out['retained_rounded_source_coordinates']:
  a,b=map(F,box);lo-=max(a*a,b*b);hi-=F(0) if a<=0<=b else min(a*a,b*b)
 assert lo>0;out['projected_rounded_source_norm_squared']=[str(lo),str(hi)];scale=10**160
 root=F(isqrt(hi.numerator*scale*scale//hi.denominator)+1,scale);assert root*root>hi
 pay=ceil(2*e*root+e*e);out['projected_source_norm_upper']=str(root);out['source_Gram_error_payment']=str(pay);out['original_projected_source_norm_squared']=[str(lo-pay),str(hi+pay)]
 credit=F(out['source_credit']);native_lo=F(out['native_diagonal'][0]);out['source_diagonal_budget_passed']=hi+pay<credit/2*native_lo
 return out

def run(parity,column,output):
 start=time.time();upper=parity.upper();cp=f'notes/data/RPB108_DNE32_{upper}_NATIVE_REMAINDER_CERTIFICATE_20261009.json.gz.b64'
 packet_path=output+'.columns';materialize(cp,packet_path);packet,ph=read(packet_path);Path(packet_path).unlink();cert,ch=read(cp)
 col=packet['columns'][column];hp='scripts/dne23_dne16_source_input.py';helper=Path(hp).read_bytes();hh=hashlib.sha256(helper).hexdigest()
 assert hh=='e4539b941f3768f177a469c68f58d34b11d3ea863247c14c1a6a59d81b2f91d8'
 target='notes/data/RPB108_DNE15_NF24_TARGETS_20261009.json.gz.b64'
 prefix=helper.decode().split('\nps=[p]+')[0];assert prefix.count('range(116)')==1;prefix=prefix.replace('range(116)','range(181)')
 old=sys.argv;sys.argv=[hp,parity,target];d={}
 try:exec(compile(prefix,hp,'exec'),d)
 finally:sys.argv=old
 I,Z,A,bases=d['I'],d['Z'],d['A'],d['bases'];plus=d['plus'];low=0 if parity=='even' else 1
 p=[Z]*(max(col['indices'])+1);dp=[Z]*len(p)
 for n,c in zip(col['indices'],map(F,col['coefficients'])):
  p=plus(p,bases[n],I(c));dp=plus(dp,bases[n],I(c)*I(sum((F(1,k) for k in range(1,n+1)),F(0))))
 u=d['make_u'](p,dp);print('complete source',parity,'seconds',round(time.time()-start,1),flush=True)
 active=(2,3,4,5,7,8);ells={n:I(n).log() for n in active};cs={n:ells[2 if n in (4,8) else n]/I(n).sqrt() for n in active}
 cuts=[I(0),A]+[(ells[n]-A if ells[n].lo>A.hi else A-ells[n]) for n in active];cuts.sort(key=lambda x:x.lo)
 assert all(l.hi<h.lo for l,h in zip(cuts,cuts[1:]))
 maxn=180-low;maxdeg=max(len(p)-1+maxn,len(u)+len(p)-2);logs={}
 for j,x in enumerate(cuts):
  xp=[x**k for k in range(maxdeg+2)];vals=[Z]*(maxdeg+1)
  for sign in (-1,1):
   b=-sign*A;bp=[b**k for k in range(maxdeg+2)];y=A+sign*x;endpoint=y.lo<=0<=y.hi
   if endpoint:assert abs(y.lo)<d['D']('1e-170') and abs(y.hi)<d['D']('1e-170')
   ly=Z if endpoint else y.log();S=Z
   for k in range(maxdeg+1):
    S=b*S+xp[k+1]/(k+1);vals[k]=vals[k]+((Z if endpoint else (xp[k+1]-bp[k+1])*ly)-S)/(k+1)
  for k,v in enumerate(vals):logs[k,j]=v
 gridpoly=10**250
 def roundpoly(poly):
  ints=[];delta=Z
  for k,v in enumerate(poly):
   z=round((F(v.lo)+F(v.hi))/2*gridpoly);ints.append(z)
   delta=delta+I(max(abs(F(v.lo)-F(z,gridpoly)),abs(F(v.hi)-F(z,gridpoly))))*A**k
  return ints,delta
 def iconv(a,b):
  out=[0]*(len(a)+len(b)-1)
  for i,x in enumerate(a):
   if x:
    for j,y in enumerate(b):
     if y:out[i+j]+=x*y
  return out
 log2=I(2).log();loga=A.log();L2=[]
 for k in range(0,2*len(p)-1,2):
  m=k//2;dd=-d['pi']*d['pi']/3+4*I(sum((F(1,(2*j+1)**2) for j in range(m+1)),F(0)))
  psi=2*log2-2*I(sum((F(1,2*j+1) for j in range(m+1)),F(0)))
  L2.append(A**(k+1)/I(k+1)*((2*loga+psi)**2+dd))
 rp,delta_p=roundpoly(p);pp=iconv(rp,rp);gram=sum((I(F(pp[k],gridpoly**2))*L2[k//2]/4 for k in range(0,len(pp),2)),Z)
 rounded_p=[I(F(x,gridpoly)) for x in rp];max_delta_u=Z
 panel_rounding=[];moments=[Z]*(maxn+1);shifts={(n,s):d['shift'](p,s*ells[n]) for n in active for s in (-1,1)}
 for panel,(l,h) in enumerate(zip(cuts,cuts[1:])):
  mid=(l+h)/2;pm=[(h**(k+1)-l**(k+1))/(k+1) for k in range(len(u)+maxn)];uj=list(u)
  for n in active:
   for s in (-1,1):
    pos=mid+s*ells[n]
    if pos.lo>-A.lo and pos.hi<A.lo:uj=plus(uj,shifts[n,s],-cs[n])
    else:assert pos.hi<=-A.hi or pos.lo>=A.hi
  ru,delta_u=roundpoly(uj);panel_rounding.append(str(delta_u.hi));max_delta_u=I(0,max(max_delta_u.hi,delta_u.hi));rounded_u=[I(F(x,gridpoly)) for x in ru]
  uu=iconv(ru,ru);up=iconv(ru,rp)
  gram=gram+d['polyint']([I(F(x,gridpoly**2)) for x in uu],l,h)-sum((I(F(x,gridpoly**2))*(logs[k,panel+1]-logs[k,panel]) for k,x in enumerate(up)),Z)
  uj=rounded_u
  for k in range(low,maxn+1,2):
   moments[k]=moments[k]+sum((v*pm[m+k] for m,v in enumerate(uj)),Z)-sum((v*(logs[m+k,panel+1]-logs[m+k,panel])/2 for m,v in enumerate(rounded_p)),Z)
  print('source panel',parity,panel,'seconds',round(time.time()-start,1),flush=True)
 coords={n:2*sum((x*moments[k] for k,x in enumerate(bases[n])),Z) for n in range(low,maxn+1,2)}
 projected=2*gram-sum((coords[n]*coords[n] for n in range(low,112,2)),Z);assert projected.lo>0
 rounding=(2*A).sqrt()*max_delta_u+delta_p*(2*L2[0]).sqrt()/2
 err=2*A*I(F(550,19))*I(F(106,125))**d['N']+I('3e-99');pay=err*I(F(col['norm_upper']))+rounding
 source_gram_pay=2*pay*I(projected.hi).sqrt()+pay*pay
 original_projected=projected+I(source_gram_pay.hi.copy_negate(),source_gram_pay.hi)
 grid=10**100
 def floor(x):return F((F(x)*grid).__floor__(),grid)
 def ceil(x):return -floor(-F(x))
 pay=ceil(pay.hi);probes=[]
 for n in range(112+low,maxn+1,2):
  v=coords[n];tr=[floor(v.lo),ceil(v.hi)];box=[tr[0]-pay,tr[1]+pay]
  dist=max(F(0),box[0],-box[1]);probes.append(dict(index=n,truncated_coordinate=list(map(str,tr)),original_coordinate=list(map(str,box)),squared_coordinate_lower=str(dist*dist)))
 C=list(map(F,cert['congruence_matrix'][column][column]));credit=F(11,100) if parity=='even' else F(7,50);budget=credit/2*C[1]
 best=max(probes,key=lambda x:F(x['squared_coordinate_lower']));bessel=sum(F(x['squared_coordinate_lower']) for x in probes)
 out=dict(stage='DNE33',parent='c392b8eb26f54734d6bfcab77e3f6e85397fff9b',parity=parity,column=column,precision=d['P'],regular_order=d['N'],certificate_path=cp,certificate_sha256=ch,normalized_packet_sha256=ph,helper_sha256=hh,exact_mass_squared=col['exact_mass_squared'],norm_upper=col['norm_upper'],uniform_original_source_operator_error_upper=str(ceil(err.hi)),coordinate_error_payment=str(pay),native_diagonal=list(map(str,C)),source_credit=str(credit),proposed_source_budget_upper=str(budget),high_source_probes=probes,strongest_single_probe=best['index'],finite_Bessel_source_squared_lower=str(bessel),single_probe_failure_proved=F(best['squared_coordinate_lower'])>budget,source_matrix_bound_failure_proved=bessel>budget,polynomial_rounding_grid_digits=250,polynomial_rounding_source_L2_error_upper=str(ceil(rounding.hi)),projected_rounded_source_norm_squared=[str(floor(projected.lo)),str(ceil(projected.hi))],source_Gram_error_payment=str(ceil(source_gram_pay.hi)),original_projected_source_norm_squared=[str(floor(original_projected.lo)),str(ceil(original_projected.hi))],source_diagonal_budget_passed=F(original_projected.hi)<credit/2*C[0],uniform_high_floor='11/25',uniform_floor_budget_upper=str(F(11,25)*C[1]),uniform_floor_source_comparison_failure_proved=bessel>F(11,25)*C[1],complete_original_source_action=True,exact_endpoint_logs=True,all_six_primes_both_orientations=True,half_translation_panels=7,sampled_quadrature=False,complete_source_Gram_certified=False,whole_aperture_positive=False,RH=False,Lean=False)
 out.update(complete_rounded_source_norm_squared=[str(floor((2*gram).lo)),str(ceil((2*gram).hi))],retained_projection_indices=list(range(low,112,2)),retained_rounded_source_coordinates=[[str(floor(coords[n].lo)),str(ceil(coords[n].hi))] for n in range(low,112,2)],logarithmic_polynomial_sup_error_upper=str(delta_p.hi),panel_regular_polynomial_sup_error_upper=panel_rounding,physical_interval_sqrt_upper=str((2*A).sqrt().hi),complete_log_squared_norm=[str((2*L2[0]).lo),str((2*L2[0]).hi)],complete_log_norm_upper=str((2*L2[0]).sqrt().hi))
 out=compact(out)
 Path(output).write_text(json.dumps(out,indent=2)+'\n');print(parity,'complete source diagonal',list(map(float,original_projected.data())),'budget',float(budget),'pass',out['source_diagonal_budget_passed'],flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('parity',choices=['even','odd']);p.add_argument('--column',type=int,default=0);p.add_argument('--output',required=True);a=p.parse_args();run(a.parity,a.column,a.output)
