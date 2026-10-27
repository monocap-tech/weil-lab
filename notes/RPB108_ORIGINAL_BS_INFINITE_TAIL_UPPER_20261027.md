# Original Birman–Schwinger infinite tail and finite count upper

Weil-Lab, 2026-10-27. Continues draft #348 at
`8217c8c97520c37f7b1889da340ac13b7cff0594`. Draft/unmerged.

## Outcome and bounded stopping point

The accepted original Fourier/Hermite and SI29 reference-inverse bounds
give a quantitative upper on the COMPLETE original BS spectral tail:

    lambda_471(B)<0.00002431,
    B=Kminus^(1/2) Astar^-1 Kminus^(1/2).

An explicit exact deflation SUBSPACE is available:

    S=range(Kminus^(1/2) J470), Pi=orthogonal projection onto S,
    R=I-Pi, rank(Pi)<=470,
    0<=R B R<=t R, t=2.4301374667791075...e-5 <0.00002431.

Pi is mathematically defined, NOT numerically evaluated. Kminus^(1/2)
means the ACTUAL square root of the supported physical compressed operator.
It is not identified with compression of sqrt(r) on the frequency side.

Combined with #348's COMPLETE-operator lower lambda_4>1-3e-12,

    4 <= #{j: lambda_j(B)>1-3e-12} <=470.

This is a genuine finite upper count and strict infinite-tail bound. It is
not an exact critical count, an isolation of the four trial vectors, or
a bound <=1 on the remaining finite spectrum. The interval 4..470 is wide.
Do not call all 470 directions critical or infer that a raw 470-dimensional
inversion is required; 470 is a proved ceiling, not a minimum algorithm size.

STOP after this exact composition and GitHub replay. No inverse solve,
new native integration, full matrix assembly, evaluated BS projection or
dimension-by-dimension campaign is started. The next gate is the FULL
finite/mixed Schur comparison described below, or a sharper count upper
that legitimately reduces it. W-ODD-NEG remains OPEN.

## Matched original inherited data

Let P be the physical orthogonal projection onto ORIGINAL J470, Q=I-P.
The native J input hash is identical in the two inherited estimates:

    c9ee487f8abe7b633c47d2ef7d72e2cc4f7289bc794b2d8fc02bb61520b25e60.

The genuine pole belongs to J. No new source or endpoint-aligned surrogate
is substituted. Original B=11/10, kappa=1/1000, full seven-prime multiplier,
and inherited original operator/domain review remain unchanged.

From #345, the actual ORIGINAL SM40 envelope E40>=Kminus satisfies

    Q E40 Q<=epsilon40 Q,
    epsilon40=2.4301374667791075...e-8.

This is the retained pointwise full-J Hermite constraint reweighted on ALL
3892 SM40 subcells, all 973 leaves and all 107 reflected clusters. The
original kappa-shift is paid. Therefore simple compression of the VALID
order Kminus<=E40 gives

    Q Kminus Q<=epsilon40 Q.

Using this bound is compatible with #345/#347 stopping global positivity
comparisons involving envelopes. E40 is only used for a SMALL Q-compressed
negative-action upper here; no global Astar>=E40 claim is made or needed.

From accepted #336, the original bounded reference B14 obeys

    Astar>=B14>=kappa_star I,
    Q B14^-1 Q <=beta Q,
    beta=(1+delta)/kappa, delta=10^-500,
    kappa_star=33621/10^9.

The original reference composition is replayed from its TWO pinned inputs.
Inverse form order Astar^-1<=B14^-1 follows variationally, also for the
inherited unbounded Astar. Thus

    Q Astar^-1 Q<=beta Q.

No inverse compression is replaced by an inverse of a compression.
No noncommuting inverse-square comparison or projection/inverse equality
is used. Independent original realization/domain review remains OPEN.

## Correct Birman–Schwinger geometry

The physical QH complement is NOT the space on which the new BS tail bound
is asserted. Define S=range(Kminus^(1/2) J), a closed finite-dimensional
space, and let v be orthogonal to S. Then

    P Kminus^(1/2) v=0,
    y=Kminus^(1/2) v belongs to QH.

The two accepted bounds now pay the entire quadratic form:

    <v,Bv>=<y,Astar^-1 y>
            <=beta ||y||^2
            =beta ||Q Kminus^(1/2) v||^2
            <=beta epsilon40 ||v||^2.

The last step uses the exact operator norm identity

    ||Q Kminus^(1/2)||^2=||Q Kminus Q||<=epsilon40.

It does NOT square a multiplier compression or commute P with Astar^-1.
Consequently RBR<=t R, t=beta epsilon40. Exact Fraction arithmetic gives

    t<2431/10^8=0.00002431.

The corresponding bound using only the global kappa_star floor would be
epsilon40/kappa_star. Reusing the FULL compressed reference inverse improves
that tail upper by more than 29.7 times. No actual Astar inverse is evaluated.

