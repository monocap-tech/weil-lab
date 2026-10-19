# SM49 — Source-adaptive original signed-positive Jensen rescue on actual SM48 nonpole witness

**October 18–19, 2026 · W-ODD-NEG active · stacked on SM48 draft PR #230.**

## Why a new positive method is necessary

The first substantive original 25-source SM48 test passed GitHub Actions 39191354830, proving the retained 17-band **positive lower reference** fails against a certified 15-band **negative lower suboperator**, with an exact non-pole source-coordinate \(e_2\) gap \(>17/1000\). This was a **reference insufficiency**, not negativity of the full original signed form: the actual positive multiplier has additional nonnegative mass everywhere outside the selected 17 bands.

SM49 makes that additional positive mass **source-adaptive** instead of performing more global source-window Fourier interpolation. The acceptance axis is the exact original SM48 source \(e_2\) and a complete original **25×25** all-cross Loewner lower. An improvement in one source direction is not a certificate on the whole negative operator.

## Original signed-positive real cell discovery without sampled multipliers

The existing SM12 \(\{[c_j-1/100,c_j+1/100]\}_{j=1}^{17}\) are known positive. Construct **only NEW** flank cells on either side, of width \(h=1/50\), \(12\) per side per \(c_j\). All chosen cells are nonoverlapping with the original 17 bands and with one another.

For each rational \([a,b]\), \(c=(a+b)/2\), compute the exact inherited original SI13 monotone archimedean lower \(\operatorname{arch}_{\rm lo}(a)\) and the original SI06 all-seven-prime rational interval at the midpoint. The original signed-prime derivative majorant \(69\) gives

\[
m(\xi)\ge m_{I,\rm lo}:=
\operatorname{arch}_{\rm lo}(a)
+\operatorname{prime}_{\rm lo}(c)
-\tfrac{69}{2}(b-a),\qquad \xi\in[a,b].
\]

Accept only if \(m_{I,\rm lo}>\kappa+1/5\) and set \(\delta_I=\operatorname{floor}_{10^{12}}(m_{I,\rm lo}-\kappa)>0\). Thus \(a_o(\xi)-\kappa=(m(\xi)-\kappa)_+\ge\delta_I\) *for every real frequency* in an accepted cell, regardless of root shapes elsewhere. This is not a numerical plot or sampled multiplier.

## Exact source-targeted selection and full 25-source proof

The real original SI10 physical \(e_2\) is among the 16 sine sources, with exact original cluster center \(c_{e_2}\). The midpoint original physical source-2 Fourier transform \(T_2(c)\) is enclosed by SM42/SM44's original SI06 rational \(F_0\) formula, never FFT. Ranking candidate cells uses the original **exact rational one-source** lower gain \(\gamma_I(v_2^2-2|v_2|e_2-e_2^2)\), with \(\gamma_I=2|I|\delta_I\) and \(e_2=r^{(0)}_2+K_{2,\mathrm{global}} (h/2)^2/6\). Choose the 32 largest **strictly positive** scores. The chosen real cells are disjoint from one another and from SM12's existing 17 source bands. Candidate selection is a deterministic finite search over proven signed-cell inequalities, not an unvalidated sampling argument.

For every chosen cell, independently recompute all 25 actual physical source Fourier midpoint values \(v_I\) and original full local frequency second derivatives, retaining the \(\sinh(x/2)\) pole. The symmetric-band mean \(u_I=|I|^{-1}\int_I T(\xi)d\xi\) has certified componentwise radius

\[
|u_{i,I}-v_{i,I}|
\le e_{i,I}
=r^{(0)}_{i,I}+\frac{K_{i,I}}{6}\left(\frac{|I|}{2}\right)^2,
\quad
K_{i,I}=\min\bigl(K_{i,\mathrm{global}},
|T_i''(c)|_{\rm up}+M_{3,i}|I|/2\bigr).
\]

Frequency-linear terms cancel in the **exact** symmetric mean. Denote \(P_{\rm add}=\sum_I\gamma_I v_Iv_I^T\) with every one of the **625** source cross entries and all actual 25 physical source vectors. The true complete original positive LOW source operator obeys

\[
\boxed{
A_{\mathrm{low},25}\succeq L_{47}
+P_{\mathrm{add}}-\epsilon_{\mathrm{add}}I_{25},
}
\]

where \(\epsilon_{\mathrm{add}}=\sum_I\gamma_I(2\sqrt{V_I^2 E_I^2}+E_I^2)\) and all roots are rational exact outward bounds. The old original SM47 \(\epsilon_{47}\) and true source contribution retain their definitions and are not weakened.

For the particular original physical \(e_2\) there is additionally the **independent, tighter** directional fee

\[
\epsilon_{2,\mathrm{add}}
=\sum_I\gamma_I\,[2|v_{2,I}|e_{2,I}+e_{2,I}^2],
\quad
\Delta_{2,\rm new}
=(P_{\mathrm{add}})_{22}-\epsilon_{2,\mathrm{add}}.
\]

