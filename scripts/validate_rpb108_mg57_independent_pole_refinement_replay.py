#!/usr/bin/env python3
"""MG57 independent exact rational original strong-action physical source replay.

No MG57 producer imports: explicitly regenerate twelve physical source
1/32-subcells through MG29 fourth-derivative formula; use a completely
separate rank-one/Young 24D matrix accumulator to rebuild old MG56,
frozen same-cell pole-error coupling, and targeted 41-cell refinement.
Independent exact LDL/negative rational source ray verification.

No claim that negative matrix lower implies negative actual operator.
"""
import argparse,json,sys
from fractions import Fraction as Q
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import original_H24_from_physical_source
import validate_rpb108_mg32_joint_fourier_residual as old
N=24;P=23
def rd(a):
 A=[[Q(x) for x in row] for row in a]
 assert len(A)==N and all(len(r)==N for r in A)
 return A
def transpose(A):return [list(v) for v in zip(*A)]
def plus(A,B):return [[x+y for x,y in zip(a,b)] for a,b in zip(A,B)]
def minus(A,B):return plus(A,[[-z for z in r] for r in B])
def qf(v,A):return sum((v[i]*A[i][j]*v[j] for i in range(N) for j in range(N)),Q(0))
def is_psd(a):
 assert a==transpose(a)
 z=[r[:] for r in a]
 for k in range(N):
  p=z[k][k]
  assert p>=0
  if p==0:
   assert all(z[k][j]==0 for j in range(k+1,N))
   continue
  for i in range(k+1,N):
   for j in range(i,N):
    z[i][j]-=z[i][k]*z[k][j]/p
    z[j][i]=z[i][j]
 return True
def own_original_subcells():
 prep=old.original_partition_preparation()
 centers,physical,aa,cc,hyp,kglobal,kthird=prep
 assert len(physical)==25
 fourth=old.original_fourth_global(physical)
 result=[]
 for index in (1,2,3):
  for m in range(4):
   left=Q(index,8)+Q(m,32)
   right=left+Q(1,32)
   mid=(left+right)/2;half=(right-left)/2
   wlo,whi,_=old.positive_cell_weight_interval(left,right)
   values=old.original_exact_physical_fourier_midpoint(
      mid,centers,physical,hyp)
   deriv,second=old.original_midpoint_derivative_intervals(
      mid,centers,physical,hyp)
   curv=[min(globalcap,old.abs_cap(s2)+cap3*half) if s2 is not None
         else globalcap
         for globalcap,s2,cap3 in zip(kglobal,second,kthird)]
   v,d,rough=old.transformed_affine(values,deriv,curv,aa,cc,half)
   decomp=old.splits_original_source(
      v,d,rough,curv,half,values,deriv,aa,cc,23,24)
   actual2=old.exact_original_second_midpoint(
      mid,centers,physical,hyp)
   local3=old.third_adapted_whole_cell(
      mid,centers,physical,hyp,aa,cc,kthird,half,fourth)
   old2=old.true_direct_adapted_curvature(
      actual2,kthird,aa,cc,curv,half)
   radii=[]
   for j,(val,deriverr,_,_) in enumerate(decomp):
    true2=actual2[j]-aa[j]*actual2[24]-cc[j]*actual2[23] if j<23 else actual2[24]
    bound=min(old2[j][0],old.abs_cap(true2)+local3[j][0]*half)
    r=old.up(val+deriverr+half*half*bound/2)
    assert Q(0)<=r<=rough[j]
    radii.append(r)
   result.append((left,right,wlo,whi,v,d,radii))
 return result
