# SZ edge recurrence 72 — third-section self-overlap and fourth exterior return

**Date:** 2026-09-28  
**Branch:** sz-cross-collar  
**Standing:** UNRATIFIED RESIDUE / ONE NF PASS / SCOPED POSITIVE RESULT  
**Canonical parent:** SZ-CROSS-COLLAR-3, unchanged  
**Immediate input:** GERM-71, retaining the pre-65 refold  
**Public promotion:** forbidden

## 0. Result and exact scope

The exterior replacement section of GERM-71 may enter the overlap without enlarging the retained source state. In the first self-overlap strip, a fourth exterior section gives three complete legal return words with a strong common cone certificate.

Define, in addition to the GERM-71 quantities,

\[
\beta=\theta-\alpha=4\theta-\tau,
\qquad
\gamma=\alpha-\beta=2\tau-7\theta.
\]

Exact prime-log arithmetic gives

\[
0<\gamma<\beta<\alpha<\theta.
\]

The new theorem is

\[
\boxed{
3h-\theta<e\le 3h-\theta+\gamma
\quad\Longrightarrow\quad
x=0
\text{ in both scalar parity kernels}.
}
\]

With the inherited GERM-63/65–71 coverage and the GERM-60 reconstruction, the experimental ambient endpoint becomes

\[
\boxed{
0<L\le L_{72}
:=\log(16/3)+3h-\theta+\gamma
=\log\!\left(
\frac{3^{7373}}{2^{8384}5^{1421}}
\right)
=1.711168966534575\ldots.
}
\]

This is a scoped, unratified source-equation result. The inherited three-layer local formulas still extend through \(e=3h\). No exclusion beyond \(L_{72}\), canonical ratification, full-form-domain persistence theorem, selected-packet custody theorem, or RH proof is asserted.

Entry pin: monocap-tech/weil-lab@af8faabfec8952d24ab5ad7c31212f7889958e8f. The parent audit is byte-pinned by SHA-256

\[
\texttt{f837da6405cce7a6aff2f67b381e00d9986dad4e41abf142b970dd21357d132b}.
\]

This pass propagates its rigorous second-section matrix enclosures by exact Fraction interval arithmetic. It does not rerun the GERM-71 parent symbolic suite or old large determinant inventory.

Companion files:

- [GERM-72 terminology](../docs/TERMINOLOGY_GERM72.md);
- [interval verifier](../tools/sz_third_section_self_overlap_audit.py);
- [recorded audit](_recurrence72_audit.json).

The repository wrapper was not independently executed from a fresh checkout during this NF order. The exact prime-log calculations and the complete Fraction-interval cone calculation recorded below were replayed in the current runtime. This distinction is part of the custody record.

## 1. Final three-layer residual arithmetic

Retain

\[
\kappa=k-5h,\qquad
\tau=h-5\kappa,\qquad
\theta=\kappa-8\tau,\qquad
\alpha=\tau-3\theta.
\]

Now put

\[
\beta=\theta-\alpha,\qquad
\gamma=\alpha-\beta.
\]

In the ordered prime-log basis \((\log2,\log3,\log5)\),

\[
\begin{aligned}
h&=(-4,4,-1),\\
k&=(4,-1,-1),\\
\kappa&=(24,-21,4),\\
\tau&=(-124,109,-21),\\
\theta&=(1016,-893,172),\\
\alpha&=(-3172,2788,-537),\\
\beta&=(4188,-3681,709),\\
\gamma&=(-7360,6469,-1246).
\end{aligned}
\]

Direct integer prime-power comparisons certify

\[
\gamma>0,\qquad
\beta-\gamma>0,\qquad
\beta>0.
\]

Together with the definitions this gives

\[
0<\gamma<\beta<\alpha<\theta.
\]

Write

\[
e=3h-\theta+\varepsilon.
\]

GERM-72 treats

\[
0<\varepsilon\le\gamma.
\]

The overlap of the GERM-71 third section is exactly

\[
I_\varepsilon=(0,\varepsilon)
\]

in its \(\theta\)-circle coordinate.

## 2. Retype the individual third-section step

The inherited third-section rotation is

\[
S_3(v)=v-\alpha\pmod\theta.
\]

