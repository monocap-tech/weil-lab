# RPB-59 — Full null-extension discharge promotion audit

**Date:** 2026-09-29  
**Branch:** research/reflected-packet-bridge  
**Status:** **PROMOTION BLOCKED / EXTERNAL KERNEL AND THRESHOLD-CONVENTION PINS PASS / RPB-33 DEPENDENCY REMOVABLE / TWO LOAD-BEARING INTERNAL CERTIFICATION GAPS REMAIN: LOG-ORDER INTERIOR ANALYTICITY AND LOCAL MELLIN-CONORMAL COMPLETENESS / STABLE AZ-FIN-WEIL-NULL-EXTENSION REMAINS OPEN**  
**Dependencies:** RPB-43, RPB-46, RPB-47, RPB-49, RPB-57, RPB-58; docs/IMPORTED_SOURCE_PINS.md; WD-T38/H1-P3.1.  
**Promotion status:** **BLOCKED**.

## 0. Objective

RPB-57/58 produced the branch-local all-support statement

~~~math
0\ne h\in\ker A_c
\Longrightarrow
\widetilde h
\text{ cannot satisfy the correct strict enlarged null equation.}
~~~

RPB-59 audits whether that statement is ready to replace the canonical open
interface AZ-FIN-WEIL-NULL-EXTENSION in the stable Horizon-1 package.

The answer is **not yet**.

The geometric/external source side is substantially clean, but two internal
regularity/completeness transitions are still stronger than the currently
pinned theorems.

---

## 1. Audit item: compact-window prime convention — PASS

Zhu's fixed-window symbol is

~~~math
\Psi_L(t)
=
\Re\psi\!\left(
\frac14+\frac{it}{2}
\right)
-\log\pi
-
\sum_{\log n<2L}
\frac{2\Lambda(n)}{\sqrt n}
\cos(t\log n).
~~~

Thus the endpoint convention is exactly

~~~math
\boxed{
\log n<2c.
}
~~~

At an equality threshold

~~~math
2c=\log n_0,
~~~

the \(n_0\)-term is absent at the endpoint and appears for every strict right
enlargement.

This is the convention required by the RPB-57/58 threshold split.

**Disposition:** PASS.

---

## 2. Audit item: exact archimedean kernel split — PASS

Zhu's Gauss/digamma representation gives

~~~math
\Re\psi\!\left(
\frac14+\frac{it}{2}
\right)
=
-\gamma
+
\int_0^\infty
\frac{2}{
1-e^{-2x}
}
\left[
e^{-2x}
-
e^{-x/2}\cos(tx)
\right]dx.
~~~

The off-diagonal physical kernel factor is therefore

~~~math
q(x)
=
\frac{
2e^{-x/2}
}{
1-e^{-2x}
}.
~~~

Near \(x=0\),

~~~math
\boxed{
q(x)
=
\frac1x
+
q_{\rm an}(x),
}
~~~

with \(q_{\rm an}\) analytic.

This is exactly the split used in RPB-57 to isolate the endpoint Stieltjes
transform from a holomorphic exterior remainder.

**Disposition:** PASS.

---

## 3. Audit item: Stieltjes jump — PASS

RPB-EXT-A4 pins the Sokhotskii--Plemelj jump principle for

~~~math
\Sigma(z)
=
\int_0^\delta
\frac{f(r)}{z+r}\,dr,
\qquad
f\in L^2(0,\delta).
~~~

If \(\Sigma\) extends holomorphically through an open subinterval of the cut,
the upper/lower boundary values coincide there and the density vanishes almost
everywhere on the corresponding source interval.

This is the support-removal step in RPB-57.

**Disposition:** PASS.

---

## 4. Audit item: dependence on corrected RPB-33 — PASS AFTER RETYPING

RPB-51 withdrew the historical inference

~~~math
0\in\sigma(A_c)
\Longrightarrow
\ker_{L^2}G_c\ne0.
~~~

The final RPB-57/58 argument no longer requires that inference.

RPB-57 works directly with

~~~math
h\in\ker A_c
~~~

and its physical endpoint Stieltjes transform.

RPB-58 likewise classifies the **physical** endpoint density

~~~math
f(s)=h(c-s)
~~~

and does not use \(u=Dh\) or ordinary screw-core membership.

