# RPB108 compensator residual terminology

In the fresh fixed packet on D_b, F=G_b^(1/2), J_t:D_t->D_b is unchanged physical inclusion, G_t=J_t*G_bJ_t, R_t=R_bJ_t, and L_t=Ran(FJ_t). Use P_t=J_t*F and the reduced signed compensator C_t=-FJ_t G_t^(-1)R_t*. Negative synthesis is R_t*=-P_tC_t. The letter L_t here denotes a positive coefficient subspace, not the finite response covariance R_tG_t^(-1)R_t*.

For a nonzero endpoint-null k in D_c and c<t<=b, let I:D_c->D_t preserve the physical vector. The **enlarged residual** is r_t=A_t I k. Its **effective inverse energy** is e_t=real inner(r_t,G_t^(-1)r_t)>0. The **compensator increment** is delta_t=C_tu-a, with u=-R_c k and a=C_cu=FJ_c k.

A signed factor X is **reduced** when its image is orthogonal to ker P_t. A nonreduced factor has the form C_t+Z with P_tZ=0. This is the sign-adjusted IsReducedFor condition in Screening/Douglas.lean.
