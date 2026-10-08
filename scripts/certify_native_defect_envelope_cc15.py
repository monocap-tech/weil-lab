"""Original two-vector necessary gate for the full matrix defect envelope.

No ordinary-correlation or uniform mixed-row estimate is used. The original
C >= c and its entire sixteen-column native/action moments give a Loewner
inverse bound. A negative sufficient lower is not original negativity.
"""
import json,gzip,hashlib,time,sys
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import get_context
from certify_native_rich_action_cc14 import *
from certify_native_inverse_correlation_cc13 import solve,pivots
_JOB=None
def worker(panel):
 prim,regs,rc,rd,pc,pd,degree=_JOB
 a,b=prim[panel:panel+2]
 mm=[(b[0][k+1]-a[0][k+1])/(k+1) for k in range(degree+1)]
 lm=[b[1][k]-a[1][k] for k in range(degree+1)]
 mm=[I(max(F(0),x.lo),x.hi) for x in mm]
 lm=[I(max(F(0),x.lo),x.hi) for x in lm]
 slen=max(len(row) for rows in regs for row in rows);plen=143
 apps=[applied(rc[j][panel],mm,slen) for j in range(19)]
 la=[applied(rc[j][panel],lm,plen) for j in range(19)]
 pairs={}
 for i in range(19):
  for j in range(i,19):
   if i>=2 and j!=18:continue
   pairs[i,j]=bil(rc[i][panel],apps[j],rd[i][panel]*rd[j][panel])+bil(pc[i],la[j],pd[i]*rd[j][panel])+bil(pc[j],la[i],pd[j]*rd[i][panel])
 moments=[dot(regs[18][panel],mm[k:]) for k in range(112)]
 return panel,pairs,moments
