# Selective original constraint pruning for a fixed BS tail target

Weil-Lab, 2026-10-27. Continues draft #349 at
`595f962e3e5abd4bd8ca454bfc88cd619c0fab90`. Draft/unmerged.

## Outcome and stopping point

For the SAME original Birman–Schwinger operator, select a SUBSPACE of the
original J470, retaining 241 original sine/cosine derivative constraints
and the original true pole. Exact rational arithmetic proves

    rank(J_selected)<=242,
    lambda_243(B_true)<1/2.

The actual certified upper is 0.4987321363773265... . Combined with the
accepted lambda_4>1-3e-12, the number of eigenvalues above 1-3e-12 is now

    4 <= critical count <=242.

This reduces the previous ceiling 470, not the proved lower count four.
It does not assert that 242 modes are critical or that four suffice.
All 107 original clusters and 3892 SM40 cells remain PAID, including 40
clusters with zero retained derivative constraints. No frequency region,
negative multiplier contribution, pole or physical endpoint is dropped.

STOP after this single fixed-target rank-allocation test and GitHub replay.
No finite source inversion, original native integration, reduced Gram,
BS block, mixed Schur or source-positivity calculation is started.
The next gate is the complete finite/mixed Schur on a valid frame, or a
legitimately sharper spectral count. Do not automatically prune toward a
new target or launch dimension-by-dimension tests.

## The trade-off, not a uniform replacement

#349 retains rank<=470 with an extremely small tail <0.00002431, using
the complete J470 compressed inverse comparison. The present pass uses a
smaller deflation space with a WEAKER tail <1/2. Both certificates remain
valid; neither pair uniformly dominates the other. The smaller rank can
reduce the size of a future finite gate, but its mixed-error allocation
is less favorable. No runtime, conditioning or algorithm-size optimum
has been certified. A rank ceiling is not a required inversion size.

The declared target is 1/2. The algorithm is a deterministic exact greedy
allocation for this one target and one family of local Fourier bounds.
The rank 242 is NOT claimed globally minimal, even within the original
family. Numerical exploratory estimates do not enter acceptance.

## Same original source functions and a smaller auxiliary space

The native input lists 107 exact original centers c_j and their original
multiplicities p_j, totaling 469 trigonometric generators. At center c_j,
retain the FIRST n_j original derivative generators, 0<=n_j<=p_j, along
with the true sinh pole. These are existing original functions, not new
candidate sources or an endpoint-aligned surrogate.

Let Q_selected be physical orthogonal projection onto this selected span's
complement. It is mathematically defined; no numerical projection is
computed. For every odd physical f with Q_selected f=f,

    fhat^(k)(c_j)=0 for k=0,...,n_j-1.

The implication follows directly from the original compact-support Fourier
derivative generators. For any p<=n_j and a real frequency xi, Taylor's
integral remainder and physical Cauchy–Schwarz give

    |fhat(xi)|^2
       <= [2B/(2p+1)] * [(2*pi*B*|xi-c_j|)^p/p!]^2 ||f||^2,
    B=11/10.

For p=0 this is the unconditional pointwise Cauchy bound 2B||f||^2;
it requires no zero. Use 2*pi<44/7 and bound |xi-c_j| by its maximum on
each exact original SM40 subcell [a,b]. Multiply by 2*(b-a)*w40 to pay both
frequency signs. The original w40 already includes the correct kappa shift.

This bounds the entire operator on an arbitrary complement vector, not
only fourteen SI29 features or individual source diagonals. There is no
frequency integration, Fourier sampling or source polynomial approximation.
The finite Taylor expression is an analytic remainder bound for a Fourier
ROW, not an approximation of the high-frequency physical source family.

## Exact local costs and selective removal

Partition all original SM40 subcells into their 107 contiguous components.
Their exact centers agree with the matched native original centers.
For cluster j and available multiplicity n, form

    C_j(n)=min_(0<=p<=n) sum_(cells in j)
       2*(b-a)*w40 * [2B/(2p+1)]
       * [((44/7)*B*max(|a-c_j|,|b-c_j|))^p/p!]^2.

Every C_j(n) is an exact nonnegative rational. Taking the minimum permits
using fewer Taylor zeros when that bound is better and makes C_j(n)
nonincreasing with n. The exact two-sided envelope mass is checked against
1073441879/64000000. No extra reflection factor is applied.

Start with all original multiplicities. At each step, among legal deletions,
choose the smallest exact increase

    C_j(n_j-1)-C_j(n_j),

