# Neutral Defect Morphology Theorem
## H1-P3.1 — Attained critical branch and compact-window null mode

This document packages the neutral branch of the completed H1-P1/H1-P2 theory.

It does **not** prove that a nonzero neutral mode persists to a larger support.

The theorem stops at the Horizon-1 interface

\[
\boxed{
\texttt{AZ-FIN-WEIL-NULL-EXTENSION}.
}
\]

---

# 1. Critical right-approach and branch selection

Fix a finite selected packet

\[
\Pi
\]

with finite negative coefficient sector

\[
M_\Pi.
\]

Let

\[
\mathcal A_{\Pi,t}
\]

be the monotone selected analysis-space filtration and let

\[
t_n\downarrow c.
\]

Suppose

\[
y_n=(a_n,u_n)\in\mathcal A_{\Pi,t_n},
\qquad
\|y_n\|=1,
\]

with

\[
\boxed{
[y_n,y_n]_J\to0.
}
\]

Because \(M_\Pi\) is finite dimensional, WD-C4 gives a nonzero right-limit vector

\[
y=(a,u)\in\mathcal A_{\Pi,c+}
\]

with

\[
[y,y]_J\le0.
\]

There are exactly two fixed-packet possibilities.

### Negative fall-through

If positive coefficient norm is lost in the weak limit, then

\[
[y,y]_J<0.
\]

That branch is already covered by H1-P3.0.

### Attained neutral branch

If

\[
\|a\|^2=\frac12,
\]

then

\[
[y,y]_J=0,
\]

and

\[
y_n\to y
\]

strongly.

Only this second alternative enters H1-P3.1.

---

## P3-U1 — Fixed-packet critical dichotomy

For a fixed finite selected packet,

\[
\boxed{
\text{critical right-approach}
\Longrightarrow
\begin{cases}
\text{strict negative persistent ray},\\
\text{attained nonzero neutral right-limit ray}.
\end{cases}
}
\]

There is no independent non-attained critical branch.

**Dependencies:** WD-C3, WD-C4.

**Standing:** PROVED.

---

# 2. Finite-exception unit-gain neutral realization

The remainder of P3.1 concerns the retained finite-exception neutral branch.

Assume the attained neutral coefficient vector is represented by a nonzero finite selected coordinate

\[
u
\]

and an endpoint minimum-compensator map

\[
C_c
\]

satisfying the unit-gain relation

\[
\boxed{
C_c^*C_cu=u.
}
\]

Then

\[
\boxed{
\|C_cu\|=\|u\|.
}
\]

Assume further that the neutral positive coordinate has a physical adjoint realization: there exists a physical vector \(k\ne0\) such that

\[
\boxed{
C_cu=P_c^*k.
}
\]

Define the negative physical synthesis by

\[
\boxed{
N_c=-P_cC_c.
}
\]

These are the finite-exception neutral hypotheses inherited from the endpoint reduction.

They are not consequences of abstract criticality alone.

---

# 3. Exact null-mode identity

From

\[
C_cu=P_c^*k
\]

and

\[
C_c^*C_cu=u,
\]

we get

\[
N_c^*k
=
-C_c^*P_c^*k
=
-C_c^*C_cu
=
-u.
\]

Hence the fixed coefficient relation is

\[
\boxed{
\Phi(u)
=
(P_c^*k,-N_c^*k)
=
(C_cu,u).
}
\]

Define the finite-exception physical Weil defect operator

\[
\boxed{
W_c
=
P_cP_c^*
-
N_cN_c^*.
}
\]

Then

\[
\begin{aligned}
W_ck
&=
P_cP_c^*k-N_cN_c^*k\\
&=
P_cC_cu-N_c(-u)\\
&=
P_cC_cu+N_cu\\
&=
0.
\end{aligned}
\]

Thus

\[
\boxed{
W_ck=0.
}
\]

---

## P3-U2 — Physical neutral null-mode theorem

Every finite-exception unit-gain neutral relation satisfying the physical adjoint realization above determines a nonzero physical null mode

\[
\boxed{
k\ne0,
\qquad
W_ck=0.
}
\]

**Standing:** PROVED CONDITIONAL on the finite-exception unit-gain realization.

### Interpretation

The neutral obstruction is not merely a coefficient-space equality.

It is an actual compact-window Weil null mode.

---

# 4. Compact-window arithmetic representation

For a test function \(f\) supported in

\[
[-c,c],
\]

with Fourier transform

\[
F=\widehat f,
\]

the compact-window Weil form has the geometric representation

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

where

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

At fixed support, the prime-power sum is finite.

In physical coordinates, up to the fixed Fourier-normalization convention, the corresponding whole-line operator species is

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

Here:

