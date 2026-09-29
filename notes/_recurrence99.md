# SZ edge recurrence 99 — closure of the post-delta13 thirteenth window

**Date:** 2026-09-29  
**Branch:** sz-cross-collar  
**Standing:** UNRATIFIED RESIDUE / ONE NF PASS / SCOPED POSITIVE RESULT  
**Canonical parent:** SZ-CROSS-COLLAR-3, unchanged  
**Entry commit:** 4b9f4e294939410bd542ef1e427faf3e0c61e2ea  
**Public promotion:** forbidden

## Result

Retain GERM-98's parameter \(v=u-c_{11}=e-e_{97}\) and write

\[
x=v-\delta_{13}=e-e_{98}.
\]

GERM-99 proves

\[
\boxed{0<x\le2\rho_{12}\Longrightarrow x_{\rm source}=0
\text{ in both scalar parity kernels}.}
\]

Equivalently,

\[
\delta_{13}<v\le\omega_{11}.
\]

Under the inherited ambient equivalence and coverage,

\[
\boxed{L_{99}=L_{98}+2\rho_{12}
=\log\!\left(\frac{2^{1020029612}5^{172684332}}{3^{896545004}}\right)
=1.711212515970572212598163580836392014764434228\ldots.}
\]

The increment is

\[
2\rho_{12}=0.000000000020603564025536394082186974321804882\ldots.
\]

The endpoint \(v=\omega_{11}\) is checked directly. This closes the remaining GERM-98 eleventh-formula window, but not the larger GERM-97 tenth window, the three-layer interval, or the four-delay target.

## Custody

The GERM-98 verifier is pinned by SHA-256

```text
9cf48a34efe672d09edd083d32c3d8e17e45d8dbd0a7d37c0e029412d8ab15c7
```

and replayed before the pass with its recorded stdout. Canonical authority remains `SZ-CROSS-COLLAR-3`; GERM-72 and GERM-87 corrections remain in force.

## Extended twelfth maps

All `A/D/E` inputs below retain their GERM-98-local eleventh definitions. GERM-99 requires

\[
D_{10}=DA^9,\quad E_{10}=EA^9,\quad
D_{11}=DA^{10},\quad E_{11}=EA^{10}.
\]

The twelfth section remains \((0,\omega_{11})\). For a ten-step source \(y\), the final eleventh source is exterior iff \(y>\rho_{12}+v\). For an eleven-step source it is exterior iff \(y+\omega_{12}>v\). All intermediate eleventh arguments are checked.

At \(v=\omega_{11}\), the exterior twelfth species disappear and `E10/E11` survive.

## Six complete thirteenth species

The thirteenth section remains \(K_{13}=(0,\rho_{12})\), with

\[
S_{13}(y)=y+\delta_{13}\pmod{\rho_{12}}.
\]

Exactly six complete temporal products occur:

\[
\begin{array}{lll}
A_0=D_{10}D_{11}, & A_1=E_{10}D_{11}, & A_2=E_{10}E_{11},\\
B_0=E_{10}D_{10}D_{11}, & B_1=E_{10}^2D_{11}, & B_2=E_{10}^2E_{11}.
\end{array}
\]

Chronology is stored explicitly in the verifier; products act rightmost first. The complete source partition is

```text
I   delta13 < v < rho12                 : A0, A1, B0
II  rho12 < v < omega12                 : A1, B0, B1
III omega12 < v < omega11-delta13       : A1, A2, B1
IV  omega11-delta13 < v < omega11       : A2, B1, B2
```

The three internal junctions retain `A1/B0`, `A1/B1`, and `A2/B1`. At the entry face `A0/B0` recover GERM-98's endpoint representation; at the terminal face only `A2/B2` survive. Every cell, junction, and endpoint is checked against the lower source equations.

## Cone certificate

The GERM-98 chart survives unchanged:

\[
C_{99}=\begin{pmatrix}-27&-145\\40&-488\end{pmatrix}.
\]

Use signs

```text
A0 +, A1 -, A2 +, B0 +, B1 -, B2 +.
```

Every signed conjugate is strictly positive under outward-rational arithmetic. The weakest certified forward factor is

\[
>8{,}339{,}804.0046873668,
\]

and the weakest backward factor is

\[
>4{,}581{,}789.5030899796.
\]

Hence the deliberately weakened common estimate is

\[
\boxed{\|\widehat Mz\|_1\ge10^6\|z\|_1,
\qquad\|\widehat M^{-1}z\|_1\ge10^6\|z\|_1.}
\]

The chart is fixed for every parameter and orbit point. No fourteenth section and no new retained coordinate are introduced.

Measure preservation on the thirteenth section and the forward/backward estimates exclude a nonzero \(L^2\) section. Invertibility propagates zero through the twelfth and eleventh circles and then through the inherited lower return hierarchy to the scalar source.

## Remaining scope

Exact arithmetic gives

\[
L_{99}=(1020029612,-896545004,172684332)
\]

in the ordered \((\log2,\log3,\log5)\) basis, equivalently

\[
e_{99}=-213845867h+41161535k.
\]

The GERM-98 eleventh formula remainder is now zero. The still-licensed GERM-97 tenth formula remainder is

\[
0.000000000657706487008770558916271037071175109\ldots,
\]

and the remaining width before \(e=3h\) is

\[
0.000031477596770793609399053967415273177156770\ldots.
\]

No exclusion above \(L_{99}\) is claimed.

## Next source change

Immediately above \(v=\omega_{11}\), a four-step eleventh return changes its last GERM-97 level-10 factor. The new chronological word is

```text
A1,B0,B0,B1
```

with matrix

\[
J_{11,\rm next}=B_1B_0^2A_1.
\]

Its coefficient spectrum is certified:

\[
1.6348865854<\operatorname{tr}J_{11,\rm next}<1.6348865855,
\]

\[
-1.3271458527<(\operatorname{tr}J_{11,\rm next})^2-4\det J_{11,\rm next}
<-1.3271458526.
\]

It is elliptic. The source-strip description is a handoff, not load-bearing to the GERM-99 theorem; GERM-100 must rederive that changed eleventh partition before using it.

```text
GERM-99: COMPLETE AS A SCOPED EXPERIMENTAL PASS
NEW EXCLUSION: delta13<v<=omega11; equivalently 0<x<=2rho12, x=e-e98
TWELFTH MAPS: D10/E10/D11/E11
THIRTEENTH MAPS: SIX SPECIES; UNCHANGED GERM-98 CHART; FACTOR 10^6
GERM-98 ELEVENTH FORMULA WINDOW: CLOSED
NEXT ELEVENTH WORD: B1 B0^2 A1; ELLIPTIC
GERM-100: NOT EXECUTED
CANONICAL CURSOR: SZ-CROSS-COLLAR-3, UNCHANGED
RATIFICATION / PUBLIC PROMOTION: NONE
```
