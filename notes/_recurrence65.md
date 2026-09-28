# SZ edge recurrence 65 — mixed-return cone transfer and the full-rotation endpoint

**Date:** 2026-09-27 (America/Los_Angeles)  
**Branch:** sz-cross-collar  
**Status:** UNRATIFIED RESIDUE / ONE NF PASS / SCOPED POSITIVE RESULT  
**Canonical parent:** SZ-CROSS-COLLAR-3, unchanged  
**Immediate input:** GERM-64 and the pre-65 refold  
**Public promotion:** forbidden

## 0. Result and custody

This pass proves the following source-equation statement:

```math
\boxed{\lambda_{\rm ret}<e\le h
\quad\Longrightarrow\quad
x=0\text{ in both scalar parity kernels}.}
```

It closes every finite partial-return path for `lambda_ret < e < h` and separately excludes a nonzero L2 invariant section at the full-rotation endpoint `e=h`. It does **not** close any positive-width interval above h.

Together with the inherited GERM-63 coverage and GERM-60 reconstruction, the experimental ambient prime-channel endpoint becomes

```math
\boxed{0<L\le\log(27/5)=1.686398953570228\ldots.}
```

This is an unratified extension under the same inherited source reduction, not a canonical SZ advancement or an RH proof.

Entry pin: `monocap-tech/weil-lab@bba155cbd6cd52a16d43d1894a72a4b763a3b3ba`. Read the governance ratification record, `notes/_recurrence60.md`, `_recurrence61.md`, `_recurrence63.md`, `_recurrence64.md`, and `notes/SZ_KERNEL_EDGE_PRE65_REFOLD_20260927.md` at that pin. Parallel input remains pinned to `monocap-tech/weil@307446bc46c07056fc32eb63f0e366face06ac76`, especially RETURN-COCYCLE-0, -3, -4, and -5 and their source-row verifiers. No moving public branch is treated as a mathematical dependency.

New notation is registered in the additive research registry [GERM-65 terminology](../docs/TERMINOLOGY_GERM65.md). Historical source notes and their standing are unchanged.

Companion files:

- [Exact verifier](../tools/sz_mixed_return_cone_audit.py).
- [Recorded successful output](_recurrence65_audit.json).

## 1. Source equations and coefficient conventions

Retain

```math
\begin{gathered}
h=\log(81/80),\quad k=\log(16/15),\quad
p=\log(10/9),\quad j=\log(9/8)=p+h,\\
q=\log(4/3),\quad r=q+j,\quad s=q-k,\quad m=q-j=p+k,\\
u=k+e,\quad v=m+e=p+u,\quad w=2q+e,\\
\kappa=k-5h,\quad\lambda_{\rm ret}=h-\kappa.
\end{gathered}
```

The exact arithmetic inequalities needed below include

```math
0<\kappa,\qquad 5\kappa<h<6\kappa,\qquad k+h<p<j.
```

In particular, for `0<e<=h` we have `u<p`, `e<j-k`, and `2h<k`. The verifier checks the nontrivial fixed inequalities by exact prime-power comparison, not floating threshold placement.

Write

```math
\beta=\sqrt{2/3}\,\frac{\log3}{\log2},\quad
\gamma=1/\sqrt2,\quad
\delta=\sqrt{2/5}\,\frac{\log5}{\log2},
```

```math
\mu=\beta\gamma,\quad d=\delta\gamma,\quad
b=\beta\mu,\quad a=b^2,\quad g=1-a,\quad\Delta=1-\mu^2.
```

These coefficient symbols are local to this pass. Certified bounds give `0<mu<1`, `d>0`, `a>1`, `g<0`, and `Delta>0`.

For each external parity `epsilon=+1` or `-1`, let `x in L2(0,w)` satisfy the GERM-60/61 equations almost everywhere:

```math
\begin{array}{ll}
x(t)+\beta x(r+t)+d[x(s+t)-\varepsilon x(u-t)]=0,
 &0<t<u,\\
x(t)+\beta x(r+t)=0,&u<t<v,\\
x(t)=0,&v<t<q,\\
x(t)+\mu[x(t-q)-\varepsilon x(w-t)]=0,&q<t<w.
\end{array}
```

