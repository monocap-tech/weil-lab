# RPB108 RC22 — Chebyshev moment head and canonical matrix interface

2026-10-10. Independent route consolidation.
Parent: 2d3b6ca6e346280def5258ccc7d7a627c9b6180d (RC21).
Only research/rpb108-route-consolidation is written.

## Result

A contour-controlled Chebyshev approximation of the actual Fourier
kernel reduces the explicit sufficient head from 23000 to 8600 features.
Its entire complementary original-form floor remains

    247/2500 >1/11.

For this head, actual canonical head floor >=1/4000 and actual source
cross norm <=1/300 would pay a Schur reserve >=1223/8892000.
Neither actual condition is certified here. The canonical projection
and finite matrices are not computed.

The head is explicitly defined by bounded Chebyshev moment functionals
and their canonical Riesz representatives. The remaining acceptance
conditions are also expressed below as matrix inequalities in the exact
canonical Gram metric, with no prior orthonormalization requirement.
This is an analytic finite-space reduction and matrix interface, not
original positivity at 1.10 or a practical implementation.

## Carrier and original-form input

Use the supported logarithmic carrier D_B at B=11/10, physical inclusion
i:D_B -> L2(-B,B), ||i||<=1, and Fourier convention exp(-2pi i xi x).
Its weight is w(xi)=log(e+|xi|). The original canonical operator is
A_Q=I+i^*R_B i, preserving the physical logarithmic principal part.

RC21 proves for T=exp(7)

    A_Q >=(1/10)I_D -12 J_T^*J_T,                  (1)

where J_T restricts Fourier(i h) to (-T,T).
The estimate includes the actual digamma multiplier, all seven active
prime powers and both signed pole moments.
RC21 pins the native form to CC27 blob
e9a44661f94ee6750fc5ad1fbf7dc719fa3ba482 at CC119
5df347d3808ac3282864a657b7380e0f54bf4daa.
No new external special-function input is needed in this step.

## Uniform Chebyshev kernel approximation

Define the Chebyshev polynomials by
T_0(t)=1, T_1(t)=t and T_(k+1)(t)=2t T_k(t)-T_(k-1)(t).
The recurrence gives T_k(cos theta)=cos(k theta), hence |T_k(t)|<=1
on [-1,1].

For each real frequency xi put z_xi=2pi B xi and introduce the Laurent
function on the punctured complex plane

    F_xi(w)=exp[-i z_xi (w+w^(-1))/2].

Its Laurent coefficients c_k(xi) satisfy c_(-k)=c_k by w ->1/w symmetry.
On |w|=1, t=(w+w^(-1))/2=cos theta, so the uniformly convergent
Laurent expansion gives

    exp(-i z_xi t)=c_0(xi)+2sum_(k>=1)c_k(xi)T_k(t).

For |w|=2, the imaginary part of (w+w^(-1))/2 is
(3/4)sin theta. Thus |F_xi(w)|<=exp(3|z_xi|/4).
The coefficient contour integral and its length bound give

    |c_k(xi)|<=exp(3|z_xi|/4) 2^(-k), k>=0.

The same symmetry controls negative coefficients. This is a uniform
complex-contour estimate, not a numerical Fourier sample.

Truncate at degrees 0,...,n-1. With z=2pi BT, the kernel error on
|xi|<=T and |x|<=B is at most

    2sum_(k>=n)exp(3z/4)2^(-k)
      =4exp(3z/4)2^(-n).                           (2)

The contour coefficient functions c_k(xi) are continuous and bounded
on the finite frequency band. Thus they define bounded finite-rank
operator outputs; their numerical evaluation is not required for the
tail theorem.

## Explicit bounded moment head

Let

    ell_k(h)=integral_(-B)^B T_k(x/B)(i h)(x)dx,

and let r_k be its canonical Riesz representative, with
ell_k(h)=<r_k,h>_D for the chosen inner-product convention.
Each functional has squared dual norm at most 2B=11/5, since
|T_k(x/B)|<=1 and ||i||<=1.

For n=8600 define the finite-rank map

    X_n h=c_0 ell_0(h)+2sum_(k=1)^(n-1)c_k ell_k(h)

into L2(-T,T). The kernel estimate (2), multiplied by the square root
of the physical/frequency rectangle area, proves

    ||J_T-X_n||<=2sqrt(BT)*4exp(3z/4)2^(-n).        (3)

Let P project CANONICALLY onto span{r_0,...,r_(n-1)}, and H=I-P.
Then every ell_k vanishes on H, so X_n H=0.
The polynomials T_k(x/B) have distinct degrees and nonzero leading
coefficients, so this feature space is the same span as the corresponding
canonical monomial-moment representatives up to degree n-1.
It is not a physical polynomial projection.

