# Weil-Lab — IV049
## Uniform physical-cell interface bound; asymptotically vanishing energy-relative *single-column* Schur correction

**Standing:** Analytic-only under incident #834. Original-source classical mathematical arguments, with an **executed exact-rational/integer/Taylor checker**. **NONKERNEL**: no IV049 Lean source, compiler, strict axiom audit, PR, commit, branch, workflow or rerun. No global signed Weil positivity, independent PI/CP equivalence, or RH claim. The actual source Γ Fourier-atom inverse and closed-form identity still require pinned-source formalization.

## 1. Original object and the distinction left open by IV048

Let \(I=(-11/10,11/10)\), and partition it into \(M\) equal physical cells \(J_j\) of width \(w=11/(5M)\). Let \(\Pi_M\) be the \(L^2(I)\) projection onto normalized cell indicators \(e_j=\mathbf 1_{J_j}/\sqrt w\), and \(Q_M=1-\Pi_M\). The **genuine original** real signed source form is
\[
W=\Gamma-P_{\rm original}+|h\rangle\langle h|-|k\rangle\langle k|,
\quad h=\sqrt2\,\mathbf1_I\cosh(x/2),\ k=\sqrt2\,\mathbf1_I\sinh(x/2).
\]
The Γ symbol is the actual \(\gamma(t)=\operatorname{Re}\psi(1/4+it/2)-\log\pi\), the original prime P contains the true two-sided von Mangoldt \(n=2,3,4,5,7,8,9\) shifts, and the two true crossed poles are retained. The classically derived NF599/PI007 physical-kernel identity gives
\[
\Gamma=\gamma(0)I+L_K,\qquad K(s)=\frac{e^{-s/2}}{1-e^{-2s}}>0\quad(s>0),
\qquad L_Kf(x)=\int_{\mathbb R}K(|x-y|)(f(x)-f(y))dy.
\]
The form is initially defined on supported Schwartz tests and completed in the logarithmic-energy form norm; indicators and the contrast profiles below belong to its classical form and operator domains. The **source attached Lean Fourier inverse/domain bridge is still OPEN**, and strict source phase/normalization remain as in the repository IV011/IV017/NF599 definitions.

The IV047 lower bound is \(C_M:=Q_MWQ_M\ge c_M Q_M\), \(c_M>0\), on the closed high-mode form domain. IV048 proved the **unweighted** block \(B_M=Q_MW\Pi_M\) has \(\|B_M\|>1/4\) in both authentic reflection-parity sectors for its 100000- and 132000-cell meshes. It does **not** determine the **energy-relative** Schur correction \(B_M^*C_M^{-1}B_M\).

## 2. New uniform one-cell source interface theorem

For **every** cell \(J=(a,a+w)\subset I\) with \(0<w\le1/1000\), let \(e_J=\mathbf1_J/\sqrt w\). Then the true source low/high block satisfies
\[
\boxed{\|Q_MW e_J\|_2<\frac{49}{5}=9.8<10.}\tag{IV049-A}
\]
Importantly this holds *uniformly in the number and physical position of the cells*, even though the original Gamma kernel is logarithmically singular at every cell boundary. No prime term is suppressed from the ambient operator.

**Exact Gamma argument.** IV048 already established the antiderivative
\[
H(s)=\operatorname{atanh}(e^{-s/2})+\arctan(e^{-s/2}),\qquad H'(s)=-K(s).
\]
For \(x=a+wu\) inside \(J\),
\[
(L_Ke_J)(x)=w^{-1/2}\{H(wu)+H(w(1-u))\}.
\]
For \(w\le1/1000\), the source local kernel comparison \(0\le K(s)-1/(2s)\le1\) for \(0<s\le w\) gives
\[
H(wu)+H(w(1-u))=2H(w)
+\tfrac12\log\frac1{u(1-u)}+r(u),\quad0\le r(u)\le2w.
\]
After subtracting the mean on that cell, \(2H(w)\) vanishes. Because
\(\int_0^1(-\log u-1)^2du=1\) and similarly for \(1-u\), the centered logarithmic part has \(L^2(0,1)\) norm \(\le1\). Hence the actual inside-cell projected Gamma norm is at most \(1+2w\).

