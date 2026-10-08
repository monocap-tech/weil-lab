"""Independent CC17 trial, inherited-lower attachment and source integration.

Does not replay the unavailable full CC16 source/Gram archives, nor assert
that interval enclosure evaluates the original inverse or settles its sign.
"""
import gzip,json,hashlib
from fractions import Fraction as F
from pathlib import Path
from certify_native_rich_action_cc14 import I,D,shifted_legendre,sqrt_rational,mid,primitives,ints,applied,bil,dot,constant_radius,factored_error,controls
from certify_native_inverse_correlation_cc13 import I as SmallI
from validate_native_even_block_cc16 import ldl
from native_terminal_odd_source_cc17 import controls as odd_controls,odd_source
BASE=Path(__file__).resolve().parents[1]/'notes/data'

def run():
 d=json.loads((BASE/'RPB108_TERMINAL_ODD_CC17_CERTIFICATE_20261008.json').read_bytes());checks=0
 for name,pin in d['input_sha256'].items():assert hashlib.sha256((BASE/name).read_bytes()).hexdigest()==pin;checks+=1
 raw=(BASE/'RPB108_TERMINAL_ODD_CC17_SOURCE_20261008.json.gz').read_bytes();assert hashlib.sha256(raw).hexdigest()==d['source_archive_sha256'];checks+=1
 decoded=gzip.decompress(raw);assert hashlib.sha256(decoded).hexdigest()==d['decoded_source_sha256'];checks+=1;s=json.loads(decoded)
 old=json.loads(gzip.decompress((BASE/'RPB108_ODD_BLOCK_CC16_CERTIFICATE_20261008.json.gz').read_bytes()));joined=json.loads((BASE/'RPB108_JOINED_CC16_SUMMARY_20261008.json').read_bytes())
 assert d['input_sha256']['RPB108_PRIME8_MATRIX112_105_COMPACT80_20261008.json.gz']==old['input_sha256']['native'];checks+=1
 assert hashlib.sha256((BASE/'RPB108_ODD_BLOCK_CC16_CERTIFICATE_20261008.json.gz').read_bytes()).hexdigest()==joined['archives']['RPB108_ODD_BLOCK_CC16_CERTIFICATE_20261008.json']['gzip_sha256'];checks+=1
 n=json.loads(gzip.decompress((BASE/'RPB108_PRIME8_MATRIX112_105_COMPACT80_20261008.json.gz').read_bytes()));pairs=[[None]*112 for _ in range(112)];p=0
 for i in range(112):
  for j in range(i+1):pairs[i][j]=pairs[j][i]=tuple(F(int(x),10**80) for x in n['lower_triangle_row_major'][p]);p+=1
 odd=list(range(1,112,2));q=list(map(F,d['rational_finite_trial_odd_coefficients']));assert len(q)==56 and q[-1]==1;checks+=1
 A=[[pairs[i][j] for j in odd] for i in odd]
 def quadratic(v):
  center=sum((v[i]*v[j]*(A[i][j][0]+A[i][j][1])/2 for i in range(56) for j in range(56)),F(0))
  radius=sum((abs(v[i]*v[j])*(A[i][j][1]-A[i][j][0])/2 for i in range(56) for j in range(56)),F(0))
  return center-radius,center+radius
 u=quadratic(q);published=list(map(F,d['native_finite_trial_value']));assert published[0]<=u[0]<=u[1]<=published[1];checks+=1
 enclosure=list(map(F,d['actual_terminal_scalar_enclosure']));assert enclosure[1]>=u[1] and enclosure[0]==F(old['failed_pivot_interval'][0]);checks+=1
 # Freshly replay the retained positive lower. The last lower pivot is an
 # inherited CC16 enclosure; its unavailable full last row is not invented.
 K=[[F(x) for x in row] for row in old['positive_leading_deterministic_lower']]
 ps,_,failed=ldl(K);assert failed is None and len(ps)==55;checks+=55
 assert old['failed_pivot_index']==55 and old['positive_leading_retained_dimension']==55 and old['remaining_odd_retained_dimension']==1;checks+=1
 native55=[[SmallI(*pairs[i][j]) for j in odd[:55]] for i in odd[:55]]
 np,_,nf=ldl(native55);assert nf is None and len(np)==55;checks+=55
 mass=sum((x*x for x in q),F(0));assert F(d['finite_trial_physical_mass'])==mass;checks+=1
 assert list(map(F,d['mass_normalized_scalar_enclosure']))==[x/mass for x in enclosure];checks+=1
 scale=F(d['source_physical_scale']);w=[scale*x for x in q];assert list(map(F,s['scaled_physical_coefficients']))==w and s['odd_degrees']==odd;checks+=1
 P=shifted_legendre(111);norms=[sqrt_rational(F(2*k+1)/D) for k in range(112)]
 weights={k:w[j]*mid(norms[k]) for j,k in enumerate(odd)}
 poly=[sum((weights[j]*(P[j][k] if k<=j else 0) for j in odd),F(0)) for k in range(112)]
 assert list(map(F,s['polynomial']))==poly;checks+=112
 M0=sum(map(abs,weights.values()),F(0));M1=sum((abs(weights[j])*j*(j+1) for j in odd),F(0))
 assert F(s['M0'])==M0 and F(s['M1'])==M1;checks+=2
 # Algebraic odd reflection on the physical t=(x+a)/(2a) chart.
 from math import comb
 reflected=[sum((poly[j]*comb(j,k)*(-1)**k for j in range(k,len(poly))),F(0)) for k in range(len(poly))]
 assert reflected==[-x for x in poly];checks+=112
 regs=[[F(x) for x in row] for row in s['regular_polynomials']];pi=I(*map(F,s['pi']));cuts=[I(*map(F,x)) for x in s['cuts']]
 print('CC17 replaying original odd source constructor',flush=True)
 rebuilt,unfactored,repi,geometry=odd_source(poly,M0,M1)
 assert rebuilt==regs and unfactored==F(s['unfactored_constructor_error']);checks+=2
 assert repi.lo==pi.lo and repi.hi==pi.hi;checks+=1
 assert [[str(x.lo),str(x.hi)] for x in geometry['cuts']]==s['cuts'] and json.loads(json.dumps(geometry['active']))==s['active'];checks+=2
 error=factored_error(poly,M0,M1,regs,constant_radius(pi))+2*10**7*sum((abs(w[j])*sqrt_rational(D/F(2*k+1)).hi/(2*I.grid) for j,k in enumerate(odd)),F(0))
 assert error==F(d['complete_source_error_paid'])==F(s['source_error']);checks+=1
 assert len(cuts)==14 and len(regs)==13 and d['all_prime_powers']==[2,3,4,5,7,8] and d['both_signed_poles'];checks+=1
 for key,name in [('constructor_sha256','certify_native_coupled_trial_cc3.py'),('fast_constructor_sha256','native_rich_action_fast_source_cc14.py'),('source_error_constructor_sha256','native_rich_action_source_error_cc14.py'),('odd_constructor_sha256','native_terminal_odd_source_cc17.py'),('original_general_source_engine_sha256','certify_native_prime8_source112_engine_105.py')]:
  assert hashlib.sha256((BASE.parents[1]/'scripts'/name).read_bytes()).hexdigest()==s[key];checks+=1
 checks+=odd_controls();assert I.grid==10**800;checks+=1
 # Reintegrate every panel and both log cross terms independently of the
 # producer's panel_worker. Pure moment/Hankel primitives are shared.
 degree=2*max(map(len,regs))-2;assert degree==d['integration_degree'];checks+=1
 prim=[primitives(t,degree) for t in cuts];pc,pd=ints(poly);count=len(poly);mom=[I(0) for _ in poly]
 h1=[];h2=[];H=F(0);H2=F(0)
 for k in range(2*count-1):
  h=k+1;H+=F(1,h);H2+=F(1,h*h);h1.append(I((F(1,h*h)+H/h)/2))
  v=I((F(2,h**3)+(H*H+H2)/h+2*H/h**2+2*H2/h)/4)-pi*pi/(12*h);h2.append(I(max(F(0),v.lo),v.hi))
 gram=bil(pc,applied(pc,h2,count),pd*pd)
 for panel,r in enumerate(regs):
  a,b=prim[panel:panel+2]
  mm=[(b[0][k+1]-a[0][k+1])/(k+1) for k in range(degree+1)];lm=[b[1][k]-a[1][k] for k in range(degree+1)]
  mm=[I(max(F(0),v.lo),v.hi) for v in mm];lm=[I(max(F(0),v.lo),v.hi) for v in lm]
  rc,rd=ints(r);gram+=bil(rc,applied(rc,mm,len(r)),rd*rd)+2*bil(pc,applied(rc,lm,count),pd*rd)
  for k in range(count):mom[k]+=dot(r,mm[k:])
  checks+=3;print('CC17 independent original source panel',panel,flush=True)
 for k in range(count):mom[k]+=dot(poly,h1[k:])
 bound=F(10**8)*(1+M0);ge=2*error*bound+error*error;assert ge==F(d['source_gram_product_error_paid']) and bound==F(d['source_gram_norm_bound']);checks+=2
 raw_norm=D*gram+I(-ge,ge);published_raw=list(map(F,d['scaled_original_source_norm_squared']));assert published_raw[0]<=raw_norm.lo<=raw_norm.hi<=published_raw[1];checks+=1
 projections=[]
 for k in range(112):
  x=I(0) if k%2==0 else D*norms[k]*dot(P[k],mom)+I(-error,error)
  y=I(0)
  for j,l in enumerate(odd):y+=w[j]*I(*pairs[k][l])
  if k%2:
   assert max(x.lo,y.lo)<=min(x.hi,y.hi);x=I(max(x.lo,y.lo),min(x.hi,y.hi))
  published=list(map(F,d['complete_original_native_projection'][k]));assert published[0]<=x.lo<=x.hi<=published[1];checks+=1;projections.append(x)
 residuals={
  'scaled_original_F112_residual_norm_squared':raw_norm-sum((x*x for x in projections),I(0)),
  'scaled_original_e111_perpendicular_residual_norm_squared':raw_norm-projections[111]*projections[111],
  'scaled_finite55_stationarity_residual_norm_squared':sum((projections[k]*projections[k] for k in odd[:55]),I(0))}
 for key,v in residuals.items():
  assert v.hi>=0;published=list(map(F,d[key]));assert published[0]<=max(F(0),v.lo)<=v.hi<=published[1];checks+=1
 # Original positive compression, then an actual scalar infimum: the lower
 # follows infimum monotonicity; the upper follows a concrete original trial.
 for flag in ['actual_terminal_scalar_sign_evaluated','actual_compression_inverse_evaluated','actual_negative_direction_certified','whole_domain_aperture_105_certified','nonstalling','lean_certified']:assert d[flag] is False;checks+=1
 # A failed sufficient lower pivot does not certify an actual negative mode.
 # K=diag(1,-1), Q=[[2,1],[1,2]] have Q-K positive and Schur(Q)=3/2.
 assert F(2)-F(1)**2/F(2)==F(3,2) and F(1)*F(3)-F(1)**2>0;checks+=2
 out={'passed':True,'exact_checks':checks,'fresh_original_source_panel_integrals_replayed':13,'fresh_original_native_projection_checks':112,'independent_native_positive_pivots':55,'independent_inherited_lower_positive_pivots':55,'terminal_scalar_enclosure':d['actual_terminal_scalar_enclosure'],'native_upper_trial_recomputed':True,'inherited_terminal_lower_recomputed_from_full_gram':False,'original_source_constructor_replayed':True,'original_source_interval_integration_replayed':True,'analytic_source_error_framework':'CC14 original factored source error extended by the original SOURCE112 odd parity rules; unchanged fixed orders; adopted analytic constructor theorem','full_CC16_even_archive_replayed':False,'actual_inverse_evaluated':False,'terminal_sign_open':True}
 (BASE/'RPB108_TERMINAL_ODD_CC17_VALIDATION_20261008.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));return out

if __name__=='__main__':run()
