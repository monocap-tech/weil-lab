# Weil-Lab — IV053
## A source-exact two-low-profile Schur certificate coupled to the entire infinite-dimensional high complement

**Standing:** mathematical proof conditional on the classical NF599 Gamma physical-kernel identification and closed logarithmic form-domain framework established analytically in IV043–IV052; **exact standard-library rational preflight PASS**. No new Lean `.olean`, original source theorem, strict axiom audit, or RH certification. Date: November 21, 2026. Source window and signs are unchanged.

## 1. Exact original objects

Let `a=11/10`, `I=(-a,a)`, `L=2a=11/5`, `M=100000`, `w=L/M=11/500000`. Fourier: `hat f(ξ)=∫exp(-2πiξx) f(x) dx`. The original signed, first-slot-antilinear Hermitian form is

\[
W[f]=\gamma(0)\|f\|_2^2+D[f]-P_{\rm orig}[f]
      +|\langle h,f\rangle|^2-|\langle k,f\rangle|^2,
\quad h=\sqrt2\,1_I\cosh(x/2),\quad k=\sqrt2\,1_I\sinh(x/2),
\]

where `D[f]=(1/2)∫∫K(x−y)|f(x)−f(y)|² dxdy`, `K(u)=exp(−|u|/2)/(1−exp(−2|u|))`, and `P_orig` is **the genuine two-orientation** `Λ(n)/sqrt(n)` pairing with all active powers `n=2,3,4,5,7,8,9`, including `n=9`. The Gamma Fourier atom and the source-operator form closure remain **Lean-unaccepted** despite their mathematical derivations. The original Lean references were re-opened from the active IV023 source lineage: `neutralNF599GammaGainSeries`, `neutralIV011OriginalMixedPrime`, and `neutralWindowCorrelation_poleCrossTerms`.

Define two unit L² low profiles:

\[
e(x)=\frac{1_I(x)}{\sqrt{2a}},\qquad
p(x)=\frac{(1-(x/a)^2)1_I(x)}{\sqrt{16a/15}},\qquad
\sigma=\langle e,p\rangle=\sqrt{5/6}.
\]

Let `Π_M` be the orthogonal physical-cell-mean projection, `Q=1−Π_M`, `v=Π_M p`. The vector `e` belongs to `ran Π_M`, the cell averages of `v` are **nonconstant**, and `e,v` are linearly independent. The full investigated function class is

\[
\mathcal S_{e,p}:=\left\{f\in C_c^\infty(I;\mathbb C):
\exists\alpha,\beta\in\mathbb C\ \forall j\quad
\int_{J_j} f(x)dx=\alpha\int_{J_j}e(x)dx+\beta\int_{J_j}p(x)dx\right\}.
\]

Every `f` in this complex infinite-dimensional Schwartz subspace decomposes **orthogonally** as `f=αe+βv+q`, with `q∈ran Q`. Note that `e,v,q` need not separately be Schwartz; they belong to the closed original Gamma form domain, and the identities are applied to the smooth *sum* `f`. Original IV047/IV051 controlled the whole infinite-dimensional high complement `W[q]>(49/100)||q||²` mathematically.

## 2. Exact source mixed Gamma–prime–pole polynomial

The normalized even cross-correlation (for `0≤u≤2a`) is

\[
C_{e,p}(u)=\sigma\left(1-\frac{3u^2}{4a^2}+\frac{u^3}{4a^3}\right),\quad
C_{e,p}(-u)=C_{e,p}(u),\quad C_{e,p}(u)=0\ (u>2a).
\]

With `α_n=n+1/4`, this gives the **genuine mixed Gamma** positive-atom series

\[
D(e,p)=\sigma\sum_{n\ge0}\left[
2\int_0^{2a}e^{-2\alpha_n u}
 \left(\frac{3u^2}{4a^2}-\frac{u^3}{4a^3}\right)du
 +\frac{e^{-4a\alpha_n}}{\alpha_n}\right].
\]

The **true original prime** contribution is

\[
P_{\rm orig}(e,p)=2\sigma\sum_{n\in\{2,3,4,5,7,8,9\}}
\frac{\Lambda(n)}{\sqrt n}
\left(1-\frac{3(\log n)^2}{4a^2}+\frac{(\log n)^3}{4a^3}\right).
\]

By reflection parity, `k` pairs to neither `e` nor `p`, while both crossed Mellin residues jointly give the **positive even pole cross term**

\[
\mathrm{Pole}(e,p)=\sigma\frac{6\sinh(a/2)}a
 \left[\frac{16\cosh(a/2)}a-\frac{32\sinh(a/2)}{a^2}\right].
\]

This retains both authentic pole terms, not two independently positive poles. Exact Fraction outward brackets (350 finite Gamma atoms, positive integral tail, small exponential correction, Machin π, rational logs, sqrt and hyperbolic Taylor bounds) give:

| Source component divided by σ | Rational interval, decimal display |
| --- | --- |
| `D(e,p)/σ` | (2.519677300607, 2.519678571015) |
| `P_orig(e,p)/σ` | (1.913553071776, 1.913553071776) outward interval |
| `Pole(e,p)/σ` | (4.766645571465, 4.766645571465) outward interval |
| **Full original signed `W(e,p)`** | **(0.000532920079, 0.000536925405)** |

(The identical printed decimal endpoints are rounding of distinct outward rational interval endpoints.) These are **rigorous exact rational enclosures from the program**, not numerical eigenvalue evidence. In particular `|W(e,p)|<11/20000=0.00055`.

