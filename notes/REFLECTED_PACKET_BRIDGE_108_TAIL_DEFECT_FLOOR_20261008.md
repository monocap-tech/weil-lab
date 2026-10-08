# RPB108 NF66: even the retained-tail error has a strict supported-mass floor

2026-10-08 UTC / 2026-10-07 Pacific. Recovered Global head `08b2cd74a850ff46ae79c3f40ed47fc0c56665cf`; independently read Coupled `26b361958d137da6e3178f99d47d0cbc2898e9c5`. Definitions: [defect-floor registry](../docs/TERMINOLOGY_RPB108_TAIL_DEFECT_FLOOR.md).

**Result.** The NF65 repair has both upper and strictly positive lower physical-mass error bounds on every bounded support window. For N=32,m=16 and all a<=21/20,

    (2e-50) mass < Delta_(32,16)(h) <= epsilon mass <1e-40 mass

for every nonzero canonical h. The exact lower constant is displayed below. This does not defeat NF65's genuine positive-anchor transfer, whose known original margin is far larger. It proves a sharper limitation: conditional on a finite ORIGINAL first contact, EVERY fixed even finite repair becomes negative on some preceding original-positive windows. Its auxiliary comparison source gain crosses one earlier. Thus a fixed accurate representation cannot supply an independent bound on the original accumulated relative loss.

