# IRT-0B1 — local \(\pi_+\) class-membership and divisor-coupling screen

**Date:** 2026-10-02 (America/Los_Angeles)  
**Repository:** \`monocap-tech/weil-lab\`  
**Branch:** \`research/inverse-realization-transfer\`  
**Parent:** IRT-0B  
**Status:** **COMPLETE / LOCAL CLASS MEMBERSHIP IS ESSENTIALLY AUTOMATIC ON BOUNDED WINDOWS / LOCAL WEYL REALIZATION IS REPRESENTATIONAL NOT RIGID / HOLOMORPHIC SLACK IDENTIFIED WITH THE EXISTING POLE-REMOVED OUTSIDE FIELD / NO NEW MIXED-DIVISOR CONTROL / NEXT CURSOR IRT-0C CANONICAL-SYSTEM / DE BRANGES RIGIDITY SCREEN**

## 0. Question

IRT-0B left one promising possibility:

> perhaps the logarithmic-derivative carrier belongs locally to a generalized
> Nevanlinna class on every canonical packet window, and the associated local
> \(\pi_+\) realization then couples the original and derivative divisors.

The screen gives a two-part answer:

\[
\boxed{
\text{local class membership: essentially automatic on bounded windows;}
}
\]

\[
\boxed{
\text{useful divisor coupling: does not follow.}
}
\]

The reason is the locally holomorphic summand allowed by the definition.

## 1. Correct definition — correction of the launch heuristic

Behrndt--Jonas define a local generalized Nevanlinna function \(\tau\in
N(\Omega)\) by requiring that for every relatively compact admissible subdomain
\(\Omega'\Subset\Omega\),

\[
\boxed{
\tau=\tau_0+\tau_{(0)},
}
\]

where \(\tau_0\) is a generalized Nevanlinna function and
\(\tau_{(0)}\) is holomorphic on \(\Omega'\).

Thus the condition is **not**

\[
\text{“the kernel of }\tau\text{ itself has finitely many negative squares
on the window.”}
\]

The generalized-Nevanlinna condition applies to one summand after an arbitrary
local holomorphic remainder has been removed.

This corrects the stronger heuristic stated at the end of IRT-0B.

## 2. Rational principal-part lemma

Let \(\tau\) be any scalar meromorphic function on a neighborhood of a bounded
admissible domain \(\Omega'\), symmetric with respect to the real axis:

\[
\tau(\overline z)=\overline{\tau(z)}.
\]

Because \(\overline{\Omega'}\) is compact and \(\tau\) is meromorphic, it has
only finitely many poles in \(\Omega'\).

Choose a rational function \(r\) whose principal parts agree with those of
\(\tau\) at every pole in \(\Omega'\), including conjugate pole pairs and real
poles with the symmetry-enforced conjugate Laurent coefficients.

Then:

1. \(r\) is real-symmetric;
2. \(\tau-r\) is holomorphic on \(\Omega'\);
3. every real-symmetric rational function belongs to some generalized
   Nevanlinna class \(N_\kappa\).

Therefore

\[
\boxed{
\tau=r+(\tau-r)
}
\]

is a local generalized-Nevanlinna decomposition on \(\Omega'\).

Since \(\Omega'\) was arbitrary:

\[
\boxed{
\text{real-symmetric meromorphic + locally finite poles}
\Longrightarrow
\text{local generalized-Nevanlinna membership}
}
\]

on the bounded-window domains relevant here.

The implication is local. It does not assert one global fixed \(N_\kappa\)
membership.

## 3. Application to the zeta logarithmic derivative

Use the critical-line coordinate in which the completed zeta carrier is real
entire on the real axis, and let \(U\) denote its logarithmic derivative
(up to the harmless sign/linear normalization chosen for the Weyl convention).

Then \(U\) is meromorphic and real-symmetric. Its poles are the zeros of the
completed zeta carrier.

On every bounded canonical packet window there are finitely many poles.

Hence the principal-part argument gives:

\[
\boxed{
U\in N(\Omega)
}
\]

for each such bounded local domain, without using RH, without bounding the
number of off-critical zeros globally, and without proving any zeta-specific
positivity.

This initially looks positive, but it is actually a warning: the membership is
too inexpensive to carry the missing theorem.

## 4. Identification of the holomorphic slack with SOURCE-II

On a packet window, split the logarithmic derivative into the explicitly
removed local divisor and the pole-removed field:

\[
U(z)
=
\sum_{\rho\in F_{\rm loc}}\frac{m_\rho}{z-\rho}
+
\sum_{\mu\in\Omega_{\rm loc}}\frac{m_\mu}{z-\mu}
+
A_{F,\Omega}(z),
\]

up to the already fixed completion/normalization terms.

The first two sums are rational principal-part data.

The remainder

\[
A_{F,\Omega}
\]

is analytic on the authorized local region.

Therefore the canonical SOURCE-II split is already a local
generalized-Nevanlinna decomposition:

\[
\boxed{
\tau_0
=
\text{finite rational local pole carrier},
\qquad
\tau_{(0)}
=
A_{F,\Omega}
+\text{fixed holomorphic normalization}.
}
\]

This is exactly the object NJDG-2 had already isolated.

Hence local generalized-Nevanlinna theory has not supplied a new estimate on
the outside field. It has repackaged the existing decomposition.

## 5. Why the zero divisor is not rigid under local membership

The pole principal parts do not determine the zeros once an arbitrary
holomorphic summand is allowed.

Fix a rational principal-part carrier \(r\). Let
\(z_1,\ldots,z_m\) be finitely many target points away from its poles, chosen
with conjugate symmetry.

By ordinary polynomial interpolation one can choose a real-symmetric
polynomial \(p\) satisfying

\[
p(z_j)=-r(z_j)
\]

for all target points.

Then

\[
\tau=r+p
\]

has the same poles and principal parts as \(r\), remains in the same local
generalized-Nevanlinna architecture, but has zeros at every \(z_j\).

Thus:

\[
\boxed{
\text{local pole data}
+
N(\Omega)\text{ membership}
\not\Rightarrow
\text{controlled local zero divisor}.
}
\]

This is the decisive divisor-coupling failure.

## 6. Weyl realization does not repair the loss

Behrndt--Jonas show that local generalized Nevanlinna functions admit local
Weyl-function representations associated with self-adjoint relations locally
of type \(\pi_+\).

Since the class-membership argument above applies to essentially any
real-symmetric meromorphic carrier on a bounded window, the corresponding
existence of a local Weyl realization is likewise too universal to be a
zeta-specific rigidity theorem.

The realization faithfully represents the already given function. It does not
add an independent law constraining its holomorphic slack.

Therefore the chain

\[
U
\to
N(\Omega)
\to
\text{local Weyl realization}
\]

is, by itself, a **representation theorem**, not a new inverse theorem.

## 7. Relation to NJDG-2

NJDG-2 concluded that the pair-removed cofactor logarithmic derivative is not a
new object: after local poles are removed it is the canonical analytic outside
field \(A_{F,\Omega}\).

IRT-0B1 now reaches the same boundary from foreign operator theory:

\[
\boxed{
\text{local generalized-Nevanlinna decomposition}
\equiv
\text{rational local divisor}
+
\text{holomorphic outside field}.
}
\]

So the foreign architecture folds back onto the existing SOURCE-II object
rather than crossing it.

This is a genuine closure result for the naive local-\(\pi_+\) route.

## 8. Exact admission tests

### Common-carrier test

**PASS REPRESENTATIONALLY.**

Both poles and zeros belong to the same meromorphic function and a local Weyl
model exists.

### Exact-kernel test

**FAIL AS NEW INPUT.**

The holomorphic summand can retain arbitrary entire/local analytic dependence,
including the exponential-mode information. No exact RENJET weighted
functional is recovered from the pole carrier.

### Quantifier test

**VACUOUSLY LOCAL.**

Membership holds window by window but yields no every-packet estimate.

### Conditioning test

**NO CONTROL.**

The realization theorem does not provide a projective condition number for
recovering zeros or weighted pole functionals from the other divisor.

### False-RH compatibility

**PASS.**

The local class is weak enough not to force RH.

This very weakness is why it supplies no divisor rigidity.

## 9. New structural dichotomy

IRT now exposes a clean tradeoff:

\[
\boxed{
\begin{array}{rcl}
\text{classical }N_0
&:&
\text{strong divisor rigidity, but RH-strength real-spectrum restriction},\\
\text{global finite }N_\kappa
&:&
\text{finite exceptional divisor budget, still too restrictive globally},\\
\text{local }N(\Omega)
&:&
\text{false-RH compatible, but too weak to constrain the zero divisor}.
\end{array}
}
\]

The missing regime would have to sit between the last two:

\[
\boxed{
\text{false-RH compatible}
+
\text{nontrivial control of the holomorphic slack}.
}
\]

## 10. What would make a local realization useful

A surviving realization route must add a **rigid subclass condition** that
controls the holomorphic remainder, for example:

- canonical-system normalization;
- de Branges / Hermite-Biehler phase law;
- a definitizing function of controlled complexity;
- a bounded negative index tied quantitatively to the packet rather than the
  entire global divisor;
- a local sign-type law on the real interval;
- a transfer matrix with determinant/positivity constraints;
- another invariant preventing arbitrary polynomial interpolation of the zero
  divisor.

Merely proving \(U\in N(\Omega)\) is not such a condition.

## 11. Determination

IRT-0B1 closes the plain local generalized-Nevanlinna / local-\(\pi_+\)
membership route as a source of new mixed-divisor information.

The important positive residue is conceptual:

\[
\boxed{
\text{the missing theorem must constrain the analytic outside field,
not merely realize it.}
}
\]

That statement now agrees simultaneously with SOURCE-II, NJDG-2, and the
foreign Weyl/Krein architecture.

## 12. Cursor

\[
\boxed{
\texttt{IRT-0C / CANONICAL-SYSTEM + DE BRANGES RIGIDITY SCREEN}
}
\]

Primary question:

> Is there a canonical-system, Hermite--Biehler, or de Branges-type
> normalization that controls the holomorphic slack while remaining usable
> under false RH, or do its phase/positivity hypotheses again collapse to
> real-zero/RH-strength structure?

No canonical theorem status changes.
