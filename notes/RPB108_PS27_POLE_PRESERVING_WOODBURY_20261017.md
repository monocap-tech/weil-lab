# PS27 — The original even pole survives the true source Schur as a renormalized positive rank-one form

**October 17, 2026 · W-PHYSICAL-SHIFT · stacked after PS26.** The canonical **W-ODD-NEG**, **W-EVEN-FORM**, full original signed Weil positivity, **CC27 D-Riesz** native domain/norm bridge and **RH** remain OPEN. PS27 does not merely recommend retaining the positive even pole; it constructs an **exact pole-preserving SOURCE-first Schur factorization**, proves that the source block remains positive before that pole is added, and identifies the actual effective even pole direction and its rigorous coefficient bounds. This replaces an imprecise post-source pole subtraction with a true source-compatible rank-one positive update.

## 1. The same original signed physical Weil form

On \(I=[-B,B]\), \(B=11/10\), \(R=11/5\), take the ORIGINAL zero-extended physical signed seven-prime form
\[
Q[f]=J[f]+c_{\rm arch}\|f\|_2^2
-2\sum_{n\in\{2,3,4,5,7,8,9\}}
\frac{\Lambda(n)}{\sqrt n}\Re C_f(\log n)
+2|\langle c,f\rangle|^2-2|\langle s,f\rangle|^2,
\]
where \(J[f]=\int_0^\infty e^{-u/2}(1-e^{-2u})^{-1}\|Zf-\tau_uZf\|_2^2\,du\), \(c=\cosh(x/2)\), \(s=\sinh(x/2)\), \(c_{\rm arch}=-\gamma-\pi/2-3\log2-\log\pi\).

The true thirteen-source sharp projector \(P\) of PS15 consists of intervals of width \(\delta=R-\log9<1/350\), whose exact labels are reflection paired \(r\leftrightarrow9/r\). Write \(C=1-P\), \(c_P=Pc\), \(c_C=Cc\). Original physical form domains split sharply and the mixed lower-order terms, including all seven original prime powers and two signed poles, are bounded by the PS15 Carleman/source analysis.

PS16 proved that the **actual full-pole original source operator**, incorporating every original source/source interaction, satisfies
\[
\boxed{A_P>\frac{323}{1000}\,I.}
\]

## 2. The crucial fact: the genuine source remains coercive *without* the positive even pole

Define the **pre-source pole-free** auxiliary form
\[
Q_0[f]:=Q[f]-2|\langle c,f\rangle|^2.
\]
This is an auxiliary form; its sign is NOT the original Weil sign. Let its ACTUAL source block be \(A_0\), mixed source-to-complement operator \(B_0:C\to P\), and complement restriction \(D_0\). Their relation to the ORIGINAL (positive-pole-included) blocks is
\[
\boxed{
A_P=A_0+2|c_P\rangle\langle c_P|,\quad
B_{PC}=B_0+2|c_P\rangle\langle c_C|,\quad
D_C=D_0+2|c_C\rangle\langle c_C|.
}
\]
All three equations are literal original physical source form-block identities. They keep all original archimedean, seven signed prime translations, negative odd pole and true source-to-complement coupling unchanged in \(Q_0\).

The original-source rational enclosures \(\delta<1/350\), \(\cosh(B/2)<7/6\) give
\[
\|c_P\|_2^2
\le13\delta\cosh^2(B/2)
<\frac{13}{350}\left(\frac76\right)^2
=\frac{91}{1800}.
\]
Consequently
\[
\boxed{
A_0=A_P-2|c_P\rangle\langle c_P|
>\left(\frac{323}{1000}-\frac{91}{900}\right)I
=\frac{1997}{9000}I>0.
}
\]
This provides a strict source-pinned lower bound for the **actual original pole-free source operator**, not a shifted graph or approximate matrix. In particular \(A_0^{-1}\) is a legitimate bounded inverse and the exact pole-free first Schur is well-defined:
\[
\boxed{
\mathfrak S_C^{(0)}[h]
=Q_0[h]-\langle B_0h,A_0^{-1}B_0h\rangle,
\qquad
h\in\mathcal D_C.
}
\]
This is mathematically different from PS26's **post-source artificial** \(\mathfrak B_C=\mathfrak S_C-2|\langle c_C,h\rangle|^2\). The two are not to be conflated.

