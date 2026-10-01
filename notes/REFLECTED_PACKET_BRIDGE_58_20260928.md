# RPB-58 — Friedrichs threshold Carleman--Stieltjes classification

**Date:** 2026-09-28  
**Branch:** research/reflected-packet-bridge  
**Status:** **PASS / PHYSICAL THRESHOLD CARLEMAN CHANNELS CLASSIFIED / EVERY NONZERO PERSISTENT FRIEDRICHS MODE MUST CARRY A NONINTEGER PHYSICAL MELLIN AMPLITUDE / ENDPOINT LOG-ENHANCEMENT FORCES EVERY SUCH AMPLITUDE TO VANISH / PRIME-POWER THRESHOLD PERSISTENCE EXCLUDED / FULL FRIEDRICHS NULL-EXTENSION EXCLUDED AT ALL SUPPORTS**  
**Dependencies:** RPB-46, RPB-47, RPB-49, RPB-57; standard Mellin diagonalization of the Carleman operator.  
**Promotion status:** none.

## 0. Objective

RPB-57 closed every nonthreshold support and reduced the full Friedrichs
residue to a prime-power equality threshold

~~~math
2c=\log n_0,
\qquad
n_0=p^m.
~~~

After parity diagonalization, strict persistence gives

~~~math
\frac12\Sigma_{\rm ev}(s)
+
a_0f_{\rm ev}(s)
=
A_{\rm ev}(s),
~~~

and

~~~math
\frac12\Sigma_{\rm odd}(s)
-
a_0f_{\rm odd}(s)
=
A_{\rm odd}(s),
~~~

where

~~~math
a_0
=
\frac{\Lambda(n_0)}{\sqrt{n_0}},
~~~

and the forcing germs are analytic.

RPB-58 classifies these equations directly on the **physical endpoint mode**
rather than on the screw source.

The local Carleman channels exist, but the endpoint null equation itself
annihilates all of them.

---

## 1. Physical parity reduction

Let

~~~math
f_+(s)
=
h(c-s),
\qquad
f_-(s)
=
h(-c+s).
~~~

Since the compact-window operator commutes with reflection, decompose \(h\)
into even and odd physical parity blocks.

### Even physical mode

If

~~~math
h(-x)=h(x),
~~~

then

~~~math
f_-(s)=f_+(s).
~~~

The parity-diagonal threshold equation becomes

~~~math
\boxed{
\frac12\mathcal C_\delta f
+
a_0f
=
A_{\rm ev},
}
~~~

modulo the analytic far-endpoint part.

### Odd physical mode

If

~~~math
h(-x)=-h(x),
~~~

then

~~~math
f_-(s)=-f_+(s),
~~~

and the threshold equation becomes

~~~math
\boxed{
\frac12\mathcal C_\delta f
-
a_0f
=
A_{\rm odd}.
}
~~~

Thus the physical parity signs are exactly the
\(\varepsilon=\pm1\) signs of the RPB-46 Carleman family.

---

## 2. Physical indicial family

For a cutoff monomial

~~~math
f_\beta(s)
=
\chi(s)s^\beta,
~~~

with noninteger

~~~math
\Re\beta>-1,
~~~

RPB-46 gives

~~~math
\mathcal C_\delta f_\beta(s)
=
-\frac{\pi}{\sin(\pi\beta)}
s^\beta
+
\text{analytic}.
~~~

Hence the physical threshold indicial family is

~~~math
\boxed{
\mathfrak m_\varepsilon(\beta)
=
-\frac{\pi}{2\sin(\pi\beta)}
+
\varepsilon a_0.
}
~~~

The indicial equation is

~~~math
\boxed{
\sin(\pi\beta)
=
\frac{\pi}{2\varepsilon a_0}.
}
~~~

As before,

~~~math
0<a_0<\frac{\pi}{2},
~~~

and define

~~~math
\tau_0
=
\frac1\pi
\operatorname{arcosh}
\left(
\frac{\pi}{2a_0}
\right)
>0.
~~~

---

## 3. \(L^2\)-admissible physical endpoint exponents

The physical endpoint mode itself belongs to

~~~math
L^2(0,\delta).
~~~

Therefore an exponent

~~~math
s^\beta
~~~

is admissible only if

~~~math
\Re\beta>-\frac12.
~~~

### Even physical parity

For

~~~math
\varepsilon=+1,
~~~

the leading admissible roots are

~~~math
\boxed{
\beta
=
\frac12
\pm
i\tau_0.
}
~~~

Thus the first physical threshold species is

