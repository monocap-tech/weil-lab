# SZ edge recurrence 72 — third-section self-overlap and fourth exterior return

**Date:** 2026-09-28  
**Branch:** sz-cross-collar  
**Standing:** UNRATIFIED RESIDUE / ONE NF PASS / SCOPED POSITIVE RESULT  
**Canonical parent:** SZ-CROSS-COLLAR-3, unchanged  
**Immediate input:** GERM-71, retaining the pre-65 refold  
**Public promotion:** forbidden

## 0. Result and exact scope

The exterior replacement section of GERM-71 may enter the overlap without enlarging the retained source state. In the first self-overlap strip, a fourth exterior section gives three complete legal return words with a very strong common cone certificate.

Define, in addition to the GERM-71 quantities,
[
eta=	heta-alpha=4	heta-	au,
qquad
gamma=alpha-eta=2	au-7	heta.
]
Exact prime-log arithmetic gives
[
0<gamma<eta<alpha<	heta.
]

The new theorem is
[
oxed{
3h-	heta<ele 3h-	heta+gamma
quadLongrightarrowquad
x=0
	ext{ in both scalar parity kernels}.
}
]

With the inherited GERM-63/65--71 coverage and the GERM-60 reconstruction, the experimental ambient endpoint becomes
[
oxed{
0<Lle L_{72}
:=log(16/3)+3h-	heta+gamma
=log!left(rac{3^{7373}}{2^{8384}5^{1421}}ight)
=1.711168966534575ldots.
}
]

This is a scoped, unratified source-equation result. The inherited three-layer local formulas still extend through (e=3h). No exclusion beyond (L_{72}), canonical ratification, full-form-domain persistence theorem, selected-packet custody theorem, or RH proof is asserted.

Entry pin: `monocap-tech/weil-lab@af8faabfec8952d24ab5ad7c31212f7889958e8f`. The parent audit is byte-pinned by SHA-256
[
	exttt{f837da6405cce7a6aff2f67b381e00d9986dad4e41abf142b970dd21357d132b}.
]
This pass propagates its rigorous second-section matrix enclosures by exact Fraction interval arithmetic. It does not rerun the GERM-71 parent symbolic suite or old large determinant inventory.

Companion files:

- [GERM-72 terminology](../docs/TERMINOLOGY_GERM72.md);
- [interval verifier](../tools/sz_third_section_self_overlap_audit.py);
- [recorded audit](_recurrence72_audit.json).

The repository wrapper was not independently executed from a fresh checkout during this NF order. The exact prime-log calculations and the complete Fraction-interval cone calculation recorded below were replayed in the current runtime. This distinction is part of the custody record.

## 1. Final three-layer residual arithmetic

Retain
[
kappa=k-5h,qquad
	au=h-5kappa,qquad
	heta=kappa-8	au,qquad
alpha=	au-3	heta.
]
Now put
[
eta=	heta-alpha,qquad
gamma=alpha-eta.
]

In the ordered prime-log basis ((log2,log3,log5)),
[
egin{aligned}
h&=(-4,4,-1),\
k&=(4,-1,-1),\
kappa&=(24,-21,4),\
	au&=(-124,109,-21),\
	heta&=(1016,-893,172),\
alpha&=(-3172,2788,-537),\
eta&=(4188,-3681,709),\
gamma&=(-7360,6469,-1246).
end{aligned}
]
Direct integer prime-power comparisons certify
[
gamma>0,qquad
eta-gamma>0,qquad
eta>0.
]
Together with the definitions this gives
[
0<gamma<eta<alpha<	heta.
]

Write
[
e=3h-	heta+arepsilon.
]
GERM-72 treats
[
0<arepsilonlegamma.
]
The overlap of the GERM-71 third section is then exactly the interval
[
I_arepsilon=(0,arepsilon)
]
in its (	heta)-circle coordinate.

## 2. Retype the individual third-section step

The inherited third-section rotation is
[
S_3(v)=v-alphapmod	heta.
]
The six second-section maps of GERM-71 are denoted
[
A_2, P_2, E_2^+, D_2, Q_2, E_2^-,
]
according to their source/target overlap bits and wrap type.

Within (0<arepsilonlegamma), only four third-section species are needed.

Their chronological second-section words and exact matrix products are
[
egin{array}{c|c|c}
	ext{type}&	ext{chronological word}&	ext{matrix}\ hline
A_3=00+&D_2,A_2,A_2&A_2^2D_2\
Q_3=01+&Q_2,E_2^+,E_2^+&(E_2^+)^2Q_2\
P_3=10-&E_2^-,E_2^+,E_2^+,P_2&P_2(E_2^+)^2E_2^-\
D_3=00-&D_2,A_2,A_2,A_2&A_2^3D_2.
end{array}
]
Products act rightmost first.

