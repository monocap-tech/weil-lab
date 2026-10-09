# RPB108 NF20 — Exact source-norm obstruction and convergent high response with an unmeasured rate

Date: 2026-10-09 UTC / 2026-10-08 Pacific. Independent branch research/rpb108-phase-geometry-localization. Recovered independent NF19 head fb040acc4ceb06af9ad6bcb7c9d2db966ad39e38 and Coupled CC54 handoff head ea0e561a521267795b3aa87e0bcfd1624c072e5b before this turn. Global NF71 and Shadow PS3 paused. New terms entered in [NF20 terminology](../docs/TERMINOLOGY_RPB108_FORM_RESPONSE_TAIL_NF20.md) before their load-bearing use. This is not whole-aperture positivity at a=53/50, RH/F4, or Lean.

## 1. NEW actual native theorem: the scalar physical-source Gram bound fails even RELATIVE to low energy

Fix a=53/50, E=E112, F=F112, and the original complete unshifted Weil form Q. NF17 rigorously certifies A=Q|E>9e-39 I; NF16 rigorously certifies C=Q|F>=kappa I with kappa=207/1000. NF19 rigorously certifies for the first TWO exterior Legendre modes in each parity:

\[
302/1000<R_{2,e}<303/1000,\qquad
275/1000<R_{2,o}<276/1000.
\tag{NF20.1}
\]

Here A_p is the ACTUAL 56x56 retained signed Gram, B2,p its complete signed mixed Gram with the first TWO high modes of that parity, C2,p the actual 2x2 high signed Gram, and R2,p is the largest generalized Rayleigh ratio of G2,p=B2,p C2,p^{-1} B2,p* against A_p. NF19's certified brackets are taken as immutable established arithmetic evidence, not numerically estimated in this new script.

The NEW NF20 re-audit of original source interval SHA256s

* E112: `f69019a895cd675e304989cbb8209c90f033264e0aef589d4b1aa3be09cf4c81`;
* first exterior native: `da5fe692dc0d3a0820ccaf68217628776f08718661696dddad54012f4f3841ee`;
* second exterior native: `0a8f4ebd0778fa5c90209b3021d22791bdb0d9b73e0f19df608e04ed9ba2bcad`

uses ONLY their original outward signed intervals to establish:

\[
\begin{array}{lll}
Q(e_{112},e_{112})>69/20,&Q(e_{114},e_{114})>7/2,
 & |Q(e_{112},e_{114})|<13/20,\\
Q(e_{113},e_{113})>339/100,&Q(e_{115},e_{115})>351/100,
 & |Q(e_{113},e_{115})|<1/2.
\end{array}
\tag{NF20.2}
\]

By the exact 2x2 Gershgorin/diagonal-dominance bound,

\[
\boxed{C_{2,e}>(14/5)I,\qquad C_{2,o}>(289/100)I.}
\tag{NF20.3}
\]

Let \(\widetilde P_{2,p}=B_{2,p}B_{2,p}^*\), the physical-orthonormal two-mode mixed-source Gram on the original E_p. Because C2,p>=c_p I, the forms satisfy \(\widetilde P_{2,p}\ge c_p G_{2,p}\). Hence the strict ORIGINAL arithmetic generalized bounds follow:

\[
\boxed{\sup_{x\ne0}
 \frac{\widetilde P_{2,e}(x,x)}{\kappa A_e(x,x)}
 >\frac{(14/5)(302/1000)}{207/1000}
 =\frac{4228}{1035}>4,}
\tag{NF20.4e}
\]

\[
\boxed{\sup_{x\ne0}
 \frac{\widetilde P_{2,o}(x,x)}{\kappa A_o(x,x)}
 >\frac{(289/100)(275/1000)}{207/1000}
 =\frac{3179}{828}>\frac{19}{5}.}
\tag{NF20.4o}
\]

The [NF20 exact rational auditor](../scripts/certify_native_source_gram_obstruction_nf20_106.py) authenticates all three complete source archives, rechecks (NF20.2), derives the strict C2 floors and outputs these actual native inequality certificates. The local exact Fraction evaluation PASSED. The script does not recompute NF19's expensive four 58x58 Bareiss tests; those are a separately published certified dependency.

**Interpretation:** The standard inequality using ONLY the global physical high floor,
\(G_{\mathrm{full}}(x)\le \|s_x\|_2^2/\kappa\),
is a VALID upper bound when the physical source representative s_x exists. But in some genuine E112 directions its right-hand side exceeds 4x the WHOLE old A-energy even/3.8x odd, merely from the first two high source coordinates. Thus the sufficient ALL-direction condition \(\|s_x\|_2^2<\kappa A(x)\) is IMPOSSIBLE for the original native form. This does **not** imply the actual inverse response exceeds A: the separately certified true FIRST-TWO inverse reaction is only <0.303 A even/<0.276 A odd! The loss is entirely from discarding source-aligned high inverse geometry, not a sign of an off-critical zero.

