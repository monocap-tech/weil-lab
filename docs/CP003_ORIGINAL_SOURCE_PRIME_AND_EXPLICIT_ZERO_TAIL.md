# Weil-Lab — CP003
## Original prime source-attachment boundary, strict normalized n=9 budget, and an unconditional zero-count input

**Canonical separate CP### head:** CP003 stacked on CP002 PR #796 -> CP001 PR #790. Do not edit or renumber the independent Phase IV IV### Lean/source-extension chain (observed IV021 PR #794) or Phase III NF### numerical matrix-custody chain (observed NF752 PR #795). PI001 PR #793 is also a separate potential-interface lane.

**Proof-status rule:** CP003 adds a reproducible **independent exact-rational preflight and mathematical proof specification**. It does **not** contain a new kernel-accepted Lean theorem, independently verified zero enumeration, complete signed-Weil numerical 3x3 matrix, a proved zeros-side normalization dictionary, global Weil positivity, or RH. Its conditional inequalities are not promoted to certified source theorems.

## 1. Exact literal IV011 source audit and orientation

On the genuine original IV011 source, the definitions and an existing **source theorem candidate** read:

```lean
neutralIV011MixedCorrelation_eq_schwartzIntegral
  -- for original-window supported complex Schwartz s,t:
  neutralWindowCorrelation b (s.toLp 2 volume) (t.toLp 2 volume) τ
    = ∫ x : ℝ, t x * conj (s (x - τ))

neutralIV011OriginalMixedPrime b s t
  = ∑' n : ℕ, ((ArithmeticFunction.vonMangoldt n / Real.sqrt n : ℝ) : ℂ) *
      (neutralWindowCorrelation b (s.toLp 2 volume) (t.toLp 2 volume) (Real.log n)
       + neutralWindowCorrelation b (s.toLp 2 volume) (t.toLp 2 volume) (-Real.log n))

neutralIV011OriginalMixed_arithmeticSplit
  -- literal unchanged W = Pole - Prime + Arch
```

**Observed source Git blob SHA** (IV021 inherited original IV011 file): `14d8f01ce34f764900eccc68399d7323b4f4a25c` at `WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportArithmeticCutoff.lean`. The CP003 executable optionally checks this exact blob and all requisite literal substrings when given `--iv011-file PATH`; the CP branch itself is not misrepresented as containing unmerged IV### source modules.

The orientation matters. `C(s,t;+log9)=∫ t(x)conj(s(x-log9))dx`, so in the ordered frozen family `(f_-,f_+,t_r)`, the **plus-signed** nonzero entry has `s=f_-`, `t=f_+`. The **minus-signed** nonzero entry has `s=f_+`, `t=f_-`. Complex conjugation is preserved; these entries happen to be real because the frozen bumps are real-positive. The two directed overlaps together contribute `2(log3/3)I9 Re(b conj(a))` to the diagonal PRIME term of `a f_-+b f_++c t_r`. They enter the **complete signed Weil form with a MINUS sign**, not as deleted terms.

CP003 source theorem targets, NOT kernel claims:
1. `CP003OriginalFrozenCorrelation_eq_schwartzIntegral`: instantiate the true IV011 mixed-source lemma for each frozen bump.
2. `CP003FrozenActivePrime_pairs`: prove the complete 2..9 both-sign pairwise zero/offdiagonal table from exact logarithm support inequalities, including inactive von Mangoldt coefficients.
3. `CP003OriginalFrozenPrimeMatrix`: use the original IV011 n>=10 cutoff and `vonMangoldt(9)=log3` to identify the full mixed PRIME matrix (zero except the two real offdiagonal entries).
4. `CP003OriginalPrimeBurden`: attach its generalized eigenvalues using the physical mass `G_r`, and prove the strictly positive translated overlap `I9`. The underlying IV008/IV009 complex Hermitian/sesquilinear candidates must first pass their original compiler/audit chain.

**Do not confuse** the prime-only indefinite 3x3 compression with the full `Pole - Prime + Arch` compression. Also `C(t_r,f_±;±log n)=0` does not imply `W(t_r,f_±)=0`: the original two poles and Gamma remain mixed.

## 2. New strict intrinsic prime burden: less than 23/240

