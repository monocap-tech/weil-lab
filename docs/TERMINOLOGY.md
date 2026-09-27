# Terminology Registry

This registry defines project terms before or with their first load-bearing use. Historical wording remains historical; changes are additive rather than retroactive.

## Horizon

A **horizon** is a finite research package with an explicit acceptance condition and an explicit stop boundary.

A horizon may contain open mathematical interfaces. Completion means that the horizon's own deliverables are satisfied, not that every downstream problem is solved.

## Phase

A **phase** is an ordered unit inside a horizon.

A phase has:

- a mathematical purpose;
- an entry condition;
- a set of allowed tasks;
- an exit condition;
- a list of outputs.

Phases are not merely chronological labels.

## Standing

**Standing** records what epistemic status a claim has inside the repository.

Current public standing labels:

- **PROVED** — established within the stated framework and hypotheses.
- **CONDITIONAL** — proved assuming an explicitly named hypothesis or branch condition.
- **DERIVED** — exact reformulation or reduction from retained inputs.
- **IMPORTED** — taken from an external theorem or source and used with explicit scope.
- **COMPUTATIONAL** — numerically certified or experimentally supported over a stated finite domain.
- **OPEN** — required for later closure but not established.

Standing is typed, not scalar: an imported theorem, an internal derivation, and a computational certificate are not interchangeable.

## Interface

An **interface** is a theorem-shaped boundary between one completed research package and a downstream problem.

An open interface is not automatically an incomplete proof inside the current horizon.

For Horizon 1, the two primary RH-facing stop-line interfaces are `AZ-NEXTJET-LOC` and `AZ-FIN-WEIL-NULL-EXTENSION`. The registry also tracks the stronger special-packet refinement `C-ACTUAL-KPH-FLOOR`:

```math
\texttt{AZ-NEXTJET-LOC},
\qquad
\texttt{C-ACTUAL-KPH-FLOOR},
\qquad
\texttt{AZ-FIN-WEIL-NULL-EXTENSION}.
```

## Re-entry

**Re-entry** is the explicit promotion of a result from one project layer or horizon into a stronger downstream theorem line.

Re-entry requires a scope audit. It is never inferred merely because the same notation or object appears in both layers.

## Custody

**Custody** means preserving the identity, hypotheses, and scope of the mathematical object being tracked through a reduction or transfer.

A valid reduction must not silently replace a selected packet, metric, support scale, or theorem hypothesis by a weaker aggregate object.

## Screening

**Spectral screening** is the finite-to-infinite phenomenon in which a negative eigenvalue present at every finite truncation may approach the zero boundary as the positive complement is restored:

```math
\lambda^-_{N,k}<0,
\qquad
\lambda^-_{N,k}\uparrow0.
```

It distinguishes finite negative index from infinite negative-mode survival.

## Defect

A **defect** is the residual obstruction left after the positive/background contribution has been separated from a selected negative or neutral channel.

In the rank-one formulation, a representative defect operator is

```math
\mathcal K_C(t)
=
\widetilde S_t\widetilde S_t^{*}
-
\widetilde g_C\otimes\widetilde g_C.
```

The term does not by itself assert negativity.

## Negative persistence

**Negative persistence** means that after the screening limit, a selected negative-signature direction survives projectively rather than collapsing entirely into the zero boundary.

## Neutral persistence

**Neutral persistence** means that the limiting obstruction survives at zero signature as a null mode rather than as a strictly negative direction.

In the current compact-window branch this is represented by

```math
W_ck=0.
```

## Morphology

A **defect morphology** is a theorem-level structural branch describing how a defect or critical sequence can persist, become neutral, or fail compactness after the completed reductions have been applied.

Horizon 1 packages three morphology classes:

1. fixed-packet negative persistence, ending at weighted next-jet localization;
2. fixed-packet attained-neutral persistence, ending at compact-window null-extension/support rigidity;
3. noncompact coefficient morphology, separating moving/infinite selected-sector escape from unselected-background escape and fixed full-divisor weak limits.


## Synthesis pair

A **synthesis pair** is a pair of bounded operators

```math
S_{+}:K_{+}\to\mathcal H,
\qquad
S_{-}:K_{-}\to\mathcal H
```

assembled into

```math
E(x,u)=S_{+}x+S_{-}u.
```

The $+$ and $-$ labels refer to the coefficient-space indefinite signature, not to positivity of the operators themselves.

## Analysis space

The **analysis space** associated with a synthesis pair is

```math
\mathcal A=(\ker E)^\perp
=
\overline{\operatorname{Ran}E^{*}}.
```

It is the coefficient space actually visible to physical synthesis.

## Physical defect operator

The **physical defect operator** is

```math
D
=
S_{+}S_{+}^{*}
-
S_{-}S_{-}^{*}
=
EJE^{*}.
```

Its quadratic form exactly represents the indefinite coefficient form on vectors of the form $E^{*}h$.

## Exact screening

**Exact screening** means

```math
\operatorname{Ran}S_{-}
\subseteq
\operatorname{Ran}S_{+}.
```

Equivalently, there exists a bounded $X$ such that

```math
S_{-}=-S_{+}X.
```

Exact screening does not imply that the screening coefficient norm fits inside the unit budget.

## Reduced screening solution

The **reduced screening solution** is the unique Douglas reduced solution $X$ of

```math
S_{+}X=-S_{-}
```

whose range lies in

```math
(\ker S_{+})^\perp.
```

It is the minimum-norm canonical screening operator.

## Over-budget defect

An **over-budget defect** occurs when exact screening holds but the reduced screening solution satisfies

```math
\|X\|>1.
```

The negative physical channel lies in the positive range, but reproducing it requires more than the unit indefinite-metric budget.

## Critical screening

**Critical screening** is the boundary case

```math
\|X\|=1.
```

Critical screening splits into attained and non-attained cases.

## Approximate-neutral boundary

The **approximate-neutral boundary** is critical screening with

```math
\|X\|=1
```

but no nonzero vector $a$ satisfying

```math
\|X^{*}a\|=\|a\|.
```

There is then no actual neutral vector, while normalized positive margins can still converge to zero along an approximate-neutral sequence.

This term is distinct from **neutral persistence**.


## Selected negative sector

A **selected negative sector** is a distinguished closed subspace

```math
M\subseteq K_{-}
```

whose defect ownership is tracked separately from the remaining negative channels.

When $M$ is finite dimensional, its dimension gives an upper bound on the negative index it can create by itself.

## Negative background

The **negative background** is the complementary negative channel space

```math
B=M^\perp\cap K_{-}.
```

Background contributions can make a selected negative witness more negative, but aggregate negativity need not belong to the selected sector.

## Residual screening budget

If a background channel is contractively screened by $X_B$, the **residual screening budget** is

```math
R_B=I-X_BX_B^{*}.
```

It records the positive coefficient-space capacity remaining for later selected channels.

## Effective positive synthesis

The **effective positive synthesis** after background elimination is

```math
S_{\rm eff}=S_{+}R_B^{1/2}.
```

It allows the selected problem to be re-entered into the same defect calculus after a legitimate background screening step.

## Shared screening budget

The **shared screening budget** principle is that negative channel blocks are jointly admissible only when their combined screening covariance fits inside the unit budget.

Separate contractivity of each block is not sufficient.

## Shorted covariance

For a positive covariance $K$ and a selected physical subspace $W$, the **shorted covariance** is the covariance remaining on $W$ after the complementary physical subspace has been optimized away.

In an invertible block decomposition

```math
K=
\begin{pmatrix}
A&B\\
B^{*}&C
\end{pmatrix},
```

it is

```math
H_W=A-BC^{-1}B^{*}.
```

Direct compression $A$ and shorted covariance $H_W$ have different inverse-control meanings.

## Signature shadow

A **signature shadow** is a coordinate projection of an indefinite coefficient vector that preserves its algebraic sign margin but need not remain in the relevant analysis space.

A signature shadow is not automatically an admissible persistent vector.


## Right-limit analysis space

For a monotone analysis-space filtration

```math
\mathcal A_s\subseteq\mathcal A_t
\qquad(s<t),
```

the **right-limit analysis space** at $c$ is

```math
\mathcal A_{c+}
=
\bigcap_{t>c}\mathcal A_t.
```

It contains coefficient vectors that persist at every support/observation scale immediately to the right of the endpoint.

## Endpoint jump

The **endpoint jump** is the Hilbert-space difference

```math
\mathcal J_c
=
\mathcal A_{c+}\ominus\mathcal A_c.
```

A nonzero endpoint jump records failure of right continuity of the analysis-space filtration.

When $\mathcal A_c$ is $J$-nonnegative, any new right-limit negative index must inject into the quotient

```math
\mathcal A_{c+}/\mathcal A_c.
```

## Right-persistent vector

A **right-persistent vector** is a vector

```math
y\in\mathcal A_{c+}.
```

It is **new at the endpoint** when

```math
y\notin\mathcal A_c.
```

Negative and neutral persistence are sign-refined forms of this notion.

## Boundary amplification

Given a bounded physical realization

```math
\mathcal A_t
=
\overline{T(\mathscr H_t)},
```