~~~math
\boxed{
h(c-s)
\sim
s^{1/2}
e^{\pm i\tau_0\log s}.
}
~~~

### Odd physical parity

For

~~~math
\varepsilon=-1,
~~~

the first roots

~~~math
-\frac12
\pm
i\tau_0
~~~

lie exactly on the non-\(L^2\) boundary and are inadmissible.

The next pair is

~~~math
\boxed{
\beta
=
\frac32
\pm
i\tau_0.
}
~~~

Thus the first admissible odd physical species is

~~~math
\boxed{
h(c-s)
\sim
s^{3/2}
e^{\pm i\tau_0\log s}.
}
~~~

All admissible nonanalytic physical channels are noninteger.

---

## 4. These channels are compatible with the Friedrichs operator domain

For the even family,

~~~math
\Re\beta=\frac12,
~~~

and for the odd family,

~~~math
\Re\beta=\frac32.
~~~

Applying the logarithmic principal operator creates

~~~math
s^\beta\log(1/s),
~~~

which remains \(L^2\) in both cases.

Therefore the logarithmic Friedrichs operator domain does not exclude these
channels merely by integrability.

This is important: the threshold contradiction below is an **equation-level**
obstruction, not a domain-membership obstruction.

---

## 5. Lawful physical Mellin amplitudes

Localize

~~~math
f(s)=h(c-s)
~~~

with a cutoff equal to one near the endpoint and define

~~~math
\widehat f_M(z)
=
\int_0^\infty
f_0(s)s^{z-1}\,ds.
~~~

For every \(L^2\)-admissible noninteger indicial root \(\beta\), define

~~~math
\boxed{
\mathfrak b_\beta(h)
=
\operatorname*{Res}_{z=-\beta}
\widehat f_M(z).
}
~~~

The same cutoff-independence argument as RPB-47 applies.

The vector

~~~math
\mathfrak B_c(h)
=
\left(
\mathfrak b_\beta(h)
\right)_{\beta\in\mathcal I_c^{\rm phys}}
~~~

is the **physical threshold Mellin-amplitude vector**.

---

## 6. Every nonzero threshold-persistent physical mode must carry a nonzero amplitude

Assume strict threshold persistence and suppose

~~~math
\mathfrak B_c(h)=0.
~~~

The localized Mellin equation then has no noninteger indicial poles.

As in RPB-47, the endpoint germ is analytic modulo integer Taylor powers.

Let the first nonzero Taylor term be

~~~math
f(s)
=
b_ks^k
+
O(s^{k+1}),
\qquad
b_k\ne0.
~~~

Then

~~~math
\mathcal C_\delta(s^k)
=
P_k(s)
+
(-1)^{k+1}
s^k\log s
+
\text{analytic}.
~~~

The threshold multiplication term

~~~math
\varepsilon a_0f(s)
~~~

and the forcing germ are analytic.

They cannot cancel the nonzero

~~~math
s^k\log s
~~~

term.

Contradiction.

Hence every Taylor coefficient vanishes.

The endpoint germ therefore vanishes on a collar, and interior analyticity
forces

~~~math
h\equiv0.
~~~

Thus a nonzero persistent physical mode must satisfy

~~~math
\boxed{
h\ne0
\text{ and threshold-persistent}
\Longrightarrow
\mathfrak B_c(h)\ne0.
}
~~~

---

## 7. The endpoint operator does not contain the equality-threshold prime

Now return to the **endpoint** null equation

~~~math
A_ch=0.
~~~

At

~~~math
2c=\log n_0,
~~~

the compact-window endpoint convention is strict:

~~~math
\log n<2c.
~~~

Therefore the equality-prime term \(n_0\), which created the multiplication
term

~~~math
\pm a_0f(s)
~~~

in the strict right-limit exterior equation, is **absent** from the endpoint
operator \(A_c\).

All active endpoint prime translations have

~~~math
\log n<2c
~~~

and therefore sample fixed analytic interior points near the boundary.

The pole/evaluation range is analytic.

Thus no endpoint lower-order term has the same noninteger conormal logarithmic
species as the archimedean principal operator.

---

## 8. Endpoint log-enhancement kills every physical threshold amplitude

Suppose

~~~math
\mathfrak b_\beta(h)\ne0
~~~

for one admissible physical threshold root \(\beta\).

Then the endpoint mode contains a nonzero conormal term

~~~math
b\,s^\beta,
\qquad
b\ne0,
~~~

with noninteger \(\beta\).

RPB-49's conormal log-enhancement applies directly to the physical mode:

~~~math
\boxed{
\mathcal A_\infty h(c-s)
\supset
b\,s^\beta\log\frac1s.
}
~~~

At the endpoint:

- every strict-\(<\) prime translation is analytic in \(s\);
- the pole/evaluation term is analytic;
- the smoother archimedean remainder produces no extra logarithm at the same
  noninteger exponent.

Hence nothing can cancel the coefficient of

~~~math
s^\beta\log(1/s).
~~~

The endpoint equation

~~~math
A_ch=0
~~~

therefore forces

~~~math
\boxed{
\mathfrak b_\beta(h)=0
}
~~~

for every admissible physical threshold channel.

Equivalently,

~~~math
\boxed{
\mathfrak B_c(h)=0.
}
~~~

---

## 9. Threshold persistence contradiction

Section 6 gives

~~~math
h\ne0
\text{ and threshold-persistent}
\Longrightarrow
\mathfrak B_c(h)\ne0.
~~~

Section 8 gives, for every endpoint Friedrichs zero mode,

~~~math
\mathfrak B_c(h)=0.
~~~

Therefore no nonzero endpoint Friedrichs zero mode can persist through a
prime-power threshold:

~~~math
\boxed{
2c=\log(p^m)
\Longrightarrow
\text{no nonzero Friedrichs zero mode admits strict null extension}.
}
~~~

This closes the full threshold residue left by RPB-57.

---

## 10. Combine threshold and nonthreshold supports

RPB-57 proved the full nonthreshold exclusion:

~~~math
2c\notin\{\log(p^m)\}
\Longrightarrow
\text{no nonzero Friedrichs zero mode admits strict null extension}.
~~~

RPB-58 proves the same statement at every threshold.

Therefore, for every

~~~math
c>0,
~~~

~~~math
\boxed{
0\ne h\in\ker A_c
\Longrightarrow
\widetilde h
\text{ cannot satisfy the correct strict enlarged null equation for any }a>c.
}
~~~

This is the **full Friedrichs strict-null-extension exclusion**.

---

## 11. Status of AZ-FIN-WEIL-NULL-EXTENSION

The canonical Horizon-1 interface asks whether an actual nonzero
finite-exception unit-gain neutral physical mode satisfying the endpoint
compact-window equation can satisfy the correct right-limit equation on a
strict enlargement.

RPB-57 and RPB-58 now answer this negatively on the full Friedrichs nullspace,
without assuming screw-core membership.

Thus, within the RPB experimental branch and under the existing carrier
identification hypotheses of WD-T38,

~~~math
\boxed{
\texttt{AZ-FIN-WEIL-NULL-EXTENSION}
\text{ is discharged negatively.}
}
~~~

This is a branch-local determination.

The stable theorem ledger and public Horizon-1 package are not modified by
RPB-58; promotion requires a separate dependency/source/scope audit.

---

## 12. RPB-58 determination

~~~math
\boxed{
\textbf{RPB-58 — THE PRIME-POWER THRESHOLD CARLEMAN CHANNELS ARE INCOMPATIBLE WITH THE ENDPOINT FRIEDRICHS NULL EQUATION; FULL NULL EXTENSION IS EXCLUDED AT EVERY SUPPORT.}
}
~~~

Threshold local classification:

~~~math
\boxed{
\begin{array}{ll}
\text{even physical parity:}
&
\beta=\frac12\pm i\tau_0,
\\[2mm]
\text{odd physical parity:}
&
\beta=\frac32\pm i\tau_0.
\end{array}
}
~~~

Persistence demands a nonzero physical Mellin amplitude.

The endpoint equation kills every physical Mellin amplitude by conormal
log-enhancement.

Therefore the threshold branch is empty.

Combined all-support result:

~~~math
\boxed{
0\ne h\in\ker A_c
\Longrightarrow
\text{strict null extension is impossible for every }a>c.
}
~~~

## Next cursor

~~~text
RPB-59 / FULL NULL-EXTENSION DISCHARGE PROMOTION AUDIT
~~~

The next pass should not search for another local mechanism.

It should audit the RPB-57/58 proof chain for promotion into the canonical
Horizon-1 interface:

1. verify every external source pin used by the full Friedrichs argument;
2. remove obsolete dependence on the corrected RPB-33 core-existence claim;
3. check that RPB-43 interior analyticity is lawfully extended to arbitrary
   Friedrichs zero modes;
4. verify the endpoint/right-limit prime convention at equality thresholds;
5. update the stable interface status only if the chain survives that audit.
