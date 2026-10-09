# CC92: conditional six-retained-direction plus all-F physical gap

CC parent: 713c1add89672a315a90518258b2f7a108fde4b5 (CC91). Immutable read-only Native Source: 6658ff2837838ab00b9b9c605fdd200d473c3293 (NF46). Other branches are unchanged. Aperture is 53/50.

## Result and hypotheses

The two positive fixed joined matrices now yield a single conditional physical restriction certificate:

    Q_original(h) >= g ||h||_L2^2,
    g > 1.1503e-52,
    h in E6+F.

E6 is the span of the original retained x,w,u32 in both parities; F is the entire original high complement. This is a very conservative physical gap, not the earlier Euclidean coordinate bound. The exact rational g is saved in JSON.

The theorem assumes the remaining-high self-adjoint/form operator A satisfies A >= kappa I, kappa=207/1000, and the inherited original form identity with its source/domain attachments. These assumptions are not discharged here. The domain statement is the original joined restriction on which the block identity holds, with the high component in the high form domain. It does not assert spectral L2 regularity for an arbitrary null vector or extend the original form to all physical L2 vectors.

## Lift custody and original identity

NF35's original definitions explicitly allow passing parity packets to join into the six-retained-direction restriction with all F. Its retained components are exactly mutually orthogonal and nonzero. However, the later inverse packet is built from NF37's selected lifted family, not NF35's original lifts: each old lift is modified by a frozen scalar multiple of the NF36 high correction. This preserves E6+F but changes Q and Gamma.

CC92 authenticates NF35's mass/orthogonality certificates and validation, original NF26 seed lift, NF29 response lift, NF30 even expanded-response trial, and both NF36/NF37 correction packets. It checks the NF35 parent hashes and the NF36 correction norm against NF37's exact coefficients. The NF35 vectors have norms below 6/5 and each subsequent NF37 movement has norm below 1/10; hence all three current lifted vectors have norm below two. Thus ||V||^2 <= trace(V*V)<12. Cross entries are not needed for this conservative trace bound.

For each parity the current NF37 selected Q and complete source Gamma are used. A freshly verified rational inverse enclosure for the full NF46 even or NF45 odd denominator reconstructs

    K = Q - Gamma/kappa + W N^-1 W*/kappa^2.

Every reconstructed entry overlaps the corresponding positive joined packet entry. This checks the actual physical source identity and records the lift change rather than silently reusing the earlier source Gram. Existing native integration and source/domain certificates are inherited; their matrix custody is checked here.

## Physical completion-square estimate

Write h=Vx+y, y in F, and R=P_F L_original V. Under the stated attachments,

    Q_original(h)
      = x*(Q-R*A^-1R)x
        + ||A^(1/2)(y+A^-1Rx)||^2
      >= epsilon ||x||^2 + kappa ||z||^2,
    z=y+A^-1Rx.

The positive joined lower certificate gives a rational coordinate epsilon>0 by CC87's triangular condensation estimate. Since Gamma=R*R and A>=kappa I,

    ||A^-1R||^2 <= trace(Gamma)/kappa^2 = D.

Also ||V||^2<12=M. The physical vector is h=(V-A^-1R)x+z, so elementary squared-norm bounds give

    ||h||^2 <= 4(M+D)||x||^2 + 2||z||^2.

Therefore g_parity=min(epsilon/[4(M+D)],kappa/2) is a physical gap on that parity's complete joined restriction. Exact original parity makes mixed even/odd mass and form terms zero; taking min(g_even,g_odd) gives the stated gap on E6+F. Real symmetric packet bounds extend to complex coefficients by separating real and imaginary parts.

This resolves the simultaneous conditional six-retained-direction restriction, including all high vectors in its attached form domain. It does not certify the full retained matrix: the other retained directions and their couplings to E6 remain absent.

## Validation and frontier

The validator reruns CC91's authenticated positive packet checks, authenticates the mass and lift chain, reconstructs both full inverse packet identities, and computes the physical gap using exact rational bounds. Exact controls verify the completion estimate with nonorthogonal lifted physical coordinates, demonstrate that a coordinate gap cannot simply be relabeled physical, and preserve a physical null mode when the Schur gap is zero despite positive high background.

The six-direction physical restriction certificate is conditional on the same unresolved floor and original form attachments. Unconditional remaining-high floor, complete remaining-background transport, full retained matrix, other 106 retained directions and collective coupling remain open. Whole-domain positivity remains certified at 21/20. No whole 53/50, old-gap-independent all-cap continuation, RH, F4, full transport or Lean closure is claimed.

Next integration must add the remaining retained directions with their complete signed native/source covariances, or establish a justified background bound that includes them. The completed fixed packets need no additional deficit-targeted source selection unless that larger assembly changes their certificate.

## Reproduction

Run `python scripts/certify_cc92_conditional_physical_restriction.py notes/cc92-source notes/cc91-source notes/cc87-source notes/cc85-source --output notes/data/RPB108_CC92_CONDITIONAL_PHYSICAL_RESTRICTION_20261009.json`. Imported mass/lift packets and NF35 parity definitions are immutable in `notes/cc92-source`.
