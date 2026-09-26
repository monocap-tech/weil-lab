# SZ-CROSS-COLLAR-SAME-SOURCE-0 — Old-domain correction theorem

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Immediate parent residue:** SZ_CHANNEL_CUSTODY_FORMDOMAIN_0_20260926.md  
**Uses:** SZ-CROSS-COLLAR-3, form-domain LOG-BESSEL residue,
WD-T20 pair diagonalization, WD-T24/25 finite exponential independence.

## 0. Objective

Let

~~~math
0\ne k\in\ker A_c,
\qquad
0<c<b,
~~~

and write

~~~math
\widetilde k=E_{c,b}k.
~~~

Assume null persistence fails:

~~~math
\Lambda_{c,b;k}\ne0.
~~~

The question is whether the negative perturbation can be chosen while keeping
the endpoint selected packet coordinate—and therefore its raw selected residue
source—exactly fixed.

The answer is yes for every fixed finite selected packet.

The key point is that the old form domain already realizes every selected
packet coordinate.

---

## 1. Selected coordinate maps on the full form domains

Fix a finite selected packet \(\Pi\) with negative coefficient space

~~~math
M_\Pi,
\qquad
\dim M_\Pi<\infty.
~~~

By the LOG-BESSEL residue, the canonical zero-coordinate map is bounded on the
closed logarithmic form domain.

Let

~~~math
\sigma_a:
\mathcal F_a
\longrightarrow
M_\Pi
~~~

denote the selected negative pair-coordinate component at support \(a\).

Zero extension preserves all selected raw zero evaluations, hence

~~~math
\boxed{
\sigma_b(E_{c,b}\phi)
=
\sigma_c(\phi)
\qquad
(\phi\in\mathcal F_c).
}
~~~

In particular,

~~~math
\boxed{
\sigma_b(\widetilde k)
=
\sigma_c(k)
=:u.
}
~~~

The fixed WD-T20 pair transform and WD-T26 residue map then identify \(u\)
with one fixed raw selected source \(v\).

---

## 2. Surjectivity of the old selected-coordinate map

We claim

~~~math
\boxed{
\sigma_c(\mathcal F_c)
=
M_\Pi.
}
~~~

It is enough to prove surjectivity on the regular core

~~~math
C_c^\infty(-c,c)
\subset
\mathcal F_c.
~~~

Suppose the image were a proper subspace of \(M_\Pi\).

Since \(M_\Pi\) is finite dimensional, there would exist

~~~math
0\ne m\in M_\Pi
~~~

orthogonal to the image:

~~~math
\langle
\sigma_c(\phi),
m
\rangle_{M_\Pi}
=
0
\qquad
\forall\phi\in C_c^\infty(-c,c).
~~~

Undo the fixed pair diagonalization.

The functional on the left becomes a finite linear combination of selected
raw zero evaluations:

~~~math
\sum_{j=1}^{N}
\alpha_j
\widehat\phi(\gamma_j)
=
0
\qquad
\forall\phi\in C_c^\infty(-c,c),
~~~

where the \(\gamma_j\) are distinct selected ordinates after the
multiplicity-null quotient.

Equivalently,

~~~math
\int_{-c}^{c}
\phi(x)
\left(
\sum_{j=1}^{N}
\alpha_j e^{-i\gamma_j x}
\right)
dx
=
0
\qquad
\forall\phi\in C_c^\infty(-c,c).
~~~

Therefore the finite exponential sum

~~~math
g_m(x)
:=
\sum_{j=1}^{N}
\alpha_j e^{-i\gamma_j x}
~~~

vanishes as a distribution, hence pointwise, on \((-c,c)\).

WD-T24/25 finite distinct-frequency independence gives

~~~math
\alpha_1=\cdots=\alpha_N=0.
~~~

Because the raw-to-pair transform is injective, this forces

~~~math
m=0,
~~~

a contradiction.

Therefore

~~~math
\boxed{
\sigma_c:
\mathcal F_c\to M_\Pi
\text{ is surjective.}
}
~~~

