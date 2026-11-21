# Weil-Lab — CF021: lawful sharp cutoff and infinite dyadic boundary decomposition

**Date:** 2026-11-21. **Status:** new analytic derivation, local floating-point controls only; no Lean build, PR, Actions, accepted numerical gate, or RH claim. Original HD/A frontier **692/968** unchanged.

## Exact source normalization and dependencies

On the original physical domain let

\[
 w(\xi)=\log(e+|\xi|),\qquad \|f\|_{\log}^2=\int_\mathbb R w(\xi)|\widehat f(\xi)|^2d\xi,
 \quad \widehat f(\xi)=\int e^{-2\pi i x\xi}f(x)dx.
\]

Let `g(t)=Re digamma(1/4+it/2)-log(pi)`. The project theorem `neutralActualZetaArchimedean_log_bound` gives a global constant `CΓ≥0` satisfying `|g(2πξ)-w(ξ)|≤CΓ`. From the digamma translation-energy identity, `g(t)-g(0)=2∫₀∞K(s)(1−cos(ts))ds`, where `K(s)=exp(−s/2)/(1−exp(−2s))`, one gets

\[
 E_\Gamma(f)=\int_0^\infty K(s)\|f-\tau_s f\|_2^2 ds
 =\int_\mathbb R[g(2\pi\xi)-g(0)]|\widehat f(\xi)|^2 d\xi.
\]

Set `DΓ=CΓ+|g(0)|`; then

\[
 |E_\Gamma(f)-\|f\|_{\log}^2|\le D_\Gamma\|f\|_2^2.
\]

Source dependencies, read on the IV023 research branch:

- `WeilDefect/Arithmetic/LogarithmicForm.lean`, `logarithmicFourierWeight`.
- `WeilDefect/Arithmetic/ActualZetaNativeLogBounds.lean`, `neutralActualZetaArchimedean_log_bound`.
- `WeilDefect/Morphology/NeutralLogHilbertCarrier.lean`, `neutralLogHilbertCarrier_norm_sq`.
- `WeilDefect/Arithmetic/ActualZetaNativeFormOperator.lean`, native full-form continuity and Gårding theorem.
- `WeilDefect/Morphology/NeutralLogPoleSourceAttachment.lean`, native cross-pole mixed formula.
- CF019–CF020 exact reference-kernel/Carleman controls.

## CF021-A: bounded sharp half-line truncation

For arbitrary complex `f` with finite logarithmic energy, split at any real `b`:

\[
 f_-={\bf1}_{(-\infty,b)}f,\qquad f_+={\bf1}_{(b,\infty)}f.
\]

With `q(s)=exp(−5s/2)/(1−exp(−2s))`, the exact kernel satisfies `K(s)=q(s)+exp(−s/2)` and `0<q(s)≤1/(2s)`.

Define the mixed interface integral

\[
 I_b(f_-,f_+)=\iint_{x<b<y}K(y-x)\overline{f_-(x)}f_+(y)dxdy.
\]

For the `q` term the Hilbert–Carleman operator of kernel `1/(r+s)` has operator norm `π`, hence

\[
 |I_{b,q}|\le\frac\pi2\|f_-\|_2\|f_+\|_2.
\]

For the exponential term, `exp(−(y−x)/2)=exp((x−b)/2)exp(−(y−b)/2)` and both half-line exponentials have `L²` norm `1`, so `|I_{b,exp}|≤\|f_-\|₂\|f_+\|₂`.

The Gamma difference-quotient identity for the disjoint split reads

\[
 E_\Gamma(f_-)+E_\Gamma(f_+)=E_\Gamma(f)+2\operatorname{Re}I_b(f_-,f_+).
\]

For an arbitrary form-domain `f`, prove this first for a positive truncated kernel `K_T(s)=K(s)1_{1/T≤s≤T}`; the interface bound is uniform in `T`. Monotone convergence of the individual positive energies then simultaneously proves membership of both pieces in the Gamma domain and the full identity. Thus

