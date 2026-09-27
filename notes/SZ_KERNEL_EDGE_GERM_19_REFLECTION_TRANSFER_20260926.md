# SZ-KERNEL-EDGE-GERM-19 — Reflected blind transfer and dyadic resonance sparsity

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Immediate residue:** SZ-KERNEL-EDGE-GERM-18  
**Target tested:** BLIND-SIDE REFLECTION TRANSFER  
**Public promotion:** forbidden

## 0. Objective

GERM-18 reduced the hard dyadic branch to a finite-dimensional family of
one-sided blind sources \(b\) whose weighted Stieltjes/archimedean transforms
are superflat at the boundary.

GERM-2/3 supplied the missing geometric comparison:

at a reflected prime site, the blind physical half for one edge orientation is
exactly the visible physical half for the opposite orientation.

This pass inserts that reflection structure into the blind-transform
filtration.

The result is a sharp but incomplete reduction.

At every reflected dyadic site, the hard branch splits into:

1. a finite-order opposite-visible branch, already detectable;
2. a **bilateral superflat branch** in which both the blind source mass and
   its Stieltjes transform are superflat to every algebraic order.

On that bilateral branch:

- the blind Laplace-moment sequence decays faster than every algebraic power;
- the boundary generating function is \(C^\infty\)-flat;
- all of its boundary jets become an explicit discrete moment system.

However this still does not force the source to vanish.

Moreover, dyadic reflection is arithmetically sparse:

\[
\boxed{
\text{unless }2c=N\log2,
\text{ at most one dyadic hinge has a reflected prime-power partner}.
}
\]

Thus reflection cannot by itself close the generic dyadic escape chain.

---

# I. Right and left source coordinates

## 1. Orientation pair

Let

\[
L=2c.
\]

For

\[
u\in K_c,
\]

define

\[
f_+(s)=u(c-s),
\qquad
f_-(s)=u(-c+s),
\qquad
0<s<L.
\]

A right-oriented prime hinge at

\[
\ell
\]

has physical site

\[
x_\ell=c-\ell.
\]

Its right-oriented visible physical half is

\[
(x_\ell-\rho,x_\ell),
\]

while its right-oriented blind physical half is

\[
(x_\ell,x_\ell+\rho).
\]

---

# II. Reflection geometry

## 2. Reflected partner

A left-oriented hinge at

\[
\lambda
\]

has physical site

\[
-c+\lambda.
\]

It coincides with \(x_\ell\) exactly when

\[
-c+\lambda=c-\ell,
\]

that is,

\[
\boxed{
\lambda=L-\ell.
}
\]

At this reflected site, the left-oriented visible physical half is

\[
(x_\ell,x_\ell+\rho),
\]

which is exactly the right-oriented blind half.

Thus:

\[
\boxed{
\text{right blind half at }\ell
=
\text{left visible half at }L-\ell.
}
\]

This is the GERM-3 reflection geometry in the local germ coordinates needed
here.

---

# III. Exact source-coordinate identity at a reflected site

## 3. Blind profile

Take a right-oriented blind profile

\[
b(r)
=
f_+(\ell-r),
\qquad
0<r<\rho.
\]

At the reflected left hinge

\[
\lambda=L-\ell,
\]

we have

\[
\begin{aligned}
f_-(\lambda+r)
&=
u(-c+\lambda+r)\\
&=
u(c-\ell+r)\\
&=
f_+(\ell-r).
\end{aligned}
\]

Therefore

\[
\boxed{
b(r)
=
f_-(\lambda+r).
}
\]

So the right-blind source germ is literally the left-visible source germ,
with no reconstruction operator and no change of norm.

---

# IV. Bilateral visible-superflat subspace

## 4. Definition on the edge obstruction

GERM-15 defined the right-visible superflat subspace.

Define its left-oriented analogue using \(f_-\).

Their intersection is the **bilateral visible-superflat subspace** registered
in the terminology registry.

Denote it schematically by

\[
\boxed{
E_{\rm bi-vis}^\infty.
}
\]

For every reflected site and every

\[
u\in E_{\rm bi-vis}^\infty,
\]

the identity of Section III gives

\[
\boxed{
\|b\|_{L^2(0,\varepsilon)}
=
o(\varepsilon^N)
\qquad
\forall N.
}
\]

Thus reflection converts the previously blind source germ into a
source-mass-superflat germ.

