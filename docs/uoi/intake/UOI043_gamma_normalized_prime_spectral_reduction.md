# Weil-Lab — UOI043: finite-support prime/Gamma spectral reduction and compact capacity

**Status:** New analytic reduction on the precisely defined UOI040 nested three-moment collar family, with a positive compact-operator eigenproblem at each finite stage. The construction uses the signed Gamma lower estimate inherited from UOI040, the literal original full von Mangoldt quadratic form, and the standard digamma high-frequency asymptotic. **This does not prove any stage is positive for the full signed Weil form.** No new Lean kernel certification or CI run. Every formalization obligation belongs to master ledger [#898](https://github.com/monocap-tech/weil-lab/issues/898), not a new queue.

## 1. Original source-typed conventions and nested family

Use the immutable original research source `614ba879f7389fdb620c474adaee273b00eac71c` for the signed literal expression, with the first input conjugated and the original **two-sided** correlations. For `f in C_c^infty(R; C)` define

\[
\widehat f(\xi)=\int f(x)e^{-2\pi i\xi x}\,dx,\qquad
\gamma(\xi)=\operatorname{Re}\psi(1/4-i\pi\xi)-\log\pi,
\]
\[
\Gamma(f)=\int_{\mathbb R}\gamma(\xi)|\widehat f(\xi)|^2\,d\xi,
\quad C_f(s)=\int_{\mathbb R}f(x)\overline{f(x-s)}\,dx,
\]
\[
P(f)=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}[C_f(\log n)+C_f(-\log n)]
   =2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\operatorname{Re}C_f(\log n).
\]
The literal original signed expression is `W_lit(f)=Gamma(f)-P(f)+Pole(f)` with `Pole` the two crossed exponential moments. **The general arbitrary-support Lean identification with the native form is still open** (F01/F08); the expressions here are analytic, not a claim of that bridge.

Let `t=log 8`, `c_j=(j+1/2)t`, `delta_j=8^{-j}/1000`, `I_j=(c_j-delta_j,c_j+delta_j)`, `D_m=union_{0<=j<m} I_j`, and `D_infty=union_{j>=0} I_j`. Define `S_m` to consist of compactly supported smooth complex functions supported in `D_m` with three **separate** local moments zero on every collar `I_j`:

\[
\int_{I_j}f_j(x)\,dx=\int_{I_j}f_j(x)e^{x/2}\,dx
=\int_{I_j}f_j(x)e^{-x/2}\,dx=0.
\]
Then `S_m` embeds by zero extension into `S_(m+1)`, every such f has `Pole(f)=0`, and its literal form is `W_lit(f)=Gamma(f)-P(f)`. Finite support makes every prime sum finite. Do not replace `S_m` by all `C_c^infty(D_m)` or by all Schwartz functions.

From UOI040's separately moment-neutral low-band bound and the pinned Gamma bracket inequalities,

\[
\boxed{\Gamma(f)\ge G\|f\|_2^2,\quad
G=\frac{2195428693}{1996093750}>1.09986,\qquad f\in S_m.}
\]
This crucial **positive Gamma energy** is only guaranteed on the restricted nested family.

## 2. Exact worst-case ratio — no arbitrary positive shift is needed

Define the genuine, **full-prime** worst-case relative quotient

\[
\boxed{\rho_m=\sup_{0\ne f\in S_m}\frac{P(f)}{\Gamma(f)}.}
\]
The denominator is positive by `Gamma(f)>=G||f||²`. Note that this definition includes *all* prime powers, **not** merely off-ladder leakage. This avoids making the powers-of-eight partition into a claimed invariant of the whole Weil form.

Since `D_m` is bounded, `P` equals a **finite** Hermitian form. Represent it on full-line `L²(R)` by the self-adjoint operator `T_m = 1_(D_m) [sum_n kappa_n(U_(log n)+U_(-log n))] 1_(D_m)`, with only terms `log n <= diam(D_m)`, where `kappa_n=Lambda(n)/sqrt(n)` and `U_s f(x)=f(x-s)` (up to the harmless sesquilinear first-slot convention). This acts as a compression to `L²(D_m)` but the extended full-line definition also makes its later Fourier cutoff composition well-typed. If `L_m=diam(D_m)`, then

\[
\|T_m\|\le 2\sum_{2\le n\le e^{L_m}}\frac{\Lambda(n)}{\sqrt n}<\infty.
\]
Hence each `rho_m` is finite, though the bound is not uniform in m.

The literal signed form satisfies the **exact variational equivalence**

