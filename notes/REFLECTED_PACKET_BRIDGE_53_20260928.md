# RPB-53 — Actual zero-mode endpoint regularity test

**Date:** 2026-09-28  
**Branch:** research/reflected-packet-bridge  
**Status:** **PASS AS A NO-GO / ZERO SPECTRAL VALUE DOES NOT REMOVE THE GENERIC LOGARITHMIC BOUNDARY LAYER / PURE LOG-LAPLACIAN ZERO EIGENMODE GIVES A SHARP WITNESS / ACTUAL-WEIL CORE LIFT REQUIRES AN EXTRA BOUNDARY-CANCELLATION THEOREM / CORE-LIFT ROUTE EXHAUSTED AT CURRENT INPUT LEVEL**  
**Dependencies:** RPB-31, RPB-49, RPB-51, RPB-52; Laptev--Weth spectral scaling for the Dirichlet logarithmic Laplacian; Hernández-Santamaría--López Ríos--Saldaña optimal boundary regularity/Hopf theorem.  
**Promotion status:** none.

## 0. Objective

RPB-52 showed that the completed generalized zero equation does not abstractly
force an ordinary \(L^2\) screw representative.

RPB-53 returns to the actual localized Weil equation

~~~math
A_ch=0
~~~

and asks whether the special spectral value \(0\) removes the generic
logarithmic boundary layer of the Dirichlet logarithmic principal operator.

The answer is negative at the level of currently available structure.

There are two independent reasons:

1. the RPB-49 logarithmic edge normal operator has a genuine homogeneous
   boundary mode
   \[
   H(t)\sim t^{-1/2};
   \]
2. the pure Dirichlet logarithmic Laplacian itself admits a scaling for which
   the principal eigenvalue is exactly zero while the corresponding positive
   eigenfunction has a nonzero optimal \(\ell^{1/2}\) boundary layer.

Thus zero spectral value is compatible with, rather than hostile to, the
generic noncore endpoint species.

---

## 1. Actual Weil zero equation near the endpoint

Write the actual fixed-window operator schematically as

~~~math
A_c
=
\frac12L_\Delta
+
B_c,
~~~

where \(B_c\) contains:

- the bounded constant and lower pseudodifferential archimedean correction;
- finitely many prime translations;
- the finite-rank pole/evaluation contribution;
- the finite selected correction when present.

RPB-31 proved

~~~math
\mathfrak D(A_c)
=
\mathfrak D(A_{\log,c}),
~~~

and for

~~~math
h\in\ker A_c
~~~

the equation gives only

~~~math
\frac12L_\Delta h
=
-B_ch.
~~~

At the guaranteed operator level,

~~~math
B_ch\in L^2.
~~~

Therefore the null equation returns exactly logarithmic operator-domain
regularity and does not bootstrap itself into \(H^\varepsilon\), much less
\(H_0^1\).

RPB-53 asks whether the **value zero itself** changes the endpoint indicial
picture.  It does not.

---

## 2. The logarithmic edge normal operator already has a zero homogeneous mode

RPB-49 put the endpoint into logarithmic coordinates

~~~math
s=c-x,
\qquad
t=\log\frac1s,
\qquad
H(t)=h(c-e^{-t}),
~~~

and obtained the leading normal operator

~~~math
\boxed{
\mathcal N_{\log}H(t)
=
2tH(t)
-
\int^t H(w)\,dw.
}
~~~

For the ansatz

~~~math
H(t)=t^{-\alpha},
~~~

the leading output is

~~~math
\mathcal N_{\log}H
=
\frac{1-2\alpha}{1-\alpha}
t^{1-\alpha}
+
o(t^{1-\alpha}).
~~~

The coefficient vanishes at

~~~math
\boxed{
\alpha=\frac12.
}
~~~

Hence

~~~math
\boxed{
H_{\rm edge}(t)
\sim
t^{-1/2}
}
~~~

is already the homogeneous zero mode of the principal endpoint operator.

In physical boundary distance,

~~~math
\boxed{
h(c-s)
\sim
\ell^{1/2}(s),
\qquad
\ell(s)\asymp\frac1{\log(1/s)}.
}
~~~

Therefore the spectral equation \(A_ch=0\) does not introduce a leading-order
condition that sets the coefficient of this boundary mode to zero.

The leading principal coefficient has already vanished identically at the
boundary exponent \(\alpha=1/2\).

---

## 3. The eigenvalue term is lower in the endpoint hierarchy

More generally, consider

~~~math
A_ch
=
\lambda h.
~~~

For the generic edge profile

~~~math
h(c-s)
\sim
b\,t^{-1/2},
~~~

the leading logarithmic normal operator is arranged to cancel at order
\(t^{1/2}\).

The spectral term has size only

~~~math
\lambda h
\sim
\lambda b\,t^{-1/2}.
~~~

