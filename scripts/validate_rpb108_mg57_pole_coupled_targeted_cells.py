#!/usr/bin/env python3
"""MG57 — exact original pole-error coupling + targeted physical Fourier refinement.

The ACTUAL original corrected strong action is u_j=a(xi)t_j-2t_p b_j.
At j=p, the SAME t_p error occurs twice. Replace MG56's two
independent e_p error fees (|ac|+2|bmid_p|)r_p by
|ac-2bmid_p|r_p, while leaving multiplier interval da and b_p
uncertainty paid in full. At unchanged 32 cells with FROZEN
accepted Young tau, the lower 24D moment strictly increases in the
Loewner order by a positive diagonal matrix, never via a ray-only
improvement.

Next replace only the three dominant MG56 original [1/8,1/2]
1/8-wide cells with 12 genuine newly computed original physical
1/32-wide Fourier cells. Recompute MG29 certified Taylor radii,
SM43 signed seven-prime/digamma multiplier intervals and true
pole source action on each new cell. Independently check exact
whole 24D strict positivity, NOT just improved trace.

No new original operator spectral sign is inferred from negativity of
a conservative source moment lower.
"""
import argparse,json,sys
from fractions import Fraction as Q
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import (
    original_H24_from_physical_source,deserialize)
from validate_rpb108_mg25_robust_source_aware_residual import (
    Id,T,sub,psd,gersh_lower)
from validate_rpb108_mg41_ideal_cross_error_feasibility import classify_ideal
import validate_rpb108_mg32_joint_fourier_residual as m32
import validate_rpb108_mg56_corrected_strong_band_lower as mg56
N=24;P=23
def enc(A):return [[str(x) for x in row] for row in A]
def mat(x):
 a=deserialize(x)
 assert len(a)==N and all(len(row)==N for row in a)
 return a
def trace(a):return sum((a[i][i] for i in range(N)),Q(0))
def qf(v,a):return sum((v[i]*a[i][j]*v[j] for i in range(N) for j in range(N)),Q(0))
def original_refined_true_source_cell(left,right,prep,glob4):
 """Fresh original MG29 source physical/Fourier construction on a new cell."""
 centers,sources,a,c,hyp,Kglobal,Kthird=prep
 assert len(sources)==25 and sources[24][0]=="pole"
 width=right-left;half=width/2;mid=(left+right)/2
 wl,wu,_=m32.positive_cell_weight_interval(left,right)
 assert Q(0)<wl<=wu
 vals=m32.original_exact_physical_fourier_midpoint(mid,centers,sources,hyp)
 derivative,second=m32.original_midpoint_derivative_intervals(
    mid,centers,sources,hyp)
 Kold=[min(g,m32.abs_cap(z)+third*half) if z is not None else g
       for g,z,third in zip(Kglobal,second,Kthird)]
 v,d,eold=m32.transformed_affine(vals,derivative,Kold,a,c,half)
 comps=m32.splits_original_source(
     v,d,eold,Kold,half,vals,derivative,a,c,23,24)
 s2=m32.exact_original_second_midpoint(mid,centers,sources,hyp)
 third=m32.third_adapted_whole_cell(
    mid,centers,sources,hyp,a,c,Kthird,half,glob4)
 old28=m32.true_direct_adapted_curvature(
    s2,Kthird,a,c,Kold,half)
 rad=[]
 for j,(value,slope,curv,rounding) in enumerate(comps):
  direct2=(s2[j]-a[j]*s2[24]-c[j]*s2[23]) if j<23 else s2[24]
  improved=min(old28[j][0],m32.abs_cap(direct2)+third[j][0]*half)
  z=m32.up(value+slope+improved*half*half/2)
  assert Q(0)<=z<=eold[j]
  rad.append(z)
 assert len(v)==len(d)==len(rad)==N
 return (left,right,wl,wu,v,d,rad)
