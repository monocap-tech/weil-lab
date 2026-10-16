# RPB-60 — Log-order interior analyticity certification

**Date:** 2026-09-29  
**Branch:** research/reflected-packet-bridge  
**Status:** **CERTIFICATION FAIL / RPB-43 ANALYTIC-ELLIPTIC SHORTCUT IS NOT VALID FOR THE FULL FINITE-DELAY OPERATOR / PRIME TRANSLATIONS ARE OFF-DIAGONAL FOURIER-INTEGRAL OPERATORS, NOT ANALYTIC PSEUDODIFFERENTIAL LOWER-ORDER TERMS / INTERIOR ANALYTICITY FOR ARBITRARY FRIEDRICHS MODES IS WITHDRAWN PENDING A DELAY-PROPAGATION THEOREM / RPB-57/58 FULL-FRIEDRICHS CANDIDATE REMAINS UNPROMOTABLE**  
**Dependencies:** RPB-31, RPB-36, RPB-37, RPB-43, RPB-57 through RPB-59; RPB-EXT-A1.  
**Promotion status:** **BLOCKED / ADDITIVE CORRECTION**.

## 0. Objective

RPB-59 isolated the first promotion blocker:

~~~math
\mathcal P_ch\in C^\omega_{\rm loc}
\stackrel{?}{\Longrightarrow}
h\in C^\omega_{\rm loc}
~~~

for the actual compact-window translation-invariant Weil operator

~~~math
\mathcal P_c
=
\mathcal A_\infty
-
\sum_{\log n<2c}
\frac{\Lambda(n)}{\sqrt n}
\left(
\tau_{\log n}
+
\tau_{-\log n}
\right).
~~~

RPB-43 had argued that the full scalar Fourier multiplier is analytic and
noncharacteristic at high frequency, and then invoked ordinary analytic
pseudodifferential elliptic regularity.

RPB-60 audits that operator-class step.

It fails.

The finite translations are not pseudodifferential operators with diagonal
canonical relation.  They are off-diagonal translation/Fourier-integral
operators and can transport analytic singularities between separated points.

---

## 1. The archimedean part is local microlocally

The archimedean multiplier is

~~~math
m_\infty(\xi)
=
\Re\psi\!\left(
\frac14+\frac{i\xi}{2}
\right)
-
\log\pi
~~~

with

~~~math
m_\infty(\xi)
=
\log|\xi|
+
O(1)
~~~

at high frequency.

After a harmless low-frequency cutoff, its derivatives have the expected
decaying high-frequency behavior inherited from the digamma asymptotic.

Thus the archimedean logarithmic operator belongs to the ordinary diagonal
pseudodifferential side of the problem.

RPB-EXT-A1 is relevant to this component.

---

## 2. A prime translation is not a pseudodifferential operator

For one delay \(\ell>0\),

~~~math
(\tau_\ell h)(x)
=
h(x-\ell).
~~~

Its distribution kernel is

~~~math
\boxed{
K_\ell(x,y)
=
\delta(x-y-\ell).
}
~~~

This kernel is singular on the shifted diagonal

~~~math
x-y=\ell,
~~~

not on the ordinary diagonal \(x=y\).

An ordinary pseudodifferential operator is pseudolocal: its Schwartz kernel is
smooth away from the diagonal.

Therefore

~~~math
\boxed{
\tau_\ell
\text{ is not an ordinary pseudodifferential operator.}
}
~~~

It is a translation Fourier-integral operator with off-diagonal canonical
relation.

---

## 3. The Fourier-multiplier notation hides the off-diagonal relation

On the Fourier side,

~~~math
\widehat{\tau_\ell h}(\xi)
=
e^{-i\ell\xi}\widehat h(\xi).
~~~

It is tempting to regard

~~~math
e^{-i\ell\xi}
~~~

as an order-zero pseudodifferential symbol.

But for \(k\ge1\),

~~~math
\partial_\xi^k
e^{-i\ell\xi}
=
(-i\ell)^k
e^{-i\ell\xi},
~~~

so

~~~math
\left|
\partial_\xi^k e^{-i\ell\xi}
\right|
=
\ell^k.
~~~

There is no high-frequency derivative decay of the form required by the
standard \(S^0_{1,0}\) analytic pseudodifferential calculus.

The Fourier multiplier is globally simple because the operator is exactly a
translation.  Locally, however, its singularity relation is off diagonal.

