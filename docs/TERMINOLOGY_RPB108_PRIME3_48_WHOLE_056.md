# RPB108 48-coordinate whole-domain sign at aperture 14/25

- E_48: the physical orthonormal Legendre span of degrees 0..47 on [-14/25,14/25]; P_48 is its physical L2 projection.
- Q_48: actual native restriction on E_48, including prime powers 2 and 3 and both pole terms at this aperture.
- R_48: actual residual Gram of all 48 native sources after P_48 is removed; Rhat_48 is the certified source-surrogate Gram.
- Complement coercivity 3/5: the previously certified actual 48-moment physical lower bound, with logarithmic coercivity 9/100 on the same lawful form domain.
- K_48: lawful form-complement lift correction. The matching complement proves K_48<=(5/3)R_48.
- Corrected margin tau=1/40000000: certified lower bound for Q_48-(5/3)R_48 and hence Q_48-K_48.
- Lift norm bound 5: the physical operator bound obtained from (25/9)(trace Rhat_48 upper+delta)<25.
- Whole-domain margin 1/2080000000: physical L2 coercivity on the actual canonical supported logarithmic form domain at a=14/25.
- Antiderivative-Horner correlation: the same exact integral of p(x)q(x-y) from x=y-1 to 1, computed by forming its polynomial x-antiderivative and evaluating the lower endpoint by Horner at x=y-1.
- Beta-integral regular factor: exact evaluation of sum_{r=1}^j binom(j,r)(-1)^r/(k+r), equal to -H_j for k=0 and j!(k-1)!/(k+j)!-1/k for k>0.
- Cached-power composition: precomputing each shift power by the original multiplication sequence, so the rational and interval polynomial compositions are unchanged.

The valid historical 36-moment scalar-family obstruction remains separate. The factor 5/3 and the new sign use the matching 48-vector matrix, 48 source columns and P_48 projection. Fixed-aperture unit domination does not close global endpoint exclusion or retained witness/null transport. F4 and FULL TRANSPORT CLOSED remain open; Lean is unchanged.
