# SM34 — Eliminate the original positive-continuum mixed coupling by an \(A_*\)-energy-dual exceptional decomposition

**October 23, 2026 correction:** Original SM33's historical h-only leakage underestimated the defined operator Kminus=(κ-m)+. The amended original SM33 validator now pays h+κ on every unresolved original cell; the conservative corrected ε remains <1/15000, so this note's 51/56 sufficient algebra survives, subject to the original domain assumptions. The historical SM33 leakage decimal and global Hneg values below are superseded; see [repaired leakage certificate](RPB108_SM33_KAPPA_LEAKAGE_REPAIR_20261023.md) and [improved θ threshold](RPB108_SM40_SHARP_ODD_COMPLEMENT_THRESHOLD_20261023.md).


**October 18, 2026 · canonical W-ODD-NEG · stacked on SM33 draft PR #214 (focused final-head Actions PASSED).**

**Principal result:** Instead of attempting to numerically bound the unbounded positive-frequency/archimedean mixed map \(C_+=Q(A_+-\kappa I)P\) in the **physical \(L^2\)-orthogonal** SM32/SM33 block decomposition, pull the same 470-dimensional ORIGINAL odd source span **backward through the entire positive pole-conditioned operator \(A_*^{-1}\)**. This produces a rigorously defined *different, nonorthogonal physical splitting* whose mixed \(A_*\)-energy cross **vanishes exactly**. The **entire** original mixed signed form then consists only of the already-certified negative-frequency operator \(K_-\), including all 973 seven-prime signed leaves and infinite residual. The original negative odd pole remains fully incorporated in \(A_*\), rather than incorrectly discarded. SM33's complete original odd complement leakage bound yields a quantitatively small *relative* full-infinite Schur correction \(\le(\varepsilon/\mu)\times\) the finite negative quadratic. A clean **470-dimensional full-operator sufficient PSD gate with the exact rational threshold \(51/56\)** follows.

**This is a NEW exact original complete-operator composition/acceptance reduction, not a sign certificate for its outstanding finite matrix.** The actual 470-dimensional full original \(A_*^{-1}\)/\(K_-\) generalized eigenvalue comparison has **not** passed or been evaluated. No full odd O1/O2, even E1–E4, signed whole Weil, native CC27 D-Riesz, RH claims. The entire original Fourier/physical form-domain identification and positivity of \(A_*\) inherited from SI29/SM17 require independent analytic audit.

## 1. Original operators and the old 470-dimensional SOURCE span

Let \(H= L^2([-11/10,11/10])_{\rm odd}\), with its original zero-extension odd closed quadratic-form realization,
\[
W_o=A_*-K_-,\qquad A_*=A_o-2|s\rangle\langle s|\succeq\kappa_*I,
\quad \kappa_*=\frac{33621}{10^9}>0,\quad
s(x)=\sinh(x/2).
\]
Here \(A_o\) is the ENTIRE original positive/archimedean high-frequency form (unbounded as an \(L^2\) operator); \(K_-\succeq0\) is the ENTIRE original seven-prime signed-negative bounded, trace-class operator. The strict original pole-conditioned \(A_*\) lower is inherited from SI29/SM17. We never approximate \(A_o\) by 14/33 bands to claim its complete positivity. Its **exact full resolvent** \(A_*^{-1}\) is defined and bounded as an operator, even though the matrix of its action has not been computed.

Let \(E_0=E_9^{\rm odd}\subset H\) be the **SAME SM32 original \(b=9\) exceptional physical source span**: 469 original odd projected cluster Taylor source generators from 107 clusters plus the original pole vector, so \(\dim E_0=d\le470\). Let \(P_0\) be true physical \(L^2\) orthogonal projection onto \(E_0\), and \(F=E_0^\perp\) (the entire infinite physical complement), with \(Q_0=I-P_0\). SI10/SM32 proved on this **entire original F**:
\[
\boxed{D_F:=W_o|_F\succeq\mu I_F,\quad \mu=\frac{17}{25000}.}
\]
SM33 proved for the entire original \(K_-\) on this **same F**:
\[
\boxed{
0\preceq Q_0 K_- Q_0\preceq\varepsilon I_F,\quad
0<\varepsilon=2B\sum_{j=1}^{107}M_j e_j^2
<\frac1{15000}.
}
\]
Each \(M_j\) pays ALL original negative signed multiplier leaves of that cluster; each \(e_j\) is its own b9 original physical sine Taylor error, and all frequency/exterior residuals are included.

## 2. NEW positive-energy DUAL exceptional subspace: zero positive cross EXACTLY

