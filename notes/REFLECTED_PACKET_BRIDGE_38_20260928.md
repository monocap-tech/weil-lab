# RPB-38 — Prime-log delay symbol spectral-synthesis test

**Date:** 2026-09-28  
**Branch:** \`research/reflected-packet-bridge\`  
**Status:** **PASS AS SYMBOL CLASSIFICATION / SCALAR SYMBOL NONDEGENERACY DOES NOT CONTROL THE COMPRESSED NULLSPACE / ZETA SPECTRUM SURVIVES THE COMPACT SOURCE**  
**Dependencies:** RPB-11, RPB-35 through RPB-37; compact-window explicit formula; Suzuki screw-function spectral expansion and mean-periodicity.  
**Promotion status:** none.

## 0. Objective

RPB-37 exhausted spatial support-order iteration.

The remaining proposed route was frequency-side:

1. analyze the finite prime-log delay symbol;
2. combine it with the exact archimedean multiplier;
3. use compact support / Paley--Wiener structure;
4. compare with Suzuki's mean-periodic/Fourier--Carleman representation;
5. determine whether symbol nondegeneracy or spectral synthesis excludes
   collar persistence of a nonzero screw-visible neutral source.

RPB-38 finds a sharp separation.

The whole-line scalar symbol is strongly nondegenerate: it is real analytic and
has only finitely many real zeros.

But the compact-window neutral mode is not a whole-line multiplier kernel.  It
is a kernel vector of a **compressed** multiplier/operator, so the Fourier
transform of the mode is not supported on the symbol zero set.

At the same time, the compact source cannot eliminate the zeta spectral
content of the screw potential: unconditionally, \(\gg T\log T\) distinct
simple critical spectral coefficients survive.

Thus the obstruction is not spectral scarcity.  It is the absence of a
quasianalytic/local-uniqueness theorem converting a spatial collar gap into
coefficientwise spectral annihilation.

---

## 1. Strict-right scalar symbol

Fix the neutral edge \(c=c_*\), and use the strict-right active prime-power set

\`\`\`math
\mathcal N_{c+}
=
\{n=p^m:\log n\le 2c\}.
\`\`\`

Define the finite prime-delay symbol

\`\`\`math
\boxed{
P_{c+}(\xi)
=
\sum_{\log n\le2c}
\frac{2\Lambda(n)}{\sqrt n}
\cos(\xi\log n).
}
\`\`\`

The exact compact-window scalar symbol is

\`\`\`math
\boxed{
\Psi_{c+}(\xi)
=
\Re\psi\!\left(
\frac14+\frac{i\xi}{2}
\right)
-
\log\pi
-
P_{c+}(\xi).
}
\`\`\`

The equality-threshold convention is the one already fixed in the
right-limit compact-window operator.

---

## 2. The prime-delay symbol is bounded quasiperiodic

Because only finitely many prime powers satisfy

\`\`\`math
\log n\le2c,
\`\`\`

the function \(P_{c+}\) is a finite trigonometric polynomial.

Hence

\`\`\`math
\boxed{
|P_{c+}(\xi)|
\le
2
\sum_{\log n\le2c}
\frac{\Lambda(n)}{\sqrt n}
<\infty.
}
\`\`\`

By RPB-37, at the actual candidate edge the frequency set contains at least

\`\`\`math
\log2,
\qquad
\log3,
\`\`\`

with irrational ratio.

Thus \(P_{c+}\) is genuinely quasiperiodic rather than periodic in the
single-frequency sense.

This changes recurrence geometry but not its boundedness.

---

## 3. The full scalar symbol tends to \(+\infty\)

The digamma asymptotic gives

\`\`\`math
\Re\psi\!\left(
\frac14+\frac{i\xi}{2}
\right)
=
\log|\xi|
-
\log2
+
O(|\xi|^{-2})
\`\`\`

as \(|\xi|\to\infty\).

Since \(P_{c+}\) is bounded,

\`\`\`math
\boxed{
\Psi_{c+}(\xi)
=
\log|\xi|
+
O_c(1).
}
\`\`\`

Therefore

\`\`\`math
\boxed{
\Psi_{c+}(\xi)\to+\infty
\qquad
(|\xi|\to\infty).
}
\`\`\`

So every real zero of the scalar symbol lies in one compact frequency interval.

---

## 4. The real zero set of the scalar symbol is finite

The function

\`\`\`math
\xi
\mapsto
\Re\psi\!\left(
\frac14+\frac{i\xi}{2}
\right)
\`\`\`

is real analytic on \(\mathbb R\).

The finite trigonometric prime term is real analytic as well.

Therefore

\`\`\`math
\boxed{
\Psi_{c+}
\text{ is real analytic on }\mathbb R.
}
\`\`\`

It is not identically zero because it tends to \(+\infty\).

A nonzero real-analytic function has isolated zeros.

Since all zeros lie in a compact interval by Section 3,

\`\`\`math
\boxed{
Z_{\mathbb R}(\Psi_{c+})
=
\{\xi\in\mathbb R:\Psi_{c+}(\xi)=0\}
\text{ is finite}.
}
\`\`\`

This is a strong whole-line symbol nondegeneracy statement.

---

## 5. Why this does not kill the compact-window neutral mode

Let

\`\`\`math
h
\in
H_0^1(-c,c)
\`\`\`

be a screw-visible neutral mode, and let

\`\`\`math
H(z)
=
\widehat h(z).
\`\`\`

Compact support gives an entire Paley--Wiener transform of exponential type
\(c\).

It is tempting to argue:

\`\`\`math
\Psi_{c+}(\xi)H(\xi)=0
\quad\Longrightarrow\quad
H=0
\`\`\`

because the real zero set of \(\Psi_{c+}\) is finite.

But the premise is false.

The localized operator is a compression of the whole-line operator:

\`\`\`math
A_c
=
P_c
\mathcal W^{\rm ext}_{c+}
P_c
\`\`\`

in the appropriate form/operator sense, plus the fixed threshold convention.

The null relation is

\`\`\`math
\boxed{
P_c
\mathcal W^{\rm ext}_{c+}h
=
0,
}
\`\`\`

not

\`\`\`math
\mathcal W^{\rm ext}_{c+}h
=
0
\quad
\text{on all of }\mathbb R.
\`\`\`

Fourier transformation diagonalizes the whole-line multiplier, but not the
spatial compression.

Therefore

\`\`\`math
\boxed{
P_cM(D)P_ch=0
\not\Longrightarrow
M(\xi)H(\xi)=0.
}
\`\`\`

This is the compressed-symbol caution.

---

## 6. Collar persistence is a gap condition on the output, not multiplier support

Under the hypothetical strict null extension to \(a>c\), put

\`\`\`math
q
=
\mathcal W^{\rm ext}_{c+}h.
\`\`\`

Then

\`\`\`math
\boxed{
q=0
\quad
\text{on }(-a,a).
}
\`\`\`

Thus \(q\) has a central spatial gap.

The Fourier-side relation is schematically

\`\`\`math
\boxed{
\widehat q(\xi)
=
\Psi_{c+}(\xi)H(\xi)
+
\widehat{\mathcal R_{\rm pole}h}(\xi),
}
\`\`\`

with the pole row treated in its finite-rank distributional realization.

The collar hypothesis says that the inverse Fourier transform of the
right-hand side has a gap.

It does **not** say the right-hand side vanishes on the frequency line.

Hence Paley--Wiener theory for \(H\) does not convert the collar condition into
support on \(Z_{\mathbb R}(\Psi_{c+})\).

The correct frequency-side problem is a gap/Wiener--Hopf problem.

---

## 7. Screw spectral expansion after convolution by a compact source

Now return to the screw carrier.

Suzuki's unconditional zero expansion is

\`\`\`math
\Psi(t)
=
\sum_\gamma
\frac{1-e^{i\gamma t}}{\gamma^2},
\`\`\`

where the zeros \(\gamma\) of
\(\xi(1/2-iz)\) are counted with multiplicity.

Since

\`\`\`math
g=-\Psi,
\`\`\`

we have

\`\`\`math
g(t)
=
\sum_\gamma
\frac{e^{i\gamma t}-1}{\gamma^2}.
\`\`\`

Let

\`\`\`math
0\ne u
\in
L_0^2(-c,c),
\`\`\`

and define

\`\`\`math
U(z)
=
\int_{-c}^{c}
u(y)e^{-izy}\,dy.
\`\`\`

Because

\`\`\`math
\int u=0,
\`\`\`

the constant term in the screw expansion disappears after convolution.

Thus the screw potential

\`\`\`math
F_u
=
g*u
\`\`\`

has the spectral representation

\`\`\`math
\boxed{
F_u(x)
=
\sum_\gamma
\frac{U(\gamma)}{\gamma^2}
e^{i\gamma x},
}
\`\`\`

with the fixed Fourier-sign convention above.

On every compact \(x\)-interval this series converges absolutely and uniformly:
the zeta ordinates remain in the fixed transverse strip, \(U(\gamma)\) is
uniformly bounded there by compact support, and

\`\`\`math
\sum_\gamma
\frac{m_\gamma}{1+|\gamma|^2}
<
\infty
\`\`\`

by the standard zeta zero count.

### External source

Masatoshi Suzuki,
*Aspects of the screw function corresponding to the Riemann zeta-function*,
Theorem 1.1, especially the zero expansion (1.3).

---

## 8. A compact source cannot cancel the critical zeta spectrum

The transform \(U\) is entire of finite exponential type \(c\).

Exactly as in RPB-11, Jensen's formula gives

\`\`\`math
\boxed{
n_U(T)
=
O_u(T)
}
\`\`\`

unless \(U\equiv0\).

Since \(u\ne0\), Fourier injectivity gives

\`\`\`math
U\not\equiv0.
\`\`\`

Conrey's unconditional theorem supplies

\`\`\`math
\gg
T\log T
\`\`\`

distinct simple critical-line zero ordinates up to height \(T\).

Therefore \(U\) can vanish at only \(O(T)\) of those ordinates.

Hence

\`\`\`math
\boxed{
\#\left\{
0<\gamma\le T:
\frac12+i\gamma
\text{ simple critical zero},
\;
U(\gamma)\ne0
\right\}
\gg
T\log T.
}
\`\`\`

So the screw potential retains a positive-proportion-scale critical spectral
population.

Equivalently:

\`\`\`math
\boxed{
\text{nonzero compact source}
\Longrightarrow
\text{no finite or sparse cancellation of the zeta spectrum}.
}
\`\`\`

This is zeta spectral survival under a compact source.

---

## 9. Spectral abundance still does not imply local uniqueness

Suppose the screw potential is constant on a strict collar.

Subtract the constant.

Then one has a locally vanishing function represented by an infinite
exponential series with many surviving zeta frequencies.

There is no general theorem that an absolutely convergent exponential series
must vanish globally when it vanishes on one interval.

The ambient regularity class is not automatically quasianalytic.

A simple generic sharpness model is a nonzero smooth periodic function that
vanishes on an interval.

Its Fourier coefficients decay faster than every power, hence are absolutely
summable, while its Fourier series still has a genuine open zero set.

Thus

\`\`\`math
\boxed{
\text{absolutely convergent spectral expansion}
+
\text{local zero interval}
\not\Rightarrow
\text{all spectral coefficients vanish}.
}
\`\`\`

This example is not a zeta-spectrum construction.

It shows that coefficient summability alone is not the missing uniqueness
input.

---

## 10. Suzuki mean periodicity remains source-blind

Suzuki proves unconditionally that \(g\) is mean periodic.

A concrete annihilator is obtained from the derivative of the standard
\(\xi\)-kernel:

\`\`\`math
g*\phi=0.
\`\`\`

For the compact-source potential

\`\`\`math
F_u=g*u,
\`\`\`

associativity gives

\`\`\`math
\boxed{
F_u*\phi
=
u*(g*\phi)
=
0.
}
\`\`\`

Therefore every compact-source screw potential lies in the same
translation-invariant mean-periodic variety generated by \(g\).

The Fourier--Carleman transform of the global convolution equation encodes the
zeta spectral data.

But the annihilator is independent of the selected source \(u\).

It cannot distinguish:

- \(u\in\ker G_c\);
- collar persistence;
- selected neutral custody;
- the over-budget/fall-through branch.

This is the universal screw mean-periodicity no-gain from RPB-37.

### External source

Masatoshi Suzuki,
*Aspects of the screw function corresponding to the Riemann zeta-function*,
§10, especially the convolution equation and Fourier--Carleman discussion.

---

## 11. Schwartz spectral synthesis does not supply collar uniqueness

On the real line, classical spectral synthesis describes closed
translation-invariant varieties in terms of exponential monomials.

That theorem concerns the global translation-invariant closure of a function
space.

The property

\`\`\`math
F_u
\text{ is constant on a prescribed interval}
\`\`\`

is not translation invariant.

Therefore global spectral synthesis of the mean-periodic variety does not
imply that local collar constancy forces \(F_u\) to be globally constant.

One would need an additional quasianalyticity or gap theorem for the specific
zeta spectral variety.

No such theorem is currently imported in RPB-38.

---

## 12. The prime-log symbol does not isolate the selected source

The bounded quasiperiodic symbol \(P_{c+}\) contains the arithmetic data of
the finite delays.

Its frequency group is dense by RPB-37.

But in the full scalar symbol

\`\`\`math
\Psi_{c+}
=
m_\infty
-
P_{c+},
\`\`\`

the logarithmic archimedean growth dominates at high frequency and leaves only
finitely many real zeros.

Thus neither extreme helps:

- the prime-delay symbol alone has rich quasiperiodic recurrence;
- the full scalar symbol has a very small real zero set.

The selected compact-window null mode is controlled by neither zero set,
because the support compression converts the problem into a spatial-gap
condition on the output.

This is the central outcome of the symbol test.

---

## 13. Exact frequency-side retyping

Let

\`\`\`math
q
=
\mathcal W^{\rm ext}_{c+}h,
\qquad
q=0
\text{ on }(-a,a).
\`\`\`

Split the exterior output formally as

\`\`\`math
q=q_-+q_+,
\`\`\`

with

\`\`\`math
\operatorname{supp}q_-
\subseteq
(-\infty,-a],
\qquad
\operatorname{supp}q_+
\subseteq
[a,\infty).
\`\`\`

The Fourier--Carleman transforms of the two tails naturally live in opposite
half-plane analytic classes.

The exact symbol identity becomes a boundary-value factorization problem of
the species

\`\`\`math
\boxed{
\Psi_{c+}(z)H(z)
+
R_h(z)
=
Q_-(z)
+
Q_+(z),
}
\`\`\`

where:

- \(H\) is entire of exponential type \(c\);
- \(R_h\) is finite dimensional from the pole row;
- \(Q_-\) and \(Q_+\) are transforms of the left/right exterior tails in the
  appropriate Fourier--Carleman sense.

RPB-38 does **not** yet promote this schematic identity as a fully typed
Hardy-space theorem; the tail growth class still has to be checked.

But it identifies the correct next object.

---

## 14. What would now be sufficient

A frequency-side closure would require a theorem strong enough to show that
the only Paley--Wiener \(H\) participating in the exterior-tail factorization
at the neutral edge is

\`\`\`math
H\equiv0.
\`\`\`

Possible sufficient inputs include:

1. a Wiener--Hopf factorization of the exact completed Weil symbol with a
   controlled index;
2. a Fourier--Carleman gap theorem for the exact left/right tail classes;
3. a quasianalyticity theorem for the selected zeta spectral variety;
4. a divisibility theorem coupling the finite pole row to the Paley--Wiener
   numerator.

None is supplied by:

- finiteness of the real symbol-zero set;
- prime-log quasiperiodicity;
- compact support alone;
- Suzuki's universal mean-periodicity relation;
- spectral abundance alone.

---

## 15. RPB-38 determination

\`\`\`math
\boxed{
\textbf{RPB-38 — PRIME-LOG SYMBOL NONDEGENERACY DOES NOT CLOSE THE COMPRESSED COLLAR PROBLEM; THE COMPACT SOURCE RETAINS THE ZETA SPECTRUM.}
}
\`\`\`

Positive results:

\`\`\`math
\boxed{
Z_{\mathbb R}(\Psi_{c_*+})
\text{ is finite},
}
\`\`\`

and for every nonzero compact screw source,

\`\`\`math
\boxed{
\gg T\log T
\text{ simple critical zeta spectral coefficients survive up to height }T.
}
\`\`\`

Negative result:

\`\`\`math
\boxed{
\text{whole-line symbol nondegeneracy}
\not\Rightarrow
\text{compressed-window nullspace triviality}.
}
\`\`\`

The collar condition is a spatial-gap condition on the whole-line output, not
frequency support on the scalar symbol zero set.

Next cursor:

\`\`\`text
RPB-39 / EXTERIOR-TAIL FOURIER-CARLEMAN FACTORIZATION
\`\`\`

The next pass should type the exterior tails precisely:

1. determine the growth/decay class of
   \(q=\mathcal W^{\rm ext}_{c_*+}h\) outside the compact source;
2. define the left/right Fourier--Carleman transforms;
3. derive the exact half-plane boundary-value identity with the completed Weil
   symbol and finite pole row;
4. compute the relevant Wiener--Hopf index or identify the precise
   factorization obstruction.
