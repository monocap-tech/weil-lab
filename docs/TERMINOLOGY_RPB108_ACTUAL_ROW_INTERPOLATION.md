# RPB108: actual-row interpolation lift

Additive definitions, 2026-10-07. Retain the hypothetical actual nonnegative contact kernel K, r=dim K, generator Phi and auxiliary real nodes t where Phi(t)=0. These auxiliary nodes remain distinct from the actual zeta divisor.

Choose X={x_1,...,x_r} consisting of DISTINCT actual simple critical-line ordinates with Phi(x_i)!=0. If the stored positive coordinate has a nonzero normalization factor alpha_i, the raw row value is b_i(f)=p_i(f)/alpha_i=F_f(x_i). Existing pair/copy weights are retained. Multiplicity copies at one ordinate do not count as distinct x_i.

P_X(z)=product_i(z-x_i), and L_i(z)=P_X(z)/[(z-x_i)P_X'(x_i)] is the polynomial Lagrange basis. H_i is the physical kernel vector with profile Phi(z)L_i(z)/Phi(x_i). The actual-row kernel lift is

    C_X f=sum_i b_i(f)H_i,   R_X=I-C_X.

C_X|_K=I and the range of R_X has zero values at all selected actual rows. C_X is a bounded physical/domain projection onto K; it need not be the physical ORTHOGONAL projection. R_X gives an alternative bounded representative gauge for D_a/K.

The corrected Cauchy factor is

    A_(X,t)(z)=1/(z-t)-sum_i L_i(z)/(x_i-t)
             =P_X(z)/[P_X(t)(z-t)].

The explicit interpolation lift uses both the auxiliary energy samples F_f(t) and r original actual source rows b_i(f). It does not identify their node sets or delete the original signed source equations.
