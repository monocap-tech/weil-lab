# Native prime recurrence tail (CC39)

Use CC33's complete original native remainder and CC38's Fourier coordinate
with modulation exp(2*pi*i*xi*x). On the fixed cap D_B define the actual
prime multiplier

    p_B(xi)=-2 sum_(log n<=2B) Lambda(n)/sqrt(n) cos(2*pi*xi*log n).

Prime powers of zero coefficient may be omitted from this displayed finite
sum only because Lambda(n)=0. Both translation orientations remain included.

For R>=1, C_prime,>R is the canonical operator of the multiplier
p_B(xi) 1_(|xi|>R), compressed to the supported logarithmic domain.
It is an error decomposition, not a truncated explicit formula.

A prime recurrence sequence is an unbounded positive sequence of integer
frequencies xi_j such that exp(2*pi*i*xi_j*log n)->1 for every active term.
The native prime tail has upper rate O_B(1/log R), and CC39 proves a matching
lower rate along such a sequence whenever 2B>log2. This statement concerns
the prime remainder on the whole carrier, not near-critical source lifts.
