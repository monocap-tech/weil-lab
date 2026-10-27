# Original affine negative cap: bounded feasibility decision

Weil-Lab, local date 2026-10-26. Continues draft #345 at
`30d4597b8c3fd68886899ba89e278e66de661dce`; no merge or manifest promotion.

## Decision and stopping point

The original SM40 step cap is replaceable by a concrete rational clipped
affine cap with a UNIFORM complete-operator overpayment below 0.00003197.
Using accepted original signed anchor information, the new cap passes the
ENTIRE SAME two-dimensional anchor space, including the near-null direction.
The corresponding 890-column Taylor/Young cap also passes, with a specified
Young parameter and ALL approximation payments included.

This is a replacement-envelope feasibility test, not another source-positivity
certificate or a dimension campaign. No new integration, full moment matrix,
inverse, Galerkin lift or mixed block is computed. The inherited physical
signed anchor was already positive; the NEW assertion concerns two larger
negative comparison operators which the previous cap could not accommodate.

Stop after GitHub custody/replay of this test. A passed anchor restriction
does not certify the full J470 gate, the exact energy-dual capped gate, any
Galerkin lifted gate, the remaining signed Schur, or the original whole odd
inequality. Those stay OPEN. In particular, #345's stronger full-dual method
obstruction is not proved absent for this new cap: its domination hypothesis
no longer applies, and this cheaper anchor-level obstruction has been removed.
Do not proceed automatically to a full 470/484 or 890-moment calculation.
The next bounded decision must address the actual inverse/mixed coupling
for the replacement criterion, rather than more unlifted source directions.

## Original operator and inherited scope

Use the SAME supported odd physical carrier, B=11/10, kappa=1/1000,
original Fourier isometry V and original signed multiplier

    m(xi)=Re psi(1/4+i*pi*xi)-log(pi)
          -2 sum_(n=2,3,4,5,7,8,9) log(p(n))/sqrt(n)*cos(2*pi*xi*log(n)).

The original negative multiplier is r=(kappa-m)_+ and Kminus=V* r V.
The inherited original SI10/SM40 cover and protected exterior give r=0
outside the retained cover and r<=w40 on each original SM40 cell.
Physical compression and multiplier squaring are never identified.
Original domain/realization standing remains inherited and audit-required.

## Global curvature, including the full archimedean term

Differentiate the trigamma series locally uniformly in Re(z)>0:

    psi''(z)=-2 sum_(n>=0) (n+z)^(-3).

For z=1/4+i*pi*xi,

    |d^2/dxi^2 Re psi(z)|
       <=2*pi^2 sum_(n>=0) (n+1/4)^(-3)
       <=2*pi^2*(64+ integral_0^infinity (t+1/4)^(-3) dt)
       =144*pi^2 <=144*(22/7)^2.

The exact original seven-prime interval constants independently give

    prime_curvature <=8*pi_upper^2 sum weight_upper*log(n)_upper^2
                    =721.98719802078... .

Thus the COMPLETE original multiplier satisfies |m''|<H=2145 globally.
The prime-only SM40 curvature would not suffice here.
Primary formula reference: https://dlmf.nist.gov/5.15.E1 .
Linear interpolation remainder: https://dlmf.nist.gov/3.3.E4 .
The proof only uses the n=1 real two-node remainder, |m-Lm|<=H*d^2/8.

## Explicit rational cap, with clipping after interpolation

Subdivide each of the original 3892 SM40 cells into 16: 62272 cells,
maximum width dmax=1/4096. These are the same fine cell boundaries as
#345, not an additional subdivision campaign.

At ALL 62379 distinct endpoints, pinned python-flint 0.8.0 at 512 bits
evaluates the ORIGINAL multiplier. Round outward to multiples of 10^-12
and verify the endpoint interval width is at most eta=2/10^12.
The resulting exact rational lower endpoints are l_a,l_b.

On a fine cell I=[a,b], d=b-a, inside its original step height w40, set

    Llo(xi)=((b-xi)*l_a+(xi-a)*l_b)/d,
    e(xi)=min(w40,max(0,kappa-Llo(xi)+H*d^2/8)).

Reflect evenly and set e=0 outside the inherited cover. This formula and
all endpoint rational intervals serialize the entire cap. Zero and upper
clipping knots are rational; the producer constructs their exact locations
when computing the cap mass. No numerical root search is involved.

Since 0<=Lm-Llo<=eta and |m-Lm|<=H*d^2/8,

    0<= e-r <= H*d^2/4+eta <=delta,
    delta=2145/(4*4096^2)+2/10^12
         =0.00003196299276080322... .

Positive-part and upper clipping preserve the inequalities because r<=w40.
One must interpolate SIGNED m before clipping: interpolation of already
clipped endpoint values can create a first-order kink overpayment.

Consequently, on the ENTIRE physical Hilbert space,

    0 <= Enew-Kminus <= delta I,   Enew=V* e V.

