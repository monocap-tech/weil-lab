# IV128 — Existence of coercive original cell-null tails

Parent db661e36d7d976c698d530e272e2a10f127963e7. The active IV127 native run 45751086812 has passed preflight and is compiling; its eventual result governs acceptance of this entire descendant chain.

For fixed a>=0, T>=0, set K=16 pi² a(2a)² T³/3. Then leakage=K/N². Select a natural N>2K+1; N²>=N>2K, hence leakage<=1/2. For any real M and eta set L=2(|M|+|eta|+1), T=exp L. Then log(e+T)>=L, and (1-leakage)log(e+T)-M>=|M|+|eta|+1-M>eta. No numerical estimate of M is needed for existence.

The final candidate uses the literal IV127 Schur receiver with M the actual IV124 response and native error budget. Quantifier order is important: for every k and eta, there exists one N such that ALL supported cell-null Schwartz tests obey the target coercivity. In particular eta=1 suffices for positive coercivity. N depends on k and eta, not on v. No assumption of packed mass orthogonality is needed for this tail inequality; intersect with that complement in the subsequent finite-head construction.

This is an existence proof, not a practically small cutoff, an evaluated matrix, or global positivity. The choice is intentionally crude; the sharper primitive/Poincare leakage bound remains a possible optimization. IV128 is not compiled or kernel-certified. Four named audit declarations; no explicit placeholders. Native gate to follow after IV127 completes; no duplicate dedicated workflow activated. Next: encode cell means as a finite linear map, prove finite codimension on the supported packed complement, and construct the finite lift and exact Schur receiver.
