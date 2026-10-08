# RPB108 CC1: protect the complement, perturb the completed Schur graph

2026-10-08 UTC. Definitions: [registry](../docs/TERMINOLOGY_RPB108_COUPLED_CONTINUATION.md).
Outcome **B: conditional joint theorem**. No useful new actual aperture is certified.

## 1. Recovered heads and custody

Shared/Global/Aperture recovered at `fba75ed4eda84f0c71286f314f85b0d29db0202a` (NF58), beyond supplied `1b5db1dc92717e7e0dcd85341ac1494de97c0b70`. Shadow recovered at `ea6431655705351b37e14a51945e5d630b7d94dc` (PS1). Starting aperture certificate remains `811b0826abf45d688d1e2da7900cda852103ddee`.

Integration branch `research/rpb108-coupled-continuation` was absent in branch recovery and created from the recovered shared head. Prepublication recovery found Shadow advanced to `345d4f7b6f1ad0e91be7771031a875391d633ca8` (PS2); its note and original whole-domain conversion script were audited before publication. All eleven PS1/PS2 additions are incorporated verbatim, with the latest Shadow commit as an additional parent. Shared and Shadow branches are never moved. Prepublication recovery and exact file pins are in the custody manifest. No earlier regularity, Abel-transfer or contact classification is restarted.

## 2. Precise coupled-continuation theorem

Let A(a),A(b) be the complete original self-adjoint bounded canonical form operators on H. Choose H=E orthogonal-sum F, dim E finite. Suppose

    C=Pi_F A(a)|F >= c0 I,       S=A_EE-K* C^(-1)K >= s I,
    c0>0, s>0, K=Pi_F A(a)|E.

Define T=C^(-1)K, W x=x-Tx, ell=||T||, D=A(b)-A(a). Independently certify

    Pi_F A(b)|F >= c I, c>0,
    ||W* D W|| <= alpha,
    ||Pi_F D W|| <= eta.

It suffices for the first premise that ||D||<=omega<c0 and c=c0-omega. A sharper complement estimate may replace this coarse choice. Set

    t=s-alpha-eta^2/c.

If t>0, the whole original form is positive and has the following certified update:

    delta_b >= d := t c/[t+c(1+ell_b^2)],
    ell_b := ell+eta/c,
    lambda_min(b) >= d/||J||^2,
    g_b^2 <= 1-d/C_b^2 < 1,

where C_b is any proved upper bound ||P_b U_b||_(H -> complete positive source space). An unevaluated proved finite C_b gives a symbolic strict-gain bound, not a numerical distance from one.

Proof: in coordinates h=W x+z (z in F), the anchor form is diag(S,C). At b it is

    [[S+W*DW, H_b*], [H_b,C_b^form]],
    H_b=Pi_F D W, C_b^form=Pi_F A(b)|F.

Complete its square again: v=z+(C_b^form)^(-1)H_b x. The finite Schur block is at least t I and

    q_b(h)>=t||x||^2+c||v||^2,
    h=x-[T+(C_b^form)^(-1)H_b]x+v,
    ||h||_H^2<=||x||^2+(||v||+ell_b||x||)^2.

The difference between this lower energy and d times the norm bound has nonnegative diagonals and determinant d^2>0. This proves the displayed canonical bound. Physical mass is at most ||J||^2||h||_H^2. Finally the full original source identity and ||P_b U_b h||^2<=C_b^2||h||_H^2 prove the gain bound. No selected source prefix or trial eigenvalue is used.

The second square completion is essential: using ell rather than ell_b in the conversion would omit the new coupling correction.

This is more than the static Schur criterion. Only a **large complement margin** is charged the full logarithmic modulus. The tiny finite margin is charged graph-local alpha and eta^2/c. In particular no term ||K||^2 omega/[c0(c0-omega)] is charged directly to s, as would occur by separately perturbing the original inverse complement. The cancellation is justified by the exact anchor graph, not by ignoring a coupling term.

## 3. Proved hypotheses and the independent condition

