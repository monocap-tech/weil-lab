# CC60 terminology: variational correlated source gate

Additive definitions precede the CC60 report; CC59 symbols are unchanged.

For any EXACT rational matrix Y:E->H2, the **trial-corrected tail source** is rho_Y=sigma-KY=P_U L(T-H2Y). Its physical projection must remove BOTH E and H2; its measured high source coordinates are generally nonzero before projection.

The **finite penalty matrix** is W0=C2(C2-kappa I)>0. The **variational source gate matrix** is J(Y)=rho_Y*rho_Y+Y*W0Y. It satisfies T_rest<=J(Y)/kappa for EVERY Y; J(Y)<kappa S2 suffices for positivity. Optimizing gives min J=P-Z*(W0+H)^{-1}Z in the quadratic-form sense, attained at Y_star=(W0+H)^{-1}Z.

The **correlation-blind space** is ker(Z) in E. On it the optimized CC59 majorant equals the coarse P/kappa. This is not ker(B*), not a full-source kernel, and not an asserted critical eigenspace. Its dimension is at least54 in a56-dimensional retained parity carrier because Z has at most two rows.

A **penalty envelope** w I>=W0 follows from kappa<C2<L I by w=L(L-kappa). Using it loses some sharpness but avoids inverse enclosures and coefficient uncertainty inside a matrix penalty. The physical source error radius still must cover every arithmetic contribution and projection error.
