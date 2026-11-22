# Weil-Lab — UOI048: exact digamma cross-kernel, exponential Gamma core–tail decoupling, and quantitative Schur criterion

**Status:** Analytic result / proof proposal, not Lean compiled or kernel/axiom audited, no GitHub write or CI submission, no NF numerical frontier promotion. The broad-support literal-to-native/original source identity F01/F08 is not discharged. The standing UOI047 far-tail prime estimate is an inherited analytic claim, not independently recertified here.

## Source fidelity

Use the exact original signed digamma Fourier multiplier specified in the local UOI045 source review of pinned Weil-Lab revision `614ba879f7389fdb620c474adaee273b00eac71c`:

`gamma(xi) = Re psi(1/4 - i pi xi) - log(pi)` and `Gamma(f,g) = int gamma(xi) conj(hat f(xi)) hat g(xi) dxi`, for `hat f(xi)=int f(x) exp(-2 pi i xi x) dx`. This normalization is consistent with `ActualZetaPhaseIVOriginalNarrowSignedGamma.lean` and `ActualZetaOriginalCollarLiteralArch.lean`. DLMF 5.9.16: https://dlmf.nist.gov/5.9.E16 (`psi(z)+EulerGamma=int_0^inf (exp(-u)-exp(-zu))/(1-exp(-u)) du`, Re(z)>0).

For the source restrictions, keep `t=log(8)`, `delta=1/1000`, `c_j=(j+1/2)t`, `delta_j=delta*8^(-j)`, and `I_j=(c_j-delta_j,c_j+delta_j)`. Let `S_infty` be the algebraic finite union of complex `C_c^infty` collar components `f_j` with **three separate local moments** `int f_j`, `int exp(x/2) f_j`, `int exp(-x/2) f_j` all zero. Its original crossed pole form vanishes on all of `S_infty`. The original full two-sided von Mangoldt prime form is unchanged.

## Theorem A: exact off-diagonal original Gamma kernel

For any disjoint Schwartz components `h` and `g` with support respectively in an earlier and later collar, the classical digamma integral identity gives

`gamma(xi) = gamma(0) + int_0^inf [2 exp(-s/2)/(1-exp(-2s))]*(1-cos(2 pi xi s)) ds`.

With the Fourier convention above, and supports strictly separated (no distributional diagonal), this yields the **exact mixed form**

`Gamma(h,g) = -int_{x in supp(h)} int_{y in supp(g)} conj(h(x)) g(y) exp(-(y-x)/2)/(1-exp(-2(y-x))) dy dx`.

For `s=y-x>0`, expand `exp(-s/2)/(1-exp(-2s)) = sum_{r>=0} exp(-(2r+1/2)s)` (absolutely uniformly on a pair of separated compact collars). Hence

`Gamma(f_j,f_k) = -sum_{r>=0} conj(M^+_{j,r}) M^-_{k,r}` for `j<k`,

`M^+_{j,r}=int f_j(x) exp((2r+1/2)x) dx`, `M^-_{k,r}=int f_k(y) exp(-(2r+1/2)y) dy`.

Both `M^+_{j,0}` and `M^-_{k,0}` vanish by the *original local* pole-neutral moment constraints. Thus, **exactly**,

`Gamma(f_j,f_k) = -sum_{r>=1} conj(M^+_{j,r}) M^-_{k,r}`.

No positivity assumption enters this cross-kernel identity, and no change to the prime form is made. The cancellation removes the `exp(-s/2)` leading factor, leaving `exp(-5s/2)/(1-exp(-2s))`.

## Theorem B: uniform exponential core–tail estimate

Let `M>=1`, `h=sum_{j<M}h_j`, `v=sum_{k>=M}v_k`, with finitely many nonzero collar terms and both `h,v` in the above three-moment space. For `j<k`, `d=k-j`, put `D_jk = c_k-c_j-delta_j-delta_k > d*log8-2delta`. Then

`|Gamma(h_j,v_k)| <= 2 sqrt(delta_j delta_k) [exp(-5 D_jk/2)/(1-exp(-2 D_jk))] ||h_j||_2 ||v_k||_2`.

Since `exp(5delta) <= 1/(1-5delta)=200/199` and `exp(4delta) <= 1/(1-4delta)=250/249`, the exact rational check

`2 (200/199)/(1-(250/249)/64)=3187200/1560757 <21/10`

proves the uniform block estimate

`|Gamma(h_j,v_k)| <= q_jk ||h_j||_2 ||v_k||_2`,

`q_jk = (21/10)*delta*8^(-j)*8^(-3(k-j))`.

The cross-block row and column sums are bounded by

`max_{0<=j<M} sum_{k>=M} q_jk <= (21/10) delta 8^(-M) (8/511) < delta 8^(-M)/30`,

`max_{k>=M} sum_{0<=j<M} q_jk <= (21/10) delta 8^(-M)/63 = delta 8^(-M)/30`.

Schur's matrix bound, combined with disjoint physical support of collars, gives for **all finite-stage** `h,v`

**`|Gamma(h,v)| <= [delta 8^(-M)/30] ||h||_2 ||v||_2 = [8^(-M)/30000] ||h||_2||v||_2`.**

This is uniform in the number of remote collars, and decays geometrically with the separating index.

The previously established (on-paper) UOI045 lower bound `Gamma(f)>=G_3||f||_2^2`, `G_3>1099/1000`, gives the normalized mixed estimate

