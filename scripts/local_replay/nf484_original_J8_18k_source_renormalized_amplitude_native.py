#!/usr/bin/env python3
"""NF484 immutable original source-native 18,000 renormalized image amplitudes.

c_m = T_m authentic NF443/NF446 ORIGINAL two matched image amplitude.
v = U(B), same original NF407 source shared with the physical principal log.
d_m = c_m - v/(m+1/4), exactly removes its same-source logarithmic image
coefficient before ANY source-independent coefficient projection/Gram.

Only source coefficient balls are emitted, not a physical signed J8 integral.
420 significant decimals preserve absolute <10^-240 interval widths even if
low-m source modes require cancellation among coefficients near 10^140:
a 145-significant-digit interval can have an absolute width ~4e-7 there.
This is an output decimal CARRIER issue, not a 4096-bit Arb failure.
Complete original finite 18000-image, odd m0 sinh pole, 273 grouped (f,k)
source modes/99 real frequencies and 246 original source dyadic generators.

Original input uncertainty sum S0 < 10^-700 is NOT already included in
native mid/radius balls. The independent Gram verifier must pay it.
"""
from __future__ import annotations
from fractions import Fraction as Q
from pathlib import Path
from flint import arb, acb, ctx
import argparse,json,sys
from nf415_original_cell6_I1_validated_acb import native_source,U,A,C
from nf454_original_n9_contact_native_moment import read,enclosure,B,SRC_SHA,SEAM_SHA
import nf471_original_J7_joint_arch_mean_native as parent
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
SOURCE_PARENT="f50e49cdc02b5e1eaacce7f8a66733fce9bc6f05"
BITS=4096
M=18000
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--start",type=int,required=True)
    ap.add_argument("--stop",type=int,required=True)
    ap.add_argument("--source",default="notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    ap.add_argument("--seams",default="notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    ap.add_argument("--output",required=True)
    args=ap.parse_args()
    assert 0<=args.start<M and args.start%2000==0 and args.stop==args.start+2000 and args.stop<=M
    ctx.prec=BITS
    original,sha=read(args.source);seams,sr=read(args.seams)
    assert (sha,sr)==(SRC_SHA,SEAM_SHA)
    assert original["original_dimension"]==242
    assert len(original["original_exact_native_original_four_critical_coefficients_mid_radius"])==4
    assert len(original["original_source_critical_sine_frequencies"])==32
    terms,pole,s0=native_source(original)
    assert len(terms)==273 and s0<Q(1,10**700)
    assert all(0<f<883 and 0<=k<=13 for f,k,c in terms)
    raw=sum((abs(c)*B**k for f,k,c in terms),abs(pole))
    assert raw<Q(10)**160
    groups={}
    for f,k,c in terms:groups.setdefault(f,[]).append((k,c))
    assert len(groups)==99
    source=U(original)
    v=source.at(C(A(B))).real
    vg0,vg1=enclosure(v,420)
    assert vg0<vg1<0
    gg=parent.image_groups(groups)
    assert len(gg)==99
    pol=A(pole)
    Bp2=(A(B)/2).exp()
    Bm2=(-A(B)/2).exp()
    rows=[]
    maxabs=Q(0)
    maxrad=Q(0)
    m0source=None
    for m in range(args.start,args.stop):
        aa=acb(A(Q(4*m+1,4)))
        total=arb(0)
        for lam,coefficients in gg:
            inv=1/(aa-lam/2)
            power=inv
            acc=acb(0)
            for c in coefficients:
                acc+=c*power
                power*=inv
            total+=2*acc.real
        if m==0:
            # Authentic odd sinh-pole finite exception: NO 1/m.
            total-=pol*Bm2
        else:
            total+=pol*(Bp2/A(m)-Bm2/A(Q(2*m+1,2)))/2
        # The SHARED original source leading coefficient EXACTLY v=U(B).
        dm=total-v/A(Q(4*m+1,4))
        clo,chi=enclosure(total,420)
        dlo,dhi=enclosure(dm,420)
        assert clo<=chi and dlo<=dhi
        maxabs=max(maxabs,abs(dlo),abs(dhi))
        maxrad=max(maxrad,chi-clo,dhi-dlo)
        if m==0:m0source=[str(clo),str(chi)]
        rows.append([str(clo),str(chi),str(dlo),str(dhi)])
        if (m+1)%250==0:print("NF484 authentic renormalized original images",m+1,"/",args.stop,flush=True)
    assert maxrad<Q(1,10**240),str(maxrad)
    assert maxabs<Q(10)**180,"METHOD STOP if original first 18k d_m exceeds crude source envelope 10^180"
    out={
      "pass":"NF484-source-native",
      "part":"original-18k-renormalized-image-coefficient-block",
      "original_nf407_source_sha256":sha,
      "original_nf406_seams_sha256":sr,
      "original_immutable_native_source_parent":SOURCE_PARENT,
      "original_246_generators":True,"original_273_grouped_modes":True,
      "original_99_frequencies":True,"original_32_critical_sines":True,
      "original_sinh_m0_removable_pole":True,
      "native_precision_bits":BITS,
      "original_source_input_radii_sum_lt":"1e-700",
      "all_finite_original_image_coefficients_m_from":args.start,
      "all_finite_original_image_coefficients_m_stop":args.stop,
      "original_source_v_at_B_outward":[str(vg0),str(vg1)],
      "original_source_Tm_and_same_source_dm_outward":rows,
      "original_dm_m_is":"T_m - U(B)/(m+1/4), original 273-mode 2-endpoint matched source",
      "original_m0_true_sinh_exception_source":m0source,
      "native_maximum_dm_absolute_strict_upper":str(maxabs),
      "native_maximum_coefficient_outward_width":str(maxrad),
      "actual_J8_terminal_signed_upper":"OPEN",
      "NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN"
    }
    dest=Path(args.output);dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(out,separators=(",",":"))+"\n")
    print("NF484 full original source c_m and renormalized d_m coefficient source-custody chunk DONE",args.start,args.stop,"maximum",float(maxabs),flush=True)
if __name__=="__main__":main()
