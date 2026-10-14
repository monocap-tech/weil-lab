# RC264 — nested Fourier tails in the inverse comparison

Parent: `551c3c6ac13dbbf7972356a6f73bcdcc3dca26f4` (RC263).
Branch: `research/rpb108-route-consolidation`.

RC264 evaluates the unchanged degree-1024 physical residual polynomial's
Fourier tail at V1=3U/2 and V2=2U, where U remains the actual augmentation's
retained half-bandwidth. These additional frequency cutoffs reduce the
inverse comparison weight on the distant Fourier tail. The actual rational
augmentation, two sources, four response trials per parity, chosen Z,
Legendre cutoff 1024, and explicit prime cutoff 2048 are unchanged.

| Actual original-action inverse upper | RC263 | RC264 |
| --- | ---: | ---: |
| Even source | 0.123820499 | 0.119404268 |
| Odd source | 0.115159769 | 0.114911466 |

Displayed upper bounds are rounded outward; the certificate stores exact
rational enclosures. The signed-gap lower bounds improve to approximately
-0.030845072 even and -0.017828650 odd. Both remain negative. These negative
lower bounds do not certify a negative actual gap, and neither source's
positive signed gap is certified.

The model outside-energy lower bounds at (3U/2,2U) are approximately
(0.00197519795,0.00011384100) even and
(0.00010339704,0.00002516087) odd. The tiny high-space trace remains useful
at the even 3U/2 cutoff; the contraction cap is active at the other three
cutoffs, where the triangle bound is used instead. All model tail energies
in this paragraph precede the subsequent full finite/global error payment.

## Physical source and Fourier tails

As in RC263, write the actual physical residual source

    g = D e = G0 Pbase-G Z = p+q+f,
    ||p||^2=A, ||q||^2<=R, ||f||<=delta.

Here q lies in the matching-parity Legendre space above degree 1024 and is
orthogonal to the complete retained space. The error f includes every
retained coefficient uncertainty, actual-s uncertainty, original global
model fault and rational augmentation comparison fault. No orthogonality
is assigned to f.

For each new V, the pinned RC262 Fourier helper computes an exact rational
enclosure [Y_lower,Y_upper] for ||P_(|xi|>V) p||^2. It retains all diagonal
and off-diagonal pairs of the complete polynomial through degree 1024.
The spherical-Bessel endpoints, diagonal tail recurrence, boundary identity,
outward accumulator and pi displacement allowance are unchanged. These
identities apply at every queried V, and each endpoint satisfies z>400.

There is no old RC261 numerical tail at the new V. The helper's low-degree
control is supplied the independently valid Parseval interval [0,A512],
where A512 is the exact norm squared of the principal polynomial through
degree 512. The output explicitly labels this as a Parseval control; it
does not claim an independent RC261 numerical tail evaluation at V.
The retained degree-1024 norm is also checked against pinned RC263.
The two new tail intervals must be strictly ordered.

## Complete model tail lower bounds

Let C_V be the ideal band operator compressed to the physical interval and
H project onto matching-parity modes above 1024. The RC263 Poisson argument
gives

    ||H C_V H|| <= min(1, 4 B V sum_(n>1024, matching parity)
                                  z_max^(2n)/((2n+1)!!)^2) = K_V.

The scalar series uses its first matching degree and a decreasing geometric
ratio. A cap of one follows from positivity and contractivity, independently
of the size of the trace bound. C_V is not assumed to be a projection.
With E=sqrt((A-Y_lower) K_V R), the model outside energy satisfies

    ||P_out,V(p+q)||^2 >= max(0,Y_lower-2E).

This follows by physical low/high orthogonality, positivity of I-C_V and
Cauchy--Schwarz for C_V. Independently, the Fourier triangle inequality gives

    ||P_out,V(p+q)||^2 >= max(0,sqrt(Y_lower)-sqrt(R))^2.

The larger of these two outward-rounded lower bounds is retained as L_V.
The high-space trace bound is useful only where its computed value permits;
no smallness assumption is imposed at the larger cutoffs. All infinitely
many omitted modes remain paid through R.

## Inverse weight with two additional cutoffs

The same actual augmented lower form from RC263 is

    G >= eta_tau L + beta_tau C_U,

where L has Fourier multiplier log(e+|xi|). For each of the same 1000 rational
tau candidates, let

    I=eta_tau+beta_tau,
    O0=eta_tau*log(U+e_lower)_lower,
    Oj=eta_tau*log(Vj+e_lower)_lower, j=1,2.

The inherited exact positive logarithm enclosure is used, with
e_lower=sum_(k=0)^29 1/k!. Only I>O0>0 candidates are eligible. Set wj=1/Oj.
Then w0>w1>w2>0. The inverse multiplier is bounded above by 1/I inside U,
w0 between U and V1, w1 between V1 and V2, and w2 beyond V2. All inside-band
logarithmic growth and all growth beyond V2 are conservatively discarded.

The full-line inverse variational comparison remains valid for the supported
physical source. If X_U_upper is RC263's model outside-energy upper, then

    B_flat = (A+R)/I + (w0-1/I)*X_U_upper,
    B_shell = B_flat - (w0-w1)*L_V1 - (w1-w2)*L_V2.

This is the exact telescoping identity for nested Fourier projections with
upper or lower energy enclosures substituted according to the signs of
their coefficients. It does not presume any shell orthogonality in physical
Legendre coordinates. The validator checks positive B_shell<=B_flat.
The exact finite shell control verifies telescoping and the enclosure signs.
RC263's nonprojective matrix controls are retained.

The weight is bounded above by w0, so all finite and global errors are paid
after the model comparison:

    <e,N^-1 e>_D <= (sqrt(B_shell)+delta*sqrt(w0))^2.

No Fourier location, smoothness or orthogonality of f is assumed. The least
certified correction on the finite tau grid is added to the unchanged
variational center upper and intersected with RC263. The original source
form lower updates the signed-gap lower. No continuous tau optimum is claimed.

N is the chosen positive augmentation of N0; G=D N, G0=D N0, and the
canonical metric remains M=D^-1 L. D has the harmonic diagonal H_n+s.
These augmented lower forms do not give a positive floor for N0.

## Validation and scope

The validator verifies 227 inherited Git blob pins. Exact replay reverses
pin order, Fourier pair order and tau candidate order, uses the inherited
higher precision and longer integration-by-parts replay settings, and
requires exact equality with the saved rational certificate. Earlier prime
and source tail materialization is reused by immutable pins.

From repository root:

    python scripts/validate_rpb108_rc264_frequency_shell_inverse.py --output certificates/rpb108_rc264_frequency_shell_inverse.json
    python scripts/validate_rpb108_rc264_frequency_shell_inverse.py --output certificates/rpb108_rc264_frequency_shell_inverse.json --replay

The full signed rank-639 response and original full auxiliary norm gate
remain unevaluated. The separate canonical eight-source inverse width stays
485647/1000000. Stage I, RH, F4 and Lean remain open/false.

Next: optimize the response trial or tighten the remaining original model
tail and global faults. The present two-source improvement does not certify
the full signed gate.