For \(x\notin J\), writing \(d\) for the distance to the nearest boundary, the **global** bound
\(K(s)\le1/(2s)+1\) gives
\[
|(L_Ke_J)(x)|\le w^{-1/2}\left[\tfrac12\log(1+w/d)+w\right].
\]
An elementary integral comparison yields
\[
\int_0^\infty\log^2(1+1/u)du
< (\log2)^2+2\log2+3<\frac{489}{100}.
\]
Using both exterior sides (each shorter than \(|I|=11/5\)), \((a+b)^2\le2a^2+2b^2\), and contracting by the full cellwise projection, we obtain
\[
\|Q_M\Gamma e_J\|_2^2
\le(1+2w)^2+\frac{489}{100}+\frac{44}{5}w
<\left(\frac52\right)^2\qquad(0<w\le1/1000).
\tag{IV049-B}
\]
The constant \(\gamma(0)e_J\) lies in \(\mathrm{ran}\,\Pi_M\), so it contributes nothing to \(Q_M\Gamma e_J\).

**Genuine remaining source terms.** The original two-sided prime operator has \(\|P_{\rm original}\|<71/10\). For the authentic crossed poles, original-window Taylor bounds yield \(\|h\|^2<5\), \(\|k\|^2<1/2\), \(\|h\|_\infty<2\), \(\|k\|_\infty<1\), hence
\[
\|(|h\rangle\langle h|-|k\rangle\langle k|)e_J\|
<6\sqrt w<1/5.
\]
Therefore \(\|Q_MW e_J\|<5/2+71/10+1/5=49/5\), proving (IV049-A). The checker verifies the rational coefficient comparison and the exact Taylor inequalities, rather than relying on floating point.

## 3. A new energy-relative asymptotic theorem — and its exact limitation

Define for low \(v\in\mathrm{ran}\Pi_M\) the **intrinsic-to-this-split** Schur loss
\[
\mathcal S_M[v]:=\sup_{0\ne q\in Q_M\cap\mathcal Q_K}\frac{|W(v,q)|^2}{W[q]}.
\]
When \(C_M\ge c_M>0\), the ordinary closed-form Lax–Milgram representation identifies it with \(\|C_M^{-1/2}B_Mv\|^2\), or with \(\langle v,B_M^*C_M^{-1}B_Mv\rangle\) where the stated operator-domain identification holds.

For **one normalized physical cell** \(e_J\), (IV049-A) gives
\[
\boxed{0\le\mathcal S_M[e_J]<\frac{(49/5)^2}{c_M}<\frac{100}{c_M}.}\tag{IV049-C}
\]
Furthermore, IV047's physical-cell Fourier concentration bound and the NF599 high-frequency gamma growth imply
\[
\boxed{c_M\longrightarrow+\infty\quad\text{as}\quad w=11/(5M)\downarrow0.}\tag{IV049-D}
\]
Indeed for any prescribed \(A>0\), choose a fixed Fourier cutoff \(R\) sufficiently high that the source Gamma symbol obeys \(\gamma(2\pi\xi)>A\) for \(|\xi|\ge R\); its NF599 nonnegative gain series implies this is possible. All frequencies still have \(\gamma>-28/5\). Every \(q\in Q_M\) has low-band fraction at most \((2Rw)^2\), and the true prime and negative-pole cost is less than \(71/10+12/25=379/50\). Therefore
\[
W[q]\ge\left[A-(A+28/5)(2Rw)^2-379/50\right]\|q\|^2.
\]
Fix A arbitrarily large, then send w to zero; this proves (IV049-D). In particular,
\[
\boxed{\sup_{J\text{ a cell}}\mathcal S_M[e_J]\longrightarrow0.}\tag{IV049-E}
\]
So the nonzero **bare** IV048 coupling and the **vanishing relative Schur penalty on any individual localized column** are simultaneously true. They probe different operator norms.

**Sparse combination extension.** If \(v=\sum_{j\in S}a_je_j\) uses at most \(s\) cell indicators, then by the triangle inequality and \(\ell^1\le\sqrt s\ell^2\),
\[
\boxed{\mathcal S_M[v]\le\frac{(49/5)^2s}{c_M}\|v\|^2.}\tag{IV049-F}
\]
Thus any family with **fixed s** has asymptotically vanishing energy-relative correction. But general low vectors may use \(s=M\to\infty\). (IV049-F) then gives **no operator-norm decay of** \(\|C_M^{-1/2}B_M\|\), and it gives **no full-window W positivity**. This is a precise remaining *dense-mode/cross-cell cancellation* obligation, not something we silently infer from basis-column control.

