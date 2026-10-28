# NF366 — Bounded negative-part transfer from the accepted physical quotient

**Standing:** exact-rational replay of *previously accepted* original PR #355 native 4×4 physical quotient balls and an analytic norm estimate; inherited original operator/form realization still requires review. No full original Weil positivity, inverse response or RH claim. J242, four original critical functions and all seven primes unchanged.

## Original native quotient

Let F:R⁴→Hodd be the four original PR348 critical functions; P is the physical projection on the unchanged selected J242 and Q=I−P. In PR355, the complete physical quotient Gram S=(QF)*QF is rigorously enclosed in native Arb balls. Sum the FOUR rational upper endpoints of its diagonal:

  0 <= tr(S) < 2^-604.

This follows from SHA-pinned original PR355 artifact 12776684037, ZIP SHA256 f7b64ceead7500fca389e3b994a208a6e8aae5be3270b750ab586e5ebe1fa1d0, original_exterior_scalar_floor_stop.json SHA256 d853e2ecf665b8bb3978ee203371c07f67d050b79e7427d6c673331fd1d60ab9. The diagonal values are ~1.0743255e-183, 2.3926661e-185, 2.8696804e-184 and 9.4186302e-183, giving trace ~1.08038503e-182 (decimal display only; rational comparison is exact).

Since S is a physical Gram, for every z∈R⁴:

  ||QFz||² <= tr(S)||z||².

No assumption of diagonal signed-form orthogonality is made.

## Entire negative multiplier norm

The complete original signed symbol is

  m(xi)=Re psi(1/4+i pi xi) - log pi
       -2 sum_(n∈{2,3,4,5,7,8,9}) (Lambda(n)/sqrt(n))cos(2 pi xi log n).

Let kminus=(1/1000-m)_+, Kminus the corresponding nonnegative compressed Fourier multiplier. The positive Euler digamma expansion yields Re psi(1/4+i pi xi)>=psi(1/4). The classical exact value psi(1/4)=-EulerGamma-pi/2-3log2 and EulerGamma<1, pi<4, log2<1, log pi<2 give archimedean >=-8. The accepted SI06 *complete seven-prime* amplitude is <70751/10000<8. Hence m(xi)>-16, kminus(xi)<17 for all real xi; physical compression gives ||Kminus||<=17. This estimate covers all frequencies; it is not an interval sampled bound.

## Strict four-column transfer

For p=P Fz and q=Q Fz,

  ||Q Kminus(Fz-p)||² = ||Q Kminus QFz||²
      <= 17² tr(S)||z||² < 10^-179||z||².

The verified exact value of the bound is approximately 3.122313e-180. This transfers the BOUNDED negative action between f and Pf to negligible error; it does not transfer the UNBOUNDED positive action Astar from f to Pf.

The actual NF362 Neumann forcing for e=p-v_p therefore decomposes as

  g=Q Kminus e = Q Kminus f − Q Kminus q − (Q Kminus Q)v_p.

Only QKminus q is paid by this certificate. The positive exterior Riesz response v_p and the last term are **uncomputed**. Do not infer g, D_3 or global signed Schur positivity.

## Replay and stop
Script scripts/local_replay/nf366_negative_quotient_transfer.py downloads PR355 original artifact (or takes --offline ZIP), checks both SHA256, reconstructs every native dyadic diagonal ball and tests tr(S)<2^-604 and 289 tr(S)<10^-179 in exact Fraction arithmetic. Original native interval correctness and analytic domain assumptions are inherited, not newly proven by this replay.

**Next:** matched exterior-positive response with the exact p/q decomposition; avoid any false small-Qf ⇒ small-Astar-Qf argument. W-ODD-NEG, even/whole form, CC27/F4 and RH all OPEN.