---

## 3. Every new direction has a selected-preserving representative

Take any

~~~math
h\in\mathcal F_b.
~~~

Its selected-coordinate variation is

~~~math
\sigma_b(h)\in M_\Pi.
~~~

By surjectivity of \(\sigma_c\), choose

~~~math
\phi_h\in\mathcal F_c
~~~

such that

~~~math
\sigma_c(\phi_h)
=
\sigma_b(h).
~~~

Define the corrected collar direction

~~~math
\boxed{
h^\circ
:=
h-E_{c,b}\phi_h.
}
~~~

Then zero-extension naturality gives

~~~math
\begin{aligned}
\sigma_b(h^\circ)
&=
\sigma_b(h)
-
\sigma_b(E\phi_h)\\
&=
\sigma_b(h)
-
\sigma_c(\phi_h)\\
&=
0.
\end{aligned}
~~~

So \(h^\circ\) is selected-preserving.

Moreover,

~~~math
[h^\circ]
=
[h]
\qquad
\text{in }
\mathcal F_b/E\mathcal F_c.
~~~

Thus every quotient collar class has a representative in
\(\ker\sigma_b\).

Equivalently,

~~~math
\boxed{
\mathcal F_b
=
E\mathcal F_c
+
\ker\sigma_b.
}
~~~

No direct-sum claim is made.

---

## 4. The cross functional is unchanged by the correction

The ratified cross functional is

~~~math
\Lambda_{c,b;k}([h])
=
q_b(\widetilde k,h).
~~~

Because \(\widetilde k\) annihilates every old direction,

~~~math
q_b(\widetilde k,E\phi_h)=0.
~~~

Hence

~~~math
\boxed{
q_b(\widetilde k,h^\circ)
=
q_b(\widetilde k,h).
}
~~~

Therefore, if

~~~math
\Lambda_{c,b;k}\ne0,
~~~

choose \(h\) with

~~~math
q_b(\widetilde k,h)\ne0.
~~~

Its corrected representative satisfies simultaneously

~~~math
\boxed{
\sigma_b(h^\circ)=0
}
~~~

and

~~~math
\boxed{
q_b(\widetilde k,h^\circ)\ne0.
}
~~~

So the selected-preserving alternative is not merely one side of a
factorization dichotomy here: for a fixed finite selected packet, it always
occurs whenever cross-collar leakage is nonzero.

---

## 5. Same-source negative perturbation

Choose a unit phase \(\omega\) such that

~~~math
\operatorname{Re}
\left(
\omega q_b(\widetilde k,h^\circ)
\right)
<0.
~~~

For sufficiently small \(t>0\),

~~~math
q_b(\widetilde k+t\omega h^\circ)
<
0.
~~~

But

~~~math
\begin{aligned}
\sigma_b(\widetilde k+t\omega h^\circ)
&=
\sigma_b(\widetilde k)
+
t\omega\sigma_b(h^\circ)\\
&=
u.
\end{aligned}
~~~

Hence

~~~math
\boxed{
\Lambda_{c,b;k}\ne0
\Longrightarrow
\exists x_b\in\mathcal F_b:
\quad
q_b(x_b)<0,
\qquad
\sigma_b(x_b)=u.
}
~~~

The negative strict-support witness can therefore be chosen with the same
selected packet coordinate as the endpoint neutral mode.

---

## 6. Raw selected residue source is also unchanged

The WD-T20 pair transform and WD-T26 raw-residue map are fixed
finite-dimensional linear maps independent of support.

Therefore

~~~math
\sigma_b(x_b)=u
~~~

implies that the associated raw selected source is exactly the endpoint source

~~~math
\boxed{
v_b=v_c=:v.
}
~~~

In particular,

~~~math
\boxed{
\mathbf 1^Tv=0.
}
~~~

The existing fixed-source arithmetic identities attached to \(v\) therefore
remain the same across the collar.

This is a source-identity statement.

