# RPB-51 — Zero-eigenspace multiplicity and core-lift audit

**Date:** 2026-09-28  
**Branch:** research/reflected-packet-bridge  
**Status:** **CORRECTION / SUZUKI §8.5 IDENTIFIES THE ZERO GENERALIZED EIGENSPACE IN THE COMPLETED SCREW SPACE \(\mathcal H(S_a)\), NOT THE ORDINARY \(L^2\) KERNEL OF THE COMPACT OPERATOR \(G_a\) / RPB-33 ACTUAL-EDGE CORE-EXISTENCE CLAIM IS NOT SOURCE-JUSTIFIED / CORE-RESTRICTED RPB-34–50 RESULTS SURVIVE CONDITIONALLY / ACTUAL-EDGE PLATEAU COLLAPSE IS WITHDRAWN PENDING A GENUINE \(L^2\) CORE-LIFT INPUT**  
**Dependencies:** RPB-30, RPB-32, RPB-33, RPB-50; Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v3, §§8.2–8.5.  
**Promotion status:** none.

## 0. Objective

RPB-50 left one multiplicity question:

~~~math
\dim\ker A_c
\stackrel{?}{=}
\dim\ker_{L^2}G_c.
~~~

RPB-33 had earlier treated Suzuki §8.5 as proving enough to infer

~~~math
0\in\sigma(A_c)
\Longrightarrow
\ker_{L^2}G_c\ne\{0\}.
~~~

RPB-51 audits that source statement at the level of the spaces on which the generalized problem is actually posed.

The result is corrective.

Suzuki's zero generalized eigenspace lives in the completed screw space
\(\mathcal H(S_a)\), and Suzuki explicitly states earlier that

~~~math
\mathcal H(S_a)\not\subset L^2(-a,a).
~~~

Therefore the source does not identify the full Friedrichs zero eigenspace with the ordinary compact \(L^2\)-kernel of \(G_a\).

---

## 1. The ordinary core carrier

Suzuki first records that

~~~math
D:H_0^1(-a,a)\overset{\sim}{\longrightarrow}L_0^2(-a,a)
~~~

is bijective.

On this ordinary carrier,

~~~math
Q_W(v)
=
\langle G_aDv,Dv\rangle_{L^2}.
~~~

Thus the ordinary compact operator

~~~math
G_a:L_0^2(-a,a)\to L_0^2(-a,a)
~~~

controls Bombieri's \(H_0^1\) problem.

RPB-32 correctly proved the exact core identity

~~~math
\boxed{
\ker A_a\cap H_0^1(-a,a)
=
D^{-1}\!\left(\ker_{L^2}G_a\right).
}
~~~

This statement remains intact.

---

## 2. Suzuki's completed screw space

Fix a spectral shift \(\mu<\lambda_a\) and define

~~~math
T_a
=
A_a-\mu I,
\qquad
S_a
=
G_a-\mu K_a,
\qquad
K_a=(-\Delta_N)^{-1}.
~~~

Suzuki defines \(\mathcal H(T_a)\) and \(\mathcal H(S_a)\) as the corresponding form completions and proves that \(D\) extends to a unitary map

~~~math
\boxed{
\bar D:
\mathcal H(T_a)
\overset{\sim}{\longrightarrow}
\mathcal H(S_a).
}
~~~

Crucially, Suzuki states

~~~math
\boxed{
\mathcal H(S_a)\not\subset L^2(-a,a).
}
~~~

So the completed screw carrier is strictly a different object from the ordinary compact-operator carrier \(L_0^2(-a,a)\).

This is exactly the distinction that RPB-33 failed to preserve.

---

## 3. The generalized eigenvalue problem is posed in the completion

Suzuki rewrites the Rayleigh quotient as

~~~math
\frac{Q_W^a(v)}{\|v\|_{L^2}^2}
=
\frac{\langle G_au,u\rangle_{L^2}}
{\langle K_au,u\rangle_{L^2}}
~~~

