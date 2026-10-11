"""RC106: residual-Gram two-sided effective-head enclosure.
Original arithmetic effective-head evaluations remain unperformed.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,sys
from validate_rpb108_rc103_complement_inverse_lift import chebyshev,residual_polynomial,polyval
from validate_rpb108_rc105_inexact_inverse_recurrence import lift
from validate_rpb108_rc31_trial_riesz import mm,tr,inverse,psd
from validate_rpb108_rc65_parity_projected_residual_refinement import add,scale
from validate_rpb108_rc47_correlated_native_transport import serialize
from validate_rpb108_rc97_additional_low_mode_coverage import pd

def sandwich(Q,D,R,Y,a,b):
 r=add(R,mm(D,Y),-1);RG=mm(tr(r),r)
 C=add(add(add(Q,mm(tr(R),Y),-1),mm(tr(Y),R),-1),mm(mm(tr(Y),D),Y))
 return C,RG,add(C,scale(RG,1/a),-1),add(C,scale(RG,1/b),-1)

def run(paths,replay=False,saved=None):
 raw=[Path(p).read_bytes() for p in paths];prior,inv=map(json.loads,raw);h=[hashlib.sha256(x).hexdigest() for x in raw]
 assert prior['milestone']=='RC105' and inv['milestone']=='RC103' and prior['input_sha256'][1]==h[1]
 rows=[]
 for j,name in enumerate(['even','odd']):
  old=inv['parity_inverse_lift_certificates'][j];a=F(old['complement_spectral_lower']);b=F(old['complement_spectral_upper']);c=(b+a)/(b-a);budgets=[]
  for t in prior['parity_inexact_inverse_certificates'][j]['local_error_budgets']:
   n=t['residual_degree'];eps=1/chebyshev(n,c,replay);actual=F(t['actual_residual_common_norm_factor_upper']);assert actual==2*eps
   width=(1/a-1/b)*actual**2
   budgets.append(dict(conditional_strong_floor_target=t['strong_floor_target'],target_is_certified_lower=False,residual_degree=n,ideal_effective_head_Loewner_width_factor_relative_source_Gram=str((1/a-1/b)*eps**2),inexact_effective_head_Loewner_width_factor_relative_source_Gram=str(width),inexact_width_bound_requires_RC105_local_error_contract=True))
  # Original complement brackets, illustrative noncommuting head/coupling only.
  D=[[F(2),F(1,4)],[F(1,4),F(1)]];R=[[F(1),F(1,3)],[F(1,2),F(-1,4)]];Q=[[F(4),F(1,5)],[F(1,5),F(3)]]
  if replay:
   det=D[0][0]*D[1][1]-D[0][1]*D[1][0];Di=[[D[1][1]/det,-D[0][1]/det],[-D[1][0]/det,D[0][0]/det]]
  else:Di=inverse(D)
  Fe=add(Q,mm(mm(tr(R),Di),R),-1);scalar=add(Q,scale(mm(tr(R),R),1/a),-1);assert pd(Fe) and not psd(scalar)
  controls=[]
  for n in [9,17]:
   p,q=residual_polynomial(n,a,b);Y=lift(D,R,n,a,b,replay);assert Y==mm(polyval(q,D,replay),R)
   C,RG,lower,upper=sandwich(Q,D,R,Y,a,b)
   r=add(R,mm(D,Y),-1);assert Fe==add(C,mm(mm(tr(r),Di),r),-1)
   assert psd(add(Fe,lower,-1)) and psd(add(upper,Fe,-1)) and psd(add(lower,scalar,-1))
   assert add(upper,lower,-1)==scale(RG,1/a-1/b)
   assert pd(lower)
   # A source-Gram upper still gives a lower, but a sharp upper needs a residual lower.
   H=add(RG,[[F(1,10**8),F(0)],[F(0),F(1,10**8)]])
   conservative=add(C,scale(H,1/a),-1);assert psd(add(Fe,conservative,-1))
   # Inexact lift has the same identity; no polynomial assumptions needed.
   Yhat=add(Y,[[F(1,1000),F(-1,2000)],[F(1,3000),F(1,4000)]])
   C2,E2,L2,U2=sandwich(Q,D,R,Yhat,a,b);assert psd(add(Fe,L2,-1)) and psd(add(U2,Fe,-1))
   controls.append(dict(residual_degree=n,abstract_scalar_floor_head=serialize(scalar),abstract_effective_head_exact=serialize(Fe),abstract_correlated_lower=serialize(lower),abstract_correlated_upper=serialize(upper),abstract_residual_Gram=serialize(RG),positive_correlated_lower_while_scalar_floor_rejects=True,inexact_lift_sandwich_verified=True))
  # Upper enclosure can certify a negative direction, separately from failure of lower.
  Qneg=add(Q,[[F(5),F(0)],[F(0),F(0)]],-1);C0,E0,L0,U0=sandwich(Qneg,D,R,Y,a,b);assert U0[0][0]<0
  rows.append(dict(parity=name,complement_spectral_lower=str(a),complement_spectral_upper=str(b),inherited_inexact_width_budgets=budgets,abstract_noncommuting_controls=controls,abstract_upper_enclosure_certifies_negative_direction=True,control_scope='illustrative matrices only, not the original arithmetic head'))
 out=dict(milestone='RC106',status='PASS',input_sha256=h,arithmetic='exact Fraction; no floating acceptance',effective_head_two_sided_analytic_proof_supplied=True,
 general_lift_identity='For any lift Y of R=P_E A_Q J, r=R-DY and C=J*A_H J-R*Y-Y*R+Y*DY, J*F J=C-r*D^(-1)r.',
 exact_residual_sandwich='C-alpha^(-1)r*r <= J*F J <= C-b^(-1)r*r; the interval width is (alpha^(-1)-b^(-1))r*r.',
 rigorous_enclosure_contract='If C_lo<=C<=C_hi and H_lo<=r*r<=H_hi, then C_lo-H_hi/alpha <= J*F J <= C_hi-H_lo/b. Without a certified residual lower, use H_lo=0.',
 ideal_polynomial_scalar_dominance='For Y=q(D)R and residual p(D)R with ||p(D)||<=epsilon<1, lower-(J*A_H J-R*R/alpha)=R*(1-p(D)^2)(D-alpha I)(alpha D)^(-1)R>=0.',
 ideal_width_bound='The two-sided exact-compression width is <=(alpha^(-1)-b^(-1))epsilon^2 G whenever R*R<=G.',
 inexact_width_scope='RC105 bounds the mathematical residual width for an implemented lift by replacing epsilon with epsilon+b eta H_n. Certified C and residual enclosure errors add separately; no actual width is computed here.',
 strong_floor_interface='On any actual strong subspace J with canonical metric M, a certified C_lo-H_hi/alpha>=beta M proves the needed exact effective strong floor. Every participating complement lift and projection must be original-operator certified.',
 inertia_interface='For a complete head, a positive lower proves positivity. A negative Rayleigh direction in a certified upper proves negativity. Matching endpoint inertia certifies head inertia by eigenvalue monotonicity. A lower failing positivity alone proves neither negativity nor a null.',
 parity_effective_head_sandwich_certificates=rows,known_corrected_positive_span_dimension=6,original_operator_nonpositive_spectral_dimension_upper=1244,new_source_integrals_evaluated=0,actual_effective_head_compressions_evaluated=False,actual_operator_actions_performed=False,actual_lifted_response_Gram_certified=False,strong_head_block_lower_certified=False,complete_nonpositive_mode_coverage_certified=False,matrix_Schur_positivity_certified=False,whole_aperture_positivity_extended=False,RH=False,F4=False)
 if saved is not None:assert out==saved
 return out

if __name__=='__main__':
 base=Path(__file__).parent.parent/'certificates';defaults=[base/'rpb108_rc105_inexact_inverse_recurrence.json',base/'rpb108_rc103_complement_inverse_lift.json']
 if len(sys.argv)>1 and sys.argv[1]=='--replay':
  run(sys.argv[3:] or defaults,True,json.loads(Path(sys.argv[2]).read_text()));print('PASS: independent inverse and polynomial replay; residual sandwiches, scalar dominance and signed controls')
 else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
