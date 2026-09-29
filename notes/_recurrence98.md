# SZ edge recurrence 98 — post-c11 last-visit transfer through a thirteenth section

**Date:** 2026-09-29  
**Branch:** sz-cross-collar  
**Standing:** UNRATIFIED RESIDUE / ONE NF PASS / SCOPED POSITIVE RESULT  
**Canonical parent:** SZ-CROSS-COLLAR-3, unchanged  
**Entry commit:** 4b1c24633f9e06b523857529c868ae36714e70a0  
**Public promotion:** forbidden

## 0. Result and exact scope

The changed last visit in the GERM-97 five-step eleventh return is incorporated. The resulting twelfth maps do not share the preceding single cone directly, but their legally forced first returns to a thirteenth section do. Three complete thirteenth words admit one signed rational cone, without adding a retained state coordinate.

Retain

\[
u=e-e_{96},\qquad v=u-c_{11}=e-e_{97}.
\]

Define

\[
\rho_{12}=c_{11}-10\omega_{11},\qquad
\omega_{12}=\omega_{11}-\rho_{12},\qquad
\boxed{\delta_{13}=\omega_{12}-\rho_{12}>0.}
\]

The new scalar-source result is

\[
\boxed{
0<v\le\delta_{13}
\quad\Longrightarrow\quad
x=0
\text{ in both scalar parity kernels}.
}
\]

Under the inherited ambient equivalence and coverage,

\[
\boxed{
L_{98}=L_{97}+\delta_{13}
=\log\!\left(\frac{2^{29136426436}5^{4932606194}}{3^{25609175812}}\right)
=1.7112125159499686485726271867542050404426\ldots.
}
\]

The increment is

\[
\delta_{13}=0.0000000000002898073401458048442460448644\ldots.
\]

The upper endpoint is included by direct source-domain checks. This is a scoped, unratified source-equation result. It does not close the larger three-layer interval ending at \(e=3h\), the four-delay interval ending at \(L=\log6\), or any RH-level obligation.

Companion records: [terminology](../docs/TERMINOLOGY_GERM98.md), [verifier](../tools/sz_post_u_c11_eleventh_last_visit_audit.py), and [execution receipt](_recurrence98_audit.json).

## 1. Custody and entry replay

The live private branch matched the entry pin before the pass. Canonical authority remains `notes/SZ_CROSS_COLLAR_RATIFICATION_20260926.md`, whose canonical head is `SZ-CROSS-COLLAR-3`. The pre-65 refold and GERM-72 / GERM-87 corrections remain in force.

The GERM-97 verifier is pinned by SHA-256

```text
a550c7ac2c8b4baaa69ea8823fcaa6f2da313b4370f7126cd8fe362a2d48a196
```

and replayed with assertions enabled. Its output SHA-256 was

```text
121afe9e00c4ed9445219502d0f7097a1c73824af4d5ca7a6a35da4b6552cfdb
```

matching the GERM-97 receipt byte for byte. This is an executable custody check, not canonical ratification.

The GERM-98 verifier freshly recomputes the physical matrices through the paired-source outward-rational solver at grid \(10^{120}\), using 400 logarithm-series terms with explicit remainders. GERM-71 interval boxes are regression targets, not rounded proof inputs.

## 2. Eleventh transfer after \(u=c_{11}\)

All `A1/B0/B1` inputs in this section are GERM-97-local level-10 matrices. Put

\[
k=c_{11}-\omega_{11}.
\]

For

\[
0<v\le\delta_{13}<\omega_{11},
\]

the eleventh section is still \((0,c_{11})\). The four-step branch has source \(0<y<k\) and the five-step branch has \(k<y<c_{11}\).

The four-step word is unchanged:

\[
A=B_0^3A_1,
\]

chronologically `A1,B0,B0,B0`.

On the five-step branch, only the final pre-return level-10 source can change on the present parameter strip. Thus

\[
D=B_0^4A_1
\]

for \(k+v<y<c_{11}\), while

\[
\boxed{E=B_1B_0^3A_1}
\]

for \(k<y<k+v\). The latter is precisely the changed word identified by GERM-97.

