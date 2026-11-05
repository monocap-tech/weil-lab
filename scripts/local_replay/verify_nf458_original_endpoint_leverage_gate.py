#!/usr/bin/env python3
"""NF458: exact original source-jet projection endpoint gate, not its numerical evaluation."""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
d=Path(__file__).resolve().parents[2]/"notes/data/provisional"
def source(path):
    raw=(d/path).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()
rank,hr=source("parents/pr350_original_BS_pruned_rank_bound.json")
nf404,h404=source("NF404_original_selected_pole_shear_exact.json")
nf403,h403=source("NF403_original_joint_complement_power_exact.json")
n512,h512=source("NF380_original_archived_unfitted_signed_dual_native.json")
n513,h513=source("NF389_original_n513_signed_native.json")
nf456,h456=source("NF456_original_J242_two_ray_residual_custody.json")
nf457,h457=source("NF457_original_log_peel_info_ceiling_custody.json")
sourceSHA="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
assert rank["retained_original_pole"] is True
assert rank["retained_physical_rank_upper"]==242
assert hr==nf404["original_rank_sha256"]
assert n512["original_rank_sha256"]==n513["original_rank_sha256"]==hr
assert n512["unfitted_n"]==512 and n513["unfitted_n"]==513
assert h512==nf403["original_n512_native_sha256"]
assert h513==nf403["original_n513_native_sha256"]
assert nf456["original_source_nf407_sha256"]==nf457["source_original_nf407_sha256"]==sourceSHA
assert nf404["original_selected_pole_index"]==241
nodes=rank["original_nodes"]; mult=rank["selected_multiplicities"]
assert len(nodes)==len(mult)==107
keep=[(F(z[0]),k) for z,n in zip(nodes,mult) for k in range(n)]
assert len(keep)==241
assert len(set(c for c,k in keep))==67
assert max(k for c,k in keep)==13
# Source physical basis is x^k*sin(2pi*c*x) for even k,
# and x^k*cos(2pi*c*x) for odd k; pole=sinh(x/2).
# Explicit original selected node (37/64,1) is NOT an
# integer sine harmonic of the B=11/10 Dirichlet family.
assert (F(37,64),1) in keep
assert F(37,64)/F(5,11) != int(F(37,64)/F(5,11))
B=F(11,10); delta=F(1,10**15)
assert all(F(5*n,11)*2*B==n for n in (512,513))
# Raw exterior sources sin(2pi*(5n/11)x) vanish at x=B.
# Their terminal collar sup <= 2pi*(5n/11)*delta,
# with pi<22/7, but the orthogonalized q_n need NOT vanish.
raw_extra_abs_bound=2*F(22,7)*F(5*513,11)*delta
assert raw_extra_abs_bound<F(15,10**13) # 1.5e-12
Rhi=F(nf404["original_selected_after_pole_shear_power_upper_exact"])
dup=F(nf403["source_strict_joint_dual_power_upper"])
assert dup==F(307,2000)*F(2401,2*10**28)
projected_power_upper=Rhi+dup
simple_radius=F(34,10**12)
assert projected_power_upper<simple_radius**2
maxKernel=(F(9,10**9)/simple_radius)**2
assert maxKernel==F(4500,17)**2
assert F(70000)<maxKernel<F(71000)
# For V=J242+span(q512,q513), original centered Pi=P_V f:
# |Pi(x)|² <= ||Pi||² * K_V(x,x), so certified
# sup_collar K_V<maxKernel SUFFICES for old NF457 Pi<9e-9.
# K_V is the actual 244x244 physical Gram inverse evaluation,
# NOT a 243-mode sine count; its numerical max is NOT computed.
assert nf457["source_valid_projector_collar_pointwise_upper_computed"] is False
assert nf456["source_current_T_upper"]=="OPEN"
report={
 "pass":"NF458",
 "status":"ACCEPTED original source-type recovery and exact projection leverage acceptance gate; actual leverage NOT evaluated",
 "rank_sha256":hr,"nf404_sha256":h404,"nf403_sha256":h403,
 "n512_sha256":h512,"n513_sha256":h513,
 "original_selected_jet_sources":241,"original_used_centers":67,
 "original_max_polynomial_order":13,"pole":"sinh(x/2)",
 "authentic_augmented_physical_dimension":244,
 "uniform_raw_512_513_terminal_probe_upper":str(raw_extra_abs_bound),
 "certified_centered_projection_power_upper":str(projected_power_upper),
 "simple_projection_norm_bound":"3.4e-11",
 "sufficient_physical_Christoffel_K_sup_upper":str(maxKernel),
 "projection_collar_bound_if_K_gate":"9e-9",
 "original_full_two_sided_L2_collar_if_K_gate":"4.01e-31",
 "authentic_K_sup_computed":False,"original_Pi_collar_upper_computed":False,
 "original_T_upper":"OPEN","NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN"}
# NF459 descendant branch only: execute native 4096-bit source evaluation, and
# leave the existing NF458 artifact as ONE valid JSON with a typed NF459 record.
if __name__=="__main__":
    import os,subprocess,sys
    if os.environ.get("GITHUB_HEAD_REF")=="research/nf459-native-physical-christoffel-collar":
        subprocess.run([sys.executable,"-m","pip","install","--only-binary=:all:","python-flint==0.8.0"],
                       check=True,stdout=sys.stderr,stderr=sys.stderr)
        cmd=[sys.executable,"-u","-X","int_max_str_digits=0",
             "scripts/verify_nf459_original_native_244D_christoffel.py",
             "--output","nf459-authentic-native-result.json"]
        try:
            subprocess.run(cmd,check=True,stdout=sys.stderr,stderr=sys.stderr)
        except Exception:
            report["NF459_native"]={"standing":"FAILED_CLOSED","numerical_acceptance":False}
            print(json.dumps(report,indent=2))
            raise
        report["NF459_native"]=json.loads(Path("nf459-authentic-native-result.json").read_text())
    print(json.dumps(report,indent=2))
