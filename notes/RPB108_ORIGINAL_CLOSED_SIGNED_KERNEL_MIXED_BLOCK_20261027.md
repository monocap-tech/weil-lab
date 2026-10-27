# Closed original signed frequency kernel and complete critical mixed block

Weil-Lab, 2026-10-27. Continues draft #350 at
`f61befddcba8600e283a276bfe6205a6d16b5222`. Draft/unmerged.

## Result and stopping point

Compute the COMPLETE original signed mixed block

    Gamma=J_selected^* W_o F_critical, size 242 x 4,
    W_o=Astar-Kminus.

J_selected is exactly #350's retained original family, including the TRUE
pole. F_critical is exactly #348's four rational physical witnesses; no
new candidate direction or source-positivity campaign is introduced.
The block uses the full original arch, all seven translated prime terms
and the true pole. Maximum source derivative order is 13; retained centers
include c=113013/128. All 968 mixed entries and their components are retained.

A new analytic frequency kernel and LOCAL frequency jets eliminate arch
quadrature from the production block. The whole block and independent
translated-prime/pole checks take about 16 seconds locally. A separate
physical/Cauchy validation takes about five seconds. The largest native
entry radius is below 4e-105. These are RAW coordinate enclosures, not an
admissible transformed error budget or a global mixed operator norm.

An exact corollary of #350 also supplies the PHYSICAL signed-complement
floor, distinct from the BS-space tail:

    Q_selected W_o Q_selected >=mu Q_selected,
    mu=1/1000-epsilon_selected >0.00098.

The original true pole belongs to the retained physical space, so its
negative rank-one action vanishes on that complement. Ao>=1/1000 I and
the accepted complete Kminus leakage upper give this form inequality.
It is NOT a transfer of a compressed Astar inverse bound to a larger
complement; those different operations remain prohibited.

STOP after GitHub replay of this fixed mixed block and representation test.
The block is not the BS mixed block D, not Astar inverse forcing, not a
strong residual and not the full finite/mixed Schur. Frame/projection error
transport remains unresolved. Do not assemble/invert a raw augmented
246-dimensional matrix merely because these raw entries are sharp.
The near-dependence of appended critical functions must be handled in a
verified physical/quotient frame. No such normalization is certified here.

## Original physical kernel

Let B=11/10, L=2B, k(s)=exp(s/2)/sinh(s), c0=psi(1/4)-log(pi).
Use angular frequency nu=2*pi*c and u_nu(x)=sin(nu*x), supported on [-B,B].
The following are complex-BILINEAR analytic continuations of the real
symmetric form; real physical combinations recover the Hermitian form.
In particular the true pole is h=-i*u_(i/2), not a real-frequency sine.

Define

    G(nu,mu)=sin((nu-mu)B)/(nu-mu)-sin((nu+mu)B)/(nu+mu),
    I(nu)=integral_0^L k(s) sin(nu*s) ds,
    A(nu)=c0+integral_L^infinity k(s) ds
                 +integral_0^L k(s)(1-cos(nu*s)) ds.

Direct trigonometric integration of the clipped translated overlap gives

    C(nu,mu;s)=sin((nu-mu)(B-s/2))/(nu-mu)*cos((nu+mu)s/2)
               -sin((nu+mu)(B-s/2))/(nu+mu)*cos((nu-mu)s/2).

Its cosine/sine decomposition yields the COMPLETE arch bilinear kernel

    H_arch(nu,mu)=G(nu,mu)*(A(nu)+A(mu))/2
       -[cos((nu-mu)B)*(I(mu)-I(nu))/(nu-mu)
          +cos((nu+mu)B)*(I(nu)+I(mu))/(nu+mu)]/2.

At nu=mu the analytic limit is

    G(nu,nu)=B-sin(2nuB)/(2nu),
    H_arch(nu,nu)=G(nu,nu)A(nu)+I'(nu)/2
                         -cos(2nuB)I(nu)/(2nu).

Prime terms are EXACTLY -2 sum log(p)/sqrt(n)*C(nu,mu;log n), for
n=2,3,4,5,7,8,9. All other prime shifts exceed the physical support.
The pole term is -2 H(nu)H(mu), where

    H(nu)=2[(1/2)cosh(B/2)sin(nuB)-nu*sinh(B/2)cos(nuB)]/(1/4+nu^2),
    H(i/2)=i*(sinh(B)-B).

