# RC154 terminology additions

These entries are additive. Historical terminology and checkpoint wording are unchanged.

**Centered analytic input-tail trial.** For the inherited self-adjoint positive endpoint contraction C on the D carrier, write a source as p+t, where p is a finite degree prefix and t is the remaining analytic source tail. If Q(p) approximates Cp, the centered trial is Q(p)+(1/2)t. The error satisfies

\[\|C(p+t)-Q(p)-(1/2)t\|_D\le\|Cp-Q(p)\|_D+(1/2)\|t\|_D.\]

This follows from 0<=C<=I and does not require C to commute with the degree cutoff. In RC154, p is psi0 at even degrees 990 through 8190 and t is psi0 at even degrees at least 8192.

**RC154 output-tail moment trial Q(p).** Q(p) is the paid finite C action polynomial at even degrees through 16382 plus a 25-term common eta moment expansion at even degrees n>=16384. Here D_n=s+H_n and eta_n=(2n+1)/(n(n+1)D_n). Its moment coefficients are rational centers of mu_k=sum_m p_m (m(m+1)/(8190*8191))^k, for k=0,...,24. The moment interval at order 25 pays the positive geometric remainder; all interval radii pay rounding. The input-tail midpoint term and this output-tail expansion are distinct parts of the trial, with overlapping supports permitted.

**Two-column action-error half-Gram gate.** This is the inequality E <= (1/2)G_cond, where E encloses the D-energy of action approximation errors for all mixtures of psi0 and delta=z_b6-v10, and G_cond is RC151's conditional source Gram lower after the five paid source directions are eliminated. It is an action approximation gate, not an inverse-response matrix-width certificate and not Stage I closure.
