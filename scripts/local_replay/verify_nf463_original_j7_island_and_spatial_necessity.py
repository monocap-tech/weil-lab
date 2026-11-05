#!/usr/bin/env python3
"""NF463 original J7 genuine enlarged signed island and conditional cap coverage.

Actual island integral is source-certified. Whole-J7 coverage, cancellation,
and z-energy bounds are NECESSARY conditional consequences of NF404, not
observations of complete D7. No native multiplier quadrature assumed.
"""
import runpy,json,hashlib,sys
from fractions import Fraction as F
from pathlib import Path
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[2]
D=ROOT/"notes/data/provisional"
S="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
G="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
B=F(11,10)
x0=F(26,25)
radius=F(4,10**16)
def read(p):
    raw=(D/p).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()
nf462=runpy.run_path(str(ROOT/"scripts/local_replay/verify_nf462_original_j7_required_signed_deficit.py"))
parent=runpy.run_path(str(ROOT/"scripts/local_replay/verify_nf453_original_j7_j8_principal_energy_signed_island.py"))
vlow,vhigh=parent["orig_arb_ball"](read("NF411_original_source_boundary_jet.json")[0]["original_original_source_value_at_B_arb"])
j7necessary=nf462["j7_necessary"]
A=-j7necessary
assert A>F("2.03475e-22") and j7necessary<0
seams,hseams=read("NF406_original_prime_support_partition_exact.json")
source,hsource=read("NF407_original_fourth_physical_coefficients_native.json")
jet,hjet=read("NF411_original_source_boundary_jet.json")
nf417,h417=read("NF417_original_cell7_full_z_pointwise_native.json")
nf418,h418=read("NF418_original_hotspot_cellwide_lipschitz_envelopes_exact.json")
nf453,h453=read("NF453_original_J7_J8_principal_and_island_custody.json")
nf462receipt,h462=read("NF462_original_forced_J7_signed_deficit_custody.json")
assert hsource==S and hseams==G
assert nf417["nf407_original_source_sha256"]==S and nf417["cell"]==7
assert F(nf417["x"])==x0 and nf417["true_original_complete_z_pointwise_certified"] is True
assert jet["nf407_source_sha256"]==S
assert nf418["original_nf407_246_source_sha256"]==S
assert nf418["original_nf406_certified_seam_partition_sha256"]==G
assert nf418["original_prior_source_point_receipt_sha256s"]["7"]==h417
assert nf418["whole_original_z_derivative_piecewise_uniform_upper_integer"]==30000
assert nf453["source_sha256"]==S and nf453["seams_sha256"]==G
assert nf453["D7_whole"]=="OPEN"
assert nf462receipt["NF404"]=="OPEN"
assert nf462receipt["original_whole_J7_D7_necessary_if_NF404_cap_approx"]=="-2.03475201128440528e-22"
island=next(z for z in nf418["original_hotspot_cellwise_envelopes"] if z["original_cell"]==7)
assert F(island["original_anchor_rational_x"])==x0
assert island["original_point_cert_sha256"]==h417
assert island["neighborhood_same_sign_certified"]
zlo,zhi=map(F,island["certified_same_sign_neighborhood_z_outward_rational_envelope_1e40"])
assert F(77,10**12)<zlo<=zhi<F(78,10**12)
assert -F(117,10**13)<vlow<vhigh<-F(116,10**13)
weights=jet["all_seven_original_prime_seam_derivative_identities"]
assert tuple(z["prime_power"] for z in weights)==(2,3,4,5,7,8,9)
c7lo=sum((F(z["c_n_positive_outward"][0]) for z in weights[:6]),F(0))
c7hi=sum((F(z["c_n_positive_outward"][1]) for z in weights[:6]),F(0))
assert F(3171,1000)<c7lo<c7hi<F(793,250)
prime={x["n"]:x for x in seams["original_prime_power_log_shifts"]}
assert set(prime)=={2,3,4,5,7,8,9}
log8lo,log8hi=map(F,(prime[8]["log_lower"],prime[8]["log_upper"]))
log9lo,log9hi=map(F,(prime[9]["log_lower"],prime[9]["log_upper"]))
assert log8hi-B<x0-radius<x0+radius<log9lo-B
assert B-x0-radius>F(1,20)
# Actual physical original J7 principal p=v(0.5 log(B/(B-x))+C7),
# with p<0. No imagined global analytic continuation is used.
log_anchor_low=parent["ln_q"](B/(B-x0))[0]
assert log_anchor_low>F(29,10)
pabs_anchor_lower=(-vhigh)*(log_anchor_low/2+c7lo)
assert pabs_anchor_lower>F(53,10**12)
# |p'(x)|=|v|/(2(B-x))<1e-9 in this genuine source subinterval.
assert (-vlow)/(2*(B-x0-radius))<F(1,10**9)
p_floor=F(5299,10**14)
assert pabs_anchor_lower-radius*F(1,10**9)>p_floor
# Original source piecewise derivative bound |z'|<30000 in J7
# together with its actual NF417 anchor: no new quadrature.
L=F(30000)
z_floor=F(77,10**12)-L*radius
z_ceiling=F(78,10**12)+L*radius
assert z_floor==F(65,10**12) and z_ceiling==F(90,10**12)
gap=2*p_floor-z_ceiling
assert gap>F(159,10**13)>0
# True original source D-density 4pz+2z²=-2z(2|p|-z)
# on the entire certified expanded physical J7 island.
D_island_upper=-(2*radius)*2*z_floor*F(159,10**13)
assert D_island_upper< -F("1.65e-36")
# Source-global (on full J7) p upper: since x<log9-B,
# d=B-x>2B-log9 > B/400 and log(B/d)<6, because e^6>400.
dmin=2*B-log9hi
assert dmin>B/F(400)
from math import factorial
assert sum((F(6)**k/F(factorial(k)) for k in range(14)),F(0))>400
p_max=F(723,10**13)
assert (-vlow)*(F(3)+c7hi)<p_max
# Pointwise D>=-2p², so the actual signed island cannot have
# magnitude greater than 2pmax² times its length.
D_island_lower=-(2*radius)*2*p_max*p_max
assert D_island_lower> -F("8.4e-36")
assert D_island_lower<D_island_upper<0
# If the NF404 CAP holds, D7<=-A. For N={x in J7:D_density<0},
# D7>=-2 pmax² meas(N); hence its negative support is nonlocal.
min_negative_measure=A/(2*p_max*p_max)
assert min_negative_measure>F(194,10000)
cell7_length_lo=log9lo-log8hi
cell7_length_hi=log9hi-log8lo
assert 0<cell7_length_lo<cell7_length_hi<F(3,25)
assert min_negative_measure>F(4,25)*cell7_length_hi
assert min_negative_measure>F(10000)*2*radius # vastly nonlocal
# D7=2(E7-Ep7) so NF404 demands >28% reduction of full principal J7 power.
ep7lo,ep7hi=map(F,nf453["original_j7_ep"])
assert F("3.62e-22")<=ep7lo<ep7hi<=F("3.63e-22")
assert A>F(28,100)*2*ep7hi
E7upper=ep7hi-A/2
assert E7upper<F("2.613e-22")
# Quantitative necessary original regularized energy Z7=int_J7 z².
# If Z7<=Z0, Cauchy plus P<=Ep7hi gives:
# Ep7-E7 <= 2 sqrt(P Z7)-Z7 <= 2 sqrt(Pmax Z0)-Z0 < A/2.
Z0=F("8.3e-24")
p_sqrt_hi=F(1906,10**14)
z_sqrt_hi=F(2881,10**15)
assert ep7hi<p_sqrt_hi**2
assert Z0<z_sqrt_hi**2
assert Z0<ep7lo
assert 2*p_sqrt_hi*z_sqrt_hi-Z0<A/2
# So original cap implies actual Z7>Z0, but Z7 is UNMEASURED.
out={
"pass":"NF463",
"standing":"SOURCE-CERTIFIED genuine enlarged J7 signed island; conditional whole-J7 spatial/correlation/regular-power obligations, D7 whole OPEN",
"source_sha256":S,"seams_sha256":G,
"source_receipts_SHA256":{"NF417":h417,"NF418":h418,"NF411":hjet,"NF453":h453,"NF462":h462},
"actual_J7_x0":"26/25","actual_J7_island_radius":str(radius),
"true_J7_z_island_strict_lower":"6.5e-11",
"true_J7_z_island_strict_upper":"9.0e-11",
"true_J7_principal_abs_lower":"5.299e-11",
"actual_island_signed_integral_strict_lower":"-8.4e-36",
"actual_island_signed_integral_strict_upper":"-1.65e-36",
"old_certified_island_signed_upper":"-8.6e-38",
"if_NF404_original_J7_required_D7_approx":format(float(-A),".17e"),
"original_full_J7_principal_abs_strict_sup":"7.23e-11",
"if_NF404_negative_D7_density_support_length_strict_gt":str(F(194,10000)),
"if_NF404_negative_support_fraction_of_J7_strict_gt":"16%",
"if_NF404_principal_energy_cancellation_fraction_strict_gt":"28%",
"if_NF404_whole_J7_pplusz_squared_energy_strict_lt":"2.613e-22",
"if_NF404_whole_J7_regular_z_squared_energy_strict_gt":"8.3e-24",
"measured_whole_J7_negative_support":False,
"measured_whole_J7_z_squared_energy":False,
"measured_whole_J7_signed_integral":False,
"original_NF404_cap":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN",
"next":"NF464 source-correlated J7 partition integration over substantial measure (>=0.0194 if original cap), using NF433 true branches and direct signed pz+z², not repeated point-island extension"}
print(json.dumps(out,indent=2))
if __name__=="__main__":
 import argparse
 ap=argparse.ArgumentParser();ap.add_argument("--output")
 args=ap.parse_args()
 if args.output:
  dst=Path(args.output);dst.parent.mkdir(parents=True,exist_ok=True)
  dst.write_text(json.dumps(out,indent=2)+"\n")
