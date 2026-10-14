# RC263 — high-mode band leakage and direct weighted inverse bound

Parent: `7c7ed9587d0347daf2752d54447e556f690b6136` (RC262).
Branch: `research/rpb108-route-consolidation`.

RC263 uses the omitted model output's orthogonality to the entire retained
Legendre space, rather than only to one retained polynomial. Its interaction
with the ideal low-frequency band is bounded by a tiny high-mode trace.
The resulting source estimate is then evaluated directly in the inverse
comparison norm before paying all finite and global errors. No output
cutoff, source, trial, Z, or actual rational augmentation changes.

| Actual full-source bound | RC262 even | RC263 even | RC262 odd | RC263 odd |
| --- | ---: | ---: | ---: | ---: |
| Outside Fourier energy upper | 0.006810417 | 0.004213348 | 0.005740809 | 0.003412856 |
| Original-action inverse upper | 0.187684022 | 0.123820499 | 0.171214893 | 0.115159769 |

The new actual outside-energy lower bounds are approximately 0.0031169155
even and 0.0021166769 odd. These are rigorous lower enclosures after all
faults, not estimates of the actual inverse response. Signed-gap lower
bounds improve to approximately -0.035262 even and -0.018077 odd, and remain
negative. Original source forms are about 0.088559 and 0.097083, respectively.
No source signed gap or Stage I closure is certified.

Display upper bounds are rounded outward. The certificate stores exact
rational enclosures. All comparisons in the table concern the same actual
operator, sources, domains and norms.

## Full low/high decomposition

Write the actual physical source as

    g_e = D e = G0 Pbase-G Z = p+q+f,

where p is RC262's complete retained model polynomial through degree 1024,
q is the complete model output in degrees above 1024, and f contains all
finite-coefficient and actual-s uncertainty and global model errors. Let

    ||p||^2=A,  ||q||^2<=R,  ||f||<=delta,
    delta=sqrt(E_finite)+E_global_fault_norm.

The model remainder q is orthogonal to every Legendre mode through 1024.
It has the same parity as p. The finite and global errors are subsequently
paid with a full operator-norm bound; no low/high orthogonality is assigned
to those errors.

Let C=J_U^*J_U be the ideal Fourier-band projection compressed to the
physical interval and let H project onto the matching-parity Legendre
modes above 1024. C is positive and contractive but need not satisfy C^2=C.
The model decomposition satisfies Hp=0 and Hq=q.

For the retained polynomial, RC262 supplies the exact A and a Fourier
outside-energy interval [Y_lower,Y_upper]. Therefore

    <p,Cp> <= A-Y_lower.

## Universal high-mode band trace

For normalized physical Legendre modes, the Fourier transform and mass are

    F(P_n)(xi)=2B(-i)^n j_n(2 pi B xi),
    mass(n)=2B/(2n+1).

The real spherical-Bessel Poisson bound from RC260,

    |j_n(t)| <= |t|^n/(2n+1)!!,

and exact frequency-power integration give

    <P_n,C P_n>/mass(n)
      <= 4 B U * z_max^(2n)/((2n+1)!!)^2,

where z_max=2 pi_upper B U. Summing matching-parity n>1024 and paying the
decreasing geometric ratio yields

    trace(H C H) <= K.

The scalar is exactly RC260's universal Poisson-tail coefficient evaluated
at unit band energy. Its use here follows from the normalized diagonal
formula above and does not restrict p to the old degree-64 Z input.
The outward bounds are K<=1e-60 even and K<=9.1e-59 odd.

Since H C H is positive, its norm is at most its trace. Hence

    <q,Cq> <= K R.

Cauchy--Schwarz for the positive form C gives the interaction bound

    |<p,Cq>| <= sqrt((A-Y_lower) K R) = epsilon.

The validator pays every positive rounding allowance; epsilon is bounded
by 1e-30 in both parities. The exact finite-dimensional controls use a
nonprojective positive contraction, a two-dimensional low space and a
one-dimensional high space to verify the trace, Cauchy and weighted-fault
steps. They explicitly check C^2 differs from C.