for core vectors \(v\in H_0^1\) and \(u=Dv\in L_0^2\), then states that this leads to the generalized problem

~~~math
\boxed{
G_au
=
\lambda K_au,
\qquad
u\in\mathcal H(S_a).
}
~~~

He then says that the spectrum of this generalized problem coincides with the spectrum of \(A_a\), and that at \(\lambda=0\) one is looking at the kernel, the \(0\)-eigenspace, of \(G_a\).

The ambient space in that sentence is still \(\mathcal H(S_a)\).

Accordingly, define the **completed generalized screw zero space**

~~~math
\boxed{
\mathcal N_a^{S}
:=
\left\{
u\in\mathcal H(S_a):
G_au=0
\text{ in the generalized/form realization}
\right\}.
}
~~~

The source supports the spectral correspondence

~~~math
\boxed{
\ker A_a
\longleftrightarrow
\mathcal N_a^{S}
}
~~~

through the completed-space reformulation.

It does not, from the quoted §8.5 statement alone, support

~~~math
\boxed{
\ker A_a
\longleftrightarrow
\ker_{L^2}G_a.
}
~~~

---

## 4. Multiplicity bookkeeping

Even granting multiplicity preservation under Suzuki's completed generalized spectral equivalence, the equality obtained is of the form

~~~math
\boxed{
\dim\ker A_a
=
\dim\mathcal N_a^{S},
}
~~~

not

~~~math
\dim\ker A_a
=
\dim\ker_{L^2}G_a.
~~~

The ordinary \(L^2\) screw kernel embeds into the completed zero space through the core:

~~~math
D^{-1}\!\left(\ker_{L^2}G_a\right)
=
\ker A_a\cap H_0^1(-a,a).
~~~

Thus the core defect is naturally retyped as

~~~math
\boxed{
\delta_{\rm core}(a)
=
\dim\mathcal N_a^{S}
-
\dim\ker_{L^2}G_a.
}
~~~

whenever these nullities are finite.

The defect is not removed by §8.5. It is precisely the possible difference between completed generalized zero modes and ordinary \(L^2\) screw-kernel vectors.

---

## 5. Correction to RPB-33

RPB-33 stated

~~~math
0\in\sigma(A_{c_*})
\Longrightarrow
\ker_{L^2}G_{c_*}\ne\{0\}.
~~~

That inference is not justified by the cited §8.5 statement.

What the source supports is

~~~math
\boxed{
0\in\sigma(A_{c_*})
\Longrightarrow
\mathcal N_{c_*}^{S}\ne\{0\}.
}
~~~

Whether

~~~math
\mathcal N_{c_*}^{S}
\cap
L_0^2(-c_*,c_*)
\ne\{0\}
~~~

is a separate core-lift question.

Therefore the RPB-33 claim

~~~text
ACTUAL NEUTRAL EDGE IS SCREW-VISIBLE / CORE-REGULAR NEUTRAL DIRECTION EXISTS
~~~

is withdrawn as a source-supported conclusion.

The historical RPB-33 artifact remains immutable; RPB-51 is its additive correction.

---

## 6. What survives downstream

The mathematical statements RPB-34 through RPB-50 that begin with an explicit hypothesis

~~~math
0\ne u\in\ker_{L^2}G_c
~~~

remain valid as **core-restricted conditional statements**.

In particular, conditional on such a nonzero ordinary screw-core neutral direction:

1. RPB-34's collar leakage test remains valid;
2. RPB-35's screw/Weil collar equivalence remains valid;
3. RPB-45–49's nonthreshold/threshold exclusion remains valid;
4. RPB-50's core-restricted null-extension discharge remains valid.

What does not survive unconditionally is the application of those statements to the actual Friedrichs neutral edge solely via RPB-33.

Thus the implication

~~~math
\boxed{
\ker_{L^2}G_c\ne0
\Longrightarrow
\text{strict-right negativity by the RPB-34–49 mechanism}
}
~~~

survives.

The implication

~~~math
\boxed{
\ker A_c\ne0
\Longrightarrow
\ker_{L^2}G_c\ne0
}
~~~

