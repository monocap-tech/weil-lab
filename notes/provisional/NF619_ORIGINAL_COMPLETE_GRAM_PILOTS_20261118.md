# NF619 — complete original oscillator and oscillator-pole Gram entry pilots

Stacked on NF618 #649 at 957981b3. NF618 focused run 44274760282 was queued at initial inspection alongside a large historical replay backlog. No fresh Lean acceptance is attributed to NF618. Prior accepted local 17/40 coercivity, intrinsic solve equivalence, analytic H,V dictionary, moment enclosure and entry-to-solve implications remain unchanged.

Let J(z)=integral over [-B,B] of exp(z x), B=11/10; let z=i*2*pi*(37/64). For every complex lambda, J(-lambda)=J(lambda) (degree zero). Derive this by comparing the accepted exact endpoint recurrence at lambda and -lambda, handling zero separately. The first selected generator is the actual sine mode at 37/64; the final selected generator is the actual sinh(x/2).

The accepted NF607 four-term entry identity therefore reduces the entire original H[0,0] to B-J(2z)/2 and H[0,241] to (-i/2)*(J(z+1/2)-J(z-1/2)), viewed in C. Taking real parts, control of Re J(2z) and Im J(z±1/2) is sufficient. New Lean proof candidates isolate these exact full-entry identities independently of the numerical receipt module, and propagate the complex-norm midpoint bounds to real entry radii. The new receipt module separately checks the missing negative-real-part mixed exponent and attaches the three degree-zero receipts.

An actual local Python Fraction replay in this turn independently evaluated the fixed-point rectangular boundary and residual arithmetic for all three required degree-zero keys (0,37/32), (1/2,37/64), (-1/2,37/64), with Q=10^40, N=48. All pass the candidate 10^-33 radius payment. The opposite real-sign mixed residual upper was 31967/(25*10^38), equivalently 31967/2500000000000000000000000000000000000000. The complete-entry candidate intervals obtained by the exact formulas are:
- H[0,0]: center 0.96365058853459560322855497082803181, radius 5e-34.
- H[0,241]: center 0.14043467082935807939230485585476647, radius 1e-33.

The numerical replay is exact rational arithmetic, not a completed Lean proof of the full entry. The committed replay script extends NF618 with the additional mixed sign and complete-entry center/radius report; the new kernel gates, real projections and exact source assembly still await compilation. The new focused workflow uses explicit paths and separates analytic assembly from receipt dependencies; inherited historical workflows were not changed or cancelled. This 40-digit pilot does not establish full solve accuracy.

Next: recover NF618/NF619 compiler receipts, establish complete entry assembly soundness, and move from small receipt tests to the shared-key high-precision table and actual row budgets. Formal physical solve custody, global Weil positivity, U400 and RH remain open. No main merge or new full Arb solve replay.

Final receipt inspection: NF618 independent rational replay job 134699952234 PASS. Pole job 134699952322 failed only at unnecessary simp after conversion and Decidable elaboration of the folded widening proposition; the explicit kernel comparison itself had no reported error. Repair by unfolding the ball before conversion and the widening predicate before applying of_decide_eq_true. New repairs pending; the entire pole theorem is not yet certified. The other NF618 focused jobs remained in progress at this inspection.
