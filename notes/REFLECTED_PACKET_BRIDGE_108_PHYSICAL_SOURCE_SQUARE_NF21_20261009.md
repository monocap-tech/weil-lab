# RPB108 NF21 — First genuine physical source-square Gram and exact compensated residual identity

Date 2026-10-09 UTC / 2026-10-08 Pacific. Independent branch research/rpb108-phase-geometry-localization. Live recovered independent parent NF20 `44b22630d0211b5204284407fe16e45a24151843`; Coupled mathematical head CC56 `39376d680a7bf1359fa41bf14c8bfda11bbf2fb1` read-only. Definitions registered beforehand in [NF21 terminology](../docs/TERMINOLOGY_RPB108_SOURCE_SQUARE_GRAM_NF21.md). Global NF71 and Shadow PS3 remain paused; no history is altered.

**New original arithmetic result:** The first exact-rational physical **SOURCE-SQUARE** Gram sector has been computed, not merely the native original Weil form Q. At aperture a=53/50, on the two normalized physical Legendre modes e0 (even) and e1 (odd), the COMPLETE six-prime translation source plus BOTH signed Hermitian pole-source terms have an exact interval-enclosed Gram. The source includes prime-prime, pole-pole, and their SIGNED prime/pole cross-correlation. The archimedean source-square and archimedean/prime/pole cross terms are deliberately NOT included. This does not evaluate the complete 58-by-58 physical residual source Gram P2 or certify whole-aperture positivity.

**New algebraic reduction:** The actual full residual physical source Gram P2 needed for the original fixed-aperture Schur test has an exact expression in terms of a finite 58-by-58 complete physical source-square Gram D for EACH parity, and the already certified native 56+2 finite matrix. The reduction has been checked by a separate exact rational source-model identity. It identifies the cancellation-sensitive finite integration one must perform, without confusing the positive native Q form with a source-square norm.

## 1. Actual prime-plus-pole source-square intervals at the first two modes

Let P={2,3,4,5,7,8}, c_n=Lambda(n)/sqrt(n), ell_n=log n and p tilde the zero extension off [-a,a]. The ORIGINAL physical source terms are

\[
(L_{\mathrm{prime}}p)(x)=-\sum_{n\in P}c_n
 [\widetilde p(x+\ell_n)+\widetilde p(x-\ell_n)],
\]

\[
(L_{\mathrm{pole}}p)(x)=e^{x/2}m_-(p)+e^{-x/2}m_+(p),
\quad m_\pm(p)=\int_{-a}^a e^{\pm y/2}p(y)\,dy.
\]

The test vectors are e0=1/sqrt(2a) and e1=sqrt(3/(2a)) x/a. Reflection makes the full parity-cross source-square term vanish identically, not merely numerically.

For the EVEN pole source define
\[
M_0=\frac{4\sinh(a/2)}{\sqrt{2a}},\qquad
L_{\rm pole}e_0=2M_0\cosh(x/2).
\]

For the ODD pole source define
\[
M_1=\sqrt{\frac3{2a}}\left(4\cosh(a/2)-\frac8a\sinh(a/2)\right),
\qquad L_{\rm pole}e_1=-2M_1\sinh(x/2).
\]

The exact physical pole-source squares therefore include
\[
\|L_{\rm pole}e_0\|_2^2=4M_0^2(\sinh a+a),\qquad
\|L_{\rm pole}e_1\|_2^2=4M_1^2(\sinh a-a).
\]

Every one of the 12 oriented active prime shifts is integrated on its complete native source support panel. For a shift t=+/-ell_n, the panel is exactly [-a,a] intersect [-a-t,a-t]; the integral of two prime-source shifted polynomials is evaluated using exact antiderivatives on their intersected panels. There are **82 nonempty ordered overlaps** among the 144 possible oriented-shift pairs. The prime–pole cross terms are integrated through exact hyperbolic antiderivatives on the same panels. No floating-point quadrature supplies a source certificate.

Resulting strict outward 1e-12 enclosures (midpoint displays are not proof values):