It does not by itself provide a fixed negative normalized margin.

---

## 7. Quotient-coordinate interpretation

The natural quotient selected-coordinate map would be

~~~math
\bar\sigma:
\mathcal F_b/E\mathcal F_c
\longrightarrow
M_\Pi/\sigma_b(E\mathcal F_c).
~~~

But Sections 1–2 give

~~~math
\sigma_b(E\mathcal F_c)
=
\sigma_c(\mathcal F_c)
=
M_\Pi.
~~~

Therefore the quotient target is zero:

~~~math
\boxed{
M_\Pi/\sigma_b(E\mathcal F_c)
=
0.
}
~~~

So

~~~math
\boxed{
\bar\sigma=0.
}
~~~

This explains why the earlier abstract factorization alternative collapses in
the actual fixed-packet setting: there is no genuinely new selected-coordinate
class modulo old support.

All new support information lies in directions invisible to the finite
selected coordinate after an old-domain correction.

---

## 8. Relation to the rejected SZ-CROSS-COLLAR-4 inference

The old rejected inference was

~~~text
same selected coordinate + negative full Weil value
=> selected packet owns the negativity.
~~~

It remains rejected.

This pass proves the antecedent can always be arranged:

~~~math
\boxed{
\text{same selected coordinate}
+
\text{negative full Weil value}.
}
~~~

It does not change WD-T07:

~~~math
\text{full negativity}
\not\Rightarrow
\text{selected negativity}.
~~~

Selected sign ownership still requires the pointwise background test and
legitimate WD-T10 elimination.

So source identity and sign custody remain correctly separated.

---

## 9. Interaction with the collar branch classification

Combine this pass with the unratified pointwise owner taxonomy.

If the background is admissible at \(b\), then WD-T10 identifies the full
negative value with the residual selected defect.

The witness can now also be chosen with

~~~math
\boxed{
\sigma_b(x_b)=u
}
~~~

equal to the endpoint source.

Thus, in the BG-admissible branch, one obtains

~~~math
\boxed{
\text{negative residual selected defect}
+
\text{same fixed selected source}.
}
~~~

If the background is inadmissible, the same-source full negative witness still
exists, but the negative owner cannot be assigned to the selected packet.

---

## 10. What still does not follow

This pass does not establish the WD-T37 entry hypotheses.

In particular it does not prove, along \(b_n\downarrow c\),

~~~math
[z_n,z_n]_J\to-\kappa
\qquad
(\kappa>0),
~~~

nor a vanishing selected amplitude, nor representative blow-up.

The collar crossing may remain infinitesimally negative:

~~~math
\text{negative margin}\to0.
~~~

Therefore

~~~text
same-source collar negativity
~~~

is strictly weaker than the fixed-margin persistent-negative morphology.

However, arithmetic statements depending only on the fixed raw source \(v\)
may now be attached without changing sources from support to support.

---

## 11. Result of this NF pass

For every fixed finite selected packet,

~~~math
\boxed{
\sigma_c(\mathcal F_c)=M_\Pi.
}
~~~

Consequently every new-support quotient direction admits an old-domain
correction with zero selected-coordinate variation.

Therefore

~~~math
\boxed{
\Lambda_{c,b;k}\ne0
\Longrightarrow
\exists
\text{ a strict-support negative witness carrying exactly the endpoint
selected source.}
}
~~~

The same-source perturbation problem is therefore closed at the form-domain
level.

The remaining obstruction is no longer source identity.

It is quantitative: whether the same fixed source acquires enough selected
residual negative margin along a right-approaching sequence to enter WD-T37,
or whether the collar defect stays infinitesimal.

---

## 12. Candidate follow-on if ratified

~~~text
SZ-SAME-SOURCE / MARGIN LAW
~~~

A future NF should quantify the residual selected signature of these
same-source collar witnesses as \(b\downarrow c\), separating:

- fixed negative margin;
- vanishing negative margin;
- background-inadmissible supports.

**No canonical cursor movement is asserted by this residue.**
