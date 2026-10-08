"""CC17: actual terminal scalar bracket and a fresh original residual source.

The lower endpoint is inherited from CC16's no-lift lower Schur pivot.
The upper endpoint is a freshly verified finite native trial. Neither is an
evaluation of the original infinite inverse. Decimal arithmetic chooses a
trial only; all asserted bounds use outward rational intervals.
"""
import json,gzip,hashlib,time
from decimal import Decimal,localcontext
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import get_context
import certify_native_rich_action_cc14 as action
from certify_native_rich_action_cc14 import F,I,D,ROOT,mid,compact,quad,shifted_legendre,sqrt_rational,fast_source,constant_radius,factored_error,ints,applied,bil,primitives,dot,bracket,panel_worker
from certify_native_even_block_cc16 import interval_ldl
from native_terminal_odd_source_cc17 import odd_source,controls as odd_controls

BASE=ROOT/'notes/data'
NATIVE='RPB108_PRIME8_MATRIX112_105_COMPACT80_20261008.json.gz'
ODD='RPB108_ODD_BLOCK_CC16_CERTIFICATE_20261008.json.gz'
SUMMARY='RPB108_JOINED_CC16_SUMMARY_20261008.json'
CERT='RPB108_TERMINAL_ODD_CC17_CERTIFICATE_20261008.json'
SOURCE='RPB108_TERMINAL_ODD_CC17_SOURCE_20261008.json.gz'

def trial(A):
 # Fixed-grid rational candidate; no claim depends on the Decimal solve.
 with localcontext() as context:
  context.prec=170
  dec=lambda x:Decimal(x.numerator)/Decimal(x.denominator)
  M=[[dec(mid(x)) for x in row] for row in A]
  L=[[Decimal(int(i==j)) for j in range(56)] for i in range(56)]
  for k in range(55):
   pivot=M[k][k]
   for i in range(k+1,56):L[i][k]=M[i][k]/pivot
   for i in range(k+1,56):
    for j in range(i,56):M[i][j]=M[j][i]=M[i][j]-M[i][k]*M[k][j]/pivot
  w=[Decimal(0)]*55+[Decimal(1)]
  for i in range(54,-1,-1):w[i]=-sum((L[j][i]*w[j] for j in range(i+1,56)),Decimal(0))
  grid=10**120
  return [F((F(x)*grid).__floor__(),grid) for x in w[:55]]+[F(1)]

