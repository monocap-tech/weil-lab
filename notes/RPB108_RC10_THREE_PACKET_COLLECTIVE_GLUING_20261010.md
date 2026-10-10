# RPB108 RC10 — collective gluing of three narrow packets

2026-10-10. Independent route consolidation.
Parent: 2fcbd5d5978236b583c78b1aebb8df930c7d30f7 (RC9).
Only research/rpb108-route-consolidation is written.

## Concrete result

Four coherent translated copies INSIDE the completed anchor improve RC9's
narrow-profile self-energy floor from 39/100 to 97/100. This stronger budget
pays every mixed interaction in a THREE-packet log9 chain, including its
outer prime81 jump.

Let epsilon=1/1000, L=log9, and let h_-,h_0,h_+ be arbitrary complex smooth
functions supported respectively in intervals of radius epsilon about
-L,0,L. Define h=h_-+h_0+h_+, S=Q(h_-)+Q(h_0)+Q(h_+), and E=Q(h)-S.
Then

    |E| <= (1136/1455) S,
    Q(h) >= (319/1455) S
         >= (319/1500)||h||_2^2.                      (1)

The profiles are independent; no evenness, nonnegativity, shape matching,
or favorable relative phase is assumed. The union fits cap 221/100.
This is positivity on three small separated support intervals, NOT whole
positivity on the centered interval of radius 2.21. No whole-aperture
certificate is extended.

## Definitions and inherited actual form

Q is the complete original native Weil form used by RC7--RC9. Its separated
continuous kernel, including the archimedean interaction and both signed
pole factors, is

    K_cont(d)=2cosh(d/2)-j(d),
    j(d)=exp(-d/2)/(1-exp(-2d)), d>0.

The prime atoms are -c_n at both +/-log n, with
c_n=Lambda(n)/sqrt(n). For ordered disjoint supports only the positive shift
has a mixed overlap; the paired diagonal cross term is 2 Re Q(h_i,h_j).
All atoms with supported overlaps are retained.

The attachment is pinned to
notes/REFLECTED_PACKET_BRIDGE_108_NATIVE_FLUX_CC27_20261008.md,
blob e9a44661f94ee6750fc5ad1fbf7dc719fa3ba482, read at
CC119 5df347d3808ac3282864a657b7380e0f54bf4daa.
Stationarity applies to the FULL form, including poles.

The inherited CC119 certificate, under its existing source/domain/high-floor
attachments, gives Q(g)>=eta||g||_2^2 for smooth g in (-53/50,53/50),
eta=1/10^37. This step neither reruns that certificate nor assumes positivity
on the target cap. Write x_i=||h_i||_2 for physical packet norms.

## A four-copy anchor probe

Take an arbitrary complex smooth phi supported in (-epsilon,epsilon),
with ||phi||_2=1 and q=Q(phi). Put b=log2 and form copies at centers

    -3b/2, -b/2, b/2, 3b/2.

They are disjoint. Since b<7/10,

    3b/2+epsilon < 53/50,

so their SUM is inside the actual certified anchor, with physical mass 4.
Stationarity makes each copy's complete self-energy equal to q.

At separations b,2b,3b the only mixed atoms are respectively prime powers
2,4,8. Their aligned overlaps are exactly one, even for complex phi.
The reverse shift does not overlap. Other integer displacements are excluded
by the fresh bounds

    exp(2epsilon)<3/2,
    exp(2epsilon)<4/3 and <5/4,
    exp(2epsilon)<8/7 and <9/8.

These exclude the nearest neighboring integers at each separation, hence
all other prime powers as well. There are three pairs at b, two at 2b,
and one at 3b. The correct coefficients obey

    c_2=log2/sqrt2 > 2/5,
    c_4=log2/2     > 3/10,
    c_8=log2/sqrt8 > 1/5.

In particular Lambda(4)=Lambda(8)=log2; their coefficients are not formed
with log4 or log8.

The complete continuous mixed allowance is <5||phi||_1^2<=10epsilon
for EACH of the six pairs. For the b pairs this is RC9's bound on cross
distances in (1/2,1). For the 2b,3b pairs, distances lie in (1,53/25).
There the pole kernel is <4 because exp(53/50)<3, and j(d)<1:
exp(1/2)>3/2 and exp(2)>4 imply
j(d)<(2/3)/(1-1/4)=8/9. Hence |K_cont(d)|<5 throughout.
No pole or archimedean cross term is omitted.

If g is the sum of the four copies, the anchor and all signed mixed terms
give

    4eta <= Q(g)
           < 4q - 2(3*(2/5)+2*(3/10)+1/5)
                + 12*(10epsilon)
           = 4q - 4 + 3/25.

Thus q>97/100+eta. By scaling, translation and the zero case,

    Q(f) >= d||f||_2^2, d=97/100,                      (2)

