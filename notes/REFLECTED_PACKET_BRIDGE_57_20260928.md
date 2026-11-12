# RPB-57 — Bounded Stieltjes residue versus the interior endpoint equation

**Date:** 2026-09-28  
**Branch:** research/reflected-packet-bridge  
**Status:** **PASS / NONTHRESHOLD STRICT PERSISTENCE UPGRADES BOUNDED STIELTJES DATA TO HOLOMORPHIC STIELTJES CONTINUATION / STIELTJES JUMP FORCES ENDPOINT COLLAR VANISHING / INTERIOR ANALYTICITY THEN FORCES THE MODE TO VANISH IDENTICALLY / FULL NONTHRESHOLD FRIEDRICHS NULL-EXTENSION EXCLUDED / THRESHOLD RESIDUE RETYPED AS A COUPLED CARLEMAN--STIELTJES SYSTEM**  
**Dependencies:** RPB-31, RPB-43, RPB-49, RPB-54 through RPB-56; Zhu 2026 equation (9) for the exact archimedean kernel; standard Stieltjes/Sokhotskii--Plemelj jump formula.  
**Promotion status:** none.

## 0. Objective

RPB-56 left, away from thresholds, the necessary persistence condition

~~~math
\Sigma_+(s;h)=O(1),
\qquad
\Sigma_-(s;h)=O(1),
~~~

where

~~~math
\Sigma_+(s;h)
=
\int_0^\delta
\frac{h(c-r)}{s+r}\,dr
~~~

and similarly at the left endpoint.

RPB-57 asks whether bounded Stieltjes data, together with the **exact**
interior/exterior Weil equation, are enough to collapse this residue.

They are.

The key improvement is that strict persistence gives an exact exterior
equation, not merely an estimate.  Off threshold, every term except the
universal \(1/(s+r)\) archimedean singularity is analytic across \(s=0\).

Therefore strict persistence forces the Stieltjes transform itself to be the
restriction of a holomorphic germ across the endpoint.

The Stieltjes jump formula then forces the boundary density to vanish on an
actual collar.

---

## 1. Exact archimedean kernel near the diagonal

Zhu's Gauss-representation formula for the digamma contribution gives, on the
positive physical half-line, the kernel factor

~~~math
q(x)
=
\frac{
2e^{-x/2}
}{
1-e^{-2x}
}.
~~~

Near

~~~math
x=0^+,
~~~

the denominator has a simple zero and

~~~math
\boxed{
q(x)
=
\frac1x
+
q_{\rm an}(x),
}
~~~

where \(q_{\rm an}\) is real analytic near \(0\).

Equivalently, in the normalization already used in RPB-49 and RPB-56,

~~~math
\mathcal A_\infty
=
\frac12L_\Delta
+
\mathcal A_{\rm an},
~~~

where the exterior kernel of
\(\mathcal A_{\rm an}\) is analytic in the positive separation variable near
zero.

This strengthens the earlier
"order \(-2\) / locally bounded" description precisely in the one-sided
exterior geometry needed here.

---

## 2. Exact right exterior decomposition

Let

~~~math
x=c+s,
\qquad
0<s<\varepsilon,
~~~

and let \(\widetilde h\) be the zero extension of a compact-window mode.

Choose

~~~math
0<\delta<\min(1,2c).
~~~

The singular part is

~~~math
-\frac12
\Sigma_+(s;h)
=
-\frac12
\int_0^\delta
\frac{
h(c-r)
}{
s+r
}
\,dr.
~~~

All remaining archimedean terms split into:

1. the analytic kernel remainder \(q_{\rm an}(s+r)\) on
   \(0<r<\delta\);
2. the far-support kernel, whose separation is bounded away from zero;
3. local identity terms, which vanish outside the old support.

Since

~~~math
h\in L^2(-c,c)\subset L^1(-c,c),
~~~

integration of a jointly holomorphic kernel against \(h\) gives a holomorphic
function of the exterior variable in a sufficiently small complex
neighborhood of \(s=0\).

Therefore

~~~math
\boxed{
\mathcal A_\infty\widetilde h(c+s)
=
-\frac12\Sigma_+(s;h)
+
A_+(s),
}
~~~

where

~~~math
A_+
~~~

extends holomorphically to a disc

~~~math
|s|<\varepsilon_0.
~~~

The same statement holds at the left endpoint.

---

## 3. Nonthreshold arithmetic and pole terms are analytic across the endpoint

Assume

~~~math
2c
\notin
\{\log(p^m)\}.
~~~

For every active delay

