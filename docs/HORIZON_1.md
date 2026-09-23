# Horizon 1 — Independent Weil-Defect Theory

## Purpose

Horizon 1 packages the currently extracted Weil-defect machinery as an independently intelligible mathematical theory before any attempt to close the Riemann Hypothesis.

The horizon acceptance condition is:

> An outside mathematician should be able to enter this repository, understand the objects, identify exactly which results are imported versus internally derived, and audit the complete Weil-defect theorem chain without needing to assume any unresolved RH-facing claim.

Horizon 1 therefore ends **before** the actual-zeta exclusion problem.

## Stop boundary

The following are interfaces out of Horizon 1:

\[
\boxed{
\texttt{AZ-NEXTJET-LOC},
\quad
\texttt{C-ACTUAL-KPH-FLOOR},
\quad
\texttt{AZ-FIN-WEIL-NULL-EXTENSION}.
}
\]

Horizon 1 may complete while all three remain open.

## Phase map

\[
\boxed{
\begin{array}{ll}
\textbf{H1-P0} & \text{Consolidation and custody}\\
\textbf{H1-P1} & \text{Abstract defect calculus}\\
\textbf{H1-P2} & \text{Zeta-Weil specialization}\\
\textbf{H1-P3} & \text{Defect morphology theorem}\\
\textbf{H1-P4} & \text{Proof audit and theorem normalization}\\
\textbf{H1-P5} & \text{Public mathematical package}
\end{array}
}
\]

Current position:

\[
\boxed{
\text{H1-P0 COMPLETE}
\qquad
\text{H1-P1 ACTIVE}.
}
\]

---

## H1-P0 — Consolidation and custody

### Purpose

Recover the theorem corpus, freeze terminology, separate imported results from internal derivations, and prevent accidental theorem promotion.

### Entry condition

Existing research contains multiple Weil-facing reductions and proof fragments but no independent public theorem architecture.

### Allowed work

- proof inventory;
- terminology registry;
- source/provenance classification;
- dependency DAG;
- standing labels;
- separation of Weil-defect theory from RH closure;
- repository-level custody rules.

### Required outputs

- public README;
- proof-status ledger;
- research map;
- terminology registry;
- initial consolidation note;
- Horizon 1 specification.

### Exit condition

Every currently retained claim has:

1. a named object;
2. a standing label;
3. a known dependency location;
4. a clear RH-facing or RH-independent classification.

### Current status

**COMPLETE.** The terminology, standing system, Horizon 1 specification, proof ledger, and public research map are integrated.

---

## H1-P1 — Abstract defect calculus

### Purpose

Determine which parts of the machinery survive after removing zeta-specific arithmetic.

### Central question

\[
\boxed{
\text{What remains true for a general finite-index / Pontryagin-type screening problem?}
}
\]

### Primary objects

- finite negative index;
- positive screening complement;
- rank-one defect operators;
- finite-to-infinite screening;
- negative, neutral, and approximate-neutral screening boundaries;
- minimum-compensator graphs;
- operator null modes.

### Target theorem family

The phase should isolate statements of the schematic form

\[
\text{finite index}
\Longrightarrow
\text{screening alternative}
\Longrightarrow
\begin{cases}
\text{negative defect},\\
\text{attained neutral mode},\\
\text{non-attained approximate-neutral boundary},\\
\text{strict positive screening}.
\end{cases}
\]

without using \(\zeta\), \(\Xi\), primes, or quartet arithmetic except as examples.

### Main extraction problem

Minimize the hypotheses behind relations such as

\[
u=-X^*a
\]

and behind rank-one positivity defects of the form

\[
AA^*-g\otimes g.
\]

### Current result

H1-P1.0 extracted the basis-free defect operator

\[
D=S_+S_+^*-S_-S_-^*
\]

and the exact equivalence between \(J\)-nonnegativity, Loewner domination, and contractive Douglas screening. See [Abstract Defect Calculus](ABSTRACT_DEFECT_CALCULUS.md).

It also identified a distinct **non-attained approximate-neutral boundary** at critical screening norm.

### Exit condition

There is a self-contained list of abstract definitions and theorems whose statements do not depend on zeta-specific notation, including the finite-index/restricted-channel extension now targeted by H1-P1.1.

---

## H1-P2 — Zeta-Weil specialization

### Purpose

Reintroduce precisely the extra structure supplied by the zeta/Weil setting.

### Central question