`|Gamma(h,v)| <= kappa_M sqrt(Gamma(h)Gamma(v))` with

**`kappa_M < 8^(-M)/32970`**.

These inequalities are about the genuine original **Gamma** form; there is no corresponding bound here for the **prime** mixed form.

## Theorem C: the Gamma Hilbert completion really splits into head plus tail

Because Gamma is a strictly positive Hermitian form on the restricted algebraic union, take its completion `H_infty`. Let `H_head(M)` and `H_tail(M)` denote the respective Gamma closures of `S_M` and `T_M`.

On all algebraic head/tail pairs,

`(1-kappa_M)(Gamma(h)+Gamma(v)) <= Gamma(h+v) <= (1+kappa_M)(Gamma(h)+Gamma(v))`,

by `2 sqrt(ab)<=a+b`. Since `kappa_M<1`, the direct-sum map from the two completed factors has a bounded inverse. It follows rigorously that

**`H_infty = H_head(M) (+)_top H_tail(M)`**,

with unique decomposition and continuous projections. This supplies a topology check that UOI047's variational reduction previously left implicit; head and tail need not be **orthogonal** in the Gamma inner product.

Moreover, the infinite off-diagonal Gamma kernel, after subtracting its exactly canceled `r=0` moment block, is Hilbert–Schmidt on the physical `L^2` direct sum of all `I_j`. Indeed its squared HS norm is at most

`2*(21/10)^2*delta^2 * (64/63)/(8^6-1) < 4*10^(-11)`.

Thus the **cross-collar Gamma correction is compact** on the restricted physical support space and on the Gamma completion via its bounded injection into L2. This does not make the entire Gamma form bounded or compact; diagonal Gamma grows logarithmically.

## Theorem D: a falsifiable quantitative prime-coupling criterion

Keep the unchanged complete original prime Hermitian mixed form `P(h,v)`. Set

`beta_M = sup_{0!=h in H_head(M), 0!=v in H_tail(M)} |P(h,v)|/sqrt(Gamma(h)Gamma(v))`.

This is finite under UOI046's previously derived full-prime Gamma-boundedness, but **not yet shown to be small**. Write `W=Gamma-P` on the restricted completion.

Assume separately:

* a core margin `W(h,h)>=alpha_M Gamma(h)` for all heads, with `alpha_M>0`;
* a tail margin `W(v,v)>=tau_M Gamma(v)` for all tails, with `tau_M>0` (UOI047 gives `tau_M=1-eps_M` only for sufficiently remote M);
* the actual prime mixed bound `beta_M` defined above.

Then for `X=sqrt(Gamma(h))`, `Y=sqrt(Gamma(v))`,

`W(h+v,h+v)>=alpha_M X^2+tau_M Y^2-2(beta_M+kappa_M)XY`.

Therefore the **sufficient sharp 2x2 Schur condition**

**`(beta_M+kappa_M)^2 < alpha_M tau_M`**

implies strict positivity on every nonzero test in `S_infty`. The non-strict `<=` version implies nonnegativity.

More precisely, the unique tail minimizer `v_h` solving `W(h+v_h,w)=0` for all tail `w` satisfies

`||v_h||_Gamma <=(beta_M+kappa_M)/tau_M * ||h||_Gamma`, and

**`W(h,h)-(beta_M+kappa_M)^2/tau_M *Gamma(h) <= W_eff,M(h) <= W(h,h)`.**

The existing first-ten-collar (finite-envelope analytic) certificate UOI045 gives `W(h,h) > (14/25)Gamma(h)` for nonzero `h in S_10` (since the full prime bound `P(h)<(11/25)sum_j g_j||h_j||² <=(11/25)Gamma(h)`). It does **not** follow that `tau_10>0`; UOI047 only proves a tail margin at some unspecified, potentially larger M. Likewise, positivity of the head at all such larger M is unproved. No false global conclusion is drawn.

## What is intrinsic vs filtration dependent?

* The original Gamma and full-prime Hermitian forms are fixed analytic functionals; a unitary preserving them preserves their mixed pairings and Gamma-relative operator norms.
* `S_M`, `T_M`, the physical `I_j` coordinates, the pole-neutral local moments, `kappa_M`, `beta_M` and the head–tail Schur complement are **filtration dependent**. They transfer only under a map preserving the relevant decomposition and form topology, not a map that preserves only the total signed Weil diagonal.
* The compactness of the *cross-collar Gamma correction* is invariant under an actual unitary intertwiner preserving the decomposition, but is not an unconditional assertion about arbitrary supports or a different splitting.

## Exact next obligation and status

1. Source/Lean F10: formalize the DLMF digamma integral or establish it from the imported digamma series, with the **exact** original `-2pi` Fourier normalization; derive the off-diagonal physical kernel on disjoint collars.
2. F25: establish the separate local moment cancellation, `r>=1` factorization, rational exponential bounds and all-index geometric Schur estimates.
3. F26: formalize the stable topological Gamma splitting and quantitative head–tail Schur criterion in the actual Gamma completion.
4. F04/F26: bound **the complete original prime mixed coupling** `beta_M`, preserving every original prime power, and establish a compatible positive core margin at an M where the tail is known coercive.
5. F01/F08: independently prove broad-support literal-to-native original form identification.

**No Lean pass, CI or original RH claim is asserted.** Accompanying exact rational checker validates the displayed elementary coefficient inequalities and HS-bound algebra, not the complex digamma Fourier identity or the infinite-dimensional theorems.