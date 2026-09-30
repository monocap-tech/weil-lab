# SZ edge recurrence 103 — closure of the post-s15 formula window by seventeenth returns

**Date:** 2026-09-29  
**Branch:** sz-cross-collar  
**Standing:** UNRATIFIED RESIDUE / ONE NF PASS / SCOPED POSITIVE RESULT  
**Canonical parent:** SZ-CROSS-COLLAR-3, unchanged  
**Entry commit:** 26cc010882c02069da2d7298f530e710f116db58  
**Public promotion:** forbidden

## Result

Retain GERM-102's parameter \(z=e-e_{101}\) and write

\[
\varepsilon=z-s_{15}=e-e_{102}.
\]

GERM-103 proves

\[
\boxed{
0<\varepsilon\le t_{15}
\Longrightarrow
x_{\rm source}=0
\text{ in both scalar parity kernels}.
}
\]

Under inherited ambient equivalence and coverage,

\[
\boxed{
L_{103}=L_{102}+t_{15}
=\log\!\left(\frac{3^{616630565}}{2^{701561468}5^{118769764}}\right)
=1.711212516168914336902071568215382674601877004879\ldots .
}
\]

The increment is

\[
t_{15}=0.000000000000027242875184250140717788943911118422\ldots .
\]

The upper endpoint is checked directly. This remains scoped, experimental, and unratified.

## Custody

The GERM-102 verifier is pinned by SHA-256