def compute():
 start=time.monotonic();raw={name:(BASE/name).read_bytes() for name in (NATIVE,ODD,SUMMARY)}
 n=json.loads(gzip.decompress(raw[NATIVE]));old=json.loads(gzip.decompress(raw[ODD]));summary=json.loads(raw[SUMMARY])
 assert n['aperture']==old['aperture']=='21/20'
 assert hashlib.sha256(raw[ODD]).hexdigest()==summary['archives']['RPB108_ODD_BLOCK_CC16_CERTIFICATE_20261008.json']['gzip_sha256']
 Q=[[None]*112 for _ in range(112)];pos=0
 for i in range(112):
  for j in range(i+1):Q[i][j]=Q[j][i]=I(*(F(int(x),10**80) for x in n['lower_triangle_row_major'][pos]));pos+=1
 odd=list(range(1,112,2));A=[[Q[i][j] for j in odd] for i in odd]
 ps,L,failed,bad=interval_ldl([row[:55] for row in A[:55]])
 assert failed is None and len(ps)==55
 q=trial(A);scale=F(1,10**14);w=[scale*x for x in q]
 U=quad(A,q);mass=sum((x*x for x in q),F(0));lower=F(old['failed_pivot_interval'][0])
 assert old['failed_pivot_index']==55 and old['positive_leading_retained_dimension']==55 and lower<0<U.hi
 P=shifted_legendre(111);norms=[sqrt_rational(F(2*j+1)/D) for j in range(112)]
 weights=[w[(j-1)//2]*mid(norms[j]) if j%2 else F(0) for j in range(112)]
 poly=[sum((weights[j]*(P[j][k] if k<=j else 0) for j in odd),F(0)) for k in range(112)]
 M0=sum((abs(weights[j]) for j in odd),F(0));M1=sum((abs(weights[j])*j*(j+1) for j in odd),F(0))
 print('CC17 constructing one original odd completion source',flush=True)
 assert odd_controls()==36
 regs,original_error,pi,geom=odd_source(poly,M0,M1)
 error=factored_error(poly,M0,M1,regs,constant_radius(pi))
 error+=2*10**7*sum((abs(w[(j-1)//2])*sqrt_rational(D/F(2*j+1)).hi/(2*I.grid) for j in odd),F(0))
 source={'stage':'CC17 original odd finite-completion source','physical_scale':str(scale),'odd_degrees':odd,'scaled_physical_coefficients':list(map(str,w)),'polynomial':list(map(str,poly)),'M0':str(M0),'M1':str(M1),'regular_polynomials':[[str(x) for x in row] for row in regs],'source_error':str(error),'unfactored_constructor_error':str(original_error),'pi':bracket(pi),'cuts':list(map(bracket,geom['cuts'])),'active':geom['active'],'interval_grid':str(I.grid),'constructor_sha256':hashlib.sha256((ROOT/'scripts/certify_native_coupled_trial_cc3.py').read_bytes()).hexdigest(),'fast_constructor_sha256':hashlib.sha256((ROOT/'scripts/native_rich_action_fast_source_cc14.py').read_bytes()).hexdigest(),'source_error_constructor_sha256':hashlib.sha256((ROOT/'scripts/native_rich_action_source_error_cc14.py').read_bytes()).hexdigest()}
 source['odd_constructor_sha256']=hashlib.sha256((ROOT/'scripts/native_terminal_odd_source_cc17.py').read_bytes()).hexdigest()
 source['original_general_source_engine_sha256']=hashlib.sha256((ROOT/'scripts/certify_native_prime8_source112_engine_105.py').read_bytes()).hexdigest()
 b=(json.dumps(source,indent=2)+'\n').encode();(BASE/SOURCE).write_bytes(gzip.compress(b,mtime=0))
 plen=len(poly);slen=max(map(len,regs));degree=2*slen-2
 print('CC17 source integration primitive degree',degree,flush=True)
 prim=[primitives(t,degree) for t in geom['cuts']]
 pc,pd=ints(poly);rc,rd=zip(*(ints(row) for row in regs))
 moments=[I(0) for _ in range(plen)];gram=I(0)
 h1=[];h2=[];harm=F(0);harm2=F(0)
 for k in range(2*plen-1):
  h=k+1;harm+=F(1,h);harm2+=F(1,h*h)
  h1.append(I((F(1,h*h)+harm/h)/2))
  h2.append(I((F(2,h**3)+(harm*harm+harm2)/h+2*harm/h**2+2*harm2/h)/4)-pi*pi/(12*h))
 h2=[I(max(F(0),x.lo),x.hi) for x in h2]
 gram+=bil(pc,applied(pc,h2,plen),pd*pd)
 action._BATCH=(prim,[regs],[rc],[rd],[pc],[pd],1,plen,slen,degree)
 with ProcessPoolExecutor(max_workers=4,mp_context=get_context('fork')) as pool:
  for panel,pm,pg in pool.map(panel_worker,range(13)):
   for k in range(plen):moments[k]+=pm[0][k]
   gram+=pg[0][0]
   print('CC17 original source panel',panel,'seconds',round(time.monotonic()-start),flush=True)
 for k in range(plen):moments[k]+=dot(poly,h1[k:])
 # This inherited constructor bound is deliberately coarse and is paid.
 normbound=F(10**8)*(1+M0);ge=2*error*normbound+error*error
 raw_norm=D*gram+I(-ge,ge)
 projected=[];overlaps=0
 for k in range(112):
  x=I(0) if k%2==0 else D*norms[k]*dot(P[k],moments)+I(-error,error)
  y=sum((w[j]*Q[k][odd[j]] for j in range(56)),I(0))
  if k%2:
   assert max(x.lo,y.lo)<=min(x.hi,y.hi),('original-native-overlap',k)
   x=I(max(x.lo,y.lo),min(x.hi,y.hi));overlaps+=1
  projected.append(x)
 complement_norm=raw_norm-sum((x*x for x in projected),I(0))
 compressed_norm=raw_norm-sum((projected[k]*projected[k] for k in (111,)),I(0))
 assert complement_norm.hi>=0 and compressed_norm.hi>=0
 residual55=sum((projected[k]*projected[k] for k in odd[:55]),I(0))
 result={'milestone':'CC17','classification':'B: actual terminal scalar enclosed; original residual source constructed; sign open','base_commit':'ee6e56cf63c4a6918f4c9e2f46c2e9f814ffce37','aperture':'21/20','terminal_coordinate_degree':111,'terminal_coordinate_value':'1','terminal_scalar_definition':'inf Q(e111+v), v in original odd e111-perpendicular form domain','actual_terminal_scalar_enclosure':[str(lower),str(U.hi)],'inherited_lower_provenance':'CC16 entire no-lift odd56 deterministic lower; positive leading55; terminal interval LDL pivot','inherited_lower_recomputed_from_full_gram':False,'native_finite_trial_value':compact(U),'native_leading_positive_pivots':list(map(compact,ps)),'rational_finite_trial_odd_coefficients':list(map(str,q)),'finite_trial_physical_mass':str(mass),'mass_normalized_scalar_enclosure':[str(lower/mass),str(U.hi/mass)],'source_physical_scale':str(scale),'fresh_original_source_count':1,'fresh_original_source_native_overlaps':overlaps,'complete_original_native_projection':list(map(compact,projected)),'scaled_original_source_norm_squared':compact(raw_norm),'scaled_original_F112_residual_norm_squared':[str(max(F(0),complement_norm.lo)),str(complement_norm.hi)],'scaled_original_e111_perpendicular_residual_norm_squared':[str(max(F(0),compressed_norm.lo)),str(compressed_norm.hi)],'scaled_finite55_stationarity_residual_norm_squared':[str(max(F(0),residual55.lo)),str(residual55.hi)],'residual_source_identity':'sigma=Q(q)-<P_D Lq,D_inverse P_D Lq>; D is original positive odd compression e111-perpendicular','complete_source_error_paid':str(error),'source_gram_product_error_paid':str(ge),'source_gram_norm_bound':str(normbound),'all_original_panels':13,'all_prime_powers':[2,3,4,5,7,8],'both_signed_poles':True,'integration_degree':degree,'source_archive_sha256':hashlib.sha256((BASE/SOURCE).read_bytes()).hexdigest(),'decoded_source_sha256':hashlib.sha256(b).hexdigest(),'input_sha256':{name:hashlib.sha256(b).hexdigest() for name,b in raw.items()},'actual_terminal_scalar_sign_evaluated':False,'actual_compression_inverse_evaluated':False,'actual_negative_direction_certified':False,'whole_domain_aperture_105_certified':False,'certified_whole_domain_aperture':'1','remaining_even_retained_dimension':0,'remaining_odd_retained_dimension':1,'positive_slice_codimension':1,'nonstalling':False,'lean_certified':False,'next_gate':'Enclose the complete original inverse-weighted reaction of the newly pinned odd residual source on the positive e111-perpendicular compression','producer_seconds':time.monotonic()-start}
 result['original_odd_source_controls']=36
 (BASE/CERT).write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({'scalar_enclosure':[float(lower),float(U.hi)],'mass_normalized_enclosure':[float(lower/mass),float(U.hi/mass)],'source_residual_norm_squared':[float(max(F(0),compressed_norm.lo)),float(compressed_norm.hi)],'seconds':result['producer_seconds']},indent=2))
 return result

if __name__=='__main__':compute()