Thus the final candidate theorem is logically independent of the corrected
RPB-33 core-existence claim.

The only inherited use of RPB-43 is its analytic-ellipticity mechanism, which
is audited separately below.

**Disposition:** PASS AFTER DEPENDENCY RETYPING.

---

## 5. Audit item: physical versus screw-source exponents — PASS

RPB-58 does not import the old source exponent and then shift it.

It rederives the Carleman indicial equation directly for

~~~math
f(s)=h(c-s).
~~~

The first \(L^2\)-admissible **physical** channels are

~~~math
\beta
=
\frac12\pm i\tau_0
~~~

in even parity and

~~~math
\beta
=
\frac32\pm i\tau_0
~~~

in odd parity.

The earlier RPB-46 source-to-physical \(+1\) shift is therefore not being
silently reused.

**Disposition:** PASS.

---

## 6. Audit item: Carleman Mellin multiplier — PASS, BUT LIMITED

RPB-EXT-A5 pins the classical Mellin diagonalization

~~~math
\mathcal C
\longleftrightarrow
\frac{\pi}{\cosh(\pi t)}
~~~

on the \(L^2\) Mellin line.

The cutoff-monomial calculation

~~~math
\mathcal C_\delta(\chi s^\beta)
=
-\frac{\pi}{\sin(\pi\beta)}
s^\beta
+
\text{analytic}
~~~

is also an elementary continuation calculation and correctly yields the
indicial family

~~~math
\mathfrak m_\varepsilon(\beta)
=
-\frac{\pi}{2\sin(\pi\beta)}
+
\varepsilon a_0.
~~~

This source pin is enough to identify candidate channels.

It is **not**, by itself, a theorem that every arbitrary
\(L^2\) solution of the inhomogeneous truncated equation has a complete
polyhomogeneous/Mellin expansion consisting only of those channels plus an
analytic Taylor germ.

That stronger step is audited in Section 8.

**Disposition:** PASS FOR CHANNEL IDENTIFICATION ONLY.

---

## 7. Promotion blocker A: logarithmic-order analytic interior regularity

RPB-57 needs:

~~~math
h\in\ker A_c
\Longrightarrow
h\in C^\omega(-c,c),
~~~

because Stieltjes continuation first gives collar vanishing and the proof then
uses interior analyticity to conclude

~~~math
h\equiv0.
~~~

RPB-EXT-A1 pins a standard analytic-wavefront elliptic regularity theorem and
RPB-43 observes that the compact-window scalar symbol is real analytic and

~~~math
\Psi_c(\xi)
=
\log|\xi|+O_c(1).
~~~

However the stable source pin does not yet contain a direct theorem or
self-contained parametrix proof showing that this **logarithmic-order**
Fourier multiplier satisfies the precise analytic pseudodifferential
hypotheses required for the full analytic-hypoelliptic conclusion.

The issue is not ordinary smooth regularity.

The promotion-level statement needed is specifically:

~~~math
\boxed{
\mathcal P_ch\in C^\omega_{\rm loc}
\Longrightarrow
h\in C^\omega_{\rm loc}.
}
~~~

Until this specialization is independently certified, the RPB-57 step

~~~math
\text{endpoint collar vanishing}
\Longrightarrow
h\equiv0
~~~

is not promotion-ready.

**Disposition:** BLOCKER.

---

## 8. Promotion blocker B: local Mellin-conormal completeness at threshold

RPB-58 proves that the truncated Carleman equation has candidate noninteger
indicial roots and defines residues at those roots.

The load-bearing next step is stronger:

~~~math
\mathfrak B_c(h)=0
\Longrightarrow
\text{the endpoint germ is analytic modulo integer Taylor powers}.
~~~

The present source pin RPB-EXT-A5 does not establish that implication for an
arbitrary \(L^2\) solution of the **inhomogeneous truncated**
Carleman--Stieltjes equation.

In particular, the current corpus has not yet ruled out, by a pinned theorem
or complete internal proof:

- flat nonanalytic endpoint germs;
- more general Mellin-continuation remainders not represented by discrete
  indicial residues;
- a residual solution class whose Mellin transform has no candidate
  noninteger poles but which is not analytic at \(s=0\).

Therefore the implication

~~~math
\boxed{
h\ne0
\text{ and threshold-persistent}
\Longrightarrow
\mathfrak B_c(h)\ne0
}
~~~