the **boundary amplification cost** of $y$ is

```math
\mathfrak B_y(t,\varepsilon)
=
\inf
\left\{
\|h\|:
h\in\mathscr H_t,\
\|Th-y\|\le\varepsilon
\right\}.
```

For a genuinely new endpoint vector, this cost diverges as

```math
(t,\varepsilon)\to(c+,0).
```

## Moving-sector escape

A **moving-sector escape** occurs when the selected negative direction itself moves through an infinite coefficient space as the filtration approaches the endpoint.

This can destroy every nonzero right-limit ray even when every stage contains a finite-dimensional negative direction.

It is distinct from positive-coordinate mass loss with a fixed finite negative sector.


## Zero-side Weil representation

The **zero-side Weil representation** is the coefficient/synthesis realization of the Weil quadratic form in terms of zero channels.

Its positive coefficient sector contains critical-line coordinates and positive off-axis pair directions; its negative sector contains antisymmetric off-axis pair directions.

## Weil pair channels

For a nonreal ordinate pair

```math
\gamma=T+i\delta,
\qquad
\bar\gamma=T-i\delta,
```

the canonical **Weil pair channels** are

```math
p
=
\frac{e_\gamma+e_{\bar\gamma}}{\sqrt2},
\qquad
n
=
\frac{e_\gamma-e_{\bar\gamma}}{\sqrt2}.
```

They satisfy

```math
Jp=p,
\qquad
Jn=-n.
```

The $p$-channel is the positive/symmetric pair direction; the $n$-channel is the negative/antisymmetric pair direction.

## Selected packet

A **selected packet** $\Pi$ is a fixed finite set of off-axis zero channels whose negative sector is tracked with custody through the defect calculus.

Its selected negative coefficient space is denoted

```math
M_\Pi\subseteq K_{-}.
```

## Unselected negative divisor

The **unselected negative divisor** relative to $\Pi$ is the complementary negative coefficient sector

```math
B_\Pi=M_\Pi^\perp\cap K_{-}.
```

It is the zeta-Weil realization of the abstract negative background.

## ZW-0 / ZW-1 / ZW-2

Horizon 1 uses three zeta-specialization layers:

- **ZW-0 — Weil/Krein pair geometry:** zero-side pair diagonalization, sign channels, finite index, and compact-window synthesis.
- **ZW-1 — zeta-divisor structure:** functional-equation/conjugation structure, selected packets, zero-moment residues, actual zero-count/compactness inputs.
- **ZW-2 — explicit-formula arithmetic:** prime, pole, archimedean, completed $\Xi$, next-jet, and finite translation structure.

These labels distinguish where arithmetic genuinely enters.

## Explicit-formula side

The **explicit-formula side** is the prime/pole/archimedean representation of the same Weil quadratic form.

It is not an additional positive screening sector and must not be added to $K_{+}$ as though it supplied independent coefficient budget.


## Raw residue vector

Given a selected negative pair-coordinate vector $u$, the **raw residue vector** $v$ is obtained by undoing the canonical pair diagonalization back to the selected zero coordinates.

For each negative pair channel, the two raw coefficients are equal and opposite.

## Zero-moment law

The **zero-moment law** is

```math
\mathbf{1}^Tv=0.
```

It is a ZW-1 structural identity coming from antisymmetry of the negative pair channels.

It is not a generic H1-P1 screening theorem and does not use the prime side of the explicit formula.

## Rational response

The **rational response** of a finite raw residue vector is

```math
R_v(z)
=
\sum_j\frac{v_j}{z-\rho_j}.
```

Under the zero-moment law,

```math
R_v(z)=O(|z|^{-2}).
```

The inverse-square order is the universal pair-geometric order unless additional moment cancellation is proved.

## Native Problem-1 synthesis

The **native Problem-1 synthesis** is Bombieri's Green-preconditioned zero synthesis into the Dirichlet $H^{-1}$-type physical carrier.

For fixed support it is Hilbert-Schmidt, hence compact.

This term distinguishes the actual Weil/Bombieri operator metric from unweighted exponential $L^2$ models.

## Unweighted mirror model

An **unweighted mirror model** is an $L^2/PW_t$ exponential or cosh/sinh sampling model in which the Green weights of native Problem 1 have been removed.

Frame or sampling lower bounds in this model are auxiliary harmonic-analytic statements and are not automatically native Problem-1 coercivity estimates.

## Metric separation

**Metric separation** is the rule that a theorem proved in an unweighted exponential/sampling norm may not be transferred to the native Problem-1 $H^{-1}$ operator without an explicit bounded comparison theorem.

In particular, a stable unweighted frame does not contradict compactness of native Problem-1 synthesis.


## Selected-preserving multiplier

A **selected-preserving multiplier** for a raw residue source $v$ is an admissible scalar multiplier $\psi$ satisfying

```math
\mathcal C_v[\psi]=0,
```

so the selected contracted-residue contribution is removed without discarding the complementary divisor, prime, and archimedean terms.

## Far complementary field

The **far complementary field** is the contribution of unselected zeros outside a fixed neighborhood of the selected packet:

```math
\mathcal F_{v,R}[\psi]
=
\sum_{\substack{\mu\notin F\\|\Im\mu-T_F|\ge R}}
m_\mu\psi(\mu)R_v(\mu).
```

For a fixed bounded multiplier and a zero-moment selected source,

```math
\mathcal F_{v,R}[\psi]
=
O((\log R)/R).
```

## Weighted next-jet field

The **weighted next-jet field** is

```math
\mathcal N_{v,R}[\psi]
=
\sum_{\mu}^{\rm near}
m_\mu\psi(\mu)
\frac{H_v^{(m_\mu)}(\mu)}
{\Xi^{(m_\mu)}(\mu)},
\qquad
H_v=\Xi R_v.
```

It is the finite/intermediate complementary divisor object left after zero-moment far-tail localization.

## Explicit-formula co-adaptation

**Explicit-formula co-adaptation** is the phenomenon that adapting $\psi$ to cancel one side of the scalar explicit formula changes the remaining prime/archimedean balance simultaneously.

In particular, under selected preservation, if

```math
\mathcal N_v[\psi]=\mathcal A_v[\psi],
```

then

```math
\mathcal P_v[\psi]=\mathcal F_v[\psi].
```

Thus adaptive near cancellation does not leave an independent prime lower bound.

## Compact-window arithmetic operator

The **compact-window arithmetic operator** at support $c$ is the physical operator representing the geometric Weil form:

```math
\mathcal W_c
=
\mathcal A_\infty
-
\sum_{\log n<2c}
\frac{\Lambda(n)}{\sqrt n}
(\tau_{\log n}+\tau_{-\log n})
+
\mathcal R_{\rm pole},
```

up to the fixed Fourier-normalization convention.

At fixed $c$, the prime-translation sum is finite.

## Logarithmic form order

The **logarithmic form order** is the high-frequency asymptotic

```math
\Psi_c(t)
=
\log|t|+O_c(1).
```

It implies that the natural form norm is equivalent, after an $L^2$ shift, to a logarithmic Fourier/Sobolev norm rather than to a positive-order Sobolev norm.


## Unit-gain neutral relation

A **unit-gain neutral relation** is a finite-exception selected direction $u\neq0$ satisfying

```math
C_c^{*}C_cu=u.
```

Equivalently,

```math
\|C_cu\|=\|u\|.
```

This is the attained-neutral boundary condition in the selected compensator metric.

## Physical neutral mode

A **physical neutral mode** is a nonzero physical vector $k$ realizing a unit-gain neutral relation through

```math
C_cu=P_c^{*}k.
```

With

```math
N_c=-P_cC_c,
```

it satisfies

```math
N_c^{*}k=-u
```

and therefore

```math
W_ck=0,
\qquad
W_c=P_cP_c^{*}-N_cN_c^{*}.
```

## Null-extension problem

The **null-extension problem** asks whether the zero extension $\widetilde k$ of a compact-window physical neutral mode has Weil output

```math
\mathcal W_c^{\rm ext}\widetilde k
```

vanishing on a nontrivial exterior collar adjacent to the original support.

It is a fixed-vector support question, not merely a regularity or approximate-closure question.

## Negative fall-through

**Negative fall-through** is the fixed-packet critical alternative in which positive coefficient mass is lost in the right-limit process, converting an approximately neutral sequence into a strictly negative persistent ray.

Negative fall-through is assigned to the negative morphology theorem rather than to the neutral branch.


## Background escape

**Background escape** is failure of strong compactness in the normalized unselected negative background after a fixed selected packet has already been anchored.

It includes:

- background norm escape;
- bounded coefficient-tail escape.

Background escape does not erase the fixed selected negative ray.

## Coefficient-tail tightness

A bounded sequence $b_n$ in an $\ell^2$-type coefficient space is **coefficient-tail tight** when, for a canonical increasing finite-coordinate exhaustion $Q_R$,

```math
\lim_{R\to\infty}
\sup_n
\|(I-Q_R)b_n\|
=
0.
```

Bounded coefficient-tail tightness implies precompactness.

## Fixed full-divisor ray

