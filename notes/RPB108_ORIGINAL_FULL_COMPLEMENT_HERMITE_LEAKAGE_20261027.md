# Whole original J470 complement: joint Hermite leakage and threshold

Base: PR #343 / 3a39bfad3581364ad52b6c8b2917e55bb06e36e0.
Active obligation W-ODD-NEG remains OPEN. No source/trial change, inverse,
arch integration, final sign claim or governance acceptance change.

## Complete operator result

For Q the PHYSICAL L2 projection onto the complement of the ORIGINAL
470-source odd space J, retain the original Kminus=(kappa-m)_+ supported
Fourier multiplier compression, kappa=1/1000 and B=11/10. The new bound is

    Q Kminus Q <= epsilon Q,
    epsilon = 2.1246634323274064e-7... <213/10^9.

This covers EVERY odd physical f in J-perp, not just the fourteen SI29
residual features. In particular, it is not a source diagonal/rank census.
It uses all 107 original source centers and 469 derivative constraints,
while retaining the genuine pole as the 470th source. The operator and
source carrier are unchanged.

For comparison, the accepted SM40 complement bound implicit in its
threshold is epsilon_old=kappa*(1-theta_old), with

    theta_old = 0.9699135819561749... .

The new complete epsilon improves that bound by a factor >141. The #343
squared strong-action bound ||Kminus W||^2 on fourteen normalized functions
is a DIFFERENT quantity; do not compare its number directly to epsilon.

## Exact Fourier zeros already supplied by the existing sources

For odd supported f, define F_f(t)=integral_(-B)^B f(x) sin(2*pi*t*x) dx.
Its Fourier transform is -i F_f(t). Compact physical support and L2 imply
L1, and differentiation under the integral is valid to every finite order.
The original source at center c_i has generators

    x^k sin(2*pi*c_i*x), k even,
    x^k cos(2*pi*c_i*x), k odd, 0<=k<p_i.

Thus f in J-perp implies F_f^(k)(c_i)=0 for EVERY k<p_i. These are exact
constraints on the whole complement, not small numerical residuals.
The pole constraint is not used to estimate F_f, so retaining it only
restricts the same complement further.

For any selected multiplicities 0<=m_i<=p_i and N=sum m_i>=1, put
w(t)=product (t-c_i)^m_i. The repeated-node Rolle argument gives

    |F_f(t)| <= sup_s |F_f^(N)(s)| * |w(t)|/N!.

Here is a direct proof, including the complex case. If t is a selected
node, the result is immediate. Otherwise rotate F_f by the complex phase
of F_f(t), take its real part H, and subtract H(t)w(s)/w(t). This real
function has the selected zeros with their multiplicities and the extra
zero at t. Repeated Rolle gives a zero of its Nth derivative; w^(N)=N!.
The real-part derivative is bounded by |F_f^(N)|. The relevant real interval
may extend beyond the cluster; the derivative estimate below is GLOBAL
in real frequency, so no extrapolation cost is omitted. For context, the
standard real-node remainder is NIST DLMF 3.3.5:
https://dlmf.nist.gov/3.3.E5 . The repeated-node/complex-phase proof above
is supplied here rather than assumed from a distinct-node citation.

Cauchy-Schwarz on the ORIGINAL physical interval gives

    |F_f^(N)(s)|^2
       <= (2*pi)^(2N) * [2B^(2N+1)/(2N+1)] * ||f||^2.

Consequently, using 2*pi<44/7, for any real frequency interval [l,r],

    |F_f(t)|^2 <= E(l,r;m) ||f||^2, t in [l,r],
    E = [2B/(2N+1)] * [((44/7)B)^N/N!]^2
        * product max(|l-c_i|,|r-c_i|)^(2m_i).

The physical moment factor 1/(2N+1) is essential. There is no dimension
factor and no uncomputed original Gram in this bound.

## Finite selection and complete leaf payment

For each full SI10 cluster, the producer sorts the original centers by
maximal distance from that cluster. It repeats each center up to its
existing order p_i, evaluates the 469 successive prefix bounds, and keeps
the least. Partial multiplicities always use the INITIAL derivative
orders 0,...,m_i-1, which the original J actually contains. It never
requests additional derivatives as source constraints. The resulting
selected N ranges from 2 to 211. Optimality of the selected subset is not
needed for correctness: the independent checker verifies admissibility
and every resulting product directly using factorials.

