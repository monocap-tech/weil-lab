# CC94 — exact remaining retained complement

Definitions are additive; historical certificates remain immutable.

**Retained packet.** In each parity E has dimension 56. CC93 uses three lifted original trial vectors whose retained projections are the exact nonzero orthogonal vectors x,w,u32. NF37 changes their high lifts, preserving these projections. F is the original infinite high complement. Retained orthogonality does not imply orthogonality of the lifted physical vectors.

**Shared finite frame.** NF33 supplies the rational 56-by-54 constraint frame T of E intersect span(x,w)-perp, its rational two-high-mode map Z, and U=T-H2 Z. The retained projection u32 is T a, where a is NF33's inherited NF32 constraint vector. NF34 expands its high lift; NF35 and NF37 preserve this retained projection.

**Remaining complement.** Set r=T-transpose u32. Choose the first index p attaining max |r_p|. For every j other than p set J_j=e_j-(r_j/r_p)e_p. Then W=U J is a fixed lifted 53-column frame. Its retained projection T J is orthogonal to x,w,u32. The 53 free identity rows certify rank 53; together with x,w,u32 it spans E. Across parity the remaining retained dimension is 106.

**Inherited finite bound.** Restriction preserves Q(Ub,Ub)>=g ||Ub||² and the physical selected-shell operator bound. Therefore Q(Wc,Wc)>=g ||Wc||². This is a finite original-form bound on span(W). It is not a bound on span(W)+F, and it is not a joint bound with the three lifted packet vectors.

**Collective join obligation.** For packet V and remaining W define Q on their combined columns and R=P_F L_original[V,W]. Subject to the inherited operator/form attachments, the true finite Schur matrix is S=Q-R-star A-inverse R. The packet block is certified conditionally; the remaining block and signed mixed block are not. A paid common lower matrix with blocks K,X,C must satisfy K>0 and C-X-star K-inverse X>0. The complete remaining source Gram and its signed mixed covariance, or a justified sharper inverse-response construction providing the same collective lower bound, are required. NF33 finite energy and selected-shell suppression do not supply them.