## 2. The finite polynomial source REPRESENTATIVES genuinely exist

The fixed-cap original Weil decomposition is \(Q=E_{\log}+\langle R_a\cdot,\cdot\rangle_{L^2}\), where the physical remainder R_a is bounded (CC33/CC37, target a=53/50) and the canonical E_log multiplier has logarithmic growth. This does NOT yield a bounded physical L2 operator on the entire canonical form domain. But each normalized physical Legendre function e_j, zero extended outside [-a,a], is piecewise polynomial of bounded variation.

Integration by parts on [-a,a] gives, for \(|\xi|\ge1\),

\[
|\widehat e_j(\xi)|\le
\frac{|e_j(a)|+|e_j(-a)|+\int_{-a}^a |e'_j(x)|\,dx}
     {2\pi|\xi|}.
\]

Therefore \(m(\xi)\widehat e_j(\xi)\in L^2(\mathbb R)\) for every \(m(\xi)=O(\log(e+|\xi|))\), because \(\int_1^\infty\log^2(e+\xi)\xi^{-2}d\xi<\infty\). The physical bounded remainder acts in L2. Thus every member of the FINITE E112 span (and each finitely many exterior Legendre modes) belongs to the physical L2 operator domain of the original native form. Its Q(x,.) action on the canonical supported domain has a legitimate physical L2 representative \(s_x\).

This resolves *source existence for these finite polynomial modes only*. It neither claims nor contradicts a bounded original native operator on ALL physical L2 or the earlier obstruction to a bounded universal L2 source reconstruction. In particular, (NF20.4) is a genuine obstruction to the scalar source-Gram certificate, not merely a conditional concern about source existence.

## 3. Galerkin tail convergence — valid but not an effective sign estimate

Let F=F112 intersect the original canonical supported logarithmic form domain, with \(C=Q|F\ge\kappa\|\cdot\|_2^2\). Since \(Q=E_{\log}+R_a\) with physical bounded R_a, positivity of C implies equivalence of its C-form norm with the canonical log norm on F:

\[
\|y\|_{\mathcal D}^2\le (1+\|R_a\|/\kappa)\,C(y,y),\quad
 C(y,y)\le(1+\|R_a\|)\|y\|_{\mathcal D}^2.
\tag{NF20.5}
\]

Supported polynomials are dense in that log carrier: first contract support slightly inward and smooth by convolution, then approximate smooth functions in C1 by polynomials; for zero-extended C1 functions the \(\log\)-weighted Fourier norm is controlled by their C1 error because their Fourier transforms decay at least 1/|xi|. The physical E112 projection is continuous in the canonical log norm, so subtracting that finite projection makes the high Legendre polynomial tail dense in F. This uses the standing carrier/density work as an input and proves the specific Legendre Galerkin consequence, rather than restarting the old endpoint-density investigation.

For x in E112 the actual form source is continuous in the C metric, hence has a unique genuine C-form Riesz response W x in F. Let H_m,p be the first m exterior Legendre modes of the corresponding parity and Y_m x the C-orthogonal projection of Wx onto H_m,p. Define

\[
G_m(x,z)=C(Y_mx,Y_mz),\quad
G_\infty(x,z)=C(Wx,Wz),\quad
T_m=G_\infty-G_m.
\]

Then

\[
\boxed{0\preceq T_{m+1}\preceq T_m,\quad
 T_m(x,x)=\|Wx-Y_mx\|_C^2,\quad
 \|A_p^{-1/2}T_mA_p^{-1/2}\|_{\mathrm{op}}\longrightarrow0.}
\tag{NF20.6}
\]

The first identities follow from C-orthogonal Pythagoras and nested trial spaces; the final convergence follows from the proved high Legendre density and finite low dimension. This establishes a genuine uniform finite-cap Galerkin LIMIT, but contains **no quantitative rate, computable m or old-gap-independent frame bound**. It does not promote NF19's m=2 positive corrected gates to a positive infinite gate.

## 4. Precise constructive residual-source certificate for the next pass

For finite m define the original form-dual residual on all y in F by
\(r_{m,x}(y)=Q(x-Y_mx,y)\), which annihilates H_m. Because both x and Y_mx are FINITE polynomial modes, its physical source representative is well-defined:
\[
\sigma_m(x)=P_F\,s_{x-Y_mx},\qquad
r_{m,x}(y)=\langle\sigma_m(x),y\rangle_2.
\]
The genuine inverse residual equals the full C-dual norm squared, and is bounded by the ORIGINAL high coercivity:

\[
\boxed{T_m(x,x)=\|r_{m,x}\|_{C^*}^2
\le\frac{1000}{207}\|\sigma_m(x)\|_2^2.}
\tag{NF20.7}
\]

This yields a concrete sufficient source-aligned finite-cap certificate: enclose the full 112-by-112 physical residual Gram
\(P_m(x,z)=\langle\sigma_m(x),\sigma_m(z)\rangle_2\)
with all original Fourier-log/prime/pole and source errors, and show

\[
\boxed{P_m<\kappa(A-G_m)}
\tag{NF20.8}
\]

as a strictly positive signed matrix inequality. If this holds, A-G_full>0 and the ORIGINAL whole-aperture sign at a=53/50 follows. For m=2, NF19 gives strict margins
\(A_e-G_{2,e}>697/1000 A_e\) and
\(A_o-G_{2,o}>724/1000 A_o\);
a sufficient, simpler target is
\(P_{2,e}<\kappa(697/1000-\theta)A_e\) and
\(P_{2,o}<\kappa(724/1000-\theta)A_o\), for some theta>0 and all errors paid.

**This is a stopping criterion, NOT a completed estimate.** The physical residual Gram P_m has not been computed. Nor is convergence of its coarse upper \(\kappa^{-1}P_m\) guaranteed by Galerkin convergence: the physical source norm can behave differently from the C-form dual norm due to the logarithmic unbounded operator. If (NF20.8) fails, it is an inconclusive SUFFICIENT estimator, not actual original negativity. The source-aligned C-dual residual remains the more fundamental target.

## 5. Exact sign controls and their scope

[The exact rational NF20 control validator](../scripts/validate_native_hidden_tail_controls_nf20.py) tests six abstract high-mode completions, two parity response brackets, and a complete physical positive-level shift. In each parity the SAME measured first-two response lies strictly inside NF19's actual brackets, every high diagonal stays >kappa, and a third unmeasured high mode yields respectively a positive, exactly zero or negative full corrected sign. For the complete physical shift control, the original 2x2 positive matrix with off-diagonal 1-mu, mu=10^-40, acquires a zero eigenvalue only after mu is subtracted from BOTH physical diagonals. All exact rational assertions pass.

Stronger abstract completion lemma using the **actual full E112, B2 and C2 finite data**: because A>0 and \(R_2<1\), set \(U=A^{-1/2}B_2 C_2^{-1}B_2^*A^{-1/2}\) and choose a unit eigenvector u with eigenvalue R2. Append a new high physical basis direction with diagonal kappa, C-cross terms zero and mixed column \(b_3=\sqrt{\kappa\alpha}A^{1/2}u\). This preserves every measured original E112 and first-two high matrix entry and C>=kappa I, while its normalized low Schur is \(I-U-\alpha uu^*\). Choosing respectively \(\alpha=(1-R_2)/2\), \(1-R_2\), and \(2(1-R_2)\) produces positive, null and negative full signs. Thus the FINITE observed source data plus physical high positivity DO NOT LOGICALLY DETERMINE the unmeasured inverse response. These are ABSTRACT extensions, NOT full Weil explicit-formula realizations; they do NOT prove that the complete original Weil identities fail to provide the needed arithmetic correlation.

## 6. NF20 decision, next load-bearing work

**Certified new actual arithmetic:** the first-two original high native C2 floors and finite collective response establish that the naive global-physical-\(1/\kappa\) source Gram estimate exceeds the available whole retained energy by >4 even and >3.8 odd. This rules out the crude energy-relative physical-source scheme, not the actual positive-cap conclusion.

**Certified structural analytic result:** complete original high Galerkin reactions converge uniformly on the finite retained carrier in A-relative form norm; no effective rate is derived. The finite polynomial physical source domain is sound, so the next output can genuinely construct a 112-by-112 SOURCE residual Gram rather than speculate about its existence.

**NF21 priority:** compute the actual physical residual source Gram after the first two high modes, \(P_2=(\langle\sigma_2(e_i),\sigma_2(e_j)\rangle)\), from the original unshifted Weil Fourier multiplier, all prime shifts and signed poles, with an independent error ledger. Test the matrix inequality P2<kappa(A-G2). If it fails, quantify whether the C-dual residual (rather than the scalar 1/kappa loss) has better source-aligned cancellation. Do not extend a finite-mode sequence without a certified tail rate, or merge original Q with CC52's separately constrained pole-free H/Fplus carrier.

**Standing:** Whole-domain original Weil positivity internally certified through a=21/20 (CC18), not through a=53/50. At 53/50 the entire finite E112 sign, infinite positive F112 diagonal and first-two full original exterior corrected gates are certified, but complete F112 source response and whole original Schur sign remain open. RH/F4, all-aperture nonstalling, old-gap-independent collective frame and Lean closure unproved.
