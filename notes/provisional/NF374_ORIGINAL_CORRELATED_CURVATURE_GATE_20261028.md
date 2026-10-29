# Weil-Lab — NF374 original physically correlated matched exterior curvature

**Pre-computation gate / GitHub custody:** 2026-10-28. **Previous:** NF373 original J242 endpoint value and derivative certified; its conditional high-tail step requires a bound on `K4 = integral_0^(11/10) |w4''|`. **Current:** Compute all four genuine second-derivative energies using the *unchanged original physical* 242-source frame, four critical probes, NF369 dyadic Y0 and NF370 T. **Next:** Accept or stop the `K4<=1/100` sufficient route; then, only if accepted, compute correlated low-frequency residual. Whole signed Schur and RH remain OPEN.

The existing original native source/physical coefficient calculation is repeated in 4096-bit Arb to obtain `X=H^{-1}V` (via a verified physical preconditioner), `M=(I+Y0)T`, and `w = (F-JX)M`. On the physical open interval `(-B,B)` with `B=11/10`, differentiate the original smooth trigonometric and sinh source terms **symbolically** and compute all actual second-derivative source Gram entries `H2=<J'',J''>`, mixed `V2=<J'',F''>`, and source `G2=<F'',F''>`. Keep all **correlated** signed cross terms in

`S2 = G2 - V2^T X - X^T V2 + X^T H2 X`,

`D2 = M^T S2 M`, `||w_i''||²_(L²(-B,B)) = (D2)_{ii}`.

Use parity and Cauchy–Schwarz: `K_i <= sqrt(B/2) ||w_i''||_(L²(-B,B))`. The rigorous outward 4096-bit upper is compared with `1/100`; the result of that test is **reported, not assumed**. If it fails, the test does not imply the true `K4>1/100`; it means this sufficient L2 route did not certify it. No extra sources and no replacement Weil operator. The derivatives refer to the smooth interior; distributional boundary terms of the zero extension are **not** misidentified with interior derivatives.

The native task also requires the same original 16 physical quotient Gram overlaps as NF373. This is a finite original-source calculation with inherited native/analytic assumptions, **not** the full high-frequency multiplier, the 242D exterior inverse, the missing 238 directions or RH. Report and CI to be attached on this draft branch without any per-pass custody permission.
