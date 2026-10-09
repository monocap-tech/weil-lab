# RPB108 CC44 — Scalar pole susceptibility leaves an invisible kernel

Date: 2026-10-09 UTC. Publication base c8cb8ec3e0cc2b8eae83afc328595ff84f2c1793.
[Definitions](../docs/TERMINOLOGY_RPB108_INVISIBLE_KERNEL_CC44.md).
Dependencies: CC40 susceptibility, CC41 supported operators, CC43 native
pole-free ground state. Concurrent NF14 finite E48/E64 handoff is preserved.

## 1. A nonzero pole moment at a pole-free zero is incompatible with positivity

Work in the actual even sector. Suppose Q>=0 and the pole-free H has
ground eigenvector g of physical norm one, eigenvalue -kappa<0.
CC43 gives a simple nonnegative even g, and alpha=c(g)>0. There is at
most one negative H eigenvalue. If Hz=0, the Q form Gram on g,z is

    [[-kappa+2alpha^2, 2alpha c(z)],
     [2alpha c(z), 2c(z)^2]].

Its determinant is -2kappa c(z)^2. Nonnegative Q forces c(z)=0.
This applies to every real zero vector; real and imaginary parts give
the complex assertion. Thus ker H is contained in ker c, and all its
vectors are original Q nulls. Ground-state simplicity has not excluded
any of them. A proposed proof that every higher zero mode has nonzero
moment would exclude contact only by contradicting original positivity;
it is not an extra property one may assume at contact.

In the odd sector Q=H-2s^2>=0 implies H>=0. For Hz=0, testing z gives
0<=Q(z)=-2s(z)^2, so s(z)=0 and z is again a Q null.

## 2. Exact even Schur test, including its singular channel

Decompose h=tg+v with v physically orthogonal to g. Put K=H restricted
to g-perp, ell(v)=c(v), and d=2alpha^2-kappa. K is a nonnegative closed
form with compact-resolvent realization. On its form domain,

    Q(tg+v)=d(t+2alpha ell(v)/d)^2
             +K(v)-2kappa ell(v)^2/d,       when d>0. (1)

Define T=sup ell(v)^2/K(v), with the extended convention in the registry.
Then Q>=0 is equivalent to

    K>=0, d>0, T<=d/(2kappa),                (2)

within the d>0 case. No inverse of K is used. If K has a kernel, finite T
forces ell to vanish on it; that kernel is invisible to the moment test.
If 2kappa T/d<1, the second term in (1) is at least
(1-2kappa T/d)K(v). Consequently the original null space is EXACTLY
ker K, even with a strict scalar susceptibility reserve. Strict positivity
additionally requires ker K=0. Compact resolvent then gives a positive
physical gap for each fixed cap, but not a computed or cap-uniform gap.

Boundary cases are explicit: d<0 gives a negative ground trial. If d=0,
nonnegative Q requires ell identically zero, since its cross term with t
otherwise has both signs. With ell=0, Q(tg+v)=K(v); g is a moment-carrying
Q null and ker K remains an independent invisible null channel.

In the odd sector, define T_o=sup s(v)^2/H(v). Nonnegative odd Q is equivalent to
H>=0 and 2T_o<=1, with the same extended convention. If 2T_o<1,
Q>= (1-2T_o)H, but ker Q=ker H may still be nonzero. Thus both actual
pole signs leave a channel unobserved by strict scalar reserves.

## 3. A complete favorable-sign control with strict reserve and a higher null

In R^3 set g0=(1,1,1), z=(1,-1,0), w=(1,1,-2), and

    H=-g0 g0^T/3+w w^T/6,
    c(x)=(g0+r w)^T x, Q=H+2c c^T.

H has eigenvalues -1,0,1 on g0,z,w respectively. All three off-diagonal
entries are strictly negative; its ground profile is simple and positive.
For 0<r<1/2 the moment profile is positive in every coordinate.
Here alpha^2=3, d=5, T=6r^2. At r=1/10, the scalar ratio
2kappa T/d=3/125<1, yet Hz=0, c(z)=0 and Qz=0.
The validator tests r=1/20,1/10,1/5 with exact fractions, all principal
minors of Q, the complete sign pattern, all three H eigenrelations,
and the Schur identity on three test vectors. These controls retain a
nonzero higher-mode moment coupling as well as the invisible zero mode.
All 57 new exact checks pass; no historical chain total is added.
They are not models satisfying the complete original Weil identities.

Positive-level control: on the w direction H(w)=||w||^2, so subtracting
physical mass with mu=1 makes w a pole-free shifted null. Its moment
is 6r, nonzero for these tests. The full shifted original form there is
Q(w)-||w||^2=72r^2>0. Removing the poles or shifting the level changes
null classification; that positive eigenmode is not an original null.

The existing genuine-crossing control remains compatible: scalar reserves
are not an all-cap continuation theorem, and no quantitative outward
correlation gain is deduced from (1).

## 4. What arithmetic estimate remains necessary for this route

At a hypothetical nonnegative contact, positivity itself makes every
pole-free zero mode invisible. The missing estimate cannot be replaced
by stricter scalar pole susceptibility or by ground-state positivity.
For this route a sufficient additional estimate is, on each fixed finite
cap, H(v)>=gamma_a ||v||_2^2 for all moment-zero v, gamma_a>0, together
with strict scalar reserves in the applicable sector. In the even d>0
decomposition this excludes ker K; in the odd sector it excludes ker H.
This is a sufficient estimate, not asserted to be the minimal all-cap
source-shell correlation estimate or equivalent to its defect-relative rate.

No such actual arithmetic floor has been certified here. The rational
control proves precisely the failure of the scalar/sign-structure inference,
not logical insufficiency of the complete Weil identities. The original
old-gap-independent collective source-shell bound, contact exclusion,
RH/F4 and Lean closure remain open. The positive whole-domain anchor
remains 21/20 with physical margin 1/(3*10^63). Finite E64 and F112
certificates still require their intervening and mixed Schur control.
