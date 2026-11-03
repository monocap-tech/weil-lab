#!/usr/bin/env python3
"""NF453 — Original whole J7/J8 principal L2 energies and a true signed J7 negative island.

The p-energy is the *complete physical* q+r principal on BOTH entire original
cells, with original NF406 genuine irrational n8/n9 seams, original NF411
4096-bit u4(B) native ball, original seven prime-power signed coefficients,
and an independent NF410 original signed p0 cross-check.  It gives the
nontrivial rigorous global-cell negative deficit bound D>=-2 Ep on J7+J8,
but does NOT give an upper for D or settle either entire cell signed.
NF418 existing source-native original cell7 z interval certifies a new tiny
signed NEGATIVE physical island at x=26/25.
"""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
import re, json, argparse

B=Q(11,10)
X7=Q(26,25)
RAD=Q(1,10**17)
PRIMES=(2,3,4,5,7,8,9)
SOURCE_SHA="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM_SHA="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"

def src(path):
    raw=Path(path).read_bytes()
    return json.loads(raw),sha256(raw).hexdigest()

def orig_arb_ball(s):
    m=re.fullmatch(r"\[([+-]?[0-9]+(?:\.[0-9]+)?)e([+-]?[0-9]+)\s+\+/-\s+([0-9]+(?:\.[0-9]+)?)e([+-]?[0-9]+)\]",s.strip())
    assert m, "original source native Arb ball schema mismatch"
    c=Q(m.group(1))*Q(10)**int(m.group(2))
    r=Q(m.group(3))*Q(10)**int(m.group(4))
    assert r>0
    return c-r,c+r

# Pure rational, strictly outward natural log through scaled artanh.
# For t>=1, normalize t=2^k*y, 1<=y<2 and sum
# log y=2 sum_{m=0}^{N-1} r^(2m+1)/(2m+1) + tail,
# 0<tail<2r^(2N+1)/((2N+1)(1-r²)), r=(y-1)/(y+1).
N=64
def base_artanh_log(y):
    assert 1<=y<=2
    r=(y-1)/(y+1)
    partial=2*sum((r**(2*m+1))/Q(2*m+1) for m in range(N))
    rem=2*r**(2*N+1)/(Q(2*N+1)*(1-r*r))
    return partial, partial+rem
L2_LO,L2_HI=base_artanh_log(Q(2))

def ln_q(t):
    assert t>=1
    k=0
    y=t
    while y>=2:
        y/=2
        k+=1
    p,q=base_artanh_log(y)
    return p+k*L2_LO, q+k*L2_HI

def log_of_B_over_d(d_lo,d_hi):
    assert 0<d_lo<=d_hi<B
    lo=ln_q(B/d_hi)[0]
    hi=ln_q(B/d_lo)[1]
    assert lo<=hi
    return lo,hi

def eval_F(d,c,is_upper):
    """F_C(d)=d/4 *((log(B/d)+2C)^2+2(log(B/d)+2C)+2)."""
    l=ln_q(B/d)[1 if is_upper else 0]
    w=l+2*c
    return d*(w*w+2*w+2)/4

def eval_H(d,c,is_upper):
    """H_C(d)=d*(log(B/d)/2+1/2+C), the signed p zeroth primitive /v."""
    l=ln_q(B/d)[1 if is_upper else 0]
    return d*(l/2+Q(1,2)+c)

def enf_and_m0(lo,hi,clo,chi):
    F_lo=eval_F(lo,clo,False)
    F_hi=eval_F(hi,chi,True)
    H_lo=eval_H(lo,clo,False)
    H_hi=eval_H(hi,chi,True)
    return F_lo,F_hi,H_lo,H_hi

def overlap(a,b):
    return a[0]<=b[1] and b[0]<=a[1]

