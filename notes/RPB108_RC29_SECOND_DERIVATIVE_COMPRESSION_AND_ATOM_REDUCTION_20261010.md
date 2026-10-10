# RPB108 RC29 — second-derivative compression and exact Cauchy atom reduction

2026-10-10. Independent research/rpb108-route-consolidation.
Parent recovered: ae3a13562844f84c8f3f09c3136ca248f36e83fe (RC28).
Other branches and historical reports are unchanged.

## Result

The positive-mixture approximation needs only 1000 atoms, down from
210000, with a stronger supported whole-operator error:

    Q_29 - (9/62500) I <= K_B
       <= Q_29 + (109/500000) I,
    ||K_B-Q_29|| < 1/4000.

This follows from a uniform integrated second-derivative bound rather
than the first-derivative bound used in RC28. The polynomial atom
integrals reduce exactly to logarithm/arctangent and a recurrence.
All 36 upper-triangle overlap polynomials for the first eight physical
Legendre modes have been assembled in rational arithmetic.

These are actual algebraic integration data. The transcendental atom
integrals and complete metric matrix remain unevaluated.

## Uniform second-derivative estimate

RC28's logarithmic integrand is

    g_u(s)=exp(-u exp s)-exp(-(u+e)exp s), u>=0.

For lambda>0 put f_lambda(s)=exp(-lambda exp s).
Writing z=lambda exp s gives

    f_lambda''(s)=(z^2-z)exp(-z),
    integral_R |f_lambda''(s)|ds
      =integral_0^infinity |z-1|exp(-z)dz=2/e.

The last integral is elementary: integrate separately on (0,1)
and (1,infinity), using the antiderivative -z exp(-z) of
(z-1)exp(-z). For lambda=0 the second derivative is zero.
Thus, uniformly including u=0,

    integral_R |g_u''(s)|ds <=4/e<2.

For a midpoint bin of length h, the integration-error functional
annihilates constants and linear functions. Its Peano kernel is
(x-left)^2/2 on the left half and (right-x)^2/2 on the right half;
the maximum is h^2/8. Direct twice-integration of g'' gives
absolute bin error <=(h^2/8)integral_bin |g''|.
Summing bins gives uniform multiplier error <h^2/4.
This proof uses no sampled frequency cutoff. Plancherel and interval
compression give the corresponding whole-operator norm bound.

## Concrete approximation

Use delta=1/100000, T=100000, N=1000. Define Q_29 exactly as in RC28,
with h=log(T/delta)/N, geometric midpoint t_j, and weights
h t_j(1-exp(-e t_j)).
The rational exponential-series control proves log10<7/3.
Hence log(T/delta)=10log10<70/3<24 and h<24/1000.

    quadrature error <h^2/4<9/62500,
    small-t tail <3/100000,
    large-t tail <=11/250000,
    total upper error <109/500000<1/4000.

Both tails are positive operators, so only the quadrature error enters
the lower enclosure. Q_29 is positive. As in RC28, a finite sum of
Cauchy operators is not itself finite rank on interval L2.

## Exact polynomial reduction of each atom

Let p_i(x)=P_i(x/B), B=11/10, R=2B. For r in [0,R] define

    O_ij(r)=integral_(-B)^(B-r)
       [p_i(x)p_j(x+r)+p_j(x)p_i(x+r)] dx.

Since the polynomials have rational coefficients, O_ij is an exact
rational polynomial of degree at most i+j+1. Splitting the square
integration region along its diagonal proves

    <p_i,C_t p_j>=2 integral_0^R
                          O_ij(r)/(t^2+4pi^2 r^2) dr.

This counts both triangles. In particular O_00=2(R-r), not R-r.
Odd i+j gives O_ij=0 by reflection.

For c=2pi and I_p(t)=integral_0^R r^p/(t^2+c^2 r^2) dr,

    I_0=atan(cR/t)/(ct),
    I_1=log(1+(cR/t)^2)/(2c^2),
    I_p=R^(p-1)/(c^2(p-1))-(t^2/c^2)I_(p-2), p>=2.

The recurrence is proved by exact polynomial division. If
O_ij=sum o_p r^p, the atom entry is 2 sum o_p I_p.
The matrix Q_29 is then the finite weighted sum of these exact entries.
No two-dimensional singular integration remains in this representation.

The recurrence can suffer numerical cancellation when t is large.
An accurate implementation needs interval arithmetic with sufficient
precision or an alternative convergent expansion; exact formulas alone
are not a floating-point error certificate.

## Data, validation, and interface

scripts/validate_rpb108_rc29_atom_reduction.py computes all 36
upper-triangle overlap rows for eight modes.
certificates/rpb108_rc29_overlap_polynomials.json stores the executed
rational output and evidence flags. The polynomial coefficients are
ordered by increasing power of r.

Executed locally: PASS, 212 exact rational checks.
They verify the budget, symmetry, endpoint value, diagonal physical
mass, parity, integrated overlap identity, and polynomial-division
recurrence controls. The uniform derivative and midpoint theorem are
analytic proofs above.

For any polynomial trial mass matrix D, replace I by D in the
enclosures. Combining with RC26's scalar enclosure gives

    L_RC26+Q_29_trial-(9/62500)D <= G
      <= U_RC26+Q_29_trial+(109/500000)D.

The scalar error and any certified transcendental/entry evaluation
error must still be included; they have not disappeared.
The 1000-atom cost does not reduce the separate 8600-feature native
head and does not identify physical polynomials with canonical Riesz
representatives.

Next: enclose the transcendental atom entries, assemble the complete
low-mode physical metric, and then attempt a trial Riesz solve with
whole weak residual bounds. No complete metric, Riesz inverse, native
head positivity, source leakage, aperture extension, RH/F4 theorem,
or Lean closure is claimed.