\[
 \boxed{E_\Gamma(f_-)+E_\Gamma(f_+)\le E_\Gamma(f)+(\pi/2+1)\|f\|_2^2.}
\]

Using the bounded symbol difference and `w≥1`, obtain the **uniform original-carrier multiplier estimate**

\[
 \boxed{\|f_-\|_{\log}^2+\|f_+\|_{\log}^2\le C_{\rm cut}\|f\|_{\log}^2,\quad C_{\rm cut}=2+2D_\Gamma+\pi/2.}
\]

There is no assumption of a boundary trace, derivative, analytic continuation, support gap, or positivity of the full Weil form. Multiplication by the interval indicator `1_(a,b)` follows by composition/difference of two bounded half-line cutoffs.

## CF021-B: strong continuity of shrinking boundary cutoffs

For every fixed `f` in the complete logarithmic form domain,

\[
 \boxed{\lim_{\ell\downarrow0}\|{\bf1}_{(b-\ell,b)}f\|_{\log}=0.}
\]

Proof: half-line multiplier boundedness is uniform in `b`, so the shrinking-interval operators are uniformly bounded. For a smooth compactly supported `φ`, write the Gamma difference quotient of `1_I φ` as a sum of a smooth-difference term `O_φ(|I|)` and an indicator-difference term `O_φ(|I|\log(1/|I|))`; the latter uses the exact identity `EΓ(1_I)=2∫K(s)min(s,|I|)ds`. Both vanish. Density of `C_c^∞(R)` in the weighted Fourier L² domain and uniform boundedness conclude the claim. No claim of a universal rate for arbitrary `f` is made.

## CF021-C: stable countable dyadic partition

Let `0<a<log2`, fix `b`, let `v` be supported in the collar `I=(b−a,b)`, and set

\[
 I_j=(b-a2^{-j},\,b-a2^{-(j+1)}),\qquad v_j={\bf1}_{I_j}v,\quad j=0,1,\ldots.
\]

Each `v_j` lies in the logarithmic form domain by CF021-A. Strong shrinking-cutoff continuity gives `v^{(N)}=∑_{j=0}^N v_j→v` in `||·||log`.

Let `R=π+2+√2` be the uniform dyadic row sum already derived in CF020 for the `q` kernel: adjacent shells use Carleman constant `π/2`, and shells with index separation `m≥2` have off-diagonal norm coefficient `≤2^{-m/2}`. For the remaining exponential kernel `exp(−|x-y|/2)≤1`, the sum of cross-interactions is at most `a∑_j||v_j||₂²`. Therefore

\[
 \sum_{j=0}^{N}E_\Gamma(v_j)
 \le E_\Gamma(v^{(N)})+(R+a)\|v^{(N)}\|_2^2.
\]

On the other hand, the interval cutoff bound gives `||v^{(N)}||log≤2√Ccut ||v||log`. Comparing `EΓ` with the logarithmic norm yields

\[
 \boxed{\sum_{j\ge0}\|v_j\|_{\log}^2
 \le (4C_{\rm cut}+R+a+2D_\Gamma)\|v\|_{\log}^2.}
\]

This is a **Bessel-type stable countable shell decomposition** for the canonical form norm; individual sharp shells are now lawful. It does *not* assert a converse lower frame bound independent of collar length.

If the CF020 finite-shell coercivity bracket is at least `1/2` for the chosen `a`, then continuity of the original bounded Weil form and the strong convergence `v^(N)→v` upgrade its finite-shell inequality to

\[
 \boxed{Q_W(v)\ge\frac12\sum_{j\ge0}\|v_j\|_{\log}^2.}
\]

This is a full **infinite-shell** coercivity theorem on a sufficiently narrow prime-silent collar, not an assertion of global positivity.

## CF021-D: quantitative consequence for hypothetical neutral modes