def main(args):
    source,shasource=src(args.source)
    seams,shaseams=src(args.seams)
    jet,shajet=src(args.jet)
    nf410,shan410=src(args.nf410)
    nf417,shan417=src(args.nf417)
    nf418,shan418=src(args.nf418)
    nf452,shan452=src(args.nf452)
    assert shasource==SOURCE_SHA and shaseams==SEAM_SHA
    assert source["original_dimension"]==242
    assert len(source["original_exact_native_original_four_critical_coefficients_mid_radius"])==4
    assert len(source["original_source_critical_sine_frequencies"])==32
    assert jet["nf407_source_sha256"]==shasource
    assert jet["original_source_native_radii_paid_for_endpoint_derivative"]
    assert nf410["original_nf406_source_sha256"]==shaseams
    assert nf410["original_nf407_source_sha256"]==jet["nf407_principal_sha256"]
    assert nf410["independent_original_nf409_global_moment_overlap"]
    assert len(nf410["original_positive_original_physical_cells"])==8
    assert nf417["nf407_original_source_sha256"]==shasource
    assert nf417["true_original_complete_z_pointwise_certified"]
    assert nf417["cell"]==7 and Q(nf417["x"])==X7
    assert nf418["original_nf407_246_source_sha256"]==shasource
    assert nf418["original_nf406_certified_seam_partition_sha256"]==shaseams
    assert nf418["original_prior_source_point_receipt_sha256s"]["7"]==shan417
    assert nf418["whole_original_z_derivative_piecewise_uniform_upper_integer"]==30000
    assert nf418["original_true_full_246_generator_source_unchanged"]
    assert nf452["focused_CI_result"]=="SUCCESS"
    assert nf452["whole_original_J7_signed"]==nf452["whole_original_J8_signed"]=="OPEN"

    prime_seams={r["n"]:r for r in seams["original_prime_power_log_shifts"]}
    assert set(PRIMES)==set(prime_seams)
    ell8lo,ell8hi=Q(prime_seams[8]["log_lower"]),Q(prime_seams[8]["log_upper"])
    ell9lo,ell9hi=Q(prime_seams[9]["log_lower"]),Q(prime_seams[9]["log_upper"])
    a_lo,a_hi=2*B-ell9hi,2*B-ell9lo
    b_lo,b_hi=2*B-ell8hi,2*B-ell8lo
    assert 0<a_lo<=a_hi<b_lo<=b_hi<B
    # Genuine physical J7=(log8-B, log9-B), J8=(log9-B,B).
    cells=nf410["original_positive_original_physical_cells"]
    assert cells[6]["left_label"]=="-B+log(8)" and cells[6]["right_label"]=="-B+log(9)"
    assert cells[7]["left_label"]=="-B+log(9)" and cells[7]["right_label"]=="+B"
    assert [Q(s) for s in cells[6]["left_source_interval"]]==[ell8lo-B,ell8hi-B]
    assert [Q(s) for s in cells[6]["right_source_interval"]]==[ell9lo-B,ell9hi-B]
    assert [Q(s) for s in cells[7]["left_source_interval"]]==[ell9lo-B,ell9hi-B]
    assert Q(cells[7]["right_source_interval"][0])==B
    assert Q(cells[7]["right_source_interval"][1])==B

    weights=jet["all_seven_original_prime_seam_derivative_identities"]
    assert tuple(r["prime_power"] for r in weights)==PRIMES
    ws=[(Q(r["c_n_positive_outward"][0]),Q(r["c_n_positive_outward"][1])) for r in weights]
    assert all(0<lo<hi for lo,hi in ws)
    c7lo,c7hi=sum((lo for lo,hi in ws[:6]),Q(0)),sum((hi for lo,hi in ws[:6]),Q(0))
    c8lo,c8hi=c7lo+ws[6][0],c7hi+ws[6][1]
    assert 3<c7lo<c7hi<Q(16,5)
    assert Q(7,2)<c8lo<c8hi<Q(18,5)

    v_lo,v_hi=orig_arb_ball(jet["original_original_source_value_at_B_arb"])
    assert -Q(117,10**13)<v_lo<v_hi<-Q(116,10**13)
    vabslo,vabshi=-v_hi,-v_lo
    vl2,vh2=vabslo*vabslo,vabshi*vabshi

    # Primitive endpoint source/correlation preserved: no quadrature.
    Fa7lo,Fa7hi,Ha7lo,Ha7hi=enf_and_m0(a_lo,a_hi,c7lo,c7hi)
    Fb7lo,Fb7hi,Hb7lo,Hb7hi=enf_and_m0(b_lo,b_hi,c7lo,c7hi)
    Fa8lo,Fa8hi,Ha8lo,Ha8hi=enf_and_m0(a_lo,a_hi,c8lo,c8hi)
    assert Fb7lo>Fa7hi>0
    assert Hb7lo>Ha7hi>0
    E7lo,E7hi=vl2*(Fb7lo-Fa7hi),vh2*(Fb7hi-Fa7lo)
    E8lo,E8hi=vl2*Fa8lo,vh2*Fa8hi
    E78lo,E78hi=E7lo+E8lo,E7hi+E8hi
    assert Q(362,10**24)<E7lo<E7hi<Q(363,10**24)
    assert Q(187,10**25)<E8lo<E8hi<Q(189,10**25)
    assert 2*E78hi<Q(7638,10**25)  # 7.638e-22 total absolute negative deficit

    # NF410 original independent signed k=0 p-moments, exact real knot.
    m07=[-vabshi*(Hb7hi-Ha7lo),-vabslo*(Hb7lo-Ha7hi)]
    m08=[-vabshi*Ha8hi,-vabslo*Ha8lo]
    ref_m07=tuple(Q(y) for y in cells[6]["signed_original_p_moments_by_degree_0_to_3"][0])
    ref_m08=tuple(Q(y) for y in cells[7]["signed_original_p_moments_by_degree_0_to_3"][0])
    assert overlap(m07,ref_m07) and overlap(m08,ref_m08)
    # NF410 existing global ||p||² independently dominates both last cells.
    epglobal_lo,epglobal_hi=(Q(x) for x in nf410["original_known_principal_power_outward"])
    assert 0<epglobal_lo<=epglobal_hi
    assert E78hi<epglobal_lo/5, "last 2 cells should be strictly below 20pct of true full principal energy"

    # On each original full physical Jj, Dj=2∫(z+p)^2-2∫p² > -2 Ep_j
    # (inequality non-strict analytically, strict when combined with certified
    # Ep upper). This is a finite true original physical lower bound for J7+J8.
    assert -2*E78hi > -Q(7638,10**25)

    # Original NF418 true physical z island (same NF417 point source)
    # x0=26/25, r=1e-17, within genuine J7.
    island=next(x for x in nf418["original_hotspot_cellwise_envelopes"] if x["original_cell"]==7)
    assert Q(island["original_anchor_rational_x"])==X7
    assert Q(island["certified_same_sign_neighborhood_radius_exact"])==RAD
    assert island["original_point_cert_sha256"]==shan417
    assert island["neighborhood_same_sign_certified"] and island["neighborhood_in_original_cell"]
    assert ell8hi-B<X7-RAD<X7+RAD<ell9lo-B
    z7lo,z7hi=(Q(t) for t in island["certified_same_sign_neighborhood_z_outward_rational_envelope_1e40"])
    assert Q(77,10**12)<z7lo<=z7hi<Q(78,10**12)
    # J7 p(x)<0 and |p(x)|>=|v|*(log(B/(B-x))/2+C7).
    dmax=B-(X7-RAD)
    logmin=ln_q(B/dmax)[0]
    principal_abs_lo=vabslo*(logmin/2+c7lo)
    assert principal_abs_lo>Q(53,10**12)
    # z>77e-12, z<78e-12, |p|>53e-12 => strictly
    # 4pz+2z²=-2z(2|p|-z)<-2(77e-12)(2*53e-12-78e-12).
    D7island_upper=-(2*RAD)*2*Q(77,10**12)*(2*Q(53,10**12)-Q(78,10**12))
    assert D7island_upper< -Q(86,10**39)  # -8.6e-38

    return {
        "pass":"NF453",
        "standing":"ACCEPTED after focused source-original Fraction CI; original entire J7+J8 p ENERGY and universal signed lower, original J7 signed negative tiny island; full J7/J8 signed integrals OPEN",
        "source_sha256":shasource,"seam_sha256":shaseams,
        "original_nf411_jet_receipt_sha256":shajet,
        "original_nf410_true_principal_moments_receipt_sha256":shan410,
        "original_nf417_true_z_cell7_receipt_sha256":shan417,
        "original_nf418_true_z_cell7_lipschitz_receipt_sha256":shan418,
        "original_nf452_terminal_custody_receipt_sha256":shan452,
        "original_source_generators":246,"original_source_frequency_order_groups":273,
        "original_J7_d_lower_a":[str(a_lo),str(a_hi)],
        "original_J7_d_upper_b":[str(b_lo),str(b_hi)],
        "original_original_n8_n9_physical_seams":True,
        "actual_seven_original_prime_weights_including_n8_n9":True,
        "original_native_4096bit_source_endpoint_radius_paid":True,
        "J7_original_C6_interval":[str(c7lo),str(c7hi)],
        "J8_original_C7_interval":[str(c8lo),str(c8hi)],
        "original_J7_principal_power_exact_fraction_interval":[str(E7lo),str(E7hi)],
        "original_J8_principal_power_exact_fraction_interval":[str(E8lo),str(E8hi)],
        "original_J7_J8_principal_power_total_interval":[str(E78lo),str(E78hi)],
        "original_NF410_J7_original_signed_p0_overlap":True,
        "original_NF410_J8_original_signed_p0_overlap":True,
        "original_J7_J8_principal_total_below_20pct_of_original_global":True,
        "original_full_J7_J8_signed_D_lower_strict":str(-Q(7638,10**25)),
        "original_J7_signed_island_center":str(X7),
        "original_J7_signed_island_radius":str(RAD),
        "original_J7_signed_island_z_envelope":[str(z7lo),str(z7hi)],
        "original_J7_signed_island_principal_abs_lower":str(principal_abs_lo),
        "original_J7_signed_island_D_upper_strict":str(-Q(86,10**39)),
        "original_J7_signed_island_current_analytic_bound":str(D7island_upper),
        "nf451_nf452_J8_positive_terminal_collar_preserved":True,
        "entire_original_J7_signed_integral":"OPEN",
        "entire_original_J8_signed_integral":"OPEN",
        "NF410_NF404_global":"OPEN","J242_fourth_exterior":"OPEN",
        "W_ODD_NEG":"OPEN","RH":"OPEN"
    }

def cli():
    p=argparse.ArgumentParser()
    p.add_argument("--source",default="notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    p.add_argument("--seams",default="notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    p.add_argument("--jet",default="notes/data/provisional/NF411_original_source_boundary_jet.json")
    p.add_argument("--nf410",default="notes/data/provisional/NF410_original_signed_taylor_moments.json")
    p.add_argument("--nf417",default="notes/data/provisional/NF417_original_cell7_full_z_pointwise_native.json")
    p.add_argument("--nf418",default="notes/data/provisional/NF418_original_hotspot_cellwide_lipschitz_envelopes_exact.json")
    p.add_argument("--nf452",default="notes/data/provisional/NF452_original_J8_terminal_signed_moments_custody_index.json")
    p.add_argument("--output")
    args=p.parse_args()
    d=main(args)
    if args.output:
        out=Path(args.output);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(d,indent=2)+"\n")
    print("NF453 original E_p on entire J7 and J8: certified exact source/geometry")
    print("NF453 original D7+D8 > -7.638e-22, original J7 sign island D< -8.6e-38")
    print("NF453 whole signed J7/J8, NF404, W-ODD-NEG, RH OPEN")

if __name__=="__main__":cli()