The six second-section maps of GERM-71 are denoted

\[
A_2,\ P_2,\ E_2^+,\ D_2,\ Q_2,\ E_2^-,
\]

according to their source/target overlap bits and wrap type.

Within \(0<\varepsilon\le\gamma\), only four third-section species are needed. Their chronological second-section words and exact matrix products are

| type | chronological word | matrix |
| --- | --- | --- |
| \(A_3=00+\) | \(D_2,A_2,A_2\) | \(A_2^2D_2\) |
| \(Q_3=01+\) | \(Q_2,E_2^+,E_2^+\) | \((E_2^+)^2Q_2\) |
| \(P_3=10-\) | \(E_2^-,E_2^+,E_2^+,P_2\) | \(P_2(E_2^+)^2E_2^-\) |
| \(D_3=00-\) | \(D_2,A_2,A_2,A_2\) | \(A_2^3D_2\) |

Products act rightmost first.

The new \(01+\) and \(10-\) types are not guessed continuations of the old seven-word library. They arise because the GERM-71 section itself has started to overlap. Their endpoint bits are retained in the literal inherited second-section words.

From the inherited determinant library,

\[
\det A_3=\det D_3=1,\qquad
\det Q_3=\rho^{-1},\qquad
\det P_3=\rho.
\]

The entry/exit factors therefore cancel in every complete return used below.

## 3. The fourth exterior section

Choose

\[
\mathcal H=(\alpha,\theta).
\]

It remains exterior to \(I_\varepsilon\) throughout the claimed range because

\[
\varepsilon\le\gamma<\alpha.
\]

Write

\[
v=\alpha+w,\qquad0<w<\beta.
\]

The first \(S_3\)-step sends \(v\) to \(w\).

Since

\[
\gamma=\alpha-\beta,
\]

the first return to \(\mathcal H\) takes:

- two \(S_3\)-steps if \(\gamma<w<\beta\);
- three \(S_3\)-steps if \(0<w<\gamma\).

For \(w>\gamma\),

\[
w+\beta>\alpha,
\]

so the second step returns. For \(w<\gamma\),

\[
w+\beta<\alpha,\qquad
\alpha<w+2\beta<\theta,
\]

so the third step is the first return.

In the \(w\)-coordinate the return map is

\[
\boxed{
S_4(w)=w-\gamma\pmod\beta.
}
\]

The two images are

\[
(\gamma,\beta)\mapsto(0,\beta-\gamma),
\qquad
(0,\gamma)\mapsto(\beta-\gamma,\beta),
\]

which tile the \(\beta\)-circle up to endpoints. Thus \(S_4\) is invertible and Lebesgue-measure preserving.

## 4. Exactly three complete return words

Because \(\varepsilon\le\gamma<\beta\), the two-step branch never enters the overlap. Its word is

\[
\boxed{
B_2=D_3A_3,
}
\]

chronologically \(A_3,D_3\).

For the three-step branch, the first target \(w\) is inside \(I_\varepsilon\) exactly when \(w<\varepsilon\). The next point \(w+\beta\) is always exterior because \(\beta>\varepsilon\). Therefore the only two three-step words are

\[
\boxed{
B_{3,\mathrm{out}}=D_3^2A_3,
}
\]

for \(\varepsilon<w<\gamma\), and

\[
\boxed{
B_{3,\mathrm{in}}=D_3P_3Q_3,
}
\]

for \(0<w<\varepsilon\).

At \(\varepsilon=\gamma\), the generic \(B_{3,\mathrm{out}}\) interval disappears and the other two types remain. Equality is included directly; no continuity argument is used.

All three complete returns have exact determinant one.

## 5. One rational cone chart

Use

\[
C_{72}=
\begin{pmatrix}
1&1\\
3/5&1/5
\end{pmatrix}.
\]

Starting only from the pinned outward interval boxes of the GERM-71 six-map library, exact Fraction interval multiplication gives:

\[
-C_{72}^{-1}B_2C_{72}
\subset
\begin{pmatrix}
(138.6456479158,138.6456481957)&(128.0190389956,128.0190392495)\\
(138.8089895489,138.8089899871)&(128.1770738091,128.1770742062)
\end{pmatrix},
\]

