# Weil-Lab — IV048
## Original Gamma cell-boundary potential, unavoidable low/high mixed coupling, and quantitative Schur correction

**Operating status:** ANALYTIC-ONLY. Classical/source-matched mathematical theorem with an **executed exact rational checker** and a separate optional numerical sanity test; **NOT a new Lean kernel theorem**. No research branch, PR, commit, workflow, run, rerun, or change to the protected certification inventory. The original signed Weil form, its physical window and its two crossed poles are unchanged. Full global Weil positivity, independent PI/CP spectral equivalence, and RH are not claimed.

### 1. Why this calculation is necessary after IV047

On the original window \(I=(-11/10,11/10)\), IV047 established an analytical high-mode bound \(W|_{Q_M}>cI\) for the mean-zero complement of an equal physical-cell partition. At \(M=100000\), \(c=1/100\) is conservative. The remaining finite-partition identity is
\[
 W=\begin{pmatrix}L&B^*\\B&C_Q\end{pmatrix},\qquad
 L=\Pi_M W\Pi_M,\quad B=Q_M W\Pi_M,\quad C_Q=Q_MWQ_M.
\]
Positive \(C_Q\) and positive \(L\) do **not** entail positivity of \(W\); the genuine Schur condition is \(L-B^*C_Q^{-1}B\ge0\), under the operator-domain assumptions detailed in IV047. This IV048 investigation tests whether the correction might be negligible on a sufficiently fine partition. **It is not negligible in operator norm.**

### 2. Source-exact logarithmic Gamma boundary potential

The actual pinned NF599 Gamma/digamma positive-gain series and the *classically derived* PI007/PI008 Fourier atom imply
\[
 \Gamma[f,g]=\gamma(0)\langle f,g\rangle+D[f,g],\qquad
 D[f]=\frac12\iint K(x-y)|f(x)-f(y)|^2dx\,dy,
\]
where \(K(u)=e^{-|u|/2}/(1-e^{-2|u|})\) for nonzero \(u\). **The direct original IV011 Fourier inversion/form-domain attachment is not yet an accepted Lean proof.** On a physical cell \(J=(a,b)\subset I\) set \(e_J=1_J/\sqrt w\), \(w=b-a\). The Dirichlet generator acting on this indicator is, for \(x\in J\),
\[
 (L_K 1_J)(x)=\int_{\mathbb R\setminus J}K(x-y)dy=H(x-a)+H(b-x),
\]
where the genuine real-place antiderivative is
\[
 \boxed{H(s)=\int_s^\infty K(u)du
 =\operatorname{atanh}(e^{-s/2})+\arctan(e^{-s/2})},\qquad H'(s)=-K(s).
\]
The closed form follows by differentiating with \(z=e^{-s/2}\); both sides vanish as \(s\to+\infty\). Outside \(J\), the generator is \(-\int_JK(x-y)dy\), and its logarithmic boundary singularities are \(L^2\)-integrable. As \(\gamma(t)=O(\log(2+|t|))\) from the same positive-gain series, the \(O(1/|\xi|)\) Fourier tail of an interval indicator shows **\(e_J\) lies in the physical-window self-adjoint operator domain** of the classical compressed Gamma, prime, and pole form. The precise statement still needs a source-bound Lean form-domain proof.

An elementary *uniform quantitative kernel estimate* holds on \(0<s\le1/10\):
\[
 \boxed{0\le K(s)-\frac1{2s}\le1.}\tag{A}
\]
For the upper inequality, \(e^{-s/2}\le1\) and \(1/(1-e^{-2s})\le1+1/(2s)\), by \(e^{2s}\ge1+2s\). For the lower inequality, write \(F(s)=2se^{-s/2}+e^{-2s}-1\). Then \(F(0)=0\) and, using \(e^{-s/2}\ge1-s/2\) and \(e^{-2s}\le1-2s+2s^2\),
\[
 F'(s)=e^{-s/2}(2-s)-2e^{-2s}
 \ge 2s-\frac72s^2>0\qquad(0<s\le1/10).
\]
Thus \(F(s)>0\), equivalently \(K(s)\ge1/(2s)\). These estimates establish
\[
 H(wu)=H(w)+\tfrac12\log(1/u)+r_w(u),\qquad 0\le r_w(u)\le w
 \quad (0<u<1,\ 0<w\le1/10).
\]

### 3. A universal nonvanishing original-W low/high interface

