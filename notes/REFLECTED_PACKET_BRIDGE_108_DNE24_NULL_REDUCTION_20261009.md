# RPB108 — DNE24: exact 104-dimensional actual-null reduction

Definitions precede use in the additive [DNE24 terminology](../docs/TERMINOLOGY_RPB108_DNE24_NULL_REDUCTION.md).
Write branch: research/rpb108-direct-null-exclusion.
Parent DNE23: 7c413f783061dc790a14b8b49628df0710aecb1e.
Read-only Phase NF34: f353936b780a4d988ec242a647ab985404f5b69e.
Read-only Coupled CC77: 2671eda30be8b08f36ae3a07c23f5391ab292798.

## Result

DNE23's eight-direction restriction with every original high mode can be
eliminated as one positive block. DNE24 constructs and checks the exact
physical orthogonal retained complement: 52 directions in each parity,
104 in total. The original unshifted actual-null equation is equivalent
to a unit-eigenvalue problem for one finite 104-dimensional positive
response matrix K. Computing that complete response remains open.

There are two additional analytic consequences of the inherited block
positivity: the original nullspace has dimension at most 104, and every
strictly negative form subspace has dimension at most 104. Each parity
has the sharper bound 52. These bound multiplicity and negative index;
they do not prove that either is zero.

| Exact remaining quantity | Even | Odd |
| --- | --- | --- |
| Independent complement columns | 52 | 52 |
| Constraint pivots, in parity coordinate indices | 0,1,2,3 | 0,1,2,3 |
| Inherited raw physical native energy gap | >5.58847e-22 | >3.62216e-19 |
| Maximum possible actual null multiplicity | 52 | 52 |
| Maximum negative form index | 52 | 52 |

The remaining native energy is positive. The unproved quantity is the
complete reaction through the eliminated positive block, including its
eight retained directions and all infinite high modes.

## Exact basis and inherited native sign

In one parity let Z have the four rows (low,x,w,u), where x,w and u are
the authenticated NF24, NF27 and NF32 retained vectors. Rational row
reduction selects four independent pivot columns P. For each nonpivot j,

    W_j=e_j-sum_i [(Z[:,P])^-1 Z[:,j]]_i e_{P_i}.

Every constraint pairs to zero with every W_j, and the 52 free rows are
the identity. Hence the columns are independent and span exactly the
physical orthogonal complement of these four directions. Their mass
matrix is G=W*W, not the coordinate identity.

Every W_j also satisfies NF31's two constraints against x and w. An
explicit exact reconstruction in that authenticated 54-column raw
constraint basis verifies this inclusion. Consequently the original
native matrix B satisfies B>=beta G with NF31's original physical beta.
No new original source calculation is needed for this inherited sign.
The finite shared high lifts from NF33 or NF34 are not substituted for
this raw native matrix.

The certificate stores the exact pivot matrix inverse, determinant,
pivots and free indices. Its basis rule together with the authenticated
existing input vectors specifies every rational column without copying
the much larger dense 56-by-52 array.

## Exact reduction of the original null equation

Write the full original physical form domain as H plus W104, where
H=Z8+F112. This is an orthogonal physical splitting. The closed form
restriction to H is coercive by DNE23: H_op>=delta I, delta=10^-36.
The restriction is closed: the finitely many retained orthogonality
conditions defining H are continuous in the original form norm. The
inherited original source construction puts each finite polynomial W
column in the physical operator domain, with its endpoint logarithms
and all prime translations in L2. Thus J=P_H L_original W is a bounded
finite-column source map into physical H.

For h=y+W a, completing the original positive block gives

    Q(h)=Q_H(y+H_op^-1 J a)+a*D a,
    D=B-J*H_op^-1 J.

The inverse is the original restricted form inverse, not a numerical
evaluation or a replacement by a scalar floor. A weak original null
tested against every vector in H first satisfies

    y=-H_op^-1 J a.

Testing against every W column then gives D a=0. Conversely these two
identities imply the original weak null equation on the entire form
domain. The coercive form solution belongs to the restricted form domain;
the full weak equation supplies the operator null realization. If a=0,
then y=0. Hence projection to W104 is injective on the full nullspace.