Keep this fixed selected subset on each of the original negative leaves
inside the cluster. Recompute each interval distance using that leaf's
endpoints. With its accepted original height h_leaf,

    M_leaf=2*(r-l)*(h_leaf+kappa),
    epsilon=sum_(all 973 leaves) M_leaf E(l,r;m_cluster).

This pays BOTH signs once and the full kappa shift. Exact checks verify
all leaf/cluster boundaries, full partition coverage, and agreement of
the accumulated masses with the accepted two-sided cluster masses.
The inherited original cover controls the remainder of the real axis.
No Fourier sample or frequency integration appears. The whole-cluster
version alone gives 2.2374912774928243e-6; respecting the existing leaf
endpoints improves it to the complete result above in about six seconds.

This use of a Hermite nodal polynomial concerns the SCALAR FOURIER FUNCTION
with exact zero constraints. It is not a global monomial approximation to
the high-frequency physical source functions. No 8,322-dimensional
polynomial Gram or fixed-4096-bit monomial evaluation from #341 is used.

## Original signed complement and sufficient threshold

The genuine pole belongs to J, so on J-perp the pole correction vanishes.
The original positive multiplier floor A_o>=kappa I therefore yields

    (Astar-Kminus)|_(J-perp) >= (kappa-epsilon) I.

In the original SM34 energy-dual splitting E_A=Astar^-1 ran(J), the positive
mixed form cancels exactly. The remaining negative mixed response satisfies

    ||Q Kminus e||^2 <= epsilon <e,Kminus e>,
    correction <= epsilon/(kappa-epsilon) * <e,Kminus e>.

Thus a sufficient WHOLE-original odd gate on all 470 dual-source
coefficients remains N<=theta G, now with

    theta=(kappa-epsilon)/kappa
         =0.9997875336567673... >999787/10^6.

These are full operator/coupled source-form statements, not diagonal
approximations. The exact rational theta and signed-complement floor are
retained. kappa=1/1000 is NOT kappa_star=33621/10^9; the latter and the
MG07 strong-residual amplification are unchanged.

## What this does and does not change

The #343 theorem stops the canonical augmented Ritz/cap method for
thresholds <=0.97. That theorem remains valid. The new threshold is ABOVE
that scope, so #343 cannot decide this changed sufficient test. It is not
an example of improving a stopped method at its unchanged threshold.

No actual cap-only necessary gate, full inverse, matched response or
strong residual has been computed at the new threshold. Existing SM40 cap
error may still defeat it, and the residual charge remains restrictive.
The next bounded diagnostic must test the same original cap/trial against
this changed threshold and its common-Young residual budget before any
large arch/484D computation is justified. Do not automatically resume that
run or add source directions. The exact signed Schur remains an alternative.

## Custody and verification

One pinned successful #343 archive carries all required inputs: run
40436010764, source 3a39bfad3581364ad52b6c8b2917e55bb06e36e0,
artifact 12704426598, archive SHA256
fdaf970d18edaaaabd8e199653d1945b8f5da61b92e51e4fcfef0eba2b9721a4.
The new workflow verifies that custody and the native original geometry,
#338 exact negative leaves/masses, and accepted original SM40 threshold
JSON hashes individually. It does not rerun the old integrals/native solve.
Everything new is stdlib Fraction arithmetic. Independent replay checks
all selected multiplicities, all 973 products/masses/payments, complete
Loewner epsilon and threshold, repeated-node polynomial saturation,
physical moment and reflection/kappa regressions.

The live parent suite finished 45 passes / 3 failures. All three failures
occurred in an unchanged endpoint-tail serializer at Python's 4300-digit
integer-string limit (runs 40436076822, 40436076874, 40436076866). They are
not represented as passes or silently repaired here. The new focused
workflow uses its existing explicit 100000-digit budget. Native input
standing, this analytic proof, arithmetic replay and independent original
Fourier/operator/domain review remain separate.

W-ODD-NEG, inherited domain review, original signed positivity/negativity,
even/CC27/Weil/RH remain OPEN. No manifest acceptance/status change.
Draft/unmerged; large source/integration work remains gated.
