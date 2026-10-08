# RPB108 CC24: unconditional pair correlation and finite exceptions

Date: 2026-10-08 UTC. Coupled parent: 4aaedf7b809660b971b40e4b8b5a05110f3a1d3a.
Definitions: [pair correlation and critical covariance](../docs/TERMINOLOGY_RPB108_PAIR_CORRELATION.md).

## Outcome

A genuine unconditional zero-pair correlation theorem is available without RH. Its statistic retains horizontal displacements and has uniformity on 0<=alpha<=1. It nevertheless does not provide the required adaptive, inverse-defect-weighted original source covariance.

We prove a specific limitation rather than merely observing that the formulas look different: this published asymptotic is stable under a finite reflected off-line perturbation, with normalized change O(T^(-1/8)) under our accepted displacement strip. Vertical PCC is also insensitive to finite location changes at its microscopic scale. A complete physical hyperbolic-source pulse control shows how a finite off-line quartet can create exponentially growing negative energy against a complete critical-line background. The two statements identify why location averages, even strong ones, cannot alone certify an every-cap statement that excludes finite exceptional locations.

The modified dictionaries are NOT the actual zeta divisor and do NOT retain the native Weil explicit formula. No logical independence from the complete ORIGINAL Weil identities is proved. The rejected transfer is from these specified averaged pair-correlation data alone to the required uniform source covariance. No new actual shell budget or aperture is certified.

## 1. Primary theorem and separate conjectural comparison

Read Baluyot, Goldston, Suriajaya and Turnage-Butterbaugh, An unconditional Montgomery Theorem for Pair Correlation of Zeros of the Riemann Zeta Function, arXiv:2306.04799v1, Theorem 1, equation (2.1) and Lemma 3:

https://arxiv.org/html/2306.04799v1

Writing rho=1/2+beta+i theta in OUR centered convention, their scalar statistic is

    F(x,T)=sum x^(rho-rho') w(rho-rho'), w(u)=4/(4-u^2).

For C_T=(T/(2pi))log T, the unconditional result is

    F(T^alpha,T)/C_T
      =T^(-2alpha)(log T+O(1))+alpha+O((log T)^(-1/2)),
      uniformly 0<=alpha<=1.                              (1)

All copies are counted. No RH premise is imported. Its nonnegativity is an unsigned Gram integral, not nonnegativity of our original signed Weil form.

Separately read Goldston, Lee, Schettler and Suriajaya, Pair Correlation Conjecture for the zeros of the Riemann zeta-function I: simple and critical zeros, arXiv:2503.15449v4, Theorem 1 and PCC in Section 4:

https://arxiv.org/html/2503.15449v4

That paper assumes vertical PCC and obtains asymptotically 100% simple critical-line zeros without assuming RH. PCC is conjectural; the conclusion is a density statement, not exclusion of every exceptional zero. We do not import PCC as a proved arithmetic input.

Version/date custody: the arXiv identifiers specify v1 (2023-06-07) and v4 (2026-03-30); the rendered pages also display a later generated Date field. The versioned identifiers and numbered statements above are the pin, rather than inferring a new theorem version from that generated field.

## 2. Our Gram representation of the actual scalar statistic