The problematic SM33 *L2-orthogonal* exceptional space \(E_0\) has a mixed high-frequency positive operator \(Q_0A_*P_0\) that is not quantitatively bounded. **Change the finite exceptional space**, not the original odd operator:

\[
\boxed{E_A:=A_*^{-1}E_0
=\{A_*^{-1}h:h\in E_0\}\subset\operatorname{Dom}A_*,\qquad
H=E_A\;\dotplus\;F.}
\]

This is an *algebraic/topological direct sum*, **NOT \(L^2\)-orthogonal**. To prove it, define the actual \(d\)-dimensional dual Gram map
\[
T:=P_0 A_*^{-1}|_{E_0}:E_0\to E_0.
\]
Because \(A_*^{-1}\) is positive and injective, \(T\) is strictly positive on the finite-dimensional \(E_0\), hence invertible. For every \(f\in H\) (and every \(f\) in the original form domain), set \(h=T^{-1}P_0f\), \(e=A_*^{-1}h\), \(v=f-e\). Then \(v\in F\), \(e\in E_A\) and both belong to the original form domain whenever \(f\) does. The decomposition is unique and bounded as a (nonorthogonal) direct-sum projection because its exceptional factor is finite dimensional.

**Exact ORIGINAL energy orthogonality** now holds for all \(e=A_*^{-1}h\in E_A\) and \(v\in F\):
\[
\boxed{a_*(e,v)=\langle A_*e,v\rangle=\langle h,v\rangle=0.}
\]
The entire positive-frequency **AND** archimedean high-frequency form, including the genuine negative odd pole \(-2|s\rangle\langle s|\), is embedded in \(a_*\) and cancels in this cross. **Do not assert that \(s\in E_A\)** or that its individual pole cross vanishes: in this new splitting, the pole contribution generally does not vanish separately; its net \(A_*\)-cross is exactly zero because the original full operator has been used.

Thus, in the genuine ORIGINAL signed Weil form on \(E_A\dotplus F\), the FULL offdiagonal is exactly
\[
\boxed{
W_o[e,v]=-\langle K_-e,v\rangle,\quad
C_A=-Q_0K_-|_{E_A}.}
\]
There is **no missing \(C_+\)** to be estimated. This is a strict operator-level improvement over SM33's physical \(L^2\) splitting, not a surrogate replacement of original \(A_*\).

## 3. Entire infinite complement inverse response, bounded RELATIVE to true original negative energy

The full original complement remains \(F=E_0^\perp\), so BOTH inherited original estimates \(\varepsilon,\mu\) apply **unchanged**; pulling the finite complement through \(A_*^{-1}\) does not move F.

For \(e\in E_A\) and \(v\in F\), the full genuine \(K_-\succeq0\) yields
\[
|\langle v,K_-e\rangle|^2
\le\langle v,K_-v\rangle\langle e,K_-e\rangle
\le\varepsilon\|v\|_2^2\langle e,K_-e\rangle.
\]
Therefore
\[
\boxed{\|Q_0K_-e\|_2^2\le\varepsilon\,\langle e,K_-e\rangle.}
\]
Since \(D_F^{-1}\preceq\mu^{-1}I_F\), the **complete original infinite-domain mixed inverse response**, with all signed-negative frequencies, satisfies the stronger **vectorwise relative** bound
\[
\boxed{
0\le\langle Q_0K_-e,D_F^{-1}Q_0K_-e\rangle
\le\frac{\varepsilon}{\mu}\langle e,K_-e\rangle.
}
\]
This estimate avoids both the weak global \(\|K_-\|\) factor used in SM33 and the ill-conditioned coordinate norm of 470 source basis generators.

The exact ORIGINAL full signed Schur on \(E_A\) is
\[
\boxed{
S_A[e]
=a_*(e,e)-\langle e,K_-e\rangle
-\langle Q_0K_-e,D_F^{-1}Q_0K_-e\rangle.
}
\]
A complete (closed-form) block minimization gives
\[
\boxed{
\operatorname{ind}_{-}(W_o)=\operatorname{ind}_{-}(S_A),\qquad
W_o\succeq0\iff S_A\succeq0
}
\]
subject to the inherited original closed form/domain and strictly positive F. The finite sign condition is **exact** but still **OPEN**: no numerical full original \(S_A\) is asserted.

The new relative full Schur lower bound is
\[
\boxed{
S_A[e]\ge
a_*(e,e)-\left(1+\frac{\varepsilon}{\mu}\right)\langle e,K_-e\rangle.
}
\]
This holds for EVERY \(e\in E_A\), hence for all exceptional combinations and the entire original infinite complement simultaneously.

