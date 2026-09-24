# Explicit-Formula Arithmetic Attachment
## H1-P2.2 — Scalar localization, completed-\(\Xi\) next jets, and compact-window arithmetic operators

This pass normalizes the ZW-2 layer.

The objective is not to prove an RH-facing exclusion theorem. It is to determine exactly what the explicit formula contributes **before** the open interfaces begin.

The result splits into two branches:

\[
\boxed{
\text{negative persistent source}
\longrightarrow
\text{weighted near next-jet field},
}
\]

and

\[
\boxed{
\text{neutral compact-window mode}
\longrightarrow
\text{logarithmic operator + finitely many prime shifts}.
}
\]

---

# Part I — Negative branch

## 1. Selected contracted-residue functional

Let \(v\ne0\) be a finite selected raw residue vector on a packet \(F\), with

\[
\mathbf1^Tv=0.
\]

Let

\[
R_v(z)=\sum_{\rho_j\in F}\frac{v_j}{z-\rho_j}.
\]

For an admissible scalar multiplier \(\psi\), write

\[
\mathcal C_v[\psi]
\]

for the selected contracted-residue term in the scalar explicit formula.

For the bounded-depth exponential family

\[
\psi_\tau(s)=e^{\tau(s-c)},
\]

define

\[
C_v(\tau):=\mathcal C_v[\psi_\tau].
\]

Because \(F\) is finite, \(C_v(\tau)\) is an exponential polynomial in \(\tau\).

---

## ZW2-T1 — Two-mode selected-preserving multiplier

Choose \(\tau_1,\tau_2\) such that

\[
(C_v(\tau_1),C_v(\tau_2))\ne(0,0).
\]

Then there is a nonzero pair \((\beta_1,\beta_2)\) for which

\[
\psi
=
\beta_1\psi_{\tau_1}
+
\beta_2\psi_{\tau_2}
\]

satisfies

\[
\boxed{
\mathcal C_v[\psi]=0.
}
\]

An explicit choice is

\[
(\beta_1,\beta_2)
=
\bigl(C_v(\tau_2),-C_v(\tau_1)\bigr).
\]

If \(C_v\equiv0\), every member of the exponential family is already selected-preserving.

**Standing:** PROVED as finite-dimensional scalar algebra.

### Scope

The earlier SOURCE-3 work also produced choices retaining a nontrivial prime-sensitive row for the fixed nonzero source.

That stronger simultaneous nondegeneracy is retained as a source-specific input, but the theorem spine below requires only:

1. a fixed selected-preserving multiplier;
2. boundedness of that multiplier on the zero strip;
3. the zero-moment far decay from H1-P2.1.

---

# 2. Far-tail localization

Fix a height center \(T_F\) for the selected packet.

Assume \(\psi\) is bounded on the zero strip:

\[
|\psi(\mu)|\le M_\psi.
\]

By ZW1-T8,

\[
R_v(\mu)
=
O_v(|\mu|^{-2})
\]

away from the finite selected packet.

Use the standard unit-height zero count

\[
N(X+1)-N(X)=O(\log(2+X))
\]

with multiplicity.

---

## ZW2-T2 — Quantitative far-tail theorem

Define the distant complementary response

\[
\mathcal F_{v,R}[\psi]
:=
\sum_{\substack{\mu\notin F\\
|\Im\mu-T_F|\ge R}}
m_\mu\psi(\mu)R_v(\mu).
\]

Then for sufficiently large \(R\),

\[
\boxed{
|\mathcal F_{v,R}[\psi]|
\ll_{v,\psi,F}
\frac{\log R}{R}.
}
\]

In particular,

\[
\boxed{
\mathcal F_{v,R}[\psi]\to0
\qquad(R\to\infty).
}
\]

### Proof

Partition the complementary zeros into unit-height shells.

On a shell at distance \(n\) from the fixed packet,

\[
|R_v(\mu)|\ll_v n^{-2},
\]

while the shell contains

