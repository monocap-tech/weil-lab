"""RC240: complete P4/P5 actions and three trials per original-action source."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial,comb
from copy import deepcopy
import argparse,hashlib,json
import validate_rpb108_rc239_exterior_band_leakage as parent
weighted=parent.parent;trial=parent.trial;material=trial.material;orig=parent.orig;p=parent.p
up=parent.up;down=parent.down;root=parent.root;rootdown=trial.rootdown
B=parent.B;CUT=64;EXT=96;ROOT=Path(__file__).resolve().parents[1]
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc239_exterior_band_leakage.json':'dfcd2ef1bc834a071c895bfcfa49370c83aa0e86','notes/RPB108_RC239_EXTERIOR_BAND_LEAKAGE_20261014.md':'da724f5c0a6751da5c7f80e25b7d3048c268010f'})
HELPER_PINS['scripts/validate_rpb108_rc239_exterior_band_leakage.py']='5b0c21280154029a4eb5ca493e7734e288131d23'
def original_action(d,reg,prime,eps,sl,sh,reverse):
 assert d in [4,5] and CUT+1>=3*d+1
 q=trial.regular_poly(d,reg);rc=[orig.project(q,n) for n in range(len(q))]
 for n in range(12):assert rc[n]==F(2*n+1,2)*orig.integral(orig.product(q,orig.legendre(n)))
 rtail=up(sum((orig.mass(n)*v*v for n,v in enumerate(rc) if n>CUT),F(0)))
 pc,ptail,pfault,segments=trial.prime_poly(d,prime,reverse)
 phi=[F(11,20)**k/factorial(k) if k%2==d%2 else F(0) for k in range(41)]
 moment=B*orig.integral(orig.product(orig.legendre(d),phi));pole=[2*(-1)**d*moment*v for v in phi];oc=[orig.project(pole,n) for n in range(CUT+1)]
 tau=2*F(11,20)**41/factorial(41);polefault=up(16*B*tau*root(orig.mass(d)))
 ll=2*sum((F(1,3)**(2*k+1)/F(2*k+1) for k in range(100)),F(0));lh=ll+2*F(1,3)**201/(201*(1-F(1,9)));out=[];rounding=F(0)
 for n in range(CUT+1):
  if (n-d)%2:out.append(dict(degree=n,coefficient='0',radius='0'));continue
  h=2*orig.H(2*n)-2*orig.H(n)+F(1,2*n+1) if n==d else F(2*n+1,abs(n-d)*(n+d+1))
  lo=h-(lh if n==d else 0)-rc[n]+pc[n]+oc[n]-(F(789,125) if n==d else 0);hi=h-(ll if n==d else 0)-rc[n]+pc[n]+oc[n]-(F(789,125) if n==d else 0)
  values=[v/(orig.H(n)+s)+(n==d) for v in [lo,hi] for s in [sl,sh]];a=min(values);b=max(values);c=down((a+b)/2);r=max(c-a,b-c);rounding+=orig.mass(n)*(orig.H(n)+sh)*r*r
  out.append(dict(degree=n,coefficient=str(c),radius=str(up(r))))
 first=CUT+1 if (CUT+1-d)%2==0 else CUT+2
 components=dict(finite_rounding=up(rounding),endpoint_omitted_output=up(3*B/((orig.H(first)+sl)*(CUT-d)**2)),regular_omitted_output=up(rtail/(orig.H(first)+sl)),prime_omitted_output=up(ptail/(orig.H(first)+sl)),regular_kernel=up((2*B*eps)**2*orig.mass(d)/sl),prime_arithmetic=up(pfault**2/sl),pole_Taylor=up(polefault**2/sl))
 total=up(sum((root(v) for v in components.values()),F(0))**2)
 return dict(input='P'+str(d),input_degree=d,parity='even' if d%2==0 else 'odd',input_D_energy_lower=str(orig.mass(d)*(orig.H(d)+sl)),input_D_energy_upper=str(orig.mass(d)*(orig.H(d)+sh)),finite_original_D_action=out,D_energy_component_squared_errors={k:str(v) for k,v in components.items()},complete_original_action_D_error_squared_upper=str(total),prime_segments=segments,complete_prime_pairs=7,signed_pole_sign=(-1)**d)
def exterior_bound(d,U):
 assert d in [4,5]
 q=orig.legendre(d);qp=[sum((q[k]*comb(k,m)*(-1/B)**m for k in range(m,len(q))),F(0)) for m in range(len(q))];assert qp[0]==1
 a=6*U;T=2*B;moments=[F(0),F(2)/a,T/a+1/a**2]
 for k in range(3,d+1):moments.append(T**(k-1)/a+(k-1)*T**(k-2)/a**2+(k-1)*(k-2)*moments[k-2]/a**2)
 correction=2/(3*a*T)+sum((abs(qp[k])*moments[k]/3 for k in range(1,d+1)),F(0));b=down(F(1,2)-correction);assert b>0
 exp9=sum((F(9)**k/factorial(k) for k in range(21)),F(0));assert exp9>24*B*U
 derivative=sum((k*abs(v) for k,v in enumerate(q)),F(0));L=up(2*U+1/(6*B)+derivative*F(10,3)/B);w=down(b/L);assert 0<w<=B
 ell=down(2*(b*b*w-b*L*w*w+L*L*w**3/3));assert 0<ell<=2*b**3/(3*L)
 return ell,dict(boundary_distance_polynomial=list(map(str,qp)),scaled_finite_sine_moment_absolute_upper=list(map(str,moments)),boundary_value_lower=str(b),polynomial_derivative_abs_upper=str(derivative),exterior_derivative_abs_upper=str(L),exterior_width=str(w),both_edges_exterior_energy_lower=str(ell),exponential_9_positive_series_lower=str(exp9),logarithm_argument_upper=str(24*B*U))
def new_augmentation(d,gram,lam,epsilon,sl,sh,U):
 band=[trial.isc(a,1/orig.mass(n)) for n,a in enumerate(gram)];captured=sum((orig.mass(n)*material.minabs(a)**2 for n,a in enumerate(band)),F(0))
 ell,proof=exterior_bound(d,U);tail=up(gram[d][1]-ell-captured);assert tail>=0
 first=EXT+1 if (EXT+1-d)%2==0 else EXT+2
 resolved=up(sum((lam*lam*orig.mass(n)*max(abs(band[n][0]),abs(band[n][1]))**2/(orig.H(n)+sl) for n in range(CUT+1,EXT+1)),F(0)))
 remainder=up(lam*lam*tail/(orig.H(first)+sl));omitted=up(resolved+remainder);finite=F(0);coeff=[]
 for n,a in enumerate(band[:CUT+1]):
  if (n-d)%2:coeff.append(dict(degree=n,coefficient='0',radius='0'));continue
  values=[lam*v/(orig.H(n)+s) for v in a for s in [sl,sh]];lo=min(values);hi=max(values);c=down((lo+hi)/2);r=max(c-lo,hi-c);finite+=orig.mass(n)*(orig.H(n)+sh)*r*r
  coeff.append(dict(degree=n,coefficient=str(c),radius=str(up(r))))
 rational=up(lam*lam*epsilon*epsilon*orig.mass(d)/sl);E=up((root(up(finite))+root(omitted)+root(rational))**2)
 return coeff,E,dict(exterior_energy_certificate=proof,band_physical_output_beyond_96_energy_upper=str(tail),degree_65_through_96_D_energy_upper=str(resolved),beyond_96_D_energy_upper=str(remainder),finite_rounding_D_energy_upper=str(up(finite)),rational_to_band_D_energy_upper=str(rational),omitted_output_D_energy_upper=str(omitted))
def loewner(intervals):
 n=len(intervals);C=[[(a+b)/2 for a,b in row] for row in intervals];r=[sum(((b-a)/2 for a,b in row),F(0)) for row in intervals]
 return [[C[i][j]-(r[i] if i==j else 0) for j in range(n)] for i in range(n)],[[C[i][j]+(r[i] if i==j else 0) for j in range(n)] for i in range(n)]
def quadratic(intervals,y):
 lo=hi=F(0)
 for i in range(len(y)):
  for k in range(len(y)):
   a,b=intervals[i][k];w=y[i]*y[k];lo+=min(w*a,w*b);hi+=max(w*a,w*b)
 return down(lo),up(hi)
def controls():
 D=[[F(2),F(0),F(0)],[F(0),F(3),F(0)],[F(0),F(0),F(5)]]
 F0=[[F(1),F(1,4),F(1,7)],[F(1,4),F(2),-F(1,5)],[F(1,7),-F(1,5),F(3)]]
 Gy=[[F(2),F(1,3),F(1,9)],[F(1,3),F(1),F(1,8)],[F(1,9),F(1,8),F(2)]];lam=F(3)
 G=p.add(F0,p.scale(lam,Gy));assert p.psd(G)
 N=p.mm(p.inv(D),G);N0=p.mm(p.inv(D),F0);assert p.mm(N,N0)!=p.mm(N0,N)
 q=[[F(1)],[F(0)],[F(0)]];y=[[F(1,7)],[-F(1,11)],[F(2,13)]];u=p.add(q,y,-1);O=p.mm(N0,q);e=p.add(O,p.mm(N,y),-1)
 T=p.mm(p.mm(p.trans(O),D),p.mm(p.inv(N),O))[0][0];R=p.mm(p.mm(p.trans(e),D),p.mm(p.inv(N),e))[0][0]
 center=2*p.mm(p.trans(y),p.mm(F0,q))[0][0]-p.mm(p.trans(y),p.mm(G,y))[0][0]
 gap=p.mm(p.trans(q),p.mm(F0,q))[0][0]-T
 assert T==center+R and gap==p.mm(p.trans(u),p.mm(F0,u))[0][0]+lam*p.mm(p.trans(y),p.mm(Gy,y))[0][0]-R
 # Row-sum radii bound a symmetric three-dimensional interval error.
 radii=[[F(1,100),F(1,200),F(1,300)],[F(1,200),F(1,150),F(1,250)],[F(1,300),F(1,250),F(1,180)]]
 intervals=[[(F0[i][k]-radii[i][k],F0[i][k]+radii[i][k]) for k in range(3)] for i in range(3)];L,H=loewner(intervals)
 from itertools import product
 for signs in product([-1,1],repeat=6):
  E=[[F(0)]*3 for _ in range(3)];t=0
  for i in range(3):
   for k in range(i,3):E[i][k]=E[k][i]=signs[t]*radii[i][k];t+=1
  X=p.add(F0,E);assert p.psd(p.add(X,L,-1)) and p.psd(p.add(H,X,-1))
 return dict(three_dimensional_nonidentity_metric_noncommuting_signed_residual_identity=True,all_64_symmetric_interval_vertex_Loewner_controls=True,new_sine_moment_recurrence_maximum_degree=5)
def response(base,columns,F0,Gy,lam,mu,nu,sl,sh,prior,reverse):
 O=[[F(r['coefficient']) for r in c['original']['finite_original_D_action']] for c in columns];A=[[F(r['coefficient']) for r in c['finite_complete_augmented_D_action']] for c in columns]
 Eo=[F(c['original']['complete_original_action_D_error_squared_upper']) for c in columns];Ea=[F(c['augmentation_action_D_error_squared_upper']) for c in columns];sm=(sl+sh)/2
 AG=[[sum((orig.mass(n)*(orig.H(n)+sm)*A[i][n]*A[k][n] for n in range(CUT+1)),F(0)) for k in range(3)] for i in range(3)]
 rhs=[sum((orig.mass(n)*(orig.H(n)+sm)*O[0][n]*A[i][n] for n in range(CUT+1)),F(0)) for i in range(3)];source=sum((orig.mass(n)*(orig.H(n)+sm)*O[0][n]**2 for n in range(CUT+1)),F(0));assert p.psd(AG)
 least_exact=[r[0] for r in p.mm(p.inv(AG),[[v] for v in rhs])];least=[down(v) for v in least_exact]
 twoGram=[row[:2] for row in AG[:2]];two=[r[0] for r in p.mm(p.inv(twoGram),[[v] for v in rhs[:2]])]
 twofit=source-sum((rhs[i]*two[i] for i in range(2)),F(0));threefit=source-sum((rhs[i]*least_exact[i] for i in range(3)),F(0));assert 0<=threefit<=twofit
 GM=[[(F0[i][k][0]+F0[i][k][1]+lam*(Gy[i][k][0]+Gy[i][k][1]))/2 for k in range(3)] for i in range(3)];fm=[(F0[i][0][0]+F0[i][0][1])/2 for i in range(3)];gal=[down(r[0]) for r in p.mm(p.inv(GM),[[v] for v in fm])]
 old=list(map(F,prior['selected_inverse_upper_trial']['trial_coefficients']))+[F(0)];assert len(old)==3
 choices={tuple(old),(F(0),)*3,tuple(least),tuple(gal)}
 for k in range(-10,21):choices.add(tuple(down(old[i]+F(k,10)*(least[i]-old[i])) for i in range(3)))
 for k in range(8,13):
  choices.add(tuple(down(F(k,10)*v) for v in least));choices.add(tuple(down(F(k,10)*v) for v in gal))
 def evaluate(y):
  v=[O[0][n]-sum((y[i]*A[i][n] for i in range(3)),F(0)) for n in range(CUT+1)];terms=[(n,orig.mass(n)*x*x) for n,x in enumerate(v)]
  if reverse:terms.reverse()
  nl=sum((x*(orig.H(n)+sl) for n,x in terms),F(0));nh=sum((x*(orig.H(n)+sh) for n,x in terms),F(0))
  fault=abs(1-y[0])*root(Eo[0])+sum((abs(y[i])*root(Eo[i]) for i in [1,2]),F(0))+sum((abs(y[i])*root(Ea[i]) for i in range(3)),F(0))
  rl=down(max(F(0),rootdown(nl)-fault)**2);rh=up((root(nh)+fault)**2);u=[1-y[0],-y[1],-y[2]];qlo,qhi=quadratic(F0,u);alo,ahi=quadratic(Gy,y)
  cl=ch=F(0)
  for i in range(3):
   for k in range(3):
    w=(y[k] if i==0 else 0)+(y[i] if k==0 else 0)-y[i]*y[k];a,b=F0[i][k];cl+=min(w*a,w*b);ch+=max(w*a,w*b)
    w=-lam*y[i]*y[k];a,b=Gy[i][k];cl+=min(w*a,w*b);ch+=max(w*a,w*b)
  return dict(trial_coefficients=list(map(str,y)),retained_center_residual_D_energy_lower=str(down(nl)),retained_center_residual_D_energy_upper=str(up(nh)),shared_complete_fault_D_norm_upper=str(up(fault)),actual_residual_D_energy_lower=str(rl),actual_residual_D_energy_upper=str(rh),original_action_inverse_response_lower=str(down(cl+rl/nu)),original_action_inverse_response_upper=str(up(ch+rh/mu)),coupled_signed_gap_lower=str(down(qlo+lam*alo-rh/mu)),coupled_signed_gap_upper=str(up(qhi+lam*ahi-rl/nu)))
 candidates=[evaluate(y) for y in sorted(choices)];lower=max(candidates,key=lambda r:F(r['original_action_inverse_response_lower']));upper=min(candidates,key=lambda r:F(r['original_action_inverse_response_upper']))
 tl=max(F(prior['actual_original_action_inverse_response_lower']),F(lower['original_action_inverse_response_lower']));th=min(F(prior['actual_original_action_inverse_response_upper']),F(upper['original_action_inverse_response_upper']));dl=max(F(prior['actual_signed_gap_lower']),max(F(r['coupled_signed_gap_lower']) for r in candidates),down(F0[0][0][0]-th));dh=min(F(prior['actual_signed_gap_upper']),min(F(r['coupled_signed_gap_upper']) for r in candidates),up(F0[0][0][1]-tl));assert tl<=th and dl<=dh
 return dict(source='N0 P'+str(base),response_trial_basis=['P'+str(base+2*k) for k in range(3)],candidate_count=len(candidates),nominal_least_residual_proposal=list(map(str,least)),nominal_Galerkin_proposal=list(map(str,gal)),two_trial_nominal_minimum_retained_Dmid_residual_energy=str(twofit),three_trial_nominal_minimum_retained_Dmid_residual_energy=str(threefit),nominal_fit_is_actual_response_certificate=False,selected_inverse_lower_trial=lower,selected_inverse_upper_trial=upper,actual_original_action_inverse_response_lower=str(tl),actual_original_action_inverse_response_upper=str(th),previous_original_action_inverse_response_upper=prior['actual_original_action_inverse_response_upper'],actual_signed_gap_lower=str(dl),actual_signed_gap_upper=str(dh),previous_signed_gap_lower=prior['actual_signed_gap_lower'],original_action_inverse_upper_improved=th<F(prior['actual_original_action_inverse_response_upper']),signed_gap_lower_improved=dl>F(prior['actual_signed_gap_lower']),signed_gap_positive_certified=dl>0,actual_negative_gap_proved=dh<0)
def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  raw=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==sha,(path,'pin');data[path]=json.loads(raw) if path.endswith('.json') else raw.decode()
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 prior=get('239_exterior_band_leakage');old=get('237_two_trial_signed_response');weightedold=get('238_weighted_action_tails');baseorig=get('231_original_polynomial_action');baseaug=get('234_materialized_band_action');bounds=get('232_augmented_polynomial_action');kernel=get('115_rational_fourier_adjoint');metric=get('129_four_vector_joint_moment')
 sl=F(metric['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(metric['actual_D_Gram_entry_upper'][0][0])/(2*B);reg=list(map(F,get('46_native_archimedean_head')['regular_kernel_coefficients']));eps=F(get('46_native_archimedean_head')['regular_kernel_uniform_error_upper']);prime=get('43_native_prime_head');pi0=F(kernel['rational_pi']);pierr=F(kernel['rational_pi_error_upper']);rows=[]
 for base in [0,1]:
  r=prior['parity_exterior_tail_response_certificates'][base];ar=old['parity_two_trial_signed_response_certificates'][base];wr=weightedold['parity_weighted_tail_response_certificates'][base];bound=bounds['polynomial_augmented_action_certificates'][base];lam=F(bound['augmentation_coefficient']);U=F(bound['rational_frequency_half_bandwidth']);epsilon=F(bound['physical_Fhat_star_Fhat_to_J_star_J_operator_norm_upper']);d=base+4
  new=original_action(d,reg,prime,eps,sl,sh,reverse);print('RC240 complete original P'+str(d),flush=True)
  gram,bandcontrols=weighted.extended_columns(U,[d],pi0,pierr,reverse)[0];ac,AE,abudget=new_augmentation(d,gram,lam,epsilon,sl,sh,U)
  full=[dict(degree=x['degree'],coefficient=str(F(x['coefficient'])+F(y['coefficient'])),radius=str(up(F(x['radius'])+F(y['radius'])))) for x,y in zip(new['finite_original_D_action'],ac)];E=up((root(F(new['complete_original_action_D_error_squared_upper']))+root(AE))**2)
  columns=[];bandcols=[]
  for k in range(2):
   if k==0:original=deepcopy(baseorig['polynomial_original_action_certificates'][base]);action=baseaug['parity_materialized_augmented_action_certificates'][base]['finite_complete_augmented_D_action'];bandold=baseaug['parity_materialized_augmented_action_certificates'][base]['actual_band_Gram_column']
   else:original=deepcopy(ar['new_complete_original_action']);action=ar['new_complete_augmented_D_action'];bandold=ar['new_band_Gram_column']
   original['complete_original_action_D_error_squared_upper']=r['action_exterior_tail_refinements'][k]['original_action_D_error_squared_upper'];original['D_energy_component_squared_errors']['endpoint_omitted_output']=wr['action_tail_refinements'][k]['accepted_endpoint_omitted_output_D_energy_upper']
   columns.append(dict(original=original,finite_complete_augmented_D_action=action,augmentation_action_D_error_squared_upper=r['action_exterior_tail_refinements'][k]['refined_augmentation_action_D_error_squared_upper'],complete_augmented_action_D_error_squared_upper=r['action_exterior_tail_refinements'][k]['refined_complete_augmented_action_D_error_squared_upper']));bandcols.append([(F(x['lower']),F(x['upper'])) for x in bandold])
  columns.append(dict(original=new,finite_complete_augmented_D_action=full,augmentation_action_D_error_squared_upper=str(AE),complete_augmented_action_D_error_squared_upper=str(E)));bandcols.append(gram);degrees=[base,base+2,d];F0=[[(F(0),F(0))]*3 for _ in range(3)];Gy=[[(F(0),F(0))]*3 for _ in range(3)]
  for i in range(3):
   for k in range(i,3):
    a=trial.original_entry(degrees[i],columns[k]['original'],sl,sh);b=trial.original_entry(degrees[k],columns[i]['original'],sl,sh);v=(max(a[0],b[0]),min(a[1],b[1]));assert v[0]<=v[1];F0[i][k]=F0[k][i]=v
    a=bandcols[k][degrees[i]];b=bandcols[i][degrees[k]];lo=max(a[0],b[0]);hi=min(a[1],b[1]);assert lo<=hi;fault=up(epsilon*root(orig.mass(degrees[i])*orig.mass(degrees[k])));v=(down(lo-fault),up(hi+fault));Gy[i][k]=Gy[k][i]=v
  for i in range(2):
   assert F0[i][:2]==[(F(a),F(b)) for a,b in r['original_trial_form_intervals'][i]]
   assert Gy[i][:2]==[(F(a),F(b)) for a,b in r['frequency_trial_Gram_intervals'][i]]
  FL,FH=loewner(F0);YL,YH=loewner(Gy);GL=p.add(FL,p.scale(lam,YL));GH=p.add(FH,p.scale(lam,YH));assert p.psd(YL) and p.inv(YL) and p.psd(GL) and p.inv(GL)
  result=response(base,columns,F0,Gy,lam,F(bound['fresh_augmented_N_D_lower']),F(bound['fresh_augmented_N_D_upper']),sl,sh,r['source_inverse_response'],reverse)
  errors=[[str(3*F(columns[i]['complete_augmented_action_D_error_squared_upper'])) if i==k else '0' for k in range(3)] for i in range(3)]
  rows.append(dict(parity=r['parity'],response_trial_basis=['P'+str(x) for x in degrees],new_complete_original_action=new,new_band_Gram_column=[dict(degree=n,lower=str(a),upper=str(b)) for n,(a,b) in enumerate(gram)],new_band_controls=bandcontrols,new_augmentation_action_budget=abudget,new_augmentation_action_D_error_squared_upper=str(AE),new_complete_augmented_D_action=full,new_complete_augmented_action_D_error_squared_upper=str(E),original_trial_form_intervals=[[[str(a),str(b)] for a,b in row] for row in F0],frequency_trial_Gram_intervals=[[[str(a),str(b)] for a,b in row] for row in Gy],original_trial_form_Loewner_lower=p.ser(FL),original_trial_form_Loewner_upper=p.ser(FH),frequency_trial_Gram_Loewner_lower=p.ser(YL),frequency_trial_Gram_Loewner_upper=p.ser(YH),augmented_trial_form_Loewner_lower=p.ser(GL),augmented_trial_form_Loewner_upper=p.ser(GH),complete_three_trial_action_error_D_Gram_upper=errors,source_inverse_response=result))
 return dict(milestone='RC240',starting_commit='36e332a2f8bb8edfbabbda397561bde05cf9090c',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,actual_new_original_and_augmented_action_inputs=['P4','P5'],actual_total_action_input_count=6,actual_response_source_count=2,actual_response_source_order=['N0 P0','N0 P1'],response_trials_per_parity=3,parity_three_trial_signed_response_certificates=rows,exact_controls=controls(),all_same_parity_cross_terms_paid=True,same_parity_action_errors_assumed_orthogonal=False,shared_source_original_action_error_coupled=True,actual_complete_prime_pairs=7,both_signed_poles_retained=True,new_response_enclosures_intersected_with_RC239=True,full_639_signed_response_matrix_evaluated=False,full_signed_gap_positive_certified=False,original_full_auxiliary_norm_below_one_certified=False,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC241: use the certified source-fit diagnostics to choose richer actual trials or stronger complementary inverse bounds; full signed positivity remains required')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');a=ap.parse_args();c=run(a.replay)
 if a.replay:assert c==json.loads(a.output.read_text())
 else:a.output.write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC240 VALIDATED: complete P4/P5 actions and three-trial responses; full signed gap open',flush=True)
