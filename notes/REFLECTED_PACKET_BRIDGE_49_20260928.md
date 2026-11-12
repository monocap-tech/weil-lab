# RPB-49 — Background resolvent endpoint parametrix

**Date:** 2026-09-28  
**Branch:** \`research/reflected-packet-bridge\`  
**Status:** **PASS / UNIVERSAL LOGARITHMIC EDGE NORMAL FORM IDENTIFIED / NONINTEGER CONORMAL MODES ACQUIRE AN UNCANCELLABLE LOG / THRESHOLD MELLIN AMPLITUDES EXTINGUISH / NO NONZERO SCREW-CORE NULL MODE CAN PERSIST TO A STRICT ENLARGEMENT**  
**Dependencies:** RPB-31, RPB-43, RPB-45 through RPB-48; RPB-EXT-A7 Chen--Weth edge kernel.  
**Promotion status:** none.

## 0. Objective

RPB-48 isolated the missing object

\`\`\`math
\mathcal B_{\beta,c}(g)
=
\mathfrak a_\beta
\left(
D A_{B,c}^{-1}g
\right),
\`\`\`

the endpoint Mellin boundary symbol of the positive background resolvent.

RPB-49 asks whether an explicit Green/Poisson formula for the full background
resolvent is actually needed.

It is not.

The universal Dirichlet logarithmic principal part already distinguishes the
generic logarithmic boundary layer from the power-scale threshold Mellin
channels.

A noninteger conormal component of the physical mode is multiplied by one
extra factor of

\`\`\`math
\log\frac1s
\`\`\`

by the archimedean logarithmic principal operator.

No other term in the endpoint compact-window Weil operator can generate that
same extra logarithm at the same noninteger exponent.

Thus the endpoint null equation itself forces every RPB-46 threshold Mellin
amplitude to vanish.

RPB-47 proved that every nonzero persistent threshold mode must have at least
one nonzero such amplitude.

Therefore the threshold persistence branch is empty.

Combined with the RPB-45 nonthreshold exclusion, no nonzero screw-visible core
neutral mode can persist to any strict support enlargement.

---

## 1. Endpoint form of the actual compact-window operator

Work at the endpoint support radius \(c\).

The whole-line physical operator is

\`\`\`math
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
\`\`\`

Its archimedean multiplier is

\`\`\`math
m_\infty(\xi)
=
\Re\psi\!\left(
\frac14+\frac{i\xi}{2}
\right)
-
\log\pi.
\`\`\`

The digamma asymptotic gives

\`\`\`math
\boxed{
m_\infty(\xi)
=
\log|\xi|
-
\log(2\pi)
+
O(|\xi|^{-2}).
}
\`\`\`

The standard logarithmic Laplacian \(L_\Delta\) has symbol

\`\`\`math
2\log|\xi|.
\`\`\`

Hence, microlocally at high frequency,

\`\`\`math
\boxed{
\mathcal A_\infty
=
\frac12L_\Delta
-
\log(2\pi)I
+
\mathcal S_{-2},
}
\`\`\`

where \(\mathcal S_{-2}\) is two orders smoother in the ordinary
pseudodifferential scale.

For the endpoint singularity analysis, only the
\(\frac12L_\Delta\) term can increase the logarithmic order of a conormal
endpoint singularity.

---

## 2. Universal one-dimensional logarithmic edge operator

Put

\`\`\`math
x=c-s,
\qquad
s\downarrow0.
\`\`\`

For the zero extension of \(h\), the Chen--Weth integral representation in
dimension one gives the universal endpoint singular piece

\`\`\`math
\boxed{
\mathcal E h(s)
=
\int_0^\delta
\frac{h(s)-h(r)}{|s-r|}\,dr
+
h(s)\log\frac1s.
}
\`\`\`

All terms omitted from \(\mathcal E\) are lower in the endpoint singular
hierarchy:

- bounded local multiplication;
- integrals with kernels smooth at the endpoint;
- contributions from source points a fixed positive distance from \(c\).

This is the logarithmic edge normal operator.

---

## 3. Logarithmic boundary coordinate

Set

\`\`\`math
t
=
\log\frac1s,
\qquad
H(t)
=
h(e^{-t}).
\`\`\`

For the model profile

\`\`\`math
H(t)
=
t^{-\alpha},
\qquad
0<\alpha<1,
\`\`\`

split the endpoint integral at \(r=s\).

The \(r<s\) piece is

\`\`\`math
O(t^{-\alpha-1}).
\`\`\`

For the \(r>s\) piece, with \(r=e^{-w}\),

\`\`\`math
\int_s^\delta
\frac{h(s)-h(r)}{r-s}\,dr
=
\int_{\log(1/\delta)}^t
\frac{
t^{-\alpha}-w^{-\alpha}
}{
1-e^{-(t-w)}
}\,dw.
\`\`\`

The leading term is

\`\`\`math
-\frac{\alpha}{1-\alpha}
t^{1-\alpha}.
\`\`\`

The exterior zero-extension term contributes

\`\`\`math
t^{1-\alpha}.
\`\`\`

Therefore

\`\`\`math
\boxed{
\mathcal E h(s)
=
\frac{1-2\alpha}{1-\alpha}
t^{1-\alpha}
+
o(t^{1-\alpha}).
}
\`\`\`

Equivalently, the leading logarithmic normal form is

\`\`\`math
\boxed{
\mathcal N_{\log}H(t)
=
2tH(t)
-
\int^t H(w)\,dw.
}
\`\`\`

Its homogeneous exponent is

\`\`\`math
\boxed{
\alpha=\frac12.
}
\`\`\`

Thus the universal boundary scale is

\`\`\`math
H(t)
\asymp
t^{-1/2},
\`\`\`

or

\`\`\`math
h(c-s)
\asymp
\ell^{1/2}(s),
\qquad
\ell(s)
=
\frac1{\log(1/s)}.
\`\`\`

This matches the optimal boundary scale in the logarithmic-Laplacian
Dirichlet literature.

---

## 4. Screw-core regularity removes the logarithmic boundary layer

For the RPB screw-visible neutral mode,

\`\`\`math
h
\in
H_0^1(-c,c).
\`\`\`

The one-dimensional endpoint trace estimate gives

\`\`\`math
\begin{aligned}
|h(c-s)|
&=
\left|
\int_{c-s}^{c}
h'(x)\,dx
\right|
\\
&\le
s^{1/2}
\|h'\|_{L^2(c-s,c)}.
\end{aligned}
\`\`\`

Therefore

\`\`\`math
\boxed{
h(c-s)
=
o(s^{1/2}).
}
\`\`\`

In particular, for every fixed \(N\),

\`\`\`math
\boxed{
h(c-s)
=
o\!\left(
(\log(1/s))^{-N}
\right).
}
\`\`\`

So every finite inverse-logarithmic boundary layer is absent on the screw
core.

This includes the universal \(\ell^{1/2}\) mode.

The threshold branch therefore lives strictly beyond the generic logarithmic
boundary hierarchy.

---

## 5. Noninteger conormal germs acquire an extra logarithm

Now suppose the zero extension of \(h\) has a noninteger endpoint conormal
component

\`\`\`math
h(c-s)
=
b\,s^\lambda
+
\text{higher conormal/analytic terms},
\`\`\`

with

\`\`\`math
b\ne0,
\qquad
\lambda\notin\mathbb Z_{\ge0}.
\`\`\`

Apply the Chen--Weth integral representation directly.

### Exterior piece

The exterior zero region contributes

\`\`\`math
b\,s^\lambda
\log\frac1s.
\`\`\`

### Interior \(h(s)\)-piece

For \(r>s\),

\`\`\`math
\int_s^\delta
\frac{b\,s^\lambda}{r-s}\,dr
=
b\,s^\lambda
\log\frac1s
+
O(s^\lambda).
\`\`\`

### Interior \(h(r)\)-piece

For noninteger \(\lambda\),

\`\`\`math
\int_s^\delta
\frac{r^\lambda}{r-s}\,dr
\`\`\`

has an asymptotic expansion consisting of:

- analytic integer powers of \(s\);
- one \(s^\lambda\) term;

but no \(s^\lambda\log s\) term.

The \(r<s\) piece contributes only \(O(s^\lambda)\).

Therefore

\`\`\`math
\boxed{
L_\Delta h(c-s)
=
2b\,s^\lambda
\log\frac1s
+
O_{\rm conormal}(s^\lambda)
+
\text{analytic powers}.
}
\`\`\`

Since \(\mathcal A_\infty\) has principal multiplier
\(\log|\xi|\), exactly one half of this logarithmic enhancement survives:

\`\`\`math
\boxed{
\mathcal A_\infty h(c-s)
=
b\,s^\lambda
\log\frac1s
+
O_{\rm conormal}(s^\lambda)
+
\text{lower endpoint order}.
}
\`\`\`

This is the conormal log-enhancement.

---

## 6. No other endpoint term can cancel that enhancement

Consider the endpoint operator with the strict endpoint prime convention

\`\`\`math
\log n<2c.
\`\`\`

For any active delay

\`\`\`math
\ell=\log n>0,
\`\`\`

and \(s>0\) sufficiently small:

- one translated copy lies outside \([-c,c]\) and is zero;
- the other evaluates \(h\) at
  \[
  c-\ell-s,
  \]
  a point a fixed positive distance inside the support.

RPB-43 gives real analyticity at every such interior point.

Thus every active prime translation is analytic in \(s\) near the endpoint.

At an equality threshold

\`\`\`math
2c=\log n_0,
\`\`\`

the \(n_0\)-term is **absent** from the endpoint operator under the strict
endpoint convention.

It appears only in the strict right-limit operator.

The pole/evaluation term has finite-dimensional analytic range.

Finally, the difference

\`\`\`math
m_\infty(\xi)
-
\log|\xi|
+
\log(2\pi)
=
O(|\xi|^{-2})
\`\`\`

is smoothing relative to the logarithmic principal term and cannot create a
new factor of \(\log(1/s)\) at the same noninteger exponent.

Therefore:

\`\`\`math
\boxed{
\text{the coefficient of }
s^\lambda\log(1/s)
\text{ in the endpoint equation is produced only by }
\mathcal A_\infty.
}
\`\`\`

---

## 7. Mellin interpretation: a simple pole becomes a double pole

Let

\`\`\`math
H_M(z)
=
\int_0^\delta
h(c-s)s^{z-1}\,ds.
\`\`\`

A nonzero conormal term

\`\`\`math
b\,s^\lambda
\`\`\`

gives a simple pole of \(H_M\) at

\`\`\`math
z=-\lambda.
\`\`\`

But

\`\`\`math
\mathcal M
\left[
h(s)\log\frac1s
\right](z)
=
-\partial_zH_M(z).
\`\`\`

Thus the conormal log-enhancement produces a **double pole** at
\(z=-\lambda\).

The lower endpoint terms from Section 6 produce at most:

- simple poles at the same conormal exponent;
- integer Taylor poles;
- holomorphic contributions.

They cannot cancel the double pole.

Hence the endpoint null equation gives:

\`\`\`math
\boxed{
\text{noninteger simple Mellin pole of }h
\Longrightarrow
\text{contradiction}.
}
\`\`\`

This is the Mellin double-pole obstruction.

---

## 8. Transfer a threshold source amplitude from \(u\) to \(h\)

The screw source is

\`\`\`math
u
=
Dh
=
i\,h_x.
\`\`\`

With \(x=c-s\),

\`\`\`math
f(s)
:=
u(c-s)
=
-i\,\partial_sh(c-s).
\`\`\`

Let

\`\`\`math
F_M(z)
=
\int_0^\delta
f(s)s^{z-1}\,ds.
\`\`\`

Using

\`\`\`math
h(c)=0
\`\`\`

and integrating by parts,

\`\`\`math
\boxed{
F_M(z)
=
i(z-1)
H_M(z-1)
+
\text{holomorphic cutoff terms}.
}
\`\`\`

Therefore, if

\`\`\`math
\mathfrak a_\beta(u)
=
\operatorname*{Res}_{z=-\beta}
F_M(z)
\ne0,
\`\`\`

then \(H_M\) has a nonzero simple pole at

\`\`\`math
\boxed{
z=-(\beta+1).
}
\`\`\`

Equivalently, the physical mode carries a nonzero conormal component of
exponent

\`\`\`math
\lambda
=
\beta+1.
\`\`\`

---

## 9. Every RPB-46 threshold exponent is forbidden by the endpoint equation

RPB-46 found the admissible threshold source exponents:

\`\`\`math
\beta
=
\frac12\pm i\tau_0
\`\`\`

in the even-source sector, and

\`\`\`math
\beta
=
\frac32\pm i\tau_0
\`\`\`

in the odd-source sector.

Thus the corresponding physical exponents are

\`\`\`math
\lambda
=
\frac32\pm i\tau_0
\`\`\`

or

\`\`\`math
\lambda
=
\frac52\pm i\tau_0.
\`\`\`

Every such \(\lambda\) is noninteger.

Section 7 therefore applies.

Hence, for every lawful threshold channel,

\`\`\`math
\boxed{
\mathfrak a_\beta(u)=0.
}
\`\`\`

This is threshold amplitude extinction.

---

## 10. Background-resolvent interpretation

On the unit-gain space,

\`\`\`math
h_v
=
A_{B,c}^{-1}\Phi_c^*v
\`\`\`

also satisfies the full endpoint neutral equation

\`\`\`math
A_ch_v=0
\`\`\`

because

\`\`\`math
A_c
=
A_{B,c}
-
\Phi_c^*\Phi_c
\`\`\`

and

\`\`\`math
\Phi_ch_v
=
v.
\`\`\`

Therefore the endpoint null-equation argument applies directly to every
threshold-compatible core unit-gain direction.

Thus the boundary-transfer rows from RPB-47/48 satisfy

\`\`\`math
\boxed{
\mathfrak T_{\beta,c}(v)
=
0
}
\`\`\`

for every admissible threshold channel and every

\`\`\`math
v\in E_*^{\rm tc}.
\`\`\`

Equivalently,

\`\`\`math
\boxed{
\mathbf T_c
=
0
\quad
\text{on }
E_*^{\rm tc}.
}
\`\`\`

So the explicit background Green kernel is not needed to compute the
admissible amplitude matrix: the endpoint logarithmic principal symbol forces
that matrix to vanish.

---

## 11. Contradiction with threshold persistence

RPB-47 proved:

\`\`\`math
\boxed{
u\ne0
\text{ threshold-persistent}
\Longrightarrow
\mathfrak A_c(u)\ne0.
}
\`\`\`

RPB-49 proves:

\`\`\`math
\boxed{
u
\text{ threshold-compatible core endpoint neutral}
\Longrightarrow
\mathfrak A_c(u)=0.
}
\`\`\`

Therefore

\`\`\`math
\boxed{
E_*^{\rm pers}
=
\{0\}.
}
\`\`\`

In words:

> no nonzero screw-visible core endpoint neutral mode can realize the
> prime-threshold Carleman branch globally.

This closes the exceptional branch left open by RPB-45 and RPB-46.

---

## 12. Combine threshold and nonthreshold support values

RPB-45 proved

\`\`\`math
2c\notin
\{\log(p^m)\}
\Longrightarrow
\text{no strict neutral collar}.
\`\`\`

RPB-49 proves the same conclusion at the remaining threshold values.

Hence, for every

\`\`\`math
c>0,
\`\`\`

and every nonzero screw-visible core neutral mode,

\`\`\`math
\boxed{
F_u
\text{ cannot remain constant on }
(-a,a)
\text{ for any }
a>c.
}
\`\`\`

Using RPB-35,

\`\`\`math
\boxed{
\text{screw collar persistence}
\iff
\text{core-regular Weil null-extension persistence},
}
\`\`\`

we obtain

\`\`\`math
\boxed{
\text{nonzero screw-visible core neutral mode}
\Longrightarrow
\text{strict null extension is impossible}.
}
\`\`\`

This is the core strict-null-extension exclusion.

---

## 13. Immediate collar leakage consequence

RPB-34 defined

\`\`\`math
\mathcal L_{c,a}u
=
G_aJ_{c,a}u.
\`\`\`

For

\`\`\`math
u\in\ker G_c\setminus\{0\},
\`\`\`

RPB-34 proved

\`\`\`math
\mathcal L_{c,a}u=0
\iff
F_u
\text{ remains constant on }(-a,a).
\`\`\`

Section 12 excludes the right side for every \(a>c\).

Therefore

\`\`\`math
\boxed{
\mathcal L_{c,a}u
\ne0
\qquad
\text{for every }a>c
}
\`\`\`

for every nonzero screw-visible core neutral source to which the RPB-49
endpoint analysis applies.

By the RPB-34 \(2\times2\) collar test, each such leakage produces a strict
negative direction in \(G_a\).

This consequence will be audited against the earlier neutral-plateau
bookkeeping in the next pass.

---

## 14. Scope

RPB-49 proves the strict-null-extension exclusion on the
**screw-visible/core neutral subspace**.

It does not yet rewrite the canonical Horizon-1 interface statement.

Historical RPB notes distinguished:

- the full Friedrichs nullspace;
- the screw-visible/core nullspace;
- the possible core-lift nullity defect.

RPB-33 guarantees that the actual neutral edge has a nonzero screw-visible
core direction, but did not promote equality of the two nullspace dimensions.

Therefore the next pass must audit exactly how the new core exclusion
propagates through:

- the neutral spectral plateau logic;
- the fixed selected unit-gain branch;
- the canonical \`AZ-FIN-WEIL-NULL-EXTENSION\` wording.

No broader promotion is made in RPB-49 itself.

---

## 15. RPB-49 determination

\`\`\`math
\boxed{
\textbf{RPB-49 — THE LOGARITHMIC ENDPOINT PRINCIPAL SYMBOL KILLS EVERY THRESHOLD MELLIN AMPLITUDE; NO NONZERO SCREW-CORE NEUTRAL MODE ADMITS A STRICT NULL EXTENSION.}
}
\`\`\`

Universal log edge:

\`\`\`math
\boxed{
\mathcal N_{\log}H
=
2tH-\int^tH,
\qquad
H_{\rm hom}\sim t^{-1/2}.
}
\`\`\`

Conormal enhancement:

\`\`\`math
\boxed{
h\sim s^\lambda
\Longrightarrow
\mathcal A_\infty h
\supset
s^\lambda\log(1/s).
}
\`\`\`

Threshold amplitude extinction:

\`\`\`math
\boxed{
\mathfrak a_\beta(Dh)=0
\qquad
\text{for every RPB-46 admissible channel}.
}
\`\`\`

Strict core null-extension exclusion:

\`\`\`math
\boxed{
0\ne u\in\ker G_c
\Longrightarrow
G_aJ_{c,a}u\ne0
\quad
(a>c)
}
\`\`\`

within the branch hypotheses above.

Next cursor:

\`\`\`text
RPB-50 / NULL-EXTENSION DISCHARGE AND NEUTRAL-PLATEAU COLLAPSE AUDIT
\`\`\`

The next pass should not discover a new local mechanism.

It should audit the consequences of RPB-49 against the earlier branch:

1. determine whether one nonzero core leakage direction is enough to collapse
   every positive-length neutral spectral plateau;
2. map the result through the RPB-30 neutral-resolvent isomorphism and the
   RPB-33 screw-visible existence theorem;
3. decide the exact new status of
   \`AZ-FIN-WEIL-NULL-EXTENSION\`;
4. determine whether the neutral branch now falls immediately into the fixed
   selected negative-custody/Birman--Schwinger route;
5. record any remaining multiplicity/custody caveat without overpromoting.
