# RPB-44 — Paired endpoint collision resonance and germ matching

**Date:** 2026-09-28  
**Branch:** \`research/reflected-packet-bridge\`  
**Status:** **PASS / PAIRED ENDPOINT RESONANCES ARE ARITHMETICALLY IMPOSSIBLE / EVERY PRIME-ENDPOINT ACTIVATION ABOVE THE SUPPORT EDGE IS UNCROSSABLE**  
**Dependencies:** RPB-43; RPB-EXT-A2 Gel'fond--Schneider theorem.  
**Promotion status:** none.

## 0. Objective

RPB-43 reduced the only possible crossing of a prime-endpoint activation to a
paired right-exit/left-entry resonance

\`\`\`math
c+\log n
=
\log m-c,
\`\`\`

equivalently

\`\`\`math
e^{2c}
=
\frac{m}{n},
\`\`\`

for prime powers \(m,n\).

RPB-44 asks whether parity and endpoint-germ matching can ever allow such a
collision to be crossed by a constant screw collar.

They cannot.

The germ-matching equations force equality of the two positive von Mangoldt
weights

\`\`\`math
\frac{\Lambda(n)}{\sqrt n}
=
\frac{\Lambda(m)}{\sqrt m}.
\`\`\`

For prime powers this equality implies \(m=n\).  The resonance equation would
then give \(c=0\), outside the branch.

Thus every prime-endpoint activation strictly above \(c>0\) is uncrossable.

Conditional on existence of a strict collar at all, its maximal radius is
therefore the first prime-endpoint activation above the original support edge.

---

## 1. Local paired-collision setup

Let

\`\`\`math
x_0
=
c+\log n
=
\log m-c
\`\`\`

be a paired endpoint collision.

Write

\`\`\`math
s=x-x_0.
\`\`\`

Let

\`\`\`math
a_n
=
\frac{\Lambda(n)}{\sqrt n},
\qquad
a_m
=
\frac{\Lambda(m)}{\sqrt m}.
\`\`\`

By RPB-43, the zero-extended screw source \(u\) is real analytic on
\((-c,c)\) and has analytic singular support only at \(\pm c\).

All screw-potential contributions other than the two colliding endpoint terms
are therefore real analytic through \(s=0\).

Let their sum in the second derivative be

\`\`\`math
A(s),
\`\`\`

real analytic near \(0\).

---

## 2. One-sided constant-collar equations

Suppose the constant screw collar crosses \(x_0\).

Then

\`\`\`math
F_u''(x_0+s)=0
\`\`\`

for sufficiently small \(s\ne0\).

For \(s<0\), the right-endpoint exit associated with \(n\) is active and the
left-endpoint entry associated with \(m\) is not yet active:

\`\`\`math
\boxed{
A(s)
+
a_n u(c+s)
=
0,
\qquad
s<0.
}
\`\`\`

For \(s>0\), the \(n\)-term has exited the support and the \(m\)-term has
entered through the left endpoint:

\`\`\`math
\boxed{
A(s)
+
a_m u(-c+s)
=
0,
\qquad
s>0.
}
\`\`\`

These are the exact local germ-matching equations.

---

## 3. Reduce the left endpoint by parity

The source lies in one parity block, so

\`\`\`math
u(-x)
=
\varepsilon_u u(x),
\qquad
\varepsilon_u\in\{+1,-1\}.
\`\`\`

Hence

\`\`\`math
u(-c+s)
=
\varepsilon_u u(c-s).
\`\`\`

Define the right-endpoint interior germ

\`\`\`math
U(s)
=
u(c+s),
\qquad
s<0.
\`\`\`

The first one-sided equation gives

\`\`\`math
-a_n^{-1}A(s)
=
U(s)
\qquad
(s<0).
\`\`\`

Since \(A\) is analytic, this identity analytically continues \(U\) across
\(s=0\).

Using this continuation, the second equation becomes

\`\`\`math
\boxed{
a_n U(s)
=
a_m\varepsilon_u U(-s)
}
\`\`\`

as an analytic germ near \(s=0\).

---

## 4. Reflection forces equality of weights

Replace \(s\) by \(-s\):

\`\`\`math
a_n U(-s)
=
a_m\varepsilon_u U(s).
\`\`\`

Substituting into the first germ relation yields

\`\`\`math
a_n^2 U(s)
=
a_m^2 U(s).
\`\`\`

The endpoint germ \(U\) is not identically zero.

If it were, \(u\) would vanish on an interior neighborhood of \(c\), and
interior analyticity from RPB-43 would force

\`\`\`math
u\equiv0,
\`\`\`

contradicting the nonzero neutral source.

Therefore

\`\`\`math
a_n^2=a_m^2.
\`\`\`

The weights are positive, so

\`\`\`math
\boxed{
a_n=a_m.
}
\`\`\`

The parity sign affects only the even/odd symmetry of the analytically
continued endpoint germ; it does not alter the positive weight equality.

---

## 5. Prime-power weight equality

Write

\`\`\`math
n=p^r,
\qquad
m=q^s,
\`\`\`

with \(p,q\) prime and \(r,s\ge1\).

Then

\`\`\`math
a_n
=
\frac{\log p}{p^{r/2}},
\qquad
a_m
=
\frac{\log q}{q^{s/2}}.
\`\`\`

The required equality is

\`\`\`math
\boxed{
\frac{\log p}{p^{r/2}}
=
\frac{\log q}{q^{s/2}}.
}
\`\`\`

There are two cases.

---

## 6. Same-prime case

If

\`\`\`math
p=q,
\`\`\`

then

\`\`\`math
p^{-r/2}
=
p^{-s/2},
\`\`\`

so

\`\`\`math
r=s.
\`\`\`

Hence

\`\`\`math
\boxed{
m=n.
}
\`\`\`

---

## 7. Distinct-prime case

Assume

\`\`\`math
p\ne q.
\`\`\`

Then the weight equality gives

\`\`\`math
\boxed{
\frac{\log p}{\log q}
=
\frac{p^{r/2}}{q^{s/2}}.
}
\`\`\`

The right side is algebraic.

The left side is irrational: if

\`\`\`math
\frac{\log p}{\log q}
=
\frac ab
\in\mathbb Q,
\`\`\`

then

\`\`\`math
p^b=q^a,
\`\`\`

contradicting unique factorization for distinct primes.

So if the equality held, \(\log p/\log q\) would be algebraic irrational.

Gel'fond--Schneider then applies to

\`\`\`math
q^{\log p/\log q}
=
p.
\`\`\`

Since \(q\) is algebraic and not \(0\) or \(1\), and the exponent would be
algebraic irrational, the left side would be transcendental.

But the right side \(p\) is algebraic.

Contradiction.

Therefore distinct primes cannot satisfy the weight equality.

### External pin

RPB-EXT-A2 records the Gel'fond--Schneider theorem.

Thus

\`\`\`math
\boxed{
a_n=a_m
\Longrightarrow
m=n.
}
\`\`\`

for prime powers.

---

## 8. The resonance equation then forces \(c=0\)

A paired collision also requires

\`\`\`math
e^{2c}
=
\frac{m}{n}.
\`\`\`

Section 7 gives

\`\`\`math
m=n.
\`\`\`

Therefore

\`\`\`math
e^{2c}=1,
\`\`\`

so

\`\`\`math
c=0.
\`\`\`

The RPB neutral support radius satisfies

\`\`\`math
c>0.
\`\`\`

Hence:

\`\`\`math
\boxed{
\text{no paired endpoint collision can be crossed in the live branch}.
}
\`\`\`

---

## 9. Endpoint collision exclusion

RPB-43 already excluded crossing of an unpaired endpoint activation.

RPB-44 excludes the only remaining paired alternative.

Therefore, for every \(c>0\),

\`\`\`math
\boxed{
\text{a constant screw collar cannot cross any prime-power endpoint activation at }x>c.
}
\`\`\`

This is the prime-endpoint collision exclusion theorem.

---

## 10. Exact maximal collar radius conditional on strict persistence

Assume a strict collar exists:

\`\`\`math
a_{\max}>c.
\`\`\`

Let

\`\`\`math
n_+(c)
=
\min\left\{
p^m:
\log(p^m)>2c
\right\}.
\`\`\`

The first right-endpoint exit above \(c\) occurs at

\`\`\`math
c+\log2.
\`\`\`

The first left-endpoint entry strictly above \(c\) occurs at

\`\`\`math
\log n_+(c)-c.
\`\`\`

Since no prime-endpoint activation can be crossed,

\`\`\`math
\boxed{
a_{\max}
=
\min
\left\{
c+\log2,\,
\log n_+(c)-c
\right\}.
}
\`\`\`

This formula is valid conditional on strict collar existence, including when
\(2c\) itself is a prime-power threshold: the definition of \(n_+(c)\) uses a
strict inequality and selects the next activation above \(c\).

---

## 11. No collision ladder exists

RPB-43 asked whether crossing one paired event could force an infinite
arithmetic collision ladder.

RPB-44 shows that no first paired event can be crossed at all.

Therefore the ladder question collapses:

\`\`\`math
\boxed{
\text{there is no admissible paired-collision ladder for }c>0.
}
\`\`\`

The arithmetic obstruction occurs at the first attempted paired crossing.

---

## 12. What remains unresolved

The result above is **conditional on having already crossed the original
support boundary**.

The initial strict null-extension question is

\`\`\`math
\boxed{
F_u
\text{ constant on }(-c,c)
\stackrel{?}{\Longrightarrow}
F_u
\text{ constant on }(-c-\varepsilon,c+\varepsilon)
}
\`\`\`

for some \(\varepsilon>0\).

RPB-44 does not settle this initial crossing.

The reason is that at the base support edge \(x=c\), the non-prime screw kernel
also meets separation

\`\`\`math
t=x-y=0
\`\`\`

at the source endpoint.

The non-prime component is analytic only for \(t>0\), not across \(t=0\).

Thus the initial crossing contains a distinct archimedean/base-kernel
singularity absent from every later prime-endpoint event \(x>c\).

At a prime threshold \(2c=\log n\), an equality-threshold prime event may also
participate at \(x=c\).

This is precisely the remaining support-extension problem.

---

## 13. Relation to \`AZ-FIN-WEIL-NULL-EXTENSION\`

RPB-44 substantially narrows the neutral interface.

If strict persistence occurs at all, its future geometry is no longer open:

\`\`\`math
\boxed{
\text{strict collar exists}
\Longrightarrow
a_{\max}
=
\min
\{c+\log2,\log n_+(c)-c\}.
}
\`\`\`

There are:

- no later unpaired crossings;
- no paired-resonance crossings;
- no collision ladder.

Therefore the remaining uncertainty has been pushed all the way back to the
**initial base endpoint** \(x=c\).

The open question is now whether the non-prime \(t=0\) screw singularity,
possibly together with an equality-threshold prime term, permits the endpoint
constant germ to extend even infinitesimally outside the original support.

---

## 14. RPB-44 determination

\`\`\`math
\boxed{
\textbf{RPB-44 — PAIRED PRIME-ENDPOINT RESONANCES CANNOT SATISFY THE REQUIRED WEIGHT MATCHING; ALL LATER PRIME ACTIVATIONS ARE UNCROSSABLE.}
}
\`\`\`

Exact germ condition:

\`\`\`math
\boxed{
\frac{\Lambda(n)}{\sqrt n}
=
\frac{\Lambda(m)}{\sqrt m}.
}
\`\`\`

Prime-power arithmetic forces

\`\`\`math
m=n,
\`\`\`

while paired collision requires

\`\`\`math
e^{2c}=m/n.
\`\`\`

Thus \(c=0\), contradiction.

Conditional maximal-radius theorem:

\`\`\`math
\boxed{
a_{\max}
=
\min
\left\{
c+\log2,\,
\log n_+(c)-c
\right\}
}
\`\`\`

whenever a strict collar exists.

Next cursor:

\`\`\`text
RPB-45 / BASE-ENDPOINT t=0 SCREW-SINGULARITY MATCHING
\`\`\`

The next pass should return to the original support boundary \(x=c\):

1. derive the local \(t\downarrow0\) asymptotic of Suzuki's non-prime screw
   kernel;
2. convolve that singular germ with the analytic endpoint germ of \(u\);
3. include any equality-threshold prime-power activation at \(2c=\log n\);
4. determine whether constancy on the interior side can cross the base endpoint
   at all;
5. if crossing is possible, identify the exact boundary-germ compatibility
   condition that replaces the now-excluded prime-endpoint resonance.
