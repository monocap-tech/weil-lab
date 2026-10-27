# Original critical-mode multiplicity lower bound before deflation

Weil-Lab, 2026-10-27. Continues draft #347 at
`556a2bdc7a17b6580bd5fc7c216243bddda5e840`. Draft/unmerged.

## Decision and bounded stopping point

The near-critical obstruction is not confined to the single #347 witness.
A fixed FOUR-dimensional rational physical trial plane, including that
unchanged witness, proves

    lambda_4(B_true)>1-3e-12,
    B_true=Kminus^(1/2) Astar^-1 Kminus^(1/2).

Eigenvalues are ordered decreasingly, with multiplicity. This is a LOWER
bound on the fourth eigenvalue of the COMPLETE original compact operator,
not a numerical count or the desired global upper bound.

For EVERY orthogonal projection Pi of rank at most three,

    ||(I-Pi) B_true (I-Pi)|| >1-3e-12.

Thus removing one, two or three directions cannot create a complementary
norm bound <=1-3e-12. This does NOT prove all such deflation methods
impossible with a smaller reserve. It prevents assigning a larger reserve
to the complement by treating #347 as the only difficult mode.

STOP after this single coupled four-dimensional test and GitHub replay.
Do not automatically test dimensions five, six, etc., or declare four to
be the exact critical rank. The next spectral acceptance gate needs a
certified upper count/isolation and the complete complementary/mixed
operator bounds. Neither exists yet. No full 470/484 matrix, new inverse
solve, original strong residual or 890-moment assembly is launched.

## Why this test is on the obligation path

The #347 numerical spectrum has several values at the binary64 floor.
Their number, sign and separation cannot be certified by those quadrature
matrices. #347 verified one fixed original physical witness natively and
stopped the affine cap globally; a plausible next strategy would isolate
the difficult mode and certify its remainder. Before investing in that
strategy, its assumed one-dimensional exceptional space must be tested.

This pass verifies a COUPLED plane with the COMPLETE original signed form.
It does not infer a spectral count from small individual Rayleigh values.
All six internal mixed entries and the physical Gram metric are enclosed.
External mixed couplings to the infinite complement remain UNCOMPUTED.

## Fixed rational plane and native source custody

Use the SAME original carrier and complete functional as #347, B=11/10:

    f_i(x)=sum_(n=1)^32 a_(i,n) sin(2*pi*(5n/11)x)+b_i sinh(x/2),
    |x|<=B, zero outside, i=0,...,3.

All coefficients are exact rationals with denominator dividing 10^12,
stored in the committed candidate JSON. The first vector is EXACTLY the
accepted #347 rational witness, not a regenerated numerical eigenvector.
The other three are fixed candidates discovered by physical-metric
orthogonalization of the retained numerical trial vectors, then rounded
once. No numerical eigenvalue, quadrature error, orthogonality or count is
an input to acceptance. The native physical Gram certifies independence.
No exact original J470 membership or energy projection is claimed.

Evaluate ten complete original scalar forms at native 512 bits:

    f_0,...,f_3, and f_i+f_j for each of the six i<j.

The same grouped exponential autocorrelation as #347 supplies the entire
arch contribution with analytic zero-shift regularization, native complex
integration at tolerance 2^-160, an explicit infinite Laplace-tail remainder,
all seven physical prime shifts and the true pole. Sine orthogonality/pole
norms and direct double-sum correlations independently check grouping and
the original normalization. No negative envelope or numerical clipping root
enters this physical signed-functional calculation.

The helper merely factors the accepted #347 scalar construction into a
reusable function; it does not replace the original signed functional by
a polynomial, derivative matrix, bounded-frequency integral or component
positivity estimate. The ten-scalar local run takes about seven seconds,
guarded at 90 seconds.

Native ball integration and original source/domain identification retain
their inherited review standing. Independent exact replay does not re-prove
Arb's complex integration or the analytic original-domain realization.

## Coupled interval matrices

For each scalar, retain native balls for norm, arch constant, finite arch
integral, infinite tail, all-prime contribution, pole and complete signed
value. Round the norm and signed energy outward to denominator 10^40.
Independent stdlib rational arithmetic recomposes every scalar functional
from its separate native components and verifies those intervals.

Construct the FULL symmetric physical and signed matrices by polarization:

    G_ij=<f_i,f_j>, T_ij=Q_o(f_i,f_j),
    T_ij=(Q_o(f_i+f_j)-Q_o(f_i)-Q_o(f_j))/2,

