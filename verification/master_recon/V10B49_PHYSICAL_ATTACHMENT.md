# V10B49 physical constraint-coordinate reconciliation

Status: independent exact rational/integer replay PASS, native carrier and kernel attachment outstanding.
Sources inspected at fe40d32389a101c42fb0bc363fd6cc07f4e0ef5f:
V08E.moment_apply; V10B13a.input/moment; V08F.physicalL1Inclusion_ae; V08K.restrictPhysical_ae; V10B8c.eval_eq; V10B17a.poleDifference; V10B17b.bank/retained; V10B29a.physicalTrial_ae/trial_carrier_exists; V10B47c.unitMatrix.
Recovered coordinates: ff02606408804d992bc0539786d719db7936248a, blob 3887cf6428125c3fba5eb6587c53df4a3f57613d.
Executable replay: python3 verification/master_recon/v10b49_physical_rows.py (commit b8dcd57148e50237de9ac8a019cb1c508055dbda, blob a270a5d9d011bc4b5d3c522c4d431f4c1492e6d5).
Independent replay: 450 inverse entries, 225 physical moment pairings, 240 trial row transforms, 2560 symbolic pole-row coefficient cancellations PASS. Reproduction script committed/read back; Python execution not observed in CI.

Let x in [-1/4,1/4], z=2x+1/2, dx=dz/2, D=2^48. Write m_i(g)=integral x^i g(x) dx, l_i(g)=integral P_i(4x)g(x)dx, p(g)=integral (exp(x/2)-exp(-x/2))g(x)dx, over this support with g the physical inclusion representative. T_ik=[x^k]P_i(4x), l=T m. Its inverse U is given by x^i=sum_j U_ij P_j(4x); both matrix products equal identity over Q; diagonal T_ii=2^i binom(2i,i)>0.
I_j=integral_0^1 exp(z/4-1/8)P_j(2z-1)dz. Let h be the literal V10B47c.load. Then
p_def=p-2 sum_{j=1,3,...,13}(2j+1)I_j l_j=62 I_15 integral_phys h(z)g(x) dx.
Scaled coordinate map: rows 0..14 are 2 D (2i+1) l_i; final row is D/I_15 times p_def. Because D>0, I_15>0, T invertible, this is an invertible row operation on the original physical constraint vector. For trial g_c with physical representative V10B47c.trial c (2x+1/2)/D on the support, its matrix is exactly V10B47c.unitMatrix. The final row equals v_c15 + sum_{j=17,19,...,159} v_cj I_j/I_15.

The above is mathematical attachment specification, not a compiled theorem. Remaining: native literal moment/pole integral equalities for all carrier elements, affine substitution and finite projection identities, trial carrier existence, invertible coordinate transformation, orthogonal-complement equivalence for V10B17b.retained, native optimized matrix surjectivity. Original V10B19 archive unavailable; energy and residual attachment separate. No adoption.
Runs 45927665008 and 45928064611 in progress, 45928684686 pending at initial check; no workflow modified or added in V10B49.

## Native reconciliation at end of V10B49

Run 45928064611 completed failure overall. New strict audits: V10B45a 5, V10B34b 2, V10B36a 6, V10B37a 4, total 17. Conservative certified inventory 581/813. The repository Python replay reproduced the historical derived SHA256 and both tight dominance budgets; coarse high row margin 2.960027988079781.
V10B38a only failed on redundant tactic and multiplication association; repaired commit eb4fc0f072ae0428db27e9c9c6d09a1f624e9843. V10B39b only failed on unresolved measure in project_sub; repaired commit 7911d214a1c9b324afc90514113ed2d71242b3c7. Repairs uncompiled; focused run 45928684686 is active on earlier source and was not interrupted. Arithmetic run 45927665008 also active at latest check. No additional theorem candidates.
