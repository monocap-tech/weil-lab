"""RC251: materialize the complete coupled residual through degree 256."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import argparse,hashlib,json
import validate_rpb108_rc250_coupled_original_output_tail as parent
direct=parent.direct;material=direct.material;band=material.band
orig=parent.orig;p=parent.p;B=parent.B;up=parent.up;down=parent.down;root=parent.root;rootdown=parent.rootdown
# Scaled inverse-power moments can be far smaller than 10^-60. Preserve
# exact interval endpoints between the explicit outward-grid operations.
def ip(x):return x,x
def ia(a,b):return a[0]+b[0],a[1]+b[1]
def im(a,b):
 v=[x*y for x in a for y in b];return min(v),max(v)
def isc(a,s):
 v=[a[0]*s,a[1]*s];return min(v),max(v)
def neg(a):return -a[1],-a[0]
ROOT=Path(__file__).resolve().parents[1];CUT=256
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc250_coupled_original_output_tail.json':'a050c85fbfdd68071ad5d265165c6ade1d2cdcf5','notes/RPB108_RC250_COUPLED_ORIGINAL_OUTPUT_TAIL_20261014.md':'1a6a8ddbd65dcf4d0ba1aeb273989e547fe99e43'})
HELPER_PINS['scripts/validate_rpb108_rc250_coupled_original_output_tail.py']='69b12b6eb2259e886c3ce1e6134221918fd00727'
def outer_grid(v,digits):
 grid=10**digits;lo,hi=v
 result=(F((lo.numerator*grid)//lo.denominator,grid),F(-((-hi.numerator*grid)//hi.denominator),grid))
 assert result[0]<=lo<=hi<=result[1];return result
def ibp_parts(m,L,z,powers):
 # Homogeneous Horner evaluation of the exact finite inverse-power series.
 zn=z.numerator;zd=z.denominator;rising=[1]
 for k in range(L-1):rising.append(rising[-1]*(m+k))
 rr=ii=0
 for k in range(L-1,-1,-1):
  rr*=zd;ii*=zd;v=rising[k]*powers[L-1-k]
  if k%4==0:ii+=v
  elif k%4==1:rr+=v
  elif k%4==2:ii-=v
  else:rr-=v
 denominator=2*powers[L-1]
 return F(rr,denominator),F(ii,denominator),F(rising[-1]*zd**(L-1),denominator)
def extended_controls():
 result=parent.controls()
 tiny=(F(1,10**900),F(2,10**900));assert isc(tiny,10**600)==(F(1,10**300),F(2,10**300))
 for m,L,z in [(2,12,F(431,3)),(65,16,F(443)),(323,20,F(887,2))]:
  rr,ii,rem=ibp_parts(m,L,z,[(2*z.numerator)**k for k in range(L)]);a=b=F(0);r=1
  for k in range(L):
   v=F(r,2**(k+1))/z**k
   if k%4==0:b+=v
   elif k%4==1:a+=v
   elif k%4==2:b-=v
   else:a-=v
   r*=m+k
  assert rr==a and ii==b and rem==F(r,2**L)*z**(1-L)/F(m+L-1)
 result['homogeneous_Horner_against_direct_finite_series_and_remainder']=True
 return result
def extended_band(a,parity,U,pi0,pierr,reverse):
 oldcut=band.CUT
 try:
  band.CUT=CUT;aa,bb=band.spherical_polynomials()
 finally:band.CUT=oldcut
 A=[F(0)]*66;C=[F(0)]*66
 for n,c in enumerate(a):
  if not c:continue
  sign=-1 if ((n-parity)//2)%2 else 1
  for k,v in enumerate(aa[n]):A[k]+=sign*c*v
  for k,v in enumerate(bb[n]):C[k]+=sign*c*v
 z=2*pi0*B*U;assert z>400;turns=int(2*B*U+F(1,2));theta=2*pi0*(2*B*U-turns);assert abs(theta)<F(22,7)
 cv=sum(((-1)**k*theta**(2*k)/factorial(2*k) for k in range(41)),F(0));sv=sum(((-1)**k*theta**(2*k+1)/factorial(2*k+1) for k in range(40)),F(0));phaseerr=abs(theta)**81/factorial(81)+2*abs(turns)*pierr
 cosine=outer_grid(ia(ip(cv),(-up(phaseerr),up(phaseerr))),120);sine=outer_grid(ia(ip(sv),(-up(phaseerr),up(phaseerr))),120)
 L=240 if reverse else 224;moments={};static={};powers=[1];inverse=[F(1)]
 for k in range(1,max(L,CUT+68)):
  powers.append(powers[-1]*(2*z.numerator));inverse.append(inverse[-1]/z)
 for m in range(2,CUT+68):
  rr,ii,rem=ibp_parts(m,L,z,powers);Rr=outer_grid(ia(ip(rr),(-up(rem),up(rem))),120);Ii=outer_grid(ia(ip(ii),(-up(rem),up(rem))),120)
  moments[m]=(outer_grid(isc(ia(im(cosine,Rr),neg(im(sine,Ii))),inverse[m]),1000),outer_grid(isc(ia(im(sine,Rr),im(cosine,Ii)),inverse[m]),1000))
  static[m]=outer_grid(ip(inverse[m-1]/F(m-1)),1000)
 print('RC251 '+('even' if parity==0 else 'odd')+' oscillatory moments complete',flush=True)
 pil=pi0-pierr;assert pil>3 and pi0+pierr<4
 S=sum(map(abs,a),F(0));fault=up(S*(4*B/pil*(2*B*U*pierr)+8*B*pierr/(pil*pi0)));gram=[]
 for n in range(CUT+1):
  if n%2!=parity:gram.append((F(0),F(0)));continue
  pa=orig.product(aa[n],A);pb=orig.product(bb[n],C);pc=band.polyadd(orig.product(aa[n],C),orig.product(bb[n],A));size=max(len(pa),len(pb),len(pc));pa+=[F(0)]*(size-len(pa));pb+=[F(0)]*(size-len(pb));pc+=[F(0)]*(size-len(pc));total=ip(F(0))
  degrees=list(range(2,size));degrees=degrees[::-1] if reverse else degrees
  for m in degrees:
   c0=(pa[m]+pb[m])/2;cc=(pb[m]-pa[m])/2;cs=pc[m]/2
   if c0:total=ia(total,isc(static[m],c0))
   if cc:total=ia(total,isc(moments[m][0],cc))
   if cs:total=ia(total,isc(moments[m][1],cs))
  sign=-1 if ((n-parity)//2)%2 else 1;tail=ia(isc(total,sign*4*B/pi0),(-fault,fault));full=orig.mass(n)*(a[n] if n<len(a) else F(0));gram.append(band.outer24(ia(ip(full),neg(tail))))
  if n in [63,64,127,128,191,192,255,256]:print('RC251 '+('even' if parity==0 else 'odd')+' band output through '+str(n),flush=True)
 return gram,dict(generation_integration_by_parts_terms=224,replay_integration_by_parts_terms=240,pi_lower_limit_prefactor_error_upper=str(fault),phase_error_upper=str(up(phaseerr)),phase_and_IBP_parts_outward_grid='1/10^120',scaled_oscillatory_and_static_moment_outward_grid='1/10^1000',all_intermediate_interval_containments_checked=True,homogeneous_Horner_exact_series=True,stored_band_Gram_grid='1/10^24',spherical_polynomial_boundary_derivative_controls_through_degree=CUT,all_input_modes_combined_before_output_pairing=True)
def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  b=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sha,(path,'pin');data[path]=json.loads(b) if path.endswith('.json') else b.decode()
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 prior=get('250_coupled_original_output_tail');old=get('248_direct_coupled_residual');forms=get('247_materialized_four_trial_response');bounds=get('232_augmented_polynomial_action');metric=get('129_four_vector_joint_moment');kernel=get('115_rational_fourier_adjoint')
 sl=F(metric['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(metric['actual_D_Gram_entry_upper'][0][0])/(2*B);pi0=F(kernel['rational_pi']);pierr=F(kernel['rational_pi_error_upper']);rows=[]
 for parity,r in enumerate(old['selected_direct_residual_certificates']):
  previous=prior['coupled_output_tail_response_certificates'][parity];proof=previous['coupled_original_output_tail_certificate'];a=list(map(F,r['exact_Z_input_Legendre_coefficients']));b=bounds['polynomial_augmented_action_certificates'][parity];lam=F(b['augmentation_coefficient']);U=F(b['rational_frequency_half_bandwidth']);mu=F(b['fresh_augmented_N_D_lower']);nu=F(b['fresh_augmented_N_D_upper'])
  gram,controls=extended_band(a,parity,U,pi0,pierr,reverse);output=[isc(g,1/orig.mass(n)) for n,g in enumerate(gram)]
  qlo=qhi=F(0)
  for n,c in enumerate(a):
   values=[c*gram[n][0],c*gram[n][1]];qlo+=min(values);qhi+=max(values)
  partition=r['band_input_energy_partition_certificate'];qlo=max(qlo,F(partition['physical_band_energy_lower']));qhi=min(qhi,F(partition['physical_band_energy_upper']));assert 0<qlo<=qhi
  captured=sum((orig.mass(n)*band.minabs(g)**2 for n,g in enumerate(output)),F(0));physical_tail=up(qhi-captured);assert physical_tail>=0
  first=257 if parity else 258;augmentation_tail=up(lam*lam*physical_tail/(orig.H(first)+sl));original_tail=F(proof['combined_original_D_energy_beyond_256_upper'])
  high={row['degree']:row for row in proof['combined_original_model_output_129_through_256']};original=[];residual=[];finite=F(0);low_preserved=True
  for n,g in enumerate(output):
   if n<=128:o=r['finite_original_combination_D_action'][n];oc=F(o['coefficient']);orr=F(o['radius'])
   elif n%2!=parity:oc=orr=F(0)
   else:
    row=high[n];v=F(row['combined_model_output_numerator_center']);rad=F(row['combined_model_output_numerator_radius']);values=[x/(orig.H(n)+s) for x in [v-rad,v+rad] for s in [sl,sh]];lo=min(values);hi=max(values);oc=down((lo+hi)/2);orr=up(max(oc-lo,hi-oc))
   original.append(dict(degree=n,coefficient=str(oc),radius=str(orr)))
   values=[lam*x/(orig.H(n)+s) for x in g for s in [sl,sh]];lo=min(values);hi=max(values);ac=down((lo+hi)/2);ar=max(ac-lo,hi-ac);c=oc-ac;rad=up(orr+ar)
   if n<=128:
    oldrow=r['complete_direct_residual_center'][n];oldc=F(oldrow['coefficient']);oldrad=F(oldrow['radius']);assert max(c-rad,oldc-oldrad)<=min(c+rad,oldc+oldrad)
    low_preserved=low_preserved and c==oldc and rad==oldrad
   residual.append(dict(degree=n,coefficient=str(c),radius=str(rad)));finite+=orig.mass(n)*(orig.H(n)+sh)*rad*rad
  assert all(F(row['coefficient'])==F(row['radius'])==0 for n,row in enumerate(residual) if n%2!=parity)
  omitted=up((root(original_tail)+root(augmentation_tail))**2);fault=F(r['original_combination_model_fault_D_norm_upper']);rational=F(r['rational_augmentation_comparison_D_error_squared_upper']);E=up((root(up(finite+omitted))+fault+root(rational))**2)
  terms=list(range(CUT+1));terms=terms[::-1] if reverse else terms
  nl=sum((orig.mass(n)*(orig.H(n)+sl)*F(residual[n]['coefficient'])**2 for n in terms),F(0));nh=sum((orig.mass(n)*(orig.H(n)+sh)*F(residual[n]['coefficient'])**2 for n in terms),F(0));rl=down(max(F(0),rootdown(nl)-root(E))**2);rh=up((root(nh)+root(E))**2)
  pr=forms['parity_materialized_four_trial_response_certificates'][parity];F0=[[(F(a),F(b)) for a,b in row] for row in pr['original_trial_form_intervals']];Gy=[[(F(a),F(b)) for a,b in row] for row in pr['frequency_trial_Gram_intervals']];y=list(map(F,r['selected_trial_coefficients']))
  cl,ch=direct.center_intervals(F0,Gy,y,lam);tl=down(cl+rl/nu);th=up(ch+rh/mu);u=[1-y[0],-y[1],-y[2],-y[3]];ql,qh=direct.quadratic(F0,u);al,ah=direct.quadratic(Gy,y);dl=down(ql+lam*al-rh/mu);dh=up(qh+lam*ah-rl/nu)
  actualtl=max(F(previous['actual_original_action_inverse_response_lower']),tl);actualth=min(F(previous['actual_original_action_inverse_response_upper']),th);actualdl=max(F(previous['actual_signed_gap_lower']),dl,down(F0[0][0][0]-actualth));actualdh=min(F(previous['actual_signed_gap_upper']),dh,up(F0[0][0][1]-actualtl));assert actualtl<=actualth and actualdl<=actualdh
  rows.append(dict(parity=r['parity'],source=r['source'],selected_trial_coefficients=r['selected_trial_coefficients'],extended_band_Gram_column=[dict(degree=n,lower=str(lo),upper=str(hi)) for n,(lo,hi) in enumerate(gram)],band_materialization_controls=controls,independent_band_input_partition_origin='RC248 same exact Z',intersected_physical_band_input_form_lower=str(down(qlo)),intersected_physical_band_input_form_upper=str(up(qhi)),captured_band_output_physical_energy_lower=str(down(captured)),band_output_beyond_256_physical_energy_upper=str(physical_tail),augmentation_D_omitted_output_energy_upper=str(augmentation_tail),original_combination_D_omitted_output_energy_upper=str(original_tail),extended_original_model_D_action=original,extended_complete_direct_residual_center=residual,retained_low_center_and_radii_exactly_preserved=low_preserved,retained_low_model_intervals_intersect_previous=True,residual_finite_rounding_D_energy_upper=str(up(finite)),residual_model_omitted_output_D_energy_upper=str(omitted),unchanged_original_model_fault_D_norm_upper=str(fault),unchanged_rational_augmentation_comparison_D_error_squared_upper=str(rational),complete_direct_residual_D_error_squared_upper=str(E),previous_direct_residual_D_error_squared_upper=previous['complete_direct_residual_D_error_squared_upper'],complete_direct_residual_actual_D_energy_lower=str(rl),complete_direct_residual_actual_D_energy_upper=str(rh),direct_inverse_response_lower=str(tl),direct_inverse_response_upper=str(th),direct_signed_gap_lower=str(dl),direct_signed_gap_upper=str(dh),actual_original_action_inverse_response_lower=str(actualtl),actual_original_action_inverse_response_upper=str(actualth),previous_original_action_inverse_response_upper=previous['actual_original_action_inverse_response_upper'],actual_signed_gap_lower=str(actualdl),actual_signed_gap_upper=str(actualdh),original_action_inverse_upper_improved=actualth<F(previous['actual_original_action_inverse_response_upper']),signed_gap_positive_certified=actualdl>0,actual_negative_gap_proved=actualdh<0))
 return dict(milestone='RC251',starting_commit='2ab55d9c6efc63d45eeb697738a60f6ed1c6fdf7',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,actual_response_source_count=2,response_trials_per_parity=4,extended_coupled_residual_response_certificates=rows,source_and_trial_spaces_unchanged=True,retained_direct_residual_output_degree=CUT,original_global_and_rational_augmentation_model_faults_paid=True,exact_controls=extended_controls(),new_response_enclosures_intersected_with_RC250=True,full_639_signed_response_matrix_evaluated=False,full_signed_gap_positive_certified=False,original_full_auxiliary_norm_below_one_certified=False,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC252: refine remaining direct residual tails or strengthen residual inverse estimates; full signed positivity remains required')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');a=ap.parse_args();c=run(a.replay)
 if a.replay:assert c==json.loads(a.output.read_text())
 else:a.output.write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC251 VALIDATED: extended complete coupled residuals; full signed gate open',flush=True)
