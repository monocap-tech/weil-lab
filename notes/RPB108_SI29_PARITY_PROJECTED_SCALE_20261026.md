# SI29: parity exposes the remaining projected scale

W-ODD-NEG remains open. This tightens actual original projected energy and matched forcing upper bounds on the same 14 SI29 features and the full original J470 space. It does not compute the projected energy matrix, its lower bound or the inverse response.

Custody starts with draft PR #326, commit `9263174dcd5693ee9d7a40e6f3594f2afe022285`, successful Actions run `40365426998`. Its explicit rational U makes the leading Taylor jets of G=(F-H106)U diagonal. Those are Taylor coordinates, not energy normalization. The present workflow freshly replays that construction and the original SI10/Hermite geometry.

## Reflected interpolation uses the same physical sources

Let c_j,p_j be the first 40 original SI10 cluster centers and b9 orders. Their sum is 215. Interpolate sin(2*pi*eta*x) at both c_j and -c_j, each with multiplicity p_j. The scalar frequency interpolation order is 430. Reflection and uniqueness make the frequency interpolant odd. Also d_eta^k sin(2*pi*eta*x) at -c_j equals (-1)^(k+1) times its value at c_j. Therefore all physical interpolants belong to the same 215 original source directions already in J470. No physical source is added.

For a feature band [c-r,c+r], the reflected nodal product is bounded by

    P = product_j max(|(c-r)^2-c_j^2|, |(c+r)^2-c_j^2|)^p_j.

The uniform feature error is at most v*(2*pi_up*B)^430*P/430!, with v=1 for means and 3/2 for the true 3u first moments. This is the classical real confluent Hermite remainder, then integrated against the actual feature weight. It applies to every physical x in [-B,B], including interpolation nodes inside a feature band. Physical differentiation commutes with frequency interpolation. With R=7229/128 and Cx=2*pi_up*R+430/B<746, the derivative error is at most Cx times the same uniform ceiling. All nodes and feature bands lie in [-R,R]. The nodal product and all payments are exact rational bounds.

Write Hsym for these physical interpolants, H106 for the previous ones, and e=(F-Hsym)U. Then G-e=(Hsym-H106)U belongs entirely to J470. Thus e is an admissible representative for bounding the *full-J* projected operator, even though only 215 sources were used to construct Hsym.

## Actual original operator bounds

The checker propagates the actual rational U componentwise to obtain each uniform e_j ceiling eps_j. It finds max eps_j<2e-59 and

    ||(I-P_J)G||_HS < 3e-59.

Under the inherited original Fourier/domain assumptions and Astar>=kappa_star I, Astar<=Ao. The original Ao majorants on low and high frequencies give

    tr(T_G) <= sum_j [36*(2B)*eps_j^2 + ((2+2B*Cx)*eps_j)^2]
             < 1.02e-111,
    0 <= T_G <= (1.02e-111) I.

Here T_G is the actual *energy-projected* matrix

    G* Astar G - G* Astar J (J* Astar J)^-1 J* Astar G.

This is a variational upper bound using admissible J approximants, not substitution of G*Astar G for T_G. The original strong-domain assumptions remain inherited. Neither the source matrix nor an inverse was numerically assembled.

For the complete original Galerkin residual J*R0=0, G*R0=e*R0 exactly. Reusing the original direct/second-ray Ao-action bounds 1,400,000 and 350,000 gives matched vector-norm upper bounds 4.2e-53 and 1.05e-53 for these same G coordinates. The pole term vanishes under the original physical orthogonal complement because sinh(x/2) belongs to J. These are upper bounds on the forcing, not computed forcing entries.

## Consequence for the next solve

Diagonal leading Taylor jets do not remove the small projected scale: every projected energy eigenvalue is below 1.02e-111 in these coordinates. A solve that assumes order-one projected energy is unjustified. The residual representative and its energy normalization must be handled before accepting a condition-number claim or committing to a large matrix calculation.

Tiny energy and tiny forcing together imply neither small nor large h* T_G^-1 h. A quantitative lower bound with compatible rank information and the matched forcing are still needed. The degree-639 truncation error from PR #326 is an absolute bound; this new upper bound does not certify its adequacy relative to the unknown minimum eigenvalue. No response, method impossibility, actual signed negative direction, global odd positivity, even-sector closure, Weil transfer or RH is established. Draft/unmerged status and independent analytic/domain review remain separate from Actions success.