| Original L2 SOURCE sector | Even e0 | Odd e1 |
| --- | ---: | ---: |
| \(\|L_{\rm prime}e_j\|^2\) | 4.249293916309... | 2.322359221687... |
| \(\|L_{\rm pole}e_j\|^2\) | 21.678748363955... | 0.176302908536... |
| \(2\langle L_{\rm prime}e_j,L_{\rm pole}e_j\rangle\) | -18.683476299190... | -1.217839085235... |
| **\(\|(L_{\rm prime}+L_{\rm pole})e_j\|^2\)** | **7.244565981074...** | **1.280823044988...** |

The exact [source-sector producer](../scripts/certify_native_source_square_prime_pole_nf21_106.py) uses Fraction arithmetic, directed 10^-44 interval grid, 125-term rational atanh logarithms and 145-term rational Taylor exponentials. Its interval source JSON has SHA256 `9ea91c5d0bf9bac4cf32d8a2bb3644c6fb7d9dd004ad3ebc5f5aac0ee1b01648`; exact producer script SHA256 `04da3f5b79c0053c63f46e523a91cf3d44e5e3d95eff326ba9a93fdd98168ece`. Both signed-pole FIRST MOMENTS were separately verified to intersect the corresponding original signed NF17 native Q pole intervals, using E112 source SHA256 `f69019a895cd675e304989cbb8209c90f033264e0aef589d4b1aa3be09cf4c81`. Eighteen new exact rational assertions passed; independent 13-cell SciPy numerical source integration agrees within double-precision tolerance and is NOT used as proof.

The cross terms are substantial, especially in the even sector: the sum of two separate source-square energies would be about25.93, whereas their actual combined physical source-square is about7.24. Thus the actual covariance must be retained when incorporating the archimedean source. Neither the pole-only nor prime-only SOURCE square is the corresponding original Weil native form entry Q(e_j,e_j), and the source's square is not automatically coercivity or a sign on the whole operator.

## 2. Exact finite algebra for the missing physical residual Gram P2

Work separately in either parity. The original retained low block E_p has dimension56; H2,p is the first TWO physical exterior modes of that parity. NF19 already certified the complete signed 58-by-58 native block

\[
\begin{pmatrix} A&B\\B^*&C_2\end{pmatrix},
\qquad C_2>0,\qquad
S_2=A-BC_2^{-1}B^*>0.
\]

By CC56's original operator-domain theorem, each finite supported Legendre polynomial in E_p⊕H2,p has a genuine physical L2 Weil source. Set
\[
T=\binom{I_{56}}{-C_2^{-1}B^*},\qquad
p_x=T x,\qquad
D_{ij}=\langle L_a g_i,L_a g_j\rangle_{L^2([-a,a])}
\]
for the complete 58 genuine source functions L_a g_i.

Because the first56 rows of the physical source-to-native pairing are [A B], the low physical projection coefficients of L_a T x are exactly S2 x. Therefore, by orthogonal physical L2 Pythagoras, the TRUE residual physical source Gram on E_p is

\[
\boxed{P_2=T^*DT-S_2^*S_2=T^*DT-S_2^2.}
\tag{NF21.1}
\]

Moreover Q(p_x,h)=0 for every h in H2,p by construction. Since Q(p_x,h)=<L_a p_x,h> physically, the physical source L_a p_x has NO component along the measured exterior modes either. Hence
\[
\boxed{
\sigma_2(x)=P_{F112}L_a(Tx)
=P_{(E_p\oplus H2,p)^\perp}L_a(Tx)
}
\tag{NF21.2}
\]
within its parity. This equality is a genuine original source-domain identity, NOT the false claim that p_x itself is physically orthogonal to H2,p.

The exact [source-square algebra validator](../scripts/validate_native_source_square_gram_identity_nf21.py) independently checks this identity, the exact annihilation of the two measured source coordinates, and positive semidefiniteness of P2 in a rational four-dimensional source model with three extra physical coordinates. It proves the algebra of (NF21.1), not the numerical value of actual 58-dimensional Weil D.

NF20's true complete source-residual criterion is now constructive with a FINITE D:
\[
\boxed{P_2\prec(207/1000)S_2
\quad\Longrightarrow\quad
A-G_{\rm full}>0.}
\tag{NF21.3}
\]