\[
\boxed{\forall f\in S_m:\ W_{\rm lit}(f)\ge0\quad\Longleftrightarrow\quad\rho_m\le1.}
\]
A uniform **Gamma-relative** margin `W_lit(f)>=epsilon Gamma(f)` for all f in all stages is equivalent to `sup_m rho_m<=1-epsilon`; then `W_lit(f)>=epsilon G||f||²` on their algebraic union. This is not positivity on all supported Schwartz functions.

The source quantities are unchanged under zero extension, so

\[
\boxed{0<\rho_2\le\rho_3\le\cdots,\qquad
\rho_\infty:=\sup_m\rho_m\in(0,+\infty].}
\]
To see `rho_2>0`, put a sufficiently narrow smooth three-moment-neutral bump in `I_1` and its translate by `log8` in `I_0`; then the exact full prime term is the positive `n=8` interaction (all other prime-power shifts miss the supports). This also proves positive `rho_m` for every larger m.

**Falsification conditions:** `rho_m>1` at a rigorously source-checked finite stage would yield a smooth supported vector with *negative literal signed quadratic*. Conversely, finite verification of `rho_m<1` for many stages cannot settle `sup_m rho_m<=1`.

## 3. A compactness result for the entire unbounded nested support union

Surprisingly, although the collar centers tend to infinity, their **combined Lebesgue measure is finite**:

\[
\boxed{|D_\infty|=2\sum_{j\ge0}\delta_j
=\frac{2}{875}.}
\]
Let `H_m` be the Hilbert completion of `S_m` in the positive Hermitian inner product induced by Gamma; let `H_infty` be the completion of the algebraic union. The ambient weighted Fourier norm is closed because the original `gamma(xi)>-28/5` and `gamma(xi) -> +infty` as `|xi|->infty` (the latter from standard digamma asymptotics). More explicitly put

\[
q_6(f)=\Gamma(f)+6\|f\|_2^2
=\int(\gamma(\xi)+6)|\widehat f(\xi)|^2\,d\xi.
\]
Since `gamma+6>2/5` everywhere and `Gamma>=G||f||²` on the domain,

\[
\Gamma(f)\le q_6(f)\le(1+6/G)\Gamma(f)\quad (f\in S_m)
\]
with constants independent of m. Thus Gamma and `q_6` have equivalent norms on `H_infty`.

For `R>0`, let `Pi_R` project onto Fourier frequencies `|xi|<=R`, and set

\[
a_R:=\inf_{|\xi|>R}(\gamma(\xi)+6)\longrightarrow+\infty.
\]
For Gamma-unit vectors in any `H_m` or `H_infty`, Plancherel gives the **uniform** high-frequency tail bound

\[
\boxed{\|(1-\Pi_R)f\|_2^2
\le \frac{1+6/G}{a_R}\Gamma(f).}
\]
On the other hand, the low-band restricted Fourier transform from `L²(D_infty)` into `L²([-R,R])` is **Hilbert–Schmidt**, because its integral kernel has modulus one:

\[
\boxed{\|\mathbf1_{[-R,R]}\,\mathcal F\,\mathbf1_{D_\infty}\|_{\rm HS}^2
=2R|D_\infty|=\frac{4R}{875}.}
\]
Therefore `Pi_R J_infty` is compact, where `J_infty:H_infty -> L²(D_infty)` is the inclusion. The high-frequency estimate says `Pi_R J_infty -> J_infty` in operator norm. **Consequently `J_infty` is compact**, even though `D_infty` is unbounded. The embedding compactness also holds at every finite stage.

This is a genuine **support-capacity theorem**: finite physical measure together with a Fourier energy weight increasing to infinity forces compactness. It is a general analytic observation; it is not original full Weil positivity.

## 4. Each finite stage has an attained principal generalized eigenvalue

Because the full-line extension `T_m` is bounded self-adjoint on physical L² and `J_m:H_m -> L²(R)` is compact, define on the Gamma Hilbert space

\[
\boxed{A_m:=J_m^*T_m J_m.}
\]
This is compact self-adjoint. Its Gamma quadratic is the actual full original prime term,

\[
\langle f,A_m f\rangle_{\Gamma}=P(f)\quad(f\in S_m).
\]
Thus

\[
\boxed{\rho_m=\lambda_{\max}(A_m)>0,}
\]
with the principal eigenvalue **attained in the Gamma-form completion** `H_m`. Its eigenvector is not claimed automatically to be a smooth compact test; density of `S_m` in `H_m` ensures approximation of its Rayleigh quotient by genuine supported smooth tests. A value `rho_m>1` would consequently yield an actual smooth negative witness.

One can obtain a **finite-band enclosure**. With

