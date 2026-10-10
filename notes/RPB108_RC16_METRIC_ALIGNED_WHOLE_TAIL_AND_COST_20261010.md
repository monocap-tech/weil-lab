# RPB108 RC16 — metric-aligned whole-tail bounds and their rank cost

2026-10-10. Independent route consolidation.
Parent: 24cc1a67d5553972e216ca6a6f7215c662991305 (RC15).
Only research/rpb108-route-consolidation is written.

## Result and computational boundary

A complete normalized tail and cross-block estimate is proved for a precisely
defined finite space. The canonical finite space must be transformed by
A_F^(-1/2) before using its physical tail in the normalized correlation
screen; leaving the projection unchanged is invalid.

At cap 1.10, a canonical physical-tail bound delta=1/10^6 gives

    ||H_F K H_F|| <= 609/5000000000,
    ||H_F K P_F||^2 <= 5887/32656250.

If the ACTUAL finite normalized head has floor at least 1/4000, these bounds
pay the full Schur complement and certify original positivity on that cap.

A Fourier--Taylor construction provides the required finite space
analytically, but its explicit cutoff is T=exp(4*10^12) and the construction
uses at least (264/7)BT Taylor terms. It is computationally infeasible. No finite matrix of
that size is generated, and no actual finite head is certified.
This is a constructive whole-tail theorem and cost audit, not a practical
new aperture certificate.

## Definitions and pinned quantitative reference

Use the canonical supported logarithmic Hilbert carrier D_B with norm

    ||h||_D^2=integral log(e+|xi|)|Fourier(h)(xi)|^2 dxi,

and physical inclusion i=i_B:D_B -> L2(-B,B).
The Fourier convention is exp(-2pi i xi x), consistent with the inherited
digamma argument 1/4+i*pi*xi. In particular ||i||<=1.

The full native decomposition and weight are pinned through RC5 and RC15 to
CC27 and CC37, read at CC119 5df347d3808ac3282864a657b7380e0f54bf4daa;
CC37 blob a8a4ec58ebc43745d73630b97188cac1597b15ed identifies the weight
log(e+|xi|) and effective remainder.

RC15 supplies at B=11/10 the explicit smooth mask, positive phase-average
operator A=A_F and physical correction T_E, with

    A>=f I, f=1/2100,
    A>=gamma i^*i, gamma=627/16000,
    ||T_E||<=C, C=58.

These are conservative non-strict bounds for RC15's strict envelopes.
Define

    L_F=i A^(-1/2),
    K=L_F^*T_E L_F,
    Q=A^(1/2)(I+K)A^(1/2).

A is the reference operator, not the original form operator. Its physical
guard gives the useful complete bound

    ||L_F||<=1/sqrt(gamma).                            (1)

No positivity of Q at 1.10 is assumed.

## From a canonical physical-tail bound to the normalized tail

Let X:D_B -> L2(-B,B) be finite rank with ||i-X||<=delta.
Let P be the canonical orthogonal projection onto range(X^*), and H=I-P.
Then XH=0, so

    ||iH||<=delta.

Define the NORMALIZED finite projection P_F to be the orthogonal projection
onto A^(-1/2)range(P), and H_F=I-P_F.
For y in range(H_F),

    <A^(-1/2)y,p>_D=<y,A^(-1/2)p>_D=0
    for every p in range(P).

Thus A^(-1/2)y lies in range(H). This exact alignment yields

    ||L_F H_F|| <= delta/sqrt(f).                      (2)

The head is transformed by A^(-1/2), not A^(1/2). It is not generally P.
Combining (1)--(2) with K=L_F^*T_E L_F proves the WHOLE-space estimates

    tau := ||H_F K H_F|| <= C delta^2/f,
    rho^2 := ||H_F K P_F||^2 <= C^2 delta^2/(f gamma). (3)

Both bounds concern the entire complement, not a sampled finite tail.
They retain every physical prime, archimedean and signed pole contribution
inside the actual bounded correction T_E.

An exact two-dimensional control illustrates the alignment:
take A^(-1/2)=[[2,1],[1,2]] and P=span(e1).
The transformed head is span((2,1)); its orthogonal vector (1,-2) maps
to (0,-3), which lies in canonical H. The untransformed tail e2 instead maps
to (1,2), containing a head component. Smallness on H cannot be applied
to that untransformed normalized vector.

