# RPB108: contact trial hierarchy

Additive definitions, 2026-10-07. Choose the real actual derivative chain e_j=D^j h_*, n_j=r-1-j, and c=kappa_R(e_(r-1))!=0. Define the finite translation polynomial and its physical remainder by

    T_t e_j=sum_(q=0)^n_j (-t)^q e_(j+q)/q!,
    R_j(t)=tau_t e_j-T_t e_j.

The polynomial uses only existing lawful derivatives in K. It does not differentiate the rough terminal vector. Put D_t=diag(t^n_j), L=log(1/t), and

    U_jk=1/[n_j! n_k! (n_j+n_k+1)],
    H_jk=(-1)^(j+k)U_jk,
    A_jk=(-1)^(r+k)/(n_j+n_k+1)!.

All three are fixed finite matrices; U and H are positive polynomial Gram matrices. A is invertible by the pinned cross determinant.

The negative graph trial space is obtained by eliminating the positive Q Gram of the R_j from span(K,{R_j}). Its Ritz values use physical mass on that actual trial space. They give upper bounds by min-max, not exact eigenvalue asymptotics of the full enlarged operator.
