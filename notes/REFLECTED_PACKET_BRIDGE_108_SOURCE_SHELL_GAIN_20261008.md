# RPB108 NF67: exact complete-source shell reaction and critical output leakage

2026-10-08 UTC / 2026-10-07 Pacific. Recovered Global `48fef33ca0cede19d81a91f8f357153372498436`; read Coupled `2386b78360d55d44b74c2998f1e321323e3ff1da` without writing that branch. Definitions: [source-shell registry](../docs/TERMINOLOGY_RPB108_SOURCE_SHELL_GAIN.md).

**Result.** There is a direct exact continuation criterion in the COMPLETE ORIGINAL source range, without a tail approximation or a physical Schur-chart choice:

    A_t=A_s+K_st K_st*,
    g_t<1 iff ||K_st*(I-A_s)^(-1)K_st||<1, if g_s<1.

Here A is the original negative-source Gram, and K is the exact incoming positive-source-orthogonal shell map. This isolates the necessary cancellation as incoming output overlap with old near-unit NEGATIVE source directions. A protected codimension-d physical/canonical complement confines those dangerous output directions to dimension at most d. They remain complete-source combinations, not selected zero rows.

The new identities and a sufficient quantitative spectral-leakage estimate are established below. The zeta-specific leakage estimate itself is NOT proved or evaluated. 1,572 exact rational controls pass, including coupled block completion, noncommuting resolvent updates, equal-size incoming sources with different critical alignment, and original versus shifted levels. No new original gain bound or aperture is claimed.

## 1. Fixed complete source rows, nested positive ranges

Fix any finite aperture cap B. Use the already established original normalized positive/negative analysis P,N on D_B, with ALL ordinates, multiplicity copies, mixed slots and historical partner normalization. The original identity is

    Q(h,k)=<P h,P k>-<N h,N k>.

Support inclusion leaves these rows and the original form unchanged. Restricted to D_a, a<=B, P has the published positive observability and boundedness, so V_a=P(D_a) is closed. In particular V_s is a closed subspace of V_t for s<t, all inside ONE positive source ambient. The ORIGINAL gain map

    T_a(P h)=N h

is simply T_B restricted to V_a. This is true without assuming Q_a nonnegative. P_B is injective and has a bounded inverse on its closed range; no inverse on the entire positive ambient is invented.

Let W_st=V_t intersect V_s^perp_positive. The exact orthogonal decomposition is V_t=V_s direct-sum W_st. The corresponding physical lift of w is P_t^(-1)w. It need not be supported in the outer physical strip, and it need not be physically or canonically orthogonal to D_s. That distinction is load-bearing: replacing W_st by a naive spatial shell changes the formulas.

Put K_st=T_t|W_st. With respect to this source decomposition,

    T_t=[T_s,K_st],
    A_a=T_a T_a* on the complete negative ambient,
    A_t=A_s+K_st K_st*.                              (1)

Both columns act into the same FULL negative source space. Equation (1) makes the original squared gain monotone under support inclusion: g_s^2=||A_s||<=||A_t||=g_t^2. No compactness of T_a is assumed. On any fixed finite cap all A_a remain absolutely bounded by ||T_B||^2; that bound need not be below one.

## 2. Exact unit-gain gate and resolvent update

Assume the OLD original window is strictly positive, equivalently g_s<1. Then both

    Dpos_s=I_(V_s)-T_s* T_s,
    Dneg_s=I_negative-A_s

are uniformly positive bounded invertible operators. The source-coordinate form of Q_t is

    I_(V_t)-T_t* T_t
       =[[Dpos_s, -T_s* K],[-K* T_s, I_W-K* K]].

Eliminate the whole old positive range, not a finite retained packet. The identity

    I+T_s Dpos_s^(-1) T_s*=Dneg_s^(-1)

gives the EXACT incoming completed block

    I_W-B_st, B_st=K* Dneg_s^(-1) K>=0.              (2)

The bounded completion graph is x=Dpos_s^(-1)T_s* K w. Congruence and bounded inverse completion prove

    g_t<1 iff I_W-B_st has a uniform positive gap
           iff ||B_st||<1.                          (3)

