# RPB108 EF04 — explicit full-original even negative-frequency rational moments

**Obligation:** W-EVEN-FORM (scoped local research); canonical active obligation remains W-ODD-NEG.  
**Parent:** EF02/EF03 merged PR #141 at 63473e43739a863b4de1def81e170fdc10942eac; SM10 on the same research branch supplies the exact original signed cap moment construction.  
**Standing:** explicit original supported **even** Taylor-source factorization with 107 exact rational moment blocks, 890 even directions, and fully signed global upper remainder. Final-head exact-rational CI is required; no positive finite inverse/Schur eigenvalue, entire even-form positivity, whole Weil, global bridge or RH is claimed.

## 1. Original even sector and the entire signed-negative operator

Let \(B=11/10\), \(\kappa=1/1000\),
\(H_e=L^2([-B,B])_{\rm even}\), and \(Z\) zero extension.
Retain the exact **original signed seven-prime plus archimedean** multiplier \(m(\xi)\) of SI10/EF01. Set
\[
a(\xi)=\max(m(\xi),\kappa),\quad
r(\xi)=(\kappa-m(\xi))_+,\quad
A_e=Z^*\mathcal F^{-1}a\mathcal FZ|_{H_e}
+2|c\rangle\langle c|,\quad c(x)=\cosh(x/2).
\]
The original full even form is \(Q_e=A_e-K_{\rm neg,e}\), with \(A_e\succeq\kappa I\).

Import SM10/SI10's *entire* original signed envelope: 973 positive-frequency unresolved rational dyadic leaves in 107 maximal clusters, plus reflections; all other original frequencies are protected with \(m>\kappa\). On each leaf \(I=[l_I,r_I]\), the height \(h_I\) gives \(0\le r(\xi)\le h_I+\kappa=:w_I\). Its full reflected integrated weight is
\[
\int_{\mathbb R}w=M+\kappa W
=\frac{1204033883}{32000000}=37.62605884375,
\qquad W=\frac{973}{32}.
\]
**This is an upper envelope of the entire original negative operator**, not an isolated negative band or a sampled frequency approximation.

With \(h_\xi^e(x)=\cos(2\pi\xi x)\) on the *actual compact physical support*,
\[
0\preceq K_{\rm neg,e}\preceq K_{\rm cap,e}
=2\int_0^\infty w(\xi)|h_\xi^e\rangle\langle h_\xi^e|\,d\xi.
\]

## 2. Explicit EVEN Taylor sources, not the odd-source matrix

For the \(j\)-th positive-frequency cluster \(J_j\) let \(c_j\) be its rational midpoint, \(p_j\) SI08's rigorous \(b=24\) Taylor order. Define
\[
u_{jk}^e(x)
=\frac{(2\pi x)^k}{k!}\cos(2\pi c_jx+k\pi/2),
\qquad k=0,\ldots,p_j-1.
\]
Every \(u_{jk}^e\) is **even** in \(x\): when \(k\) is odd, both \(x^k\) and the phase-shifted cosine are odd. The Taylor polynomial is
\[
T_j^e(\xi,x)=\sum_{k<p_j}(\xi-c_j)^k u_{jk}^e(x).
\]
The signed original-cover Taylor regression gives the uniform **physical** remainder
\[
\|h_\xi^e-T_j^e(\xi)\|_{H_e}
\le\sqrt{2B}\,2^{-24}
\]
on every unresolved original leaf. There are **890** such even source columns. These are not odd sine columns, and no rank independence is presumed for the source synthesis.

## 3. Exact full rational moment covariance

For each cluster and \(k,l<p_j\), set
\[
\boxed{
C^{(j)}_{kl}
=2\sum_{I\subset J_j}
(h_I+\kappa)
\frac{(r_I-c_j)^{k+l+1}-(l_I-c_j)^{k+l+1}}
{k+l+1}.
}
\]
These are the exact (not quadrature sampled) rational moments of the original signed **upper envelope**. They depend on \(k+l\), so every \(C^{(j)}\) is symmetric Hankel. They are strictly positive definite: any nonzero polynomial of degree below \(p_j\) has positive squared weighted \(L^2\) norm on a positive-measure leaf where \(h_I+\kappa>0\). The focused validator reconstructs **every** source coefficient via SM10's original SI10-cover rational recursion and performs exact rational LDL with strictly positive pivots across all 107 blocks.

