# RPB108: logical strength of the signed cutoff endpoint target

Date: 2026-10-07 UTC. Recovered live head 6e3411729403c5610912e745dc4c08b77f3d8ede.
Category: endpoint exclusion. This is a dependency audit, not a new arithmetic estimate.

## Exact statement and quantifiers

Use the actual native family, its canonical supported domains D_a, and its full mixed weak kernels K_a. Fix r=3/2 and, at each window, any fixed admissible t0>0. For a physical L2 orthonormal basis h_1,...,h_m of K_a set

    I^K_(epsilon,r) =
      sum_j sum_actual_copies J_(epsilon,r)(theta_q)
        (|p_q(h_j)|^2-|n_q(h_j)|^2),
    J_(epsilon,r)(theta) =
      integral_epsilon^t0 (1-cos(theta t)) t^(-1-r) dt.

These are the previously defined finite-epsilon sums, not differences of infinite moments. At fixed epsilon the multiplier is bounded and the complete actual analyses are bounded. The finite-dimensional quadratic trace is therefore basis independent. Changing t0 to another positive admissible value adds a finite convergent integral away from zero and does not change the criterion.

Consider the following assertions about this same actual family:

| Assertion | Exact scope |
| --- | --- |
| S | At every nonnegative actual window, liminf as epsilon decreases to zero of I^K_(epsilon,3/2) is less than +infinity. |
| C | If an attained nonnegative first contact exists beyond the certified positive interval, its entire kernel satisfies that same finite-liminf condition. |
| Z | Every nonnegative actual window has K_a={0}. |
| U | Q_a is nonnegative on D_a at every finite window; equivalently the complete negative actual source norm is dominated by the positive one. |
| H | Every finite window has its own strictly positive logarithmic coercivity constant. |

Within the already established architecture,

    S <-> C <-> Z <-> U <-> H.

No uniform-in-a coercivity constant or cutoff bound is asserted. C is conditional: it is vacuously true when no first contact exists. The trace of the zero kernel is zero. This vacuity is part of the reverse implication, not an estimate on a nonzero kernel.

## Proof and dependency custody

The signed cutoff theorem gives, on the entire finite actual kernel,

    I^K_(epsilon,r) >= W^K_(epsilon,r)/2-L_(K,r),

where W^K is nonnegative and monotone as epsilon decreases. For r=3/2 a finite liminf forces every basis vector into H^(3/4). The negative-distributional promotion theorem then puts every such vector in H1. Differentiation invariance of the full native kernel and the finite-dimensional derivative-chain obstruction imply K_a=0. Equivalently, any nonzero actual K_a has I^K_(epsilon,r)->+infinity for every 1<r<2. This is a whole-kernel conclusion; one smoother null vector alone does not suffice.

Consequently S implies Z and S implies C. If C holds and any window had a negative direction, the certified positive seed, norm continuity and I+compact Fredholm structure would supply an attained nonnegative first contact with nonzero kernel. C and the preceding implication contradict that contact. Hence C implies U.

If U holds, a nonzero full-null vector at a window has unchanged diagonal zero at every strict larger support. Positivity there upgrades diagonal zero to full mixed nullity. The established strict-enlargement obstruction excludes this. Hence U implies Z. Z makes every trace in S empty, so Z implies S. Finally U implies H by the nonnegative I+compact operator with zero kernel at each fixed window; H implies U directly.

This proof reuses the earlier positive-seed/global-interface equivalence and global/F4 entry audit. The source cutoff and promotion results supply a new expression of its endpoint condition. They do not weaken its globally quantified logical strength.

## What the improved strip proves, and what it leaves

The accepted external seven-eighths theorem and functional-equation symmetry give |beta_q|<=3/8, including possible endpoint equality. For both existing subcritical source moments and r=3/2, choose s=3/8. The complete transverse remainder has finite integral against t^(-5/2), with cross-term margin 1/4. The same integrability argument also worked at the earlier strip bound 1/2.

The unbounded ordinate multipliers J_(epsilon,3/2)(theta_q) are not controlled by this transverse improvement. No estimate derived so far gives S or C. The exact full-native zero equation identifies the exterior residual, but the projected fractional test leaves that entire residual term. The combined edge decomposition supplies its actual prime/pole/Carleman custody, not its required signed integral bound.

At critical order r=1 the two remaining inputs are distinct:

    whole-kernel Xcrit membership
        + exact zero-kernel derivative promotion K_a intersect Xcrit -> L2 derivative
        -> whole K_a in H1 -> K_a=0.

