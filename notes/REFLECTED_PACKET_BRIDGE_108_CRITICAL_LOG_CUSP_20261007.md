# RPB108: an actual-drive control exactly at the critical threshold

Date: 2026-10-07 UTC. Recovered live head 50c9f97e17ecb9f90d6c348d2f9778afe165f054.
Definitions: [critical inverse-log native-drive control](../docs/TERMINOLOGY_RPB108_CRITICAL_LOG_CUSP.md).
Category: critical derivative promotion / endpoint exclusion.

## Result and why it sharpens the preceding control

The preceding actual-drive power cusp was globally H^(5/8). This pass constructs, using the same actual aperture and boundary constraints, a positive-energy actual-native carrier h which is in Xcrit and even has global Fourier weight r w^3, but is in no global H^s for s>1/2. It has both genuine endpoint moment matches, continuous zero endpoint values, all earlier pure-log/subcritical regularity properties, the actual drive-variation and full-residual Hardy budgets, and the necessary exterior upper-flux sign. Its physical derivative is not L2.

Its actual critical positive-source moment is finite by the pinned source/Fourier comparison. Q(h)>=9e-30 ||h||_2^2>0 by reuse of the certified 97/100 whole-domain result. It is not an eigenvector.

The exact homogeneous interior equation rejects it with a computed leading defect:

    q_h(a-v)=(7/6)log^(-3)(1/v)+O(log^(-4)(1/v)).       (1)

Thus even actual drive attachment and stronger half-order logarithmic regularity do not replace full interior nullity. This is an obstruction to a boundary-only implication, NOT a counterexample to K_a intersect Xcrit -> L2 derivative. No new aperture calculation is performed.

## 1. Actual construction and lawful boundary matching

Reuse the preceding geometry, cutoff and two reflected smooth bumps. Replace the right cusp by f_R(v)=log^(-4)(1/v)chi(v), and the one-sided interior prime-2 cusp by log^(-3)(1/u)chi(u) immediately to the right of x0=a-log 2. Both are zero at their cusp point and on the other side.

Both endpoint inverse moments are absolute: at the right endpoint the only contribution near zero becomes integral^infinity L^(-4)dL; the left endpoint has a support gap. The actual functionals L_R=M_R-2A_R(0) and L_L=M_L-2A_L(0) therefore remain lawful. Their values on the unchanged smooth bumps give exactly the same matrix B as before, with eigenvalues >230. Solving c=B^(-1)L(h0) and subtracting c_R b_R+c_L b_L enforces both genuine moment matches. The coefficients affect only smooth interior pieces.

The same 31 support-separation checks apply. For the actual prime-2 shift, right exterior x0+u enters the interior cusp while right interior x0-v lies on its zero side. All other prime profiles and all bump profiles vanish in the relevant shifted collars. These are actual arithmetic translations, not independently assigned drives.

## 2. Critical logarithmic regularity without any supercritical Sobolev input

For a one-sided log cusp g_q(v)=log^(-q)(1/v)chi(v), q>0, its translated difference obeys

    ||tau_t g_q-g_q||_2^2
       <=C[t log^(-2q)(1/t)+t^2], t sufficiently small.  (2)

The edge region has length O(t) and amplitude <=C log^(-q)(1/t). On the region v>=t, the derivative is bounded by C/[v log^(q+1)(1/v)] near zero. Its squared integral, multiplied by t^2, is O(t log^(-2q-2)(1/t))+O(t^2): set v=exp(-s), split s at half of log(1/t), and bound the exponential tail with its endpoint polynomial. The smooth cutoff region contributes O(t^2). Enlarging constants gives (2).

The Fourier difference-norm calculation with weight log^j(1/t)/t^2 is equivalent at high frequencies to r w^j, for j=1 or 3. Tonelli, the cosine upper split at 1/|xi| and its fixed-phase lower interval give this equivalence just as in the pinned critical matching proof. Inserting (2) leaves integral^infinity L^(j-2q)dL. It is finite if 2q>j+1. Both q=4 and q=3 satisfy this condition even for j=3. Smooth bumps preserve the result. Therefore h has global r w^3 energy, hence Xcrit and its actual critical positive-source moment.

In contrast, for 1/2<s<1 the zero-exterior fractional difference energy contains the positive cross-boundary term

    c_s integral_0^b |h(a-v)|^2/v^(2s) dv
       =c_s integral^infinity exp((2s-1)L)L^(-8)dL
       =infinity.

Thus h is in no H^s with s>1/2; larger s would imply membership at one of these smaller exponents. Its physical derivative also has infinite squared norm, since the right cusp derivative is 4/[v log^5(1/v)] and integral^infinity exp(L)L^(-10)dL diverges. No endpoint delta is responsible. Global r w^3 energy implies all finite pure-log moments and every H^s with s<1/2, but no higher power follows.

This control lies precisely in the regime outside the already closed supercritical null-promotion theorem. It cannot be disposed of by assuming H^(5/8), as for the earlier power example. It still is not a null solution.

## 3. Actual exterior cancellation and its exact scale

Write L=log(1/u). From the genuine prime-2 cusp and the smooth pole/regular-Euler terms,

    A_R,h(u)-A_R,h(0)=-w2 L^(-3)+O(u),
    w2=log(2)/sqrt(2)>1/6.

For example log 2>1/2 and sqrt 2<2 give w2>1/4. The same support geometry proves that every other prime profile is zero here.