The theorem in this note concerns this explicitly displayed system. Its return to the ambient prime channel uses the inherited GERM-60 equivalence, not an additional assumption about classical endpoint traces.

## 2. Exact elimination down to the low head

Put `T(y)=x(q+y)`. The paired tail block has determinant `Delta`, and the exact tail reconstruction is

```math
T(y)=
\begin{cases}
-\dfrac{\mu}{\Delta}[x(y)+\varepsilon\mu x(e-y)],&0<y<e,\\
-\mu[x(y)-\varepsilon x(q+e-y)],&e<y<q,\\
\dfrac{\mu}{\Delta}[\mu x(z)+\varepsilon x(e-z)],
&y=q+z,\ 0<z<e.
\end{cases}
```

This is the GERM-61/RETURN-COCYCLE-3 Schur solve, now reused directly rather than replacing scalar x-values by an unproved P/J-state interface.

For `u<t<m`, the middle equation becomes `x(t)+b epsilon x(v-t)=0`. Reflection preserves `(u,p)`. Applying the equation at both reflected arguments gives `g x(t)=0`; hence

```math
x=0\quad\text{on }(u,p).
```

The rest of the middle band is reconstructed from the low head by

```math
x(p+z)=
\begin{cases}
-b\varepsilon x(u-z),&0<z<k,\\
-\dfrac b\Delta[\mu x(z-k)+\varepsilon x(u-z)],&k<z<u.
\end{cases}
```

Together with the dead strip `(v,q)` and the displayed tail formulas, all values outside `(0,u)` are thus determined by the low head. These eliminations are reversible on their stated source equations, and all their denominators are certified nonzero.

## 3. The actual two-coordinate state and k-bridge

Define

```math
W(t)=\begin{pmatrix}x(t)\\\varepsilon x(u-t)\end{pmatrix},
\qquad
J=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
```

It obeys `W(u-t)=epsilon J W(t)`. It is a bounded L2 observation of x, not a freely chosen boundary jet and not an assumed copy of the historical P/J state.

For `0<z<e<=h`, the argument `j+k+z` lies in the dead strip. The source row at `k+z`, after the preceding eliminations, is exactly

```math
g\,x(k+z)=\frac d\Delta[\mu x(z)+\varepsilon x(e-z)].
```

Let `f=d/(g Delta)`. Applying this equation at z and e-z gives

```math
W(z)=\begin{pmatrix}1&0\\ f&f\mu\end{pmatrix}
\begin{pmatrix}x(z)\\\varepsilon x(e-z)\end{pmatrix},
```

```math
W(k+z)=\begin{pmatrix}f\mu&f\\0&1\end{pmatrix}
\begin{pmatrix}x(z)\\\varepsilon x(e-z)\end{pmatrix}.
```

The first matrix is invertible. Therefore the exact bridge is

```math
\boxed{
W(k+z)=K W(z),\qquad
K=\begin{pmatrix}
-\dfrac d{g\mu}&\dfrac1\mu\\
-\dfrac1\mu&\dfrac{g\Delta}{d\mu}
\end{pmatrix},\qquad\det K=1.
}
```

This is a state-transfer map derived from the source rows, not a determinant inference from a large constraint matrix. It agrees with RETURN-COCYCLE-3's K2 row after the explicit middle-band substitution. That identity is checked for both parity signs by the verifier.

## 4. Exact h-step library, including both gates

Write `W(t)=(X,Y)^T` and `W(t+h)=(X1,Y1)^T`.

On `e<t<k-h`, the first-cell source row and its reflected companion are

```math
gX+aY_1-dY=0,\qquad gY_1+aX-dX_1=0.
```

They give the genuine bulk map

```math
\boxed{
M=\begin{pmatrix}
\dfrac{2a-1}{da}&\dfrac ga\\
-\dfrac ga&\dfrac da
\end{pmatrix},\qquad\det M=1.
}
```

