# IRT-0D1 — resolvent-to-semigroup continuum-control screen

**Date:** 2026-10-02 (America/Los_Angeles)  
**Repository:** \`monocap-tech/weil-lab\`  
**Branch:** \`research/inverse-realization-transfer\`  
**Parent:** IRT-0D  
**Status:** **COMPLETE / RIESZ--DUNFORD BRIDGE COLLAPSES TO THE ORIGINAL-DIVISOR WEIGHTED CONTOUR / CLASSICAL LOCAL LOG-DERIVATIVE ESTIMATES CONTROL ONLY THE REGULAR REMAINDER AFTER POLE EXTRACTION / CONTOUR DEFORMATION REINTRODUCES COMPLEMENT RESIDUES / NO NEW NEXTJET CLOSURE / NEXT CURSOR IRT-0E MOMENT-PRONY-SUPERRESOLUTION SCREEN**

## 0. Objective

IRT-0D identified the first RENJET near response as a matrix-function /
semigroup observable and left one theorem class not excluded by the finite-row
nonspan:

\[
\text{continuum resolvent control}
\Longrightarrow
\text{semigroup / functional-calculus control}.
\]

IRT-0D1 asks whether this class supplies a genuinely new zeta bridge.

The answer is no for the direct finite-divisor realization.

The exact functional-calculus contour is the same weighted original-divisor
contour already isolated in NJDG-7. Standard unconditional zeta
logarithmic-derivative estimates control the analytic remainder after nearby
poles are extracted, but do not supply a new selected/complement separation.

## 1. Riesz--Dunford formula for the near realization

For the finite near block

\[
A_\Omega=\operatorname{diag}(w_1,\ldots,w_n),
\qquad
b=(m_1,\ldots,m_n)^T,
\qquad
c^\ast=(1,\ldots,1),
\]

the resolvent scalar is

\[
H_\Omega(z)
=
c^\ast(zI-A_\Omega)^{-1}b
=
\sum_{\mu\in\Omega}
\frac{m_\mu}{z-w_\mu}.
\]

For any function \(f\) holomorphic on a neighborhood of the finite spectrum,
Riesz--Dunford functional calculus gives

\[
f(A_\Omega)
=
\frac{1}{2\pi i}
\oint_\Gamma
f(z)(zI-A_\Omega)^{-1}\,dz.
\]

Pairing with \(c^\ast,b\),

\[
\boxed{
c^\ast f(A_\Omega)b
=
\frac{1}{2\pi i}
\oint_\Gamma
f(z)H_\Omega(z)\,dz.
}
\]

But \(H_\Omega\) is a finite sum of simple poles. Therefore the residue theorem
immediately yields

\[
\boxed{
\frac{1}{2\pi i}
\oint_\Gamma
f(z)H_\Omega(z)\,dz
=
\sum_{\mu\in\Omega}m_\mu f(w_\mu).
}
\]

For

\[
f=K_t,
\]

this is exactly

\[
Q_t(\Omega)
=
\sum_{\mu\in\Omega}m_\mu K_t(w_\mu).
\]

Thus the systems-theoretic continuum bridge is not a new theorem object.

It is the residue theorem in realization notation.

## 2. Identification with NJDG-7

NJDG-7 already observed that a weighted contour of

\[
U(z)=\frac{\Xi'}{\Xi}(z)
\]

on the original divisor directly produces the exponential/mode-weighted
original-zero response.

The Dunford formula above does the same thing after restricting to the finite
near divisor.

Hence:

\[
\boxed{
\text{Riesz--Dunford functional calculus}
=
\text{original-divisor weighted contour}
}
\]

for the current diagonal realization.

The systems route therefore folds directly into the already screened NJDG-7
route at the exact stage where the exponential weighting appears.

## 3. Classical local logarithmic-derivative control

Unconditionally, standard local zeta theory gives, on fixed-width regions at
height \(T\), a local formula of the schematic form

\[
-\frac{\zeta'}{\zeta}(s)
=
-\sum_{\rho:\rho=s+O(1)}
\frac1{s-\rho}
+
\frac1{s-1}
+
O(\log T).
\]

The same local theory gives:

- \(O(\log T)\) zeros in a fixed-size disk near height \(T\);
- local \(L^1\) control of \(|\zeta'/\zeta|\) of order \(O(\log T)\) on a
  fixed-size rectangle.

These statements are enough to move classical contours through regions where
the logarithmic derivative is not too large on average.

But their structure is decisive for IRT:

\[
\boxed{
\text{log derivative}
=
\text{explicit nearby pole sum}
+
O(\log T)\text{ analytic remainder}.
}
\]

The \(O(\log T)\) term is a regular-remainder bound after the local poles have
already been extracted.

## 4. Why the local estimate does not bound RENJET independently

The target near response is a weighted functional of the extracted poles:

\[
Q_t(\Omega)
=
\sum_{\mu\in\Omega}m_\mu K_t(w_\mu).
\]

The classical local formula controls what remains after these poles are
removed.

Therefore it does not imply a new estimate of \(Q_t(\Omega)\) unless one adds
an independent theorem controlling the pole configuration or a sign/phase law
that prevents cancellation.

This is exactly the canonical distinction between:

- local divisor data;
- the pole-removed outside field \(A_{F,\Omega}\).

The standard \(O(\log T)\) remainder estimate belongs to the second species.

## 5. Safe contours do not remove the debt

Local \(L^1\) bounds allow the choice of contours or line segments on which
\(\zeta'/\zeta\) is not exceptionally large.

However, if such a contour encloses the target near poles, then

\[
\frac1{2\pi i}\oint K_t(z)\frac{\Xi'}{\Xi}(z)\,dz
\]

contains the target residues by definition.

A size bound on the full contour integral can control the target only if the
bound is already strong enough to dominate or separate those same pole
contributions.

The generic local estimates do not provide that separation.

Thus there is a contour compensation debt:

\[
\boxed{
\text{bound full contour}
\not\Rightarrow
\text{selected/complement separation}.
}
\]

## 6. Contour deformation reproduces the complement ledger

One may try to deform the contour from the dangerous packet toward a region
where the logarithmic derivative is easier to bound.

But every zero crossed during that deformation contributes its residue.

Therefore

\[
\boxed{
\text{contour deformation}
=
\text{target residues}
+
\text{crossed complement residues}
+
\text{new boundary integral}.
}
\]

This is precisely the selected-versus-complement bookkeeping already present
in SOURCE-II and NJDG.

The deformation does not erase the complement; it moves it from a local
analytic field into an explicit crossed-residue list.

## 7. Hille--Yosida / semigroup norm theorems are not the right scalar input

Abstract semigroup theorems such as Hille--Yosida control an operator
semigroup from operator-resolvent estimates on a half-plane/ray.

In the current finite divisor realization, however, the generator
\(A_\Omega\) is already explicitly diagonal and

\[
e^{tA_\Omega}
\]

is known exactly.

The missing object is not existence or norm control of the semigroup as an
operator. It is the scalar observable

\[
c^\ast K_t(A_\Omega)b
\]

with the actual packet weights and selected-only freezing constraints.

A generic operator norm estimate would discard exactly the signed/projective
information needed by the canonical wedge.

Thus importing a Hille--Yosida bound would be weaker than the exact diagonal
formula unless it were supplemented by a new theorem connecting the
observation vectors \(b,c\) to the selected/complement geometry.

No such theorem is supplied by semigroup theory alone.

## 8. Full original-divisor contour is already known to be the right kernel

There is therefore no remaining mystery about how an exponential/mode-weighted
kernel arises from the original divisor.

It arises naturally from a holomorphic functional-calculus / residue contour.

This confirms NJDG-7's conclusion:

\[
\boxed{
\text{the exponential weighting itself is not the missing theorem}.
}
\]

The missing theorem is the coupling/estimate that controls the relevant
weighted original-divisor response from admissible independent information.

## 9. Exact collapse map

The IRT systems sequence is now:

\[
\begin{aligned}
\text{critical rows}
&\leftrightarrow
\text{finite resolvent samples},
\\
\text{finite Loewner}
&\leftrightarrow
\text{rank-scale critical frame},
\\
\text{semigroup observable}
&\leftrightarrow
\text{RENJET exponential response},
\\
\text{Dunford contour}
&\leftrightarrow
\text{NJDG-7 original-divisor weighted contour},
\\
\text{local resolvent remainder bound}
&\leftrightarrow
A_{F,\Omega}\text{ control},
\\
\text{contour deformation}
&\leftrightarrow
\text{explicit complement-residue transfer}.
\end{aligned}
\]

Every branch of the systems formulation therefore maps to an already named
canonical object or an already identified missing condition.

## 10. IRT-0D1 matrix

| Systems input | Zeta interpretation | New? |
|---|---|---|
| Dunford contour | weighted original-divisor residue sum | no; NJDG-7 |
| finite resolvent samples | critical-value/curvature rows | no; NJDG-3--6 |
| half-plane/contour resolvent norm | coarse log-derivative control | insufficient scalar information |
| local pole extraction + bounded remainder | near divisor + \(A_{F,\Omega}\) | no; SOURCE-II |
| contour deformation | move complement into crossed residues | no bypass |
| semigroup norm bound | loses packet signed observable | too coarse |

## 11. Determination

IRT-0D1 closes the direct continuum resolvent-to-semigroup route as a new
mixed-divisor mechanism.

The exact functional-calculus identity is useful conceptually because it shows
that NJDG-7 had already reached the natural systems-theoretic endpoint.

The obstruction is not:

\[
\text{how do we turn resolvents into exponentials?}
\]

That can be done exactly.

The obstruction remains:

\[
\boxed{
\text{how do we control the weighted original-divisor response
packetwise without complement-adaptive information?}
}
\]

Standard unconditional local log-derivative estimates control the regular
outside field after pole extraction; they do not answer that question.

## 12. Cursor

The systems-realization family is now screened through:

1. finite rational/Loewner reconstruction;
2. structured exponential realization;
3. exact semigroup realization;
4. continuum functional calculus / contour control.

The next distinct foreign architecture is the moment/Prony/super-resolution
family:

\[
\boxed{
\texttt{IRT-0E / MOMENT--PRONY--SUPERRESOLUTION SCREEN}
}
\]

Primary question:

> Does sparse exponential/moment reconstruction provide an exact or stable
> packetwise theorem that uses data actually present in SOURCE-II and survives
> collisions without assuming a separation floor equivalent to the missing
> KPH/NEXTJET condition?

No canonical theorem status changes.
