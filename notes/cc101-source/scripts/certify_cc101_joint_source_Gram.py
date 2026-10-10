#!/usr/bin/env python3
"""Complete original joint tested/remainder projected source Gram.

All source correlations, whole-source analytic integrals, paid common-grid
coefficient rounding, and complete E112 projection. No quadrature.
"""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import argparse,base64,gzip,hashlib,json,sys,time
from materialize_cc101_joint_sources import run as materialize

PARENT='07d68dc04c8cccde065b3d20b6563b260625447e'
def read(p):
 b=Path(p).read_bytes()
 if p.endswith('.gz.b64'):b=gzip.decompress(base64.b64decode(b))
 return json.loads(b),hashlib.sha256(b).hexdigest()
def packed_conv(a,b):
 """Exact signed Kronecker substitution with an explicit no-carry bound."""
 am=max(map(abs,a),default=0);bm=max(map(abs,b),default=0)
 if not am or not bm:return [0]*(len(a)+len(b)-1)
 bits=am.bit_length()+bm.bit_length()+min(len(a),len(b)).bit_length()+2
 base=1<<bits;half=base>>1;mask=base-1
 assert min(len(a),len(b))*am*bm<half
 def pack(v):
  out=0
  for x in reversed(v):out=(out<<bits)+x
  return out
 value=pack(a)*pack(b);out=[]
 for k in range(len(a)+len(b)-1):
  digit=value&mask
  if digit>=half:digit-=base
  out.append(digit);value=(value-digit)>>bits
 assert value==0
 return out