---

# V. Reflected-site dichotomy

## 5. Opposite-visible filtration

Fix a reflected right hinge \(\ell\).

Restrict the finite-dimensional edge obstruction to the corresponding
left-visible half.

As in GERM-15, the resulting local-mass filtration stabilizes at a finite
order.

Therefore every right-blind direction at the reflected site lies in exactly
one of two branches.

### Branch R1 — finite-order opposite-visible mass

The left-visible germ is not superflat.

Then there exists a finite filtration order at which

\[
\boxed{
\|b\|_{L^2(0,\varepsilon)}
\ne
o(\varepsilon^N).
}
\]

This is already a finite-order local source channel.

### Branch R2 — bilateral superflat mass

The left-visible germ is superflat to every order.

Then

\[
\boxed{
\|b\|_{L^2(0,\varepsilon)}
=
o(\varepsilon^N)
\qquad
\forall N.
}
\]

Only Branch R2 remains compatible with the fully hard reflected case.

---

# VI. Combine with the blind-transform filtration

## 6. Transform branch

GERM-18 supplies the second dichotomy:

\[
\mathscr Tb
\]

either has finite-order boundary mass, or belongs to the stabilized
blind-transform superflat subspace.

Thus at a reflected dyadic site the terminal hard branch satisfies
simultaneously

\[
\boxed{
\|b\|_{L^2(0,\varepsilon)}
=
o(\varepsilon^N)
}
\]

and

\[
\boxed{
\|\mathscr Tb\|_{L^2(0,\varepsilon)}
=
o(\varepsilon^N)
}
\]

for every \(N\).

This is the reflected hard branch.

---

# VII. Superflat source mass gives inverse-power regularity

## 7. Weighted \(L^2\) lemma

Assume

\[
\|b\|_{L^2(0,\varepsilon)}
=
o(\varepsilon^N)
\qquad
\forall N.
\]

Then for every integer

\[
M\ge0,
\]

\[
\boxed{
r^{-M}b(r)\in L^2(0,a).
}
\]

One proof uses dyadic shells.

On

\[
2^{-(k+1)}a<r<2^{-k}a,
\]

\[
r^{-2M}
\lesssim
2^{2Mk}.
\]

The superflat prefix estimate, with an order larger than \(M\), makes the
resulting geometric shell series summable.

Thus source-mass superflatness gives every inverse algebraic weight in
\(L^2\).

---

# VIII. Rapid decay of the blind moments

## 8. Laplace moments

Recall

\[
A_m(b)
=
\int_0^a
e^{-\lambda_m r}b(r)\,dr,
\qquad
\lambda_m=2m+\frac12.
\]

Write

\[
b(r)=r^M h_M(r)
\]

with

\[
h_M=r^{-M}b\in L^2.
\]

Then

\[
|A_m(b)|
\le
\|h_M\|_2
\left(
\int_0^a
e^{-2\lambda_mr}r^{2M}\,dr
\right)^{1/2}.
\]

Hence

\[
\boxed{
|A_m(b)|
\lesssim_M
\lambda_m^{-M-1/2}.
}
\]

Because \(M\) is arbitrary,

\[
\boxed{
A_m(b)
=
O_M(m^{-M})
\qquad
\forall M.
}
\]

So the reflected hard branch has a rapidly decreasing archimedean moment
sequence.

---

# IX. Smooth boundary generating function

## 9. \(q\)-variable

GERM-18 gives

\[
(\mathscr Tb)(\eta)
=
-e^{\eta/2}A_+(b)
+
\sum_{m=1}^{\infty}
e^{-\lambda_m\eta}A_m(b).
\]

Set

\[
q=e^{-\eta/2}.
\]

Then

\[
\boxed{
H_b(q)
=
-A_+(b)q^{-1}
+
\sum_{m=1}^{\infty}
A_m(b)q^{4m+1}.
}
\]

The rapid decay from Section VIII implies that the series and all of its
termwise derivatives converge at

\[
q=1.
\]

Therefore

\[
\boxed{
H_b
\text{ extends }C^\infty\text{ to }q=1.
}
\]

---

## 10. Transform superflatness becomes boundary jet vanishing

Since

\[
1-q
\asymp
\eta
\]

as

\[
\eta\downarrow0,
\]