for every arbitrary complex smooth profile f supported in an interval of
radius epsilon. This bounds the COMPLETE self-energy. It is an anchor-derived
width estimate, not a direct estimate of the singular archimedean self-term.

## Every interaction in the target three-packet chain

The centers -L,0,L fit cap 221/100 because L<11/5 and L+epsilon<221/100.
For the adjacent pairs the displacement is L=log9. Only the prime9 atom
overlaps. For the outer pair the displacement is 2L=log81. Only the prime81
atom overlaps. The nearest-integer exclusion bounds are

    exp(2epsilon)<9/8 and <10/9,
    exp(2epsilon)<81/80 and <82/81.

They exclude ALL other prime-power displacements regardless of how many
are active on the larger cap. The remaining aligned overlaps need not be
one; for independent complex profiles their absolute values are bounded
by x_i x_j using physical L2 Cauchy--Schwarz.

Adjacent cross distances lie in (2,12/5), where |K_cont|<6 as in RC8--RC9.
Outer cross distances lie in (4,23/5). There the pole kernel is <11 because
exp(23/10)<10, and j(d)<1, so |K_cont|<12.
For two radius-epsilon profiles, their L1 norm product is at most
2epsilon x_i x_j. Consequently the FULL mixed estimates are

    |Q(h_-,h_0)| <= r x_- x_0,
    |Q(h_0,h_+)| <= r x_0 x_+,
    |Q(h_-,h_+)| <= s x_- x_+,

where

    r = log3/3 upper + 12epsilon
      = 11/30 + 12epsilon = 142/375,
    s = log3/9 upper + 24epsilon
      = 11/90 + 24epsilon = 329/2250.

The outer coefficient is Lambda(81)/sqrt81=log3/9,
NOT log81/9. Both archimedean and pole interactions are paid in r,s.
In particular s<r.

## Collective budget, rather than multiplying pairwise statements

The total correction obeys

    |E| <= 2r(x_-x_0+x_0x_+)+2s x_-x_+.

Applying 2xy<=x^2+y^2 to each edge gives

    |E| <= (r+s)(x_-^2+x_+^2)+2r x_0^2
         <= kappa (x_-^2+x_0^2+x_+^2),
    kappa=2r=284/375 < d=97/100.

This includes all three pairs in one budget; it does not apply RC9 twice
and silently charge the middle packet twice. Equation (2) gives S>=d sum x_i^2,
so

    |E| <= (kappa/d) S = (1136/1455)S.

The disjoint supports give ||h||_2^2=sum x_i^2, and

    d-kappa = 319/1500,
    1-kappa/d = 319/1455.

This proves (1) with arbitrary amplitudes and complex phases.

## General finite-packet interface extracted here

For disjoint radius-epsilon intervals with center gaps delta_ij>2epsilon,
a fully paid absolute mixed coefficient is

    r_ij =
      sum_{n: |log n-delta_ij|<=2epsilon} Lambda(n)/sqrt(n)
      +2epsilon sup_{d in [delta_ij-2epsilon,delta_ij+2epsilon]} |K_cont(d)|.

The sum ranges over prime powers with a possible overlap. It is not a
new-prime-only truncation. Exact overlap information can reduce the sum.
Set R_ii=0 and R_ij=r_ij. Then

    |E| <= x^T R x <= ||R|| sum_i x_i^2.

Whenever ||R||<=kappa<97/100, the same anchor-derived floor (2) proves

    Q(sum_i h_i) >= (1-kappa/d)sum_i Q(h_i)
                  >= (d-kappa)||sum_i h_i||_2^2.

A maximum row-sum bound is one elementary sufficient bound on ||R|| for
this real symmetric nonnegative matrix. RC10 evaluates that criterion on
the three-packet chain. This is a concrete finite collective interface, not
a theorem that its inequality holds for arbitrary configurations or caps.

## What remains open

The proven family is sparse and narrow. It does not cover functions in the
gaps, wide pieces, arbitrary packet counts, or the whole canonical support
domain at any enlarged centered aperture. More pieces can accumulate prime
and continuous mixed costs; pole correlations grow with separation.
The present absolute estimate may become too costly even where the true
signed form is positive.

The remaining route is a collective gluing bound on a lawful whole-domain
partition, or RC5's decay restricted to genuine near-null vectors. This step
does not evaluate such a vector or establish the global endpoint estimate.

## Validation and standing

scripts/validate_rpb108_rc10_three_packet_gluing.py passes 50 fresh exact
rational checks: the four-copy anchor support, all atom exclusions,
continuous allowances, correct prime-power coefficients, the 97/100 floor,
the three-packet interaction budget, and both positive reserves.
Exponential bounds use rational positive Taylor sums and geometric tail
bounds. Finite algebra controls illustrate the universal square identities;
they do not replace the analytic proof above.

The original whole 1.06 certificate remains unchanged. No whole-aperture
extension, negative original vector, RH/F4 theorem, or Lean closure is
claimed. Other branches and historical files remain unchanged.