Let `k≠0` belong to the full signed Weil kernel at a nonnegative window `[-c,c]`. For `ell` small set `v=1_(c−ell,c)k` and `u=k−v`. CF021-A ensures both are actual domain vectors; full mixed nullity gives `Q_W(v)=−B_W(u,v)`.

From uniform local microcoercivity, `Q_W(v)≥(1/2)||v||log²`. For ordered disjoint supports CF020 gives `|B_ref(u,v)|≤(π/2)||u||₂||v||₂`. The exact arithmetic discrepancy mixed form is a fixed-window bounded L² operator with norm at most `S_c+2(e^c−1)`, where `S_c=∑_{log n<2c}Λ(n)/√n`. Thus

\[
 |B_W(u,v)|\le L_c\|u\|_2\|v\|_2,
 \quad L_c=\frac\pi2+2S_c+4(e^c−1).
\]

Using interval Fourier capacity `||v||₂≤α(ell)||v||log`, with `α(ell)=√[2/log(e+1/(4ell))]`, and `||u||log≤√Ccut||k||log`, obtain

\[
 \boxed{\|v\|_{\log}\le 2L_c\sqrt{C_{\rm cut}}\alpha(\ell)\|k\|_{\log}.}
\]

Applying interval capacity again gives the stronger *conditional-on-nullity* endpoint mass estimate

\[
 \boxed{\int_{c-\ell}^{c}|k(x)|^2dx
 \le \frac{16L_c^2C_{\rm cut}}{[\log(e+1/(4\ell))]^2}\|k\|_{\log}^2.}
\]

The reflected statement holds at `−c`. This is an `O_c(log(1/ell)^{-2})` mass upper bound, improving the earlier `O_c(log(1/ell)^{-1})` boundary Hardy estimate **for a hypothetical full neutral mode**. It does not exclude such a mode.

## CF021-E: important sharpness/negative control

Support saturation alone gives no lower decay rate. For example, on `(-c,c)` the smooth bump

\[
 k_0(x)=\begin{cases}\exp[-1/(c^2-x^2)],&|x|<c,\\0,&|x|\ge c\end{cases}
\]

is nonzero in every endpoint collar and has finite logarithmic energy, but for `0<ell<c` its right collar mass is bounded by `ell*exp[-1/(c ell)]` (since `c²−x²≤2c ell`). Hence no lower bound by a fixed inverse power of `log(1/ell)` follows from support saturation and form-domain membership alone. To exclude a genuine null mode one must exploit its exact Gamma–prime–pole *equation* to deduce an independent lower observability estimate.

## Verification and controlled CI plan

Local test: `python /mnt/data/cf021_sharp_cutoff_dyadic_validator.py` confirms the complex split identity, exact Gamma kernel decomposition, Carleman upper bound for an adjacent rectangle pair, and the dyadic row-energy estimate. These floating-point checks are not rigorous interval enclosures.

**Formal proof obligations, in order:**
1. An exact complex Gagliardo/translation-energy dictionary for the genuine Gamma multiplier, including Fourier factors and global L² domain.
2. A complex Hilbert–Carleman theorem (or a preexisting Mathlib import), and the rank-one exponential bound.
3. Uniform half-line cutoff continuity on the complete canonical logarithmic carrier, without assuming classical boundary traces.
4. Strong continuity of shrinking interval projections, then countable dyadic Bessel bound and original-form mixed continuity.
5. Native first-contact null-mode attachment and explicit endpoint mass estimate, retaining cross-pole normalization.

**Actions:** no current GitHub submission or heavy CI. The NF753/NF756 branch lineage was previously found diverged; verify that the eventual chosen new branch inherits the repaired workflow scoping, manifest-sensitive preflight order, and bounded PR fan-out before introducing a targeted Lean PR. Preserve NF750–NF753 accepted records and strict axiom audits. Frontier **692/968** unchanged.
