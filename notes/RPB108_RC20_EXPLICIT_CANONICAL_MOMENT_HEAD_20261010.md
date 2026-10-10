# RPB108 RC20 — explicit canonical moment head with a whole-tail bound

2026-10-10. Independent route consolidation.
Parent: 3ffa3df22f6a0b91ec86f6424580a9f100a219dc (RC19).
Only research/rpb108-route-consolidation is written.

## Result

An explicitly specified canonical moment head of rank at most 460000
replaces RC19's abstract concentration eigenspace. Its WHOLE complementary
original-form floor at B=11/10 is

    9847/100000 >1/11.

The head is the span of the canonical Riesz representatives of physical
moments of degrees 0,...,459999. Its definition requires no concentration
diagonalization. Its canonical orthogonal projection and finite matrix
are nevertheless NOT numerically constructed here.

If that actual head has floor >=1/4000 and its actual canonical source
cross norm is <=1/300, the paid Schur reserve is

    48623/354492000 >0.

Neither actual bound is certified. The feature count is more than
65 times smaller than RC19's 30-million rank upper envelope, but a dense
matrix at this size remains prohibitive. No practical full matrix
algorithm or positivity at 1.10 is claimed.

## Definitions and pinned native input

Use RC19's supported logarithmic carrier D_B, physical inclusion
i:D_B -> L2(-B,B), and Fourier convention exp(-2pi i xi x).
The canonical norm is the physical Fourier norm weighted by
w(xi)=log(e+|xi|), and ||i||<=1.

Let J_T restrict Fourier(i h) to (-T,T). The actual bounded canonical
original-form operator is A_Q=I+i^*R_B i.
RC19 proves, for T=exp(10),

    A_Q >=(1/10)I_D -(153/10)J_T^*J_T.               (1)

This estimate retains the actual native digamma multiplier, every active
prime power and both signed pole moments. It is an original-form
estimate, not a phase-reference estimate.
RC19 pins the native identity to CC27 blob
e9a44661f94ee6750fc5ad1fbf7dc719fa3ba482 at CC119
5df347d3808ac3282864a657b7380e0f54bf4daa.
The present step uses (1) as its analytic input and introduces no new
special-function identity.

## Explicit finite approximation of the low band

For k>=0 define the bounded physical moment functional on D_B,

    ell_k(h)=integral_(-B)^B x^k (i h)(x) dx.

Cauchy--Schwarz and ||i||<=1 bound each functional by the physical L2
norm of x^k. Let r_k be its CANONICAL Riesz representative, with the
inner-product convention chosen so ell_k(h)=<r_k,h>_D.

Set n=460000 and define X_n:D_B -> L2(-T,T) by

    (X_n h)(xi)=sum_(k=0)^(n-1)
                  [(-2pi i xi)^k/k!]ell_k(h).

This is the Taylor approximation of the Fourier kernel in its real
phase variable 2pi xi x. It is finite rank and bounded: every coefficient
functional is bounded and every polynomial output is in L2(-T,T).

For |x|<=B and |xi|<=T, put z=2pi BT.
The real-phase integral Taylor remainder has absolute value at most
z^n/n!, since the derivative's exponential factor has modulus one.
The physical-to-frequency error kernel therefore has Hilbert--Schmidt
norm at most 2sqrt(BT) z^n/n!. Composing with i gives

    ||J_T-X_n|| <=2sqrt(BT) z^n/n!.                  (2)

No exp(z) factor is needed. This is a uniform operator bound for the
complete low band, not a collection of sampled Fourier values.

## Fresh exact rank and residual budget

Fresh rational Taylor bounds give exp(10)<22100 and e<11/4.
Together with the inherited pi<22/7,

    BT<24310,
    3z=6pi BT<(132/7)*24310=3208920/7<460000=n.

The integral comparison for log(n!) implies n!>=(n/e)^n.
Consequently

    z^n/n! <=(e z/n)^n <(11/12)^n
            <=(11/12)^128 <1/40000.

Also 2sqrt(BT)<312, since 4*24310<312^2.
Equation (2) gives

    ||J_T-X_n|| <312/40000 <1/100.                   (3)

