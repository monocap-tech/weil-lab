# Stop the fixed-4096-bit global monomial implementation

Parent PR #340 / 0d6ea85d21f631e02ab2e6f4803bf2f02d3c1c57.
Live manifest: W-ODD-NEG remains OPEN. No governance or acceptance change.

## Decision and stopping point

Do NOT enlarge the moment table and assemble a dense global monomial arch
matrix with independently evaluated 4096-bit raw Taylor coefficient balls.
The bounded feasibility test identifies a necessary actual-source subproblem
that this representation cannot certify. No large integration, precision
campaign, D regeneration or polynomial matrix assembly was launched.

This is an implementation-specific stop. It does not rule out Chebyshev,
local panels, exact symbolic coefficient dependence, direct oscillatory
integration, higher precision with a new measured cost plan, or the original
operator inequality. The scalar kernel certificates in #340 remain valid.

## A necessary degree for the ACTUAL normalized trial space

The accepted original source list contains k=0 at c=113013/128=882.9140625:
j(x)=sin(2*pi*c*x), on [-B,B], B=11/10. This is not a newly added direction.
U=JD spans the whole original J470, so j=Uv for an exact coefficient vector v.
The accepted U*U >=99/100 I implies

    ||v||^2 <= ||j||_L2^2/(99/100) <= 2B/(99/100) <9/4.

Thus a degree-d polynomial approximation to the normalized trial frame with
uniform coefficient-operator error <=1/3 would approximate this j uniformly
with error <1/2. (The same conclusion holds if only U is approximated.)
No actual D regeneration or giant coefficient-norm estimate is required.

There are 1942 positive extrema x=(2k+1)/(4c) inside [0,B], and their 1942
negative reflections. Their signs alternate. A polynomial with uniform error
<1/2 must have these same signs, hence at least 3883 distinct real roots
between successive extrema. Consequently d>=3883. This is a rigorous
necessary degree for this UNIFORM GLOBAL POLYNOMIAL approximation goal,
not a lower bound for every possible operator/form approximation method.

## Raw Taylor sufficient degree and cost

For the raw sine, the real-variable Taylor/Lagrange estimate at |x|<=B is

    remainder <= t^(K+1)/(K+1)!, t=(44/7)*B*c >2*pi*B*c.

The first odd K for which this particular upper bound is <2^-80 is 16643.
The preceding odd degree fails that UPPER-BOUND test. We do NOT assert that
16643 is the minimal true approximation degree. Nor is this a normalized
484-function remainder bound: normalization may demand additional accuracy.

A universal odd monomial space through degree 16643 has dimension 8322,
69,255,684 dense Gram entries (34,632,003 independent symmetric entries).
These are exact entry counts, not a measured runtime or a memory lower
bound. The current 128 scalar moments cover only polynomial degree 63;
they do not make this actual-source assembly inexpensive.

## Fixed-precision interval-box ceiling

At native precision 4096, construct the actual source's Taylor coefficient
at odd degree k=6105:

    a_k = (2*pi*B*c)^k/k!.

Its true sign is irrelevant to the radius. The pinned python-flint 0.8.0
native computation retains its full dyadic midpoint and radius. Exact
stdlib replay verifies that the radius is strictly greater than 2^4700.
At x/B=1, a sum or Horner evaluation that regards coefficient intervals as
independent must contain the full interval width contributed by this ONE
coefficient. Such an interval-box evaluation cannot certify unit error,
even though the true sine is bounded by one. This is a representation and
lost-dependence obstruction, not an assertion of uncertainty in pi itself.
Using analytic dependence on pi, different polynomial coordinates, a factored
representation, or substantially more precision changes this method and is
outside the scoped ceiling. The result does not establish the least working
precision for any of those alternatives.

## Custody and next decision

The workflow checks accepted run 40417043904, source
0e3321350980247f8cba46cdbb45b717e49ad213, artifact 12694539474, archive digest
and BOTH exact native-projection/full-frame input hashes. The bounded native
check runs in under a second locally. Exact replay checks source extrema,
the coefficient-norm implication, degree inequalities, dense counts, and
the retained radius. Native ball generation, exact replay and analytic
reasoning have separate standing; no independent domain review is claimed.

A subsequent attempt must change the representation and show an actual-source
approximation error AND bounded measured cost before a large matrix run.
This scoped stop is the promised feasibility outcome, not permission to
keep increasing degrees, scalar moments or arithmetic precision by default.
The original arch mixed matrix, complete Astar projection, matched forcing,
inverse response and W-ODD-NEG remain UNCOMPUTED / OPEN. Inherited domain,
even/CC27/Weil/RH obligations remain OPEN. Draft/unmerged.
