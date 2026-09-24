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

For Horizon 1, the principal RH-facing interfaces are:

\[
\texttt{AZ-NEXTJET-LOC},
\qquad
\texttt{C-ACTUAL-KPH-FLOOR},
\qquad
\texttt{AZ-FIN-WEIL-NULL-EXTENSION}.
\]

## Re-entry

**Re-entry** is the explicit promotion of a result from one project layer or horizon into a stronger downstream theorem line.

Re-entry requires a scope audit. It is never inferred merely because the same notation or object appears in both layers.

## Custody

**Custody** means preserving the identity, hypotheses, and scope of the mathematical object being tracked through a reduction or transfer.

A valid reduction must not silently replace a selected packet, metric, support scale, or theorem hypothesis by a weaker aggregate object.

## Screening

**Spectral screening** is the finite-to-infinite phenomenon in which a negative eigenvalue present at every finite truncation may approach the zero boundary as the positive complement is restored:

\[
\lambda^-_{N,k}<0,
\qquad
\lambda^-_{N,k}\uparrow0.
\]

It distinguishes finite negative index from infinite negative-mode survival.

## Defect

A **defect** is the residual obstruction left after the positive/background contribution has been separated from a selected negative or neutral channel.

In the rank-one formulation, a representative defect operator is

\[
\mathcal K_C(t)
=
\widetilde S_t\widetilde S_t^*
-
\widetilde g_C\otimes\widetilde g_C.
\]

The term does not by itself assert negativity.

## Negative persistence

**Negative persistence** means that after the screening limit, a selected negative-signature direction survives projectively rather than collapsing entirely into the zero boundary.

## Neutral persistence

**Neutral persistence** means that the limiting obstruction survives at zero signature as a null mode rather than as a strictly negative direction.

In the current compact-window branch this is represented by

\[
W_ck=0.
\]

## Morphology

A **defect morphology** is the exact structural form that a surviving defect must take after all completed reductions have been applied.

For Horizon 1, the two principal morphologies are:

1. weighted next-jet localization on the negative branch;
2. compact-window null-extension/support rigidity on the neutral branch.


## Synthesis pair

A **synthesis pair** is a pair of bounded operators

\[
S_+:K_+\to\mathcal H,
\qquad
S_-:K_-\to\mathcal H
\]

assembled into

\[
E(x,u)=S_+x+S_-u.
\]

The \(+\) and \(-\) labels refer to the coefficient-space indefinite signature, not to positivity of the operators themselves.

## Analysis space

The **analysis space** associated with a synthesis pair is

\[
\mathcal A=(\ker E)^\perp
=
\overline{\operatorname{Ran}E^*}.
\]

It is the coefficient space actually visible to physical synthesis.

## Physical defect operator

The **physical defect operator** is

\[
D
=
S_+S_+^*
-
S_-S_-^*
=
EJE^*.
\]

Its quadratic form exactly represents the indefinite coefficient form on vectors of the form \(E^*h\).

## Exact screening

**Exact screening** means

\[
\operatorname{Ran}S_-
\subseteq
\operatorname{Ran}S_+.
\]

Equivalently, there exists a bounded \(X\) such that

\[
S_-=-S_+X.
\]

Exact screening does not imply that the screening coefficient norm fits inside the unit budget.

## Reduced screening solution

The **reduced screening solution** is the unique Douglas reduced solution \(X\) of

\[
S_+X=-S_-
\]

whose range lies in

\[
(\ker S_+)^\perp.
\]

It is the minimum-norm canonical screening operator.

## Over-budget defect

An **over-budget defect** occurs when exact screening holds but the reduced screening solution satisfies

\[
\|X\|>1.
\]

The negative physical channel lies in the positive range, but reproducing it requires more than the unit indefinite-metric budget.

## Critical screening

**Critical screening** is the boundary case

\[
\|X\|=1.
\]

Critical screening splits into attained and non-attained cases.

## Approximate-neutral boundary

The **approximate-neutral boundary** is critical screening with

\[
\|X\|=1
\]

but no nonzero vector \(a\) satisfying

\[
\|X^*a\|=\|a\|.
\]

There is then no actual neutral vector, while normalized positive margins can still converge to zero along an approximate-neutral sequence.

This term is distinct from **neutral persistence**.


## Selected negative sector

A **selected negative sector** is a distinguished closed subspace

\[
M\subseteq K_-
\]

whose defect ownership is tracked separately from the remaining negative channels.

When \(M\) is finite dimensional, its dimension gives an upper bound on the negative index it can create by itself.

## Negative background

The **negative background** is the complementary negative channel space

\[
B=M^\perp\cap K_-.
\]

Background contributions can make a selected negative witness more negative, but aggregate negativity need not belong to the selected sector.

## Residual screening budget

If a background channel is contractively screened by \(X_B\), the **residual screening budget** is

\[
R_B=I-X_BX_B^*.
\]

