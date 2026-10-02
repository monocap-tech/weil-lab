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


## Positive canonical-system barrier

The **positive canonical-system barrier** is the following structural fact.

A classical two-dimensional canonical system with positive semidefinite
Hamiltonian has a Herglotz--Nevanlinna Weyl coefficient, and its finite-stage
endpoint entire function is Hermite--Biehler. Consequently the corresponding
real spectral components have real/interlacing zero sets.

For IRT, a direct identification of the completed-zeta critical-line entire
function with such a spectral component therefore imports RH-strength
real-zero information rather than deriving a weaker mixed-divisor estimate.

## Suzuki shift family

The **Suzuki shift family** is

\[
\Theta_\omega(z)
=
\frac{\xi(1/2-\omega-iz)}
     {\xi(1/2+\omega-iz)},
\qquad \omega>0,
\]

as used by Masatoshi Suzuki in the canonical-system criterion for RH.

The family supplies an unconditional positive-canonical-system realization in
the known large-shift regime \(\omega>1\). Extending the corresponding positive
Hamiltonian construction through all \(\omega>0\) is RH-criterion strength.

## Parameter-flow residual

The **parameter-flow residual** is the narrower surviving IRT question whether
one can use a regime with an already valid canonical-system realization
(e.g. the large-shift Suzuki regime) and propagate only a packet-local invariant
toward the critical regime, without proving the full positivity/innerness
statement whose continuation would already be equivalent to RH.

A parameter-flow argument counts as new progress only if its propagated
quantity maps explicitly to the frozen RENJET/KPH target and is strictly
weaker than global Hamiltonian positivity.


## Outward shift semigroup

The **outward shift semigroup** is Suzuki's exact transformation

\[
\Psi_{\omega+\eta}(t)
=
e^{-\eta t}\Psi_\omega(t)
+
2\eta\int_0^t e^{-\eta u}\Psi_\omega(u)\,du
+
\eta^2\int_0^t (t-u)e^{-\eta u}\Psi_\omega(u)\,du,
\]

for real \(\omega,\eta\).

When \(\eta>0\), every coefficient/kernel in this formula is nonnegative.
Therefore nonnegativity of \(\Psi_\omega\) on an interval propagates to the
larger shift \(\omega+\eta\).

This propagation is **outward**, away from the critical line.

## Inward sign-loss

**Inward sign-loss** is the failure of the preceding transform to preserve
positivity when run toward smaller \(\omega\).

Substituting a negative shift changes the sign of the first integral coefficient
while introducing exponential growth in the pointwise factor. Thus positivity
at a safe outer shift does not propagate inward by the same theorem.

In Laplace variables, the outward operator has multiplier

\[
F_\omega(p+\eta)\longmapsto
\frac{(p+\eta)^2}{p^2}F_\omega(p+\eta),
\]

so its inverse is not positivity-preserving.

## Zero-free shift threshold

The **zero-free shift threshold** is the horizontal parameter detected by
Suzuki's shifted screw function:

\[
\xi(s)\ne0\ \text{for }\Re s>\frac12+\omega
\]

if and only if \(\Psi_\omega(t)\) is eventually nonnegative.

This is a global half-plane threshold. It does not identify which packet or
height is responsible for failure below the threshold.

## Parameter-flow compensation debt

The **parameter-flow compensation debt** is the fact that the imaginary part of
the shifted logarithmic derivative decomposes as a sum over all zeros,