Freeze `h=1/2000`, old centers `±1099/1000`, `t_r` centered at `1/5`, radii `r∈{1/1000,1/500}`, and the CP001 bump profile
`
 phi(u)= exp(1-1/(1-u^2)) for |u|<1; phi(u)=0 outside;
 f_±(x)=phi((x∓1099/1000)/h);
 t_r(x)=phi((x-1/5)/r).
`
The true `n=9` positive integral is `I9=∫ f_+(x+log9) f_-(x) dx>0`.

**New controlled overlap bound.** The exact rational atanh-series certificate encloses `219722/100000<log9<219723/100000`, while the old center distance is `D=1099/500`. The intersecting translated support interval has length `log9-(D-2h)<23/100000`. For any point in this overlap, the two normalized bump coordinates differ by `(D-log9)/h>3/2`; therefore at least one has absolute value greater than `3/4`. On `|u|≥3/4`, `phi(u)≤exp(-9/7)<1/2` (since `exp(9/7)>1+9/7>2`), while the other `phi≤1`. Consequently

```
 0 < I9 < 23/200000.
```

**New explicit true mass lower.** Let `a2=∫_{-1}^1 phi(u)^2 du`. For `u∈[0,7/8]`, `phi(u)^2=exp(-2u²/(1-u²))`. Partition into 64 equal rectangles with right endpoints `u_j=j*(7/8)/64`. Since the integrand decreases, and `exp(-x)≥(1-x/32)^32` for `0≤x≤98/15<32`, an **exact Fraction sum** proves

```
 a2 >= 2*((7/8)/64)*sum_(j=1..64)
     (1-[2u_j²/(1-u_j²)]/32)^32
    > 24/25.
 m0=h*a2 > 3/6250.
```

Thus, **if the prime matrix is attached to the source and the earlier positive witness is attached**, the true mass-normalized original prime burden of this frozen span satisfies

```
 pi(V_r)= (log3/3)*I9/m0
       < (2/5)*(23/96)
       = 23/240 < 1/10.
```

Unlike the support embedding capacity `kappa(V_r)=eta*(1/1000+r)` (with `eta<2`), this exact prime burden is **independent of the new radius r** for the frozen old bump pair; the prime-matrix null central row/column is source-conditional and must be proved first.

**Improved conditional full-form margins.** The real original signed Gamma+two-pole bound in IV019 gives `q_A(f)≥(11/10)M(f)-75||f||_1²-Re P_A(f,f)` for tests in its physical window, conditional on original source proof acceptance. Therefore, using `kappa<2*(1/1000+r)` and `pi<23/240`, the exact rational arithmetic yields

```
 lambda_A(V_(1/1000)) > 7/10,
 lambda_A(V_(1/500))  > 11/20.
```

These are **not** uniform claims on the entire three-cell geometric class in IV021; they apply only to the precisely frozen three-bump finite spans. No computed actual Rayleigh minimum is asserted. The stronger bounds arise from actual bump shape / overlap rather than a coordinate-dependent original whole-collar measure budget.

## 3. A non-RH zero-count input with explicit usable constants

Use the published explicit zero-count theorem of **Elchin Hasanalizade, Quanli Shen and Peng-Jie Wong**, *Counting zeros of the Riemann zeta function*, Journal of Number Theory 235 (2022), arXiv:2107.06506. For `U>=e`, the positive-ordinate multiplicity count obeys an explicit Riemann–von Mangoldt error estimate (here conservatively allowing an additional `7/8` term relative to the arXiv abstract):

```
 N_+(U) <= U/(2*pi)*log(U/(2*pi*e))
       + 7/8 + 0.1038*log U + 0.2573*log log U + 9.3675.
```

For `U>=100`, use `pi>3`, `log log U<=log U`, `7/8+9.3675<11`, and `0.1038+0.2573<2`. Therefore
`
 N_+(U) < (U/6+2) log U + 11 <= (U/2) log U.
`
The last inequality is elementary for `U>=100`: `(U/3-2)log U>11`. The classical conjugate-zero symmetry and absence of real nontrivial zeros give the two-sided count
`
 N_abs(U) := #{rho nontrivial : |Im rho|<=U, with multiplicities}
            <= U log U                 (U>=100).
`
This is a **published unconditional theorem input and explicit analytical corollary**, not a Lean formalization or a certified enumeration of individual zeros.

## 4. New fully rational k=2 matrix-tail budget at a fixed height

The original CP002 dyadic tail inequality uses the centered transforms and counts ALL possible off-critical zeros; **RH is never assumed**.

