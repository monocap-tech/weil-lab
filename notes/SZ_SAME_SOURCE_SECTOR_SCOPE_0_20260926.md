# SZ-SAME-SOURCE-SECTOR-SCOPE-0 — C2 parity/reality normalization

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** AUDIT NORMALIZATION / RESTRICTED-SECTOR THEOREM  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Purpose:** discharge audit item C2  
**Depends on:** SZ-ZERO-SIDE-NORMALIZATION-0 and unrestricted
same-source surjectivity  
**Traversal movement:** none

## 0. Objective

The post-SZ-3 audit observed that

\[
\sigma_c:\mathcal F_c\to M_\Pi
\]

is surjective on the unrestricted complex form carrier, but warned against
silently reusing that statement after imposing parity or reality.

This note gives the exact restricted-sector version.

For a functional-equation-symmetric packet consisting of complete quartets:

\[
\boxed{
\text{surjectivity survives in every parity/reality sector,}
}
\]

but the target is the corresponding symmetry-compatible subspace of
\(M_\Pi\), not the full unreduced \(M_\Pi\).

That is the normalization needed for the same-source collar correction.

---

## 1. Symmetric selected packet

Assume \(\Pi\) is closed under the full zeta quartet symmetry.

For one simple quartet write its Bombieri ordinates as

\[
\gamma_+=T+i\delta,
\qquad
\bar\gamma_+=T-i\delta,
\]

\[
\gamma_-=-T+i\delta=-\bar\gamma_+,
\qquad
\bar\gamma_-=-T-i\delta=-\gamma_+.
\]

Functional-equation/conjugation symmetry preserves multiplicity, so the
normalized coordinates of SZ-ZERO-SIDE-NORMALIZATION-0 have equal
multiplicity weight throughout the quartet.

Let

\[
n_+,
\qquad
n_-
\]

be the two normalized negative pair coordinates:

\[
n_+
=
\frac{
w_{\gamma_+}-w_{\bar\gamma_+}
}{\sqrt2},
\]

\[
n_-
=
\frac{
w_{\gamma_-}-w_{\bar\gamma_-}
}{\sqrt2}.
\]

Before parity reduction, one simple quartet therefore contributes the complex
two-space

\[
\mathbb C n_+\oplus\mathbb C n_-.
\]

---

## 2. Physical parity and its coefficient action

Let

\[
(\mathsf P f)(x):=f(-x).
\]

Under the fixed Fourier convention

\[
\widehat f(z)
=
\int f(x)e^{izx}\,dx,
\]

we have

\[
\boxed{
\widehat{\mathsf P f}(z)
=
\widehat f(-z).
}
\]

On the negative pair coordinates of one quartet this gives

\[
\boxed{
\mathsf P_M(n_+,n_-)
=
(-n_-,-n_+).
}
\]

Indeed,

\[
-\gamma_+=\bar\gamma_-,
\qquad
-\bar\gamma_+=\gamma_-.
\]

Thus \(\mathsf P_M\) is a unitary involution on the quartet negative space.

For a complete selected packet, take the orthogonal direct sum of these
quartet involutions.

The selected-coordinate map is equivariant:

\[
\boxed{
\sigma_c(\mathsf P f)
=
\mathsf P_M\sigma_c(f).
}
\]

---

## 3. Complex parity sectors

Let

\[
\varepsilon\in\{+1,-1\},
\]

with

\[
\mathcal F_c^\varepsilon
:=
\{f\in\mathcal F_c:\mathsf P f=\varepsilon f\}.
\]

Define the coefficient parity sector

\[
\boxed{
M_\Pi^\varepsilon
:=
\{u\in M_\Pi:\mathsf P_Mu=\varepsilon u\}.
}
\]

For one quartet,

\[
\mathsf P_M(u_+,u_-)
=
(-u_-,-u_+),
\]

so

\[
\boxed{
u_-
=
-\varepsilon u_+.
}
\]

