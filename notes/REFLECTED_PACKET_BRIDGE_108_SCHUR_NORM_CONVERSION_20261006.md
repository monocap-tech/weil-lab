# RPB-108: tighter whole-domain Schur norm conversion

Date: 2026-10-06 UTC. Parent: `ab6a14df99cb6226da85e6077400440849bb047d`.
Branch: `research/rpb108-larger-aperture-complement`.
Definitions: [Schur norm conversion registry](../docs/TERMINOLOGY_RPB108_SCHUR_NORM_CONVERSION.md).

## Result

At aperture a=81/100, the actual full-domain native form now satisfies

```
Q(h) >= mu ||h||_2^2,
mu = 51/(5151*10^29+100).

Q(h) >= kappa Elog(h),
kappa = 51/[10(118473*10^29+2351)].
```

Both constants are almost twice their previous values. This is a tightening
of the norm-conversion step from the already certified Schur inputs.
The corrected matrix margin remains tau=10^(-29); the aperture remains
81/100. The newly certified raw finite margin 10^(-18) is not used here.

## Inherited actual inputs and custody

The [complete actual Schur note](REFLECTED_PACKET_BRIDGE_108_PRIME5_84_SCHUR_081_20261005.md)
supplies the corrected margin tau=10^(-29), complement bound c=51/100,
and physical lift norm strictly below L=10.
Its [validation manifest](data/RPB108_PRIME5_84_SCHUR_081_VALIDATION_20261005.json)
identifies the independently reproduced full Gram by SHA256
`32f664f3e4a686dd220755c18f8aa38b790955b9c6b1a08e99fb8c5ac3a1615c`.
The [endpoint bridge note](REFLECTED_PACKET_BRIDGE_108_ENDPOINT_BRIDGE_AUDIT_20261005.md)
supplies the actual global Garding bound
Q>=(1/10)Elog-23 physical mass.

The new script verifies those three unchanged files by exact Git blob hashes
and records their SHA256 values. The theorem below inherits their analytic
certification; this pass does not independently recertify the original
matrix or source Gram. Raw retrieval of the 8.89 MB Gram failed the connector
size check; the alternative Git blob API route closed its transport.
No changed Gram or corrected matrix is inferred from those failures.

## Physical conversion proof

Write h=s+z-Ts, where s belongs to the finite physical span and z,T s
belong to its orthogonal complement. The existing energy completion gives

```
Q(h) >= tau x^2+c y^2,
||h||_2^2 <= x^2+(y+Lx)^2,
x=||s||_2, y=||z||_2.
```

Set mu=tau*c/[tau+c(1+L^2)]. The difference between the energy lower
bound and mu times the physical norm upper bound is the quadratic form
of

```
[ tau-mu(1+L^2)    -mu L ]
[ -mu L                c-mu ].
```

Its diagonal entries are nonnegative and its determinant is exactly mu^2>0,
because mu[tau+c(1+L^2)]=tau*c. Hence it is positive definite. This proves
the physical inequality for every vector in the actual supported form
domain, including complex vectors: x,y are their real nonnegative norms.

The old proof used the coarser inequality
||h||^2<=2(1+L^2)x^2+2y^2 and selected
min(tau/[2(1+L^2)],c/2)=1/(202*10^29).
Keeping the cross term in the scalar 2x2 inequality removes almost all of
that factor-of-two loss. It does not change any actual source data.
No optimality claim is made.

## Logarithmic conversion and lawful consequences

Combine Q>=mu physical mass and Q>=(1/10)Elog-23 physical mass.
With weight theta=mu/(mu+23) on the second inequality, the mass term cancels:

```
(1-theta)*mu-theta*23 = 0,
kappa=theta/10=mu/[10(mu+23)].
```

The displayed new kappa follows by exact rational substitution. The existing
physical support-inclusion argument gives the same bounds on smaller
windows. On the fixed dilated logarithmic carrier at 81/100, the operator
lower bound is at least kappa, and perturbations of norm at most kappa/2
preserve a gap kappa/2. Norm continuity still gives a strict neighborhood
to the right, with no numerical continuity modulus or new aperture.

## Validation and reproduction

The rational certificate checks the conversion matrix diagonals and exact
determinant, both improvements, and the logarithmic blending identity.
Thirty-six rational input controls also satisfy the general conversion.
Doubling the new physical coefficient makes its conversion-matrix
determinant negative and is rejected. A changed inherited note is rejected
by its pinned Git hash. Two runs produce byte-identical output.

```sh
python scripts/certify_native_schur_norm_conversion_081.py --output /tmp/schur-norm-conversion.json
cmp /tmp/schur-norm-conversion.json notes/data/RPB108_SCHUR_NORM_CONVERSION_081_20261006.json
```

These arithmetic checks verify this conversion and its input custody.
The universal scalar implication is proved above; the inherited analytic
source certificate is not freshly mechanically reproved here.

## Standing and next work

Historical proof notes and certificates keep their original wording and
constants. This additive result updates the current full-domain constants.
No actual selected off-line packet is instantiated. Global endpoint
exclusion, historical fixed witness attachment, F4 and FULL TRANSPORT CLOSED
remain open. No Lean or workflow edits and no CI run.

Next: make the complete Gram available in smaller exact chunks, or regenerate
it from the pinned source certificate, then test larger corrected matrix
shifts. The 10^(-18) raw finite bound cannot itself replace the corrected
10^(-29) Schur margin.
