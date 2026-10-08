# RPB108 CC31: cap-uniform critical rank reduces the covariance target to scalar residual norms

Date: 2026-10-08 UTC. Parent: 3d67de4ba4c44c6b4e164ee064663cc531a04527.
Definitions: [uniform critical rank](../docs/TERMINOLOGY_RPB108_UNIFORM_CRITICAL_RANK.md).
Classification: actual analytic structural reduction; scalar arithmetic
suppression remains unproved. No new aperture or Lean certification.

## Result

The original native Garding estimate and complete positive-source upper
bound supply a finite critical-rank bound depending only on the finite
cap, uniformly over all its old strictly positive subwindows. This
strengthens the chart-dependent rank interface in the source-shell note:
one does not need to assert that the aperture-one retained complement
continues to protect every larger aperture.

Consequently the CC29 vanishing-modulus target follows from a bound for
each individual critical EIGENVECTOR's complete forced residual norm,
with a finite cap-dependent loss. Full collective coherence creates a
factor at most d_B; it need not be estimated separately to prove the
endpoint sufficient target. The scalar residual is still an adaptive
whole arithmetic combination, and its defect dependence is not established.

## 1. Actual inputs, with the old gap excluded

Use the established canonical domain D_B of physical functions supported
in [-B,B], with squared norm integral log(e+|xi|)|Fourier h(xi)|^2.
The full native form satisfies

    Q(h)>=alpha||h||_D^2-kappa||h||_2^2, alpha>0, kappa>=0.  (1)

Here alpha and kappa depend only on B. This is the Garding bound retained
in LOG_SOURCE_ANALYSIS section 4, expressed in lower-bound form. The
native archimedean log growth and finite-cap bounded prime and pole
terms give the same bound; see CC27 for the unchanged native formula.
It is not positivity of Q, a source-defect lower bound, or a physical
operator-domain regularity assertion. Use also the established actual
source observability

    c_B||h||_D<=||Ph||<=U_B||h||_D.                         (2)

No compactness of the unweighted negative source N or source Gram A is
assumed. No Lindelof or local transverse-density premise is imported.
This uses existing form bounds to sharpen the current critical interface;
it does not restart a generic compactness investigation.

## 2. A quantitative finite-rank protected complement on the entire cap

Suppose first kappa>0. Choose R>=1 so

    log(e+R)>=4 kappa/alpha;

for example R=max(1,exp(4 kappa/alpha)) suffices. The Fourier tail gives

    ||h||_2^2 <= <Z_R h,h>+||h||_D^2/log(e+R),

where Z_R is the low-frequency Gram on D_B. For each xi, the Fourier
evaluation functional has D_B dual norm at most sqrt(2B), by physical
Cauchy--Schwarz and ||h||_2<=||h||_D. Hence F_R:D_B->L2[-R,R] is
Hilbert--Schmidt, Z_R is positive trace class, and

    tr Z_R <= integral_(-R..R) 2B dxi = 4BR.              (3)

Let F_B be its spectral subspace for eigenvalues strictly above
tau=alpha/(4 kappa). It has dimension

    d_B=dim F_B <= floor(16 kappa B R/alpha).              (4)

On its D_B-orthogonal complement Z_R<=tau I. Thus (1) gives

    Q(h)>=alpha||h||_D^2/2, h perpendicular F_B.           (5)

When kappa=0, take F_B=0 and d_B=0; (5) follows directly. The displayed
bound is explicit in the cap form constants, although those constants
have not been optimized or numerically evaluated in this pass.

Every D_s, s<=B, is an isometrically included supported subspace. Its
intersection with F_B perpendicular has codimension at most d_B IN D_s.
The vectors spanning F_B need not have support in D_s; intersecting its
orthogonal complement is sufficient and avoids that false assumption.
This is a cap-wide auxiliary complement, not an inherited numerical
aperture certificate or a retained source-height prefix.

## 3. Uniform rank for the complete near-unit source output

For each original strictly source-positive old s, use V_s=P(D_s),
T_s(Ph)=Nh, and Dpos_s=I-T_s*T_s on V_s. On the positive image of
the complement just constructed, (2) and (5) yield

    <Dpos_s v,v> >= gamma_B||v||^2,
    gamma_B=alpha/(2 U_B^2).                              (6)

This image is closed with codimension at most d_B, since P is an
isomorphism onto V_s. Choose the FIXED band

    eta_B=min(1/2,alpha/(4 U_B^2)) < gamma_B.

