# E19D: choice-independent pivot obstruction and bounded preceding-cell correction

Status: analytic derivation and exact rational replay; not Lean-certified.
Source: E18O positive series, E18M exact positive mass, E18K1 seed moments,
E18P Cauchy-Binet determinant transfer; E19C full constraint correction.

## Far pivot conditioning
At k=34, A_ij=sum W_n Y_n^i X_n^j (i,j=0..33), lambda_n=2n+1/2,
X_n=exp(lambda_n h), Y_n=exp(-lambda_n d), h=11/3325, d=3/68000.
For n>=1, integration by parts three times using b=t^5(1-t)^5 gives
-W_polynomial = (lambda_n h)((lambda_n h)^2-h^2/4) * integral_0^1 exp(lambda_n h t)b(t)dt.
All remaining factors in W_n X_n^j are positive. Relative to n=1,
the polynomial prefactor ratio is <=n^3, and the common positive double
integral over row-zero profile and seed is damped by exp(-2(n-1)gap).
For cells 1..34 gap>2 exactly, hence ratio <= n^3/50^(n-1)
using exp(4)>50 (finite positive series). W_0=0.
Let c_i=(-1)^i binom(33,i). Then (c^T A)_j =
sum W_n X_n^j(1-Y_n)^33, all nonnegative.
For n<=50 the factor is <=(1/225)^33 by 1-exp(-x)<=x.
For n>=51 bound the factor by 1 and use the ratio majorant
n^3/50^(n-1), whose consecutive ratio <=1/40.
Therefore (c^T A)_j <= B A_0j, B=225^-33+(40/39)*51^3/50^50.
Since ||c||_2^2=binom(66,33), ||A||_2>=max_j A_0j,
sigma_min(A)<=sqrt(34)*B*||A||_2/||c||_2.
Exact rational replay establishes kappa_2(A)>10^86 if A is invertible.
No approximation to the choice-defined bump enters.

## Reselect pivot and surplus
Cells 630..663 and preceding surplus cell 629 are all eligible. Their
pivot support-to-collar gaps lie between 829/532000 and 8781/76000.
Shifted response matrix A' has weights W'_n=W_n X_n^629 and exponents
0..33. Strict determinant orientation follows from the same E18P infinite
transfer, provided the corresponding E18O series is attached.
This is not a claim that the near pivot has a certified favorable condition number.

The preceding cell response b' has exponent -1 relative to A'.
In a finite Cauchy-Binet truncation, each ordered tuple of 34 distinct
nodes X_n with positive weights contributes a determinant with identical
orientation. Cramer's numerator with column j replaced by b' is the same
weighted sum times the coefficient of x^j in the interpolation polynomial
for 1/x at those tuple nodes:
P(x)=(1-prod_l(1-x/X_l))/x.
Its coefficient is (-1)^j e_{j+1}(1/X_1,...,1/X_34).
Since all X_n>1, the signed coefficient is between zero and binom(34,j+1).
Thus the finite Cramer ratio is a positive weighted average of such
coefficients. Entrywise series convergence and nonzero limiting determinant
give the same bound for the infinite response system:
0<=(-1)^j (A'^-1 b')_j<=binom(34,j+1).
In particular ||A'^-1 b'||_1<=2^34-1=17179869183 and max coefficient
<=2333606220. This is a coefficient enclosure, not an entrywise inverse
bound. It is specific to a preceding-cell surplus; it does not apply
to arbitrary right-hand sides or the original later surplus cell 37.

The corrected rough vector is f_629-sum_j c_j f_(630+j), nonzero by
disjoint interiors and nonzero f_629. Base rows vanish by literal individual
cell mean and pole moments, and separation from packed carrier. The
response rows vanish by the exact equation A'c=b'. Carrier admission,
base rows and determinant attachment still need native verification.
The corrected combination can be smoothed directly with E19C full
observation rather than independently smoothing every column and paying
the large coefficient l1 amplification. This is a candidate single
kernel direction, not a complete E16 trial solve or residual enclosure.