\[
\varepsilon_R:=\sqrt{\frac{1+6/G}{a_R}},\qquad
A_{m,R}:=J_m^*\Pi_R T_m\Pi_R J_m,
\]
we have `||J_m||<=G^(−1/2)`, `||J_m−Pi_R J_m||<=epsilon_R`, and therefore

\[
\boxed{\|A_m-A_{m,R}\|
\le \frac{2\|T_m\|}{\sqrt G}\,\varepsilon_R.}
\]
The same error bounds the difference of their largest spectral values. This is a controlled **finite-stage approximation route**, not a declaration that the band-limited operator is finite rank (it is compact/Hilbert–Schmidt; discretization and certified errors remain separate tasks). Because `||T_m||` is not uniformly bounded, the error estimate does **not** magically pass to `m=infty`.

## 5. Exact extension and cross-projection preservation laws

For a proposed target Hilbert test system `(H'_m,Gamma'_m,P'_m)` and maps `Phi_m` from original tests, assume:

1. `Phi_m` preserves the Gamma Hermitian form (thus is an isometry for the positive Gamma norm);
2. `Phi_m` preserves the **entire** prime Hermitian form including the actual `±log n` phases and coefficients;
3. `Phi_(m+1) ∘ inclusion = inclusion' ∘ Phi_m`.

Then the ratio on the **image subspace** is exactly `rho_m`; the target's unrestricted supremum is **at least** `rho_m`. Equality for the full target stage requires that the map reach the comparison domain (e.g. surjectively), not merely embed it. A mismatch of a rigorously computed stage ratio falsifies a claimed isometric-surjective `Gamma/Prime` dictionary. Merely preserving the *combined* `W` is insufficient to preserve its decomposition-specific ratio.

One may instead use the off-ladder quotient `sup E(f)/(Gamma(f)-P_8(f))`; the denominator is positive on these `S_m` because the UOI040 original ladder bound is below the Gamma lower bound. It yields an equivalent test for the **sign** of the full form, but it is **coordinate-dependent** because the `8^k` ladder is selected by the chosen collars. The full-prime `rho_m` is preferable as the primary compatibility invariant (relative to the original Gamma/prime decomposition).

## 6. What this accomplishes — and what remains open

**Established analytically:** a legitimate positive Gamma form on every nested stage, monotone exact **worst-case** full-prime ratios, an attained compact generalized eigenproblem for each finite stage, a compact support-capacity embedding on an *unbounded* nested union of total measure `2/875`, and a concrete finite-band tail error budget. This replaces UOI042's favorable-example comparison by a variational statement covering **all admissible tests at any chosen stage**.

**Not established:** `rho_m<=1` for even one nontrivial enlarged stage by a certified full-prime estimate; `sup_m rho_m<1`; uniform control of the genuinely unbounded arithmetic operator on the Gamma-form completion; existence/convergence of original global exponential pole integrals for arbitrary elements of `H_infty`; the universal literal-to-native form identity F08; full original all-Schwartz positivity; RH.

A subtle domain warning: every *finite-support* smooth test in the union has two zero pole moments, but an arbitrary Gamma-completion element supported on the unbounded `D_infty` need not have convergent integrals against `e^{±x/2}`. The zero pole form is therefore asserted on the algebraic test union, **not** automatically on every completed vector.

**Next decisive research target:** establish a **uniform-in-m upper bound** on `lambda_max(A_m)`, preferably strictly below one, using arithmetic cancellation/localization and Gamma form energy; or find a valid finite-stage witness forcing it above one. Stage-by-stage approximations alone cannot resolve that uniform statement.

## 7. Formalization intake / evidence provenance

Register UOI043 in master [#898](https://github.com/monocap-tech/weil-lab/issues/898) under **F10, F25, F26, F34** (plus **F01/F08** if attached to the native source). The new obligations are: exact positive Gamma domain/completion on the restricted local-moment kernel; total-volume computation; HS finite-band compactness; full-prime finite-stage self-adjoint compression; monotone ratio and principal eigenvalue; finite-band operator error theorem; and exact transport conditions. Mark **M/O**, no `.olean`, no strict named-axiom audit, and no CI acceptance. This document is an analytic source note, not an accepted original-source theorem.

**Inputs checked:** UOI040/UOI041/UOI042 saved analytical reports; pinned original definitions at `614ba879f7389fdb620c474adaee273b00eac71c` (`ActualZetaOriginalCollarPrimeBound`, `ActualZetaPhaseIVOriginalNarrowSignedGamma`, `NeutralWeilSourceMixedForm`, `Def_Zeta23_ExplicitFormula`); standard DLMF digamma asymptotics §5.11.2. No assumptions about RH are made.