is not yet promotion-certified.

The later log-enhancement implication

~~~math
\mathfrak B_c(h)\ne0
\Longrightarrow
\text{endpoint contradiction}
~~~

is structurally sound once a genuine conormal channel is present.

The gap is the **completeness of the channel decomposition**, not the
log-enhancement calculation.

**Disposition:** BLOCKER.

---

## 9. Audit item: endpoint log-enhancement — PASS CONDITIONALLY ON A CHANNEL

RPB-EXT-A7 pins the Chen--Weth integral representation for \(L_\Delta\).

RPB-49 directly derives

~~~math
s^\beta
\Longrightarrow
2s^\beta\log(1/s)
~~~

for every noninteger conormal endpoint term under the full logarithmic
Laplacian.

Since the actual Weil archimedean multiplier has principal symbol
\(\log|\xi|\), the coefficient is halved.

At an equality threshold the endpoint strict-\(<\) prime convention excludes
the only prime shift capable of sampling the opposite endpoint.

All remaining endpoint prime and pole contributions are analytic at the same
noninteger exponent.

Thus, **if** an admissible physical conormal amplitude is present, its
extinction by the endpoint null equation is promotion-ready.

**Disposition:** PASS CONDITIONAL ON BLOCKER B BEING RESOLVED.

---

## 10. Source-pin delta

The existing RPB source-pin ledger already contains:

- RPB-EXT-A1 — analytic elliptic regularity;
- RPB-EXT-A4 — Sokhotskii--Plemelj;
- RPB-EXT-A5 — Carleman Mellin diagonalization;
- RPB-EXT-A7 — logarithmic-Laplacian edge kernel.

RPB-59 adds one exact external pin needed by RPB-57:

~~~text
RPB-EXT-A8 — Zhu v2 equations (3) and (9):
strict prime support convention and exact Gauss/digamma kernel.
~~~

No source is falsely assigned to Blocker B.

A Mellin-conormal completeness theorem must be located and checked, or the
needed expansion must be proved internally.

---

## 11. Canonical disposition

Because Blockers A and B are both load-bearing, RPB-59 does **not** modify:

- docs/THEOREM_LEDGER.md;
- docs/PROOF_STATUS.md;
- docs/RH_INTERFACE_APPENDIX.md;
- docs/NEUTRAL_DEFECT_MORPHOLOGY.md;
- the public Horizon-1 status of AZ-FIN-WEIL-NULL-EXTENSION.

The stable interface therefore remains

~~~text
OPEN
~~~

despite the strong branch-local RPB-57/58 candidate proof.

This is deliberate custody, not a mathematical reversal of the candidate
mechanism.

---

## 12. RPB-59 determination

~~~math
\boxed{
\textbf{RPB-59 — FULL NULL-EXTENSION PROMOTION IS BLOCKED BY TWO CERTIFICATION GAPS, NOT BY THE EXTERIOR/THRESHOLD GEOMETRY.}
}
~~~

Audit matrix:

~~~text
ZHU STRICT PRIME CONVENTION:              PASS
ZHU EXACT ARCHIMEDEAN KERNEL:             PASS
STIELTJES JUMP:                           PASS
RPB-33 INDEPENDENCE:                      PASS AFTER RETYPING
PHYSICAL THRESHOLD EXPONENTS:             PASS
CARLEMAN CHANNEL IDENTIFICATION:          PASS
LOG-ORDER INTERIOR ANALYTICITY:           BLOCKED
MELLIN-CONORMAL COMPLETENESS:              BLOCKED
ENDPOINT LOG-ENHANCEMENT GIVEN CHANNEL:    PASS
CANONICAL PROMOTION:                       NO
~~~

## Next cursor

~~~text
RPB-60 / LOG-ORDER INTERIOR ANALYTICITY CERTIFICATION
~~~

The next pass should isolate the first promotion blocker.

It should prove or source-pin, for the actual compact-window scalar multiplier,

~~~math
\mathcal P_ch\in C^\omega_{\rm loc}
\Longrightarrow
h\in C^\omega_{\rm loc},
~~~

with hypotheses broad enough for arbitrary Friedrichs zero modes.

Do not use the historical RPB-33 screw-core bridge.

If that certification succeeds, the subsequent pass should address the
remaining threshold Mellin-conormal completeness blocker.
