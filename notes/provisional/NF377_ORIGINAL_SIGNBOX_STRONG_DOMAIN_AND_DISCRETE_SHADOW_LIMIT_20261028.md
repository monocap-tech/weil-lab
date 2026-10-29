# NF377 — Original annular strong-domain entry and discrete-shadow limit

**2026-10-28 Pacific; provisional analytic clarification.** This extends the informal sign-box-to-original-J242 comparison on draft PR #361. Not a completed original source-pairing certificate, not a source-pinned imported Mittermeier theorem, not method promotion, not an NF375 STOP, and not `W-ODD-NEG` closure. The original carrier and source set are unchanged.

## Previous / current / next

**Previous:** Exact Bessel dimension counting shows at least one of 492 normalized odd annuli has at least half its physical squared norm outside `S=J242+span(E1,...,E4)` (rank <=246). Original 4096-bit selection CI and conditional exact-Fraction highband threshold CI are QUEUED; no specific annulus and no signed pairing are accepted.

**Current:** Prove directly that each raw sign-box annulus and each **finite original J242+E4-projected** annular diagnostic belongs to the strong domain of the **original logarithmically growing Fourier signed multiplier** under its inherited local-boundedness assumption, even though the boxes jump. Give a numerical-tail bound for the RAW annulus alone and explicitly show why 492 finite cell measurements cannot recover a general complete signed residual upper bound.

**Next:** Native CI identify `i` and enclose `||(I-P_S)delta_i||²>(49/100)(11/4920)`; then a SINGLE original signed continuum dual calculation with the source/normalization/pole and NF375 highband paid.

## Direct Fourier transform and original strong Fourier-multiplier domain

Let `B=11/10`, `n=492`, `h=B/n=11/4920`, `a=(i-1)h`, `b=ih`. Define the Mittermeier-normalized **physical odd annulus**

`delta_i(x)=2^(-1/2) sign(x) 1_(a<|x|<=b)`.

It is compactly supported, `||delta_i||²=h`, and is a difference of two normalized odd sign boxes. For the original Fourier convention `hat f(xi)=int f(x) exp(-2 pi i xi x) dx`, exact elementary integration gives for `xi != 0`

`hat(delta_i)(xi)=(-i sqrt(2)/(2 pi xi)) [cos(2 pi xi a)-cos(2 pi xi b)]`.

Hence `|hat(delta_i)(xi)|<=sqrt(2)/(pi|xi|)`. More generally, every compactly supported bounded-variation (BV) test `f` satisfies `|hat f(xi)|<=TV(f)/(2 pi |xi|)` by distributional integration by parts; each original selected generator `x^k sin(2 pi c x)` or `x^k cos(2 pi c x)`, the original `sinh(x/2)` pole, and the four original finite sources is compact BV after restriction to `[-B,B]`. Therefore each *actual* orthogonalized `q_i=delta_i-P_S delta_i` is a **finite BV linear combination** (no infinite-source assumption), hence has an `O(1/|xi|)` Fourier tail.

Under NF375's original multiplier bound `|m(xi)|<=17+log|xi|` for `|xi|>=1` and local boundedness on finite frequency intervals, `m hat(q_i)∈L²(R)`, so every such `q_i` belongs to the **strong log-multiplier domain** of the zero-extended Fourier action `m(D)`. This is a **narrow original Fourier-domain membership lemma**; it does NOT establish exact Connes/Weil `W` sign, pole correction, the closure of the full physical carrier realization, or equivalence with Suzuki's normalizations. It also does not yield a uniform bound on `TV(q_i)` without original projection coefficients.

For **raw** `delta_i`, both Fourier half-lines obey the explicitly computable bounds at `Lambda=2^20`:

`int_(|xi|>Lambda)|hat(delta_i)(xi)|² dxi < 4/(9 Lambda) = 1/2359296`,

`int_(|xi|>Lambda)|m(xi) hat(delta_i)(xi)|² dxi < [4/(9 Lambda)]*[(17+log Lambda)²+2(17+log Lambda)+2] < 4100/(9 Lambda) = 1025/2359296 < 1/2000`.

Proof uses `pi>3`, `log2<7/10` so `17+log(2^20)<31`, and exact integral `int_Lambda^infty (17+log xi)² xi^-2 dxi = ((17+log Lambda)² + 2(17+log Lambda)+2)/Lambda`. The two rational bounds are independently replayed in `scripts/local_replay/nf377_annular_strong_domain_bound.py` (local PASS). These tail numbers apply to **raw annulus** only; transferring them unmodified to `q_i` would discard its potentially huge finite projection correction and is PROHIBITED.

## Exact information insufficiency of a finite annular grid

Fix any finite original selected-plus-fitted odd space S (dim <=246). The map from an arbitrary odd smooth residual `r∈C_c^infty((-B,B))∩S^perp` to its 492 annular observations `(<r,delta_1>,...,<r,delta_492>)` is **not injective**: impose the finite linear constraints of orthogonality to S and to the 492 annuli on the infinite-dimensional odd smooth test space. Its kernel contains a nonzero test. Scaling that test changes its L2 norm arbitrarily while all 492 observations remain zero. Thus **no uniform whole-exterior L2 norm upper bound can follow from only the 492 exact cell observations without additional regularity or inverse-response information**.

This is an EXACT information-type STOP for a naive finite-grid `all small observations => small full residual` inference, **not** a STOP for the NF375 lowband method on its fixed actual `u4`, and not a statement that no enriched bandlimited sampling or a priori derivative bound could control it. One well-chosen annular pairing is still valid as a *lower-bound* obstruction witness.

## Decision / standing

- **PASS (analytic):** all finite selected-plus-fitted annular `q_i` lie in the original Fourier-log strong domain given inherited `m` bounds/local boundedness; exact raw-annulus Fourier and two rational highband tail caps; finite annulus data alone insufficient for universal full-residual upper.
- **PENDING (native):** identify one original `i` with outward physical quotient norm >49/100 of its raw annulus norm; all 492 are explicit candidate observables, no new exceptional source.
- **OPEN:** quantitative *projected* `q_i` highband, original signed complete `<W u4,q_i>`, source-normalization/pole identification to `Psi`, actual original lowband `I4`, full inverse response, 238 remaining selected directions, form realization, W-ODD-NEG, even/whole Weil and RH.

**Promotion condition:** actual original signed continuum witness with justified identification and error payment changes a live NF376 accept/STOP decision. **Closure condition:** full original odd-operator positivity and remaining canonical domain/infinite coupling conditions. These are separate gates; neither met.
