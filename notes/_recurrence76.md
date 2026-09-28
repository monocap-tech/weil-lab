# SZ edge recurrence 76 — fifteenth-visit control by a seventh exterior return

**Date:** 2026-09-28  
**Branch:** sz-cross-collar  
**Standing:** UNRATIFIED RESIDUE / ONE NF PASS / SCOPED POSITIVE RESULT  
**Canonical parent:** SZ-CROSS-COLLAR-3, unchanged  
**Entry commit:** 39da808600e0b7edee589317bf0baf396c103bba  
**Public promotion:** forbidden

## 0. Result and exact scope

The fifteenth-visit sixth-return matrix identified at the end of GERM-75 is genuinely elliptic, but its legal forced neighbors admit a new exterior first-return section with a common cone certificate.

\[
\boxed{
3h-\beta+14\xi<e\le3h-\beta+14\xi+\eta_7
\Longrightarrow
x=0
\text{ in both scalar parity kernels},
}
\]

where

\[
\eta_7=\xi-\omega.
\]

Together with the inherited GERM-63/65–75 coverage and GERM-60 reconstruction, the experimental ambient endpoint becomes

\[
\boxed{
L_{76}
=
\log\!\left(
\frac{3^{1222107}}{2^{1390428}5^{235392}}
\right)
=
1.7112120261385615638\ldots.
}
\]

The upper endpoint is included. This remains a scoped, unratified source-equation result. No exclusion above \(L_{76}\), canonical ratification, full-form-domain persistence theorem, selected-packet custody theorem, or RH conclusion is asserted.

Companion records are docs/TERMINOLOGY_GERM76.md, tools/sz_fifteen_visit_forced_neighbor_audit.py, and notes/_recurrence76_audit.json.

## 1. Source custody

The GERM-72 source-word correction remains in force. GERM-75 already proves the typed third-, fourth-, fifth-, and sixth-section source contracts used here. This pass does not rebuild those layers or restart flat orbit enumeration.

Only the three sixth-return atoms adjacent to the new boundary are needed:

\[
A_{19}=B_{14,19},
\qquad
A_{20}=B_{14,20},
\qquad
E_{20}=B_{15,20}.
\]

Here \(E_{20}\) is the first fifteenth-visit atom. GERM-75 certifies it as projectively elliptic, so no generator-wise expanding-cone claim is made for it.

The verifier pins the GERM-75 verifier SHA-256

~~~text
805831ec2a937babcd3bb37a4528af22fc17cdade5dcee032befb592a79149fd
~~~

and freshly recalculates the physical matrices through the inherited outward-rational source solver on the \(10^{60}\) grid.

## 2. Seventh residual scale

Define

\[
\eta_7=\xi-\omega,
\qquad
\chi_7=2\omega-\xi,
\qquad
\psi_7=2\xi-3\omega.
\]

Exact prime-power comparisons certify

\[
0<\psi_7<\chi_7<\eta_7<\omega<\xi,
\]

and

\[
\boxed{
\eta_7=\chi_7+\psi_7,
\qquad
\omega=\eta_7+\chi_7,
\qquad
\xi=2\eta_7+\chi_7.
}
\]

In the \((h,k)\) basis,

\[
\begin{aligned}
\xi&=8593h-1654k,\\
\omega&=-161724h+31129k,\\
\eta_7&=170317h-32783k,\\
\chi_7&=-332041h+63912k,\\
\psi_7&=502358h-96695k.
\end{aligned}
\]

For orientation only,

\[
\eta_7\approx1.41255895869\times10^{-7},
\quad
\chi_7\approx1.03546881292\times10^{-7},
\quad
\psi_7\approx3.77094693249\times10^{-8}.
\]

Write the GERM-75 overlap width as

\[
\zeta=14\xi+d.
\]

The present pass treats

\[
\boxed{0<d\le\eta_7.}
\]

The domain audit verifies that this whole strip remains inside the GERM-75 sixth-section formula scope.

## 3. Seventh exterior section

In the GERM-75 sixth-section circle \(0<y<\xi\), choose

\[
\mathcal U_7=(2\eta_7,\xi).
\]

Set

\[
y=2\eta_7+z,
\qquad
0<z<\chi_7.
\]

The first return takes either three or five sixth-return steps:

\[
N(z)=
\begin{cases}
3,&\psi_7<z<\chi_7,\\
5,&0<z<\psi_7.
\end{cases}
\]

In the \(z\)-coordinate,

\[
\boxed{
S_7(z)=z-\psi_7\pmod{\chi_7}.
}
\]

The two translation images tile the \(\chi_7\)-circle up to endpoints, so \(S_7\) is invertible and Lebesgue-measure preserving.

## 4. Five legal complete words

For the three-step branch:

~~~text
3out : A20, A20, A19
3in  : A20, E20, A19
~~~

For the five-step branch:

~~~text
5out : A20, A20, A19, A20, A19
5one : A20, E20, A19, A20, A19
5two : A20, E20, A19, E20, A19
~~~

Every intermediate source is checked against the already-proved GERM-75 sixth-return contract, and every affine output is required to equal the next input exactly. The endpoint \(d=\eta_7\) is checked directly.

The three-step words contain 96,695 original rotation steps. The five-step words contain 160,607. These are temporal products of \(2\times2\) matrices, not matrices of those dimensions.

## 5. Common rational cone certificate

Use

\[
C_{76}=
\begin{pmatrix}
1&1\\
-5/2&-3
\end{pmatrix}.
\]

Fresh outward rational arithmetic proves every entry of \(C_{76}^{-1}BC_{76}\) strictly positive for all five complete returns. No overall sign change is needed.

