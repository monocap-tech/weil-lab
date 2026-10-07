# RPB108: dense actual prime feedback and the boundary obstruction to full-line inversion

Date: 2026-10-07 UTC. Recovered live head 3d40b852e2e2a71cbf7600c65574c811f2570a2d.
Definitions: [admissible paths, multiplier and exterior residual](../docs/TERMINOLOGY_RPB108_DENSE_PRIME_BOUNDARY.md).
Category: endpoint exclusion / critical derivative promotion. Structural obstruction audit, not a new arithmetic estimate or endpoint theorem.

## Outcome

Two checks delimit the extension of the preceding finite-cusp exclusion to general critical null vectors.

1. The actual prime-2/3 admissible path graph generated from an endpoint is dense throughout the physical interval once 2a>log 6. This condition already holds below the certified 97/100 frontier, hence at every possible future finite first contact. Finite prime support therefore does not justify a finite profile system.
2. The complete full-line archimedean-minus-prime multiplier is uniformly invertible at sufficiently high frequency on every H^s, irrespective of those dense paths. Thus the geometric obstruction is not proof of actual singular propagation, nor an obstruction to full-line high-frequency ellipticity. The failed step is replacing an interior homogeneous equation by a full-line homogeneous equation without controlling its exterior residual.

Neither result closes K_a intersect Xcrit -> L2 derivative or whole-kernel Xcrit membership. No new critical positive-source moment bound follows from the transverse strip.

## 1. Exact dense path construction, with all intermediate points supported

Put alpha=log 2, beta=log 3, L=alpha+beta. Suppose 2a>L. The strip J=[a-L,a] lies in the physical closed interval, with its lower endpoint strictly interior. Both primes are active.

On y in [0,L), set

    R(y)=y+alpha if y<beta,
         y-beta  if y>=beta.

This is rotation by alpha modulo L. Starting y_0=0 gives x_0=a and x_k=a-y_k. Each step is exactly x -> x-alpha or x -> x+beta. It uses an actual prime-2 or prime-3 translation and remains in J. No abstract integer combination with an unsupported intermediate point is substituted.

The ratio alpha/L is irrational: rational equality would yield a nontrivial equality of powers of 2 and 3, contradicted by unique prime factorization. Hence the rotation orbit is dense in [0,L). In particular no later y_k equals zero; all noninitial x_k are physically interior. For completeness, density follows from the elementary circle subgroup argument: the closure of the integer orbit is a closed subgroup; an irrational generator cannot give a finite subgroup, and every infinite closed subgroup of the circle is the full circle. Recurrence to zero identifies the closure of the positive orbit with that integer orbit closure.

This gives a dense reachable subset in J. For each integer k>=0, continue a finite path by k steps x -> x-alpha whenever its endpoint remains greater than -a. Intermediate points are decreasing and therefore also remain supported. The reachable set is dense in (J-k alpha) intersect I_a. These intervals cover I_a: their width L is larger than the displacement alpha, and their left endpoints tend to -infinity. Thus the entire endpoint-generated reachable set is dense in I_a.

At a=97/100, the rational logarithm enclosure verifies log 6<2a. A future first contact must be strictly beyond this certified positive aperture, so the same conclusion applies automatically. This reuses the aperture result; it does not request or compute another aperture certificate.

Consequence: there is no finite set containing this endpoint seed that is closed under all admissible prime-2/3 steps. The prior finite inverse-log class theorem stays valid but cannot be upgraded by counting the finitely many original prime terms.

Important limitation: possible profile locations are not actual singularities. No wavefront propagation equality, nonzero singular coefficient, null vector or critical-gate counterexample is inferred from the graph. Dense possible locations can coexist with a smooth solution.

## 2. Joint high-frequency inversion succeeds on the full line

The full-line prime multiplier obeys |t_a(xi)|<=tau_a on R. The actual archimedean envelope gives m0(xi)>=w(xi)-C0. Choose R so ell_R=log(e+R)-C0>tau_a. Then for |xi|>=R,

    m0(xi)-t_a(xi)>=ell_R-tau_a>0.

On H_R^s, P_R m0(D)^(-1) T_full has norm at most tau_a/ell_R<1, for every real s, since all factors commute as full-line Fourier multipliers. The Neumann inverse of I-P_R m0(D)^(-1) T_full is bounded by (1-tau_a/ell_R)^(-1). Equivalently the reciprocal joint symbol is bounded by 1/(ell_R-tau_a); at sufficiently high frequencies it is also bounded by C/w(xi).

This uses the entire finite prime sum, not omission of arithmetic terms, a selected packet or the separately constructed effective background. Arbitrarily repeated prime words are already summed by the full-line inverse. There is no high-frequency arithmetic cancellation of the logarithmic principal growth.