A **fixed full-divisor ray** is historical shorthand reserved for the stronger case of a full strong coefficient limit

```math
Y_{\rm full}=(a,u,b)
```

containing the positive coordinate, fixed selected negative coordinate, and a strongly convergent unselected negative background.

On the negative morphology branch its full signature remains strictly negative. The audited WD-T39 theorem generally guarantees only a **fixed full-divisor negative weak limit**; use “fixed full-divisor ray” only when positive-coordinate strong convergence is additionally available.

## Selected-sector escape

**Selected-sector escape** is the noncompact morphology in which the selected negative direction or mass moves through successively new coordinates so that every fixed finite coordinate projection tends to zero.

Selected-sector escape may produce normalized approximate zero-edge relations with weak coefficient limit zero.

It is distinct from background escape.


## Stable theorem ID

A **stable theorem ID** is the additive public identifier assigned during H1-P4.

Stable theorem IDs use the form

```math
\texttt{WD-T01},\texttt{ WD-T02},\ldots
```

and do not replace historical labels. Historical labels remain immutable provenance aliases.

A stable theorem ID is a name, not a certification mark.

## Verification status

**Verification status** records how far a theorem has progressed through proof/source audit independently of its mathematical standing.

The completed H1-P4 verification labels used on the stable inventory are:

- **P4-AUDIT-PASSED**;
- **SOURCE-PINNED**;
- **COMPOSITE-AUDIT-PASSED**;
- **EXAMPLE-AUDIT-PASSED**;
- **SCOPE-ONLY**.

The corresponding pending labels are queue/history states, not current terminal H1-P4 standings.

Verification status is distinct from whether the repository contains an internal proof.

## Internal proof standing

**INTERNAL-PROOF** means that proof text is present in the repository under the stated hypotheses.

It does not mean that the proof has been independently certified, formally verified, or externally refereed.


## Source-pinned

**SOURCE-PINNED** means that a load-bearing external input has been tied to an exact theorem, lemma, equation, or page location and that the convention imported from that source has been recorded.

Source-pinned does not mean the repository's downstream use of the source has completed internal proof audit.

## Source pin

A **source pin** is the durable record connecting one external input to:

1. its bibliographic source;
2. its exact theorem/equation location;
3. the notation or convention imported into this project;
4. the stable theorem IDs that consume it.


## P4-audit-passed

**P4-AUDIT-PASSED** means that the theorem's current repository proof/reduction has passed the Horizon-1 internal audit for stated hypotheses, domains, topology transitions, quantifiers, and dependency custody, after any recorded corrections.

It does not mean independent certification, formal verification, or external refereeing.


## Composite-audit-passed

**COMPOSITE-AUDIT-PASSED** means that a packaged morphology theorem has passed the Horizon-1 end-to-end dependency/hypothesis audit after any recorded narrowing corrections.

It does not mean independent certification or external refereeing.

## Right-limit compact-window operator

Under the strict endpoint convention

```math
\log n<2c,
```

the **right-limit compact-window operator** is the operator seen under arbitrarily small strict right enlargement:

```math
\mathcal W_{c+}^{\rm ext}
=
\mathcal A_\infty
-
\sum_{\log n\le2c}
\frac{\Lambda(n)}{\sqrt n}
(\tau_{\log n}+\tau_{-\log n})
+
\mathcal R_{\rm pole}.
```

Away from a prime-power threshold it equals $\mathcal W_c^{\rm ext}$. At a threshold it differs by the finite equality-threshold translation terms.

## P4 audit clarification — fixed full-divisor limit

In the audited stable theorem WD-T39, a **fixed full-divisor negative weak limit** is

```math
Y_{\rm full}=(a,u,b)
```

with

```math
a_n\rightharpoonup a,
\qquad
u_n\to u,
\qquad
b_n\to b.
```

Thus the whole negative sector converges strongly while the positive coordinate may converge only weakly.

The earlier stronger phrase **fixed full-divisor ray** applies as a full strong limit only when the additional positive-coordinate compactness condition

```math
a_n\to a
```

is also available.


## Example-audit-passed

**EXAMPLE-AUDIT-PASSED** means that an explicit example/sharpness construction has been checked algebraically and that the theorem boundary it is claimed to sharpen has been verified.

It does not mean independent certification or external refereeing.


## Lean certification

**LEAN-CERTIFIED** means that a mapped Lean declaration has passed the pinned Lean/mathlib build with no project-level unfinished proof placeholders or project axioms.

Lean certification is separate from P4 internal audit status.

## Lean-certified from imported premise

**LEAN-CERTIFIED-FROM-IMPORTED-PREMISE** means Lean kernel-checks the project's downstream deduction from an explicitly represented external theorem premise, while the external theorem itself has not yet been reconstructed in Lean.

This status must never be presented as formal verification of the imported source theorem.

## Lean-blocked

**LEAN-BLOCKED** means a formalization pass has been exhausted and a precise missing formal dependency, library theorem, or source reconstruction obligation has been recorded.

It is a terminal status for the current LEAN-H1 exhaustion test, but not a claim that the theorem is impossible to formalize.

## Lean formalization exhaustion

**Lean formalization exhaustion** is reached when every stable Horizon-1 theorem/example is assigned one of:

- LEAN-CERTIFIED;
- LEAN-CERTIFIED-FROM-IMPORTED-PREMISE;
- LEAN-BLOCKED with an exact blocker;
- SCOPE-ONLY.

No stable theorem/example may remain merely unattempted when LEAN-H1 closes.


## Dyadic escape filtration

The **dyadic escape filtration** is the descending family attached to a finite-dimensional source subspace (Wsubseteq K_c) under repeated truncated translation by the first-prime length

[
a=log2.
]

With (S_a) denoting the right-oriented truncated shift, define

[
C_j(W)
=
left{
fin W:
S_a^k fin K_c
	ext{ for }0le kle j
ight}.
]

Thus

[
W=C_0(W)supseteq C_1(W)supseteqcdots.
]

The quotient

[
C_j(W)/C_{j+1}(W)
]

is the **escape layer at depth (j+1)**: its nonzero classes remain inside the regular kernel through (j) dyadic relocations and acquire a nonzero (K_c^perp) component at the next relocation.

The integer (j+1) is the **dyadic escape depth** of that layer.

These terms are currently research-local and unratified. They do not assert that the escaped component is persistent, negative, or canonically identified with any zero-side channel.


## Blind-transform filtration

The **blind-transform filtration** is the descending finite-dimensional filtration obtained by measuring the boundary flatness of the archimedean transform of a one-sided blind source cell.

For the first-prime cell width (a=log2), a blind-cell profile (bin L^2(0,a)) is observed by

[
(mathscr T_{m blind}b)(eta)
=
int_0^a
a_infty''(eta+r)b(r),dr,
qquad
eta>0.
]

For a finite-dimensional blind-cell family (V), define

[
V_N^{m blind}
=
left{
bin V:
|mathscr T_{m blind}b|_{L^2(0,arepsilon)}
=
o(arepsilon^N)
ight}.
]

The stabilized intersection

[
V_infty^{m blind}
=
igcap_N V_N^{m blind}
]

is the **blind-transform superflat subspace**.

These terms are currently research-local and unratified. Transform superflatness refers to the observed archimedean field, not automatically to (L^2)-mass flatness of the blind source germ itself.


## Bilateral visible-superflat subspace

The **bilateral visible-superflat subspace** is the subspace of the finite edge obstruction whose local (L^2)-mass is superflat to every algebraic order on the inward-visible half-collars for **both** right-edge and left-edge orientations.

At a reflected prime site
[
c-ell=-c+(2c-ell),
]
the right-oriented blind physical half is the left-oriented visible physical half. Thus membership in the bilateral visible-superflat subspace makes the right-blind source germ itself (L^2)-superflat at every reflected site.

This term is currently research-local and unratified. It does not assert that the full source vanishes near a reflected site, only that both one-sided visible mass functions are superflat there.


## Arithmetic ratio germ

An **arithmetic ratio germ** is a local source germ created by the exact threshold equation when a prime-power delay (lambda=log m) acts inside a larger threshold delay (ell=log n).

Its source location in right-oriented coordinates is

[
ell-lambda=log(n/m).
]

If (m) and (n) are powers of the same prime and (mmid n), this difference is another prime-power hinge. Otherwise it is an **off-hinge ratio germ**: a rough interior source germ sampled directly by the prime translation term even though its location is not one of the original edge prime singular sites.

These terms are currently research-local and unratified. They describe source custody under multi-delay first-kind equations; they do not create a new singularity of the screw kernel at that physical point.


## Ratio-germ filtration

The **ratio-germ filtration** is the finite-dimensional local-mass filtration on the first off-hinge arithmetic ratio layer

[
mathscr R_c^{(1)}
=
{
ell-lambda:
0<lambda<ell,;
lambda,ellinmathscr H_c^circ,;
ell-lambda
otinmathscr H_c^circ
}.
]

For a finite obstruction family (W), the order-(N) ratio-flat subspace consists of those sources whose local (L^2)-mass on every right-sided ratio germ (d+eta), (dinmathscr R_c^{(1)}), is (o(arepsilon^N)). Its stabilized intersection is the **ratio-superflat subspace**.

