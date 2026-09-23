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