The constants are deliberately conservative. The enormous true Taylor
exponent is never instantiated in a giant rational power; n>=128 and
the fixed rational power suffice for the residual proof.
No array of 460000 source columns or matrix entries is generated.

## Canonical head and entire original-form complement

Let P be the canonical orthogonal projection onto

    span{r_0,...,r_(n-1)},

and H=I-P. Equivalently, this span is range(X_n^*).
The frequency monomials defining X_n are linearly independent; its
adjoint range is exactly the span of the moment representers.
For h in range(H), every ell_k(h)=0 for k<n, hence X_n h=0.
Equation (3) therefore proves

    ||J_T H||<=1/100.

Inserting this into the inherited original-form inequality (1) yields

    H A_Q H >=[1/10-(153/10)*(1/100)^2]I_H
              =(9847/100000)I_H.                   (4)

This controls the entire infinite complement, including high frequencies
and the full signed native form. It does not infer positivity by checking
a finite sampled tail.

The physical polynomials x^k are not silently treated as canonical basis
vectors. It is their bounded moment FUNCTIONALS whose canonical Riesz
representatives define the head. The canonical metric and projection
remain necessary for a subsequent actual finite certificate.
The explicitly specified head differs from RC19's concentration head;
neither head's measured spectrum is known.

## Remaining actual head and source-residual gate

Let

    G=P A_Q P,
    Z=H A_Q P=H i^*R_B i P,
    D=H A_Q H.

Orthogonality is in D_B, so H I P=0.
The source residual Z includes the full actual bounded remainder,
including its signed pole and prime components; (1)'s lower envelope
does not replace the actual source columns.

Suppose certified actual bounds give G>=m I_P and ||Z||<=beta.
By (4), the finite Schur complement obeys

    G-Z^*D^(-1)Z
      >=[m-beta^2/(9847/100000)]I_P.

For m=1/4000 and beta=1/300,

    beta^2/(9847/100000)=10/88623,
    m-10/88623=48623/354492000>0.

The exact bounded Schur factorization would then prove original whole
positivity at B=11/10. No current result establishes either actual bound.
RC18's whole-source column-error interface applies only after constructing
a canonical orthonormal basis for THIS head and its actual sources.
Existing source data for a different projection cannot be substituted.

A small low-band residual alone is insufficient to bound the cross
block. For example, the generic physical inclusion bound on this tail
is only

    ||iH||^2 <=1/10000+1/10.

Combined with ||R_B||<=21, its resulting generic Schur cost fails badly.
The required beta is an actual source-specific obligation.
Positive head and tail blocks by themselves can also have a negative
coupled direction; the validator includes that control.

## Computational boundary

The former concentration diagonalization obligation is removed from the
HEAD DEFINITION. Canonical Riesz representation, stable basis construction,
actual finite head certification and complete source-residual estimates
remain. The n physical monomials are a mathematical definition, not a
recommended stable numerical basis: large-degree moment coordinates
can be badly conditioned. A stable basis with the same canonical span
would preserve (4), but its certified metric conversion is not supplied.

The 460000 bound does not show this many features are needed. It is a
constructive sufficient head size from a conservative Fourier--Taylor
bound. Further compression must prove the retained whole-tail inequality
or quantify the loss; deleting features by observed finite eigenvalues
alone is unsafe. No practical compressed head is produced here.

## Validation and standing

scripts/validate_rpb108_rc20_explicit_moment_head.py passes 18 exact rational
checks: exponentials, Fourier phase and factorial budgets, kernel residual,
whole-tail floor, rank comparison, conditional Schur reserve, adjoint-range
orthogonality, failure of the generic cross budget and unsafe block control.
The Fourier-kernel, Riesz-space and whole-complement arguments are analytic
proofs above; finite controls do not certify any actual source columns.

No canonical projection, actual head matrix or source residual is computed.
No original negative vector, new whole positivity at 1.10, RH/F4 theorem
or Lean closure is claimed. Existing 1.06 positivity and prior restricted
results remain intact. Other branches and historical files are unchanged.