\[
\Im\!\left[i\frac{\xi'}{\xi}(s+\omega)\right]
=
\sum_\rho
\frac{\Re(s+\omega)-\Re\rho}{|s+\omega-\rho|^2}.
\]

An off-critical zero can contribute with the adverse sign when the shift crosses
its horizontal displacement, but the total remains a sum over the entire
divisor. Turning that one adverse term into a packetwise lower bound therefore
requires control of the complementary field.

This is the shift-family version of the existing NEXTJET/KPH compensation
problem, not an automatic bypass.


## Reflected-pair shift well

Let an off-critical zero in critical-line coordinates have horizontal
displacement \(\delta>0\) and ordinate \(\gamma\), so the same-height reflected
pair lies at \(1/2\pm\delta+i\gamma\).

For the shifted Herglotz/logarithmic-derivative kernel evaluated at ordinate
\(t\), the pair contributes

\[
C_{\delta,\gamma}(\omega,t)
=
\frac{\omega-\delta}
     {(\omega-\delta)^2+(t-\gamma)^2}
+
\frac{\omega+\delta}
     {(\omega+\delta)^2+(t-\gamma)^2}.
\]

Algebraically,

\[
C_{\delta,\gamma}(\omega,t)
=
\frac{
2\omega\bigl(\omega^2+(t-\gamma)^2-\delta^2\bigr)}
{
\bigl((\omega-\delta)^2+(t-\gamma)^2\bigr)
\bigl((\omega+\delta)^2+(t-\gamma)^2\bigr)
}.
\]

Hence for \(0<\omega<\delta\) it is negative on

\[
|t-\gamma|<\sqrt{\delta^2-\omega^2}.
\]

At \(t=\gamma\) it diverges negatively as \(\omega\uparrow\delta\).

This local well is the horizontal-shift manifestation of approaching the
selected pole. It is not yet a canonical packet lower bound.

## Threshold finite-part collapse

**Threshold finite-part collapse** is the fact that subtracting the selected
pole from the shifted logarithmic derivative and then taking
\(\omega\to\delta\) leaves the regular Laurent coefficient at that zero.

That coefficient is the pole-removed cofactor logarithmic derivative, hence the
same analytic outside-field species already represented canonically by
\(A_{F,\Omega}\).

Higher \(\omega\)-derivatives after selected-pole subtraction produce higher
resolvent/jet data of the same type already covered by SOURCE-II/NJDG.

Therefore the divergent reflected-pair shift well does not survive canonical
selected-pole renormalization as a new independent theorem object.


## RENJET semigroup realization

For the first exponential-mode near kernel

\[
K_t(w)=\frac{e^{tw}-1-tw}{w^2},
\qquad K_t(0)=\frac{t^2}{2},
\]

the **RENJET semigroup realization** is the exact identity

\[
K_t(w)=\int_0^t (t-r)e^{rw}\,dr.
\]

Thus \(K_t(-s)\) is the Laplace transform of the triangular finite-impulse
kernel \((t-r)\mathbf 1_{[0,t]}(r)\).

For a finite near divisor
\(\Omega=\{w_1,\ldots,w_n\}\) with multiplicity/weight vector \(b\), define

\[
A_\Omega=\operatorname{diag}(w_1,\ldots,w_n),
\qquad
c^\ast=(1,\ldots,1).
\]

Then

\[
E_\Omega(r)=c^\ast e^{rA_\Omega}b
\]

and the mode-weighted near response is

\[
Q_t(\Omega)
=
c^\ast K_t(A_\Omega)b
=
\int_0^t(t-r)c^\ast e^{rA_\Omega}b\,dr.
\]

This is an exact finite-dimensional semigroup realization for each fixed finite
near block.

## Resolvent row

A **resolvent row** for the near realization is

\[
H_\Omega(\delta)
=
c^\ast(\delta I-A_\Omega)^{-1}b
=
\sum_{\mu\in\Omega}\frac{m_\mu}{\delta-w_\mu}.
\]

Higher critical curvature rows correspond to higher resolvent powers/derivatives.

This terminology records the exact systems interpretation of the NJDG
critical-value/curvature data.

## Loewner exactness route

The **Loewner exactness route** is the conditional reconstruction:

\[
\text{sufficient well-conditioned samples of }H_\Omega
\Longrightarrow
\text{finite rational realization of }H_\Omega
\Longrightarrow
A_\Omega\text{-realization}
\Longrightarrow
Q_t(\Omega).
\]

For a rational transfer function of McMillan degree \(n\), a sufficiently rich
Loewner data set can recover a minimal degree-\(n\) interpolant exactly.

IRT may count this route only if the required sample locations and values are
available under the canonical selected-only order and with projective
conditioning.

## Realization-rank debt

The **realization-rank debt** is the need for a number of independent,
well-conditioned resolvent observations commensurate with the McMillan
degree/rank of the finite near transfer function.

If the near block size can grow or its nodes collide, no fixed finite number of
critical rows supplies a uniform exact reconstruction theorem.

## Structure-baked interpolation

**Structure-baked interpolation** is structured realization in which the
analytic basis functions \(h_k(s)\), such as delay factors \(e^{-\tau s}\), are
prescribed in advance and only the finite coefficient matrices are identified.

Such a realization may represent a transcendental transfer function exactly,
but it does not derive the prescribed exponential structure from finite
unstructured data.

For IRT, inserting the already known RENJET exponential kernel as a prescribed
basis function is representational, not a mixed-divisor theorem.

## Resolvent-to-semigroup gap

The **resolvent-to-semigroup gap** is the distinction between finitely many
point samples

\[
c^\ast(\lambda_j I-A)^{-1}b
\]

and control of

\[
c^\ast e^{tA}b
\]

or of a matrix function such as \(c^\ast K_t(A)b\).

Classical semigroup generation/stability theorems bridge resolvent information
to semigroup information only from continuum/half-plane or contour-scale
resolvent hypotheses, not from a fixed finite collection of scalar samples.

This is the systems-theoretic analogue of the NJDG finite-row obstruction.


## Dunford-residue collapse

The **Dunford-residue collapse** is the exact identification, for a finite
diagonal near-divisor realization,

\[
Q_f(\Omega)
=
c^\ast f(A_\Omega)b
=
\frac{1}{2\pi i}
\oint_\Gamma
f(z)\,
c^\ast(zI-A_\Omega)^{-1}b\,dz
=
\sum_{\mu\in\Omega}m_\mu f(w_\mu).
\]

For \(f=K_t\), this is the first RENJET near response.

Because the resolvent scalar is a sum of simple pole terms, the
Riesz--Dunford functional-calculus contour is exactly the ordinary residue
formula for the original divisor.

Therefore the continuum systems representation is not a new weighted identity
relative to NJDG-7.

## Regular-remainder bound

A **regular-remainder bound** is a local estimate obtained after all nearby zero
poles have been explicitly extracted from the zeta logarithmic derivative.

Classically, on fixed-width regions at height \(T\), one has a representation
of the form

\[
-\frac{\zeta'}{\zeta}(s)
=
-\sum_{\rho\ {\rm nearby}}\frac1{s-\rho}
+
\frac1{s-1}
+
O(\log T),
\]

with \(O(\log T)\) nearby zeros in a fixed disk and corresponding local
\(L^1\) control of the logarithmic derivative.

Such a bound controls the pole-removed analytic remainder. It does not bound
the selected weighted residue functional independently of the extracted pole
sum.

## Contour compensation debt

The **contour compensation debt** is the failure of a contour norm estimate on
the full logarithmic derivative to separate the target near-divisor residues
from the complementary field.

If a contour encloses the target near poles, the target weighted sum is exactly
the residue contribution to the contour integral. Bounding the integral via
the full logarithmic derivative therefore requires a bound whose strength or
sign information already controls those pole contributions.

Deforming the contour to a region where the logarithmic derivative is easier
to estimate crosses other zeros and adds their residues. This reproduces the
original selected-versus-complement accounting rather than bypassing it.


## Reciprocal Prony sequence

For a fixed exponential selector \(\psi\), the SOURCE-II higher-resolvent
near statistic

\[
S_r^\Omega(\psi)
=
\sum_{\mu\in\Omega}
m_\mu\frac{\psi(\mu)}{(\mu-c)^{r+1}}
\]

is a **reciprocal Prony sequence**. With

\[
y_\mu=(\mu-c)^{-1},
\qquad
a_\mu=m_\mu\psi(\mu)(\mu-c)^{-1},
\]

one has

\[
S_r^\Omega(\psi)=\sum_{\mu\in\Omega}a_\mu y_\mu^r.
\]

Thus, if the \(S_r^\Omega\) were independently known through sufficiently many
orders, classical Prony/annihilating-filter machinery would apply.

## Prony observability debt

The **Prony observability debt** is the fact that SOURCE-II does not expose
\(S_r^\Omega\) as an independent data stream.

The canonical higher jet has the joint finite-part form

\[
\mathfrak J_r
=
S_r(x,v)\psi^{(r+1)}(c)
+
\frac{M_r}{r!}(\psi B_F)^{(r)}(c)
+
M_r S_r^\Omega(\psi).
\]

The \(B_F\) term contains the same unselected divisor whose explicit
higher-resolvent contribution appears in \(S_r^\Omega\); the two pieces form a
collision-safe finite part.

Recovering the Prony sequence by subtraction therefore requires independent
knowledge of the pole-removed/complement field. That is the existing NEXTJET
debt, not free measurement data.

## Prony rank debt

The **Prony rank debt** is the requirement that exact algebraic recovery of an
\(n\)-node exponential sum needs a number of independent exact moments
commensurate with \(n\) (classically \(2n\) scalar moments in the generic
Prony system).

SOURCE-II supplies arbitrary **fixed** finite jet order for any preassigned
projective accuracy. It does not supply a uniform fixed bound on the number of
unselected nodes in every admissible mesoscopic block, nor a growing-order
theorem with constants uniform in the required reconstruction rank.

## Confluent stability debt

The **confluent stability debt** distinguishes collision-safe uniqueness from
stable inversion.

Confluent Prony systems can encode exact collisions/multiplicities, and
separation-free noiseless reconstruction theorems exist for finite sparse
models. But near-collisions make the inverse Prony/Vandermonde map badly
conditioned. Quantitative super-resolution error bounds deteriorate with the
cluster size and inverse separation.

Since the SOURCE-II tower is an asymptotic finite-order normal form with a
nonzero truncation/far-tail remainder, noiseless uniqueness alone is
insufficient for a projective packet theorem.

## Truncated-moment nullspace

The **truncated-moment nullspace** is the algebraic nonuniqueness remaining
when only finitely many moments of an unbounded-rank signed/complex atomic
measure are known.

If \(f\) is not in the finite span of the measured moment kernels, one can
choose a finite signed atomic configuration annihilating all measured moments
while retaining a nonzero \(f\)-functional.

Therefore finite moment data cannot determine the entire RENJET kernel
uniformly over packets of unbounded realization rank without additional
sparsity, positivity, separation, or structural constraints.

## Positive-measure mismatch

The **positive-measure mismatch** records that some separation-free
super-resolution theorems exploit positivity of a measure on a real compact
domain.

After the reciprocal transformation relevant to the false-RH divisor, the
nodes may be complex and the effective amplitudes
\(m_\mu\psi(\mu)(\mu-c)^{-1}\) are generally complex. Those positivity-based
convex recovery theorems therefore do not transfer directly.


## Independent rigidity source

An **independent rigidity source** is information constraining the unknown
complement/divisor that is fixed or valid before the complement-dependent
response being bounded is observed.

Examples in foreign theories include:

- Herglotz positivity and self-adjointness;
- a fixed finite negative index;
- a canonical-system Hamiltonian law;
- a prescribed finite realization rank plus enough external samples;
- a known sparse model plus an independent moment stream.

A representation theorem is not an independent rigidity source if it is built
from the same unknown function/divisor it is later used to constrain.

## Complement-oblivious observability law

A **complement-oblivious observability law** is a quantitative theorem of the
form

\[
\mathcal D(F)\ \Longrightarrow\
\|\mathcal O_F x\|
\ge
L^{-C}\|x\|
\]

or an equivalent signed/discrepancy statement, where:

1. \(\mathcal D(F)\) is selected/public data available before the unselected
   complement response is read;
2. \(\mathcal O_F\) is fixed from that data and canonical source rules;
3. the bound holds for every admitted actual complement;
4. its condition number is projective;
5. no coefficient of \(\mathcal O_F\) is chosen after inspecting the complement.

This is the abstract foreign-theory feature missing from the current
NEXTJET/KPH stack.

## Stable mixed-divisor observability

A **stable mixed-divisor observability theorem** is a complement-oblivious
observability law whose measurements come from a genuinely different divisor
or realization channel and whose output controls the original-divisor
weighted response.

Schematically,

\[
\boxed{
\text{independent second channel}
+
\text{stable observability}
\Longrightarrow
\text{original-divisor weighted packet control}.
}
\]

The second channel must remain informative after the canonical selected-pole
renormalizations and must not reduce to the same joint finite-part tower.

## Representation--rigidity dichotomy

The **representation--rigidity dichotomy** is the IRT-0 synthesis:

- if an architecture is weak enough to represent arbitrary false-RH local
  geometry, its free holomorphic/rank/complement parameters retain the missing
  \(A_{F,\Omega}\)-type information;
- if it constrains those parameters strongly enough to determine the divisor,
  its standard global form usually imports positivity, finite exceptional
  budget, complete data, or conditioning assumptions at least as strong as the
  desired packet theorem.

Progress therefore requires a zeta-specific intermediate rigidity law rather
than another representation.

## Upstream theorem criterion

An **upstream theorem** is a theorem whose statement can be verified or invoked
before the SOURCE-II selected-only multiplier is frozen against the actual
complement.

Because SOURCE-II-8 makes oblivious smallness of the frozen total jet tower
projectively equivalent to the local KPH-floor failure-sequence exclusion, a
purportedly weaker theorem stated only as post-freeze tower smallness is not a
new intermediate gate.

An IRT theorem counts as a genuinely different input only if it constrains the
actual divisor upstream -- for example through an independent mixed-divisor
frame, discrepancy law, or local orientation theorem -- and only afterwards
implies the canonical packet exclusion.

## Observable-orientation theorem

An **observable-orientation theorem** is the weakest abstract theorem shape
currently surviving IRT-0:

For every admitted dangerous selected packet, an independently specified
measurement family from a second channel produces a quantity whose phase,
sign, or distance from the soft direction has a projective lower bound,
uniformly over the actual complement.

It need not reconstruct the complement. It must only prevent the exact
compensating alignment responsible for KPH/NEXTJET failure.

This theorem shape is strictly about information orientation, not another
coordinate representation of the existing explicit formula.