## Model and actual outside-energy intervals

Low/high physical orthogonality and Fourier Parseval give

    ||P_out(p+q)||^2
      = Y_p+||q||^2-<q,Cq>-2 Re<p,Cq>.

Using positivity and contractivity of C,

    max(0,Y_lower-2 epsilon)
      <= ||P_out(p+q)||^2
      <= min(A+R,Y_upper+R+2 epsilon).

This replaces the much larger unstructured cross allowance in the earlier
one-vector orthogonality estimate. All infinitely many high modes are still
paid through R and the analytic trace K. No omitted-output energy is
identified with a Fourier outside-band energy.

Add/subtract delta at the level of Fourier-projected norms, square with
outward rounding, and intersect with RC262 to enclose the actual full-source
outside energy. The validator checks 0<=X_lower<=X_upper<=S, where S is the
inherited valid actual full-source physical-energy bound.

## Direct inverse comparison norm

The actual rational augmented G retains the established lower form

    G >= eta_tau L + beta_tau C,

with full canonical comparison error still paid. L has multiplier
log(e+|xi|). For each of the same 1000 rational tau candidates, set

    I=eta_tau+beta_tau,
    O=eta_tau*log(U+e_lower)_lower.

Here e_lower=sum_(k=0)^29 1/k! is a rigorous lower bound on exp(1).
The logarithm uses the inherited exact positive atanh-series enclosure.
This slightly sharpens the earlier outside floor eta_tau*log(U)_lower.
Only candidates with I>O>0 are used.

A full-line inverse variational comparison bounds the supported source by
the Fourier weight W equal to 1/I inside the band and 1/O outside. If M_out
is the new model outside-energy upper, then

    ||W^(1/2)(p+q)||^2
      <= (A+R)/I + M_out*(1/O-1/I) = B_model.

The Fourier weight is bounded above by 1/O. Therefore every finite and
global physical error is paid through

    ||W^(1/2) f|| <= delta/sqrt(O),
    <e,N^-1 e>_D <= (sqrt(B_model)+delta/sqrt(O))^2.

This is a bound on the actual augmented inverse correction. The global
regular-kernel, prime-arithmetic, pole-Taylor and rational-augmentation
errors remain fully included. The source model's ideal C does not replace
the actual rational augmentation in G or N.

The least certified correction on the finite tau grid is added to the
unchanged variational center upper; the actual inverse-response enclosure
is intersected with RC262. Original source form lower bounds update the
signed-gap lower bounds. No continuous tau optimality is claimed.

N is the chosen positive augmented operator, N0 the original Weil operator,
and M=D^-1 L the canonical metric. D still has the harmonic diagonal H_n+s.
None of the augmented lower forms supplies a positive floor for N0.

## Validation and scope

Generation and exact replay verify 224 inherited blob pins. Replay reverses
pin and candidate order and requires exact equality with the stored rational
certificate. Exact nonprojective matrix controls check the new geometric
and weighted-error steps. Earlier retained Fourier, prime and infinite-tail
certificates are reused by pins; their large calculations are unchanged.

From repository root:

    python scripts/validate_rpb108_rc263_high_mode_inverse.py --output certificates/rpb108_rc263_high_mode_inverse.json
    python scripts/validate_rpb108_rc263_high_mode_inverse.py --output certificates/rpb108_rc263_high_mode_inverse.json --replay

The retained physical source cutoff stays 1024, the prime cutoff stays 2048,
and there are still two sources and four trials per parity. The full signed
rank-639 response and original full auxiliary norm gate are unevaluated.
The separate canonical eight-source inverse width remains 485647/1000000.
Stage I, RH, F4 and Lean remain open/false.

Next: retain more frequency variation in the inverse multiplier or optimize
the response trial using these strengthened bounds. Further uncertainty
reduction is not asserted to certify the full signed gate by itself.
