# Original selected physical frame: raw signed-box transport stop

This is a bounded continuation of draft PR #351, using its exact accepted
242-by-4 signed block, not another source direction or a full signed matrix.
It keeps W-ODD-NEG and the inherited original domain/realization review OPEN.
No acceptance or canonical obligation status is changed.

## Custody and replay

The focused workflow requires successful run 40587516182 at source
877cb8d2e5d60f9c2597879837dcb096ee9d4e21, artifact 12772418317,
`original-signed-critical-mixed-block`, archive SHA256
`d48b0b05fbdaf4ba4996c6fd1aeaf7aacd2fce9ab6ae8c2c9617b5fceda8febc`.
It hashes all seven retained JSONs, replays the accepted reduced rank and
signed-block validation, then rebuilds the new native frame and independently
replays the rational error ledger. The block hash is
`2cb869033f2c6722d356e769f35fc0e1b041ae46a8c11360e66cd7d2c694c548`.
The rank hash is
`9b9820a0163e5e8bf08dd1c2525c757ff67214b49a40cb093d00bc611c9ff9e2`.

## Actual physical frame

At 4096 bits, pinned python-flint 0.8.0, reconstruct the complete physical
Gram H=J_selected*J_selected from the inherited closed physical primitives.
Choose an exact dyadic candidate D by midpoint-rounded Cholesky and triangular
solve. Candidate arithmetic proves nothing by itself. Verify against the
ORIGINAL interval H that N=D*H D has every absolute error row sum below .01.
Consequently .99 I <= N <= 1.01 I, and J_selected D is a verified physical
frame. It is not asserted exactly orthonormal. A deterministic SHA256 commits
to every exact dyadic D coefficient; CI reconstructs D rather than trusting a
serialized normalized Gram. No raw 246-dimensional inversion is attempted.

The observed largest D coefficient is about 6.50312e148; its Frobenius norm
is about 1.11684e149, rigorously below 2^496. The frame exists, but its raw
coordinate amplification is decisive.

## Exact independent-box transport obstruction

Let Gamma be the accepted raw signed mixed block from #351. Each accepted
native ball supplies a dyadic midpoint and radius rho_jt. For each output
coordinate of D*Gamma the exact radius of the image of the Cartesian input
box is R_it=sum_j |D_ji| rho_jt. Native evaluation encloses all 968 such
positive sums. The worst exact dyadic D column is retained, so the stdlib
replayer recomputes that complete positive sum with Fraction arithmetic.
Its lower bound exceeds 6.5e37. Direct native transport agrees with this
large enclosure. Thus the existing INDEPENDENT raw balls do not certify a
useful normalized mixed block.

This is a stop for this enclosure composition, not a lower bound on the
actual correlated analytic error, a physical large coupling, an obstruction
to correlated kernel evaluation, or a negative signed direction. Analytic
correlations could reduce uncertainty; they have not been certified here.

A concrete diagnostic budget: if every raw entry absolute error is at most
2^-581, then ||Delta Gamma||_F <= sqrt(968) 2^-581 and
||D*Delta Gamma||_F <= ||D||_F sqrt(968) 2^-581 < 2^-80.
The 2^-80 target is explicitly a diagnostic, NOT a derived Schur stability
budget and NOT enough by itself to resolve the augmented physical quotient.
This is about 175 decimal digits of absolute raw entry accuracy. It does not
specify a sufficient working precision or Laplace length: both arithmetic
and the analytic remainder must be budgeted through the complete jet
algebra. In particular increasing the #351 working precision alone leaves
its fixed 64-term analytic Laplace tail unchanged.

## Actual critical physical quotient, without raw augmentation

Build the original physical B=J_selected*F and Fm=F*F. Put V=D*B and solve
the well-conditioned verified system N Y=V in native balls. The exact
physical quotient Gram is S=Fm-V*N^-1 V. Check also its residual-Gram
expression Fm-V*Y-Y*V+Y*N Y. All 16 entries are enclosed; all four diagonal
entries are strictly positive, approximately
1.07433e-183, 2.39267e-185, 2.86968e-184, 9.41863e-183.
These are squared physical distances from the selected span. They show that
appending the raw critical functions would introduce extremely small
physical residual directions. Positive diagonals do not certify independence
of all four residuals. No quotient conditioning or augmented frame is claimed.
The residual expression is an algebraic consistency check using the same
physical primitives, not an independent integral implementation.

## Stop and next necessary gate

Stop before recomputing 968 entries or assembling the selected signed matrix.
The physical normalization and its actual error amplification are now known.
The next implementation must first demonstrate a joint arithmetic/Laplace
error budget in these physical coordinates (or certify cancellation before
interval boxing). A normalized critical quotient needs its own verified
conditioning and error transport before any raw append. Strong complementary
coupling Q W U, the complete finite signed block, and its mixed Schur correction
remain uncomputed. The signed complement floor from #351 remains valid under
the inherited assumptions, but does not discharge these obligations.

This bounded result supplies no full odd-sector positivity or RH conclusion.
