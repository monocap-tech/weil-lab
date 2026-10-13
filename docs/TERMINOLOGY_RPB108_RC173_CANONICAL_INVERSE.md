# RC173 terminology: actual canonical inverse and two-source width gate

The **two-source canonical inverse response** is Sigma=S^*D(D^-1 L)^-1 S=(D S)^*L^-1(D S), for S=[P0,P2]. It uses the actual canonical metric L. Its physical dual inputs are s P0 and (s+3/2) P2. It is distinct from the principal reference inverse P^-1 and the original augmented inverse Hhat^-1.

The **two-source canonical half-Gram gate** tests U-Lower <= (1/2) G_D,lower for this response enclosure. RC173 passes at the sufficient width 0.296983. This is not the historical seven-source reference gate or a prescribed Stage I completion tolerance.

The **canonical Riesz vector trial** is S Y, with a fixed rational two-by-two coefficient matrix. Its residual is S-(D^-1 L)S Y. The response identity adds the inverse residual correction. A narrow matrix interval is not a high-accuracy vector trial: vector error Grams are separately certified in both canonical and D energy.

The **two-source canonical warm start** is this represented vector trial with error bounded by 0.288212 times the true canonical Riesz image norm, uniformly over source mixtures. This follows from an additional exact error-Gram comparison with the inverse-response lower matrix; it is not inferred from matrix width.

The **correlated endpoint residual tail** combines both action columns through their common eta factor before a rank-one-plus-remainder bound. All degrees after the finite residual prefix are paid. No mixed action error is assumed orthogonal.
