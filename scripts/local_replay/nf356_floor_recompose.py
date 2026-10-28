#!/usr/bin/env python3
"""Read-only Weil-Lab NF356 complete exterior floor *conditional* recomposition.

Proves rational inequality from retained old cover bound and local gap reports.
The gap report's interval arithmetic and analytic Binet attachment are separate
proof inputs. No GitHub/CI/domain acceptance is asserted.
"""
from fractions import Fraction as F
from pathlib import Path
import os
CUSTODY_ROOT = Path(os.environ.get("WEIL_CUSTODY_DATA_DIR", "/mnt/data"))
import json, zipfile,hashlib

def verify_archive(path,digest):
    p=Path(path);assert hashlib.sha256(p.read_bytes()).hexdigest()==digest
    return zipfile.ZipFile(p)

p350=verify_archive(str(CUSTODY_ROOT / 'pr350-certificate.zip'),'3389809c3a01c223b95e9dc96ea7c9dd776cb83049bb2d93a3c9d9bbad45af09')
r350=p350.read('original_BS_pruned_rank_bound.json')
assert hashlib.sha256(r350).hexdigest()=='9b9820a0163e5e8bf08dd1c2525c757ff67214b49a40cb093d00bc611c9ff9e2'
bound=json.loads(r350)
pre=json.loads(Path(str(CUSTODY_ROOT / 'nf356_old_cover_001_report.json')).read_text())
gaps=json.loads(Path(str(CUSTODY_ROOT / 'nf356_gap_001_report.json')).read_text())
rgaps=json.loads(Path(str(CUSTODY_ROOT / 'nf356_gap_001_replay.json')).read_text())
assert gaps['gaps']==rgaps['gaps']==107 and gaps['threshold']==rgaps['threshold']=='1/100'
assert F(gaps['smallest_accepted_floor'])>F(1,100)
assert F(rgaps['smallest_accepted_floor'])>F(1,100)
assert pre['intervals_checked']==62272 and pre['strictly_above_level']+pre['strictly_below_level']+pre['unresolved_included']==62272
assert pre['zero_constraint_clusters_excluded']==40
assert pre['bounded_clusters']==64
assert F(pre['test_level'])==F(1,100)
assert bound['retained_physical_rank_upper']==242
E=F(bound['pruned_physical_complement_negative_upper'])
D=F(pre['projector_on_old_support_upper_exact'])
lam=F(1,100);old=F(1,1000)
mu=lam-E-(lam-old)*D
assert mu>F(998,100000)
# precise retained PR355 countercheck
p355=verify_archive(str(CUSTODY_ROOT / 'pr355-exterior.zip'),'f7b64ceead7500fca389e3b994a208a6e8aae5be3270b750ab586e5ebe1fa1d0')
r355=p355.read('original_exterior_scalar_floor_stop.json')
assert hashlib.sha256(r355).hexdigest()=='d853e2ecf665b8bb3978ee203371c07f67d050b79e7427d6c673331fd1d60ab9'
q=json.loads(r355)
v=(3,4,4,-2)
def dyadic(x):return F(int(x[0]))*F(2)**int(x[1])
def Qform(key):
    M=q[key];a=b=F(0)
    for i in range(4):
     for j in range(4):
      lo=dyadic(M[i][j][0])-dyadic(M[i][j][1]);hi=dyadic(M[i][j][0])+dyadic(M[i][j][1]);t=v[i]*v[j]
      a+=min(t*lo,t*hi);b+=max(t*lo,t*hi)
    return a,b
AL,AU=Qform('projected_strong_norm_variational_lower_matrix_native')
BL,BU=Qform('signed_energy_Gram_native')
assert BL>0 and AL>F(79,10000)*BU
assert mu>F(79,10000) # not a verified strong-action UPPER, just clearance of this known LOWER witness
report={
 'result':'LOCAL CONDITIONAL ORIGINAL J242 EXTERIOR FLOOR, NOT INTEGRATED',
 'base_kappa':'1/1000','target_lambda':'1/100',
 'original_negative_leakage_upper':str(E),'new_sublevel_projector_upper_on_old_cover':str(D),
 'gap_count':107,'gap_min_lower_at_shift16':gaps['smallest_accepted_floor'],
 'gap_min_lower_at_shift32':rgaps['smallest_accepted_floor'],
 'tail':'analytic Binet lower m(x)>0.0699 for x>=1300, pure rational threshold arithmetic',
 'mu_new_lower_exact':str(mu),'mu_new_lower_float':float(mu),
 'mu_new_greater_than':'499/50000', # .00998
 'mu_old_lower_float':float(old-E),
 'new_floor_over_old_floor':float(mu/(old-E)),
 'PR355_known_coupled_direction':'(3,4,4,-2)',
 'known_L2_strong_lower_ratio':float(AL/BU),
 'scalar_strong_sufficient_bound_verified':False,
 'whole_infinite_Schur_upper_verified':False,
 'original_operator_form_domain_review':'OPEN','W_ODD_NEG':'OPEN',
 'limitations':'Gap intervals use mpmath.iv; no native Arb CI/independent exact original multiplier replay; no repo commit.'
}
Path(str(CUSTODY_ROOT / 'nf356_floor_local_report.json')).write_text(json.dumps(report,indent=2)+'\n')
for k,v in report.items():
 if k.endswith('exact'):continue
 print(k,v)