## Fresh exact residual and whole-tail bounds

Fresh rational enclosures give exp(7)<1100 and exp(2/3)<2,
hence log2>2/3. With pi<22/7 and BT<1210,

    n log2-3z/4
      >(2/3)*8600-(3/4)*(44/7)*1210
      =610/21>16.

Also e>2 and 2sqrt(BT)<70.
Consequently the uniform kernel error in (2) is <4exp(-16)<1/16384,
and (3) gives

    ||J_T-X_n||<70/16384<1/100,
    ||J_T H||<=1/100.

Inserting this entire low-band residual into (1) proves

    D:=H A_Q H >=[1/10-12/10000]I_H
                 =(247/2500)I_H.                 (4)

The full infinite complement is controlled, without concentration
diagonalization or complementary sampling. The feature rank is at most
8600. The ratio of RC21's sufficient count to this one is 115/43>5/2.
The true minimum adequate rank is not estimated.

## Canonical matrix interface for the remaining actual conditions

Let R:C^n -> D_B be the feature map R a=sum_j a_j r_j.
The moment functionals are independent on the supported smooth core:
a polynomial that integrates to zero against every such test is zero.
Therefore their Riesz representatives are independent and

    M=R^*R

is positive definite. Its entries are the exact canonical feature Gram.
A numerical lower bound or conditioning estimate for M is NOT supplied.

Define the actual head matrix

    A=R^* A_Q R.

The head lower condition P A_Q P>=m P is equivalent to

    A>=m M.                                       (5)

This is a generalized canonical-metric inequality. A Euclidean entrywise
or ordinary spectral lower estimate on A alone does not replace it.

Define actual bounded remainder source columns

    sigma_j=i^*R_B i r_j,

their head-pairing matrix V=R^*sigma, and full source Gram U=sigma^*sigma.
Since A_Q=I+i^*R_B i and the remainder is selfadjoint,

    V=A-M,   V=V^*.

The exact orthogonal projection is P=R M^(-1)R^*.
The whole canonical source-residual Gram is therefore

    Gamma=sigma^*H sigma
          =U-V^*M^(-1)V >=0.                       (6)

Writing Z=H A_Q P, the source condition ||Z||<=beta is equivalent to

    Gamma<=beta^2 M.                               (7)

Indeed every head vector is R a, its canonical norm squared is a^*M a,
and its residual norm squared is a^*Gamma a.
The columns sigma contain every actual archimedean remainder, prime
and signed pole term. U is their FULL canonical Gram; it is not a sampled
tail Gram or a physical source norm substituted for the canonical norm.

Equations (5)--(7) specify a finite-matrix acceptance interface without
first computing an orthonormal basis. They still require rigorous entries,
a validated canonical M inverse or equivalent solves, and whole source
error control. Subtracting two approximate Gram matrices without an
error enclosure cannot certify (6).

With m=1/4000 and beta=1/300, (4) gives

    A_Q's finite Schur reserve
      >=m-beta^2/(247/2500)
      =1/4000-1/8892=1223/8892000>0.

The exact bounded Schur factorization would then prove original whole
positivity at B=11/10. No entries of M, A, V, U or Gamma for this actual
head are computed here, so the acceptance conditions remain open.

## Computational boundary and validation

The physical Chebyshev polynomials are uniformly bounded, avoiding the
exponential growth of raw monomial feature norms. This does NOT prove
a well-conditioned canonical Gram matrix or a stable numerical
implementation. Canonical Riesz representation and actual arithmetic
head/source certification remain the main uncompleted steps.

The lower feature count preserves only the stated tail guarantee.
The actual head floor and source residual may differ from the previous
larger head. No monotonic improvement in those unknown quantities is
assumed. There is no new arithmetic positivity or cancellation theorem.

scripts/validate_rpb108_rc22_chebyshev_head.py passes 35 exact rational
checks: contour geometry, exponential/logarithmic enclosures, residual
and whole-tail budgets, rank ratio, Laurent/Chebyshev recurrence controls,
conditional Schur reserve, a nonorthonormal source-Gram subtraction
control, and unsafe block positivity. The infinite contour expansion,
Riesz-space and operator proofs are analytic arguments above; finite
controls do not evaluate the actual head or sources.

No actual canonical projection or matrix is constructed. No original
negative vector, new whole aperture positivity, RH/F4 theorem or Lean
closure is claimed. Existing 1.06 positivity and restricted theorems
remain intact. Other branches and historical files are unchanged.