For an independently known g_s<=gamma<1 and ||B_st||<=rho^2<1,
put d0=1-gamma^2 and M=gamma||K||/d0. The bounded graph has
norm at most M, and elementary square completion gives the quantitative bound

    g_t^2<=1-min(d0,1-rho^2)/[2(1+M^2)]<1.          (3a)

This is an ORIGINAL gain consequence with independently bounded inputs,
not an evaluated new zeta constant.

Uniformity matters on the possibly infinite-dimensional W. Merely checking positive values on finite trial vectors is insufficient. If g_t<=1 then B_st<=I; this necessary inequality from known nonnegativity is not an independent strict arithmetic estimate. Original contact yields a unit direction; a cost above one gives an original negative vector after exact physical lifting.

When ||B_st||<1, the whole negative-source defect resolvent updates as

    Dneg_t^(-1)=Dneg_s^(-1)
      +Dneg_s^(-1)K(I_W-B_st)^(-1)K*Dneg_s^(-1).     (4)

These are bounded operator identities. They do not use a Fredholm determinant in an infinite source space, pretend the shell is finite, or assume source matrices commute. Unlike the repaired comparison in NF66, every operator here belongs to the ORIGINAL actual source identity.

## 3. What cancellation is actually needed

Let E_s be the spectral measure of A_s. The scalar identity

    1/(1-lambda)=1+integral_0^lambda du/(1-u)^2

and bounded spectral calculus (||A_s||<1) give

    B_st=K* K+integral_0^1
          K* E_s((u,1]) K /(1-u)^2 du.              (5)

The integral vanishes above ||A_s||. Thus bounded incoming norm alone controls only the first term. The second measures alignment with old near-unit negative output. It is a WHOLE operator inequality on W, with all source correlations and cross-prime/archimedean/pole information implicit in the exact original analysis.

For example, a sufficient independent arithmetic estimate would be, for some alpha>0,

    ||K||^2<=b_st,
    K* E_s((u,1]) K<=L_st(1-u)^(1+alpha) I_W
                       for EVERY 0<=u<1.

It implies by (5)

    B_st <=[b_st+L_st/alpha] I_W.                    (6)

If b_st+L_st/alpha<1, this PROVES strict original gain at t. Such a spectral-leakage estimate is a precise new sufficient arithmetic target, not an assertion that the completed zeta rows satisfy it. A critical-power bound with only (1-u) gives a logarithmic integral and does not itself give a uniform endpoint budget.

Conversely, any bound B_st<=rho^2 I_W necessarily gives

    K* E_s((u,1])K<=rho^2(1-u) I_W.                 (7)

This follows by restricting the inverse-defect spectral integrand, which is at least 1/(1-u) on that space. Suppression relative to the old defect is therefore necessary. General source boundedness, finite prime count and beta strip width do not establish it. NF55's rowwise tanh countertest remains valid; no rowwise domination is introduced.

A transparent control has A_s=diag(1-d,0) and incoming column K=(k_parallel,k_perp). Its exact cost is

    B=k_parallel^2/d+k_perp^2.

Parallel and orthogonal incoming columns can have the SAME raw norm but continuation costs differing by 1/d. Keeping k_parallel fixed as d decreases makes this cost diverge. The full source identity exposes rather than cancels the dangerous correlation. An estimate must make this component shrink, or obtain its cancellation from actual arithmetic.

## 4. Protected complements reduce the dangerous OUTPUT to finite dimension

Suppose on one ORIGINAL-positive chart the physical retained space has dimension d and its complement F_s has canonical coercivity

    Q_s(h)>=c ||h||_D^2 on F_s,
    ||P h||<=C ||h||_D on the fixed cap.

P(F_s) is a closed codimension-d subspace of V_s. On it,

    <Dpos_s v,v>=Q_s(P^(-1)v)
                    >=(c/C^2)||v||^2.

By min-max, for any 0<eta<c/C^2, Dpos_s has at most d spectral directions below eta. Equivalently T_s* T_s has at most d directions above 1-eta. T_s* T_s and A_s=T_s T_s* have the same nonzero spectral spaces up to the polar isometry, so

    rank E_s((1-eta,1])<=d.                          (8)

This is an analytic rank bound, not a claim that old source coordinates form a finite dictionary. No norm continuity of projections V_s or compactness of T_s is used.

