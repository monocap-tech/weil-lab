# Weil-Lab — UOI049: prime core–tail coupling (read-only analytic investigation)

**Status:** Conditional mathematical lemmas and an exact rational arithmetic checker. No GitHub writes, no CI, no Lean acceptance, no source-to-native bridge, and no positivity or RH conclusion.

## Preserved input

UOI048 gives the Gamma head–tail bound `kappa_M < 8^(-M)/32970` after three local moment conditions, with `alpha_10=14/25` and no certified positive `tau_10` or sufficiently small `beta_10`. The prime mixed operator retains every genuine von Mangoldt prime power and its complex Hermitian phase.

## 1. Finite cutoff: compact after Gamma normalization

Assume the positive Gamma energy on the moment-neutral family controls a logarithmically growing Fourier weight, which is consistent with the classical digamma asymptotics. On each fixed compact collar, the embedding of the Gamma-energy completion into L^2 is compact: bounded Gamma energy bounds Fourier tails through the growing weight, while fixed compact physical support supplies local L^2 compactness. For a fixed pair of collars only finitely many shifts `log(n)` meet their difference set. Each weighted shift is bounded on L^2, so the finite-block prime form factors through compact embeddings and defines a compact mixed operator between the Gamma-energy spaces. Every finite head-to-finite tail cutoff is therefore compact **subject to the Gamma-domain equivalence and exact form identification**.

This does not imply compactness on the **whole infinite tail**; one needs a uniform norm tail estimate.

## 2. An arithmetic resonance that moment conditions do not remove

Conditional on the usual 8-adic realization — centers `a+j log 8`, width `delta*8^(-j)`, `delta=1/1000` — fix `M>=1` and put `N=8^M=2^(3M)`. Select a smooth precursor supported in a subinterval of diameter `ell=delta/N` inside the first collar. Apply the physical differential operator

`D_x (D_x^2 - 1/4)`

to obtain a nonzero compactly supported `h_M`, normalized in L^2. Integration by parts gives exactly

`int h_M(x) dx = int h_M(x) exp(x/2) dx = int h_M(x) exp(-x/2) dx = 0`.

Define `t_M(x)=h_M(x-log N)`, which fits inside collar M. Translation preserves these three moment cancellations. The difference set of the packets lies in `(log N-ell, log N+ell)`. Since

`ell=delta/N < 1/(N+1) <= log(1+1/N)`,

no integer `n != N` has `log n` in that difference interval. Thus **only the actual prime power `n=N` contributes**. In the standard Hermitian polarization of the two-sided prime term,

`|P(h_M,t_M)| = (Lambda(N)/sqrt(N))*||h_M||_2^2 = (log 2)*8^(-M/2)*||h_M||_2^2`,

up to any global bilinear normalization already built into the project's definition of `P`. No cancellation of this translated product follows from the three exponential moments.

## 3. Candidate asymptotic obstruction to overly fast beta_M bounds

The original digamma Fourier symbol grows like a positive constant times `log(2+|xi|)`. Normalized bumps of diameter `ell=10^(-3)8^(-M)` formed with the differential annihilator above consequently have `Gamma(h_M) <= C (1+M) ||h_M||_2^2`, with `C` independent of `M`; translation invariance gives the same for `t_M`. This gives the **conditional analytic lower bound**

`beta_M >= c * 8^(-M/2)/(1+M)`

for an `M`-independent `c>0`, if the 8-adic geometry and Gamma Fourier representation are as assumed. It rules out a uniform `O(8^(-M))` estimate for `beta_M`. It does **not** rule out `beta_M -> 0`; in fact this witness decays to zero.

The corresponding high-frequency test on a *fixed* pair of collars has a nonzero prime L^2 pairing but growing Gamma energy, so its normalized pairing tends to zero. Thus any persistent essential-norm obstruction would have to use a moving-collar or collective arithmetic network, not merely high frequency in one fixed block.

## 4. Compactness criterion and next verifications

Let `B_M` be the Gamma-normalized operator from the finite head into the full tail, and let `Q_{>=K}` denote truncation to collars `>=K`. With uniformly bounded tail truncations converging strongly to zero, compactness of `B_M` is equivalent to

`lim_(K->infty) || Q_{>=K} B_M || = 0`.

Finite-block compactness proves only the truncated half. The main open task is a uniform, phase-sensitive bound for prime-power shift sums, with a certified `tau_M` and `alpha_M` at a common cutoff. The conditional lower bound above prevents over-optimistic Gamma-rate targets. A valid terminal certificate still needs `(beta_M+kappa_M)^2 < alpha_M*tau_M`.

## 5. Audit state

- Checked by exact rational arithmetic: isolation of the `n=8^M` shift from the neighboring integer logarithms for the packet diameter `delta/8^M`.
- Analytical argument requiring written proof in the project's exact conventions: compact local Gamma embedding; physical differential-annihilator test; digamma upper estimate on the scaled test; normalized prime lower bound.
- Not established: full prime operator boundedness/compactness, complete infinite-tail margin at M=10, source-to-native identification, unrestricted Weil positivity, RH.