## 3. The actual original positive even pole is a RENORMALIZED rank-one SOURCE SCHUR update

The exact positive quadratic addition \(2|\langle c_P,p\rangle+\langle c_C,h\rangle|^2\) must be added **before** minimizing over the source variable \(p\), not merely after its elimination.

Complete the source square in \(Q_0[p+h]\):
\[
Q_0[p+h]
=\|A_0^{1/2}(p+A_0^{-1}B_0h)\|^2
+\mathfrak S_C^{(0)}[h].
\]
Set \(v=p+A_0^{-1}B_0h\), and let
\[
t=\langle c_P,A_0^{-1}c_P\rangle\ge0,
\qquad
d=c_C-B_0^*A_0^{-1}c_P.
\]
The exact variational identity
\[
\inf_v\Big(\langle v,A_0v\rangle
+2|\langle c_P,v\rangle+\langle d,h\rangle|^2\Big)
=\frac{2}{1+2t}|\langle d,h\rangle|^2
\]
follows from a one-dimensional positive Schur/Woodbury completion of squares; it requires only the already-proved \(A_0>1997/9000\) and bounded source mixed operator. Therefore the ENTIRE original source-eliminated signed Schur is exactly
\[
\boxed{
\mathfrak S_C[h]
=\mathfrak S_C^{(0)}[h]
+\alpha|\langle d,h\rangle|^2,\qquad
\alpha=\frac{2}{1+2t}.
}
\]
**CRITICAL:** The effective positive even-pole vector is \(\boxed{d=c_C-B_0^*A_0^{-1}c_P}\), generally **not** \(c_C\). The original thirteen-source inverse RESPONSE renormalizes both its coefficient and its direction. Replacing this with an uncorrected \(+2|c_C\rangle\langle c_C|\) added after eliminating the source would be an incorrect source-first derivation. Conversely, PS26's post-Schur subtraction \(\mathfrak B_C\) is simply an artificial lower form and was not claimed to equal \(\mathfrak S_C^{(0)}\).

The source-pinned strict rational mass/coercivity estimates provide
\[
0\le t
<\frac{91/1800}{1997/9000}
=\frac{455}{1997},
\]
hence
\[
\boxed{
\frac{3994}{2907}<\alpha\le2,
\qquad\alpha>1.37.
}
\]
This is a **rigorous coefficient interval for the actual renormalized even pole** after real source elimination. The full effective-vector function \(d\), the scalar \(t\), and the remaining Feshbach/Gram sign are **not numerically evaluated**; the rational envelope does not pretend otherwise. The signed pole-free source mixed bound \(\|B_0\|<1403/80<18\) shows \(d\in L^2(C)\) is well-defined, but its coarse error from \(c_C\) is NOT small enough to justify substituting \(c_C\).

## 4. True pole-free Schur has an explicit negative even witness; this is NOT an RH counterexample

RC315's original normalized constant \(u_0=R^{-1/2}\) on \(I\) is form-admissible and has original signed form
\[
0<Q[u_0]<0.040260.
\]
Its original positive even pole obeys \(2|\langle c,u_0\rangle|^2\ge2R=4.4\). Thus the *auxiliary* original pole-free form is genuinely negative:
\[
\boxed{Q_0[u_0]<-4.359740.}
\]
Take \(h_C=Cu_0\) and \(p_0=Pu_0\). PS15 ensures both are admissible. Because **the actual pole-free source block \(A_0\) is positive**, its exact first Schur is variational:
\[
\boxed{
\mathfrak S_C^{(0)}[h_C]
=\inf_{p\in\mathcal D_P}Q_0[p+h_C]
\le Q_0[p_0+h_C]=Q_0[u_0]<-4.359740.
}
\]
This is a sharper negative auxiliary source-Schur witness than PS26's post-Schur \(\mathfrak B_C[h_C]<-4.212\), but it is still emphatically **not negative evidence for the original positive-pole-restored form**.

The exact positive rank-one update \(\alpha|\langle d,h\rangle|^2\) is the *only* difference between \(\mathfrak S_C^{(0)}\) and the actual \(\mathfrak S_C\). Any proof claiming positivity of the latter must show that this single coherent original pole really compensates the negative pole-free direction and all its couplings.

