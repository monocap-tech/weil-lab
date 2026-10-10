# RPB108 — CC99 response frontier terminology

Definitions are additive; CC93 and all historical statements retain their original scope.

**Common comparison floor:** kappa=11/25 is the inherited original high floor on F112. A comparison of methods uses this same floor, original operator and physical trial packet. CC93 historically used 207/1000; its literal historical certificate is not a dominance theorem over DNE's stronger current floor.

**High operator A:** the original positive high restriction on F112, with A>=kappa I. Its inverse exists by the inherited high coercivity theorem. It is not evaluated here.

**Trial map Z and source map R:** Z maps finite coefficients to the frozen physical trial packet; Q=Z*L_original Z and R=P_F112 L_original Z. Gamma=R*R is the complete projected original source Gram, including the infinite high tail.

**Paid high map Y:** a finite family of high vectors in the original operator domain, whose native and complete source moments have been certified. Define N=Y*A^2 Y/kappa-Y*A Y and W=R*(A-kappa I)Y. The formula below requires a certified positive definite N; redundant zero-response columns must be removed before inversion.

**Uniform-floor Schur lower matrix:** S0=Q-Gamma/kappa. DNE's signed matrix is kappa S0=kappa Q-Gamma.

**Response Schur lower matrix:** SY=S0+kappa^-2 W N^-1 W*. Its correction is positive semidefinite. Strictly stronger as a criterion means that every S0>0 packet passes SY>0, and an admissible packet exists with SY>0 but S0 not positive. It does not mean that SY-S0 is positive definite or that every failed packet is rescued.

**Failure-direction response threshold:** for an exact trial v with v*(kappa Q-Gamma)v<0, a necessary condition for SY>0 is v*(kappa^-2 W N^-1 W*)v> -v*(kappa Q-Gamma)v/kappa. Passing that scalar threshold does not certify collective positivity.

**Input and arithmetic costs:** m is the number of trial columns, r the number of paid high columns. Input comparisons count unique signed source moments, while matrix arithmetic comparisons count dense operations; they are distinct from the cost of rigorous analytic original-source integration.
