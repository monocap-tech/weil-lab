# SM51 — Original direct signed multiplier on the actual e₂ Fourier core

**October 18–19, 2026 · W-ODD-NEG active · stacks on SM50/50A draft PR #232.**

## Prerequisite status and exact objective

Final SM50A PR-head Actions [39198594893](https://github.com/monocap-tech/weil-lab/actions/runs/39198594893) and SM50 PR-head Actions 39198594878 both **SUCCESS**. SM50A certified the full original 973-leaf, 3,892-subcell negative upper on physical odd supported source e₂:
- Original full negative upper sharpened from 0.859214278052 to 0.578168474932;
- True original positive [0,4096] one-sided lower with all 25-source Loewner error 0.095123987434;
- True original physical \(\sinh(x/2)\) pole correction upper 0.000126906031;
- **signed source scalar lower −0.483171393529, inconclusive** (a negative lower is not an actual negative witness).

SM51 confronts the **true original signed multiplier \(m(\xi)\)** without throwing away all nonnegative original contributions near the troublesome sine source frequency \(1845/128\). The exact identity \(\max(\kappa,m)-(\kappa-m)_+=m\) motivates integrating \(m\) *directly* on a bounded physical source-dominant core. This does not assert a global operator positivity decomposition.

## All frequencies accounted for without double counting

Work on the actual original selected physically supported odd sine \(g_2(x)=\mathbf1_{[-B,B]}\sin(2\pi (1845/128)x)\), \(B=11/10\), with actual Fourier sine transform \(T_2(\xi)\). The original signed odd source Rayleigh form is
\[
\langle g_2,W_og_2\rangle =
2\int_0^\infty m(\xi)\,T_2(\xi)^2\,d\xi
-2|\langle g_2,\sinh(x/2)\rangle|^2.
\]
Under inherited original SI06/SM42 physical Fourier and closed-domain identities, this is the target, including its true original exceptional pole.

Choose the rational source-centered core \(C=[13,16]\), and partition it into exactly **768** real closed subcells of width \(1/256\); cell endpoints and true original SI10/SM39 dyadic subcell endpoints align at the integer boundaries. On every core cell \(I=[a,b]\), use original SM39 rational archimedean monotone lower \(\operatorname{arch}_{lo}(a)\) and **two independent original SI06 all-seven-prime real-frequency bounds**, taking their maximum:

\[
m_I^- = \operatorname{arch}_{lo}(a)+
\max\left(
 \operatorname{prime}_{lo}((a+b)/2)-69(b-a)/2,\quad
 \min(\operatorname{prime}_{lo}(a),\operatorname{prime}_{lo}(b))
 -D_2(b-a)^2/8
\right)
\le m(\xi)\quad(\xi\in I).
\]
The original SM40 \(D_2\) is a rigorous global second derivative bound for the complete seven-prime signed trigonometric sum, including prime powers. No interpolated unsampled sign is accepted.

For the actual source2 Fourier transform on each real cell, use exact original SM42 \(F_0,F_1,F_2\) analytic source intervals and the true spatial third-moment bound to enclose the actual affine Taylor approximation \(\hat T=v+d(\xi-\mathrm{mid})\). Compute:
- **Upper** mean-square bound \(\bar Q^+_I=\min(s_I^2,v^2+d^2r^2/3+2R\sqrt{v^2+d^2r^2/3}+R^2)\), with \(R=e_0+e_1r+K_Ir^2/2\), using original SM43 true whole-cell sinc source supremum \(s_I\) and outward exact rational sqrt;
- **Lower** mean-square bound \(\bar Q^-_I=[\max(0,|v|-e_0-K_Ir^2/6)]^2\), by Jensen's inequality and exact cancellation of the linear derivative over a symmetric real cell.

The lower signed contribution is thus
\[
2|I|\begin{cases}
m_I^-\bar Q_I^-,&m_I^-\ge0,\\
m_I^-\bar Q_I^+,&m_I^-<0.
\end{cases}
\]
It is a true lower for the original signed \(2\int_I m(\xi)T_2(\xi)^2d\xi\), not a partial-positive LOWER vs partial-negative LOWER comparison.

Outside \([13,16]\), negative-frequency support is bounded **from above** by the original complete exhaustive SI10 973-leaf / SM39 3,892-real-subcell whole-frequency cap. No negative contribution is dropped. Recalculate each disjoint exterior subcell \(J\) with its inherited real signed upper \(w_J=\min(h_{\mathrm{parent}}+\kappa,\mathrm{ceil}_{10^{-6}}(\kappa-m_J^-)_{+})\), then the actual original supported physical source2 affine-square integral upper. Thus \(N_{\mathrm{outside}}\ge2\int_{\mathbb R_{+}\setminus C}(\kappa-m)_+T_2^2d\xi\). The original SI06 certified sign-safe high-frequency region \(\xi\ge896\) has zero negative multiplier.

Add **only exterior-disjoint** original SM12's 17 rigorously signed-positive source windows and the 32 genuine selected SM49 adaptive source-positive windows, requiring each added positive Jensen band lie *entirely outside* \(C\). Discard any intersecting \(C\) to avoid double counting. All selected original SM12/SM49 positive windows are pairwise disjoint. Because \(m(\xi)\ge\delta>0\) on such a band and \((\kappa-m)_+=0\), their direct signed contributions are bounded below by genuine source2 Fourier Jensen mean squares.

Finally subtract the exact true original SM42 physical pole upper once:
\[
\boxed{
\langle g_2,W_og_2\rangle
\ge
L_{\mathrm{signed},[13,16]}
-N_{\mathrm{original},\mathrm{outside}}
+P_{\mathrm{exterior,disjoint}}
-2|\langle g_2,\sinh(x/2)\rangle|_{\mathrm{upper}}^2.
}
\]

## Acceptance and scope

The exact-rational validator fails closed unless 768 original signed core subcells are exhaustively accounted for, 973 original parent negative leaves are all partitioned into exactly 3,892 subcells with every one inside or outside core (none crossing), all 49 true signed-positive old/new windows are independently either outside/disjoint or discarded, true original sinh pole is paid, and **strict positive source2 sign is claimed only if the exact lower is positive**.

If the signed lower remains nonpositive, it is still **not evidence that the actual original signed form is negative**; improve original signed-m interpolation, source analytic Fourier localization or core selection. **Even if one source becomes certified positive, full original 25×25 coupled odd signed PSD/inertia, 470 original sources, complete positive Astar inverse/strong residual, even E1–E4, signed Weil positivity, CC27 and RH remain OPEN.** Independent original Fourier/form-domain audit and peer review remain separate from passing Actions.

The scoped direct signed calculation is not a substitute for the original complete-operator odd O1/O2 acceptance gate.