Equivalently, X=Astar^-1/2 Kminus^(1/2) has a rank<=470 approximation
X_P=Astar^-1/2 P Kminus^(1/2), with

    ||X-X_P||^2<=beta epsilon40.

The error is on the FACTOR. A rank bound for a direct expansion of X*X
must not silently drop its cross terms; the subspace proof above avoids
that mistake entirely.

## Complete spectrum upper count

B is the same positive compact original operator used in #347/#348.
There is a codimension<=470 subspace on which its Rayleigh quotient is
at most t. Min-max therefore gives lambda_471(B)<=t<0.00002431.
This bounds the high-index spectrum of the ENTIRE original operator,
including all couplings. It is not a finite-section eigenvalue estimate.

#348 supplies lambda_4>1-3e-12. Since t<1-3e-12, the number of eigenvalues
above that level lies between four and 470. These facts do not require the
four trial functions to lie in S, nor do they identify S with a top spectral
subspace. The strict negative index of Astar-Kminus is at most 470 under
the inherited form Birman–Schwinger congruence. Its vanishing is NOT proved.

## Remaining full finite/mixed Schur gate

Write B on S plus S-perp as

    B=[[H,D],[D*,C]], 0<=C<=t I, t<1.

Because I-C is strictly positive and boundedly invertible,

    I-B>=0 iff I-H-D(I-C)^-1 D*>=0.

This finite-dimensional Schur object includes the full infinite coupling.
H alone is not the complete test. Its entries, D, and the Schur value are
NOT computed in this pass. Neither S nor its physical-coordinate Gram
has been numerically assembled.

For any independent synthesis U=Kminus^(1/2) J_selected spanning S,
the orthonormalized finite compression would involve

    G_K=J_selected* Kminus J_selected,
    N_K=J_selected* Kminus Astar^-1 Kminus J_selected,
    H=G_K^-1/2 N_K G_K^-1/2.

This formula uses the TRUE inverse and requires the actual Gram and
congruence to be controlled. It is not the physical J Gram, not the #348
compressed signed matrix, and not an inverse of a finite Astar Galerkin
matrix unless a valid complete residual/transfer is separately provided.

If one uses only positivity of B and C<=t I, the generic mixed upper is

    DD*<=t H,
    D(I-C)^-1 D*<=t/(1-t) H.

Thus H<=(1-t)I is a valid SUFFICIENT finite test. It is not equivalent to
the exact Schur test and is not certified here. Sharper matched information
may be needed for the genuinely near-critical modes. The tail result
does not restart either stopped SM40 or affine-cap global comparison.

## Verification and source standing

The standard-library generator composes three hash-pinned results and
checks that the reference and Hermite bounds use the SAME native J470.
The independent checker recomposes the tail, count and Schur constants.
An exact noncommuting 3x3 model verifies the correct S-perp compression;
the false shortcut Q B Q<=beta epsilon fails on that same model. A second
exact positive-block model rejects omitting the mixed Schur term even
when both diagonal blocks are individually below one.

Those algebra models are regression checks, not original-operator evidence.
The operator proof above and inherited native/analytic standing remain
separate from exact arithmetic replay. Local new composition/replay take
less than one second; no native integration is repeated.

GitHub-first inputs:

* #336 reference: run 40419084302, source
  b24e57ed4bd9eb687008ea03aa73f42f6dcbc180, artifact 12697340918,
  archive d44200d6c444adf48d7b659088f82ddad16915fc1524025c852855fd232b1f87,
  result f1149e27da8a0e1d90e48b8ee0eb8a0a0b8ef51d0910499a7fcd19a082efca07.
* #345 full-Q envelope: run 40451367065, source
  30d4597b8c3fd68886899ba89e278e66de661dce, artifact 12710727196,
  archive a15f8ff4a6161f3b2a84201ec1ff7fba5591b35f29dd009422848b5bc84166c8,
  result 19af532b6bbd4a808854696b2a993e7ebd966e04da27fdd5f55e8b736668770b.
* #348 coupled lower count: run 40516665209, source
  8217c8c97520c37f7b1889da340ac13b7cff0594, artifact 12738593751,
  archive 735ab9b78b6df9b09590ba70a8e51049aa19e73ebb526f22c58797b455cc4968,
  result a84b19c1fefc4e680c5c19ea643bbe5badce639374cb0a424211ee980020f922.

The focused workflow verifies all three successful run/source/artifact/
archive chains and all six extracted JSON hashes. It replays the reference
composition from its matched native/trial inputs, replays #348, then runs
the new complete-tail composition and independent exact checks.

W-ODD-NEG, exact critical count, complete finite/mixed Schur, original full
inverse response, global BS norm <=1 and independent original-domain review
remain OPEN. Even/CC27/Weil/RH unchanged. Manifest unchanged.