## Ratio incidence operator

The **ratio incidence operator** is the finite weighted operator that inserts the off-hinge ratio germs into the vector of prime-threshold equations:

[
(mathsf A_c g)_ell
=
sum_{substack{lambda<ell\
ell-lambdainmathscr R_c^{(1)}}}
rac{Lambda(e^lambda)}{e^{lambda/2}},
g_{ell-lambda}.
]

Here (g_d) denotes the local source germ at the ratio location (d). The operator records arithmetic multi-cell custody only; it does not include the archimedean cell transforms or the same-prime/endpoint terms already absorbed into the superflat remainder.

These terms are currently research-local and unratified.


## Arithmetic center lattice

The **arithmetic center lattice** associated to the active prime bases is the additive subgroup

[
Gamma_c
=
sum_{p:,log p<2c}mathbb Z,log p
subsetmathbb R.
]

Its points in ((0,2c)) are **reachable arithmetic centers** for movable-center bookkeeping: repeated shifts by active prime delays move source locations and centers within this additive group.

When at least two distinct prime bases are active, (Gamma_c) is dense in (mathbb R), because the logarithms of distinct primes have irrational ratio.

This term is currently research-local and unratified. Density of the arithmetic center lattice concerns center reachability; it does not assert regularity or pointwise evaluation of (L^2) kernel vectors.


## Diagonal symmetrization

For an interior source center (h) and radius (ho>0) with ((h-ho,h+ho)subset(0,2c)), the **diagonal symmetrization** is

[
(Sigma_{h,ho}f)(t)
=
f(h+t)+f(h-t),
qquad
0<t<ho.
]

The centered archimedean second-difference kernel is even in the source displacement from (h), so its nonanalytic local diagonal contribution depends only on (Sigma_{h,ho}f). The antisymmetric local germ (f(h+t)-f(h-t)) is exactly invisible to that local diagonal channel.

This term is currently research-local and unratified. Vanishing of one diagonal symmetrization is a parity statement, not a claim that the full source or full movable-center equation vanishes.


## Prime-invisible core

Let (L=2c) and (a=log2). In the support regime

[
a<L<2a=log4,
]

the **prime-invisible core** is the open source interval

[
J_c=(L-a,a).
]

For every active prime-power delay (lambdage a), every interior movable center (hin(0,L)), and every admissible centered scale (0<delta<min(h,L-h)), the prime tent neighborhoods centered at (hpmlambda) are disjoint from (J_c). Consequently every source supported in (J_c) is exactly invisible to the complete finite prime-tent part of every movable-center equation.

This term is currently research-local and unratified. Prime invisibility refers only to the prime translation channels; the archimedean diagonal channel still observes such a source.


## Prime-silent regular kernel

Let

[
(mathsf P_cf)(x)
=
sum_{lambdainmathscr H_c^circ}
a_lambda
left[
f(x-lambda)+f(x+lambda)
ight]
]

on ((0,2c)), with (f) extended by zero outside the support interval.

The **prime-silent regular kernel** is

[
K_c^{m ps}
=
K_ccapkermathsf P_c.
]

Equivalently, it consists of regular kernel vectors whose complete all-center prime-tent observation vanishes identically. This is a canonical subspace of (K_c).

Prime silence does not mean the source vanishes or is archimedean-invisible. It means only that the finite prime-translation part has zero interior second derivative / zero movable-center tent field.


## Boundary transfer state

A **boundary transfer state** is the finite-dimensional source state used after a boundary-ordering change prevents scalar residue-chain closure.

For the post-p SZ edge chamber, write X(x)=H(x), S(x)=H(s+x), h=log(81/80), p=log(10/9), and e=u-p. The bulk state is

V(x)=(X(x),S(x))^T.

On the overlap window e-h < x < p it obeys one constant unimodular transfer matrix V(x+h)=M V(x). The lower and upper defect strips (0,e) and (p,u) are paired by adjoining the translated copy V(p+t), 0<t<e. Thus the closed defect bookkeeping uses the two-sheet state

W(t)=(V(t),V(p+t)),

with only finitely many additional gated k=log(16/15) translations.

This term is research-local and unratified. It describes the finite-state recurrence mechanism; it does not assert injectivity or shrinking-collar coercivity.


## Paired defect block

In the post-p boundary transfer, when the defect width e satisfies k < e <= k+h, the only defect-internal k-feedback pairs the lower strip 0<t<e-k with the upper strip k<t<e.

After folding t with t+k, the local coefficient block on the four scalar values (X(t),S(t),X(t+k),S(t+k)) is

D1 =
[[G, delta, 0, beta],
 [delta, G, 0, 0],
 [0, 0, G, delta],
 [beta, 0, delta, G]].

This is the **paired defect block**. Its determinant factors as

det D1
=
-(-G^2 + G beta + delta^2)
 ( G^2 + G beta - delta^2).

For the exact Weil weights both factors are positive, so the paired defect block is invertible.

This term is research-local and unratified. Invertibility of the paired defect block excludes local rank loss from the single k-feedback pair; it does not by itself prove global boundary transversality.


## Boundary monodromy

After finite atom folding of a prime-channel boundary-transfer system, eliminate every tree-like atom using the locally invertible defect/overlap blocks. The remaining cycle state is the **boundary monodromy state**.

If C is the return map obtained by propagating that cycle state once around the surviving folded cycle, then global boundary rank loss occurs exactly when

det(I-C)=0.

In the first post-p chamber, the folded graph has cycle rank at most one when e<=k and at most two when k<e<=k+h. Therefore the monodromy state has at most two bulk-state copies: two scalar coordinates per cycle, hence at most four scalar coordinates.

This term is research-local and unratified. Boundary monodromy concerns fixed-L prime-channel transversality; it does not imply shrinking-collar coercivity.


## Matched defect scattering insertion

In the post-p boundary transfer, suppose one lower point carries the forward k-tap and its paired point x+k carries the matching backward tap. Let V(x)=(X(x),S(x))^T, let M0 be the 2-state bulk transfer, let e1=(1,0)^T and e2=(0,1)^T, and let c_plus,c_minus be the exact forward/backward tap columns from the finite-tap transfer.

The **matched defect scattering insertion** is the 4-by-4 transfer matrix K on the paired state (V(x),V(x+k)) defined by

V(x+h) = M0 V(x) + c_plus e2^T V(x+k),

V(x+k+h) = M0 V(x+k) - c_minus e1^T V(x+h).

Equivalently,

K =
[[M0, c_plus e2^T],
 [-c_minus e1^T M0, M0 - (e1^T c_plus)c_minus e2^T]].

It factors into a lower shear times an upper block-triangular transfer and therefore det K = 1.

This term is research-local and unratified. It isolates one matched k-excursion; additional endpoint/defect scattering may still be present in a complete boundary monodromy word.


## Unmatched defect shear

Let M0 be the two-state bulk transfer, let B4=diag(M0,M0), and let c_plus,c_minus be the exact forward/backward k-tap columns in the post-p boundary transfer.

The **unmatched defect shears** are the doubled-state matrices

E_plus =
[[M0, c_plus e2^T],
 [0,  I]],

E_minus =
[[I, 0],
 [-c_minus e1^T, M0]].

Both have determinant 1. The matched defect scattering insertion satisfies

K = E_minus E_plus.

A separated one-k-excursion word is therefore represented by E_minus B4^m E_plus B4^n, or the reverse orientation.

This term is research-local and unratified. An unmatched shear by itself leaves one doubled sheet unadvanced; complete boundary closure may require additional endpoint relations.


## Endpoint graph line

For the gate-free prime-channel boundary transfer, the **endpoint graph lines** are the one-dimensional bulk-state subspaces

L_in = span((1,R)^T),

L_out = span((1,R^(-1))^T),

where R is the exact P/J transfer coefficient.

They encode the entrance relation S=R X and the terminal relation S=R^(-1) X. When a doubled unmatched shear carries one sheet by an identity block, that carried sheet is not free: true endpoint closure restricts it to one of these graph lines.

The resulting zero-bulk unmatched closure determinant is beta (mu^2-G^2)/(G delta^2), which is strictly positive for the exact Weil weights.

This term is research-local and unratified. Gated endpoint atoms may require corrected graph subspaces with an additional translated-sheet coordinate.


## Gated endpoint graph

When the post-p terminal k-gate is active, the gate-free endpoint graph line S=R^(-1)X is replaced by the **gated endpoint graph** on the doubled state (V(x),V(x+k)):

S(x) - R^(-1) X(x) + (beta/delta) S(x+k) = 0.

Equivalently, with W=(X,S,X_k,S_k), the terminal endpoint row is

(-R^(-1), 1, 0, beta/delta) W = 0.

The gate-free endpoint graph line is recovered when the translated-sheet term is absent.

This term is research-local and unratified. It identifies the exact remaining endpoint closure condition after the zero-bulk identity-sheet artifact is removed.


## Three-sheet boundary state

In the four-delay SZ chamber, let k=log(16/15) and let u=L-log5. Since u<3k, every head coordinate x in (0,u) lies in one of the three k-cells

