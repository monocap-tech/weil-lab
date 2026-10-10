# RPB108 RC11 — uniform gluing for pole-neutral resonant chains

2026-10-10. Independent route consolidation.
Parent: 2ec153d78fb07ed99c22441881e234a08627cf8b (RC10).
Only research/rpb108-route-consolidation is written.

## Result, with the restrictions stated first

A collective gluing rule is proved for ARBITRARILY MANY packets, with a
positive physical guard independent of packet count. The family has two
essential restrictions: exact cancellation of both global pole moments,
and widths shrinking with chain length so that no neighboring prime atom
can overlap.

Precisely, let N>=1 be finite, L=log9, and choose

    0<epsilon<=1/(1000*9^(N-1)),
    x_i=(i-(N-1)/2)L, i=0,...,N-1.

Let h_i be independent arbitrary complex smooth profiles supported in
(x_i-epsilon,x_i+epsilon), and put h=sum_i h_i. Define pole moments

    m_+(h)=integral h(x)exp(x/2) dx,
    m_-(h)=integral h(x)exp(-x/2) dx.

Here "pole-neutral" means m_+(h)=m_-(h)=0. Under this constraint, with
S=sum_i Q(h_i) and E=Q(h)-S, the COMPLETE native form satisfies

    |E| <= (554/575)S,
    Q(h) >= (21/575)S >= (21/500)||h||_2^2.           (1)

The support caps grow without bound as N grows. This is a uniform theorem
on a sparse constrained family, not whole-domain positivity on any enlarged
centered interval. It supplies no bound on arbitrary functions in the gaps
or with nonzero global pole moments.

## Native attachment and full signed poles

Q is the actual native Weil form pinned in RC7--RC10 to
notes/REFLECTED_PACKET_BRIDGE_108_NATIVE_FLUX_CC27_20261008.md,
blob e9a44661f94ee6750fc5ad1fbf7dc719fa3ba482, read at
CC119 5df347d3808ac3282864a657b7380e0f54bf4daa.

Define the signed pole form

    P(h)=conjugate(m_-(h))m_+(h)+conjugate(m_+(h))m_-(h),
    B(h)=Q(h)-P(h).

P is not presumed positive. Q and B are stationary under simultaneous
physical translation. On ordered disjoint supports the separated mixed
kernel of B is -j(d), with

    j(d)=exp(-d/2)/(1-exp(-2d)), d>0,

and the prime atoms are -Lambda(n)/sqrt(n) at +/-log n. Only one orientation
overlaps in each ordered mixed pairing, and the diagonal cross term is
twice its real part. No active prime-power term is dropped.

The global moment condition gives P(h)=0, hence Q(h)=B(h). It does NOT
give P(h_i)=0 for each packet. Those individual signed poles must still be
paid when passing from complete local energies Q(h_i) to B(h_i).

The inherited CC119 anchor gives Q(g)>=eta||g||_2^2 on smooth tests supported
in (-53/50,53/50), eta=1/10^37, under its existing source/domain/high-floor
attachments. This step does not rerun that certificate or assume positivity
on the larger target support.

## Sharper four-copy local floor

Repeat RC10's four-copy anchor probe at centers
(-3/2,-1/2,1/2,3/2)log2 for an arbitrary normalized complex profile
phi supported in (-epsilon,epsilon), epsilon<=1/1000.

All copies and their sum lie inside the anchor. There are three aligned
prime2 pairs, two prime4 pairs and one prime8 pair, with overlap exactly one.
All other atoms are excluded as in RC10. The complete separated continuous
kernel has absolute value <5 on every support product, so each mixed
continuous allowance is at most 10epsilon. Six pairs, each doubled in the
diagonal form, cost at most 120epsilon.

Improve only the rational coefficient enclosures:

    log2>69/100,
    sqrt2<23/16, sqrt8<23/8,
    c_2>12/25, c_4>17/50, c_8>6/25.

The coefficients of prime powers 4 and 8 still use Lambda=log2.
Applying anchor positivity to the SUM of the four copies yields

    Q(phi) >
      [2(3*(12/25)+2*(17/50)+6/25)-120epsilon]/4 + eta
      >= 23/20 + eta.

Thus every arbitrary smooth complex profile f of radius at most 1/1000
satisfies the complete local-energy bound

    Q(f)>=d||f||_2^2, d=23/20.                         (2)

This is a quantitative refinement of RC10's 97/100 bound, using the same
actual anchor and the same complete native form.

## Local poles remain in the budget

Translate each h_i to its profile phi_i supported in (-epsilon,epsilon).
Translation weights of its two moments cancel in P(h_i). Cauchy--Schwarz
and the support bound give

    |P(h_i)|
      <=2 exp(epsilon)||phi_i||_1^2
      <=4epsilon exp(epsilon)||h_i||_2^2
      <=(1/200)||h_i||_2^2,                            (3)

using epsilon<=1/1000 and exp(1/1000)<5/4.
Therefore B(h_i)>= (23/20-1/200)||h_i||_2^2.
Global pole cancellation has not been substituted for individual pole
cancellation.

## All prime-power overlaps, uniformly in N

Put M=9^(N-1). For a pair i<j with k=j-i, the center displacement is
log n with n=9^k<=M.