Every intermediate level-10 source is substituted into its GERM-97 contract, every affine output is matched to the next input, and absence of an earlier eleventh-section return is checked. At \(v=0\), \(A/D\) recover the GERM-97 endpoint representation. At the present upper endpoint, \(A/E\) are checked directly.

The new map \(E\) remains elliptic. No individually expanding real cone for \(E\) is claimed.

## 3. Twelfth maps on the present strip

Retain the twelfth circle \((0,\omega_{11})\). Its return times are ten and eleven because

\[
10\omega_{11}<c_{11}<11\omega_{11}.
\]

Set

\[
\rho_{12}=c_{11}-10\omega_{11},
\qquad
\omega_{12}=\omega_{11}-\rho_{12}.
\]

On the present much smaller parameter interval \(v\le\delta_{13}<\omega_{12}\), the eleven-step branch always ends in \(D\). The ten-step branch ends in \(E\) only on the thin source strip created by \(v\). The three relevant complete twelfth matrices are therefore

\[
D_{10}=DA^9,
\qquad
E_{10}=EA^9,
\qquad
D_{11}=DA^{10}.
\]

The twelfth map remains

\[
y\mapsto y+\omega_{12}\pmod{\omega_{11}}
=y-\rho_{12}\pmod{\omega_{11}}.
\]

All three source cells are checked against the new eleventh contracts.

## 4. Thirteenth section and exact return words

Because

\[
\omega_{12}>\rho_{12},
\]

choose

\[
K_{13}=(0,\rho_{12}).
\]

Define

\[
\delta_{13}=\omega_{12}-\rho_{12},
\qquad
c_{13}=\rho_{12}-\delta_{13}.
\]

For a source \(0<y<\rho_{12}\), the first twelfth step goes to \(y+\omega_{12}\), outside \(K_{13}\). The second step returns if \(y<c_{13}\); otherwise one further step is required. Thus the induced map is

\[
\boxed{S_{13}(y)=y+\delta_{13}\pmod{\rho_{12}}.}
\]

The exact tower identity is

\[
2c_{13}+3\delta_{13}=\omega_{11}.
\]

For \(0<v\le\delta_{13}\), the complete words are exactly

\[
\boxed{
A_{13}=D_{10}D_{11},
\qquad
D_{13}=D_{10}^{2}D_{11},
\qquad
E_{13}=E_{10}D_{10}D_{11}.
}
\]

Chronologically they are `D11,D10`, `D11,D10,D10`, and `D11,D10,E10`. The final \(E_{10}\) visit in the third word occurs exactly on the source interval created by \(v\); it is not favorable padding. Products act rightmost first.

At \(v=0\), \(A_{13}/D_{13}\) survive. At \(v=\delta_{13}\), \(A_{13}/E_{13}\) survive. Both endpoint faces and every intermediate lower source contract are checked directly.

## 5. One signed rational cone

Use

\[
C_{98}=
\begin{pmatrix}
-27&-145\\
40&-488
\end{pmatrix},
\qquad
\det C_{98}=18976.
\]

Use signs \(+1,-1,+1\) for \(A_{13},D_{13},E_{13}\), respectively. Fresh outward rational arithmetic proves every entry of each signed conjugate strictly positive.

The certified lower factors are enormous. The weakest forward factor exceeds

\[
98{,}470{,}565.0909,
\]

and the weakest backward factor exceeds

\[
29{,}837{,}698{,}051{,}318.5.
\]

The theorem deliberately records only

\[
\boxed{
\|\widehat M z\|_1\ge10^6\|z\|_1\quad(z\in C_+),
\qquad
\|\widehat M^{-1}z\|_1\ge10^6\|z\|_1\quad(z\in C_-).
}
\]

The actual overall signs remain in the recurrence; simultaneous negation preserves both double cones and the norm. All three complete thirteenth matrices are hyperbolic, but hyperbolicity alone is not the proof. Positivity and both growth directions are certified separately.

No fourteenth section and no additional retained coordinate are used.

## 6. \(L^2\) exclusion and reconstruction

For an actual scalar source restrict the inherited two-coordinate observation to \(K_{13}\) and apply \(C_{98}^{-1}\). This remains an \(L^2\) field.