\`\`\`text
bc9f783b9c9c89072e5c6a468cf29d3dd98e85299bd9cf3cb274f078ea247a5e
\`\`\`

and replayed byte-for-byte against its recorded stdout. The inherited \(10^{240}\) rational grid and 800-term logarithm-series stack are retained.

## Sixteenth transfer

All \(H_1,J_1,J_2\) inputs retain their GERM-102 fifteenth definitions. Define the GERM-103-local sixteenth maps

\[
A_0=H_1^3J_1,\qquad
A_1=H_1^3J_2,\qquad
B_0=H_1^4J_1,\qquad
B_1=H_1^4J_2.
\]

The \(A\)-maps are four-step returns and the \(B\)-maps are five-step returns. The suffix records whether the initial fifteenth source lies outside or inside \(0<y<\varepsilon\).

Every intermediate fifteenth source is checked. At \(\varepsilon=0\), \(A_0/B_0\) recover the GERM-102 endpoint representation. At \(\varepsilon=t_{15}\), only \(A_1/B_1\) survive.

## Seventeenth section

Set

\[
c_{16}=t_{15}-\rho_{16},
\qquad
\rho_{17}=t_{15}-5c_{16},
\qquad
c_{17}=c_{16}-\rho_{17}.
\]

Exact arithmetic gives

\[
0<\rho_{17}<c_{16},
\qquad
5c_{17}+6\rho_{17}=t_{15}.
\]

Use

\[
K_{17}=(0,c_{16}),
\]

with induced map

\[
\boxed{
S_{17}(y)=y+\rho_{17}\pmod{c_{16}}.
}
\]

The first return takes five steps for \(y<c_{17}\) and six for \(y>c_{17}\). The translation branches tile the section.

For \(0<\varepsilon\le c_{16}\), the complete words are

\[
\boxed{
B_0^{N-1}A_i,
\qquad i\in\{0,1\},\quad N\in\{5,6\}.
}
\]

For \(c_{16}\le\varepsilon\le t_{15}\), the initial map is always \(A_1\), and later internal visits form a final consecutive run:

\[
\boxed{
B_1^sB_0^{N-s-1}A_1,
\qquad N\in\{5,6\},\quad0\le s<N.
}
\]

The two \(s=0\) products are shared between the regimes. Thus there are **13 distinct complete temporal products and 15 parameter/chart tests**.

At the final endpoint the surviving complete words are

\[
B_1^4A_1,\qquad B_1^5A_1.
\]

Both pass directly.

## Cone certificate

Use

\[
C_{\rm low}=
\begin{pmatrix}
1&1\\
-2827/2000&-27/20
\end{pmatrix},
\qquad
\det C_{\rm low}=\frac{127}{2000},
\]

and

\[
C_{\rm high}=
\begin{pmatrix}
1&1\\
-279/200&-283/200
\end{pmatrix},
\qquad
\det C_{\rm high}=-\frac1{50}.
\]

The chart is chosen by the fixed parameter and held constant along the orbit. Both charts certify the shared junction.

Every required signed conjugate is strictly positive. The weakest certified bounds are

\[
\text{forward}>21.2185157340,
\qquad
\text{backward}>20.5144189739.
\]

Hence

\[
\boxed{
\|\widehat Mv\|_1\ge20\|v\|_1\quad(v\in C_+),
\qquad
\|\widehat M^{-1}v\|_1\ge20\|v\|_1\quad(v\in C_-).
}
\]

A five-step seventeenth return contains 2,271,842,500,980 original rotation steps; a six-step return contains 2,743,334,531,329. These remain products of \(2\times2\) matrices.

Measure preservation and the forward/backward cone bounds give the usual \(L^2\)-section exclusion. Invertibility and the inherited return towers propagate zero back to the scalar source.

## Endpoint and remaining obligations

Exact arithmetic gives

\[
L_{103}=(-701561468,616630565,-118769764)
\]

in the ordered \((\log2,\log3,\log5)\) basis, and

\[
e_{103}=147080066h-28310302k.
\]

The GERM-102 fourteenth/fifteenth formula remainder is now zero.

The still-licensed GERM-100 eleventh formula remainder is

\[
\omega_{11}
=0.000000000020893371365682198926433019186282259509\ldots .
\]

The remaining width before \(e=3h\) is

\[
3h-e_{103}
=0.000031477398428669305491066588424613339713993483\ldots .
\]

The full unresolved four-delay interval remains \(L_{103}<L\le\log6\).

## Next source change

Immediately beyond \(z=\tau_{14}\), equivalently beyond the GERM-101 formula endpoint \(b=\rho_{12}\), the ten-step twelfth return acquires an interior final eleventh source.

The new chronological word is nine GERM-100-local \(A_1\) steps followed by \(B_1\):

\[
\boxed{
J_{12,\rm next}=B_1A_1^9.
}
\]

Its determinant encloses one and

\[
0.7071860460
<
\operatorname{tr}J_{12,\rm next}
<
0.7071860461,
\]

while

\[
-3.4998878964
<
(\operatorname{tr}J_{12,\rm next})^2-4\det J_{12,\rm next}
<
-3.4998878963.
\]

It is elliptic. This is a newly changed twelfth source species beyond the completed GERM-102 formula window, not an unhandled seventeenth word inside it.

\`\`\`text
GERM-103: COMPLETE AS A SCOPED EXPERIMENTAL PASS
NEW EXCLUSION: 0<epsilon<=t15, epsilon=e-e102
SIXTEENTH FORMULAS: A0/A1/B0/B1 THROUGH THE FULL REMAINING GERM-102 WINDOW
SEVENTEENTH PROOF: 13 DISTINCT WORDS / 15 TESTS / TWO RATIONAL CHARTS
COMMON CONE FACTOR: 20
GERM-102 FORMULA WINDOW: CLOSED THROUGH z=tau14
EXPERIMENTAL ENDPOINT: log(3^616630565/(2^701561468*5^118769764))
NEXT TWELFTH WORD: GERM-100-LOCAL B1 A1^9; ELLIPTIC
GERM-104 / POST-z=TAU14 TWELFTH FINAL-VISIT TRANSFER: NOT EXECUTED
CANONICAL CURSOR: SZ-CROSS-COLLAR-3, UNCHANGED
RATIFICATION / PUBLIC PROMOTION: NONE
\`\`\`