On an actual cell \(J=(a,a+w)\), introduce the normalized **mean-zero high test**
\[
 e_J(x)=\frac{1_J(x)}{\sqrt w},\qquad
 q_J(x)=\frac{2\,1_{(a+w/4,a+3w/4)}(x)-1_J(x)}{\sqrt w}.
\]
Then \(\|e_J\|=\|q_J\|=1\), \(\langle e_J,q_J\rangle=0\), and \(q_J\in\ker\Pi_M\) for the whole equal-cell partition. Both are actual finite-Gamma-energy form-domain tests, though not Schwartz; they admit genuine supported smooth approximations, including mean-preserving approximations of \(q_J\) on each cell.

With \(s(u)=+1\) for \(1/4<u<3/4\) and \(-1\) on the outer quarters, the source Gamma mixed term is **exactly**
\[
 \Gamma[e_J,q_J]
 =\int_0^1 s(u)\left(H(wu)+H(w(1-u))\right)du
 =-\frac12\log\frac{27}{16}+\varepsilon_w,
 \qquad |\varepsilon_w|\le2w.
\]
The logarithm is not a numerical approximation: integrating \(\log(u(1-u))\) on the three rational subintervals yields \(\int s(u)\log[u(1-u)]du=\log(27/16)\). The exact arctanh expansion \(\log(27/16)=2\operatorname{atanh}(11/43)>22/43\) gives
\[
 \Gamma[e_J,q_J]\le-\frac{11}{43}+2w.
\]
There are **no same-cell original prime correlations**, because \(w<\log2\), and the two *true crossed* source Mellin residues obey
\[
 |\mathrm{Pole}(e_J,q_J)|\le 8\|e_J\|_1\|q_J\|_1=8w.
\]
Consequently the **complete original signed Weil mixed form** satisfies the strict bound
\[
 \boxed{\operatorname{Re}W(e_J,q_J)<-\frac{11}{43}+10w.}\tag{B}
\]
For either of IV047's existing source partitions, \(M=100000\) (\(w=11/500000\)) or \(M=132000\) (\(w=1/60000\)), this is **strictly less than \(-1/4\)**. Thus the true mixed physical low/high block obeys
\[
 \boxed{\|Q_M A_W\Pi_M\|_{\rm op}>1/4}\tag{C}
\]
under the source form/operator-domain identification. This is an explicit **failure of norm-smallness**, not a negative full-Weil diagonal test. In fact the result persists as \(w\downarrow0\), with source Gamma pairing tending to \(-\tfrac12\log(27/16)\), while the actual pole cross contribution decays at least linearly with \(w\).

### 4. It persists independently in BOTH reflection parity sectors

Pick the **literal** right-hand physical cell containing \(1/4\), and its reflected left-hand cell. Exact geometry for the existing partitions is:

| \(M\) | Right-cell zero-based index | Actual right physical interval | Reflected index | Cell width |
|---:|---:|---|---:|---:|
| 100000 | 61363 | \((124993/500000,\ 31251/125000)\) | 38636 | \(11/500000\) |
| 132000 | 81000 | \((1/4,\ 15001/60000)\) | 50999 | \(1/60000\) |

The supports lie on opposite sides of zero, separated by more than \(49/100\), with the combined diameter below \(51/100<\log2\). Therefore **even the cross-reflection prime term is exactly zero**. The original Gamma kernel bound gives \(K(\delta)<99/49\), and the original two crossed poles contribute at most \(8w\), hence every cross-reflection mixed entry is bounded by \(<11w\) in modulus.

Form normalized real even and odd tests \(e_\pm=(e_J\pm e_{-J})/\sqrt2\) and \(q_\pm=(q_J\pm q_{-J})/\sqrt2\). By actual source reflection invariance and Hermitian symmetry,
\[
 \boxed{\operatorname{Re}W(e_\pm,q_\pm)<-\frac{11}{43}+21w<-\frac14.}\tag{D}
\]
Thus **both** compressed parity-resolved mixed block norms exceed \(1/4\). This is a falsifiable source-support observation relevant to CP: a representation based solely on cell means that discards its high-mode boundary interface is not compatible with the original signed form, even if its finite prime spectrum matches.

### 5. A strictly nonzero Schur correction — without assuming spectral invertibility

A direct positive high-mode test makes the cost of ignoring the interface quantitative. For any interval \(L\) the exact NF599/IV043 single-atom calculation is
\[
 D[1_{(0,L)}]=\sum_{n\ge0}\frac{1-e^{-2(n+1/4)L}}{2(n+1/4)^2}
 \le L\sum_{n<N}\frac1{n+1/4}+\sum_{n\ge N}\frac1{2(n+1/4)^2}.
\]
Set \(N=2^{17}=131072\). Exact dyadic harmonic blocks show \(\sum_{n<N}1/(n+1/4)\le4+17=21\); integral comparison bounds the tail by \(1/[2(N-1)]\). For either of the IV047 mesh widths, this tail is \(<w/2\), so
\[
 \frac{D[1_J]}w<22,\qquad \frac{D[1_{\mathrm{middle}\,J}]}w<11.
\]
By the quadratic triangle inequality,
\[
 D[q_J]\le\frac8wD[1_{\mathrm{middle}\,J}]+\frac2wD[1_J]<132.
\]
The actual original \(\gamma(0)<0\), same-cell prime term is zero, and \(|\mathrm{Pole}[q_J]|\le8w\), hence
\[
 \boxed{0<W[q_J]<133.}
\]
Positivity uses the *previous IV047 high-mode theorem*, not the sign of the Gamma term alone. Reflection combinations similarly satisfy \(0<W[q_\pm]<265\).

