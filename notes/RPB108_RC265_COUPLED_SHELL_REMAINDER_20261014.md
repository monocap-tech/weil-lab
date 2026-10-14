# RC265 — one common omitted energy across Fourier shells

Parent: `dee8de1cd531cc210c73f134cb6ab7fff12ac19e` (RC264).
Branch: `research/rpb108-route-consolidation`.

RC265 retains a common unknown omitted-mode energy across all frequency
shells in the inverse comparison. It adds one Fourier-tail evaluation per
parity: 8U/5 for the even source, 21U/20 for the odd source. The earlier
3U/2 and 2U evaluations are reused by pins. The actual rational augmentation,
two sources, four response trials per parity, chosen Z, physical source
degree 1024 and prime output cutoff 2048 are unchanged.

| Actual original-action inverse upper | RC264 | RC265 |
| --- | ---: | ---: |
| Even source | 0.119404268 | 0.116973243 |
| Odd source | 0.114911466 | 0.114207160 |

Displayed upper bounds are rounded outward. Exact rational enclosures are
stored in the certificate. Signed-gap lower bounds improve to approximately
-0.028414047 even and -0.017124345 odd. They remain negative; neither a
positive signed gap nor a negative actual-gap witness is certified.

At each selected tau, the three-cutoff model bound before the global error
payment changes from approximately 0.1027606535 to 0.1009101811 even, and
0.0902849236 to 0.0901262638 odd, when the common-energy coupling is enabled.
These are model comparison bounds, not actual inverse responses. They
separate the benefit of coupling from the extra cutoff's benefit.

## Common physical remainder

As in RC263–264, the actual physical residual source is

    g = D e = G0 Pbase-G Z = p+q+f,
    ||p||^2=A, ||q||^2<=R, ||f||<=delta.

The model remainder q has matching parity and is orthogonal to every
Legendre mode through 1024. The error f includes all finite coefficient and
actual-s uncertainty and all original and rational-augmentation model
faults. No low/high orthogonality is assigned to f.

Introduce u=||q||/sqrt(R), so 0<=u<=1. This is one common unknown in every
shell. R is an upper bound, and is never assumed to be the actual energy.

Let C_V be the ideal Fourier band compressed to the physical interval.
The inherited Poisson/geometric-series argument gives

    ||H C_V H|| <= K_V <= 1,

where H projects onto matching-parity degrees above 1024. A cap of one
bounds the compressed operator norm, not the trace. The certificate uses
the explicit field high_space_band_operator_norm_upper for this quantity.
C_V need not be a projection. If the retained polynomial's outside-energy
interval is [Y_V_lower,Y_V_upper], put

    E_V = sqrt((A-Y_V_lower) K_V R)_upper.

Positivity and physical low/high orthogonality imply

    X_U(p+q) <= Y_U_upper + R u^2 + 2 E_U u,
    X_V(p+q) >= Y_V_lower + (1-K_V) R u^2 - 2 E_V u.

The lower inequality keeps the high modes' own outside energy, which RC264
discarded. Separately, the inherited unconditional lower bound L_V from
the trace/triangle argument remains available for every 0<=u<=1.

## Joint inverse comparison

For each unchanged rational tau candidate, the actual augmented lower form
is G>=eta_tau L+beta_tau C_U. The canonical L multiplier is log(e+|xi|).
Set I=eta_tau+beta_tau, and use inverse weight w0 outside U and decreasing
weights w1,w2,w3 at the three additional cutoffs. These use the inherited
rigorous lower logarithms and the same positive series bound for exp(1).
Only I>1/w0>0 candidates are eligible. Write d_j=w_(j-1)-w_j>0.

Nested full-line Fourier projections give

    ||W^(1/2)(p+q)||^2
      <= (A+R u^2)/I + (w0-1/I) X_U - sum_j d_j X_Vj.

For each j, select either the unconditional lower L_j or the quadratic
lower Y_j+(1-K_j)R u^2-2E_j u. For any such fixed selection, the resulting
upper polynomial in u has quadratic coefficient

    R * (w0 - sum_(selected j) d_j(1-K_j)) >= R*w3 > 0,

and a nonnegative linear coefficient. Its maximum on [0,1] is therefore
at u=1. This monotonicity step permits the common endpoint evaluation;
it does not turn R into a measured source norm.

At u=1, each shell's larger deductible value can be selected independently:

    D_j = max(L_j, Y_j+(1-K_j)R-2E_j),
    B_flat = A/I + (w0-1/I)Y_U_upper + w0 R + 2(w0-1/I)E_U,
    B_joint = B_flat - sum_j d_j D_j.

The values D_j are joint-bound endpoints. When their quadratic branch is
selected, they are NOT unconditional lower bounds on actual model tail
energies. The certificate explicitly distinguishes this from L_j.
Every selected branch retains the strictly positive quadratic coefficient;
outward rounding of cross terms, deductions and final bounds is paid.

For comparison, the certificate also stores the three-cutoff model bound
using only the unconditional L_j. Thus the extra cutoff and the common
energy coupling are distinguishable in the selected-candidate calculation.
No continuous optimality in tau or in the new cutoff is claimed.

All finite and global physical errors are paid after this model bound:

    <e,N^-1 e>_D <= (sqrt(B_joint)+delta*sqrt(w0))^2.

The comparison weight is bounded by w0, so this payment covers every error
without assumptions about its Fourier location. The least certified result
on the same 1000-point tau grid is added to the unchanged variational center
upper and intersected with RC264. The original source form lower updates
the signed-gap lower bound.

N is the chosen positive augmented operator, N0 the original Weil operator,
G=D N and G0=D N0. The canonical metric remains M=D^-1 L; D has harmonic
diagonal H_n+s. These lower forms do not give a positive floor for N0.

## New Fourier evaluation and verification

The new cutoff uses the complete pinned polynomial through degree 1024,
with every diagonal and cross term retained in the RC262 Fourier helper.
The principal degree-512 numerical control is the valid Parseval enclosure
[0,A512], explicitly labeled as such. It is not an older numerical Fourier
tail at the new cutoff. The exact degree-1024 physical norm must match
RC263, and the three tail enclosures must be strictly ordered.

All 230 inherited blob pins are verified. Exact replay reverses pin order,
Fourier pair order and tau candidate order and uses the inherited higher
precision and longer integration-by-parts replay settings. It must reproduce
the saved rational certificate exactly. The two previous cutoff evaluations
are reused through immutable RC264 pins rather than recomputed.

The finite controls use nested positive, nonprojective compressed band
operators. They check every mixed constant/quadratic branch and compare
the actual weighted form, the bound at each tested u, and its u=1 endpoint.
The retained shell telescoping and RC263 geometric/error controls also pass.

From repository root:

    python scripts/validate_rpb108_rc265_coupled_shell_remainder.py --output certificates/rpb108_rc265_coupled_shell_remainder.json
    python scripts/validate_rpb108_rc265_coupled_shell_remainder.py --output certificates/rpb108_rc265_coupled_shell_remainder.json --replay

The full signed rank-639 response and original full auxiliary norm gate
remain unevaluated. The separate eight-source canonical inverse width is
485647/1000000. Stage I, RH, F4 and Lean remain open/false.

Next: source-specific rational augmentation action errors or response-trial
optimization. Improving these two source bounds does not itself certify
the full signed gate.