and \(\mathscr Tb\) is superflat, the \(C^\infty\) extension satisfies

\[
\boxed{
H_b^{(k)}(1)=0
\qquad
\forall k\ge0.
}
\]

Thus the reflected hard branch is equivalent to a moment sequence satisfying:

1. rapid decay in \(m\);
2. all boundary generating-function jets vanish at \(q=1\);
3. the coefficients arise from the Hausdorff/Laplace moment range of one
   actual \(L^2(0,a)\) source.

This is substantially stronger than the raw Stieltjes-flat branch of GERM-18.

---

# X. Exact discrete moment-jet system

## 11. Differentiate in the \(\eta\)-variable

Rapid decay of the coefficients also permits termwise differentiation of

\[
\mathscr Tb(\eta)
=
-e^{\eta/2}A_+
+
\sum_{m\ge1}
e^{-\lambda_m\eta}A_m
\]

at

\[
\eta=0.
\]

Because the transform is \(C^\infty\)-flat there,

\[
\frac{d^k}{d\eta^k}
\mathscr Tb(0)=0
\qquad
(k\ge0).
\]

Hence

\[
\boxed{
-\left(\frac12\right)^kA_+
+
\sum_{m=1}^{\infty}
(-\lambda_m)^kA_m
=
0
\qquad
(k\ge0).
}
\]

Equivalently,

\[
\boxed{
\sum_{m=1}^{\infty}
(-\lambda_m)^kA_m
=
\left(\frac12\right)^kA_+.
}
\]

All sums converge absolutely because the sequence is rapidly decreasing.

So reflection converts the hard blind branch into a Schwartz-type discrete
moment problem on the spectral lattice

\[
\left\{
-\lambda_m:m\ge1
\right\}
\cup
\left\{
\frac12
\right\}.
\]

---

# XI. Sequence algebra alone still does not close

## 12. Flat disk functions with rapidly decreasing coefficients

Rapid coefficient decay plus infinite-order radial flatness at one boundary
point is not, by itself, a quasi-analytic condition for analytic functions on
the disk.

For example, choose

\[
0<\alpha<1
\]

and consider

\[
\Phi(q)
=
q^5
\exp
\left(
-\frac1{(1-q^4)^\alpha}
\right)
\]

on the unit disk, using the analytic branch determined by

\[
\Re(1-q^4)>0.
\]

Along

\[
q\uparrow1,
\]

\[
\Phi(q)
\]

is flatter than every power of \(1-q\).

Its boundary values are \(C^\infty\)-flat at the fourth roots of unity, and
its Taylor coefficients decay faster than every algebraic power.

The exponents are of the form

\[
4m+1
\]

after the initial shift.

Therefore the abstract sequence conditions

\[
\text{rapid coefficients}
+
\text{flat boundary generating function}
\]

do not force all coefficients to vanish.

This example is not asserted to satisfy the Hausdorff/Laplace range condition

\[
A_m
=
\int_0^a e^{-\lambda_mr}b(r)\,dr
\]

for one \(L^2\) source \(b\).

That range condition is now load-bearing.

---

# XII. Dyadic reflection arithmetic

## 13. Reflection condition

A dyadic right hinge has the form

\[
\ell_j=j\log2.
\]

It is reflected when

\[
L-\ell_j
\]

is itself a prime-power logarithm.

Equivalently,

\[
\boxed{
\frac{e^L}{2^j}
\text{ is a prime power}.
}
\]

---

## 14. Two reflected dyadic hinges force dyadic resonance

Suppose two distinct indices

\[
j<k
\]

are reflected.

Then there exist prime powers

\[
p^r,
\qquad
q^s
\]

such that

\[
e^L
=
2^jp^r
=
2^kq^s.
\]

Therefore

\[
p^r
=
2^{k-j}q^s.
\]

The left side is a power of one prime.

If

\[
q\ne2,
\]

the right side contains the distinct prime factors \(2\) and \(q\), which is
impossible.

Hence

\[
q=2.
\]

Then \(p=2\) as well.

Therefore

\[
\boxed{
e^L=2^N
}
\]

for some integer \(N\).

Equivalently,

\[
\boxed{
L=N\log2.
}
\]

Thus:

\[
\boxed{
\text{two distinct reflected dyadic hinges}
\Longrightarrow
2c=N\log2.
}
\]

---

# XIII. Generic versus resonant support lengths