This is a full operator error bound, not an error estimate only on the
anchor. Enew<=E40 and ||Enew||<=M=3114203/250000. Its exact two-sided mass
is about 16.0171294915683, compared with SM40's 16.772529359375.
There are 62407 affine pieces, 35064 nonzero. No full-frequency integral
of a source, new original multiplier cutoff, or Fourier-tail deletion is used.

## Reuse the COMPLETE original physical anchor

Retain the SAME original basis

    f1=sin(2*pi*(37/64)x)+(4096/3013)*sinh(x/2),
    f2=sin(2*pi*(37/64)x)-sinh(x/2).

The accepted repaired signed certificate, verified by the inherited
physical-anchor inverse checker, gives the COMPLETE form lower

    [ (Astar-Kminus)(fi,fj) ] >= diag(1/8000,1/24).

It follows from its retained diagonal/cross bounds and an exact positive
2x2 determinant reserve; its omitted positive high-frequency form is PSD.
We do NOT bound the omitted positive mixed entry by the retained cross bound.

The physical norm Gram G=[<fi,fj>] has trace 2.69940124646... <27/10.
Its entries are evaluated natively by the producer and independently
bounded by rational sine/cosine Taylor remainders and positive hyperbolic
series in the replay. For coefficient vectors c, ||sum c_i fi||^2<=27/10||c||^2.
Thus

    [ (Astar-Enew)(fi,fj) ] >= mu_affine I,
    mu_affine=1/8000-(27/10)*delta
              =0.0000386999195458313... >0.0000386.

This covers the full anchor and both previously stopping rays, which are
linear combinations in it. It concerns unlifted physical functions only.

## Pay for the SAME 890-column Taylor/Young construction

Let R be the e-weighted Fourier analysis. Let R0 be its original 24-bit
Taylor approximation on the SAME 107 clusters and orders, totaling 890
columns. Taylor's uniform phase remainder is independent of the choice
of nonnegative frequency density. The new mass is smaller, so the old mass
gives a valid Hilbert-Schmidt and hence operator error bound

    ||R-R0||^2 <=e2=2B*mass40*2^-48=1.31093587862896e-13.

All packet orders are rechecked. The affine density has rational moments,
so an exact weighted-moment realization is available; no 890-column Gram,
Hankel factorization or source inverse has been assembled in this test.

Choose tau=2^-23, and define the usual finite-column-plus-identity cap

    Ctau=(1+tau)R0*R0+(1+1/tau)e2 I >=R*R=Enew.

Its UPPER overpayment must also be paid: R0 is not interchangeable with R.
With sqrt(M)<s=353/100 and sqrt(e2)<u=363/10^9,

    0<=Ctau-Enew<=p_tau I,
    p_tau=tau*M+2*(1+tau)*s*u+(2+tau+1/tau)*e2
          =0.000005147440996177414... .

This follows by expanding R0=R+(R0-R), bounding both cross terms, and
including both quadratic error payments. In particular the cross term
2*(1+tau)*s*u is essential; omitting it would be an invalid reverse bound.
The corresponding COMPLETE original anchor therefore obeys

    [ (Astar-Ctau)(fi,fj) ] >=mu_Young I,
    mu_Young=1/8000-(27/10)*(delta+p_tau)
             =0.0000248018288561523... >0.0000248.

This explicitly passes a realizable Taylor/Young comparison on the same
anchor. It does not establish its global or energy-dual acceptance.

## GitHub-first inputs and independent checks

Parent #345: successful run 40451367065, source
30d4597b8c3fd68886899ba89e278e66de661dce, artifact 12710727196,
archive SHA256 a15f8ff4a6161f3b2a84201ec1ff7fba5591b35f29dd009422848b5bc84166c8.
The parent result JSON hash is
19af532b6bbd4a808854696b2a993e7ebd966e04da27fdd5f55e8b736668770b;
the original negative-geometry JSON hash is
a693261c31f01a4a1e11ea6400e5173435a8260b41b1f6b43aa6f67f784ccb7f.

Repaired signed anchor: successful run 40260136876, source
8844685d3e72a3d38f943b084b6e5bc70ef3d09c, artifact 12623752657,
archive SHA256 2cc62e9fe52f38b021166605e40402f3d8aa4980f1148d7e3738ca3b1afa82ea,
JSON SHA256 264fd853ca006a578d76369ac5bd4588a2097145b829fbba7036693f29b04044.

The focused workflow verifies both run/source/artifact/archive chains and
all three matched JSONs; replays the inherited physical-anchor Loewner
reserve; builds the new native endpoint cap; independently reconstructs
all clipping integrals, grid coverage, global error, physical Gram trace,
Taylor orders and both Young payments with stdlib exact rational arithmetic.
The replay does not independently re-prove native digamma endpoint balls;
their native-library standing and analytic source/domain standing remain
separate from exact arithmetic replay. No FFT, quadrature, or matrix solve.

Regression checks saturate the interpolation curvature constant, handle
crossing zero and upper clipping, verify the reverse Young cross term,
and distinguish anchor positivity from global positivity.

W-ODD-NEG, complete original 470-source/inverse response, remaining signed
Schur, independent original-domain review and even/CC27/Weil/RH remain OPEN.
No inherited coercivity floor or obligation status is changed.