## Constructing X with an explicit rank bound

For any T>0, split the physical Fourier transform at |xi|=T.
The high-frequency part, restricted back to (-B,B), obeys

    ||high part||_2 <= [log(e+T)]^(-1/2)||h||_D.        (4)

For the low-frequency inverse transform, approximate exp(2pi i xi x) by
its Taylor polynomial with n terms (degrees 0,...,n-1).
At |x|<=B, |xi|<=T, put z=2pi BT.
The REAL-phase Taylor remainder is at most z^n/n!: the integral remainder
uses |exp(i t)|=1 and needs no exp(z) factor.

The resulting reconstruction X_{T,n} has range in the span of the n
physical polynomial functions 1,x,...,x^(n-1) on (-B,B). Its coefficient
functionals are the bounded moments of Fourier(h) over [-T,T].
It is a bounded finite-rank map on D_B; the physical polynomials are not
silently treated as canonical orthonormal vectors.
Cauchy--Schwarz on the frequency band and physical interval gives

    ||i-X_{T,n}|| <=
      [log(e+T)]^(-1/2)+2sqrt(BT) z^n/n!.              (5)

The finite canonical feature space is range(X_{T,n}^*), defined by the
Riesz representatives of those bounded moment functionals. No physical
projection is substituted for its canonical orthogonal projection.

For a desired delta, choose

    T=exp(4/delta^2).

Then the first term in (5) is strictly below delta/2.
The integral bound for log(n!) gives n!>=(n/e)^n; e<3 implies

    z^n/n! <= (3z/n)^n.

Using the inherited pi<22/7, choose an integer n satisfying both

    n >= (264/7)BT,
    2^n >= 4sqrt(BT)/delta.

The first condition implies n>=6z and bounds the remainder by 2^(-n);
the second pays the low-frequency term by delta/2.
Thus ||i-X_{T,n}||<=delta. This proves a finite whole-tail construction
for every positive delta. It does not numerically instantiate the huge n.

## Quantitative cap-1.10 Schur gate

With C=58, f=1/2100, gamma=627/16000 and delta=1/10^6, equations (3) give

    tau <= 609/5000000000 <1/10^6,
    rho^2 <= 5887/32656250 <1/5000.

Consequently

    rho^2/(1-tau)
      <=188384000/1044999872719
      <1/4999 <1/4000.

If the actual normalized head P_F(I+K)P_F has floor m>=1/4000,
its Schur reserve is at least

    1/4000 -188384000/1044999872719
      =291463872719/4179999490876000 >0.

RC14's exact block identity would then prove whole original positivity
at B=1.10. No assertion is made that this actual head floor holds.
The numerical constants certify (3) for the mathematically defined
projection; they are not observed spectral values.

## Cost audit and what must improve

Here T=exp(4*10^12) and n is at least (264/7)BT. The number of head features
is therefore enormous. The construction quantifies compactness but does
not offer a feasible matrix computation or a cheaper alternative to the
existing source-response certificates.

The logarithmic carrier permits slow uniform L2 Fourier-tail decay:
small delta requires an exponentially large generic cutoff in this bound.
The normalized cross cost also carries the factors 1/f and 1/gamma.
Neither shrinking the masks nor computing a few low modes removes these
whole-space costs.

A practical implementation requires a substantially sharper approximation
of the ACTUAL correlation operator or source profiles, with its metric
alignment and whole tail certified. It must then evaluate the finite head.
This step provides no such sharper rate or arithmetic head estimate.

## Fresh validation and standing

scripts/validate_rpb108_rc16_metric_aligned_tail.py passes 24 exact rational
checks: the complete normalized tau and rho budgets, paid Schur reserve,
Fourier cutoff exponent, Taylor remainder controls, and the correct versus
incorrect metric alignment. The infinite-space approximation and norm
arguments are analytic proofs above; finite controls do not replace them.

No actual finite matrix or correlation spectrum is evaluated. The explicit
finite space is specified mathematically, not generated computationally.
The original whole 1.06 certificate and prior restricted theorems remain
intact. No whole positivity at 1.10, original negative vector, RH/F4 theorem
or Lean closure is claimed. Other branches and historical files are unchanged.