## 4. Exact finite-mesh directional Schur intervals

Revisit IV048's specific single-cell mean-zero middle-half contrast
\(q_J=(2\mathbf1_{J_{\rm middle}}-\mathbf1_J)/\sqrt w\).
Its support is one cell, so **all genuine original prime terms on that test vanish**, while both crossed pole residues are retained. The IV042 finite real Gamma atom bound gives for any \(N\)
\[
W[q_J]>\left[-\frac{28}{5}+\sum_{n<N}\frac4{4n+1}-(N+8)w\right]\|q_J\|^2.
\]
At \(N=32768\), a completely independent integer audit establishes
\[
\boxed{\sum_{n=0}^{32767}\left\lfloor10^6\frac4{4n+1}\right\rfloor=14608246.}
\]
Consequently \(W[q_J]>8.287174\) on the 100000-cell mesh, and \(W[q_J]>8.4619793\) on the 132000-cell mesh. The normalized even/odd reflected contrasts also satisfy \(W[q_\pm]>8.28\), after the exact source reflection cross-pair bound of IV048.

The exact atanh series (\(\tfrac12\log(27/16)=\operatorname{atanh}(11/43)\)) and the true pole envelopes give on **both** physical meshes
\[
|W(e_J,q_J)|<131/500,
\quad |W(e_\pm,q_\pm)|<263/1000.
\]
Combining these **upper** bounds with the IV048 strict **lower** directional Schur losses gives the new rigorous brackets
\[
\boxed{\frac1{2128}<\frac{|W(e_J,q_J)|^2}{W[q_J]}<\frac{17161}{2070000}\approx0.00829034,}\tag{IV049-G}
\]
\[
\boxed{\frac1{4240}<\frac{|W(e_\pm,q_\pm)|^2}{W[q_\pm]}<\frac{69169}{8280000}\approx0.00835374.}\tag{IV049-H}
\]
The inequalities are **for this one specifically constructed high direction** and its two parity reflections, not for the supremum over all high modes. They do not certify a positive full Schur complement. In particular, comparing their upper values with IV046's unrelated low-mode Rayleigh value does **not** prove positivity of any combined finite-plus-infinite operator.

## 5. Verification and future falsifiable gate

The executable local standard-library checker `IV049_energy_relative_cell_schur_checker.py` verifies exact source physical widths, 32768-term integer Gamma floor sum, all displayed rational inequalities, exp/sinh/cosh Taylor upper enclosures for the exact original pole norm and pointwise bounds, source IV048 atanh upper series, finite-mesh Schur loss brackets, and source checker SHA identities. Its report is `IV049_energy_relative_cell_schur_receipt.json`; the source script SHA256 is `2a2010172c9bda33c3c58477b8ada82ba850862ba96442e528425e342590144d`.

The **continuum** claims (Gamma inverse Fourier atom, global kernel, Poincaré/Bernstein, closed form/domain, bound \(c_M\to\infty\), operator Schur identification) have analytical proofs above or in IV043/IV047/IV048 but are **not machine-proved** by the checker and **not new Lean PASS**. The exact 100000 and 132000 meshes are coordinate-dependent, not independent PI/CP invariants. A proposed independent spectral transport must preserve both bare seam coupling and its correctly normalized form-domain energy if it claims equivalence.

**Precise next IV050 target (still analytic-only):** control \(\|C_M^{-1/2}B_M\|\) on the whole **dense** low cell-average space, including simultaneously many neighboring cells and their authentic prime-shift geometry. Test if a square-function estimate, discrete commutator bound or parity-sensitive block preconditioner yields a usable a posteriori Schur certificate. Do not infer uniform operator decay or global Weil/RH positivity from (IV049-E)/(IV049-F).

**Historical numerical/Lean custody (not changed by this investigation):** Phase III NF750–NF753 true kernel/strict-axiom PASS, 692/968 kernel-passed original HD/A frontiers versus the body of canonical registry #761 historically recording 628/968 until reconciliation; original IV009 Lean PASS; IV018/IV023 pre-Lean manifest failures, no accepted Lean certificates. At IV048 passive CI inspection, queued Actions count 0 while 15 were in progress; check live status separately before citing current counts. Incident #834 analytic-only hold remains active until operator criteria are met.
