# RH-Facing Interface Appendix

## H1-P5.4 — Exact Horizon-1 stop boundary

This appendix records the open actual-zeta interfaces reached by the
independent Weil-defect theory.

It is not part of the proof-producing theorem spine.  No interface listed here
is imported upstream to prove the Horizon-1 theorem that reaches it.

The appendix distinguishes:

1. what Horizon 1 already proves before the interface;
2. the exact missing statement;
3. which morphology branch consumes it;
4. whether the interface is primary or only a stronger sufficient refinement;
5. what would follow if the interface were discharged;
6. what does not follow without it.

---

# 1. AZ-NEXTJET-LOC

## 1.1 Branch

**Consumed by:** the fixed-packet persistent negative morphology, WD-T37.

**Status:** OPEN.

**Type:** primary actual-zeta interface.

## 1.2 Upstream output supplied by Horizon 1

Assume the WD-T37 fixed-packet negative branch hypotheses.  Horizon 1 supplies:

- a nonzero persistent selected negative endpoint ray;
- selected-amplitude-normalized representatives with diverging norm;
- normalized full Weil negativity bounded away from zero;
- a nonzero finite selected raw source \(v\);
- the zero-moment identity
  \[
  \mathbf 1^Tv=0;
  \]
- inverse-square rational-response decay
  \[
  R_v(z)=O(|z|^{-2});
  \]
- for every fixed bounded selected-preserving multiplier \(\psi\), the far
  complementary estimate
  \[
  \mathcal F_{v,R}[\psi]
  =
  O\!\left(\frac{\log R}{R}\right);
  \]
- localization of the remaining finite/intermediate complementary divisor into
  the weighted completed-\(\Xi\) next-jet field
  \[
  \boxed{
  \mathcal N_{v,R}[\psi]
  =
  \sum_{\mu}^{\rm near}
  m_\mu\psi(\mu)
  \frac{H_v^{(m_\mu)}(\mu)}
  {\Xi^{(m_\mu)}(\mu)}.
  }
  \]

The far divisor has therefore been quantitatively removed up to an arbitrarily
small \(O((\log R)/R)\) error.  The remaining burden is local/finite-scale.

## 1.3 Missing statement

The interface asks, in the quantifier regime required by the application:

> Can the actual complementary zeta divisor realize the weighted reciprocal
> completed-\(\Xi\) next-jet geometry forced by the nonzero selected source
> \(v\)?

Equivalently, one needs an actual-zeta theorem controlling or excluding the
weighted near next-jet field strongly enough to contradict or close the
persistent negative morphology.

The interface name is

~~~text
AZ-NEXTJET-LOC
~~~

because the missing information is local/near-field control after the far
divisor has already been disposed of.

## 1.4 What discharge would accomplish

A sufficiently strong theorem at AZ-NEXTJET-LOC would close the arithmetic
stop in WD-T37 for the branch and quantifiers covered by that theorem.

In the intended RH application, such a closure could exclude the corresponding
fixed-packet persistent negative morphology.

The exact global conclusion would still have to be assembled with the other
morphology branches and their own hypotheses; discharge of this interface is
not, by itself, a statement that RH has been proved.

## 1.5 What Horizon 1 does not claim

Horizon 1 does not prove:

- that the actual zeta divisor cannot realize \(\mathcal N_{v,R}[\psi]\);
- a uniform source-free lower bound for the weighted next-jet field;
- a positive lower bound obtained merely from the far-tail estimate;
- that adaptive cutoffwise scalar cancellation gives a global bypass.

WD-T33 shows instead that cutoffwise adaptive cancellation reallocates the
explicit-formula balance: the corresponding prime term collapses onto the far
term.  Asymptotic conclusions require a fixed or uniformly bounded multiplier
family.

---

# 2. C-ACTUAL-KPH-FLOOR

## 2.1 Branch

**Associated with:** the negative morphology WD-T37.

**Status:** OPEN.

**Type:** stronger special-packet sufficient refinement.

This is not the generic primary interface.  It is retained for the
KPH/reciprocal-Cauchy packet class where stronger packetwise structure is
available.

## 2.2 Upstream output supplied by Horizon 1

The same WD-T37 upstream outputs are available:

- fixed selected negative endpoint custody;
- nonzero zero-moment selected source;
- inverse-square far decay;
- \(O((\log R)/R)\) far-tail control;
- localization to the weighted near next-jet field.

The additional KPH packet structure is not automatically supplied by the
generic morphology theorem; it is part of the special-packet setting in which
this refinement is posed.

## 2.3 Missing statement

One seeks a packetwise transversality/KPH floor strong enough to prevent the
actual complementary divisor from supplying the compensation demanded by the
selected negative source.

The interface is recorded as

~~~text
C-ACTUAL-KPH-FLOOR
~~~

to emphasize that it is a stronger coercive/transversality statement, not
merely the generic next-jet localization question.

## 2.4 Logical role

