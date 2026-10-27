# Compact original Birman–Schwinger: near-critical witness and affine-cap stop

Weil-Lab, local date 2026-10-26. Continues draft #346,
`71c5b0c00640f31e7f6a89d97e658a44de15bf81`. Draft/unmerged.

## Decision and stopping point

The bounded compact-operator feasibility investigation reveals an actual
near-critical direction of the ORIGINAL odd problem. A fixed exact rational
physical candidate, verified independently of the numerical eigensolver,
has COMPLETE signed action

    0 < Q_o(f) < 8e-18 ||f||^2.

The original true negative action has a certified positive lower from ONE
short frequency cell. The variational quotient therefore proves

    ||Kminus^(1/2) Astar^-1 Kminus^(1/2)|| > 1-6e-12.

This is a LOWER bound, not the desired upper <=1. It does not prove a
global strict gap, a kernel, an original negative direction, or RH.

The SAME candidate proves the #346 affine envelope is too large globally:

    <f,(Enew-Astar)f> >4e-9,
    ||Enew^(1/2) Astar^-1 Enew^(1/2)|| >1+3e-10.

Consequently the whole-operator comparison Astar>=C fails for every
C>=Enew, including EVERY Young parameter for that same envelope.
The #346 two-dimensional anchor result remains valid; its global extension
was never certified. This scoped stop prevents a large matrix campaign
based on its anchor feasibility alone.

STOP this affine-cap whole-operator route. Do not escalate trial dimensions,
quadrature or uniform cap precision automatically. The next method must
handle the near-critical mode with true negative action or a sufficiently
matched, mode-sensitive error bound. No full 470/484 or 890-moment assembly,
full SI29 response, strong residual or global norm upper is computed here.

The new probe is a legitimate ORIGINAL physical odd test function, not a
claim of exact membership in J470. This pass does NOT stop the exact
J470 energy-dual source gate, all Galerkin methods, or alternative criteria.
It stops the GLOBAL comparison by caps dominating this particular Enew.

## Compact formulation and finite inverse diagnostic

Retain the original supported odd carrier, B=11/10, original r=(kappa-m)_+,
kappa=1/1000, true pole, full seven-prime multiplier, and inherited
Astar>=kappa_star I, kappa_star=33621/10^9.

The negative Fourier analysis R=sqrt(r)V is Hilbert–Schmidt because its
kernel is bounded on a finite physical interval and r has finite mass.
Indeed ||R||_HS^2<=2B*mass40<37. Thus Kminus=R*R is trace class,
and B=Kminus^(1/2) Astar^-1 Kminus^(1/2) is compact positive under the
inherited realization/domain hypotheses. Compactness itself does not
supply the missing norm upper. All domain review remains OPEN.

For a finite trial synthesis Phi, set A_N=Phi* Astar Phi,
K_N=Phi* Kminus Phi, Z_N=Phi A_N^-1 Phi*. The nonzero spectrum of
Kminus^(1/2) Z_N Kminus^(1/2) is that of A_N^-1/2 K_N A_N^-1/2.
Exact Galerkin monotonicity gives Z_N<=Astar^-1; nested trial values are
LOWER approximants, not upper certificates. Numerical stabilization cannot
replace an infinite operator-norm remainder.

Use the fixed physical basis

    sin(n*pi*x/B)/sqrt(B), n=1,...,N,
    sinh(x/2)/sqrt(sinh(B)-B),

at the PREDECLARED N=32,64,128 (dimensions 33,65,129). Include the true pole.
Its exact-form physical Gram is used consistently; raw coefficient geometry
is not mistaken for physical orthogonality. These spaces target the complete
original operator, not another family of positive-source restrictions.

Ordinary binary64 computes the FULL original signed physical matrix Q_N,
true K_N on all 973 negative-cover leaves, then the MATCHED A_N=Q_N+K_N.
No original matrix is replaced by a derivative or component bound.
Arch quadrature orders 512/1024 and negative orders 8/16 are compared.
Negative positive-part crossing roots are split numerically from the
retained fine endpoint grid; this is not a certified root enumeration.
The initial unsplit 8/16 negative blocks differed by 3.7e-5; after splitting,
the physical spectral difference is about 3.3e-14. The signed block differs
by about 3.8e-12, much LARGER than the eventual native signed ray action.
Thus the numerical pilot CANNOT certify that action or a global gap.