The removable diagonal and true-pole cases are handled analytically.
The retained real centers do not coincide with the critical sine frequencies;
no singular divided difference is silently inverted in the mixed jets.

## Digamma/Laplace representation that remains regular at the true pole

Writing alpha_j=2j+1/2, k(s)=2 sum_(j>=0)exp(-alpha_j s), isolate j=0.
Let E(z)=exprel(z)=(exp(z)-1)/z, E(0)=1, and

    E_plus=E((-1/2+i*nu)L), E_minus=E((-1/2-i*nu)L),
    I_head=L/i*(E_plus-E_minus),
    J_head=2L*[E(-B)-(E_plus+E_minus)/2].

Then

    I(nu)=I_head+[psi(5/4+i*nu/2)-psi(5/4-i*nu/2)]/(2i)
      -2 sum_(j>=1) exp(-alpha_j L)
         *(alpha_j sin(nuL)+nu cos(nuL))/(alpha_j^2+nu^2),

    A(nu)=[psi(5/4+i*nu/2)+psi(5/4-i*nu/2)]/2
       -log(pi)-4+4exp(-B)+J_head
       +2 sum_(j>=1) exp(-alpha_j L)
          *(alpha_j cos(nuL)-nu sin(nuL))/(alpha_j^2+nu^2).

Use the analytic PAIR of psi functions, not real/imaginary extraction inside
a complex-frequency callback. The recurrence psi(z+1)=psi(z)+1/z isolates
the apparent unshifted digamma pole at nu=i/2. Shifted arguments have positive
real part on every required disk. E(0) and its local series are entire.
Primary formula sources: https://dlmf.nist.gov/5.5.E2 and
https://dlmf.nist.gov/5.9.E16 . These support the special-function identities;
they are not sources for the new mixed-block calculation.

Retain j=1,...,63 plus the exact head. On |Im nu|<=3/4 the omitted sine or
cosine tail is bounded by

    2exp(-(511/4)L)/[(511/4)(1-exp(-2L))] <2^-406.

The clean inequality is independently checked using exp(7/10)>2,
(511/4)L>401*(7/10), and 2L>6*(7/10). Cauchy's estimate on radius 1/4
bounds EVERY omitted Taylor coefficient of order k by 2^-406*4^k.
These errors are explicitly added to the complex coefficient balls before
any divided difference or physical source combination is evaluated.

## Local jets and original source normalization

At each retained original center nu0, build the local Taylor jet through
the required order using native scalar polygamma coefficients and formal
series algebra. Trigonometric jets use exponential identities and an actual
radius guard, rather than relying on a requested precision setting alone.
The expansion variable is LOCAL angular frequency, not the physical source
monomial coordinate. There is no large global Taylor polynomial in x.

The original source at index k is x^k sin(nu0*x) for even k and
x^k cos(nu0*x) for odd k. Its mixed entry is therefore

    (-1)^floor(k/2) * k! * [local frequency coefficient of order k].

All conversion factors are included. The true pole row is evaluated with
the factor -i on its analytic sine. The same original primitive library
encloses each raw source's physical norm; these diagonal norms do NOT
establish orthogonality or a frame condition number.

The full four-by-four critical signed Gram reconstructed from the kernel
lies in the accepted #348 physical-form intervals, including every mixed
entry. This validates the target functions and whole-form normalization
against the independent physical shift-integral construction.

## Independent verification

1. For ALL 968 entries, the seven-prime component is independently recomputed
   from the original clipped polynomial/trigonometric physical primitives,
   including all seven asymmetric shifts. The true pole component is
   independently recomputed from physical overlaps. These calculations do
   not differentiate the new kernel.
2. Three original anchor combinations (sine, pole, sine+pole at c=37/64)
   compare arch, prime and pole components with the inherited direct native
   physical shift integral. Verification uses small scalar integrations;
   production of the 242x4 mixed block uses NO arch quadrature.
