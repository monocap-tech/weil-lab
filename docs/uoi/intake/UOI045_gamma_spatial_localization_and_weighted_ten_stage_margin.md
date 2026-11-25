# Weil-Lab — UOI045: real-place logarithmic energy localizes across nested collars

**Custody/status:** 2026-11-21. Analytic theorem/research note, with exact rational arithmetic rechecking the pre-existing UOI044 ten-stage prime-envelope matrix. **Not Lean certified; no new CI work.** All formalization tasks belong to the existing GitHub master ledger `monocap-tech/weil-lab` issue #898. Original source snapshot for the literal Weil normalization: `614ba879f7389fdb620c474adaee273b00eac71c`; in particular `ActualZetaOriginalCollarGammaLower.lean`, `ActualZetaPhaseIVOriginalNarrowSignedGamma.lean`, and `Def_Zeta23_ExplicitFormula.lean`. Native/source correspondence for arbitrary supports remains a separate open F01/F08 obligation.

## A. Exact scope

Use the unchanged UOI040–UOI044 nested, disjoint support collars

\[
 t=\log8,\quad c_j=(j+\tfrac12)t,\quad \delta_j=\frac1{1000\,8^j},\quad I_j=(c_j-\delta_j,c_j+\delta_j),\quad D_m=\bigcup_{0\le j<m} I_j.
\]

Let `S_m` consist of complex compactly supported smooth functions `f=Σ_{j<m} f_j`, with `supp f_j ⊂ I_j`, and *on each individual collar* the three linear moments against `1,e^{x/2},e^{-x/2}` vanish. These restrictions make the original two crossed pole moments zero, while the mean-zero condition gives the previously established uniform original signed Gamma estimate

\[
 \Gamma(f)\ge G\|f\|_2^2,\qquad G=\frac{2195428693}{1996093750}>\frac{1099}{1000}.
\]

For Schwartz `f` define `hat f(ξ)=∫ f(x)e^{−2πiξx}dx` and the **literal original** signed Gamma weight

\[
 \gamma(\xi)=\operatorname{Re}\psi(\tfrac14-i\pi\xi)-\log\pi,\qquad
 \Gamma(f)=\int\gamma(\xi)|\widehat f(\xi)|^2d\xi.
\]

The full original prime term is `P(f)=Σ_{n≥2} Λ(n)n^(−1/2)[C_f(log n)+C_f(−log n)]` with `C_f(s)=∫f(x)overline{f(x−s)}dx`. Only finitely many prime powers contribute for any finite `m`. The analytic literal signed expression is `W_lit(f)=Γ(f)−P(f)` on `S_m`; equating it to a separate native operator on this enlarged support has **not** been established in Lean.

## B. New original-Gamma comparison from the digamma series

For every `a>0` and real `y`, the classical real-part digamma difference identity is

\[
 \operatorname{Re}\psi(a+iy)-\psi(a)
 =\sum_{n=0}^{\infty}\frac{y^2}{(n+a)((n+a)^2+y^2)}.
\]

The summand is a nonnegative decreasing function of `n+a`. Comparing the sum with its integral from zero to infinity gives

\[
 \sum_{n\ge0}\frac{y^2}{(n+a)((n+a)^2+y^2)}
 \ge \int_0^\infty\frac{y^2}{(s+a)((s+a)^2+y^2)}ds
 =\frac12\log\left(1+\frac{y^2}{a^2}\right).
\]

At `a=1/4`, `y=−πξ`, this proves the **global pointwise lower comparison**

\[
 \boxed{\gamma(\xi)\ge\gamma(0)+\frac12\log(1+16\pi^2\xi^2).}\tag{B1}
\]

Pinned source theorem `neutralNF599GammaZero_lower` proves `γ(0)>−28/5`. Put

\[
 L(f)=\int\frac12\log(1+16\pi^2\xi^2)|\widehat f(\xi)|^2d\xi.
\]

Then Plancherel and (B1) imply `Γ(f)>L(f)−(28/5)||f||²` for nonzero Schwartz `f`.

## C. Exact physical nonlocal energy and collar-localization error

The elementary Laplace identity

\[
 \int_0^\infty\frac{e^{-s/2}}s[1-\cos(2\pi\xi s)]ds
 =\frac12\log(1+16\pi^2\xi^2)
\]

provides the exact physical representation

\[
 \boxed{L(f)=\frac12\int_0^\infty\frac{e^{-s/2}}s\|f(\cdot-s)-f\|_2^2ds.}\tag{C1}
\]