and similarly for G. Each diagonal and BOTH ends of each mixed interval
are paid. Native coefficient correlations are not assumed independent
facts of exact cancellation; interval loss is conservative.

An exact absolute row-sum bound certifies

    ||G-I||<1/100, hence G>=(99/100)I.

A full interval absolute row bound certifies

    -sigma I <= T <= sigma I,
    sigma=9.836565223706795...e-17.

The mixed entries matter: diagonal upper bounds alone would not imply
this operator inequality. The first diagonal signed interval reproduces
the accepted #347 interval exactly.

This is a COMPRESSED FORM bound Phi* W Phi, W=Astar-Kminus. It is NOT a
bound on ||W Phi||, not an approximately invariant-subspace certificate,
not an infinite residual, and not full signed positivity. No inverse
projection or component norm is substituted for those missing quantities.

## Original complete-operator min-max transfer

Under the retained original closed-form/coercivity assumptions,

    Astar>=kappa_star I, kappa_star=33621/10^9.

For every coefficient vector c, with f=Phi c in this physical plane,

    a(f,f)>=kappa_star*(99/100)||c||^2,
    Q_o(f)<=sigma||c||^2,
    <f,Kminus f>/a(f,f)=1-Q_o(f)/a(f,f)
                       >=1-eta,
    eta=sigma/[kappa_star*(99/100)]
       =2.9552733316649424...e-12 <3e-12.

G>0 proves the physical plane has dimension four. Coercivity makes
Astar^(1/2) injective, so its image is also four-dimensional. Apply
the variational min-max principle to the compact positive operator
C=Astar^-1/2 Kminus Astar^-1/2. Its nonzero eigenvalues agree with
B_true (the two products of the same bounded factor and its adjoint).
The four-dimensional Rayleigh lower therefore gives lambda_4(B_true)>=1-eta.
No global nonnegativity of Q_o or RH hypothesis is used in this inference.
In particular, these eigenvalues are not certified to be <=1.

For any rank<=3 orthogonal Pi in the Hilbert space of B_true, its kernel
intersects a four-dimensional top spectral space nontrivially. A unit vector
in that intersection has Rayleigh value at least lambda_4. Consequently
the complementary compression has norm >=lambda_4>=1-eta>1-3e-12.
The projection need not be an exact spectral projection for this LOWER bound.

This statement is in the Birman–Schwinger Hilbert geometry. It is not a
license to identify physical orthogonal, energy-orthogonal and spectral
projections, nor does the candidate physical plane compute the top Riesz
projection of B_true.

## Next acceptance gate and standing

The exceptional dimension is AT LEAST four at this declared separation.
The exact count, a spectral upper bound on the complementary operator,
the coupling to that complement and the <=1 condition on the exceptional
block remain OPEN. Four-mode treatment is necessary to create a reserve
of 3e-12 by finite-rank deflation; it is not shown sufficient.

A future successful criterion must type these separate obligations and
pay the full operator/domain transfer. Do not infer a positive complement
from this lower multiplicity result or from stabilized finite spectra.
Do not restart a source-count campaign as a substitute for the upper count.

## GitHub custody and replay

Parent #347: successful run 40461812230, source
556a2bdc7a17b6580bd5fc7c216243bddda5e840, artifact 12714962092,
archive SHA256 978000dfecf2ce7e6275790d4c2cc3fae4824caea77dfe604ebee2d37a618e5e.
Native JSON SHA256:
2cd494b1558c43790f683d21926e1d1a83cc68a4edfdebd0d6074ac968f85919.
Inherited affine-cap JSON SHA256:
8b58972bbdd2f9cb5d00275820ab6d6891feeff3bbd584a1c28231770368f514.

The focused workflow verifies run/source/artifact/archive and both matched
JSON hashes, replays the accepted #347 witness, installs pinned python-flint
0.8.0, computes all ten original scalar forms and independently replays
their rational physical composition, all six mixed entries, metric lower,
row-sum energy bound and min-max/deflation constants. No NumPy/SciPy
diagonalization is repeated or promoted to acceptance.

W-ODD-NEG, independent original-domain review, exact spectral count,
complete true signed Schur, global true BS norm upper, infinite remainder,
even/CC27/Weil/RH remain OPEN. No manifest acceptance/status change.