The finite positive minimum is approximately 0.310 at these sizes. The
largest numerical BS eigenvalue is indistinguishable from one at binary64
accuracy. All matrices, physical Grams, quadrature settings and actual
finite inverse outputs are retained; they remain numerical diagnostics.

The inherited normalized pole is also used as an unchanged physical RHS.
Partition A_N=[[G,M],[M*,H]], physical RHS (b,c). The actual calculation pays

    T=H-M*G^-1 M,
    h=c-M*G^-1 b,
    response=b*G^-1 b+h*T^-1 h.

It agrees with the direct full solve. For N=128, the numerical pole response
is about 1.350994, including an extra matched response about 0.006173.
The forcing changes with M; it is not held fixed during elimination.
These are NOT the full J470/14-dimensional SI29 response and are not
certified infinite inverse entries.

## Fixed candidate: numerical discovery, native verification

Take the N=32 signed generalized eigenvector only as a candidate generator.
Convert its coefficients to the unnormalized sine/sinh basis, round ONCE
to exact rationals with denominator dividing 10^12, and commit the candidate
JSON. The proof does not consume a numerical eigenvalue or quadrature error.

    f(x)=sum_(n=1)^32 a_n sin(2*pi*(5n/11)x)+b sinh(x/2), |x|<=B,

and zero outside. Every coefficient is fixed in the candidate JSON.
The original Fourier convention, physical carrier and pole are unchanged.
This piecewise analytic function has 1/xi Fourier decay, so its logarithmic
form energy and squared-log multiplier action are integrable at infinity;
operator attachment retains the inherited analytic/domain review.

At native 512 bits, the complete physical original signed functional is
computed using the same accepted normalization as #345:

    Q_o(f)=(c0+tail)*||f||^2 + integral_0^(2B) k(s)(||f||^2-C_f(s)) ds
           -2 sum log(p)/sqrt(n) C_f(log n) -2<f,sinh(x/2)>^2,
    c0=psi(1/4)-log(pi), k(s)=exp(s/2)/sinh(s).

All seven powers 2,3,4,5,7,8,9 lie below exp(2B) and are physically clipped
as before. The arch infinite tail has 64 positive Laplace terms plus an
explicit geometric remainder. No frequency cutoff is used in Q_o.

For the 66 exponential terms, group the translated correlation EXACTLY as

    C_f(s)=sum_j (d_j+t_j*s) exp(lambda_j*s).

An O(66^2) setup permits O(66) evaluation. This avoids an enormous global
monomial expansion and does not invoke the stopped #341 representation.
Use exprel to evaluate (||f||^2-C_f(s))/s analytically at zero. Arb's complex
integrator at 512 bits, tolerance 2^-160, explicit evaluation/depth limits
encloses the regularized integral. Possible kernel poles cause nonfinite
enclosures/subdivision, not an ignored singularity.

Independent native identities check sine orthogonality/pole overlaps,
the grouped correlation against the direct double exponential sum at
zero, the support endpoint, 1/7 and all seven prime shifts, its zero-shift
derivative identity, the quarter-digamma constant, and the selected Fourier
point against a separate exponential integral formula.

The resulting signed value is approximately

    Q_o(f)=7.305152636441038e-18, ||f||^2 approximately one.

Its POSITIVE interval is quantized outward at denominator 10^40. The native
balls and independently recomposed rational physical components are retained.
The scalar native calculation takes about one second locally, guarded at
120 seconds. Native-library integration, exact rational replay, analytic
identification and independent domain review have separate standing.

## One cell certifies the true BS lower and the cap failure

Use the fixed original fine cell

    I=[1755/4096,439/1024], d=1/4096, w40=72377/1000000.

It belongs to the #346 grid, lies above frequency 1/4, and has no zero or
upper clipping in the affine cap. Its endpoint affine heights are checked
strictly between zero and w40 using the retained exact lower endpoints.
Native Fourier and original multiplier intervals at its exact midpoint,
together with the global derivative bounds

    |fhat'|<=11, |m'|<132,

