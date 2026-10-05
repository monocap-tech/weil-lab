# RPB108: exact boundary scaling and the limit of norm-only collar estimates

Base: b3dc9e56d29c2ace138a04fa9b71c6ca50dbdb65.
Definitions: docs/TERMINOLOGY_RPB108_BOUNDARY_SCALING.md.

## Result and scope

The actual exterior archimedean operator is a half-Carleman operator plus a Hilbert-Schmidt remainder. Its scale-invariant singularity survives in the actual exterior residual on vectors concentrated at the support edge: the finite prime shifts miss a sufficiently small collar and the pole contribution vanishes after scaling. Consequently the exterior residual map into any fixed collar is noncompact in the physical L2 norm.

These are statements about the actual kernel on arbitrary carrier vectors, not hypothetical weak-null vectors. They identify a limitation of norm-only estimates; they do not exclude stronger estimates derived from the mixed null equation. No endpoint or nonzero null vector is asserted to exist.

## Exact decomposition, with a global remainder bound

Fix a>0, L=2a and k(s)=exp(-s/2)/(1-exp(-2s)). On the right exterior half-line use x=a+u, y=a-v, with u>0 and 0<v<L. Set

    H_k f(u)=integral_0^L k(u+v)f(v)dv,
    C_L f(u)=integral_0^L f(v)/(u+v)dv,
    r(s)=k(s)-1/(2s).

Then H_k=(1/2)C_L+H_r. The elementary inequalities 1-exp(-2s)<=2s and exp(2s)-1>=2s give

    k(s)>=exp(-s/2)/(2s),
    k(s)<=exp(-s/2)+1/(2s).

Since 1-exp(-s/2)<=s/2, we have -1/4<=r(s)<=exp(-s/2), hence |r(s)|<=1 for 0<s<=1. For s>=1, positivity of k and the upper bound also give

    |r(s)|<=exp(-s/2)+1/(2s).

The area of {u>0,v>0,u+v<=1} is 1/2. On its complement use (b+c)^2<=2b^2+2c^2 and integrate first in s=u+v. This proves

    integral_0^L integral_0^infinity |r(u+v)|^2 du dv
      <=1/2+L[2/exp(1)+1/2] <1/2+5L/4,

where exp(1)>8/3. Thus H_r is Hilbert-Schmidt, in particular compact, from L2(0,L) to L2(0,infinity). No pointwise series truncation or support gap is used.

## A lawful boundary concentration sequence

For 0<epsilon<L/2 define

    h_epsilon(y)=epsilon^(-1/2) 1_[a-2epsilon,a-epsilon](y).

It has physical L2 norm one, belongs to D_a, and converges weakly to zero in physical L2. Weak convergence follows from absolute continuity of the L2 integral on its shrinking support. Its edge profile is epsilon^(-1/2)1_[epsilon,2epsilon](v).

For 1<=t<=2 the scaled archimedean output is

    sqrt(epsilon) H_k f_epsilon(epsilon t)
      =integral_1^2 epsilon k(epsilon(t+z))dz
      -> (1/2)integral_1^2 dz/(t+z)
       =(1/2)log((t+2)/(t+1)),

uniformly in t. Uniformity follows directly from the bounded remainder: epsilon r(epsilon(t+z))->0. The limiting function is nonzero. This proves noncompactness of H_k, as well as of the leading truncated-input Carleman operator.

## Prime and pole terms cannot cancel this boundary scaling

Use the previously derived exact exterior formula q_h=p_h-H_k f minus the frozen finite prime translations, including prime threshold equalities. If 4epsilon<log(2), then at x=a+epsilon t, 1<=t<=2, every prime translation vanishes almost everywhere: x-log(n) could meet the support only if log(n)=epsilon(t+z), 1<=z<=2, and x+log(n) is outside the support. No assumption about the size of a or the number of frozen prime terms is needed.