## 15. Generic support

If

\[
2c\notin(\log2)\mathbb N,
\]

then:

\[
\boxed{
\text{at most one dyadic hinge is reflected}.
}
\]

Therefore almost the entire dyadic escape chain consists of isolated
right-blind sites whose opposite physical half is not an active left-prime
rough channel.

Reflection can improve at most one dyadic step.

It cannot close the generic chain.

---

## 16. Dyadic-resonant support

If

\[
2c=N\log2,
\]

then for every interior dyadic hinge

\[
j\log2,
\qquad
1\le j\le N-1,
\]

the reflected delay is

\[
(N-j)\log2
=
\log(2^{N-j}),
\]

which is again a prime-power hinge.

Thus the full dyadic spine is reflection-closed:

\[
\boxed{
j
\longleftrightarrow
N-j.
}
\]

This is an exceptional arithmetic geometry.

On the bilateral visible-superflat branch, every dyadic blind cell encountered
by the chain is then source-mass superflat as well as transform-superflat.

That produces rapid moment sequences and the discrete moment-jet identities
at every dyadic cell.

It still does not, by the present argument, force those cells to vanish.

---

# XIV. What reflection actually buys

## 17. Reflected-site upgrade

At a reflected site, the hard branch has the simultaneous package

\[
\boxed{
\text{blind source mass superflat}
}
\]

\[
\boxed{
\text{blind Stieltjes transform superflat}
}
\]

\[
\boxed{
A_m=O_M(m^{-M})\quad\forall M
}
\]

and

\[
\boxed{
\sum_{m\ge1}
(-\lambda_m)^kA_m
=
\left(\frac12\right)^kA_+
\quad
\forall k.
}
\]

This is a genuine strengthening over GERM-18.

But it is still a non-quasi-analytic sequence problem unless the
Hausdorff/Laplace range structure is exploited.

---

# XV. Result of this NF pass

Reflection transfer is now sharply classified.

At a reflected dyadic site:

\[
\boxed{
\text{right blind germ}
=
\text{left visible germ}.
}
\]

Hence the terminal reflected hard branch has both source-mass and
transform-mass superflatness.

This gives rapid Laplace-moment decay and the exact infinite jet system

\[
\boxed{
\sum_{m\ge1}
(-\lambda_m)^kA_m
=
\left(\frac12\right)^kA_+
\qquad
(k\ge0).
}
\]

However:

\[
\boxed{
\text{rapid discrete moments + flat generating function}
}
\]

remain non-quasi-analytic at the abstract sequence level.

And reflection is generically sparse:

\[
\boxed{
2c\notin(\log2)\mathbb N
\Longrightarrow
\text{at most one reflected dyadic hinge}.
}
\]

Therefore reflection does not close the generic visible-germ obstruction.

The exceptional dyadic-resonant support lengths

\[
2c=N\log2
\]

form a distinct branch where the full dyadic spine is reflection-closed.

---

# XVI. Next traversal target

The next genuinely new target is

\[
\boxed{
\text{SZ-KERNEL-EDGE-GERM-20 / HAUSDORFF-RANGE JET RIGIDITY}.
}
\]

The next pass should use the fact that the rapidly decaying sequence

\[
A_m
\]

is not arbitrary.

It lies in the Hausdorff/Laplace moment range

\[
\boxed{
A_m
=
\int_0^{\log2}
e^{-(2m+1/2)r}b(r)\,dr
}
\]

of one actual blind source \(b\).

The target is to determine whether the simultaneous conditions

\[
r^{-M}b\in L^2
\quad
\forall M
\]

and

\[
\sum_{m\ge1}
(-\lambda_m)^kA_m
=
\left(\frac12\right)^kA_+
\quad
\forall k
\]

force

\[
b=0
\]

inside this Hausdorff range.

A positive theorem would eliminate every reflected hard branch and completely
close the exceptional dyadic-resonant support geometry.

A negative theorem would prove that even bilateral reflection does not cross
the quasi-analyticity barrier.

No Hausdorff-range jet rigidity theorem is proved in this pass.

---

# XVII. Cursor status

The canonical theorem cursor remains

\[
\boxed{\text{SZ-CROSS-COLLAR-3}}.
\]

This is an unratified reflection-transfer / resonance-sparsity result.

No public promotion and no canonical cursor movement are asserted.