Let \(U:\mathbb R^{890}\to H_e\) synthesize the **actual even** \(u_{jk}^e\), and \(C=\oplus_{j=1}^{107} C^{(j)}\). Then the explicit *source* approximation satisfies the exact identity
\[
K_{T,e}=UCU^*
=2\sum_{j,I\subset J_j}\int_I w_I
|T_j^e(\xi)\rangle\langle T_j^e(\xi)|\,d\xi.
\]
**Important:** the cap's frequency-cluster moment matrix \(C\) is block diagonal, but the **physical** Gram \(U^*U\), the actual supported inverse \(U^*(A_e-\eta I)^{-1}U\), and the final positive-vs-negative Loewner matrix generally have NONZERO intercluster cross entries. In fact, the validator certifies an explicit original-support cosine cross-Gram example at frequencies \(0.30,0.76\) strictly between \(0.11\) and \(0.12\) to catch false block-diagonal assumptions. Those two illustrative frequencies are not claimed to be EF04 cluster centers.

## 4. Rigorous whole-frequency upper Loewner bound with every cross term

Let \(R_{\rm cap}\) be the full true physical even cap analysis operator, and \(R_T\) the explicit Taylor-replaced analysis. Using SI10's **entire original** signed upper mass,
\[
\|R_{\rm cap}-R_T\|^2
\le d_{24}^2
:=2B(M+\kappa W)2^{-48}.
\]
Young's inequality pays the complete true/Taylor cross terms for any \(\tau>0\). Take EF03's \(\tau=1/65536\) and
\[
\eta=(1+\tau^{-1})d_{24}^2
<1.93\times10^{-8}<\kappa.
\]
Consequently the **actual original even** negative operator obeys
\[
\boxed{
K_{\rm neg,e}
\preceq K_{\rm cap,e}
\preceq (1+\tau)UCU^*+\eta I.
}
\]
This is a finite-rank *source-factorized* upper bound for the **entire** original signed negative continuum, not EF03's abstract physical \(PK_{\rm cap}P\). It preserves all cross terms in the bound instead of deleting them.

## 5. The concrete remaining 890-source original inverse Schur gate

Let
\[
B_e=A_e-\eta I\succeq(\kappa-\eta)I>0,
\qquad D=(1+\tau)C\succ0.
\]
Since \(Q_e\succeq B_e-UDU^*\), a sufficient, exactly scoped **finite** test is
\[
\boxed{D^{-1}-U^*B_e^{-1}U\succeq0.}
\]
This is a full **890-by-890** physical supported inverse/Schur matrix; its entries couple all 107 clusters. The positive even pole is in \(B_e\) and cannot be dropped while asserting equality. This is the real W-EVEN-FORM bottleneck, and **the inequality is not established by EF04**.

In particular, for a trial \(Y:\mathbb R^{890}\to\operatorname{Dom} B_e\) and residual \(E=U-B_eY\), the correct inverse identity and safe upper are
\[
U^*B_e^{-1}U
=U^*Y+Y^*U-Y^*B_eY+E^*B_e^{-1}E
\preceq U^*Y+Y^*U-Y^*B_eY+
(\kappa-\eta)^{-1}E^*E.
\]
No unrestricted pointwise Fourier reciprocal or uncharged residual may replace the actual supported inverse. Also, the tiny \(\eta\) is **not** a certified eigenvalue of the finite gate.

A subsequent pass should **evaluate an actual original supported positive inverse response or a rigorous low-cost necessary obstruction for the EF04 cap**, not spend further turns merely reformulating the same criterion. A smaller native RC even carrier can be substituted only with checked domain/metric transport, including its original signed boundary terms.

## 6. Evidence and limitations

**EF04 advance:** explicit 107 exact rational signed-negative moment blocks, 890 original supported even Taylor columns, strict rational SPD checks, and complete continuous-frequency upper-tail custody. These are mathematical ingredients on the original even *carrier*, not positivity of the complete form. EF02's 15-negative-eigenvalue obstruction to sparse references and EF03's global upper carrier remain intact.

**W-EVEN-FORM: OPEN.** No actual \(U^*B_e^{-1}U\) upper Loewner enclosure or 890-source gate positivity. W-WHOLE-FORM, global original-zeta transfer, Lean original-form attachment and RH remain open.

Reproduce: python3 scripts/validate_rpb108_ef04_explicit_even_cap_moments.py; this relies on SM10's exact signed-original SI10 leaf and moment validators. Passing GitHub Actions is not an independent mathematical peer review.
