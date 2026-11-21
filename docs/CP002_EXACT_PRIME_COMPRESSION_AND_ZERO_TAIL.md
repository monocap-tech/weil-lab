# Weil-Lab — CP002
## Exact original prime-compression topology and a quantitative zero-side tail interface

**Separate cross-projection track, stacked on CP001 PR #790.** Preserve Phase IV's original IV020 PR #788 (uncompiled 1/10 enlarged-support proof candidates) and Phase III's original NF### numerical-custody chain. This is NOT a kernel certificate, an unconditional spectral matrix computation, an equivalence theorem for other RH approaches, or RH.

### 1. Real source audit: frozen tests and literal signed arithmetic

Use the UNCHANGED original Phase IV original window `[-11/10,11/10]`; exactly the original signed source decomposition and its actual `neutralWindowCorrelation`. Source files in IV020's ancestor IV011:

- `WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportArithmeticCutoff.lean`:
  `neutralIV011OriginalMixedPrime b s t = sum'_n (Lambda(n)/sqrt(n)) [C_b(s,t)(log n)+C_b(s,t)(-log n)]`;
  `neutralIV011OriginalMixedPole` retains both genuine `paperFT` half-poles;
  `neutralIV011OriginalMixedArch` retains `(1/(2*pi))*integral paperFT*C_gamma`;
  `neutralIV011OriginalMixed_arithmeticSplit` states `W = Pole - Prime + Arch`.
- `WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalMixedHermitian.lean` targets source-exact mixed divisor attachment and Hermitian symmetry. These declarations belong to the Phase IV Lean pipeline and are NOT counted as CP002 kernel-accepted without their real strict audit artifacts.

Freeze CP001's **actual, nonzero, real-positive compactly supported Schwartz** functions
`
 b_(c,h)(x) = exp(1-h^2/(h^2-(x-c)^2)) when |x-c|<h, and 0 otherwise;
 f_- = b_(-1099/1000,1/2000), f_+ = b_(1099/1000,1/2000),
 t_r = b_(1/5,r), r=1/1000 or 1/500.
`
All three supports are disjoint, so the physical `L²` Gram matrix is `G_r=diag(m0,m0,mr)`, `m0,mr>0`. The equality of old masses is a translation invariance of the ordinary L² measure, **not** a Weil-invariance assertion.

Define real translated overlap `I_9 = integral_R f_+(x+log 9)*f_-(x) dx`. It is strictly positive: the fully rational atanh-log enclosure proves `219722/100000 < log9 < 219723/100000`. On the **entire rational open interval**
`(-21973/20000,-21971/20000)=(-1.09865,-1.09855)`,
both `f_-(x)>0` and `f_+(x+log9)>0`. Hence `I_9>0` by positivity of an integral of a continuous function on a positive-length interval. CP002's exact Fraction preflight proves the STRICT interval statements but does not purport to integrate exponentials using rational arithmetic.

### 2. New exact frozen finite-prime graph

The independent exact-Fraction preflight verifies **144 signed translated-support comparisons per radius**, testing EVERY n=2..9, both signs, and all 3x3 ordered bump pairs (including non-prime-power indices for extra conservatism). The ONLY possible actual overlaps are
`
 n=9, +log9:  source plus -> target minus;
 n=9, -log9:  source minus -> target plus.
`
Every excluded signed comparison has strictly positive certified interval clearance > 1/20. There is no new-old, old-new, new-new, or individual old-self prime overlap. Additionally `log10>11/5` makes the actual n>=10 original cutoff exact in the fixed window; n=0,1 have zero von Mangoldt coefficient. The active old/old n=9 edge is genuine and strictly nonzero, not a source hypothesis or speculative generic support graph.

