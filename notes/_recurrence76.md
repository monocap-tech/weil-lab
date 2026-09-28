# SZ edge recurrence 76 — fifteenth-visit control by a seventh exterior return

**Date:** 2026-09-28  
**Branch:** sz-cross-collar  
**Standing:** UNRATIFIED RESIDUE / ONE NF PASS / SCOPED POSITIVE RESULT  
**Canonical parent:** SZ-CROSS-COLLAR-3, unchanged  
**Entry commit:** 39da808600e0b7edee589317bf0baf396c103bba  
**Public promotion:** forbidden

## 0. Result

The first fifteenth-visit sixth-return matrix from GERM-75 is elliptic, but its legal first return to a smaller exterior section necessarily contains surrounding non-elliptic atoms. Grouping the forced sequence restores a uniform cone certificate.

Define

\[
\eta_7=\xi-\omega,\qquad
\chi_7=2\omega-\xi,\qquad
\psi_7=2\xi-3\omega.
\]

The new source-equation theorem is

\[
\boxed{
3h-\beta+14\xi<e\le3h-\beta+14\xi+\eta_7
\Longrightarrow x=0
\text{ in both scalar parity kernels}.
}
\]

Together with inherited coverage and the GERM-60 reconstruction, the experimental ambient endpoint is

\[
\boxed{
L_{76}
=
\log\!\left(
\frac{3^{1222107}}
{2^{1390428}5^{235392}}
\right)
=
1.7112120261385615638\ldots .
}
\]

This remains an unratified source-equation result. The inherited three-layer local formulas still extend through \(e=3h\). No canonical ratification, full-form-domain persistence theorem, selected-packet custody statement, or RH conclusion is added.

## 1. Custody

Governance remains notes/SZ_CROSS_COLLAR_RATIFICATION_20260926.md and the pre-65 refold remains the integration record. The GERM-72 correction issued in GERM-73 remains in force.

The new verifier pins tools/sz_fourth_section_self_overlap_audit.py by SHA-256

\[
\texttt{805831ec2a937babcd3bb37a4528af22fc17cdade5dcee032befb592a79149fd}.
\]

It freshly recalculates the physical matrices through that source stack at rational grid \(10^{60}\). Rounded parent matrices are not used as numerical proof input.

Companion artifacts are:

- docs/TERMINOLOGY_GERM76.md;
- tools/sz_fifteen_visit_forced_neighbor_audit.py;
- notes/_recurrence76_audit.json.

## 2. Residual arithmetic

Exact prime-power comparisons certify

\[
0<\psi_7<\chi_7<\eta_7<\omega<\xi,
\]

and

\[
\eta_7=\chi_7+\psi_7,\qquad
\omega=\eta_7+\chi_7,\qquad
\xi=2\eta_7+\chi_7.
\]

For orientation only,

\[
\begin{aligned}
\xi&=3.8605890045692569\cdot10^{-7},\\
\omega&=2.4479594089087864\cdot10^{-7},\\
\eta_7&=1.4126295956604706\cdot10^{-7},\\
\chi_7&=1.0353298132483158\cdot10^{-7},\\
\psi_7&=3.7729978241215486\cdot10^{-8}.
\end{aligned}
\]

Write

\[
d=\zeta-14\xi.
\]

GERM-76 treats

\[
0<d\le\eta_7.
\]

The affine domain audit also certifies the rational enclosure

\[
\frac{777}{157}<\frac{\beta}{\gamma}<\frac{292}{59}.
\]

## 3. Seventh exterior section

In the GERM-75 sixth-section circle \(0<y<\xi\), use

\[
\mathcal U_7=(2\eta_7,\xi).
\]

With

\[
y=2\eta_7+z,\qquad0<z<\chi_7,
\]

the first return takes three steps when \(z>\psi_7\) and five steps when \(z<\psi_7\). In the section coordinate,

\[
\boxed{
S_7(z)=z-\psi_7\pmod{\chi_7}.
}
\]

The two branches tile the \(\chi_7\)-circle, so the induced map is invertible and Lebesgue-measure preserving.

## 4. Five legal complete words

Only three sixth-return atoms occur:

\[
A_{19}=B_{14,19},\qquad
A_{20}=B_{14,20},\qquad
E_{20}=B_{15,20}.
\]

The five complete first-return words are:

| type | chronological sixth-return word |
| --- | --- |
| 3out | \(A_{20},A_{20},A_{19}\) |
| 3in | \(A_{20},E_{20},A_{19}\) |
| 5out | \(A_{20},A_{20},A_{19},A_{20},A_{19}\) |
| 5one | \(A_{20},E_{20},A_{19},A_{20},A_{19}\) |
| 5two | \(A_{20},E_{20},A_{19},E_{20},A_{19}\) |

The five-step branch therefore contains zero, one, or two elliptic \(E_{20}\) visits. A second visit can only occur after the first.

At \(d=\eta_7\), only 3in and 5two survive generically. Both endpoint faces are checked directly.

Every complete word has determinant one.

## 5. Common cone

Use

\[
C_{76}=
\begin{pmatrix}
1&1\\
-5/2&-3
\end{pmatrix}.
\]

Every conjugated complete return has strictly positive entries. Certified forward/backward lower factors are:

| word | forward | backward |
| --- | ---: | ---: |
| 3out | \(>76.4809\) | \(>105.3357\) |
| 3in | \(>12.5150\) | \(>12.0261\) |
| 5out | \(>1586.8816\) | \(>2186.7783\) |
| 5one | \(>207.1842\) | \(>287.9598\) |
| 5two | \(>30.8054\) | \(>25.4734\) |

