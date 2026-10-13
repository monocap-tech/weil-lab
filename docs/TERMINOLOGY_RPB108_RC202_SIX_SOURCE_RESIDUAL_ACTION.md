# RC202 terminology: six-source residual action

All quantities use the actual supported canonical operator M=D^-1 L, aperture B=11/10 and D-energy norm. Response order remains P0,P2,f0,psi0,w14,v10. The native seven-source frame is unchanged.

| Term | Definition and scope |
|---|---|
| Actual focus residual | r=Sx-MTYx for RC201's selected seven-trial inverse coefficients Y and a specified six-source probe x. This is distinct from the represented residual Sx-VYx. |
| q202 | Exact rational even polynomial through degree512 obtained by rounding the finite represented residual on the P0 coordinate. Its stored centers define the polynomial; coefficient radii measure approximation uncertainty, not a variable input. Distinct from q179 and q185. |
| Input approximation error | Certified upper for norm_D(r-q202), including retained coefficient rounding, omitted finite and infinite residual tails, and represented-to-actual action uncertainty. |
| Input half-norm budget | The local construction condition error_upper/residual_norm_lower <1/2. It is not the inverse half-Gram gate and not a Stage I tolerance. |
| Complete q202 action | q202 plus its signed endpoint action, negative-r D-inverse correction, and regular action. The endpoint carrier includes a finite prefix and25 exact signed output moments; all omitted output tails are paid. |
| Residual action transfer | From norm_D(M)<=2, the q202 action carrier approximates Mr within action_error+2*input_error. This bound is distinct from the much smaller action error on the exact polynomial itself. |
| Enriched inverse | A future inverse trial using q202 with certified mixed rows. RC202 does not evaluate this enlarged trial or a new inverse width. |

The latest evaluated six-source inverse remains RC201, width1.823489 G_lower and ratio3.646978 against its0.5 G_lower gate. The accepted five-source RC196 result remains intact. Original Stage I source-range and augmented positivity obligations, RH,F4 and Lean closure remain open/unclaimed.
