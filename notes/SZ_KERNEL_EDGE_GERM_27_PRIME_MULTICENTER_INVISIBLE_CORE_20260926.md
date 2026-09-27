# SZ-KERNEL-EDGE-GERM-27 — Prime-coupled multicenter Volterra system and invisible core

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Immediate residue:** SZ-KERNEL-EDGE-GERM-26  
**Target tested:** PRIME-COUPLED MULTICENTER COMPATIBILITY  
**Public promotion:** forbidden

## 0. Objective

GERM-26 exhausted the local archimedean rigidity route:

\[
\text{full Suzuki archimedean diagonal}
\not\Rightarrow
\text{local finite-order rigidity}.
\]

The only remaining local mechanism in the movable-center equation is the
finite prime-tent coupling.

This pass writes that coupling in its exact Volterra form and tests whether
simultaneous prime compatibility can recover the source.

The answer is again mixed.

The exact prime field at a movable center is a second-order Volterra transform
of a weighted sum of neighboring **diagonal symmetrizations**.

Thus prime coupling does constrain multiple local source germs at once.

However:

1. superflat prime-tent output does not imply vanishing of the underlying
   source combination;
2. in the entire regime
   \[
   \log2<L<\log4,
   \]
   there is an infinite-dimensional **prime-invisible core**
   \[
   J_c=(L-\log2,\log2)
   \]
   missed identically by every prime tent at every admissible movable center;
3. a true kernel vector cannot live purely in that core, because the remaining
   archimedean endpoint equation is injective there.

Therefore the core is not a free kernel sector; it is a globally reconstructed
sector whose custody is carried only by the archimedean coupling to its
complement.

This proves that prime-coupled multicenter compatibility, by itself, cannot
supply the missing local coercivity.

---

# I. Exact prime tent operator

## 1. One local tent

For a source location

\[
d\in\mathbb R
\]

and zero-extended

\[
f\in L^2(0,L),
\]

define

\[
\boxed{
V_d(\delta;f)
=
\int_{\mathbb R}
(\delta-|s-d|)_+
f(s)\,ds.
}
\]

For

\[
\delta>0,
\]

write

\[
s=d\pm t.
\]

Then

\[
\boxed{
V_d(\delta;f)
=
\int_0^\delta
(\delta-t)
\left[
f(d+t)+f(d-t)
\right]dt.
}
\]

Thus

\[
\boxed{
V_d(\delta;f)
=
\int_0^\delta
(\delta-t)
(\Sigma_df)(t)\,dt,
}
\]

where

\[
\Sigma_df(t)
=
f(d+t)+f(d-t)
\]

is the zero-extended local symmetrization.

This is the exact Volterra form of one prime tent.

---

# II. Full movable-center prime field

## 2. Active delays

Let

\[
\mathscr H_c^\circ
=
\{
\lambda=\log n:
\Lambda(n)\ne0,\;
0<\lambda<L
\},
\]

and

\[
a_\lambda
=
\frac{\Lambda(n)}{\sqrt n}.
\]

At source-coordinate center

\[
h\in(0,L),
\]

GERM-4 gives prime tent centers

\[
h-\lambda,
\qquad
h+\lambda.
\]

Define

\[
\boxed{
\mathscr P_h(\delta)f
=
\sum_{\lambda\in\mathscr H_c^\circ}
a_\lambda
\left[
V_{h-\lambda}(\delta;f)
+
V_{h+\lambda}(\delta;f)
\right].
}
\]

---

## 3. Prime adjacency germ

Define the weighted neighboring symmetrization

\[
\boxed{
(\mathcal C_hf)(t)
=
\sum_{\lambda\in\mathscr H_c^\circ}
a_\lambda
\left[
\Sigma_{h-\lambda}f(t)
+
\Sigma_{h+\lambda}f(t)
\right].
}
\]

Then

\[
\boxed{
\mathscr P_h(\delta)f
=
\int_0^\delta
(\delta-t)
(\mathcal C_hf)(t)\,dt.
}
\]

So the full prime part is exactly the second-order Volterra transform of the
finite weighted adjacency germ.

Distributionally,

\[
\boxed{
\frac{d^2}{d\delta^2}
\mathscr P_h(\delta)f
=
(\mathcal C_hf)(\delta).
}
\]

No pointwise differentiability of \(f\) is required.

---

# III. Relation to the diagonal-superflat branch

## 4. Full centered kernel identity

For

\[
f\in K_c
\]

the movable-center equation is

\[
\boxed{
\mathscr D_h(\delta)f
+
\mathscr P_h(\delta)f
=
0.
}
\]

GERM-24 selected finitely many reachable centers

\[
h_1,\ldots,h_M
\]

and defined a hard branch

\[
V_\infty^{\rm diag}
\]

on which

\[
\boxed{
\|\mathscr D_{h_j}(\cdot)f\|_{L^2(0,\varepsilon)}
=
o(\varepsilon^N)
\qquad
\forall N.
}
\]

Therefore, by exact equality,