Thus \(\lambda\) enters at a strictly lower endpoint order than the leading
indicial cancellation selecting the exponent \(1/2\).

Setting

~~~math
\lambda=0
~~~

removes this lower-order term.  It does **not** impose

~~~math
b=0.
~~~

Accordingly, zero spectral value cannot be treated as a Dirichlet trace
condition on the logarithmic boundary amplitude.

---

## 4. Sharp pure-model witness at eigenvalue zero

The previous conclusion is not merely formal.

Let

~~~math
\mathcal H_\Omega
=
\frac12L_\Delta
~~~

be the Dirichlet logarithmic Laplacian on a bounded Lipschitz domain
\(\Omega\).

Laptev--Weth give the scaling law

~~~math
\boxed{
\lambda_k(R\Omega)
=
\lambda_k(\Omega)
-
\log R.
}
~~~

Choose

~~~math
R
=
e^{\lambda_1(\Omega)}.
~~~

Then

~~~math
\boxed{
\lambda_1(R\Omega)=0.
}
~~~

Thus the rescaled pure logarithmic Dirichlet operator has a genuine
nontrivial principal zero eigenfunction \(\phi_1\ge0\).

This is already a zero spectral mode of exactly the same logarithmic principal
species that governs the actual Weil endpoint.

---

## 5. The zero eigenfunction carries the optimal logarithmic boundary layer

The optimal boundary regularity/Hopf theorem for the Dirichlet logarithmic
Laplacian gives, at a boundary point satisfying the interior sphere condition,
for a nontrivial nonnegative weak supersolution,

~~~math
\liminf_{s\downarrow0}
\frac{
\phi_1(x_0-s\nu)
}{
\ell^{1/2}(s)
}
>
0.
~~~

Apply this to the principal eigenfunction at the scaled support for which

~~~math
\frac12L_\Delta\phi_1=0.
~~~

Then

~~~math
\boxed{
\phi_1(x_0-s\nu)
\gtrsim
\ell^{1/2}(s)
}
~~~

near the boundary.

So a **zero eigenfunction itself** can have a nonzero generic logarithmic
boundary amplitude.

This is the sharp witness that RPB-52 lacked.

---

## 6. Such a zero mode is genuinely outside the screw core

Every

~~~math
h\in H_0^1
~~~

satisfies the one-dimensional endpoint trace estimate

~~~math
|h(c-s)|
\le
s^{1/2}
\|h'\|_{L^2(c-s,c)}
=
o(s^{1/2})
~~~

along the endpoint.

But

~~~math
\ell^{1/2}(s)
=
(\log(1/s))^{-1/2}
~~~

decays much more slowly than \(s^{1/2}\).

Therefore a function satisfying the Hopf lower bound

~~~math
h(c-s)
\gtrsim
\ell^{1/2}(s)
~~~

cannot lie in \(H_0^1\).

Hence the scaled pure logarithmic problem realizes the exact phenomenon

~~~math
\boxed{
0\ne h\in\ker A_{\log}
\quad\text{with}\quad
h\notin H_0^1.
}
~~~

This is an actual endpoint-PDE witness, not merely the abstract sequence-space
countermodel of RPB-52.

---

## 7. Consequence for the actual Weil zero mode

The actual Weil operator differs from its logarithmic principal operator by
terms that do not raise endpoint order.

Near a fixed endpoint:

- active prime translations evaluate either outside the support or at interior
  points a fixed positive distance away;
- the pole/evaluation contribution has finite-dimensional smooth range;
- the exact archimedean remainder is lower pseudodifferential order;
- bounded selected corrections do not alter the logarithmic indicial root.

Therefore the actual equation may determine the coefficient of the
\(\ell^{1/2}\) layer through a special global cancellation, but no currently
available principal-order or mapping theorem forces that coefficient to
vanish.

In particular,

~~~math
\boxed{
A_ch=0
\not\Longrightarrow
h\in H_0^1
}
~~~

by any mechanism established in the current RPB corpus.

Any such implication would be a new actual-Weil boundary theorem.

---

## 8. Parity and arithmetic delays do not change the conclusion

Reflection symmetry splits the zero eigenspace into parity blocks, but the
logarithmic edge normal operator and its exponent

~~~math
\alpha=\frac12
~~~

occur in either block after imposing the corresponding left/right relation.

Parity can relate boundary coefficients; it does not force both to vanish.

Likewise, the finite prime delays are lower-order at the endpoint.  They can
supply scalar cancellation conditions involving interior values, but they
cannot remove the homogeneous logarithmic edge species by operator order
alone.

Thus a successful actual-Weil core-lift theorem would need an **explicit
arithmetic boundary-amplitude cancellation**, not merely parity or finite-delay
regularity preservation.

---

## 9. The correct remaining endpoint datum

Whenever an actual zero mode admits an optimal boundary expansion, write
schematically