| word | forward factor | backward factor |
| --- | ---: | ---: |
| 3out | \(>76.4809175528\) | \(>105.3357346073\) |
| 3in | \(>12.5150991391\) | \(>12.0261122779\) |
| 5out | \(>1586.8816360261\) | \(>2186.7783511693\) |
| 5one | \(>207.1842039116\) | \(>287.9598515422\) |
| 5two | \(>30.8054906505\) | \(>25.4734915551\) |

Hence

\[
\boxed{
\|B'z\|_1\ge12\|z\|_1
\quad(z\in C_+),
\qquad
\|(B')^{-1}z\|_1\ge12\|z\|_1
\quad(z\in C_-).
}
\]

The factor 12 is per complete seventh return, not per original step and not an expanding norm for \(E_{20}\) alone.

## 6. L2 exclusion and reconstruction

Restrict the inherited two-coordinate scalar-source observation to \(\mathcal U_7\) and apply \(C_{76}^{-1}\). This remains an \(L^2\) field.

On a common full-measure source set, the certified equations give the induced seventh-return recurrence. Forward expansion on the same-sign cone and backward inverse expansion on the opposite-sign cone, together with measure preservation, imply vanishing almost everywhere by the same integral argument used in the preceding passes.

The invertible sixth-return atoms then propagate zero to the full GERM-75 sixth circle. The inherited finite reconstruction propagates zero through the fifth, fourth, third, second, and first sections, the \(h\)-circle, low head, middle bands, and tail.

All reconstruction statements concern actual source solutions; no surjectivity from arbitrary vector cocycles is assumed.

## 7. Endpoint arithmetic

The GERM-75 endpoint is

\[
e_{75}=3h-\beta+14\xi.
\]

Adding \(\eta_7\) gives

\[
e_{76}=3h-\beta+14\xi+\eta_7
=291500h-56108k.
\]

Therefore

\[
L_{76}
=
-1390428\log2
+1222107\log3
-235392\log5,
\]

equivalently

\[
\boxed{
L_{76}
=
\log\!\left(
\frac{3^{1222107}}{2^{1390428}5^{235392}}
\right).
}
\]

Numerically,

\[
L_{76}=1.7112120261385615638\ldots.
\]

The remaining distance to the inherited local three-layer endpoint is

\[
3h-e_{76}\approx3.19674287814\times10^{-5}.
\]

In the same unratified experimental scope,

\[
\boxed{
\ker P_c=\{0\},
\qquad
K_c^{\rm ps}=K_c\cap\ker P_c=\{0\},
\qquad
0<L\le L_{76}.
}
\]

The \(K_c\) conclusion retains its regular-kernel scope.

## 8. Exact stopping word

Immediately above \(d=\eta_7\), the seventh-section source itself enters the overlap. On the certified first new strip the required five-step word is

~~~text
E20, E20, A19, E20, A19
~~~

with positive determinant and

\[
-1.2071973591<
\operatorname{tr}B_{\rm next}
<-1.2071973590,
\]

\[
-2.5426745365<
(\operatorname{tr}B_{\rm next})^2-4\det B_{\rm next}
<-2.5426745364.
\]

Thus the immediate new complete return is projectively elliptic. It cannot simply join the present common expanding-cone library. This does not construct a nonzero kernel and does not rule out another forced-neighbor induction.

The remaining already-derived three-layer range is

\[
3h-\beta+14\xi+\eta_7<e\le3h.
\]

The full unresolved four-delay range remains \(L_{76}<L\le\log6\).

## 9. Execution receipt

Run with assertions enabled:

~~~text
python tools/sz_fifteen_visit_forced_neighbor_audit.py
~~~

The verifier replayed successfully with exit code zero, and the replay output was byte-identical to the recorded successful output.

Verifier SHA-256:

~~~text
f823d55f9bc9f27b00c89d6d766c526fa44cc4c1ed11cc897ffd2758328a6bbc
~~~

Repository Git blob:

~~~text
e50144183dd2dd663f62c022dac8ee42df27812e
~~~

Complete indented stdout SHA-256:

~~~text
72a11e4cbf603b0aacc8b5f1b47a9edbcea56b20b668d7198262a76a275586b7
~~~

The full parent symbolic suites, full GERM-60 reduction, and old large determinant inventory were not rerun. This is a rational computational certificate accompanying the written source-domain and \(L^2\) proof, not Lean certification or canonical ratification.

## 10. Next individual target

~~~text
SZ-KERNEL-EDGE-GERM-77 / SEVENTH-SECTION SELF-OVERLAP CONTROL
~~~

Start from the new elliptic five-step word and its exact activation strip. Preserve the GERM-72 correction, typed compositional source domains, physical translations, and the current three-layer formula boundary.

~~~text
GERM-76: COMPLETE AS A SCOPED EXPERIMENTAL PASS
FIFTEENTH-VISIT ELLIPTIC ATOM: ABSORBED BY FORCED NEIGHBORS
SEVENTH EXTERIOR SECTION: FIVE COMPLETE WORDS
COMMON CONE FACTOR: 12
NEW EXCLUSION: 0<d<=eta7
EXPERIMENTAL ENDPOINT: L=log(3^1222107/(2^1390428*5^235392))
FIRST ABOVE-SCOPE SEVENTH WORD: PROJECTIVELY ELLIPTIC
THREE-LAYER LOCAL FORMULAS: STILL AVAILABLE THROUGH e=3h
GERM-77: NOT EXECUTED
CANONICAL THEOREM CURSOR: SZ-CROSS-COLLAR-3, UNCHANGED
RATIFICATION / PUBLIC PROMOTION: NONE
~~~
