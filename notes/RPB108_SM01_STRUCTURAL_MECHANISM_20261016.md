# RPB108 SM01 — structural mechanism: pole-absorbed coercivity, band-only no-go, exact full-negative Schur gate

**Track:** NEW INDEPENDENT **SM (Structural Mechanism)**, parallel to incremental SI and native RC high-Schur.  
**Source:** original complete signed physically supported Weil form from RC312–313, SI10–SI11, and the SI29 **focused exact-rational** pole-only validator (PR #124, focused passing Actions run 38977766432, October 16, 2026). SI29 final-head push and PR regression both passed; PR #124 is merged at `86aa35d5521167fcebac4f7b231f6053284dddc3`. Distinguish the repository's checked certificate from independent peer review or Lean formalization.  
**Status:** mathematical conditional operator theorems plus a small exact-rational sign/budget regression; not a new whole-original-form positivity theorem, not Stage I, Lean or RH.

## 1. The object that a structural argument must control

Let \(I=[-B,B]\), \(B=11/10\), \(H_o=L^2(I)_{\rm odd}\), and \(Z\) physical zero-extension. The original signed form is
\[
Q_{\rm Weil}[f]=\int_{\mathbb R}m(\xi)|\widehat{Zf}(\xi)|^2d\xi
+2|\langle c,f\rangle|^2-2|\langle s,f\rangle|^2
\]
with \(s(x)=\sinh(x/2)\), \(c(x)=\cosh(x/2)\) and the full original seven signed prime cosines. SI11 fixes \(\kappa=1/1000\) and uses the exact split \(m=a-r\), where
\[
a(\xi)=\max\{m(\xi),\kappa\},\quad r(\xi)=(\kappa-m(\xi))_+\ge0.
\]
On the **odd** carrier the positive form operator \(A_o\succeq\kappa I_o\) has no even pole; the genuine negative operator is
\[
K_o=K_{{\rm freq},o}+2|s\rangle\langle s|,
\quad
K_{{\rm freq},o}=Z^*\mathcal F^{-1}r\mathcal F Z\big|_{H_o}\succeq0.
\]
Thus
\[
Q_o[f]=\langle f,A_o f\rangle
-\langle f,K_{{\rm freq},o}f\rangle
-2|\langle s,f\rangle|^2.
\]
All operator inverses here are of the **physically supported** operators, never the pointwise whole-line Fourier reciprocal. The form statement is interpreted on \(\mathrm{Dom}\,A_o^{1/2}\).

## 2. First structural consequence of SI29: a uniform pole-absorbed floor

**Theorem SM01-A (rank-one pole absorption).** Let \(A\ge\kappa I\) be positive selfadjoint, and \(s\in H\). If
\[
\lambda=2\langle s,A^{-1}s\rangle\le L<1,
\]
then the operator defined by the closed quadratic form
\[
A_\star=A-2|s\rangle\langle s|
\]
obeys the **uniform quadratic-form inequality on all \(f\)**:
\[
\boxed{A_\star\succeq(1-L)A\succeq(1-L)\kappa I.}
\]
*Proof.* Cauchy–Schwarz in the \(A^{1/2}\)-energy yields
\[
2|\langle s,f\rangle|^2
=2|\langle A^{-1/2}s,A^{1/2}f\rangle|^2
\le\lambda\langle f,Af\rangle.
\]
No finite-feature ansatz is needed in the conclusion.

**Application from the merged SI29 rational replay:** The validator printed \(2\langle s,A_o^{-1}s\rangle<0.9663787350758407\). Take the weaker **rational** \(L=966379/10^6\). Then
\[
\boxed{
A_{\star,o}\succeq\frac{33621}{10^6} A_o
\succeq\frac{33621}{10^9}I_o.
}
\]
The new strictly positive \(L^2\) floor \(3.3621\cdot10^{-5}\) applies simultaneously to **every odd physically supported direction**, but **only after the rank-one pole**. The full \(K_{{\rm freq},o}\) is not included in this floor. This does not infer even-sector or complete Weil positivity.

## 3. A genuine structural no-go: finitely many disjoint positive windows do not yield a uniform frequency-only inequality

**Theorem SM01-B (compact-band-only domination fails).** Let \(E_+\), \(E_-\) be disjoint bounded symmetric measurable subsets of \(\mathbb R\), each of positive measure; assume bounded nonnegative weights \(w_\pm\) supported there and positive on nontrivial symmetric subbands. On \(H_o=L^2([-B,B])_{\rm odd}\), define the frequency observations
\[
(Sf)(\xi)=\sqrt{w_+(\xi)}\,\widehat{Zf}(\xi),\qquad
(Rf)(\xi)=\sqrt{w_-(\xi)}\,\widehat{Zf}(\xi).
\]
Suppose, for simplicity, \(w_\pm\) are even and strictly positive almost everywhere on their respective positive-measure bands. Then **no finite constant \(C\)** can make
\[
\boxed{\|Rf\|_2^2\le C\|Sf\|_2^2\quad\text{for all }f\in H_o.}
\]
In particular, without a positive scalar floor or an independent spectral/regularity restriction, a finite union of positive bands **alone** cannot uniformly absorb even one disjoint bounded negative band on every physical function.

*Proof.* If \(R^*R\preceq C S^*S\), Douglas' range inclusion/majorization lemma forces
\(\operatorname{Ran}R^*\subseteq\operatorname{Ran}S^*\). Choose a nonzero odd frequency profile \(\varphi\) supported in a negative subband where \(w_->0\); its weighted inverse Fourier synthesis \(R^*\varphi\) is the restriction to \(I\) of a nonzero entire function, because its Fourier coefficient is compactly supported. If it also belonged to \(\operatorname{Ran}S^*\), it would agree on the real interval \(I\) with an entire inverse Fourier synthesis whose frequency support lies inside \(E_+\). The identity theorem makes the two entire functions identical globally; injectivity of the Fourier transform makes their disjointly supported profiles identical, forcing both zero, contradiction. The parity restriction does not change this argument: choose and extend nonzero odd profiles, with reflected symmetric frequency bands.

This demonstrates a critical distinction: **analytic uniqueness is not uniform stable observability**. Paley–Wiener supplies uniqueness but not the above global inequality. The familiar Logvinenko–Sereda spectral inequalities require an appropriate thick observation set and a specified spectral class, conditions not satisfied by an arbitrary fixed bounded \(E_+\). This no-go is only for the *floor-free band-only* inequality, not for \(A_\star\succeq K_{{\rm freq},o}\), where \(\kappa I\), unbounded positive high-frequency strength, and native support geometry all matter.

## 4. Exact Schur normal form of the remaining full signed odd problem

Write the **actual signed negative-frequency analysis** on the physical odd carrier:
\[
R_o:H_o\to\mathcal E_-:=L^2(\operatorname{supp}r),\qquad
(R_of)(\xi)=\sqrt{r(\xi)}\,\widehat{Zf}(\xi).
\]
Then \(R_o^*R_o=K_{{\rm freq},o}\), with appropriate odd parity representation and closure. Define
\[
\lambda=2\langle s,A_o^{-1}s\rangle<1,\quad
X=R_oA_o^{-1}R_o^*,\quad
v=R_oA_o^{-1}s.
\]
The Birman–Schwinger matrix on \(\mathcal E_-\oplus\mathbb C\) for \((R_o,\sqrt2\,s^*)\) is
\[
\mathcal B=
\begin{pmatrix}
X&\sqrt2\,v\\
\sqrt2\,v^*&\lambda
\end{pmatrix}.
\]
The **exact correct-sign Schur complement** implies
\[
\boxed{
Q_o\succeq0\quad\Longleftrightarrow\quad
X+\frac{2}{1-\lambda}|v\rangle\langle v|\preceq I_{\mathcal E_-}.
}
\]
Equivalently, Sherman–Morrison for the *supported inverse* gives
\[
A_{\star,o}^{-1}
=A_o^{-1}+\frac{2}{1-\lambda}
A_o^{-1}|s\rangle\langle s|A_o^{-1},
\]
so the entire remaining odd signed-frequency gate is
\[
\boxed{R_oA_{\star,o}^{-1}R_o^*\preceq I_{\mathcal E_-}.}
\]
This expression exposes exactly the **coupling** that could make negative frequencies overwhelming even after the pole is absorbed. The rank-one correction is *positive*, not negative. Omitting the \(2|v\rangle\langle v|/(1-\lambda)\) term is logically invalid.

These are general Hilbert-space operator identities, not an assertion that the final inequality is true. They specify *what* a genuine common structural constraint must bound for the **entire family** of negative-frequency modes simultaneously.

## 5. What the already certified SI11 residual tells us about feasibility

SI11 has an **all-original-negative-frequency** support-preserving Taylor approximation \(P_bK_{{\rm freq},o}P_b\) with residual norm
\[
\eta_b\le 4BR\,2^{-b},\qquad
R=\frac{1204033883}{32000000}<38,\qquad B=11/10.
\]
The original exact odd pole vector is included in SI11's finite physical space. After pole absorption, the uniform floor is only \(\kappa(1-L)\), so a coarse perturbation via \(A_{\star,o}^{-1/2}\) has relative bound
\[
\frac{\eta_b}{\kappa(1-L)}.
\]
The **exact-rational SM01 validator** certifies the following conservative ceilings: for \(b=24\) the ratio is \(<0.30\), \(b=28\) is \(<0.019\), and \(b=32\) is \(<0.0012\). These are feasibility/error *budgets*, not the computed eigenvalues of the finite negative-frequency BS matrix. The \(b=32\) SI11 physical rank bound is 2151, whereas the native RC high-Schur positive complement may produce a much smaller effective block; do not conflate carriers or count a 2151-dimensional matrix as closure.

## 6. Concrete next SM02 theorem experiment

**The structural target, different from adding bands:**

Find an explicitly defined finite-dimensional negative-packet space \(V_-\subset H_o\), an analysis map \(R_o\), and an intrinsic **frame/energy transport inequality** controlling *all* negative-frequency modes at once, e.g.
\[
\boxed{
\|R_of\|_2^2\le (1-\epsilon)\langle f,A_{\star,o}f\rangle
\quad\forall f\in\mathrm{Dom}\,A_o^{1/2},
\qquad\epsilon>0,
}
\]
proved from weighted observability and a **rigorously controlled complement**, *not* assumed by a per-direction numerical scan. The displayed inequality is an unproved target, logically equivalent to a strict full-negative BS bound. A genuine new structural theorem must supply a verifiable inequality on a specified function class or a uniform frame constant independently of verifying every signed-negative direction.

A computational bridge exists if one uses SI29's finite positive reference
\[
C_{14}=\kappa I+G\Gamma G^*\preceq A_o,
\]
with its pole-absorbed \(C_{14,\star}=C_{14}-2|s\rangle\langle s|\succ0\). Then \(A_{\star,o}\succeq C_{14,\star}\), so the sufficient (not necessary) structural gate is
\[
R_oC_{14,\star}^{-1}R_o^*\preceq I.
\]
The inverse \(C_{14,\star}^{-1}\) can be written **exactly** via a finite Woodbury matrix and the pole Schur correction, retaining *all* negative-frequency cross-Gram entries. A failure of this sparse lower reference would **not** show failure of the original operator, exactly as SI26 warned.

**Work split:** retain SI/RC certified continuation unchanged. SM02 should audit (a) the negative-frequency spectral packet concentration/observability geometry under physical support, (b) the correct pole-conditioned full negative-frequency coupling, and (c) the rank/error tradeoff versus native RC's possible-negative-sector localization. Stop and change candidate principle if it collapses to a tautological restatement of \(Q_o\ge0\).

**Regression:** \`python scripts/validate_rpb108_sm01_pole_schur.py\` checks the exact rational SI29-derived coercivity constants, original SI11 residual budgets, and the positive Schur coupling sign in a 2×2 analytic toy model. It is not a numerical proof of the infinite-dimensional theorems or a stand-in for independent analysis.
