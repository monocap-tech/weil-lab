# RPB108 RC25 — exact Legendre singular metric and endpoint-log matrix

2026-10-10. Independent route consolidation.
Parent: 4909f4de9506fc5a47c3b275d4794843bcde0c9e (RC24).
Only research/rpb108-route-consolidation is written.

## Result and evidence boundary

The actual canonical metric source from RC24 splits exactly into

    L_B =T_0 +W_B +c_R I +K_B,   R=2B,

on polynomial trial vectors. The universal singular operator T_0 is
diagonal on Legendre polynomials, with eigenvalues H_n.
The endpoint multiplication W_B has exact rational polynomial-basis
matrix entries. The remaining kernel operator K_B is Hilbert--Schmidt,
with norm <24 at B=11/10.

An executable exact component assembler evaluates the first eight
physical Legendre trial modes. Those are actual pieces of the canonical
metric, not synthetic surrogate matrices. The scalar c_R and compact
kernel matrix are not evaluated, so the complete metric matrix and
the canonical Riesz-head matrices remain unknown.

This removes singular quadrature from two concrete components of a
trial-space Riesz solve. It does not compute the metric inverse, a small
weak residual, the original positivity head, or source leakage.

## Definitions and attachment

Use the supported logarithmic metric with weight log(e+|xi|) and
Fourier convention exp(-2pi i xi x), at B=11/10.
RC24 attaches its physical source L_B to every Lipschitz interval trial
vector, retaining both zero-extension endpoint terms.

Its density is

    ell(r)=2integral_0^infinity exp(-e t)/
                  (t^2+4pi^2 r^2) dt, r>0.

Define the nonnegative remainder density

    k(r)=1/(2r)-ell(r)
        =2integral_0^infinity (1-exp(-e t))/
                  (t^2+4pi^2 r^2) dt.

For R=2B put

    F_R=integral_R^infinity ell(r)dr,
    K_R=integral_0^R k(r)dr,
    c_R=1+2F_R-2K_R.

These are exact scalar definitions. Define

    (T_0 v)(x)=(1/2)integral_(-B)^B
                         [v(x)-v(y)]/|x-y| dy,
    W_B(x)=(1/2)log[R^2/(B^2-x^2)],
    (K_B v)(x)=integral_(-B)^B k(|x-y|)v(y)dy.

T_0 is understood with its internal difference cancellation.
W_B is unbounded at the endpoints; it is not discarded or replaced
by a constant. K_B is a bounded integral operator despite its density
having a logarithmic singularity. No pointwise value at r=0 is required.

## Exact source split

For an endpoint distance d in (0,R],

    integral_d^infinity ell(r)dr
      =(1/2)log(R/d)-integral_d^R k(r)dr+F_R.

Substitute this into RC24's two exterior terms and replace the internal
ell density by 1/(2r)-k(r). The internal negative multiplication
involves integrals of k over distances 0 to B-x and 0 to B+x.
The two exterior negative terms complete each of those integrals to R.
Their sum is exactly -2K_R v.

The remaining source is therefore

    L_B v=T_0 v+W_B v+c_R v+K_B v.                  (1)

All four pieces are physically L2 on polynomial trials by RC24 and the
bounds below. Equation (1) preserves its full canonical weak attachment.
It is a source identity, not an assertion that L_B is bounded on all L2.

## Legendre diagonalization of the internal singular part

Put t=x/B and let P_n(t) be the Legendre polynomials, with P_0=1,
P_1=t and the usual recurrence
(n+1)P_(n+1)=(2n+1)t P_n-n P_(n-1).

On monomials, direct integration of the divided difference gives

    T_0(t^n)=H_n t^n
       -(1/2)sum_(j=0)^(n-1)
            [(1+(-1)^(j+1))/(j+1)]t^(n-1-j),

where H_0=0 and H_n=sum_(j=1)^n 1/j.
Thus T_0 preserves every polynomial degree subspace and its leading
coefficient on degree n is H_n.

The symmetric difference kernel makes T_0 selfadjoint on polynomials:
symmetrizing its mixed integral gives the product of two differences
over 2|t-s|. The integral is finite for polynomials.
For every polynomial q of degree below n,

    <q,T_0 P_n>_2=<T_0 q,P_n>_2=0,

since T_0 q still has degree below n.
Legendre orthogonality and the leading coefficient therefore prove

    T_0 P_n=H_n P_n.                               (2)

This is a complete analytic proof of the polynomial diagonalization.
It is not a sampled spectrum or a diagonalization of the original Q.
The unnormalized physical mass of P_n(x/B) is 2B/(2n+1), so its
singular metric matrix entry is H_n*2B/(2n+1).

## Exact rational endpoint-log entries

Since R=2B,

    W_B(Bt)=log(2/sqrt(1-t^2)).