That would certify whole original positivity at this fixed aperture. **Neither D nor P2 has yet been calculated**, so the implication is a certified conditional reduction, not an achieved sign.

## 3. Numerical stability and error ledger

The bare identity P2=T*DT-S2² suffers potentially catastrophic cancellation near retained eigenvalues around 10^-35: two large individual physical-source-square terms may subtract to an extremely small source residual. The actual exact low2 prime/pole calculation already demonstrates substantial source-sector cancellation on simple modes.

For a scalable certificate the more stable representation is to construct, on the ORIGINAL physical interval, the compensated source vectors
\[
r_i(x)=(L_a T e_i)(x)-\sum_{k\in E_p}(S_2)_{ki}\,e_k(x),
\quad
P_{2,ij}=\int_{-a}^a r_i(x)r_j(x)\,dx.
\tag{NF21.4}
\]

CC56 supplies the exact original endpoint-log source action: its archimedean source is an inside polynomial-difference integral with kernel j(|x-y|), plus the two explicit boundary J(a±x) terms and the complete local digamma constant. The singular 1/(2|x-y|) portion is removable in the polynomial difference, while the endpoint logarithms must be enclosed and squared/integrated with their true correlations. The six-prime translation panels and both pole-source terms are finite and their polynomial/exponential cross integrals can be enclosed. No unbounded logarithmic multiplier may be substituted by a bounded universal physical L2 model.

Computing (NF21.4) requires the complete original **archimedean-source contributions and their cross products**, with rigorous quadrature/integration and retained near-critical conditioning. This is the substantive outstanding computation. The pole+prime sector on e0/e1 is an independently certified implementation preflight, not the complete 58-by-58 D.

## 4. NF22 stopping rule and Coupled interface

**NF22 should compute the missing ORIGINAL archimedean physical source for e0 and e1**, checking that the complete source \(\langle L e_i,L e_j\rangle\) agrees with the direct formula (NF21.1) and the NF17 native pairings. Then move to the compensated residual norm of explicit NF18 rational near-critical E112 witnesses, measuring a directional P2/S2 bound with error below the actual retained margins before attempting all 56+56 columns. Failure of the coarse physical P2 gate is inconclusive; direct C-form-dual source correlation may succeed.

CC56 concurrently proves genuine physical finite-polynomial source injectivity, but supplies no numerical source lower or source-tail upper. NF21 uses its operator-domain result and prepares the explicit SOURCE-SQUARE object needed for an UPPER reaction bound. Injectivity cannot replace the residual source Gram. Coupled's CC52 moment-zero H/Fplus carrier is different from unconstrained original Q with poles; no carrier transport is silently assumed.

**Standing:** Complete E112 native signed finite positivity and F112 positive high floor207/1000 remain; NF19's first-two high-mode corrected gate is positive with retained fraction >.697 even/>.724 odd. NF21 computes a true low2 prime/pole SOURCE-square sector and a finite exact P2 reduction, but not the complete original physical source or high inverse. Whole-domain a=53/50 remains OPEN; highest internally certified WHOLE aperture remains a=21/20. No RH/F4, all-cap non-stalling, full transport or Lean closure.

## Subsequent arch-source sector — NF22

[NF22 rigorously reconstructs and squares the original archimedean physical low2 source](REFLECTED_PACKET_BRIDGE_108_ARCH_SOURCE_LOW2_NF22_20261009.md) with exact endpoint logarithms and a degree320 rational regular kernel whose uniform source L2 remainder is <1e-19. Strict source-squared arch enclosures are 7.082144075590..7.082144075591 even, and 1.083143528165..1.083143528166 odd. Combining these with NF21's rigorous prime/pole source sectors still requires the arch-prime and arch-pole SOURCE CROSS terms; initial combined full source squares ~0.08366/~0.33814 are numerical diagnostics only, not certificates. The complete 58x58 source Gram D and residual P2 remain uncomputed. Concurrent CC59 uses the same 58 source functions for a conditional correlated high-floor response bound; no final Schur sign is claimed.