This is a full-line statement only. Multiplication by the sharp support indicator does not commute with these multipliers. The native inverse on a bounded interval is not this Neumann inverse followed by support restriction.

## 3. Exact full-native equation identifies the missing term

For h in the actual kernel intersect Xcrit, let eta be the compact pole extension defined above. Its localized pole is smooth. Critical membership makes m0(D)h an L2 distribution because log^2(e+|xi|) is bounded by a constant times the critical Fourier weight. T_full h is L2. Thus F_h is well-defined in L2, and exact homogeneous native nullity gives

    F_h=0 on I_a,
    (m0-t_a) Fourier(h)=Fourier(F_h)-Fourier(eta p_h) on R.  (1)

The full residual generally does NOT vanish outside I_a. Equation (1) retains it; replacing F_h by zero would illegally assert full-line, hence enlarged, cancellation.

High-frequency inversion now yields

    P_R h = (m0-t_a)^(-1) P_R(F_h-eta p_h).             (2)

The low-frequency part belongs to every H^s by compact Fourier support and h in L2. If F_h were in H^s for any s>1/2, (2) would imply h in H^s and the pinned supercritical null-promotion theorem would give an L2 derivative. This is only a stronger sufficient diagnostic: no such exterior H^s estimate has been proved. Critical dual/logarithmic residual budgets cannot be silently replaced by this power estimate.

In particular bounded/continuous drives, matched inverse moments and the critical collar identities do not eliminate F_h. The preceding actual critical control supplies a nonzero residual and is not an exact-null counterexample. The failure diagnosed here is an unjustified inference in a proof route, not a proof that no null-exclusive boundary estimate can exist.

## 4. Remaining theorem and external input scope

Exact failed implication A: finite frozen prime list -> finite boundary-generated location system. The supported prime-2/3 rotation is an explicit counterexample.

Exact failed step B: invert the full-line joint symbol -> promote a supported critical null vector, while discarding F_h. Exact equation (1) exposes the omitted exterior source. Its needed regularity remains unproved.

Smallest remaining theorem is unchanged: actual q_h=0 on I_a and h in K_a intersect Xcrit -> h' in L2. A boundary-resolvent theorem must either control the complete exterior residual or establish the corresponding supported critical regularity directly; it must accommodate all profiles, not just a finite cusp ansatz. Whole-contact-kernel critical membership remains an independent obligation. This audit adds no new sufficient hypothesis to the canonical kernel and claims no progress on the general gate from a reformulation alone.

The accepted external |beta_rho|<=3/8 is preserved. It concerns the transverse actual zero coordinates, whereas alpha,beta in this note are explicitly the positive real numbers log 2 and log 3, NOT zero coordinates. The strip does not alter the translation graph or the archimedean multiplier envelope and does not supply the exterior power estimate. No historical packet attachment, same-vector enlarged cancellation or F4 assembly is attempted.

## Custody and validation

Read at the recovered head:

- FINITE_LOG_CUSP_EXCLUSION_20261007, blob fb787de667a06527a4cfb08d4127afed7e20aeed.
- CRITICAL_INTERIOR_GAIN_20261007, blob 05f53463842cb5aafbb5116c7f3a4bf65207400e.
- CRITICAL_DERIVATIVE_PROMOTION_20261007, blob 26627f85c34572a8197b32a1216382e8d02e07f5.
- MATCHED_96_097_WHOLE_DOMAIN_20261007, blob 8604e8d6429c91b9ccea4a5c8a7e75dee4f078c6.
- LOGARITHMIC_BOOTSTRAP_20261005, blob c2d087875d8dd85dfcdbd64893923ef51fcf1028: full-line translations, multiplier envelope and actual equation.
- scripts/certify_native_drive_cusp_geometry.py, blob 0c86fb92fc627219767138a2fa1098b668dfb173: imported exact logarithm enclosure.

Analytic validation: support at every rotation step, irrationality, orbit-density argument, covering of the full interval, full-line operator norms and the retained exterior term. The companion script uses exact rational logarithm enclosures to check the frontier threshold and 1024 actual steps, with narrow-strip and omitted-step controls. It checks finite walks, not the infinite density theorem, analytic regularity or Lean. No external regularity theorem newly imported; a literature check supplied no adopted derivative-promotion result. No assertion that such a theorem is absent from the literature.

Canonical cursor updated additively. Concurrent 973/1000 native/source custody, complete source milestone and certified 97/100 frontier preserved. No new aperture, Lean/axiom/workflow change, global endpoint exclusion, RH, F4 or FULL TRANSPORT CLOSED.