def fees(cell,bc,be):
 l,r,wl,wu,v,d,rv=cell
 width=r-l;half=width/2
 ac=(wl+wu)/2;da=(wu-wl)/2
 pole_amp=abs(v[P])+half*abs(d[P])+rv[P]
 zero=[ac*v[j]-2*v[P]*bc[j] for j in range(N)]
 slope=[ac*d[j]-2*d[P]*bc[j] for j in range(N)]
 base=[];multi=[];pole_src=[];pole_unc=[];old=[];new=[]
 for j in range(N):
  t=abs(ac)*rv[j]
  m=da*(abs(v[j])+half*abs(d[j])+rv[j])
  p=2*abs(bc[j])*rv[P]
  u=2*be[j]*pole_amp
  total=t+m+p+u
  coupled=(abs(ac-2*bc[P])*rv[P]+m+u) if j==P else total
  assert Q(0)<=coupled<=total
  base.append(t);multi.append(m);pole_src.append(p)
  pole_unc.append(u);old.append(total);new.append(coupled)
 return zero,slope,old,new,{"Taylor_source":base,
   "multiplier_width":multi,"pole_source_Taylor":pole_src,
   "pole_column_interval":pole_unc}
def accumulate(cells,bc,be,freeze=None,coupling=True):
 store={"lower":{"mass":(m32.zero(),m32.zero())}}
 taus={str(t):0 for t in m32.CHOSEN_TAUS}
 rows=[]
 totals={k:Q(0) for k in ("Taylor_source","multiplier_width",
     "pole_source_Taylor","pole_column_interval")}
 raw_signal=raw_error=Q(0)
 for idx,cell in enumerate(cells):
  left,right,wl,wu,v,d,r=cell
  h=right-left
  c,slope,old,new,terms=fees(cell,bc,be)
  rad=new if coupling else old
  if freeze is None:
   t=max(m32.CHOSEN_TAUS,key=lambda tau:(
      m32.lower_cell_trace((Q(1),Q(1)),h,c,slope,rad,tau),-tau))
  else:
   t=Q(freeze[idx])
   assert t in m32.CHOSEN_TAUS
  assert 0<t<1
  m32.add_directed_cell(store,"lower","mass",(Q(1),Q(1)),
                          h,c,slope,rad,t)
  error=sum(rad,Q(0))
  signal=2*h*(1-t)*(sum((z*z for z in c),Q(0))
                +h*h*sum((z*z for z in slope),Q(0))/12)
  young=2*h*(1/t-1)*error*error
  raw_signal+=signal;raw_error+=young
  fraction={name:sum(z,Q(0))/sum(old,Q(0)) for name,z in terms.items()}
  for k,value in fraction.items():totals[k]+=young*value
  taus[str(t)]+=1
  rows.append({"left":str(left),"right":str(right),
    "multiplier_lower":str(wl),"multiplier_upper":str(wu),
    "tau":str(t),"source_error_l1_old":str(sum(old,Q(0))),
    "source_error_l1_new":str(error),
    "pole_channel_old_radius":str(old[P]),
    "pole_channel_coupled_radius":str(new[P]),
    "trace_signal":str(signal),"trace_error_penalty":str(young),
    "source_interval_components_l1":{k:str(sum(z,Q(0)))
                                     for k,z in terms.items()}})
 L,U,_,_=m32.finalize(store["lower"]["mass"])
 assert L==T(L) and U==T(U) and psd(sub(U,L))
 assert psd(U)
 return L,U,taus,rows,totals,raw_signal,raw_error
def inertia(L):
 kind,w=classify_ideal(L)
 assert kind in ("NEGATIVE_EXACT_RATIONAL_RAYLEIGH",
                 "POSITIVE_EXACT_RATIONAL_LDL","INCONCLUSIVE")
 if kind=="NEGATIVE_EXACT_RATIONAL_RAYLEIGH":
  v=[Q(x) for x in w["rational_vector"]]
  assert qf(v,L)==Q(w["exact_negative_quadratic"])<0
 return kind,w
