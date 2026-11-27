# IV106-E19R — signed pole and choice-defined packed rows

The original C3 pole column on the window is p(x)=2 sinh(x/2). Approximate
it by cell midpoint values a_i, frozen at scale 10^12, from the odd Taylor
polynomial through degree 15. Rational series remainder <10^-12; rounding
and Taylor combined <2*10^-12. cosh(11/20)<6/5 by rational series.
Physical approximation norm <= (6/5)*sqrt(665*h^3/12)+2*10^-12*sqrt(665*h),
upper 42495506374161984871/25000000000000000000000.
Both physical reconstruction adjoint and supported projection contract.

Authenticates E19P coefficient NPZ and E19Q matrix NPZ and JSON against
their recorded SHA256. First reuse original row synthesis in direction a,
then solve the joint interior/exterior least-squares system using the
existing three whole-bin Toeplitz weights (candidate selection only).
Freeze dedicated coefficients at scale 10^12. Replay the three quadratic
contractions using Python arbitrary precision integer arithmetic, no
intermediate flooring. Add exact entry error h/H*(ea*||x||_1^2+
ev*||q||_1^2+2*ec*||x||_1||q||_1), using E19Q's 61-unit entry bounds.
Infinite tail uses directional exact squared l2 jump norms and E19Q's
periodic Parseval argument. All estimates conditional on E19Q's analytic
derivations and literal step admission.

Inherited pole error upper .187897910689; dedicated .184581210784.
Dedicated finite squared upper .0334228872852, tail .000022715716561,
physical error norm .001699820255. This is too loose to assert that
the eventual terminal inequality is feasible. It is an absolute bound.

Packed columns: use the original certified IV097/IV100/E18M profile,
nonnegative, <=1 by normalized bump integration, disjoint, L1 mass
1/(1000k). Thus exact physical packed synthesis squared <=
1/(1000k)*sum |c_i|^2. The two adjoints contract, so zero approximants
supply a joint absolute row-error squared upper 1/34000 at k=34.
Zero approximants are not useful for relative row control or rank.
A potential proxy, equal to 1 on the original inner plateau and 1/2
on both transition strips, is independent of bump choice. Physical
squared joint proxy discrepancy <=1/(4000k)=1/136000. Its projected
Riesz approximation has not yet been evaluated. It cannot be substituted
as if it were the original column.

Using Cauchy-Schwarz over the three groups (665 cell, 1 pole, 34 packed)
gives conditional 700-coordinate absolute error norm <=.185195150448
with squared reserve <=.0342972437493 (rounded display). This does not
cover 34 IV105C projected response columns, and does not certify rank,
relative error, an action Gram, or positivity.

Local replay: remaining_reserves.py SHA256 027c41ea8af8576f7662e77e534c9d51c2d1925453834d58f70a8dfbe7336b82
remaining_certificate.json SHA256 59fe6feb3dc0e39d7c21c719bea36f0d124a7b9c2941da391077a62fd5f46a72.
The conversation artifacts contain the frozen pole coefficients and
exact rational reserves. Repository receipt is not a native verification.
