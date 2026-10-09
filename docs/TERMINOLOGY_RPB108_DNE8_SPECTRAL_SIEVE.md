# RPB108 DNE8 — Native low-energy reflection sieve

**Prior custody:** DNE7 head `43c34826d5a2a187fd2ad40cf38e43b81d6e20ba`. This DNE8 investigation does not alter active Coupled (CC) or Aperture (NF) branches.

**Native positive jump operator:** `J_a` is DNE3's closed supported positive selfadjoint operator containing the exact archimedean jump density `j(d)=exp(-|d|/2)/(1-exp(-2|d|))`, every active original prime-power shift with coefficients `c_n=Lambda(n)/sqrt(n)`, both orientations, and exterior killing. Its physical form domain is D_a; `H_a=J_a-kappa_a I`, with `kappa_a=log(pi)-psi(1/4)+2sum c_n`. Full original signed poles are NOT included in J_a.

**Low-energy spectral projector:** `P_(a,Lambda)=1_[0,Lambda](J_a)`, with finite rank `N_a(Lambda)` by compact resolvent, for Lambda>=0. For an actual moment-zero pole-free null, `J_a h=kappa_a h`, so h belongs to `ran P_(a,kappa_a)`. This is not a claim that such a null exists.

**Heat-regularized spectral sieve:** DNE5's exact killed heat domination and log-growth give `||P_(a,Lambda)h||_infty <= e^(Lambda+3)*sqrt(2/e)*||P_(a,Lambda)h||_2`. For measurable E subset (-a,a) of measure m, `||1_E P_(a,Lambda)||_(L2->L2)^2 <= m*(2/e)*e^(2Lambda+6)`. This is an operator estimate, independent of the old source gap.

**Heat-trace rank sieve:** The same killed time-one kernel is Hilbert-Schmidt on the finite cap, and `N_a(Lambda)<=e^(2Lambda)*Tr(e^(-2J_a))<4a exp(2Lambda+5)`. No numerical eigenvalues or genuine low-spectrum basis are computed by this bound.

**Reflected Hankel operator:** `B_a` on L2(0,a) is the bounded selfadjoint operator with quadratic form DNE7's reflected archimedean Hankel kernel `j(x+y)` plus all original prime reflections `c_n f(log n-x)` restricted to positive half support. Carleman's inequality and `j(t)<=1/(2t)+1` show `||B_a||<=pi*(1/2+2a)+sum c_n`. At a=53/50, `||B_a||<13` using the inherited sum bound. This is the REFLECTED PARITY COMPARISON, not full H, Q or J.

**Spectrally adapted matrix gate:** Let U_-:L2(0,a)->L2_odd(-a,a) be the normalized odd extension, and `P^-_(a,Lambda)=U_-^* P_(a,Lambda)U_-`. Then `P^-_(a,Lambda) B_a P^-_(a,Lambda)` has finite rank. It is NOT automatically positive; its sign requires the actual jump spectral basis or rigorous enclosures.

**Explicit anti-concentration witness:** With a=53/50 and `eps=10^(-22)`, DNE7's two positive-half intervals centered at 3log2/8 and 5log2/8, together with their negatives, form E of measure 8eps. Every h in ran P_(a,kappa_a) obeys `||1_E h||_2^2<10^(-3)||h||_2^2`. The DNE7 infinite negative reflected test subspace remains supported on these tiny intervals, so no nonzero member can itself be a low-energy eigenfunction. This does not imply positivity of B_a on the low-energy space.

**Control:** A connected two-site positive jump graph with positive rank-one even pole correction can possess a higher odd zero and a negative odd reflection expectation inside its finite-dimensional low-energy range. The spectral sieve does not alone exclude first contact.