For `f=b_(c,h)` supported inside the true window and `|sigma|<=1/2`, set
`
 C2(f)=sup_(|sigma|<=1/2)|| (exp(sigma*x) f(x))'' ||_L1.
`
The elementary bump calculus gives
`
 phi'(u)=(-2u/(1-u²)^2)*phi(u),
 phi''(u)=(2(3u^4-1)/(1-u²)^4)*phi(u)
`
inside `|u|<1`; its smooth extension is flat at the endpoints. Hence `||phi||_1<=2`, `||phi'||_1=2`, and because `phi''` changes sign exactly once on `(0,1)` and `max|phi'|<=8/e<4`, `||phi''||_1<16`. Together with `exp(11/20)<2` and `m_h=h*a2>=4h/9`, this yields the **simple explicit rational bounds**
`
 C2(b_(c,h)) < 32/h + 4 + h,
 m_h >= 4*h/9.
`

Instantiate the unconditional counting constants `A=1,B=1,T0=100`, `T=2^20=1048576`. CP002's exact dyadic result gives
`
 K2(T)= (2/T^3) * [(8/7)log(2T)+(8/49)log 2].
`
Since `log2<1`, a **fully rational** upper bound at `T=2^20` is
`
 K2(T) < (2/T^3)*[(8/7)*21+8/49].
`
Write `h0=1/2000`, `Mr(h)=32/h+4+h`. The normalized three-test matrix tail is bounded above by the exact rational number
`
 E_r=(2/T^3)*[(8/7)*21+8/49]*(9/4)*
     [2*Mr(h0)^2/h0+Mr(r)^2/r].
`
**Independent exact Fraction preflight passes `E_(1/1000)<1/500` and `E_(1/500)<1/500`.**

**Precise promotion boundary:** if and only if (i) the complete original arithmetic/spectral mixed dictionary holds in the specified conventions, (ii) all low zeros in `|gamma|<=T` are independently exhaustively enclosed, with multiplicities and off-line zeros not silently omitted, and (iii) the bump derivative and counting inequalities are formally verified or accepted under a stated proof standard, then
`
 ||G_r^(-1/2)(A_r-Z_(T,r))G_r^(-1/2)||_op < 1/500.
`
Until then, **this is a proven-mathematics-based conditional tail calculation, not a verified finite spectral comparison**. A point sampler of known zeros on the critical line cannot close (ii).

## 5. Independent PI001 test-domain negative control

Potential-interface PI001 PR #793 notes that a naive norm pullback of `h(t,t)` to Masullo's stated norm-one trace-test domain fails because `h(t,t)(0)=||t||²>0` for nonzero t, while a disjoint-support old/new *mixed* correlation has `h(s,t)(0)=0`. CP003's finite 3x3 **diagonals therefore cannot be imported naively into that alternative trace model**; the trace-domain, Haar normalization, and correction required to transport diagonal pairings are missing. PI001 and CP003 are kept separate; the observation is a non-equivalence test, not a new PI proof.

## 6. Falsifiers and CP004 gate

- **Falsifier CP003-1:** an exact source theorem shows a different orientation, sign, or multiplicity for the `n=9` original correlation.
- **Falsifier CP003-2:** any rigorous error enclosure disproves the stated shape overlap/mass lower bounds or violates `pi(V_r)<23/240`; a mismatch in CP002's normalized prime-only source matrix halts its use in the full-form lower inequality.
- **Falsifier CP003-3:** once a complete low-zero enumeration and a proved full-form dictionary exist, the arithmetic and spectral Hermitian matrices have rigorously disjoint entry interval enclosures, or normalized mismatch exceeds the certified tail bound. That falsifies the proposed correspondence/normalization, **not** a claim of RH.
- **CP004:** obtain actual Phase IV source-kernel audit receipts; build the `neutralWindowCorrelation` three-bump interface directly in Lean on a properly imported original Phase IV branch; separately certify a finite zero enumeration through `2^20` (or a lower T with correspondingly larger proven tail); only then compare the full original signed matrices. The CP### and IV### PRs must not be merged or relabeled merely to make import paths appear to exist.

**References:** CP001 PR #790; CP002 PR #796; Phase IV IV011 PR #774, IV019 #787, IV021 #794; PI001 PR #793; Hasanalizade–Shen–Wong https://arxiv.org/abs/2107.06506 ; CNRS explicit-zero-count summary https://archimede.pages.math.cnrs.fr/tme-emt-wiki/Art06.html .
