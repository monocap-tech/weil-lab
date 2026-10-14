# RC266 — integrated contour bound for the unchanged rational augmentation

Parent: `e27e100e5e3e32d3d8c2d53244fad2d3771e1428` (RC265).
Branch: `research/rpb108-route-consolidation`.

RC266 certifies a positive signed gap for the current odd P1-source test.
The even P0-source bound also improves but its signed gap is not certified
positive. This is one individual source test, not positivity of the entire
odd sector or the full rank-639 response criterion. Stage I remains open.

| Actual source bound | RC265 | RC266 |
| --- | ---: | ---: |
| Even original-action inverse upper | 0.116973243 | 0.104695285 |
| Odd original-action inverse upper | 0.114207160 | 0.083217799 |
| Even signed-gap lower | -0.028414047 | -0.016136089 |
| Odd signed-gap lower | -0.017124345 | **+0.013865017** |

Displayed upper/lower bounds are rounded outward. Exact rational enclosures
are stored in the certificate. A negative lower bound is not a negative
actual-gap witness. The odd lower bound is positive after every error payment.

No trial, source, retained degree, prime output cutoff or actual augmentation
changes. The improvement comes from a much sharper analytical comparison of
the exact RC115 rational kernel with the ideal band restriction. It replaces
the old radius-two worst-frequency comparison allowance with an integrated
bound on a finite grid of rational ellipse radii, retaining parity.

## Exact operator being compared

Let B=11/10 and J_U be the physical Fourier restriction to [-U,U], using
exp(-2 pi i xi x). The actual rational operator Fhat remains RC115's
degree-2400 Taylor kernel, with its physical Chebyshev expansion truncated
at exactly n=495 even and n=783 odd. Its pi_0, band U and rational coefficients
are unchanged. X_(n,U) denotes the corresponding exact-kernel Chebyshev
truncation, solely as a comparison operator.

The actual augmented physical form is still

    G = G0 + lambda Fhat* Fhat,

with the unchanged exact rational lambda. Neither Fhat nor its product is
replaced by J_U or C_U=J_U*J_U in an asserted operator identity.

## Rational Laurent ellipse and matching parity

Choose rational r>1 and set

    t=(w+w^-1)/2, |w|=r, b=(r-r^-1)/2.

For f_xi(t)=exp(-2 pi i B xi t), the ellipse bound is

    |f_xi(t)| <= exp(2 pi B b |xi|).

Cauchy's Laurent coefficient estimate gives physical Chebyshev coefficients
|a_j(xi)|<=2 exp(2 pi B b |xi|) r^-j for j>0. For a physical input of parity p,
opposite-parity Chebyshev moments vanish exactly. Equivalently use the parity
kernel (f_xi(t)+(-1)^p f_xi(-t))/2; its ellipse bound is no larger.

Let m be the first omitted matching degree: m=n when n has parity p and
m=n+1 otherwise. Thus m=496 even and m=783 odd. The exact matching-parity
tail is bounded by the geometric series

    |K_tail(x,xi)| <= 2 r^-m exp(2 pi B b |xi|)/(1-r^-2).

This is a bound on the parity-restricted physical integral operator. It
retains the same n and the same actual rational kernel; it is not a change
in truncation rank. The exact controls check Chebyshev parity, the opposite
physical moments, and the scalar geometric sum.

## Integrate the frequency dependence

Take the inherited rigorous pi_upper, and write

    a=2 pi_upper B b,
    g=m log(r)_lower-a U.

All queried gaps are positive. Integrating the squared kernel bound first
in x and then in xi gives the physical Hilbert--Schmidt bound

    ||J_U-X_(n,U)||^2
      <= [8 B/(a(1-r^-2)^2)] r^(-2m) (exp(2aU)-1)
      <= [4/(pi_upper b(1-r^-2)^2)] exp(-2g).

The second inequality drops the negative one. The same pi_upper is used
in the pointwise exponential and in its exact elementary frequency integral;
the denominator is not independently substituted for an exact-pi denominator.

For comparison, replacing the frequency integral by its maximum times 2U
would give

    16 B U exp(-2g)/(1-r^-2)^2.

The certificate stores both bounds and checks the integrated bound is smaller.
It also recomputes the radius-two all-degree rectangle (without the parity
improvement), recovering RC112's contour setup. This control must be below
the inherited RC115 complete J-to-Fhat error budget before it is sharpened.

The finite rational radius grid is r=k/100 for 145<=k<=180. Each of its 36
certificates is saved. The chosen radii are 41/25 even and 79/50 odd. The
least certified bound on this grid is used; no continuous ellipse optimum
is claimed.

## Exact arithmetic for logarithms and exponentials

The existing positive atanh-series logarithm enclosure supplies log(r)_lower.
For x=2g>0, the new helper encloses exp(x) by positive Taylor terms with
outward rational arithmetic. The lower sum is bounded above by exp(x).
The upper sum includes a geometric upper remainder: after term N-1, the
next term is divided by 1-x/(N+1). Here 0<x<100 and N is 400 in generation,
440 in replay, so the remainder ratio is strictly below one.

Reciprocating these positive enclosures bounds exp(-x). Generation uses
120-digit term grids; replay uses 140 digits, more terms and reversed
summation. Both must give the same saved 80-digit rational interval.
The accepted Hilbert--Schmidt bounds are outward rounded on the inherited
60-digit grid. No floating-point value is used in any acceptance decision.

