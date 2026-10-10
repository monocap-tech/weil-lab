# RPB108 RC41 — exact native moment reconstruction with projector-gap control

2026-10-10. Parent RC40: `d44c6cc348f7455ce893653e9befac2af29a82a8`.
Only `research/rpb108-route-consolidation` is written. Historical artifacts
and other branches are unchanged.

## Result

An emitted rational 32-by-8 coefficient matrix now reconstructs a physical
polynomial from the first eight **actual native Chebyshev moments**. Every
moment is preserved exactly, not within a numerical tolerance. The resulting
operator O is an idempotent oblique projection whose kernel is exactly the
canonical orthogonal complement of the actual low-eight native Riesz head.

For P the true canonical orthogonal projector onto that head, the certified
whole-domain bounds are

    ||O-P||_D <523/10000 =0.0523,
    ||O||_D <100137/100000 =1.00137.

This is an explicit low-eight moment reconstruction, not an evaluation of
the exact canonical projector. It does not construct the full 8600-feature
head, evaluate original Weil sources, or certify new original positivity.

## Input custody and exact physical attachment

The carrier, B=11/10, logarithmic metric, and Fourier convention are unchanged.
RC39 certifies the first eight canonical Riesz representatives r_j of

    ell_j(h)=integral T_j(x/B) i h(x) dx, j=0,...,7.

Let R a=sum_j a_j r_j and M=R^*R. RC39 also emits 32-mode Legendre
coefficients of a trial map V for R, and proves

    (V-R)^*(V-R) <=q2 M,
    q2=1531371999127928832/561420614948974609375
       =0.002727673260211703... <1.

Here and below operator adjoints use the actual canonical metric. Let C be
the exact Chebyshev-to-Legendre conversion from RC39. For physical Legendre
mass d_i=11/[5(2i+1)], the trial moment pairing is exactly

    J=R^*V=C^* diag(d_0,...,d_7) V_top.

There is no canonical inverse approximation in this identity: Riesz duality
identifies R^*v with the physical moments of v. V_top comprises the first
eight rows of the emitted native trial coefficient matrix. The exact check

    (J+J^*)/2 >=(1/2) M_phys

proves nonsingularity. J is not assumed symmetric; rounded RC38 trial
coefficients need not solve the nominal system exactly. The validator
computes its exact rational inverse and checks both inverse products.

## Explicit reconstruction and identities

Define W=V J^(-1), and, for any h in the canonical carrier, set

    O h=W ell(h),  ell(h)=(ell_0(h),...,ell_7(h)).

The certificate emits all 256 rational Legendre coefficients of W. Direct
physical integration gives

    ell(W a)=a,  R^*W=I_8,  WJ=V.

Consequently

    O^2=O,
    range O=range V,
    ker O=ker R^*=(range R)^perp_D,
    ell((I-O)h)=0.

Thus the reconstruction residual belongs to the actual native canonical
complement exactly. The reconstructed polynomial itself lies in the trial
space; it is not asserted to lie in the actual Riesz head. O is generally
not selfadjoint. All opposite-parity reconstruction coefficients are zero.

An independent replay expands both Chebyshev and Legendre polynomials in
the power basis and integrates their products directly on [-B,B]. It
rechecks all 64 moment identities, J, both inverse products, WJ=V, and the
published operator budgets without relying on the Legendre diagonal-mass
formula used to build J.

## Whole canonical projector-gap proof

Let U=range R and Z=range V. Both have dimension eight, since M is positive
and J is invertible. For any u=R a,

    dist_D(u,Z) <=||R a-V a||_D <=sqrt(q2)||u||_D.

The largest principal-angle sine between the two equal-dimensional spaces
is therefore at most sqrt(q2). Equality of the two directional gap norms
follows from the singular values of the orthonormal cross-Gram: both
directional squared gaps are one minus its smallest squared singular value.
In particular Z is a graph over U, say Z={u+L u:u in U}, with L:U->U^perp.
The angle bound gives

    ||L||^2 <=q2/(1-q2)=t2
             =0.0027351338115726305... .

The unique projection onto Z along U^perp is O=(I+L)P. Its moment identity
established above selects precisely this projection. Thus

    O-P=LP,
    ||O-P||^2 <=t2,
    ||O||^2 <=1+t2=1/(1-q2).

The displayed outward bounds 0.0523 and 1.00137 are checked by exact
rational squaring. These are operator bounds on the entire carrier, not
tests on eight input vectors. The principal-angle argument is an analytic
proof attached to the exact certificates; it is not Lean formalization.

## Safe future source-residual transfer

For an arbitrary canonical source map sigma define

    U_src=sigma^*sigma,
    G_ob=sigma^*(I-O)^*(I-O)sigma,
    Gamma=sigma^*(I-P)sigma.

The exact relation (I-P)sigma=(I-O)sigma+(O-P)sigma and Young's inequality
give, for any s>0,

    Gamma <=(1+s)G_ob+(1+1/s)t2 U_src.

The fixed rational s=1 budget stored in the certificate is

    Gamma <=2 G_ob+0.005470267623145261... U_src.

The fractional coefficient in the JSON, rather than its decimal display,
is the acceptance value. Full source covariance remains required. Neither
G_ob nor U_src is evaluated in RC41. Cross terms cannot simply be deleted,
and G_ob cannot be substituted for Gamma.

A replayed exact control makes this distinction concrete. In R^2 let the
native head be span(e_1), the trial space span(e_1+e_2/20), and use the
corresponding moment-preserving O. For sigma=e_1+e_2/20, G_ob=0 while
Gamma=1/400. This is a discrimination control, not an original Weil source
or a negative native vector.

## Validation and scope

Run:

    python scripts/validate_rpb108_rc41_native_moment_reconstruction.py
    python scripts/validate_rpb108_rc41_native_moment_reconstruction.py --replay certificates/rpb108_rc41_native_moment_reconstruction.json

Generation and direct power-basis replay pass. The source SHA-256 binds the
RC39 certificate bytes. No RC38/39/40 metric, coefficient, error budget, or
historical proof is modified. RC40's Gram inverse enclosure remains intact;
J^(-1) here is a different, exactly known moment/trial pairing inverse.

This supplies a usable exact-moment reconstruction and controlled low-eight
projector surrogate. It does not improve the inherited Riesz approximation
error. In particular eight moments do not inherit RC22's 8600-moment Fourier
annihilation bound or its whole complementary Weil floor. A principal
eight-feature projector is not the full-head projector. Actual original
Weil head and source matrices, the full 8600-feature construction, new
aperture positivity, RH/F4, and Lean closure remain open.