~~~math
h(c-s)
=
b_+(h)\,\ell^{1/2}(s)
+
o(\ell^{1/2}(s))
~~~

and similarly at the left endpoint with coefficient \(b_-(h)\).

RPB-53 does not assert that every Friedrichs zero mode has such a classical
expansion; the current guaranteed domain is weaker.

The point is structural:

~~~math
\boxed{
\text{core lift requires eliminating the logarithmic boundary layer,}
}
~~~

while

~~~math
\boxed{
\lambda=0
\text{ does not eliminate it.}
}
~~~

Thus the missing information has been reduced from a vague regularity question
to a boundary-amplitude cancellation problem for the actual zeta-Weil kernel.

Even vanishing of the leading \(\ell^{1/2}\) coefficient would not by itself
prove \(H_0^1\); further residual boundary regularity would still have to be
controlled.

---

## 10. Core-lift route status

RPB-31 showed:

~~~math
\ker A_c
\subset
\mathfrak D(A_{\log,c})
~~~

with no positive Sobolev gain.

RPB-52 showed that the generalized zero eigenvalue does not abstractly lift the
mode into the ordinary screw carrier.

RPB-53 now shows that the actual logarithmic endpoint principal equation also
does not make zero special in the required way.

Indeed the pure principal operator has a genuine zero eigenmode carrying the
optimal noncore boundary layer.

Therefore:

~~~text
GENERIC DOMAIN BOOTSTRAP: EXHAUSTED
GENERALIZED-PENCIL ZERO LIFT: EXHAUSTED
ZERO-SPECTRAL-VALUE ENDPOINT LIFT: EXHAUSTED
ACTUAL-WEIL CORE LIFT: REQUIRES A NEW ARITHMETIC BOUNDARY-CANCELLATION THEOREM
~~~

---

## 11. New direct opportunity: noncore boundary leakage

The failure of core lift is not necessarily bad for null-extension rigidity.

If an actual zero mode carries a nonzero boundary layer

~~~math
h(c-r)
\sim
b\,\ell^{1/2}(r),
\qquad
b\ne0,
~~~

then just outside the support, at \(x=c+s\), the logarithmic integral kernel
contains the contribution

~~~math
-\int_0^\delta
\frac{h(c-r)}{s+r}\,dr.
~~~

For the model boundary profile,

~~~math
\int_s^\delta
\frac{dr}{
r\sqrt{\log(1/r)}
}
=
2\sqrt{\log(1/s)}
+
O(1).
~~~

Hence one expects the exterior logarithmic output

~~~math
\boxed{
L_\Delta h(c+s)
\sim
-2b\sqrt{\log(1/s)}
}
~~~

up to normalization and lower-order terms.

The finite active prime translations sample interior points and do not have
this boundary divergence.

Thus a **nonzero noncore logarithmic boundary amplitude may itself force
immediate exterior leakage**, potentially giving a direct null-extension
obstruction complementary to the screw-core route.

RPB-53 records this only as the next mechanism to test; it does not promote the
asymptotic as a theorem for every Friedrichs zero mode.

---

## 12. RPB-53 determination

~~~math
\boxed{
\textbf{RPB-53 — ZERO SPECTRAL VALUE DOES NOT KILL THE GENERIC LOGARITHMIC BOUNDARY LAYER; THE CURRENT CORE-LIFT ROUTE IS EXHAUSTED WITHOUT A NEW ACTUAL-WEIL BOUNDARY-CANCELLATION THEOREM.}
}
~~~

Principal endpoint species:

~~~math
\boxed{
h(c-s)\sim
b\,(\log(1/s))^{-1/2}
}
~~~

is compatible with eigenvalue zero.

Sharp witness:

~~~math
\boxed{
\lambda_1(R\Omega)=0
\quad\text{and}\quad
\phi_1\gtrsim\ell^{1/2}
}
~~~

for a suitable scaling of the pure Dirichlet logarithmic Laplacian.

Therefore the actual-Weil implication

~~~math
\ker A_c
\subseteq
H_0^1(-c,c)
~~~

cannot follow from zero spectral value plus logarithmic principal structure.

## Next cursor

~~~text
RPB-54 / NONCORE LOG-LAYER EXTERIOR LEAKAGE TEST
~~~

The next pass should test the complementary route:

1. assume an actual Friedrichs zero mode has a nonzero optimal logarithmic
   boundary amplitude;
2. compute the exact exterior singularity of the logarithmic principal
   operator across the zero-extension boundary;
3. verify that finite prime translations, pole terms, and smoother
   archimedean corrections cannot cancel the resulting
   \(\sqrt{\log(1/s)}\)-type divergence;
4. determine whether every such noncore mode is thereby excluded from strict
   null extension;
5. isolate the residual class with vanishing leading logarithmic boundary
   amplitude.