Hence the weakened uniform statement is

\[
\boxed{
\|B'z\|_1\ge12\|z\|_1\quad(z\in C_+),
\qquad
\|(B')^{-1}z\|_1\ge12\|z\|_1\quad(z\in C_-).
}
\]

This is a complete-return estimate. No expanding norm is asserted for \(E_{20}\) by itself.

## 6. Domain certificate and \(L^2\) exclusion

Every sixth-return atom is already a typed GERM-75 source word. GERM-76 substitutes each affine seventh-section intermediate argument into those complete lower-level domain contracts.

The generic cells check respectively 552, 552, 915, 915, and 915 affine margins on exact rational-polytope vertices. The immediate above-scope guard checks another 907 margins.

Thus legality is established through every intermediate source, not inferred from endpoint bits or spectra.

The section field is an \(L^2\) restriction/translation of the actual two-coordinate scalar-source observation. After conjugating by \(C_{76}\), forward same-sign expansion and backward opposite-sign expansion, together with measure preservation, force the section field to vanish almost everywhere. Applying the argument separately to real and imaginary parts covers complex profiles.

The finite invertible return maps then reconstruct zero through the GERM-75 sixth section and the inherited fifth, fourth, third, second, first, and \(h\)-circle sections. The established local reconstruction finally kills the low head, middle bands, and tail.

## 7. Endpoint arithmetic

The new residual is

\[
\eta_7=170317h-32783k.
\]

Therefore

\[
3h-\beta+14\xi+\eta_7
=
291500h-56108k.
\]

Adding \(\log(16/3)\),

\[
L_{76}
=
-1390428\log2
+1222107\log3
-235392\log5,
\]

which gives the exact expression in Section 0.

The increment over \(L_{75}\) is exactly \(\eta_7\).

Combining with the inherited ambient equivalence,

\[
\boxed{
\ker P_c=\{0\},\qquad
K_c^{\rm ps}=K_c\cap\ker P_c=\{0\},\qquad
0<L\le L_{76}.
}
\]

The \(K_c\) statement remains in the regular-kernel scope.

## 8. Exact stop

Immediately above the endpoint, let

\[
d=\eta_7+\epsilon_*,
\qquad
0<z<\epsilon_*<
\min(\psi_7,\chi_7-\psi_7).
\]

The seventh-section source itself is now active. The first new five-step word is

\[
\boxed{
E_{20},E_{20},A_{19},E_{20},A_{19}.
}
\]

Its source strip is certified exactly. The corresponding matrix satisfies

\[
-1.2071973591<\operatorname{tr}B_{\rm new}<-1.2071973590,
\]

and

\[
-2.5426745365<
(\operatorname{tr}B_{\rm new})^2-4\det B_{\rm new}
<-2.5426745364.
\]

It is projectively elliptic. This stops the current five-word cone library, but does not construct a nonzero kernel or rule out another forced-neighbor induction.

The remaining already-derived three-layer interval is

\[
3h-\beta+14\xi+\eta_7<e\le3h.
\]

The full unresolved four-delay range remains

\[
L_{76}<L\le\log6.
\]

## 9. Execution receipt

The final local verifier completed successfully with exit code zero.

Executed source SHA-256:

\[
\texttt{f823d55f9bc9f27b00c89d6d766c526fa44cc4c1ed11cc897ffd2758328a6bbc}.
\]

Complete stdout SHA-256:

\[
\texttt{72a11e4cbf603b0aacc8b5f1b47a9edbcea56b20b668d7198262a76a275586b7}.
\]

The committed verifier differs from the executed local file only in comments/formatting; every non-comment load-bearing line was compared line-by-line and matched exactly. The repository blob is recorded separately in the audit receipt.

The full parent symbolic suites, full GERM-60 reduction, and old large determinant inventory were not rerun. This is an outward-rational computational certificate accompanying the written source-domain and \(L^2\) proof, not Lean certification or canonical ratification.

## 10. Next individual target

\[
\boxed{
\texttt{SZ-KERNEL-EDGE-GERM-77 / SEVENTH-SECTION SELF-OVERLAP CONTROL}.
}
\]

Start from the new elliptic five-step word and its exact source strip. Preserve the typed GERM-75 source domains and physical section coordinates. Seek forced-neighbor or section-dependent control; do not restart flat determinant enumeration or reopen the stopped screw route.

~~~text
GERM-76: COMPLETE AS A SCOPED EXPERIMENTAL PASS
B15,20 ELLIPTIC ATOM: ABSORBED INTO FIVE COMPLETE SEVENTH RETURNS
SEVENTH SECTION: ROTATION BY -psi7 ON A chi7-CIRCLE
COMMON CONE FACTOR: 12
NEW EXCLUSION: 0<d<=eta7
EXPERIMENTAL ENDPOINT: L=log(3^1222107/(2^1390428*5^235392))
FIRST ABOVE-SCOPE COMPLETE WORD: PROJECTIVELY ELLIPTIC
THREE-LAYER LOCAL FORMULAS: STILL AVAILABLE THROUGH e=3h
GERM-77: NOT EXECUTED
CANONICAL THEOREM CURSOR: SZ-CROSS-COLLAR-3, UNCHANGED
RATIFICATION / PUBLIC PROMOTION: NONE
~~~