The new (01+) and (10-) types are not guessed continuations of the old seven-word library. They arise because the GERM-71 section itself has started to overlap. Their endpoint bits are retained in the literal inherited second-section words.

From the inherited determinant library,
[
det A_3=det D_3=1,qquad
det Q_3=ho^{-1},qquad
det P_3=ho.
]
The entry/exit factors therefore cancel in every complete return used below.

## 3. The fourth exterior section

Choose
[
mathcal H=(alpha,	heta).
]
It remains exterior to (I_arepsilon) throughout the claimed range because
[
arepsilonlegamma<alpha.
]

Write
[
v=alpha+w,qquad0<w<eta.
]
The first (S_3)-step sends (v) to (w).

Since
[
gamma=alpha-eta,
]
the first return to (mathcal H) takes:

- two (S_3)-steps if (gamma<w<eta);
- three (S_3)-steps if (0<w<gamma).

For (w>gamma),
[
w+eta>alpha,
]
so the second step returns. For (w<gamma),
[
w+eta<alpha,qquad
alpha<w+2eta<	heta,
]
so the third step is the first return.

In the (w)-coordinate the return map is
[
oxed{
S_4(w)=w-gammapmodeta.
}
]
Indeed the two images are
[
(gamma,eta)mapsto(0,eta-gamma),
qquad
(0,gamma)mapsto(eta-gamma,eta),
]
which tile the (eta)-circle up to endpoints. Thus (S_4) is invertible and Lebesgue-measure preserving.

## 4. Exactly three complete return words

Because (arepsilonlegamma<eta), the two-step branch never enters the overlap. Its word is
[
oxed{
B_{2}=D_3A_3,
}
]
chronologically (A_3,D_3).

For the three-step branch, the first target (w) is inside (I_arepsilon) exactly when (w<arepsilon). The next point (w+eta) is always exterior because (eta>arepsilon). Therefore the only two three-step words are
[
oxed{
B_{3,mathrm{out}}=D_3^2A_3,
}
]
for (arepsilon<w<gamma), and
[
oxed{
B_{3,mathrm{in}}=D_3P_3Q_3,
}
]
for (0<w<arepsilon).

At (arepsilon=gamma), the generic (B_{3,mathrm{out}}) interval disappears and the other two types remain. Equality is therefore included directly; no continuity argument is used.

All three complete returns have exact determinant one.

## 5. One rational cone chart

Use
[
C_{72}=
egin{pmatrix}
1&1\
3/5&1/5
end{pmatrix}.
]

Starting only from the pinned outward interval boxes of the GERM-71 six-map library, exact Fraction interval multiplication gives:

[
-C_{72}^{-1}B_2C_{72}
subset
egin{pmatrix}
(138.6456479158,138.6456481957)&(128.0190389956,128.0190392495)\
(138.8089895489,138.8089899871)&(128.1770738091,128.1770742062)
end{pmatrix},
]

[
C_{72}^{-1}B_{3,mathrm{out}}C_{72}
subset
egin{pmatrix}
(3108.6172228332,3108.6172322209)&(2870.4321441993,2870.4321527652)\
(3114.2213552747,3114.2213702897)&(2875.6072046372,2875.6072183309)
end{pmatrix},
]

[
C_{72}^{-1}B_{3,mathrm{in}}C_{72}
subset
egin{pmatrix}
(21.4050844706,21.4050847528)&(22.1953134186,22.1953136812)\
(20.6537200770,20.6537205421)&(21.4629281754,21.4629286083)
end{pmatrix}.
]

Every displayed entry is strictly positive. The interval determinant calculations stay strictly positive without inserting the exact determinant-one identities into the numerical division.

For a positive matrix
[
B=egin{pmatrix}a&b\c&dend{pmatrix}
]
with positive determinant (delta), the same-sign forward (ell^1) factor is at least
[
min(a+c,b+d),
]
and the inverse expands the opposite-sign cone by at least
[
rac{min(d+c,b+a)}{delta}.
]

The deliberately weakened common conclusion is
[
oxed{
|widehat Bz|_1ge40|z|_1quad(zin C_+),
qquad
|widehat B^{-1}z|_1ge40|z|_1quad(zin C_-),
}
]
where
[
C_+={XYge0},qquad C_-={XYle0}.
]
The actual overall sign of (B_2) is retained; simultaneous negation preserves the two double cones and the norm.

The raw certified lower factors are far larger than 40: the weakest complete word still exceeds (42.05) forward and (42.11) backward.

## 6. L2 exclusion and reconstruction

For an actual scalar source define
[
Z(w)=C_{72}^{-1}W(alpha+w),
qquad0<w<eta.
]
Restriction, translation, and the fixed chart are bounded, so (Zin L^2(0,eta)).

The exact source equations and the inherited reductions imply
[
Z(S_4w)=sigma(w)widehat B(w)Z(w)
]
almost everywhere, where (widehat B(w)) is one of the three positive representatives above and (sigma(w)in{pm1}).