\[
C_{72}^{-1}B_{3,\mathrm{out}}C_{72}
\subset
\begin{pmatrix}
(3108.6172228332,3108.6172322209)&(2870.4321441993,2870.4321527652)\\
(3114.2213552747,3114.2213702897)&(2875.6072046372,2875.6072183309)
\end{pmatrix},
\]

\[
C_{72}^{-1}B_{3,\mathrm{in}}C_{72}
\subset
\begin{pmatrix}
(21.4050844706,21.4050847528)&(22.1953134186,22.1953136812)\\
(20.6537200770,20.6537205421)&(21.4629281754,21.4629286083)
\end{pmatrix}.
\]

Every displayed entry is strictly positive. The interval determinant calculations stay strictly positive without inserting the exact determinant-one identities into the numerical division.

For a positive matrix

\[
B=\begin{pmatrix}a&b\\c&d\end{pmatrix}
\]

with positive determinant \(\delta\), the same-sign forward \(\ell^1\) factor is at least

\[
\min(a+c,b+d),
\]

and the inverse expands the opposite-sign cone by at least

\[
\frac{\min(d+c,b+a)}{\delta}.
\]

The deliberately weakened common conclusion is

\[
\boxed{
\|\widehat Bz\|_1\ge40\|z\|_1\quad(z\in C_+),
\qquad
\|\widehat B^{-1}z\|_1\ge40\|z\|_1\quad(z\in C_-),
}
\]

where

\[
C_+=\{XY\ge0\},\qquad C_-=\{XY\le0\}.
\]

The actual overall sign of \(B_2\) is retained; simultaneous negation preserves the two double cones and the norm.

The raw certified lower factors are much larger than 40: the weakest complete word still exceeds \(42.05\) forward and \(42.11\) backward.

## 6. L2 exclusion and reconstruction

For an actual scalar source define

\[
Z(w)=C_{72}^{-1}W(\alpha+w),
\qquad0<w<\beta.
\]

Restriction, translation, and the fixed chart are bounded, so \(Z\in L^2(0,\beta)\).

The exact source equations and inherited reductions imply

\[
Z(S_4w)=\sigma(w)\widehat B(w)Z(w)
\]

almost everywhere, where \(\widehat B(w)\) is one of the three positive representatives above and \(\sigma(w)\in\{\pm1\}\).

Remove the inherited exceptional sets and their countably many required return preimages. No classical endpoint value is introduced.

For a real state split the section into

\[
E_+=\{Z_1Z_2\ge0\},\qquad E_-=\{Z_1Z_2<0\}.
\]

Forward cone invariance and measure preservation give

\[
40^{2n}\int_{E_+}\|Z(w)\|_1^2\,dw
\le
\int_0^\beta\|Z(w)\|_1^2\,dw.
\]

The right side is finite and independent of \(n\), hence \(Z=0\) almost everywhere on \(E_+\). The inverse cone estimate gives the same result on \(E_-\). Real and imaginary parts satisfy the same real matrix equation, so the complex case follows.

Thus \(W\) vanishes almost everywhere on \(\mathcal H\).

Every point of the complementary interval \((0,\alpha)\) reaches \(\mathcal H\) after at most two \(S_3\)-steps: one step if it lies above \(\gamma\), two otherwise. All four local third-section species used here are invertible. Hence \(W\) vanishes on the full GERM-71 \(\theta\)-circle.

The bounded reconstruction already proved in GERM-71 then propagates zero through the second and first induced sections, the \(h\)-circle, the low head, the middle bands, and the tail. No surjectivity from arbitrary vector fields to scalar sources is assumed.

Therefore

\[
\boxed{
3h-\theta<e\le3h-\theta+\gamma
\Longrightarrow x=0.
}
\]

## 7. Endpoint arithmetic

Since

\[
\theta=41k-213h,\qquad
\gamma=1543h-297k,
\]

we obtain

\[
3h-\theta+\gamma
=1759h-338k.
\]

Consequently

\[
\log(16/3)+3h-\theta+\gamma
=
-8384\log2+7373\log3-1421\log5,
\]

and therefore