def independent_matrices(cells,b,e,coupled,freeze=None):
 L=[[Q(0)]*N for _ in range(N)]
 U=[[Q(0)]*N for _ in range(N)]
 allrows=[]
 for n,(left,right,lo,hi,v,d,eps) in enumerate(cells):
  w=right-left;h=w/2
  mid=(lo+hi)/2;spread=(hi-lo)/2
  y=[];s=[];r_old=[];r_new=[];terms=[]
  maxpole=abs(v[P])+h*abs(d[P])+eps[P]
  for i in range(N):
   y.append(mid*v[i]-2*v[P]*b[i])
   s.append(mid*d[i]-2*d[P]*b[i])
   taylor=abs(mid)*eps[i]
   m=spread*(abs(v[i])+h*abs(d[i])+eps[i])
   pole=2*abs(b[i])*eps[P]
   unknown=2*e[i]*maxpole
   oldr=taylor+m+pole+unknown
   nr=abs(mid-2*b[P])*eps[P]+m+unknown if i==P else oldr
   assert 0<=nr<=oldr
   terms.append((taylor,m,pole,unknown))
   r_old.append(oldr);r_new.append(nr)
  radius=r_new if coupled else r_old
  def unweighted_lower_trace(tau):
   ell=sum((yi*yi for yi in y),Q(0))
   ell+=(w*w/12)*sum((di*di for di in s),Q(0))
   Esum=sum(radius,Q(0))
   return 2*w*((1-tau)*ell-(1/tau-1)*Esum*Esum)
  if freeze is None:
   tau=max(old.CHOSEN_TAUS,key=lambda t:(unweighted_lower_trace(t),-t))
  else:
   tau=Q(freeze[n])
   assert tau in old.CHOSEN_TAUS
  error=sum(radius,Q(0))
  signal=2*w*(1-tau)*(sum(z*z for z in y)
                       +w*w*sum(z*z for z in s)/12)
  payment=2*w*(1/tau-1)*error*error
  for i in range(N):
   for j in range(N):
    quadratic=y[i]*y[j]+w*w*s[i]*s[j]/12
    L[i][j]+=2*w*(1-tau)*quadratic
    U[i][j]+=2*w*(1+tau)*quadratic
   L[i][i]-=2*w*(1/tau-1)*error*radius[i]
   U[i][i]+=2*w*(1+1/tau)*error*radius[i]
  components={
   "Taylor_source":sum(x[0] for x in terms),
   "multiplier_width":sum(x[1] for x in terms),
   "pole_source_Taylor":sum(x[2] for x in terms),
   "pole_column_interval":sum(x[3] for x in terms)}
  allrows.append({
   "left":str(left),"right":str(right),
   "multiplier_lower":str(lo),"multiplier_upper":str(hi),
   "tau":str(tau),
   "source_error_l1_old":str(sum(r_old,Q(0))),
   "source_error_l1_new":str(error),
   "pole_channel_old_radius":str(r_old[P]),
   "pole_channel_coupled_radius":str(r_new[P]),
   "trace_signal":str(signal),"trace_error_penalty":str(payment),
   "source_interval_components_l1":{k:str(z) for k,z in components.items()}
  })
 oldL,oldU,_,_=old.finalize((L,U))
 assert is_psd(minus(oldU,oldL)) and is_psd(oldU)
 return oldL,oldU,allrows
def negative_witness(A,kind,witness):
 if kind=="NEGATIVE_EXACT_RATIONAL_RAYLEIGH":
  x=[Q(z) for z in witness["rational_vector"]]
  assert len(x)==N and any(x)
  assert qf(x,A)==Q(witness["exact_negative_quadratic"])<0
 elif kind=="POSITIVE_EXACT_RATIONAL_LDL":
  z=[r[:] for r in A]
  for k in range(N):
   d=z[k][k]
   assert d>0
   for i in range(k+1,N):
    for j in range(i,N):
     z[i][j]-=z[i][k]*z[k][j]/d
     z[j][i]=z[i][j]
 else:assert kind=="INCONCLUSIVE"