The domain-certified source equations give the signed thirteenth recurrence almost everywhere. Remove the inherited exceptional sets and their countably many required affine/rotation preimages before iteration. No classical endpoint trace is introduced.

Forward cone invariance, the factor \(10^6\), and measure preservation force vanishing on the same-sign cone by the usual integral argument. The inverse estimate gives vanishing on the opposite-sign cone. Apply the real argument separately to real and imaginary parts for complex scalar profiles.

The thirteenth first-return towers cover the twelfth circle up to null boundaries. Invertibility then propagates zero through the twelfth, eleventh, tenth, ninth, eighth, seventh, and sixth circles. The inherited finite reconstruction covers the \(h\)-circle, head, middle bands, and tail. All statements concern actual scalar-source solutions; no arbitrary-vector surjectivity is assumed.

## 7. Endpoint arithmetic and remaining scope

Exact prime-log arithmetic gives

\[
\delta_{13}
=(29487130972,-25917424123,4991978177)
\]

in the ordered \((\log2,\log3,\log5)\) basis, and

\[
e_{98}=-6108356401h+1175750207k.
\]

Therefore

\[
L_{98}
=(29136426436,-25609175812,4932606194),
\]

which is the logarithm displayed in Section 0.

The remaining width in the current eleventh formula window is

\[
\omega_{11}-\delta_{13}=2\rho_{12}
\approx2.06035640255\times10^{-11}.
\]

The larger remaining sixth/seventh formula width is approximately

\[
1.41043434263\times10^{-7},
\]

and the remaining width before \(e=3h\) is

\[
3h-e_{98}
=0.0000314776173743576349354480496022474989\ldots.
\]

The full unresolved four-delay interval remains \(L_{98}<L\le\log6\). None of these larger intervals is claimed closed.

## 8. Exact next source change

Immediately above the new endpoint write

\[
v=\delta_{13}+x,
\qquad0<x<\rho_{12}-\delta_{13}.
\]

For \(0<y<x\), the first later twelfth source in the two-step thirteenth return switches from \(D_{10}\) to \(E_{10}\). The new chronological word is

```text
D11,E10
```

with matrix

\[
\boxed{J_{13,\mathrm{next}}=E_{10}D_{11}.}
\]

Every lower source contract and the first-return condition are checked on that strip. The matrix has determinant one and certified

\[
-725770969.5804560826
<\operatorname{tr}J_{13,\mathrm{next}}
<-725770969.5804560825,
\]

with strictly positive discriminant. It is **hyperbolic**. The stop is therefore a changed thirteenth source word beyond the completed interval, not an elliptic no-go or a nonzero-kernel construction.

## 9. Execution and stopping state

The GERM-97 entry verifier replayed with its recorded output byte for byte. The GERM-98 verifier then passed the fresh physical coefficient calculation, composed level-10 contracts, new eleventh and twelfth cells, all three thirteenth source cells, all cone certificates, entry and endpoint faces, the next-word guard, and independent endpoint arithmetic.

A second execution reproduced the output byte for byte. Full lower symbolic suites, the complete GERM-60 ambient reduction, and old large determinant inventories were not rerun. Midpoint reconnaissance was used only to locate a rational chart; all final signs, domains, and coefficient inequalities are exact or outward rational. This is not Lean certification or canonical ratification.

Next individual target:

```text
SZ-KERNEL-EDGE-GERM-99 / POST-v=DELTA13 THIRTEENTH TWO-STEP TRANSFER
```

```text
GERM-98: COMPLETE AS A SCOPED EXPERIMENTAL PASS
NEW EXCLUSION: 0<v<=delta13, v=e-e97
DELTA13: omega12-rho12
THIRTEENTH SECTION: THREE COMPLETE WORDS; ONE SIGNED RATIONAL CHART; FACTOR 10^6
FOURTEENTH INDUCTION / NEW RETAINED COORDINATES: NONE
EXPERIMENTAL ENDPOINT: log(2^29136426436*5^4932606194/3^25609175812)
NEXT COMPLETE WORD: E10 D11; HYPERBOLIC
GERM-99: NOT EXECUTED
CANONICAL CURSOR: SZ-CROSS-COLLAR-3, UNCHANGED
RATIFICATION / PUBLIC PROMOTION: NONE
```
