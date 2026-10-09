# RPB108 DNE13 — Actual compensated constant-source diagnostic

Date: 2026-10-09 UTC / 2026-10-08 Pacific. DNE-only continuation from verified head 546594aa31c64fa64bd7daf487ca998fac049ac7. Terminology: [compensated constant](../docs/TERMINOLOGY_RPB108_DNE13_COMPENSATED_CONSTANT.md). Aperture dependency read at immutable head 1261995ecc9ce80351ab3cfbaf802929444fe92e. No other branch changed.

## Outcome and scope

DNE13 computes the complete original signed physical source of an actual two-high-mode corrected constant direction at a=53/50 and removes ALL 56 retained even physical Legendre projections. The numerical scalar residual budget is favorable. This is a numerical diagnostic, not an interval certificate, not the full 56-column Gram, and not a near-critical-vector calculation.

At integration order 360:

| Quantity | Numerical value |
|---|---:|
| c112 in w=e0-c112 e112-c114 e114 | -0.00709430182085 |
| c114 | 0.00513147655844 |
| Complete compensated source square | 0.0825065727686 |
| Complete E112 even projection square | 0.0785552885433 |
| Complete F112 physical source residual square | 0.00395128422533 |
| Corrected original energy | 0.0399313913300 |
| (207/1000) times corrected energy | 0.00826579800531 |
| Residual / sufficient budget | 0.478028161684 |

The sign of the subtraction is essential. The unsubtracted complete source square is about 0.0825 and would fail the scalar budget; the high source AFTER the complete retained projection is about 0.00395 and passes numerically. Integrating the projected source directly agrees with the difference of squares. Every original archimedean/prime/pole cross is retained before squaring.

Orders 160, 240 and 360 give residual squares 0.00395128463176, 0.00395128429919 and 0.00395128422533. These agreements are convergence diagnostics only. No rigorous discretization error follows from them.

## Independent native reconstruction

The source uses the exact DNE11 endpoint decomposition, all six original active prime powers {2,3,4,5,7,8} in both orientations, and the original even pole action. In the even sector the odd signed pole moment vanishes by parity. The regular convolution is split at y=x. Both outer endpoint panels use a square coordinate substitution; no endpoint source is discarded.

The singular polynomial action is computed using D[e_n]=H_n e_n. The independent Fraction validator verifies this polynomial identity for every n=0,...,114 by constructing Legendre coefficients and integrating the divided difference exactly. All 115 identities passed locally. These checks validate this finite singular action, NOT the complete quadrature.

The reconstructed high block agrees with NF19's published numerical diagnostics: Q112,112 about 3.45121178709; Q114,114 about 3.54567844637; Q112,114 about 0.636855534117. At order 360 the errors against those displayed values are about 3e-10. The constant diagonal agrees with the authenticated NF12 value to about 1.2e-12. The uncompensated complete source square agrees with DNE12 and DNE11's numerical pilot. High pairings after the numerical solve are about 1e-12.

The NF17/NF18/NF19 attached signed archives were not recovered in this workspace. Their hashes and published bounds were read, but no archive replay or exact NF19 coefficient authentication is claimed. The numerical source reconstruction is independent of those missing archive bytes.

## Rational successor and exact sufficient criterion

Freeze the explicit trial

    wbar=e0+(7094302/10^9)e112-(5131477/10^9)e114.

It has exact rational Legendre coefficients. Its numerical residual and budget agree with the solved trial; its remaining high pairings are approximately 3.4e-10 and -1.5e-9. They must remain in any rigorous residual, not be replaced by zero.

For ANY such finite polynomial w=e0+y with y in F112, define r(z)=Q(w,z), z in F112. With the inherited ORIGINAL signed high coercivity C>=kappa I, kappa=207/1000, completing the high square gives exactly

    S_Q(e0,e0)=Q(w,w)-||r||_(C*)^2
              >=Q(w,w)-(1/kappa)||P_F L_Q w||_2^2.

This does not require w to be the exact two-mode Galerkin minimizer. Thus freezing rational coefficients avoids an unnecessary prerequisite of computing an interval C2 inverse. A rigorous inequality P(wbar)<kappa Q(wbar,wbar) would certify the constant low line after its ENTIRE high inverse response. It would not certify all 56 even retained directions, the odd sector, or the original full aperture.

The available numerical margin is about 0.00431451 in squared-source units. A practical scalar target is rigorous P(wbar)<0.0041 and Q(wbar,wbar)>0.0399: then kappa Q>0.0082593, leaving a comfortable sufficient scalar surplus. These bounds are targets, not established inequalities.

## Next DNE14

Enclose the FIXED rational wbar source square and all 56 retained projection pairings by outward arithmetic using DNE11's finite polynomial/log source formula. Pay the complete regular-kernel and pole approximation errors and endpoint integration errors. No monotonicity of the high-degree source is assumed. DNE12's constant monotone Darboux argument cannot simply be reused.

After certifying this scalar gate, test a genuine near-critical retained rational direction, where the allowed budget can be many orders smaller. The present constant direction has energy about 0.04 and is not representative of NF17's tiny finite eigenmargins. Success on this scalar line supplies a source-residual method checkpoint, not an all-direction arithmetic theorem.

Scripts and numerical output were executed locally. The infinite-dimensional high inverse was not evaluated, no interval compensated-source certificate was obtained, and no Lean proof was completed. Global first-contact exclusion and RH remain open.
