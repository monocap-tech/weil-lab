# RPB108: certified positive weighted prime Schur test at 19/20

The actual combined prime translation operator on I=(-19/20,19/20) is

    Tf(x)=sum A_n [1_I(x+log n)f(x+log n)+1_I(x-log n)f(x-log n)],

for n=2,3,4,5 and A_n=Lambda(n)/sqrt(n), with Lambda(4)=log(2).
It is bounded, self-adjoint and has a nonnegative translation kernel.
Positive semidefiniteness of T is not assumed.

The auxiliary weight w is an exact rational, positive piecewise-constant
function on the 441 coarse cells of the certified tenth-power support
partition. Its minimum is 745503259/125000000000>0 and its maximum is 1.
It is bounded and bounded away from zero. It is not a native-domain vector,
an eigenvector, or a positivity witness for the full native form.

Every source-weight cut, every support boundary, and every target-weight cut
pulled back by an actual translation is covered by a 533-cell refinement.
The constructor uses the next reachable-displacement layer; the independent
audit instead pulls back every actual coarse cut by each of the eight
translations. Extra refinement cuts are harmless. Exact strict logarithm
enclosures isolate all cuts. On each open refined cell, source and target
weights and support predicates are constant. The finite set of boundary
points, including its translated preimages, has measure zero.

The exact pointwise assertion is Tw<=b w almost everywhere, where
b=35037/20000. Every amplitude uses a checked rational outward ceiling;
all 533 rational weighted row sums are verified. This implies ||T||<=b.
For completeness, weighted Cauchy-Schwarz gives

    |Tf(x)|^2 <= (Tw)(x) sum_s A_s 1_I(x+s)|f(x+s)|^2/w(x+s).

Integrating and changing variables in each paired translation gives

    ||Tf||^2 <= b integral |f(y)|^2 (Tw)(y)/w(y) dy <= b^2 ||f||^2.

Self-adjointness and the identical paired amplitudes justify the middle
step. Thus the bound controls both signs of T, as required for prime loss.
Float iterations only locate the rational weights; no floating-point value
is used as proof evidence. A smaller pointwise bound is rejected for this
same stored weight using independent lower amplitude bounds. That control
is not an operator-norm lower bound.

Replacing the separated prime loss in the pinned fresh two-band complement
with b leaves the complete archimedean masses, pole and logarithmic bounds
unchanged and gives 0.8843682322149314...>221/250. This stronger scalar
bound is checked against the same complete fresh 84-vector Gram. The prior
399/500 scalar obstruction remains valid and immutable; its positive native
energy was never a negative full-form witness.

Whole-domain promotion requires all 84 corrected pivots with the actual
source correction delta=eta(2M+eta), exact lift/physical conversion and fresh
logarithmic conversion. F4, global endpoint exclusion and Lean formalization
are separate claims and are not supplied by this weighted prime test.
