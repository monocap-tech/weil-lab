# Weil-Lab — IV047
## Explicit infinite-dimensional high-mode coercivity and a finite-codimension Schur reduction

**Status:** new original-source mathematical theorem plus executed exact integer/Fraction preflight. **NONKERNEL**: no IV047 Lean theorem, no new branch, commit, PR, Actions dispatch, rerun, or CI workload under the user-directed #834 analytical-only hold. No claim of positivity on the full original window, an independent spectral equivalence, or RH.

### 1. Original-source dictionary

Fix the original symmetric logarithmic physical support window
\[
I=(-11/10,11/10),\qquad |I|=11/5.
\]
Extend every test by zero outside \(I\). The original first-slot-antilinear signed Schwartz form is
\[
\operatorname{Re}W[f]=\Gamma[f]-P_{\rm orig}[f]+\operatorname{Pole}_{\rm cross}[f],
\]
with actual NF599 digamma symbol \(\gamma(t)=\Re\psi(1/4+it/2)-\log\pi\), original ±log(n) translated prime correlation with \(\kappa_n=\Lambda(n)/\sqrt n\) and all \(n\in\{2,3,4,5,7,8,9\}\), and the exact two crossed Mellin poles. The unitary Fourier variable is \(\widehat f(\xi)=\int f(x)e^{-2\pi i\xi x}\,dx\); hence \(\Gamma[f]=\int\gamma(-2\pi\xi)|\widehat f(\xi)|^2d\xi\).

The source input for this mathematical theorem is the exact NF599 positive-gain formula and global Gamma lower \(\gamma(t)>-28/5\), as well as the original IV011 full-source pole-minus-prime-plus-Gamma decomposition, IV017 Fourier diagonal, and IV043's analytic Gamma difference-form/closed-form completion. **Source-connected Lean proof of the Gamma finite inverse Fourier atom and the full form-domain bridge is still outstanding.** The new arithmetic checker does not substitute for those proofs.

### 2. An explicit high-frequency Gamma certificate

For \(a_n=n+1/4\) and \(t=30000\), the genuine NF599 positive gain equals the rational number
\[
g_n(30000)=\frac{(15000)^2}{a_n(a_n^2+15000^2)}
=\frac{14,400,000,000}{(4n+1)((4n+1)^2+3,600,000,000)}.
\]
The *actual executed* integer checker verifies the exact identity
\[
\boxed{\sum_{n=0}^{19999}\lfloor10^7g_n(30000)\rfloor=136191112.}
\]
Since the source \(\gamma(0)>-28/5\) and gains are nonnegative and monotone in \(|t|\), it follows mathematically that
\[
\gamma(t)>-\frac{28}{5}+\frac{136191112}{10^7}
=\frac{10023889}{1250000}>8\qquad(|t|\ge30000).
\]
This is **exact finite arithmetic**, not floating-point sampling of the digamma function or a new compiled NF599 Lean theorem.

Use the rational low-frequency cutoff \(R=5000\) in \(\xi\). For \(|\xi|\ge5000\), \(2\pi|\xi|\ge10000\pi>30000\), using \(\pi>3\). For all frequencies the original \(\gamma>-28/5\) persists.

### 3. Exact physical-cell Fourier concentration inequality

Partition \(I\) into \(M\) equal half-open cells \(I_j\) of width \(w=|I|/M\), and denote the L²-orthogonal projection to their characteristic-function span by \(\Pi_M\). Its complement consists of functions \(q\) satisfying the **exact moment constraints** \(\int_{I_j}q(x)dx=0\) for every \(j\). This includes an infinite-dimensional subspace of supported complex Schwartz functions.