This directional quantity **cannot** be substituted for the full-matrix Loewner error. The original SM48 negative fifteen-band lower \(N_{15}-\epsilon_NI\) is recomputed identically and held fixed. Define the previous exact *reference* deficit \(d_{\rm old}=(N_{15}-\epsilon_NI-L_{47})_{22}>17/1000\) and the new *directional reference* deficit \(d_{\rm new}=d_{\rm old}-\Delta_{2,\rm new}\). Require \(\Delta_{2,\rm new}>10^{-6}\) and \(d_{\rm new}<d_{\rm old}\). No implication that the true original signed \(W_o\) is negative, or that the new 49-band source reference controls the full negative spectrum, follows from this one-coordinate comparison.

## Scope and acceptance

A focused validator and GitHub Actions will rerun original SM12, SM04, SM42/SM46 original source physical evidence, check exact signed positivity on **every chosen whole real cell**, original 17-band disjointness, all 25-source mixed/pole cross, outward full and directional Loewner fees and strict source-2 gain. If the selection or source-2 improvement fails, SM49 must remain an open method candidate. The new matrix is a one-sided positivity **lower**, not a complete inverse or full-operator signed Schur.

The canonical complete original **W-ODD-NEG O1/O2**, 470 original polynomial sources and full pole-conditioned Astar inverse/strong residual, even sector **E1–E4**, original Weil positivity, CC27 and RH all remain **OPEN**. The inherited original Fourier/closed-domain identification and independent peer review are not supplied by GitHub Actions.

**Next decision after the actual numbers:** If source-conditioned extra true-positive mass produces material directional gain, extend coverage to all important negative packet directions and require an *entire* original source-coupled Schur margin. If the directional rescue is too small, optimize whole-real positive selection against full original inverse response, not by further arbitrary narrow window count. No complete-operator promotion from diagonal gains.


## First source-adaptive original certificate — focused CI PASS

**First GitHub Actions focused run [39192702260](https://github.com/monocap-tech/weil-lab/actions/runs/39192702260) SUCCESS**, verifying the original whole-real adaptive positive search, all 25 original supported physical sources and 625 matrix entries, all old 15 true-negative/17 true-positive source constraints, original sinc Fourier source mean enclosures, exact rational outward full Loewner error, and strict e2 source-directed gain.

| Original-source SM49 metric | Focused output |
| --- | ---: |
| Newly certified original signed-positive whole-real candidate cells | **365** |
| Selected disjoint exterior positive Jensen cells | **32** |
| Original signed SM48 e2 witness Fourier source center | **1845/128 = 14.4140625** |
| New original 25×25 global Loewner scalar fee | **1750720061/1000000000000 ≈ 0.001750720061** |
| New independently tight source2 directional fee | **40598563/250000000000 ≈ 0.000162394252** |
| Original SM48 e2 positive-lower-reference deficit vs 15-band negative lower | approximately **+0.0173332178482** |
| New certified positive gain on that actual original e2 | approximately **+0.0945442126163**, using directional fee |
| New e2 reference gap against retained 15-band negative **lower** | approximately **−0.0772109947681** |
| Strict source-local second-frequency-derivative improvements | **768** |

**Further comparison using the stronger standard:** Even using the **entire 25×25 Loewner scalar error** instead of the source-specific directional fee, the newly captured original-positive lower gain on e2 is approximately \(+0.0929558868\). Therefore the old \(+0.01733\) source-reference deficit changes to approximately **\(-0.07562\)** with the complete matrix error paid. This stronger exact inequality was subsequently made a fail-closed acceptance gate in the validator and workflow; its final-head run is separate from the initial successful run.

**What this does and does not establish.** The previously demonstrated **SM48 reference insufficiency along e2 is repaired** by actual missing original positive spectral mass. That conclusion is about comparing the new *positive LOWER* and the same 15-band *negative LOWER*, not the **full actual negative-frequency operator**; satisfying it does not certify even this source's full true signed Weil value. In particular, the entire actual original 25×25 \(P_{\rm add}-\epsilon_{\rm add}I\) is not automatically PSD: resolving one or several source directions never proves full source-space or 470-source operator positivity. No original odd spectral index/exceptional pole compensation, entire original W-ODD-NEG, even sector, Weil/CC27 or RH is proved.

**Next obligation, conditional on independent acceptance:** Test the new complete source-coupled **original positive lower** against a certified original negative-frequency **UPPER** on the same 25-source carrier, including pole subtraction, and quantify spectral/complement margins. Only that direction of the inequalities is capable of certifying actual signed positivity. If successful locally, extend the original 470 genuine sources and strong residual to the full physical domain; a 15-band negative LOWER is not sufficient for complete operator acceptance.

**Custody:** first substantive focused CI 39192702260 passed. Added stronger complete-matrix-error-paid witness threshold in subsequent draft commits; post-report head CI and independent mathematical audit remain separate, and all canonical operator obligations stay OPEN.