Remove the inherited exceptional sets and their countably many required return preimages. No classical endpoint value is introduced.

For a real state split the section into
[
E_+={Z_1Z_2ge0},qquad E_-={Z_1Z_2<0}.
]
Forward cone invariance and measure preservation give
[
40^{2n}int_{E_+}|Z(w)|_1^2,dw
le
int_0^eta|Z(w)|_1^2,dw.
]
The right side is finite and independent of (n), hence (Z=0) almost everywhere on (E_+). The inverse cone estimate gives the same result on (E_-). Real and imaginary parts satisfy the same real matrix equation, so the complex case follows.

Thus (W) vanishes almost everywhere on (mathcal H).

Every point of the complementary interval ((0,alpha)) reaches (mathcal H) after at most two (S_3)-steps: one step if it lies above (gamma), two otherwise. All four local third-section species used here are invertible. Hence (W) vanishes on the full GERM-71 (	heta)-circle.

The bounded reconstruction already proved in GERM-71 then propagates zero through the second and first induced sections, the (h)-circle, the low head, the middle bands, and the tail. No surjectivity from arbitrary vector fields to scalar sources is assumed.

Therefore
[
oxed{
3h-	heta<ele3h-	heta+gamma
Longrightarrow x=0.
}
]

## 7. Endpoint arithmetic

Since
[
	heta=41k-213h,qquad
gamma=1543h-297k,
]
we obtain
[
3h-	heta+gamma
=1759h-338k.
]
Consequently
[
log(16/3)+3h-	heta+gamma
=
-8384log2+7373log3-1421log5,
]
and therefore
[
oxed{
L_{72}
=
log!left(rac{3^{7373}}{2^{8384}5^{1421}}ight).
}
]

Combining with the inherited coverage gives
[
oxed{
ker P_c={0},
qquad
K_c^{m ps}=K_ccapker P_c={0},
qquad
0<Lle L_{72}.
}
]
The (K_c) conclusion retains the regular-kernel scope. The factor 40 is a property of this induced source recurrence, not a new global uniform-in-(L) kernel gap.

## 8. Exact stop: an elliptic two-step return enters

Immediately above the endpoint, write
[
arepsilon=gamma+delta,qquad
0<delta<eta-gamma.
]
On the nonempty strip
[
gamma<w<gamma+delta
]
the two-step branch now enters the overlap on its first target. Its complete word is
[
oxed{
B_{mathrm{changed}}=P_3Q_3.
}
]

Exact interval propagation from the pinned parent boxes gives
[
-1.4091229485
<
operatorname{tr}B_{mathrm{changed}}
<
-1.4091229414,
]
[
0.9999999958
<
det B_{mathrm{changed}}
<
1.0000000042,
]
and
[
-2.0143725531
<
(operatorname{tr}B_{mathrm{changed}})^2
-4det B_{mathrm{changed}}
<
-2.0143724991.
]

Thus the first newly admitted complete return is projectively elliptic. It cannot be appended to the present complete-return expanding-cone library. This is a precise obstruction to this proof mechanism, not a construction of a nonzero kernel and not a no-go for forced-neighbor induction.

The remaining already-derived three-layer range is
[
3h-	heta+gamma<ele3h.
]
Since
[
	heta-gamma=2eta,
]
its width is exactly (2eta). The full unresolved four-delay range remains
[
oxed{
L_{72}<Llelog6.
}
]

## 9. Verification and custody limits

The repository verifier loads only the byte-pinned GERM-71 audit and propagates its rigorous second-section interval boxes using exact Fraction arithmetic. It verifies:

1. the four required retyped third-section words;
2. the three complete fourth-section words;
3. positivity in the rational chart (C_{72});
4. forward and backward cone factors greater than 40;
5. the exact prime-log ordering (0<gamma<eta<alpha<	heta);
6. the endpoint prime-log vector;
7. the negative projective discriminant of the first above-scope word.

The core exact arithmetic and interval computation were replayed successfully in the current runtime. The repository wrapper itself was not independently executed from a fresh checkout during this NF order, and the audit states that fact explicitly. The parent symbolic suites and old large determinants were not rerun.

This is a scoped computational certificate accompanying the written source-domain and (L^2) proof. It is not Lean certification or canonical ratification.

## 10. Next individual target

[
oxed{
	exttt{SZ-KERNEL-EDGE-GERM-73 / FOURTH-SECTION ELLIPTIC-VISIT CONTROL}.
}
]

Start from (B_{mathrm{changed}}=P_3Q_3). Use the forced neighboring fourth-section steps before changing the local layer system. Preserve the three-word result through (arepsilon=gamma). Do not restart flat determinant enumeration or reopen the stopped screw-family route.

```text
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
```
