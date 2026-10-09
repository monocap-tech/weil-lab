# DNE21 terminology — joint six-direction restriction

These definitions are additive and leave historical wording unchanged.

**Joint retained plane Z6.** At a=53/50,
Z6=span(e0,e1,x_even,w_even,x_odd,w_odd). The seed and response are the
same frozen retained vectors used in DNE18/DNE20. Each parity contributes
three independent retained vectors. This is their linear union span,
not a union of separate positive test sets.

**Low/lift native pairing.** Q(e0,v),Q(e0,t) in the even parity and
Q(e1,v),Q(e1,t) in the odd parity. NF31's retained source-coordinate
intervals enclose them after enlarging by the published physical
source-reconstruction error. t uses NF30's even lift or NF29's odd lift.

**Complete coarse three-direction matrix.** For T=(e_j,v,t), Q_T is its
native energy and Gamma_T its complete source Gram into F112. The lower
form is U_T=Q_T-Gamma_T/kappa, with kappa=11/25. The two new Gram crosses
are bounded by source Cauchy-Schwarz; no sign is assigned to them.

**Fixed rational congruence.** D=diag(s0,s1,s2) with positive rational
scales. Positive Gershgorin margins on D U_T D give
U_T >= g diag(s0^-2,s1^-2,s2^-2), where g is the smallest paid margin.
The retained basis is not assumed orthonormal.

**Completed column mass.** An upper bound b_i on
||T_i-C^-1 P_F L T_i||, bounded by ||T_i||+||P_F L T_i||/kappa.
These masses pay the physical norm after exact high square completion.