~~~math
\ell_n=\log n<2c,
~~~

and sufficiently small complex \(s\), the inward translated point

~~~math
c+s-\ell_n
~~~

lies in a fixed compact subinterval of \((-c,c)\).

RPB-43's analytic-ellipticity argument extends to every Friedrichs zero mode,
so

~~~math
h\in C^\omega(-c,c).
~~~

Hence

~~~math
s\mapsto h(c+s-\ell_n)
~~~

extends holomorphically near \(s=0\).

The outward translate remains zero on the real exterior collar and contributes
no endpoint singularity.

The pole/evaluation range is spanned by fixed exponential functions and is
entire.

Thus every non-archimedean term appearing in the strict right exterior equation
is a holomorphic germ at \(s=0\).

---

## 4. Strict nonthreshold persistence forces holomorphic continuation of the Stieltjes transform

Suppose a nonzero Friedrichs endpoint mode were to persist to some strict
support enlargement.

Away from thresholds, the right-limit operator is the same local
compact-window operator.

On a real exterior collar,

~~~math
0<s<\varepsilon,
~~~

strict persistence gives

~~~math
\mathcal W_c^{\rm ext}\widetilde h(c+s)
=
0.
~~~

Sections 2 and 3 therefore give

~~~math
-\frac12\Sigma_+(s;h)
+
B_+(s)
=
0,
~~~

where \(B_+\) is holomorphic on a full disc around \(s=0\).

Hence

~~~math
\boxed{
\Sigma_+(s;h)
=
2B_+(s)
\qquad
(0<s<\varepsilon).
}
~~~

The Stieltjes transform itself is holomorphic on

~~~math
\mathbb C\setminus[-\delta,0].
~~~

By the identity theorem, the equality with \(2B_+\) on the positive real
interval forces

~~~math
\boxed{
\Sigma_+
\text{ to extend holomorphically through }s=0
}
~~~

and, after shrinking the disc, through a nontrivial subinterval

~~~math
(-\varepsilon_1,0)
~~~

of its original Stieltjes cut.

---

## 5. The Stieltjes jump forces boundary-density extinction

Let

~~~math
f_+(r)
=
h(c-r)
\in
L^2(0,\delta).
~~~

For the Stieltjes/Cauchy transform

~~~math
\Sigma_+(z)
=
\int_0^\delta
\frac{
f_+(r)
}{
z+r
}
\,dr,
~~~

the Sokhotskii--Plemelj jump across the negative real axis is, for almost every

~~~math
0<r<\delta,
~~~

~~~math
\boxed{
\Sigma_+(-r+i0)
-
\Sigma_+(-r-i0)
=
-2\pi i\,f_+(r),
}
~~~

up to the fixed orientation convention.

But Section 4 gives a single holomorphic continuation across

~~~math
(-\varepsilon_1,0).
~~~

Its upper and lower boundary values agree there.

Therefore

~~~math
\boxed{
f_+(r)=0
\quad
\text{for a.e. }
0<r<\varepsilon_1.
}
~~~

Equivalently,

~~~math
\boxed{
h=0
\quad
\text{a.e. on }
(c-\varepsilon_1,c).
}
~~~

No boundary trace coefficient, boundedness assumption, or screw-core lift is
used.

---

## 6. Interior analyticity forces global triviality

RPB-43's scalar analytic-ellipticity argument gives

~~~math
h\in C^\omega(-c,c).
~~~

A real-analytic function vanishing on a nonempty open interval vanishes
identically on the connected interior interval.

Hence

~~~math
\boxed{
h\equiv0
\quad
\text{on }
(-c,c).
}
~~~

This contradicts the nonzero neutral-mode hypothesis.

Therefore:

~~~math
\boxed{
2c\notin\{\log(p^m)\}
\Longrightarrow
\text{no nonzero Friedrichs zero mode admits strict null extension}.
}
~~~

This is the **full nonthreshold Friedrichs null-extension exclusion**.

Unlike RPB-45, it is not restricted to screw-core modes.

---

## 7. Left endpoint is redundant off threshold

The right-endpoint argument already forces

~~~math
h\equiv0.
~~~

Thus the left endpoint need not be invoked for nonthreshold exclusion.

The two-sided Stieltjes bookkeeping of RPB-56 remains useful for symmetry and
for thresholds, but one endpoint is enough off threshold.

---

## 8. Why the same argument does not immediately cross an equality threshold

Now suppose

~~~math
2c=\log n_0.
~~~

At the right exterior point the newly active equality-prime translation
samples

~~~math
h(-c+s),
~~~