A suitable C-ACTUAL-KPH-FLOOR theorem can serve as a **sufficient refinement**
for closing the same packetwise negative branch.

It is not used to prove WD-T37, and failure to establish it does not weaken the
generic WD-T37 reduction to AZ-NEXTJET-LOC.

## 2.5 What Horizon 1 does not claim

Horizon 1 does not claim:

- a generic KPH floor for all packets;
- that the packetwise floor follows from zero moment;
- that the compactness or finite-head approximation theorem supplies such a
  floor;
- that C-ACTUAL-KPH-FLOOR is logically necessary whenever a different
  AZ-NEXTJET-LOC theorem could close the branch.

---

# 3. AZ-FIN-WEIL-NULL-EXTENSION

## 3.1 Branch

**Consumed by:** the attained fixed-packet neutral morphology, WD-T38.

**Status:** OPEN.

**Type:** primary support/right-limit interface.

## 3.2 Upstream output supplied by Horizon 1

Assume the WD-T38 neutral-branch hypotheses:

- one fixed finite selected packet;
- critical right approach;
- the attained-neutral rather than negative-fall-through alternative;
- a finite-exception unit-gain selected relation
  \[
  C_c^{*}C_cu=u;
  \]
- a nonzero physical adjoint realization
  \[
  C_cu=P_c^{*}k;
  \]
- carrier identification with the compact-window Weil form/operator used in
  the arithmetic part.

Then Horizon 1 proves the nonzero physical null equation

\[
\boxed{
W_ck=0.
}
\]

The corresponding compact-window operator species is:

- logarithmic-order nonlocal archimedean part;
- finitely many symmetric prime-power translations;
- finite-rank pole term.

Its symbol/form order is

\[
\boxed{
\Psi_c(t)=\log|t|+O_c(1).
}
\]

Horizon 1 also fixes the endpoint/right-limit threshold convention:

- away from a prime-power threshold, sufficiently small strict right
  enlargements use the same active prime set;
- at a threshold, the strict right-limit operator has a finite
  equality-threshold correction.

No positive-Sobolev or quasianalytic continuation gain is inferred from this
logarithmic form estimate.

## 3.3 Missing statement

Let \(\widetilde k\) denote the zero extension of the endpoint neutral mode.

The interface asks:

> For an actual nonzero finite-exception unit-gain neutral mode satisfying
> the endpoint equation
> \[
> P_{[-c,c]}\mathcal W_c^{\rm ext}\widetilde k=0,
> \]
> does the same fixed relation satisfy the correct right-limit compact-window
> equation on some strict enlargement?

Away from a prime threshold, this is the exterior-collar question

\[
\mathcal W_c^{\rm ext}\widetilde k=0
\]

on a nontrivial collar outside the endpoint interval.

At a threshold, the question uses the finitely corrected strict right-limit
operator

\[
\mathcal W_{c+}^{\rm ext}.
\]

The interface name is

~~~text
AZ-FIN-WEIL-NULL-EXTENSION
~~~

because the missing theorem is a finite-exception actual-Weil null-extension
or support-rigidity statement.

## 3.4 What discharge would accomplish

A positive resolution strong enough for the required branch would determine
whether the attained endpoint neutral relation persists correctly into a
strict right enlargement.

Depending on the direction of the theorem, it could exclude an endpoint-only
neutral mode or force a stronger persistence relation.

That would close the support stop of WD-T38 for the hypotheses covered by the
theorem.

## 3.5 What Horizon 1 does not claim

Horizon 1 does not prove:

- that \(W_ck=0\) implies zero extension satisfies the enlarged equation;
- an exterior unique-continuation theorem;
- quasianalyticity from logarithmic form order;
- positive-Sobolev regularity of the neutral mode;
- termwise vanishing of pole, prime, and archimedean contributions;
- persistence across a prime threshold without the finite threshold
  correction.

The neutral equation is a global quadratic/operator cancellation.  The
support-extension question is genuinely additional.

---

# 4. Relation among the interfaces

The two primary fixed-packet exits are

~~~text
WD-T37  →  AZ-NEXTJET-LOC
WD-T38  →  AZ-FIN-WEIL-NULL-EXTENSION
~~~

The stronger special-packet refinement is

~~~text
WD-T37  →  C-ACTUAL-KPH-FLOOR
~~~

No arrow points from any open interface back into the Horizon-1 theorem DAG.

The noncompact morphology WD-T39 adds no new interface.  It decides when a
sequence has failed to enter one of the fixed-packet branches and when
background noncompactness remains possible after selected custody is already
anchored.

---

# 5. Horizon-1 boundary statement

The package boundary is exactly:

\[
\boxed{
\text{independent Weil-defect theory}
\quad\Vert\quad
\text{actual-zeta interface problem}.
}
\]

Horizon 1 establishes the theory on the left and reaches the named interfaces
on the right.

It does not claim that those interfaces are solved, and it does not claim RH
closure.