## 3. Passage from p to the physical-cell-average vector v

The existing original IV045 source indicator calculation yields `W[e]>201/5000`; the original IV052 parabolic source enclosure yields the sharper lower `W[p]>639/1000000`. Original IV052 also proves `||W_op p||<489/20`, while the physical mean-error satisfies

\[
q_p=p-v\in\operatorname{ran}Q,\qquad \|q_p\|<w/2.
\]

Using the genuine original high-mode bound `W[q_p]>0`,

\[
W[v]=W[p]-2\Re W(p,q_p)+W[q_p]
 >\frac{639}{10^6}-\frac{489}{20}w
 =0.0001011>\frac1{10000}.
\]

Moreover the genuine **source** mixed-cell column inequalities previously derived in IV051/052 are

\[
\|QWe\|<\frac6{\sqrt{100000}}<\frac{19}{1000},\qquad
\|QWv\|<\frac{229}{6}w<\frac{84}{100000}.
\]

Since `q_p∈Q`, the adjusted *true* low mixed form obeys

\[
|W(e,v)|\le |W(e,p)|+|W(e,q_p)|
 <\frac{11}{20000}+\frac{19}{1000}\frac w2
 <\frac{56}{100000}.
\]

Each inequality retains the original Gamma, prime and **both** signed poles. No positivity on the full low `M=100000` space is assumed.

## 4. A complete 2-low + infinite-high Schur certificate

Set `µ=1/20000`, `c=49/100`, `b_e=19/1000`, `b_v=84/100000`. For `f=αe+βv+q` with `q∈Q` and arbitrary complex `α,β`, apply the full original Hermitian polarization and minimize in the **entire** infinite-dimensional `q` using the bound `W[q]>(c)||q||²`. Since `||e||=1`, `||v||≤1`, `|<e,v>|≤1`, a sufficient lower comparison for `W[f]−µ||f||²` has the real Hermitian `2×2` coefficient budget

\[
A=\frac{201}{5000}-\mu-\frac{b_e^2}{c-\mu},\quad
D=\frac1{10000}-\mu-\frac{b_v^2}{c-\mu},\quad
B=\frac{56}{100000}+\mu+\frac{b_e b_v}{c-\mu}.
\]

Explicit **independent short rational computation** gives

\[
A>0,\quad D>0,\quad
\boxed{AD-B^2=\frac{73541319}{48995000000000}>\frac1{1000000}>0.}
\]

This is an *exact* determinant calculation with small rational numbers, not a floating-point test of a finite physical matrix. Completing the square in `q`, then using the strict `2×2` determinant, proves the new mathematical theorem:

\[
\boxed{
W_{\rm original}[f]>\frac1{20000}\|f\|_2^2
\qquad (0\ne f\in\mathcal S_{e,p}).
}
\]

**This extends IV051 and IV052 simultaneously:** the entire two-dimensional low span generated by the constant and parabolic physical cell-average vectors, **plus every** zero-cell-mean high mode, is covered. The full original physical-window space has another `M−2=99998` independent low directions; their interactions are not controlled here. The positive determinant is a certificate only for the specified two-low-profile Schur gate, not global Weil positivity or RH.

## 5. Reproducibility, source gaps, and CI gating

`IV053_two_low_profile_schur_checker.py` — executed locally with exact `Fraction` comparisons, original 350-atom mixed Gamma rational sum and certified tail, all genuine prime multiplicities, real crossed pole signs, finite source bounds and compact rational Schur determinant. Receipt `IV053_two_low_profile_schur_receipt.json` includes a SHA-256 binding for the current script and predecessor IV045/IV051/IV052 scripts. The checker passed, and the three predecessor scripts were independently rerun. **No new Lean source or GitHub Actions runs were generated**.

Required Lean chain: exact NF599 digamma-series import; IV011 original two-sign mixed prime; IV017 physical Gamma Fourier/source identification; original two crossed Mellin moments; PI007/IV043 finite Gamma Fourier atom and logarithmic form-domain closure; true interval zero-mean Poincaré; IV047/051 high-mode and IV052 jump-gradient bounds; new finite mixed Gamma atom/source cross calculation, exact Schur algebra and strict standard-only axiom/source-SHA/object audit. The mathematical source-inverse/closed-domain bridge is not already accepted Lean. Preserve original mathematical custody, existing numerical source identities and all prior strict audits.

CI: Existing IV023 PR #805 newly advanced to head `614ba879f7389fdb620c474adaee273b00eac71c` after an operational four-workflow source-scope repair for NF453/NF454/NF457/NF463; the earlier NF456/NF471 and Lake-first manifest repair remains in its lineage. However other workflows **NF455/NF458/NF459/NF460/NF464/NF465** still have unrestricted `pull_request` on this effective 611-workflow branch. **No bounded full-lineage trigger fan-out certificate, no IV018/023 post-repair kernel/axiom artifacts, and no IV053 heavy CI submission**. Queue=0 on the last read-only inspection does not clear the gate. Controlled research reopening permits mathematical work and preparation without uncontrolled CI.

**Next IV054:** (i) test an authentic odd low profile, whose mixed coupling to the even two-low block vanishes by reflection, as a candidate third independent low direction; or (ii) derive a scalable multivariate low-profile Gram certificate from exact polynomial autocorrelations with its entire high-mode correction. Neither creates an independent PI/CP equivalence, full-window positivity, or RH.
