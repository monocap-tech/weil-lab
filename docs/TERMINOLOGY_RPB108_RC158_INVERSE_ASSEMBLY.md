# RC158 terminology additions

These definitions are additive; previous terminology is unchanged.

**Seven-source reference inverse response Sigma.** For the complete RC150 source frame s_i and A=I+C, Sigma_ij=<s_i,A^-1 s_j>_D. The inverse is the inherited bounded reference inverse with I<=A<=2I. This is not an original Weil/augmented action inverse.

**Full variational inverse enclosure.** For seven trial vectors y_i and residuals r_i=Ay_i-s_i, define L_ij=<s_i,y_j>+<y_i,s_j>-<y_i,Ay_j>. Then Sigma=L+r^*A^-1 r, so L<=Sigma<=L+r^*r. Directed Gram, endpoint, and action-error intervals give numerical Loewner bounds for those terms. Midpoint matrices select rational trials only.

**Conditioned residual source direction.** RC158 eliminates the five paid coordinates using the source Gram lower and replaces delta by delta+0.4828795091395692... psi0 with those paid-coordinate corrections. This is the seventh conditioned source column, not the unadjusted two-source mixture alone.

**Structural reference inverse enclosure.** The operator inequalities (1/2)I<=A^-1<=I give (1/2)G_Lo<=Sigma<=G_Hi for certified source Gram bounds. RC158 retains this positive baseline when its complete variational candidate fails the stronger positivity or width checks. Its use must not be reported as a successful precision gate.

**Enclosure-width failure witness.** A rational source coefficient vector whose quadratic value for the checked upper-minus-lower exceeds one half of its certified source Gram lower. This proves failure of that enclosure to meet the gate. It is not a lower bound on uncertainty of the true inverse and does not prove that sharper information cannot close the gate.
