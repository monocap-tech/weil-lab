"""Complete original even56 matrix defect envelope, at fixed CC14 Z16.

All896 source/action crosses are integrated. The full archived original
source/Gram112 inputs are decoded, authenticated and their errors retained.
No full complement inverse or odd-sector sign is presumed.
"""
import json,gzip,hashlib,time,sys
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import get_context
from certify_native_rich_action_cc14 import *
EVEN=list(range(0,112,2));_JOB=None
def panel_worker_full(panel):
 prim,oldregs,zregs,zpc,zpd,zrc,zrd,oldpc,degree=_JOB
 a,b=prim[panel:panel+2]
 mm=[(b[0][k+1]-a[0][k+1])/(k+1) for k in range(degree+1)]
 lm=[b[1][k]-a[1][k] for k in range(degree+1)]
 mm=[I(max(F(0),x.lo),x.hi) for x in mm];lm=[I(max(F(0),x.lo),x.hi) for x in lm]
 oldlength=max(len(row) for rows in oldregs for row in rows)
 apps=[applied(zrc[j][panel],mm,oldlength) for j in range(16)]
 za=[applied(zrc[j][panel],lm,112) for j in range(16)]
 oa=[applied(oldregs[i][panel],lm,143) for i in range(56)]
 out=[[I(0) for _ in range(56)] for _ in range(16)]
 den=10**40
 for j in range(16):
  for i in range(56):
   out[j][i]=bil(oldregs[i][panel],apps[j],den*zrd[j][panel])+bil(oldpc[i],za[j],zrd[j][panel])+bil(zpc[j],oa[i],zpd[j]*den)
 return panel,out
def interval_ldl(A):
 A=[[I(x) if not isinstance(x,I) else x for x in row] for row in A];n=len(A);L=[[I(int(i==j)) for j in range(n)] for i in range(n)];ps=[]
 for k in range(n):
  p=A[k][k]
  if p.lo<=0:return ps,L,k,p
  ps.append(p)
  for i in range(k+1,n):L[i][k]=A[i][k]/p
  for i in range(k+1,n):
   for j in range(i,n):A[i][j]=A[j][i]=A[i][j]-A[i][k]*A[k][j]/p
 return ps,L,None,None
def correlated_chart(A,GB,H,L,J,chart,delta,c,weak_cross=None):
 # Apply the SAME exact chart to sources and lifts BEFORE their products.
 # Congruencing independent interval entries of the already expanded credit
 # would charge cancelling weak-column errors independently at scale10^32.
 n=56;basis=[0]+list(range(2,56));v=chart[0]
 def congruence(M):
  out=[[I(0) for _ in range(n)] for _ in range(n)];out[0][0]=quad(M,v)
  for i,k in enumerate(basis,1):
   out[0][i]=out[i][0]=sum((v[j]*M[j][k] for j in range(n)),I(0))
   for j,l in enumerate(basis,1):out[i][j]=M[k][l]
  return out
 AC=congruence(A);GC=congruence(GB)
 HC=[[sum((H[i][j]*v[j] for j in range(n)),I(0))]+[H[i][k] for k in basis] for i in range(16)]
 if weak_cross is not None:
  for i in range(16):
   a,b=HC[i][0],weak_cross[i]*10**16
   HC[i][0]=I(max(a.lo,b.lo),min(a.hi,b.hi))
 LC=[[sum((L[i][j]*v[j] for j in range(n)),F(0))]+[L[i][k] for k in basis] for i in range(16)]
 JL=[[sum((J[i][k]*LC[k][j] for k in range(16)),I(0)) for j in range(n)] for i in range(16)]
 SC=[[AC[i][j]-GC[i][j]/c+sum((HC[k][i]*LC[k][j]+LC[k][i]*HC[k][j]-LC[k][i]*JL[k][j] for k in range(16)),I(0))-delta/c*sum((chart[i][k]*chart[j][k] for k in range(n)),F(0)) for j in range(n)] for i in range(n)]
 for i in range(n):
  for j in range(i+1,n):
   a,b=SC[i][j],SC[j][i];SC[i][j]=SC[j][i]=I(min(a.lo,b.lo),max(a.hi,b.hi))
 return SC
