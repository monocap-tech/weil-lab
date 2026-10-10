# RPB108 RC8 — signed pole compensation for a long prime jump

2026-10-10. Independent route consolidation.
Parent: d2c3f8ccc2cbf1672faacd98849a43ac74b30f84 (RC7).
Only research/rpb108-route-consolidation is written.

## Concrete result

At the SAME packet separation log9, the actual full native localization
correction has both signs, depending on packet width:

* normalized smooth nonnegative packets of half-width 1/1000:
  E_chi < -241/375;
* sufficiently close smooth approximants to normalized flat packets of
  half-width 1/8:
  E_chi > 61/660.

The second calculation retains the additional prime8 and prime11 overlaps.
Both calculations include the signed archimedean and pole interactions.
Thus the pole term can compensate for a long prime jump on some profiles,
but cannot supply an automatic nonnegative gluing correction. These are
cross-interaction results, not negative original vectors, near-null estimates,
or a new positivity certificate.

## Pinned native form and localization

Use RC7's complete native form, inherited from CC27
notes/REFLECTED_PACKET_BRIDGE_108_NATIVE_FLUX_CC27_20261008.md,
blob e9a44661f94ee6750fc5ad1fbf7dc719fa3ba482, read at
CC119 5df347d3808ac3282864a657b7380e0f54bf4daa.

For disjoint real packets u,v the mixed pairing is

    Q(u,v) = integral integral u(x)v(y)[2cosh((y-x)/2)-j(y-x)] dx dy
             -sum_n c_n integral u(x)v(x+log n) dx,

when the support of v is strictly to the right of u; the reverse shift has
zero overlap in this mixed pairing. Here j(d)=exp(-d/2)/(1-exp(-2d)),
c_n=Lambda(n)/sqrt(n), and all active prime powers are included.
The diagonal cross term is 2Q(u,v).

Set L=log9 and u(x)=phi(x+L/2), v(x)=phi(x-L/2), with phi nonnegative,
even and L2-normalized. Choose smooth square-sum localization functions
constant (1,0) on the left support and (0,1) on the right support, with
transitions in the gap. Then the localized products are exactly u,v and

    E_chi(u+v)=Q(u+v)-Q(u)-Q(v)=2Q(u,v).

Each local product has support radius at most 1/8 in the wider test, so
translation places it inside the certified 1.06 anchor. Cutoffs can have
support diameter at most 2.12: the two supports and gap allow this choice.
The long displacement log9 exceeds 2.12.

## Exact pole threshold

For any such even profile define m_phi=integral phi(x)cosh(x/2) dx.
The exact pole mixed pairing is

    P(u,v)=(sqrt9+1/sqrt9)m_phi^2=(10/3)m_phi^2.

The aligned prime9 mixed pairing is exactly -log3/3. Even before paying the
negative archimedean interaction and other prime overlaps, pole compensation
therefore requires

    m_phi^2 >= log3/10.

More generally, aligned prime-power n requires m_phi^2 >= Lambda(n)/(n+1).
This is only a necessary pole-only threshold, not a sufficient full signed
bound. At the central displacement the continuous kernel is exactly

    K_cont(log9)=10/3-27/80=719/240.

A pointwise positive continuous kernel does not dominate the prime atom on
arbitrarily narrow L2-normalized packets: their continuous mixed mass tends
to zero while the aligned atom remains fixed.

## Narrow smooth packets: compensation fails

Take phi smooth, even, nonnegative, supported in (-epsilon,epsilon),
epsilon=1/1000. The packets fit inside cap 11/10 since exp(1099/500)>9.
Also exp(11/5)<10, so the only active prime powers are 2,3,4,5,7,8,9.

The log9 atom has overlap one. All other prime overlaps vanish, since the
closest lower displacement log8 is separated by more than 2epsilon:
exp(1/500)<9/8. No higher prime displacement overlaps either.
The coefficient is log3/3, NOT log9/3.