Thus the scalar multiplier

~~~math
\Psi_c(\xi)
=
m_\infty(\xi)
-
\sum_{\ell_j}
2a_j\cos(\ell_j\xi)
~~~

cannot be inserted into an ordinary diagonal analytic-pseudodifferential
ellipticity theorem merely because

~~~math
|\Psi_c(\xi)|
\gtrsim
\log|\xi|
~~~

at high frequency.

---

## 4. Correct analytic-wavefront relation for a translation

Translation acts on analytic wavefront sets by spatial transport:

~~~math
\boxed{
(x,\xi)\in WF_A(\tau_\ell h)
\iff
(x-\ell,\xi)\in WF_A(h).
}
~~~

Hence the interior equation

~~~math
\mathcal A_\infty h
-
\sum_j a_j
\left(
\tau_{\ell_j}
+
\tau_{-\ell_j}
\right)h
=
g_{\rm an}
~~~

does not give the ordinary local implication

~~~math
(x,\xi)\in WF_A(h)
\Longrightarrow
(x,\xi)\in WF_A(g_{\rm an}).
~~~

Instead it gives a propagation problem in which a singularity at \(x\) may be
balanced by singularities at

~~~math
x\pm\ell_j.
~~~

This is exactly the finite-delay obstruction already encountered structurally
in RPB-36 and RPB-37.

---

## 5. Why logarithmic dominance does not automatically remove transported singularities

At high frequency the archimedean symbol grows like

~~~math
\log|\xi|,
~~~

while the translation coefficients are bounded.

This makes the full Fourier multiplier nonzero for sufficiently large
\(|\xi|\).

But local analytic regularity is not determined only by pointwise
nonvanishing of the **global** Fourier multiplier.

Formally, a high-frequency inverse may be expanded as

~~~math
\frac1{
m_\infty(\xi)-p_c(\xi)
}
=
\frac1{m_\infty(\xi)}
\sum_{k\ge0}
\left(
\frac{p_c(\xi)}{m_\infty(\xi)}
\right)^k,
~~~

where \(p_c\) is the finite trigonometric prime symbol.

Each power \(p_c^k\) expands into finite combinations of translations by
integer combinations of the active prime delays.

The coefficient gains only inverse powers of

~~~math
\log|\xi|.
~~~

Such logarithmic attenuation does not by itself remove analytic wavefront
singularities, which require exponential-type high-frequency control.

Thus the Neumann picture itself exhibits delay-orbit propagation rather than a
local analytic parametrix.

---

## 6. Correction to RPB-43

RPB-43 stated that regrouping the finite prime translations with the
archimedean multiplier into one scalar Fourier symbol makes the full operator
analytic-elliptic and therefore forces

~~~math
h\in C^\omega(-c,c).
~~~

That conclusion is not justified by RPB-EXT-A1.

The correct statement currently available is weaker:

- the archimedean component is analytically pseudolocal/elliptic in the usual
  diagonal sense;
- each prime shift transports singularities by its delay;
- the full equation imposes an analytic-wavefront **delay-orbit relation**.

RPB-43 remains immutable as a historical note.

RPB-60 is the additive correction.

The claim

~~~math
\boxed{
A_ch=0
\Longrightarrow
h\in C^\omega(-c,c)
}
~~~

is withdrawn from the branch unless separately proved by a delay-propagation
argument.

---

## 7. Effect on RPB-57

RPB-57 uses interior analyticity twice.

First, at a nonthreshold exterior point

~~~math
x=c+s,
~~~

the inward prime sample

~~~math
h(c+s-\ell_j)
~~~

was declared holomorphic in \(s\) across \(s=0\).

Without a certified interior analyticity theorem, this term is only known at
the regularity level carried by the actual Friedrichs zero mode near the fixed
interior point.

Therefore the exterior equation no longer isolates

~~~math
\Sigma_+(s;h)
~~~

against a holomorphic remainder.

Second, even if Stieltjes continuation forced \(h\) to vanish on an endpoint
collar, RPB-57 used interior analyticity to propagate collar vanishing to

~~~math
h\equiv0.
~~~

That step is likewise not currently certified.

Hence the branch-local **full nonthreshold Friedrichs exclusion** from RPB-57
must be downgraded to a candidate conditional on an additional delay-analyticity
or unique-continuation theorem.

