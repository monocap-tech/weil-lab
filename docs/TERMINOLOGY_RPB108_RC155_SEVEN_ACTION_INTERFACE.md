# RC155 terminology additions

Historical definitions are unchanged. The following entries apply to RC155.

**Seven-source action-error map Ecal.** In the RC150 augmented source frame s=(P0,f0,w14-alpha*psi0,(v10+z_b6)/2,t10,psi0,z_b6-v10), let q_i be the paid full-carrier approximation to Cs_i. The first five q_i and their error bounds are RC138's trial action columns; the last two are RC154's centered analytic-tail trial and RC153's correlated difference trial. Define Ecal(c)=sum_i c_i(Cs_i-q_i). This is a linear map into the full D carrier; the q_i need not belong to the seven-source span.

**Signed rank-one action-error control.** If ||Cs_i-q_i||_D<=epsilon_i and G is a positive source Gram lower, a real sign vector sigma produces v_sigma=(sigma_i epsilon_i). The inequality beta G-v_sigma v_sigma^T>=0 is equivalent to v_sigma^T G^-1 v_sigma<=beta. Checking every sign up to simultaneous reversal proves ||Ecal(c)||_D^2<=beta c^T G c for all real c. Because the sources, endpoint operator, and paid trials are real, this bound extends to complex c by decomposing into real and imaginary parts. It does not assume mutual error orthogonality or known error signs.

**Inherited trial-source pairing enclosure.** For H_ij=<Cs_i,s_j>_D, an interval enclosing H_ij and the bound epsilon_i||s_j||_D give an interval enclosing Q_ij=<q_i,s_j>_D. Q need not be symmetric. RC155 transports existing endpoint intervals this way; it does not directly evaluate the new trial coefficients in these pairings.

**Full seven-source action half-Gram gate.** The inequality ||Ecal(c)||_D^2<=(1/2)c^*G c for all source coefficients c. This concerns approximation of C on the source span. A variational inverse-response matrix and its certified width require separate calculations.