Neither critical input has been proved. The narrower transverse strip does not alter the physical support-projection threshold. The supercritical criterion avoids the separate critical promotion gate by using H^(3/4), but its global premise S still has the strength displayed above.

The actual positive-eigenvalue rough mode at certified 24/25 satisfies the sharper strip and all derived subcritical source bounds while its supercritical signed trace diverges. It rejects an estimate insensitive to the exact zero interior normalization. It is not a zero-kernel counterexample. The supported cusp rejects certain separate local collar estimates and likewise is not an actual null vector.

## Failed implication and smallest remaining theorem

Failed inference: the established reductions, sharper strip, finite kernel and fixed-epsilon lawful tests already supply the uniform-in-epsilon signed trace bound. They supply only legality and comparison; the zero-specific arithmetic bound remains independent.

The smallest sufficient target on this route is C: a finite-liminf signed cutoff trace at order 3/2 for any hypothetical attained nonnegative first contact. It needs no uniformity in window or basis. Its advantage is an explicit finite-source-cutoff formulation with an integrable remainder. Its global logical strength is endpoint exclusion itself. Calling it a smaller target refers to its formulation and hypotheses, not to a proved weakening of the global problem.

This is not a new obstruction to the truth of C, and does not show it impossible. It prevents counting successive equivalent formulations as additional arithmetic closure.

## F4 and validation scope

If C is eventually proved, the above graph closes global unit domination and excludes actual full-null contact vectors. It does not identify a prescribed historical retained packet with a fresh actual selection, or construct a nonzero same-vector enlarged full-null witness. Those historical F4 morphology/attachment obligations remain distinct. No RH equivalence is asserted here.

Validation is a direct proof audit against the pinned source notes. There is no new numerical estimate or executable theorem; re-running algebra controls would not validate C. No Lean build or axiom audit was performed. The external theorem remains an accepted pinned input without a local rebuild. The certified 24/25 aperture result is preserved. Global endpoint exclusion, historical F4 assembly and FULL TRANSPORT CLOSED remain unproved.

## Pinned source custody

- [REFLECTED_PACKET_BRIDGE_108_SIGNED_CUTOFF_SOURCE_MOMENT_20261007.md](REFLECTED_PACKET_BRIDGE_108_SIGNED_CUTOFF_SOURCE_MOMENT_20261007.md), blob 52f34cc5c348c7ad5b00058c1208599f531bf4c7.
- [REFLECTED_PACKET_BRIDGE_108_SUBCRITICAL_DISTRIBUTIONAL_PROMOTION_20261007.md](REFLECTED_PACKET_BRIDGE_108_SUBCRITICAL_DISTRIBUTIONAL_PROMOTION_20261007.md), blob 665a473edee975b2d346d0511a292e4a64cb56e8.
- [REFLECTED_PACKET_BRIDGE_108_EXTERNAL_SEVEN_EIGHTHS_CRITICAL_FLUX_20261007.md](REFLECTED_PACKET_BRIDGE_108_EXTERNAL_SEVEN_EIGHTHS_CRITICAL_FLUX_20261007.md), blob c369d3760606d9e5b9ae0f4862156fd712e5be29.
- [REFLECTED_PACKET_BRIDGE_108_ACTUAL_SUPERCRITICAL_SOURCE_CONTROL_20261007.md](REFLECTED_PACKET_BRIDGE_108_ACTUAL_SUPERCRITICAL_SOURCE_CONTROL_20261007.md), blob 1d1157c7257ada74d1a42c02245243b4d2edd364.
- [REFLECTED_PACKET_BRIDGE_108_POSITIVE_SEED_GLOBAL_INTERFACE_EQUIVALENCE_20261004.md](REFLECTED_PACKET_BRIDGE_108_POSITIVE_SEED_GLOBAL_INTERFACE_EQUIVALENCE_20261004.md), blob 69327050106adc5650034a129cc55e636fd4f053.
- [REFLECTED_PACKET_BRIDGE_108_GLOBAL_F4_ENTRY_AUDIT_20261006.md](REFLECTED_PACKET_BRIDGE_108_GLOBAL_F4_ENTRY_AUDIT_20261006.md), blob a6891f7eeac57999879bd4aded6867badaa0340b.
- [REFLECTED_PACKET_BRIDGE_108_THREEBAND_POSITIVITY_096_20261007.md](REFLECTED_PACKET_BRIDGE_108_THREEBAND_POSITIVITY_096_20261007.md), blob 119a2a3198ea0df81486e9f0ba98795f72685c98.

The corresponding manifest records these exact blobs at the recovered head.