For m>=0 define its even moment

    J_m=integral_0^1 t^(2m)log(2/sqrt(1-t^2))dt.

The positive power series of -log(1-t^2), followed by nonnegative
sum/integral interchange, gives

    J_m=log2/(2m+1)
        +sum_(j>=1) 1/[2j(2m+2j+1)].

Partial fractions express the sum as
[sum_(q=0)^m 1/(2q+1)-log2]/(2m+1).
The log2 identity follows from the alternating harmonic series, or
integrating its finite geometric sums for 1/(1+t).
Thus the logarithms CANCEL EXACTLY:

    J_m=[sum_(q=0)^m 1/(2q+1)]/(2m+1).             (3)

For example J_0=1, J_1=4/9 and J_2=23/75.
If P_i(t)P_j(t)=sum a_k t^k, its physical endpoint matrix entry is

    W_ij=2B sum_(k even) a_k J_(k/2).               (4)

Odd-parity entries vanish. With rational B and the unnormalized rational
Legendre coefficients, every entry in (4) is rational.
An orthonormal basis would introduce its normalization square roots;
the exact rational generalized metric representation avoids that step.

The first actual trial components at B=11/10 are:

| Entry | Physical mass | Singular metric | Endpoint metric |
| --- | ---: | ---: | ---: |
| (0,0) | 11/5 | 0 | 11/5 |
| (1,1) | 11/15 | 11/15 | 44/45 |
| (2,2) | 11/25 | 33/50 | 451/750 |
| (0,2) | 0 | 0 | 11/30 |

These are components of the metric on PHYSICAL trial polynomials.
They are not RC22's Gram M of canonical Riesz representatives.

## Compact remainder and explicit whole norm allowance

Using 1-exp(-e t)<=min(e t,1), split the density integral at t=1.
With e<3 and pi>1,

    k(r)<=3log(1+1/(4r^2))+2
         <=11/4+6log_+(1/r).                       (5)

For r<=1 this follows from 1+1/(4r^2)<=5/(4r^2) and
log(5/4)<=1/4. For r>=1, log(1+1/(4r^2))<=1/4.

At R=11/5, the elementary logarithmic moments give

    K_R<= (11/4)R+6=241/20,
    integral_0^R k(r)^2 dr
      <=(121/16)R+33+72.

The kernel's full Hilbert--Schmidt norm squared is

    ||K_B||_HS^2
      =2integral_0^R (R-r)k(r)^2 dr
      <=2R integral_0^R k(r)^2 dr
      <=107041/200<24^2.                           (6)

Thus K_B is compact and ||K_B||<24.
The pointwise nonnegative density is not asserted to make K_B a
positive operator. Compactness alone does not prove it is a small
correction relative to a near-critical original head.

RC24's far-tail bound also gives F_R<=1/(4R), and hence

    -231/10<=c_R<=27/22.

These broad bounds establish finiteness but are too loose for an actual
inverse or near-critical matrix calculation. Neither c_R nor K_B's
actual matrix entries are evaluated here.

## Executable component construction

scripts/validate_rpb108_rc25_legendre_metric_split.py supplies
exact_components(count,B), returning rational matrices for:

- physical Legendre mass;
- the internal singular metric, diagonal by (2);
- the full endpoint-log multiplication, by (3)--(4).

The exact partial metric matrix is

    singular_metric +endpoint_metric +c_R*physical_mass,

and the K_B matrix must still be added to obtain the COMPLETE canonical
metric on this trial space.
This metric can enter an actual Galerkin Riesz construction, but the
Galerkin solution and whole residuals from RC24 are still required.
A finite solve alone does not certify the actual Riesz inverse.

The default run assembles the first eight trial modes and checks their
endpoint matrix in exact arithmetic. The recurrence control verifies
(2) through degree 15; the all-degree statement follows from the
analytic proof above. No floating quadrature is used for these components.

## Computational boundary, validation and standing

29 exact rational checks pass: Legendre singular action, endpoint moment
identities, actual low-mode matrix entries, symmetry/parity, a positive
endpoint control, compact kernel allowance and scalar bounds.
The singularity extraction and all-degree operator arguments are analytic
proofs; the component matrices are actual partial trial data.

The remaining certified computation is the scalar and compact kernel
evaluation, a stable trial Riesz solve, and whole weak residual enclosure.
The native original head/source matrices remain separate obligations.
The compression achieved here follows from matching each exact operator
piece to its structure: Legendre diagonalization for the internal
difference kernel, exact moments for the endpoint logarithm, and
compact-kernel approximation for the remainder. No general arithmetic
positivity rule follows merely from this decomposition.

No complete metric matrix, actual Riesz-head matrix, source leakage or
negative original vector is evaluated. No new whole aperture positivity,
RH/F4 theorem or Lean closure is claimed.
Existing 1.06 positivity and prior restricted results remain intact.
Other branches and historical files are unchanged.
