# RPB-67 — WD-T40 Lean certification preflight

**Date:** 2026-09-29  
**Branch:** research/reflected-packet-bridge  
**Status:** **PREFLIGHT COMPLETE / FAITHFUL FORMALIZATION IS PLAUSIBLE IN MATHLIB V4.34 BUT BLOCKED AT THE CURRENT PROJECT ABSTRACTION / WD-T38 LEAN CARRIER IS ABSTRACT AND DOES NOT YET EXPOSE COMPACT SUPPORT, L2 FOURIER DATA, TEMPERED-DISTRIBUTION RESIDUALS, OR THE ACTUAL WEIL MULTIPLIER / WD-T40 MOVES TO LEAN-BLOCKED WITH AN EXACT FOUR-LAYER FORMAL DEPENDENCY STACK**  
**Dependencies:** WD-T38 Lean interface; WD-T34/35 Lean arithmetic layer; mathlib v4.34 Fourier/L2/Gaussian/distribution infrastructure.  
**Formal target class if completed:** **LEAN-CERTIFIED-FROM-IMPORTED-PREMISE**, unless EXT-4 and EXT-5 are themselves reconstructed.

## 0. Objective

RPB-66 left WD-T40 mathematically promoted but formally unattempted.

RPB-67 asks a narrower question:

> Can the Gaussian support-gap null-extension exclusion be formalized faithfully
> at the present abstraction level without replacing it by a weaker surrogate?

The answer is:

~~~text
IN PRINCIPLE WITH CURRENT MATHLIB:
    YES

AT THE PRESENT WEILDEFECT LEAN ABSTRACTION:
    NO

DIRECT CERTIFICATION THIS PASS:
    BLOCKED
~~~

The blocker is not a lack of Fourier analysis in Lean.

It is the missing project-specific bridge from the abstract WD-T38 neutral
interface to the concrete real-line Fourier/distribution carrier used by
WD-T40.

---

## 1. What the current WD-T38 Lean theorem actually contains

The current neutral formalization defines

~~~lean
structure NeutralNullExtensionInterface
    (c : ℝ)
    (H EndpointObs RightObs : Type*)
    ...
~~~

with fields including:

~~~lean
kExt : H
kExt_ne : kExt ≠ 0
endpointOperator : H →L[ℂ] H
rightLimitOperator : H →L[ℂ] H
endpointRestriction : H →L[ℂ] EndpointObs
rightRestriction : H →L[ℂ] RightObs
~~~

and the persistence goal

~~~lean
rightRestriction (rightLimitOperator kExt) = 0.
~~~

This correctly certifies the abstract P3-U7 reduction.

But the type H is generic.

The structure contains no formal data for:

- H = L2(R);
- a representative h : R -> C;
- support containment
  \[
  \operatorname{supp}h\subseteq[-c,c];
  \]
- zero extension as an actual real-line function;
- the whole-line residual as a function or tempered distribution;
- vanishing of that residual on (-a,a);
- a Fourier transform of h;
- the exact scalar Weil multiplier \(\Psi_a\).

Therefore WD-T40 cannot currently even be stated faithfully as a theorem
about NeutralNullExtensionInterface alone.

This is Formal Blocker 1.

---

## 2. Existing project arithmetic is not yet an operator realization

WD-T34 formalizes:

- finite active prime-power support;
- finite physical translation shifts;
- the threshold set.

WD-T35 formalizes a scalar logarithmic form comparison using abstract functions

~~~lean
symbol density : ℝ → ℝ
~~~

and hypotheses such as

~~~lean
a * logarithmicFourierWeight t ≤ symbol t + shift.
~~~

This is sufficient for the Horizon-1 logarithmic-order theorem.

It is not yet a definition of the actual whole-line Fourier multiplier

~~~math
h
\mapsto
\mathcal F^{-1}
\left(
\Psi_a\widehat h
\right)
~~~

on \(L^2(\mathbb R)\) or on tempered distributions.

Thus the current arithmetic layer cannot supply the Fourier-side quadratic
identity used by WD-T40 without a new carrier/operator bridge.

This is part of Formal Blocker 1 rather than a defect in WD-T34/35.

---

## 3. Mathlib v4.34 already supplies the base Fourier infrastructure

The pinned mathlib version contains:

### L2 Fourier transform

Mathlib.Analysis.Fourier.LpSpace defines

~~~lean
MeasureTheory.Lp.fourierTransformₗᵢ
~~~

as a linear isometry equivalence on \(L^2\).

