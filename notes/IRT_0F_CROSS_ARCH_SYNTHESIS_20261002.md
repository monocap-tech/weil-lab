# IRT-0F — cross-architecture synthesis and theorem-type extraction

**Date:** 2026-10-02 (America/Los_Angeles)  
**Repository:** \`monocap-tech/weil-lab\`  
**Branch:** \`research/inverse-realization-transfer\`  
**Parent:** IRT-0E  
**Status:** **COMPLETE SYNTHESIS / REPRESENTATION-ONLY ROUTES EXHAUSTED / COMMON SUCCESS INGREDIENT IDENTIFIED AS INDEPENDENT RIGIDITY + STABLE OBSERVABILITY / POST-FREEZE TOWER SMALLNESS IS NOT A WEAKER GATE BY SOURCE-II-8 / NEW SURVIVING THEOREM SHAPE IS UPSTREAM MIXED-DIVISOR ORIENTATION / NEXT CURSOR IRT-1A OBSERVABLE-ORIENTATION THEOREM DESIGN**

## 0. Objective

IRT-0 has now screened five distinct foreign architectures:

1. Weyl/Herglotz/two-spectra;
2. generalized Nevanlinna/Pontryagin, including local \(\pi_+\);
3. canonical systems/de Branges and Suzuki shift flow;
4. systems/Loewner/semigroup/functional calculus;
5. moment/Prony/super-resolution.

IRT-0F asks one question:

> What structural ingredient is present in the foreign theories when they
> actually transfer information between two data species, and absent when they
> merely re-represent the unknown complement?

The answer is stable across all five families.

\[
\boxed{
\text{successful transfer}
=
\text{independent rigidity source}
+
\text{stable observability/conditioning}.
}
\]

Representation alone never supplies the missing packet theorem.

## 1. Cross-architecture comparison

### A. Weyl/Herglotz/two-spectra

The transfer succeeds because one self-adjoint realization imposes:

- positivity;
- real spectral support;
- interlacing;
- normalization;
- common resolvent structure.

These are independent constraints on the spectral data. They are not derived
from knowing the two spectra separately.

For zeta, the classical version is too strong: its real-spectrum condition is
RH-strength.

### B. Global generalized Nevanlinna / Pontryagin

The transfer retains rigidity by spending a finite negative-index budget.

This allows a finite exceptional nonreal divisor but still imposes a global
structural count.

For zeta, one fixed finite \(\kappa\) is too restrictive because false RH does
not imply finitely many off-critical zeros.

### C. Local generalized Nevanlinna / local \(\pi_+\)

This regime is false-RH compatible but loses rigidity.

The arbitrary local holomorphic summand absorbs the pole-removed outside field:

\[
\tau_{(0)}
\sim
A_{F,\Omega}.
\]

The realization therefore represents rather than constrains the missing data.

### D. Canonical systems / de Branges

The holomorphic slack is eliminated by a common positive Hamiltonian and
Hermite--Biehler law.

This supplies exactly the desired rigid coupling, but again at RH-strength
real-spectrum positivity.

Suzuki's shift family confirms that safe positivity propagates outward, while
crossing inward through an off-critical zero produces a local negative well
whose selected-pole finite part collapses to the same outside field.

### E. Systems / Loewner

Exact transfer is possible if enough independent resolvent samples identify
the finite realization with controlled rank and conditioning.

Without those independent observations, the target exponential response is
only represented, not identified.

The continuum functional-calculus route collapses to the same original-divisor
weighted contour already present in NJDG-7.

### F. Prony / super-resolution

Exact nonlinear recovery is possible from enough independent moments together
with a finite sparse model.

But SOURCE-II does not expose the reciprocal moments independently; they are
entangled with the same complement field in the joint finite part.

Even with oracle moments, quantitative stability near collisions requires
rank/conditioning information not currently available packetwise.

## 2. The common foreign success mechanism

All successful foreign transfers contain three logically separate ingredients.

### R1 — independent model restriction

The unknown object belongs to a class smaller than "all meromorphic functions
with the observed local poles."

Examples:

- self-adjoint/Herglotz;
- finite Pontryagin index;
- positive canonical system;
- known finite realization order;
- known sparse atomic rank.

### R2 — independent observations

The data used for reconstruction/control are not algebraically the same
functional whose value is being bounded.

Examples:

- a second boundary spectrum;
- external resolvent samples;
- an independent moment stream;
- a fixed transfer law/measurement operator.

### R3 — quantitative observability

The restriction and observations control the unknown with a nondegenerate
condition number.

Examples:

- interlacing/positive residues;
- full-rank Loewner matrix;
- nondegenerate Vandermonde/Prony map;
- positive reproducing kernel;
- stable frame inequality.

Without R3, exact uniqueness can still be useless under the finite errors
present in SOURCE-II.

Therefore the foreign theorem template is

\[
\boxed{
\text{R1 model restriction}
+
\text{R2 independent measurements}
+
\text{R3 stable observability}
\Longrightarrow
\text{target response control}.
}
\]

## 3. What the current zeta stack already has

The project already has:

- exact common-carrier formulas;
- arbitrary-order collision-safe finite-part coordinates;
- exact weighted original-divisor contours;
- exact source covariance;
- selected-only total-source transversality;
- arbitrary fixed projective truncation accuracy;
- a frozen multiplier chosen without complement data.

Those correspond largely to **representation** and **source selection**.

What it does not have is R1--R3 for the actual unselected complement.

In particular, the complement can still align with the selected soft direction
in precisely the way that destroys the local KPH floor.

## 4. SOURCE-II-8 forbids a false intermediate gate

The synthesis must respect the terminal SOURCE-II result.

SOURCE-II-7 gives a selected-only frozen multiplier
\(\psi_*^{\rm tot}\) with total-source margin

\[
|\mathcal S_v[\psi_*^{\rm tot}]|
\ge
L^{-C_{\rm tot}}.
\]

SOURCE-II-4/5 gives

\[
\mathcal S_v[\psi_*^{\rm tot}]
=
\mathcal T_{K,L}[\psi_*^{\rm tot}]
+
O_K(L^{-K/2}).
\]

On a local KPH-dangerous failure sequence, choose fixed
\(K>2C_{\rm tot}\). Then the tower is forced to obey

\[
|\mathcal T_{K,L}[\psi_*^{\rm tot}]|
\ge
\frac12L^{-C_{\rm tot}}
\]

for all sufficiently large packets.

Therefore a theorem of the form

\[
|\mathcal T_{K,L}[\psi_*^{\rm tot}]|
=
o(L^{-C_{\rm tot}})
\]

on every dangerous packet is not a weaker localization lemma.

SOURCE-II-8 proves it is projectively equivalent to exclusion of the local
KPH-floor failure sequence.

Hence IRT must not rename post-freeze tower smallness as a new intermediate
theorem.

## 5. The new theorem must live upstream

A genuinely different theorem must constrain the actual divisor **before**
the frozen tower value is invoked.

This changes the target from

\[
\text{“prove the tower is small”}
\]

to

\[
\boxed{
\text{“prove the complement cannot acquire the bad orientation/alignment
that would make the packet KPH-dangerous.”}
}
\]

The theorem must use information independent of the same frozen explicit-formula
identity.

This is the first important synthesis result.

## 6. Minimal surviving theorem shape

The weakest abstract theorem type located by IRT-0 is an
**observable-orientation theorem**.

Let \(F\) be an admitted selected dangerous packet and let
\(\mathcal D(F)\) denote data available from the selected packet and some
independent second channel before the complement response is read.

The theorem would provide an observable

\[
\mathcal O_F
\]

fixed from \(\mathcal D(F)\) such that for every admitted actual complement
environment \(\mathcal C\),

\[
\boxed{
\operatorname{dist}
\left(
\mathcal R(F,\mathcal C),
\mathcal S_F
\right)
\ge
L^{-C}.
}
\]

Here:

- \(\mathcal R(F,\mathcal C)\) is the complement response in whatever
  realization is used;
- \(\mathcal S_F\) is the selected soft/compensating direction whose approach
  produces KPH/NEXTJET failure;
- \(C\) is fixed/projective;
- \(\mathcal O_F\) and the orientation test are chosen without reading
  \(\mathcal C\).

Equivalent forms may be:

\[
|\det M_F(\mathcal C)|\ge L^{-C},
\]

\[
\sigma_{\min}(M_F(\mathcal C))\ge L^{-C},
\]

\[
|\langle q_F,\mathcal R(F,\mathcal C)\rangle|\ge L^{-C},
\]

or a signed phase/discrepancy inequality.

The point is not the coordinate form.

The essential content is:

\[
\boxed{
\text{the actual complement is uniformly transverse to the dangerous
selected soft direction.}
}
\]

## 7. Why this is the common residue of the foreign theories

### Herglotz

Interlacing and positive residues prevent arbitrary spectral orientation.

### Pontryagin

Finite negative index limits how much bad orientation can occur.

### Canonical systems

Positive Hamiltonian structure fixes phase orientation through the transfer
matrix/HB law.

### Loewner

Full-rank sample matrices give quantitative observability.

### Prony

Nondegenerate moment/Vandermonde maps make the hidden atomic state observable.

So the common invariant is not "spectral theory," "positivity," or
"realization" per se.

It is:

\[
\boxed{
\text{stable orientation of hidden data relative to an independently fixed
measurement geometry}.
}
\]

That is exactly the piece missing from the current zeta packet reduction.

## 8. What could serve as the second channel

IRT-0 does not prove that any candidate works.

The remaining admissible second-channel species are narrower than before.

A useful channel must:

1. survive selected-pole subtraction;
2. not be algebraically equivalent to the existing finite-part tower;
3. be available before the complement-dependent multiplier/tower value;
4. have packetwise, not average, jurisdiction;
5. carry projective conditioning.

Possible theorem species include:

### X1 — derivative-divisor stable frame

A theorem assigning to every dangerous \(\Xi\)-packet a finite/growing family
of \(\Xi'\)-data whose observation matrix has a projective lower singular-value
bound and whose mixed transfer controls the original-divisor weighted response.

This is stronger and more precise than the failed NJDG critical-point route:
existence of derivative zeros is not enough; stable mixed observability is the
actual target.

### X2 — local phase/orientation law

A theorem giving a projective lower bound on a phase derivative, argument
increment, winding discrepancy, or signed mixed-divisor quantity attached
before the complement is read.

It must survive false RH and selected-pole renormalization.

### X3 — local index budget tied to the selected packet

A theorem that assigns a finite local negative-index/defect budget to the
canonical packet and quantitatively limits compensating complement alignment,
without assuming a globally finite exceptional divisor.

Local generalized-Nevanlinna membership alone is too weak; the index must be
bounded by actual zeta structure.

### X4 — independent arithmetic measurement family

A second explicit-formula/arithmetic observable whose coefficients are fixed
from selected/public data and are not linearly covariant with the existing
SOURCE-II total-source functional, together with a stable frame inequality.

This would be a truly new arithmetic data channel rather than another rewrite
of the same formula.

## 9. What does not qualify

IRT-0F rejects the following as a "new theorem type":

- another exact representation of the same divisor;
- another finite jet or resolvent coordinate;
- another local generalized-Nevanlinna realization with free holomorphic slack;
- full positive de Branges/Herglotz structure that already forces RH;
- one fixed finite Pontryagin index for the global divisor;
- Loewner/Prony reconstruction using complement-chosen measurements;
- post-freeze total-tower smallness;
- averaged derivative-zero or gap statistics promoted to every packet;
- a theorem whose condition number can collapse on the dangerous sequence.

## 10. Relation to "genuinely new"

IRT-0 resolves the terminology issue that motivated this branch.

The project should not say merely

\[
\text{“a genuinely new theorem is required.”}
\]

The sharper statement is now:

\[
\boxed{
\text{a theorem outside the current dependency closure must provide
complement-oblivious stable orientation information from an independent
channel.}
}
\]

This says exactly *what kind* of additional theorem is missing.

It does not claim that no such theorem exists in mathematics, nor that proving
one would necessarily be historically novel.

## 11. IRT-0 final synthesis matrix

| Architecture | What makes transfer work | Why direct zeta use fails |
|---|---|---|
| Herglotz / two-spectra | positivity + common self-adjoint realization | RH-strength real spectrum |
| global \(N_\kappa\) | finite negative-index rigidity | globally finite exceptional budget |
| local \(N(\Omega)\) | none beyond representability | holomorphic slack retains \(A_{F,\Omega}\) |
| canonical / de Branges | positive Hamiltonian + phase rigidity | RH-strength positivity |
| Suzuki flow | global shifted positivity/zero-free law | wrong direction; finite part returns to outside field |
| Loewner | independent rank-scale samples + full-rank observability | sample-frame/rank debt |
| semigroup calculus | continuum resolvent data | collapses to original-divisor contour |
| Prony | independent moments + finite rank + stable inversion | observability/rank/collision-stability debt |

## 12. Determination

IRT-0 is complete as an architecture screen.

The investigation has not proved NEXTJET, KPH, or RH.

It has materially narrowed the missing input.

The missing theorem is **not**:

- a representation theorem;
- an exponential-kernel identity;
- a finite interpolation formula;
- or another source-coordinate rewrite.

The surviving theorem type is:

\[
\boxed{
\textbf{COMPLEMENT-OBLIVIOUS STABLE MIXED-DIVISOR OBSERVABILITY / ORIENTATION.}
}
\]

Any future theorem candidate should be tested directly against this signature.

## 13. Next cursor

Open the first theorem-design stage rather than another architecture survey:

\[
\boxed{
\texttt{IRT-1A / OBSERVABLE-ORIENTATION THEOREM DESIGN}
}
\]

Tasks:

1. formalize the dangerous soft direction in a coordinate-independent way;
2. identify the smallest independent second-channel datum that could measure
   orientation against it;
3. state a candidate projective frame/transversality inequality;
4. prove that the candidate would imply either
   \(\texttt{AZ-NEXTJET-LOC}\) or
   \(\texttt{C-ACTUAL-KPH-FLOOR}\);
5. audit whether the candidate is genuinely upstream or merely equivalent to
   the frozen tower/KPH gate.

No canonical theorem status changes.
