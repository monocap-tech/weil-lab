# RPB108 terminology — finite physical source-square and residual Gram (NF21)

Date 2026-10-09 UTC. Additive definitions. Do not revise CC33, CC47–CC56, NF17–NF20 historical terminology or old certificates.

**Finite original physical source map.** Fix a=53/50 and parity p. Let E_p be the 56-dimensional physical-orthonormal supported Legendre low space, and H2,p the two exterior modes (112,114) even or (113,115) odd. Every vector of E_p ⊕ H2,p is a supported polynomial and belongs to the physical L2 operator domain of the complete original signed Weil form. Write L_p for the resulting L2 source map, representing Q(u,v)=<L_pu,v> for supported form tests. This is NOT a bounded source operator on all physical L2 or all canonical form-domain vectors.

**Original native blocks.** In this fixed 58-dimensional parity basis,
A=Q(E_p,E_p), B=Q(E_p,H2,p), C2=Q(H2,p,H2,p)>0,
and S2=A-B C2^(-1) B* is the TRUE signed two-high finite Schur form certified positive by NF19.

**Two-mode compensated source lift.** The rectangular coefficient matrix
T=[I_56; -C2^(-1)B*] maps each low x to the finite supported polynomial
p_x=x-Y2x. By construction Q(p_x,h)=0 for every h in H2,p. This is C-form orthogonality to the measured two high modes, NOT physical L2 orthogonality of p_x itself.

**Finite source-square Gram.** Let D be the complete physical L2 Gram of the 58 genuine original source vectors:
D_ij=<L_p e_i,L_p e_j>_L2, including archimedean log source, ALL original prime translations, both signed pole source terms, and EVERY arch/prime/pole cross. D is distinct from the native Q matrix.

**Physical high residual source Gram.** Define sigma_2(x)=Pi_F112 L_p (T x), with Pi_F112 the physical orthogonal projection off the entire retained E112 space. The matrix P2=Gram(sigma_2(e_i),sigma_2(e_j)) is the residual physical source Gram, and is exactly
P2=T* D T - S2* S2.
Since Q(Tx,h)=0 for every h in H2,p, the high physical projection onto H2,p vanishes; equivalently
sigma_2(x)=Pi_(E_p⊕H2,p)^perp L_p(Tx)
within the relevant parity. The latter gives a cancellation-resistant direct source representation. This identity does NOT assert that P2 has been numerically evaluated.

**Complete residual C-dual reaction.** On the infinite canonical physical complement F112 let C_full=Q|F112>=kappa I with kappa=207/1000. The true unmeasured response after two modes is T_rest(x,x)=||Q(Tx,.)||_(C_full*)^2. It satisfies T_rest(x,x)<=kappa^(-1) P2(x,x). Consequently P2<kappa S2 is a SUFFICIENT full original Schur sign gate, not yet verified. A failed Gram bound does not imply actual negativity.

**Low-mode source-sector squared Gram.** The physical L2 Gram of (L_prime+L_pole) restricted to E2=span{e0,e1}, with the complete active six-prime translation operator and original signed pole source. Its four source-square channels include prime-prime, pole-pole and TWO prime-pole cross terms, but OMIT the full archimedean source and its cross terms. It is neither the complete D nor P2.

**Error and cancellation rule.** Enclosing D and subtracting S2* S2 can be catastrophically ill-conditioned in near-critical directions. A valid certificate must pay errors through this subtraction, or construct sigma_2(x) pointwise with rigorous archimedean/prime/pole cancellation BEFORE squaring and integrating. No positive full-aperture sign may be inferred from separate diagonal source-square sectors.