Since B is positive definite, define

    K=B^-1/2 J*H_op^-1 J B^-1/2,
    D=B^1/2 (I-K) B^1/2.

The exact equivalence is

    original actual null <=> eigenvalue 1 occurs in K.

The retained coefficients are a=B^-1/2 b for a unit-response eigenvector
b; the high and tested retained coordinates are recovered by the first
identity. Reflection makes K block diagonal into two 52-dimensional
problems. No entries of K are computed here.

## Sign, multiplicity, and the next response estimate

The completed-square change of variables is an invertible map on the
form domain. The positive H block contributes no null or negative
directions. Therefore nullity and negative index equal those of D and
are at most 104, or 52 per parity. A direct dimension proof also works:
any subspace of dimension greater than 104 has a nonzero vector with
zero W coordinate, which lies in the strictly positive H restriction.

K<I is sufficient and necessary for strict full positivity, given these
inherited positive blocks. Absence of eigenvalue one is sufficient and
necessary for actual-null exclusion at this fixed aperture. The latter
does not exclude negative directions. At a separately established first
contact where the full form is nonnegative, K<=I and the obstruction is
its top eigenvalue reaching one. Full nonnegativity at 1.06 is not assumed.

One conservative sufficient source estimate follows from the physical
gap: H_op^-1<=delta^-1 I. Thus

    ||J B^-1/2||^2 < delta

would certify K<I. This estimate is not claimed, and delta=10^-36 makes
it demanding. The sharper target is the response in the actual H_op
inverse metric. A complete raw F112 source Gram, by itself, omits the
reaction through the retained part of H. A selected shell omits most
of J. The fixed-aperture exact reduction tells us precisely which mixed
response must be controlled; it does not create an all-aperture estimate.

## Relation to the new read-only heads

NF34's expanded corrections lie entirely in high modes and target the
same inherited NF32 retained probe. Their improved directional source
ratios are useful response evidence, but their retained range is already
inside Z8. They therefore do not increase the DNE23 dimension count.
The NF34 report itself leaves its mixed source crosses and collective
remaining Gram open. CC77 transfers the rejection of the older H2 lift
at its inherited floor and localizes the source outside its selected
shell. Neither result evaluates K or contradicts the positive H block.
Only the DNE branch is modified.

## Validation and reproduction

Two fresh exact basis consumers give byte-identical certificates, each
passing 11664 explicitly counted rational assertions. A separate
validator passes 1138 checks. It uses permutation determinants, cofactor
inverses and Cramer's rule independently of the producer's row reduction.
It verifies the exact 52-column constraints and includes three genuine
finite positive/null/negative crossings, 147 completed-square identities,
nonorthogonal coordinate rescaling and a positive ground-level control.

For the last control, the original matrix [[3,2],[2,3]] has ground level
one. Shifting BOTH physical masses by one gives a null; shifting only
the remainder misses it. This preserves the whole-mass distinction from
the original source workflow. A true response diag(2,1/2) has norm above
one but no unit eigenvalue, checking that a loading inequality alone is
not an exact-null diagnosis. These are abstract controls, not actual
Weil countermodels. Python syntax compilation passed.

From the repository root:

```sh
python3 scripts/certify_dne24_null_reduction.py notes/data/RPB108_DNE15_NF24_TARGETS_20261009.json.gz.b64 notes/data/RPB108_DNE20_NF27_INPUT_20261009.json notes/data/RPB108_DNE22_NF32_TRIAL_20261009.json notes/data/RPB108_DNE21_NF31_INPUT_20261009.json.gz.b64 notes/data/RPB108_DNE23_EIGHT_DIRECTION_CERTIFICATE_20261009.json --output /tmp/dne24.json
```

Run again with a separate output for replay. The validator takes these
same five inputs, certificate, replay, and output path as positional
arguments. Authenticated source hashes and output hashes are in custody.
No expensive complete original source producers are rerun; no actual
inverse response, new directional source, or new positivity dimension is
claimed. The analytic reduction is an argument from the inherited closed
form and original-source theorems, not a Lean proof.

Whole 1.06 positivity, a unit-response exclusion on W104, reusable
all-aperture continuation, RH/F4, full transport and Lean remain open.
