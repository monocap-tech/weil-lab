# RPB108 SI11 — exact supported Birman–Schwinger bridge and signed inverse-response gate

**Parent:** SI10 integrated at \`f741cbefe0985b69d3c3dd13007ec3ca7bd9d451\`.  
**Front:** independent SI structural investigation. Native RC signed high-Schur work continues independently.  
**Standing:** exact *conditional* finite-dimensional Birman–Schwinger / correct-sign residual criterion for the **full original Weil quadratic form**, with a rigorous numerical error/size frontier. **No** positivity of the finite matrix, full Weil positivity, Stage I, F4, Lean or RH is proved.

## 1. Correct decomposition of the original complete form

Work on the physical Hilbert space \(H=L^2(I)\), \(I=[-B,B]\), \(B=11/10\), with zero extension \(Z\) and original Fourier convention \(\widehat{Zf}(\xi)=\int_I f(x)e^{-2\pi i x\xi}\,dx\). On the original supported form core, RC312–313 and SI10 identify
\[
Q_{\rm Weil}(f)=\int_{\mathbb R}m(\xi)|\widehat{Zf}(\xi)|^2\,d\xi
+2|\langle c,f\rangle|^2-2|\langle s,f\rangle|^2
\]
with the **original** seven signed prime coefficients, \(c(x)=\cosh(x/2)\), \(s(x)=\sinh(x/2)\).

Let \(\kappa=1/1000\), let \(U\) be SI10's exact certified rational frequency cover (total width \(W=973/32=30.40625\)), and define
\[
a(\xi)=\max\{m(\xi),\kappa\},\qquad r(\xi)=(\kappa-m(\xi))_+.
\]
SI10 proves \(m(\xi)>\kappa\) on \(U^c\). Consequently \(r\ge0\) and \(\operatorname{supp}r\subseteq U\), with exact outward mass budget
\[
\boxed{\int r\le\int m_-+\kappa |U|\le
R:=M+\kappa W
=\frac{1204033883}{32000000}<38},
\quad M=\frac{1203060883}{32000000}.
\]
These are **upper certificates**, not claims that \(m_-\) or \(r\) have constant values.

Define the positive closed quadratic form
\[
\mathfrak a[f]=\int_{\mathbb R}a(\xi)|\widehat{Zf}(\xi)|^2d\xi
+2|\langle c,f\rangle|^2,\quad
A=A^*\ge\kappa I
\]
in the supported physical form domain, with its associated strictly positive selfadjoint operator \(A\) (Friedrichs/form realization). Define the bounded positive trace-class negative operator
\[
K=Z^*\mathcal F^{-1}r\mathcal F Z+2|s\rangle\langle s|\succeq0.
\]
**Exact original identity:**
\[
\boxed{Q_{\rm Weil}[f]=\mathfrak a[f]-\langle f,Kf\rangle}
\]
on the form domain. Unlike simply writing \(m=m_+-m_-\), the deliberate positive margin \(\kappa\) makes \(A^{-1}\) bounded and permits an explicit operator-error budget.

## 2. Exact Birman–Schwinger equivalence

Since \(A\ge\kappa I\) and \(K\) is bounded positive, the closed-form representation implies
\[
\boxed{Q_{\rm Weil}\ge0\ \Longleftrightarrow\
T:=A^{-1/2}KA^{-1/2}\preceq I.}
\]
This is an equivalence on the actual **supported** Hilbert carrier, not a frequencywise pointwise comparison.

Choose SI10's compactly supported modulated-polynomial span \(V_b\) with physical orthogonal projection \(P_b\). The signed negative odd-pole vector \(s\) is included **exactly**. Put
\[
K_b=P_bKP_b\succeq0,\qquad E_b=K-K_b.
\]
From SI10's all-input Taylor projection bound on every frequency of \(U\), the original positive mass representation and the rank-one difference inequality give
\[
\boxed{\|E_b\|\le\eta_b:=4BR\,2^{-b}.}
\]
The **complementary quadratic** penalty, crucially smaller by one more factor of \(2^{-b}\), is
\[
\boxed{\|(I-P_b)K(I-P_b)\|\le2BR\,2^{-2b}.}
\]
These are different obligations. The second underlies SI10's positive complementary form; the first is needed to perturb the **whole** Birman–Schwinger operator:
\[
\|A^{-1/2}E_bA^{-1/2}\|\le\eta_b/\kappa.
\]

Let \(U_b:\mathbb C^{d_b}\to H\) be a physical **orthonormal** synthesis map onto \(V_b\); \(d_b\le1+2\sum p_j\). Define the finite Hermitian positive matrices
\[
M_b=U_b^*KU_b\succeq0,\qquad G_b=U_b^*A^{-1}U_b\succeq0.
\]
Then the nonzero eigenvalues of \(A^{-1/2}K_bA^{-1/2}\) equal those of \(M_b^{1/2}G_bM_b^{1/2}\). Hence the rigorous **sufficient finite-dimensional gate**
\[
\boxed{
\lambda_{\max}\bigl(M_b^{1/2}G_bM_b^{1/2}\bigr)
+\frac{\eta_b}{\kappa}\le1
\quad\Longrightarrow\quad Q_{\rm Weil}\ge0.
}
\]
If \(\eta_b<\kappa\), the matrix threshold is strictly positive, but SI11 **does not certify** this matrix eigenvalue. The gate is a conditional reduction, not a hidden theorem of RH.

## 3. Concrete certified feasibility frontier

The SI11 exact-rational validator regenerates the full SI10 protected interval cover (973 unresolved rational leaves, 107 positive-frequency clusters, all reflections), validates \(W,M,R\), and computes physical Taylor feature dimensions and their signed-source error without floating-point acceptance.

| Local Taylor bits \(b\) | Sufficient feature dimension \(d_b\) | Rigorous bound \(\eta_b/\kappa\) | Meaning |
|---:|---:|---:|---|
| 9 | 939 | \(<324\) | SI10 complement positivity works; crude global inverse-error gate is vacuous |
| 10 | 1003 | \(<162\) | Still vacuous |
| 12 | 1121 | \(<41\) | Still vacuous |
| 16 | 1367 | \(<2.527\) | Still vacuous |
| **20** | **1561** | \(<0.158\) | At least a nontrivial matrix target is possible |
| **21** | **1631** | \(<0.079\) | Conditional finite gate asks for \(\lambda_{\max}<0.921\) |
| **24** | **1781** | \(<0.0099\) | Conditional finite gate asks for \(\lambda_{\max}<0.9901\) |
| 32 | 2151 | \(<0.000039\) | Very small inverse perturbation budget |

The table entries are **upper error bounds**, not lower bounds or measurements of the actual negative operator norm. Specifically, \(\eta_9/\kappa\approx323.35\) does not prove the true approximation fails; it proves this *coarse perturbative criterion* does not certify a matrix threshold at rank 939. The first passing Actions replay certified the previously unpublished \(b=20,21,24\) sufficient dimensions **1561, 1631 and 1781**; these are now exact mandatory rank assertions in the validator. The physical operator-norm error bounds are, respectively, \(0.0001578852262\), \(0.0000789426131\), and \(0.0000098678267\), each strict with exact rational enclosures. These are *not* measured finite Birman–Schwinger matrix eigenvalues.

## 4. Correct-sign supported inverse response: the actual matrix obligation

The difficult factor is
\[
G_b=U_b^*A^{-1}U_b,
\]
the inverse of the **supported** positive operator. It is not obtained merely by multiplying the Fourier transform by \(1/a(\xi)\) and clipping.

For a trial response map \(Y:\mathbb C^{d_b}\to\operatorname{Dom}A\), set
\[
R_b=U_b-AY.
\]
The exact signed inverse-response identity is
\[
\boxed{
G_b=U_b^*Y+Y^*U_b-Y^*AY+
R_b^*A^{-1}R_b
}
\]
and the *correct positive residual contribution* gives the **rigorous Loewner upper bound**
\[
\boxed{
G_b\preceq U_b^*Y+Y^*U_b-Y^*AY+
\kappa^{-1}R_b^*R_b.
}
\]
Thus one can try to certify the finite Birman–Schwinger matrix from original **native residuals**. Leaving the residual out would provide a **lower** rather than an upper bound on the inverse response, an invalid positivity argument. SI11 supplies the exact interface but **no original \(Y\), full signed residual Gram, or matrix Loewner certificate**.

### Why the unrestricted Fourier inverse is not the solution

Even for a finite-dimensional example, compression and inversion fail to commute:
\[
A_{\rm toy}=\begin{pmatrix}2&1\\1&2\end{pmatrix},\quad
P=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad
(PA_{\rm toy}P)|_{\operatorname{Ran}P}=2,
\]
while \(\langle e_1,A_{\rm toy}^{-1}e_1\rangle=2/3\neq1/2\).
The supported inverse is the operator inverse **after** imposing physical support. The compressed whole-line inverse is generally a different operator. Via the variational formula for the positive form inverse it can provide a conservative upper comparison, but it is not an exact replacement.

A sharper *structural obstruction* is the original SI06 certified negative multiplier witness \(m(882.91)<-0.08\). At this frequency \(a(\xi)=\kappa\) and \(r(\xi)=\kappa-m(\xi)>0.081\); hence \(r(\xi)/a(\xi)>81\), locally by continuity. A **whole-line pointwise** Birman–Schwinger norm bound, \(\sup_\xi r(\xi)/a(\xi)\), therefore exceeds 81. It cannot possibly prove the target \(\le1\); the necessary positivity, if true, depends on the **compact-support carrier constraint** and signed coupling, not on pointwise multiplier comparison.

## 5. Decision and SI12 frontier

**Established here:** a correct-sign finite matrix *conditional* gate for positivity of the **entire** original signed Weil form; a fully paid negative-operator approximation error with a dimension/relative-margin tradeoff; and a precise identification of the supported inverse-response computation that remains.

**Not established:** positivity of \(M_b^{1/2}G_bM_b^{1/2}\) below the threshold; a certified signed inverse response for even a one-column physical feature; a rank-939 full-Schur certificate; any improvement over RC314's 301-dimensional potential-negative localization; Stage I, F4, complete Lean, or RH.

**SI12:** Build and certify a small, genuinely supported \(A^{-1}\) inverse-response test (e.g. one or several SI10 central feature vectors) including the correct positive residual Gram; first compare its computational cost and margin to the native RC331/332 inverse-response chain. If no efficient signed interface appears, retain SI11 as a valid but currently more expensive reduction and prioritize the smaller RC front.

### Reproduce

\`python scripts/validate_rpb108_si11_birman_schwinger_gate.py\`.

The validator uses only exact \`Fraction\` arithmetic for inequalities and replays SI10's earlier original signed frequency support audit. The operator-theoretic equivalences rely on standard closed-form spectral calculus, variational inverses and Cauchy–Schwarz, not standalone Lean formalization. They are conditional on the inherited original CC27/RC312–313 explicit-formula identification and are **not** independent peer review of a complete RH proof.
