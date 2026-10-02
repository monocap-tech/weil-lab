# Inverse Realization Transfer

**Branch:** `research/inverse-realization-transfer`  
**Launch date:** 2026-10-02  
**Parent:** `research/nextjet-derivative-geometry`  
**Standing:** EXPERIMENTAL / NEGATIVE-BRANCH INVESTIGATION / NO CANONICAL PROMOTION.

See [IRT terminology](TERMINOLOGY_IRT.md) before using the terms below.

## 1. Why this branch exists

NJDG terminated at

[
oxed{
	exttt{TSTOP-NJDG-PENDING-NEW-MIXED-DIVISOR-WEIGHTED-INPUT}
}
]

after showing that the known finite derivative-critical routes do not exactly
reconstruct the frozen mode-weighted RENJET kernel.

The stop does not prove that derivative-divisor information is useless. It
shows that the attempted transfers remained inside one insufficient data class:

- local values of a logarithmic derivative;
- finitely many derivatives/jets;
- finite rational-resolvent combinations;
- separate explicit formulas for the original and derivative divisors.

IRT asks a different question:

[
oxed{
	ext{Can both divisor species be realized as constrained data of one
ambient analytic/operator object?}
}
]

If yes, the missing transfer might come from realization rigidity rather than
another local zeta identity.

## 2. Exact inherited obstruction

Set

