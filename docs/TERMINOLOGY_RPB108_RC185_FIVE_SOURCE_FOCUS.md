# RC185 terminology: paid five-source focus action

Historical meanings and the native seven-source frame remain unchanged.

- **RC184 focus coefficient x**: (-1/120,3/50,-14/25,-26/25,1) in the response order (P0,P2,f0,psi0,w14).
- **Actual focus residual R185**: (S-MS Y)x, using RC184's selected least-residual trial matrix Y and actual canonical operator M=D^-1 L at B=11/10.
- **Nominal focus residual Rhat185**: (S-VY)x, with the complete finite/analytic represented action map V used in RC184. This differs from R185 by the paid action representation error.
- **q185**: the exact rational degree-256 polynomial obtained by rounding the even Legendre coefficients of Rhat185's degree-256 prefix to a 10^-40 coefficient grid. The interval radii and all discarded finite and infinite coefficients are paid. q185 is a new auxiliary trial direction; it does not rename or overwrite RC179's q, nor any native direction.
- **Single-focus action representation error**: sum_i |(Yx)_i| epsilon_i, where epsilon_i is the inherited complete D norm error of column i of V. This is a triangle bound on one vector. It does not replace RC184's simultaneous five-source error Gram.
- **Complete q185 action**: q185+Cq185-rD^-1 q185+D^-1 Rq185, with a finite represented endpoint/regular carrier and paid complete output tails. The regular kernel R in this expression is the canonical regular operator, not the focus residual R185.
- **Residual approximation ratio**: ||R185-q185||_D upper divided by a certified lower bound for ||R185||_D. It is a norm ratio on this single residual, not an inverse-width ratio or Stage I completion ratio.

The current pass certifies q185 and its actual canonical action. It does not evaluate an enriched inverse, close the five-source gate, or establish original augmented Weil positivity.