The coupled branch already has the retained-logarithm representation and faithful completed-Schur error theorem in [CC6](https://github.com/monocap-tech/weil-lab/blob/26b361958d137da6e3178f99d47d0cbc2898e9c5/notes/REFLECTED_PACKET_BRIDGE_108_LOG_TAIL_RETENTION_CC6_20261008.md). That theorem is not duplicated here. This step supplies an explicit supported FLOOR for NF65's one-sided defect and traces its consequences through complete sources and exact Schur completion. No coupled or paused branch is written.

## 1. Exact remainder, now retaining its positivity

Use NF65's q=N+1/4, z=pi^2 xi^2, R_N and S_m, with m even. Its finite partial-fraction proof gives the exact identity

    R_N(z)-S_m(q,z)
      =integral_0^infinity exp(-qt)[1-cos(sqrt(z)t)] E_m(t) dt,
    E_m(t)=2t^(2m+1) sum_(n>=1)
           1/{[(2pi n)^2]^m[(2pi n)^2+t^2]} >0.      (1)

All factors are nonnegative. For the Fourier convention exp(-2pi i xi x), Plancherel and Tonelli give

    Delta(h)=integral_0^infinity exp(-qt) E_m(t)
                    [mass-Re C_h(t/2)] dt,            (2)
    C_h(s)=integral h(x+s) conjugate(h(x)) dx,
    mass-Re C_h(s)=(1/2)||tau_s h-h||_2^2.

This is the complete ORIGINAL-minus-repaired difference. Prime and pole contributions cancel exactly; they are not estimated or omitted. The integral applies to every supported L2 vector as a bounded defect operator, separately from membership in the original logarithmic form domain. No derivative of h or quadrature approximation is needed.

## 2. Support forces a uniformly nonzero response

If h is supported in [-B,B] and k s>=2B, then h and tau_(ks)h have disjoint supports up to null endpoints. Telescoping translations and the triangle inequality imply

    2mass=||tau_(ks)h-h||^2 <=k^2||tau_s h-h||^2,
    mass-Re C_h(s)>=mass/k^2.                         (3)

Choose t in [1,1+1/q], s=t/2, and k=k_B=ceil(4B). Then k s>=2B. The elementary bounds pi<4 and e<3 follow respectively from pi=4 integral_0^1 (1+x^2)^(-1)dx and the exponential factorial series. Keeping only n=1 in (1) gives throughout this interval

    E_m(t) >2/[64^m(64+(1+1/q)^2)],
    exp(-qt)>3^(-ceil(q+1)).                          (4)

Integrate (2) over this interval of length 1/q and use (3):

    Delta(h)>=kappa_(N,m,B) mass,
    kappa_(N,m,B)=2/{3^ceil(q+1) q 64^m
                    [64+(1+1/q)^2] ceil(4B)^2}>0.    (5)

Strictness holds for nonzero h; the weak form of (5) suffices. NF65 supplies the upper bound Delta<=epsilon_(N,m) mass. The inequalities are proved for ALL vectors and frequencies, not inferred from a finite list of shift samples.

At N=32,m=16, q=129/4 and B=21/20, ceil(q+1)=34, k_B=5. Exact rational arithmetic gives

    kappa=43/1490199325540563166095914388296927184542535725875200
          >2e-50.

At B=1 it is 43/953727568345960426301385208510033398107222864560128, approximately 4.5086e-50. These are conservative positive floors, NOT claims of optimal error size or a new original Rayleigh margin. The ceiling in (5) merely coarsens an estimate and creates no form or spectral jump.

## 3. Hypothetical contact forces an earlier lower-comparison failure

Assume the ORIGINAL first contact occurs at some finite a_*>1, with unit physical kernel vector h_*. This is a CONDITIONAL analysis; no such contact is asserted to exist. Choose an aperture cap B>=a_*. From (5),

    Q_minus,a_*(h_*)=-Delta(h_*)<=-kappa_(N,m,B)<0.    (6)

More is true. For a<a_* let r=a/a_* and h_a(x)=r^(-1/2)h_*(x/r), a unit vector supported in [-a,a]. Dilation is strongly continuous on the canonical logarithmic carrier near r=1. Indeed its Fourier action is sqrt(r) hhat(r xi); the logarithmic weight ratios are uniformly bounded near one, and continuity follows first on smooth Fourier cores and then by density. The archimedean form is continuous in this norm. The complete prime terms and exact pole are continuous under physical L2 convergence on one fixed finite cap, with one finite dictionary and zero overlap at activation thresholds. Consequently

    Q_original,a(h_a)->Q_original,a_*(h_*)=0

as a increases to a_*. Since a_* is FIRST contact, these original energies are strictly positive for a<a_*. But the uniform supported floor still gives Delta(h_a)>=kappa_(N,m,B). Therefore, for every a sufficiently close below a_*,

    Q_minus,a(h_a)<-kappa_(N,m,B)/2<0,
    Delta(h_a)/Q_original,a(h_a)->infinity.            (7)

Thus no uniform finite bound on that ratio, and no inequality Delta<=theta Q_original with theta<1, can hold throughout the hypothetical original-positive interval for any fixed N and finite even m. NF65's chosen repaired form starts strictly positive at the existing aperture-one anchor. Under this hypothetical contact it later has negative directions BEFORE original contact. Continuity gives a lower-comparison zero between; no numerical aperture or original zero location is claimed.

This is stronger than saying that a tiny fixed tolerance might be problematic. The strict supported floor makes the obstruction unavoidable under the hypothesis. It is much smaller than CC5's discarded-tail floor and does not reinstate that inefficient cutoff architecture.

## 4. Complete original sources and the lawful auxiliary comparison gain

Preserve the normalized COMPLETE original identity

    Q_original(h)=||P_a h||^2-||N_a h||^2.

The bounded positive physical defect operator D_a representing Delta has a square root. Hence the EXACT repaired identity is

    Q_minus(h)=||P_a h||^2
                 -||(N_a h,D_a^(1/2)h)||^2.          (8)

The second slot is explicitly an AUXILIARY channel, not an actual divisor row, ordinate, or changed prime dictionary. On the closed positive range of P_a define the comparison gain using P_a h ->(N_a h,D_a^(1/2)h). Original positive observability makes this a bounded map on each fixed aperture. The NF65 canonical anchor margin makes its norm strictly below one at a=1.

A negative repaired direction in (7) proves that this auxiliary gain is strictly above one, while the ORIGINAL gain remains strictly below one at those pre-contact apertures. At contact, the unit h_* gives quotient

    [||N_a h_*||^2+Delta(h_*)]/||P_a h_*||^2
       =1+Delta(h_*)/||P_a h_*||^2>1.                 (9)

The denominator is finite and nonzero by complete positive observability. This is consistent with bounded, convergent original sources whose signed difference vanishes. Neither (8) nor (9) bounds the original gain above or below one away from its stated original standing. NF64's bare g_32 is a third, different comparison gain and is left intact.

## 5. Completed Schur chart: an actual negative direction, not an inverse estimate

Use a protected physical chart from [CC4](https://github.com/monocap-tech/weil-lab/blob/26b361958d137da6e3178f99d47d0cbc2898e9c5/notes/REFLECTED_PACKET_BRIDGE_108_ARITHMETIC_RELATIVE_LOSS_CC4_20261008.md). Its exact ORIGINAL graph W and Schur S satisfy Q_original(Wx)=S(x). If the original complement has physical protection c>epsilon, the repaired complement stays positive, so its exact Schur minimization S_minus is lawful. Testing the ORIGINAL minimizer, with no inverse substitution, gives

    S_minus(x)<=Q_minus(Wx)
                 <=S(x)-kappa_(N,m,B)||Wx||^2.        (10)

At original contact, choose x corresponding to a nonzero original kernel vector Wx. Then S(x)=0 but S_minus(x)<0. This does not contradict CC6's graph-sensitive lower error bound; the graph mass must be retained in BOTH bounds. It proves the fixed repaired Schur block cannot remain positive to original contact whenever the protected-complement gate applies. If that gate fails, no repaired Schur determinant is assigned; the whole-form negative-vector statement (7) still holds.

The genuinely crossing differential/logarithmic operators already proved in CC4 permit finite contact with bounded complete sources. Subtracting this positive bounded multiplier from the genuine logarithmic control gives exactly the earlier-comparison failure above. Thus support, canonical logarithmic growth, compactness, tiny absolute error, and an anchor do not imply original nondivergence. The exact rational coupled matrix control in this step recomputes BOTH diagonal blocks after subtracting a mass defect and exhibits comparison Schur zero while its original Schur is still positive.

For an original positive physical eigenlevel mu, subtract the same mu mass from both forms. On its unit eigenmode, the repaired shifted value is -Delta<=-kappa; the ORIGINAL value is mu, not zero. An unshifted repaired value can also be negative when 0<mu<kappa. No zeta eigenlevel in that range is asserted to exist. Prime-power weights, both orientations, the exact signed pole, and threshold zero-overlap remain unchanged throughout.

## 6. Decision: representation error is now controlled; original relative loss is not

NF65 and CC6 have solved the representation-loss problem at the existing tiny-margin controls. This floor theorem closes the inference boundary: fixed absolute accuracy cannot turn into an arithmetic bound relative to a hypothetically closing original gap. Adaptive accuracy can follow a KNOWN gap; choosing it from an independently proved relative bound would be valid. It does not prove that bound or that the true gap cannot close. Further tail refinements are therefore not the default Global continuation.

The decisive missing input remains a zeta-specific estimate for the ORIGINAL shell reaction H^*D^(-1)H relative to its ORIGINAL completed Schur S, with complement protection, or an equivalent complete original source-gain inequality. The floor above is an approximation defect, NOT that aperture reaction and NOT evidence for an actual zeta contact. It supplies no new larger-window sign or finite accumulated-loss bound.

620 exact rational controls pass, including the quantitative floors, exact continuous-shift correlations on BOTH unchanged NF64 rational physical witnesses, a genuinely coupled comparison/original Schur separation, and positive-eigenlevel shifts. Infinite-dimensional contact/dilation arguments are analytic and not Lean-formalized. The original witness form certificates and full source/Gram constructors are not replayed. No new original negative vector, certified aperture, RH, F4, full transport, or Lean closure is claimed. Historical notes remain immutable; all additions are on Global only, with the coupled and paused refs untouched.
