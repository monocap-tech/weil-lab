"""RC96: exact correlated completion budget and abstract coverage obstructions.

This validates consequences of RC94/95; it does not recompute their source
integrals and does not certify a strong block of the original Weil form.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,sys
from validate_rpb108_rc31_trial_riesz import mm,tr,inverse,psd

def mat(a):return [[F(x) for x in r] for r in a]
def ser(a):return [[str(x) for x in r] for r in a]
def sub(a,b,s=F(1)):return [[x-s*y for x,y in zip(r,t)] for r,t in zip(a,b)]
def quad(a,x):return sum((x[i]*a[i][j]*x[j] for i in range(len(x)) for j in range(len(x))),F(0))
def arrow(L,c,d):return [L[0]+[c[0]],L[1]+[c[1]],[c[0],c[1],d]]
def positive(a):return a[0][0]>0 and a[0][0]*a[1][1]-a[0][1]**2>0

def block(L,parity,replay=False):
 assert L==tr(L) and positive(L)
 a,b,d=L[0][0],L[0][1],L[1][1];det=a*d-b*b;p=det/a;r=b/a
 if replay:
  # Adjugate inversion and a different triangular identity.
  Li=[[d/det,-b/det],[-b/det,a/det]]
  E=[[F(1),-r],[F(0),F(1)]]
  assert mm(mm(tr(E),L),E)==[[a,F(0)],[F(0),p]]
 else:Li=inverse(L)
 assert mm(L,Li)==[[F(1),F(0)],[F(0),F(1)]]
 # The exact inverse quadratic is x0^2/a+(x1-r*x0)^2/p.
 B=[[1/a+r*r/p,-r/p],[-r/p,1/p]];assert B==Li
 # Matrix-valued tests: U at one half of the budget, and at its boundary.
 U=[[x/2 for x in row] for row in L];assert positive(sub(L,U))
 assert not positive(sub(L,L)) and psd(sub(L,L))
 # Independent exact rank-one inverse-penalty identity.
 c=[a,b];rank=[[x*y/a for y in c] for x in c]
 assert psd(sub(L,rank)) and not positive(sub(L,rank))
 null=arrow(L,c,a);negative=arrow(L,[2*x for x in c],a)
 witness=[F(1),F(0),F(-1)]
 assert psd(null) and quad(null,witness)==0
 assert quad(negative,witness)==-2*a and not psd(negative)
 missing=arrow(L,[F(0),F(0)],F(-1));assert quad(missing,[0,0,1])==-1
 # A passing nonzero cross block (same strong diagonal) has exact slack.
 passing=arrow(L,[x/2 for x in c],a)
 assert psd(passing) and positive(sub(L,rank,F(1,4)))
 # Four-response reduction: metric-aware projection, no strong basis rows.
 # This illustrative metric is not an inherited canonical Gram.
 M=[[F(2),0,0],[0,F(3),0],[0,0,F(7)]]
 Mi=[[F(1,2),0,0],[0,F(1,3),0],[0,0,F(1,7)]]
 response=mm(mm(passing,Mi),passing)
 capture=mm(mm(L,[[F(1,2),0],[0,F(1,3)]]),L)
 response_weak=[row[:2] for row in response[:2]]
 residual=sub(response_weak,capture)
 expected=[[x*y/28 for y in c] for x in c]
 assert residual==expected and psd(residual)
 if replay:
  # Direct strong component of T w in the metric diag(2,3,7).
  strong_components=[x/14 for x in c]
  assert residual==[[7*x*y for y in strong_components] for x in strong_components]
 return dict(parity=parity,corrected_weak_lower=ser(L),inverse_corrected_weak_lower=ser(Li),
  LDL_first_pivot=str(a),LDL_second_pivot=str(p),cross_correlation_slope=str(r),
  axis_0_cross_amplitude_squared_per_unit_strong_floor=str(1/Li[0][0]),
  axis_1_cross_amplitude_squared_per_unit_strong_floor=str(1/Li[1][1]),
  aligned_cross_amplitude_squared_per_unit_strong_floor=str(a),
  cross_budget_half_L_passes=True,cross_budget_equal_L_has_no_strict_margin=True,
  abstract_uncontrolled_strong_direction=dict(matrix=ser(missing),negative_witness=['0','0','1'],quadratic_value='-1'),
  abstract_cross_boundary=dict(matrix=ser(null),null_witness=list(map(str,witness)),quadratic_value='0'),
  abstract_cross_failure_with_positive_diagonal_blocks=dict(matrix=ser(negative),negative_witness=list(map(str,witness)),quadratic_value=str(-2*a)),
  abstract_nonzero_cross_pass=dict(matrix=ser(passing),inverse_penalty_fraction='1/4'),
  illustrative_metric_aware_response_Gram=ser(response_weak),
  illustrative_weak_capture_Gram=ser(capture),
  illustrative_strong_response_Gram=ser(residual),
  response_projection_identity_verified=True)

def run(paths,replay=False):
 raw=[Path(p).read_bytes() for p in paths];prior,old=map(json.loads,raw)
 hashes=[hashlib.sha256(x).hexdigest() for x in raw]
 assert prior['milestone']=='RC95' and old['milestone']=='RC94'
 assert prior['input_sha256'][0]==hashes[1]
 alpha=F(prior['inherited_1250_complement_floor']);assert alpha==F(247,2500)==F(old['inherited_1250_complement_floor'])
 assert prior['full_four_known_weak_span_corrected_positive_definite']
 assert prior['parity_orthogonality_analytic_proof_supplied']
 rows=[]
 for parity in ['even','odd']:
  z=next(b for b in old['weak_source_block_certificates'] if b['parity']==parity)
  Q=mat(z['updated_actual_original_weak_head_Loewner_lower'])
  G=mat(prior['actual_rank_1250_even_weak_source_coupling_Gram_upper'] if parity=='even' else z['actual_rank_1250_weak_source_coupling_Gram_upper_via_nesting'])
  L=mat(prior['corrected_even_weak_block_Loewner_lower'] if parity=='even' else z['corrected_weak_block_Loewner_lower'])
  assert L==sub(Q,G,1/alpha) and psd(G) and positive(Q)
  rows.append(block(L,parity,replay))
 return dict(milestone='RC96',status='PASS',input_sha256=hashes,arithmetic='exact Fraction; no floating acceptance',
  head_rank=1250,known_weak_dimension=4,uncontrolled_head_dimension=1246,original_operator_nonpositive_spectral_dimension_upper=1246,
  codimension_index_bound_analytic_proof_supplied=True,
  abstract_index_bound_saturation_negative_direction_count=1246,
  inherited_complement_floor=str(alpha),
  parity_completion_budgets=rows,
  conditional_completion_theorem='If D=T_SS >= beta M_S > 0 and U >= C M_S^(-1) C* with beta L-U > 0, then T > 0; C=T_WS for the full corrected head.',
  conditional_trace_test='trace(L^(-1) U) < beta is sufficient; for each parity the inverse quadratic is c0^2/a+(c1-(b/a)c0)^2/p.',
  four_response_Gram_reduction='U_actual=W* T P_H T W - B M_W^(-1) B, where B=W* T W and M_W=W*W in the canonical metric; U_actual=C M_S^(-1) C*.',
  response_projection_identity_analytic_proof_supplied=True,
  dense_strong_basis_evaluation_required_by_completion_theorem=False,
  actual_four_response_Gram_certified=False,
  canonical_strong_metric_required=True,original_head_cross_alone_is_insufficient=True,
  compact_finite_rank_countermodel_construction_supplied=True,
  countermodel_scope='Only known corrected weak lower, parity, complement floor, compact embedding and bounded remainder. Not the original arithmetic operator, its norm bounds, or all inherited entry enclosures.',
  coverage_and_cross_are_independent_obligations=True,
  complete_weak_mode_coverage_certified=False,strong_head_block_certified=False,
  weak_strong_cross_block_certified=False,matrix_Schur_positivity_certified=False,
  whole_aperture_positivity_extended=False,RH=False,F4=False)

if __name__=='__main__':
 base=Path(__file__).parent.parent/'certificates'
 defaults=[base/'rpb108_rc95_jump_aware_even_source_tail.json',base/'rpb108_rc94_weak_source_capture_128.json']
 if len(sys.argv)>1 and sys.argv[1]=='--replay':
  saved=json.loads(Path(sys.argv[2]).read_text());assert run(sys.argv[3:] or defaults,True)==saved
  print('PASS: inherited corrected blocks, adjugate inverse, triangular congruence, cross budgets, and exact abstract null/negative witnesses')
 else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