def reassemble(d):
 # Canonical consumer-format assembly pays compact100 endpoint rounding.
 # It can resume after source integration without repeating any panel.
 base=ROOT/'notes/data';prior=json.loads(gzip.decompress((base/'RPB108_DEFECT_ENVELOPE_CC15_CERTIFICATE_20261008.json.gz').read_bytes()))
 mat=lambda x:[[I(*map(F,y)) for y in row] for row in x]
 A=mat(d['whole_even_native_matrix']);GB=mat(d['whole_even_source_gram_surrogate']);H=mat(d['whole_defect_source_cross']);L=[[F(x) for x in row] for row in d['rational_complete_matrix_lift']];J=mat(prior['whole_defect_matrix']);chart=[[F(x) for x in row] for row in d['original_even_coordinate_chart']]
 # Replace the inherited coarse product error by an independently justified
 # full physical source-norm payment. Raw integration/projection intervals
 # and compact endpoint rounding remain, since only the explicit symmetric
 # source-error allowance is removed and replaced.
 z=json.loads(gzip.decompress((base/'RPB108_RICH_ACTION_CC14_CERTIFICATE_20261008.json.gz').read_bytes()));s=json.loads(gzip.decompress((base/'RPB108_PRIME8_SOURCE112_105_CERTIFICATE_20261008.json.gz').read_bytes()))
 zr=mat(z['complete_trial_native_rows']);GZ=mat(z['complete_action_gram']);cross=mat(d['whole_action_retained_source_cross'])
 newerrors=[]
 for i in range(16):
  zfull=sqrt_rational(GZ[i][i].hi+sum((max(abs(x.lo),abs(x.hi))**2 for x in zr[i]),F(0))).hi
  er=[]
  for j,k in enumerate(EVEN):
   oldeta=F(s['rows'][k]['normalized_uniform_error']);zeta=F(z['source_errors'][i+2])
   oldproxy=sqrt_rational(GB[j][j].hi).hi+sqrt_rational(sum((max(abs(A[l][j].lo),abs(A[l][j].hi))**2 for l in range(56)),F(0))).hi+oldeta
   olderror=oldeta*10**12+zeta*10**12+oldeta*zeta
   newerror=oldeta*zfull+zeta*oldproxy
   if not d.get('actual_full_source_norm_error_payment',False):
    x=cross[i][j];cross[i][j]=I(x.lo+olderror-newerror,x.hi-olderror+newerror)
   er.append(str(F((newerror*10**100).__ceil__(),10**100)))
  newerrors.append(er)
 H=[[cross[i][j]/F(699,1000)-zr[i][EVEN[j]] for j in range(56)] for i in range(16)]
 ac=mat(prior['whole_mixed_action_source_cross']);nc=mat(prior['whole_mixed_native_source_cross']);weak=[ac[i][0]/F(699,1000)-nc[i][0] for i in range(16)]
 SC=correlated_chart(A,GB,H,L,J,chart,F(d['complete_source_operator_error_paid']),F(699,1000),weak)
 grid=10**100;weights=[F(1,10**20)]+[F(1)]*55
 payments=[sum(((SC[i][j].hi-SC[i][j].lo)/2*weights[j]/weights[i] for j in range(56)),F(0)) for i in range(56)]
 payments=[F((p*grid).__ceil__()+56,grid) for p in payments]
 K=[[F((mid(SC[i][j])*grid).__floor__(),grid)-(payments[i] if i==j else 0) for j in range(56)] for i in range(56)]
 ps,ldl,failed,bad=interval_ldl(K)
 d.update({'whole_action_retained_source_cross':[[compact(x) for x in row] for row in cross],'whole_defect_source_cross':[[compact(x) for x in row] for row in H],'actual_full_source_norm_error_payment':True,'actual_cross_source_error_payments':newerrors,'cc15_precise_weak_cross_intersection_used':True,'whole_chart_schur_lower':[[compact(x) for x in row] for row in SC],'chart_whole_interval_row_payment':str(max(payments)),'weighted_interval_diagonal_payments':list(map(str,payments)),'interval_row_weights':list(map(str,weights)),'whole_chart_deterministic_lower':[[str(x) for x in row] for row in K],'interval_ldl_pivots':list(map(compact,ps)),'failed_pivot_index':failed,'failed_pivot_interval':None if bad is None else compact(bad),'whole_even56_lower_passed':failed is None,'source_coordinate_chart_applied_before_all_credit_products':True,'compact100_input_endpoint_errors_paid':True})
 d.pop('whole_even_schur_lower',None)
 return d