For `0<t<e`, use the k-bridge to eliminate the additional seed value:

```math
\varepsilon x(e-t)=\frac{Y/f-X}{\mu}.
```

The low source row and its reflected upper-gate companion then become

```math
aY_1+X-\left(d+\frac{ag}{d}\right)Y=0,
\qquad
dX_1-gY_1-\frac{ag}{d}Y=0.
```

Thus the lower-gate map is

```math
\boxed{
N=\begin{pmatrix}
-\dfrac g{da}&g\left(\dfrac1{d^2}+\dfrac1a\right)\\
-\dfrac1a&\dfrac gd+\dfrac da
\end{pmatrix},\qquad\det N=\frac g{d^2}<0.
}
```

Reflection gives the upper-gate map

```math
\boxed{H=J N^{-1}J,\qquad\det H=d^2/g.}
```

The complete h-step domains used by this pass are

| Source interval | Exact equation |
| --- | --- |
| `0<t<e` | `W(t+h)=N W(t)` |
| `e<t<k-h` | `W(t+h)=M W(t)` |
| `k-h<t<u-h` | `W(t+h)=H W(t)` |

The upper-gate rule follows by applying the lower-gate rule at `u-h-t` and using the exact reflection of W. N and H are **not** individually determinant-one maps. Their determinant factors must be retained.

The unmatched first-cell rows provide the endpoint conditions

```math
(g,-d)W(t)=0\quad (u-h<t<k),
```

and, by reflection,

```math
(-d,g)W(s)=0\quad (e<s<h).
```

These are almost-everywhere identities on intervals. They are not endpoint traces of x.

All algebraic inversions above use only nonzero factors among `a,d,mu,g,Delta`; the numerical enclosure stage certifies their signs. The symbolic stage checks the bridge identity, both h-step row pairs, the gate reflection, and all determinant formulas.

## 5. The two directed internal returns

Now restrict to `lambda_ret<e<=h`. Use the rotation

```math
R(t)=t+\kappa\pmod h
```

and retain an edge only if both its endpoints lie in `(0,e)`.

For `0<t<e-kappa`, follow the h-ladder from `t+kappa` to `t+k`. Its five steps are one N, three M, and one H. Comparing with the k-bridge gives

```math
K W(t)=H M^3 N W(t+\kappa).
```

Therefore

```math
\boxed{
W(t+\kappa)=T_\kappa W(t),\qquad
T_\kappa=N^{-1}M^{-3}H^{-1}K.
}
```

For `lambda_ret<t<e`, put `s=t-lambda_ret`. The h-ladder from s to `t+k=s+6h` has one N, four M, and one H. Consequently

```math
K W(t)=H M^4 N W(t-\lambda_{\rm ret}),
```

and

```math
\boxed{
W(t-\lambda_{\rm ret})=T_{-\lambda}W(t),\qquad
T_{-\lambda}=N^{-1}M^{-4}H^{-1}K.
}
```

Products act rightmost first. In either return matrix the determinants of N and H cancel, giving determinant one.

**The direction is essential:** the two forward edges of this section are `+kappa` and `-lambda_ret`. This pass does not assert a common expanding cone for `+kappa`, `+lambda_ret`, and arbitrary inverses. Reversing the second return is licensed by the exact h-circle section, not chosen merely to improve a numerical spectrum.

This section uses a different quotient from GERM-64's kappa-circle description. Both are compatible with the retained delay lattice. We only need the displayed necessary return equations in the stated parameter range; no complete two-matrix model for the upper chamber is assumed.

## 6. Refolded bulk compression, with the interface now explicit

The derived M has

```math
\operatorname{tr}M=\frac{2a-1+d^2}{da},\qquad\det M=1.
```

Hence the Cayley-Hamilton/Chebyshev identity imported from RETURN-COCYCLE-0 applies in these **proved W-coordinates**:

```math
M^r=U_{r-1}(\operatorname{tr}M/2)M
-U_{r-2}(\operatorname{tr}M/2)I\quad(r\ge1).
```

