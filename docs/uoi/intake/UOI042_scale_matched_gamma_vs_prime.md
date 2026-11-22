# Weil-Lab — UOI042: the unbounded off-ladder Rayleigh witnesses incur growing Gamma energy

**Status:** New analytic proposition derived from the explicitly specified UOI041 two-collar witness family by choosing one fixed nonzero smooth profile at all scales. It uses the classical prime number theorem and the classical digamma asymptotic. **Not Lean kernel-certified.** Not an extension-stable positivity theorem on *all* admissible functions, not an RH claim, not an identification with the native operator. No CI submitted. Formalization target belongs to master formalization ledger [#898](https://github.com/monocap-tech/weil-lab/issues/898).

## 1. Source and scope

We use the exact original literal correlation convention from pinned repository commit `614ba879f7389fdb620c474adaee273b00eac71c`:

\[
 C_f(t)=\int_\mathbb R f(x)\overline{f(x-t)}\,dx,\qquad
 P(f)=2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\operatorname{Re}C_f(\log n).
\]

The original poles are the two exponential moments `m_±(f)=∫f(x)e^{±x/2}dx`, with crossed quadratic `2Re(conj(m_-(f))m_+(f))`. With the positive-exponent paper Fourier and unitary Mathlib Fourier normalization, define the *analytic* signed Gamma term by

\[
 \Gamma(f)=\int_\mathbb R \gamma(\xi)|\widehat f(\xi)|^2\,d\xi,\quad
 \gamma(\xi)=\operatorname{Re}\psi(\tfrac14-i\pi\xi)-\log\pi.
\]

The literal original signed expression for these compact Schwartz tests is `W_lit(f)=Γ(f)−P(f)+Pole(f)`. The current fixed-collar Lean theorem `neutralNF600SmoothWeil_split` cannot be applied directly on the enlarged windows; the stated decomposition here follows from the analytic literal RHS and its Fourier transform convention, and the general support/identity formalization is still an obligation.

The pinned Lean source `ActualZetaOriginalCollarGammaLower.lean` contains the uniform analytic bound `γ(ξ)>−28/5`; the high-frequency behavior `γ(ξ)=log|ξ|+O(1/|ξ|)` is the classical digamma asymptotic (DLMF §5.11.2), applied to `z=1/4−iπξ`.

## 2. Canonically scaled UOI041 witnesses

Fix `ε=1/4000` and a **fixed**, nonzero, real `η∈C_c^∞((-1,1))`, independent of `d`. For every sufficiently large integer `d`, write

\[
 N=8^d,\quad t=\log8,\quad c_j=(j+\tfrac12)t,\quad
 \delta_j=(1000\,8^j)^{-1},\quad
 w=(10000N)^{-1}.
\]

Let `P_d` denote primes in `[Ne^(−ε),Ne^ε]`, put `κ_p=(log p)/√p`, `S_d=(Σ_{p∈P_d} κ_p²)^{1/2}`, and `a_p=κ_p/S_d`. For sufficiently large `d`, `S_d>0` by PNT. Let

\[
 \eta_d(x)=\eta\left(\frac{x-c_d}{w}\right),\quad
 \phi_d=(\partial_x^3-\tfrac14\partial_x)\eta_d,\quad
 f_d(x)=\phi_d(x)+\sum_{p\in\mathcal P_d}a_p\phi_d(x+\log p).
\]

Each term lies in the `d`th or zeroth collar in the nested `K_{d+1}` family of UOI040. For the chosen `w`, distinct translated bumps do not overlap and no pair has a prime-power sampled displacement other than `log p` across the two collars. The nearest possible distinct integer displacements differ by `≫1/N`, whereas `2w=1/(5000N)`.

For each local summand, integration by parts shows

\[
 \int (\partial_x^3-\tfrac14\partial_x)\eta_d(x)e^{\lambda x}\,dx
 =-\lambda(\lambda^2-\tfrac14)\int\eta_d(x)e^{\lambda x}\,dx=0,
 \quad \lambda=0,\pm\tfrac12.
\]

Consequently `f_d∈K_{d+1}` and the **complete original pole form is exactly zero**. Disjoint translates and `Σa_p²=1` imply

\[
 \|f_d\|_2^2=2\|\phi_d\|_2^2,\quad
 P(f_d)=2S_d\|\phi_d\|_2^2,\quad
 \frac{P(f_d)}{\|f_d\|_2^2}=S_d.
\]

The full prime quadratic term equals the off-ladder leakage for this family; the original `8`-power ladder contributes zero. Classical PNT with partial summation gives

\[
 S_d^2=\sum_{p\in\mathcal P_d}\frac{(\log p)^2}{p}
 =2\varepsilon\log N+o(\log N),\quad
 S_d=\sqrt{2\varepsilon\log N+o(\log N)}.
\]

Thus their off-ladder prime quotient really is unbounded, as UOI041 states.

## 3. Low-frequency suppression from the *fixed scaled bump*

Use Mathlib's unitary Fourier convention `\hat f(ξ)=∫f(x)e^(−2πi xξ)dx`. Then

\[
 \widehat{\phi_d}(\xi)
 =w e^{-2\pi i c_d\xi}
 \Big((2\pi i\xi)^3-\tfrac14(2\pi i\xi)\Big)\widehat\eta(w\xi),
\]

and

\[
 \widehat f_d(\xi)=\widehat\phi_d(\xi)
 \Big(1+\sum_{p\in\mathcal P_d}a_p e^{2\pi i\xi\log p}\Big).
\]

Put `k_d=#P_d`. Cauchy–Schwarz and `Σa_p²=1` yield the pointwise factor bound

\[
 \left|1+\sum_p a_p e^{2\pi i\xi\log p}\right|\le1+\sqrt{k_d}.
\]

Since `η` is fixed, there is a constant `C_η` independent of `d` such that, for every `R≥1` and `w` sufficiently small,

\[
 \int_{|\xi|\le R}|\widehat{\phi_d}(\xi)|^2d\xi
 \le C_\eta w^2R^7,
 \qquad \|\phi_d\|_2^2
 =w^{-5}\|\eta'''-\tfrac{w^2}{4}\eta'\|_2^2
 \ge c_\eta w^{-5}>0.
\]

The first follows from `|\hat η|≤‖η‖₁` and the degree-three Fourier symbol; the second is scaling and `η'''≠0`. There are at most `O(N)` integers in the fixed multiplicative interval, hence `k_d=O(N)` without PNT.

Take `R=√N`. The **relative low-frequency mass** is therefore

\[
 q_d:=\frac{\int_{|\xi|\le\sqrt N}|\widehat f_d(\xi)|^2d\xi}{\|f_d\|_2^2}
 \le C'_\eta(1+\sqrt{k_d})^2(w\sqrt N)^7
 =O_\eta(N^{-5/2}).
\]

This estimate is decisive: although the packet uses many prime-resonant translates, it has asymptotically negligible Fourier mass below frequency `√N`.

## 4. Gamma dominates the unbounded prime Rayleigh quotient on these witnesses

Classical digamma asymptotics yield an absolute constant `C_Γ` so that for all `R≥R₀`

\[
 \gamma(\xi)\ge\log R-C_\Gamma\quad (|\xi|\ge R),
 \qquad \gamma(\xi)\ge-28/5\quad(\xi\in\mathbb R).
\]

Split the Gamma integral at `R=√N` and use Plancherel:

\[
 \frac{\Gamma(f_d)}{\|f_d\|_2^2}
 \ge (\tfrac12\log N-C_\Gamma)(1-q_d)-\tfrac{28}{5}q_d
 =\tfrac12\log N-C_\Gamma-o(1).
\]

Since all pole moments vanish, combine the exact prime identity and PNT asymptotic:

\[
 \boxed{
 \frac{W_{\mathrm{lit}}(f_d)}{\|f_d\|_2^2}
 \ge \tfrac12\log N-C_\Gamma
 -\sqrt{2\varepsilon\log N+o(\log N)}-o(1)
 \xrightarrow[d\to\infty]{}+\infty.}
\]

Therefore **the very same canonically chosen UOI041 family** exhibits *unbounded positive off-ladder prime leakage* **and** an eventual growing positive value of the **complete literal signed** expression. In particular its prime-to-Gamma ratio tends to zero: 

\[
 \boxed{\frac{P(f_d)}{\Gamma(f_d)}\longrightarrow0.}
\]

Here `Γ(f_d)>0` for all sufficiently large `d`. For completeness, `Γ(f_d)=O_η((\log N)‖f_d‖²)` follows from the global upper bound `γ(ξ)≤C+log(2+|ξ|)`, Jensen's inequality for normalized Fourier mass, and `‖f_d'‖²/‖f_d‖²=‖φ_d'‖²/‖φ_d‖²=O(w^(−2))`. Thus `Γ/‖f‖²=Θ_η(log N)`.

**Quantifier qualification:** this conclusion holds for this explicitly scaled choice of the UOI041 two-collar Rayleigh witnesses. It **does not** prove any uniform Gamma-relative bound over all `f∈K_m` or over all Schwartz tests. A general counterexample may have very different spectral concentration. `sup_m ell_m=∞` and `P(f_d)/Γ(f_d)→0` are fully compatible.

## 5. What must be tested next

A falsifiable extension-stable conjecture should specify the exact `K_m`, original arithmetic form, cutoff-independent Gamma logarithmic form domain, and **all** prime powers. For example, ask whether there are `θ<1` and `C` independent of `m` such that

\[
 E_m(f)\le\theta\Gamma(f)+C\|f\|_2^2\qquad (f\in K_m\cap C_c^\infty(D_m)).
\]

This is **unproved** and might be false. To deduce a positive margin one must separately account for the on-ladder term and the sign/size of `C`; a relative estimate alone is insufficient. The first productive test is a *general Rayleigh optimization*, not another selected favorable packet: try multiscale, asymmetric, or high-phase-variation test vectors at a fixed extension radius. Any cross-projection dictionary must preserve the *full signed quadratic form* and its admissible domains, not just the off-ladder graph.

### Formalization ledger handoff

Master [#898](https://github.com/monocap-tech/weil-lab/issues/898): create/append **UOI042** under existing **F10, F25, F34**, and **F08** for the separate full-source/native bridge. Explicit targets: digamma high-frequency bound in the pinned normalization; scaled-bump Fourier concentration; exact prime/Rayleigh identities on UOI041 packets; proof of the resulting eventual positive literal signed margin. **No new F-ID, no parallel Lean backlog or CI submission.** New analytic findings remain uncompiled.

### Analytic inputs

- Weil-Lab UOI041 saved report, `/mnt/data/uoi041/UOI041_unbounded_off_ladder_prime_leakage.md` (construction and prime interaction computation).
- Pinned repository original literal correlation, pole and Gamma definitions at commit `614ba879f7389fdb620c474adaee273b00eac71c`.
- NIST Digital Library of Mathematical Functions, §5.11.2, asymptotic `ψ(z)~log z−1/(2z)+…`: https://dlmf.nist.gov/5.11
- Classical Prime Number Theorem and partial summation for the fixed relative-width prime interval.
