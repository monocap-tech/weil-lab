# RPB-107 — concrete EXT-4 pole attachment and test-duality audit

**Date:** 2026-09-30 (America/Los_Angeles)  
**Branch:** research/reflected-packet-bridge  
**Status:** **AUDIT COMPLETE / NAMED TWO-EXPONENTIAL POLE ALGEBRA ATTACHED / HERMITIAN GAUSSIAN DUAL TEST BUILD-CERTIFIED / CURRENT COMPLEX-BILINEAR WEAK-REALIZATION INTERFACE NOT YET A HERMITIAN ENERGY IDENTITY / FULL EXT-4 POLARIZATION-COMPLEXIFICATION ATTACHMENT STILL OPEN / COERCIVITY NOT STARTED**

## 0. Objective

RPB-106 certified the explicit two-exponential source pole, all Gaussian
cutoff/pairing infrastructure, and a conditional Gaussian-admissibility
constructor.  One load-bearing source boundary remained:

~~~text
hEXT4 : RightLimitWeilWeakRealizationPremise
  c carrier residual hSymbol (neutralWeilSourcePole carrier)
~~~

RPB-107 audits whether the pinned EXT-4 quadratic formula itself supplies that
complex weak realization and whether the existing moving Gaussian test has the
duality required by the Fourier energy step of WD-T40.

The answer separates into two parts.

## 1. Concrete pole algebra: PASS

For

~~~math
M_s(h)=\int_{-c}^{c}h(y)e^{sy}\,dy,
~~~

RPB-106 defined

~~~math
p_h(x)
=
M_{-1/2}(h)e^{x/2}
+
M_{1/2}(h)e^{-x/2}.
~~~

RPB-107 proves:

~~~lean
neutralWeilPoleMoment_eq_integral
neutralWeilPoleMoment_integrable_global
neutralWeilSourcePole_pairing_eq
~~~

and in particular

~~~math
\int_{\mathbb R} h(x)p_h(x)\,dx
=
2 M_{-1/2}(h)M_{1/2}(h).
~~~

This is exactly the two-evaluation pole algebra appearing in Zhu's compact
formula / Lemma 6.1 before parity splitting.  The pole growth and the pole
quadratic factor are therefore no longer separate informal identifications.

This does **not** by itself construct the entire multiplier-plus-pole weak
operator identity.

## 2. Source custody: quadratic identity versus polarized operator identity

The pinned source presents a quadratic Weil form through the autocorrelation
and, for the real-even convention, a frequency expression involving

~~~math
|\widehat f(t)|^2.
~~~

Its general real parity decomposition gives the pole factor

~~~math
2\widehat f(i/2)\widehat f(-i/2).
~~~

The current Lean structure

~~~lean
RightLimitWeilWeakRealizationPremise
~~~

is stronger in a different direction: it asserts a complex-linear
distribution identity against **every compactly supported complex Schwartz
test**.

That statement is a polarized operator realization.  It is not literally the
displayed quadratic identity in the pinned source.

Therefore the remaining EXT-4 attachment is now typed as:

~~~text
derive the polarized weak operator identity from the quadratic compact-window
formula, with the real/complex extension and Fourier normalization explicit.
~~~

The project must not silently promote local integrability or the quadratic
formula into that stronger complex-linear premise.

## 3. Test duality: current Gaussian test is bilinear

The current weak-realization structures use the ordinary complex product

~~~math
\int u(x)q(x)\,dx.
~~~

If both arguments acquire a common phase (i), the pointwise product changes
sign:

~~~lean
complex_bilinear_phase_I
~~~

certifies

~~~math
(iz)(iw)=-zw.
~~~

Thus the unconjugated test cannot, for arbitrary complex carriers, be
identified directly with the Hermitian energy required by

~~~math
\int
\Psi_a(\xi)\phi_R(\xi)|\widehat h(\xi)|^2\,d\xi.
~~~

## 4. Hermitian Gaussian dual test

RPB-107 registers and implements the **Hermitian Gaussian dual test**:

~~~lean
conjugateSchwartz
movingGaussianFilteredModeDualTest
movingGaussianFilteredModeDualTest_apply
~~~

with

~~~math
G_R^{\vee}(x)=\overline{G_R(x)}.
~~~

Conjugation is implemented as a real-linear isometric postcomposition on
Schwartz space, so no new regularity assumption is introduced.

The phase audit

~~~lean
complex_hermitian_phase_I
~~~

certifies

~~~math
\overline{iz}\,(iw)
=
\overline z\,w.
~~~

This is the phase behavior needed for a Hermitian quadratic energy.

## 5. Validation

Validation branch:

~~~text
validation/rpb107-ext4-duality-audit
~~~

Validation PR:

~~~text
#22
~~~

Final successful run:

~~~text
run:  36807944842
job:  110196386366
head: 52c22e7dd49ac50f8ea228b046db5faf5b2362de

target:
lake build WeilDefect.Morphology.NeutralGaussianDualityAudit

result:
PASS (8948 jobs)

unfinished/project-axiom rejection gate:
PASS
~~~

Certified source blob:

~~~text
NeutralGaussianDualityAudit.lean
e9d4fde62ea2bbd8e7c586b134e81e58103b9085
~~~

The first compiler attempt failed only on conjugation namespace and
(I^2=-1) normalization.  Commit
`52c22e7dd49ac50f8ea228b046db5faf5b2362de` repaired those elaboration
details; no hypotheses or theorem statements were weakened.

## 6. Effect on RPB-106

RPB-106 remains valid as a **conditional** Gaussian-admissibility assembly:

~~~text
explicit pole growth: certified
cutoff package: certified
ordinary integral limits: certified
Gaussian weak identity from exact compact weak witness: certified
~~~

But its source-pole specialization still consumes an exact compact weak
realization witness.

RPB-107 now shows that:

~~~text
the pole component of that witness is source-attached,
but the full complex operator witness still requires polarization/
complexification.
~~~

## 7. Effect on WD-T40 formalization

The promoted mathematical WD-T40 argument used Hermitian bracket notation in
the Fourier-energy step.  RPB-107 does not refute that mathematical argument.

It does show that the present Lean F-2/F-4 interface encoded a complex
**bilinear** test pairing, and therefore cannot be used directly as that
Hermitian energy identity for an arbitrary complex carrier.

The formal route must be repaired before logarithmic coercivity begins.

## 8. RPB-107 determination

~~~math
\boxed{
\textbf{RPB-107 — THE TWO-EXPONENTIAL POLE IS NOW ATTACHED AT THE QUADRATIC-ALGEBRA LEVEL, BUT THE PINNED EXT-4 QUADRATIC FORM STILL HAS TO BE POLARIZED/COMPLEXIFIED INTO THE WEAK OPERATOR INTERFACE; THE WD-T40 ENERGY TEST MUST USE THE CONJUGATED GAUSSIAN DUAL TEST.}
}
~~~

## Next cursor

~~~text
RPB-108 / WD-T40 F-4
POLARIZED EXT-4 OPERATOR REALIZATION
+ HERMITIAN GAUSSIAN CUTOFF BRIDGE
~~~

Priority order:

1. derive a source-faithful polarized compact-test identity from the pinned
   quadratic formula;
2. make the real-to-complex extension explicit;
3. expose the multiplier and named two-exponential pole in that polarized
   identity;
4. construct compact cutoffs for the Hermitian Gaussian dual test and pass the
   identity to its limit;
5. only after that identity is certified may logarithmic coercivity begin.

Do not reopen the Gaussian seed, moving-mode Schwartz realization, or the
repaired cutoff convergence proofs.