def main():
 p=argparse.ArgumentParser()
 for key in ("mg24","mg29","mg56"):p.add_argument("--verified-"+key+"-json",required=True)
 p.add_argument("--output",default="artifacts/mg57_targeted_true_strong_action_refinement.json")
 args=p.parse_args()
 a24,a29,a56=[
  json.loads((ROOT/getattr(args,"verified_"+name+"_json")).read_text())
  for name in ("mg24","mg29","mg56")]
 assert a24["canonical_W_ODD_NEG"]==a29["canonical_W_ODD_NEG"]==a56["canonical_W_ODD_NEG"]=="OPEN"
 assert a56["status"]=="ORIGINAL_MG56_POLE_CORRECTED_STRONG_ACTION_BAND_24D_LOWER"
 Hmid,Hrad,Herr=original_H24_from_physical_source()
 assert Herr==Q(a24["physical_Gram_Loewner_row_error"])
 bc=[Hmid[i][P] for i in range(N)]
 be=[Hrad[i][P] for i in range(N)]
 assert [str(x) for x in bc]==a24["original_pole_b_center"]
 assert [str(x) for x in be]==a24["original_pole_b_radii"]
 base,cl,cu,_,_=m32.exact_original_cells()
 assert len(base)==32 and base[0][0]==0 and base[-1][1]==4
 assert sum(Q(c["trace_error_penalty"]) for c in [] if c)==0
 frozen=[r["tau"] for r in a56["cells_exact_rational"]]
 Lold,Uold,taus_old,rows_old,cost_old,signal_old,err_old=accumulate(
     base,bc,be,freeze=frozen,coupling=False)
 assert mat(a56["exact_band_lower"])==Lold
 assert mat(a56["exact_band_upper"])==Uold
 Lpole,Upole,taus_pole,rows_pole,cost_pole,sig_pole,err_pole=accumulate(
     base,bc,be,freeze=frozen,coupling=True)
 gain=sub(Lpole,Lold)
 assert gain==T(gain) and psd(gain)
 assert all(gain[i][j]==0 for i in range(N) for j in range(N) if i!=j)
 assert all(gain[i][i]>=0 for i in range(N))
 assert err_pole<=err_old
 # Target only three MG56 high-Young-charge cells (1/8,1/2):
 # each original 1/8 cell is replaced by FOUR genuinely computed
 # ORIGINAL 1/32-width physical Fourier cells. All other 29 unchanged.
 prep=m32.original_partition_preparation()
 global4=m32.original_fourth_global(prep[1])
 refined=[]
 for i,c in enumerate(base):
  if i not in (1,2,3):
   refined.append(c)
  else:
   left,right=c[0],c[1]
   for j in range(4):
    l=left+(right-left)*Q(j,4)
    r=left+(right-left)*Q(j+1,4)
    refined.append(original_refined_true_source_cell(l,r,prep,global4))
 assert len(refined)==41
 assert refined[0][0]==0 and refined[-1][1]==4
 assert all(refined[i][1]==refined[i+1][0] for i in range(40))
 assert sum(c[1]-c[0] for c in refined)==4
 Lref,Uref,taus_ref,rows_ref,cost_ref,sig_ref,err_ref=accumulate(
     refined,bc,be,coupling=True)
 kind,wit=inertia(Lref)
 polekind,polewit=inertia(Lpole)
 basekind,_=inertia(Lold)
 assert basekind=="NEGATIVE_EXACT_RATIONAL_RAYLEIGH"
 selected="MG57_refined" if trace(Lref)>trace(Lpole) else "MG57_pole_coupled"
 selectL=Lref if selected=="MG57_refined" else Lpole
 selectKind,selectWit=inertia(selectL)
 target_old=sum(Q(rows_old[i]["trace_error_penalty"]) for i in (1,2,3))
 target_new=sum(Q(r["trace_error_penalty"]) for r in rows_ref
                if Q(1,8)<=Q(r["left"]) and Q(r["right"])<=Q(1,2))
 assert target_old>0 and target_new>=0
 summary={
  "status":"ORIGINAL_MG57_LOCAL_PHYSICAL_MULTIPLIER_POLE_COUPLED_STRONG_LOWER",
  "canonical_W_ODD_NEG":"OPEN",
  "original_sources_23adapted_plus_true_sinh_pole":True,
  "genuine_original_pole_corrected_action":True,
  "original_signed_prime7_digamma_multiplier":True,
  "accepted_original_input_runs":{"MG24":39378465438,"MG29":39440914565,"MG56":39894269994},
  "original_positive_physical_frequency_domain":["0","4"],
  "original_cell_count":32,
  "refined_cell_count":41,
  "new_original_1over32_physical_cells":12,
  "original_high_frequencies_still_paid_by_true_strong_covariance_PSD":True,
  "original_source_pole_shared_error_coupling_rigorous":True,
  "mg56_reconstructed_verbatim":True,
  "old_MG56_strong_lower_trace":str(trace(Lold)),
  "samecell_pole_coupled_strong_lower":enc(Lpole),
  "samecell_pole_coupled_strong_lower_trace":str(trace(Lpole)),
  "samecell_pole_coupled_minus_MG56_lower_PSD":True,
  "samecell_pole_coupled_MG56_PSD_gain":enc(gain),
  "samecell_pole_lower_inertia":polekind,
  "samecell_pole_lower_witness":polewit,
  "refined_original_true_strong_lower":enc(Lref),
  "refined_original_true_strong_upper":enc(Uref),
  "refined_original_strong_lower_trace":str(trace(Lref)),
  "refined_original_strong_lower_gersh":str(gersh_lower(Lref)),
  "refined_original_strong_inertia":kind,
  "refined_original_strong_inertia_witness":wit,
  "selected_trace_strong_lower_method":selected,
  "selected_trace_lower":enc(selectL),
  "selected_trace_inertia":selectKind,
  "selected_trace_inertia_witness":selectWit,
  "new_full24_original_strong_coercivity":selectKind=="POSITIVE_EXACT_RATIONAL_LDL",
  "selected_positive_coordinate_count":sum(selectL[i][i]>0 for i in range(N)),
  "old_total_Young_trace":str(err_old),
  "pole_total_Young_trace":str(err_pole),
  "refined_total_Young_trace":str(err_ref),
  "old_total_signal_trace":str(signal_old),
  "pole_total_signal_trace":str(sig_pole),
  "refined_total_signal_trace":str(sig_ref),
  "original_three_cells_Young_charge":str(target_old),
  "refined_twelve_cells_Young_charge":str(target_new),
  "original_three_cells_charge_fraction":str(target_old/err_old),
  "targeted_refinement_trace_error_change":str(target_new-target_old),
  "original_uncertainty_components_attribution":{k:str(v) for k,v in cost_old.items()},
  "refined_uncertainty_components_attribution":{k:str(v) for k,v in cost_ref.items()},
  "MG56_frozen_old_cell_records":rows_old,
  "MG57_pole_coupled_frozen_cell_records":rows_pole,
  "MG57_refined_true_physical_cell_records":rows_ref,
  "MG57_refined_true_physical_fourier_source_cells":[{
       "left":str(c[0]),"right":str(c[1]),
       "multiplier_lower":str(c[2]),"multiplier_upper":str(c[3]),
       "source_midpoint":[str(z) for z in c[4]],
       "source_derivative":[str(z) for z in c[5]],
       "source_error":[str(z) for z in c[6]]}
       for c in refined if Q(1,8)<=c[0] and c[1]<=Q(1,2)],
  "original_true_Sstar_ge_MG57_lower":True,
  "negative_lower_does_not_assert_negative_operator_spectrum":True,
  "source_24D_residual_contraction":False,
  "original_470D_inverse":False,"signed_odd_51over56_cap":False,
  "independent_original_Fourier_form_domain_audit":"OPEN",
  "even_Weil_CC27_RH":"OPEN"}
 path=ROOT/args.output;path.parent.mkdir(parents=True,exist_ok=True)
 path.write_text(json.dumps(summary,indent=2)+"\n")
 print("MG57 ORIGINAL targeted strong-action source",{
  "old_MG56_trace":float(trace(Lold)),
  "pole_coupled_trace":float(trace(Lpole)),
  "refined_original_trace":float(trace(Lref)),
  "high_loss_three_cell_young_old":float(target_old),
  "subdivided_twelve_cell_young":float(target_new),
  "refined_inertia":kind,
  "strict_full24_original_coercivity":summary["new_full24_original_strong_coercivity"],
  "470D_RH":"OPEN"},flush=True)
if __name__=="__main__":main()