Imported analytic facts: complete actual form/source equality; bounded positive analysis and positive-range observability; physical compact resolvent; PS1's modulus; NF54's mass-resolvent dictionary. The complete aperture-one interval certificate is imported, not replayed here.

The published physical complement F_112 (zero physical Legendre coefficients 0..111) satisfies Q_1>=0.93 mass. The archived whole-domain auditor uses Q_1>=E_log/10-24 mass, rather than a unit logarithmic coefficient. Combining the two gives

    Q_1|F_112 >= [93/24930] E_log.

F_112 is closed in H. Taking E=F_112^perp_H supplies a lawful canonical split of dimension 112. **This E is not the physical Legendre span.** The whole-domain aperture-one bound also implies its exact S>=2e-34 I_E, since ||Wx||_H>=||x||_H. These existence/lower bounds do not compute W, its coordinate Gram, ell, or its Fourier tails.

At this anchor the precise independent condition for a proposed b is

    omega(1,b)<93/24930,
    alpha(1,b)+eta(1,b)^2/[93/24930-omega(1,b)] < s,

with s>=2e-34 or a separately audited stronger exact Schur margin in the SAME canonical coordinates. These inequalities, with the original source/error custody, are the missing numerical/analytic certificate. The original physical corrected margin 3.125e-30 cannot simply be relabeled s in this split.

### A finite graph certificate can replace an exact inverse construction

Let W_Z x=x-Zx, Z:E->F, and certify r>=||Pi_F A(a)W_Z||. Then

    ||W-W_Z||<=e:=r/c0,       ||W||<=||W_Z||+e.

For independently enclosed approximate-graph budgets alpha_Z=||W_Z* D W_Z|| and eta_Z=||Pi_F D W_Z||,

    alpha <= alpha_Z+omega(2||W_Z||e+e^2),
    eta <= eta_Z+omega e.

This follows by expansion and ||D||<=omega. It retains the inverse-complement residual in both slots. It enables one anchor solve plus localized updates, rather than a fresh complete 112-column target source Gram at every b. However, the current published source Gram has not been converted into this graph certificate: it certifies anchor Schur positivity, not these graph residual/tail constants. Setting Z=0 need not make r small enough. Approximate-lift density gives no numerical rate by itself.

## 4. Updated aperture bound

No new actual nontrivial aperture is obtained. Certified macroscopic frontier remains a=1. PS1's existing analytically derived interval 1<=b<=1+2^(-10^36) remains valid, with canonical margin >1.5e-34; it is not counted as a practical breakthrough.

CC1 supplies an explicit test for larger b without fresh full target Grams. Its actual missing graph budgets are isolated above. Neither a new value of b nor a new sign is invented from them.

## 5. Canonical versus physical spectral margins

The starting published bounds are Q_1>=2e-34 E_log and Q_1>=4e-32 mass. They are separate inequalities. CC1 yields d and d/||J||^2, not equality of the two spectral gaps. Here ||J||<=1.

With m_b=||J[W-(C_b^form)^(-1)H_b]||, a possibly better physical bound from the second completed square is

    lambda_min(b)>=[m_b^2/t+||J|F||^2/c]^(-1).

This is weighted Cauchy-Schwarz on the physical norm of the two completed components. Both mass constants need proved upper enclosures. Trial Rayleigh values give upper bounds and cannot replace it.

For b>=1 the native energy obeys E_log(U_b f)<=||f||_H^2, so Q_b>=d E_log on D_b. On a general compact parameter interval weight equivalence gives E_log(U_b f)<=[1+|log b|]||f||_H^2 and native margin d/[1+|log b|].

Keep the physical resolvent exactly R(b)=J[A(b)+beta J*J]^(-1)J*. Its eigenvalues obey rho_j=1/(lambda_j+beta). Replacing J*J by I changes the spectral problem. The Gårding/physical-gap conversion remains kappa lambda/(lambda+beta)<=delta<=||J||^2 lambda when its stated positive-gap hypotheses hold. NF54 continuity is a control, not exclusion.

## 6. Complete actual source-gain update

