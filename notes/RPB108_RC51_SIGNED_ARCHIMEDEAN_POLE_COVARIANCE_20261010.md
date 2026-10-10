# RPB108 RC51 — signed archimedean–pole source covariance

2026-10-10. Parent RC50: `afcf4e989f8cf75f2b706e1b427b7b334906f7ee`.
Only `research/rpb108-route-consolidation` is written.

## Result and scope

The complete signed archimedean–pole physical trial source covariance
is now enclosed on native features 0 through 7. Paying both the
archimedean approximation and actual Riesz-map transfer gives

    (sigma_arch+sigma_pole)^*(sigma_arch+sigma_pole)
       <=11.187844253772395... M_8 <(2797/250) M_8.

The separate-component triangle bound from RC50 and RC42 is
95.69361094483993... M_8. The new allowance is more than 8.55 times
smaller. Both pole signs are retained. Nominal cross diagonals are
negative on even features and positive on odd features: the positive
even pole cancels part of the archimedean remainder action, while the
negative odd pole reinforces it. No negative-semidefinite assertion
about the entire mixed covariance matrix follows from its diagonals.

The bound applies only to this eight-feature source map. It does not
extend the refined allowance to the full 1250-feature map. Actual
canonical source entries and the projected residual remain unevaluated.
Generation and independent reflected exponential/log-moment replay pass.

## Sources and signed mixed covariance

Keep RC50's bounded physical remainder K_arch=L_arch-L_w, with
||K_arch||<8. RC50 supplies nominal trial sources

    F_nom,j(y)=A_j(y)+B_j(y)log y+C_j(y)log(1-y),
    y=(x+B)/R_width, B=11/10, R_width=11/5,
    ||(K_arch iV-F_nom)a||_2<=delta ||iV a||_2,
    delta<49/200000.

The same delta, including constant, entire metric-kernel and regular
archimedean-kernel errors, is paid here. Native rounded trials V and
actual Riesz representatives R_native are distinct throughout.

Write g_even=cosh(x/2), g_odd=sinh(x/2), s_j=(-1)^j, and
m_j=<exp(x/2),iV_j>. RC49 supplies certified m_j and pole Gram entries.
On a trial of parity j,

    F_pole,j=2 s_j m_j g_(j mod 2).

Compute z_j=<exp(x/2),F_nom,j>. For equal parity, the symmetrized
archimedean–pole cross entry and nominal joint source Gram are

    X_ij=2 s_i(m_j z_i+m_i z_j),
    U_ij=Q_arch,nom,ij+X_ij+O_ij,
    O_ij=4 m_i m_j ||g_(i mod 2)||_2^2.

Opposite-parity entries vanish exactly. All 20 same-parity entries are
evaluated; both ordered mixed contributions are included. X refers to
the nominal archimedean source, rather than an unpaid exact-source
identification. The subsequent joint-source transfer pays its error.

## Exponential/logarithmic moment generation and replay

Generation uses the degree-128 rational Taylor polynomial for exp(By).
Its uniform error on [0,1] is at most

    epsilon_exp=2 B^129/129!,

because the remaining term ratio is at most B/130<1/2. Integrating
each coefficient uses the inherited exact moments

    integral y^k=1/(k+1),
    integral y^k log y=-1/(k+1)^2,
    integral y^k log(1-y)=-H_(k+1)/(k+1).

Multiply the result by R_width exp(-B/2). The nominal source norm from
RC50 pays the direct tail by Cauchy:

    |tail contribution to z_j|
       <=epsilon_exp sqrt(R_width Q_arch,nom,jj_upper).

The omitted exp(-B/2) factor is at most one, so this is a safe upper
allowance. Polynomial products have degree at most 352, within the
inherited moment table. Directed 220-digit arithmetic is rounded
outward to rational moment endpoints at denominator 10^35.

Independent replay uses C_j(y)=s_j B_j(1-y) and integrates

    z_j=R_width exp(-B/2)[integral A_j exp(By)
          +integral B_j log y (exp(By)+s_j exp(B)exp(-By))].

This replaces the log(1-y) moment family with a reflected log y
integral and a negative exponential series. Separate positive and
negative exponential tails are paid using coefficient L1 bounds and
integral |log y|=1. Every replayed moment lies inside its saved rational
interval. Reusing the validated nominal source builder is explicit;
the replay independently checks the new moment integration identity.

