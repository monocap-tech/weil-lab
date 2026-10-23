#!/usr/bin/env python3
"""MG07 conditional original 470-source SI29-weighted Galerkin residual gate.
This script verifies exact algebra and original source geometry, NOT an
actual 470x470 resolvent certificate or any RH assertion.
"""
import argparse,json
from fractions import Fraction as F
from validate_rpb108_sm35_full_original_resolvent_galerkin_enclosure import (
 ROOT,mat,transpose,mm,scale,add,sub,eye,inv,psd2,
 actual_original_basis_and_cap_geometry)
from validate_rpb108_sm17_compact_spectral_gate import KAPPA_STAR
from validate_rpb108_sm34_positive_energy_dual_schur import CLEAN_THRESHOLD
from validate_rpb108_si29_pole_threshold_three_bands import FEATURES

def diag(xs):
 return [[F(xs[i]) if i==j else F(0) for j in range(len(xs))] for i in range(len(xs))]
def psd3(X):
 # Exact principal-minor criterion for 3x3 symmetric PSD; all
 # principal minors, not only leading minors (the latter test PD).
 assert len(X)==3 and all(len(row)==3 for row in X)
 assert all(X[i][j]==X[j][i] for i in range(3) for j in range(3))
 if any(X[i][i]<0 for i in range(3)):return False
 if any(X[i][i]*X[j][j]-X[i][j]**2<0
        for i,j in ((0,1),(0,2),(1,2))):return False
 a,b,c=X[0][0],X[1][1],X[2][2]
 x,y,z=X[0][1],X[0][2],X[1][2]
 return a*b*c+2*x*y*z-a*z*z-b*y*y-c*x*x>=0

def string_matrix(A):return [[str(x) for x in r] for r in A]
def exact_model():
 # 3D physical toy with one positive SI29-style feature, rank-one
 # pole, a 2-source coupled nonzero strong Galerkin residual.
 Fcol=mat([[1],[0],[0]]); s=mat([[0],[F(1,4)],[0]])
 k=F(1);gam=F(2);ks=F(7,8); H=F(1,4);theta=CLEAN_THRESHOLD
 C=add(eye(3),scale(gam,mm(Fcol,transpose(Fcol))))
 B=sub(C,scale(2,mm(s,transpose(s))))
 A=add(B,mat([[1,0,F(1,8)],[0,1,F(1,8)],[F(1,8),F(1,8),1]]))
 assert B==diag([3,F(7,8),1])
 J=mat([[1,0],[0,1],[0,0]])
 Z=mat([[F(1,4),0],[0,F(8,15)],[0,0]])
 R=sub(J,mm(A,Z))
 assert R==mat([[0,0],[0,0],[-F(1,32),-F(1,15)]])
 assert mm(transpose(Z),R)==mat([[0,0],[0,0]])
 E=mm(transpose(R),R)
 # Complete low-rank SI29/SM19 Woodbury with correct pole sign.
 M=add([[1/gam]],mm(transpose(Fcol),Fcol))
 Mi=inv(M)
 Ci=sub(eye(3),mm(mm(Fcol,Mi),transpose(Fcol)))
 alpha=F(1)-2*mm(mm(transpose(s),Ci),s)[0][0]
 assert alpha==F(7,8)>0
 Fr=mm(transpose(Fcol),R)
 z=mm(mm(transpose(R),Ci),s)
 DB=add(sub(E,mm(mm(transpose(Fr),Mi),Fr)),
        scale(F(2)/alpha,mm(z,transpose(z))))
 assert DB==mm(mm(transpose(R),inv(B)),R)
 # Nontrivial test verifies both low-rank and pole corrections.
 Q=mat([[F(1,7),F(1,9)],[F(2,7),-F(1,5)],[F(1,11),F(3,11)]])
 Fq=mm(transpose(Fcol),Q);zq=mm(mm(transpose(Q),Ci),s)
 Dq=mm(transpose(Q),Q)
 Qref=add(sub(Dq,mm(mm(transpose(Fq),Mi),Fq)),
          scale(F(2)/alpha,mm(zq,transpose(zq))))
 assert Qref==mm(mm(transpose(Q),inv(B)),Q)
 assert Fq!=[[0,0]] and zq!=[[0],[0]]
 Ai=inv(A);K=scale(H,eye(3))
 assert psd3(sub(inv(B),Ai))
 assert psd3(diag([0,1,0])) # singular PSD passes
 assert not psd3(mat([[1,2,0],[2,1,0],[0,0,1]])) # negative minor rejected
 assert psd2(sub(scale(1/ks,E),DB))
 G0=mm(mm(transpose(Z),A),Z)
 G=mm(mm(transpose(J),Ai),J)
 assert G==add(G0,mm(mm(transpose(R),Ai),R))
 N0=mm(mm(transpose(Z),K),Z)
 N=mm(mm(mm(mm(transpose(J),Ai),K),Ai),J)
 Nnew=add(scale(2,N0),scale(2*H/ks,DB))
 Nold=add(scale(2,N0),scale(2*H/ks**2,E))
 assert psd2(sub(Nnew,N))
 assert psd2(sub(Nold,Nnew)) and Nold!=Nnew
 assert psd2(sub(scale(theta,G0),Nnew))
 assert psd2(sub(scale(theta,G),N))
 return {"exact_full_coupled_two_source_test":True,
         "strict_reference_residual_gain_trace":str(sum(
              Nold[i][i]-Nnew[i][i] for i in range(2))),
         "new_upper":string_matrix(Nnew),
         "old_scalar_upper":string_matrix(Nold)}