(0,k), (k,2k), (2k,u).

The **three-sheet boundary state** is the finite L2 state obtained by collecting the bulk state V=(X,S) on these three cells, with zero/truncation on the last cell when 2k>=u.

All k-shift taps act only between adjacent sheets. The forward-gate source width satisfies alpha=u-k<=j<2k, so no fourth forward sheet can occur. The terminal k-gate is absent in the four-delay post-p chamber because k>h implies u-h>u-k=alpha on the terminal strip.

This term is research-local and unratified. It corrects the earlier two-sheet state as a globally complete bookkeeping device; the two-sheet state remains valid for the one-excursion subfamilies already audited.


## Three-sheet scattering block

Let M0 be the 2-state bulk transfer, C_plus=c_plus e2^T the forward k-coupling block, and C_minus=c_minus e1^T the backward coupling block.

For three active k-sheets V0,V1,V2, define the homogeneous sheet update sequentially by

Y0 = M0 V0 + C_plus V1,

Y1 = M0 V1 + C_plus V2 - C_minus Y0,

Y2 = M0 V2 - C_minus Y1.

The resulting 6-by-6 matrix K3 is the **three-sheet scattering block**.

Equivalently K3=L3 U3, where U3 is block upper bidiagonal with M0 on the diagonal and C_plus on the superdiagonal, while L3 is unit block lower bidiagonal with -C_minus on the subdiagonal.

Hence det K3=(det M0)^3=1.

More generally the same construction defines an r-sheet scattering block Kr with det Kr=(det M0)^r.

This term is research-local and unratified. In the four-delay chamber only r=1,2,3 occur. A separate causal past-tap term may enter the first sheet when x>k-h; K3 denotes the homogeneous local scattering block after that past contribution is separated.


## Causal lag injection

In the four-delay three-sheet transfer, the backward tap column simplifies exactly to

c_minus = (beta/delta) e1 = eta e1,

with eta=beta/delta.

After the active k-sheets are stacked and the internal backward taps are absorbed into the lower-triangular scattering block Kr, the only external history dependence is the scalar past coordinate

X(x-(k-h)).

For r active sheets its injection vector has first-coordinate blocks

-eta, eta^2, ..., (-1)^r eta^r

and zero second-coordinate blocks.

This rank-one delayed forcing is the **causal lag injection**. It is causal because k-h>0. For the exact Weil weights eta<9/10.

This term is research-local and unratified. It isolates the sole remaining nonlocal ingredient after finite k-sheet closure.


## Causal path expansion

For the four-delay three-sheet transfer, write the exact recurrence at the output coordinate y=x+h as

W(y) = K_r W(y-h) + b_r X(y-k).

A **causal path** is a backward dependency word from y obtained by steps of length h or k. Every step strictly decreases the absolute coordinate.

Because the head width satisfies u<3k, any causal path contains at most two k-steps. Hence repeated substitution produces a finite path expansion with causal degree at most two; there is no lag-generated feedback cycle.

The injection also factors universally:

K_r^(-1) b_r
=
-(d,0,...,0)^T,

where

d=(F,F/R)^T

occupies only the first two-state sheet. Equivalently,

W(y)
=
K_r [ W(y-h) - d_r X(y-k) ],

with d_r=(d,0,...,0)^T.

This term is research-local and unratified. The finite causal path expansion reduces global closure to finitely many endpoint path matrices; their nonvanishing is a separate transversality problem.


## p-defect relay

In the post-p four-delay chamber, the finite-tap transfer derived from the P/J overlap is not valid on the entire lower defect. For 0<t<e define the **p-defect relay**

P(t)=X(p+t),
Q(t)=S(p+t).

On 0<t<e-h the exact lower-defect equations are

mu P(t+h)
=
G X(t)+delta S(t)+beta S(t+k),

mu Q(t+h)
=
G S(t)-mu P(t)+delta X(t)
+beta 1_(t>k) X(t-k).

Thus the relay is triangular: P(t+h) is determined directly from the base k-sheet state, while Q(t+h) depends on the current scalar P(t) but Q(t) does not feed forward. The relay introduces no independent p-lattice.

This term is research-local and unratified. It repairs the domain gap in treating the P/J finite-tap recurrence as a globally complete head recurrence.


## Relay Schur closure

For the p-defect relay define the base forcing functionals

A(t) = [G X(t)+delta S(t)+beta S(t+k)]/mu,

B(t) = [G S(t)+delta X(t)+beta 1_(t>k) X(t-k)]/mu.

Then on h<t<e,

P(t)=A(t-h),

Q(t)=B(t-h)-P(t-h).

On the terminal relay strip max(0,e-h)<t<e, the exact endpoint constraint is P(t)=B(t).

Therefore, wherever t>h, relay closure reduces to the scalar base-state equation

A(t-h)=B(t).

On the part of the terminal strip with t<h, P(t) is supplied by the P/J overlap output at x=p+t-h and is equated to B(t).

This elimination of the relay variables is the **relay Schur closure**. It shows that the nilpotent relay contributes no independent recurrence state; it contributes a finite terminal closure row on the base transfer system.

This term is research-local and unratified.


## Four-delay residue alphabet

Let

h=log(81/80),
k=5h+kappa,
p=8h+rho,

with 0<kappa,rho<h.

In the repaired four-delay transfer, any connected directed dependency component contains at most two k-moves and at most one one-way p-relay move. Therefore its base arguments occupy only the ten h-residue classes

m kappa + epsilon rho mod h,

m in {-2,-1,0,1,2},
epsilon in {0,1}.

This set is the **four-delay residue alphabet**.

Its ten elements are distinct. Their order on [0,h) is

0,
rho-2kappa,
kappa,
rho-kappa,
2kappa,
rho,
-2kappa,
rho+kappa,
-kappa,
rho+2kappa

with negative entries understood modulo h.

The ordering can be certified without transcendental comparison by exponentiating: exp(h), exp(kappa), and exp(rho) are rational numbers, so every residue-order comparison reduces to an integer/rational inequality.

This term is research-local and unratified. It is a per-dependency-component alphabet; it does not assert that the full function space decomposes into ten global residue classes.


## Provenance-labeled residue state

In the four-delay residue alphabet, a residue coordinate must retain its path label

(m, epsilon),

with m in {-2,-1,0,1,2} recording net k-sheet displacement and epsilon in {0,1} recording whether the one-way p-relay has been used.

The **provenance-labeled residue state** is the pair consisting of the geometric h-residue and this label. Shift transitions are permitted only when the path budget allows them:

- h-shift: (m,epsilon) -> (m,epsilon);
- +k: (m,epsilon) -> (m+1,epsilon) only for m<2;
- -k: (m,epsilon) -> (m-1,epsilon) only for m>-2;
- +p: (m,0) -> (m,1);
- no +p transition from epsilon=1.

This label is load-bearing for matrix generation. Treating the ten residues as unlabeled points can create spurious third k-moves or repeated p-relays and therefore a false enlarged matrix.

This term is research-local and unratified.


## Causal certificate subsystem

A **causal certificate subsystem** is a provenance-respecting subset of the exact four-delay row equations, chosen so that every retained row is closed on a finite directed state alphabet and is used only on the domain where it was proved.

Crucially, if one term of an exact row would leave the finite provenance budget, the term may not be discarded. The entire row must be omitted from that certificate subsystem. Every actual prime-silent source still satisfies every retained row, so full column rank of the subsystem is sufficient for injectivity of the actual source problem.

This differs from a complete constraint matrix. The ten-symbol four-delay residue alphabet is not closed under all exact rows; it is only a candidate state alphabet for a directed causal certificate after row selection.

This term is research-local and unratified.


## Sliding k-window

In the four-delay chamber, the **sliding k-window** at base coordinate x is the physically present local stack

V(x), V(x+k), V(x+2k),

with absent translates deleted by support.

Because u<3k, at most three consecutive k-translates can occur in one local window. The labels m=-2,...,2 used in residue bookkeeping describe possible relative displacements across different causal paths; they are not five simultaneous sheet coordinates and must not all be initialized as free entrance data.

When the causal predecessor y-k is followed, the base of the sliding k-window moves backward by k. The new window overlaps the old one but is not represented by adding a permanent m=-1 sheet to the same local stack.

This term is research-local and unratified. It replaces the unsafe interpretation of the four-delay residue alphabet as a fixed global column set.


## Irrational sliding-window cocycle

Set
h=log(81/80),
k=log(16/15),
p=log(10/9).

In the basis (log2,log3,log5), their exponent vectors are
h=(-4,4,-1),
k=(4,-1,-1),
p=(1,-2,1).

The determinant of this integer matrix is -1, so h,k,p are Q-linearly independent.

The **irrational sliding-window cocycle** is the global exact-row system obtained by moving the finite local k-window through the compact equations. Although only at most three consecutive k-translates coexist locally, the window base drifts through an infinite dense residue orbit. Therefore finite local window width does not imply finite global residue closure.

This term is research-local and unratified.


## Dynamic ejection observability

Let V be a finite-dimensional subspace of the regular kernel K_c, let T be a one-sided truncated translation T_{ell,c} with 0<ell<=log2, and let Pi_V be the orthogonal projection onto V.

