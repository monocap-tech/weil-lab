# RPB108 CC48 — Actual F112 moments are tiny, not a frame reserve

Date: 2026-10-09 UTC. Publication base a3271faa85fb69c280462702d1a4990f21ddfc3f.
[Definitions](../docs/TERMINOLOGY_RPB108_HIGH_MOMENT_TAIL_CC48.md).
Inputs: NF10 original F112 physical coercivity17/100 at53/50 and CC47's
form-domain constrained Schur theorem. No E112/source Gram is presumed.

## 1. Rigorous physical moment-tail bounds

Set B=53/50, t=B/2=53/100. Every polynomial through degree111 belongs
to E112. Approximate cosh(x/2) by its degree110 Taylor polynomial and
sinh(x/2) by its degree111 Taylor polynomial. Taylor's integral remainder
through order111 (respectively112) gives uniform errors at most

    epsilon_e,point <=2 t^112/112!,
    epsilon_o,point <=2 t^113/113!.                  (1)

Every needed derivative is bounded by exp(t)<2. An elementary rational
series bound certifies that inequality; the even polynomial's degree111
coefficient and the odd polynomial's degree112 coefficient are zero.
Physical orthogonal projection is a best L2 approximation, so for the
actual moment tails f_e,f_o,

    ||f_e||_2^2 <=(212/25)t^224/(112!)^2 =:eta_e^2,
    ||f_o||_2^2 <=(212/25)t^226/(113!)^2 =:eta_o^2.   (2)

Here 212/25=4 times the physical interval length2B. No pole sign or
normalization is changed by the Taylor approximation.

## 2. Native high Riesz beta bounds and strict positivity

On F112, C=original Q satisfies C>=kappa||.||_2^2, kappa=17/100.
By the dual variational identity,

    beta_p=sup_(z in F112) m_p(z)^2/C(z)
           <=eta_p^2/kappa,
    0<beta_e<10^-424, 0<beta_o<10^-429.             (3)

The exact rational bounds are (848/17)t^(2k)/(k!)^2 for k=112,113.
The decimal powers in (3) are checked by integer/fraction comparisons,
not floating eigenvalues or numerical quadrature.

Strict beta positivity also needs justification: cosh and sinh on a
nonempty interval are not polynomials of degree111. Their projected
physical tails are nonzero. Each tail, zero-extended outside the cap,
is piecewise smooth of bounded variation, with Fourier decay O(1/|xi|),
so it belongs to the logarithmic form domain. It is physically orthogonal
to E112 and tests its own moment to ||f_p||_2^2>0. Hence the high moment
functional is nonzero and its C-Riesz norm beta_p is strictly positive.
No positive numerical LOWER bound on beta is certified.

Thus the beta=0 case of CC47 is not the actual E112/F112 case. Approximate
interval data that contain0 cannot license division by an interval or
replacement by beta=0; a stable certificate still needs lawful enclosures.

## 3. Why small beta does not suppress the dangerous response

Let W be the complete high form response, G(x)=C(Wx), and a=m_low-m(Wx).
Riesz Cauchy-Schwarz gives

    |m(Wx)|^2 <= beta G(x).                         (4)

For a low vector with m_low(x)=0, the exact constrained gate is

    K_m(x)=Q_low(x)-G(x)+m(Wx)^2/beta
          =Q_low(x)-C(W_perp x),                    (5)

where W_perp x=Wx-[m(Wx)/beta]r is orthogonal to the normalized high
moment response in the C metric. Therefore

    Q_low(x)-G(x) <= K_m(x) <= Q_low(x).            (6)

The quotient in (5) can be as large as G even when beta is arbitrarily
tiny. Its upper bound is G, NOT eta^2 G. Conversely it can vanish for a
response orthogonal to r. The pole-tail norm does not measure this angle.

On the entire parity low space the correction a*a/beta has rank at most1.
It vanishes on ker a, of dimension at least55 when E112 has56 vectors in
that parity. Strict positivity still requires S=Q_low-G to be positive on
that kernel. Tiny beta supplies no lower frame bound on those directions.
For an actual moment-zero h=x+y, (2) does yield
|m_low(x)|<=eta_p||y||_2, but it does not control G or the finite Schur sign.

## 4. Exact angular and positive-level controls

Use one low coordinate and two high coordinates, with high C=I,
Q_low=1, mixed row B=(2,0), and zero low moment. For a high moment
epsilon(1,0), beta=epsilon^2, a=-2epsilon, G=4 and K=1. For high
moment epsilon(0,1), beta is the SAME, a=0 and K=-3. Arbitrarily small
identical tails can thus give opposite constrained signs solely through
their angle to the complete response. These are structural controls,
not actual Weil matrices.

A genuine positive-level control has Q_low=2, C=I, B=(1,0) and moment
epsilon(0,1). Original Q is positive (eigenvalues (3+sqrt5)/2,
(3-sqrt5)/2,1), and K=1. Shift the ENTIRE physical mass by mu=1/2:
Q_low becomes3/2, C becomes I/2, W=(2,0), G=2, beta=2epsilon^2 and
K=-1/2. The moment-zero restriction crosses at the original positive
level (3-sqrt5)/2; high coercivity stays positive. Small beta and its exact
shift scaling do not prevent genuine crossing or distinguish original
from positive-level shifted nulls. The local differential genuine-crossing
control likewise is not excluded by a statement about tail size alone.

The validator checks (1)'s exponential envelope, both rational beta
bounds, the response-angle controls at three epsilon values, and the
full physical shift. It does not compute actual W, r, beta or a native
constrained gate. All29 new exact checks pass; no historical total is added.

## 5. Remaining target

We have quantified the actual high pole tail using complete F112
coercivity, but have not evaluated the source-response directions it
observes. The missing target is the signed response Gram on ker a and
its coupling to the normalized high moment response, not a smaller
Taylor tail. NF15 E80 plus F112 still leaves32 intermediate directions;
neither full E112 nor a native gate is made positive here. Whole-domain
anchor remains21/20. Contact exclusion, the collective defect-relative
frame estimate, RH/F4 and Lean closure remain open.