The theorem gives g_b^2<=1-d/C_b^2, using the complete original P_b,N_b and the proved closed positive range. PS1 supplies local finite upper constants from a fixed larger domain; none has been evaluated here. The source-surrogate norm about 6.954 is NOT ||P_b|| and is unusable for this conversion.

This gain update is an algebraic consequence of the same margin, not a third independent arithmetic advance. NF55's parity control still forbids rowwise contraction from strip width. NF56's exact discrepancy formula could improve alpha_Z or eta_Z only via a new signed form enclosure on these same graph vectors. Its scalar discrepancy sign is insufficient. No such independent improvement is claimed.

## 7. Localized arithmetic budgets and potential resistance improvement

PS1 gives the full omega including the smooth archimedean/pole budget

    v(a,b)=5|log(b/a)|+4[cosh(B)+B sinh(B)]|b-a|

and complete clipped shifts d_n=|min(log(n)/a,2)-min(log(n)/b,2)|, coefficients c_n=2Lambda(n)/sqrt(n). All n with log n<=2B are included.

A quantitative graph bound can be obtained WITHOUT asserting derivative regularity. Suppose independently

    ||JW||<=m,  ||W x||_Xk<=L_k||x||_E,
    ||f||_Xk^2=integral w(xi)^(2k)|fhat(xi)|^2 dxi.

For any R>0, Fourier splitting gives

    ||(tau_u-tau_v)W||_(E -> L2)
       <=2pi R |u-v| m+2 L_k/[log(e+R)]^k.

Compressed opposite shifts have the same bound; compression is an L2 contraction. Therefore

    eta_all := v(a,b)m+sum_n c_n theta_k(d_n),
    ||D W|| <= eta_all,  eta <= eta_all,
    alpha <= ||W|| eta_all,
    theta_k(d)=inf_R[2pi R d m+2L_k/log(e+R)^k], theta_k(0)=0.

The archimedean difference is a bounded physical multiplier, and the pole difference is a bounded physical kernel, so their contributions use m. The full action bound eta_all, rather than the projected coupling alone, controls alpha. At 0<d<1, R=d^(-1/2) gives theta_k<=2pi sqrt(d)m+2L_k[2/log(1/d)]^k. The two-slot diagonal estimate may be improved independently; this one is sufficient.

If instead W has a certified global H1 bound ||(JW x)'||_2<=D1||x||, translation gives theta(d)<=d D1 and a linear local budget eta_all<=K|b-a|. With omega<=c0/2 and ||W||K epsilon+2K^2 epsilon^2/c0<=s/2, t>=s/2. For example the sufficient choices

    epsilon<=s/(4||W||K),
    epsilon<=sqrt(s c0/(8K^2))

give that inequality. This changes an inverse-logarithmic tiny-margin radius into a polynomial tiny-margin radius, subject to a separately protected complement. It is a conditional scale comparison, not an actual Weil interval.

**None of these W moment/H1 constants is supplied by NF58.** NF58 bounds original physical eigenvectors in a bounded eigenlevel range. A completed Schur graph vector solves a constrained complement equation, and is not automatically an original eigenvector. Nor does the finite-dimensionality of E remove the rough complement correction. NF49's rough projection control makes an automatic H1 claim especially inappropriate. Applying NF58 here requires a new justified forced-equation estimate, or direct Fourier-tail enclosure. This is the smallest repair to the tempting low-mode shortcut.

The graph moment estimate does not contradict NF57's sharp 1/log full-domain error. Only a fixed finite graph is tested sharply; the whole complement still pays the coarse norm modulus against c0, not against s.

## 8. Prime-8 threshold behavior

On 1<=b<=21/20, log(8)<2b<log(9) at the diagnostic upper endpoint, so the complete dictionary is 2,3,4,5,7,8. The new coefficient is c_8=2log(2)/sqrt(8). Activation is at a_8=log(8)/2. At equality compression is zero; above it the clipped displacement from anchor 1 is d_8=2-log(8)/b.

Both full omega and graph theta include this activation; the abstract theorem remains valid across the threshold if its inequalities pass. No eleven-panel decomposition, retained dimension adequacy, or operator-norm derivative is inherited.