This is nonnegative and holds by Tonelli/Plancherel for Schwartz functions. When `f=Σf_j` has disjoint collar supports, expanding the quadratic gives the **exact IMS-type decomposition**

\[
 L(f)=\sum_j L(f_j)-\sum_{j<k}\operatorname{Re}\int_{I_j}\!\int_{I_k}
  f_j(x)\overline{f_k(y)}\frac{e^{-(y-x)/2}}{y-x}\,dy\,dx.\tag{C2}
\]

The kernel is well-defined because `I_j` lies strictly left of `I_k`. The identity contains **one** cross pairing for each `j<k`; no additional factor of two is missing.

For one collar, the shift `s≥2δ_j` has zero self-overlap, so

\[
 \boxed{L(f_j)\ge E_1(\delta_j)\|f_j\|_2^2},\qquad
 E_1(z)=\int_z^\infty e^{-u}du/u.\tag{C3}
\]

For `d_{jk}=c_k−c_j−δ_j−δ_k>0`, the offdiagonal cross term in (C2) is bounded by

\[
 h_{jk}\|f_j\|_2\|f_k\|_2,\qquad
 h_{jk}=\frac{2\sqrt{\delta_j\delta_k}\,e^{-d_{jk}/2}}{d_{jk}}.\tag{C4}
\]

This uses `||f_j||_1≤sqrt(2δ_j)||f_j||_2` and the monotonic kernel bound on separated collars. In particular, it applies **without** the three moment restrictions.

Set `r=8^(−1/2)`. Elementary exact rational estimates verified in the companion checker give

* `log 8>2`, `exp(999/1000)>5/2`, and `r<3/8`;
* `d_jk>2(k−j)−2/1000>k−j` and `e^(−d_jk/2)<2/5`;
* consequently `h_jk<(4/5) sqrt(δ_j δ_k)/(k−j)`;
* for **every** row `j` in the full *infinite* collar array, the geometric summation of all `k≠j` yields

\[
 \boxed{\sum_{k\ne j}h_{jk}<\frac45\cdot\frac65\cdot\delta_0
 =\frac{24}{25000}<\frac1{1000}.}\tag{C5}
\]

Thus the complete cross term in (C2) is at most half of the row-sum bound times `||f||²`, in particular **strictly less than `||f||²/1000`**, independent of `m`.

Finally, `E_1(δ)≥log(1/δ)−1` follows by `e^(−u)≥1−u` for `δ≤u≤1`; `log1000>69/10` and `log8>2` are verified by exact-rational Taylor/exponential bounds. Combining (B1)–(C5) with the source-proved `γ(0)>−28/5` yields the main **all-stage spatial Gamma estimate**:

\[
 \boxed{\forall m\ge1,\ \forall f\in S_m,\quad
 \Gamma(f)\ge\sum_{j<m}\Bigl(\frac{299}{1000}+2j\Bigr)\|f_j\|_2^2.}\tag{C6}
\]

For nonzero smooth inputs, the estimates above can be taken strictly. **C6 grows linearly with collar index and is uniform under genuine support inclusion.** It is not positivity of the full signed Weil expression, because the complete prime term still must be bounded against this Gamma energy.

## D. Ten-stage improvement with the unchanged UOI044 exact full-prime matrix

Convexly combine (C6) with the inherited original `Γ(f)≥(1099/1000)||f||²` using coefficients `3/10` and `7/10` respectively. For all `m`:

\[
 \boxed{\Gamma(f)\ge \sum_{j<m}g_j\|f_j\|_2^2,\qquad
 g_j=\frac{859}{1000}+\frac{3j}{5}.}\tag{D1}
\]

This keeps a useful positive margin at `j=0` while charging increasingly remote collars for their Fourier uncertainty.

**Reuse the exact pre-existing UOI044 ten-stage matrix**, not a new or truncated prime enumeration: the integer matrix `B_micro` has `B_micro[j][k]/10^6` as an upper bound on the full original prime edge norm, retaining all non-ladder prime powers. The previous UOI044 finite arithmetic checks established `P(f)≤aᵀB_10 a`, where `a_j=||f_j||_2`.

The new *generalized weighted Schur super-solution* is the positive integer vector

\[
 v=(181,116,69,42,47,33,31,27,24,20)^\top.
\]

The checker verifies **ten integer inequalities**

\[
 (B_{10}v)_j < \frac{11}{25}g_jv_j \quad(0\le j<10),
\]

and the largest exact normalized ratio is `18660353/42449000 < 11/25`. By the weighted Schur inequality, this is an exact rational certificate that