It also proves the L2 Plancherel identity

~~~lean
MeasureTheory.Lp.norm_fourier_eq.
~~~

### Tempered-distribution compatibility

The same file proves

~~~lean
MeasureTheory.Lp.fourier_toTemperedDistribution_eq.
~~~

Thus L2 functions can be transferred coherently into the tempered-distribution
Fourier framework.

### Exact Gaussian Fourier transform

Mathlib.Analysis.SpecialFunctions.Gaussian.FourierTransform contains the
general complex Gaussian integral and Fourier transform, including

~~~lean
fourierIntegral_gaussian
fourier_gaussian_pi'
~~~

and the finite-dimensional inner-product-space Gaussian formulas.

### Fourier inversion

Mathlib.Analysis.Fourier.Inversion proves Fourier inversion for integrable
functions with integrable Fourier transform, using the same Gaussian
approximate-identity mechanism.

Therefore the WD-T40 proof does **not** require inventing a Fourier theory or
Gaussian integral library from scratch.

---

## 4. Formal Blocker 1 — physical Fourier carrier lift

A faithful Lean theorem needs a concrete refinement of the WD-T38 neutral
carrier.

The minimum new object must expose, without weakening the mathematical
hypotheses:

1. a physical mode on the real line;
2. L2 membership;
3. compact support in [-c,c];
4. compatibility with the abstract WD-T38 kExt;
5. the correct enlarged/right-limit operator as an actual whole-line
   Fourier-multiplier-plus-pole object;
6. the restriction statement which turns strict persistence into
   distributional vanishing on (-a,a).

A possible future structure is schematically:

~~~text
NeutralPhysicalFourierCarrier
~~~

but RPB-67 deliberately does **not** canonize an API before the exact
function/distribution representation is settled.

Until this lift exists, a theorem proved only from an abstract assumption such
as

~~~text
"Gaussian window coercivity holds"
~~~

would merely assume the core of WD-T40 and would not certify the promoted
mathematical theorem.

**Disposition:** BLOCKING.

---

## 5. Formal Blocker 2 — support-gap Gaussian pairing in the distribution carrier

WD-T40 pairs the enlarged residual

~~~math
q=\mathcal W_a^{\rm ext}h
~~~

with the Gaussian-filtered mode.

The residual need not be an \(L^2\) function globally.

The faithful formal object is therefore naturally a tempered distribution or
another distributional carrier.

The missing internal theorem must connect:

- support of h in [-c,c];
- vanishing of q on (-a,a);
- the Gaussian Fourier multiplier
  \[
  \phi_R^\pm(\eta)=e^{-(\eta\mp R)^2/R};
  \]
- the physical modulated-Gaussian kernel;
- the estimate
  \[
  \left|
  \langle q,\phi_R^\pm(D)h\rangle
  \right|
  \le
  C e^{-\kappa R}.
  \]

Mathlib has the Gaussian transform and distribution infrastructure, but this
support-separated pairing estimate is project-specific and is not presently
formalized.

**Disposition:** BLOCKING AFTER Blocker 1.

---

## 6. Formal Blocker 3 — actual symbol coercivity as a multiplier theorem

The eventual formal proof may consume EXT-4 and EXT-5 as explicit imported
premises, exactly as WD-T35 already does.

That is compatible with the target status

~~~text
LEAN-CERTIFIED-FROM-IMPORTED-PREMISE.
~~~

However the current Lean layer only stores abstract scalar comparison
hypotheses.

WD-T40 needs a concrete theorem identifying the enlarged physical operator's
Fourier multiplier with a symbol satisfying, for fixed a,

~~~math
\Psi_a(\eta)
\ge
\log|\eta|-C_a
~~~

at high frequency, including the finite threshold correction.

This bridge should be proved downstream from explicit imported source premises,
not replaced by assuming the final Gaussian coercive estimate.

**Disposition:** BLOCKING.

---

## 7. Formal Blocker 4 — exponential Fourier weight to strip holomorphy

The final internal WD-T40 step is

~~~math
\int
e^{\alpha|\eta|}
|\widehat h(\eta)|^2\,d\eta
<
\infty
\Longrightarrow
h
\text{ has a holomorphic strip representative}.
~~~

Mathlib has the required basic ingredients:

- complex integration;
- differentiation/analyticity under suitable integral hypotheses;
- Fourier inversion;
- analytic continuation/identity theorems.

No packaged Paley--Wiener theorem implementing exactly this L2
exponential-weight statement was identified in the pinned corpus.

