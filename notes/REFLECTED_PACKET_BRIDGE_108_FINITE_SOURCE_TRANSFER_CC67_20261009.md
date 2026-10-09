# CC67: finite original source transfer and actual CC65 full-source diagnostics

Read [definitions](../docs/TERMINOLOGY_RPB108_FINITE_SOURCE_TRANSFER_CC67.md) first.

## New rigorous finite-source estimate

At a=53/50, for EVERY physical normalized Legendre mode e_n with n<=115,

    ||L_a e_n||_2 < 200000.

This deliberately coarse original arithmetic upper bound is useful for
tiny coefficient perturbations. It is neither a physical boundedness
claim for the full logarithmic operator nor a near-critical lower frame.

Use NF24's exact original arch source identity:

    L_arch p=c p-(p/2)log(a²-x²)+S_p(x)
             -integral_-a^a r(|x-y|)p(y)dy,
    S_p(x)=(1/2)integral_-a^a (p(x)-p(y))/|x-y| dy,
    c=-gamma-log(2pi).

For normalized e_n, |e_n|<=sqrt((2n+1)/(2a)).
The identity P_n'=sum_(j=n-1,n-3,...) (2j+1)P_j and |P_j|<=1 give
|e_n'|<=sqrt((2n+1)/(2a))*n(n+1)/(2a).
The singular difference term consequently has L2 norm at most
[n(n+1)/2]sqrt(2n+1)<106720 for n<=115, using sqrt(231)<16.

The logarithm is retained exactly. Each log(a plus/minus x) has squared
norm 2a[(log(2a))²-2log(2a)+2].
Since 0<log(53/25)<1, triangle inequality and the normalized sup bound
give a safe endpoint contribution<48. The constant contribution is<4:
0<gamma<1 and log(2pi)<log8<3.

NF22's original analytic Cauchy coefficient bound |h_m|<=10/(5/2)^m,
where j(t)=h(t)/t and r(t)=j(t)-1/(2t), yields

    sup_[0,2a]|r| <= (10/(5/2))/(1-106/125)=500/19.

The integral Schur bound for the regular convolution is
2a*500/19=1060/19. There are exactly six original active prime powers
2,3,4,5,7,8, each in both orientations. Each translated restriction has
physical operator norm<=1 and each weight<log8<3; their total norm<36.
The two original signed pole sources have integral kernel
exp((x-y)/2)+exp(-(x-y)/2). Its Schur norm is at most4a exp(a)<4a*9,
because a<2 and e<3. Thus its contribution is<954/25.

Adding the six rational sector bounds gives less than200000.
The bounds on gamma and e follow from harmonic-integral comparison and
the elementary factorial series; log(2a)<1 follows from e>5/2.
No sampled source values or numerical quadrature prove this estimate.
The [Fraction validator](../scripts/validate_finite_source_transfer_cc67.py)
checks the rational arithmetic; the analytic derivation above is the proof
of the individual bounds. It is not asserted to be a Lean certificate.

## Tiny finite corrections now have paid complete-source errors

For a two-high coefficient difference beta,

    ||L_a(H2 beta)|| <= 200000(|beta1|+|beta2|)
                       <=400000||beta||_2.

This applies to the complete signed source, not merely the measured rows.
Physical projection onto F112 cannot increase the error.

Direct exact comparison of the NF24 and CC63 coefficient integers gives
complete original source difference<8e-70, with their retained coefficients
identical. This pays transfer between the distinct rational vectors without
assuming a bounded full L on physical L2.

More importantly, let u=Q(H2,p) for the fixed CC63 trial and
p_exact=p-H2 C2^-1 u. CC63 certifies ||u||²<2e-120; the original C2 lower
bounds are14/5 even and289/100 odd. Consequently

    ||L_a(p-p_exact)||_2 <4e-55,
    0<=Q(p)-Q(p_exact)=u*C2^-1 u <1e-120.

Both inequalities are original finite-source estimates independent of the
old retained gap. They show exactly why the tiny measured residual can be
removed after paying its effect on ALL high coordinates. They do not make
that effect zero, and do not evaluate the full source of either trial.

CC64's warning that a tiny u alone does not bound the K effect remains
correct under its earlier partial-data hypotheses; the original finite
upper bound proved here supplies the missing perturbation payment.
It does not supply the much larger correlation credit needed for a sign.

## Existing diagnostic rerun on exact CC65 inputs

The unchanged
[NF24 diagnostic](https://github.com/monocap-tech/weil-lab/blob/b7fa4461ab4cca2ebc9383ae4b9407c03a580826/scripts/diagnose_native_compensated_source_nf24_106.py)
was fetched and hashed. It was run on the exact published CC65 combined
polynomials at inner/outer orders96/64 and128/96, with90-digit Decimal
arithmetic. The [compatibility input](data/RPB108_CC65_DIAGNOSTIC_INPUT_CC67_20261009.json)
explicitly marks the new exact vectors; inherited field names do not
assert exact Galerkin minimization or identify them with NF24's vectors.

| Non-certifying quantity | Even | Odd |
| --- | ---: | ---: |
| Full high source-square / Q(v), larger order | 0.349005186472 | 0.280227000160 |
| Omitted source-square / CC65 budget, smaller order | 1.794087136389 | 1.412491629397 |
| Omitted source-square / CC65 budget, larger order | 1.794087136386 | 1.412491629394 |

The independent orders agree to relative discrepancy below1e-10.
Numerical full-minus-high source squares agree with the exact retained
projection ledger to relative discrepancy below1e-10. The numerical
e118/e117 projections agree with the authenticated original coordinates
to relative discrepancy below1e-10. All checks pass.

[Raw outputs](data/RPB108_CC65_SOURCE_DIAGNOSTICS_CC67_20261009.json) and
[validation](data/RPB108_FINITE_SOURCE_TRANSFER_CC67_VALIDATION_20261009.json)
keep the diagnostics explicitly NON-CERTIFYING. There is no rigorous
quadrature remainder. These ratios therefore do NOT prove that the native
CC65 scalar gate fails; no negativity, null or RH consequence follows.

The diagnostics suggest that the observed correction mildly improves the
complete source score but remains insufficient. That is useful routing
information, not a rigorous native sign decision. The new finite transfer
estimate cannot turn unproved quadrature into a certificate.

## Next and unchanged standing

The original arithmetic producer has not advanced past NF24 at recovery.
Next certify the complete source-square comparison, or evaluate the
source-aligned three-source correlations before choosing another frozen
correction. Do not treat numerical agreement as the missing theorem.

CC65's strict omitted-source budgets remain untested rigorously. Whole
anchor21/20 and CC62 E2+F112 gap1/100 remain. Whole53/50 positivity,
cap-uniform old-gap-independent leakage, defect-relative collective frame,
actual null exclusion, RH/F4, transport and Lean remain open.
Historical wording, independent source ownership and paused fronts are
preserved.