Let \(\mathcal B_R\) be the Fourier band projection to \(|\xi|\le R\). We claim the **uniform operator inequality**
\[
\boxed{\|\mathcal B_Rq\|_2^2\le(2Rw)^2\|q\|_2^2\quad(q\perp\operatorname{ran}\Pi_M).}\tag{IV047-band}
\]
Proof: by L² duality, test \(\mathcal B_Rq\) against any unit bandlimited \(v\). Since \(q\) has zero mean on each cell,
\[
|\langle q,v\rangle|=|\langle q,v-\Pi_Mv\rangle_{L^2(I)}|
\le\|q\|_2\|v-\Pi_Mv\|_{L^2(I)}.
\]
The **sharp interval Neumann Poincaré–Wirtinger inequality** on each length-\(w\) cell gives
\[
\|v-\Pi_Mv\|_{L^2(I)}\le\frac w\pi\|v'\|_{L^2(I)},
\]
while the **bandlimited Bernstein estimate** (Plancherel) gives \(\|v'\|_{L^2(\mathbb R)}\le2\pi R\|v\|_2\). Combining and taking the dual supremum yields \(\|\mathcal B_Rq\|_2\le2Rw\|q\|_2\). No restriction on the phase, parity or Mellin moments of \(q\) is needed. A bandlimited \(v\) is smooth, so cell averages are well-defined.

Consequently, \(\Gamma[q]\) has the **source-based real signed lower bound**
\[
\Gamma[q]\ge8\|q\|^2-\bigl(8+28/5\bigr)\|\mathcal B_Rq\|^2
\ge\left[8-\frac{68}{5}(2Rw)^2\right]\|q\|^2.\tag{IV047-Gamma}
\]
Strictness is inherited from the genuine Gamma symbol lower bound.

### 4. Source prime and both original pole terms

Original source support and exact \(\log10>11/5\) leave precisely the active prime powers \(n\in\{2,3,4,5,7,8,9\}\). Their authentic two-sided translated correlations obey
\[
P_{\rm original}[q]\le2\sum_{n\in\mathcal N}\frac{\Lambda(n)}{\sqrt n}\,\|q\|^2<\frac{71}{10}\|q\|^2.
\]
The executed checker recomputes this strict upper bound by outward rational \(\log p\) enclosures and integer-square-root bounds, using **every genuine active prime power**, not a graph proxy.

Both original Mellin residues retain their true, **indefinite** form:
\[
\mathrm{Pole}_{\rm cross}[q]=|\langle h,q\rangle|^2-|\langle k,q\rangle|^2,
\quad h=\sqrt2\,1_I\cosh(x/2),\quad k=\sqrt2\,1_I\sinh(x/2).
\]
The exact Taylor-tail audit encloses \(\|k\|^2=2(\sinh(11/10)-11/10)<12/25\). Hence
\[
\mathrm{Pole}_{\rm cross}[q]\ge-\|k\|^2\|q\|^2>-\frac{12}{25}\|q\|^2.
\]
The positive even pole has **not** been discarded as negative; it is retained then used only favorably for a rigorous lower bound.

Together with (IV047-Gamma), for **every** original-window supported complex Schwartz \(q\) with all cell means zero:
\[
\boxed{
\mathrm{Re}W[q]>
\left[\frac{21}{50}-\frac{68}{5}(10000w)^2\right]\|q\|_2^2.
}\tag{IV047-general}
\]
A strictly positive high-mode coefficient follows whenever
\[
\boxed{w<\frac{1}{10000}\sqrt{\frac{21}{680}}\approx0.0000175734.}
\]
The threshold is **sufficient and estimate dependent**. It does not identify a sharp spectral boundary or the exact global Weil bottom.

### 5. Concrete finite-codimension certificate

Choose the **literal rational physical partition**
\[
M=132000,\qquad w=\frac{|I|}{M}=\frac1{60000},\qquad R=5000.
\]
Then \((2Rw)^2=1/36\), so
\[
\Gamma[q]>\left[8-\frac{68}{5}\frac1{36}\right]\|q\|^2=\frac{343}{45}\|q\|^2.
\]
With the true prime and crossed pole bounds above, the complete source inequality is
\[
\boxed{
\operatorname{Re}W_{\rm original}[q]>
\left(\frac{343}{45}-\frac{71}{10}-\frac{12}{25}\right)\|q\|^2
=\frac{19}{450}\|q\|_2^2,
}\tag{IV047-main}
\]
for **every nonzero complex supported Schwartz \(q\)** whose integral on every rational cell is zero. This covers an infinite-dimensional subspace of **finite codimension at most 132,000** in \(L^2(I)\), with genuine original odd pole and prime shifts present. It extends to the closed log-Gamma form-domain complement by density and lower semicontinuity of the associated Fourier form (strictness can become non-strict upon completion, so \(\ge19/450\) is the safe statement on the closure).

The symmetric equal-cell partition preserves reflection. The high-mode theorem holds independently in even and odd sectors, leaving \(66000\) cell-average dimensions in each. Under the source-attached closed compact-resolvent operator construction of IV043–IV044, the **variational negative eigenvalue count** obeys \(n_-(W)\le132000\) and \(n_-(W_e),n_-(W_o)\le66000\) from this partition alone; the improved 100,000-cell variant below sharpens these to 100,000 and 50,000. These are very coarse **upper index bounds**, not statements that any negative eigenvalues exist. The IV046 low-energy 16-cell trial vectors need not satisfy every fine-cell mean-zero constraint and are not contradicted.

**Improved finite-codimension variant — only 100,000 cell means.** A separately executed exact integer certificate uses \(t=26000\), 100,000 NF599 gain terms, and floor scale \(10^8\):
\[
\boxed{\sum_{n=0}^{99999}\lfloor10^8g_n(26000)\rfloor=1369127830,}
\]
so \(\gamma(t)>8.0912783>8091/1000\) for every \(|t|\ge26000\). Take \(R=4334\) (since \(2\pi R>6R=26004>26000\)), \(M=100000\) and \(w=11/500000\). The exact Fourier low-band fraction is
\[
\beta=(2Rw)^2=\left(\frac{23837}{125000}\right)^2
=\frac{568202569}{15625000000}.
\]
With the same rigorous original two-sided prime upper and negative odd pole bound, the second analytical theorem is
\[
\boxed{
\operatorname{Re}W[q]
>
\frac{205113627821}{15625000000000}\|q\|_2^2
>\frac1{100}\|q\|_2^2
}
\]
for every nonzero original-window supported complex Schwartz \(q\) whose 100,000 rational cell means vanish. This strengthens the **codimension** consequence of IV047: the negative index of the original fixed-window form is **at most 100,000** (50,000 in each reflection sector), subject to the same mathematical source/closed-form identification. It is a **smaller margin** than the 132,000-cell theorem, not a stronger bound on the same class of tests. These are two different high-mode subspaces: fewer constraints yield a larger class of functions.

More expensive but stronger exact rational variants by the same argument: M=176000, w=1/80000 gives lower \(83/400=0.2075\); M=220000, w=1/100000 gives lower \(71/250=0.284\). Those constants are not full-window coercivity coefficients either.

### 6. What this *does* and *does not* reduce

Let \(V_M=\operatorname{ran}\Pi_M\), and \(Q_M=I-\Pi_M\). The IV047 theorem gives a **strict positive lower bound for the compression** \(Q_MWQ_M\) on its source form domain. It does **not** imply \(W\ge0\) on all supported Schwartz functions. In particular, even a positive finite compression \(\Pi_MW\Pi_M\) cannot complete the proof without the mixed block \(Q_MW\Pi_M\): the exact rational 2×2 Hermitian toy with both diagonal blocks positive, \(A=1/100\), \(D=19/450\), and cross entry \(B=1/10\), has determinant \(-431/45000<0\).

**Conditional exact Schur reduction:** if the actual source closed form is represented by self-adjoint \(A_W\), if all piecewise cell indicators lie in its operator domain (as expected from \(\gamma(2\pi\xi)=O(\log(2+|\xi|))\) and their Fourier \(O(1/|\xi|)\) tails), and if the high compression \(C_Q=Q_MA_WQ_M\ge(19/450)Q_M\) is the associated positive self-adjoint Friedrichs compression, define \(B=Q_MA_W\Pi_M\), \(L=\Pi_MA_W\Pi_M\). Then
\[
\boxed{
 A_W\ge0\quad\Longleftrightarrow\quad L-B^*C_Q^{-1}B\ge0
}\tag{IV047-Schur}
\]
with domains/closures properly identified. The residual object is a finite-dimensional **matrix of size 132,000** (or 100,000 using the optimized coarser partition), but its entries contain an **uncomputed infinite-dimensional resolvent correction** \(B^*C_Q^{-1}B\). This is not a finite verification receipt and not a shortcut to RH. The true operator-domain and cross-block attachment need to be formalized; absent them, treat the displayed equivalence as a precise conditional operator-theoretic handoff.

### 7. Reproducibility, Lean source and CI custody

- `IV047_infinite_dim_high_mode_checker.py` — executed pure Python stdlib exact integer/rational audit: 20,000- and 100,000-term Gamma floor-gain certificates, all original active prime powers with outward log/sqrt bounds, two original pole eigenvalue enclosure, exact cell/Fourier/Schur constants, source SHA checks on IV044 and IV046 predecessors.
- `IV047_infinite_dim_high_mode_receipt.json` — SHA256-bound receipt containing all checks, explicit operator-domain and Fourier hypotheses, and no CI promotion claim.
- `IV047_INFINITE_DIMENSIONAL_HIGH_MODE_WEIL_COERCIVITY.md` — this mathematical theorem and the exact remaining domain/cross-block obligations.

**Certification boundary:** no IV047 Lean kernel or `#print axioms` proof, no new source or GitHub Actions job. The Gamma frequency-source equality and infinite-series/inverse Fourier source bridge in IV017/PI007/IV043 remain separate unaccepted Lean gates; mathematical arguments are written here, but exact arithmetic alone does not certify their functional-analytic steps. The previous original-source IV009 Lean mixed Schwartz polarization **PASS**, numerical NF750–NF753 **PASS**, and the 692/968 kernel-passed original HD/A frontier are retained **as compiled evidence**; the canonical #761 registry body still records 628/968 as formally accepted pending independent archive reconciliation of NF750–NF753. IV018 and IV023 both failed earlier at missing `lake-manifest.json` Python source preflight before their Lean compilation started. The #834 analytics-only/no-new-CI directive remains active.

**Next IV048 (analytic-only):** seek a quantitative source-exact bound on the mixed high/low block \(B=Q_MA_W\Pi_M\), using the logarithmic operator action on cell indicators and rigorous a posteriori Schur enclosures. Test whether any *computationally tractable* coarser projection can replace 100,000 means by exploiting genuine prime-shift geometry or finite-rank poles. Preserve source SHA and separate all nonkernel mathematics from Lean acceptance.
