# RPB108 DNE12 — First enclosed complete original physical source-square and signed covariance

Date: 2026-10-08 America/Los_Angeles (GitHub UTC October 9). Base DNE11 `06e3ac1ef4e7f24d8ba99d0eabbcbf606f6d44af`. Independent DNE only. [Definitions](../docs/TERMINOLOGY_RPB108_DNE12_NATIVE_E0_INTERVAL.md), [directed-interval certificate reproducer](../scripts/certify_dne12_complete_e0_source_interval.py). Read-only dependencies NF21 and CC58 for the previously certified prime-plus-pole source-square; NF12/CC40 for the exact original low native pairing.

**Classification: genuine complete original-source physical L2-square computational enclosure for normalized constant Legendre e0; independent arch squared-source enclosure; sign/magnitude of arch-versus-(prime+pole) SOURCE covariance; quantitative projection onto e0-only complement. NO 56/58-mode compensated Gram, full F112 residual estimate, corrected Schur sign, all-cap contact exclusion, RH/F4 or Lean theorem.**

## 1. Exact original source (not a pole-free approximation)

Fix a=53/50 and normalized physical e0=1/sqrt(2a) on I=(-a,a), zero elsewhere. CC56's complete original physical source has for x>=0

    sqrt(2a) (L_Q e0)(x) = S0(x)
       =a0+J(a-x)+J(a+x)
         -sum_(n in {2,3,4,5,7,8}) c_n
             [1_(x+ell_n<a)+1_(x-ell_n>-a)]
         +8sinh(a/2)cosh(x/2),                           (1)

    a0=-gamma_E-pi/2-3log2-log pi,
    c_n=Lambda(n)/sqrt(n)>0,
    ell_n=log n,
    J(t)=atanh(exp(-t/2))+atan(exp(-t/2)).

All six ACTUAL prime powers and both shift orientations are present. The final even pole source equals e^(x/2)m_-(e0)+e^(-x/2)m_+(e0), multiplied by sqrt(2a), and retains the ORIGINAL even positive pole sign. Equation (1) contains the full native digamma, primes and pole. No bounded physical full operator on arbitrary functions is claimed; e0 belongs to the fixed polynomial operator domain.

S0 is even, so normalization gives the EXACT physical source-square

    ||L_Q e0||²_(L2(I)) = (1/a)int_0^a S0(x)²dx.       (2)

The aim is a valid finite interval for this TRUE source-square, NOT the native form Q(e0,e0), the pole-free H source-square, or the full E112/F112 source residual.

## 2. Why monotone Darboux bounds are legal

The archimedean constant-mode source is

    A(x)=a0+J(a-x)+J(a+x).

Since J'(t)=-j(t), j(t)=exp(-t/2)/(1-exp(-2t))>0 strictly decreasing, for 0<x<a

    A'(x)=j(a-x)-j(a+x)>0.                              (3)

The even pole-source term 8sinh(a/2)cosh(x/2) also strictly increases on x>0. The prime-source indicator in (1) is a piecewise constant integer, with jumps only at native panel locations x=|a-log n|. For a<log n<2a it turns on, and for log n<a the second orientation is always on while the other turns off. Across any rational panel [l,r], outward interval comparisons of log n with a-l,a-r or a+l,a+r yield an exact possible indicator range {0},{1},{2}, or the necessary adjacent range.

Thus an outward enclosure for S0 over EACH panel follows from evaluating A and the pole at interval endpoints plus the interval prime counts. Squaring this interval bounds S0² for every real x in that panel; no assumption that S0² is monotone is required. Multiply by panel width and add with outward rounding.

The certificate `certify_dne12_complete_e0_source_interval.py` uses mpmath.iv directed intervals at 35 decimal digits with exactly 60,000 rational panels over [0,a-delta], delta=10^-8. It encloses the NORMALIZED interior contribution as

    0.08342746333974804... < I_interior
                             <0.08450130374049884...  (4)

All interval arithmetic operations include their rounding directions. The numerical literals in the displayed endpoints are deliberately abbreviated; the reproducer checks the final wider strict rational thresholds rather than trusting those abbreviations.

## 3. Paying the endpoint logarithmic square, not sampling an infinity

At t=a-x->0+, the exact CC56 primitive has the decomposition

    J(t) = -(1/2)log t +CJ-int_0^t r(s)ds,
    CJ=log2+pi/4,
    r(s)=j(s)-1/(2s).

DNE11's holomorphic Cauchy bound on radius5/2 yields |r(s)|<11/(5/2-delta)<5 for 0<s<delta. Every one of the six native prime powers contributes EXACTLY one negative translation source near x=a, because delta<log2 and delta<2a-log8. The regular part of the complete source is

    B(t)=a0+CJ+J(2a-t)-sum_n c_n
          +8sinh(a/2)cosh((a-t)/2)-int_0^t r(s)ds.

Directed interval evaluation at the two endpoints, together with the analytic |r|<5 and the fixed active dictionary, certifies |B(t)|<10 for all 0<t<delta. Thus

    |S0(a-t)| <= (1/2)(-log t)+10.

