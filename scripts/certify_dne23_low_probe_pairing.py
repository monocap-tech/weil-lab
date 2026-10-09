#!/usr/bin/env python3
"""Fresh complete original unsquared low/probe pairing, outward source error."""
from pathlib import Path
from fractions import Fraction as F
import json,sys,argparse,hashlib,time
def run(parity,targets,trial,low,output):
 helper=Path(__file__).with_name('dne23_dne16_source_input.py');source=helper.read_bytes()
 assert hashlib.sha256(source).hexdigest()=='e4539b941f3768f177a469c68f58d34b11d3ea863247c14c1a6a59d81b2f91d8'
 assert hashlib.sha256(Path(trial).read_bytes()).hexdigest()=='7e94e46f1f14d8991d44bf1d54b6886f4b7da50a52a0e9ddf6e3c786fb0c3ccc'
 assert hashlib.sha256(Path(low).read_bytes()).hexdigest()=='ebca74e6237cf401b7480afe08b91caba2c3412dc08e55ac2ac55f1970d8f788'
 # Execute the exact source engine prefix through make_u's definition.
 # The later DNE16 three-source experiment is deliberately not executed.
 prefix=source.decode().split('\nps=[p]+')[0];assert prefix.endswith(' return u\n')
 oldargv=sys.argv;sys.argv=[str(helper),parity,targets];d={}
 try:exec(compile(prefix,str(helper),'exec'),d)
 finally:sys.argv=oldargv
 I=d['I'];Z=d['Z'];A=d['A'];bases=d['bases'];plus=d['plus'];conv=d['conv'];polyint=d['polyint'];N=d['N']
 START=0 if parity=='even' else 1
 t=next(r for r in json.loads(Path(trial).read_text())['parities'] if r['parity']==parity)
 coeff=list(map(F,t['fixed_rational_probe_coefficients']));mass=sum(v*v for v in coeff)
 assert mass==F(t['exact_physical_probe_mass']) and mass<F(1001,1000)**2
 probe=[Z]*112
 for n,c in zip(t['retained_indices'],coeff):probe=plus(probe,bases[n],I(c))
 p=bases[START];dp=[v*START for v in p];u=d['make_u'](p,dp)
 active=(2,3,4,5,7,8);ells={n:I(n).log() for n in active};cs={n:ells[2 if n in (4,8) else n]/I(n).sqrt() for n in active}
 cuts=[I(0),A]+[(ells[n]-A if ells[n].lo>A.hi else A-ells[n]) for n in active];cuts.sort(key=lambda x:x.lo)
 assert all(l.hi<h.lo for l,h in zip(cuts,cuts[1:]))
 maxdeg=len(p)+len(probe)-2
 # Full endpoint logarithm moments, including exact continuous endpoint.
 logprims={}
 for j,x in enumerate(cuts):
  xp=[x**k for k in range(maxdeg+2)];vals=[Z]*(maxdeg+1)
  for sign in (-1,1):
   b=-sign*A;bp=[b**k for k in range(maxdeg+2)];y=A+sign*x;endpoint=y.lo<=0<=y.hi
   if endpoint:assert abs(y.lo)<d['D']('1e-170') and abs(y.hi)<d['D']('1e-170')
   ly=Z if endpoint else y.log();S=Z
   for k in range(maxdeg+1):
    S=b*S+xp[k+1]/(k+1);v=Z if endpoint else (xp[k+1]-bp[k+1])*ly
    vals[k]=vals[k]+(v-S)/(k+1)
  for k,v in enumerate(vals):logprims[k,j]=v
 values=[Z,Z];tests=[probe,p];products=[conv(p,z) for z in tests];shifts={(n,s):d['shift'](p,s*ells[n]) for n in active for s in (-1,1)}
 for j,(l,h) in enumerate(zip(cuts,cuts[1:])):
  mid=(l+h)/2;uj=list(u)
  for n in active:
   for s in (-1,1):
    pos=mid+s*ells[n]
    if pos.lo>-A.lo and pos.hi<A.lo:uj=plus(uj,shifts[n,s],-cs[n])
    else:assert pos.hi<=-A.hi or pos.lo>=A.hi
  for i,test in enumerate(tests):
   singular=sum((v*(logprims[k,j+1]-logprims[k,j])/2 for k,v in enumerate(products[i])),Z)
   values[i]=values[i]+polyint(conv(uj,test),l,h)-singular
  print('low/probe panel',parity,j,flush=True)
 values=[2*v for v in values]
 delta=I(F(550,19))*I(F(106,125))**N;operr=2*A*delta+I('3e-99')
 native=[]
 for v,norm in zip(values,[I(F(1001,1000)),I(1)]):
  error=operr*norm;native.append(v+I(error.hi.copy_negate(),error.hi))
 row=next(r for r in json.loads(Path(low).read_text())['native_parity_gates'] if r['parity']==parity)
 lo,hi=map(F,row['native_Q_diagonal']);assert F(native[1].lo)<=hi and lo<=F(native[1].hi)
 out={'stage':'DNE23','parity':parity,'precision':d['P'],'regular_order':N,
  'helper_sha256':hashlib.sha256(source).hexdigest(),'fixed_trial_sha256':hashlib.sha256(Path(trial).read_bytes()).hexdigest(),
  'original_low_probe_pairing':native[0].data(),'truncated_low_probe_pairing':values[0].data(),
  'uniform_low_source_operator_error_upper':str(operr.hi),
  'independent_original_low_diagonal_replay':native[1].data(),'CC62_low_diagonal_overlap':True,
  'original_all_six_primes_both_orientations_paid':True,'exact_endpoint_log_paid':True,
  'half_translation_panels':len(cuts)-1,'fixed_probe_mass_squared':str(mass),
  'sampled_quadrature_used':False,'whole_aperture_positive':False,'RH':False,'Lean':False}
 Path(output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'parity':parity,'pairing':[float(v) for v in native[0].data()],'source_error':float(operr.hi)}))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('parity');p.add_argument('targets');p.add_argument('trial');p.add_argument('low');p.add_argument('--output',required=True);a=p.parse_args();run(a.parity,a.targets,a.trial,a.low,a.output)
