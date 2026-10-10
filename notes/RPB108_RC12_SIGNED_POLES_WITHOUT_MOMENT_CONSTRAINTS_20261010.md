# RPB108 RC12 — signed poles paid without moment constraints

2026-10-10. Independent route consolidation.
Parent: 7f4847f7bb8b6be4587615930ddb7f005eed891c (RC11).
Only research/rpb108-route-consolidation is written.

## Result and remaining support restriction

RC11's two global zero-moment constraints are removed. The existing width
rule controls the entire negative pole contribution as well as neighboring
prime overlaps.

Let N>=1, L=log9, and

    0<epsilon<=1/(1000*9^(N-1)),
    x_i=(i-(N-1)/2)L, i=0,...,N-1.

Let h_i be arbitrary independent complex smooth profiles supported in
(x_i-epsilon,x_i+epsilon), put h=sum_i h_i, and set
S=sum_i Q(h_i), E=Q(h)-S. No moment of h is required to vanish. Then

    E >= -(17773/18400)S,
    Q(h) >= (627/18400)S >= (627/16000)||h||_2^2.       (1)

The physical guard is independent of N. All signed pole terms are retained.
This is a one-sided relative-loss estimate; no absolute-value bound on E
with the same constant is asserted.

The union of the small packet intervals remains sparse. Formula (1) proves
positivity on that support family at arbitrarily large caps, NOT whole
positivity on those centered intervals. The shrinking-width and log9-center
conditions remain essential hypotheses of this proof.

## Definitions and inherited native budgets

Q denotes the complete original native Weil form pinned through RC7--RC11 to
notes/REFLECTED_PACKET_BRIDGE_108_NATIVE_FLUX_CC27_20261008.md,
blob e9a44661f94ee6750fc5ad1fbf7dc719fa3ba482, read at
CC119 5df347d3808ac3282864a657b7380e0f54bf4daa.

Define the two linear pole moments and the signed pole form by

    m_+(f)=integral f(x)exp(x/2) dx,
    m_-(f)=integral f(x)exp(-x/2) dx,
    P(f)=conjugate(m_-(f))m_+(f)+conjugate(m_+(f))m_-(f),
    B(f)=Q(f)-P(f).

Q, P and B are stationary under simultaneous physical translation.
The disjoint-support continuous kernel of B is -j(d), where
j(d)=exp(-d/2)/(1-exp(-2d)), and the prime atoms have coefficients
-Lambda(n)/sqrt(n) at both shift orientations.

RC11's four-copy anchor probe and complete interaction estimates give,
BEFORE imposing its global moment constraint,

    Q(h_i) >= d||h_i||_2^2, d=23/20,
    |P(h_i)| <= p||h_i||_2^2, p=1/200,                (2)
    |2 Re sum_{i<j} B(h_i,h_j)|
       <= a sum_i ||h_i||_2^2, a=1103/1000.           (3)

These estimates hold for arbitrary complex profiles under the stated width
rule. They inherit the completed CC119 1.06 anchor and its source/domain/
high-floor attachments, not positivity on any larger target interval.

For clarity, (3) includes ALL prime atoms: the width rule isolates the
aligned displacement 9^k at index gap k, with coefficient log3/3^k.
The complete separated archimedean allowance is at most 3epsilon/3^k
times the packet norm product. Thus the mixed background matrix is bounded
by a3^(-|i-j|); its infinite comparison row sum is a.
Other integer displacements are excluded by RC11's universal inequality
exp(2epsilon)<1+1/9^(N-1). Neither a new-prime truncation nor prime smearing
is used.

Equations (2)--(3) already imply

    B(h) >= (d-p-a)||h||_2^2 = (21/500)||h||_2^2,      (4)

without any global pole condition. RC11 used P(h)=0 to identify Q(h)=B(h).
The new task is to lower-bound P(h) directly.

## Exact negative direction of the signed pole form

Let Omega be the union of the N radius-epsilon intervals. It is symmetric
about zero, regardless of the profiles occupying it. Put

    I = integral_Omega exp(x) dx
      = integral_Omega exp(-x) dx,
    J = |Omega| = 2Nepsilon.

Define even and odd moment coordinates

    e(f)=(m_+(f)+m_-(f))/sqrt2,
    o(f)=(m_+(f)-m_-(f))/sqrt2.

For ANY complex f, including profiles with nonzero moments,

    P(f)=|e(f)|^2-|o(f)|^2.

The L2(Omega) representer of o is sqrt2 sinh(x/2). Its squared physical norm
is exactly

    integral_Omega 2sinh(x/2)^2 dx = I-J.