\[
\boxed{
\|\mathscr P_{h_j}(\cdot)f\|_{L^2(0,\varepsilon)}
=
o(\varepsilon^N)
\qquad
\forall N.
}
\]

Thus every selected prime Volterra output is operator-superflat on the hard
branch.

---

# IV. Why Volterra superflatness is not source rigidity

## 5. Second-order flat source model

Let

\[
H(\delta)
=
e^{-1/\delta^2}
\]

for \(\delta>0\), with the standard smooth extension by zero.

Set

\[
g=H''.
\]

Then

\[
g\in C^\infty
\]

locally and

\[
\boxed{
H(\delta)
=
\int_0^\delta
(\delta-t)g(t)\,dt.
}
\]

Hence a nonzero source germ can have a nonzero but infinitely-flat
second-order Volterra output.

Therefore

\[
\boxed{
\mathscr P_h
\text{ superflat}
\not\Rightarrow
\mathcal C_hf=0.
}
\]

Nor does it imply a finite-order lower bound for the neighboring
symmetrizations.

This is the prime analogue of the local archimedean no-go.

---

# V. Minimal-delay geometry

## 6. The first prime length

Set

\[
\boxed{
a=\log2.
}
\]

Every active prime-power delay satisfies

\[
\lambda\ge a.
\]

Assume

\[
\boxed{
a<L<2a.
}
\]

Equivalently,

\[
\log2<L<\log4.
\]

Define

\[
\boxed{
J_c=(L-a,a).
}
\]

Because

\[
L<2a,
\]

this interval is nonempty.

---

# VI. Prime-invisible core theorem

## 7. One plus-shift tent

Take

\[
s\in J_c,
\qquad
h\in(0,L),
\qquad
\lambda\ge a,
\]

and an admissible scale

\[
0<\delta<\min(h,L-h).
\]

For the plus-shift tent center

\[
d=h+\lambda,
\]

we have

\[
d-s
>
h+a-a
=
h.
\]

Therefore

\[
\boxed{
|s-(h+\lambda)|>\delta.
}
\]

So the tent centered at

\[
h+\lambda
\]

does not meet \(J_c\).

---

## 8. One minus-shift tent

For

\[
d=h-\lambda,
\]

we have

\[
s-d
>
L-a-(h-a)
=
L-h.
\]

Therefore

\[
\boxed{
|s-(h-\lambda)|>\delta.
}
\]

So the tent centered at

\[
h-\lambda
\]

also misses \(J_c\).

---

## 9. All prime channels vanish

The previous two inequalities hold for every active

\[
\lambda\ge a.
\]

Hence if

\[
\operatorname{supp}f\subseteq J_c,
\]

then for every interior center \(h\) and every admissible \(\delta\),

\[
\boxed{
\mathscr P_h(\delta)f=0.
}
\]

Thus

\[
\boxed{
L^2(J_c)
\subseteq
\bigcap_{h,\delta}
\ker\mathscr P_h(\delta).
}
\]

This is the prime-invisible core registered in the terminology file.

It is an infinite-dimensional exact kernel of the complete movable-center
prime observation family.

---

# VII. Regime consequences

## 10. One-prime-base range

If

\[
\log2<L\le\log3,
\]

only the prime base \(2\) is active.

Since

\[
\log3<\log4,
\]

the prime-invisible core is nonempty throughout this regime.

So the entire movable-center prime system has an infinite-dimensional blind
sector before any cross-prime arithmetic appears.

---

## 11. Early multi-prime range

If

\[
\log3<L<\log4,
\]

both prime bases \(2\) and \(3\) are active.

Nevertheless the same core

\[
J_c=(L-\log2,\log2)
\]

remains invisible to **all** prime delays.

Indeed every larger delay \(\lambda>\log2\) has an even wider individual
central shadow interval

\[
(L-\lambda,\lambda)
\supset
(L-\log2,\log2).
\]

Thus activating the second prime base does not immediately remove the prime
blind core.

---

## 12. Geometric transition at \(\log4\)

At

\[
L=\log4=2\log2,
\]

the minimal-delay central shadow collapses:

\[
L-a=a.
\]

For

\[
L\ge\log4,
\]

the argument above supplies no nonempty interval missed by every prime tent.

This is a genuine geometric transition in the prime observation system.

No injectivity claim is made above that transition.

---

# VIII. Pure-core kernel exclusion

## 13. Prime-free endpoint equation on \(J_c\)

Now suppose

\[
f\in K_c
\]

and

\[
\operatorname{supp}f\subseteq J_c.
\]

Because

\[
J_c\subset(0,a)
\]

and the smallest prime hinge is

\[
a=\log2,
\]

the endpoint inward prime contribution is identically zero for sufficiently
small endpoint motion.

Also,

\[
J_c
\Subset
(0,L),
\]

because

\[
L-a>0.
\]

Therefore the exact endpoint inward first-kind equation reduces to a purely
archimedean analytic transform on a source interval separated from the
archimedean origin.

GERM-2 archimedean injectivity applies.

Hence

\[
\boxed{
f=0.
}
\]

Therefore

\[
\boxed{
K_c\cap L^2(J_c)=\{0\}.
}
\]