## 4. An exact simple 470-dimensional **full-operator** sufficient acceptance threshold

The exact 107-cluster original \(\varepsilon<1/15000\) and \(\mu=17/25000\) give
\[
\frac{\varepsilon}{\mu}<\frac{5}{51},\quad
1+\frac{\varepsilon}{\mu}<\frac{56}{51},\quad
\boxed{\frac{\mu}{\mu+\varepsilon}>\frac{51}{56}=0.910714285714\ldots.}
\]
Define **actual original finite** quadratic forms, indexed by \(h,k\in E_0\), via the unmodified original whole-positive inverse:
\[
\mathsf G(h,k)=\langle h,A_*^{-1}k\rangle,\qquad
\mathsf N(h,k)=\langle A_*^{-1}h,K_-A_*^{-1}k\rangle.
\]
Here \(K_-\) includes the complete seven-prime negative frequency and the source basis is the genuine 470-generator original E0. \(\mathsf G\) is SPD; \(\mathsf N\) PSD. The complete original odd signed positivity **would follow** if the following **single finite generalized-eigenvalue matrix test** can be certified:
\[
\boxed{\mathsf N\preceq\frac{51}{56}\,\mathsf G\quad\text{on all }E_0.}
\]
Indeed, for every \(h\ne0\), \(e=A_*^{-1}h\ne0\) and the exact original full Schur obeys
\[
S_A[e]\ge\mathsf G[h]-
 \left(1+\frac{\varepsilon}{\mu}\right)\mathsf N[h]
>\mathsf G[h]-\frac{56}{51}\cdot\frac{51}{56}\mathsf G[h]=0.
\]
Thus this gate would deliver **strict whole-original ODD positivity** with all infinite signed negative residual and true pole/high-frequency positive continuum included. It is a **sufficient**, not necessary, gate: if it fails, the true signed \(W_o\) could still be positive, and the exact corrected \(S_A\) remains the necessary/sufficient acceptance.

**SM34 DOES NOT EVALUATE OR CERTIFY \(\mathsf N\preceq(51/56)\mathsf G\).** The finite original \(A_*^{-1}\) source Gram and entire \(K_-\) mixed Gram must be computed with all original source cross/covariance, or a direct positive-energy coercivity proof found. Thus full W-ODD-NEG O1/O2 remains OPEN.

## 5. Exact rational regression and next action

The SM34 focused validator:
- Replays **all original** SM33 full 973-leaf/107-cluster weighted odd complement bound, including \(\varepsilon<1/15000\), the SI10/SM32 \(\mu\) floor, original pole-conditioned SI29/SM17 \(\kappa_*>0\), and the 470-dimensional original physical source count.
- Verifies the exact rational \(\varepsilon/\mu<5/51\), source-independent **\(51/56\)** acceptance threshold, and a sharper computed decimal for \(\mu/(\mu+\varepsilon)\).
- Uses **exact Fraction selfadjoint finite physical 2×2 positive A and PSD K** to verify the *nonorthogonal* energy-dual basis \(E_A=A_*^{-1}E_0\), a nonzero originally missed L2 positive cross which **vanishes in the full \(A_*\)-energy form**, complete finite Schur congruence, and the possibility that both uncorrected blocks are positive while the coupled full signed matrix is indefinite. A second rational case passes the sufficient \(51/56\) gate and independently proves full 2×2 PSD.
- Preserves the mandatory original full PS36 O1/O2, E1–E4, whole Weil, CC27 D-Riesz and RH **OPEN** in machine-readable custody. Scoped arithmetic and finite algebra tests do not certify the inherited full functional analysis on their own.

**SM35 next acceptance:** build a rigorously enclosed true original generalized finite pair \((\mathsf G,\mathsf N)\) on the b9 470-source \(E_0\) using the original positive-pole-resolvent source response and all original signed-negative seven-prime Fourier covariance. Certify the **complete generalized eigenvalue** maximum \(\lambda_{\max}(\mathsf G^{-1/2}\mathsf N\mathsf G^{-1/2})\le51/56\), retaining all cross terms and infinite residual; do not use 2D Ritz, selected positive windows or surrogate lower-reference failures to promote. If that conservative gate fails, evaluate the exact \(S_A\) residual Schur instead. Canonical whole-original W-ODD-NEG, even E1–E4, signed Weil, native CC27 D-Riesz and RH stay OPEN.

Replay: \`python3 scripts/validate_rpb108_sm34_positive_energy_dual_schur.py\`.