The two pole moments satisfy |M_pm(h_epsilon)|<=sqrt(epsilon) exp(a/2). Consequently

    |sqrt(epsilon) p_h(a+epsilon t)|
      <=2epsilon exp(a+epsilon),

which tends to zero. Therefore sqrt(epsilon) q_h(a+epsilon t) converges uniformly, with the negative sign, to the same nonzero half-Carleman profile. This argument uses the full actual exterior dictionary, not an abstract substitute kernel.

Here is a rational lower constant, avoiding asymptotic ambiguity. If

    epsilon<=1/8, 4epsilon<log(2),
    epsilon<=exp(-(a+1))/64, epsilon<L/2,

then exp(-epsilon(t+z)/2)>=1-2epsilon>=3/4, and

    sqrt(epsilon) H_k f_epsilon(epsilon t)>=3/32,
    |sqrt(epsilon) p_h(a+epsilon t)|<=1/32.

The reverse triangle inequality gives

    integral_(a+epsilon)^(a+2epsilon) |q_h(x)|^2 dx >=1/256.

For any fixed delta>0, eventually this interval lies in (a,a+delta). The residual map to L2(a,a+delta) is bounded: the archimedean bound was proved previously, prime translations are bounded and the pole is finite rank on a bounded collar. A compact operator sends a bounded weakly zero sequence to a norm-zero sequence. The displayed lower bound therefore proves this actual residual map is noncompact in physical L2. The pole is compact there; the finite translations need not be compact, but they miss the scaling interval, which is the argument actually used.

## What logarithmic normalization changes

Use the existing Fourier convention exp(-2pi i xi y) and w(xi)=log(exp(1)+|xi|). For f=1_[1,2], |Fourier(f)(xi)|<=min(1,1/(pi|xi|)). On |xi|<=1, w<2; on |xi|>=1, w<=2+log|xi|. Since pi>3,

    Elog(f)<4+(2/9) integral_1^infinity (2+log t)/t^2 dt
            =14/3<5.

Fourier scaling and w(eta/epsilon)<=w(eta)+log(1/epsilon), for epsilon<=1, imply

    Elog(h_epsilon)<=5+log(1/epsilon).

Let v_epsilon=h_epsilon/sqrt(Elog(h_epsilon)), so its actual logarithmic carrier norm is one. The actual residual still satisfies

    integral_(a+epsilon)^(a+2epsilon) |q_v(x)|^2 dx
      >=1/[256(5+log(1/epsilon))].

It follows that, for no alpha>0 and finite C, can all unit-logarithmic-norm carrier vectors satisfy the uniform shrinking-collar estimate

    integral_a^(a+2epsilon) |q_h(x)|^2 dx <= C epsilon^alpha.

This does not conflict with compactness of the embedding D_a into physical L2. It gives a logarithmic lower rate along a particular sequence, not a positive norm lower bound after logarithmic normalization. In particular it is not a counterexample on the finite-dimensional actual weak-null subspace. The Gaussian signed pairing has an oscillatory test and is a different quantity; no implication from this squared collar norm to that pairing is claimed.

## Consequence for the active endpoint route

The boundary regularity result at the base commit is valid, including the derived multiplier L2 domain and M_R=O((log R)^(-2)). Regularity and carrier norms alone cannot make the boundary residual small by a power of collar width, because the actual singularity just exhibited remains. Any successful exponential signed Gaussian estimate must use additional consequences of full mixed nullity or specific cancellation in the signed pairing. Replacing k by a bounded kernel or invoking compactness in physical L2 would be invalid.

The accompanying exact-rational certificate checks the lower constants, Hilbert-Schmidt budget coefficients, logarithmic energy budget and a negative control that drops the singular term. The operator, Fourier scaling and noncompactness arguments are analytic proofs, not mechanically checked or Lean formalized. The numerical aperture frontier remains 81/100. Global endpoint exclusion, retained selected-witness attachment, F4 and FULL TRANSPORT CLOSED remain open. Lean, axioms and CI unchanged.