def compute():
 start=time.monotonic();base=ROOT/'notes/data'
 names={'cc14':'RPB108_RICH_ACTION_CC14_CERTIFICATE_20261008.json.gz','cc13':'RPB108_INVERSE_CORRELATION_CC13_CERTIFICATE_20261008.json','cc9':'RPB108_TWO_RETAINED_BLOCK_CC9_CERTIFICATE_20261008.json','nf71':'RPB108_CORRELATED_WEAK_ROW_NF71_CERTIFICATE_20261008.json','saved':'RPB108_PRIME8_SCHUR112_105_CERTIFICATE_20261008.json','cc11':'RPB108_ODD_BATCH_CC11_CERTIFICATE_20261008.json'}
 rawin={k:(base/v).read_bytes() for k,v in names.items()}
 dat={k:json.loads(gzip.decompress(v) if k=='cc14' else v) for k,v in rawin.items()};d=dat['cc14'];old=dat['cc9'];nf=dat['nf71']
 v=list(map(F,dat['saved']['rational_coefficient_witness']))
 raw=gzip.decompress((base/'RPB108_PRIME8_MATRIX112_105_COMPACT80_20261008.json.gz').read_bytes())
 assert hashlib.sha256(raw).hexdigest()==dat['saved']['input_sha256']['native']==d['input_sha256']['native']
 nat=json.loads(raw);Q=[[None]*112 for _ in range(112)];pos=0
 for i in range(112):
  for j in range(i+1):
   Q[i][j]=Q[j][i]=I(*(F(int(x),10**80) for x in nat['lower_triangle_row_major'][pos]));pos+=1
 P=shifted_legendre(142);norms=[sqrt_rational(F(2*j+1)/D) for j in range(143)]
 weights=[v[j]*mid(norms[j]) if j%2==0 else F(0) for j in range(112)]
 ph=[sum((weights[j]*(P[j][k] if k<=j else 0) for j in range(112)),F(0)) for k in range(111)]
 nu=mid(norms[0]);nz=[mid(norms[n]) for n in DEGREES];n2=mid(norms[2])
 polys=[ph,[nu]]+[[nz[i]*x for x in P[n]] for i,n in enumerate(DEGREES)]+[[n2*x for x in P[2]]]
 m0=[sum(map(abs,weights),F(0)),abs(nu)]+list(map(abs,nz))+[n2]
 m1=[sum((abs(weights[j])*j*(j+1) for j in range(112)),F(0)),F(0)]+[abs(nz[i])*n*(n+1) for i,n in enumerate(DEGREES)]+[6*n2]
 regs=[];cachepins={}
 for i in range(18):
  path=base/f'RPB108_RICH_ACTION_CC14_SOURCE_CACHE_{i}.json.gz';b=path.read_bytes();cachepins[path.name]=hashlib.sha256(b).hexdigest();cached=json.loads(gzip.decompress(b))
  bind=hashlib.sha256(json.dumps([original_source_function_sha256,hashlib.sha256((ROOT/'scripts/native_rich_action_fast_source_cc14.py').read_bytes()).hexdigest(),list(map(str,polys[i])),str(m0[i]),str(m1[i]),str(I.grid)]).encode()).hexdigest()
  assert bind==cached['binding'];regs.append([[F(x) for x in row] for row in cached['regular_polynomials']])
  pi=I(*map(F,cached['pi']));cuts=[I(*map(F,x)) for x in cached['cuts']]
 print('CC15 new ORIGINAL degree-two source',flush=True)
 reg,e,pi,geom=fast_source(polys[18],m0[18],m1[18]);assert len(geom['cuts'])==14
 regs.append(reg);sr=constant_radius(pi);errors=[factored_error(p,m0[i],m1[i],regs[i],sr) for i,p in enumerate(polys)]
 errors[0]+=2*F(10**7)*sum((abs(v[j])*sqrt_rational(D/F(2*j+1)).hi/(2*I.grid) for j in range(0,112,2)),F(0))
 assert all(str(errors[i])==d['source_errors'][i] for i in range(18))
 plen=143;slen=max(len(row) for rows in regs for row in rows);degree=2*slen-2
 prim=[primitives(t,degree) for t in cuts];pc,pd=zip(*(ints(p) for p in polys));rc=[];rd=[]
 for rows in regs:
  a,b=zip(*(ints(row) for row in rows));rc.append(a);rd.append(b)
 h1=[];h2=[];harm=F(0);harm2=F(0)
 for k in range(2*plen-1):
  n=k+1;harm+=F(1,n);harm2+=F(1,n*n);h1.append(I((F(1,n*n)+harm/n)/2));h2.append(I((F(2,n**3)+(harm*harm+harm2)/n+2*harm/n**2+2*harm2/n)/4)-pi*pi/(12*n))
 h2=[I(max(F(0),x.lo),x.hi) for x in h2]
 pairs={}
 for j in range(19):
  app=applied(pc[j],h2,plen)
  for i in range(j+1):
   if i<2 or j==18:pairs[i,j]=bil(pc[i],app,pd[i]*pd[j])
 moments=[dot(polys[18],h1[k:]) for k in range(112)]
 global _JOB
 _JOB=(prim,regs,rc,rd,pc,pd,degree)
 with ProcessPoolExecutor(max_workers=4,mp_context=get_context('fork')) as pool:
  for panel,pg,pm in pool.map(worker,range(13)):
   for ij,x in pg.items():pairs[ij]+=x
   for k in range(112):moments[k]+=pm[k]
   print('CC15 entire mixed panel',panel,'seconds',round(time.monotonic()-start),flush=True)
 rows=[[sum((v[j]*Q[k][j] for j in range(0,112,2)),I(0)) for k in range(112)],[nu*sqrt_rational(D)*Q[k][0] for k in range(112)]]
 rows += [[I(*map(F,x)) for x in row] for row in d['complete_trial_native_rows']]
 # moments are monomial moments; the Legendre pairing needs its full slice.
 row2=[I(0) if k%2 else D*norms[k]*dot(P[k],moments)+I(-errors[18],errors[18]) for k in range(112)]
 normalization=D*n2/F(5)*norms[2];pairing_audits=0
 for k in range(0,112,2):
  y=normalization*Q[k][2];x=row2[k];assert max(x.lo,y.lo)<=min(x.hi,y.hi);pairing_audits+=1
 rows.append(row2);coarse=[F(10**8)*(1+x) for x in m0]
 for (i,j),x in list(pairs.items()):
  err=errors[i]*coarse[j]+errors[j]*coarse[i]+errors[i]*errors[j]
  pairs[i,j]=D*x+I(-err,err)-sum((rows[i][k]*rows[j][k] for k in range(112)),I(0))
 def gs(i,j):return pairs[min(i,j),max(i,j)]
 overlap=0
 for i in range(2):
  for j in range(i,2):
   y=I(*map(F,old['actual_retained_source_gram'][i][j]));x=gs(i,j)
   if i==j==0:y-=I(0,64*F(old['odd_original_witness_mass']))
   assert max(x.lo,y.lo)<=min(x.hi,y.hi);overlap+=1
 plane=[[F(x) for x in row] for row in nf['even_plane_deterministic_lower']];rho=plane[0][1]/plane[1][1]
 hm=sum((v[j]*v[j] for j in range(2,112,2)),F(0));alpha=v[2]/hm
 # Physical rational source matches the exactly even coefficient quotient;
 # finite norm rounding is paid against the complete source-map upper 8.
 vw=[v[j] if j%2==0 else F(0) for j in range(112)];vw[0]-=rho
 vr=list(map(F,dat['cc13']['even_test_vector_orthogonal_to_all_cc11_five']))
 charts=[[F(1),-rho,F(0)],[-alpha,alpha*v[0],F(1)]]
 idx=[0,1,18];GB=[[sum((charts[i][k]*gs(idx[k],idx[l])*charts[j][l] for k in range(3) for l in range(3)),I(0)) for j in range(2)] for i in range(2)]
 # Native orthonormal charts give exact physical source vectors. The tiny
 # discrepancy in rational polynomial normalizations is paid conservatively.
 source_rounding=[F(10**10)*(1+sum(map(abs,a),F(0)))/I.grid for a in charts]
 for i in range(2):
  for j in range(2):
   guard=source_rounding[i]*10**10+source_rounding[j]*10**10+source_rounding[i]*source_rounding[j]
   GB[i][j]+=I(-guard,guard)
 vectors=[vw,vr];A=[[sum((vectors[i][k]*Q[k][l]*vectors[j][l] for k in range(0,112,2) for l in range(0,112,2)),I(0)) for j in range(2)] for i in range(2)]
 G=[[I(*map(F,x)) for x in row] for row in d['complete_action_gram']];T=[[I(*map(F,x)) for x in row] for row in d['complete_trial_native_gram']]
 actioncross=[[sum((gs(z+2,idx[k])*charts[j][k] for k in range(3)),I(0))+I(-source_rounding[j]*10**10,source_rounding[j]*10**10) for j in range(2)] for z in range(16)]
 nativecross=[[sum((rows[z+2][k]*vectors[j][k] for k in range(112)),I(0)) for j in range(2)] for z in range(16)]
 c=F(699,1000);J=[[G[i][j]/c-T[i][j] for j in range(16)] for i in range(16)]
 H=[[actioncross[i][j]/c-nativecross[i][j] for j in range(2)] for i in range(16)]
 center=[[mid(x) for x in row] for row in J];rowradius=max(sum(((x.hi-x.lo)/2 for x in row),F(0)) for row in J)
 lower=[[center[i][j]-(rowradius if i==j else 0) for j in range(16)] for i in range(16)];pivots(lower)
 grid=10**100;liftcols=[solve(center,[mid(H[i][j]) for i in range(16)]) for j in range(2)]
 L=[[F((liftcols[j][i]*grid).__floor__(),grid) for j in range(2)] for i in range(16)]
 credit=[[sum((H[k][i]*L[k][j]+L[k][i]*H[k][j] for k in range(16)),I(0))-sum((L[k][i]*J[k][l]*L[l][j] for k in range(16) for l in range(16)),I(0)) for j in range(2)] for i in range(2)]
 envelope=[[A[i][j]-GB[i][j]/c+credit[i][j] for j in range(2)] for i in range(2)]
 det=envelope[0][0]*envelope[1][1]-envelope[0][1]*envelope[1][0]
 # Certify failure of the BEST matrix credit in this span, if a candidate
 # negative direction exists. A failed nonoptimal rational lift is weaker.
 failure=None
 if envelope[0][0].hi<0 or (det.hi<0 and envelope[1][1].lo>0):
  x=[F(1),F(0)] if envelope[0][0].hi<0 else [F(1),-mid(envelope[0][1])/mid(envelope[1][1])]
  hx=[sum((H[i][j]*x[j] for j in range(2)),I(0)) for i in range(16)]
  hc=[mid(y) for y in hx];hr=[(y.hi-y.lo)/2 for y in hx]
  invcols=[solve(lower,[F(i==j) for i in range(16)]) for j in range(16)]
  uppercredit=sum((invcols[j][i]*hc[i]*hc[j]+abs(invcols[j][i])*(abs(hc[i])*hr[j]+hr[i]*abs(hc[j])+hr[i]*hr[j]) for i in range(16) for j in range(16)),F(0))
  ideal=quad(A,x)-quad(GB,x)/c+uppercredit
  failure={'pair_direction':list(map(str,x)),'best_entire_span_credit_upper':str(uppercredit),'best_defect_envelope_direction_upper':str(ideal.hi),'strictly_negative':ideal.hi<0}
 result={'stage':'CC15 original matrix defect-envelope two-vector gate','aperture':'21/20','action_dimension':16,'source_pair_dimension':2,'all_panels':13,'all_prime_powers':[2,3,4,5,7,8],'both_signed_poles':True,'native_pairing_audits':pairing_audits,'cc9_retained_gram_overlaps':overlap,'integration_degree':degree,'complete_source_pair_gram':[[compact(x) for x in row] for row in GB],'original_native_pair':[[compact(x) for x in row] for row in A],'whole_mixed_action_source_cross':[[compact(x) for x in row] for row in actioncross],'whole_mixed_native_source_cross':[[compact(x) for x in row] for row in nativecross],'whole_defect_matrix':[[compact(x) for x in row] for row in J],'whole_defect_lower_ldl_pivots':list(map(str,pivots(lower))),'rational_matrix_lift':[[str(x) for x in row] for row in L],'entire_matrix_credit':[[compact(x) for x in row] for row in credit],'compatible_pair_schur_lower':[[compact(x) for x in row] for row in envelope],'pair_lower_determinant':compact(det),'normalization_source_rounding_guards':list(map(str,source_rounding)),'ell_historical':nf['even_weak_margin'],'test_mass':dat['cc13']['test_mass'],'whole_even54_sign':False,'whole_odd53_sign':False,'protected_codimension':107,'certified_aperture':'1','actual_inverse_evaluated':False,'nonstalling':False,'lean_certified':False,'input_sha256':{k:hashlib.sha256(b).hexdigest() for k,b in rawin.items()},'source_cache_sha256':cachepins,'producer_seconds':time.monotonic()-start,'displays':{'pair_lower':[[[float(x.lo),float(x.hi)] for x in row] for row in envelope],'determinant':[float(det.lo),float(det.hi)]}}
 result['classification']='B-conditional' if envelope[0][0].lo>0 and det.lo>0 else 'C' if envelope[0][0].hi<0 or det.hi<0 else 'inconclusive'
 result['best_span_obstruction']=failure
 result['full_block_checkpoint_closed']=False
 result['whole_even_obstruction_overcome']=False
 result['cc14_uniform_estimator_replaced_on_actual_pair']=True
 if result['classification']=='B-conditional':
  cross=max(abs(envelope[0][1].lo),abs(envelope[0][1].hi))
  result['pair_relative_schur_loss_upper']=str(cross*cross/(envelope[0][0].lo*envelope[1][1].lo))
  result['pair_completed_weak_margin_lower']=str(envelope[0][0].lo-cross*cross/envelope[1][1].lo)
 raw_certificate=(json.dumps(result,indent=2)+'\n').encode()
 (base/'RPB108_DEFECT_ENVELOPE_CC15_CERTIFICATE_20261008.json').write_bytes(raw_certificate)
 (base/'RPB108_DEFECT_ENVELOPE_CC15_CERTIFICATE_20261008.json.gz').write_bytes(gzip.compress(raw_certificate,mtime=0))
 print(json.dumps(result['displays'],indent=2));return result
if __name__=='__main__':compute()
