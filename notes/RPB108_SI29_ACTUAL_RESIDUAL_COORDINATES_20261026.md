# Actual SI29 Hermite-residual coordinates and certified series evaluation

## Scope

This constructs a rational candidate coordinate system for the ACTUAL
fourteen continuous SI29 features after subtracting their original
Hermite-106 interpolants. It supplies exact Taylor data and rigorous
finite-series truncation bounds in the original operator norms.
It does not compute the full-J470 energy projection, its Schur T,
the matched forcing, or the inverse response. No positivity count is used
as evidence of global odd positivity.

The workflow first replays the existing original SI10/Hermite validator:
15 original cluster centers with multiplicities totaling 106, all 470
original generators, and all 14 true continuous feature definitions.
Then it constructs the new coordinates with exact Fraction arithmetic.

## Exact residual coefficient generator

Let W(eta)=product_j(eta-c_j)^p_j, degree N=106, and I_N the confluent
frequency-Hermite interpolant. For every nonnegative integer k,

    eta^k - I_N(eta^k) = eta^k - (eta^k mod W).

For a mean feature, the frequency moment is
[(c+r)^(k+1)-(c-r)^(k+1)]/[2r(k+1)].
For a first-moment feature, integrate 3*(eta-c)/r against the same
normalized interval measure. The first two moments are checked exactly.
The generator computes remainders by repeated multiplication modulo W,
then integrates the monomial residual exactly.

For E=F-J*C_Hermite, the first possible odd spatial powers are
107,109,... . The coefficient of x^k in E_j is

    (-1)^((k-1)/2)*(2*pi)^k/k! * M_kj,

where M_kj is the exact band integral of the monomial residual. No nearly
equal sine functions are evaluated and subtracted in floating arithmetic.

The first 14 such coefficient rows, powers 107 through 133, have exact
rank 14. This is checked by modular elimination and an explicit rational
inverse witness. For the first row, the independent polynomial identity
eta^107-I_N(eta^107)=W(eta)*(eta+sum_j p_j*c_j) is also checked.

## Candidate coordinates

An invertible rational U is constructed so that

    M U = diag(s_k),
    s_k=(-1)^((k-1)/2)*k!/(2*pi_up)^k, pi_up=22/7.

For G=E U, the first 14 nontrivial physical Taylor coefficients are
diagonal, with positive diagonal (pi/pi_up)^k in (9/10,1). Thus the
actual G_j have distinct leading powers 107,109,...,133 and are linearly
independent as physical analytic functions.

This is a Taylor-jet normalization, NOT an energy-conditioning
certificate. The transformation has large coefficients. It must not be
treated as proof that the projected energy Schur is well-conditioned,
or that G is independent modulo the ENTIRE original J470 space.

## Certified finite-series representation

The module residual_jets(nodes,features,max_degree) generates the exact
frequency coefficients for any finite truncation. U and the known
physical Taylor factors then define the corresponding polynomial P_K.

For the original Hermite error ceiling eps_j<1e-21, the frequency
monomial remainder theorem gives a uniform series-tail bound using

    lambda=2*pi_up*B*15,
    |G_l-P_K,l| <= sum_j |U_jl| eps_j *
                     sum_(n>=K+1-N) lambda^n/n!.

The derivative tail gains (N+n)/B. Both sums have exact geometric
majorants after their first retained term. Use K=639 and compact the
column weights UPWARD to finite integer bounds. This proves, for all
14 candidate coordinates on [-11/10,11/10],

    sup |G_l-P_639,l| < 1e-95,
    a_star[G_l-P_639,l] < 1e-180,
    ||Astar(G_l-P_639,l)||^2 < 1e-180.

These are coarse certified ceilings, not decimal quadrature diagnostics.
The full degree-639 polynomial coefficient array is not materialized in
this artifact; the exact generator defines and can construct it on demand.
The saved witness contains the first coefficient matrix, U, and all
uniform/function-derivative/action tail bounds.

The original Ao estimates used are: a_o<=36 on |xi|<=1 and
a_o<=17+ln|xi| beyond 1. For an error with sup e and derivative sup e',
zero-extension variation is at most V=2e+2B e'. Consequently

    a_star[error] <=36*(2B)*e^2+V^2,
    ||Ao error||^2 <=36^2*(2B)*e^2+(325/18)*V^2.

Since Astar=Ao-2|s><s| and ||s||^2=sinh(11/10)-11/10<1,

    ||Astar error||^2 <=2||Ao error||^2+8*(2B)*e^2.

The workflow separately checks the pole-norm ceiling and all exact
arithmetic. The original Fourier normalization, closed-domain realization,
and multiplier inequalities remain inherited analytic premises.

## What the next response calculation must compute

Let A=Astar, E=F-J*C_Hermite and AJ=J^* A J. The ACTUAL feature Schur is

    T=E^* A E - E^* A J AJ^-1 J^* A E.

For the same full original Galerkin residual R0 with J^* R0=0,
h=F^*R0=E^*R0. Under the invertible candidate transform U,

    T_G=U^* T U, h_G=U^*h,
    h_G^* T_G^-1 h_G = h^* T^-1 h

when the inverse is justified. Otherwise rank/kernel compatibility must
be certified. The matrix T is not simply E^*AE. Neither exact residual
independence nor tiny approximation errors remove the full J470
projection or establish a positive lower bound for T_G.

The new representation removes raw subtraction of nearly equal physical
features from the evaluation problem. It provides no evaluated full
projected response, MG07 feasibility pass, or signed Schur closure.
The original auxiliary reference operator must retain its matched
covariance when trial coordinates change.

W-ODD-NEG, independent original analytic/domain review, even/CC27/Weil
and RH remain OPEN. No canonical acceptance condition is changed.