- \(\mathcal A_\infty\) is the archimedean nonlocal Fourier multiplier;
- the prime part is a finite sum of symmetric translations;
- \(\mathcal R_{\rm pole}\) is finite rank.

---

## P3-U3 — Finite arithmetic-shift theorem

At every fixed compact support \(c\),

\[
\boxed{
\text{the arithmetic part contains only finitely many prime-power translations}.
}
\]

The active prime set is locally constant under a sufficiently small right variation of \(c\), except at a discrete prime-power threshold, where only a finite threshold event occurs.

**Dependencies:** ZW2-T6.

**Standing:** PROVED from the compact-window support truncation.

### Consequence

Neutral persistence is not driven by an infinite local cascade of newly activated primes.

The infinite-order part is archimedean.

---

# 5. Logarithmic principal order

The digamma asymptotic gives

\[
\Re\psi\!\left(
\frac14+\frac{it}{2}
\right)
=
\log|t|
+
O(1).
\]

Because the prime sum is finite and bounded in \(t\),

\[
\boxed{
\Psi_c(t)
=
\log|t|
+
O_c(1).
}
\]

Consequently, after adding a sufficiently large harmless \(L^2\) shift,

\[
\boxed{
Q_c(f)+C_c^{(0)}\|f\|_2^2
\asymp_c
\int_{\mathbb R}
\log(e+|t|)
|F(t)|^2\,dt.
}
\]

The superscript on \(C_c^{(0)}\) distinguishes this scalar shift from the compensator map \(C_c\).

---

## P3-U4 — Logarithmic-order neutral carrier theorem

The physical neutral mode belongs naturally to a logarithmic Fourier/form domain.

The explicit-formula operator has principal order

\[
\boxed{
\log|D|,
}
\]

perturbed only by order-zero finite translations and a finite-rank term.

**Dependencies:** ZW2-T7.

**Standing:** DERIVED CONDITIONAL on the neutral-mode setup.

---

# 6. No automatic regularity bootstrap

Translations preserve ordinary Sobolev and logarithmic Fourier norms:

\[
\|\tau_af\|_{H^s}
=
\|f\|_{H^s}.
\]

Thus the finite prime-delay operator does not increase differential order.

The compact-window neutral equation therefore does not, from the retained inputs alone, imply

\[
|D|^\varepsilon k\in L^2
\]

for any

\[
\varepsilon>0.
\]

Repeated substitution only creates further translated copies at the same order.

---

## P3-U5 — No free quasianalyticity theorem

The neutral equation supplies logarithmic regularity but no automatic positive-Sobolev or quasianalytic bootstrap.

\[
\boxed{
\text{finite prime translations}
+
\log|D|
\not\Rightarrow
H^\varepsilon
}
\]

without an additional theorem.

**Dependencies:** ZW2-T8.

**Standing:** PROVED as an operator-order statement.

---

# 7. Neutrality is global

The null equality

\[
Q_c(k)=0
\]

does not imply that the terms in the geometric explicit formula vanish separately.

In particular, it does not imply individually that

\[
F(i/2)=0
\]

or that

\[
\Psi_c(t)|F(t)|^2=0
\]

pointwise.

The prime trigonometric polynomial can make

\[
\Psi_c
\]

sign-indefinite.

Thus the neutral mode is one global cancellation of the whole compact-window Weil form.

---

## P3-U6 — Global-cancellation scope theorem

Neutrality supplies

\[
\boxed{
W_ck=0,
}
\]

but does not split into termwise prime, pole, and archimedean vanishing.

**Dependencies:** ZW2-T9.

**Standing:** SCOPE/LOGICAL CONSEQUENCE.

---

# 8. Fixed-vector persistence problem

Let

\[
\widetilde k
\]

denote the zero extension of \(k\) outside

\[
[-c,c].
\]

The endpoint null-mode identity gives the interior equation

\[
\boxed{
P_{[-c,c]}
\mathcal W_c^{\rm ext}
\widetilde k
=
0
}
\]

in the retained operator/form realization.

The finite-exception MTP-2 question is not whether an approximate endpoint relation exists.

The fixed vector already exists.

The question is whether the **same fixed neutral relation** persists on a strictly larger interval.

Equivalently, one asks whether the exterior Weil output

\[
\mathcal W_c^{\rm ext}\widetilde k
\]

vanishes on a nontrivial collar adjacent to the support boundary, subject to the unit-gain/self-duality constraints above.

Away from a prime-power threshold, the active finite translation operator is locally unchanged.

At a threshold, the right enlargement introduces only the corresponding finite new arithmetic term before the active set stabilizes again.

Thus the problem remains a finite-delay support question.

---

## P3-U7 — Neutral null-extension reduction

Every finite-exception unit-gain neutral branch reduces to the following support problem:

\[
\boxed{
P_{[-c,c]}
\mathcal W_c^{\rm ext}\widetilde k=0,
\qquad
k\ne0,
}
\]

with

\[
\mathcal W_c^{\rm ext}
=
\text{logarithmic-order archimedean operator}
+
\text{finitely many arithmetic translations}
+
\text{finite-rank pole term}.
\]

Exact persistence to a larger support requires a nontrivial exterior collar on which the corresponding global Weil output continues to vanish, with the finite threshold convention included when necessary.

**Standing:** DERIVED CONDITIONAL on P3-U2.

---

# 9. What P3-U7 does not say

P3-U7 is a reduction theorem.

It does **not** assert that a nonzero neutral mode has such an exterior collar.

It does **not** assert that immediate exterior activation is forced.

It does **not** import a generic logarithmic-Laplacian unique-continuation theorem for the full shifted operator.

It does **not** infer persistence from:

- logarithmic form regularity;
- finite prime shifts;
- finite-dimensionality of the neutral selected space;
- smoothness or flatness of an auxiliary representation;
- ordinary frame or Picard closure.

Those questions belong downstream.

---

# 10. Neutral Defect Morphology Theorem

Collecting P3-U1 through P3-U7:

## H1-P3.1 Neutral Defect Morphology Theorem

Assume:

1. \(\Pi\) is a fixed finite selected packet;
2. \(t_n\downarrow c\);
3. \(y_n\in\mathcal A_{\Pi,t_n}\) are unit critical vectors with
   \[
   [y_n,y_n]_J\to0;
   \]
4. the fixed-packet critical limit falls in the attained-neutral rather than positive-mass-loss alternative;
5. the resulting nonzero neutral selected coordinate \(u\) has the finite-exception unit-gain realization
   \[
   C_c^*C_cu=u;
   \]
6. there exists \(k\ne0\) with
   \[
   C_cu=P_c^*k;
   \]
7. \(N_c=-P_cC_c\).

Then:

### Attained neutral geometry

The critical sequence converges strongly to a nonzero neutral right-limit vector.

### Physical null mode

\[
\boxed{
W_ck=0,
\qquad
W_c=P_cP_c^*-N_cN_c^*.
}
\]

### Arithmetic operator species

The corresponding compact-window Weil operator is a logarithmic-order nonlocal archimedean operator plus finitely many prime-power translations and a finite-rank pole term.

### Form order

\[
\boxed{
\Psi_c(t)=\log|t|+O_c(1).
}
\]

Its natural form domain is logarithmic rather than positive-Sobolev.

### Rigidity limit

Neither the null equality nor the finite translation structure supplies a free quasianalytic/positive-Sobolev continuation theorem.

### Persistence reduction

The remaining fixed-vector question is exactly whether the zero-extended neutral mode can satisfy the same global Weil equation on a nontrivial exterior collar.

---

# 11. Exact stop line

The theorem package ends at

\[
\boxed{
\texttt{AZ-FIN-WEIL-NULL-EXTENSION}.
}
\]

The interface asks:

> For an actual nonzero finite-exception unit-gain neutral mode \(k\) with
>
> \[
> P_{[-c,c]}
> \mathcal W_c^{\rm ext}\widetilde k
> =
> 0,
> \]
>
> must
>
> \[
> \mathcal W_c^{\rm ext}\widetilde k
> \]
>
> vanish on a nontrivial exterior collar, or can it activate immediately outside the old support?

The answer is not assumed in H1-P3.1.

---

# 12. Dependency chain

The neutral morphology theorem consumes

\[
\boxed{
\begin{array}{c}
\text{WD-C4 / attained critical branch}\\
\downarrow\\
\text{finite-exception unit-gain realization}\\
\downarrow\\
W_ck=0\\
\downarrow\\
\text{ZW2-T6 / finite prime shifts}\\
\downarrow\\
\text{ZW2-T7 / logarithmic form order}\\
\downarrow\\
\text{ZW2-T8,T9 / no free bootstrap and global cancellation}\\
\downarrow\\
\text{null-extension support interface}.
\end{array}
}
\]

No downstream support-rigidity theorem is consumed above the stop line.

---

# H1-P3.1 determination

The neutral branch is now packaged as a single auditable morphology theorem.

Its output is:

\[
\boxed{
\text{attained fixed-packet criticality}
\Longrightarrow
\text{physical compact-window null mode}
}
\]

whose operator is

\[
\boxed{
\text{logarithmic order}
+
\text{finite arithmetic translations}
+
\text{finite-rank pole term},
}
\]

with no automatic positive-order regularity gain.

The unresolved question is purely a fixed-vector exterior support/null-extension problem.

---

# Next cursor

\[
\boxed{
\texttt{H1-P3.2 / NONCOMPACT BACKGROUND MORPHOLOGY THEOREM}
}
\]