Define

A = Pi_V T|_V,

E = (I-Pi_V) T|_V.

The pair (A,E) has **dynamic ejection observability** if

intersection_{m=0}^{d-1} ker(E A^m) = {0},

where d=dim V.

This property holds for every nonzero V subset K_c. If a nonzero vector were annihilated by E A^m for m=0,...,d-1, Cayley-Hamilton would extend the vanishing to every m>=0, and the cyclic span generated by A would become a nonzero T-invariant subspace of K_c, contradicting the no-raw-descent theorem.

For a prime-silent regular-kernel branch V=K_c^{ps}, the prime translation equation forces the dynamically observable first-prime ejection to be reproduced exactly by the weighted compensator ejections from the opposite first-prime direction and the other active prime delays.

This term is research-local and unratified.


## Symmetrized ejection

Let R be reflection of the source interval, let V_epsilon be a parity subspace of a reflection-invariant regular-kernel branch, and let Pi_epsilon be the orthogonal projection onto V_epsilon. For an active delay lambda define

C_lambda = S_lambda^+ + S_lambda^-,

and the **symmetrized ejection**

Ecal_lambda
=
(I-Pi_epsilon) C_lambda|_{V_epsilon}.

If f has parity epsilon, then the oriented ejections satisfy

E_{lambda,-} f
=
epsilon R E_{lambda,+} f,

so

Ecal_lambda f
=
E_{lambda,+}f+E_{lambda,-}f
=
2 P_epsilon E_{lambda,+}f.

Thus the opposite-parity component of the one-sided ejection cancels within the same plus/minus prime pair and is invisible to prime silence.

This term is research-local and unratified.

## Dyadic prime reduction

Let a=log2 and

D_a
=
P_(0,a)
+
P_(L-a,L)

be the sum of the two boundary-strip multiplication projections in right-oriented source coordinates.

For the symmetric first-prime shift

C_a=S_a^+ + S_a^-,

the exact truncated-shift identity is

C_(2a)
=
C_a^2
-
2I
+
D_a.

Since log4=2a, the four-delay prime-silent equation is equivalently

gamma C_a^2
+
C_a
+
beta C_(log3)
+
delta C_(log5)
+
gamma D_a
-
2 gamma I
=
0.

This is the **dyadic prime reduction**. It shows that the log4 channel is a polynomial recurrence of the log2 channel plus an explicit boundary correction, not an independent compensator direction.

This term is research-local and unratified.


## Symmetric first-prime observability

Let a=log2 and C_a=S_a^+ + S_a^- on L2(0,L). In the four-delay chamber log5<L<=log6, one has 2a<L<3a. Fiber decomposition modulo a shows

spec(C_a)={sqrt(2),0,-sqrt(2),1,-1}.

The four-delay prime-silent equation excludes a nonzero eigenvector of C_a at each of these five eigenvalues. Therefore, for every finite-dimensional V subset ker(P_c), if Pi_V is orthogonal projection, B=Pi_V C_a|_V, and Ecal=(I-Pi_V)C_a|_V, then

intersection_{m=0}^{dim(V)-1} ker(Ecal B^m)={0}.

This property is **symmetric first-prime observability**. It is the prime-pair analogue of dynamic one-sided ejection observability and is directly visible to the symmetric prime-silent equation.

This term is research-local and unratified.


## Nondyadic edge operator

In the four-delay chamber let

b=log3,
d=log5,

and define the weighted **nondyadic edge operator**

N
=
beta C_b
+
delta C_d,

where C_lambda=S_lambda^+ + S_lambda^-.

Because b,d>L/2, both C_b and C_d are two-edge partial swaps. Writing

r=d-b=log(5/3),
w_b=L-b=r+(L-d),

the b-edge coordinate interval has length w_b<2r. In the decomposition into left/right b-edge blocks,

C_b=[[0,I],[I,0]],

C_d=[[0,T],[T^*,0]],

where T is the truncated left shift by r on L2(0,w_b) and T^2=0.

Hence

N=[[0,beta I+delta T],[beta I+delta T^*,0]]

on the b-edge space and N=0 on the central gap.

Its spectrum is

{0, +-beta, +-sigma_+, +-sigma_-},

where sigma_+^2 and sigma_-^2 are the two roots of

x^2-(2 beta^2+delta^2)x+beta^4=0.

Equivalently N satisfies the degree-seven polynomial

z(z^2-beta^2)(z^4-(2 beta^2+delta^2)z^2+beta^4)=0.

This term is research-local and unratified.


## Seven-step spectral ejection

In the four-delay chamber split the normalized prime operator as

P_c/A2 = D + N,

with

D = C_(log2) + gamma C_(log4),

N = beta C_(log3) + delta C_(log5).

The dyadic block satisfies

p_D(D)=0,

p_D(z)=(z^2-1)(z+gamma)(z^2-gamma z-2),

while the nondyadic edge operator satisfies

p_N(N)=0,

p_N(z)=z(z^2-beta^2)(z^4-(2 beta^2+delta^2)z^2+beta^4).

The root sets of p_D(z) and p_N(-z) are disjoint for the exact Weil weights.

For any closed subspace V subset ker(P_c), let Pi be orthogonal projection onto V and define

B=Pi D|_V,
F=(I-Pi)D|_V.

Since N|_V=-D|_V, its compression/ejection are -B and -F.

The **seven-step spectral ejection** property is

intersection_{m=0}^6 ker(F B^m)={0}.

It follows from the two incompatible annihilating polynomials: vanishing of F B^m through m=6 makes D^j and N^j agree with B^j and (-B)^j through the required polynomial degrees, forcing both p_D(B) and p_N(-B) to annihilate the vector; Bezout then forces the vector to be zero.

A quantitative seven-step lower bound follows with a constant depending only on the fixed Weil weights, not on dim(V).

This term is research-local and unratified.


## Two-stage nonkernel escape detector

In the four-delay chamber let a=log2, let K=K_c be the regular screw kernel, and let Q_K=I-Pi_K.

Because 2a<L<3a, the truncated one-sided first-prime shift T=S_a^+ satisfies T^3=0.

The **two-stage nonkernel escape detector** on K is

J_K g
=
(
Q_K T g,
Q_K T^2 g
).

It is injective on K. Indeed, if both components vanish, then Tg and T^2g lie in K. Since T^3g=0 and K intersects ker(T) trivially by the no-raw-descent theorem, backward induction gives T^2g=0, Tg=0, and g=0.

Since K is finite dimensional, there is a fixed constant nu_K>0 such that

||Q_K T g||^2 + ||Q_K T^2 g||^2
>=
nu_K^2 ||g||^2

for all g in K.

When combined with the seven-step spectral ejection F=H+M on a prime-silent regular-kernel branch, this yields a 21-channel detector landing entirely in K^perp:

- 7 primary nonkernel channels M B^m;
- 14 secondary channels Q_K T^j H B^m, j=1,2.

This term is research-local and unratified.


## Arithmetic field-return detector

Let V=K_c^{ps} in the four-delay chamber and let L_1,...,L_21:V->K_c^perp be the 21 nonkernel escape channels from the two-stage spectral escape theorem. Set

W_NK = sum_i Ran(L_i),

Y = G_c(W_NK) subset H^1(-c,c).

The **arithmetic field-return detector** is a finite set of reachable arithmetic centers x_1,...,x_M such that point evaluation on Y at those centers is injective.

Such a finite set exists because:
- Y is finite dimensional;
- H^1(-c,c) functions have continuous representatives;
- reachable arithmetic centers are dense once the log2 and log3 prime bases are active;
- a continuous field vanishing on that dense set is zero;
- finite dimensionality extracts finitely many evaluations.

Consequently there are constants epsilon_0>0 and c_ret>0 such that, for every f in V and 0<epsilon<epsilon_0,

sum_{i=1}^{21} sum_{j=1}^M
|| G_c L_i f ||^2_{L^2((x_j-epsilon,x_j+epsilon) intersect (-c,c))}
>=
c_ret epsilon ||f||^2.

This is a shrinking-scale interior-field estimate. It does not place the centers at the physical edge or at the canonical singular set Sigma_c, and therefore is not yet a shrinking-collar coercivity theorem.

This term is research-local and unratified.


## Field transport cocycle

For a zero-extended source w and a one-sided truncated translation T_{ell,+}, the screw potential satisfies the global identity

F_{T_{ell,+}w}(x)
=
F_w(x-ell)
-
B_{ell,+}w(x),

where B_{ell,+}w is the screw potential generated by the boundary strip discarded by the translation.

Iterating this identity along a finite arithmetic translation word transports an interior field sample by the net word displacement, but produces a finite sum of transported boundary-strip potentials. This finite correction family is the **field transport cocycle**.

For nonkernel escape fields, arithmetic recentering therefore does not preserve the finite H1 field family: it reintroduces L2 boundary-strip source carriers at every step.

This term is research-local and unratified.

## Finite edge Runge gate

Let W be a finite-dimensional subspace of K_c^perp and let U be a prescribed open subset of (-c,c). The **finite edge Runge gate** for (W,U) is the injectivity condition

