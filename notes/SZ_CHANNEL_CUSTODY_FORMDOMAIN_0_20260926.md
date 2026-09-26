# SZ-CHANNEL-CUSTODY-FORMDOMAIN-0 — Logarithmic Bessel closure

**Date:** 2026-09-26  
**Branch:** \`sz-cross-collar\`  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** \`SZ-CROSS-COLLAR-3\`  
**Immediate parent residue:** \`SZ_PRECOND_FORM_BRIDGE_2_20260926.md\`  
**Uses:** WD-T35 logarithmic form order, EXT-3 unit-height zero counting,
H1-P2 canonical zero-coordinate decomposition.

## 0. Objective

The regular screw-carrier pass left one issue:

> Does the logarithmic closed form norm control the square-sum of the canonical
> zero evaluations strongly enough to extend positive / selected-negative /
> background-negative channel custody beyond \(H_0^1\)?

Yes.

The needed estimate is a weighted Paley-Wiener Bessel inequality:

~~~math
\boxed{
\sum_{\gamma\in\Gamma}
|F(\gamma)|^2
\le
C_a
\int_{\mathbb R}
\log(e+|t|)
|F(t)|^2\,dt,
}
~~~

for every Fourier transform \(F\) of an \(L^2\) function supported in
\([-a,a]\), with zeros counted with multiplicity in Bombieri ordinate
coordinates.

No positive Sobolev estimate is used.

---

## 1. Form-domain Paley-Wiener setting

Let

~~~math
v\in L^2(-a,a)
~~~

and zero-extend it to the line.

Write

~~~math
F(z)
=
\widehat v(z).
~~~

Then \(F\) is an entire function of exponential type at most \(a\).

The shifted compact-window Weil form controls

~~~math
\boxed{
\|F\|_{\log}^2
:=
\int_{\mathbb R}
w(t)|F(t)|^2\,dt,
\qquad
w(t):=\log(e+|t|).
}
~~~

By WD-T35, this weighted norm is equivalent, up to the fixed harmless
\(L^2\) shift and finite-rank pole term, to the closed form norm.

So it is enough to prove the zero-evaluation Bessel bound in
\(\|\cdot\|_{\log}\).

---

## 2. A rapidly decaying reproducing kernel

Choose

~~~math
\chi\in C_c^\infty(\mathbb R)
~~~

with

~~~math
\chi(\xi)=1
\qquad
(|\xi|\le a).
~~~

Let

~~~math
K(z)
=
\frac1{2\pi}
\int_{\mathbb R}
\chi(\xi)e^{-i\xi z}\,d\xi.
~~~

Since the inverse Fourier transform of \(F\) is supported in \([-a,a]\),

~~~math
\boxed{
F(z)
=
\int_{\mathbb R}
F(t)K(z-t)\,dt.
}
~~~

For every fixed strip width \(Y>0\) and every integer \(N\ge1\), repeated
integration by parts in \(\xi\) gives

~~~math
\boxed{
|K(x+iy)|
\le
C_{a,Y,N}
(1+|x|)^{-N}
\qquad
(|y|\le Y).
}
~~~

We will use \(Y=1/2\), which contains all zeta ordinates in Bombieri
coordinates.

---

## 3. Unit-shell point-evaluation estimate

Let

~~~math
I_n=[n,n+1),
\qquad
E_n(F)
=
\int_{I_n}|F(t)|^2\,dt.
~~~

Take \(z=x+iy\) with

~~~math
x\in I_n,
\qquad
|y|\le\frac12.
~~~

Split the reproducing integral over the unit shells \(I_m\).

Cauchy-Schwarz on each shell and the rapid kernel decay give, for sufficiently
large \(N\),

~~~math
|F(z)|
\le
C
\sum_{m\in\mathbb Z}
(1+|m-n|)^{-N}
E_m(F)^{1/2}.
~~~

A second weighted Cauchy-Schwarz estimate yields

~~~math
\boxed{
|F(z)|^2
\le
C
\sum_{m\in\mathbb Z}
(1+|m-n|)^{-N}
E_m(F).
}
~~~

The constant is uniform for every \(z\) in the fixed strip
\(|\Im z|\le1/2\).

This is the local Paley-Wiener estimate needed below.

---

## 4. Insert zeta zero density

Let

~~~math
\Gamma_n
=
\{
\gamma\in\Gamma:
\Re\gamma\in I_n
\},
~~~

counted with multiplicity.

EXT-3 gives

~~~math
\boxed{
\#\Gamma_n
\le
C_\Gamma
\log(e+|n|).
}
~~~

Therefore Section 3 implies

~~~math
\sum_{\gamma\in\Gamma_n}
|F(\gamma)|^2
\le
C
\log(e+|n|)
\sum_{m\in\mathbb Z}
(1+|m-n|)^{-N}
E_m(F).
~~~

Summing over \(n\),

~~~math
\sum_{\gamma\in\Gamma}|F(\gamma)|^2
\le
C
\sum_m
E_m(F)
\sum_n
\frac{\log(e+|n|)}
{(1+|m-n|)^N}.
~~~

---

## 5. The logarithmic weight absorbs the shell count

For \(N>2\), the discrete convolution satisfies

~~~math
\boxed{
\sum_{n\in\mathbb Z}
\frac{\log(e+|n|)}
{(1+|m-n|)^N}
\le
C_N
\log(e+|m|).
}
~~~

Reason: the logarithmic weight is moderate under translation,

~~~math
\log(e+|n|)
\le
C\bigl(
\log(e+|m|)
+
\log(e+|n-m|)
\bigr),
~~~

and both

~~~math
\sum_j(1+|j|)^{-N}
~~~

and

~~~math
\sum_j
\log(e+|j|)
(1+|j|)^{-N}
~~~

converge.

Thus

~~~math
\sum_{\gamma\in\Gamma}|F(\gamma)|^2
\le
C
\sum_m
\log(e+|m|)
E_m(F).
~~~

Since \(w(t)=\log(e+|t|)\) is comparable to
\(\log(e+|m|)\) on each unit shell,

~~~math
\boxed{
\sum_{\gamma\in\Gamma}|F(\gamma)|^2
\le
C_a
\int_{\mathbb R}
\log(e+|t|)
|F(t)|^2\,dt.
}
~~~

This is the desired LOG-BESSEL estimate.

---

## 6. Why this does not contradict WD-T36

WD-T36 says logarithmic form control does not dominate any fixed positive
Sobolev frequency weight

~~~math
|t|^{2\varepsilon}.
~~~

The present estimate asks for no such domination.

The extra ingredient is that \(F\) belongs to a Paley-Wiener class of fixed
exponential type because \(v\) has compact support.

The proof uses:

1. compact support / exponential type;
2. rapid decay of a reproducing kernel away from the evaluation shell;
3. the actual divisor count
   \[
   O(\log T);
   \]
4. the already-present logarithmic form weight.

Thus

~~~math
\boxed{
\text{LOG-BESSEL}
\not\Rightarrow
H^\varepsilon\text{ coercivity}.
}
~~~

No hidden positive-Sobolev bootstrap has been introduced.

---

## 7. Bounded zero-coordinate analysis on the closed form domain

Let

~~~math
\mathfrak F_a
~~~

denote the shifted logarithmic closed form domain.

Define initially on the regular core

~~~math
\mathcal Z_a v
=
(F(\gamma))_{\gamma\in\Gamma}.
~~~

The LOG-BESSEL estimate gives

~~~math
\boxed{
\|\mathcal Z_a v\|_{\ell^2(\Gamma)}^2
\le
C_a
\|v\|_{\mathfrak F_a}^2.
}
~~~

Hence \(\mathcal Z_a\) extends uniquely by continuity to a bounded map

~~~math
\boxed{
\mathcal Z_a:
\mathfrak F_a
\longrightarrow
\ell^2(\Gamma).
}
~~~

This closes the square-summability seam left by the regular
\(H_0^1\) argument.

---

## 8. Pair diagonalization extends automatically

The raw-to-pair transform of WD-T20 is a fixed unitary transformation on each
conjugate-pair block.

After quotienting multiplicity-null directions it extends orthogonally to the
whole \(\ell^2\) zero-coordinate carrier.

Therefore

~~~math
\mathcal Z_a
=
\mathcal Z_{+,a}
\oplus
\mathcal Z_{-,a},
~~~

with

~~~math
K_-
=
M_\Pi\oplus B_\Pi.
~~~

The selected and background projections are bounded, so

~~~math
\mathcal Z_{M,a}
=
P_{M_\Pi}\mathcal Z_{-,a},
~~~

and

~~~math
\mathcal Z_{B,a}
=
P_{B_\Pi}\mathcal Z_{-,a}
~~~

are bounded on the full logarithmic form domain.

---

## 9. Extend the polarized zero-side identity

On the regular core, H1-P2 gives

~~~math
Q_W(v_1,v_2)
=
\langle
\mathcal Z_{+,a}v_1,
\mathcal Z_{+,a}v_2
\rangle
-
\langle
\mathcal Z_{M,a}v_1,
\mathcal Z_{M,a}v_2
\rangle
-
\langle
\mathcal Z_{B,a}v_1,
\mathcal Z_{B,a}v_2
\rangle.
~~~

Each channel term is continuous in the logarithmic form norm by Section 7.

The closed Weil form is also continuous in its form norm.

Therefore density of the regular core gives the identity for all

~~~math
v_1,v_2\in\mathfrak F_a.
~~~

Hence

~~~math
\boxed{
Q_W(v_1,v_2)
=
Q_{+,a}(v_1,v_2)
-
Q_{M,a}(v_1,v_2)
-
Q_{B,a}(v_1,v_2)
}
~~~

on the entire closed logarithmic form domain.

This is a **form decomposition**; no claim is made that each channel is a
bounded operator on ambient \(L^2\).

---

## 10. Full-form-domain channel custody is therefore available

The previous open item

~~~text
PFB-3F — channel custody on full logarithmic form domain
~~~

is discharged at the form level.

For every fixed selected packet \(\Pi\), a closed-form-domain vector has
well-defined square-summable

- positive zero coordinates;
- selected negative coordinates;
- unselected background coordinates.

Moreover, their signed squared norms reproduce the same closed Weil form.

Thus the custody distinction

~~~math
\boxed{
\text{selected negativity}
\Longrightarrow
\text{full negativity},
}
~~~

and the warning

~~~math
\boxed{
\text{full negativity}
\not\Longrightarrow
\text{selected negativity}
}
~~~

remain meaningful on the full logarithmic form domain.

Background elimination and Douglas norm classifications still require choosing
the appropriate Hilbert carrier for the bounded channel maps; the **owner
decomposition of the form itself**, however, is now closed.

---

## 11. Consequence for the ratified cross-collar theorem

The ratified cross-collar theorem applies to an arbitrary endpoint neutral
mode in the closed form domain.

LOG-BESSEL now gives that mode—and every strict-support perturbation in the
closed form domain—a canonical \(\ell^2\) zero-coordinate decomposition.

Therefore the earlier regular/singular custody split is unnecessary at the
level of form ownership.

The remaining collar question is no longer

~~~text
Can the singular neutral mode be assigned selected/background coordinates?
~~~

It can.

The remaining issue is the **dynamical source question**:

> when null persistence fails, can the negative cross-collar perturbation be
> chosen so that its selected raw source is the same fixed source carried by
> the endpoint neutral mode?

That is stronger than channel custody and is not answered here.

---

## 12. Result of this NF pass

The logarithmic form norm is exactly strong enough to absorb the logarithmic
density of the zeta divisor:

~~~math
\boxed{
\sum_{\gamma\in\Gamma}|F(\gamma)|^2
\lesssim_a
\int_{\mathbb R}
\log(e+|t|)
|F(t)|^2\,dt.
}
~~~

Thus

~~~text
SZ-CHANNEL-CUSTODY-FORMDOMAIN / LOG-BESSEL — CLOSED as residue.
~~~

This extends the canonical zero-side positive / selected-negative / background
polarization to Suzuki's full closed logarithmic form domain without any
positive-Sobolev bootstrap.

The next unresolved issue is source preservation across the cross-collar
negative perturbation, not form-domain square summability.

---

## 13. Candidate follow-on if ratified

~~~text
SZ-CROSS-COLLAR / SAME-SOURCE PERTURBATION
~~~

A future NF should determine whether the nonzero quotient cross-functional can
be detected inside the kernel of the selected-coordinate variation map on the
closed form domain, now that that map is well-defined and bounded there.

**No canonical cursor movement is asserted by this residue.**