The verifier checks the characteristic-polynomial identity symbolically. No identification with the old P/J state is required. The return maps still contain N, H, and K; they have not been replaced by powers of M alone.

## 7. Rational common-cone certificate

The companion verifier encloses log2, log3, log5 by exact rational atanh series with a positive tail bound. Square roots use integer-square comparisons. Every arithmetic operation is rounded outward to a rational decimal grid. Printed decimal endpoints are also rounded outward.

It proves the following strict **componentwise** interval boxes:

```math
T_\kappa\in
\begin{pmatrix}(10,11)&(3,4)\\(6,7)&(2,3)\end{pmatrix},
\qquad
T_{-\lambda}\in
\begin{pmatrix}(12,13)&(3,5)\\(9,10)&(2,4)\end{pmatrix}.
```

For orientation, the much narrower recorded enclosures surround

```math
T_\kappa\approx
\begin{pmatrix}
10.309153122&3.301991627\\
6.571660989&2.201884994
\end{pmatrix},
```

```math
T_{-\lambda}\approx
\begin{pmatrix}
12.683390441&3.990450401\\
9.167057295&2.962984356
\end{pmatrix}.
```

Only the rational interval tests, not these approximations or eigenvalue estimates, are load-bearing.

For the real double cones

```math
C_+=\{(X,Y):XY\ge0\},\qquad C_-=\{(X,Y):XY\le0\},
```

each T in the two-map library strictly preserves C+ away from zero and satisfies

```math
\|Tv\|_1\ge5\|v\|_1\quad(v\in C_+).
```

Indeed, every entry is positive and both column sums exceed 5.

Since `det T=1`, its inverse has the form

```math
T^{-1}=\begin{pmatrix}t_{22}&-t_{12}\\-t_{21}&t_{11}\end{pmatrix}.
```

It preserves C- and satisfies

```math
\|T^{-1}v\|_1\ge5\|v\|_1\quad(v\in C_-),
```

because `t22+t21>5` and `t12+t11>5`. These backward bounds are explicitly checked, not inferred from a positive numerical Lyapunov exponent.

## 8. Finite partial-return paths: exact endpoint nonresonance

Assume `lambda_ret<e<h`. Irrationality of `kappa/h` follows from the nonproportional prime-log vectors of h and kappa. The restricted rotation graph on `(0,e)` therefore has no cycles. Every forward and backward orbit eventually enters the nonempty open gap `(e,h)`, so every retained component is a finite directed path. Compactness gives a bound after fixing e, but no bound uniform as `e` tends to h is used.

The exact entry and exit intervals are

```math
I_{\rm in}=(e-\lambda_{\rm ret},\kappa),\qquad
I_{\rm out}=(e-\kappa,\lambda_{\rm ret}).
```

For an entry point t, its h-ladder ends at `t+5h in (u-h,k)`. Thus the top endpoint row gives

```math
\ell_{\rm in}W(t)=0,\qquad
\ell_{\rm in}=(g,-d)M^4N.
```

For an exit point t, `s=t+kappa in (e,h)`. The h-ladder from s to `t+k` and the k-bridge give

```math
W(s)=M^{-4}H^{-1}K W(t).
```

The bottom endpoint row therefore gives

```math
\ell_{\rm out}W(t)=0,\qquad
\ell_{\rm out}=(-d,g)M^{-4}H^{-1}K.
```

The rational audit certifies

```math
\ell_{\rm in,1}\in(-1,-4/5),\quad
\ell_{\rm in,2}\in(13/10,3/2),
```

```math
\ell_{\rm out,1}\in(4,6),\qquad
\ell_{\rm out,2}\in(1,2).
```

Thus a nonzero real entry state in `ker ell_in` has coordinates of the same strict sign. Every legal product of the two positive return matrices preserves that property. But `ell_out` has both coefficients positive, so it cannot annihilate the resulting nonzero exit state. Therefore every finite-path state is zero.

For complex states, `ker ell_in` is the complex span of one strictly positive real vector. A real positive product followed by `ell_out` has a nonzero value on that vector, so the same conclusion holds. Equivalently, apply the real argument to real and imaginary parts.

