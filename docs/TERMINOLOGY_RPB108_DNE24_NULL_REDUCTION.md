# RPB108 — DNE24 terminology: exact remaining null reduction

Definitions are additive. Earlier terminology and certificates are unchanged.

**E112 and F112:** the physical retained Legendre space of degrees 0 through 111 and its original infinite orthogonal high complement, at aperture a=53/50. Reflection splits each retained space into 56 coordinates per parity.

**Z8:** DNE23's physical retained span of the low modes e0,e1, seeds x, responses w and fixed NF32 probes u, with four independent directions per parity. The certified positive form restriction is H=Z8+F112, including arbitrary high vectors, with physical coercivity guard delta=10^-36.

**W104:** the physical L2 orthogonal complement of Z8 inside E112. Its two parity spaces have dimension 52. In each parity the four constraint rows Z are (low,x,w,u). With P their four pivot columns, the exact basis column at a nonpivot index j is W_j=e_j-sum_i [(Z[:,P])^-1 Z[:,j]]_i e_{P_i}. Free rows form the identity. These are generally nonorthogonal columns; their coordinate mass is G=W*W.

**Native remainder B:** the original form matrix B_ij=Q(W_i,W_j), before eliminating H. NF31's positive raw 54-column restriction contains W104 and gives B>=beta G, with the inherited physical beta in each parity.

**Positive block H_op:** the self-adjoint operator associated with the original closed form restricted to H. It is distinct from the high-only operator C on F112. DNE23 gives H_op>=delta I and a bounded inverse on physical H.

**Mixed source map J:** J a=P_H L_original(W a), from the finite remainder coordinates to physical H. Original finite polynomial columns have physical L2 sources. This map contains the tested retained coordinates and the entire infinite high source. It is not just a selected high shell or just P_F L W.

**Exact reduced matrix D:** D=B-J*H_op^-1 J. The star denotes the physical Hilbert adjoint together with the ordinary coordinate adjoint. This is the single exact collective remainder after eliminating all of H.

**Energy-normalized total response K:** K=B^-1/2 J*H_op^-1 J B^-1/2. B is positive definite in the exact coordinate basis. K is positive semidefinite, but need not be <=I. It is not the raw source Gram divided by a scalar high floor. Neither D nor K is evaluated in DNE24.

**Unit response condition:** an actual unshifted original null corresponds exactly to a unit eigenvector of K. Whole positivity requires K<I. A large coarse loading, or even a true K norm greater than one, is not by itself the assertion that eigenvalue one occurs.

**Whole-mass shifted reduction:** for a spectral level lambda<delta, H_op becomes H_op-lambda I and B becomes B-lambda G. J stays unchanged because W is physically orthogonal to H. This rule pays the mass on both blocks. Normalization by B-lambda G is used only if that matrix is positive definite.
