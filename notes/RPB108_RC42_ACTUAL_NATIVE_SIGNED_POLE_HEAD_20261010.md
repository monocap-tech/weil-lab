# RPB108 RC42 — actual native signed-pole head and whole-source bounds

2026-10-10. Parent RC41: `6b01958faf05f355a42efb7eb5699b92e7f97b94`.
Only `research/rpb108-route-consolidation` is written.

## Result

All 36 upper-triangular entries of the original signed-pole contribution
to the actual first eight native Riesz features are now rigorously enclosed.
The actual pole head has rank two and inertia (one positive, one negative,
six zero). Opposite-parity entries are exactly zero.

The entire canonical pole operator has norm below 4.776523. Its negative
part has norm below 0.462126. Whole canonical pole-source Gram bounds are
also certified in the actual native metric, separately by parity.

These are actual original-form component bounds, including both signed
cross-paired pole moments. They do not certify the full original Weil head
or its combined source covariance. There is no new aperture positivity.

## Original form custody and definitions

The unchanged carrier is D_B at B=11/10 with physical inclusion i and
logarithmic Fourier weight log(e+|xi|). RC32 supplies ||i||^2<=rho=252/257.
The original form is pinned to CC27 blob
`e9a44661f94ee6750fc5ad1fbf7dc719fa3ba482`, inherited through RC21/22.
Its pole term is exactly

    Q_pole(h,f)=conjugate(m_-(h)) m_+(f)
                 +conjugate(m_+(h)) m_-(f),
    m_+(h)=integral i h(x) exp(x/2) dx,
    m_-(h)=integral i h(x) exp(-x/2) dx.

Let c(x)=cosh(x/2), s(x)=sinh(x/2). The physical operator is

    K_pole=2|c><c|-2|s><s|.

Its actual canonical lift is

    A_pole=i^*K_pole i
          =2|i^*c><i^*c|-2|i^*s><i^*s|.

For R the actual low-eight native Riesz feature map, define the **signed
pole head** as H_pole=R^*A_pole R and the **pole source map** as
sigma_pole=A_pole R. Neither definition replaces the full A_Q or its full
remainder source map. All these adjoints use the actual canonical metric.

## Actual native moment enclosures

RC39 supplies the polynomial trial V, the exact physical native Gram
P_phys, and the whole canonical error bound

    (R-V)^*(R-V)<=beta P_phys,
    beta=91276884027/64250000000000.

Reflection is unitary on the logarithmic carrier, so r_j and v_j have
the parity of j. Put u_j=m_+(r_j), then

    m_-(r_j)=(-1)^j u_j.

For even j, u_j is the c moment; for odd j it is the s moment. Their
physical functional norms are exactly

    ||c||_2^2=B+sinh B,
    ||s||_2^2=sinh B-B.

Consequently, writing u_trial,j=m_+(v_j), the rigorous error is

    |u_j-u_trial,j|^2 <=rho beta (P_phys)_jj n_j,
    n_j=B+sinh B  for even j,
    n_j=sinh B-B  for odd j.

The JSON stores these two positive norms explicitly.

Trial moments are integrated by a degree-80 rational Taylor polynomial
for exp((B/2)t). On |t|<=1 its uniform tail is at most

    2(B/2)^81/81! <10^(-140).

The ratio of successive omitted terms is below 1/2. Since |P_n(t)|<=1,
the trial integral tail is bounded by 2B times this tail times the sum
of absolute Legendre coefficients. All bounds include the emitted
rounded RC38 coefficients directly. Directed 220-digit Decimal arithmetic
encloses square roots and sinh; final endpoints are outward rational.

Some representative actual moment enclosures are

| Native feature | Lower u_j | Upper u_j |
| --- | ---: | ---: |
| 0 | 2.052432101236 | 2.225225082052 |
| 1 | 0.333434128240 | 0.364464690523 |
| 2 | -0.798739924120 | -0.680699846311 |
| 3 | -0.257015266274 | -0.219557600426 |

All eight enclosures and all head entries are in the certificate.

## Signed head attachment and rank

For equal parity, the exact actual entry formula is

    (H_pole)_ij=2(-1)^i u_i u_j;

for opposite parity the entry is zero. The even block is a positive
rank-one outer product; the odd block is a negative rank-one outer product.
Certified u_0>0 and u_1>0 show both ranks are exactly one, hence the stated
inertia. This is a component inertia, not a negative vector for full Q.
Diagonal intervals retain their exact nonnegative/even or nonpositive/odd
sign even when a moment interval contains zero.

For example the native (0,0) pole entry is contained in
[8.424955060368,9.903253331587], and the native (1,1) pole entry in
[-0.265669021277,-0.222356635750], with outward display endpoints.
The rational JSON endpoints are authoritative.

## Whole canonical source control

The canonical images i^*c and i^*s are orthogonal by reflection parity.
Define outward rational bounds

    k_even>=2rho(B+sinh B)=4.77652266514786...,
    k_odd >=2rho(sinh B-B)=0.462125777988327... .

The exact stored fractions are slightly outward; displayed decimals are
for orientation. These give the actual generalized head inequality

    -k_odd M <=H_pole<=k_even M,  M=R^*R,

and the full canonical source Gram estimate

    sigma_pole^*sigma_pole <=k_even^2 M.

Within odd parity the sharper bound is k_odd^2 M_odd. More precisely the
source Gram has zero opposite-parity blocks and is bounded by
k_even^2 M_even plus k_odd^2 M_odd. The even squared bound is about
22.815169; the odd squared bound is about 0.213561. These control the
entire canonical source, without sampling a complementary tail. They are
conservative norm bounds, not an evaluation of its exact source Gram.

They do not pay RC22's full combined residual requirement. In particular
the archimedean, prime, and pole sources must be combined with all their
cross correlations; the norm or inertia of this one component does not
decide their sum.

## Validation and scope

Generation and independent replay pass:

    python scripts/validate_rpb108_rc42_native_signed_pole_head.py
    python scripts/validate_rpb108_rc42_native_signed_pole_head.py --replay certificates/rpb108_rc42_native_signed_pole_head.json

The replay uses Rodrigues' formula and integration by parts to obtain the
positive, cancellation-free series

    integral_(-1)^1 exp(k t)P_n(t)dt
      =sum_(l>=0) 2^(n+1)k^(n+2l)(l+n)!/[l!(2l+2n+1)!].

It encloses the remainder after l=40, independently checks all eight trial
moments against the emitted intervals, rechecks each actual-moment radius
by exact rational squaring, and verifies every head-entry interval, both
signed norm budgets, source bounds, and the rank/inertia controls.

The source SHA-256 binds RC39's certificate bytes. The analytic Riesz,
reflection, and rank-two operator arguments are documented here, not
Lean-certified. Python Decimal's documented correctly-rounded elementary
operations remain the same enclosure assumption as RC30 onward.

All historical results remain intact. The full 8600-feature head is not
constructed. The original archimedean remainder and active prime sources,
their combined covariance, the original Weil head floor, new whole-aperture
positivity at 1.10, RH/F4, and Lean closure remain open.
