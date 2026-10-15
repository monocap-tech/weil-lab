"""RC268: full-range signed Schur reduction and nonpositive-index ceiling 637."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
import validate_rpb108_rc267_rescaled_even_response as parent
ROOT=parent.ROOT;orig=parent.orig;B=parent.B;p=parent.coercive.p
up=parent.up;down=parent.down
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc267_rescaled_even_response.json':'308185c3a838e95ea59f9e8c30832e0cda44b3c4','notes/RPB108_RC267_RESCALED_EVEN_RESPONSE_20261014.md':'fcc15f5c1275eab7dd12c7e6b9db7851c48f740a'})
HELPER_PINS['scripts/validate_rpb108_rc267_rescaled_even_response.py']='db9df222dd0419268d4553c87780f3c2378e4305'

def inertia(A):
 """Exact symmetric congruence elimination, including zero diagonal pivots."""
 A=[list(map(F,row)) for row in A];positive=negative=zero=0
 assert A==p.trans(A)
 while A:
  n=len(A);i=next((i for i in range(n) if A[i][i]),None)
  if i is not None:
   order=[i]+[j for j in range(n) if j!=i];A=[[A[i][j] for j in order] for i in order];d=A[0][0]
   positive+=d>0;negative+=d<0
   A=[[A[i][j]-A[i][0]*A[0][j]/d for j in range(1,n)] for i in range(1,n)]
  else:
   ij=next(((i,j) for i in range(n) for j in range(i+1,n) if A[i][j]),None)
   if ij is None:zero+=n;break
   i,j=ij;order=[i,j]+[k for k in range(n) if k not in [i,j]];A=[[A[i][j] for j in order] for i in order];b=A[0][1];positive+=1;negative+=1
   A=[[A[i][j]-(A[i][0]*A[1][j]+A[i][1]*A[0][j])/b for j in range(2,n)] for i in range(2,n)]
 return dict(positive=positive,negative=negative,zero=zero)

def block(A,rows,cols):return [[A[i][j] for j in cols] for i in rows]
def controls():
 I=[[F(i==j) for j in range(4)] for i in range(4)]
 D=[[F([2,3,4,5][i] if i==j else 0) for j in range(4)] for i in range(4)]
 L=[[F([3,4,6,7][i] if i==j else 0) for j in range(4)] for i in range(4)];L[0][2]=L[2][0]=F(1,5);L[1][3]=L[3][1]=F(1,7)
 assert p.psd(D) and p.psd(L) and p.inv(D) and p.inv(L)
 Q=p.scale(F(2),I);K=p.mm(p.trans(Q),Q);cases=[]
 shapes={'coupled_negative':([F(1),F(2),F(1)],[F(1),F(2),F(1)]),'zero':([F(1),F(1),F(1)],[F(1),F(1),F(1)]),'mixed':([F(1),F(2),F(1)],[F(1),F(1),F(1)]),'positive':([F(2),F(1,2),F(1)],[F(2),F(1,2),F(1)])}
 for name,parities in shapes.items():
  G0=[[F(0) for j in range(4)] for i in range(4)]
  for indices,(a,b,d) in zip([[0,2],[1,3]],parities):
   i,j=indices;G0[i][i]=a;G0[i][j]=G0[j][i]=b;G0[j][j]=d
  G=p.add(G0,K);assert p.psd(G) and p.inv(G)
  N=p.mm(p.inv(D),G);N0=p.mm(p.inv(D),G0);M=p.mm(p.inv(D),L);H=p.mm(p.inv(L),G);AQ=p.mm(p.inv(L),G0)
  assert p.mm(M,H)==N and p.mm(M,N)!=p.mm(N,M)
  assert p.mm(L,AQ)==p.mm(D,N0)==G0
  Baux=p.mm(Q,p.mm(p.inv(G),p.trans(Q)));signed=p.add(G0,p.mm(G0,p.mm(p.inv(G),G0)),-1)
  assert signed==p.mm(p.trans(Q),p.mm(p.add(I,Baux,-1),Q))
  assert signed==p.mm(D,p.add(N0,p.mm(N0,p.mm(p.inv(N),N0)),-1))
  Gamma=block(signed,[0,1],[0,1]);C=block(signed,[0,1],[2,3]);Frest=block(signed,[2,3],[2,3]);assert p.psd(Gamma) and p.inv(Gamma)
  payment=p.mm(p.trans(C),p.mm(p.inv(Gamma),C));reduced=p.add(Frest,payment,-1)
  T=[[F(i==j) for j in range(4)] for i in range(4)];off=p.scale(F(-1),p.mm(p.inv(Gamma),C))
  for i in range(2):
   for j in range(2):T[i][j+2]=off[i][j]
  expected=[[F(0) for j in range(4)] for i in range(4)]
  for i in range(2):
   for j in range(2):expected[i][j]=Gamma[i][j];expected[i+2][j+2]=reduced[i][j]
  assert p.mm(p.trans(T),p.mm(signed,T))==expected
  ig=inertia(G0);isigned=inertia(signed);iaux=inertia(p.add(I,Baux,-1));ir=inertia(reduced)
  assert ig==isigned==iaux and ig['negative']==ir['negative'] and ig['zero']==ir['zero']
  assert ig['negative']+ig['zero']<=2 and isigned['positive']==2+ir['positive']
  if name=='coupled_negative':assert all(signed[i][i]>0 for i in range(4)) and ir['negative']==2 and not p.psd(signed)
  if name=='zero':assert ir['zero']==2
  if name=='mixed':assert ir['negative']==ir['zero']==1
  if name=='positive':assert ir['positive']==2
  # Certified cross-column error payments must retain their covariance.
  E=[[F(1,100),F(1,300)],[F(1,400),F(-1,100)]];Chat=p.add(C,E,-1);Glo=p.scale(F(1,2),Gamma);weight=p.inv(Glo)
  paid=p.add(p.scale(F(2),p.mm(p.trans(Chat),p.mm(weight,Chat))),p.scale(F(2),p.mm(p.trans(E),p.mm(weight,E))))
  assert p.psd(p.add(paid,payment,-1)) and p.psd(p.add(reduced,p.add(Frest,paid,-1),-1))
  cases.append(dict(name=name,original_form_inertia=ig,reduced_form_inertia=ir,positive_pivot_block=p.ser(Gamma),nonzero_cross_block=p.ser(C),signed_reduced_block=p.ser(reduced),all_signed_diagonals_positive=all(signed[i][i]>0 for i in range(4)),metric_bridge_noncommuting=True,exact_Schur_congruence=True,weighted_cross_error_payment_checked=True))
 assert inertia([[F(0),F(1)],[F(1),F(0)]])==dict(positive=1,negative=1,zero=0)
 assert -1-F(1,3)==4-F(16,3)<0 and 2+246==248 and 2+389==391
 return dict(cases=cases,zero_diagonal_two_by_two_pivot_checked=True,nullity_not_discarded=True,positive_pivots_do_not_imply_full_positivity=True,scalar_extension_negative_even_count=246,scalar_extension_negative_odd_count=389,abstract_rank_639_sharp_nonpositive_count=2+246+389,abstract_controls_not_actual_negative_Weil_directions=True)

def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  b=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sha,(path,'pin')
  if path.endswith('.json'):data[path]=json.loads(b)
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 prior=get('267_rescaled_even_response');coverage=get('230_augmentation_range_bridge');metric=get('129_four_vector_joint_moment');oldcoverage=get('112_parity_spectral_coverage')
 assert coverage['exact_full_source_range_specified'] and coverage['full_chosen_augmentation_rank']==639
 sl=F(metric['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(metric['actual_D_Gram_entry_upper'][0][0])/(2*B);assert 0<sl<=sh
 rows=[]
 for parity,(r,c) in enumerate(zip(prior['trial_rescaling_response_certificates'],coverage['parity_source_range_and_bridge_certificates'])):
  assert r['parity']==c['parity'];degrees=c['retained_native_indices'];assert degrees==list(range(parity,c['maximum_physical_polynomial_degree']+1,2)) and len(degrees)==c['rank']
  lo=F(r['actual_signed_gap_lower']);hi=F(r['actual_signed_gap_upper']);assert 0<lo<=hi and r['signed_gap_positive_certified']
  dmasslo=orig.mass(parity)*(orig.H(parity)+sl);dmasshi=orig.mass(parity)*(orig.H(parity)+sh)
  remaining=degrees[1:];assert parity not in remaining and len(remaining)==c['rank']-1
  rows.append(dict(parity=r['parity'],pivot_source='P'+str(parity),actual_signed_pivot_lower=str(lo),actual_signed_pivot_upper=str(hi),pivot_inverse_lower=str(down(1/hi)),pivot_inverse_upper=str(up(1/lo)),pivot_D_energy_lower=str(dmasslo),pivot_D_energy_upper=str(dmasshi),signed_pivot_D_normalized_lower=str(down(lo/dmasshi)),unchanged_augmentation_rank=c['rank'],remaining_Legendre_source_degrees=remaining,remaining_signed_Schur_dimension=len(remaining),original_nonpositive_spectral_dimension_upper=len(remaining),original_strict_below_one_hundredth_count_upper_unchanged=next(v['original_eigenvalues_strictly_below_one_hundredth_count_upper'] for v in oldcoverage['parity_coverage_certificates'] if v['parity']==r['parity'])))
 pairD=min(F(v['signed_pivot_D_normalized_lower']) for v in rows);assert pairD>0
 count=sum(v['remaining_signed_Schur_dimension'] for v in rows);assert count==637
 exact=controls();assert exact['abstract_rank_639_sharp_nonpositive_count']==count
 print('RC268 actual signed pivots positive; remaining even 247, odd 390; original nonpositive dimension <=637',flush=True)
 return dict(milestone='RC268',starting_commit='9fc7ab304abc506d00e38524350f1eaf62f55cb5',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,two_pivot_Schur_certificates=rows,exact_controls=exact,actual_response_source_count=2,response_trials_per_parity=4,both_actual_source_signed_pivots_positive=True,opposite_parity_pivot_pairing_zero_by_actual_reflection_symmetry=True,signed_form_identity='S=N0-N0 N^-1 N0=Kaug-Kaug N^-1 Kaug=Q*_D (I-Baux) Q',full_signed_form_supported_on_exact_augmentation_range=True,signed_form_common_pair_D_energy_floor_lower=str(pairD),signed_form_common_pair_canonical_energy_floor_lower=str(down(pairD/2)),full_range_signed_inertia_equals_original_nonpositive_inertia=True,full_chosen_augmentation_rank_unchanged=639,positive_pivot_count=2,remaining_exact_signed_Schur_dimension=count,original_full_nonpositive_spectral_dimension_upper=count,nonpositive_bound_includes_kernel_dimension=True,original_eigenvalue_threshold_one_hundredth_bound_sharpened=False,cross_column_Gram_payment_required=True,cross_column_error_covariance_payment_required=True,remaining_signed_Schur_matrix_evaluated=False,remaining_signed_Schur_positive_certified=False,full_639_signed_response_matrix_evaluated=False,full_signed_gap_positive_certified=False,original_full_auxiliary_norm_below_one_certified=False,numerical_full_frequency_Gram_conditioning_certified=False,finite_eight_canonical_inverse_width_preserved='485647/1000000',chosen_rational_augmentation_unchanged=True,Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC269: materialize or uniformly bound the residual 247-even/390-odd Schur form and its two weighted cross columns; retain all discarded-range and cross-error payments')

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');args=ap.parse_args();result=run(args.replay)
 if args.replay:assert result==json.loads(args.output.read_text())
 else:args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 print('RC268 VALIDATED: complete-range two-pivot reduction; Stage I open',flush=True)