The spectral subspace of Dpos_s for defects in (0,eta_B] has dimension
at most d_B: any larger subspace would intersect the protected complement
nontrivially and contradict (6). The nonzero spectral spaces of T_s*T_s
and A_s=T_s T_s* correspond by the polar isometry. Therefore

    rank E_s <= d_B,
    E_s=1_[1-eta_B,1)(A_s),                               (7)

uniformly for every such s<=B. This supplies the independently justified
protected-rank input needed in CC20 on a fixed cap. It does NOT show
that its individual critical vectors have finite coordinate height
moments, nor that critical leakage is small.

## 4. Scalar arithmetic bound sufficient for the full matrix target

On ran E_s choose any orthonormal eigenbasis y_i, with lambda_i>0 and
delta_i=1-lambda_i. Use the complete CC20 residual

    J_i(f)=Q(h_i,f)-delta_i<Ph_i,Pf>,
    h_i=P_s^-1 T_s* y_i/sqrt(lambda_i),
    M_t=P_t*P_t.

CC20 gives the exact full covariance

    C_st=L_st L_st*=Lambda^-1/2 J M_t^-1 J* Lambda^-1/2.  (8)

Assume a scalar arithmetic estimate with cap-only b_B<infinity, fixed
band, positive admissible step, and bounded vanishing modulus omega:

    ||M_t^-1/2 J_i*||^2 <= b_B lambda_i omega(delta_i)     (9)

for every basis row and every admissible s,t. This estimate is NOT proved.
It measures the dual norm on ALL of D_t in the complete positive metric.
It already includes all divisor copies, both prime orientations and the
full pole; bounding selected zero coordinates or finite trial tests is
not (9). A stronger sufficient canonical-dual version is

    ||J_i||_(D_t*)^2 <= b_B c_B^2 lambda_i omega(delta_i).

To deduce the matrix bound, let z_i=M_t^-1/2 J_i*/sqrt(lambda_i).
Then ||z_i||^2<=b_B omega(delta_i). Weighted Cauchy--Schwarz gives

    ||sum_i c_i z_i||^2
       <= (sum_i |c_i|^2 omega(delta_i))
          (sum_i ||z_i||^2/omega(delta_i))
       <= d_B b_B sum_i |c_i|^2 omega(delta_i).

If omega(delta_i)=0, (9) forces z_i=0; omit that row, so no inverse of
a zero weight is used. We obtain the complete Loewner bound

    L_st L_st* <= d_B b_B omega(G_s).                     (10)

No off-diagonal term is discarded: positivity of the entire Gram bounds
its mixed terms. Conversely a matrix bound supplies each diagonal bound
with its matrix constant. Thus, up to the finite cap factor, the scalar
and collective vanishing targets have the same endpoint sufficiency.
No uniform rank bound across ALL caps is needed; CC29 permits cap-dependent
constants and steps. If the rank is zero the target is vacuous there.

For the strict linear continuation budget, omega(x)=x and the resulting
critical cost is at most d_B b_B. One still needs low cost ell_B and
d_B b_B+ell_B<1. The weaker endpoint argument requires no such reserve,
but the actual scalar vanishing bound remains essential.

## 5. Sharpness and controls

The loss d is sharp: for positive diagonal weights omega_i, take all
z_i parallel with ||z_i||^2=omega_i. The normalized Gram is the all-ones
matrix with norm d. Orthogonal z_i have the SAME diagonal data but norm
one. Phase signs do not improve the worst case. Without a cap-uniform
rank, rows of squared norm 1/d can tend to zero while the Gram norm
stays one. Thus individual smallness alone is insufficient when rank
can grow; (7) is the load-bearing actual input here.

The genuine differential crossing retains only one critical direction
near contact, yet its fixed-target leakage tends to a positive value.
It satisfies the structural rank conclusion but violates the proposed
scalar vanishing bound. The full positive-level finite source control
also has finite rank while its correctly shifted critical plus low cost
is exactly one. Finite critical rank therefore cannot be relabeled as
arithmetic suppression or zero-level discrimination.

## Validation and standing

All 25,375 exact checks pass: 388 new and 24,987 inherited from CC30.
The validator replays CC30 and adds finite protected-complement,
normalized Gram, sharp coherent amplification, and unbounded-rank controls.
These finite rational tests do not evaluate actual zeta eigenvectors.
The infinite trace-class construction and actual uniform rank theorem
are analytic deductions from the existing form/source bounds, not Lean
results certified by a count of rational samples.

Original whole-domain positivity remains certified through 21/20,
even0/odd0, with physical margin 1/(3*10^63). RH/F4, retained attachment,
reusable continuation, scalar arithmetic suppression and Lean closure
remain open. Global NF71, Aperture and Pre-Contact Shadow remain paused.
