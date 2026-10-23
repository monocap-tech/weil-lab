#!/usr/bin/env python3
"""MG56 independent reverse-order exact rational strong-lower sign replay.

The accepted original MG56 physical source interval construction and
forward LDL source loss census are independently checked in the
opposite elimination order. Reverse Schur pivots prove -L strictly
positive, i.e. the CONSERVATIVE lower L is negative definite.

Separately reconstruct Young loss numerators exactly for the physical
[1/8,1/2] subset and verify dominance. Never infer a true original
operator negative spectral mode from an indefinite/NSD lower bracket.
"""
import argparse,json,sys
from fractions import Fraction as Q
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
N=24
def matrix(x):
 a=[[Q(z) for z in r] for r in x]
 assert len(a)==N and all(len(r)==N for r in a)
 return a
def reverse_positive(A):
 assert all(A[i][j]==A[j][i] for i in range(N) for j in range(N))
 # Reverse exact Schur elimination: independent of producer's forward
 # LDL and full-source original inertia helper.
 m=[r[:] for r in A]
 pivots=[]
 for k in reversed(range(N)):
  d=m[k][k]
  assert d>0,("reverse LDL failure",k)
  pivots.append(d)
  for i in range(k):
   t=m[i][k]/d
   for j in range(i,k):
    m[i][j]-=t*m[k][j]
    m[j][i]=m[i][j]
 return pivots
def main():
 p=argparse.ArgumentParser()
 p.add_argument("--verified-mg56-json",required=True)
 p.add_argument("--verified-mg56-census-json",required=True)
 args=p.parse_args()
 read=lambda p:json.loads((ROOT/p).read_text())
 src=read(args.verified_mg56_json)
 doc=read(args.verified_mg56_census_json)
 assert src["status"]=="ORIGINAL_MG56_POLE_CORRECTED_STRONG_ACTION_BAND_24D_LOWER"
 assert doc["status"]=="MG56_INDEPENDENT_ACCEPTED_STRONG_BAND_EXACT_ERROR_LOSS_CLASSIFICATION"
 assert src["canonical_W_ODD_NEG"]=="OPEN"
 L=matrix(src["exact_band_lower"])
 reverse_pivots=reverse_positive([[-x for x in row] for row in L])
 assert len(reverse_pivots)==N
 # Reconstruct the same geometric original frequency error
 # payments using an algebraically different expansion.
 total=Q(0)
 peak=Q(0)
 for c in src["cells_exact_rational"]:
  left=Q(c["left"]);right=Q(c["right"]);theta=Q(c["tau"])
  radius=sum((Q(x) for x in c["strong_error_radius"]),Q(0))
  current=2*(right-left)*(1-theta)*radius*radius/theta
  assert current>=0
  total+=current
  if Q(1,8)<=left and right<=Q(1,2):
   peak+=current
 # This algebra is exactly (1/tau-1)*rho^2.
 assert total==Q(doc["original_full24_directional_error_charge_trace"])
 assert peak==Q(doc["three_cell_total_exact_diagonal_Young_charge"])
 assert peak/total==Q(doc["three_cell_share_of_total_Young_charge"])
 assert Q(3,4)<peak/total<Q(4,5)
 assert doc["whole_original_24D_new_band_lower_NEGATIVE_DEFINITE"]
 assert doc["zero_PSD_lower_strictly_dominates_this_certificate"]
 assert doc["true_original_physical_strong_action_Sstar_still_PSD"]
 assert not doc["new_original_strong_action_negative_eigenmode_claim"]
 assert doc["even_Weil_CC27_RH"]=="OPEN"
 print("MG56 INDEPENDENT reverse LDL + exact Fourier error attribution PASS",{
  "negative_definite_conservative_lower":True,
  "reverse_positive_pivots":len(reverse_pivots),
  "top_original_cells_charge_fraction":float(peak/total),
  "physical_original_operator_negative_direction":"NOT_CLAIMED",
  "RH":"OPEN"},flush=True)
if __name__=="__main__":main()