Consequently

```math
\boxed{W=0\text{ almost everywhere on }(0,e),\qquad
\lambda_{\rm ret}<e<h.}
```

Threshold points and their countably many rotation/affine preimages are null. The argument is made on a common full-measure set on which the required source equations and their iterates hold. No continuity of x or boundary evaluation on a null seam is assumed.

## 9. Full-rotation endpoint: an explicit L2 exclusion proof

At `e=h`, `(0,e)` is the h-circle up to endpoints. The return equation is now

```math
W(Rt)=T(t)W(t),\qquad
T(t)=
\begin{cases}
T_\kappa,&0<t<\lambda_{\rm ret},\\
T_{-\lambda},&\lambda_{\rm ret}<t<h.
\end{cases}
```

The state W belongs to L2 because it is formed from restrictions and a reflection of x. R preserves Lebesgue measure.

For a real-valued W, let `E+` be the set where its coordinates have product at least zero, and `E-` the set where that product is negative. On E+, forward cone invariance gives

```math
\|W(R^nt)\|_1\ge5^n\|W(t)\|_1.
```

Integrating over E+ and using measure preservation yields

```math
5^{2n}\int_{E_+}\|W(t)\|_1^2\,dt
\le\int_0^h\|W(t)\|_1^2\,dt.
```

The right side is finite and independent of n, so W vanishes almost everywhere on E+.

On E-, use the inverse matrices along backward iterates. Backward C- invariance and expansion give the identical estimate with `R^{-n}` in place of `R^n`; hence W also vanishes almost everywhere on E-.

Apply this argument separately to the real and imaginary parts of a complex W. The matrices are real, so both satisfy the same cocycle equation. We have proved

```math
\boxed{W=0\text{ almost everywhere at }e=h.}
```

This is a complete L2 implication for this endpoint cocycle. It does not infer pointwise boundedness of an L2 function on a dense orbit, and it does not rely on a heuristic growth exponent.

## 10. Faithful reconstruction back to the source

It remains to verify that killing W on the lower defect kills the original scalar profile.

For an h-residue `s in (0,e)`, the state W(s) is zero. The invertible h-step library propagates zero through its entire low-head ladder.

If `e<h` and `s in (e,h)`, then, because `e>lambda_ret>kappa`, the point `s+5h` lies in the top strip `(k,k+e)`. Its k-bridge preimage is `s-kappa in (0,e)`, where W is zero. Thus the top state is zero and the invertible h-step maps propagate it backward through the ladder. At `e=h` there is no such gap residue.

Every low-head coordinate is covered almost everywhere. A ladder uses at most six h-steps; no unbounded return-path length enters this reconstruction. Therefore `x=0` on `(0,u)`. Section 2 then gives zero on the middle bands, dead strip, and tail, hence on `(0,w)`.

The observation of the original kernel into the reduced state is therefore injective, with an explicit reconstruction on actual source solutions. We do **not** assert that every unconstrained vector-valued cocycle field lifts to a scalar x; it would also have to satisfy the inherited reflection compatibility. Such surjectivity is unnecessary for the exclusion just proved.

## 11. Source-level regression and execution receipt

The verifier was executed successfully in the working runtime, with exit code zero. It checks:

1. the exact local Schur, bridge, gate, determinant, and characteristic-polynomial identities;
2. all rational matrix and endpoint-covector boxes used in Sections 7-9;
3. the RETURN-COCYCLE-4 31-site skeleton, its exact 124-point affine orbit, and the literal source/block-row correspondence;
4. the RETURN-COCYCLE-5 lower/middle/upper split `186 / 124 / 186`, the 93+93 orientation split, exact reflected upper rows, and row-for-row identification of the middle system with the base system;
5. the external-parity gauge for those source systems and the exact polygon-region inequalities;
6. the algebraic extra term in the above-h scope guard below.

