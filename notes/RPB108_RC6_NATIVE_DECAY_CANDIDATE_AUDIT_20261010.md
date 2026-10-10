# RPB108 RC6 — native decay candidate audit

2026-10-10. Independent branch research/rpb108-route-consolidation.
Parent: 3d4589a25cad2eeb2a05966e2454548dd7f15724 (RC5).
Only this branch is written.

## Question and answer

Does old-window positivity, bounded native remainder, and a small enlargement
automatically supply RC5's outward-forcing decay with near-null energy?

No. Those inputs control a mixed row absolutely or relative to the OLD gap.
They do not supply a cap-uniform near-null factor. The stronger signed
Cauchy--Schwarz bound is available if the ENLARGED form is already nonnegative,
which is the unknown premise.

The audit checks this directly in RC5's canonical native coordinates, and
matches the result to the historical CC23 stop condition. It does not prove
that the complete actual Weil identities cannot yield a new mixed estimate.

## Definitions before use

Use RC5's old canonical operator H_s>0 on D_s, outward map
O_st=(Pi_t-Pi_s)C_B|D_s, and canonical output space
Z_st=D_t intersect D_s perpendicular. In the canonical orthogonal decomposition
D_t=D_s direct-sum Z_st the original target operator is

    H_t = [[H_s, O_st*], [O_st, D_st]],

where D_st is the target native form restricted to Z_st.
D_st is not assumed positive solely from old positivity.

When D_st>=d I>0, the exact target sign is determined by

    H_s-O_st*D_st^(-1)O_st >=0.                      (1)

Every outgoing direction and mixed entry is included. This is an identity
and acceptance condition; writing it is not a bound from actual arithmetic.

## The linear native rule is a factorization obligation

For a fixed old-positive pair, the linear version of RC5's rule is

    O_st*O_st <= C_B H_s.                            (2)

Equivalently there is a bounded R_st on the completion of ran(H_s^(1/2))
with

    O_st = R_st H_s^(1/2), ||R_st||^2<=C_B.           (3)

Proof: define R_st(H_s^(1/2)h)=O_st h. Inequality (2) makes this well-defined
and bounded; extend by continuity. Conversely (3) gives (2).
At an individually coercive old aperture, R_st=O_st H_s^(-1/2).
No inverse OLD-GAP-INDEPENDENT estimate follows merely from its existence.

A finite cap-only bound C_B in (2) is sufficient for the ENDPOINT contradiction
of RC5, with a cap-only admissible step. It need not be below one.
If one instead wants an immediate strict target sign from (1), the
sufficient comparison C_B<d applies when D_st>=d I; that is a different
finite-step use of the bound.

A nonlinear vanishing modulus remains allowed in the endpoint route.
The factorization characterization concerns the linear rule only and does
not impose linear decay as the new minimum target.

## Signed Cauchy--Schwarz has the missing target premise

If H_t>=0 were already established, its signed Cauchy--Schwarz inequality
would give, for h in D_s and z in Z_st,

    |<z,O_st h>|^2 <= Q_s(h)<z,D_st z>.

If ||D_st||<=M_B, taking the supremum over canonical unit z yields

    ||O_st h||^2<=M_B Q_s(h).                       (4)

This is exactly a linear outward-decay estimate. Its derivation, however,
uses positivity on D_t, not the known positivity on D_s. The second vector
z is outside the old domain. Separate positive-source Cauchy--Schwarz
bounds cannot be substituted for the signed inequality.

This recovers CC23's old circularity finding in the native formulation.
Pinned report read at CC119 5df347d3808ac3282864a657b7380e0f54bf4daa:

    notes/REFLECTED_PACKET_BRIDGE_108_SIGNED_BUDGET_CC23_20261008.md
    Git blob fa6696ffe96b299248e3e39daaba5ef9d94f625d.

Historical words and scope are preserved. This is not a claim that EVERY
possible proof from the original explicit formula is circular.

## Small enlargement controls width, not near-null energy

Even granting a cap-only bound ||O_st||<=m_B(t-s), m_B(w)->0 as w->0,
the resulting estimate is

    ||O_st h||^2<=m_B(t-s)^2||h||_D^2.

Its right side need not vanish with Q_s(h) at any FIXED allowed width.
It therefore does not establish RC5's endpoint property.

If H_s>=g_s I and D_st>=d I, the elementary sufficient Schur test is

    m_B(t-s)^2 < d g_s.

This chooses a safe step depending on the old gap. As g_s->0, that proof's
step can collapse. It is not a cap-only non-stalling rule.

A sharp finite signed-block control takes width w>0 and

    H_s=w^4, O_st=w, D_st=1.

The old energy is positive and the mixed norm tends to zero with width,
but the target determinant is w^4-w^2<0 for 0<w<1. Its normalized
outgoing cost is 1/w^2, which diverges. The control does not model the
literal original native arithmetic; it refutes the indicated inference
from old positivity and absolute smallness.

The genuine support-enlargement discriminator is CC19/CC23's differential
source-shell model. In its exact rational coordinates u=2s/pi, v=2t/pi,

    defect=1-u^2, leakage=2u(v-u).

For fixed rho<1 a relative reserve forces

    v-u <= rho(1-u^2)/(2u),

which tends to zero with distance to contact. At a fixed target v>1,
leakage tends to 2(v-1)>0 as u->1. Any vanishing-modulus endpoint bound
fails there. Thus the small-width inference also fails in a genuine
nested-domain operator, not just in the finite block control.

## Arithmetic content still required

The actual native identity specifies O_st via the complete archimedean,
prime-power and pole form after CANONICAL projection. A valid new estimate
must exploit that signed arithmetic to obtain either

    ||O_st h||^2<=C_B Q_s(h),

or another uniformly vanishing function of Q_s(h), for the actual near-null
vectors and a positive cap-only enlargement width. Absolute component norms,
smaller numerical source error, old-only test vectors, and target-positive
signed Cauchy--Schwarz do not supply it.

RC5's canonical 1.06 guard is a sound starting bound under its inherited
attachments. It does not by itself determine the decay of O_st as a later
old gap closes. The proposed rule is now a precise arithmetic obligation;
the present candidate has not extracted it from the successful local
response certificate.

Stop the automatic small-enlargement / signed-Cauchy--Schwarz candidate.
A further step must identify and estimate an actual new mixed relation,
rather than relabel (1)-(4) as a theorem of native positivity.

## Fresh validation and standing

scripts/validate_rpb108_rc6_native_rule_controls.py passes 51 fresh rational
checks: arbitrarily small outgoing rows with negative target completions,
linear factorization ratios, genuine differential step budgets, and the
target-positive premise of the signed mixed bound. The full positive-level
mass controls from RC2-RC5 remain inherited; unshifted H_s is used here.

No actual arithmetic outward-decay bound, new aperture, RH/F4 theorem or
Lean closure is certified. Other refs and historical artifacts are untouched.