---

## 8. Effect on RPB-58

RPB-58's threshold Carleman--Stieltjes forcing was called analytic because:

- strict-\(<\) active prime shifts were assumed analytic at fixed interior
  sample points;
- pole terms are analytic;
- the archimedean regular remainder is analytic.

The pole and archimedean pieces remain analytic.

The prime-shift forcing is not promotion-certified without Blocker A.

Therefore RPB-58 inherits Blocker A **in addition** to its independent
Mellin-conormal completeness blocker from RPB-59.

The physical indicial calculation itself remains correct as a local model once
analytic forcing is supplied.

---

## 9. What survives from the RPB-57/58 mechanism

The following statements survive unchanged:

1. the exact endpoint Stieltjes transform is the exterior logarithmic singular
   object;
2. Zhu's strict prime convention and exact kernel split are pinned;
3. the threshold physical indicial family is correctly calculated;
4. a genuine noninteger physical conormal channel is killed by endpoint
   log-enhancement;
5. the final argument is independent of the corrected RPB-33 core-existence
   claim.

What does **not** survive as an unconditional full-Friedrichs theorem is the
claim that the finite-delay forcing is analytic at arbitrary interior sample
points.

---

## 10. Current promotion blocker A is now a delay-propagation problem

The correct first blocker is no longer

~~~text
verify a standard analytic pseudodifferential hypothesis.
~~~

It is:

~~~math
\boxed{
\text{classify analytic/smooth singularity propagation for }
\mathcal A_\infty
-
\sum_j a_j(\tau_{\ell_j}+\tau_{-\ell_j})
\text{ on a compact interval.}
}
~~~

A sufficient theorem could take one of several forms:

- analytic-wavefront delay-orbit exclusion for compactly supported null modes;
- unique continuation from an endpoint collar for the finite-delay
  logarithmic operator;
- a delay-orbit argument showing every possible transported singular chain
  reaches an exterior zero region;
- a stronger actual-zeta relation that prevents cancellation along dense delay
  orbits.

RPB-37 already shows that naive finite triangularization is unavailable once
multiple prime delays generate dense additive orbits.

---

## 11. External literature check

A current 2026 regularity result for the pure logarithmic Laplacian proves
Hölder/Schauder-type interior regularity for Hölder forcing.

That result concerns the pure \(L_\Delta\) equation and does not supply
analytic regularity for the finite-delay Weil operator.

Thus no currently identified external theorem repairs the RPB-43 shortcut.

---

## 12. RPB-60 determination

~~~math
\boxed{
\textbf{RPB-60 — THE STANDARD ANALYTIC-PSEUDODIFFERENTIAL ROUTE DOES NOT CERTIFY INTERIOR ANALYTICITY FOR THE FINITE-DELAY WEIL OPERATOR.}
}
~~~

Exact correction:

~~~text
ARCHIMEDEAN ANALYTIC PSEUDODIFFERENTIAL COMPONENT:
    LAWFUL

FINITE PRIME TRANSLATIONS AS ORDINARY PSEUDODIFFERENTIAL TERMS:
    FALSE

FULL SCALAR-MULTIPLIER ANALYTIC-ELLIPTIC SHORTCUT:
    WITHDRAWN

INTERIOR ANALYTICITY OF ARBITRARY FRIEDRICHS ZERO MODES:
    OPEN

RPB-57 FULL NONTHRESHOLD EXCLUSION:
    CONDITIONAL / UNPROMOTED

RPB-58 FULL THRESHOLD EXCLUSION:
    CONDITIONAL / UNPROMOTED

CANONICAL AZ-FIN-WEIL-NULL-EXTENSION:
    OPEN
~~~

## Next cursor

~~~text
RPB-61 / ANALYTIC-WAVEFRONT DELAY-ORBIT PROPAGATION
~~~

The next pass should work in the correct operator class.

Priority order:

1. derive the analytic-wavefront propagation relation induced by
   \(\mathcal A_\infty\) and the finite translations;
2. determine whether compact support and endpoint collar information forbid an
   infinite singular delay orbit;
3. distinguish rational single-delay cycles from the multi-prime dense-orbit
   case;
4. test whether logarithmic dominance supplies enough attenuation to exclude a
   closed analytic-singularity orbit;
5. stop if a genuine delay-FIO unique-continuation theorem is required.