The **particular imported complement protection** fails to certify reaching a_8: already 5log(a_8)>0.19>93/24930. Thus c0-omega is negative under this sufficient bound. This is failure of the bound, not a lower bound on the true perturbation, and not an impossibility theorem for crossing 8. Even perfect graph budgets cannot repair this chosen complement budget at that target. Reaching 21/20 requires an independent sharper target-complement estimate or a larger retained space, besides graph control. It does not require a full fresh source Gram as a matter of logic.

## 9. Countercontrols

- Positive physical eigenmode: the original equation stays ||P h||^2-||N h||^2=mu||h||_2^2. Shifting adds sqrt(mu)h to the negative channel and replaces A by A-mu J*J, including its graph and coupling. Original and shifted gain are different.
- Generic crossing: A(a)=diag((a_*-a)I_r,I), P=I, N=diag(sqrt(1-a_*+a)I_r,0), with compact diagonal physical inclusion, passes the local theorem only while its explicit t remains positive. Steps can approach a_* forever. It refutes non-stalling from these inputs.
- Dropping the new coupling: a positive retained block with excessive eta can have a negative full Schur complement. The checker includes this failure and tests the second completion/conversion on nonzero coupling.
- NF49/NF50: no source-height truncation, uniform height limit, smooth/height exchange or H1-preserving projection is used. Full unweighted analysis is retained.
- NF56: the indefinite discrepancy component receives a norm/signed enclosure; its scalar sign is not promoted to positive definiteness.
- NF57: full-domain logarithmic sharpness is retained; the sharper graph-rate premise is independent, not silently substituted.

## 10. Finite stalling

CC1 is local only. In the generic crossing family s shrinks to zero, g approaches one, and available steps shrink. No positive uniform step or positive lower defect at a finite limit follows. Non-stalling needs an original arithmetic inequality controlling the limiting low graph/source defect, beyond observability, spectral continuity, or this Schur update. Such a theorem remains unproved. Arbitrarily many finite positive steps do not imply global positivity.

## 11. Resistance relative to PS1

**Decreased for the conditional local estimate:** the full logarithmic modulus is no longer subtracted from the tiny finite gap, provided completed-graph estimates are available. **Unchanged for actual useful extension:** those graph estimates and coordinates have not been certified. **Unchanged for non-stalling/global exclusion.** A separate complement obstruction is now quantified at prime 8.

Concurrent PS2 independently restores and audits the conservative physical comparison matrix. It excludes candidate margins 1e-28 and 1e-29 for that matrix, without bounding the true physical gap above. Its independent-block theorem retains a complement-sensitive loss and therefore still requires omega at approximately 2.21e-34. CC1 addresses the same gate by jointly transporting its exact completed graph; it does not invalidate PS2's counterexample. On that counterexample W*DW=-T* zeta T, so alpha already contains the dangerous loss. Sharp estimates for original polynomial columns alone remain insufficient. PS2's archive audit is imported here, not replayed by CC1.

## 12. Smallest next task and validation boundary

At a=1, certify ONE completed-graph perturbation/residual budget satisfying alpha+eta^2/c<s at ONE explicit b>1 for which complement protection is positive. This requires lawful canonical coordinates (or a separately derived nonorthogonal version), an approximate complement solve, its residual, and a tail/translation enclosure for the corrected vectors. Do not merely extend NF58's homogeneous eigenvector recurrence or construct another uncorrected retained matrix.

For the specific target a_8 or 21/20, first sharpen the complement estimate: the imported omega cannot protect it there. No further generic contact cycle is opened. This publication stops at B, with the independent conditions made explicit.

New validation: written analytic proof of the anchored graph update, actual Fourier-split estimates and residual accounting; exact finite rational controls of square completions, conversions, coupling failures, compact-mass crossing, source gain and a conditional polynomial-radius example. These controls do not certify actual W, target arithmetic, zero ordinates, or new interval matrices. The aperture-one archives are not replayed. No Lean declarations, axioms, workflow or new CI validation are added. Existing analytic/interval/Lean status stays distinct. RH, Global exclusion, F4 and full transport remain open.