which is an **opposite-endpoint boundary germ**, not an interior analytic germ.

Thus strict persistence yields

~~~math
-\frac12\Sigma_+(s;h)
-
a_0h(-c+s)
+
B_+(s)
=
0,
~~~

and similarly

~~~math
-\frac12\Sigma_-(s;h)
-
a_0h(c-s)
+
B_-(s)
=
0,
~~~

with

~~~math
a_0
=
\frac{\Lambda(n_0)}{\sqrt{n_0}},
~~~

and \(B_\pm\) holomorphic.

The nonanalytic endpoint term can therefore carry the Stieltjes cut.

One can no longer conclude that \(\Sigma_\pm\) extend holomorphically by
themselves.

---

## 9. Parity diagonalization of the threshold residue

Define the endpoint germs

~~~math
f_+(s)=h(c-s),
\qquad
f_-(s)=h(-c+s),
~~~

and parity combinations

~~~math
f_{\rm ev}=f_++f_-,
\qquad
f_{\rm odd}=f_+-f_-.
~~~

Likewise let

~~~math
\Sigma_{\rm ev}
=
\Sigma_++\Sigma_-,
\qquad
\Sigma_{\rm odd}
=
\Sigma_+-\Sigma_-.
~~~

Adding and subtracting the two threshold exterior equations gives two scalar
Carleman--Stieltjes systems:

~~~math
\boxed{
\frac12\Sigma_{\rm ev}(s)
+
a_0f_{\rm ev}(s)
=
A_{\rm ev}(s),
}
~~~

and

~~~math
\boxed{
\frac12\Sigma_{\rm odd}(s)
-
a_0f_{\rm odd}(s)
=
A_{\rm odd}(s),
}
~~~

where

~~~math
A_{\rm ev},
\quad
A_{\rm odd}
~~~

are holomorphic endpoint germs.

This is exactly the functional species that appeared locally in the
RPB-45--48 threshold analysis.

Therefore the full Friedrichs threshold residue is not a generic bounded
Stieltjes class.

It is a pair of forced inhomogeneous Carleman--Stieltjes boundary equations.

---

## 10. Relation to the earlier threshold Mellin line

RPB-46 diagonalized the homogeneous Carleman operator in Mellin variables and
found admissible threshold channels.

RPB-47--49 then analyzed those channels on the screw-core branch.

RPB-57 shows that, after the RPB-51 correction, the same Carleman--Stieltjes
operator is still the correct object for the **noncore/full Friedrichs**
threshold residue, but the core-specific Mellin-amplitude extinction theorem
cannot simply be imported.

The remaining threshold problem is therefore sharply typed:

~~~math
\boxed{
\text{solve or exclude the inhomogeneous parity-diagonal
Carleman--Stieltjes system in the Friedrichs endpoint class.}
}
~~~

---

## 11. RPB-57 determination

~~~math
\boxed{
\textbf{RPB-57 — FULL NONTHRESHOLD FRIEDRICHS NULL-EXTENSION IS EXCLUDED BY HOLOMORPHIC STIELTJES CONTINUATION; ONLY PRIME-POWER THRESHOLDS REMAIN.}
}
~~~

Nonthreshold conclusion:

~~~math
\boxed{
2c\notin\{\log(p^m)\},
\quad
0\ne h\in\ker A_c
\Longrightarrow
\widetilde h
\text{ cannot satisfy the strict enlarged null equation.}
}
~~~

The proof uses:

1. the exact \(1/t+\) analytic archimedean kernel split;
2. analytic interior prime/pole data;
3. holomorphic continuation of the endpoint Stieltjes transform;
4. its jump formula;
5. interior analytic continuation of \(h\).

The remaining full Friedrichs residue is now **threshold-only**.

## Next cursor

~~~text
RPB-58 / FRIEDRICHS THRESHOLD CARLEMAN--STIELTJES CLASSIFICATION
~~~

The next pass should analyze

~~~math
\frac12\Sigma_\pm^{\rm parity}(s)
\pm
a_0f_\pm^{\rm parity}(s)
=
A_\pm^{\rm parity}(s)
~~~

in the actual Friedrichs endpoint class.

Priority order:

1. Mellin-diagonalize the homogeneous parity equations without assuming
   \(H_0^1\);
2. determine the \(L^2\)-admissible endpoint exponents for the physical mode
   itself;
3. test which channels lie in the logarithmic Friedrichs operator domain;
4. determine whether the analytic inhomogeneous germ can excite any admissible
   homogeneous channel;
5. only after that compare with the earlier core-specific threshold amplitude
   extinction.
