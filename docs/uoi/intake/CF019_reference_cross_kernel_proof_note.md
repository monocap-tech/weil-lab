# Weil-Lab CF019 — Gamma-reference cross kernel and three-zone screening

Date: 2026-11-21. **Analytic/local-only**. No Lean, PR, or Actions run; original HD/A certification frontier remains 692/968. No claim of RH or contact exclusion.

## Source identities and normalization

Source branch read-only: `research/iv023-original-four-cell-schwartz-partition-and-prime-transfer` in `monocap-tech/weil-lab`. This note treats the original native complex Hermitian quadratic, not the selected-background surrogate.

- `WeilDefect/Arithmetic/ActualZetaNativeWeilForm.lean` has original native form = Gamma symbol minus genuine prime symbol plus Hermitian cross-pole (blob `961b6742782fa3f808ac9b70cfadfc0790c8fc32`).
- `WeilDefect/Morphology/NeutralLogPoleSourceAttachment.lean` has exactly `conj(M_-(u))*M_+(v)+conj(M_+(u))*M_-(v)` (blob `331ad94a02336a124eb6c17e3ee94480694a8c5c`).
- `WeilDefect/Arithmetic/LogarithmicForm.lean` has `w(xi)=log(exp(1)+abs(xi))` (blob `ae932d4f3f7e4d6d06dbd778a5708927172238dc`).
- `WeilDefect/Arithmetic/ActualZetaNativeFormOperator.lean` gives a bounded Hermitian form operator in the original log energy norm and its mixed bound (blob `93beff3a82207f44fd5a431987c39f1aeb7e0092`).

Angular Fourier convention: `fhat(t)=∫e^{-itx} f(x) dx`; for Mathlib `xi`, `t=2*pi*xi`. Let `K(s)=exp(-s/2)/(1-exp(-2s))`, `s>0`. The digamma identity gives

`g(t)=g(0)+2∫_0^∞K(s)[1-cos(ts)]ds`, with `g(t)=Re digamma(1/4+it/2)-log pi`.

Write `B_ref=B_Gamma + B_G` where the positive reference contribution has convolution kernel `G(s)=exp(-abs(s)/2)`. The identity `B_W = B_ref - 2D` is the exact CF015–CF017 continuous-prime/pole cancellation, not a heuristic replacement of discrete primes. The underlying `D` retains original complex polarization and von Mangoldt factors.

## CF019-A — exact cross kernel for separated supports

Let `u,v` be compactly supported log-form vectors with disjoint physical supports a positive distance `d>0` apart. Since `inner(u,v)=0`, polarizing the Gamma translation-energy formula and adding the positive reference gives the exact identity

`B_ref(u,v) = - ∫∫ conj(u(x)) v(y) q(abs(x-y)) dx dy`, where

`q(s)=K(s)-exp(-s/2)=exp(-5*s/2)/(1-exp(-2*s)) = ∑_{j>=1}exp(-(2*j+1/2)*s)`.

The identity holds for arbitrary complex phases. It is not a positivity claim about `B_ref` in general; nonnegative real disjoint packets have a negative cross term, while phase changes can reverse its real part.

For ordered supports `supp(u)⊂(-∞,b]`, `supp(v)⊂[b+d,∞)`, set `lambda_j=2*j+1/2` for `j>=1`,

`U_j=∫_{x<=b} conj(u(x)) exp(-lambda_j*(b-x)) dx`,

`V_j=∫_{y>=b+d} v(y) exp(-lambda_j*(y-b-d)) dy`.

Then `B_ref(u,v)=-∑_{j>=1}exp(-lambda_j*d)*U_j*V_j`. This is an exact **phase-sensitive Laplace-moment factorization**. At positive gap the geometric series is absolutely dominated, and truncation after `j=J` obeys

`|remainder| <= exp(-(2J+5/2)*d)/(1-exp(-2*d)) * ||u||_1 ||v||_1`.

In particular,

`|B_ref(u,v)| <= q(d) ||u||_1 ||v||_1`.

The ratio is in fact exact: `q(s)/K(s)=exp(-2s)`, so at an actual prime-power separation `s=log(n)` the residual/reference Gamma ratio is `n^(-2)` (e.g. 1/4 at n=2, 1/9 at n=3). This is a pointwise comparison of off-diagonal kernel densities, **not** a direct comparison of discrete prime translation operators. The first Gamma exterior exponent `1/2` cancels exactly in the reference, leaving `5/2,9/2,...`. This cancellation applies **to the new reference representation**, not to the original Gamma operator by itself or the complete exterior null residual.

## CF019-B — adjacent-contact control

The kernel remains singular at touching supports: `q(s)=1/(2s)-3/4+O(s)` as `s->0`. Therefore no positive-gap truncation bound is uniform as `d->0`.

Let `u_ell = ell^(-1/2) 1_[-ell,0]`, `v_ell = ell^(-1/2) 1_[0,ell]`. Both belong to the logarithmic form domain. The disjoint-support formula holds by nonnegative integral convergence at the shared endpoint, and

`B_ref(u_ell,v_ell)=-1/ell ∫_0^ell∫_0^ell q(r+s) dr ds -> -log(2)`.

