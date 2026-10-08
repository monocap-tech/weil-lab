"""Fresh complete ORIGINAL degree114 native row for NF71, no inverse claim."""
from pathlib import Path
import json,hashlib,sys
from certify_native_coupled_trial_cc3 import F,I,D,source,shifted_legendre,sqrt_rational,primitives,dot,bracket
def compact(x):
 previous=I.grid;I.grid=10**100
 try:z=I(x.lo,x.hi)
 finally:I.grid=previous
 assert z.lo<=x.lo<=x.hi<=z.hi
 return bracket(z)
def compute(cc9_path,old_path):
 cc=json.loads(Path(cc9_path).read_bytes());old=json.loads(Path(old_path).read_bytes())
 P=shifted_legendre(114);norms=[sqrt_rational(F(2*k+1)/D) for k in range(115)]
 nz=(norms[114].lo+norms[114].hi)/2
 p=[nz*x for x in P[114]]
 print('NF71 degree114 original source',file=sys.stderr,flush=True)
 regs,err,pi,geom=source(p,abs(nz),abs(nz)*114*115)
 assert err<F(1,10**44)
 degree=max(len(row) for row in regs)-1+114
 print('NF71 native primitives',degree,file=sys.stderr,flush=True)
 prim=[primitives(t,degree) for t in geom['cuts']]
 moments=[I(0) for _ in range(115)]
 harmonic=F(0);h1=[]
 for k in range(229):
  nn=k+1;harmonic+=F(1,nn)
  h1.append(I((F(1,nn*nn)+harmonic/nn)/2))
 for k in range(115):moments[k]+=dot(p,h1[k:])
 for panel,(a,b) in enumerate(zip(prim,prim[1:])):
  print('NF71 native panel',panel,file=sys.stderr,flush=True)
  powers=[(b[0][k+1]-a[0][k+1])/F(k+1) for k in range(degree+1)]
  powers=[I(max(F(0),x.lo),x.hi) for x in powers]
  for k in range(115):moments[k]+=dot(regs[panel],powers[k:])
 row=[]
 for k in range(112):
  value=I(0) if k%2 else D*norms[k]*dot(P[k],moments)+I(-err,err)
  row.append(value)
 v=list(map(F,old['rational_coefficient_witness']))
 uh=I(cc['constant_rational_scale'])*sqrt_rational(D)
 audits=[
 (sum((v[k]*row[k] for k in range(112)),I(0)),cc['mixed_trial_native'][1][0]),
 (uh*row[0],cc['mixed_trial_native'][1][1])]
 nz112=(norms[112].lo+norms[112].hi)/2
 mass114=D*nz*nz/F(229);mass112=D*nz112*nz112/F(225)
 self_native=D*nz*dot(P[114],moments)+I(-err*sqrt_rational(mass114).hi,err*sqrt_rational(mass114).hi)
 mixed=D*nz112*dot(P[112],moments)+I(-err*sqrt_rational(mass112).hi,err*sqrt_rational(mass112).hi)
 audits.extend([(self_native,cc['trial_native_gram'][1][1]),(mixed,cc['trial_native_gram'][0][1])])
 for got,saved in audits:
  l,h=map(F,saved);assert max(l,got.lo)<=min(h,got.hi)
 return {'passed':True,'aperture':'21/20','degree':114,'rational_normalization':str(nz),
 'mass_squared':str(mass114),'source_error':str(err),'native_projection_row':list(map(compact,row)),
 'self_native':compact(self_native),'mixed112_native':compact(mixed),'independent_cc9_overlap_checks':len(audits),
 'prime_powers':[2,3,4,5,7,8],'both_signed_poles_retained':True,'panels':13,
 'primitive_degree':degree,'interval_digits':800,'published_interval_digits':100,'outward_compact_inclusions_checked':114,'normalization_defined_rationally':True,
 'full_inverse_evaluated':False,'whole_aperture_positive':False,'lean_certified':False}
if __name__=='__main__':
 r=compute(*sys.argv[1:3]);Path(sys.argv[3]).write_text(json.dumps(r,indent=2)+'\n')
 print(json.dumps({'passed':r['passed'],'overlaps':r['independent_cc9_overlap_checks'],'primitive_degree':r['primitive_degree']},indent=2))