The width rule implies

    exp(2epsilon)
      <=1/(1-2epsilon)
      <=500M/(500M-1)
      <(M+1)/M
      <=(n+1)/n
      <n/(n-1).

The strict central inequality follows from the exact identity

    (M+1)(500M-1)-500M^2 = 499M-1 > 0.

Thus the displacement interval (log n-2epsilon,log n+2epsilon) contains
NO other integer logarithm. In particular every neighboring prime and
prime-power overlap vanishes. This works for all finite N, not only the
sample chain lengths checked in the script.

Only the aligned atom n=9^k survives. Its coefficient is

    Lambda(9^k)/sqrt(9^k)=log3/3^k,

not log(9^k)/3^k. Its mixed overlap for independent profiles is bounded in
absolute value by ||h_i||_2||h_j||_2. The reverse shift does not overlap.

Fixed width would not justify this isolation for arbitrarily large k:
integer logarithm spacing shrinks as n grows. The explicit width dependence
is essential and prevents this theorem from covering a fixed-width tiling.

## Geometric archimedean allowance and collective summation

All cross distances at index gap k satisfy d>=kL-2epsilon. Thus

    j(d)
      <= exp(epsilon)3^(-k)/(1-exp(4epsilon)81^(-k))
      < (3/2)3^(-k).

Indeed exp(epsilon)<5/4, exp(4epsilon)<2, and
(5/4)/(1-2/81)=405/316<3/2. The profiles' L1 norm product is at most
2epsilon||h_i||_2||h_j||_2. Consequently the complete background mixed bound is

    |B(h_i,h_j)| <= a 3^(-|i-j|)||h_i||_2||h_j||_2,
    a=11/10+3/1000=1103/1000,                         (4)

using log3<11/10. Equation (4) includes every surviving prime atom and the
entire separated archimedean interaction. The poles have already been
handled exactly globally and by (3) locally.

Set z_i=||h_i||_2. The symmetric nonnegative off-diagonal matrix
R_ij=a3^(-|i-j|) has every finite row sum below

    2a sum_{k>=1}3^(-k)=a.

The elementary edge inequalities 2z_i z_j<=z_i^2+z_j^2 therefore give

    |2 Re sum_{i<j} B(h_i,h_j)| <= a sum_i z_i^2.

This is a collective estimate independent of N, not multiplication of
pairwise positivity statements. Since P(h)=0,

    E=Q(h)-sum_i Q(h_i)
     =-sum_i P(h_i)+2 Re sum_{i<j}B(h_i,h_j).

Using (3)--(4),

    |E| <= (1/200+1103/1000)sum_i z_i^2
         = (277/250)sum_i z_i^2
         <= (554/575)S,

where (2) gives S>=(23/20)sum_i z_i^2. The supports are disjoint, so their
physical masses add. The reserves are exactly

    1-554/575 = 21/575,
    23/20-277/250 = 21/500.

This proves (1) for arbitrary finite N and arbitrary complex packet shapes
subject to the two global moment constraints.

## Nonvacuity of the constrained family

For three common profiles at centers -L,0,L, take amplitudes

    (1,-10/3,1).

The two translation-moment weight vectors are (1/3,1,3) and (3,1,1/3).
Each has zero dot product with these amplitudes. Thus both global moments
vanish for ANY common profile; a nonzero smooth profile gives a nonzero h.
Its physical mass is (118/9)||phi||_2^2.

For N>=3 common nonnegative profiles, the two moment constraints have rank
two on the N coefficient variables, leaving an N-2 dimensional space.
Independent profiles permit an even larger family. No asserted near-null
or actual zero vector is used.

## Consolidation consequence and remaining boundary

This establishes a genuine all-count relative gluing theorem using the
actual prime-power coefficients and complete local energies. Two previous
costs are handled explicitly: long signed poles are canceled by stated
moment constraints, and neighboring prime overlaps are excluded by stated
width constraints. Neither is silently dropped.

The next transfer issue is whether useful whole-domain or near-null functions
admit a decomposition with comparable budgets without these restrictions.
The present theorem does not supply that decomposition. In particular:

* shrinking widths leave almost all of the large support interval uncovered;
* nonzero global pole moments retain a signed finite-rank obligation;
* fixed widths activate additional neighboring prime powers at long gaps;
* arbitrary center spacings lose the aligned geometric prime coefficients.

These are concrete arithmetic/decomposition hypotheses, not a consequence
of compactness or of the existing anchor alone. Whole centered positivity
and RC5's near-null decay remain open.

## Fresh validation and standing

scripts/validate_rpb108_rc11_pole_neutral_chains.py passes 147 exact rational
checks: sharper short-prime bounds, anchor support and continuous allowances,
local pole costs, geometric decay constants, reserves, integer-isolation
and row-sum controls at selected finite N, and an exact nonzero pole-null
three-packet coefficient vector. Exponential enclosures use rational Taylor
sums with geometric tail bounds.

The universal N statement is proved analytically above; finite controls are
not treated as a proof by sampling. No actual critical mode is evaluated.
The whole 1.06 certificate remains unchanged. No whole-aperture extension,
negative original vector, RH/F4 theorem or Lean closure is claimed.
Other branches and historical files remain unchanged.
