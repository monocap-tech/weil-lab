# RPB108 NF24 — Compensated source targets and uniform reconstruction error

These definitions extend NF21's physical source-square and NF23's kernel
construction. Historical terminology and certificates remain unchanged.

At a=53/50 let e_j be the physical normalized Legendre modes and let x be
one of NF18's authenticated rational E112 directions. H2 is span(e112,e114)
in even parity or span(e113,e115) in odd parity. Its original native Gram is
C2 and its coupling with x is t. The exact minimizer is -C2^-1 t.

**Compensated rational target p:** x plus a fixed rational H2 coefficient
vector obtained by rounding an enclosure of that minimizer to denominator
10^80. It is a new explicit polynomial vector. Its measured H2 source
coordinates are tiny certified intervals, not asserted to vanish exactly.

**Physical residual source r_p:** P_F112 L_a p, with F112=E112^perp in
physical L2. Subtract all 56 retained source coordinates in the appropriate
parity. This includes the remaining tiny measured H2 source coordinates.
It is not the exact T-column P2 object unless the exact H2 minimizer is used.

**Arch source approximant L_arch,N:** preserve the true endpoint logarithm
and constant c=-gamma-log(2pi), replace only r(t)=j(t)-1/(2t) by NF22's
rational regular polynomial r_N. The same inside/boundary cancellation is
performed before evaluating the approximation error.

**Uniform reconstruction error eta_N:** 2a epsilon_N, where epsilon_N
bounds |r-r_N| on [0,2a]. For every supported polynomial p,
||L_arch p-L_arch,N p||_2 <= eta_N ||p||_2. This error bound is independent
of polynomial degree. It does not assert boundedness of the original
logarithmic archimedean operator on all physical L2.

**Finite residual projection lower bound:** for distinct high degrees J,
sum_{j in J}|Q_a(p,e_j)|² <= ||r_p||² by physical Bessel. This is a LOWER
bound on a source square, not an upper bound on the true high inverse.

The directional sufficient test is ||r_p||² < (207/1000) Q_a(p,p).
Success certifies the full high-extension sign for this one retained x;
failure rejects only this sufficient estimator for this direction.
