# RC157 terminology additions

These definitions are additive; earlier checkpoint definitions are unchanged.

**Old/new source split.** The old source frame is (P0,f0,w14-alpha*psi0,(v10+z_b6)/2,t10). The new source frame is (psi0,delta), delta=z_b6-v10. Their union is RC150's invertible seven-source frame. The old action trials are RC138's five full-carrier action columns, and the new action trials are RC154's q_psi and RC153's q_delta.

**Directed cross trial-source blocks.** Q_new,old contains <q_new,j,s_old,i>_D and has size 2-by-5. Q_old,new contains <q_old,i,s_new,j>_D and has size 5-by-2. They are evaluated independently and are not presumed transposes. The true endpoint source cross block H_old,new is symmetric under exchange of its two sources, so both action directions provide intervals to intersect after their errors are paid.

**Mixed old/new trial Gram block.** R_old,new contains <q_old,i,q_new,j>_D. Its transpose is the reverse block of the full symmetric trial Gram. RC157 pays all ten entries directly from the finite coefficients and signed analytic tail polynomials.

**Complete seven-source pairing interface.** RC149 supplies the paid old response block and preceding old-source Gram/endpoint data, RC156 supplies the new trial/source and trial Gram block, and RC157 supplies the cross blocks. Their availability allows a full variational inverse-response assembly; it does not itself certify that inverse matrix or its width.
