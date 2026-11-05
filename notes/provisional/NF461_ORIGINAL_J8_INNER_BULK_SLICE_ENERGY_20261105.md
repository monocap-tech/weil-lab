# NF461 — Original physical J8 first interior bulk slice, 2026-11-05

**Standing: ACCEPTED scoped, original-source two-sided interior L2 upper.** The full bulk, NF404 and W-ODD-NEG remain OPEN. This pass extends the source-certified NF459 physical endpoint method; it is not eight-cell bulk closure.

## Previous / Current / Next

**Previous NF460:** The original cofinite residual h=f-P_V f has seven genuine nonzero support jumps and is not globally H1; there is no valid all-eight-cell uniform smooth approximation. NF459 had certified the complete positive/negative terminal collar d=B-|x|<=delta0=10^-15: T_collar<8e-32.

**Current NF461:** On the actual eighth physical positive cell, d=B-x, enlarge the endpoint segment to delta1=10^-13. Since the original n9 seam is at d=2B-log 9>1/1000, this interval crosses NO seam. Negative side mirrors by oddness. Reconstruct the identical original 242D polynomial-trigonometric-jet/sinh Gram, 4096-bit near-normal frame and both genuine n512,n513 exterior Schur probes, with no replacement of the 246-source original multiplier response. The 72-term *source-correlated* Taylor coefficients of the complete original evaluation vector, transformed to the normal frame before interval Horner, and a Cauchy tail paid at radius rho=10^-4, rigorously enclose K_V(x,x) on ALL x in [B-10^-13,B]:

    K_V(x,x) in [12521.0563 +/- 5.38e-5] (native Arb outward),
    in particular K_V<12996=114^2.

Source-normal projector power R+d12<(3.4e-11)^2 (NF403/NF404) thus yields the uniform ORIGINAL |Pi=P_V f|<114*(3.4e-11)=3.876e-9 on that extended segment.

**True original physical source action, paid analytically:** The original NF407 and NF446 identities for x=B-d in J8 give

    h(B-d)=(v/2)*log(B/d)+v*C8+z(B-d)-Pi(B-d),
    v=u4(B), C8=sum_{n=2,3,4,5,7,8,9} Lambda(n)/sqrt(n).

NF411/NF407 exact v and positive weights give |v|<1.17e-11 and C8<18/5. NF450 original continuous z(B) has |z(B)|<4.4e-10. NF451 authentic original compact-kernel modulus holds for 0<d<=delta1:

    |z(B-d)-z(B)|<d*(14000+600 log(2B/d))
                   <=delta1*(14000+600*32)=3.32e-9.

The logarithmic comparison log(2B/delta1)<32 is checked in *exact* rational arithmetic using e>8/3 and (8/3)^32>2B/delta1; monotonicity of d log(2B/d) also holds. Thus

    |v*C8+z(B-d)-Pi(B-d)| < 7.67812e-9 <8e-9.

With |v|/2<117/(2*10^13), the exact log-square primitive gives the **actual original two-sided physical residual power**

    2 int_0^delta1 |h(B-d)|^2 dd
      < 4 delta1 [(117/(2*10^13))^2 (32^2+2*32+2) +(8e-9)^2]
      =2.561492101e-29 <2.6e-29.

The first genuinely *bulk* slice delta0<d<=delta1 is contained in that segment, so its two-sided physical squared energy is separately certified <2.6e-29, albeit conservatively charging the old collar twice if compared naively. For the new remaining interior |x|<=B-delta1, the sufficient original NF404 power cap becomes

    T_interior <= gamma²-dUP-(Rhi-Rlo)-2.6e-29
                ≈3.28431328676142914e-26.

This is an acceptance **threshold** for the as-yet unmeasured interior, NOT a proved upper.

**Exact custody:** NF407 source SHA 0a83cdb7..., NF406 seams SHA c2731e3b..., NF458 rank SHA 9b9820a0..., original NF450/NF451, NF411 source coefficients, NF403/NF404 projection powers, unchanged. The original 72-jet method is generalized solely in permitted delta/rho to 10^-9. Native 244D run and independent original-source Fraction verifier both PASS [Actions #42083545372](https://github.com/monocap-tech/weil-lab/actions/runs/42083545372); job #127442555344 and source artifact #13442466230. See [exact verifier](../../scripts/local_replay/verify_nf461_original_cell8_inner_slice_exact.py).

**Scope:** True original inner part of J8 and its negative reflected counterpart CERTIFIED. The vast remainder of J8, all seven other positive cells, full bulk T, E78 full upper, NF404, W-ODD-NEG, even/whole Weil, operator-domain and RH are **OPEN**. The logarithmic endpoint is analytically integrated; no invalid global H1 or point-sample-to-integral promotion.

**Next bold NF462:** Move from an endpoint-local modulus to source-correlated panel integration farther inside genuine J8, using the NF446 compact joint archimedean kernel and the now-original 244D physical projection. Partition at n9 and charge all real seams; do not keep extending a coarse modulus until its L2 charge exhausts the admissible bulk budget.