\[
\boxed{
\text{Which stronger identities come from functional-equation and explicit-formula geometry?}
}
\]

### Required specialization results

- quartet channel decomposition;
- raw selected residue vector \(v\);
- zero-moment law
  \[
  \mathbf1^Tv=0;
  \]
- far response
  \[
  R_v(z)=O(|z|^{-2});
  \]
- completed-\(\Xi\) lift;
- compact-window Weil operator;
- finite prime-shift structure;
- logarithmic principal order.

### Constraint

H1-P2 may specialize H1-P1 but may not silently strengthen an abstract theorem by importing zeta-specific structure into its hypotheses after the fact.

### Exit condition

Every zeta-specific theorem states explicitly which H1-P1 theorem it specializes and which new arithmetic hypotheses it consumes.

---

## H1-P3 — Defect morphology theorem

### Purpose

Package the surviving screening-boundary morphologies as exact theorem families. H1-P1.0 shows that the abstract boundary has a third case beyond strict negative and attained neutral behavior: non-attained approximate neutrality.

### Negative branch target

\[
\boxed{
\text{persistent defect}
\Longrightarrow
\text{normalized negative signature}
\Longrightarrow
\mathbf1^Tv=0
\Longrightarrow
O(z^{-2})
\Longrightarrow
\text{finite/intermediate localization}
\Longrightarrow
\text{weighted next jet}.
}
\]

### Neutral branch target

\[
\boxed{
\text{neutral persistence}
\Longrightarrow
W_ck=0
\Longrightarrow
\text{log-order operator}
+
\text{finite arithmetic translations}.
}
\]

### Approximate-neutral branch target

H1-P2/P3 must decide whether the abstract non-attained critical branch

\[
\|X\|=1
\quad\text{with no norm-attaining vector}
\]

can occur in the zeta-Weil specialization and, if so, what arithmetic morphology it carries.

### Central question

> If screening does not erase the defect, or drives the margin to zero without producing a null mode, what exact form must the surviving obstruction take?

### Exit condition

The negative, attained-neutral, and any admissible approximate-neutral branches are stated as theorem packages with precise hypotheses, conclusions, and downstream open interfaces.

---

## H1-P4 — Proof audit and theorem normalization

### Purpose

Convert research-chain arguments into a theorem set that can be independently audited.

### Required work for every theorem

- canonical theorem label;
- exact hypotheses;
- exact conclusion;
- dependency list;
- source/import boundary;
- proof with no hidden transfer;
- edge cases;
- finite/infinite distinction;
- conditional/unconditional standing;
- counterexample or sharpness note where relevant.

### Naming convention

The public theorem sequence should use stable labels such as

\[
\texttt{WD-T1},\texttt{ WD-T2},\ldots
\]

with auxiliary lemmas and counterexamples under separate namespaces.

### Exit condition

Every theorem in the Horizon 1 dependency DAG has an auditable normalized statement and proof.

---

## H1-P5 — Public mathematical package

### Purpose

Turn the audited theorem system into a forward-facing mathematical artifact.

### Required deliverables

1. technical manuscript;
2. theorem index;
3. proof-status matrix;
4. dependency diagram;
5. examples and counterexamples;
6. appendix containing the RH-facing interfaces;
7. repository README aligned with the manuscript.

### Final public separation

The package should make the following distinction visually and logically explicit:

\[
\boxed{
\text{Here is the Weil-defect theory.}
}
\]

versus

\[
\boxed{
\text{Here are the additional actual-zeta statements needed for an RH application.}
}
\]

### Exit condition

An external reader can verify the Horizon 1 theorem package without traversing the original RH research history.

---

## Horizon 1 completion condition

Horizon 1 is complete when all of the following hold:

\[
\boxed{
\begin{aligned}
&\text{abstract defect theory extracted;}\\
&\text{zeta-Weil specialization normalized;}\\
&\text{negative, neutral, and approximate-neutral boundary morphologies classified;}\\
&\text{all theorem standings independently audited;}\\
&\text{RH-facing obligations isolated at explicit interfaces;}\\
&\text{public manuscript/package assembled.}
\end{aligned}
}
\]

No RH proof is required for Horizon 1 completion.

## Beyond Horizon 1

Later horizons may attack one or more actual-zeta interfaces, extend the defect calculus, formalize proofs, or develop computational certification.

Those horizons are intentionally left unspecified until Horizon 1 has a stable theorem inventory.