def root(x):
 scale=10**160;v=F(isqrt(x.numerator*scale*scale//x.denominator)+1,scale);assert v*v>x;return v

def run(parity,count,output):
 start=time.time();upper=parity.upper();cp=f'notes/data/RPB108_DNE32_{upper}_NATIVE_REMAINDER_CERTIFICATE_20261009.json.gz.b64';packet_path=output+'.columns';materialize(cp,packet_path);packet,ph=read(packet_path);Path(packet_path).unlink();cert,ch=read(cp)
 cols=packet['columns'][:count];assert count==21 and len(cols)==count
 hp='scripts/dne23_dne16_source_input.py';helper=Path(hp).read_bytes();hh=hashlib.sha256(helper).hexdigest();assert hh=='e4539b941f3768f177a469c68f58d34b11d3ea863247c14c1a6a59d81b2f91d8'
 target='notes/data/RPB108_DNE15_NF24_TARGETS_20261009.json.gz.b64';prefix=helper.decode().split('\nps=[p]+')[0];assert prefix.count('range(116)')==1;prefix=prefix.replace('range(116)','range(181)')
 old=sys.argv;sys.argv=[hp,parity,target];d={}
 try:exec(compile(prefix,hp,'exec'),d)
 finally:sys.argv=old
 I,Z,A,bases=d['I'],d['Z'],d['A'],d['bases'];plus=d['plus'];low=0 if parity=='even' else 1;ps=[];us=[]
 for col in cols:
  p=[Z]*(max(col['indices'])+1);dp=[Z]*len(p)
  for n,c in zip(col['indices'],map(F,col['coefficients'])):
   p=plus(p,bases[n],I(c));dp=plus(dp,bases[n],I(c)*I(sum((F(1,k) for k in range(1,n+1)),F(0))))
  ps.append(p);us.append(d['make_u'](p,dp));print('block source',parity,len(ps),round(time.time()-start,1),flush=True)
 active=(2,3,4,5,7,8);ells={n:I(n).log() for n in active};cs={n:ells[2 if n in (4,8) else n]/I(n).sqrt() for n in active};cuts=[I(0),A]+[(ells[n]-A if ells[n].lo>A.hi else A-ells[n]) for n in active];cuts.sort(key=lambda x:x.lo);assert all(l.hi<h.lo for l,h in zip(cuts,cuts[1:]))
 maxn=110+low;maxdeg=max(max(map(len,ps))-1+maxn,max(map(len,us))+max(map(len,ps))-2);logs={}
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
   z=round((F(v.lo)+F(v.hi))/2*gridpoly);ints.append(z);delta=delta+I(max(abs(F(v.lo)-F(z,gridpoly)),abs(F(v.hi)-F(z,gridpoly))))*A**k
  return ints,delta
 log2=I(2).log();loga=A.log();L2=[]
 for k in range(0,2*max(map(len,ps))-1,2):
  m=k//2;dd=-d['pi']*d['pi']/3+4*I(sum((F(1,(2*j+1)**2) for j in range(m+1)),F(0)));psi=2*log2-2*I(sum((F(1,2*j+1) for j in range(m+1)),F(0)));L2.append(A**(k+1)/I(k+1)*((2*loga+psi)**2+dd))
 rounded=[roundpoly(p) for p in ps];rps=[x[0] for x in rounded];delta_ps=[x[1] for x in rounded];rpis=[[I(F(x,gridpoly)) for x in p] for p in rps]
 gram=[[Z for _ in cols] for _ in cols];moments=[[Z]*(maxn+1) for _ in cols];panel_errors=[[] for _ in cols]
 for i in range(count):
  for j in range(i,count):
   pp=packed_conv(rps[i],rps[j]);gram[i][j]=sum((I(F(pp[k],gridpoly**2))*L2[k//2]/4 for k in range(0,len(pp),2)),Z)
 shifts=[{(n,s):d['shift'](p,s*ells[n]) for n in active for s in (-1,1)} for p in ps]
 for panel,(l,h) in enumerate(zip(cuts,cuts[1:])):
  mid=(l+h)/2;pm=[(h**(k+1)-l**(k+1))/(k+1) for k in range(max(map(len,us))+maxn)];rus=[]
  for i,(p,u) in enumerate(zip(ps,us)):
   uj=list(u)
   for n in active:
    for s in (-1,1):
     pos=mid+s*ells[n]
     if pos.lo>-A.lo and pos.hi<A.lo:uj=plus(uj,shifts[i][n,s],-cs[n])
     else:assert pos.hi<=-A.hi or pos.lo>=A.hi
   ru,de=roundpoly(uj);rus.append(ru);panel_errors[i].append(str(de.hi));ui=[I(F(x,gridpoly)) for x in ru]
   for k in range(low,maxn+1,2):moments[i][k]=moments[i][k]+sum((v*pm[m+k] for m,v in enumerate(ui)),Z)-sum((v*(logs[m+k,panel+1]-logs[m+k,panel])/2 for m,v in enumerate(rpis[i])),Z)
  for i in range(count):
   for j in range(i,count):
    uu=packed_conv(rus[i],rus[j]);up=packed_conv(rus[i],rps[j]);pu=packed_conv(rus[j],rps[i]);assert len(up)==len(pu);mixed=[x+y for x,y in zip(up,pu)]
    gram[i][j]=gram[i][j]+d['polyint']([I(F(x,gridpoly**2)) for x in uu],l,h)-sum((I(F(x,2*gridpoly**2))*(logs[k,panel+1]-logs[k,panel]) for k,x in enumerate(mixed)),Z)
  print('block panel',parity,panel,round(time.time()-start,1),flush=True)
 coords=[[2*sum((x*moments[i][k] for k,x in enumerate(bases[n])),Z) for n in range(low,112,2)] for i in range(count)]
 grid=10**100
 def floor(x):return F((F(x)*grid).__floor__(),grid)
 def ceil(x):return -floor(-F(x))
 def box(v):return [str(floor(v.lo)),str(ceil(v.hi))]
 whole=[[None]*count for _ in cols]
 for i in range(count):
  for j in range(i,count):whole[i][j]=whole[j][i]=box(2*gram[i][j])
 cboxes=[[box(v) for v in row] for row in coords]
 # All load-bearing projection arithmetic and source payments are rational.
 projected=[[None]*count for _ in cols]
 for i in range(count):
  for j in range(i,count):
   lo,hi=map(F,whole[i][j])
   for a,b in zip(cboxes[i],cboxes[j]):
    al,ah=map(F,a);bl,bh=map(F,b);v=[al*bl,al*bh,ah*bl,ah*bh];lo-=max(v);hi-=min(v)
   projected[i][j]=projected[j][i]=[str(lo),str(hi)]
 eta=ceil((2*A*I(F(550,19))*I(F(106,125))**d['N']+I('3e-99')).hi);sqrta=ceil((2*A).sqrt().hi);lognorm=ceil((2*L2[0]).sqrt().hi)
 rounding=[ceil(sqrta*max(map(F,row))+F(de.hi)*lognorm/2) for row,de in zip(panel_errors,delta_ps)];errors=[ceil(eta*F(c['norm_upper'])+e) for c,e in zip(cols,rounding)];roots=[root(F(projected[i][i][1])) for i in range(count)];original=[[None]*count for _ in cols];payments=[[None]*count for _ in cols]
 for i in range(count):
  for j in range(count):
   e=ceil(errors[i]*roots[j]+errors[j]*roots[i]+errors[i]*errors[j]);lo,hi=map(F,projected[i][j]);original[i][j]=[str(lo-e),str(hi+e)];payments[i][j]=str(e)
 out=dict(stage='CC101',parent=PARENT,parity=parity,columns=list(range(count)),precision=d['P'],regular_order=d['N'],certificate_path=cp,certificate_sha256=ch,normalized_packet_sha256=ph,helper_sha256=hh,exact_masses=[c['exact_mass_squared'] for c in cols],physical_norm_upper=[c['norm_upper'] for c in cols],polynomial_rounding_grid_digits=250,logarithmic_polynomial_sup_error_upper=[str(x.hi) for x in delta_ps],panel_regular_polynomial_sup_error_upper=panel_errors,physical_interval_sqrt_upper=str(sqrta),complete_log_squared_norm=box(2*L2[0]),complete_log_norm_upper=str(lognorm),uniform_original_source_operator_error_upper=str(eta),polynomial_rounding_source_L2_error_upper=list(map(str,rounding)),source_L2_error_upper=list(map(str,errors)),complete_rounded_source_Gram=whole,retained_projection_indices=list(range(low,112,2)),retained_rounded_source_coordinates=cboxes,projected_rounded_source_Gram=projected,projected_source_norm_upper=list(map(str,roots)),source_Gram_error_payments=payments,original_projected_source_Gram=original,native_block=packet['native_matrix'],column_labels=packet['column_labels'],joint_packet_input_sha256=packet['input_sha256'],source_credit='11/100' if parity=='even' else '7/50',complete_original_source_action=True,exact_endpoint_logs=True,all_six_primes_both_orientations=True,half_translation_panels=7,sampled_quadrature=False,complete_joint_source_Gram_certified=True,complete_remaining_source_Gram_certified=False,whole_aperture_positive=False,RH=False,Lean=False)
 Path(output).write_text(json.dumps(out,indent=2)+'\n');print(parity,count,'complete coherent source block',round(time.time()-start,1),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('parity',choices=['even','odd']);p.add_argument('--count',type=int,default=21);p.add_argument('--output',required=True);a=p.parse_args();run(a.parity,a.count,a.output)