## 5. The mathematically exact parity and effective-vector acceptance criterion

Reflection preserves P and C by \(r\leftrightarrow9/r\); \(c_P,c_C\) are even and the actual original digamma, symmetric seven-prime quadratic operator, and pole terms preserve parity. Thus \(A_0\), \(A_0^{-1}\), \(B_0\) preserve parity and the **effective vector \(d\) is even**. Consequently
\[
\boxed{
\mathfrak S_C[h]_{\rm odd}=
\mathfrak S_C^{(0)}[h]_{\rm odd}.
}
\]
The original negative odd pole is fully present in both forms. No positive even-pole correction is available in the odd sector.

For the even form domain, let
\[
K_{\rm eff}
=\{k\in\mathcal D_C:
k\text{ even},\ \langle d,k\rangle=0\}.
\]
On this exact effective-pole-orthogonal carrier,
\[
\boxed{\mathfrak S_C[k]=\mathfrak S_C^{(0)}[k].}
\]
If the actual original even Schur is nonnegative, its pole-free even restriction MUST be nonnegative on \(K_{\rm eff}\).

More strongly, because \(\mathfrak S_C^{(0)}[h_C]<0\), the even pole-free form has **at least one** strictly negative direction. A single positive rank-one correction can remove **at most one** independent negative direction. Therefore a *necessary* condition for the original even Schur to be nonnegative is
\[
\boxed{
\operatorname{ind}_-(\mathfrak S_C^{(0)}\vert_{\rm even})=1.
}
\]
This index equality is **conditional**, not established: PS27 certifies only the lower bound \(\ge1\).

If \(d\ne0\), define \(\phi=d/\|d\|_2\). Positivity of the **true** original even source Schur is then exactly equivalent to BOTH:
\[
\boxed{\mathfrak S_C^{(0)}[k]\ge0\quad(k\in K_{\rm eff}),}
\]
\[
\boxed{
\inf_{k\in K_{\rm eff}}
\big(\mathfrak S_C^{(0)}[\phi+k]
+\alpha\|d\|_2^2\big)\ge0.
}
\]
These are true domain-level variational conditions, with the same original seven signed prime powers, digamma kernel and negative odd pole as above. They do not require a fabricated inverse on \(K_{\rm eff}\), and the infimum remains meaningful if the orthogonal form has null modes. If \(d=0\), the negative even pole-free witness shows whole even \(\mathfrak S_C\ge0\) is impossible; hence \(d\ne0\) is necessary for a future positive original even proof, **not separately asserted as proven here**.

The three remaining substantive gates are **(i)** odd original signed source Schur positivity, **(ii)** even effective-pole-orthogonal pole-free signed positivity, and **(iii)** the coherent one-scalar effective-pole compensation. None is proved in PS27. The same original CC27 D-Riesz native domain/norm transfer and independent analytic audit remain necessary.

## 6. Next frontier

**PS28:** evaluate or rigorously constrain the actual effective even-pole source inverse response \(A_0^{-1}c_P\), including the coherent vector \(d\) and \(t\), without substituting a crude norm bound for an evaluated inverse. Then attack the true \(K_{\rm eff}\) signed form and odd sign through parity-separated operator representations, or produce a genuine negative witness. A precise coherent scalar compensation is the legitimate next step; expanding PS25's pole-blind full partition is mathematically ruled out.

**Standing:** the ORIGINAL full physical signed Weil, W-ODD-NEG, W-EVEN-FORM, native CC27 D-Riesz identification and RH remain OPEN.

**Replay:** \`python3 scripts/validate_rpb108_ps27_pole_preserving_woodbury.py\` replays PS26→PS25→...→source-pinned RC315, proves the source-rational pole-free block bound and renormalized coefficient bounds, computes the RC315 explicit auxiliary negative witness, checks source-label reflection and fail-closed governance, and replays exact **Fraction** finite symmetric source-block identities to detect missing source/cross pole terms and inverse sign errors. This validates rational constants and a finite algebraic model; the infinite-dimensional functional-analysis factorization still requires independent mathematical proof review.