---

# IX. Schur meaning of the invisible core

## 14. Core restriction is reconstructed from the complement

Let

\[
R_{\rm out}:
K_c
\to
L^2((0,L)\setminus J_c)
\]

be restriction to the complement of the core.

If

\[
R_{\rm out}f=0,
\]

then

\[
\operatorname{supp}f\subseteq J_c.
\]

Section VIII gives

\[
f=0.
\]

Thus

\[
\boxed{
R_{\rm out}
\text{ is injective on }K_c.
}
\]

Since \(K_c\) is finite dimensional, its inverse on the image is bounded.

Hence the core component is a finite-dimensional Schur reconstruction from
the source outside the core.

So the prime-invisible core is:

\[
\boxed{
\text{prime-invisible but globally archimedean-reconstructed}.
}
\]

It is not an independent kernel degree of freedom.

---

# X. What multicenter prime coupling actually buys

## 15. Positive structural statement

The full prime system gives the exact relation

\[
\boxed{
\mathscr P_h
=
\mathcal V_2(\mathcal C_hf),
}
\]

where \(\mathcal V_2\) is the second-order Volterra operator.

Thus all prime couplings are organized by a finite weighted adjacency of local
symmetrizations.

This is a genuine global source-custody description.

---

## 16. Negative coercivity statement

But the prime system has two independent failure modes:

1. **Volterra flatness:** a nonzero neighboring source combination can produce
   a superflat prime output;
2. **geometric invisibility:** for
   \[
   \log2<L<\log4,
   \]
   every source supported in \(J_c\) is missed exactly by every prime tent at
   every center.

Therefore there is no source-independent estimate of the form

\[
\boxed{
\|f\|_{\text{local}}
\lesssim
\text{finite power of }\delta^{-1}
\cdot
\|\text{prime multicenter field}\|
}
\]

on the full local source class.

Any such estimate must use the actual finite-dimensional kernel geometry.

---

# XI. Relation to the selected finite-center branch

## 17. Hard branch equation

For

\[
f\in V_\infty^{\rm diag},
\]

at each selected center

\[
h_j
\]

we have

\[
\boxed{
\mathscr D_{h_j}
=
-\mathscr P_{h_j},
}
\]

and both sides are superflat.

GERM-26 shows that the left side can be superflat for a nonzero even local
source.

The present pass shows that the right side can also be superflat without
source rigidity, and in the low-support range can even vanish identically on
an infinite-dimensional source sector.

Thus finite selected-center compatibility does not yet cross the local
flatness barrier.

---

# XII. What remains open above \(\log4\)

## 18. No core, but no proved injectivity

When

\[
L\ge\log4,
\]

the prime-invisible interval disappears.

However, the complete prime observation operator may still have:

- cancellation modes among several delays;
- Volterra-flat modes;
- finite-dimensional kernels on the actual obstruction.

This pass does not classify that kernel.

So the disappearance of \(J_c\) is a geometric transition, not a proof of
prime coercivity.

---

# XIII. Result of this NF pass

The prime-coupled multicenter system now has an exact local form:

\[
\boxed{
\mathscr P_h(\delta)f
=
\int_0^\delta
(\delta-t)
\sum_{\lambda}
a_\lambda
\left[
\Sigma_{h-\lambda}f(t)
+
\Sigma_{h+\lambda}f(t)
\right]dt.
}
\]

On the selected diagonal-superflat branch, every such prime output at the
selected centers is superflat.

Nevertheless:

\[
\boxed{
\log2<L<\log4
\Longrightarrow
L^2(L-\log2,\log2)
\subset
\ker(\text{all movable-center prime observations}).
}
\]

And

\[
\boxed{
K_c\cap
L^2(L-\log2,\log2)
=
\{0\}.
}
\]

Therefore the prime-invisible core is not a free kernel sector; it is
reconstructed globally from its complement by the archimedean first-kind
equation.

This shows exactly why local prime coupling does not complete the argument:
the missing information lives in the global Schur relation between
prime-visible source and prime-invisible source.

---

# XIV. Next traversal target

The next genuinely new target is

\[
\boxed{
\text{SZ-KERNEL-EDGE-GERM-28 / PRIME-TENT KERNEL CLASSIFICATION}.
}
\]

The next pass should study the all-center prime observation operator

\[
f
\longmapsto
\{\mathscr P_h(\cdot)f\}_{h\in(0,L)}
\]

itself.

The immediate targets are:

1. classify its exact kernel in the one-delay regime;
2. determine how the kernel changes when \(\log3\), \(\log4\), and later
   delays enter;
3. test whether the transition at
   \[
   L=\log4
   \]
   removes geometric blindness or merely replaces it by cancellation modes;
4. intersect that classification with the finite-dimensional regular kernel
   \(K_c\).

No complete prime-tent kernel classification is proved in this pass.

---

# XV. Cursor status

The canonical theorem cursor remains

\[
\boxed{\text{SZ-CROSS-COLLAR-3}}.
\]

This is an unratified prime-multicenter structural/no-go result.

No public promotion and no canonical cursor movement are asserted.