It records the positive coefficient-space capacity remaining for later selected channels.

## Effective positive synthesis

The **effective positive synthesis** after background elimination is

\[
S_{\rm eff}=S_+R_B^{1/2}.
\]

It allows the selected problem to be re-entered into the same defect calculus after a legitimate background screening step.

## Shared screening budget

The **shared screening budget** principle is that negative channel blocks are jointly admissible only when their combined screening covariance fits inside the unit budget.

Separate contractivity of each block is not sufficient.

## Shorted covariance

For a positive covariance \(K\) and a selected physical subspace \(W\), the **shorted covariance** is the covariance remaining on \(W\) after the complementary physical subspace has been optimized away.

In an invertible block decomposition

\[
K=
\begin{pmatrix}
A&B\\
B^*&C
\end{pmatrix},
\]

it is

\[
H_W=A-BC^{-1}B^*.
\]

Direct compression \(A\) and shorted covariance \(H_W\) have different inverse-control meanings.

## Signature shadow

A **signature shadow** is a coordinate projection of an indefinite coefficient vector that preserves its algebraic sign margin but need not remain in the relevant analysis space.

A signature shadow is not automatically an admissible persistent vector.


## Right-limit analysis space

For a monotone analysis-space filtration

\[
\mathcal A_s\subseteq\mathcal A_t
\qquad(s<t),
\]

the **right-limit analysis space** at \(c\) is

\[
\mathcal A_{c+}
=
\bigcap_{t>c}\mathcal A_t.
\]

It contains coefficient vectors that persist at every support/observation scale immediately to the right of the endpoint.

## Endpoint jump

The **endpoint jump** is the Hilbert-space difference

\[
\mathcal J_c
=
\mathcal A_{c+}\ominus\mathcal A_c.
\]

A nonzero endpoint jump records failure of right continuity of the analysis-space filtration.

When \(\mathcal A_c\) is \(J\)-nonnegative, any new right-limit negative index must inject into the quotient

\[
\mathcal A_{c+}/\mathcal A_c.
\]

## Right-persistent vector

A **right-persistent vector** is a vector

\[
y\in\mathcal A_{c+}.
\]

It is **new at the endpoint** when

\[
y\notin\mathcal A_c.
\]

Negative and neutral persistence are sign-refined forms of this notion.

## Boundary amplification

Given a bounded physical realization

\[
\mathcal A_t
=
\overline{T(\mathscr H_t)},
\]

the **boundary amplification cost** of \(y\) is

\[
\mathfrak B_y(t,\varepsilon)
=
\inf
\left\{
\|h\|:
h\in\mathscr H_t,\ 
\|Th-y\|\le\varepsilon
\right\}.
\]

For a genuinely new endpoint vector, this cost diverges as

\[
(t,\varepsilon)\to(c+,0).
\]

## Moving-sector escape

A **moving-sector escape** occurs when the selected negative direction itself moves through an infinite coefficient space as the filtration approaches the endpoint.

This can destroy every nonzero right-limit ray even when every stage contains a finite-dimensional negative direction.

It is distinct from positive-coordinate mass loss with a fixed finite negative sector.


## Zero-side Weil representation

The **zero-side Weil representation** is the coefficient/synthesis realization of the Weil quadratic form in terms of zero channels.

Its positive coefficient sector contains critical-line coordinates and positive off-axis pair directions; its negative sector contains antisymmetric off-axis pair directions.

## Weil pair channels

For a nonreal ordinate pair

\[
\gamma=T+i\delta,
\qquad
\bar\gamma=T-i\delta,
\]

the canonical **Weil pair channels** are

\[
p
=
\frac{e_\gamma+e_{\bar\gamma}}{\sqrt2},
\qquad
n
=
\frac{e_\gamma-e_{\bar\gamma}}{\sqrt2}.
\]

They satisfy

\[
Jp=p,
\qquad
Jn=-n.
\]

The \(p\)-channel is the positive/symmetric pair direction; the \(n\)-channel is the negative/antisymmetric pair direction.

## Selected packet

A **selected packet** \(\Pi\) is a fixed finite set of off-axis zero channels whose negative sector is tracked with custody through the defect calculus.

Its selected negative coefficient space is denoted

\[
M_\Pi\subseteq K_-.
\]

## Unselected negative divisor

The **unselected negative divisor** relative to \(\Pi\) is the complementary negative coefficient sector

\[
B_\Pi=M_\Pi^\perp\cap K_-.
\]

It is the zeta-Weil realization of the abstract negative background.

## ZW-0 / ZW-1 / ZW-2

Horizon 1 uses three zeta-specialization layers:

- **ZW-0 — Weil/Krein pair geometry:** zero-side pair diagonalization, sign channels, finite index, and compact-window synthesis.
- **ZW-1 — zeta-divisor structure:** functional-equation/conjugation structure, selected packets, zero-moment residues, actual zero-count/compactness inputs.
- **ZW-2 — explicit-formula arithmetic:** prime, pole, archimedean, completed-\(\Xi\), next-jet, and finite translation structure.