def compute():
 start=time.monotonic();base=ROOT/'notes/data'
 paths={'source':'RPB108_PRIME8_SOURCE112_105_CERTIFICATE_20261008.json.gz','gram':'RPB108_PRIME8_GRAM112_105_CERTIFICATE_20261008.json.gz','native':'RPB108_PRIME8_MATRIX112_105_COMPACT80_20261008.json.gz','cc14':'RPB108_RICH_ACTION_CC14_CERTIFICATE_20261008.json.gz','cc15':'RPB108_DEFECT_ENVELOPE_CC15_CERTIFICATE_20261008.json.gz','saved':'RPB108_PRIME8_SCHUR112_105_CERTIFICATE_20261008.json','cc11':'RPB108_ODD_BATCH_CC11_CERTIFICATE_20261008.json'}
 raw={k:(base/v).read_bytes() for k,v in paths.items()};decoded={k:gzip.decompress(b) if paths[k].endswith('.gz') else b for k,b in raw.items()};dat={k:json.loads(b) for k,b in decoded.items()}
 s,g,n,z=dat['source'],dat['gram'],dat['native'],dat['cc14']
 assert hashlib.sha256(decoded['source']).hexdigest()==g['source_certificate_sha256']
 assert hashlib.sha256(decoded['native']).hexdigest()==g['native_certificate_sha256']==z['input_sha256']['native']
 assert s['aperture']==g['aperture']==n['aperture']=='21/20' and g['panel_count']==13 and g['all_mixed_terms_retained']
 Q=[[None]*112 for _ in range(112)];pos=0
 for i in range(112):
  for j in range(i+1):Q[i][j]=Q[j][i]=I(*(F(int(x),10**80) for x in n['lower_triangle_row_major'][pos]));pos+=1
 # Actual parity is exact; proxy parity is not used as an unproved identity.
 assert len(s['rows'])==112 and g['physical_degrees']==list(range(112))
 P=shifted_legendre(142);norms=[sqrt_rational(F(2*j+1)/D) for j in range(143)]
 oldpc=[[int(x) for x in P[i]] for i in EVEN]
 oldregs=[[row['panels'][p]['low_degree_numerators']+row['common_high_degree_numerators'] for p in range(13)] for row in (s['rows'][i] for i in EVEN)]
 assert s['coefficient_grid_digits']==40 and all(len(row)<=472 for panels in oldregs for row in panels)
 zregs=[];zpoly=[];cachepins={};m0=[];m1=[]
 for j,degree in enumerate(DEGREES):
  nz=mid(norms[degree]);p=[nz*x for x in P[degree]];zpoly.append(p);m0.append(nz);m1.append(nz*degree*(degree+1))
  path=base/f'RPB108_RICH_ACTION_CC14_SOURCE_CACHE_{j+2}.json.gz';b=path.read_bytes();cachepins[path.name]=hashlib.sha256(b).hexdigest();d=json.loads(gzip.decompress(b))
  bind=hashlib.sha256(json.dumps([original_source_function_sha256,hashlib.sha256((ROOT/'scripts/native_rich_action_fast_source_cc14.py').read_bytes()).hexdigest(),list(map(str,p)),str(m0[-1]),str(m1[-1]),str(I.grid)]).encode()).hexdigest();assert d['binding']==bind
  zregs.append([[F(x) for x in row] for row in d['regular_polynomials']]);pi=I(*map(F,d['pi']));cuts=[I(*map(F,x)) for x in d['cuts']]
 sr=constant_radius(pi);zerrors=[factored_error(zpoly[i],m0[i],m1[i],zregs[i],sr) for i in range(16)]
 assert list(map(str,zerrors))==z['source_errors'][2:]
 degree=max(len(row) for rows in zregs for row in rows)+max(len(row) for rows in oldregs for row in rows)-2
 print('CC16 complete cross primitive degree',degree,flush=True);prim=[primitives(t,degree) for t in cuts]
 zpc,zpd=zip(*(ints(p) for p in zpoly));zrc=[];zrd=[]
 for rows in zregs:a,b=zip(*(ints(row) for row in rows));zrc.append(a);zrd.append(b)
 h2=[];harm=F(0);harm2=F(0)
 for k in range(253):
  m=k+1;harm+=F(1,m);harm2+=F(1,m*m);h2.append(I((F(2,m**3)+(harm*harm+harm2)/m+2*harm/m**2+2*harm2/m)/4)-pi*pi/(12*m))
 h2=[I(max(F(0),x.lo),x.hi) for x in h2]
 cross=[[I(0) for _ in range(56)] for _ in range(16)]
 for j in range(16):
  app=applied(zpc[j],h2,111)
  for i in range(56):cross[j][i]=bil(oldpc[i],app,zpd[j])
 global _JOB
 _JOB=(prim,oldregs,zregs,zpc,zpd,zrc,zrd,oldpc,degree)
 with ProcessPoolExecutor(max_workers=4,mp_context=get_context('fork')) as pool:
  for panel,pg in pool.map(panel_worker_full,range(13)):
   for j in range(16):
    for i in range(56):cross[j][i]+=pg[j][i]
   print('CC16 all896 mixed panel',panel,'seconds',round(time.monotonic()-start),flush=True)
 zrows=[[I(*map(F,x)) for x in row] for row in z['complete_trial_native_rows']]
 # Full source L2 normalization is ni. Old recorded row error is physical
 # L2, including its entire decimal coefficient payment and truncation.
 # Both source norms are bounded by the conservative inherited 10^12
 # allowance at degrees<=142. No error is set to zero.
 crosses=[]
 for j in range(16):
  row=[]
  for i,native_degree in enumerate(EVEN):
   e=F(s['rows'][native_degree]['normalized_uniform_error'])*10**12+zerrors[j]*10**12+F(s['rows'][native_degree]['normalized_uniform_error'])*zerrors[j]
   row.append(D*norms[native_degree]*cross[j][i]+I(-e,e)-sum((Q[k][native_degree]*zrows[j][k] for k in EVEN),I(0)))
  crosses.append(row)
 # Complete source operator allowance is a Loewner diagonal, not56*56
 # independent-entry errors. It is retained BEFORE coordinate congruence.
 delta=F(g['actual_gram_operator_error_upper']);GB=[[I(*map(F,g['residual_gram_surrogate'][i][j])) for j in EVEN] for i in EVEN]
 A=[[Q[i][j] for j in EVEN] for i in EVEN];c=F(699,1000)
 J=[[I(*map(F,x)) for x in row] for row in dat['cc15']['whole_defect_matrix']]
 H=[[crosses[i][j]/c-zrows[i][EVEN[j]] for j in range(56)] for i in range(16)]
 center=[[mid(x) for x in row] for row in J];pivots([[center[i][j]-(max(sum(((x.hi-x.lo)/2 for x in row),F(0)) for row in J) if i==j else 0) for j in range(16)] for i in range(16)])
 # Exact midpoint solve once; all56 right sides use the same full inverse.
 columns=[solve(center,[F(i==j) for i in range(16)]) for j in range(16)]
 grid=10**100
 L=[[F((sum((columns[k][i]*mid(H[k][j]) for k in range(16)),F(0))*grid).__floor__(),grid) for j in range(56)] for i in range(16)]
 # Reassociate L*J*L without deleting mixed products.
 JL=[[sum((J[i][k]*L[k][j] for k in range(16)),I(0)) for j in range(56)] for i in range(16)]
 credit=[[sum((H[k][i]*L[k][j]+L[k][i]*H[k][j]-L[k][i]*JL[k][j] for k in range(16)),I(0)) for j in range(56)] for i in range(56)]
 S=[[A[i][j]-GB[i][j]/c+credit[i][j]-(delta/c if i==j else 0) for j in range(56)] for i in range(56)]
 for i in range(56):
  for j in range(i+1,56):
   a,b=S[i][j],S[j][i]
   S[i][j]=S[j][i]=I(min(a.lo,b.lo),max(a.hi,b.hi))
 # Exact chart spans ALL56 even coordinates, including the constant.
 # It exposes the preserved weak direction instead of hiding its tiny pivot.
 v=list(map(F,dat['saved']['rational_coefficient_witness']));nf=json.loads((base/'RPB108_CORRELATED_WEAK_ROW_NF71_CERTIFICATE_20261008.json').read_bytes());plane=[[F(x) for x in row] for row in nf['even_plane_deterministic_lower']];rho=plane[0][1]/plane[1][1];w=[v[i] for i in EVEN];w[0]-=rho
 chart=[[F(10**16)*x for x in w],[F(j==0) for j in range(56)]]+[[F(j==i) for j in range(56)] for i in range(2,56)]
 assert w[1]!=0
 # Sparse congruence: all but the first column are original basis vectors.
 SC=correlated_chart(A,GB,H,L,J,chart,delta,c)
 # Outer interval widths and rational rounding receive a single whole row
 # radius. This pays every original Gram/cross/source error after congruence.
 radius=max(sum(((x.hi-x.lo)/2 for x in row),F(0)) for row in SC)
 radius=F((radius*grid).__ceil__()+56,grid)
 K=[[F((mid(SC[i][j])*grid).__floor__(),grid)-(radius if i==j else 0) for j in range(56)] for i in range(56)]
 ps,ldl,failed,bad=interval_ldl(K)
 print('CC16 full even56 LDL passed pivots',len(ps),'failed',failed,flush=True)
 out={'stage':'CC16 complete original even56 matrix defect envelope','aperture':'21/20','action_degrees':DEGREES,'retained_even_degrees':EVEN,'all_original_panels':13,'all_prime_powers':[2,3,4,5,7,8],'both_signed_poles':True,'mixed_cross_count':896,'integration_degree':degree,'full_source_gram_archives_decoded':True,'full_source_gram_reintegrated':False,'complete_source_operator_error_paid':str(delta),'whole_action_retained_source_cross':[[compact(x) for x in row] for row in crosses],'whole_defect_source_cross':[[compact(x) for x in row] for row in H],'rational_complete_matrix_lift':[[str(x) for x in row] for row in L],'whole_even_source_gram_surrogate':[[compact(x) for x in row] for row in GB],'whole_even_native_matrix':[[compact(x) for x in row] for row in A],'whole_even_schur_lower':[[compact(x) for x in row] for row in S],'original_even_coordinate_chart':[[str(x) for x in row] for row in chart],'whole_chart_schur_lower':[[compact(x) for x in row] for row in SC],'chart_whole_interval_row_payment':str(radius),'whole_chart_deterministic_lower':[[str(x) for x in row] for row in K],'interval_ldl_pivots':list(map(compact,ps)),'failed_pivot_index':failed,'failed_pivot_interval':None if bad is None else compact(bad),'whole_even56_lower_passed':failed is None,'whole_odd53_sign':False,'whole_domain_aperture_105_certified':False,'certified_whole_domain_aperture':'1','historical_protected_codimension':107,'actual_complement_inverse_evaluated':False,'nonstalling':False,'lean_certified':False,'input_sha256':{k:hashlib.sha256(b).hexdigest() for k,b in raw.items()},'decoded_input_sha256':{k:hashlib.sha256(b).hexdigest() for k,b in decoded.items()},'source_cache_sha256':cachepins,'producer_seconds':time.monotonic()-start}
 out=reassemble(out)
 rawcert=(json.dumps(out,indent=2)+'\n').encode();(base/'RPB108_EVEN_BLOCK_CC16_CERTIFICATE_20261008.json').write_bytes(rawcert);(base/'RPB108_EVEN_BLOCK_CC16_CERTIFICATE_20261008.json.gz').write_bytes(gzip.compress(rawcert,mtime=0));print(json.dumps({'whole_even56_lower_passed':out['whole_even56_lower_passed'],'failed_pivot_index':out['failed_pivot_index'],'row_radius':float(F(out['chart_whole_interval_row_payment'])),'producer_seconds':out['producer_seconds']},indent=2));return out
if __name__=='__main__':
 if '--reassemble' in sys.argv:
  p=ROOT/'notes/data/RPB108_EVEN_BLOCK_CC16_CERTIFICATE_20261008.json';d=reassemble(json.loads(p.read_bytes()));b=(json.dumps(d,indent=2)+'\n').encode();p.write_bytes(b);p.with_suffix('.json.gz').write_bytes(gzip.compress(b,mtime=0));print(json.dumps({'passed':d['whole_even56_lower_passed'],'pivots':len(d['interval_ldl_pivots']),'radius':float(F(d['chart_whole_interval_row_payment']))},indent=2))
 else:compute()
