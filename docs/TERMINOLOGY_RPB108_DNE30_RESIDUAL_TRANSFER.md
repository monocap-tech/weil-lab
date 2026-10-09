# RPB108 — DNE30 terminology: actual residual response transfer

Definitions are additive; historical source-front claims and certificates are preserved.

**Common original high operator A:** the selfadjoint operator associated with the original unshifted Weil form restricted to its closed form domain in F112 at a=53/50. NF42 calls it A; DNE17 calls the same restriction C. Both physically project off the first 112 native Legendre modes. DNE17's all-F112 form floor applies to this operator.

**NF42 base packet B and R:** B is the three frozen joined polynomial columns recorded in NF41; R=P_F112 L_original B is their complete physical high source. NF42's first source is a seed source, not DNE29's separate low-mode source.

**Optimized packet T:** DNE29's T=B-Z Csel, where Z contains NF38's two finite original high correction columns and Csel is the selected rational functional matrix. The retained coefficients are identical, while high lifts and native energy matrices differ.

**Actual high Schur matrix S:** Q_B-R* A^-1 R. It is the original high-eliminated energy of the retained three-column packet. It is unchanged by adding or subtracting any finite original high lift. DNE29 supplies the strict lower S>L=diag(ell_i/s_i^2) on this packet.

**NF42 model Schur matrix K1:** Q_B-R* A1^-1 R, where A1 is NF42's four-high-source minorant. This is an exact finite-rank-model quantity enclosed by the NF42 signed interval matrix; it is a lower bound for S after the floor hypothesis is discharged. Its negative certificate remains negative.

**Actual residual inverse response T1:** R*(A1^-1-A^-1)R. It is positive semidefinite and satisfies S=K1+T1. DNE30 derives bounds on T1 from DNE29's existing positivity; it does not evaluate the actual inverse or reconstruct new source columns.

**Scaled model envelopes:** after diagonal congruence by S_c=diag(s_i), M is the midpoint of the symmetric interval box for K1 and epsilon is its maximal radius row sum. Then M-epsilon I<=S_c K1 S_c<=M+epsilon I.

**Forced signed residual floor D:** diag(ell)-M-epsilon I. It satisfies S_c T1 S_c>D. D can be indefinite and is not asserted positive semidefinite. It is a signed matrix lower bound for the separately positive T1.

**Complete signed acceptance:** the model lower envelope plus D equals diag(ell)-2 epsilon I>0. This converts the inherited actual Schur bound into a robust full-matrix acceptance certificate in NF42's reference coordinates; it is not a new independent proof of DNE29 positivity.

**Forced witness response:** for NF42's frozen unnormalized h, h*T1 h>h*L h-upper(h*K1 h). The upper endpoint uses the intersection of direct signed-matrix and published witness enclosures. Its ratio to the necessary post-A1 witness deficit is not a physical gap or a normalized reaction norm.