def main():
 p=argparse.ArgumentParser()
 p.add_argument("--output",default="artifacts/mg07_470_preconditioned_residual.json")
 args=p.parse_args()
 ledger=json.loads((ROOT/"research/obligations.json").read_text())
 odd=next(o for o in ledger["obligations"] if o["id"]=="W-ODD-NEG")
 assert odd["status"]==ledger["objective"]["status"]=="open"
 assert ledger["active_obligation"]=="W-ODD-NEG"
 assert ledger["governance"]["no_automatic_promotion"]
 assert all(z in odd["evidence"] for z in ("SI29","SM19","SM34","SM35"))
 g=actual_original_basis_and_cap_geometry()
 assert g["source_dim"]==470 and g["cap_columns"]==890
 assert len(FEATURES)==14
 k=F(1,1000);ks=KAPPA_STAR;theta=CLEAN_THRESHOLD
 H=g["full_negative_norm"]
 assert ks==F(33621,10**9) and theta==F(51,56)
 assert k*(1-F(966379,10**6))==ks
 assert F(80)<H<F(83)
 old=2*H/ks**2;new=2*H/ks
 orthogonal=new/k
 assert orthogonal/old==ks/k==F(33621,10**6)
 toy=exact_model()
 result={
  "status":"CONDITIONAL_COMPLETE_ORIGINAL_470_SOURCE_SI29_RESIDUAL_GATE",
  "canonical_W_ODD_NEG":"OPEN",
  "original_exceptional_source_count":470,
  "original_negative_cap_columns":890,
  "original_true_positive_reference_features":14,
  "original_kappa_star":str(ks),
  "whole_odd_sufficient_theta":str(theta),
  "original_full_negative_norm_upper":str(H),
  "old_t1_scalar_residual_coefficient":str(old),
  "new_t1_operator_reference_coefficient":str(new),
  "feature_and_pole_orthogonal_coefficient":str(orthogonal),
  "feature_and_pole_orthogonal_ratio_to_old":str(ks/k),
  "acceptance":"(1+t)*N0_cap+(1+1/t)*(H/kstar)*R*B14^-1*R <= theta*G0",
  "whole470_schur_acceptance_certified":False,
  "original_complete_residual_physical_Grams_computed":False,
  "entire_original_odd_negative_index_classified":False,
  "even_Weil_CC27_RH":"OPEN",
  "independent_Fourier_and_form_domain_audit":"OPEN",
  "toy":toy
 }
 target=ROOT/args.output;target.parent.mkdir(parents=True,exist_ok=True)
 target.write_text(json.dumps(result,indent=2)+"\n")
 print("MG07 original full470 reference-weighted residual gate:",json.dumps({
  "source_count":470,"cap_columns":890,"ratio":str(ks/k),
  "toy_passed":True,"whole_odd_Weil_RH":"OPEN"}),flush=True)
if __name__=="__main__":main()
