# RPB108 actual native scalar sign audit — 2026-10-04

## Starting point and scope

Start: certified research head `936e723ac9c22592f9fb0901f2f25bbf238227c2`. The carrier, finite-packet and mixed Gram criteria already make the WD-T10 background sign obstruction exact. This chunk examines the actual native scalar multiplier itself, without introducing another carrier or representation premise.

## Actual special-value computation

The pinned Mathlib duplication, reflection and half-value identities give

Re digamma(1/4) = -3 log 2 - Euler gamma - pi/2.

The exclusion of integer poles and negative natural poles is proved for the quarter argument. Cot(pi/4)=1 and the existing exact half-value complete the calculation. No numerical digamma approximation, zero database or positivity assumption is used.

Each existing compact-window prime coefficient 2 Lambda(n)/sqrt(n) is nonnegative. At zero frequency its cosine is one. Hence the exact threshold-corrected native symbol satisfies

M_a(0) = -3 log 2 - Euler gamma - pi/2 - log pi
         - sum over the retained right-limit prime powers of their prime coefficients.

The already proved Euler gamma > 1/2, positive logarithms and pi show M_a(0)<0 for every window parameter a. Continuity supplies an open frequency neighborhood on which M_a is strictly negative. Thus global pointwise nonnegativity of the actual scalar multiplier is false.

## What this rules out

A route that attempts to pay the WD-T10 unshifted budget by global pointwise multiplier nonnegativity cannot apply to this actual symbol. The scalar negativity already occurs in its archimedean component; removing all active primes would not eliminate it.

This result does not decide the background quadratic on supported Green vectors. That quadratic integrates the multiplier against the actual vector's Fourier mass and includes the cross-pole contribution and exact selected negative energy. Supported-window restrictions must remain in the argument. A freely chosen Fourier-localized vector is not automatically a lawful supported source vector, a Green graph vector, or the retained k.

No actual negative finite background packet, actual mixed Gram violation, uniform background positivity theorem, full graph density or retained source/null attachment is produced.

## Certification

Lean 4.34.0; exact tested validation head `4be78ae10508ce7e33b243757d9960a3b0890cb4`. [Actions run 37232043029](https://github.com/monocap-tech/weil-lab/actions/runs/37232043029) / job `111523667095` passed isolated 9176/full 9203 build jobs. All six theorem audits depend exactly on `[propext, Classical.choice, Quot.sound]`; unfinished/project-axiom gate passed. New module and root import were fetched and verified byte-for-byte. Certified Gram cache restored and native-sign cache `rpb108-actual-native-symbol-sign-verified-v1` saved.

## Cursor and residue

At 936e723, the actual native scalar multiplier sign is audited using pinned digamma special-value identities. Its value at zero is -3 log 2 - Euler gamma - pi/2 - log pi minus a finite sum of nonnegative prime coefficients, hence strictly negative for every window; continuity gives a negative frequency neighborhood. Global pointwise multiplier nonnegativity is therefore unavailable as a WD-T10 route. This is not a negative supported Green packet or a decision of the integrated background quadratic. Next arithmetic work must retain supported-window constraints, multiplier integration, cross-pole contribution and actual selected energy together, using the certified finite-packet and mixed Gram criteria. No actual background violating pair, finite negative packet or uniform unshifted positivity theorem is established. Do not replace the lawful same-vector graph by an arbitrary Fourier-localized vector. Retained same-vector membership/attachment or a fresh concrete WD-T38 attained-unit-gain realization and endpoint null witness remains independent. Full graph density, zero simplicity, spectral operator-domain membership and background positivity are not assumed. Central cancellation, background completion, boundary removal and F-4 remain open. FULL TRANSPORT CLOSED is not certified. SOURCE remains off the critical path.