The old 124/186/248/310/372 determinant programs were **not rerun**. The present regressions compare source rows and exact affine topology, not merely dimensions or approximate determinant signs. The new chamber proof uses the two return matrices and endpoint/L2 arguments, not a newly enumerated large determinant library.

Run with assertions enabled:

```text
python tools/sz_mixed_return_cone_audit.py
```

Executed verifier SHA-256:

```text
f43eaf0e86e823a2f7ebeb6580b8ea12fcf4587ad405f708c3b66d6939b2a6c0
```

Its repository blob was read back and matches:

```text
cae5c12c4f4d5c4aa643e001feb8d1cd430ef6f9
```

Recorded output SHA-256:

```text
b08bef7ab49e977a1bf025c23747b78e7ce50c11e5a7c8639245add58b88b920
```

This is a symbolic/rational computational certificate accompanying the written proof. It is not Lean certification or a separate canonical ratification.

## 12. Why the same two matrices are not yet licensed above h

The bridge derivation used `x(j+k+z)=0` for every `0<z<e`. That is valid through e=h, but fails immediately above it.

For

```math
h<e<\min(2h,p-k,j-k),\qquad 0<z<e-h,
```

we instead have `j+k+z=m+h+z in (m,v)`. The exact middle-band formula gives

```math
x(j+k+z)=-\frac b\Delta
[\mu x(h+z)+\varepsilon x(e-h-z)].
```

The top source row consequently becomes

```math
\boxed{
g\,x(k+z)
=\frac d\Delta[\mu x(z)+\varepsilon x(e-z)]
-\frac a\Delta[\mu x(h+z)+\varepsilon x(e-h-z)].
}
```

The second bracket is the new bridge feedback. It is absent from K. On `e-h<z<e`, the earlier dead-strip simplification remains available in this small above-h range, but it is no longer uniform on the whole seed interval.

Thus the current proof has a specific, source-level stopping boundary. We may not carry its K, gate, or two-matrix cocycle formulas into a positive-width above-h interval without controlling this added term and rechecking the state dimension and domains. This scope audit derives the changed row; it does not solve the next interval.

## 13. Experimental status and next individual target

Combining GERM-63 with Sections 8-10 gives

```math
0<e\le h
```

for the post-log(16/3) scalar parity reduction. Hence

```math
L_h=\log(16/3)+h=\log(27/5),
```

and the inherited ambient reconstruction gives

```math
\boxed{\ker P_c=\{0\},\qquad
K_c^{\rm ps}=K_c\cap\ker P_c=\{0\},\qquad
0<L\le\log(27/5).}
```

The `K_c` statement retains its regular-kernel scope. No uniform-in-L kernel norm gap, full-form-domain persistence exclusion, selected-packet custody, or global RH closure is added by this pass.

The remaining four-delay interval is

```math
\boxed{h<e\le j,\quad\text{equivalently}\quad
\log(27/5)<L\le\log6.}
```

Its logarithmic width is p=`log(10/9)`. The later coefficient-pattern change at `e=p` remains inside this unresolved range.

Next individual target:

```text
SZ-KERNEL-EDGE-GERM-66 / POST-h BRIDGE-FEEDBACK TRANSFER
```

Start from the changed bridge row in Section 12. Determine whether the added shifted/reflected seed pair can be eliminated in a norm-controlled, kernel-faithful way, or whether a larger retained state is necessary. Preserve the current directed cone certificate wherever its hypotheses survive; do not restart the old finite-template traversal or reopen the stopped screw shortcut.

```text
GERM-65: COMPLETE AS A SCOPED EXPERIMENTAL PASS
PARTIAL MIXED-RETURN CHAMBER: CLOSED
FULL-ROTATION ENDPOINT e=h: CLOSED
POSITIVE-WIDTH UPPER CHAMBER e>h: OPEN
GERM-66: NOT EXECUTED
CANONICAL THEOREM CURSOR: SZ-CROSS-COLLAR-3, UNCHANGED
RATIFICATION / PUBLIC PROMOTION: NONE
```

This pass supersedes only the pre-65 handoff's pending-next-pass status. The original refold remains the historical source-custody record.