Hence each simple quartet contributes one complex negative coordinate after
parity reduction.

In particular:

- even sector \((\varepsilon=+1)\):
  \[
  u_-=-u_+;
  \]
- odd sector \((\varepsilon=-1)\):
  \[
  u_-=u_+.
  \]

Thus for \(q\) simple selected quartets,

\[
\boxed{
\dim_{\mathbb C}M_\Pi^\varepsilon=q,
}
\]

whereas the unreduced packet has complex dimension \(2q\).

---

## 4. Surjectivity in a complex parity sector

The unrestricted same-source theorem gives surjectivity already on the
regular core:

\[
\sigma_c:
C_c^\infty(-c,c)
\twoheadrightarrow
M_\Pi.
\]

Take

\[
u\in M_\Pi^\varepsilon.
\]

Choose

\[
f\in C_c^\infty(-c,c)
\]

with

\[
\sigma_c(f)=u.
\]

Define the parity projection

\[
f_\varepsilon
:=
\frac12
\left(
f+\varepsilon\mathsf P f
\right).
\]

Then

\[
f_\varepsilon\in
C_c^\infty(-c,c)\cap\mathcal F_c^\varepsilon
\]

and equivariance gives

\[
\begin{aligned}
\sigma_c(f_\varepsilon)
&=
\frac12
\left(
u+\varepsilon\mathsf P_Mu
\right)\\
&=
\frac12
\left(
u+\varepsilon^2u
\right)\\
&=
u.
\end{aligned}
\]

Therefore

\[
\boxed{
\sigma_c:
\mathcal F_c^\varepsilon
\twoheadrightarrow
M_\Pi^\varepsilon.
}
\]

No new finite-exponential-independence theorem is needed beyond the
unrestricted surjectivity already proved.

---

## 5. Physical reality and its coefficient action

Let

\[
(\mathsf C f)(x)
:=
\overline{f(x)}.
\]

Then

\[
\boxed{
\widehat{\mathsf C f}(z)
=
\overline{
\widehat f(-\bar z)
}.
}
\]

On one quartet's negative coordinates,

\[
\boxed{
\mathsf C_M(u_+,u_-)
=
(\overline{u_-},\overline{u_+}).
}
\]

This is an antiunitary involution.

The selected-coordinate map is equivariant in the real-linear sense:

\[
\boxed{
\sigma_c(\mathsf C f)
=
\mathsf C_M\sigma_c(f).
}
\]

Define the real coefficient form

\[
\boxed{
M_\Pi^{\mathbb R}
:=
\operatorname{Fix}(\mathsf C_M).
}
\]

For one quartet this is exactly

\[
\boxed{
u_-=\overline{u_+}.
}
\]

It has real dimension two per quartet.

---

## 6. Surjectivity on the real carrier

Let

\[
\mathcal F_c^{\mathbb R}
:=
\{f\in\mathcal F_c:\mathsf C f=f\}.
\]

Take

\[
u\in M_\Pi^{\mathbb R}.
\]

Choose complex \(f\) with

\[
\sigma_c(f)=u.
\]

Realify:

\[
f_{\mathbb R}
:=
\frac12
(f+\mathsf C f).
\]

Then

\[
f_{\mathbb R}\in\mathcal F_c^{\mathbb R}
\]

and

\[
\begin{aligned}
\sigma_c(f_{\mathbb R})
&=
\frac12
\left(
u+\mathsf C_Mu
\right)\\
&=
u.
\end{aligned}
\]

Hence, as a real-linear map,

\[
\boxed{
\sigma_c:
\mathcal F_c^{\mathbb R}
\twoheadrightarrow
M_\Pi^{\mathbb R}.
}
\]

---

## 7. Real parity sectors

Parity and reality commute on the physical carrier:

\[
\mathsf P\mathsf C
=
\mathsf C\mathsf P.
\]

