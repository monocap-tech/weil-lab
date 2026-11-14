# NF506 — Independent full 242D a posteriori Schur contraction and exact support-liberation law

**2026-11-13 PT. Locally VERIFIED; dedicated GitHub focused verification pending.** Stacked on NF505 draft PR #534, branch `research/nf506-original-J8-independent-posterior-schur`. Original whole Weil/RH claims remain OPEN. This is not a new test-source or operator-domain theorem.

## Recover the NF505 completed original numerical result

The authentic NF505 dedicated run **43352403600** completed both jobs SUCCESS (native job 131646362039 and independent exact-source audit job 131649161950), although the historical staged PR text still says QUEUED. Its original source-native payload is artifact **14004781980**, raw JSON SHA256 **ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec**. The NF505 exact-source audit is artifact **14005655074**, raw JSON SHA256 **0fd77189a8b49106ca634bda33173e8adae91126144e33ba740e437f831b9a28**. Both retained artifacts expire 2027-02-11 UTC unless durably backed up (separate RC04).

The independently source-audited NF505 original 242D physical J8 two-collar verdict is **CERTIFIED_PHYSICAL_SUPPORT_NO_GO**, using original NF407/NF406 sources, selected NF401 D-frame, NF404 fixed gamma, genuine original NF494 H400/U400, and original J7/J8 source-certified energies. The native source proof interval is approximately
\[
1.5782989705548823\cdot10^{-22}\leq\mathcal R(S)
\leq1.6059616072170955\cdot10^{-22}.
\]
This excludes corrections supported **only** in the genuine terminal collars \(S=\{549/500<|x|<11/10\}\) under this fixed selected NF404 sufficient test. It does not exclude other physical supports, other projectors, admissible multipliers, or RH.

## NF506 new result: independent full 242D inverse contraction

The previous NF505 independent Fraction auditor verified original source ledger, 242² Gram symmetry, primal/dual equations, and source interval overlap, **but did not independently invert** the 242×242 numerical Gram. NF506 supplies a different inverse/contraction architecture: NumPy binary64 produces only a **candidate** \(x\approx G^{-1}b\) and \(B\approx G^{-1}\); all acceptance is then verified with exact integer arithmetic against the original NF505 **outward source intervals**, not a float tolerance test.

Set \(S_0=10^{70}\) and \(T_0=10^{35}\). Floor every original dyadic Gram midpoint to an integer divided by \(S_0\), and independently prove each original radius is \(<1/S_0\). Consequently every physical entry obeys \(|G_{ij}-M_{ij}/S_0|<2/S_0\). Independently quantize original exterior mixed-moment **intervals** to \(b_i\) with exactly checked coordinate uncertainties. Quantize the new binary64 candidate inverse/trial to denominator \(T_0\).

With \(\widehat B\) the quantized independently computed 242×242 candidate inverse, perform **every 242³ multiply-and-accumulate in integers** to verify
\[
\epsilon=\|I-G\widehat B\|_\infty<1,
\qquad
\|G^{-1}\|_\infty
\leq {\|\widehat B\|_\infty\over1-\epsilon}.
\]
This bound includes the entire input interval Gram uncertainty; it does not appeal to NF504's native inverse or a merely numerical spectral condition number.

For independent rational trial \(x\), use the exact quadratic identity
\[
b^\top G^{-1}b
=2b^\top x-x^\top Gx+
(b-Gx)^\top G^{-1}(b-Gx).
\]
The finite original exterior Gram is positive definite by independence of the original analytic 242 source generators restricted to the open central interval. Bound every input perturbation in the first two terms and bound the residual correction by \(242\|G^{-1}\|_\infty\|b-Gx\|_\infty^2\).

**Local verified result** from original source-artifact SHA-pinned inputs:

| Quantity | Rigorous bound / scale |
| --- | ---: |
| Inverse Neumann defect | \(\epsilon\leq5.19394422073\times10^{-6}<1\) |
| \(\|G^{-1}\|_\infty\) | \(\leq8.02269668194\times10^9\) |
| New trial residual \(\|b-Gx\|_\infty\) | \(\leq4.988450817\times10^{-25}\) |
| Independent full 242D projection power | \(b^\top G^{-1}b\leq7.435834306032652\times10^{-22}\) |
| Original source \(E_O\) lower | \(\geq9.014133276602936\times10^{-22}\) |
| **Independent physical saturated residual lower** | **\(\mathcal R(S)\geq1.5782989705702848\times10^{-22}\)** |
| Unchanged NF404 \(\gamma^2\) | \(5.1296807867614294\times10^{-26}\) |
| **Strict lower ratio \(\mathcal R(S)/\gamma^2\)** | **\(\geq3076.797633575\)** |