Proof: substitute `r=ell*r'`, `s=ell*s'` and use `ell*q(ell(r'+s'))->1/[2(r'+s')]`; dominated convergence is allowed since `q(s)<=1/(2s)` for sufficiently small s. The integral `0.5∫_0^1∫_0^1 1/(r'+s') dr' ds'=log(2)`.

Thus the Gamma-reference cross coupling can remain finite across an adjacent narrow interface in physical L2 normalization. Compared with each packet's logarithmic norm squared `~log(1/ell)`, the normalized coupling is of order `1/log(1/ell)`. This does **not** prove a uniform bound for all possible adjacent profiles, and the strong-coupling branch in CF018 remains unresolved.

## CF019-C — original arithmetic coupling survives remote separation

Take `c=0.4`, `a=log(2)`, and two L2-unit positive rectangular packets of width `ell<min(2*c-a,a)` separated by exactly `a` between corresponding points; the physical gap between supports is `a-ell>0`.

Because only `n=2` is active, the exact mixed discrepancy is

`D(u_ell,v_ell)=kappa/2 - (8*sqrt(2)/ell)*sinh(ell/4)^2 -> kappa/2`, `kappa=log(2)/sqrt(2)`.

But the Gamma reference cross kernel obeys

`B_ref(u_ell,v_ell)=-ell*q(a)+o(ell)= -ell/(3*sqrt(2))+o(ell)`.

Therefore the original full mixed form has

`B_W(u_ell,v_ell)=B_ref(u_ell,v_ell)-2D(u_ell,v_ell) -> -kappa`.

A relative complex phase multiplies this mixed value by the corresponding conjugate phase; the sign of its real part is **not determined by the unsigned prime interaction graph**. This is a rigorous concrete separation of arithmetic remote coupling from the shorter-range Gamma-reference interaction. No negative diagonal witness follows: each individual packet's positive log energy grows as `log(1/ell)`.

## CF019-D — three-zone boundary screening inequality

Fix a support window `[-c,c]`. Let `k` be a hypothetical nonzero full-form neutral mode at a nonnegative window, and choose a smooth partition `k=u_far+u_near+v`, with `v` supported in an endpoint interval of width `ell` and `u_far` physically separated from `v` by a **fixed positive gap** `d`. The near term may overlap `v`; the separated-kernel identity must not be applied to `u_near` without justification. Smooth cutoffs preserve the log form domain.

Set `h(ell)=sqrt(2/log(exp(1)+1/(4*ell)))`, and let `A_c(ell)` be the rigorous CF018 arithmetic discrepancy coefficient. Since `||u_far||_1<=sqrt(2*c)||u_far||_2` and `||v||_1<=sqrt(ell)||v||_2`, and the log norm dominates L2,

`|B_ref(u_far,v)| <= F(c,d,ell)||u_far||log||v||log`

with `F(c,d,ell)=q(d)*sqrt(2*c*ell)*h(ell)=O_(c,d)(sqrt(ell/log(1/ell)))`.

By `B_W=B_ref-2D`, 

`|B_W(u_far,v)| <= [F(c,d,ell)+2*A_c(ell)]||u_far||log||v||log`.

The native bounded operator gives `|B_W(u_near,v)|<=C_c||u_near||log||v||log` with `C_c=||A_native,c||` in the logarithmic carrier.

CF018's narrow-packet coercivity gives `Q_W(v)>=0.5||v||log^2`. Exact mixed nullity `B_W(k,v)=0` then implies, provided `v!=0`,

`0.5||v||log <= C_c||u_near||log + [F(c,d,ell)+2*A_c(ell)]||u_far||log`.

The remote term coefficient tends to zero as `ell->0` for fixed `(c,d)`. Consequently the boundary packet must be screened by genuinely near-interface log-energy, unless the remote part has a norm large relative to the packet. This is a **necessary quantitative inequality**, not an RH proof. In particular, `||v||log` might vanish even more rapidly and no lower bound for a neutral mode's collar energy is established.

## Verification status and CI gate

Local file `cf019_reference_cross_validator.py` independently checks `K-G=q`, the Laplace series, adjacent-packet `-log(2)` limit, and original `Gamma+pole-prime` mixed form versus the reference discrepancy form for the genuine `n=2` case. `cf019_reference_cross_output.txt` records output. These are numerical controls; not rigorous interval arithmetic.

Highest-value next formal sequence:
1. Verify the Gamma translation-energy identity in the exact Mathlib angular-frequency convention and provide same-domain complex polarization.
2. Prove the positive-gap Laplace-moment factorization and finite-tail bound (can be a standalone analytic lemma, not a theorem about RH).
3. Prove the phase-sensitive one-prime packet asymptotics and the native bounded-form three-zone inequality.
4. Investigate whether any genuine neutral mode has a lower bound on the near-interface energy strong enough to combine with this inequality.
5. Cross-projection: compare the `lambda=5/2+2j` moments with the CF002 Gamma exterior moments and IV030's phase-sensitive graph without assuming equivalence.

Before any GitHub write/PR or Actions run, verify the selected research base contains both accepted source ancestry and repaired source-scoped workflows. Previously compared NF753/NF756 lineages diverge, so that gate is not discharged by this note. Preserve certificates and strict axiom audits, and do not promote the HD/A count.