Their induced coefficient involutions commute as well.

Define

\[
\mathcal F_c^{\varepsilon,\mathbb R}
:=
\mathcal F_c^\varepsilon
\cap
\mathcal F_c^{\mathbb R},
\]

and

\[
M_\Pi^{\varepsilon,\mathbb R}
:=
M_\Pi^\varepsilon
\cap
M_\Pi^{\mathbb R}.
\]

For one quartet,

\[
u_-=-\varepsilon u_+,
\]

and

\[
u_-=\overline{u_+}.
\]

Therefore

\[
\boxed{
\overline{u_+}
=
-\varepsilon u_+.
}
\]

So:

### Real even sector

For

\[
\varepsilon=+1,
\]

\[
\boxed{
u_+\in i\mathbb R,
\qquad
u_-=-u_+.
}
\]

### Real odd sector

For

\[
\varepsilon=-1,
\]

\[
\boxed{
u_+\in\mathbb R,
\qquad
u_-=u_+.
}
\]

Thus each simple quartet contributes exactly one **real** selected negative
coordinate in each real parity sector.

For \(q\) selected quartets,

\[
\boxed{
\dim_{\mathbb R}
M_\Pi^{\varepsilon,\mathbb R}
=
q.
}
\]

---

## 8. Surjectivity on a real parity sector

Take

\[
u\in M_\Pi^{\varepsilon,\mathbb R}.
\]

Choose \(f\) with

\[
\sigma_c(f)=u.
\]

Apply the commuting symmetry projections:

\[
\boxed{
f_{\varepsilon,\mathbb R}
=
\frac14
(I+\mathsf C)
(I+\varepsilon\mathsf P)
f.
}
\]

Then

\[
f_{\varepsilon,\mathbb R}
\in
\mathcal F_c^{\varepsilon,\mathbb R},
\]

and equivariance gives

\[
\boxed{
\sigma_c(f_{\varepsilon,\mathbb R})
=
u.
}
\]

Therefore, as a real-linear map,

\[
\boxed{
\sigma_c:
\mathcal F_c^{\varepsilon,\mathbb R}
\twoheadrightarrow
M_\Pi^{\varepsilon,\mathbb R}.
}
\]

This is the exact restricted-sector form of the same-source surjectivity
theorem.

---

## 9. Sector-specific old-domain correction

Fix

\[
0<c<b.
\]

Zero extension commutes with parity and reality.

Let \(S\) denote any one of the four carriers:

- unrestricted complex;
- complex parity \(\varepsilon\);
- real;
- real parity \((\varepsilon,\mathbb R)\).

Let \(M_\Pi^S\) be its corresponding symmetry-compatible selected target.

For

\[
h\in\mathcal F_b^S,
\]

we have

\[
\sigma_b(h)\in M_\Pi^S.
\]

Restricted surjectivity at the old support gives

\[
\phi_h\in\mathcal F_c^S
\]

such that

\[
\sigma_c(\phi_h)
=
\sigma_b(h).
\]

Then

\[
\boxed{
h^\circ
=
h-E_{c,b}\phi_h
}
\]

satisfies simultaneously

\[
\boxed{
h^\circ\in\mathcal F_b^S
}
\]

and

\[
\boxed{
\sigma_b(h^\circ)=0.
}
\]

Thus the old-domain correction theorem preserves every symmetry sector once
the target is typed correctly.

---

## 10. Leakage can be tested in the endpoint symmetry sector

Suppose the endpoint neutral mode \(k\) lies in a parity sector

\[
\mathsf Pk=\varepsilon k.
\]

The Weil form is parity invariant.

Hence if \(h\) has opposite parity,

\[
q_b(Ek,h)=0.
\]

Therefore a nonzero cross functional against \(Ek\) is already detected on
the same parity sector.

For reality, assume

\[
\mathsf Ck=k.
\]

If

\[
q_b(Ek,h)\ne0,
\]

