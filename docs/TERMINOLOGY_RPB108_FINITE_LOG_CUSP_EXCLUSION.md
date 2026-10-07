# RPB108: finite inverse-log cusp exclusion

Definitions used in the companion note.

- Actual aperture: a fixed finite a>0 with physical interval I_a=(-a,a); zero extension is understood.
- Full-native residual: q_h=m0(D)h-T_a h+p_h. Here m0(xi)=Re psi(1/4+i pi xi)-log pi, T_a is the complete frozen prime-power translation operator, and p_h is the actual two-moment pole term. Full nullity is q_h=0 on I_a in distributions, together with the canonical native carrier condition. No selected-background equation is substituted.
- Xcrit: squared Fourier weight (1+|xi|)log(e+|xi|).
- Finite inverse-log cusp class: h=b+sum c_(j,side,q) chi_(j,side)(x) log^(-q)(1/|x-x_j|) on the indicated side of x_j, with finitely many centers x_j in the closed interval, finitely many real exponents q>1, smooth cutoffs equal to one near the center, and b smooth compact on R. All terms are zero outside the physical interval; endpoint terms have only the inward side. Cutoffs can be supported in mutually disjoint short neighborhoods of the distinct centers, of radius <1. Equal center/side/exponent terms are combined before selecting the least nonzero exponent.
- Leading exponent q0: the smallest exponent with a nonzero combined cusp coefficient. At a given center a_+,a_- denote its right/left coefficients at exponent q0, with zero assigned if absent.
- Interior coefficient matrix: B_q=I+[1/(2(q-1))] ones(2,2). Its symmetric eigenvalue is q/(q-1), antisymmetric eigenvalue is 1.
- Inward endpoint coefficient: b_q=1+1/[2(q-1)]=(2q-1)/(2(q-1)).
- Finite cusp exclusion: full interior homogeneity forces every cusp coefficient of a member of this class to vanish. It then belongs to H1. This is a theorem about the defined class, not a boundary classification of the actual kernel.
