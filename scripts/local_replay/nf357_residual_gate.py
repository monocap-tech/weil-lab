#!/usr/bin/env python3
"""Read-only exact-rational screening of an *uncomputed* full strong residual.

Source: #355 artifact 12776684037, with local NF356 >.00998 floor.
This script does NOT compute the full R=QW(Phi-EY) or prove W-ODD-NEG.
"""
from fractions import Fraction as F
from decimal import Decimal, localcontext
import hashlib, zipfile, json, sys
from pathlib import Path
import os
CUSTODY_ROOT = Path(os.environ.get("WEIL_CUSTODY_DATA_DIR", "/mnt/data"))
sys.set_int_max_str_digits(100000)
ARCHIVE=Path(str(CUSTODY_ROOT / 'pr355-exterior.zip'))
ARCHIVE_SHA='f7b64ceead7500fca389e3b994a208a6e8aae5be3270b750ab586e5ebe1fa1d0'
DIAG_SHA='d853e2ecf665b8bb3978ee203371c07f67d050b79e7427d6c673331fd1d60ab9'
NF356=Path(str(CUSTODY_ROOT / 'nf356_v2_aggregate_report.json'))
with localcontext() as ctx:
 ctx.prec=45

def digest(x):return hashlib.sha256(x).hexdigest()
def dy(v):
 m,e=v
 return F(int(m))*F(2)**int(e)
def dstr(q,prec=20):
 with localcontext() as ctx:
  ctx.prec=prec
  return str(Decimal(q.numerator)/Decimal(q.denominator))

def main():
 assert digest(ARCHIVE.read_bytes())==ARCHIVE_SHA
 with zipfile.ZipFile(ARCHIVE) as z:
  raw=z.read('original_exterior_scalar_floor_stop.json')
 assert digest(raw)==DIAG_SHA
 a=json.loads(raw)
 fl=json.loads(NF356.read_bytes())
 assert fl['mu_new_greater_than']=='499/50000'
 assert fl['retained_4x4_lower_matrix_still_only_lower']
 assert not fl['global_full_infinite_schur_upper_certified']
 assert a['source_direction_count']==4 and a['selected_rank']==242
 assert a['four_probe_upper_is_global_upper'] is False
 assert a['complete_strong_action_computed'] is False
 assert a['global_Schur_penalty_upper_computed'] is False
 mu=F(499,50000)
 t=F(1,500)
 gamma=F(99,100)
 g=F(a['four_probe_Schur_energy_operator_upper'])
 assert 0<g<t
 maxrowerr=max(F(x) for x in a['signed_energy_error_row_upper'])
 assert 0<=maxrowerr<F(1,100)
 assert maxrowerr<1-gamma
 # For H=Phi^* W Phi, H >= gamma I (from native row errors)
 # the 4-probe variational form S_Y<= S_E <= g H < t H.
 # For any trial Y (in the 4-probe physical complement), define the
 # *complete* strong R=QW(Phi-EY). Under the inherited operator domain:
 # Full_Schur = S_Y + R^* C_Q^-1 R
 #             <= t H + mu^-1 R^*R.
 # Therefore ||R||_F^2 < mu * gamma * (1-t) => Full_Schur < H.
 residual_sq_upper_target=mu*gamma*(1-t)
 assert residual_sq_upper_target==F(24651099,2500000000)
 # Physical Gram of original selected energy coords is G with
 # .99 I < G < 1.01 I. Thus each physical norm^2 of Phi_j is
 # > .99 ||P_j||_2^2, EVEN when the signed-energy Gram H~I.
 P=[[dy(v) for v in row] for row in a['signed_energy_source_exact_dyadic_coefficients']]
 assert len(P)==242 and all(len(row)==4 for row in P)
 infos=[]
 for j in range(4):
  sq=sum((r[j]**2 for r in P),F())
  physlow=gamma*sq
  physup=F(101,100)*sq
  # Avoid unwieldy exact rational strings; compute them, show rounded
  # directions and exact decimal-power *proof* lower bounds.
  k=0
  while physlow >= F(10)**(k+1):k+=1
  assert physlow>F(10)**k and physup<F(10)**(k+2)
  infos.append({'direction':j,'P_l2_squared_approx':dstr(sq,14),
   'physical_l2_squared_lower':dstr(physlow,14),
   'physical_l2_squared_upper':dstr(physup,14),
   'physical_l2_squared_gt':f'1e{k}',
   'energy_gram_diag_approximately_one':True})
 out={
  'status':'RIGOROUS_CONDITIONAL_FOUR_SOURCE_RESIDUAL_ENTRY_GATE_NOT_DISCHARGED',
  'scope':'four selected signed-energy directions only, NOT all 242',
  'archive_sha256':ARCHIVE_SHA,'diagnostic_sha256':DIAG_SHA,
  'original_source_rank':242,'source_energy_coordinates':4,
  'conditional_exterior_floor_lower':str(mu),
  'signed_energy_Gram_min_lower':str(gamma),
  'four_probe_Schur_energy_op_upper':dstr(g,22),
  'simplified_four_probe_Schur_energy_op_upper':str(t),
  'complete_strong_residual_required':
    'R = Q W (Phi - E Y_C); include every original frequency, pole, physical projector, and support',
  'full_energy_Schur_identity':
    'S_full = (Y_C^* Z + Z^* Y_C - Y_C^* C_E Y_C) + R^* C_Q^{-1} R',
  'complete_residual_Frobenius_squared_sufficient_target_exact':str(residual_sq_upper_target),
  'complete_residual_Frobenius_squared_sufficient_target_approx':dstr(residual_sq_upper_target),
  'complete_residual_Frobenius_norm_target_approx':'0.099299746...',
  'complete_residual_calculated':False,
  'four_probe_Schur_upper_is_NOT_full_infinite_Schur_upper':True,
  'physical_norm_conditioning':infos,
  'full_242_selected_signed_positivity_proved_by_this_four_column_gate':False,
  'source_domain_realization_still_open':True,'W_ODD_NEG':'OPEN'
 }
 Path(str(CUSTODY_ROOT / 'nf357_residual_entry_gate.json')).write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
