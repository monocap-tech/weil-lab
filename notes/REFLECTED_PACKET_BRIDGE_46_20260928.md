# RPB-46 — Threshold Carleman--Mellin endpoint realization

**Date:** 2026-09-28  
**Branch:** \`research/reflected-packet-bridge\`  
**Status:** **PASS AS LOCAL MODEL / FORMAL INDICIAL ROOTS ARE GENUINE \(L^2\)-ADMISSIBLE CONORMAL MODES / THRESHOLD BRANCH NOT LOCALLY EXCLUDED / GLOBAL REALIZATION REMAINS OPEN**  
**Dependencies:** RPB-45; RPB-EXT-A5 Mellin diagonalization of the Carleman operator.  
**Promotion status:** none.

## 0. Objective

RPB-45 reduced every possible strict neutral collar to a prime-power threshold

\`\`\`math
2c=\log n_0
\`\`\`

and the local endpoint equation

\`\`\`math
\frac12
\int_0^{2c}
\frac{f(r)}{s+r}\,dr
+
\varepsilon_u
a_0
f(s)
+
A(s)
=
0,
\qquad
s>0,
\`\`\`

where

\`\`\`math
a_0
=
\frac{\Lambda(n_0)}{\sqrt{n_0}},
\qquad
\varepsilon_u\in\{+1,-1\},
\qquad
A\in C^\omega.
\`\`\`

RPB-45 extracted the formal indicial equation

\`\`\`math
\sin(\pi\beta)
=
\frac{\pi}{2\varepsilon_u a_0}.
\`\`\`

RPB-46 asks whether those roots are merely formal, or whether they correspond
to genuine local \(L^2\) endpoint species of the singular integral equation.

They are genuine local conormal modes modulo analytic forcing.

Therefore the exceptional threshold branch is **not** eliminated by local
\(L^2\), \(H_0^1\), parity, or Mellin-spectrum considerations.

The remaining obstruction is global realization.

---

## 1. The threshold singular operator

Define the truncated endpoint Carleman operator

\`\`\`math
(\mathcal C_\delta f)(s)
=
\int_0^\delta
\frac{f(r)}{s+r}\,dr,
\qquad
s>0.
\`\`\`

The singular part of the threshold endpoint equation is

\`\`\`math
\boxed{
\mathcal T_{\varepsilon}
=
\frac12\mathcal C_\delta
+
\varepsilon a_0 I.
}
\`\`\`

The finite interval

\`\`\`math
[\delta,2c]
\`\`\`

and all non-Carleman kernel corrections contribute functions analytic in
\(s\) near \(0\).

Thus local nonanalyticity is determined entirely by
\(\mathcal T_\varepsilon\).

---

## 2. Classical Mellin diagonalization

On the full half-line, the Carleman operator

\`\`\`math
(\mathcal C f)(x)
=
\int_0^\infty
\frac{f(y)}{x+y}\,dy
\`\`\`

is diagonalized by the Mellin transform.

The multiplier on the \(L^2\) Mellin line is

\`\`\`math
\boxed{
\frac{\pi}{\cosh(\pi t)}.
}
\`\`\`

Hence

\`\`\`math
\boxed{
\sigma(\mathcal C)
=
[0,\pi]
}
\`\`\`

and the spectrum is absolutely continuous.

### External pin

RPB-EXT-A5 records the Yafaev/classical Carleman diagonalization.

---

## 3. The threshold weight always lies below the half-Carleman edge

For

\`\`\`math
n_0=p^m,
\`\`\`

we have

\`\`\`math
a_0
=
\frac{\log p}{p^{m/2}}
\le
\frac{\log p}{\sqrt p}.
\`\`\`

For real \(x>1\),

\`\`\`math
\frac{\log x}{\sqrt x}
\`\`\`

has maximum \(2/e\) at \(x=e^2\).

Therefore

\`\`\`math
\boxed{
0<a_0
\le
\frac{2}{e}
<
\frac{\pi}{2}.
}
\`\`\`

Define

\`\`\`math
\boxed{
\tau_0
=
\frac1\pi
\operatorname{arcosh}
\left(
\frac{\pi}{2a_0}
\right)
>0.
}
\`\`\`

---

## 4. Full-line \(L^2\) Mellin spectral typing

The full-line threshold model has Mellin multiplier

\`\`\`math
M_\varepsilon(t)
=
\frac{\pi}{2\cosh(\pi t)}
+
\varepsilon a_0.
\`\`\`

### Even screw source

For

\`\`\`math
\varepsilon=+1,
\`\`\`

we have

\`\`\`math
M_+(t)>0
\`\`\`

for all real \(t\).

Thus the full-line \(L^2\) Carleman model has no real Mellin spectral zero in
the even-source sector.

### Odd screw source

For

\`\`\`math
\varepsilon=-1,
\`\`\`

the equation

\`\`\`math
M_-(t)=0
\`\`\`

is

\`\`\`math
\cosh(\pi t)
=
\frac{\pi}{2a_0}.
\`\`\`

Hence there are exactly two real solutions

\`\`\`math
\boxed{
t=\pm\tau_0.
}
\`\`\`

These belong to the absolutely continuous spectrum of the full Carleman
operator.

They are generalized Mellin modes, not \(L^2\) eigenfunctions.

This distinction will matter below.

---

## 5. Local monomial asymptotics

Let

\`\`\`math
\chi\in C_c^\infty([0,\delta))
\`\`\`

satisfy

\`\`\`math
\chi=1
\`\`\`

near \(0\).

For noninteger \(\beta\) with

\`\`\`math
\Re\beta>-1,
\`\`\`

set

\`\`\`math
f_\beta(r)
=
\chi(r)r^\beta.
\`\`\`

Then the singular endpoint integral has the standard expansion

\`\`\`math
\boxed{
\mathcal C_\delta f_\beta(s)
=
-\frac{\pi}{\sin(\pi\beta)}
s^\beta
+
H_\beta(s),
}
\`\`\`

where

\`\`\`math
H_\beta
\in
C^\omega
\`\`\`

near \(s=0\).

### Direct derivation

For the uncut model,

\`\`\`math
I_\beta(s)
=
\int_0^\delta
\frac{r^\beta}{s+r}\,dr.
\`\`\`

When

\`\`\`math
-1<\Re\beta<0,
\`\`\`

the substitution \(r=st\) gives the nonanalytic coefficient

\`\`\`math
\int_0^\infty
\frac{t^\beta}{1+t}\,dt
=
-\frac{\pi}{\sin(\pi\beta)}.
\`\`\`

For larger \(\Re\beta\), repeated use of

\`\`\`math
\frac{r^\beta}{s+r}
=
r^{\beta-1}
-
s
\frac{r^{\beta-1}}{s+r}
\`\`\`

reduces to this strip.

Each reduction contributes only a polynomial/analytic term in \(s\).

The coefficient of the noninteger power remains

\`\`\`math
-\frac{\pi}{\sin(\pi\beta)}.
\`\`\`

The cutoff error is analytic because it is supported away from \(r=0\).

---

## 6. Exact indicial family

Applying the threshold singular operator gives

\`\`\`math
\mathcal T_\varepsilon
f_\beta
=
\left[
-\frac{\pi}{2\sin(\pi\beta)}
+
\varepsilon a_0
\right]
s^\beta
+
\text{analytic}.
\`\`\`

Therefore the exact indicial family is

\`\`\`math
\boxed{
\mathfrak m_\varepsilon(\beta)
=
-\frac{\pi}{2\sin(\pi\beta)}
+
\varepsilon a_0.
}
\`\`\`

A zero of

\`\`\`math
\mathfrak m_\varepsilon
\`\`\`

removes the entire nonanalytic leading term.

Thus

\`\`\`math
\boxed{
\mathfrak m_\varepsilon(\beta)=0
\Longrightarrow
\mathcal T_\varepsilon f_\beta
\in
C^\omega
}
\`\`\`

near the endpoint.

This is local conormal realization modulo analytic forcing.

---

## 7. Even-source indicial roots

Let

\`\`\`math
\varepsilon=+1.
\`\`\`

The indicial equation is

\`\`\`math
\sin(\pi\beta)
=
\frac{\pi}{2a_0}.
\`\`\`

Since the right side is \(>1\), the roots are complex.

Using

\`\`\`math
\sin
\left[
\pi
\left(
\frac12+i\tau
\right)
\right]
=
\cosh(\pi\tau),
\`\`\`

the first \(L^2\)-admissible pair is

\`\`\`math
\boxed{
\beta
=
\frac12
\pm
i\tau_0.
}
\`\`\`

All copies are obtained by adding even integers.

Thus the leading admissible endpoint source species is

\`\`\`math
\boxed{
f(s)
\sim
s^{1/2}
e^{\pm i\tau_0\log s}.
}
\`\`\`

For a real source this appears as a real linear combination

\`\`\`math
s^{1/2}
\cos(\tau_0\log s),
\qquad
s^{1/2}
\sin(\tau_0\log s).
\`\`\`

These functions are in

\`\`\`math
L^2(0,\delta).
\`\`\`

---

## 8. Odd-source indicial roots

Let

\`\`\`math
\varepsilon=-1.
\`\`\`

The indicial equation is

\`\`\`math
\sin(\pi\beta)
=
-\frac{\pi}{2a_0}.
\`\`\`

The first formal roots are

\`\`\`math
\boxed{
\beta
=
-\frac12
\pm
i\tau_0.
}
\`\`\`

Their real part is exactly

\`\`\`math
-\frac12.
\`\`\`

Hence

\`\`\`math
|s^\beta|^2
\sim
s^{-1},
\`\`\`

so these are not \(L^2\)-admissible endpoint sources.

Because the indicial family is \(2\)-periodic in \(\beta\), the next pair is

\`\`\`math
\boxed{
\beta
=
\frac32
\pm
i\tau_0.
}
\`\`\`

These are \(L^2\)-admissible.

Thus the leading admissible odd-source species is

\`\`\`math
\boxed{
f(s)
\sim
s^{3/2}
e^{\pm i\tau_0\log s}.
}
\`\`\`

---

## 9. Compatibility with the screw-core physical mode

Recall

\`\`\`math
u
=
ih'.
\`\`\`

Near the right endpoint,

\`\`\`math
f(s)
=
u(c-s).
\`\`\`

If

\`\`\`math
f(s)
\sim
s^\beta,
\`\`\`

then one integration gives

\`\`\`math
h(c-s)
\sim
s^{\beta+1}
\`\`\`

up to a nonzero complex scalar.

### Even screw source

For

\`\`\`math
\Re\beta=\frac12,
\`\`\`

the physical mode has

\`\`\`math
h(c-s)
\sim
s^{3/2}
e^{\pm i\tau_0\log s}.
\`\`\`

### Odd screw source

For

\`\`\`math
\Re\beta=\frac32,
\`\`\`

the physical mode has

\`\`\`math
h(c-s)
\sim
s^{5/2}
e^{\pm i\tau_0\log s}.
\`\`\`

Both are compatible with

\`\`\`math
h\in H_0^1(-c,c).
\`\`\`

Therefore the screw-core domain does not exclude either parity sector.

---

## 10. Local model modes are not full-line Carleman eigenfunctions

The even-sector endpoint roots exist even though

\`\`\`math
M_+(t)>0
\`\`\`

on the real \(L^2\) Mellin line.

There is no contradiction.

The truncated endpoint equation is a boundary/conormal problem, not the
global half-line eigenvalue problem.

Its indicial roots are obtained by meromorphic continuation of the Mellin
symbol away from the \(L^2\) line.

Likewise, in the odd sector the roots

\`\`\`math
-\frac12\pm i\tau_0
\`\`\`

correspond to the global continuous-spectrum zeros on the critical
\(L^2\) Mellin line, while the first actual \(L^2\) endpoint species is the
period-shifted pair

\`\`\`math
\frac32\pm i\tau_0.
\`\`\`

Thus full-line Carleman spectral theory types the local problem but does not
replace the endpoint analysis.

---

## 11. The local threshold equation is not obstructed

For either parity, choose one of the admissible roots \(\beta\) and a cutoff
monomial

\`\`\`math
f_\beta
=
\chi s^\beta.
\`\`\`

Section 6 gives

\`\`\`math
\boxed{
\frac12
\mathcal C_\delta f_\beta
+
\varepsilon a_0f_\beta
=
A_\beta(s),
}
\`\`\`

with

\`\`\`math
A_\beta
\in
C^\omega
\`\`\`

near \(0\).

Therefore there exists an analytic forcing for which this nonzero \(L^2\)
endpoint germ solves the exact local singular equation.

This proves:

\`\`\`math
\boxed{
\text{the threshold endpoint operator has genuine nonzero local }
L^2
\text{ conormal modes modulo analytic forcing}.
}
\`\`\`

So the exceptional threshold branch cannot be killed by local singular
integral theory alone.

---

## 12. Zero mean and parity do not remove the local modes

Parity is already built into the sign

\`\`\`math
\varepsilon_u.
\`\`\`

The two parity sectors simply select different admissible exponent families.

The zero-mean law

\`\`\`math
\int_{-c}^{c}u=0
\`\`\`

is global.

For the odd source sector it is automatic.

For the even source sector it imposes one global scalar constraint on the
interior continuation.

It does not alter the local indicial family and does not force the endpoint
amplitude to vanish.

Therefore:

\`\`\`math
\boxed{
\text{parity + zero mean do not provide a local threshold exclusion}.
}
\`\`\`

---

## 13. What is and is not realized

RPB-46 proves **local realization modulo an analytic remainder**.

It does not prove that the actual analytic remainder produced by the global
Weil neutral equation equals the \(A_\beta\) associated with a chosen local
mode.

Therefore RPB-46 does not prove existence of a strict neutral collar.

The remaining statement is global:

> Does the actual finite-dimensional screw-kernel neutral mode at a threshold
> have a nonzero endpoint Mellin amplitude in one of the admissible indicial
> channels, with the analytic remainder matched by the global interior
> equation?

This is the threshold global-realization gap.

---

## 14. Regularity consequence if a threshold mode is realized

Although no global realization is promoted, the admissible endpoint species
would be substantially smoother than the generic logarithmic boundary layer
from RPB-28.

The physical endpoint powers are:

\`\`\`math
3/2\pm i\tau_0
\`\`\`

in the even-source sector, and

\`\`\`math
5/2\pm i\tau_0
\`\`\`

in the odd-source sector.

Thus any globally realized threshold collar mode would have far more than the
\(H^{1/2}\) regularity required by the earlier support-differentiation route.

This is consistent with RPB-33's screw-core \(H_0^1\) regularity and shows that
the exceptional threshold mechanism is a highly regular branch.

No global Sobolev exponent is promoted here without a full endpoint expansion
theorem.

---

## 15. RPB-46 determination

\`\`\`math
\boxed{
\textbf{RPB-46 — THE PRIME-THRESHOLD CARLEMAN EQUATION HAS GENUINE \(L^2\)-ADMISSIBLE LOG-OSCILLATORY CONORMAL MODES; LOCAL ENDPOINT ANALYSIS DOES NOT EXCLUDE STRICT PERSISTENCE.}
}
\`\`\`

Exact indicial family:

\`\`\`math
\boxed{
\mathfrak m_{\varepsilon_u}(\beta)
=
-\frac{\pi}{2\sin(\pi\beta)}
+
\varepsilon_u
\frac{\Lambda(n_0)}{\sqrt{n_0}}.
}
\`\`\`

Exact oscillation rate:

\`\`\`math
\boxed{
\cosh(\pi\tau_0)
=
\frac{\pi}{
2\Lambda(n_0)/\sqrt{n_0}
}.
}
\`\`\`

First \(L^2\)-admissible source exponents:

\`\`\`math
\boxed{
\begin{array}{ll}
\varepsilon_u=+1:
&
\beta=\frac12\pm i\tau_0,
\\[2mm]
\varepsilon_u=-1:
&
\beta=\frac32\pm i\tau_0.
\end{array}
}
\`\`\`

The threshold branch therefore survives local Mellin analysis.

Next cursor:

\`\`\`text
RPB-47 / GLOBAL THRESHOLD MELLIN-AMPLITUDE MATCHING
\`\`\`

The next pass should return to the actual finite-dimensional endpoint nullspace:

1. define a lawful threshold Mellin-amplitude map on the screw-visible kernel;
2. determine whether the global interior neutral equation forces that amplitude
   to vanish;
3. use parity and the zero-mean constraint to reduce the amplitude dimension;
4. test whether a nonzero amplitude is compatible with the selected
   Birman--Schwinger unit-gain relation;
5. decide whether any prime-power threshold can realize the local conormal mode
   globally.
