# NF26 terminology — fixed high correction and directional Schur certificate

These definitions are additive; historical wording is unchanged.

Let E be the original E112 retained space, F its physical orthogonal
complement, and C the original high form on F with the certified lower
bound C >= kappa I, kappa=207/1000. An NF24 target p has a retained
component x in E and a frozen two-mode high component in F.

A **fixed rational high correction** y is a finite polynomial in original
normalized high Legendre modes, with rational coefficients fixed before
proof evaluation. Diagnostic values may choose y; they supply no bounds.
The corrected trial is v=p-y. Its retained component remains x.

The **corrected residual source** is r_v=P_F L_a v. The **directional
sufficient Schur score** is Q(v,v)-||r_v||_2^2/kappa. If its rigorous lower
bound is positive, square completion and C>=kappa I certify strict
positivity of the original Schur form on the retained direction x.

The **original directional Schur value** equals
Q(v,v)-<r_v,C^-1 r_v>, independently of the chosen high correction.
The inverse denotes the coercive high-form response, not a bounded
realization of the full logarithmic Weil operator on physical L2.

A pair of certified opposite-parity retained directions spans a positive
two-dimensional Schur restriction by exact reflection parity. It does
not certify the complete retained Schur matrix: couplings to the other
retained directions still require collective control. A failed score is
only failure of this sufficient test and does not prove negativity.
