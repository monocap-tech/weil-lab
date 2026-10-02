# IRT-1D — alignment necessity and alternate-channel triage

**Date:** 2026-10-02 (America/Los_Angeles)  
**Repository:** \`monocap-tech/weil-lab\`  
**Branch:** \`research/inverse-realization-transfer\`  
**Parent:** IRT-1C  
**Status:** **COMPLETE TRIAGE / ALIGNMENT NECESSITY PROVED ABSTRACTLY / DERIVATIVE CHANNEL HAS CLEAN INDEPENDENCE BUT NO BRIDGE / ARITHMETIC TOTAL-SOURCE CHANNEL HAS THE RIGHT RAY BUT THE WRONG RESPONSE SIGNATURE / PHASE-WINDING HAS NO SOURCE-FREE SEPARATOR POWER / SAME-EVENT P CHANNEL HAS RAY AND JURISDICTION MISMATCH / NO EXISTING CHANNEL SURVIVES BOTH ACTIVATION AND VANISHING-RESPONSE TESTS / IRT AT THEOREM-INPUT STOP**

## 0. Objective

IRT-1C returned no source hit for the mixed derivative Cauchy theorem.

IRT-1D asks whether the mixed-alignment requirement is itself only a disguised
KPH floor, and whether another already-custodied channel can satisfy the
soft-cone sandwich more naturally.

The answer is:

\[
\boxed{
\text{the implication is necessarily KPH-floor strength,}
}
\]

but this does not make a future theorem tautological if its lower and upper
controls come from genuinely independent zeta structure.

Under current custody, no existing candidate channel supplies both pieces.

## 1. General nonlinear sandwich

Let

\[
A_F=A_F^{\rm KPH}
\]

and let \(\mathcal O_F\) be a second-channel observable.

Assume on every relevant soft vector \(v\),

\[
\boxed{
\|\mathcal O_Fv\|\ge \alpha_F
}
\]

and

\[
\boxed{
\|\mathcal O_Fv\|
\le
\Phi_F(\|A_Fv\|),
}
\]

where \(\Phi_F\) is monotone near zero and has a projectively controlled inverse.

Then

\[
\alpha_F
\le
\Phi_F(\|A_Fv\|)
\]

implies

\[
\boxed{
\|A_Fv\|
\ge
\Phi_F^{-1}(\alpha_F).
}
\]

Thus any useful second channel needs only:

1. independent activation on the KPH soft sector;
2. an upper response that vanishes quantitatively with the KPH residual.

The linear factor-through theorem from IRT-1A is the special case

\[
\Phi_F(r)=H_F^br+\eta_F.
\]

## 2. Alignment-necessity theorem

Suppose the second channel has a projective activation scale

\[
\alpha_F\ge H_F^{-a}.
\]

If its response obeys any projectively invertible vanishing law

\[
\Phi_F(r)\to0
\quad(r\to0),
\]

then the resulting theorem excludes superprojective KPH softness.

Therefore:

\[
\boxed{
\text{independent activation}
+
\text{vanishing-response alignment}
\Longrightarrow
\text{KPH floor}.
}
\]

This is unavoidable.

The new mathematical content can therefore reside only in proving one or both
pieces from information not already equivalent to KPH.

There is no weaker representation-only stage after this point.

## 3. Candidate A — derivative divisor

### Activation side

Best of the candidates.

IRT-1B proves that \(n-1\) legal derivative sampling points give exact
injectivity on the zero-moment selected sector, with an explicit
Cauchy--Vandermonde determinant.

A projective frame theorem would therefore give an independent lower bound.

### Vanishing-response side

No source theorem is known.

Ordinary criticality controls

\[
D_{\tau,F}{\bf1},
\]

not

\[
D_{\tau,F}v.
\]

IRT-1C found no weighted mixed-divisor theorem converting KPH softness into
small derivative-frame response.

### Determination

\[
\boxed{
\text{INDEPENDENT CHANNEL YES / MIXED ALIGNMENT NO HIT}.
}
\]

The derivative divisor remains conceptually clean, but it does not advance
under current sources.

## 4. Candidate B — selected-only total source / Q-loc wedge

This candidate uses the correct dangerous selected channel.

SOURCE-II-7 gives a selected-only source wedge with projective lower size.

But on a KPH-dangerous failure sequence, SOURCE-II-5/8 force the complement
wedge itself to reproduce that nonzero source wedge:

\[
\frac{|W_{\rm cmp}|}{N_C}
\gtrsim
L^{-C_{\rm tot}}.
\]

Thus the available arithmetic observable does **not** vanish as

\[
KPH(F)\to0.
\]

It remains projectively large.

Therefore it cannot be the upper/vanishing side of the IRT soft-cone
sandwich.

Trying to prove it small is precisely the theorem-equivalent SOURCE-II-8 gate.

### Determination

\[
\boxed{
\text{RIGHT CHANNEL/RAY / WRONG RESPONSE SIGNATURE}.
}
\]

It detects the failure shadow rather than suppressing it.

## 5. Candidate C — phase / winding / argument data

There are two versions.

### Selected-only phase

Any phase/winding invariant built only from the selected finite divisor is
source-free selected geometry.

CF-A17 already realizes the full selected symmetry and bounded packet
jurisdiction with

\[
KPH=0.
\]

Therefore no universal selected-only phase law can exclude the KPH defect
unless the phase invariant is itself chosen to vanish precisely on the bad
locus.

In that case a projective lower bound for the actual zeta image is simply
another selected separator theorem implying the KPH floor.

### Full-\(\Xi\) phase

A phase or argument observable using the full completed function contains the
complementary logarithmic-derivative field.

That returns to the same actual-zeta source problem:

\[
\text{selected packet}
+
\text{complement field}
\to
\text{orientation}.
\]

No retained phase theorem isolates a projectively controlled weighted soft-ray
quantity.

### Determination

\[
\boxed{
\text{SOURCE-FREE VERSION TOO WEAK / SOURCE-SPECIFIC VERSION IS THE SAME
MISSING ORIENTATION THEOREM}.
}
\]

No concrete phase/winding channel survives current custody.

## 6. Candidate D — same-event P activation channel

The LOTUS interface has unusually strong upstream data.

For one false-RH P event, it supplies:

- the same actual packet \(F\);
- a canonically marked coefficient ray \(v_t\);
- exact P activation
  \[
  \mathfrak a_P(E)>1;
  \]
- exact Q evaluation on the same ray;
- an exact raw half-line exponential--Cauchy identity.

This looks like an ideal independent channel.

But Q-loc failure uses a different selected channel \(v_Q\), namely the
minimal-cubic/KPH-dangerous ray.

INTERFACE-2 explicitly identifies the selector swap:

\[
v_t
\ne
v_Q
\quad\text{without a new theorem}.
\]

Thus the P channel observes one ray while the KPH floor quantifies over the
KPH minimizing ray.

This is a **ray mismatch**.

Moreover false RH launches the P event; it does not independently force the
same packet into the Q-loc dangerous jurisdiction.

Therefore a same-event P channel cannot presently prove the universal local
KPH floor.

To make it useful one would need at least:

1. a same-packet theorem putting the launched event into Q-loc;
2. a projective overlap/alignment theorem between \(v_t\) and \(v_Q\);
3. the already missing support/native transfer from raw Cauchy response to
   the route-native scalar.

That is more missing structure than the derivative-divisor route.

### Determination

\[
\boxed{
\text{UPSTREAM AND INDEPENDENT / RAY MISMATCH + JURISDICTION MISMATCH}.
}
\]

Reject as the next IRT channel.

## 7. Candidate E — native/arithmetic feature channels

APR1/LJFR and related Prime--Weil channels can provide actual-zeta arithmetic
information on the corrected first-jet operator.

But near CF-A17:

\[
m(F)\ge c_*>0
\]

can coexist source-freely with

\[
KPH(F)=0.
\]

Hence native feature activation does not vanish with KPH softness.

The missing feature-to-KPH attachment is already JOINT-2's actual-zeta source
gate and is projectively equivalent to the KPH floor in this jurisdiction.

### Determination

\[
\boxed{
\text{GOOD ACTIVATION / NO INDEPENDENT VANISHING BRIDGE}.
}
\]

No new IRT interface is gained.

## 8. Candidate F — global null-response scalar

The exact selected KPH eigenchannel identity gives a completed-zeta global
response scalar involving selected first jets and all unselected zeros.

On the zero-moment sector

\[
q={\bf1}^Tv=0,
\]

the regularization constants disappear and the global complement sum is
absolutely convergent.

However the exact eigenchannel identity has the form

\[
\mathcal S_\Xi(F,v)
=
\epsilon(1-\theta)q.
\]

Thus on the exact zero-moment channel,

\[
\boxed{
\mathcal S_\Xi(F,v)=0
}
\]

independently of the KPH eigenvalue \(\theta\).

So this scalar is not an activating second channel on the minimal-cubic
zero-moment sector.

Its source-specific cancellation law is useful diagnostically but cannot be
the IRT-1A lower observable.

### Determination

\[
\boxed{
\text{RIGHT RAY / IDENTICALLY NULL ON THE ZERO-MOMENT SECTOR}.
}
\]

Reject as an activation channel.

## 9. Candidate G — generic World-to-atom separator

The post-WORLD regroup proves that the Q-loc failure residue is already atomic:

\[
\boxed{
\text{one selected channel}
+
\text{one scalar complement wedge}.
}
\]

A future actual-zeta theorem can therefore act directly on that atomic witness
without constructing another large carrier.

This is a legitimate theorem-input species.

But it is not currently a concrete independent channel.

Inside the developed \(U_*\) architecture, excluding the bad Q-loc atom with
the required every-packet projective quantifier remains theorem-equivalent to
the KPH floor.

Thus World-to-atom is the correct **source provenance level**, not a weaker
intermediate theorem already in hand.

## 10. Alternate-channel matrix

| Candidate | Independent upstream data? | Sees KPH soft ray? | Projective activation? | Vanishes with KPH residual? | Current disposition |
|---|---:|---:|---:|---:|---|
| derivative divisor | yes | potentially | not proved | not proved | clean but source-stopped |
| total-source / complement wedge | selected-only | yes | yes | **no; stays large** | failure shadow |
| selected-only phase | yes | packet only | possible | no source-free bridge | CF-A17 blocks |
| full-\(\Xi\) phase | yes | potentially | not proved | not proved | complement-field debt |
| P same-event ray | yes | different ray | yes on \(v_t\) | raw relation only | ray/jurisdiction mismatch |
| APR/native feature | arithmetic | different adjudicator | potentially yes | no | JOINT-2 gate |
| null-response scalar | actual zeta | correct eigenchannel | **zero on q=0** | trivially | no activation |
| World-to-atom | yes in principle | yes by design | theorem-dependent | theorem-dependent | source-input species only |

## 11. No existing channel wins the sandwich

The triage therefore produces no current candidate satisfying simultaneously:

\[
\boxed{
\text{independent upstream definition}
}
\]

\[
\boxed{
\text{projective activation on every KPH-soft vector}
}
\]

and

\[
\boxed{
\text{projectively controlled response vanishing with the KPH residual}.
}
\]

Every current candidate fails at least one coordinate.

This is the exact point where IRT reaches a theorem-input boundary.

## 12. Relation to “KPH-floor strength in disguise”

The alignment theorem is necessarily strong enough to imply a KPH floor once
combined with a conditioned second channel.

But it is not logically the same as writing

\[
KPH(F)\ge H_F^{-A}
\]

if:

1. the second-channel activation is independently proved from another divisor,
   source, or World law;
2. the vanishing-response bridge is an actual cross-channel theorem;
3. neither premise assumes the KPH floor or uses the minimizing vector
   adaptively.

That is exactly how successful foreign theories operate.

So IRT has not shown the desired theorem is tautological.

It has shown that **all remaining novelty must be in actual-zeta cross-channel
alignment**, not in representation.

## 13. Final IRT theorem signature

The most general surviving input is:

### AZ-WORLD-SOFT-ORIENTATION

For every sufficiently high admitted packet in the local Key-C jurisdiction,
actual-zeta provenance supplies an upstream observable \(\mathcal O_F\) such
that on every unit KPH-soft vector \(v\),

\[
\boxed{
\|\mathcal O_Fv\|\ge H_F^{-a}
}
\]

and

\[
\boxed{
\|\mathcal O_Fv\|
\le
\Phi_F(\|A_F^{\rm KPH}v\|),
}
\]

where \(\Phi_F\) has a projectively controlled inverse near zero.

Then C-ACTUAL-KPH-FLOOR follows.

The theorem may be scalar, low-rank, mixed-divisor, or arithmetic. Its
provenance matters more than its output dimension.

## 14. Determination

IRT-1D establishes:

- bounded linear factor-through is necessary: **NO / nonlinear vanishing law
  suffices**;
- some projectively invertible vanishing-response law is necessary for the
  soft-cone sandwich: **YES**;
- any such law plus independent activation implies a KPH floor: **YES**;
- derivative divisor is the only current clean independent channel: **YES,
  but source-stopped**;
- SOURCE-II total-source wedge can be the vanishing upper channel: **NO**;
- selected-only phase/winding supplies a source-free separator: **NO**;
- same-event P channel removes the ray mismatch: **NO**;
- APR/native feature channel bypasses JOINT-2: **NO**;
- global null-response scalar activates the zero-moment KPH channel: **NO**;
- generic World-to-atom remains a lawful new theorem species: **YES**;
- a concrete retained World-to-soft-cone theorem exists: **NO**;
- one existing channel should be promoted to IRT-2 under current inputs: **NO**;
- IRT representation/design line is structurally exhausted: **YES**;
- KPH floor proved: **NO**;
- NEXTJET proved: **NO**;
- RH proved: **NO**.

## 15. Cursor

Set the investigation to theorem-input stop:

\[
\boxed{
\texttt{TSTOP-IRT-PENDING-ACTUAL-ZETA-WORLD-SOFT-ORIENTATION-INPUT}
}
\]

Re-entry requires one named theorem/source/construction satisfying at least one
of:

1. derivative-divisor soft-cone activation **and** mixed alignment;
2. an actual-zeta phase/arithmetic observable with a proved vanishing-response
   law on the KPH soft cone;
3. a same-event cross-jurisdiction theorem resolving both ray alignment and
   native transfer;
4. a direct World-to-atom separator whose implication to the local KPH floor is
   explicit.

Do not open another representation architecture or adjacent interpolation
formalism under unchanged inputs.

No canonical theorem status changes.