\[
\boxed{
L_{72}
=
\log\!\left(\frac{3^{7373}}{2^{8384}5^{1421}}\right).
}
\]

Combining with the inherited coverage gives

\[
\boxed{
\ker P_c=\{0\},
\qquad
K_c^{\rm ps}=K_c\cap\ker P_c=\{0\},
\qquad
0<L\le L_{72}.
}
\]

The \(K_c\) conclusion retains the regular-kernel scope. The factor 40 is a property of this induced source recurrence, not a new global uniform-in-\(L\) kernel gap.

## 8. Exact stop: an elliptic two-step return enters

Immediately above the endpoint, write

\[
\varepsilon=\gamma+\delta,\qquad
0<\delta<\beta-\gamma.
\]

On the nonempty strip

\[
\gamma<w<\gamma+\delta
\]

the two-step branch enters the overlap on its first target. Its complete word is

\[
\boxed{
B_{\mathrm{changed}}=P_3Q_3.
}
\]

Exact interval propagation from the pinned parent boxes gives

\[
-1.4091229485
<
\operatorname{tr}B_{\mathrm{changed}}
<
-1.4091229414,
\]

\[
0.9999999958
<
\det B_{\mathrm{changed}}
<
1.0000000042,
\]

and

\[
-2.0143725531
<
(\operatorname{tr}B_{\mathrm{changed}})^2
-4\det B_{\mathrm{changed}}
<
-2.0143724991.
\]

Thus the first newly admitted complete return is projectively elliptic. It cannot be appended to the present complete-return expanding-cone library. This is a precise obstruction to this proof mechanism, not a construction of a nonzero kernel and not a no-go for forced-neighbor induction.

The remaining already-derived three-layer range is

\[
3h-\theta+\gamma<e\le3h.
\]

Since

\[
\theta-\gamma=2\beta,
\]

its width is exactly \(2\beta\). The full unresolved four-delay range remains

\[
\boxed{
L_{72}<L\le\log6.
}
\]

## 9. Verification and custody limits

The repository verifier loads only the byte-pinned GERM-71 audit and propagates its rigorous second-section interval boxes using exact Fraction arithmetic. It verifies:

1. the four required retyped third-section words;
2. the three complete fourth-section words;
3. positivity in the rational chart \(C_{72}\);
4. forward and backward cone factors greater than 40;
5. the exact prime-log ordering \(0<\gamma<\beta<\alpha<\theta\);
6. the endpoint prime-log vector;
7. the negative projective discriminant of the first above-scope word.

The core exact arithmetic and interval computation were replayed successfully in the current runtime. The repository wrapper itself was not independently executed from a fresh checkout during this NF order, and the audit states that fact explicitly. The parent symbolic suites and old large determinants were not rerun.

This is a scoped computational certificate accompanying the written source-domain and \(L^2\) proof. It is not Lean certification or canonical ratification.

## 10. Next individual target

\[
\boxed{
\texttt{SZ-KERNEL-EDGE-GERM-73 / FOURTH-SECTION ELLIPTIC-VISIT CONTROL}.
}
\]

Start from \(B_{\mathrm{changed}}=P_3Q_3\). Use the forced neighboring fourth-section steps before changing the local layer system. Preserve the three-word result through \(\varepsilon=\gamma\). Do not restart flat determinant enumeration or reopen the stopped screw-family route.

~~~text
GERM-72: COMPLETE AS A SCOPED EXPERIMENTAL PASS
THIRD-SECTION SELF-OVERLAP: CONTROLLED THROUGH epsilon=gamma
FOURTH EXTERIOR SECTION: THREE COMPLETE RETURN WORDS
COMMON CONE FACTOR: 40
EXPERIMENTAL ENDPOINT: L=log(3^7373/(2^8384*5^1421))
THREE-LAYER LOCAL FORMULAS: STILL AVAILABLE THROUGH e=3h
FIRST ABOVE-SCOPE COMPLETE WORD: PROJECTIVELY ELLIPTIC
GERM-73: NOT EXECUTED
CANONICAL THEOREM CURSOR: SZ-CROSS-COLLAR-3, UNCHANGED
RATIFICATION / PUBLIC PROMOTION: NONE
~~~