Write Ecrit=E_s((1-eta,1]), L_st=Ecrit K, and Gcrit=Ecrit(I-A_s)Ecrit restricted to that finite output space. Then

    B_st=K* E_low(I-A_s)^(-1)E_low K
                           +L_st*Gcrit^(-1)L_st,
    first term <=eta^(-1)||E_low K||^2 I_W.          (9)

The potentially singular inverse is therefore a finite CRITICAL OUTPUT defect matrix, paired against a map from the entire incoming shell. It is still a whole norm estimate, not positivity of a finite restriction of W. The protected-complement gate itself must remain independently established; the aperture-one complement is not asserted to protect all larger windows.

At a nonnegative original contact, if p=P h for a kernel vector, original weak nullity gives T* T p=p. Consequently n=T p=N h satisfies A n=n, and ||n||=||p||>0. Conversely a unit output eigenvector produces a unit positive-range direction via T* and thus an original kernel vector through P^(-1). The critical unit output cluster has the original kernel's dimension. Its entries are complete actual negative source combinations N h, not individual zeros or a frozen height prefix.

This makes a concrete interface to the existing finite contact cluster: bound incoming COMPLETE-source overlap with those critical output combinations relative to Gcrit. It does not prove that overlap bound or exclude a kernel. The abstract cluster theorem alone supplies dimension, not suppression.

## 5. Anchor, shell sequences, crossing and positive-level controls

The aperture-one whole-domain certificate still gives g_1<1 through the complete original positive upper bound. Equation (3) would continue this anchor once an independent incoming cost is bounded below one. Repeated use of (4) on nested source ranges accounts for all old and new columns. No accumulated-loss bound is inferred just from absolute boundedness of A: a monotone scalar A can reach one at a finite aperture while staying bounded.

The genuine differential and logarithmic crossing operators in CC4 also satisfy the source-shell algebra whenever their positive analysis is injective/coercive. At their original contact the complete source energies are finite and equal, and the incoming cost reaches the unit threshold. Thus (1)-(4) do not by themselves rule out genuine crossing. The finite controls include fixed original nested source columns, exact coupled unit contact with nonzero source energies, and cost above one; no such zeta crossing is claimed.

For an original positive physical level mu, the shifted negative analysis is

    N_mu h=(N h,sqrt(mu)h).

The common positive ranges remain V_a, but the negative ambient, old A, and incoming K must ALL be recomputed. Its cost may reach one at an original eigenvector with Q(h)=mu mass>0, while the unshifted original cost remains below one. The exact rational control uses original lowest level 11/100, preserving the mass term instead of relabeling it zero.

The complete physical prime/pole identity has not changed. At any finite cap there are finitely many active prime powers with Lambda(p^r)=log p and both orientations; activation equality has zero physical overlap. Nothing in W_st deletes old/new mixed prime terms: W is source-orthogonal, not a spatial-strip approximation. No derivative in aperture, frozen source prefix, smearing, auxiliary defect channel or global H1 assumption is used.

## 6. Validation and next arithmetic task

1,572 exact controls pass across 288 coupled complete-source block cases, including 204 positive and 81 negative incoming completions (the remaining cases are exact unit cases). The checks verify A_t-A_s=KK*, old-positive/negative-defect inverse identities, exact lifted quadratic forms, entire mixed resolvent updates, raw norm versus critical alignment, equal nonzero sources at nullity, and positive-eigenlevel shifts. The infinite-dimensional range, spectral and min-max arguments above are analytic, not proved by samples or Lean-formalized.

This is a new exact ORIGINAL arithmetic relation and explicit sufficient leakage condition. It does not establish the missing zeta estimate. The next substantive task is to bound L_st*Gcrit^(-1)L_st and the low-output remainder using complete actual source correlations, or prove the stronger spectral inequality (6). More generic approximation accuracy, bounded-source observations or contact-cluster descriptions are insufficient. An evaluated WHOLE bound, retaining the complement gate when using (8), is required before claiming an aperture or original loss result.

Global NF65/NF66 and Coupled CC4/CC7 are preserved. The coupled branch was inspected read-only; paused Aperture and Pre-Contact Shadow refs remain untouched. No new aperture, original negative vector/contact, arithmetic nondivergence theorem, global gain, RH, F4, full transport or Lean closure is claimed.