breaking ties by cluster index. Accept a deletion only while the COMPLETE
sum remains strictly below kappa_star/2. Stop at the first minimum deletion
which does not fit. All 228 deletions and exact cumulative sums are retained.
The replay verifies each chosen increment against every legal increment.
That verifies the greedy trace, not a global rank optimum.

The resulting selected sum is

    epsilon_selected=sum_j C_j(n_j)
       =1.6767873157142093...e-5 <kappa_star/2.

Forty clusters retain n_j=0. Their cost is STILL strictly positive:
the full local mass times 2B. These bands are paid by unconditional Cauchy
bounds; they are not declared positive, ignored or removed from the operator.
The code and independent replay check all 3892 original subcells explicitly.

## Correct inverse bound for the SMALLER physical complement

The full-J470 bound Q470 Astar^-1 Q470 approximately <=1000 Q470 does NOT
transfer automatically to the larger selected complement. Its SI29 feature
projection error was certified for the full J470, not this selected subset.
Retaining the pole alone does not supply that missing comparison.

This pass instead uses ONLY the inherited GLOBAL original coercivity

    Astar>=kappa_star I, kappa_star=33621/10^9,
    Astar^-1<=kappa_star^-1 I.

It includes the original pole correction. No kappa=1/1000 floor is silently
upgraded or transplanted. Consequently

    Q_selected Kminus Q_selected<=epsilon_selected Q_selected.

The original envelope is used solely to upper-bound compressed negative
action. No stopped global Astar>=E40 or Astar>=Enew comparison is reopened.

## Complete BS tail and count transfer

Define S_selected=range(Kminus^(1/2) J_selected), Pi_selected the orthogonal
projection onto this finite-dimensional space, and R=I-Pi_selected. The
square root is of the ACTUAL supported physical operator Kminus, not a
compressed frequency square root. rank(Pi_selected)<=242.

For v perpendicular to S_selected, y=Kminus^(1/2)v lies in Q_selected H.
The exact norm identity ||Q_selected Kminus^(1/2)||^2=
||Q_selected Kminus Q_selected|| therefore gives

    <v,B_true v>=<y,Astar^-1 y>
       <=kappa_star^-1 ||y||^2
       <=t_selected ||v||^2,
    t_selected=epsilon_selected/kappa_star
              =0.4987321363773265... <1/2.

Thus R B_true R<=t_selected R on the COMPLETE original Hilbert carrier.
Min-max yields lambda_243(B_true)<=t_selected<1/2. All infinite couplings
are respected in this codimension argument. No finite-section eigenvalue,
physical projection/inverse commutation or inverse of a compression is used.

The accepted lower lambda_4>1-3e-12 then gives the count interval 4..242.
Neither the four trial vectors nor the actual critical spectral subspace
are claimed to lie literally in S_selected. Spectral vectors can have
components on both sides; their coupling is the remaining Schur problem.

## Remaining full finite/mixed gate

On S_selected plus its orthogonal complement, write

    B_true=[[H,D],[D*,C]], C<=t_selected I< I/2.

The exact positivity condition is still

    I-H-D(I-C)^-1 D*>=0.

The inverse of I-C is bounded above by 1/(1-t_selected)<2. H, D and the
Schur value are uncomputed. A generic sufficient threshold H<=(1-t_selected)I
is recorded but not certified and may be conservative. Separate diagonal
positivity or a finite inverse solve is not a substitute for the full mixed
gate. The reduced physical Gram and its conditioning require their own
control before any future numerical solve.

## GitHub custody and independent replay

Parent #349: successful run 40547751923, source
595f962e3e5abd4bd8ca454bfc88cd619c0fab90, artifact 12752629674,
archive SHA256 030a07bb1b93208d22567fc51de3ef0810be930adf6e253714de58a344946f20.
Its result JSON SHA256 is
931e5c64db19b28201ce96958495a8bfd8337eb7ebe08096466d86db29a1f801.

The same retained archive contains the matched native J input (c9ee487f...)
and original envelope input (19af532b...), plus the prior reference and
critical-block inputs needed to replay #349. The focused workflow verifies
the successful run/source/artifact/archive chain and all FIVE exact JSONs,
replays #349, computes the new exact allocation and independently verifies
every local Taylor cost, chosen proof order, subcell payment, removal and
operator/count constant. New composition and replay each take under a second
locally; no native projection, integration or eigensolver is repeated.

Native-input validity, the analytic Fourier/operator proof and independent
original domain review retain separate standing. W-ODD-NEG, exact critical
count, complete finite/mixed signed Schur, global true BS norm <=1 and
independent original-domain review remain OPEN. Even/CC27/Weil/RH unchanged.
No manifest acceptance/status change. Draft/unmerged.
