# RPB108 — NF40: native boundary defect and missing response coupling

Date: 2026-10-09. Aperture: a=53/50. Branch:
`research/rpb108-phase-geometry-localization`. Predecessor: NF39,
commit `85bc9f259cbbddb400f417617171a29b6b5a61d3`.

Terminology is fixed before use in
[the additive NF40 terminology note](../docs/TERMINOLOGY_RPB108_BOUNDARY_DEFECT_NF40.md).

NF40 certifies a positive **boundary energy defect compression** from
original native arithmetic data. It also proves, by an exact
**zero-response extension**, that these extra energy moments alone do
not force the **joined inverse improvement** needed after NF39.

## Original native certificate

Keep NF38's frozen two high columns Z and three joined physical source
columns R. Put kappa=207/1000, M=Z*Z,
C=Z*AZ-kappa M, V=AZ-kappa Z and A0=kappa I+V C^-1 V*.
The uncertain C is rigorously positive definite, as in NF39.

Take Y=(e112,e114) in the even sector and Y=(e113,e115) in the odd
sector. Y*Y=I. The exact polynomial coefficients give X=Y*Z. The
reconstructed original Z source coordinates, enlarged by their uniform
physical source errors, give P=Y*V. The original signed native archives
give QY=Y*AY. Thus the following is an actual original compression,
not a quadrature estimate:

\[
D_Y=Y^*(A-A_0)Y=Q_Y-\kappa I-P C^{-1}P^*.
\]

All operations use rational outward interval arithmetic at the inherited
500-digit grid. Off-diagonal symmetry is enclosed by intersection. The
positive leading diagonal and positive determinant certify D_Y>0.
The physical gap lower bound is `1 / upper(trace(D_Y^-1))`.
It is strictly below the least eigenvalue of this positive 2 by 2 matrix.

| Certified quantity | Even | Odd |
| --- | ---: | ---: |
| Physical boundary defect gap, strict lower bound | 1.52713025714900 | 1.56317765849180 |

The displayed bounds are rational decimal bounds rounded downward from
the exact certificate. For orientation only, approximate entries of D_Y
are (3.09815470627, 0.520325757710, 3.18392542535) even and
(3.17284368438, 0.458286629579, 3.21168796075) odd, in diagonal/cross/diagonal
order. Approximate determinants are 9.59355464684 and 9.98015722759.
The JSON intervals, rather than these diagnostic decimals, carry the proof.

This excludes NF39's bare minimal model A0 as a model of the expanded
boundary packet: it would have D_Y=0. It does not supply a whole-high
defect gap. Comparison with the actual inverse continues to use NF39's
background-floor hypothesis; NF40 does not establish that hypothesis
anew or certify a whole-domain sign.

## Exact extension with positive defect and zero joined response

Select the same rational aggregate packet used by NF39 and rational
boundary P,QY within the new outward enclosures. Extend the seven-vector
Gram of (Z,V,R) by two orthonormal Y columns, preserving X and P.
The new Y*R moments have not been certified for the actual sources and
are left free in this information-sufficiency test.

Choose them so that, with Ytilde=Y-Z M^-1 X*,

\[
\widetilde Y^* A_0^{-1}R=0.
\]

Concretely, if the old inverse source coordinates are AR=A0^-1 R,
then choose Y*R=kappa (X M^-1 Z*AR-P AR_V), where AR_V denotes its
V coordinates. The nine-vector physical Gram is exactly positive
definite in both sectors by rational LDL reconstruction. Define
L=Ytilde*Ytilde>0 and D=QY-kappa I-P C^-1 P*>0 for this chosen packet.
The exact operator

\[
A_-=A_0+\widetilde Y L^{-1}D L^{-1}\widetilde Y^*
\]

has A_- >= kappa I, A_- Z=AZ and Y*A_-Y=QY. It preserves every
NF39 aggregate moment M,QZ,GZ,B,S,G and the retained native Q.
The added positive operator kills A0^-1 R, hence

\[
A_-^{-1}R=A_0^{-1}R,\qquad
R^*(A_0^{-1}-A_-^{-1})R=0.
\]

The joined Schur matrix is exactly the NF39 minimal-background ceiling.
Its first two LDL pivots are positive and its final pivot is negative:
approximately -9.79276133334e-23 even and -1.66208780456e-21 odd.
These are signs of an exact abstract model only. The chosen Y*R
correlations are synthetic; this is an enclosure-compatible extension,
not a claim that the actual complete Weil geometry or unknown exact
moments have been realized. Actual Weil negativity is not claimed.
NF40 does not certify an opposite-sign extension for the expanded packet.

## Reproducibility and checks

Run from the repository root with the authenticated original native
archives available at the inherited `nf24-inputs/Weil/` paths:

```sh
python scripts/certify_native_boundary_defect_nf40_106.py --parity even --output notes/data/RPB108_NF40_EVEN_BOUNDARY_DEFECT_CERTIFICATE_20261009.json
python scripts/certify_native_boundary_defect_nf40_106.py --parity odd --output notes/data/RPB108_NF40_ODD_BOUNDARY_DEFECT_CERTIFICATE_20261009.json
python scripts/validate_native_boundary_defect_nf40_106.py --output notes/data/RPB108_NF40_BOUNDARY_DEFECT_VALIDATION_20261009.json
```

The inherited loader authenticates the original native archives and
source construction inputs. The validator authenticates NF39's two
certificates and validation manifest, replays the NF39 packet identities,
recomputes the outward native defect, and independently solves the exact
A0 system to check the zero-response extension. It verifies the nine-vector
Gram, the PSD factor construction, all named moments and boundary energy,
and the negative abstract joined Schur sign. It also checks D_Y-gap I>0.
No sampling or numerical quadrature enters these proofs.

Controls include three positive boundary defects with exactly zero
uncoupled inverse response, and positive response after adding a coupled
defect; the inherited six full-block positive/null/negative crossings;
and three positive whole-physical-mass controls. Validation: PASS.

## Next frontier

The arithmetic boundary defect is now certified. The next source task is
to certify the missing signed Y*R correlations and reconstruct boundary
source columns AY with their paid physical errors. Together with the
signed defect-source crosses, that would make a stronger operator
minorant reviewable. A positive energy compression by itself cannot pay
NF39's necessary joined response improvement.

The actual joined inverse improvement, complete remaining background
transport, and whole-domain Schur sign at 53/50 remain open. The highest
internally certified whole-domain aperture remains 21/20. RH, F4 and Lean
closure are not claimed. This checkpoint writes only the Phase Geometry
branch; Coupled, DNE and paused branches are unchanged.
