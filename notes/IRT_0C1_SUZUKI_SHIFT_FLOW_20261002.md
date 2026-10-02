# IRT-0C1 — Suzuki-shift parameter-flow audit

**Date:** 2026-10-02 (America/Los_Angeles)  
**Repository:** \`monocap-tech/weil-lab\`  
**Branch:** \`research/inverse-realization-transfer\`  
**Parent:** IRT-0C  
**Status:** **COMPLETE / EXACT OUTWARD POSITIVITY FLOW LOCATED / INWARD PROPAGATION FAILS BY SIGN LOSS / SHIFT POSITIVITY IS EQUIVALENT TO A GLOBAL ZERO-FREE HALF-PLANE / REFLECTED-PAIR NEGATIVE WELL IDENTIFIED / SELECTED-POLE RENORMALIZATION COLLAPSES IT TO THE EXISTING OUTSIDE FIELD / NO NEW NEXTJET CLOSURE / NEXT CURSOR IRT-0D SYSTEMS-REALIZATION CLASS SCREEN**

## 0. Objective

IRT-0C left a narrow question:

> Starting from a shift \(\omega\) where the zeta-derived canonical/Herglotz
> structure is already valid, can one propagate a strictly weaker packet-local
> invariant toward the critical regime without proving the full RH-strength
> positivity statement?

The answer is now substantially determined.

Suzuki's later shifted screw-function formalism gives an exact \(\omega\)-flow,
but the positivity-preserving direction is outward, not inward. The invariant
it controls is a global zero-free half-plane, not the selected packet.
A local adverse signature does appear when the shift crosses an off-critical
zero, but canonical selected-pole subtraction reduces its finite part to the
already known outside field.

## 1. Two different safe thresholds must be distinguished

The 2012 canonical-system paper contains two different thresholds.

### Innerness / de Branges availability

For

\[
\Theta_\omega(z)
=
\frac{\xi(1/2-\omega-iz)}
     {\xi(1/2+\omega-iz)},
\]

Suzuki records that the required inequality, hence meromorphic innerness, is
known unconditionally for

\[
\omega\ge \frac12.
\]

More precisely, Proposition 1.2 states that for \(\omega_0\ge0\),

\[
\xi(s)\ne0
\quad\text{for}\quad
\Re s>\frac12+\omega_0
\]

is equivalent to \(\Theta_\omega\) being meromorphic inner for every
\(\omega>\omega_0\).

### Explicit Hamiltonian construction

The explicit Fredholm-determinant canonical-system construction in that paper
is proved under the stronger technical restriction

\[
\omega>1.
\]

Suzuki explicitly separates this from the innerness threshold and remarks that
the construction is expected to extend unconditionally to \(\omega>1/2\);
the main added issues are kernel/operator regularity, not a new zero-free
theorem.

Therefore the branch must not conflate

\[
\boxed{\omega\ge1/2\ \text{innerness}}
\]

with

\[
\boxed{\omega>1\ \text{published explicit Hamiltonian construction}.}
\]

## 2. Exact shifted screw-function flow

Suzuki's 2023 shifted screw function is

\[
\Psi_\omega(t)
=
e^{-\omega t}\Psi(t)
+
2\omega\int_0^t e^{-\omega u}\Psi(u)\,du
+
\omega^2\int_0^t(t-u)e^{-\omega u}\Psi(u)\,du,
\qquad t>0.
\]

Its Fourier--Laplace transform is

\[
\boxed{
\int_0^\infty \Psi_\omega(t)e^{izt}\,dt
=
-\frac1{z^2}
\frac{\xi'}{\xi}
\left(\frac12+\omega-iz\right).
}
\]

The parameter satisfies the exact composition law

\[
\boxed{
\Psi_{\omega+\eta}(t)
=
e^{-\eta t}\Psi_\omega(t)
+
2\eta\int_0^t e^{-\eta u}\Psi_\omega(u)\,du
+
\eta^2\int_0^t(t-u)e^{-\eta u}\Psi_\omega(u)\,du.
}
\]

Thus the shift is a genuine semigroup-like transform, not a heuristic
deformation.

## 3. Positivity propagates only outward

For \(\eta>0\), every coefficient/kernel in the preceding transform is
nonnegative.

Hence

\[
\Psi_\omega\ge0
\quad\Longrightarrow\quad
\Psi_{\omega+\eta}\ge0
\]

on any interval where the first inequality holds.

This is the correct monotone direction:

\[
\boxed{
\text{smaller shift}
\to
\text{larger shift}.
}
\]

The route needed by IRT would start at a safe large shift and push toward
smaller \(\omega\). The same transform does not preserve sign in that direction.

Indeed, replacing \(\eta\) by \(-\eta\) gives a negative coefficient on the
first integral term and exponentially growing pointwise weight.

In Laplace variables, if \(F_\omega(p)\) is the transform of
\(\Psi_\omega\), the outward operator satisfies

\[
F_{\omega+\eta}(p)
=
\frac{(p+\eta)^2}{p^2}F_\omega(p+\eta).
\]

Its inverse therefore shifts the transform toward the analytic boundary and is
not positivity preserving.

Thus:

\[
\boxed{
\text{safe outer positivity}
\not\Rightarrow
\text{inner positivity by the shift law}.
}
\]

## 4. The propagated sign is a global zero-free invariant

Suzuki's Theorem 11.1 states:

\[
\boxed{
\xi(s)\ne0
\ \text{for}\ 
\Re s>\frac12+\omega
}
\]

if and only if there exists \(t_0>0\) such that

\[
\Psi_\omega(t)\ge0
\qquad (t\ge t_0).
\]

So the sign invariant transported by the \(\omega\)-flow is not a weaker
packet observable. It is exactly a global half-plane zero-free condition.

Likewise the 2012 innerness statement is threshold-global:

\[
\Theta_\omega\ \text{inner for every }\omega>\omega_0
\Longleftrightarrow
\xi\ \text{zero-free to the right of }1/2+\omega_0.
\]

This is too coarse for the canonical NEXTJET packet interface.

## 5. Explicit zero-side decomposition

The shifted logarithmic derivative satisfies

\[
\Im\!\left[
i\frac{\xi'}{\xi}(s+\omega)
\right]
=
\sum_\rho
\frac{\Re(s+\omega)-\Re\rho}
     {|s+\omega-\rho|^2}.
\]

This formula makes the parameter-flow obstruction transparent.

Let an off-critical zero have same-height reflected pair

\[
\rho_\pm
=
\frac12\pm\delta+i\gamma,
\qquad
\delta>0.
\]

At the critical-line ordinate \(t\), their combined contribution is

\[
C_{\delta,\gamma}(\omega,t)
=
\frac{\omega-\delta}
     {(\omega-\delta)^2+(t-\gamma)^2}
+
\frac{\omega+\delta}
     {(\omega+\delta)^2+(t-\gamma)^2}.
\]

Algebra gives

\[
\boxed{
C_{\delta,\gamma}(\omega,t)
=
\frac{
2\omega\left(
\omega^2+(t-\gamma)^2-\delta^2
\right)}
{
\left((\omega-\delta)^2+(t-\gamma)^2\right)
\left((\omega+\delta)^2+(t-\gamma)^2\right)
}.
}
\]

Therefore when \(0<\omega<\delta\),

\[
C_{\delta,\gamma}(\omega,t)<0
\]

on the interval

\[
|t-\gamma|<\sqrt{\delta^2-\omega^2}.
\]

At \(t=\gamma\),

\[
C_{\delta,\gamma}(\omega,\gamma)
=
\frac{2\omega}{\omega^2-\delta^2}
\to-\infty
\qquad
(\omega\uparrow\delta).
\]

So an off-critical reflected pair creates an exact localized negative well as
the horizontal shift approaches the pair.

This is a real local signature, not merely global innerness language.

## 6. Why the negative well does not yet close NEXTJET

The divergence in Section 5 comes from approaching the selected pole itself.

Write locally

\[
\frac{\xi'}{\xi}(s)
=
\frac{m_\rho}{s-\rho}
+
R_\rho(s),
\]

where \(R_\rho\) is regular at \(\rho\).

Canonical SOURCE-II does not permit the selected principal part to count as
new complement information. It explicitly removes selected poles before
forming the collision-safe scalar response.

After subtracting the selected term and taking the threshold limit,

\[
\lim_{s\to\rho}
\left(
\frac{\xi'}{\xi}(s)-\frac{m_\rho}{s-\rho}
\right)
=
R_\rho(\rho).
\]

But \(R_\rho(\rho)\) is precisely the pole-removed cofactor logarithmic
derivative species already identified in NJDG-1/2 and represented canonically
by the analytic outside field \(A_{F,\Omega}\), up to the fixed completion
terms and whatever other authorized local poles have also been removed.

Thus:

\[
\boxed{
\text{shift-threshold singularity}
-
\text{selected pole}
=
\text{existing outside-field finite part}.
}
\]

No new independent packet datum remains.

## 7. Higher shift derivatives also fold back

Differentiating the selected-pole-subtracted logarithmic derivative in
\(\omega\) generates higher powers

\[
(s-\rho)^{-2},
\quad
(s-\rho)^{-3},
\quad\ldots
\]

and the corresponding derivatives of the regular field.

These are exactly higher-resolvent / higher-jet species already covered by the
SOURCE-II arbitrary-order tower and the NJDG finite-jet no-bypass analysis.

Therefore the parameter direction does not evade NJDG by creating an
independent infinite family at one fixed packet unless one imports a genuinely
global/infinite transform theorem beyond these local derivatives.

## 8. Compensation debt reappears explicitly

Before selected-pole subtraction, one adverse off-critical term may be
compensated by the rest of the zero divisor in the total sum

\[
\sum_\rho
\frac{\Re(s+\omega)-\Re\rho}
     {|s+\omega-\rho|^2}.
\]

After subtraction, the remaining compensation field is the same
pole-removed outside field already present in the canonical negative branch.

Thus the shift-family problem is another representation of the existing debt:

\[
\boxed{
\text{selected adverse channel}
\quad\text{versus}\quad
\text{complementary field}.
}
\]

The Suzuki flow does not supply the missing every-packet floor on that
complementary field.

## 9. Relation to the canonical-system route

This explains why the 2012 and 2023 pictures agree.

- Full innerness/positivity at shift \(\omega\) is equivalent to a global
  zero-free half-plane.
- Positivity propagates from smaller \(\omega\) to larger \(\omega\), exactly
  the easy direction.
- Crossing inward through an off-critical horizontal displacement creates a
  local adverse pole signature.
- Removing the selected pole leaves the same uncontrolled analytic residue as
  SOURCE-II.

So the parameter flow does not create an intermediate invariant between
canonical positivity and the packet compensation theorem.

## 10. Additional deformation-family screen

Suzuki's 2013 two-parameter deformations of the Riemann xi-function provide
another continuous deformation architecture with functional/difference
relations and Hermite--Biehler motivation.

However the advertised useful zero-free condition for a fixed deformation
parameter is again sufficient for RH rather than a known packet-local
mixed-divisor transfer.

No source located in this pass supplies a monotone deformation quantity that:

1. is unconditional in the false-RH regime;
2. survives selected-pole renormalization;
3. controls the complement field packetwise;
4. maps to the frozen RENJET/KPH quantity.

Thus that family does not alter the current determination.

## 11. IRT-0C1 matrix

| Test | Suzuki shift result | IRT disposition |
|---|---|---|
| exact parameter flow | yes | PASS |
| positivity-preserving direction | increasing \(\omega\) only | WRONG DIRECTION |
| safe unconditional inner regime | \(\omega\ge1/2\) | GLOBAL |
| published explicit Hamiltonian regime | \(\omega>1\) | TECHNICAL SUBREGIME |
| inward propagation | not positivity preserving | FAIL |
| local off-critical signature | explicit negative reflected-pair well | YES |
| survives selected-pole removal as new object | no | FAIL |
| post-renormalization residue | existing \(A_{F,\Omega}\)/higher jets | CANONICAL ALREADY |
| packetwise complement floor | none | OPEN |
| NEXTJET/KPH closure | none | NO |

## 12. Determination

IRT-0C1 closes the Suzuki shift parameter flow as a direct bypass.

It adds two useful exact facts to the program:

\[
\boxed{
\text{positivity has an exact outward semigroup law}
}
\]

and

\[
\boxed{
\text{off-critical reflected pairs create explicit inward shift wells}.
}
\]

But the first runs in the wrong direction for a safe-to-critical proof, and the
second loses its new content under the selected-pole renormalization required
by the canonical packet architecture.

The surviving residue is again the same object:

\[
\boxed{
A_{F,\Omega}
\text{ / complement-field control}.
}
\]

## 13. Cursor

The canonical-system/de Branges family has now been screened through both
static realization and shift flow.

The next distinct foreign architecture is the systems-theoretic realization
class rather than another positivity deformation:

\[
\boxed{
\texttt{IRT-0D / SYSTEMS-REALIZATION + LOEWNER EXACTNESS SCREEN}
}
\]

Primary question:

> Can an infinite-dimensional or structured systems realization recover the
> frozen entire/exponential RENJET response exactly from a data species that is
> lawfully available in the packet, rather than from complete global divisor
> knowledge?

No canonical theorem status changes.
