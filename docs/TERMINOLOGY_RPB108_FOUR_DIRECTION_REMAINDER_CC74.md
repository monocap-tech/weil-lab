# CC74 terminology: four retained directions and the remaining background

All quantities in this entry concern the original Weil form Q at aperture 53/50. E is the original 112-dimensional retained space; F112 is its entire orthogonal high space. The authenticated high floor is C >= kappa I, kappa=207/1000. The retained seeds x and orthogonal responses w are the exact rational NF24/NF27 vectors, with separate even and odd copies.

Z4 = span(x_even,w_even,x_odd,w_odd). Its physical retained mass M is diagonal in these coordinates because each x is exactly orthogonal to w and the parities are orthogonal. T is the orthogonal complement of span(x,w) in each parity of E; each T has dimension 54. Thus Z4 leaves 108 retained directions outside the full-high restriction.

For fixed high lifts H, let Lz=z+Hz, D=L*QL, R=P_F QL, and C=Q|F112. The sufficient retained Schur matrix is U=D-R*R/kappa. The actual retained Schur matrix is D-R*C^-1R and is bounded below by U. Each two-coordinate physical gap is bounded below by det(U)_lower/(U11_upper M00+U00_upper M11).

Write eta²=trace(R*R M^-1)_upper/kappa² and xi²=trace(H*H M^-1). Completing the square and paying the change to original physical mass gives a gap min(mu/(1+4eta²+4xi²),kappa/2) on Z4+F112, where mu is the smaller parity retained gap. This is a restriction of the original physical form, not merely positivity in lifted coordinates.

For the unlifted remaining background, A_T=Q|T and G=P_F QT. Its unchanged scalar-floor loading is theta=||G A_T^-1/2||²/kappa. For any unit original high mode e_h, with g=Q(T,e_h), theta >= g*A_T^-1g/kappa. A certified lower bound above one rejects A_T-G*G/kappa as a positive lower estimator. It does not establish negativity of A_T-G*C^-1G.

For joint condensation of T and F112 relative to the lifted pair, write B=Q(F112,T), R=Q(F112,L), N=Q(T,L), and D=Q(L,L). After high elimination, A'=A_T-B*C^-1B, N'=N-B*C^-1R, D'=D-R*C^-1R. The remaining obligation is A'>0 and D'-N'*A'^-1N'>0. Subtracting a finite remaining reaction independently from an already high-condensed pair estimate is not a valid joint lower bound.
