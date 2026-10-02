# IRT-1A — observable-orientation theorem design

**Date:** 2026-10-02 (America/Los_Angeles)  
**Repository:** \`monocap-tech/weil-lab\`  
**Branch:** \`research/inverse-realization-transfer\`  
**Parent:** IRT-0F  
**Status:** **COMPLETE THEOREM-DESIGN PASS / DANGEROUS SOFT DIRECTION TYPED AS KPH RIGHT-SINGULAR CONE / FULL FRAME REQUIREMENT WEAKENED TO SOFT-CONE ACTIVATION / ELEMENTARY FACTOR-THROUGH SANDWICH PROVES KPH FLOOR / EXISTING FEATURE/APR CHANNELS FAIL INDEPENDENCE OR REDUCE TO THE KNOWN FLOOR / DERIVATIVE-DIVISOR CHANNEL REMAINS THE CLEANEST INDEPENDENT CANDIDATE / NEXT CURSOR IRT-1B MIXED-DIVISOR SOFT-CONE FRAME DESIGN**

## 0. Objective

IRT-0F extracted the abstract missing input as

\[
\text{complement-oblivious stable mixed-divisor observability/orientation}.
\]

IRT-1A makes that statement mathematically minimal and tests whether it is
actually weaker in form than a direct KPH floor.

The result is a soft-cone theorem rather than a full second-channel coercivity
theorem.

## 1. Native soft object

In the authorized local Key-C normalization, define

\[
\boxed{
A_F^{\rm KPH}
=
I+\varepsilon^{-1}C_F,
}
\]

where \(C_F\) is the direct reciprocal-Cauchy matrix of the selected packet.

Then

\[
\boxed{
KPH(F)=\sigma_{\min}(A_F^{\rm KPH}).
}
\]

The dangerous direction is therefore not a heuristic "bad packet direction."
It is the right-singular soft cone of \(A_F^{\rm KPH}\).

For exponent \(B>0\), define

\[
\mathcal S_B(F)
=
\left\{
v:\|v\|=1,\
\|A_F^{\rm KPH}v\|\le H_F^{-B}
\right\}.
\]

Failure of every projective KPH floor produces, along a dangerous sequence,
unit vectors in \(\mathcal S_B(F)\) for arbitrarily large fixed \(B\).

## 2. A full second-channel frame is unnecessarily strong

One possible theorem would be

\[
\sigma_{\min}(\mathcal O_F)\ge H_F^{-a}
\]

for some independently defined observation operator \(\mathcal O_F\).

That is more than is required.

Only directions that are KPH-soft need to be observed.

Thus replace full coercivity by:

### IRT-SC-ACT — soft-cone activation

For every sufficiently high admitted actual packet and every unit vector
\(v\) satisfying

\[
\|A_F^{\rm KPH}v\|\le H_F^{-B_0},
\]

one has

\[
\boxed{
\|\mathcal O_Fv\|\ge H_F^{-a}.
}
\]

The observation rule for \(\mathcal O_F\) must be fixed upstream and cannot
depend on the post-freeze complement response or on the minimizing vector.

This is a strictly smaller output than a global frame bound on \(\mathcal O_F\).

## 3. The transfer theorem can also be one-sided

The second required statement is:

### IRT-SC-BRIDGE — projective factor-through control

For every relevant unit \(v\),

\[
\boxed{
\|\mathcal O_Fv\|
\le
H_F^b
\|A_F^{\rm KPH}v\|
+
\eta_F,
}
\]

where \(b\) is fixed and

\[
\eta_F
\le
\frac12H_F^{-a}
\]

for all sufficiently high packets.

A stronger operator identity

\[
\mathcal O_F
=
M_FA_F^{\rm KPH}+E_F,
\]

with

\[
\|M_F\|\le H_F^b,
\qquad
\|E_F\|\le\frac12H_F^{-a},
\]

is sufficient but not necessary.

Thus IRT does not require an exact intertwiner or metric equivalence.

## 4. Soft-cone sandwich lemma

Assume IRT-SC-ACT and IRT-SC-BRIDGE.

Let \(v\) be any unit vector to which the activation theorem applies.

Then

\[
H_F^{-a}
\le
\|\mathcal O_Fv\|
\le
H_F^b\|A_F^{\rm KPH}v\|
+\frac12H_F^{-a}.
\]

Therefore

\[
\frac12H_F^{-a}
\le
H_F^b\|A_F^{\rm KPH}v\|,
\]

hence

\[
\boxed{
\|A_F^{\rm KPH}v\|
\ge
\frac12H_F^{-(a+b)}.
}
\]

Choose

\[
B_0>a+b+1
\]

or simply state activation on every vector below the candidate scale
\(\frac12H_F^{-(a+b)}\).

Then no unit vector can have KPH residual below that scale, and

\[
\boxed{
KPH(F)
\ge
\frac12H_F^{-(a+b)}.
}
\]

Thus the two second-channel statements imply
\(\texttt{C-ACTUAL-KPH-FLOOR}\) with an explicit exponent ledger.

No compactness, singular-vector continuity, or reconstruction theorem is
needed for this implication.

## 5. Why the design is not automatically tautological

Abstractly, one could set

\[
\mathcal O_F=A_F^{\rm KPH}.
\]

That would make the theorem meaningless.

Therefore the observation must satisfy the independent-channel contract:

1. \(\mathcal O_F\) is defined from an independently typed actual-zeta channel;
2. its definition does not use the KPH minimizing vector;
3. IRT-SC-ACT is proved without assuming the KPH floor;
4. IRT-SC-BRIDGE is a separately proved mixed-channel identity/estimate;
5. its constants are projective and uniform on the actual packet jurisdiction.

The useful mathematical content is not the sandwich lemma. It is constructing
an \(\mathcal O_F\) satisfying both sides from independent zeta structure.

## 6. Relation to SOURCE-II-8

The theorem is upstream of the frozen total-source tower.

IRT-SC-ACT constrains the selected packet's admissible orientation before
SOURCE-II chooses or evaluates the complement response for the frozen
multiplier.

The implication chain is

\[
\boxed{
\text{second-channel soft-cone activation}
+
\text{mixed factor-through bridge}
\Longrightarrow
KPH\text{ floor}
\Longrightarrow
\text{no SOURCE-II dangerous failure sequence}.
}
\]

It does **not** begin by postulating smallness of the frozen jet tower.

Therefore it passes the SOURCE-II-8 no-false-intermediate test.

## 7. Candidate-channel audit

### O1 — native/ideal corrected feature operator

Near CF-A17, the corrected feature margin is bounded below:

\[
m(F)\ge c_*>0.
\]

This looks ideal for soft-cone activation.

But CF-A17 itself certifies

\[
m(F_*)>0,
\qquad
KPH(F_*)=0.
\]

Hence no source-free projective factor-through theorem from KPH to this
feature operator can hold in the required neighborhood with sufficiently small
error.

JOINT-2 further proves that an **actual-zeta-specific** feature/KPH attachment
on \(U_*\) is projectively equivalent to the KPH floor.

Therefore this candidate does not produce a new theorem interface.

**Disposition:** STRONG ACTIVATION / BRIDGE IS EXACTLY THE KNOWN SOURCE GATE.

### O2 — APR1/arithmetic corrected feature operator

APR1 and LJFR use the same corrected feature operator in different positive
metrics. Their unresolved theorem is a directional arithmetic coercivity /
attachment statement.

That machinery can yield native first-jet coercivity, but CF-A17 shows that
native feature coercivity alone does not exclude KPH softness.

To use APR1 as \(\mathcal O_F\), one still needs a source-specific
APR/KPH factor-through bridge. No retained theorem supplies it.

In the local CF-A17 jurisdiction this again collapses to an actual-zeta KPH
attachment theorem.

**Disposition:** NOT INDEPENDENT ENOUGH FOR KEY-C CLOSURE UNDER CURRENT CUSTODY.

### O3 — SOURCE-II total-source / jet observable

SOURCE-II-8 already proves that post-freeze tower smallness is projectively
equivalent to excluding the KPH-dangerous sequence.

Using it as \(\mathcal O_F\) violates the upstream independent-channel
contract.

**Disposition:** REJECT / FALSE INTERMEDIATE.

### O4 — ordinary critical-line packet geometry

For an odd simple all-critical-line packet,

\[
KPH(F)=1
\]

exactly because the direct reciprocal-Cauchy matrix is real
skew-symmetric.

This supplies a safe stratum, not an independent observation of an off-axis
dangerous packet.

CF-A17 already has the required source-free symmetry structure for an off-axis
KPH defect.

**Disposition:** CALIBRATION ONLY.

### O5 — derivative divisor / critical-point channel

The zeros of \(\Xi'\) are an independently typed divisor species.

A canonical rule could assign to each selected packet a derivative-divisor
observation matrix without choosing it from the KPH singular vector or from
the SOURCE-II complement response.

This candidate therefore satisfies the *type* requirement for independence.

What is missing are exactly the two IRT-SC theorems:

1. a soft-cone activation theorem for that derivative-divisor observation;
2. a projective mixed-divisor factor-through bridge into
   \(A_F^{\rm KPH}\).

NJDG proved that ordinary finite critical values/curvatures do not supply these
automatically. But it did not prove that no richer derivative-divisor
observation family can satisfy them.

**Disposition:** CLEANEST SURVIVING INDEPENDENT CHANNEL.

### O6 — a genuinely new arithmetic measurement family

A second explicit-formula/arithmetic channel could also satisfy the contract,
provided its source functional is not covariant with SOURCE-II under the same
selected-only constraints.

No such channel is currently constructed.

**Disposition:** OPEN ABSTRACT POSSIBILITY.

## 8. Weakest derivative-divisor theorem signature

The next design should not ask derivative zeros to reconstruct RENJET.

Instead, let

\[
\mathcal O_F^{\Xi'}
\]

be a canonically assigned matrix or finite/growing observation operator built
from derivative-divisor data in a prescribed packet-scale neighborhood.

The target pair is:

### DD-ACT

There are fixed \(a,B_0\) such that

\[
v\in\mathcal S_{B_0}(F)
\Longrightarrow
\boxed{
\|\mathcal O_F^{\Xi'}v\|
\ge H_F^{-a}.
}
\]

### DD-BRIDGE

There is fixed \(b\) and negligible/projectively subordinate error such that

\[
\boxed{
\|\mathcal O_F^{\Xi'}v\|
\le
H_F^b
\|A_F^{\rm KPH}v\|
+
o(H_F^{-a})
}
\]

on the same soft cone.

Together they imply the KPH floor.

Neither statement asks for exact recovery of the exponential RENJET kernel.

## 9. Why this is weaker than NJDG's failed targets

NJDG tested:

- critical-point existence;
- local derivative capture;
- field-value/curvature reconstruction;
- finite rational synthesis of the RENJET kernel;
- direct weighted mixed-divisor identities.

IRT-1A instead asks only whether the derivative divisor is **transverse to the
KPH soft cone**.

The observation family may contain more information than one or two critical
rows but need not reconstruct the complement or the weighted exponential
response.

Thus the new target is an orientation theorem, not an interpolation theorem.

## 10. Exact no-credit conditions for IRT-1B

The derivative-divisor route will not count as progress if:

- \(\mathcal O_F^{\Xi'}\) is chosen after identifying the KPH singular vector;
- the observation points are chosen from the complement to optimize the bound;
- DD-ACT is merely a restatement of \(KPH(F)\ge H^{-A}\);
- DD-BRIDGE uses an inverse of \(A_F^{\rm KPH}\);
- the matrix reduces to finitely many rational critical rows already ruled out
  by NJDG without a new frame theorem;
- the result is averaged over derivative zeros rather than uniform on every
  admitted dangerous selected packet;
- the condition number may be superprojectively bad on the dangerous sequence.

## 11. Determination

IRT-1A produces the first exact theorem-design contract after the architecture
survey:

\[
\boxed{
\text{SOFT-CONE ACTIVATION}
+
\text{PROJECTIVE FACTOR-THROUGH}
\Longrightarrow
\text{C-ACTUAL-KPH-FLOOR}.
}
\]

This strictly minimizes the foreign-theory lesson:

- no full second-channel reconstruction;
- no full frame on all directions;
- no exact operator equivalence;
- no exponential-kernel synthesis.

Only the dangerous singular cone must be seen.

Among already named channels, the derivative divisor is the cleanest one not
already collapsed by CF-A17 or SOURCE-II covariance.

## 12. Cursor

\[
\boxed{
\texttt{IRT-1B / MIXED-DIVISOR SOFT-CONE FRAME DESIGN}
}
\]

Tasks:

1. define a canonical derivative-divisor observation operator
   \(\mathcal O_F^{\Xi'}\) that does not depend on the KPH soft vector;
2. determine the smallest number/growth rate of derivative observations needed;
3. derive the exact algebraic relation between those observations and the
   selected reciprocal-Cauchy/KPH operator;
4. test whether the relation admits DD-BRIDGE with projective loss;
5. only then investigate DD-ACT from actual-zeta geometry.

No canonical theorem status changes.