[
U(z)=rac{Xi'(z)}{Xi(z)}.
]

The zeros of (Xi) are poles of (U), while ordinary zeros of (Xi') are
zeros of (U).

The weighted contour on (U) naturally sees the original divisor and produces
the exponential/mode-weighted kernel class used by RENJET. Switching to
(Xi''/Xi') exposes derivative zeros as poles only by changing divisor.

NJDG-6 further shows that any finite family of derivative-critical value and
curvature rows generates a finite rational-resolvent kernel, while the frozen
two-mode RENJET kernel is nonconstant entire/exponential type.

Thus IRT inherits two hard requirements:

1. couple the two divisor species without silently replacing one by the other;
2. escape the finite-rational realization class exactly, not approximately.

## 3. Candidate foreign architectures

The first screen is deliberately outside ordinary zeta-zero technique.

### IRT-A — Weyl/Herglotz inverse spectral architecture

Audit Weyl (m)-functions, Herglotz/Nevanlinna representations, two-spectra
theorems, rank-one perturbations, and spectral-measure reconstruction.

Question:

> Under what hypotheses can poles and zeros of one meromorphic transfer
> function be interpreted as two coupled spectra, and which weighted spectral
> functionals become recoverable?

Load-bearing features to isolate:

- positivity or sign of the imaginary part;
- real-axis pole/zero geometry;
- interlacing;
- normalization at infinity;
- complete versus local spectral data;
- residue positivity;
- uniqueness/reconstruction theorem.

### IRT-B — generalized Nevanlinna / Pontryagin architecture

Audit generalized Nevanlinna classes (N_kappa), negative squares, Pontryagin
space realizations, definitizable operators, and finite-negative-index
spectral reconstruction.

Question:

> Can finite failure of positivity replace ordinary Herglotz positivity in a
> way compatible with a false-RH reductio and still couple zero/pole data?

The branch must not assume that a zeta-derived carrier has finite negative
index. Class membership itself is a theorem obligation.

### IRT-C — canonical-system / de Branges architecture

Audit canonical systems, Hermite-Biehler functions, de Branges spaces, and
their Weyl functions.

Question:

> Is there a realization in which the relevant entire/logarithmic-derivative
> data arise from one canonical system, so zeros/poles or phase derivatives
> inherit a spectral law strong enough for the weighted packet functional?

Any RH-equivalent positivity condition must be identified explicitly and may
not be used inside a false-RH argument.

### IRT-D — rank-one perturbation / Clark-measure architecture

Audit theorems where Möbius transforms of one Herglotz/inner object generate
different spectral measures or interlacing point sets.

Question:

> Can the two divisor species be interpreted as spectra of related rank-one
> perturbations, with a transfer identity for weighted observables?

This track is particularly relevant if a single transfer function can be
normalized into an admissible Schur/Herglotz object.

### IRT-E — systems realization / Loewner architecture

Audit rational interpolation, Loewner realization, descriptor systems,
infinite-dimensional transfer functions, and delay/exponential systems.

Question:

> Can NJDG-6 be reformulated as a minimal-realization obstruction, and what
> exact infinite/growing realization would be required to recover the RENJET
> exponential kernel?

Finite-order approximation or Padé accuracy is not enough. The target is an
exact transfer or a theorem with an error term strong enough for the canonical
packet contradiction.

### IRT-F — moment / Prony / super-resolution architecture

Audit finite-rate-of-innovation reconstruction, exponential sums, moment
problems, collision conditioning, confluent Prony systems, and sparse measure
recovery.

Question:

> Which assumptions permit stable recovery of an exponential population from
> finitely/growingly many rational or moment observations, especially through
> collisions?

This track is useful primarily for conditioning and information-count
obstructions. Sparsity/separation assumptions must be compared against the
actual selected/complement packet geometry rather than silently imported.

## 4. Primary target

IRT does not seek a generic analogy. Its first target is to locate an abstract
theorem schema of the form

[
oxed{
egin{array}{c}
	ext{one realized transfer/Weyl object}\
+ 	ext{zero/pole divisor data}\
+ 	ext{realization rigidity}
end{array}
Longrightarrow
	ext{controlled weighted functional of the pole divisor}
}
]

where the controlling data can be supplied by the derivative divisor or by a
second spectrum naturally coupled to it.

The weighted output must be comparable to the frozen RENJET complement wedge or
to (	exttt{C-ACTUAL-KPH-FLOOR}).

## 5. First theorem-shape tests

Every candidate architecture should be reduced to the following questions.

### T1 — common-carrier test

Are both point sets genuinely spectral/divisor data of one realized object, or
are two unrelated formulas merely being compared?

### T2 — exact-kernel test

Does the theorem recover the exponential/mode-weighted kernel exactly, or only
a finite rational approximation?

### T3 — quantifier test

Is the result packetwise/every-configuration, or only averaged/almost-everywhere?

### T4 — conditioning test

Does the transfer carry an inverse-spacing, inverse-residue, or small-singular
value loss? If yes, is that loss projectively controlled?

### T5 — false-RH compatibility test

Does the theorem assume positivity, real zeros, self-adjointness, or an
equivalent RH-strength property that is unavailable inside the reductio?

### T6 — locality/data-volume test

Does the theorem require complete infinite spectral data? If so, can the
canonical setup lawfully supply it, or does the supposed bridge simply import
more information than NEXTJET has?

## 6. Failure classes

The following outcomes do not count as canonical progress:

- another finite jet identity;
- another rational interpolation of the frozen entire kernel;
- a two-spectra theorem whose hypotheses already force real zeros;
- an operator realization obtained only under RH;
- average spectral reconstruction promoted to every packet;
- approximation without an error theorem at the required projective scale;
- a theorem relating two auxiliary spectra without identifying them with the
  actual (Xi) and (Xi') divisor species;
- class membership asserted by analogy.

## 7. Promotion ladder

### IRT-0 — architecture screen

Locate and classify foreign theorem families by their exact hypotheses and
outputs.

### IRT-1 — abstract transfer candidate

Select at least one theorem architecture whose output type can represent the
frozen RENJET weighted functional.

### IRT-2 — zeta-carrier compatibility

Construct a precise transform of the actual zeta-derived carrier and test all
class-membership/normalization hypotheses.

### IRT-3 — mixed-divisor transfer

Prove or import a theorem that couples the actual divisor species and produces
the required weighted response with lawful quantifiers and conditioning.

### IRT-4 — canonical re-entry

Map the result explicitly into (	exttt{AZ-NEXTJET-LOC}) or
(	exttt{C-ACTUAL-KPH-FLOOR}).

No stage is skipped.

## 8. Initial cursor

[
oxed{
	exttt{IRT-0 / FOREIGN REALIZATION ARCHITECTURE SCREEN}
}
]

First priority order:

1. Weyl/Herglotz two-spectra and rank-one perturbation;
2. generalized Nevanlinna/Pontryagin realization;
3. canonical systems/de Branges;
4. infinite-dimensional systems realization;
5. Prony/moment conditioning.

The purpose of IRT-0 is not to prove RH-facing content. It is to determine
whether the missing theorem type already has a mature abstract analogue and,
if so, exactly which hypothesis supplies the coupling that NJDG lacked.

## 9. Canonical status guard

This branch preserves the NJDG stop. It does not reopen NJDG by renaming it.

[
oxed{
	exttt{AZ-NEXTJET-LOC: OPEN}
}
]

[
oxed{
	exttt{C-ACTUAL-KPH-FLOOR: OPEN}
}
]

[
oxed{
	exttt{NJDG: TSTOP RETAINED}
}
]

No RH claim is made.


## 10. IRT-0A determination — Weyl/Herglotz screen

IRT-0A located the exact foreign architecture sought at launch.

Classical meromorphic Herglotz/Weyl theory couples zeros and poles because one
common self-adjoint realization supplies positivity, real spectral support,
interlacing, normalization, and inverse reconstruction. Rank-one perturbation
and two-spectra theorems show that this can recover the full realized object,
so the NJDG-6 finite-rational obstruction is not universal when complete
realization data are available.

The same mechanism is too strong for direct use in the negative false-RH
branch: a classical scalar Herglotz realization whose pole set is the full
critical-line-coordinate \(\Xi\)-divisor forces that spectral pole set onto the
real axis. That is incompatible with using the realization as an assumption
while analyzing an off-critical zero.

Thus the classical route is:

\[
\boxed{
\text{FORMALLY MATCHED / REALIZATION MECHANISM IDENTIFIED / DIRECT FALSE-RH USE BLOCKED}.
}
\]

See [IRT-0A checkpoint](../notes/IRT_0A_WEYL_HERGLOTZ_20261002.md).

The next question is whether generalized Nevanlinna/Pontryagin realization
retains enough two-divisor rigidity while admitting controlled nonreal or
nonpositive-type spectral data.

## 11. Current cursor

\[
\boxed{
\texttt{IRT-0B / GENERALIZED-NEVANLINNA-PONTRYAGIN SCREEN}
}
\]


## 12. IRT-0B determination — generalized Nevanlinna / Pontryagin screen

IRT-0B separates the generalized-Nevanlinna route into two different regimes.

A single global class \(N_\kappa\) with finite \(\kappa\) is too restrictive as
a general false-RH ambient class: the negative index is a finite budget on
nonpositive-type exceptional structure, and the scalar theory permits only
finitely many nonreal poles in the upper half-plane.

The branch therefore does not assume one global finite Pontryagin index for a
carrier whose pole divisor is intended to include all off-critical zeta zeros.

However, the foreign literature contains a distinct theory of **local
generalized Nevanlinna functions** and self-adjoint Krein-space relations that
are locally of type \(\pi_+\). In that theory the finite negative index may
depend on the selected subdomain.

This yields a surviving architecture aligned with the canonical packet/window
structure:

\[
\boxed{
\Omega\mapsto\kappa(\Omega)<\infty
\quad\text{locally, without a uniform global finite bound.}
}
\]

No zeta-derived carrier has yet been proved to satisfy this local class
condition, and no mixed-divisor RENJET transfer follows from locality alone.

See [IRT-0B checkpoint](../notes/IRT_0B_GENERALIZED_NEVANLINNA_20261002.md).

## 13. Current cursor

\[
\boxed{
\texttt{IRT-0B1 / LOCAL-}\pi_+\texttt{ CLASS-MEMBERSHIP + DIVISOR-COUPLING SCREEN}
}
\]


## 14. IRT-0B1 determination — local class membership is non-rigid

The local generalized-Nevanlinna definition allows

\[
\tau=\tau_0+\tau_{(0)}
\]

with \(\tau_0\) generalized Nevanlinna and \(\tau_{(0)}\) arbitrary holomorphic
on the selected relatively compact window.

For a real-symmetric meromorphic logarithmic derivative with finitely many
poles in that window, a rational function can match all local principal parts;
every real-symmetric rational function belongs to some \(N_\kappa\). The
remainder is holomorphic.

Thus the zeta logarithmic derivative belongs locally to the class for essentially
formal meromorphic reasons. The corresponding local Weyl realization is
representational rather than restrictive.

Moreover, the holomorphic summand is exactly the species of the already
canonical pole-removed outside field \(A_{F,\Omega}\). It can alter the local
zero divisor without changing the captured pole principal parts.

Therefore:

\[
\boxed{
N(\Omega)\text{ membership}
+
\text{local }\pi_+\text{ realization}
\not\Rightarrow
\text{mixed-divisor control}.
}
\]

See [IRT-0B1 checkpoint](../notes/IRT_0B1_LOCAL_PI_PLUS_20261002.md).

The surviving question is whether a stricter realization architecture controls
the holomorphic slack without already imposing RH-strength real-spectrum
positivity.

## 15. Current cursor

\[
\boxed{
\texttt{IRT-0C / CANONICAL-SYSTEM + DE BRANGES RIGIDITY SCREEN}
}
\]


## 16. IRT-0C determination — canonical-system / de Branges rigidity

Classical canonical systems genuinely solve the holomorphic-slack problem:
one positive semidefinite Hamiltonian controls the Weyl coefficient, transfer
matrix, Hermite--Biehler endpoint function, phase, and self-adjoint spectral
zero sets.

The same positivity is too strong for direct use on the false-RH branch.
A direct realization of the critical-line completed-zeta divisor as a
self-adjoint/de Branges spectral component forces the relevant zeros onto the
real spectral axis.

The zeta-specific Suzuki family confirms the boundary. For

\[
\Theta_\omega(z)
=
\frac{\xi(1/2-\omega-iz)}
     {\xi(1/2+\omega-iz)},
\]

an explicit canonical system is known unconditionally in the large-shift
regime \(\omega>1\), while extension of the positive Hamiltonian construction
through all \(\omega>0\) gives an RH criterion.

Therefore the classical positive route is:

\[
\boxed{
\text{RIGID ENOUGH / DIRECT FALSE-RH USE TOO STRONG}.
}
\]

See [IRT-0C checkpoint](../notes/IRT_0C_CANONICAL_DEBRANGES_20261002.md).

A narrower unresolved route remains: propagate only a packet-local invariant
from the large-shift realized regime toward the critical regime, strictly below
the full positivity/innerness statement.

## 17. Current cursor

\[
\boxed{
\texttt{IRT-0C1 / SUZUKI-SHIFT PARAMETER-FLOW AUDIT}
}
\]


## 18. IRT-0C1 determination — Suzuki shift parameter flow

The Suzuki shift family supplies an exact parameter transform for the shifted
screw functions \(\Psi_\omega\). For positive increment \(\eta\), the transform

\[
\Psi_\omega\mapsto\Psi_{\omega+\eta}
\]

has nonnegative kernels and therefore propagates nonnegativity **outward** to
larger shift.

The required safe-to-critical direction is inward. The inverse transform is not
positivity preserving.

Moreover, eventual nonnegativity of \(\Psi_\omega\) is equivalent to the global
zero-free half-plane

\[
\Re s>\frac12+\omega,
\]

so the transported sign is not a packet-local invariant.

An off-critical reflected pair does create an explicit negative shift well when
\(\omega\) crosses its horizontal displacement. However the divergent part is
the selected pole itself. Canonical selected-pole subtraction leaves its regular
finite part, which is exactly the existing pole-removed outside-field species
\(A_{F,\Omega}\). Higher shift derivatives similarly reduce to the already
available higher-resolvent/jet tower.

Thus:

\[
\boxed{
\text{EXACT SHIFT FLOW LOCATED / WRONG POSITIVITY DIRECTION /
THRESHOLD SIGNATURE COLLAPSES TO EXISTING COMPLEMENT FIELD}.
}
\]

See [IRT-0C1 checkpoint](../notes/IRT_0C1_SUZUKI_SHIFT_FLOW_20261002.md).

## 19. Current cursor

\[
\boxed{
\texttt{IRT-0D / SYSTEMS-REALIZATION + LOEWNER EXACTNESS SCREEN}
}
\]


## 20. IRT-0D determination — systems realization / Loewner exactness

The systems-theory screen identifies the first RENJET near kernel as an exact
semigroup observable:

\[
K_t(w)=\int_0^t(t-r)e^{rw}\,dr.
\]

For a fixed finite near block \(\Omega\), the exponential population is
\(c^\ast e^{rA_\Omega}b\), the mode-weighted near response is
\(c^\ast K_t(A_\Omega)b\), and derivative-critical rows are resolvent
observations \(c^\ast(\delta I-A_\Omega)^{-1}b\) and their derivatives.

Thus the canonical deficit has a precise systems interpretation:

\[
\boxed{
\text{resolvent observations}
\longrightarrow
\text{semigroup / matrix-function observable}.
}
\]

Finite Loewner realization can solve this exactly for one finite rational near
transfer only with enough well-conditioned samples commensurate with its
McMillan degree. The canonical derivative-zero branch does not supply such an
every-packet sample frame; this is the existing NJDG realization-rank/
conditioning debt in systems language.

Structured realization can represent exponential/delay dependence exactly
when the analytic basis functions are prescribed in advance, but that bakes the
already known RENJET structure into the model rather than deriving it from
critical rows.

The surviving distinct theorem class uses continuum resolvent control:
Hille--Yosida, inverse-Laplace, Kreiss/Gearhart-type mechanisms control
semigroup behavior from resolvent bounds on a ray, half-plane, contour, or
boundary family rather than from finitely many scalar samples.

See [IRT-0D checkpoint](../notes/IRT_0D_SYSTEMS_LOEWNER_20261002.md).

## 21. Current cursor

\[
\boxed{
\texttt{IRT-0D1 / RESOLVENT-TO-SEMIGROUP CONTINUUM-CONTROL SCREEN}
}
\]


## 22. IRT-0D1 determination — continuum resolvent control collapses to NJDG-7

For the finite near-divisor realization, the Riesz--Dunford formula gives

\[
c^\ast f(A_\Omega)b
=
\frac1{2\pi i}\oint_\Gamma
f(z)c^\ast(zI-A_\Omega)^{-1}b\,dz.
\]

Since the resolvent scalar is a finite pole sum, this is exactly the residue
formula

\[
\sum_{\mu\in\Omega}m_\mu f(w_\mu).
\]

For \(f=K_t\), the continuum systems bridge is therefore the same
original-divisor weighted contour already isolated in NJDG-7.

Classical unconditional local formulas for \(\zeta'/\zeta\) have the form

\[
\text{log derivative}
=
\text{nearby pole sum}
+
O(\log T)\text{ regular remainder}
\]

on fixed-width regions, with corresponding local \(L^1\) control. These
estimates control the pole-removed analytic field after the local divisor has
been extracted; they do not independently control the target weighted residue
functional.

Contour deformation toward easier regions crosses additional zeros and merely
moves the complementary field into explicit residue terms.

Thus:

\[
\boxed{
\text{DUNFORD/CONTINUUM BRIDGE EXACT BUT NOT NEW;}
\quad
\text{COMPLEMENT DEBT RETAINED}.
}
\]

See [IRT-0D1 checkpoint](../notes/IRT_0D1_RESOLVENT_SEMIGROUP_CONTINUUM_20261002.md).

## 23. Current cursor

\[
\boxed{
\texttt{IRT-0E / MOMENT--PRONY--SUPERRESOLUTION SCREEN}
}
\]


## 24. IRT-0E determination — moment / Prony / super-resolution

The higher-resolvent near statistics admit an exact reciprocal-coordinate
Prony form:

\[
S_r^\Omega(\psi)
=
\sum_{\mu\in\Omega}
m_\mu\frac{\psi(\mu)}{(\mu-c)^{r+1}}
=
\sum_{\mu\in\Omega}a_\mu y_\mu^r,
\]

with \(y_\mu=(\mu-c)^{-1}\).

This is a genuine formal identification of the SOURCE-II near tower with a
finite-rate-of-innovation / exponential-moment model.

However, SOURCE-II does not expose \(S_r^\Omega\) as an independent measurement
stream. It appears only inside the joint finite-part jet together with the
\(B_F\)/outside-field derivative. Isolating the Prony moments therefore
requires independent complement-field information.

Even if those moments were supplied by an oracle, exact Prony inversion has a
rank-scale data cost, while stable inversion near collisions has a
Vandermonde/super-resolution conditioning cost. SOURCE-II supplies arbitrary
**fixed** jet order and a finite truncation remainder, not a uniform
rank-adaptive exact moment stream or a packetwise separation/conditioning
floor.

Separation-free noiseless uniqueness therefore does not close the actual
problem, because the project requires quantitative stability under nonzero
truncation/far-tail error.

Thus:

\[
\boxed{
\text{PRONY MODEL MATCHES EXACTLY / OBSERVABILITY + RANK + STABILITY DEBTS REMAIN}.
}
\]

See [IRT-0E checkpoint](../notes/IRT_0E_PRONY_SUPERRESOLUTION_20261002.md).

## 25. Current cursor

\[
\boxed{
\texttt{IRT-0F / CROSS-ARCHITECTURE SYNTHESIS + NEW-THEOREM-TYPE EXTRACTION}
}
\]


## 26. IRT-0F determination — cross-architecture synthesis

IRT-0 has completed the planned foreign-architecture screen.

Across Weyl/Herglotz, generalized Nevanlinna, canonical systems, systems
realization, and Prony/super-resolution, successful transfer always requires:

\[
\boxed{
\text{independent model rigidity}
+
\text{independent observations}
+
\text{stable observability/conditioning}.
}
\]

When those ingredients are weakened enough to admit arbitrary false-RH local
geometry, the missing information reappears as holomorphic slack,
complement-field freedom, realization-rank debt, or unstable inversion.

When they are strengthened enough to determine the divisor globally, the
standard versions import RH-strength real-spectrum positivity, a finite global
exceptional budget, complete data, or equivalent conditioning assumptions.

SOURCE-II-8 adds a decisive project-specific constraint: post-freeze smallness
of the selected-only total jet tower on every dangerous packet is not a weaker
localization lemma. It is projectively equivalent to excluding the local
KPH-floor failure sequence.

Therefore a genuinely different input must act **upstream** of the frozen
tower and provide complement-oblivious orientation information from an
independent channel.

The surviving theorem signature is

\[
\boxed{
\textbf{STABLE MIXED-DIVISOR OBSERVABILITY / ORIENTATION}
}
\]

with a projective condition number and the correct selected-before-complement
quantifier order.

See [IRT-0F checkpoint](../notes/IRT_0F_CROSS_ARCH_SYNTHESIS_20261002.md).

## 27. Current cursor

\[
\boxed{
\texttt{IRT-1A / OBSERVABLE-ORIENTATION THEOREM DESIGN}
}
\]


## 28. IRT-1A determination — observable-orientation theorem design

The dangerous Key-C direction is the right-singular soft cone of

\[
A_F^{\rm KPH}=I+\varepsilon^{-1}C_F.
\]

A full second-channel frame bound is unnecessary.

It is enough to construct an upstream observation operator
\(\mathcal O_F\) satisfying two inequalities on the KPH soft cone:

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
H_F^b\|A_F^{\rm KPH}v\|
+\frac12H_F^{-a}.
}
\]

The elementary sandwich gives

\[
KPH(F)\ge \frac12H_F^{-(a+b)}.
\]

This is the minimal IRT implication contract. Its content lies in proving the
two inequalities from an independent actual-zeta channel, not in the sandwich
itself.

Existing feature/APR channels do not produce a new local Key-C interface:
CF-A17 makes source-free feature/KPH factor-through false, and JOINT-2 shows an
actual-zeta feature/KPH attachment near \(U_*\) is projectively equivalent to
the KPH floor itself.

SOURCE-II post-freeze observables fail the upstream independence contract.

The derivative divisor remains the cleanest independently typed candidate:
the next pass will design a canonical \(\Xi'\)-observation operator and ask only
for transversality to the KPH soft cone, not reconstruction of RENJET.

See [IRT-1A checkpoint](../notes/IRT_1A_OBSERVABLE_ORIENTATION_DESIGN_20261002.md).

## 29. Current cursor

\[
\boxed{
\texttt{IRT-1B / MIXED-DIVISOR SOFT-CONE FRAME DESIGN}
}
\]