is again open.

---

## 7. Consequence for RPB-50 plateau collapse

RPB-50's abstract plateau theorem

~~~math
G_c\succeq0,
\quad
\ker_{L^2}G_c\ne0
\Longrightarrow
G_a\not\succeq0
\quad(a>c)
~~~

remains valid.

But its application at the actual neutral edge used the now-withdrawn RPB-33 bridge.

Therefore the branch-local statement

~~~text
ACTUAL NEUTRAL EDGE HAS NO POSITIVE-LENGTH NONNEGATIVE PLATEAU
~~~

is no longer established by the current RPB chain.

The corrected status is:

~~~text
CORE-RESTRICTED PLATEAU COLLAPSE: PROVED CONDITIONALLY
ACTUAL-EDGE CORE EXISTENCE: OPEN
ACTUAL-EDGE PLATEAU COLLAPSE VIA THIS ROUTE: OPEN
~~~

This is a scope rollback, not a failure of the collar mechanism itself.

---

## 8. Consequence for AZ-FIN-WEIL-NULL-EXTENSION

RPB-49/50 still give the negative answer for every actual neutral mode already known to lie in

~~~math
\ker A_c\cap H_0^1(-c,c).
~~~

So

~~~text
AZ-FIN-WEIL-NULL-EXTENSION / CORE-RESTRICTED:
DISCHARGED NEGATIVELY, CONDITIONAL ON CORE MEMBERSHIP.
~~~

For an arbitrary Friedrichs neutral mode, the canonical interface remains open.

After RPB-51, its residual problem is more sharply typed:

~~~math
\boxed{
\text{Does the actual Friedrichs zero eigenspace contain a nonzero }H_0^1
\text{ vector, or even lie entirely in }H_0^1?
}
~~~

Equivalently, on the completed screw side:

~~~math
\boxed{
\mathcal N_c^S
\cap
L_0^2(-c,c)
\stackrel{?}{\ne}
\{0\},
}
~~~

and, for full promotion,

~~~math
\boxed{
\mathcal N_c^S
\stackrel{?}{=}
\ker_{L^2}G_c.
}
~~~

---

## 9. RPB-51 determination

~~~math
\boxed{
\textbf{RPB-51 — SUZUKI'S GENERALIZED ZERO EIGENSPACE LIVES IN THE COMPLETED SCREW SPACE, SO §8.5 DOES NOT CLOSE THE ORDINARY \(L^2\) CORE-LIFT DEFECT.}
}
~~~

The corrected object map is

~~~math
\boxed{
\ker A_a
\longleftrightarrow
\mathcal N_a^{S}
\supseteq
\ker_{L^2}G_a,
}
~~~

with the ordinary core relation

~~~math
\boxed{
D^{-1}\!\left(\ker_{L^2}G_a\right)
=
\ker A_a\cap H_0^1(-a,a).
}
~~~

RPB-33's source-based actual-edge \(L^2\) kernel existence claim is withdrawn.

The downstream RPB null-extension mechanism remains intact only on the explicitly assumed ordinary screw-core subspace.

## Next cursor

~~~text
RPB-52 / COMPLETED-TO-L2 SCREW CORE-LIFT TEST
~~~

The next pass should attack the now-correctly typed inclusion problem

~~~math
\mathcal N_c^S
\cap
L_0^2(-c,c)
\stackrel{?}{\ne}
\{0\}
~~~

at the actual neutral edge.

Priority order:

1. determine whether Suzuki's completed zero mode has any extra regularity forced by the zero eigenvalue;
2. test whether the \(G_a\)-kernel equation itself regularizes a completed generalized zero mode into \(L^2\);
3. inspect parity or ground-state simplicity only if they act on the completed zero space and genuinely force an \(L^2\) representative;
4. if no lift is available, isolate the quotient \(\mathcal N_c^S/\ker_{L^2}G_c\) as the exact remaining object rather than treating it as an ordinary multiplicity defect.
