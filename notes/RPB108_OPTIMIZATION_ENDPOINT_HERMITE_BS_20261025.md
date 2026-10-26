# Endpoint-jet preflight and structural optimization audit

## Current evidence and priority

The complete physical xcos coupling calculation is already accepted by
GitHub run 40267592408 at 74f0e4f08cef9f1e8984471eefe8c8f68587e386.
Its scalar Schur lower is approximately -0.1369083914: INCONCLUSIVE,
not an actual negative witness. Do not start a dimension-by-dimension
source campaign from this result.

The cheap endpoint preflight below uses that accepted artifact, all source
identities from the same repository head, and no frequency quadrature.

## Two endpoint conditions

Write w=2*pi*(37/64), B=11/10, u=sin(wx), s=sinh(x/2).
For r=x*cos(wx)+a*u+b*s, the true endpoint matrix is

    [ sin(wB)       sinh(B/2)  ] [a] = [ -B*cos(wB)             ]
    [ w*cos(wB)     cosh(B/2)/2] [b]   [ -cos(wB)+wB*sin(wB)    ].

Exact original trigonometric/hyperbolic intervals put its determinant
strictly between 0.944 and 0.945. Hence the exact REAL coefficients,
defined by this matrix inverse, are unique. Rational interval enclosures:

    1.884802846601 <= a <= 1.884802846602
    3.707849526107 <= b <= 3.707849526108.

These are enclosures of exact real coefficients, not assertions that
finite decimals cancel transcendental endpoint values exactly.

For the exact solution r(B)=r'(B)=0, three physical integrations by parts
give |rhat(xi)| <= C3/|xi|^3, where

    C3=(2|r''(B)|+integral |r'''|)/(8*pi_lo^3),
    integral |r'''| <=6B*wup^2+wup^3*B^2
                      +2B*|a|*wup^3+|b|*sinh(B/2)/2.

The rounded rational choice a0=1.884803, b0=3.707850 instead has the
rigorous all-frequency tail C1/|xi|+C2/xi^2+C3/|xi|^3.
The small C1,C2 must be retained. Pure cubic asymptotic decay is not
claimed for these rational approximants.

Reusing the accepted anchor packet majorants and the complete signed
logarithmic tail envelope gives >10-fold reduction in EACH absolute
mixed high12 payment and >48-fold reduction in the negative diagonal
high12 payment, for both constructions. These compare different
representatives of the same quotient direction; they do not certify a
better complete Schur value by themselves.

Adding any anchor combination leaves the EXACT full scalar Schur
unchanged: with c in R^2, b'=b+Hc and d'=d+2c^T b+c^T Hc give

    d'-(b')^T H^-1 b' = d-b^T H^-1 b.

An exact nontrivial rational algebra regression checks this identity.
No new lowband calculation, actual scalar Schur positivity, or global
odd closure is claimed by the preflight. The next numerical acceptance
must retain matched full 2x2 covariance and all complete mixed terms.
A lower matrix for the full retained 3x3 form may alternatively discard
a WHOLE positive high-frequency PSD form, but never omit only its mixed
entries while claiming bounds for the complete mixed functionals.

## SI29 Hermite residual representation

Repository source validate_rpb108_si29_hermite106_fullJ_residual.py already
establishes more than L2 proximity. It gives a true 14-feature Hilbert-
Schmidt residual bound <1.6e-21 and an Astar-energy Schur upper
T<2e-37 I, conditional on inherited original source/operator premises.
It does not evaluate the actual energy Schur, its lower bound, or the
normalized inverse response. Tiny T alone is neither success nor failure.

For any certified Hermite coefficient map C, E=F-JC and J*R0=0 give the
EXACT identity F*R0=E*R0. This is a useful residual representation.
For A=Astar and AJ=J*AJ, the actual feature Schur is

    T=E*AE - E*AJ (J*AJ)^-1 J*AE.

Here J*AJ means J^* A J and E*AJ means E^* A J; every star is an adjoint.
In conventional notation:

    T = E^* A E - E^* A J (J^* A J)^-1 J^* A E.

It is NOT simply E^*AE unless the residual basis has been proved
A-orthogonal to J. The forcing for the same Galerkin response is
h=E^*R0=F^*R0. A nonsingular diagonal normalization Ehat=E D^-1
gives That=D^-1 T D^-1, hhat=D^-1 h and

    h^* T^-1 h = hhat^* That^-1 hhat.

The useful next target is a normalized energy-Schur lower enclosure
paired with its SAME normalized forcing, plus the complete original
470-source projection/action certificate. If rank deficiency is possible,
certify the kernel and forcing compatibility rather than silently
inverting fourteen presumed independent residuals.

Block factorization can avoid a raw 484x484 solve. It does not remove
the unresolved original 470-source energy projection. The existing
Hermite-106 script proves residual bounds, not a constructed, normalized,
certified 14-dimensional response matrix.

## Compact Birman-Schwinger route: recover, do not rediscover

This route already appears in:
- scripts/validate_rpb108_si11_birman_schwinger_gate.py
- scripts/validate_rpb108_sm17_compact_spectral_gate.py.

For the complete original split use k=(kappa-m)_+, including the
+kappa payment, rather than substituting the strictly negative m_- mass.
On the physically supported odd Hilbert space define

    R=M_sqrt(k) Fourier extension, K=R^*R.

Then the frequency-carrier operator is B=R Astar^-1 R^*, with the
SUPPORTED Astar inverse. Under the inherited domain/closed-form premises,
Wodd>=0 iff B<=I. R is Hilbert-Schmidt when k is integrable on its
certified support, hence B is trace class. Equivalently one may use the
square root of the PHYSICAL compression K, but it must not be confused
with a compressed full-line multiplier square root.

SI11 already quantifies finite-rank remainder/coercivity loss. SM17
already states a conditional 890-source compact gate and records a crude
trace upper bound near 2.49 million. Compactness alone therefore supplies
no useful norm gap below one. The unresolved object is the complete
supported inverse response plus a sufficiently sharp operator-norm
remainder, not the Birman-Schwinger equivalence itself.

A limited feasibility audit should compare the actual leading spectral
margin and inverse-response cost against these existing remainder bounds.
A new finite-rank carrier method may improve them, but should not be
presented as a new reduction or as an automatic bypass of the inverse.

## Stopping rules

1. Accept this cheap endpoint preflight before another expensive integral.
2. Reuse accepted lowband artifacts and prove coordinate transport where
   possible; do not assume the old diagonal inverse cap is basis invariant.
3. Prefer the normalized 14-dimensional SI29 response over raw augmented
   inversion, with the full original projection requirement explicit.
4. Audit SI11/SM17 feasibility before opening a new compact-operator lane.
5. No 3D/4D/5D positivity count substitutes for full matched signed coupling.

No canonical obligation, closure status or acceptance condition changes.
W-ODD-NEG, inherited analytic/domain review, even/CC27/Weil and RH are OPEN.
