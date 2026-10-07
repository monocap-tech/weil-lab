# RPB108: the rough flux leading term cannot be cancelled by bounded source corrections

Date: 2026-10-06 (America/Los_Angeles). Live source 29dddc23d7f562668cff7167b9bdd264116c6c83.
Definitions: [leading rough flux registry](../docs/TERMINOLOGY_RPB108_LEADING_ROUGH_FLUX.md).
Analytic endpoint-route audit. Actual whole-domain positivity through 19/20 is reused.

## New exact comparison

For a fixed physical h with finite logarithmic energy but h not in global H1,
\[
\frac{D_{\rm mass}(t;h)}{D_w(t;h)}\longrightarrow0,\qquad
\frac{t^2}{D_w(t;h)}\longrightarrow0.
\tag{1}
\]
Therefore any bounded real multiplier correction b satisfies D_b=o(D_w). In the actual eigenmode flux identity, the finite prime contribution, the bounded archimedean correction, the eigenvalue mass term and the pole are all lower order:
\[
\boxed{F_h^{\rm ext}(t)=-D_w(t;h)(1+o(1)).}
\tag{2}
\]
This sharpens divergence of F/t^2 to a relative asymptotic with the actual combined residual. It applies both to hypothetical actual zero-null vectors and to the established rough positive native eigenmode control. It does not show that such an actual zero-null vector exists.

## Proof without a boundary trace

For h not in H1, Fatou on bounded frequency cutoffs, then expanding the cutoff, gives D_w(t)/t^2->infinity. The cosine quotient tends pointwise to 2 pi^2 xi^2, and its integral against w|hhat|^2 is infinite. All defects are finite because h has logarithmic energy.

Fix L>1. Choose N so w(xi)>=L for |xi|>=N. On the low band,
1-cos(2 pi xi t)<=2 pi^2 N^2 t^2.
With C_N=2 pi^2 N^2 ||h||_2^2,
\[
0\le D_{\rm mass}(t)\le C_Nt^2+D_w(t)/L.
\tag{3}
\]
Divide by D_w, first let t->0 at fixed N,L, then let L->infinity. This proves (1). In particular no uniform rate in h is being inferred from Fatou.

If ||b||_infinity<=B, positivity of the cosine defect gives
\[
|D_b|\le B D_{\rm mass}=o(D_w).
\tag{4}
\]
At the fixed actual aperture m_a=w+b_a, with ||b_a||_infinity finite by the recovered logarithmic envelope and finite-prime bound. The genuine flux of an eigenmode satisfying q_h=mu h in the interior is
\[
F_h^{\rm ext}=-D_w-D_{b_a}+\mu D_{\rm mass}
 +(\cosh(t/2)-1)P_0(h).
\tag{5}
\]
The pole is O(t^2), so (1), (4) give (2), with its fixed negative sign.

More explicitly, set H_t=D_w(t)/t^2. On 0<t<=1, |cosh(t/2)-1|<=t^2/4. For |mu|<=M the comparison functional obeys
\[
\left|\frac{\Phi_\mu(h;t)}{-D_w(t;h)}-1\right|
\le (B_a+M)\left(\frac1L+\frac{C_N}{H_t}\right)
 +\frac{|P_0(h)|}{4H_t}.
\tag{6}
\]
Taking the limits in the same order proves uniformity over bounded mu for this **fixed h**. Only its actual eigenvalue makes Phi_mu the genuine exterior flux. Changing mu does not provide a new interior equation, zero-null vector, or actual packet.

## What this rules out

Subtracting the interior mass correction from the rough positive eigenmode control changes its flux by mu D_mass, which is o(D_w). It cannot cancel the leading rough logarithmic term. Likewise any additive O(t^2) bound on the pole, or a bounded fixed-window prime multiplier estimate, cannot reverse that leading sign or yield a quadratic lower flux bound for a rough mode.

Failed implication: boundedness of all finite prime/pole/mass corrections plus the logarithmic envelope -> a quadratic lower bound for the genuine exterior flux. The existing actual positive eigenmode supplies a genuine-residual control, and (2) identifies the exact dominating term. This is not a counterexample to actual zero-eigenvalue exclusion: that control has mu>0, and the interior zero equation might constrain which physical vectors are admissible.

Thus a successful endpoint proof must use the zero-normalized interior equation to exclude the rough mode itself or constrain its spectral tail. Rearranging the bounded terms of the already derived flux formula cannot supply a cancellation for an existing rough h. This does not say bounded arithmetic terms are irrelevant to locating an eigenvalue: they can change the kernel and the eigenvectors. The comparison holds after fixing h.

The smallest remaining theorem on this route is unchanged: at every hypothetical nonnegative actual null window, the full-kernel flux trace has a quadratic lower bound along one sequence. The derivative-chain ceiling supplies a rough mode if K is nonzero, whose flux has (2), so that theorem would exclude contact. No new argument proving that arithmetic lower bound is obtained here.

## Finite-kernel trace and limitations

For a physical orthonormal basis of a nonzero hypothetical K, write D_w^K=sum D_w(h_j). At least one basis vector is rough, so D_w^K/t^2->infinity. Apply the cutoff inequality (3) to the sum (its low-band constant uses sum ||h_j||^2=dim K). The same proof yields
\[
\sum_j F_{h_j}^{\rm ext}(t)=-D_w^K(t)(1+o(1)).
\tag{7}
\]
This relative trace identity is basis independent. It uses the entire kernel covariance, not a rank-one averaged inverse-boundary observation. Regular basis vectors do not spoil the estimate; their mass and pole defects are still dominated by the diverging full trace. This proof does not assume every basis vector is rough.

No moving-eigenspace or aperture-uniform asymptotic is claimed. In particular one cannot pass this limit through a family h_mu as mu->0 without an independent uniform tail theorem. The exact zero normalization remains indispensable to the unproved admissibility/endpoint argument.

## F4 and transport custody

Category: endpoint exclusion. Physical h stays fixed; translated h is only a test. No dilation, enlarged mixed cancellation or retained-packet substitution occurs. Historical named attachment gates, including the optional normalization-compatible repair test, are independent. The result records a sharper obstruction for a proposed flux cancellation route, not another conditional realization layer.

Pinned source blobs and repeat rational inequality controls are recorded in notes/data/RPB108_LEADING_ROUGH_FLUX_20261006.json. Controls verify cutoff budgets, bounded-correction signs and the relative remainder estimate; they do not prove analytic Fatou limits, compute an actual eigenmode or certify actual arithmetic estimates. No Lean build, Lean-file change, new axiom audit or CI result is claimed. Historical wording/certificates and the independent aperture lane remain intact. F4 and FULL TRANSPORT CLOSED remain open.
