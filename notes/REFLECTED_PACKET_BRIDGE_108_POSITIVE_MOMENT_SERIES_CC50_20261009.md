# RPB108 CC50 — Constructive exact moment-tail coordinates in the form norm

Date: 2026-10-09 UTC. Publication base dba345728e137f6b76ef972a81f74882459c919c.
[Definitions](../docs/TERMINOLOGY_RPB108_POSITIVE_MOMENT_SERIES_CC50.md).
This makes CC49's moment-tail direction constructible without catastrophic
physical projection subtraction. It is not a native source-action Gram.

## 1. Positive Legendre coefficient formula

Let B=53/50, t=B/2=53/100. For the appropriate parity, the coefficient
of cosh(x/2) or sinh(x/2) on phi_n is the positive number

    a_n=sqrt(2B(2n+1)) t^n/(2n+1)!! S_n(t),
    S_n(t)=sum_(k>=0) t^(2k)/[2^k k! product_(j=1..k)(2n+2j+1)]. (1)

The opposite parity coefficient is zero. Rodrigues's formula, integration
by parts n times (its endpoint factors vanish), and expansion of exp(tu)
give

    integral_-1^1 exp(tu)P_n(u)du
      =t^n/(2^n n!) integral_-1^1 exp(tu)(1-u^2)^n du,

which evaluates to (1) by the even beta-integrals. This is an elementary
coefficient derivation, not a borrowed spectral-domain assertion.

All summands are positive, and S_n decreases with n. Consequently

    (a_(n+2)/a_n)^2
       <=t^4/[(2n+1)(2n+3)^2(2n+5)]
       <1/(180000)^2 for n>=112.                          (2)

Thus the actual even F112 tail starts with phi112 and the odd tail with
phi113; each subsequent coefficient is at most q=1/180000 times its
predecessor. The positive leading coefficient is never obtained as a
difference of nearly equal moments.

## 2. A lawful logarithmic-form norm bound

For these supported Legendre modes, ||phi_n||_2=1. Their zero-extended
total variation is bounded by

    V_n<=sqrt((2n+1)/(2B))[n(n+1)+2].                       (3)

Indeed |P_n|<=1, and the polynomial derivative identity expressing P_n'
as the sum of (2k+1)P_k over k<n of opposite parity gives
|P_n'|<=n(n+1)/2; the two endpoint jumps add2. The bound |P_n|<=1 on
[-1,1] follows, for example, from its elementary Laplace integral whose
complex integrand has modulus at most1.

The Fourier BV bound is |Fourier phi_n(xi)|<=V_n/(2pi|xi|). Splitting
at R=V_n^2, Plancherel and integration by parts of the scalar tail yield

    ||phi_n||_D^2
       <=log(e+R)+(log(e+R)+1)/(2pi^2)
       <=10n+13, n>=112.                                (4)

For the last conservative estimate, B>=1 gives V_n^2<=(n+2)^5;
e<3, log2<1, log(n+2)<=n+1 and pi>1 suffice. No H1 assumption is made
on the zero extension and no unbounded form is replaced by physical L2.

## 3. Certified constructive truncation

Set n=112 or113 and F=f/a_n, with f the actual matching F112 moment tail.
Then F=phi_n+sum_(k>=1) b_k phi_(n+2k), 0<b_k<=q^k. Let F_K retain
k=0,...,K-1. Minkowski in D, not physical orthogonality in D, gives

    ||F-F_K||_D <=sqrt(10n+13) q^K
                           [(K+1)/(1-q)+q/(1-q)^2].       (5)

Here sqrt(10(n+2k)+13)<=sqrt(10n+13)(1+k). Physical orthogonality is
used ONLY for the normalization correction: the omitted physical norm
squared is <=q^(2K)/(1-q^2), and ||F||_2,||F_K||_2>=1. Hence

    ||f/||f||_2 - F_K/||F_K||_2||_D
      <=sqrt(10n+13){q^K[(K+1)/(1-q)+q/(1-q)^2]
                      +q^(2K)/[2(1-q^2)(1-q)^2]}.        (6)

Exact rational comparisons show errors <1e-3 for K=1, <1e-27 for K=6,
and <1e-59 for K=12 in BOTH parities. These are analytic truncation bounds
for the exact-coefficient normalized approximation, not rounding-error
budgets for a finite signed native matrix.

The machine-readable certificate also encloses the positive relative
coefficients b_k for K=12 using 24-term positive S_n series and outward
square-root rounding at grid1e-80. The term ratios are <1/1600 for all
n>=112, so the omitted S_n series is paid by its first omitted term over
1-1/1600. No floating special function or cancellation supplies the values.
Coefficient interval errors must still be propagated through D and the
actual signed gate in any future source computation.
All58 new exact checks pass; no historical chain total is added.

## 4. What can and cannot be transferred

The normalized high pole profile is within1e-3 of the next physical
Legendre mode in the logarithmic norm, and can be reconstructed to1e-59
with12 positive terms (degrees112..134 even,113..135 odd). This supplies
a stable representation of CC49's compensated tail, whose separate low
moment component must still be retained exactly or enclosed lawfully.

It does NOT prove that the C-Riesz response r/sqrt(beta) is close to that
Legendre mode: applying the actual high inverse is a separate operation.
Nor is1e-3 remotely enough to pay a tiny finite signed margin automatically.
For form-continuous mixed values the D error can be propagated with a
certified form bound, but the actual columns and response Gram remain
unevaluated. Modes beyond111 are not present in NF16 E96's native source.

The high complement207/1000 and E96 finite sign remain valid inputs.
No enriched constrained Schur sign, new whole-aperture certificate,
old-gap-independent collective source-frame bound, RH/F4 or Lean closure
is claimed. Whole-domain original positivity remains21/20.
