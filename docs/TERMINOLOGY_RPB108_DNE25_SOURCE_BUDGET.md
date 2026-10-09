# RPB108 — DNE25 terminology: native energy source budgets

Definitions are additive. DNE23–DNE24 definitions and historical certificates remain unchanged.

**Tested frame T:** the four original finite lifts (low,v,t,u) in each parity used in DNE23. Their retained components span Z8 across both parities. The seed and response columns include their authenticated high corrections. u is the raw NF32 probe. The exact original native energy matrix is A=Q(T,T); the full original projected high source map is R=P_F L_original T and its Gram is Gamma_T=R*R. F is the entire original F112, not a finite shell.

**Paid coarse matrix L:** DNE23 proves A-Gamma_T/kappa>=L>0, with kappa=11/25. In the rationally scaled columns D=diag(1,s1,s2,s3), D L D is the diagonal matrix with entries alpha,g,g,g. alpha and g are the DNE23 joint coordinate bounds. This matrix is a lower form bound, not physical coordinate mass.

**Native energy contraction credit c:** a certified positive rational c with L>=(c/kappa)A. It implies Gamma_T<=(kappa-c)A. c is dimensionless: it measures source square relative to the original native energy. It is distinct from the physical L2 gap delta=10^-36.

**Raw remaining frame W:** DNE24's 52-column physical orthogonal retained complement in each parity, with 104 columns in total.

**Native energy orthogonal remainder Y:** set P=Q(T,W), K0=A^-1 P and Y=W-T K0. Then Q(T,Y)=0 and B_Y=Q(Y,Y)=Q(W,W)-P*A^-1 P. This exact finite native inverse is distinct from the infinite high inverse. B_Y is not presumed positive. The retained projection of Y to the quotient E/Z8 is the original W basis, so T,Y,F still span the full original form domain.

**Complete remainder source Gamma_Y:** the full Gram of R_Y=P_F L_original Y. The source criterion c B_Y-Gamma_Y>0 is a strict positive definite matrix inequality. It automatically makes B_Y positive. It requires the whole 52-column Gram per parity, not positive diagonal scores or measured shell coordinates.

**Frozen rational remainder hatY:** a finite frame chosen using a rational approximation to K0 before the sign proof. Let hatB=Q(hatY,hatY)>0, E=Q(T,hatY), and hatGamma be its complete F112 source Gram. A native mixed dual norm epsilon bounds ||A^-1/2 E hatB^-1/2||. A source ratio r bounds hatGamma<=r hatB. The sufficient paid budget is r+kappa epsilon<c. These norms use original native energy, not physical coordinate identity.

**Coherent source bound:** the actual full source maps enforce ||R z+R_Y a||<=sqrt(kappa-c) sqrt(z*A z)+sqrt(r) sqrt(a*B_Y a). Cauchy-Schwarz gives a total ratio at most kappa-c+r when the native blocks are orthogonal. This pays all source crosses together without assuming their signs or evaluating them separately.
