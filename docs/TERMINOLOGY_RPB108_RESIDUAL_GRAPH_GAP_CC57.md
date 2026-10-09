# CC57 terminology: Galerkin form error and physical residual

These definitions precede their use in the CC57 report. They do not identify the abstract control below with the original Weil operator.

For a positive selfadjoint high operator C >= kappa I, a physical source g, and W=C^{-1}g, the **form Galerkin projection** Y_m is the C-form orthogonal projection of W onto a finite trial space H_m contained in Dom(C). The **true response remainder** is T_m=||C^{1/2}(W-Y_m)||². The **physical residual squared** is P_m=||g-CY_m||². These obey T_m <= P_m/kappa, but convergence of T_m does not by itself imply convergence of P_m.

The **graph norm** is ||v||_graph²=||v||²+||Cv||² on Dom(C). A sequence of projections is **uniformly graph bounded** if its operator norms in this norm have a common finite bound. Graph density of the nested trial union together with uniform graph boundedness is one sufficient upgrade from form convergence to physical residual convergence. It is not asserted to be necessary for convergence for a particular source.

The **physical residual gate** is P_m < kappa(A-G_m), as a quadratic-form inequality on the retained carrier, where G_m is the eliminated finite trial response. It suffices for positivity because G=G_m+T_m. The abstract one-dimensional retained control makes this gate fail at every stage even though A-G>0.

An **inference control** tests a proposed consequence of stated operator hypotheses. It is not an original arithmetic countermodel and establishes no logical nonimplication from the complete Weil identities.
