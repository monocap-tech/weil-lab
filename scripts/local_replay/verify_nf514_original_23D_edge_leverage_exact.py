#!/usr/bin/env python3
"""NF514 exact source-original 23D subspace witness for local selected leverage.

No numerical inverse is trusted: the candidate is ONLY an explicit integer
selected-source direction. Every integral and strict inequality is checked
in rational / fixed-point integer arithmetic with analytic error bounds.
"""
import argparse, hashlib, json, math, sys
from pathlib import Path
from fractions import Fraction as F
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
SOURCE_SHA="ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec"
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAMS="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
S=10**160;T=10**250;B=F(549,500);h=B/4096
def read(p):
    raw=Path(p).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()
def atan(q,n=140):
    s=sum(((-1)**j*q**(2*j+1)/F(2*j+1) for j in range(n)),F(0))
    er=q**(2*n+1)/F(2*n+1)
    return (s,s+er) if n%2==0 else (s-er,s)
def main():
    ap=argparse.ArgumentParser()
    for name in ("native","seed","output"):ap.add_argument("--"+name,required=True)
    o=ap.parse_args()
    src,sha=read(o.native);seed,sseed=read(o.seed)
    assert sha==SOURCE_SHA and src["pass"]=="NF504-native"
    assert src["source_original_NF407_sha256"]==SRC
    assert src["source_original_NF406_sha256"]==SEAMS
    assert src["original_selected_J_dimension"]==242
    assert src["original_exterior_center_radius"]=="549/500"
    assert src["original_support_saturated_physical_Hilbert_gate"]=="CERTIFIED_PHYSICAL_SUPPORT_NO_GO"
    nodes=[(F(f),k) for f,k in seed["original_source_basis_nodes"]]
    assert len(nodes)==23 and src["original_source_basis_nodes"][:23]==[[str(f),k] for f,k in nodes]
    assert nodes==[(F(37,64),k) for k in range(14)]+[(F(211,128),k) for k in range(9)]
    denom=int(seed["coefficient_denominator"])
    c=list(map(int,seed["integer_coefficients"]))
    assert len(c)==23 and max(map(abs,c))==denom
    assert sum(map(abs,c))<5*denom
    a,b=atan(F(1,5)),atan(F(1,239))
    pl,ph=16*a[0]-4*b[1],16*a[1]-4*b[0]
    assert 3<pl<ph<F(22,7)
    p_int=int(pl*S)
    assert F(p_int,S)<=pl and ph<F(p_int+1,S)
    trig={}
    for f in set(f for f,k in nodes):
        wl,wh=2*f*pl,2*f*ph
        w=int(wl*S)
        assert F(w,S)<=wl and wh<F(w+6,S)
        trig[f]=[S]+[w**j//(S**(j-1)*math.factorial(j)) for j in range(1,161)]
    q=[0]*175
    for ci,(f,k) in zip(c,nodes):
        for j,z in enumerate(trig[f]):
            if j%2==k%2:continue
            sign=-1 if ((j-1)//2 if k%2==0 else j//2)%2 else 1
            q[k+j]+=sign*(ci*z//denom)
    assert all(q[j]==0 for j in range(0,len(q),2))
    assert 2*max(f for f,k in nodes)*F(22,7)*B<12
    assert F(12)**161/math.factorial(161)<F(1,10**112)
    assert 5*(F(11,10)**13)*F(12)**161/math.factorial(161)<F(1,10**109)
    assert 23*161*(F(11,10)**174)/S<F(1,10**145)
    assert 5*(F(11,10)**13)*6*B/S<F(1,10**150)
    delta=F(1,10**100)
    envelope=sum((F(abs(v),S)*B**i for i,v in enumerate(q) if v),F(0))
    assert envelope<10**20
    # Full support |v-q|<=delta; hence |v²-q²|<=2*envelope*delta+delta².
    error=2*B*(2*envelope*delta+delta**2)
    poly=[0]*(len(q)*2-1)
    active=[(i,v) for i,v in enumerate(q) if v]
    for i,vi in active:
        for j,vj in active:poly[i+j]+=vi*vj
    assert all(poly[i]==0 for i in range(1,len(poly),2))
    polyabs=sum(map(abs,poly))
    def integrate(lo,hi):
        assert 0<=lo<hi<=B
        n=0
        for degree,coeff in enumerate(poly):
            if not coeff:continue
            factor=2*(hi**(degree+1)-lo**(degree+1))/F(degree+1)*T
            n+=coeff*(factor.numerator//factor.denominator)
        return F(n-polyabs,S*S*T)-error,F(n+polyabs,S*S*T)+error
    total=integrate(F(0),B)
    assert total[0]>0
    cases=(("H4095",B-h,B,F(3,25),F(1,5)),
           ("H4094",B-2*h,B-h,F(13,100),F(1,6)),
           ("H4094_union_H4095",B-2*h,B,F(1,10),F(2,5)))
    found={}
    for name,l,r,old_threshold,floor in cases:
        z=integrate(l,r)
        low,upper=z[0]/total[1],z[1]/total[0]
        assert floor*total[1]<z[0]
        assert 0<old_threshold<floor<low<=upper
        found[name]={"lower":str(low),"upper":str(upper),
                     "display":[float(low),float(upper)],
                     "NF513_conditional_no_go_threshold":str(old_threshold),
                     "strict_simple_rational_floor":str(floor),
                     "threshold_not_reachable_by_actual_full_tau":True}
        print("Original J242 tau",name,">",floor," witness",float(low),flush=True)
    out={"pass":"NF514-authentic-original-selected-23D-subspace-leverage-lower-exact",
         "standing":"SOURCE-EXACT 23D source-selected Rayleigh witness lower bounds full J242 tau; NF513 cheap conditional no-go tests impossible. Named physical NF404 and RH OPEN.",
         "original_NF505_native_SHA256":sha,"witness_seed_SHA256":sseed,
         "source_nf407_SHA256":SRC,"source_nf406_SHA256":SEAMS,
         "original_selected_basis_first_23":[[str(f),k] for f,k in nodes],
         "original_selected_true_rank":242,
         "original_basis_witness_coefficients_scale":str(denom),
         "original_basis_witness_coefficients_integer":list(map(str,c)),
         "pi_rational_Machin_terms":140,
         "original_sine_cosine_Taylor_degree":160,
         "fixed_source_polynomial_scale":str(S),
         "spatial_integral_fixed_point_scale":str(T),
         "witness_uniform_source_analytic_approx_error_upper":str(delta),
         "witness_pointwise_polynomial_abs_envelope_upper":str(envelope),
         "witness_squared_integral_error_upper":str(error),
         "witness_full_original_O_L2_squared_outward":list(map(str,total)),
         "original_selected_subspace_rayleigh_leverage_lower_by_named_cell":found,
         "NF513_original_conditional_named_support_no_go_gates":"UNREACHABLE_FOR_THE_ACTUAL_242D_SELECTED_TRACE_LEVERAGE",
         "actual_full_original_J242_trace_leverage_values":"UNCOMPUTED",
         "original_globally_fitted_local_residual_eH":"OPEN",
         "original_NF404_named_cell_physical_verdict":"OPEN",
         "original_Weil_multiplier_image_graph_domain":"OPEN",
         "W_ODD_NEG":"OPEN","RH":"OPEN"}
    Path(o.output).write_text(json.dumps(out,indent=2)+"\n")
if __name__=="__main__":main()
