# IRT-0B — generalized Nevanlinna / Pontryagin screen

**Date:** 2026-10-02 (America/Los_Angeles)  
**Repository:** \`monocap-tech/weil-lab\`  
**Branch:** \`research/inverse-realization-transfer\`  
**Parent:** IRT-0A  
**Status:** **COMPLETE PRIMARY SCREEN / GLOBAL FIXED-\(\kappa\) ROUTE TOO RIGID / LOCAL GENERALIZED-NEVANLINNA ROUTE SURVIVES / WINDOWED INDEX IDENTIFIED / NEXT CURSOR IRT-0B1 LOCAL-\(\pi_+\) CLASS-MEMBERSHIP AND DIVISOR-COUPLING SCREEN**

## 0. Question

IRT-0A found that ordinary Herglotz/self-adjoint realization supplies exactly
the missing zero/pole coupling, but only by forcing the relevant spectrum onto
the real axis.

IRT-0B asks whether generalized Nevanlinna functions and Pontryagin-space
realizations weaken that rigidity enough to admit off-axis divisor geometry
without losing the common-realization theorem architecture.

The answer splits sharply:

\[
\boxed{
\text{global fixed }N_\kappa:\ \text{too restrictive},
\qquad
\text{local generalized Nevanlinna}:\ \text{still live}.
}
\]

## 1. Fixed \(N_\kappa\) is a finite-negative-index theory

For a scalar generalized Nevanlinna function \(q\in N_\kappa\), the kernel

\[
K_q(z,w)=\frac{q(z)-\overline{q(w)}}{z-\overline w}
\]

has exactly \(\kappa\) negative squares in the generalized-Nevanlinna sense.

The operator model is a Pontryagin-space realization with finite negative
index \(\kappa\).

This is not merely a qualitative weakening of Herglotz positivity. The index
is a finite budget.

The standard theory gives, in particular:

- at most \(\kappa\) poles in the upper half-plane;
- generalized zeros/poles of nonpositive type encoded by finite rational
  factors;
- factorization of the scalar function into a rational exceptional factor
  and an ordinary \(N_0\) Herglotz component.

A useful scalar form is schematically

\[
q(z)=r^\#(z)\,q_0(z)\,r(z),
\qquad q_0\in N_0,
\]

with the degree of the rational exceptional factor controlled by \(\kappa\).

The Dijksma--Langer--Luger--Shondin factorization shows more locally that
removing a nonreal pole and a nonreal zero of the relevant nonpositive type
lowers the negative index by one.

Thus the nonreal exceptional divisor is not arbitrary data attached to an
otherwise Herglotz function; it consumes negative index.

## 2. Consequence for a zeta-divisor realization

Move to a critical-line coordinate, writing schematically

\[
\xi(t)=\Xi\!\left(\frac12+it\right).
\]

A zero of \(\Xi\) off the critical line becomes a nonreal zero of \(\xi\), hence
a nonreal pole of its logarithmic derivative (up to the final sign/normalization
chosen for a Weyl candidate).

Suppose a global carrier with exactly that pole divisor belonged to one fixed
class \(N_\kappa\) for finite \(\kappa\).

Then the generalized-Nevanlinna theory would allow only finitely many
upper-half-plane nonreal poles, with a count controlled by \(\kappa\).

Therefore a global fixed-\(\kappa\) realization cannot be adopted as a neutral
false-RH framework unless one separately proves that the off-critical divisor
is finite or supplies another branch for the possibility of infinitely many
off-critical zeros.

The false-RH reductio supplies only

\[
\exists\ \rho\ \text{off the critical line},
\]

not

\[
\#\{\rho:\Re\rho\ne1/2\}<\infty.
\]

Hence the global finite-index premise would silently add information not
available from the contradiction hypothesis.

## 3. Stronger determination than IRT-0A

IRT-0A failed because \(N_0\) forces a real spectral axis.

IRT-0B shows that replacing \(N_0\) by one fixed \(N_\kappa\) does not simply
remove that problem.

Instead it changes the forbidden condition from

\[
\text{no nonreal exceptional spectral points}
\]

to

\[
\text{only finitely many, with finite negative-index budget}.
\]

So:

\[
\boxed{
\text{fixed finite Pontryagin index is not a general false-RH ambient class.}
}
\]

This is a structural limitation, not a failed estimate.

## 4. The local generalized-Nevanlinna escape exists in the literature

The screen located a distinct theory of **local generalized Nevanlinna
functions** and self-adjoint relations in Krein spaces that are locally of type
\(\pi_+\).

In that framework, on each admissible subdomain \(\Omega'\) one has a local
decomposition into a generalized-Nevanlinna component plus a locally
holomorphic component. Crucially, the finite negative index of the
generalized-Nevanlinna component may depend on the chosen subdomain.

Thus one need not posit a single global finite \(\kappa\).

Schematically:

\[
\boxed{
\Omega_1\subset\Omega_2\subset\cdots,
\qquad
\kappa(\Omega_j)<\infty
\text{ for each }j,
\qquad
\sup_j\kappa(\Omega_j)\text{ need not be finite}.
}
\]

This is the first realization architecture found by IRT that is formally
compatible with both:

1. finitely many divisor points in each bounded analytic window;
2. no assumed global finite bound on off-critical divisor points.

Relevant theory:

- Behrndt--Jonas, local generalized Nevanlinna functions in boundary
  conditions and locally \(\pi_+\) realizations;
- Behrndt--Luger, analytic characterization of eigenvalues for self-adjoint
  extensions in Krein spaces that locally have Pontryagin-space spectral
  behavior;
- the locally definitizable / local generalized-Nevanlinna framework in the
  same operator-theoretic lineage.

## 5. Why locality matches the packet architecture

The canonical NEXTJET problem is already windowed:

- one selected finite packet;
- one authorized finite near complement block;
- collision-safe removal of local poles;
- one frozen pair of source modes;
- one weighted near/intermediate functional.

Therefore a realization theorem whose finite negative index is required only
on the same physical/spectral window is formally better matched to the
canonical quantifiers than a global \(N_\kappa\) theorem.

This suggests the investigation object

\[
\boxed{
\kappa(\Omega)
=
\text{negative index required on one canonical packet/window}.
}
\]

No such zeta index has been constructed.

The point is only that the foreign theory licenses this *type* of object
without assuming a uniform global finite index.

## 6. What locality does not give for free

The local theory is not an automatic realization theorem for every
real-symmetric meromorphic function.

In particular, local finiteness of zeros/poles does **not** by itself prove:

- that a chosen transform of \(\xi'/\xi\) is a local generalized Nevanlinna
  function;
- that its local Nevanlinna kernel has finitely many negative squares with a
  useful bound;
- that the \(\xi\)- and \(\xi'\)-divisors become two spectra of the same local
  realization;
- that the required zero/pole coupling survives addition of the locally
  holomorphic component;
- that the resulting inverse theorem recovers the frozen exponential RENJET
  functional;
- that the condition number is projectively controlled.

Those are now the actual obligations.

## 7. Common-carrier test

### Global \(N_\kappa\)

**FORMALLY PASS / FALSE-RH COVERAGE FAIL.**

A common Pontryagin realization exists in the foreign theory, but one fixed
finite index cannot cover an uncontrolled global nonreal pole divisor.

### Local generalized Nevanlinna

**ARCHITECTURALLY PASS / ZETA MEMBERSHIP OPEN.**

The literature supplies local Krein/Pontryagin-type realizations. Whether the
actual zeta-derived carrier belongs to the required local class remains
unproved.

## 8. Exact-kernel test

No IRT-0B source yet supplies the frozen RENJET exponential functional directly.

However, unlike the finite critical-row route, a local operator realization
can in principle retain the full local Weyl/Q-function rather than only a
finite rational jet.

Therefore NJDG-6 does not by itself exclude the local realization route.

**Disposition:** NOT CLOSED / EXACT WEIGHTED OUTPUT STILL OPEN.

## 9. Quantifier and conditioning tests

The local framework is promising precisely because its domain can be aligned
with one packet/window.

But no theorem has yet been attached that says:

\[
\text{for every dangerous packet}
\Longrightarrow
\text{a local }\pi_+\text{ realization with controlled }\kappa(\Omega)
\]

or that the associated divisor reconstruction has a packet-independent
projective condition number.

These are separate requirements.

## 10. New central question

The IRT question is now no longer

> Can generalized Nevanlinna theory tolerate nonreal poles?

It can, finitely per finite-index realization.

The sharper question is:

\[
\boxed{
\text{Does a lawful transform of the actual zeta logarithmic derivative
belong locally to the generalized-Nevanlinna / locally-\(\pi_+\) class
on every canonical packet window?}
}
\]

If yes, the next question is whether the local zero/pole spectral coupling is
strong enough to control the frozen RENJET functional.

If no, the Pontryagin route closes for a precise class-membership reason.

## 11. IRT-0B matrix

| Test | Global fixed \(N_\kappa\) | Local generalized-Nevanlinna |
|---|---|---|
| common realization | yes in foreign theory | yes locally in foreign theory |
| nonreal divisor allowed | finitely, index-controlled | finitely on each local subdomain |
| uncontrolled global off-line divisor | incompatible with one fixed finite \(\kappa\) | not ruled out by global count |
| full local object retained | yes | yes |
| zeta class membership | not proved | not proved |
| mixed \(\xi/\xi'\) divisor transfer | not proved | not proved |
| exact RENJET weighted output | not proved | not proved |
| packetwise conditioning | not proved | not proved |
| direct canonical re-entry | no | no |

## 12. Determination

IRT-0B closes the naive global finite-Pontryagin-index route.

It simultaneously identifies a materially different surviving architecture:

\[
\boxed{
\text{LOCAL GENERALIZED-NEVANLINNA}
+
\text{LOCALLY }\pi_+\text{ KREIN REALIZATION}
+
\text{WINDOW-DEPENDENT }\kappa(\Omega).
}
\]

This is not a semantic weakening of the failed global route. It removes the
unlicensed assumption of a uniform finite global exceptional divisor.

## 13. Cursor

\[
\boxed{
\texttt{IRT-0B1 / LOCAL-}\pi_+\texttt{ CLASS-MEMBERSHIP + DIVISOR-COUPLING SCREEN}
}
\]

First tests:

1. choose the correct critical-line-coordinate logarithmic-derivative carrier
   and sign/Möbius normalization;
2. state the local generalized-Nevanlinna kernel condition on a packet window;
3. determine whether known \(\xi\)-function identities imply, contradict, or
   leave open finite negative squares locally;
4. determine what the local realization actually says about zeros of the
   carrier versus its poles;
5. test whether the locally holomorphic summand destroys the two-spectra
   rigidity needed for RENJET.

No canonical theorem status changes.