**Mathematical source-level consequence** (pending formal connection of these geometric facts to the authentic `neutralWindowCorrelation`): for any complex a,b,c,
`
 f = a*f_- + b*f_+ + c*t_r,
 P_original(f,f) = 2*(log3/3)*I_9 * Re(b*conj(a)).
`
Here `Lambda(9)=log3` and `sqrt9=3`. The **prime contribution to the signed Weil form is -P**, so its polarized Hermitian 3x3 matrix in the ordered basis `(f_-,f_+,t_r)` is exactly
`
 A_prime = [ [0, -lambda9*I9, 0],
             [-lambda9*I9, 0, 0],
             [0, 0, 0] ], lambda9=log(3)/3 > 0.
`
Its ordinary eigenvalues are `-lambda9*I9, 0, +lambda9*I9`; its generalized `G_r`-relative eigenvalues are `-lambda9*I9/m0, 0, +lambda9*I9/m0`. This signed PRIME-only compression is indefinite. **No contradiction with IV018/IV020's proposed positive bounds for the FULL original pole-minus-prime-plus-Gamma source** follows: the analytic pole/Gamma blocks remain and can compensate. Also `P(f_-,t_r)=P(f_+,t_r)=P(t_r,t_r)=0` does NOT say the entire mixed Weil entries involving `t_r` vanish.

Under an invertible basis change `C`, `A_prime -> C* A_prime C` and `G -> C* G C`; raw edge placement is coordinate-dependent while inertia and the generalized eigenvalues remain unchanged. A simultaneous physical translation preserves relative difference sets and prime-graph topology, but may move a test outside the original fixed window; source-window admissibility is NOT translation-invariant.

### 3. A *quantitative* zeros-side tail estimate without assuming RH

This is CP002's new proposed analytic interface for CP-C1(B), not an already instantiated bound. Let `H_f(z)=integral f(x)*exp(z*x) dx`. For any test `f in Cc-infinity`, any nontrivial zero `rho=1/2+sigma+i gamma` (so `|sigma|<1/2`), and integer k>=2, define
`
 C_k(f) := sup_(|sigma|<=1/2) || (d/dx)^k (exp(sigma*x)*f(x)) ||_L1.
`
Integration by parts gives `|H_f(sigma+i gamma)| <= C_k(f)/|gamma|^k` for `gamma !=0`, **without RH**. The reflection `-conj(sigma+i gamma)=-sigma+i gamma` obeys the same bound.

Suppose one has independently **proved and numerically instantiated** a two-sided zero-count bound (with multiplicities)
`
 N_abs(U) := # {nontrivial rho : |Im rho|<=U} <= A*U*log(B*U)
`
for all `U>=T0`, with `A>0, B>0, B*T0>=1`. This is a *required* numerical input, not a made-up certified value. For `T>=T0`, dyadic shells with `q=2^(1-2k)` then give the explicit bound
`
 sum_(|gamma|>T) |H_f(z_rho)*conj(H_g(-conj(z_rho)))|
   <= K_k(T)*C_k(f)*C_k(g),
 K_k(T) = 2*A*T^(1-2k)*
          (log(2*B*T)/(1-q)+q*log(2)/(1-q)^2).
`
**Derivation:** the shell `2^j T < |gamma| <= 2^(j+1) T` contributes at most `A*(2^(j+1)T)*log(B*2^(j+1)T)*C_k(f)C_k(g)/(2^j T)^(2k)`; sum its geometric and j-weighted geometric factors. All zeros are counted by multiplicity; the proof never replaces `-conj(z_rho)` by `z_rho` unless RH is *separately* assumed (and RH is not assumed here).

For `k=2`, `q=1/8` and
`
 K_2(T) = 2*A*T^(-3)*
    ((8/7)*log(2*B*T)+(8/49)*log(2)).
`
Since all frozen supports lie in [-11/10,11/10], the elementary bound `exp(11/20)<2` gives
`
 C_2(f) <= 2*(||f''||_1 + ||f'||_1 + (1/4)*||f||_1).
`
This reduces tail certification to explicit derivative-norm enclosures of the three frozen bumps, a specified valid zero count, and certified low-zero enumeration.