w in W and (G_c w)|_U=0
implies
w=0.

By self-adjointness of G_c, this is equivalent to

W intersect
[
G_c(L2(U))
]^perp
=
{0},

where L2(U) is embedded by zero extension into L2(-c,c).

If the gate holds, finite dimensionality extracts finitely many test functions supported in U that separate W, and the H1 regularity of G_c(W) gives a quantitative local observation. The current arithmetic field-return theorem proves this gate only for an adaptively chosen finite collection of interior point neighborhoods, not for the physical edge or the prescribed singular-site neighborhoods.

This term is research-local and unratified.


## Arithmetic transport holonomy

In the four-delay chamber let

D=C_(log2)+gamma C_(log4),

N=beta C_(log3)+delta C_(log5),

and define the **arithmetic transport holonomy**

Hhol=[D,N]=DN-ND.

Whole-line translations commute, so Hhol is produced entirely by support-truncation boundary commutators. Same-orientation truncated shifts commute exactly; only opposite-orientation pairs contribute.

For 0<x<y<L, with L_x=S_x^+ and R_y=S_y^-,

[L_x,R_y]f(s)
=
[
1_(y-x,L-x)(s)
-
1_(y,L)(s)
]
f(s-(y-x)),

and

[R_x,L_y]f(s)
=
[
1_(x,L-y+x)(s)
-
1_(0,L-y)(s)
]
f(s+(y-x)),

with empty intervals omitted. The x>y case follows by antisymmetry.

Thus Hhol is a finite sum of translated source restrictions to cells whose endpoints are arithmetic edge/ratio locations such as log(3/2), log(4/3), log(5/2), and log(5/4), together with reflected support endpoints.

This term is research-local and unratified.

## Six-step holonomy observability

Let Z=ker(D+N), the ambient four-delay prime-silent space. The dyadic and nondyadic blocks satisfy relatively prime annihilating polynomials p_D(D)=0 and p_N(N)=0 from the seven-step spectral separation theorem.

For f in Z, define Hhol=[D,N]. Then there exists a constant c_hol>0 depending only on the four fixed Weil weights such that

(
sum_{m=0}^5
|| Hhol D^m f ||^2
)^(1/2)
>=
c_hol ||f||.

In particular,

intersection_{m=0}^5
ker(Hhol D^m|_Z)
=
{0}.

The proof uses the recursion comparing N^j f with (-D)^j f. Every discrepancy is controlled by Hhol D^m f; the nondyadic annihilating polynomial therefore yields p_N(-D)f as a bounded linear combination of the six holonomy channels. Bezout with p_D then recovers f.

This term is research-local and unratified.


## Holonomy boundary atlas

In the four-delay chamber, for each ordered pair 0<x<y<L with x+y>=L, the symmetric-shift commutator has the exact form

[C_x,C_y]f(s)
=
1_(y-x,L-x)(s) f(s-(y-x))
-
1_(y,L)(s) f(s-(y-x))
+
1_(x,x+L-y)(s) f(s+(y-x))
-
1_(0,L-y)(s) f(s+(y-x)).

Its only cell boundaries are

0, L, x, y, y-x

and their reflected points

L-x, L-y, L-(y-x).

For the four commutators comprising the arithmetic transport holonomy [D,N], the union of these boundaries is the **holonomy boundary atlas** Xi_L. It consists of:
- the physical source endpoints 0,L;
- the active prime-power delays log2, log3, log4, log5 and their reflections;
- the ratio gaps log(3/2), log(5/2), log(4/3), log(5/4) and their reflections.

Thus Xi_L equals the canonical edge/prime singular geometry plus one finite off-hinge ratio layer.

This term is research-local and unratified.

## Holonomy interior core

Let V be a finite-dimensional subspace of the four-delay prime-silent space, let Hhol=[D,N], and let Xi_L be the holonomy boundary atlas.

For N>=0 define the joint boundary-flatness subspace by requiring every channel

Hhol D^m f,  m=0,...,5,

to have L2 mass o(epsilon^N) in the epsilon-neighborhood of every point of Xi_L.

The descending chain stabilizes. Its terminal all-orders-flat subspace is the **holonomy interior core**.

On a nonzero holonomy interior core, six-step holonomy observability forces a uniform fixed amount of the holonomy-channel mass to remain in the interiors of the finitely many Xi_L-cells after sufficiently small boundary neighborhoods are removed.

The existence of this interior-core alternative shows that cell-boundary flatness alone does not close the holonomy detector. Eliminating the core requires a Weil-specific local range/unique-continuation statement for the associated nonkernel fields, or an equivalent cell-interior rigidity theorem.

This term is research-local and unratified.


## Holonomy orbit recustody

Let V=K_c^{ps} and decompose the dyadic block D relative to

L2(0,L)=V direct_sum V^perp

as

D=[[B,C],[F,E]].

For m>=0 define

A_m = Pi_V D^m|_V,

R_m = (I-Pi_V) D^m|_V.

Then

D^m|_V=A_m+R_m,

with A_m(V) subset V, and

A_(m+1)=B A_m + C R_m,

R_(m+1)=F A_m + E R_m.

Hence

R_m
=
sum_(j=0)^(m-1)
E^(m-1-j) F A_j.

The **holonomy orbit recustody** is the decomposition of each ambient holonomy channel

Hhol D^m|_V

into

Hhol A_m
+
Hhol R_m,

where the first term is generated by a genuine prime-silent regular-kernel vector and the second belongs to a finite ejection-word space containing at least one F.

For m<=5 this gives a finite exact recustody of the entire six-step holonomy orbit.

This term is research-local and unratified.

## Recustodied holonomy detector

Let K=K_c, Q_K=I-Pi_K, T=S_(log2)^+, and let

R_m=H_m+N_m

be the orthogonal split of the recustody error into

H_m=Pi_K R_m in K,
N_m=Q_K R_m in K^perp.

For m=1,...,5 define the 15-channel nonkernel error detector

O_ej
=
(
N_m,
Q_K T H_m,
Q_K T^2 H_m
)_(m=1,...,5).

Let

O_cus
=
(
Hhol A_m
)_(m=0,...,5)

be the six kernel-custodied holonomy channels.

The **recustodied holonomy detector** is

O_rec=(O_cus,O_ej).

Using six-step holonomy observability, boundedness of Hhol, and the two-stage nonkernel escape estimate on K, there is c_rec>0 such that

||O_rec f||
>=
c_rec ||f||

for every f in V.

Thus every nonzero prime-silent regular-kernel vector is detected either through holonomy of genuine kernel-custodied orbit vectors or through a finite K^perp ejection family. No ambient D^m source needs to be treated as a kernel vector.

This term is research-local and unratified.


## Dyadic spectral shadow

In the four-delay chamber let D=C_(log2)+gamma C_(log4), let V=K_c^{ps}, and let Pi_V be orthogonal projection onto V. Let

D = sum_{lambda in spec(D)} lambda P_lambda

be the ambient spectral decomposition of the finite-spectrum self-adjoint dyadic block.

For each dyadic eigenvalue lambda define the **dyadic spectral shadow**

S_lambda
=
Pi_V P_lambda|_V.

Then every S_lambda is positive semidefinite and self-adjoint on V,

sum_lambda S_lambda=I_V,

and for

A_m=Pi_V D^m|_V

one has

A_m
=
sum_lambda lambda^m S_lambda.

Because the five dyadic eigenvalues are distinct, the first five A_m are related to the five shadows by an invertible Vandermonde transform. The sixth source A_5 is constrained by the ambient annihilating polynomial p_D(D)=0 and adds no independent spectral shadow.

This term is research-local and unratified.

## Spectral-shadow diagonal hard core

Let W_diag be a finite-center all-orders-superflat diagonal subspace inside V, for example the stabilized hard branch of the selected movable-center Suzuki diagonal observations.

The **spectral-shadow diagonal hard core** is

W_sh
=
{ f in V : S_lambda f in W_diag for every lambda in spec(D) }.

Equivalently, by Vandermonde inversion,

f in W_sh

iff

A_m f in W_diag for m=0,...,4.

On W_sh, every recustodied source in the entire projected dyadic moment sequence A_m f has the same diagonal-superflat property, because the A_m satisfy the exact recurrence p_D in m.

Current results do not force W_sh=0. The exact full-Suzuki local flat-profile space is infinite dimensional, so finite source multiplicity and the five-shadow Vandermonde structure alone do not supply local quasi-analytic rigidity.

This term is research-local and unratified.


## Spectral-shadow ejection detector

Let V=K_c^{ps}, let D be the dyadic finite-spectrum block, and let P_lambda be its ambient spectral projections. Define

S_lambda=Pi_V P_lambda|_V,

J_lambda=(I-Pi_V)P_lambda|_V.

The family (J_lambda)_lambda is the **spectral-shadow ejection detector**.

For every lambda,

ker(J_lambda)=ker(P_lambda|_V)=ker(S_lambda).

Indeed, if J_lambda f=0 then P_lambda f=S_lambda f lies in V and is a D-eigenvector. The four-delay prime-silent space contains no nonzero D-eigenvector, so P_lambda f=0. The converse is immediate.