Thus the likely faithful route is a project-local theorem:

1. exponential L2 weight gives L1 integrability of
   \[
   e^{iz\eta}\widehat h(\eta)
   \]
   for \(|\Im z|<\alpha/2\) by Cauchy--Schwarz;
2. define the strip representative by the inverse Fourier integral;
3. prove holomorphy by dominated differentiation/local domination;
4. identify its real boundary values with the original L2 mode using
   Fourier inversion / L2-distribution compatibility;
5. compact support gives vanishing on a real open interval;
6. analytic continuation gives the zero function.

This is a substantial but self-contained analytic formalization task.

**Disposition:** BLOCKING AFTER Blockers 1--3.

---

## 8. What may be imported versus what must remain internal

A faithful WD-T40 formal certificate may legitimately leave the following as
explicit imported premises:

- EXT-4 compact-window explicit formula / strict prime support convention;
- EXT-5 digamma asymptotic.

That would yield the formal status

~~~text
LEAN-CERTIFIED-FROM-IMPORTED-PREMISE.
~~~

The following may **not** be turned into imported or opaque premises merely to
obtain a certificate, because they are the internal mathematical content of
WD-T40:

- support-gap Gaussian pairing;
- Gaussian-window logarithmic coercivity deduction;
- exponential Fourier decay;
- strip-holomorphy deduction;
- compact-support contradiction.

Doing so would certify only a surrogate implication, not WD-T40.

---

## 9. Preflight verdict

Audit matrix:

~~~text
MATHLIB L2 FOURIER / PLANCHEREL:
    AVAILABLE

MATHLIB TEMPERED-DISTRIBUTION FOURIER BRIDGE:
    AVAILABLE

MATHLIB GAUSSIAN FOURIER FORMULAS:
    AVAILABLE

MATHLIB BASIC COMPLEX ANALYTICITY / IDENTITY THEOREM:
    AVAILABLE

PROJECT WD-T38 PHYSICAL REAL-LINE CARRIER:
    MISSING

PROJECT ACTUAL WEIL FOURIER-MULTIPLIER REALIZATION:
    MISSING

PROJECT SUPPORT-GAP GAUSSIAN PAIRING:
    MISSING

PROJECT EXPONENTIAL-FOURIER -> STRIP-HOLOMORPHY THEOREM:
    MISSING

FAITHFUL DIRECT WD-T40 CERTIFICATE THIS PASS:
    NO
~~~

Therefore:

~~~math
\boxed{
\textbf{WD-T40: LEAN-BLOCKED AT THE CURRENT ABSTRACTION LEVEL.}
}
~~~

This is an exact formalization blocker, not a mathematical objection to
WD-T40.

---

## 10. Required formalization order

The correct order is:

~~~text
F-1  Physical Fourier carrier lift
     abstract WD-T38 mode -> concrete real-line L2/distribution carrier

F-2  Actual compact-window Weil multiplier realization
     including threshold-corrected finite prime symbol

F-3  Gaussian support-gap pairing theorem

F-4  Gaussian-window logarithmic coercivity -> exponential Fourier weight

F-5  Exponential Fourier weight -> strip holomorphy -> compact-support zero

F-6  Assemble WD-T40 from WD-T38 + EXT-4/EXT-5 premises
~~~

Only after F-1 through F-6 succeed may WD-T40 move to

~~~text
LEAN-CERTIFIED-FROM-IMPORTED-PREMISE.
~~~

---

## 11. RPB-67 determination

~~~math
\boxed{
\textbf{RPB-67 — WD-T40 IS FORMALIZABLE IN PRINCIPLE, BUT THE CURRENT WEILDEFECT LEAN ABSTRACTION IS ONE PHYSICAL FOURIER/DISTRIBUTION LAYER TOO HIGH.}
}
~~~

No Lean theorem claiming WD-T40 is added in this pass.

No mathematical theorem is weakened.

## Next cursor

~~~text
RPB-68 / WD-T40 PHYSICAL FOURIER CARRIER LIFT
~~~

The next pass should attack Formal Blocker 1 only.

Priority order:

1. design the concrete real-line carrier without altering WD-T38's existing
   abstract theorem;
2. choose the exact Lp / representative / tempered-distribution split;
3. encode compact support and strict enlarged residual vanishing;
4. prove an adapter from the new concrete carrier to
   NeutralNullExtensionInterface;
5. stop before Gaussian coercivity unless the carrier layer is complete.