def main():
 p=argparse.ArgumentParser()
 for k in ("mg24","mg56","mg57"):
  p.add_argument("--verified-"+k+"-json",required=True)
 args=p.parse_args()
 a={k:json.loads((ROOT/getattr(args,"verified_"+k+"_json")).read_text())
    for k in ("mg24","mg56","mg57")}
 src=a["mg56"];z=a["mg57"]
 assert z["status"]=="ORIGINAL_MG57_LOCAL_PHYSICAL_MULTIPLIER_POLE_COUPLED_STRONG_LOWER"
 assert all(x["canonical_W_ODD_NEG"]=="OPEN" for x in a.values())
 H,rad,err=original_H24_from_physical_source()
 assert err==Q(a["mg24"]["physical_Gram_Loewner_row_error"])
 b=[H[i][P] for i in range(N)]
 e=[rad[i][P] for i in range(N)]
 original,*_=old.exact_original_cells()
 assert len(original)==32
 freeze=[x["tau"] for x in src["cells_exact_rational"]]
 L0,U0,rows0=independent_matrices(original,b,e,False,freeze=freeze)
 assert L0==rd(src["exact_band_lower"])
 assert U0==rd(src["exact_band_upper"])
 assert rows0==z["MG56_frozen_old_cell_records"]
 Lc,Uc,rowsc=independent_matrices(original,b,e,True,freeze=freeze)
 assert Lc==rd(z["samecell_pole_coupled_strong_lower"])
 assert is_psd(minus(Lc,L0))
 assert rowsc==z["MG57_pole_coupled_frozen_cell_records"]
 assert z["samecell_pole_coupled_minus_MG56_lower_PSD"]
 assert minus(Lc,L0)==rd(z["samecell_pole_coupled_MG56_PSD_gain"])
 assert all(Lc[i][j]-L0[i][j]==0
            for i in range(N) for j in range(N) if i!=j)
 newcells=own_original_subcells()
 archive=z["MG57_refined_true_physical_fourier_source_cells"]
 assert len(newcells)==len(archive)==12
 for source,record in zip(newcells,archive):
  assert [str(q) for q in source[:4]]==[
     record[x] for x in ("left","right","multiplier_lower","multiplier_upper")]
  assert [str(q) for q in source[4]]==record["source_midpoint"]
  assert [str(q) for q in source[5]]==record["source_derivative"]
  assert [str(q) for q in source[6]]==record["source_error"]
 new=[]
 for i,cell in enumerate(original):
  if i in (1,2,3):
   new.extend(newcells[4*(i-1):4*i])
  else:new.append(cell)
 assert len(new)==41
 L,U,rows=independent_matrices(new,b,e,True)
 assert L==rd(z["refined_original_true_strong_lower"])
 assert U==rd(z["refined_original_true_strong_upper"])
 assert rows==z["MG57_refined_true_physical_cell_records"]
 assert sum(L[i][i] for i in range(N))==Q(z["refined_original_strong_lower_trace"])
 assert sum(Lc[i][i] for i in range(N))==Q(z["samecell_pole_coupled_strong_lower_trace"])
 negative_witness(L,z["refined_original_strong_inertia"],z["refined_original_strong_inertia_witness"])
 negative_witness(Lc,z["samecell_pole_lower_inertia"],z["samecell_pole_lower_witness"])
 selected=(L if z["selected_trace_strong_lower_method"]=="MG57_refined" else Lc)
 assert selected==rd(z["selected_trace_lower"])
 negative_witness(selected,z["selected_trace_inertia"],z["selected_trace_inertia_witness"])
 assert z["new_full24_original_strong_coercivity"]==(z["selected_trace_inertia"]=="POSITIVE_EXACT_RATIONAL_LDL")
 assert sum(selected[i][i]>0 for i in range(N))==z["selected_positive_coordinate_count"]
 topold=sum(Q(rows0[i]["trace_error_penalty"]) for i in (1,2,3))
 topnew=sum((Q(v["trace_error_penalty"]) for v in rows
             if Q(1,8)<=Q(v["left"]) and Q(v["right"])<=Q(1,2)),Q(0))
 assert topold==Q(z["original_three_cells_Young_charge"])
 assert topnew==Q(z["refined_twelve_cells_Young_charge"])
 assert topnew-topold==Q(z["targeted_refinement_trace_error_change"])
 for name,records in (("old",rows0),("pole",rowsc),("refined",rows)):
  rawerror=sum(Q(r["trace_error_penalty"]) for r in records)
  rawsignal=sum(Q(r["trace_signal"]) for r in records)
  assert rawerror==Q(z[name+"_total_Young_trace"])
  assert rawsignal==Q(z[name+"_total_signal_trace"])
 assert not z["source_24D_residual_contraction"]
 assert not z["original_470D_inverse"]
 assert not z["signed_odd_51over56_cap"]
 assert z["independent_original_Fourier_form_domain_audit"]=="OPEN"
 assert z["even_Weil_CC27_RH"]=="OPEN"
 print("MG57 INDEPENDENT true physical 41-cell targeted source and pole shared-error full24 replay PASS",{
   "old_trace":float(Q(z["old_MG56_strong_lower_trace"])),
   "pole_trace":float(Q(z["samecell_pole_coupled_strong_lower_trace"])),
   "refined_trace":float(Q(z["refined_original_strong_lower_trace"])),
   "full24_strong_coercivity":z["new_full24_original_strong_coercivity"],
   "RH":"OPEN"},flush=True)
if __name__=="__main__":main()