Since sum_lambda P_lambda=I, the joint map

J_sh: f -> (J_lambda f)_lambda

is injective on V. Finite dimensionality gives a constant nu_sh(V)>0 with

sum_lambda ||J_lambda f||^2
>=
nu_sh(V)^2 ||f||^2.

Each P_lambda is a polynomial in D of degree at most four, so every J_lambda lies in the finite recustody-error space generated by R_1,...,R_4.

After splitting each J_lambda into its K_c and K_c^perp parts and applying the two-stage nonkernel escape detector to the K_c part, one obtains fifteen K_c^perp channels that are jointly injective on V.

This term is research-local and unratified.


## Dyadic eigenspace edge flexibility

In the four-delay chamber let D=C_(log2)+gamma C_(log4), and let E_lambda=ker(D-lambda I) be one of its five ambient eigenspaces.

The **dyadic eigenspace edge-flexibility** property is the existence, for every lambda in spec(D), of a sufficiently small two-sided physical edge neighborhood U_epsilon and an infinite-dimensional subspace

E_lambda^edge
subset
E_lambda intersect L0^2(0,L)

such that

(G_c w)|_(U_epsilon)=0

for every w in E_lambda^edge.

For lambda=+-1 this follows from the two-chain fiber profile and a local second-kind equation at the log3 sample. For the three-chain eigenvalues it follows after choosing the free profile to vanish near the two source endpoints and solving local second-kind equations at the log(5/4) and L-log5 profile points. The remaining slope/centering/mean-zero conditions are finitely many scalar constraints on an infinite-dimensional far-profile space.

Thus the explicit dyadic eigenpattern alone cannot prove the spectral-shadow finite edge Runge gate.

This term is research-local and unratified.

## Kernel-generated spectral-shadow edge gate

Let V=K_c^{ps}, let P_lambda be the ambient dyadic spectral projections, and let U be a prescribed physical edge or Sigma_c neighborhood.

The **kernel-generated spectral-shadow edge gate** is the joint injectivity statement

f in V,
(G_c P_lambda f)|_U=0 for every lambda
implies
f=0,

possibly augmented by the secondary two-stage escape fields arising from the K_c-valued portions of (I-Pi_V)P_lambda f.

Dyadic eigenspace edge flexibility shows that this gate cannot follow from D-eigenstructure alone. A proof must use the fact that all five spectral pieces arise simultaneously from one f satisfying both

G_c f=0

and

(D+N)f=0.

This term is research-local and unratified.


## Four-field shadow commutator basis

Let V=K_c^{ps}, let D be the dyadic finite-spectrum block with spectral projections P_lambda, and let G_c be the regular screw operator.

For f in V, G_c f=0. Since every P_lambda is a degree-at-most-four polynomial

P_lambda=q_lambda(D)=sum_(j=0)^4 q_(lambda,j) D^j,

the five spectral-shadow fields satisfy

G_c P_lambda f
=
sum_(j=1)^4
q_(lambda,j) G_c D^j f.

Conversely,

G_c D^j f
=
sum_lambda
lambda^j G_c P_lambda f,
j=1,...,4.

The 5-by-4 coefficient matrix (q_(lambda,j)) has rank four, because the five Lagrange polynomials q_lambda form a basis of the degree-at-most-four polynomial space and sum_lambda q_lambda=1.

Thus the five shadow fields have exactly four independent operator directions. The family

K_j f:=G_c D^j f,
j=1,...,4,

is the **four-field shadow commutator basis**.

For every open set U,

(G_c P_lambda f)|_U=0 for every lambda

iff

(K_j f)|_U=0 for j=1,...,4.

This term is research-local and unratified.

## Twelve-channel shadow recustody

For j=1,...,4 write the exact recustody split

D^j f
=
A_j f
+
R_j f,

with A_j f in V and R_j f in V^perp.

Further split

R_j f
=
H_j f
+
N_j f,

where

H_j f=Pi_K R_j f in K_c,

N_j f=Q_K R_j f in K_c^perp.

Since G_c A_j f=G_c H_j f=0,

G_c D^j f
=
G_c N_j f.

The **twelve-channel shadow recustody** is the K_c^perp family

N_j f,
Q_K T H_j f,
Q_K T^2 H_j f,
j=1,...,4,

with T=S_(log2)^+.

The fifteen spectral-shadow escape channels of GERM-57 are fixed rank-four linear combinations of these twelve channels. Hence the twelve-channel family is jointly injective on V and has a positive finite-dimensional norm floor.

This term is research-local and unratified.


## Prime-silent edge inverse system

In the four-delay chamber let

D=C_(log2)+gamma C_(log4),
N=beta C_(log3)+delta C_(log5),

so the ambient prime-silent equation is

(D+N)f=0.

Since 0 is not in spec(D), D is invertible. Define the edge source

h=Df=-Nf.

Because log3 and log5 exceed L/2, Nf is supported on the two log3-edge blocks

(0,L-log3) union (log3,L).

The **prime-silent edge inverse system** is the closed functional equation on this edge-supported h obtained by writing

f=D^{-1}h

fiberwise in the log2 residue decomposition and substituting into

h=-Nf.

It is exactly equivalent to the ambient four-delay prime-silent equation.

This term is research-local and unratified.

## Parity edge recurrence

Let a=log2, b=log3, d=log5 and define

R=d-b=log(5/3),
r=b-a=log(3/2),
q=2a-b=log(4/3),
s=d-2a=log(5/4),
p=R-r=log(10/9),
u=L-d,
w=R+u,
omega=s+u,
v=p+u.

For an edge source h define

x(t)=h(t),
z(t)=h(b+t),
0<t<w.

The exact edge inverse system reduces on a reflection-parity sector epsilon in {+1,-1} by

z(t)=epsilon x(w-t).

The resulting single-profile **parity edge recurrence** is

x(t)
+ beta x(r+t)
+ delta gamma [x(s+t)-epsilon x(u-t)]
=0,
0<t<u;

x(t)+beta x(r+t)=0,
u<t<v;

x(t)=0,
v<t<q;

x(t)
+ beta gamma [x(t-q)-epsilon x(w-t)]
=0,
q<t<w.

Conversely every L2 solution x of this system reconstructs a parity prime-silent source f=D^{-1}h.

Thus ambient four-delay prime-silent injectivity is equivalent to triviality of the two parity edge recurrences.

This term is research-local and unratified.


## Parity tail Schur reduction

In the post-log(16/3) four-delay chamber, let

c=beta gamma,
Delta_c=1-c^2>0,

and let x be one parity profile from the parity edge recurrence with sign epsilon.

For the tail variable

T(y)=x(q+y),

0<y<omega=q+e,

the final parity equation can be solved exactly.

For 0<y<e,

T(y)
=
-(c/Delta_c)
[
x(y)+c epsilon x(e-y)
].

For e<y<q,

T(y)
=
-c
[
x(y)-epsilon x(q+e-y)
].

For 0<z<e,

T(q+z)
=
(c/Delta_c)
[
c x(z)+epsilon x(e-z)
].

The **parity tail Schur reduction** is the elimination of every x-coordinate above q by these three formulas. It reduces the scalar recurrence to the base interval (0,q) with one forced zero strip (v,q).

This term is research-local and unratified.

## Low-head return cocycle

Let

h=log(81/80),
k=log(16/15),

and

kappa=k-5h.

In the exact incidence graph of the parity edge recurrence:

- translation by +h is admissible on (0,u-h), with inverse -h on (h,u);
- translation by +k is admissible from (0,e) to (k,u), with inverse -k;
- therefore the composite +k followed by five -h steps gives a return by

kappa=k-5h

on (0,e-kappa), with inverse return -kappa on (kappa,e).

The number kappa is positive because

16*80^5-15*81^5=127033985>0.

Moreover h/kappa is irrational: in the prime-log basis (log2,log3,log5),

h=(-4,4,-1),

kappa=(24,-21,4),

and no nonzero rational proportionality is possible.

The resulting partial action on the lower defect is the **low-head return cocycle**.

For e>h both h- and kappa-returns are simultaneously internal to the lower defect on nonempty subintervals. Consequently no finite periodic residue lattice can be invariant under the exact return geometry. This blocks a chamber-independent reduction to one finite constant matrix indexed by a common arithmetic mesh.

This term is research-local and unratified.


## First-return-free parity chamber

Let

kappa = k-5h
=
log[(16/15)(80/81)^5]
>0,

with

h=log(81/80),
k=log(16/15).

The **first-return-free parity chamber** is

0<e<=kappa,

for the post-log(16/3) parity edge recurrence.

In this chamber, after exact tail Schur elimination, a generic recurrence orbit meets the lower defect (0,e) only in one reflection pair

{t,e-t}.

No nonzero translated lower-defect return is admissible.

Consequently every generic orbit has one constant coefficient template, independent of e and of the seed t up to relabeling. The template has 124 source coordinates and 124 recurrence rows for either parity sign.

The exceptional seeds that hit recurrence boundaries form a finite union of affine points and are null for the L2 problem.

This term is research-local and unratified.
