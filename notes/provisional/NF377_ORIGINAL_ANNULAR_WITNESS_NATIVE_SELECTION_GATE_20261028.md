> **NF377 CORRECTION / EXACT-RATIONAL METHOD-GATE — 2026-10-28 Pacific:** The existence lemma guarantees `||q_i||²>=h/2` for some i, not necessarily the *strict* inequality `>h/2` used in the initial script. The native selector has been corrected to certify `||q_i||²>(49/100)h=(539/492000)`, which is **strictly guaranteed attainable** by the original `>=h/2` theorem. A single 242-dimensional preconditioned interval inverse is reused across candidate annuli rather than solving the same Gram system hundreds of times. No individual annulus is certified while CI is queued. The original NF375 cutoff `2^20` exact-rational direction-four highband bound is `beta=2850389356588036711829238471476032212853080316741097/(1572864*10^58)≈1.8122287474e-13`. Therefore a **whole-frequency** sign-box pairing can STOP the NF375 `1.5e-13` lowband sufficient gate only if `|W(u4,q)|/||q|| > beta+1.5e-13≈3.3122287474e-13`, *subject to an exact original form/pole/domain identity*. The entirely rational conservative absolute-squared sufficient threshold is `|W(u4,q)|²>(3313/10^16)²*(11/4920)`, since `||q||²<=h`; **no such signed pairing is measured**. The threshold is replayable in [exact Fraction script](../../scripts/local_replay/nf377_exact_annular_fullband_stop_threshold.py). These new constraints supersede any historical strict half-claim below; no method promotion/closure.

# NF377 — Original annular exterior witness selection: native physical certificate gate

**Status:** COMPUTATION IMPLEMENTED / NATIVE GITHUB CI QUEUED (as of 2026-10-28 Pacific); **no selected annulus accepted yet, no signed continuum pairing, no method promotion**. This remains a bounded informal external-method investigation attached to draft PR #361, not a new RH-facing branch. `W-ODD-NEG` OPEN.

## Previous cursor / current / next

Previous: NF376 genuine original smooth fifth exterior test `q5` was strictly linearly independent but only `<3e-20` of its physical *squared* norm lay outside the four already fitted exterior directions, giving a tiny `||q5_perp||≈2.04636e-89`. The external Suzuki/Mittermeier paper motivates testing normalized odd **sign-box annuli**, not further smooth near-fitted harmonics.

Current: `scripts/verify_nf377_original_annular_outfit_witness.py` computes exact signed odd annulus moment primitives using inherited 4096-bit Arb, **original J242 Gram and original F4**, SHA-pinned PR350/PR355/NF369 inputs, exact frame and 16 parent-quotient overlap checks, and a 5th test-vector Schur subtraction against all four fitted E modes. The whole selected carrier remains unchanged.

Next: require a **successful original native workflow** `.github/workflows/nf377-original-annular-exterior-witness.yml` naming one explicit index `i`, rational endpoints `[(i-1)*11/4920, i*11/4920]`, outward `||q_i||²>11/9840`, and an archived report including strict signed *point* samples. Only then decide whether to evaluate one genuine original signed continuum dual pairing.

## Mathematical reason a candidate must exist

Take `B=11/10`, `n=492`, `h=B/n=11/4920`. Each `delta_i=2^-1/2 sgn(x) 1_( (i-1)h<|x|<=ih )` has `||delta_i||²=h`; the normalized `delta_i/sqrt(h)` are orthonormal.

The physically odd original subspace `S=J242+span(E4)` has rank `<=246`. Bessel gives `Σ_i ||P_S (delta_i/sqrt h)||²<=246`, hence some `i` satisfies `||(I-P_S)delta_i||²>=h/2=11/9840`. Nothing about actual signed Weil response follows from this dimension inequality.

The native program tests `i=1,492,246` first, then the remaining indices if needed. This is only an evaluation order: acceptance for a **specific** index comes from an outward certified original physical projection, *not* from assuming the first candidate succeeds.

## Exact original projection math, and what to check

Define `J` 242-column physical source synthesis, `F` the same original four PR355 critical functions, `H=J*J`, `V=J*F`, `G=F*F`, `X_F=H^-1 V`, `S_F=G-V*X_F`. For annulus `delta_i` set `b=J*delta_i`, `c=F*delta_i`, `X_d=H^-1 b`, `r²=h-b*X_d`, `z=c-V*X_d`, and

`||q_i||² = r²-z* S_F^-1 z,\quad q_i=delta_i-P_{J+E4} delta_i`.

The script implements the inversion in the preconditioned exact physical frame `D (D*H D)^-1 D*...` and checks overlap against all 16 preexisting original NF369 four-quotient Gram intervals. It stops upon a **strict** interval lower `q_i²>h/2`. A large number printed by an uncertified floating solver would NOT pass.

To calculate analytic inner products with a physical odd original source `x^k sin(2πcx)` for even k or `x^k cos(2πcx)` for odd k, each annular overlap is `sqrt2 ∫_((i-1)h)^(ih) f(x) dx`, with exact trigonometric primitive recurrences for arbitrary polynomial order and `2(cosh(t/2)-1)` for the inherited sinh pole. An independent local mpmath comparison of primitive differences with direct quadrature on three representative J-generators (low frequency, degree 4, high frequency degree 3) gave residuals near `1e-62` at 60 decimal digits. This verifies the formula implementation design, **not** the full Arb native result.

## Signed evidence is not an integral

After a selected annulus is certified, the program computes six actual inherited real-frequency signed multiplier knots `xi=1/4,1,4,8,16,32` for `u4` and projected `q_i`. This is *genuinely signed original point evidence*, but **not** `I4(q_i;2^20)`. Signs at finitely many frequencies have no integration consequence without interval curvature/quadrature bounds.

The prior NF375 cutoff `2^20` and sufficient method threshold `h4=1.5e-13` remain the same. Once a real annulus is selected, any lower bound `|I4(q_i;2^20)|>h4||q_i||` would STOP only the NF375 individual direction-four sufficient residual method, **not** W-ODD-NEG. A small pairing cannot give the missing norm upper.

## Separate decisions

- **Informal continuation:** implementation and queued CI are an allowed preflight. Not a promoted external method.
- **Method promotion:** accepted specific original physical annulus **plus** full interval signed continuum integral, source covariance and highband/domain payment that change the live NF376 acceptance or STOP test. The source theorem/location and original convention transfer must be pinned independently.
- **Theorem closure:** complete original odd positivity under canonical O1/O2, including full Schur complement, other 238 directions and original domain. Even/whole Weil and RH remain separate open obligations.

**Custody:** additive script, narrowly scoped GitHub workflow, this note. No rewriting NF356–NF364 historical data, no source addition to J242, no changes to `research/obligations.json` or imported-source pins, no merge.
