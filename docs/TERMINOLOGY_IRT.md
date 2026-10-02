# Terminology — Inverse Realization Transfer

**Date:** 2026-10-02  
**Branch:** `research/inverse-realization-transfer`  
**Status:** additive investigation terminology; no canonical theorem status changed.

This registry is introduced before the first load-bearing use of the corresponding
terms. It is intentionally narrower than the terminology of any external field.

## IRT

**IRT** means **Inverse Realization Transfer**: the investigation of whether the
missing NEXTJET mixed-divisor control can be recast as a realization problem in
which two divisor species are constrained as spectral/realization data of one
analytic object.

IRT is an investigation label only. It is not a theorem or source premise.

## Original divisor

The **original divisor** is the zero divisor of the completed zeta carrier
\(\Xi\). For

\[
U(z)=\frac{\Xi'(z)}{\Xi(z)},
\]

the original divisor appears as the pole divisor of \(U\), with multiplicity
encoded in the corresponding residues.

## Derivative divisor

The **derivative divisor** is the zero divisor of \(\Xi'\) away from common
zeros with \(\Xi\). Such points are zeros of \(U=\Xi'/\Xi\), not poles of
\(U\). They become poles only after changing carrier, for example to
\(\Xi''/\Xi'\).

## Two-divisor realization

A **two-divisor realization** is an ambient analytic/operator structure in which
both the pole divisor and zero divisor of one transfer/Weyl-type function are
constrained by a single realization theorem.

This term does not assert that \(\Xi'/\Xi\) presently has such a realization.

## Mixed-divisor transfer

A **mixed-divisor transfer** is a theorem that converts controlled data attached
to one divisor species into the specific weighted response required from the
other divisor species, with the packet quantifier and conditioning required by
the canonical NEXTJET/KPH interfaces.

Separate explicit formulas for the two divisors are not, by themselves, a
mixed-divisor transfer.

## Realization rigidity

**Realization rigidity** means structural constraints supplied by an ambient
function/operator class beyond meromorphicity alone. Examples in foreign
theories include positivity, Herglotz/Nevanlinna representation, self-adjoint
or Pontryagin-space realization, interlacing, normalization, rank constraints,
and complete spectral data.

Any IRT argument must state exactly which rigidity property is imported or
proved. Formal resemblance is not rigidity.

## Foreign analogue

A **foreign analogue** is a theorem architecture outside the immediate analytic
number-theory lineage whose input/output types resemble the missing transfer.

A foreign analogue is admissible evidence for investigation design, not a
source theorem for zeta until an explicit bridge is proved.

## Herglotz/Nevanlinna route

The **Herglotz/Nevanlinna route** asks whether a transform of the relevant
logarithmic-derivative carrier can be placed in a classical Nevanlinna/Herglotz
class with an integral/spectral representation rigid enough to couple zeros,
poles, and weighted spectral functionals.

No such class membership is assumed.

## Generalized-Nevanlinna/Pontryagin route

The **generalized-Nevanlinna/Pontryagin route** asks whether allowing finite
negative index provides the correct realization category when positivity is too
strong.

No finite-index realization for the zeta carrier is assumed.

## Finite-realization obstruction

The **finite-realization obstruction** is the NJDG-6 fact that finitely many
critical value/curvature rows span finite rational-resolvent kernels, while the
frozen RENJET kernel is nonconstant entire/exponential type.

IRT treats this as a model-class mismatch, not merely a failed interpolation
formula.

## Infinite/growing realization

An **infinite/growing realization** is any exact transfer requiring an
infinite-dimensional state space, a growing family of observations, a continuum
transform, or complete spectral data.

Such a route is admissible only if its conditioning and packet quantifiers are
proved; approximation alone does not close NEXTJET.

## IRT admission test

An external architecture is **IRT-admissible** only if it can plausibly address
all of:

1. one common carrier/realization containing both divisor species;
2. the exact weighted original-divisor functional used by RENJET or an
   equivalent canonical quantity;
3. packetwise rather than merely averaged control;
4. projectively controlled conditioning;
5. compatibility with the false-RH reductio;
6. no hidden replacement of the original divisor by the derivative divisor.

## IRT re-entry criterion

IRT may claim progress toward the canonical branch only after producing at
least one of:

- a proved realization-class membership for a zeta-derived carrier together
  with a theorem yielding the needed mixed-divisor weighted transfer;
- a two-spectra/interlacing-style theorem specialized to the actual carrier and
  the RENJET functional;
- a generalized-Nevanlinna/Pontryagin realization whose finite negative index
  gives the required every-packet control;
- an exact infinite/growing realization with proved conditioning that recovers
  the frozen RENJET kernel.

Anything weaker remains structural reconnaissance.

## Status guard

IRT does **not** alter:

- `AZ-NEXTJET-LOC` — open;
- `C-ACTUAL-KPH-FLOOR` — open;
- `TSTOP-NJDG-PENDING-NEW-MIXED-DIVISOR-WEIGHTED-INPUT` — retained;
- WD-T40 / neutral-branch status;
- RH standing.



## Finite-index global realization

A **finite-index global realization** is a realization of one global carrier in a
fixed generalized Nevanlinna class \(N_\kappa\) for one finite \(\kappa\).

For scalar \(N_\kappa\), the negative index is a finite global budget on
nonpositive-type exceptional structure. IRT must not silently treat such a fixed
\(\kappa\) as compatible with an uncontrolled infinite off-axis divisor.

## Local generalized Nevanlinna realization

A **local generalized Nevanlinna realization** is a realization on a domain
\(\Omega\) whose restriction to each admissible smaller domain can be decomposed
using a generalized Nevanlinna component plus a locally holomorphic component.

The finite negative index of the generalized Nevanlinna component may depend on
the chosen subdomain. This is qualitatively different from membership in one
global fixed class \(N_\kappa\).

## Windowed Pontryagin index

The **windowed Pontryagin index**, written schematically as
\(\kappa(\Omega)\), denotes the finite negative index required by a local
Pontryagin/generalized-Nevanlinna realization on one admissible spectral window.

This is investigation notation only. No function of the zeta carrier has yet
been proved to possess such an index.

## Local \(\pi_+\) route

The **local \(\pi_+\) route** asks whether the zeta-derived carrier can be
realized on each canonical packet/window as a Weyl or \(Q\)-function associated
with a self-adjoint relation that is locally of type \(\pi_+\).

The route is useful only if it yields the actual mixed-divisor weighted
functional with packetwise conditioning. Local realizability by itself is not
canonical progress.


## Holomorphic slack

**Holomorphic slack** is the unconstrained locally holomorphic summand
\(\tau_{(0)}\) in a local generalized-Nevanlinna decomposition

\[
\tau=\tau_0+\tau_{(0)}.
\]

On a bounded packet window for a logarithmic derivative, the rational/generalized-
Nevanlinna part can be chosen to carry the finitely many local principal parts,
while the pole-removed outside field is absorbed into \(\tau_{(0)}\).

Holomorphic slack can move or create zeros without changing the captured pole
principal parts. Therefore local generalized-Nevanlinna membership alone does
not couple the zero and pole divisors strongly enough for IRT.

## Local realization universality

**Local realization universality** is the fact that on bounded windows, a
real-symmetric meromorphic function with locally finite poles can be decomposed
as

\[
\text{real-symmetric rational principal-part carrier}
+
\text{holomorphic remainder},
\]

and every real-symmetric rational function belongs to some generalized
Nevanlinna class \(N_\kappa\).

Consequently membership in the local class \(N(\Omega)\), and the existence of
a corresponding local Weyl/Krein realization, may be representational rather
than restrictive.

IRT must not count such a universal realization as divisor-control progress.

## Rigid realization subclass

A **rigid realization subclass** is a realization class that constrains the
holomorphic slack by additional global or local structure: for example a fixed
Nevanlinna index with normalization, a canonical-system/de Branges law, a
definitizing function of controlled complexity, a phase/interlacing rule, or
another condition that quantitatively couples zeros and poles.

Only such additional rigidity can qualify as a candidate mixed-divisor input.
