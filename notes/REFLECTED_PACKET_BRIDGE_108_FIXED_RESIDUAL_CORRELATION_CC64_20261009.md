# CC64: original residual transfer and correlation with nonzero measured sources

Read [definitions](../docs/TERMINOLOGY_RPB108_FIXED_RESIDUAL_CORRELATION_CC64.md) first.

## Recovered arithmetic and exact replay

Integration parent CC63 de08033d192b85da27f11e52d3b74c7404ff6ea1 and read-only
Phase Geometry NF24 b7fa4461ab4cca2ebc9383ae4b9407c03a580826 were recovered.
NF24's authenticated target producer was replayed on the three original
source archives and NF18 seed file. Its target JSON agrees exactly.
Its projection validator was replayed on the published compressed source;
every replay output field equals the corresponding upstream certificate.
The 116 new original records give 464 ordered component interval checks,
with original arch/prime/pole/full compatibility and raw source SHA256
4c8b0067088486e20f31a7904d3bf56a9f654e982b15450efa85cd6b25e24346.

The native source builder itself was read and hashed but not rerun in this
consumer. The complete-source numerical diagnostic was not rerun and has
no certified integration remainder. Upstream results are not silently
reclassified as consumer-produced native intervals.

The NF24 target and CC63 trial are DISTINCT exact vectors. Both have the
same retained rational seed, but denominator10^80 versus10^75 high
coefficients. Their squared physical difference is below2e-150.
Rather than infer source continuity from this tiny physical difference,
the consumer directly evaluates the authenticated new signed source
columns on each CC63 vector. This avoids any assumed boundedness of L.

| Certified CC63 consequence | Even | Odd |
| --- | ---: | ---: |
| New original high coordinate | e118 | e117 |
| Strict coordinate square / Q(p) bracket | (0.0284,0.0285) | (0.0298,0.0300) |
| Complete high residual nonzero | yes | yes |
| Coarse residual gate decided | no | no |

The [exact consumer certificate](data/RPB108_FIXED_RESIDUAL_CORRELATION_CC64_CERTIFICATE_20261009.json)
records the pairings and full error budgets.
A single nonzero coordinate is not a collective lower frame.

## Uniform source reconstruction precision

NF24's endpoint cancellation preserves the singular source exactly and
reduces the regular-kernel approximation error to convolution with
r-r_320. The integral Schur estimate gives

    ||(L_arch-L_arch,320)p|| <= 2a epsilon ||p||,
    epsilon=4(106/125)^320/(1-106/125),
    2a epsilon<7e-22.

This bounds the approximation ERROR for every supported polynomial,
independently of degree; it does not bound the original logarithmic L on
all physical L2. CC63 masses are below1001/1000. Add its retained projection
center error8e-60 to the arch error. Using CC63's conservative LOWER energy
thresholds, the resulting sufficient reconstructed-residual-square budgets
retain more than999/1000 of kappa times the lower energy.
Thus the already certified reconstruction accuracy is adequate for this
directional test. Actual signed source size and rigorous integration,
including prime and pole construction errors, remain obligations.
No full norm is certified by this error budget.

## Correlation bound without exact measured annihilation

Let C=[[C2,K*],[K,D_U]]>=kappa I and r=(u,v), where u=H*r is the actual
nonzero measured residual. Both high polynomials have complete physical
sources G=CH, after subtracting their entire retained projections.
Put P=r*r, D=G*G, z=G*r and

    V=D-kappa C2=C2(C2-kappa I)+K*K>0,
    zbar=z-kappa u=(C2-kappa I)u+K*v.

For ANY exact finite Y, complete the response square:

    <r,C^-1 r>
      =2 Re(u*Y)-Y*C2Y+<r-GY,C^-1(r-GY)>
      <=2 Re(u*Y)-Y*C2Y+||r-GY||²/kappa.

The quadratic numerator is P-2 Re(Y*zbar)+Y*VY.
Its minimum, attained at Y=V^-1 zbar, yields

    T_full=<r,C^-1 r> <= (P-zbar*V^-1 zbar)/kappa <= P/kappa.

This is CC59's correlation credit extended to a fixed trial with u != 0.
Setting u=0 recovers its zero-measured-source case. Dropping -kappa u
without payment is not justified by saying that u is tiny. Nor does a tiny
u alone bound ||K C2^-1 u||: complete high source information is needed.

For one fixed retained seed the corrected energy remains Q(p)-T_full.
Consequently

    P-zbar*V^-1 zbar < kappa Q(p)

is sufficient. It needs only the complete joint Gram of the THREE physical
high sources r,G1,G2 per parity, together with the known C2 and u.
Full56-dimensional collective transport still requires collective data.

A rational Y avoids certifying an inverse. Reconstruct the combined
polynomial source r-GY directly, retain all original signed sectors and
projection coefficients, and enclose its norm. If an approximant has
squared-norm upper B and physical L2 error eta, pay
||r-GY||² <= (sqrt(B)+eta)^2 before dividing by kappa; alternatively use
Young's rational bound (1+t)B+(1+1/t)eta².
The finite correction 2 Re(u*Y)-Y*C2Y must also be outward enclosed.
Use a LOWER Q(p) enclosure. This is a concrete directional interface,
not an evaluated native correlation certificate.

## Scope of sharpness and controls

The least high completion compatible with C2,K and kappa is

    D_min=kappa I+K(C2-kappa I)^-1 K*.

It attains the response majorant for arbitrary r, including nonzero u.
Equivalently C_min=kappa I+R(C2-kappa I)^-1 R* with
R=[C2-kappa I;K]; the finite-rank inverse gives the displayed credit.
Additional original arithmetic may improve it. This is not a logical
nonimplication statement about the complete Weil identities.

The [Fraction validator](../scripts/certify_fixed_residual_correlation_cc64.py)
tests c=3,k=3,kappa=207/1000, u=1/1000, v=1 and a genuinely fixed trial
p=x+(1/7)h. It verifies the nonzero-source formula, rational-Y identity,
attainment at D_min and four unknown-high increments.
A continuous original full-form family has exact Schur levels
-1/100,0,+1/100: the corrected bound crosses at the actual null while the
coarse estimator fails at all three. An orthogonal unit tail receives no
correlation credit. Three genuine positive ground levels
1e-40,1/100,1/20 use Q_0+mu I on the WHOLE physical mass; only that whole
shift creates a null. No positive original eigenlevel is relabeled as zero.
These are abstract controls of the estimator, not actual Weil models.

## Numerical guidance and remaining arithmetic

NF24's unproved quadrature diagnostics give residual-square/Q(p) near
0.3500748 even and0.2802820 odd, above kappa0.207. These refer to the
NF24 vectors, not automatically to CC63. If such ratios were rigorously
confirmed, correlation credit exceeding approximately0.1430748 Q(p) even
or0.0732820 Q(p) odd would suffice, using the exact energy enclosure and
error payments. They are guidance, not achieved native credit.

Next load-bearing arithmetic: rigorously evaluate the complete signed
three-source directional Gram or a paid rational-Y combined residual,
then test the corrected correlation gate. The finite Bessel observations
neither prove nor refute its success. Do not build the full matrix on the
assumption that the scalar-floor gate must pass.

CC62's original E2+F112 gap1/100 and whole-domain anchor21/20 remain.
Whole target53/50 positivity, uniform all-cap old-gap-independent leakage,
defect-relative collective frame, actual null exclusion, RH/F4, full
transport and Lean remain open. Paused fronts and historical wording are
preserved; no independent source producer is duplicated.
