# Original matched Schur error allocation before further arch computation

Base: PR #341, e95cfd14b3ac14a68e3685cc24b99034bb6c524b.
Live canonical manifest inspected: W-ODD-NEG remains OPEN.

## Outcome and run guard

Derive the error contract for the SAME original normalized U=JD,
W=(I-P_J470)FC. Do not choose an arch integration tolerance in isolation.
The actual signed-gate margin, anchor/quotient energy matrices and matched
forcing remain unavailable. Therefore a final useful arch tolerance cannot
yet be selected. The numerical allocations below are illustrative stability
contracts, NOT positivity thresholds and NOT reasons to launch an arch run.

In particular, keeping the accepted negative mixed component as a ball
centered at zero has radius 0.003001. That alone exhausts the illustrative
1% Schur-inverse stability allocation by more than 750,000 times. A very
accurate arch block does not remove that uncertainty. This is a limitation
of this allocation, not evidence of instability of the true positive Schur.
Separate component inverse charges cannot be added without mixed terms.

## Original blocks and matched forcing

Write the exact full energy matrix on [U,W] as

    A = [[G,M],[M*,H]],   T=H-M*G^-1 M.

Accepted original conditional bounds are

    ell I <= A <=44 I, ell=3328479/10^11,
    t I <= T <=44 I, t=9/9091.

For an unchanged original physical source synthesis S let f=U*S, g=W*S.
The exact extra inverse-response matrix after eliminating U is

    h=g-M*G^-1 f,   R=h*T^-1 h.

For source synthesis U itself, g=0 and f=U*U, with ||f||<=101/100.
For raw J sources one must apply the actual source congruence consistently.
Do not transfer a JD error budget directly to raw J. These identities do
not compute the infinite Astar inverse or a full strong residual.

## Joint perturbation bound

Let Gtilde=G+dG, Mtilde=M+E, Htilde=H+dH, in the SAME coordinates, with

    ||dG||<=delta_G, ||E||<=epsilon, ||dH||<=delta_H,
    gamma=delta_G/ell<1.

Set C=G^-1/2 M and D=G^-1/2 E. Positivity of T and H<=44I give
C*C=H-T<=44I, so ||C||<=sqrt(44)<20/3. Also
||D||<=epsilon/sqrt(ell)<174 epsilon; both rational roundings are checked.
With Q=G^-1/2 dG G^-1/2, ||Q||<=gamma,

    Mtilde* Gtilde^-1 Mtilde=(C+D)*(I+Q)^-1(C+D).

Resolvent and triangle bounds give the COMPLETE 14x14 Schur error

    ||Ttilde-T|| <= sigma,
    sigma = delta_H + [2320 epsilon+30276 epsilon^2+44 gamma]/(1-gamma).

The gamma term pays anchor error; delta_H pays quotient diagonal error.
It is invalid to report an arch-only tolerance while silently taking
uncomputed G and H as exact in the final calculation.

For an EXACT unchanged right-hand side f,g, put chi=||G^-1/2 f||. The
MATCHED forcing changes, with

    ||htilde-h|| <= d_h,
    d_h=chi*[174 epsilon+(20/3)gamma]/(1-gamma).

For source U, chi<176. Additional right-hand-side enclosure errors must
be separately paid. They are not implicitly included in this exact-RHS
formula. For arbitrary source coefficient families these are joint
operator norm bounds, not scalar diagonal checks.

If sigma<t, then Ttilde >=(t-sigma)I, and

    ||Rtilde-R|| <= sigma ||h||^2/[t(t-sigma)]
                   +[2||h|| d_h+d_h^2]/(t-sigma).

This explicitly pays BOTH inverse and forcing movement. A two-by-two
non-diagonal anchor/mixed-block exact Fraction regression verifies the
full four-dimensional inverse gain identity, and rejects holding h fixed
when M changes. A zero-mixed starting example shows that a fixed zero
forcing would miss the entire newly introduced response.

## Numerical contracts, not final margins

If G,H and the RHS were exact, epsilon=1/250000000=4e-9 gives
sigma=9.280000484416e-6<t/101. Consequently

    ||T^-1/2(Ttilde-T)T^-1/2|| <=sigma/t,
    relative inverse Loewner error <=sigma/(t-sigma)<1/100.

This is a sufficient bound on the Schur INVERSE, not a 1% bound on the
extra response R, and not a required tolerance for the signed theorem.
Even at that epsilon, the generic source-U forcing uncertainty bound is
0.000122496; its effect must be paid by the response formula or sharper
matched information. A separate epsilon=2e-7 contract preserves half of
the known Schur floor, but does not pay 1% inverse accuracy.

Recomposing #339's exact near-zero shift formula from the same full-frame
input gives 3.6434279856404313e-7 on [0,2^-36], already larger than the
illustrative 4e-9 TOTAL mixed budget. This is not a reason to lower the
cutoff now: the final tolerance and other component allocations must first
be established. The tiny #340 kernel replacement error does not certify
any actual source/correlation approximation or full arch matrix.

If the #338 negative mixed bound is used as a zero-centered error,
epsilon_negative=3001/10^6 gives sigma>7.23 even with exact G,H. This
sufficient bound does NOT preserve the known Schur floor. It does not prove
that the actual negative matrix has that norm, that the actual Schur is
ill-conditioned, or that separately bounded negative action is useless.
The accepted actual T>=t remains valid independently of this perturbation
exercise. One may need actual negative entries, a sharper coupled/energy
weighted enclosure, or a legitimately coarser final-gate allocation.

## Component accounting and next bounded decision

In the JD/W operator norm, a valid unweighted mixed budget is

    epsilon <= epsilon_arch + epsilon_prime_after_D
               + epsilon_negative + epsilon_arithmetic.

The #337 prime matrix/error is RAW J: D must be applied and the error
transported before inclusion here. The #338 norm bound is already JD/W.
There is no cancellation assumption between component errors. The final
response and signed-gate margin must specify the admissible perturbation;
the examples above do not supply that margin. The historical J-only method-stop
margin is not a reserve for the augmented trial and must not be reused as one.

The next bounded decision is whether the actual final-gate budget can
absorb the available negative norm enclosure and anchor/diagonal errors.
If not, those quantities need resolution before arch refinement. No
oscillatory quadrature pilot or large run is justified solely by this
contract. The fixed-4096-bit global monomial implementation stays stopped.

## Custody and standing

All arithmetic here uses stdlib Fractions and the accepted frame, Schur
inverse and negative-budget JSON witnesses. One pinned #338 archive carries
all three. Workflow verifies run 40423854196, source
fa7986b3fd83b8fd93014c886eb26943807e0202, artifact 12699072252, archive digest
and EACH matched JSON hash. No native projection or integration is repeated.
Exact regression/CI, analytic sensitivity proof and inherited original
operator/domain review have separate standing. This is required matched
inverse/covariance information, not another source-positivity checkpoint.

Original matrices G,M,H, actual matched forcing, inverse response, full
strong residual, signed original operator gate and infinite transfer remain
UNCOMPUTED / OPEN. W-ODD-NEG, independent domain review, even/CC27/Weil/RH
remain OPEN. No manifest acceptance change. Draft/unmerged.
