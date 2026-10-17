# SM10 — explicit rational moment matrix for the entire original odd negative-frequency cap

**Canonical obligation:** \`W-ODD-NEG\` **OPEN**.  
**Parent:** SM09 merged at \`750695af1403c8c72fdaa5cb7553722737773b98\` (PR #139).  
**Standing:** proposed exact-rational certificate for an *explicit* global finite weighted odd source, replacing SM09's abstract projected compression. No finite Schur positivity claimed. Focused GitHub Actions and end-head custody required.

## 1. From the certified full negative upper envelope to explicit rational moments

Work on the original physical odd space \(H_o=L^2([-B,B])_{\mathrm{odd}}\), \(B=11/10\). Retain SI10/SM09's original signed seven-prime multiplier \(m(\xi)\), scalar \(\kappa=10^{-3}\), and exact unresolved positive-frequency dyadic leaves \(I=[l,r]\) of the global cover. Each has an outward rational height \(h_I\) with

\[
0\le (\kappa-m(\xi))_+\le w(\xi):=h_I+\kappa,\quad \xi\in I,
\]
and the left-hand side vanishes outside the reflected cover. There are 973 positive-frequency leaves in 107 maximal clusters, all on \([0,896]\); every frequency outside is protected by the original all-real SI10 \(m>\kappa\) argument, including \(|\xi|\ge896\).

For each maximal positive-frequency cluster \(J_j=[a_j,b_j]\), take its rational midpoint \(c_j\), and the exact SI08/SI10 order \(p_j\) at \(b=24\), satisfying the uniform Taylor bound

\[
\|h_\xi-T_j(\xi)\|_{L^2([-B,B])}
\le \sqrt{2B}\,2^{-24},\quad
h_\xi(x)=\sin(2\pi \xi x),
\]
where
\[
T_j(\xi,x)=\sum_{k=0}^{p_j-1}(\xi-c_j)^k u_{jk}(x),
\qquad
u_{jk}(x)=\frac{(2\pi x)^k}{k!}
\sin(2\pi c_j x+k\pi/2).
\]
Every \(u_{jk}\) belongs to the **actual supported odd physical carrier**; there is one real source per Taylor degree, not two complex parity copies. The combined source count is **890**.

Define the exact cap operator
\[
K_{\mathrm{cap},o}=2\int_0^\infty w(\xi)
|h_\xi\rangle\langle h_\xi|\,d\xi
\]
and the explicit Taylor cap
\[
K_{T,o}=\sum_{j=1}^{107}\sum_{0\le k,l<p_j}
C^{(j)}_{kl}|u_{jk}\rangle\langle u_{jl}|.
\]

All source covariance entries are **rational and exactly computable**, even though the physical vectors \(u_{jk}\) contain \(\pi\):

\[
\boxed{
C^{(j)}_{kl}
=
2\sum_{I=[l_I,r_I]\subset J_j}
(h_I+\kappa)
\frac{(r_I-c_j)^{k+l+1}-(l_I-c_j)^{k+l+1}}
{k+l+1}.
}
\]

Crucially, the covariance is *block diagonal in the disjoint frequency clusters*, but **the physical source Gram and the final Birman–Schwinger inverse are not block diagonal**. Every intercluster physical overlap and every odd-pole coupling remains necessary.

Each moment block \(C^{(j)}\) is positive definite: for any nonzero polynomial \(p\) of degree below \(p_j\), \(\int_{J_j}w(\xi)|p(\xi-c_j)|^2\,d\xi>0\), since each cluster has at least one positive-width leaf with \(w\ge\kappa>0\). The validator also checks every entry's exact rational construction and positive rational LDL pivots across all 107 blocks.

## 2. A global certified upper bound with complete coupling payment

Let \(R_{\mathrm{cap}}:H_o\to L^2(\mathbb{R}_+,d\xi)\) be the analysis operator \((R_{\mathrm{cap}}f)(\xi)=\sqrt{2w(\xi)}\langle f,h_\xi\rangle\), and \(R_T\) its replacement \(h_\xi\mapsto T_j(\xi)\) on each covered leaf. Then

\[
R_T^*R_T=K_{T,o},\qquad R_{\mathrm{cap}}^*R_{\mathrm{cap}}=K_{\mathrm{cap},o}.
\]

From SI10's exact reflected integrated upper caps \(M=2\sum_Ih_I|I|\), \(W=2\sum_I|I|\), one has

\[
\|R_{\mathrm{cap}}-R_T\|^2
\le 2B(M+\kappa W)\,2^{-48}=d_{24}^2.
\]

For \(\tau=1/1024\), the operator Young inequality (not an unsupported deletion of cross terms) gives

\[
\boxed{
K_{\mathrm{neg},o}
\preceq K_{\mathrm{cap},o}
\preceq
(1+\tau) K_{T,o}
+\eta I,
\qquad
\eta=(1+\tau^{-1})d_{24}^2
<3.02\times10^{-10}.
}
\]

This is an **upper bound on the entire original negative-frequency operator**, unlike SM05–SM08's lower subband packet absorptions. It is explicit in 107 rational moment matrices, 890 odd physical Taylor source functions, and one certified all-frequency remainder.

## 3. The exact, still-unproved finite gate

With \(s(x)=\sinh(x/2)\) and the original positive supported operator \(A_o\succeq \kappa I\), write

\[
B_o=A_o-\eta I \succeq (\kappa-\eta)I>0,
\quad
V=(s,\{u_{jk}\}_{j,k}),
\quad
D=\mathrm{diag}\big(2,\,(1+\tau) C\big),
\]
where \(C=\oplus_{j=1}^{107} C^{(j)}\succ0\).

The required full original odd positivity is **sufficiently implied**, but not proved, by

\[
\boxed{
D^{-1}-V^*B_o^{-1}V\succeq0,
}
\]
where every term represents the actual physical supported Gram/inverse and every pole/intercluster/cross-mode entry is included. Equivalently, \(B_o-VDV^*\succeq0\).

A legitimate conservative computation can replace \(B_o\) by the original SM05/06 positive minorant with the paid scalar \(\kappa-\eta\):

\[
B_o\succeq C_{16}-\eta I
=(\kappa-\eta)I+G\Gamma G^*.
\]

For the 891-source \(V\), the exact matrix identity

\[
V^*(C_{16}-\eta I)^{-1}V
=(\kappa-\eta)^{-1}V^*V
-(\kappa-\eta)^{-2}
Q^*(\Gamma^{-1}+G^*G/(\kappa-\eta))^{-1}Q
\]
shows precisely what Gram data are required. A rational variational dual witness \(Z\) can produce a **correct-sign Loewner upper** without inverting a huge physical matrix. However, **there is no current certified nonnegativity or strict eigenvalue margin** for the resulting 891-dimensional gate. The retained C16 reference may itself be insufficient.

Next: evaluate the actual supported 891-source coupling, run a low-cost necessary/sufficient pilot to detect C16 insufficiency, or transport the original RC higher Schur source with an explicit equivalence. Do not repeatedly extend scalar floors or selected lower signed packets as a substitute for this finite upper gate.

## 4. Reproduction and limits

\`python scripts/validate_rpb108_sm10_explicit_odd_cap_moments.py\`

A passing focused replay checks the original SI10 full-frequency sign envelope, the precise 107 block moment construction and rational LDL positivity, source dimension, and global infinite remainder. This does **not** verify original physical Gram positivity for the mixed 891-source Birman–Schwinger matrix. The complete odd form, even form, whole form, global original-zeta attachment, Lean completion and RH remain OPEN.

Independent audit of the inherited SI10 multiplier identification and continuum-to-operator inequalities remains necessary.