Let Z_T be the complete finite positive-ordinate multiset. Functional reflection within the upper half-plane permits the scalar reindexing

    F(x,T)=sum_{q,q'} x^(z_q+conj(z_q')) w(z_q+conj(z_q')),
    z_q=beta_q+i theta_q.                                 (2)

For |Re(u)|<2,

    w(u)=integral_R exp(-2|v|) exp(u v) dv.

Expanding the finite sum in (2) therefore gives the exact representation

    F(x,T)=integral_R exp(-2|v|)
                 |sum_{q in Z_T} exp[z_q(log x+v)]|^2 dv. (3)

This alternative representation is our elementary derivation, not a new asymptotic imported from the paper. It is equivalent in value to the published resolvent Gram representation. There is no convergence interchange with an infinite zero kernel: Z_T is finite and the exponential weight is integrable since |beta|<1/2.

Pairing beta with -beta in the inner sum produces cosh(beta(log x+v)). It explains both the scalar nonnegativity and why it is not P*P-N*N. The scalar probes equal coefficients on all copies. Critical negative-source coefficients need not be equal: N h changes sign under beta reflection, and critical outputs in its range inherit that antisymmetry. Changing to arbitrary copy weights changes the statistic, and the scalar reindexing in (2) must then reindex those weights as well. No bound for all such weighted statistics is asserted by (1).

## 3. Precise finite-perturbation stability of the unconditional estimate

Add a fixed finite multiset E with all reflected/sign partners, m positive-ordinate copies, and |beta|<=kappa<1/2. Let S and S_E be the inner sums in (3). The weighted Gram norm of S_E obeys, for x>=1,

    F_E(x)<=m^2 x^(2kappa)/(1-kappa^2).                    (4)

Indeed, each term has squared norm x^(2beta)/(1-beta^2), and the triangle inequality yields (4). Cauchy-Schwarz in THIS unsigned Gram gives

    |F_{Z+E}(x,T)-F_Z(x,T)|
      <=2 sqrt(F_Z(x,T) F_E(x))+F_E(x)                    (5)

once T exceeds the fixed added heights. This is a lawful unsigned Cauchy-Schwarz, unlike the circular signed use rejected in CC23.

Equation (1) implies F_Z(T^alpha,T)=O(T(log T)^2) uniformly on its alpha interval. Since x<=T, dividing (5) by C_T gives

    O(T^(kappa-1/2))+O(T^(2kappa-1)/log T).               (6)

For kappa=3/8 this is O(T^(-1/8)), smaller than the error in (1). Thus adding fixed off-line reflected copies preserves the very same stated normalized asymptotic and its uniform alpha interval. Deletions follow by comparing the smaller background and the finite removed set. Finite changes also preserve the asymptotic total count and the CC22 second transverse count bound, whenever the background satisfies them; finite low-height constants may change.

This establishes invariance of the specified LOCATION STATISTICS. It does not manufacture new actual zeros, preserve exact explicit-formula coefficients, or verify any full native form for the altered measure. Extending alpha beyond the proved interval cannot be done silently; x^(2kappa) can then grow beyond the saving in (6).

## 4. Vertical PCC has an even sharper finite-exception limitation

The referenced PCC counts pairs with strictly positive gap at most 2pi lambda/log T, for lambda in a fixed compact positive interval. In a locally finite multiset, only finitely many background locations are within distance one of each of finitely many changed heights. The minimum nonzero difference among these relevant locations is positive. For all sufficiently large T the allowed gap is smaller than that minimum, uniformly in the bounded lambda interval.

Therefore the finite alteration changes NONE of those positive-gap pair counts eventually. Equal ordinates are excluded by the strict positive-gap convention. The asymptotic PCC cannot exclude finitely many off-line reflected pairs. This is consistent with the primary paper's asymptotically 100% conclusion; it is not a criticism of that theorem. It proves no native arithmetic realization of the perturbed set.

## 5. Complete physical dictionary control: a finite off-line quartet

Take any complete critical-line background of both ordinate signs with polynomial counting growth, so smooth compact Fourier samples are square summable. Add the quartet (theta,beta)=(Theta,+/-kappa),(-Theta,+/-kappa), with Theta>0 and 0<kappa<=3/8. All four copies remain. Use the original normalized profiles p=integral h exp(i theta x)cosh(beta x), n=integral h exp(i theta x)sinh(beta x).

Choose a nonzero, nonnegative, even g in C_c^infinity(-epsilon,epsilon), and form chi=P(-d^2/dx^2)g with

    P(z^2)=[z^2-(2Theta+i kappa)^2]
              [z^2-(2Theta-i kappa)^2].

This real even differential polynomial preserves smooth compact support. With Fourier convention F_chi(z)=integral chi(x)exp(i z x)dx,

    F_chi(+/-2Theta+/-i kappa)=0,
    A=F_chi(i kappa)=F_chi(-i kappa)>0.

The last claim follows from P(-kappa^2)=16Theta^2(Theta^2+kappa^2)>0 and F_g(i kappa)>0. The signs in the four roots are independent.

Now use the PHYSICAL packet

    h_a(x)=exp(-i Theta x)[chi(x-a)-chi(x+a)], a>epsilon.

It is smooth and supported in the finite cap a+epsilon. Its entire transform is

    F_h(z)=2i sin((z-Theta)a) F_chi(z-Theta).

At the two +Theta off-line copies, p=0 and n=+/-2A sinh(kappa a). At the two -Theta copies, both profiles vanish by the imposed roots. Thus the quartet contributes EXACTLY

    P_quartet energy=0,
    N_quartet energy=8A^2 sinh^2(kappa a).                 (7)

For every critical-line background copy, n=0 and

    |p_q(h_a)|<=2|F_chi(theta_q-Theta)|.

The complete background positive energy is consequently bounded by the finite constant C=4 sum_q |F_chi(theta_q-Theta)|^2, independently of a. Schwartz decay and polynomial counting prove finiteness; no finite source truncation is used. Hence

    Q_modified(h_a)<=C-8A^2 sinh^2(kappa a),               (8)

which is negative at some finite cap. This is a genuine compact physical test in a complete hyperbolic dictionary, rather than a scalar eigenlevel renamed as a zero.

If the critical-line background also satisfies the correlation asymptotics, its finite modification retains them by Sections 3-4 yet has (8). Such a background's existence with PCC is not asserted as a proved zeta fact. This conditional compatibility control, and the unconditional statistic-invariance theorem, are the exact claims. We do not assert that (8) belongs to the actual original Weil form or that the altered dictionary has all-cap positive observability. An old positive anchor for a particular background would require its own quantitative lower bound; it is not deduced from counting alone. Genuine first-contact crossing tests remain the independently established differential/logarithmic controls replayed below.

## 6. What correlation estimate WOULD suffice

The missing theorem remains the actual adaptive estimate, for every critical coefficient vector alpha,

    ||M_t^(-1/2) sum_i alpha_i J_i*/sqrt(lambda_i delta_i)||^2
                <=q ||alpha||^2,                        (9)

equivalently J M_t^(-1)J*<=q Lambda G, with the independent low cost ell and q+ell<1. Its constants and step choice must be controlled by the finite cap rather than min(delta_i).

The J_i are the ORIGINAL forced rows associated to actual old generalized critical modes. They include the complete positive-source correction and all mixed physical pairings. They are not equal-copy weights or a fixed scalar function of ordinate difference; the protected inverse M_t^(-1) also depends on the complete positive dictionary. Formula (1) contains neither uniformity over these rows nor the old defect factor. Using a scalar asymptotic error after division by a freely small delta_i is invalid without a joint estimate. An upper bound averaged over heights likewise cannot remove finite exceptional modes on every cap.

This specifies the needed uniformity without asserting that all possible weighted pair-correlation approaches fail. A new operator estimate might establish (9); the two published statements inspected here do not state it and the invariance/pulse controls rule out the proposed inference from their averaged location data alone.

## 7. Controls and standing

22,492 exact checks pass: 1,656 new (33 exponential Gram-kernel identities, 1,143 polynomial/pulse/profile identities, 300 strip exponent/perturbation controls and 180 relative-loss/full positive-mass checks), plus 20,836 inherited CC23 checks. The inherited genuine crossing and whole signed completion controls remain active. The full shifted negative physical mass channel is retained in the positive-level test; original incoming cost 9/34 and shifted unit cost are not conflated. Rational proxies verify algebra, not logarithmic asymptotics, actual zero locations or the external theorem's proof. Sections 2-5 are analytic derivations.

No new aperture or actual arithmetic relative bound. Original whole-domain anchor remains 21/20 even0/odd0, joined margin 1/(3*10^63). RH/F4, retained attachment, reusable continuation, accumulated finite-cap loss and Lean closure remain open. Global stays paused at NF71; Aperture and Pre-Contact Shadow stay paused.

Stop the scalar-pair-correlation transfer in this form. Reopening it requires an actual weighted, adaptive correlation theorem that estimates (9), preserves all partners and the original sign, and survives both genuine crossing and full positive-level controls. An asymptotic density-one result is not that theorem.