## Actual head and source transport

Let T be the physical trial Gram, e_j RC47's physical Riesz-error
column norm, and v_j an upward square root of T_jj. The bounded joint
operator K=K_arch+K_pole satisfies parity bounds

    k_even=8+2||cosh(x/2)||_2^2,
    k_odd=8+2||sinh(x/2)||_2^2.

For the nominal joint source, let n_j=sqrt(U_jj_upper), rounded upward.
Then the true trial source norm is at most n_j+delta v_j. The nominal
joint remainder head is RC50's nominal archimedean remainder head plus
2 s_i m_i m_j. Its paid trial-to-actual head radius is

    delta sqrt(T_ii T_jj)
      +e_i(n_j+delta v_j)+e_j(n_i+delta v_i)
      +k_(i mod 2)e_i e_j.

Add the actual canonical M_8 enclosure once, and intersect with RC50's
actual archimedean head plus RC47's signed pole head. Thus the saved
`actual_joint_archimedean_pole_head_entry_enclosures` includes M_8.
Adding RC48's actual prime head and intersecting with RC50's complete
original head gives the new complete original intervals.

Actual physical source columns differ from nominal ones by at most
d_j=delta v_j+k_(j mod 2)e_j. The physical joint source-Gram entry
error is bounded by d_i n_j+d_j n_i+d_i d_j. Physical entries are
kept separate from actual canonical source entries.

For a whole-map canonical envelope, let P be RC39's physical native
Gram and B_err RC47's physical Riesz-error Gram upper bound. Check
P>=I/8. If h is the maximum nominal Gram entry halfwidth, define

    U_up=center(U)+64h P,
    S=diag(k_(j mod 2)),
    D_err=(33/32) S B_err S+33 delta^2 T.

Exact parity decoupling permits the separate operator bounds in S.
The fixed Young inequality pays the correlated actual-map transfer
and nominal source approximation together. With rho=252/257,

    (sigma_arch+sigma_pole)^*(sigma_arch+sigma_pole)
       <=A_t=rho[(1+t)U_up+(1+1/t)D_err].

Exact rational PSD bisection checks A_t<=lambda_t P for six rational
values of t. The selected value is 1/16. RC39's M_8>=alpha P,
alpha=8947777583/17179869184, gives the asserted lambda_t/alpha bound.
No floating eigenvalue or trial-to-actual substitution is used.

## Complete original head and remaining frontier

Display endpoints below are rounded further outward. Features 0 and 2
gain narrower complete intervals; historical intersections preserve
the other diagonal enclosures.

| Native feature | Complete actual original Weil diagonal |
|---:|---:|
| 0 | [-0.090515, 0.166257] |
| 1 | [-0.020415, 0.099014] |
| 2 | [-0.032184, 0.083164] |
| 3 | [-0.023578, 0.078503] |
| 4 | [-0.008679, 0.063317] |
| 5 | [-0.007774, 0.041298] |
| 6 | [0.035377, 0.079832] |
| 7 | [0.038690, 0.076464] |

The actual joint archimedean–pole head intervals are all narrower than
the separate-component intervals by a factor greater than 1.001; the
minimum is 1.0017835531.... Exact inequalities preserve RC50's floor

    Q(h)>=(1/25)||h||_D^2
    on span{actual native representatives r_6,r_7}.

The full eight-feature original head floor is still open. The remaining
unevaluated source cross covariance is archimedean–prime; evaluating it
will allow all three signed components to be combined before transport.
The full 1250-feature source/projection construction, projected residual,
and whole-aperture positivity remain open. RC44's complement floor and
RC45's conditioning certificate are preserved. No RH/F4 or Lean closure
is claimed.

## Reproduction

The validator's default inputs are the published RC39, RC42, RC47,
RC46, RC49, RC50, RC48 and RC38 metric certificates, in that order.
Input hashes and shared-input dependencies are checked. Existing
validated self-covariances and pole moments are inherited explicitly.

    python scripts/validate_rpb108_rc51_archimedean_pole_covariance.py
    python scripts/validate_rpb108_rc51_archimedean_pole_covariance.py --replay certificates/rpb108_rc51_archimedean_pole_covariance.json

The replay verifies reflected moments, all signed mixed entries,
paid approximation and actual transfers, historical intersections,
the two-feature floor, and exact rational whole-map PSD bounds.