The Carleman tail obeys

    M_R-C_R(u)=(1/3)L^(-3)+O(L^(-4)).                 (3)

To justify (3), change v=exp(-s). The near-edge integral becomes integral s^(-4)/(1+exp(L-s))ds. The step-function part is exactly integral_L^infinity s^(-4)ds=L^(-3)/3. The difference kernel is bounded by exp(-|s-L|); splitting at s=L/2 proves an O(L^(-4)) smoothing error. Outer support and smooth bump contributions are O(u). Cutoff transition pieces are also separated.

Since M_R=2A_R,h(0), the actual residual is

    r_R(u)=(1/6-w2)L^(-3)+O(L^(-4)).                  (4)

The physical Hardy integral is integral L*L^(-8)dL. The residual and drive-variation Hardy integrals with weight 1/[u L(u)] reduce to integral L^(-7)dL. All are finite. The actual matching limits and the previous absolute-collar and matched quadratic identities are consequently lawful for this control.

Scaling u=t x and applying dominated convergence to the bounded ratios of logarithms gives

    F_R(t)~(1/6-w2)t log^(-7)(1/t)<0.                 (5)

Indeed log(1/(t x)) and log(1/(t(1-x))) are at least log(1/t), and their ratios tend to one at every 0<x<1; the integrand is bounded independently of x after normalization. Its integral tends to one. The critical absolute flux integral is finite, whereas the order-3/2 signed exterior-flux integral diverges to -infinity. The left physical profile remains zero on a short collar, giving left flux zero. This satisfies the available necessary native upper sign at both ends.

As before, this exterior flux is NOT substituted for the diagonal-subtracted signed source trace: the full interior null equation is absent.

## 4. Exact interior nullity leaves a nonzero critical-scale defect

All actual prime shifts vanish on the right interior collar, particularly the prime-2 shift on the zero side of its interior cusp. Apply the pinned pointwise actual Euler formula on that collar and split its singular 1/(2s) part at s=v and at a fixed b<delta/4.

After subtracting the boundary constant, the leading terms are

    f_R(v)log(1/v)+(1/2)integral_0^v f_R(s)/s ds
       =L^(-3)+(1/6)L^(-3), L=log(1/v).              (6)

The small-s second difference is O(L^(-5)): scale s=v y and use the integrability of |log(1-y)|/y and |log(1+y)|/y on (0,1) for the differences of L^(-4). For v<s<b, replacing f_R(v+s) by f_R(s) incurs O(L^(-5))+O(v^(1/2)); the derivative bound gives v integral_v^sqrt(v) ds/[s^2 log^5(1/s)], and the remaining separated part is exponentially small compared to an inverse logarithmic power. The bounded local regular kernel, m0(0)f_R(v) and the distant actual-kernel mass terms contribute O(L^(-4)); after changing variables, distant profile motion acts on a smooth kernel and contributes O(v). Pole variation is O(v).

The actual boundary constant is -M_R/2+A_R,h(0)=0 by the enforced match. Equations (6) and the controlled remainders prove (1). The coefficient 7/6 is positive, so q_h is nonzero on an entire sufficiently short interior collar. The full-null equation has not been imposed or inferred from the scalar match.

This is an exact arithmetic/source compatibility failure for a critically regular actual carrier vector. It shows where the one-sided prime attachment separates exterior matching from interior homogeneity. It does not assert that a general actual null vector has an inverse-log power expansion or a fixed sign.

## Remaining gate and custody

Failed implication: actual drive/source custody + critical source moment + global r w^3 energy + both endpoint matches + all proved boundary budgets/identities + necessary exterior flux sign -> L2 derivative. The actual slow-cusp control rejects it without any supercritical Sobolev regularity premise.

The smallest remaining critical theorem is unchanged: for actual h in K_a intersect Xcrit, the exact full-native homogeneous interior equation must imply h' in L2. Whole-contact-kernel critical membership remains a separate unproved obligation. No scalar injectivity, fixed-phase or boundary-expansion premise is added to the kernel. The alternative supercritical whole-kernel signed trace remains open.

Pinned sources at recovered head:

- ACTUAL_DRIVE_CUSP_20261007, blob b0fc27ece02f8f5cbdce6d86eda4c28d60d12c81: actual geometry, bump matrix, source/drive normalization and pointwise interior formula.
- CRITICAL_INTERIOR_GAIN_20261007, blob 05f53463842cb5aafbb5116c7f3a4bf65207400e: previously derived interior r w^3 conclusion and its scope.
- FRACTIONAL_POSITIVE_SOURCE_MOMENTS_20261006, blob 955ff7b4bd0d7f58221c300a962a803824232fd6: actual critical source/Fourier comparison.
- MATCHED_96_097_WHOLE_DOMAIN_20261007, blob 8604e8d6429c91b9ccea4a5c8a7e75dee4f078c6: reused positive-energy certificate.

The accepted external |beta_rho|<=3/8 input is preserved and applies to the same actual zeros; it does not remove (1). No new external theorem, aperture marching, retained packet identification, enlarged null transport, positive eigenvector or nonzero null claim. Proof validation is analytic for the log-cusp differences, cosine norm comparison, Carleman tail and exact Euler asymptotic. The companion check verifies rational exponent/coefficients and reuses the 31 support checks; it does not certify the analytic theorem in Lean. Canonical cursor updated additively, including preservation of the concurrent 973/1000 preflight. Endpoint exclusion, critical promotion, RH, F4 and FULL TRANSPORT CLOSED remain unproved.