\[
O(\log(2+n+|T_F|))
\]

zeros counted with multiplicity.

Thus

\[
|\mathcal F_{v,R}[\psi]|
\ll
M_\psi
\sum_{n\ge R}
\frac{\log(2+n+|T_F|)}{n^2}
\ll
\frac{\log R}{R}.
\]

**Standing:** PROVED from ZW1-T8 + zero counting.

### Consequence

For a fixed selected source and multiplier, the infinite distant divisor is not the residual arithmetic obstruction.

All macroscopically necessary compensation can be localized into a finite/intermediate neighborhood of \(F\).

---

# 3. Near complementary field

Define the near response

\[
\boxed{
\mathcal N_{v,R}[\psi]
=
\sum_{\substack{\mu\notin F\\
|\Im\mu-T_F|<R}}
m_\mu\psi(\mu)R_v(\mu).
}
\]

For fixed \(R\), this is a finite sum.

Since

\[
R_v(\mu)
=
\sum_{\rho_j\in F}
\frac{v_j}{\mu-\rho_j},
\]

we may interchange the two finite sums:

\[
\boxed{
\mathcal N_{v,R}[\psi]
=
\sum_{\rho_j\in F}
v_j
\sum_{\substack{\mu\notin F\\
|\Im\mu-T_F|<R}}
\frac{m_\mu\psi(\mu)}
{\mu-\rho_j}.
}
\]

Thus the remaining divisor burden is a finite weighted complementary logarithmic-derivative field evaluated against \(v\).

**Standing:** PROVED.

---

# 4. Completed-\(\Xi\) lift

Define

\[
\boxed{
H_v(z):=\Xi(z)R_v(z).
}
\]

Let \(\mu\notin F\) be a zero of \(\Xi\) of multiplicity \(m_\mu\).

Because \(\mu\) is not selected, \(R_v\) is analytic at \(\mu\).

Write locally

\[
\Xi(z)
=
(z-\mu)^{m_\mu}g_\mu(z),
\qquad
g_\mu(\mu)\ne0.
\]

Then

\[
H_v(z)
=
(z-\mu)^{m_\mu}g_\mu(z)R_v(z).
\]

---

## ZW2-T3 — Complementary next-jet identity

At every complementary zero \(\mu\notin F\),

\[
\boxed{
R_v(\mu)
=
\frac{H_v^{(m_\mu)}(\mu)}
{\Xi^{(m_\mu)}(\mu)}.
}
\]

### Proof

Differentiating exactly \(m_\mu\) times at \(z=\mu\) gives

\[
H_v^{(m_\mu)}(\mu)
=
m_\mu!\,g_\mu(\mu)R_v(\mu),
\]

while

\[
\Xi^{(m_\mu)}(\mu)
=
m_\mu!\,g_\mu(\mu).
\]

Divide.

**Standing:** PROVED.

---

## ZW2-T4 — Weighted near next-jet representation

Substituting ZW2-T3 into the near field gives

\[
\boxed{
\mathcal N_{v,R}[\psi]
=
\sum_{\substack{\mu\notin F\\
|\Im\mu-T_F|<R}}
m_\mu\psi(\mu)
\frac{
H_v^{(m_\mu)}(\mu)
}{
\Xi^{(m_\mu)}(\mu)
}.
}
\]

Thus the residual negative-branch arithmetic object is precisely a weighted complementary next-jet field.

**Standing:** PROVED.

### Near-collision warning

If a simple complementary zero approaches a selected point,

\[
\mu=\rho_j+\delta,
\]

then

\[
R_v(\mu)
=
\frac{v_j}{\delta}
+
O(1).
\]

The entire lift \(H_v\) remains regular; the large response is encoded by the reciprocal local metric