These labels distinguish where arithmetic genuinely enters.

## Explicit-formula side

The **explicit-formula side** is the prime/pole/archimedean representation of the same Weil quadratic form.

It is not an additional positive screening sector and must not be added to \(K_+\) as though it supplied independent coefficient budget.


## Raw residue vector

Given a selected negative pair-coordinate vector \(u\), the **raw residue vector** \(v\) is obtained by undoing the canonical pair diagonalization back to the selected zero coordinates.

For each negative pair channel, the two raw coefficients are equal and opposite.

## Zero-moment law

The **zero-moment law** is

\[
\mathbf1^Tv=0.
\]

It is a ZW-1 structural identity coming from antisymmetry of the negative pair channels.

It is not a generic H1-P1 screening theorem and does not use the prime side of the explicit formula.

## Rational response

The **rational response** of a finite raw residue vector is

\[
R_v(z)
=
\sum_j\frac{v_j}{z-\rho_j}.
\]

Under the zero-moment law,

\[
R_v(z)=O(|z|^{-2}).
\]

The inverse-square order is the universal pair-geometric order unless additional moment cancellation is proved.

## Native Problem-1 synthesis

The **native Problem-1 synthesis** is Bombieri's Green-preconditioned zero synthesis into the Dirichlet \(H^{-1}\)-type physical carrier.

For fixed support it is Hilbert-Schmidt, hence compact.

This term distinguishes the actual Weil/Bombieri operator metric from unweighted exponential \(L^2\) models.

## Unweighted mirror model

An **unweighted mirror model** is an \(L^2/PW_t\) exponential or cosh/sinh sampling model in which the Green weights of native Problem 1 have been removed.

Frame or sampling lower bounds in this model are auxiliary harmonic-analytic statements and are not automatically native Problem-1 coercivity estimates.

## Metric separation

**Metric separation** is the rule that a theorem proved in an unweighted exponential/sampling norm may not be transferred to the native Problem-1 \(H^{-1}\) operator without an explicit bounded comparison theorem.

In particular, a stable unweighted frame does not contradict compactness of native Problem-1 synthesis.


## Selected-preserving multiplier

A **selected-preserving multiplier** for a raw residue source \(v\) is an admissible scalar multiplier \(\psi\) satisfying

\[
\mathcal C_v[\psi]=0,
\]

so the selected contracted-residue contribution is removed without discarding the complementary divisor, prime, and archimedean terms.

## Far complementary field

The **far complementary field** is the contribution of unselected zeros outside a fixed neighborhood of the selected packet:

\[
\mathcal F_{v,R}[\psi]
=
\sum_{\substack{\mu\notin F\\|\Im\mu-T_F|\ge R}}
m_\mu\psi(\mu)R_v(\mu).
\]

For a fixed bounded multiplier and a zero-moment selected source,

\[
\mathcal F_{v,R}[\psi]
=
O((\log R)/R).
\]

## Weighted next-jet field

The **weighted next-jet field** is

\[
\mathcal N_{v,R}[\psi]
=
\sum_{\mu}^{\rm near}
m_\mu\psi(\mu)
\frac{H_v^{(m_\mu)}(\mu)}
{\Xi^{(m_\mu)}(\mu)},
\qquad
H_v=\Xi R_v.
\]

It is the finite/intermediate complementary divisor object left after zero-moment far-tail localization.

## Explicit-formula co-adaptation

**Explicit-formula co-adaptation** is the phenomenon that adapting \(\psi\) to cancel one side of the scalar explicit formula changes the remaining prime/archimedean balance simultaneously.

In particular, under selected preservation, if

\[
\mathcal N_v[\psi]=\mathcal A_v[\psi],
\]

then

\[
\mathcal P_v[\psi]=\mathcal F_v[\psi].
\]

Thus adaptive near cancellation does not leave an independent prime lower bound.

## Compact-window arithmetic operator

The **compact-window arithmetic operator** at support \(c\) is the physical operator representing the geometric Weil form:

\[
\mathcal W_c
=
\mathcal A_\infty
-
\sum_{\log n<2c}
\frac{\Lambda(n)}{\sqrt n}
(\tau_{\log n}+\tau_{-\log n})
+
\mathcal R_{\rm pole},
\]

up to the fixed Fourier-normalization convention.

At fixed \(c\), the prime-translation sum is finite.

## Logarithmic form order

The **logarithmic form order** is the high-frequency asymptotic

\[
\Psi_c(t)
=
\log|t|+O_c(1).
\]

It implies that the natural form norm is equivalent, after an \(L^2\) shift, to a logarithmic Fourier/Sobolev norm rather than to a positive-order Sobolev norm.
