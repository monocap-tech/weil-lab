# RC108 — nine native modes with full complement coupling

Date: 2026-10-11. Aperture a=11/10. Branch: `research/rpb108-route-consolidation`.

RC108 enlarges the previously certified six-dimensional corrected positive native span to nine dimensions. The enlargement includes all coupling to the canonical complement of the complete sufficient 1,250-feature head, and the mixed original Weil entries between the retained weak directions and the three newly admitted native directions.

The resulting explicit positive subspace has codimension 1,241. The original operator's nonpositive spectral dimension upper improves from 1,244 to 1,241. This is not a count of actual nonpositive modes. The remaining finite head is not certified positive, and no whole-aperture extension, RH or Global/F4 theorem is claimed.

## What is new relative to RC107

RC107 proves positivity of the entire original native 22-dimensional compression. That certificate alone does not pay its interactions with omitted directions. RC108 certifies a nine-dimensional native subspace *after* coupling it to the infinite original complement E. It keeps the same complete head H1250 and the same inherited original complement floor alpha=247/2500.

The selected native subspace is:

| Parity | Retained weak directions | Newly admitted RC107 candidates | Corrected dimension |
|---|---:|---|---:|
| Even | Three RC63 directions, including the positive control | Candidate index 10 | 4 |
| Odd | Three RC63 directions, including the positive control | Candidate indices 9 and 10 | 5 |

The new candidates are among the high compression spectral directions, rather than additional near-zero modes. Exact actual canonical metric lower checks prove that the nine selected vectors are independent. The six previously certified weak directions are retained, so this is a joint enlargement rather than a separate, unrelated positive test span.

All source integrals are inherited. New work consists of signed contractions, original source capture, actual error transport, mixed-covariance domination, and exact coupled matrix certification.

## Original operator and complete complement

Let A_Q=I+i*Ki be the original canonical Weil operator, H the complete sufficient 1,250-feature canonical Riesz head, E=H perpendicular, and

\[
D=P_EA_QP_E|_E\succeq\alpha I.
\]

Let J parameterize the selected native vectors in H. Its original head matrix is Q=J*A_QJ. Its complement source is R=P_EA_QJ, with coupling Gram Gamma=R*R. A lower for

\[
Q-\alpha^{-1}\Gamma
\]

proves positivity of the original operator on ran(J) plus E. No floor for a smaller canonical head is assumed, and the remainder of H is not eliminated in this argument.

## Coupling bounds for the new columns

The actual source for a native Riesz column u_j=i*q_j is i*(q_j+K i u_j). Its physical trial source is F_nom,j=q_j+K_nom i v_j, with v_j the unchanged RC67 64-degree Riesz trial.

Use RC83's signed source/Legendre pairing centers to form a *fixed* physical polynomial p_j of degree below 64. This polynomial maps by i* into H1250, so the actual complement projection kills it. RC68's signed complete physical source covariance and RC83's pairing radii enclose the Gram of F_nom-p.

For pairing center h_nj, radius r_nj and Legendre mass m_n, the residual Gram center is

\[
U_{ij,\rm center}-\sum_n h_{ni}h_{nj}/m_n.
\]

Its capture uncertainty is bounded by

\[
\sum_n (|h_{ni}|r_{nj}+|h_{nj}|r_{ni})/m_n.
\]

There is no missing radius-product term here: p is fixed at the center, so the exact residual Gram is U minus the two actual source/p pairings plus the known p/p Gram. It depends linearly on the uncertain pairings. This is a variational fixed-polynomial subtraction, not a claim that the pairing centers are the exact orthogonal projection coefficients.

A balanced symmetric interval row bound gives a common residual Gram upper W_up. RC95's actual rank-1250 adjoint tail bound tau gives N=tau squared times W_up for the nominal projected source covariance.

The actual source error includes the physical Riesz trial error through K and the nominal K correction applied to the trial. With rho=252/257 and nu=1/65536, the inherited projected archimedean, prime and pole transfer estimates give

\[
E_{\rm source}
=\rho(1+\nu)k_{1250}^2 E_{\rm Riesz,physical}
+(1+1/\nu)\delta_K^2\tau^2 T_{\rm trial}.
\]

Here k1250 is the RC89 projected transfer factor scaled by tau1250/tau38, as in RC98–101. The physical Riesz error upper is newly contracted from the raw signed RC81 intervals in the selected candidate coordinates. All original arithmetic components and uncertainty terms remain attached.

With source Young parameter t=1/8,

\[
\Gamma_{\rm new}\preceq G_{\rm new}
=(1+t)N+(1+1/t)E_{\rm source}.
\]

The selected new even block has one column and the odd block two. The covariance signs are used in common matrix uppers; they are not asserted as signs of the unknown actual projected covariance entries.

## A common bound for retained weak and new sources

Let G_weak be the unchanged actual rank-1250 source covariance upper from RC100 or RC101. The unknown mixed covariance between weak and new columns must also be paid. For arbitrary coefficient vectors x and y,

\[
\|R_{\rm weak}x+R_{\rm new}y\|^2
\le(1+s)\|R_{\rm weak}x\|^2
+(1+1/s)\|R_{\rm new}y\|^2.
\]