\[
\frac1{\Xi'(\mu)}
\]

or its multiplicity-\(m\) analogue.

Nothing in the abstract persistence calculus excludes this geometry.

---

# 5. Explicit-formula decomposition

For the fixed selected source and admissible multiplier, write the scalar explicit formula schematically as

\[
\boxed{
\mathcal C_v[\psi]
+
\mathcal N_v[\psi]
+
\mathcal F_v[\psi]
=
\mathcal P_v[\psi]
+
\mathcal A_v[\psi].
}
\]

Here:

- \(\mathcal C_v\) is the selected contracted-residue term;
- \(\mathcal N_v\) is the finite/intermediate complementary divisor term;
- \(\mathcal F_v\) is the distant complementary divisor term;
- \(\mathcal P_v\) is the prime-power term;
- \(\mathcal A_v\) is the archimedean/pole term.

For a selected-preserving multiplier,

\[
\mathcal C_v[\psi]=0,
\]

so

\[
\boxed{
\mathcal N_v[\psi]
+
\mathcal F_v[\psi]
=
\mathcal P_v[\psi]
+
\mathcal A_v[\psi].
}
\]

**Standing:** retained exact explicit-formula decomposition.

---

## ZW2-T5 — Adaptive co-cancellation identity

Suppose a selected-preserving multiplier is additionally chosen to satisfy

\[
\mathcal N_v[\psi]
=
\mathcal A_v[\psi].
\]

Then the explicit formula forces

\[
\boxed{
\mathcal P_v[\psi]
=
\mathcal F_v[\psi].
}
\]

Hence an adaptive multiplier that annihilates the near-minus-archimedean response cannot simultaneously leave an independent prime lower bound: the prime term collapses onto the far tail.

By ZW2-T2, for a far cutoff sent outward,

\[
\mathcal F_{v,R}[\psi]\to0.
\]

**Standing:** PROVED algebraically from the explicit-formula identity.

### Interpretation

\[
\boxed{
\text{adaptive near cancellation}
\ne
\text{independent prime detection}.
}
\]

The multiplier must be chosen independently of the unknown near field if the prime signal is to carry separate information.

---

# 6. Negative-branch theorem boundary

Combining H1-P1, H1-P2.1, and ZW2-T1–T5 yields the lawful chain

\[
\boxed{
\begin{aligned}
\text{persistent selected negative ray}
&\Longrightarrow
v\ne0,\ \mathbf1^Tv=0\\
&\Longrightarrow
R_v(z)=O(|z|^{-2})\\
&\Longrightarrow
\mathcal F_{v,R}[\psi]\to0\\
&\Longrightarrow
\text{finite/intermediate complementary field}\\
&\Longrightarrow
\mathcal N_{v,R}[\psi]
=
\sum_{\mu}^{\rm near}
m_\mu\psi(\mu)
\frac{H_v^{(m_\mu)}(\mu)}
{\Xi^{(m_\mu)}(\mu)}.
\end{aligned}
}
\]

This chain is a theorem/reduction package.

The next statement is **not** in the package:

> the actual zeta divisor cannot realize such a weighted near field.

That is exactly the downstream interface

\[
\boxed{
\texttt{AZ-NEXTJET-LOC}
}
\]

or an equivalent actual-zeta KPH/transversality floor.

---

# Part II — Neutral branch

## 7. Compact-window geometric explicit formula

Let \(f\) be supported in

\[
[-c,c],
\]

and let

\[
F=\widehat f.
\]

The compact-window Weil form has the geometric representation

\[
\boxed{
Q_c(f)
=
2|F(i/2)|^2
+
\frac1{2\pi}
\int_{\mathbb R}
|F(t)|^2
\Psi_c(t)\,dt,
}
\]

with

\[
\boxed{
\Psi_c(t)
=
\Re\psi\!\left(
\frac14+\frac{it}{2}
\right)
-\log\pi
-
\sum_{\log n<2c}
\frac{2\Lambda(n)}{\sqrt n}
\cos(t\log n).
}
\]

At fixed \(c\), only finitely many prime powers satisfy

\[
\log n<2c.
\]

**Standing:** IMPORTED compact-window explicit-formula identity / specialization. The current compact-window literature explicitly works with this finite-support arithmetic truncation. 

---

## ZW2-T6 — Finite prime-support theorem

For every fixed support \(c<\infty\),

\[
\boxed{
\#\{n=p^m:\log n<2c\}<\infty.
}
\]

Hence the prime contribution to the compact-window Weil operator is a finite trigonometric polynomial in Fourier space and a finite sum of translations in physical space.

Moreover, because the threshold set

\[
\left\{
\frac12\log n:
n=p^m
\right\}
\]

is discrete, there exists a right neighborhood of \(c\) on which the active prime-power set is unchanged, except when \(c\) itself is a threshold, in which case one finite threshold event occurs before the set again stabilizes.

**Standing:** PROVED from support truncation + discreteness of prime powers.

---

# 8. Physical operator form

Multiplication by

\[
\cos(t\log n)
\]

in Fourier space corresponds, under the project Fourier convention, to the symmetric translation

\[
\frac12
\left(
\tau_{\log n}
+
\tau_{-\log n}
\right)
\]

in physical space.

Define the archimedean multiplier

\[
\widehat{\mathcal A_\infty f}(t)
=
\left[
\Re\psi\!\left(
\frac14+\frac{it}{2}
\right)
-\log\pi
\right]
\widehat f(t).
\]

Let \(\mathcal R_{\rm pole}\) denote the finite-rank pole/evaluation contribution.

Then, up to the fixed Fourier-normalization convention already encoded in \(Q_c\),

\[
\boxed{
\mathcal W_c
=
\mathcal A_\infty
-
\sum_{\log n<2c}
\frac{\Lambda(n)}{\sqrt n}
\left(
\tau_{\log n}
+
\tau_{-\log n}
\right)
+
\mathcal R_{\rm pole}.
}
\]

**Standing:** DERIVED from the compact-window geometric formula.

---

# 9. Logarithmic principal order

The digamma asymptotic gives

\[
\Re\psi\!\left(
\frac14+\frac{it}{2}
\right)
=
\log|t|
+
O(1)
\qquad(|t|\to\infty).
\]

The prime trigonometric polynomial is bounded because it contains finitely many terms.

Therefore

\[
\boxed{
\Psi_c(t)
=
\log|t|
+
O_c(1).
}
\]

---

## ZW2-T7 — Logarithmic form-domain theorem

There exist constants

\[
A_c,B_c>0
\]

and \(C_c\in\mathbb R\) such that

\[
\boxed{
A_c
\int_{\mathbb R}
\log(e+|t|)
|F(t)|^2\,dt
\le
Q_c(f)+C_c\|f\|_2^2
}
\]

and

\[
\boxed{
Q_c(f)+C_c\|f\|_2^2
\le
B_c
\int_{\mathbb R}
\log(e+|t|)
|F(t)|^2\,dt.
}
\]

Thus the natural compact-window form domain is a logarithmic Fourier/Sobolev space.

**Standing:** DERIVED from ZW2-T6 + digamma asymptotics + boundedness of the finite-rank pole term.

### Consequence

The finite arithmetic translations do not increase the principal regularity order.

They preserve every ordinary Sobolev scale and every logarithmic Fourier scale.

Therefore

\[
\boxed{
\text{finite prime translations}
\not\Rightarrow
H^\varepsilon\text{ regularity gain}
}
\]

for any \(\varepsilon>0\).

---

## ZW2-T8 — No automatic quasianalytic bootstrap

The compact-window explicit formula supplies logarithmic-frequency control, but does not by itself imply

\[
|D|^\varepsilon f\in L^2
\]

for any \(\varepsilon>0\).

Repeated substitution of the finite translation equation does not alter this conclusion: translations are order-zero operators and do not create smoothing.

**Standing:** PROVED as an operator-order consequence of ZW2-T7.

---

# 10. Neutral null modes

Suppose the compact-window defect operator is nonnegative:

\[
W_c\succeq0.
\]

If a physical vector \(k\) satisfies

\[
Q_c(k)=0,
\]

then positivity gives

\[
\boxed{
W_ck=0
}
\]

in the corresponding operator/form sense.

This null-mode step is abstract positive-operator geometry.

What ZW-2 adds is the concrete operator species:

\[
\boxed{
\text{archimedean log multiplier}
+
\text{finite prime translations}
+
\text{finite-rank pole term}.
}
\]

---

## ZW2-T9 — Neutrality is global, not termwise

The equality

\[
Q_c(k)=0
\]

does **not** imply separately that

\[
F(i/2)=0
\]

or that each pointwise integrand contribution vanishes.

The symbol

\[
\Psi_c(t)
\]

need not be pointwise nonnegative because the finite prime trigonometric polynomial can change its sign contribution.

Thus neutral equality is one global quadratic cancellation.

**Standing:** SCOPE/LOGICAL CONSEQUENCE of the geometric formula.

---

# 11. Neutral-branch theorem boundary

Let \(\widetilde k\) be the zero extension of a compact-window neutral mode.

The explicit operator is

\[
\boxed{
\mathcal W_c^{\rm ext}
=
\mathcal A_\infty
-
\sum_{\log n<2c}
\frac{\Lambda(n)}{\sqrt n}
\left(
\tau_{\log n}
+
\tau_{-\log n}
\right)
+
\mathcal R_{\rm pole}.
}
\]

The arithmetic theorem package determines its order and finite translation structure.

What it does **not** determine is whether

\[
\mathcal W_c^{\rm ext}\widetilde k
\]

must vanish on a nontrivial exterior collar, or whether the finite arithmetic shifts can cancel the exterior archimedean tail.

That is exactly the downstream interface

\[
\boxed{
\texttt{AZ-FIN-WEIL-NULL-EXTENSION}.
}
\]

---

# 12. H1-P2.2 determination

The explicit-formula attachment is now normalized.

## Negative branch

Established:

\[
\boxed{
\begin{aligned}
\mathbf1^Tv=0
&\Longrightarrow
R_v(z)=O(z^{-2})\\
&\Longrightarrow
\mathcal F_{v,R}=O((\log R)/R)\\
&\Longrightarrow
\text{near-field localization}\\
&\Longrightarrow
\text{weighted completed-}\Xi\text{ next jet}.
\end{aligned}
}
\]

Adaptive cancellation cannot produce an independent prime signal because the exact explicit formula co-adapts.

The first unproved statement is actual-zeta control/exclusion of that near next-jet field.

## Neutral branch

Established:

\[
\boxed{
\text{fixed support}
\Longrightarrow
\text{finitely many prime translations},
}
\]

and

\[
\boxed{
\Psi_c(t)=\log|t|+O_c(1).
}
\]

Hence the operator is logarithmic order with only bounded/order-zero arithmetic translations.

There is no free quasianalytic bootstrap.

The first unproved statement is the null-extension/support-rigidity interface.

---

# H1-P2 completion status

H1-P2 now has:

1. H1-P2.0 — specialization map;
2. H1-P2.1 — quartet channel and residue structure;
3. H1-P2.2 — explicit-formula arithmetic attachment.

The remaining question is whether another internal zeta-Weil normalization pass is needed before morphology packaging.

The theorem inventory indicates that the required specialization outputs have now all been normalized.

Therefore:

\[
\boxed{
\textbf{H1-P2 — ZETA-WEIL SPECIALIZATION: COMPLETE.}
}
\]

---

# Next cursor

\[
\boxed{
\texttt{H1-P3.0 / NEGATIVE DEFECT MORPHOLOGY THEOREM}
}
\]

H1-P3 should no longer discover ingredients.

It should package the already established chains into exact morphology theorems, starting with the negative branch and terminating explicitly at

\[
\texttt{AZ-NEXTJET-LOC}
\]

without attempting to solve that interface.
