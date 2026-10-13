# RC186 terminology: enriched five-source canonical inverse

Definitions are additive. RC184's response sources, RC185's exact q185, and the native seven-source frame retain their historical meanings.

- **Response source map S**: (P0,P2,f0,psi0,w14), exactly the RC184 family in its original order. The target is Sigma=S*D M^-1 S for the same full-domain canonical operator M=D^-1 L at B=11/10.
- **Raw trial map T186**: (P0,P2,f0,psi0,w14,q185). This enlarges the trial space, not the response source family.
- **Selected trial coordinate transformation A186**: the exact rational invertible matrix that retains the first five trial columns and replaces the last with (q185-Sb)/d. Here b is a rounded midpoint D-projection coefficient vector and d is a rational positive normalization. The transformed Gram lower is certified positive. This is a paid coordinate change, not a claim that actual source vectors are exactly orthogonal.
- **Enriched least-residual trial**: a rational coefficient matrix Y selected in the transformed coordinates and converted back to the raw trial basis. Its actual response residual is S-MT186 Y. Approximate midpoint matrices select Y but do not certify its validity or error; independently evaluated full residuals do that.
- **Baseline least-residual trial**: RC184's selected Y with a zero q185 row. It has the identical represented residual to RC184 and provides a same-family control.
- **Direct response error envelope**: the absolute columnwise triangle errors sum_k |Y_kj| epsilon_k, paid simultaneously for arbitrary complex response mixtures by a diagonal Young envelope. The alternative raw trial envelope is transformed by congruence with Y. Both are independently valid; selection uses whole valid matrices.
- **Nominal residual relative Gram upper**: a certified beta with Rhat*D Rhat <= beta G_lower, where Rhat=S-V186 Y includes every represented action tail. This is a squared-error factor for represented residuals, not an inverse response width and not the actual residual factor until action errors are included.
- **Variational response C**: Sym(S*D U)+Sym(U*D R), with U=T186 Y and R=S-MU. Equivalently C=2 Sym(S*D U)-U*D MU. The exact inverse response is C+R*D M^-1 R. Sym denotes the Hermitian part; all stored coefficients are real and the resulting bounds apply to complex mixtures.
- **Algebraic variational enclosure**: the same C enclosed using full trial source and canonical Gram Loewner endpoints. **Direct variational enclosure**: independently accumulated finite U/residual products with paid complete tails and action errors. Their complete matrix endpoints are alternatives, never combined entrywise.

Inherited RC184 inverse endpoints are also valid bounds on the unchanged target. Selection explicitly records when they are retained. Merely adding a trial direction does not constitute acceptance of the five-source inverse gate or closure of Stage I.