give a positive Fourier absolute lower F_I and r>=r_I>0 on the whole cell.
The Fourier derivative bound follows from Cauchy–Schwarz, B and the actual
native physical norm interval, NOT a coefficient-sum surrogate.
Then Kminus(f)>=k_lo=2*d*r_I*F_I^2, paying both frequency signs.

For xi>=1/4, pi*xi>=3/4. The trigamma derivative series gives the sharper
LOCAL arch curvature bound

    2*(22/7)^2*(64/27+104/125),

where 64/27 bounds the n=0 complex denominator and 104/125 bounds the
remaining positive tail by its first term plus an integral.
Adding the exact seven-prime curvature upper gives |m''|<786 here.
The new cap used GLOBAL H=2145 in every fine cell. With no clipping on I,

    e-r=m-L_endpoint_lower+2145*d^2/8
       >=(2145-786)*d^2/8.

Endpoint lower rounding HELPS this lower bound; it is not an unpaid error.
Consequently its actual overpayment, not a worst-case norm upper, satisfies

    Enew(f)-Astar(f)
       >=2*d*((2145-786)*d^2/8)*F_I^2-Q_o(f)
        =4.102497713879951e-9... >4e-9.

Outside I and its reflection, Enew-Kminus is PSD and can be discarded.
Hence the whole comparison fails, regardless of Young tuning or matrix size.
This is NOT a true signed negative direction: Q_o(f) is strictly POSITIVE.

For positive Astar, the variational characterization of
Astar^-1/2 Kminus Astar^-1/2, which shares its nonzero spectrum with B, gives

    ||B|| >= k_lo/(k_lo+Q_upper) >1-6e-12.

Similarly Astar(f)<=M*norm_upper+Q_upper, M=3114203/250000, yields

    ||B_Enew|| >=1+gap/(M*norm_upper+Q_upper)>1+3e-10.

These are conditional original-operator norm LOWER bounds. No global norm
upper, exact equality at one or failure of true signed positivity is inferred.

## A concrete residual budget, with its exact jurisdiction

For a finite Galerkin trial Phi in the strong domain, define

    A_N=Phi^* Astar Phi, Y=Phi A_N^-1 Phi^* Kminus^(1/2),
    R=Kminus^(1/2)-Astar Y.

Energy orthogonality gives the complete identity

    B-B_N=R* Astar^-1 R <=kappa_star^-1 R*R.

This includes the infinite couplings. It is not a finite-block or
componentwise residual identity. No actual R is evaluated here.
If the trial CONTAINS this exact probe (as do the fixed numerical spaces),
its exact finite BS norm is already >1-6e-12. Thus a certificate relying
ONLY on the scalar coercivity-norm residual upper must achieve

    ||R||^2 < kappa_star*(1-k_lo/(k_lo+Q_upper)) <2.01726e-16

to fit a strict margin. The precise rational ceiling is retained.
This is a necessary budget for THIS sufficient residual allocation, not
a theorem that the actual residual exceeds it or that every method needs
that tolerance. Matched energy-weighted estimates or treating the critical
mode explicitly can change the allocation. Do not launch a large solve
without demonstrating a credible complete-error plan at the relevant scale.

## Custody and standing

GitHub first: #346 run 40454006262 SUCCESS, source
71c5b0c00640f31e7f6a89d97e658a44de15bf81, artifact 12712076196,
archive SHA256 c853b66001e3a36346ce1310df3b60ca694b3b458e8d658a3e6955cf5a14291e,
affine-cap JSON SHA256
8b58972bbdd2f9cb5d00275820ab6d6891feeff3bbd584a1c28231770368f514.
The workflow verifies the run/source/artifact/archive and every extracted
input hash, replays #346, runs the bounded pinned NumPy/SciPy diagnostic,
then verifies the FIXED rational candidate with pinned python-flint 0.8.0
and independently replays all exact compositions and norm/cap inequalities.
The pilot is evidence for candidate selection only. Its numerical quadrature
does not enter the native scalar certificate's acceptance.

W-ODD-NEG, independent original-domain review, exact true signed Schur,
full original inverse response, global true BS norm upper and infinite
remainder remain OPEN. Even/CC27/Weil/RH unchanged. Manifest unchanged.