3. The hardest order-13 coefficient is checked by a DIFFERENT derivative
   algorithm: 256 native points on a complex circle of radius r=1/8,
   with analytic radius R=1/4. A priori |Q(u_nu,f_0)|<M=10^8 holds on
   that disk. The actual rational majorant composed from physical amplitude,
   derivative, pole and Kminus bounds is below 1458. This uses the inherited
   original general Ao upper <=36||u||^2+variation(u)^2, and the exact
   supported-Fourier trace bound ||Kminus||<=2B*mass40<37.

   For coefficient k=13 the discrete Cauchy alias error, after multiplying
   by k!, is

       M/R^k * (r/R)^256/[1-(r/R)^256] * k! <3.61e-52.

   This is a rigorous alias remainder, not empirical quadrature convergence
   or a finite-difference comparison. No numerical derivative value enters
   the production jet enclosure. The native samples/roots/phases are retained
   for exact complex-interval arithmetic replay.

The standard-library replay recomposes every raw entry, checks all independent
component intersections, reproduces the accepted critical Gram, verifies the
clean Laplace tail/Cauchy constants and independently sums the Cauchy estimate.
It does not independently re-prove native digamma/polygamma balls, the direct
Arb physical integrals, or the inherited original operator realization.
Those have separate analytic/native review standing.

## Physical complementary floor and the actual remaining gate

Let P_selected be the PHYSICAL projection onto the selected source span and
Q_selected=I-P_selected. The true pole belongs to that span. Thus, on its
form-domain complement,

    Q_selected W_o Q_selected >=(kappa-epsilon_selected) Q_selected,
    mu=0.0009832321268428579... >0.00098.

This is a lower on a COMPRESSED SIGNED FORM. It does not assert
Q_selected Astar^-1 Q_selected<=1/kappa or define a global W_o inverse.

For a verified physical orthonormal finite synthesis U, set

    L_U=U^* W_o U, B_U=Q_selected W_o U,
    C_W=W_o restricted as a closed form to Q_selected H, C_W>=mu I.

The exact complete signed Schur condition is

    L_U-B_U^* C_W^-1 B_U>=0.

The chosen piecewise analytic source functions have square-log Fourier
action integrable at infinity, so the finite strong columns are legitimate
under the inherited operator/domain hypotheses. Their strong values and
norms are nevertheless NOT computed here. Gamma=J_selected^* W_o F_critical
is an ACTUAL component for projecting/aligning the fixed critical plane;
it is not B_U or the BS-space mixed block. Adding F_critical to a finite
space preserves the positive complementary floor, but its near-dependence
must be controlled in a verified quotient/frame before a solve.

The selected-selected finite matrix, strong complementary coupling,
critical physical projection, augmented frame conditioning and complete
Schur remain OPEN. The present one-variable jet implementation also does
not certify a full two-variable source-jet matrix at coincident centers.
Do not extrapolate the measured block runtime to that unimplemented step.

Raw-coordinate error below 1e-100 is not a final useful error budget.
The Laplace tail is fixed at 64 terms here; increasing arithmetic precision
alone cannot remove that analytic error. Future frame transport must jointly
choose native precision, tail length and matched Schur tolerance. A small
raw column norm or separate component inverse charge is not a substitute.

## Custody and standing

Parent #350: successful run 40582136032, source
f61befddcba8600e283a276bfe6205a6d16b5222, artifact 12770022548,
archive SHA256 3389809c3a01c223b95e9dc96ea7c9dd776cb83049bb2d93a3c9d9bbad45af09.
Rank JSON SHA256:
9b9820a0163e5e8bf08dd1c2525c757ff67214b49a40cb093d00bc611c9ff9e2.
Critical block SHA256:
a84b19c1fefc4e680c5c19ea643bbe5badce639374cb0a424211ee980020f922.

One pinned archive contains both and the matched inputs needed to replay
#350. The focused workflow verifies run/source/artifact/archive and all
five extracted JSONs, replays the accepted rank proof, installs pinned
python-flint 0.8.0, computes the block, runs the separate native validations,
then independently replays both retained outputs with exact arithmetic.

W-ODD-NEG, exact critical count, full finite/mixed signed Schur, actual
inverse/strong residual, transformed error budget and independent original
domain review remain OPEN. Even/CC27/Weil/RH unchanged. Manifest unchanged.