For any **fixed** normalized low test \(e\) and actual high test \(q\) with \(W[q]>0\), the *exact variational completion-of-squares* identity, valid on the common form domain, is
\[
 \inf_{z\in\mathbb C}W[e+zq]
 = W[e]-\frac{|W(e,q)|^2}{W[q]}.
\]
The explicit IV048 tests therefore force the **nonzero** reductions
\[
 \boxed{\inf_zW[e_J+zq_J]<W[e_J]-\frac1{2128}},\tag{E}
\]
\[
 \boxed{\inf_zW[e_\pm+zq_\pm]<W[e_\pm]-\frac1{4240}}.\tag{F}
\]
These are rigorous *lower bounds on the amount of Schur correction* along specific source directions, not a computed full finite Schur complement. In particular, dropping the cross block is demonstrably incorrect. Conversely, knowing only \(\|B\|>1/4\) and \(C_Q\ge1/100\) makes the naive worst-case norm subtraction \(\|B\|^2/(1/100)>25/4\); this loose estimate cannot resolve a near-zero low-sector margin such as IV046's \(0.0087\) upper bound. **This does NOT imply that the true Schur correction is as large as \(25/4\)**; the true positive high operator can be much larger on the particular boundary directions.

### 6. Domain, originality and what remains open

- True source actual original diagonal \(W=\gamma(0)I+D-P+\mathrm{Pole}_{\rm cross}\); original first-slot antilinearity, full two-sided von Mangoldt weights, and both crossed residues preserved. The present compact two-cell witnesses are prime-free *on their own supports*, but no prime term has been removed from the ambient operator, Schur complement or previous IV047 high-mode estimate.
- \(V_M\) cell indicators and the high contrast tests belong to the **classically established original Gamma form domain**, not the Schwartz class. Smoothing transfers the variational strict inequalities to source Schwartz tests; it does not mean their smoothed approximants lie exactly in \(V_M\). The closed-form/operator-domain and finite Fourier inverse identity require eventual source-SHA-bound Lean proof.
- \(H(s)\), its logarithmic boundary behavior, and the mixed cell/contrast pairing are *intrinsic to the original Gamma physical kernel*; the numerical \(M,w\), physical-cell basis, and \(1/4\) positioning are coordinate- and partition-dependent. Do not treat \(\|B_M\|\) as an abstract invariant transported automatically to an independent PI/CP construction.
- No global lower bound for \(W\) on the full fixed window has been established. Neither a negative Weil diagonal nor a failure of RH has been found.

**Precisely missing next bound:** A useful IV049 target is an *energy-relative* mixed estimate \(\|C_Q^{-1/2}B\|\), rather than \(\|B\|\) alone. Any certified bound must include the true cell-boundary logarithmic Gamma action and simultaneous cross-cell interactions. It must be compared with the actual finite low-form eigenstructure and must not replace the infinite-dimensional resolvent by a zero block.

### 7. Local verifier and passive CI status

The executable pure-stdlib script `IV048_mixed_block_nonvanishing_checker.py` checked rational interval geometry, both 100000/132000 partitions, exact \(\log(27/16)>22/43\) arctanh lower bound, same/reflected prime exclusions, true two-pole mixed envelope, finite-atom harmonic/tail bounds, both parity mixed comparisons, and exact variational Schur-loss fractions. The checker passed and wrote `IV048_mixed_block_nonvanishing_receipt.json`, binding its SHA256 and source checker SHA256s. The calculus/kernel identity and form closure are **written mathematical arguments, not machine formalized**.

Passive GitHub Actions snapshot during IV048: protected original NF750–NF753 all successful source-specific kernel/strict 35-declaration axioms; IV009 accepted; IV018/IV023 failed earlier at the same `lake-manifest.json` Python source preflight, both before Lean. The **live queued count reached 0** in a non-atomic GitHub API snapshot. Queue clearance alone does not lift the #834 incident hold, certify IV018/IV023 or reconcile the #761 registry body's historical **628/968** with the newer **692/968 kernel-passed** frontier. No new CI work was initiated.