Let `G_r=diag(m0,m0,mr)`, `v_i=C_k(f_i)/sqrt(m_i)` and let `Z_(T,r)` sum **every** zero of absolute height <=T, including multiplicity and off-line reflected partners. Assuming the classical full-matrix dictionary `A_r=Z_(infinity,r)` is established with identical constants and the complete zeros, the *matrix* bound is
`
 ||G_r^(-1/2)(A_r - Z_(T,r))G_r^(-1/2)||_op
 <= K_k(T)*sum_i C_k(f_i)^2/m_i.
`
This follows by controlling each normalized entry by `K_k(T)*v_i*v_j` and Cauchy--Schwarz. It is the missing **quantitative bridge** for CP-C1(B), but not its verified numerical instantiation. The entire expression requires validated A,B,T0, derivative norms, verified zeros and source normalization.

### 4. Structural and falsification gates

**CP002-A (verified by independent exact Fraction preflight, but not Lean):** 288 signed interval comparisons across the two radii have precisely the two directed n9 overlaps listed above; the overlap has a positive-measure witness, and `n>=10` is excluded by the original physical cutoff. Check all true `neutralWindowCorrelation` orientations before promoting this to a source theorem.

**CP002-B (genuine mathematical derived formula, pending source attachment):** the original prime-only Hermitian matrix has exactly one nonzero offdiagonal pair and nonzero inertia (one positive, one negative); source proof must account for `vonMangoldt(9)`, both `+/-log9` terms, and exactly the unmodified `Lambda/sqrt n` convention.

**CP002-C (conditional exact analytic theorem, not numerical receipt):** derive the preceding dyadic tail estimate from a specified unconditionally proved zero count bound. A specific executable certificate must enclose all `m_i` and `C_2(f_i)`, verify finite zeros including multiplicities, and compute an outward-rounded operator-error bound before declaring CP-C1(B) tested.

**Falsifiers:** a rigorously verified non-n9 active correlation on this frozen family; a rigorous proof that `I9=0` despite its exhibited positive overlap; a source-normalization mismatch against `neutralIV011OriginalMixedPrime`; or incompatible exact full-form mixed entries / independently bounded zero-side entries once the tail is actually certified. A negative prime-only eigenvalue is **not** a falsifier for positivity of the full Weil form.

### 5. Safeguards and dependencies

1. **No silent source promotion:** CP001/CP002 arithmetic geometry and Python are not Lean kernel proofs; IV009–IV020 still need actual pinned-source `.olean` and complete strict axiom audits.
2. **No shortcut through the zero side:** a zero list of critical-line zeros is not complete without certified exclusion of off-line zeros below T. An RH-dependent spectral model cannot be used as an unconditional dictionary.
3. **No unconditional error constant yet:** the value `K_2(T)` is a formula depending on separately verified A,B,T0 and bump derivative norms, none supplied numerically here.
4. **Source provenance correction:** primary arXiv:2608.24827 attributes the compact-window study to **Marcus Chuk**, not Xuefeng Zhu. CP001 was corrected in its own parent branch before CP002; no mathematical equivalence with that work is assumed.
5. **Next CP003:** source-bind the frozen 3-bump prime-pair matrix to genuine `neutralWindowCorrelation`; separately instantiate derivative bounds and explicit two-sided zero counts with a traceable, unconditional zero certification. Only then attempt any numerical comparison of the complete matrices.

**Primary cross-check references:** CP001 PR #790, IV011 PR #774, IV020 PR #788, Marcus Chuk https://arxiv.org/abs/2608.24827, Payam Danesh https://arxiv.org/abs/2611.10726, the classical Guinand--Weil explicit formula https://openmaths.org/courses/NT-EXPF/NT-EXPF-01.html. External materials give mathematical comparison context, not source-bound Lean theorem receipts.