At s=1/8, this proves the joint Loewner upper

\[
\boxed{\Gamma\preceq
\mathrm{diag}((9/8)G_{\rm weak},\ 9G_{\rm new}).}
\]

This estimate does not require independence, orthogonality, or known signs of mixed complement sources. It retains the certified correlations inside the weak and new blocks, while paying their unknown mutual correlations by the displayed block inequality.

## Mixed original Weil entries remain signed

RC107 supplies signed entry enclosures in a complete eleven-vector native basis per parity. An exact rational solve expresses each retained RC63 weak vector in that basis. The solve is checked by exact multiplication. Contracting the signed centers and absolute radii against those exact coordinates encloses the original weak/new mixed entries.

The retained weak head lower is the original three-vector lower from RC100/101, not a recentered approximation inferred from the new candidate basis. The new head lower is formed from its matching RC107 signed entries. Their diagonal source penalties use the common joint covariance bound above.

Thus the corrected selected head has a valid lower family

\[
\begin{pmatrix}
L_{\rm weak}&C\\ C^*&L_{\rm new}
\end{pmatrix},
\]

where

\[
L_{\rm weak}=Q_{\rm weak,lo}-(9/8)G_{\rm weak}/\alpha,
\qquad
L_{\rm new}=Q_{\rm new,lo}-9G_{\rm new}/\alpha,
\]

and each entry of C ranges over its certified signed original Weil interval. Outward rational rounding is applied to all stored lower and upper matrices.

There are three unknown mixed entries in even parity and six in odd parity. The certificate checks all eight even and all sixty-four odd interval vertices. Positive definiteness of an affine matrix at every vertex proves it throughout the interval box by convexity. The actual canonical metric is bounded above by rho times the exact physical target Gram. Every vertex is also checked against the same positive canonical floor, with determinant-ratio replay.

The corresponding weak Schur matrices are checked separately using exact inverses of the new blocks. This certifies the retained exceptional weak directions jointly with the new native directions and with their full E coupling.

## Certified floors

| Selected corrected block | Dimension | Canonical lower floor |
|---|---:|---:|
| Even | 4 | 1e-19 |
| Odd | 5 | 1e-16 |

These floors concern the selected head after its scalar complement penalty. The actual complement-inverse effective head is at least as large, since D inverse is at most alpha inverse.

RC108 also supplies a positive floor on the *entire* selected-native-plus-E subspace, rather than only on the finite corrected block. Let g bound the actual selected complement source squared norm relative to its actual canonical metric. An exact relative matrix bound proves g approximately 0.0285347 even and 0.0640524 odd.

For x in the selected native space and z in E, completion of the square gives

\[
Q(x+z)\ge\beta\|x\|_c^2
+\alpha\|z+\alpha^{-1}Rx\|_c^2.
\]

Since ||R x|| squared is at most g||x|| squared and x is canonically orthogonal to E,

\[
\|x\|_c^2+\|z\|_c^2
\le\max(2,1+2g/\alpha^2)
\left(\|x\|_c^2+\|z+\alpha^{-1}Rx\|_c^2\right).
\]

Consequently the original floor on that complete positive subspace is

\[
\mu=\frac{\min(\beta,\alpha)}{\max(2,1+2g/\alpha^2)}.
\]

The accepted floors are approximately 1.46062e-20 even and 7.08037e-18 odd. Their minimum, recorded exactly as 62473216/4277173326341304779052734375, is a shared original canonical floor.

The selected native dimensions add to nine. Together with E, this explicit positive subspace has codimension 1250-9=1241. Any nonpositive original spectral subspace intersects it only at zero; projection onto its finite-dimensional orthogonal complement is therefore injective. This proves the updated nonpositive spectral dimension upper 1241. It does not locate or assert the existence of any nonpositive modes in that remaining space.

## Validation and scope

The validator binds eleven exact input byte hashes, including RC107, the retained weak certificates, and the matching source/metric/transfer data. It checks source and Riesz residual contractions, the exact coordinate changes, actual metric independence, all interval vertices, all canonical-floor inequalities, exact Schur inverses, and the joint coupling norm bound.

Independent replay reverses signed contractions and uses leading determinant ratios computed with fraction-free Bareiss elimination in place of LDL inertia tests. Replay reports PASS and reproduces the certificate exactly.

Repository reproduction:

```sh
python scripts/validate_rpb108_rc108_nine_mode_complement_closure.py > /tmp/rc108.json
python scripts/validate_rpb108_rc108_nine_mode_complement_closure.py --replay /tmp/rc108.json
```

Published artifacts are the validator, `certificates/rpb108_rc108_nine_mode_complement_closure.json`, and this note.

The nine selected directions with E are now certified positive. All 22 native directions remain positive as an original compression by RC107, but all 22 have not been certified after complement coupling. Neither complete spectral coverage nor a positive floor on the remaining full finite-head strong space is established. The remaining original head has dimension 1241 after removing the selected nine; it still requires a structural theorem or further certified block control. Whole-aperture positivity at 1.10, RH and Global/F4 remain open.
