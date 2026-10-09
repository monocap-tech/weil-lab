# CC78 — new probe restriction with the entire high space

Definitions are additive. All original quantities concern aperture 53/50. E112 is the retained space, F112 its entire orthogonal high complement, and C=Q|F112 >= kappa I with kappa=207/1000.

Let u_even and u_odd be the original retained NF32 probes, not their lifted versions. U2=span(u_even,u_odd). Each probe lies exactly in its parity's remaining T and is physically orthogonal to the seed x and response w. The NF34 witness v=u+Hu has the same retained component, with its high lift in the disjoint H2 and expanded shells.

For each parity, m=||u||², h=||Hu||², gamma=||P_F Lv||² and s=Q(v,v)-gamma/kappa. The original retained directional Schur value is at least s. Exact parity gives a retained physical Schur gap mu=min(s_even_lower/m_even,s_odd_lower/m_odd) on U2.

Set eta²=sum gamma_upper/(kappa² m) and xi²=sum h/m. Completing the original high square and converting back to original physical mass gives a gap min(mu/(1+4eta²+4xi²),kappa/2) on U2+F112. This excludes original null vectors whose retained component lies in U2. It is separate from the prior Z4+F112 restriction.

For adjoining one probe to its same-parity successful pair, let A be that pair's exact two-by-two sufficient matrix, c the new sufficient diagonal, and b_i=Q(v_i,v_new)-<P_F Lv_i,P_F Lv_new>/kappa. The complete three-by-three sufficient matrix is [[A,b],[b*,c]]. Since A>0, its minimal border condition is c-b*A^-1b>0, with a quantitative positive remainder for a gap. This uses signed native and physical source crosses. Separate positive diagonals do not imply it; physical source covariance signs do not determine inverse-weighted covariance signs.