Cauchy--Schwarz therefore gives the full signed lower bound

    P(f) >= -(I-J)||f||_2^2 >= -I||f||_2^2.           (5)

No parity is assumed for f. Symmetry is a property of the support container.
For comparison, the even representer has norm squared I+J and is orthogonal
to the odd representer. Hence the pole operator on physical L2(Omega) has
its two nonzero eigenvalues I+J and -(I-J).
This identifies the actual negative pole cost; it does not declare the pole
form nonnegative or discard the negative direction.

## The same width rule pays the negative pole cost

The interval centers have exp(x_i)=3^(2i-(N-1)). Thus

    I = 2sinh(epsilon) sum_{i=0}^{N-1}3^(2i-(N-1)),
    sum_{i=0}^{N-1}3^(2i-(N-1))
       = (9^N-1)/(8*3^(N-1))
       < (9/8)3^(N-1).

Since sinh(epsilon)<=epsilon exp(epsilon) and exp(epsilon)<5/4,

    I < (45/16)epsilon 3^(N-1)
      <= 9/(3200*3^(N-1))
      <= 9/3200.                                     (6)

The support weight grows as 3^(N-1), but the width decreases as 9^(-(N-1)).
Consequently the signed negative pole allowance actually decreases with
packet count. The exact cost I-J is smaller still.
The preceding estimate concerns global moments directly, not a sum of
pairwise pole magnitudes.

Combining (4)--(6) immediately proves

    Q(h)=B(h)+P(h)
         >= [21/500-9/3200]||h||_2^2
         = (627/16000)||h||_2^2.                     (7)

It holds for arbitrary amplitudes, phases, shapes, and nonzero pole moments.

## Relative gluing against COMPLETE local energies

To retain the useful relative-energy formulation, write the exact correction

    E = P(h)-sum_i P(h_i)+2 Re sum_{i<j}B(h_i,h_j).

Use the global lower bound (5)--(6), local signed allowance (2), and complete
background cost (3):

    E >= -(9/3200+1/200+1103/1000)sum_i ||h_i||_2^2
      = -(17773/16000)sum_i ||h_i||_2^2.

Since S>=d sum_i ||h_i||_2^2 with d=23/20=18400/16000,

    E >= -(17773/18400)S,
    Q(h)>= (627/18400)S.

Multiplying the reserve by the local floor gives
(627/18400)(23/20)=627/16000, agreeing with (7).
The correction need not have a favorable sign; its negative cost is paid.

## Controls showing the poles really are signed

For three common even profiles at centers -L,0,L, the moment translation
weights are (1/3,1,3) and (3,1,1/3). Coefficients (1,0,-1) yield opposite,
nonzero global moments, so their pole form is NEGATIVE:
the coefficient-level factor is

    2(1/3-3)(3-1/3)=-128/9,

multiplied by the square of the common profile's nonzero moment.
This profile is allowed by the theorem. It verifies that removal of the
zero-moment condition has substance; the proof pays the actual negative
pole direction. It is not a negative original Q vector.

Equal positive coefficients give a positive pole contribution, and complex
coefficients retain P=|e|^2-|o|^2. The bound covers both signs.

## Remaining route boundary

There is now an all-count gluing theorem on the sparse log9 family with NO
global moment restrictions. The remaining limitation is support geometry
and its arithmetic overlap budget, rather than zero-moment cancellation.

The pole estimate itself would allow widths on the scale 3^(-(N-1)) for a
fixed global pole allowance. The all-integer prime-isolation proof uses the
much smaller scale 9^(-(N-1)). This comparison does not authorize widening:
extra prime and prime-power overlaps would then have to be counted and paid.

No decomposition of an arbitrary whole-domain function into these thin
resonant cells is provided. The gaps do not disappear, and generic center
spacings do not preserve the geometric aligned-prime coefficients.
A whole-domain collective estimate or RC5's near-null arithmetic decay
remains open.

## Fresh validation and standing

scripts/validate_rpb108_rc12_signed_pole_budget.py passes 64 exact rational
checks: inherited budget arithmetic, the signed even/odd pole identity,
nonzero moments with both pole signs, exact center-weight sums and integral
enclosures at selected finite N, the all-count geometric comparison, and
both reserves. Exponential bounds use rational Taylor sums and geometric
tail bounds. The universal N statement and exact functional norm are proved
analytically above, not inferred from finite controls.

The whole original 1.06 certificate remains unchanged. No actual critical
mode is evaluated. No whole-aperture extension, negative original vector,
RH/F4 theorem or Lean closure is claimed. Other branches and historical
files remain unchanged.