\[
 \boxed{P(f)<\frac{11}{25}\sum_{j<10}g_j\|f_j\|_2^2.}\tag{D2}
\]

Thus for every nonzero `f ∈ S_10` (and therefore every earlier nested stage),

\[
 \boxed{W_{\rm lit}(f)>
 \frac{14}{25}\sum_{j<10}\left(\frac{859}{1000}+\frac{3j}{5}\right)\|f_j\|_2^2
 \ge\frac{6013}{12500}\|f\|_2^2
 >\frac{12}{25}\|f\|_2^2.}\tag{D3}
\]

The new plain `L²` margin `>12/25=0.48` materially strengthens the earlier UOI044 `>3/20=0.15`. More importantly, (D3) is **spatially weighted**: mass in later collars has a larger coercivity charge. This is an analytic-plus-exact-finite-arithmetic result, **not a Lean kernel pass**.

## E. A rigorous limitation: even Gamma-weighted scalar edge envelopes fail as m→∞

The new diagonal energy does *not* rescue every scalar-envelope approach. Write `b_jk` for UOI044's genuine all-prime block norm **upper envelope**, and set

\[
 \widetilde B_{jk}=\frac{b_{jk}}{\sqrt{g_jg_k}},\quad
 g_j=\frac{859}{1000}+\frac{3j}{5}.
\]

For the first collar `j=0` and a remote collar `k`, the prime interval defining `b_0k` contains the ordinary primes in

\[
 [8^k e^{-\delta_0},8^k e^{\delta_0}],\qquad\delta_0=\frac1{1000}.
\]

By the standard Prime Number Theorem with partial summation,

\[
 b_{0k}^2\ \ge\sum_{p\in[8^ke^{-\delta_0},8^ke^{\delta_0}]}\frac{(\log p)^2}{p}
 =2\delta_0\,k\log8+o(k).
\]

Since `g_k=(3/5)k+O(1)`, this implies

\[
 \liminf_{k\to\infty}\widetilde B_{0k}^{\,2}
 \ge \frac{2\delta_0\log8}{(859/1000)(3/5)} >0.
\]

Therefore the first row of `\widetilde B_m` has Euclidean norm growing at least as a positive constant times `sqrt(m)`; the top eigenvalue of the **nonnegative symmetric scalar envelope** also diverges:

\[
 \boxed{\lambda_{\max}(\widetilde B_m)\longrightarrow\infty.}\tag{E1}
\]

**Crucial interpretation:** E1 falsifies the strategy of proving a uniform all-stage result by applying the UOI044 collarwise `ℓ²` prime-block matrix and *only* the diagonal linear Gamma lower bound. It does **not** show that the actual generalized prime/Gamma supremum `rho_m` diverges. The scalar block estimate discards Fourier-profile correlations across many remote interactions; those correlations are precisely what an eventual all-stage estimate must exploit.

## F. Falsifiable next target and cross-projection relevance

The next task is to compare the full prime operator with the **genuine nonlocal Gamma energy**, not only the diagonal `g_j`. Specifically, construct an operator-valued block bound retaining frequency profiles or a Bessel/Carleson-type estimate for the outgoing infinitely many arithmetic shifts from early collars. It must control all `±log n`, all complex phases, and mixed terms. A scalar bound based only on collar norms is provably inadequate by (E1).

**Preservation caution:** the existence of an intrinsic lower bound for the actual Gamma form is source meaningful; the individual collar masses and `g_j` are artifacts of this nested support coordinate model. An independent cross-projection dictionary must preserve the original complete Gamma and prime Hermitian forms and the support inclusions before these weighted inequalities can be transferred. The exact generalized spectral ratios `rho_m` of UOI043 are the more intrinsic diagnostic under such a form-preserving map.

**Formalization targets:** file under existing ledger **#898**: F10 (digamma sum-vs-integral and exact logarithmic physical kernel); F25 (disjoint-collar localization and infinite Schur cross-error bound); F26 (weighted ten-stage Schur certificate and limitation of scalar envelopes); F34 (form-preserving compatibility). Retain F01/F08 for literal/native source identification. Never create a competing formalization task list.

**Reproduction:** `check_uoi045.py` (stdlib `Fraction`, loads UOI044's unchanged integer matrix); `UOI045_exact_rational_receipt.json` (ten integer row inequalities, exponential comparisons, SHA256 link to source matrix). The script verifies the finite inequalities, not the complex-analysis digamma identity, functional-analysis localization, or the PNT asymptotic. No repo writes and no CI runs were made by this report.
