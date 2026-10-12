# RC166 terminology additions

Historical trials and certificates retain their meanings.

**Three-action reference interface.** The approximated endpoint action on a source mixture y=WYc is the sum of four native action columns and three separately evaluated trial columns q_t, q_psi, q_delta, with coefficients Y4, Y5, Y6. The old native fitted Ct column is removed. The three-by-seven trial-source matrix and three-by-three trial Gram matrix describe these actual changed vectors.

**Native residual after Ct removal.** The correlated native residual term is W(Y-X)+T4 Y[0..3], where T4 contains only the four unchanged native action columns. Its cross terms with the three separate action trials and the full three-trial Gram are paid before applying a residual norm estimate.

**Independent lower-bound candidates.** The structural half-Gram lower bound remains valid even when a positive variational lower bound is weaker in some directions. RC166 tests each applicable lower against every tested upper instead of replacing the structural lower solely because a variational lower passes PSD.

**Reference half-Gram width gate.** The selected reference inverse enclosure [L,U] passes this gate when (1/2)G_lower-(U-L) is PSD. Passing it is a specific matrix-width certificate; it does not by itself certify the required final Stage I tolerance, original Weil source transport, or whole-aperture positivity.
