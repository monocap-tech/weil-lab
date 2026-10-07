# RPB108: actual native drive with critically regular rough control

Registered 2026-10-07 before first load-bearing use.

- The aperture is the already certified a=97/100. The actual active prime powers are 2,3,4,5; n=6 has zero von Mangoldt weight. No new aperture estimate is introduced.
- k(s)=exp(-s/2)/(1-exp(-2s)) is the actual Euler kernel; k_reg(s)=k(s)-1/(2s). J(s)=k(s)-2cosh(s/2) is used only to express two boundary compatibility functionals. It is not asserted positive on the whole interval.
- For continuous supported vectors with absolutely convergent endpoint inverse moments, define L_R(h)=M_R(h)-2A_R,h(0) and L_L(h)=M_L(h)-2A_L,h(0), with A_R the genuine full-native combined drive and A_L its reflected version. These two functionals are boundary compatibility tests, not an injective observation on the carrier.
- Choose epsilon=1/1000 and delta=1/10000. A nonnegative smooth cutoff chi is one on [0,delta/2] and zero for v>=delta. The right cusp is h_R(a-v)=v^(1/4)chi(v), v>0. The interior cusp is h_I(x0+u)=u^(1/4)log(1/u)chi(u), u>0, where x0=a-log 2. Each is zero elsewhere. Set h0=h_R+h_I.
- b_R and b_L are nonnegative smooth interior bumps of integral one, supported at distances (epsilon,2epsilon) from the right and left endpoints respectively, and reflected copies of one another.
- B is the real 2-by-2 matrix B_ij=L_i(b_j), with i,j in {R,L}. It has no relation to the finite null-response matrix D_s, a selected packet, or a negative observation matrix. Its invertibility only solves the two boundary matching constraints.
- Set (c_R,c_L)^T=B^(-1)(L_R(h0),L_L(h0))^T and h=h0-c_R b_R-c_L b_L. This physical vector is a supported actual-native carrier control. Its actual drive and actual source coordinates are those of this same h.
- q_h=m_a(D)h+p_h is the exact full-native residual. The control does NOT solve q_h=0 on the interior. Its interior defect is proved explicitly in the note.

Scope: an actual-drive/actual-source positive-form control for a failed boundary-only derivative implication. It is not a positive eigenvector, a nonzero actual null vector, a counterexample to the homogeneous critical gate, or an F4 closure.