Writing L=-log(delta), the exact positive improper square majorant is

    I_endpoint
       <=delta/a*[1/4*(L²+2L+2)+10*(L+1)+100]
       < 0.00000366743.                               (5)

This controls the entire omitted singular endpoint and does not extrapolate a bounded source value at x=a. The other endpoint is already included by evenness and the 1/a normalization in (2).

Combining (4),(5), with outward endpoint errors paid, gives the first fixed native DNE source-square certificate:

    +-----------------------------------------------------+
    | 0.0834 < ||L_Q e0||²_(L2(-a,a)) < 0.0846.           |
    +-----------------------------------------------------+                  (6)

This is a reproducible directed-interval computational certificate. It is not a Lean proof or a verified full E112 source Gram.

## 4. Separately certified archimedean source-square and original cross-covariance

Use (3) and the same 60,000 panels for A(x)², with an endpoint bound using B_arch(t)=a0+CJ+J(2a-t)-int_0^t r(s)ds and the same safe |B_arch|<10. The source-square enclosure is

    7.0819 < ||L_arch e0||² < 7.0828.                   (7)

NF21 independently certifies the full prime-plus-pole SOURCE-square `K=(L_prime+L_pole)e0`, preserving prime-prime, pole-pole and signed prime-pole cross terms. The read-only [CC58 replay](https://github.com/monocap-tech/weil-lab/blob/research/rpb108-coupled-continuation/notes/REFLECTED_PACKET_BRIDGE_108_COMPENSATED_CORRELATION_CC58_20261009.md) records strict rational dependency bounds

    7.244 < ||K||² < 7.245.                            (8)

Consequently the exact physical polarization identity (ALL the original source terms have been combined before squaring)

    2<L_arch e0,K>
       =||L_Q e0||²-||L_arch e0||²-||K||²

gives the genuinely signed native source covariance certificate

    +------------------------------------------------------------+
    | -14.245 < 2<L_arch e0,K> < -14.241.                         |
    +------------------------------------------------------------+                (9)

This quantitatively confirms the pronounced cancellation seen in DNE11's noncertified pilot; in DNE12 the aggregate and arch sectors have an outward interval proof and the prime/pole sector is imported from the independently certified NF21/CC58 arithmetic. Neither source-square is the same object as a Weil quadratic-form entry.

The results are robust to the choice of prime panel boundaries because ambiguous indicator cells are conservatively enclosed in the directed Darboux computation. No unproved cancellation sign is inserted.

## 5. A first physical projection (one low coordinate only)

The authenticated CC40/NF12 original signed native rational enclosure has

    Q(e0,e0) in [401520842754207446870744,
                401520842754207446870745] / 10^25.

In particular

    0.0015 < Q(e0,e0)^2 < 0.0017.

Since the physical low vector e0 is normalized and L_Qe0 is a genuine physical source,

    ||(I-|e0><e0|)L_Qe0||²
          =||L_Qe0||² -Q(e0,e0)^2.

Combining the strict rational bounds yields

    +---------------------------------------------------------------+
    | 0.0817 < ||(I-|e0><e0|)L_Q e0||² < 0.0831.           |
    +---------------------------------------------------------------+              (10)

**This is NOT the F112 high residual:** all the other 55 EVEN low Legendre directions have not been projected off. Thus (10) is at most a one-column upper bound on the TRUE F112 physical residual after all 56 low components are removed; it is not the compensated source residual after NF19's two-high correction.

NF20/CC57 warn that the physical residual bound is only a SUFFICIENT majorant for the full form-dual high inverse and may fail despite a positive Schur complement. No positivity is inferred from (10).

## 6. Controls, custody, and DNE13 task

New actual arithmetic result: (6) complete original physical e0 source-square, (7) arch squared source, (9) native SIGNED arch/(prime+pole) source covariance, and (10) one-coordinate corrected physical residual.

The script is executed with the exact original `J` at all interior panel endpoints and does not rely on Taylor-truncating the native source. The only analytic estimate is the fully paid logarithmic endpoint tail. It uses a numerical outward interval library (mpmath.iv), so it is a computational certificate with explicit mathematical monotonicity and endpoint justification, not a formally verified arbitrary-precision kernel.

A separate earlier e0 mpmath point quadrature returned ~0.0836618343819 for the full source norm-square; this value is INSIDE (6) and is a sanity check, not a premise of the interval enclosure. The code also checks the original Q00 rational pin exactly, independent of floating-point quadrature.

**DNE13:** Extend the source enclosure from the original constant-mode e0 to the first compensated NF19 pair `w=e0-C2^-1B*e0`, retaining the TRUE signed arch/prime/pole source before squaring. Build the 58-column compensated residual matrix P2 from the 56 source vectors and pay the errors in the low near-critical basis. The first checkpoint should evaluate a single actual near-critical EVEN witness direction and compare the physical-source upper bound to its retained `S2` energy. If the scalar physical criterion is inadequate, move to the genuine C-form-dual residual rather than falsely inferring a negative original Weil vector.

No other branch was changed. Whole supported positivity remains internally certified to a=21/20; a=53/50 full sign, all-cap first-contact exclusion, F4, RH and Lean remain OPEN.
