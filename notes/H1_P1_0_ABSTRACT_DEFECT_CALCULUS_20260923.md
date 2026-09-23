# H1-P1.0 — Abstract Defect Calculus
Date: 2026-09-23

## Determination

The first Horizon-1 abstraction pass closes successfully.

Starting from two bounded synthesis maps

\[
S_+:K_+\to\mathcal H,
\qquad
S_-:K_-\to\mathcal H,
\]

and

\[
E(x,u)=S_+x+S_-u,
\]

the entire sign problem on

\[
\mathcal A=(\ker E)^\perp
\]

is governed by

\[
\boxed{
D=S_+S_+^*-S_-S_-^*.
}
\]

For every \(h\),

\[
[E^*h,E^*h]_J
=
\langle Dh,h\rangle.
\]

Hence

\[
\boxed{
\mathcal A\text{ is }J\text{-nonnegative}
\iff
D\succeq0,
}
\]

and

\[
\boxed{
\operatorname{ind}_-(\mathcal A,J)
=
\operatorname{ind}_-(D).
}
\]

Douglas factorization then gives

\[
\boxed{
D\succeq0
\iff
S_-=-S_+X
\text{ for a contraction }X.
}
\]

Under mere exact range inclusion, the reduced solution gives

\[
\boxed{
\mathcal A
=
\{(a,-X^*a):a\perp\ker S_+\}
}
\]

and

\[
[(a,-X^*a)]_J
=
\|a\|^2-\|X^*a\|^2.
\]

Thus the abstract defect problem is exactly a reduced-screening norm problem.

## New correction

The previous public map used a negative/neutral boundary dichotomy.

That is incomplete.

When

\[
\|X\|=1,
\]

the norm may fail to be attained. Then there is no nonzero neutral vector even though the positivity margin collapses to zero along an approximate-neutral sequence.

So the abstract classification is:

1. range defect;
2. over-budget negative defect;
3. strict positive screening;
4. attained neutral boundary;
5. non-attained approximate-neutral boundary.

A concrete \(L^2(0,1)\) multiplication example realizes case 5.

## Rank-one recovery

If \(K_-=\mathbb C\) and \(S_-\alpha=\alpha g\), then

\[
D
=
S_+S_+^*
-
g\otimes g.
\]

Hence the rank-one Weil defect is not a separate construction. It is the one-negative-channel specialization of the abstract calculus.

## Spectral-screening recovery

For increasing positive projections \(P_N\uparrow I\),

\[
D_N
=
S_+P_NS_+^*
-
S_-S_-^*
\]

satisfies

\[
D_N\uparrow D
\]

strongly and

\[
\operatorname{ind}_-(D_N)
\]

is nonincreasing.

The scalar example with

\[
c_j^2=\frac1{j(j+1)}
\]

gives

\[
D_N=-\frac1{N+1}
\to0,
\]

so strict finite negativity can disappear completely at the infinite limit.

## Standing

- WD-A1 defect identity / index transfer: **PROVED**;
- WD-A2 contractive screening equivalence: **PROVED using imported Douglas theorem**;
- WD-A3 graph normal form: **PROVED**;
- WD-A4 complete abstract screening morphology: **PROVED**;
- WD-A5 rank-one specialization: **PROVED**;
- WD-A6 monotone positive screening: **PROVED**;
- WD-E1 complete-screening example: **PROVED**;
- WD-E2 non-attained critical example: **PROVED**.

No zeta-specific theorem is consumed in these results.

## Next cursor

\[
\boxed{
\texttt{H1-P1.1 / RESTRICTED-CHANNEL AND FINITE-INDEX TRANSFER}
}
\]