choose a unit phase \(\omega\) so that

\[
q_b(Ek,\omega h)\in\mathbb R\setminus\{0\}.
\]

Then the realification

\[
h_{\mathbb R}
=
\frac12
\left(
\omega h+\mathsf C(\omega h)
\right)
\]

satisfies

\[
\boxed{
q_b(Ek,h_{\mathbb R})
=
q_b(Ek,\omega h)\ne0.
}
\]

Combining with parity projection shows that when \(k\) is real and has parity
\(\varepsilon\), any nonzero collar leakage is detectable in

\[
\boxed{
\mathcal F_b^{\varepsilon,\mathbb R}.
}
\]

So the same-source perturbation may be constructed without leaving the
physical symmetry sector of the endpoint mode.

---

## 11. Exact scope correction to the earlier same-source note

The unrestricted statement

\[
\sigma_c(\mathcal F_c)=M_\Pi
\]

remains correct.

After restricting the physical carrier, the correct statement is **not**

\[
\sigma_c(\mathcal F_c^S)=M_\Pi.
\]

It is

\[
\boxed{
\sigma_c(\mathcal F_c^S)=M_\Pi^S.
}
\]

In particular, for a real parity sector the full two-complex-dimensional
negative coordinate of each quartet is reduced to one real degree of freedom.

This is the scope correction required by audit item C2.

---

## 12. Non-symmetric selected packets

The preceding theorem requires that the selected packet be invariant under
the physical symmetries being imposed.

If \(\Pi\) contains only part of a functional-equation quartet, then

\[
\mathsf P_M
\]

or

\[
\mathsf C_M
\]

need not preserve \(M_\Pi\).

In that case there is no canonical parity/reality-restricted surjectivity
statement onto the same selected packet.

The correct options are:

1. enlarge \(\Pi\) to its symmetry closure; or
2. remain on the unrestricted complex carrier.

No partial-packet sector theorem is asserted here.

The Horizon-1 quartet packets are symmetry-closed, so this limitation does
not affect the intended fixed-quartet applications.

---

## 13. Consequence for same-source custody

For a symmetry-closed packet and an endpoint neutral mode in sector \(S\),

\[
\boxed{
\Lambda_{c,b;k}\ne0
}
\]

implies there exists a leaking direction

\[
h^\circ\in
\ker\sigma_b
\cap
\mathcal F_b^S.
\]

Therefore the strict-support negative perturbation can be chosen in the same
sector while retaining exactly the endpoint selected coordinate

\[
u\in M_\Pi^S.
\]

Thus the same-source theorem survives parity/reality reduction.

As before, this is source custody only.

It does **not** imply selected sign ownership without the pointwise background
test.

---

## 14. Audit determination

Audit item C2 is discharged.

The exact sector rule is

\[
\boxed{
\text{restrict physical carrier}
\Longleftrightarrow
\text{restrict selected target to the matching symmetry eigenspace/fixed form}.
}
\]

For a complete quartet:

\[
\boxed{
\begin{array}{c|c}
\text{sector} & \text{negative coordinate relation}\\
\hline
\text{complex even} & u_-=-u_+\\
\text{complex odd} & u_-=u_+\\
\text{real} & u_-=\overline{u_+}\\
\text{real even} & u_+\in i\mathbb R,\ u_-=-u_+\\
\text{real odd} & u_+\in\mathbb R,\ u_-=u_+
\end{array}
}
\]

and \(\sigma_c\) is surjective onto each corresponding target.

The earlier same-source result may therefore be used in parity/reality sectors
provided this typed target replaces the unreduced \(M_\Pi\).

Remaining audit obligations:

- C3 — compact-collar uniformity of \(\sigma_b\) and \(G_b\);
- C4 — superflat Stieltjes example remains explicitly non-load-bearing unless
  its jump representation is expanded or source-pinned.

**No canonical cursor movement is asserted by this audit-normalization pass.**
