# RC163 terminology additions

Definitions are additive. Historical trials and certificates retain their meanings.

**Centered omitted-difference trial.** Write delta=p+t, where p retains the canonical rational delta coefficients through even degree 4094 and t contains every remaining finite and analytic source coefficient. The new trial is Q_24(p)+t/2. The spectral inequality for the paid positive contraction is ||(C-I/2)t||_D <= ||t||_D/2; no commutation with the degree cutoff is assumed.

**Captured finite-prefix output tail.** Beyond even degree 8190, Cp has the exact representation -eta_n sum_{k>=0} mu_k r_n^k, with eta_n=(2n+1)/(n(n+1)D_n), r_n=4094*4095/[n(n+1)], and mu_k=sum_{m<=4094}(-delta_m)[m(m+1)/(4094*4095)]^k. The coefficients delta_m are negative and rational. Q_24 keeps 25 outward-controlled moment centers and pays their rounding and the entire geometric remainder separately.

**Changed physical inverse trial.** Keeping the RC158 coefficient matrix Y while replacing the delta action column changes the actual inverse trial vectors. The new marginal error controls are valid for these new vectors. Direct trial-source pairings, trial Gram entries, and nominal residuals for the previous vectors cannot be used as if their vectors were unchanged.

**Pairing rebase.** For h=q_delta_new-q_delta_old, add <h,s_j> to the delta trial-source row, add <h,q_j> to its trial Gram cross entries, and add 2<h,q_delta_old>+<h,h> to its trial Gram diagonal. Those terms must be enclosed before rebuilding the reference inverse estimate.