The full exact rational projection upper/lower and quantified Neumann/residual gates are written to the verifier output, not certified by their rounded table display. The new lower fits within the original full outward source interval. The signed physical no-go is now independently re-contracted with an entirely different numerical inverse solver and exact integer a posteriori acceptance.

**Boundary:** The original NF505 outward source integrals are *inputs*. Their independent reintegration remains unperformed; this NF506 independently validates the 242D solve/contraction given those authenticated source intervals. The physical \(L^2(S)\) optimization is still deliberately broader than the authentic Weil multiplier image or graph domain. No W-ODD-NEG, even-branch, full form positivity, or RH promotion.

## NF506 new structural theorem: exact support liberation

Let \(O\) contain an open interval, \(D\subset O\) be measurable, and \(O'=O\setminus D\) still contain an open interval. Let \(J(x)\) denote the original 242-generator column and define
\[
G_A=\int_AJJ^\top,\quad b_A=\int_AJW,\quad
\mathcal R(A)=\int_AW^2-b_A^\top G_A^{-1}b_A.
\]
Let \(a=G_O^{-1}b_O\), \(r=W-J^\top a\) and \(k_D=\int_DJr\). Then **exactly**
\[
\boxed{
\mathcal R(O)-\mathcal R(O')
=\int_Dr^2+k_D^\top G_{O'}^{-1}k_D.
}
\]
Proof: \(b_{O'}-G_{O'}a=-k_D\). Minimizing \(\|r-J^\top h\|_{L^2(O')}^2\) over \(h\) subtracts precisely \(k_D^\top G_{O'}^{-1}k_D\), while \(\|r\|^2_{O'}=\mathcal R(O)-\|r\|_D^2\).

Both terms are nonnegative, so enlarging admissible physical support always decreases the best residual, and **the reduction has an exact, computable first energy term and a nonnegative reoptimization correction**. The former is not generally the entire gain. Under sufficient continuity at a moving interior boundary, the leading first variation is the squared current exterior residual density; the cross-correlation correction is second order in the removed-strip width whenever \(G_{O'}^{-1}\) stays bounded. Thus genuinely new support can change the NF505 verdict; further optimization *strictly inside the fixed collars* cannot.

An independent 192-case exact Fraction regression covers 5/6/7-site physical models, deletion of one or two sites, and large and rational selected-space recenterings. These are algebra checks, **not new original Weil source data**.

## Reproduction and progression

Files in this PR:
- `scripts/local_replay/verify_nf506_independent_a_posteriori_schur.py`: authenticated original NF505 artifact inputs, independent 242D NumPy candidate solve, all-entries integer inverse residual, exact-rational physical lower/threshold gate.
- `scripts/local_replay/verify_nf506_support_expansion_exact.py`: 192 exact rational source-recentering/support-deletion controls.

Required original artifacts come from run 43352403600:
1. `nf504-original-J8-full-242D-support-saturated-exterior-source-native`, containing `nf504-original-J8-physical-support-saturated-exterior-source-native.json`.
2. `nf505-original-independent-242D-true-J8-saturated-Schur`, containing `nf505-original-J8-support-saturated-independent-exact.json`.

**Acceptance:** locally rerun both verifiers against the SHA-pinned artifact pair; then focused GitHub CI must succeed before source-independent NF506 repository promotion. Refuse to promote if the source input SHA changes, the integer Neumann bound reaches 1, or the strict independent support residual lower fails to exceed unchanged \(\gamma^2\).

**Next bold NF507:** build a source-certified interval profile of the original complete exterior residual \(r(x)\) and use the exact support-liberation identity to identify quantitative interior support enlargements that can lower \(\mathcal R\) toward \(\gamma^2\); separately determine whether any such physical support is realized by a genuine admissible Weil-source multiplier/graph-domain direction. If not, stop this selected sufficient architecture rather than recycle endpoint rays. RC02/RC04 artifact custody remains a parallel maintenance obligation; no main merge.
