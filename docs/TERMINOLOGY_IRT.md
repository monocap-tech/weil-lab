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