Every cross distance lies in (2,12/5). In this range the pole kernel is <5,
j(d)<1, hence |K_cont(d)|<6. Physical Cauchy--Schwarz gives
||phi||_1^2 <= 2epsilon. Thus the entire continuous mixed term has absolute
value at most 12epsilon. Since log3>1,

    Q(u,v) < -1/3+12epsilon,
    E_chi < -2/3+24epsilon = -241/375.

This retains both pole moments and the complete separated archimedean kernel.
No sign is inferred for the full Q(u+v) from the correction alone.

## Wider profile: compensation succeeds after all overlaps are paid

Use the flat reference profile

    phi_e(x) = 1/sqrt(2e) for |x|<e, zero otherwise, e=1/8.

We compute only its separated cross pairing and then pass to smooth
nonnegative even L2-normalized approximants supported in (-e,e).
The continuous kernel is bounded on the separated support product, pole
moments are continuous there, and each prime shift pairing is L2-continuous.
Consequently the strict cross bound below persists for sufficiently close
smooth approximants. This argument needs no extension of the complete
self-energy form to rough tests.

The packets fit cap 123/100 since L<11/5 and L/2+e<123/100.
The cap has exp(123/50)<12. Among its active powers 2,3,4,5,7,8,9,11,
the ONLY nonzero mixed atom overlaps are 8,9,11:

    r_n = max(0,1-|log n-log9|/(2e)),
    r_9 = 1, r_8 < 3/5, r_11 < 1/5.

The exclusions and strict allowances follow from

    exp(1/4)<9/7,       exp(1/4)>9/8 and >11/9,
    exp(1/10)<9/8,      exp(1/5)<11/9.

Thus prime7 and all smaller powers are outside the overlap range; prime11
must be retained. The reverse shift remains zero. For n>11, either the cap
or the support separation excludes the interaction.

Since cosh(x/2)>=1, m_phi^2 >= ||phi_e||_1^2=2e=1/4.
The pole mixed pairing is therefore at least 5/6. Every cross distance
satisfies d>L-1/4>19/10, by exp(43/20)<9.
Using exp(19/20)>5/2 and exp(19/5)>40 gives j(d)<1/2.
The full archimedean mixed loss is consequently less than
(1/2)||phi_e||_1^2=1/8.

Retain the correct coefficients and bound

    c_8=log2/sqrt8 < 1/4,
    c_9=log3/3 < 11/30,
    c_11=log11/sqrt11 < 8/11.

Then the complete mixed pairing, with all active atoms, obeys

    Q(u,v)
      > 5/6 - 1/8 - (1/4)(3/5) - 11/30 - (8/11)(1/5)
      = 61/1320 > 0.

Therefore sufficiently close smooth approximants satisfy E_chi>61/660.
This proves a genuine sign change of the localization correction at fixed
log9 displacement. It does not establish whole positivity at cap 1.23.

## Consequence for the consolidation route

A displacement-only assertion that the poles pay long prime jumps is false.
Their contribution depends on profile moments; prime losses depend on
translation correlations; widening changes which neighboring primes overlap.
An adequate quantitative gluing estimate must couple these quantities to the
actual complete local energies, or restrict them to genuine near-null vectors
and prove RC5's required decay.

The sufficient relative-loss target E_chi>=-theta_B sum_j Q(chi_j h),
theta_B<1, remains unproved. Neither sign test decides it: narrow packets can
have large local self-energies. No critical-mode evaluation is performed.

## Validation and standing

scripts/validate_rpb108_rc8_pole_compensation.py passes 37 fresh exact rational
checks. It uses rational Taylor lower bounds for exp(x) and a geometric upper
bound on the omitted positive tail. Checks cover caps, support exclusions,
neighboring-prime overlaps, coefficient bounds, the complete continuous
allowance, and both strict signed bounds. The analytic identities and smooth
approximation argument are stated above; the check count is not a proof of a
whole functional inequality.

The original 1.06 certificate and RC5 canonical guard remain unchanged.
No new positive aperture, negative original vector, arithmetic outward-decay
estimate, RH/F4 theorem or Lean closure is claimed. Other branches and
historical files remain untouched.