## Finite rational kernel error and physical/canonical comparison

The exact Taylor/pi model error is separately paid. Let e0 be RC115's
rigorous pi-phase error plus real-axis Taylor remainder. A uniform error e0
has constant Chebyshev coefficient error at most e0 and every other
coefficient error at most 2e0. Therefore the retained finite kernel error is
at most 2n e0 pointwise and has physical squared operator norm at most

    e_X^2 = 16 n^2 B U e0^2.

The validator recomputes this physical bound and conservatively takes the
larger of it and RC115's saved finite-model squared error. It then pays

    delta_new^2 = (sqrt(HS_integrated_upper)+sqrt(e_X^2))^2_upper.

This bounds J_U-Fhat on the physical parity space. It also bounds the same
error from the canonical carrier, since the physical inclusion has norm at
most one: the canonical Fourier multiplier log(e+|xi|) is at least one.
The derivation does not infer a physical bound merely from a canonical
operator estimate.

| Complete comparison squared error | Inherited | RC266 |
| --- | ---: | ---: |
| Even | approximately 3.81438e-6 | less than 1.012269e-14 |
| Odd | approximately 1.66027e-5 | less than 6.141745e-19 |

## Actual augmentation action error and retained lower form

Physical Fourier restriction has norm at most one. For E=Fhat-J_U, without
any commutation assumption,

    Fhat*Fhat-J_U*J_U = E*J_U+Fhat*E,
    ||Fhat*Fhat-J_U*J_U|| <= delta_new(2+delta_new) = epsilon_new.

Consequently, for the same exact selected polynomial Z,

    ||lambda(Fhat*Fhat-C_U)Z||^2
      <= lambda^2 epsilon_new^2 ||Z||^2.

The exact physical norm of the pinned Z is evaluated with Legendre masses.
The resulting squared global augmentation faults fall from approximately
1.888576e-6 to 5.002169e-15 even, and from 1.040554e-5 to 3.833624e-19 odd.
Every original regular-kernel, prime-arithmetic and pole-Taylor fault remains
unchanged and is added in norm. The retained coefficient and actual-s
uncertainty are also unchanged. No error component is silently removed.

The original lower form G0>=gamma L-p C_U is unchanged. Reverse Young with
the new canonical comparison gives, for each eligible 0<tau<1/5,

    G >= eta_tau L+beta_tau C_U,
    eta_tau=gamma-lambda(1/tau-1)delta_new^2,
    beta_tau=lambda(1-tau)-p.

The same actual operator is used for both this coercivity estimate and the
source action-error payment. The reduced comparison error permits smaller
tau values. The finite search contains the former 1000 candidates and
tau=k/10^j for 1<=k<=99, 3<=j<=9, after deduplication: 1639 candidates.
Candidates must have positive eta and satisfy the inherited inverse-weight
ordering. Selected tau is 79/10000000 even and 41/1000000000 odd. There is no
claim of continuous tau optimality.

## Source inverse and positive odd-source signed gap

RC265's physical model decomposition p+q, all three frequency cutoffs and
their retained Fourier energy enclosures are unchanged. Its common unknown
omitted energy u=||q||/sqrt(R) is still bounded over the full interval [0,1].
The same coupled-shell lemma is evaluated with the improved actual lower
form and smaller complete physical error norm. If B_joint is the resulting
model comparison and w0 the maximum inverse weight, every remaining finite
and global error is paid through

    <e,N^-1 e>_D <= (sqrt(B_joint)+delta_source sqrt(w0))^2.

The least correction on the finite tau grid is added to the unchanged valid
variational center upper. The actual inverse upper is intersected with RC265.
That inverse upper is then subtracted from the original actual source-form
lower:

    signed_gap_lower = F00_lower - inverse_response_upper.

For the odd source this is strictly positive. The validator explicitly checks
the odd inverse upper is below F00_lower, and that each updated response and
gap interval remains consistent with the inherited lower/upper endpoints.
The even-source lower bound remains negative, leaving that test unresolved.

N is the chosen positive augmentation of N0; G=D N, G0=D N0, and the canonical
metric remains M=D^-1 L. D retains the harmonic diagonal H_n+s. No augmented
floor is asserted as a positive floor for the original Weil operator N0.

## Validation and scope

Generation and exact replay verify 233 inherited Git blob pins. Replay
reverses pin, ellipse and tau order, changes positive-exponential precision
and term count, reverses its term accumulation, and must reproduce the
entire rational certificate exactly. Earlier Fourier/prime calculations are
reused through immutable pins. The new exact controls and all inherited
nonprojective shell, joint-energy and global-error controls pass.

From repository root:

    python scripts/validate_rpb108_rc266_integrated_contour_augmentation.py --output certificates/rpb108_rc266_integrated_contour_augmentation.json
    python scripts/validate_rpb108_rc266_integrated_contour_augmentation.py --output certificates/rpb108_rc266_integrated_contour_augmentation.json --replay

There are still two tested sources and four response trials per parity.
The full signed rank-639 response and original full auxiliary norm gate
remain unevaluated. The separate eight-source canonical inverse width stays
485647/1000000. Stage I, RH, F4 and Lean remain open/false.

Next: improve or change the even-source response trial, and extend the
signed calculation beyond these two source tests. The positive odd-source
test does not certify the full auxiliary response norm below one.
