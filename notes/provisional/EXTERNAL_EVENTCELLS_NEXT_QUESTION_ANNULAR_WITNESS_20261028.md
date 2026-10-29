# External event-cells next question: a finite, quantitatively out-of-fit original witness family

**Classification:** provisional original-carrier mathematical design / external literature inference. **Not** an accepted signed original Weil estimate, **not** a new NF research branch, **not** an imported Mittermeier theorem, and **not** W-ODD-NEG closure. Dated 2026-10-28 Pacific; current draft PR #361. Existing historical and external provenance unchanged.

## Question and source position

**Question:** can the Suzuki/Mittermeier parity-box representation provide more useful information than the NF376 smooth fifth harmonic about the original signed exterior response?

The now-inspected October 25 Mittermeier v2 PDF **Proposition 3, Eqs. (9)–(13), pp.9–10** gives normalized odd sign-boxes `o_{2t}(x)=2^(-1/2)sgn(x)1_{|x|<=t}` with `<o_{2s},o_{2t}>=min(s,t)`, and exact **odd PHYSICAL** kernel
`Ko(2s,2t)=2Psi(s)+2Psi(t)-Psi(s+t)-Psi(|s-t|)`.
**Theorem 4, pp.10–11** establishes form continuity/density of these boxes in its own compact Weil normalization. This is not a result proved specifically about the NF376 signed Fourier implementation.

## Exact finite-grid witness lemma (new elementary deduction)

Let `H_odd=L2_odd((-B,B))` with `B=11/10`, and let `S` be **any** real or complex odd subspace of dimension `d<=246`. For the original NF376 application, take `S=J242+span(E1,E2,E3,E4)` (dimension at most 242+4). Define `n=492`, `h=B/n=11/4920`, `t_i=i h` for `i=0,...,n`, and odd annular sign-box differences

`delta_i=o_{2t_i}-o_{2t_(i-1)}`, for `1<=i<=n`.

Their supports occupy disjoint annuli `t_(i-1)<|x|<=t_i`; their physical squared norms are exactly `||delta_i||²=h`, and the normalized vectors `v_i=delta_i/sqrt(h)` form an orthonormal family of size 492.

For any rank-`d` physical orthogonal projection `P_S`, Bessel's inequality gives

`sum_{i=1}^n ||P_S v_i||² <= d <=246`.

Consequently

`sum_{i=1}^n ||(I-P_S)v_i||² >= n-d >=246`,

so **at least one** `i∈{1,...,492}` satisfies

`||(I-P_S)v_i||² >= (n-d)/n >=1/2`.

Equivalently, with `q_i=(I-P_S)delta_i`,

`||q_i||² >= h/2 = 11/9840 ≈ 0.00111788617886`,

`||q_i|| >= sqrt(11/9840) ≈ 0.0334348049024`,

and **at least half the squared norm of that annular source survives the J242+E4 projection**. In particular `q_i⊥J242` and `q_i⊥E4`, so it is a genuinely unfitted diagnostic on the **unchanged** original carrier. No assumptions on the detailed J242 coefficients, original signed operator, or RH are used in this geometric proof. The conclusion is **existence among an explicit finite rational grid**, not a certified identification of which i works for the actual original J242/E4.

Contrast: NF376's particular fifth smooth harmonic has `||q5_perp||≈2.04636e-89` and relative unfitted norm <`2e-10`. This annular family proves a much stronger **available** absolute witness scale and guarantees a relative squared unfitted fraction >=1/2 **for at least one node**, without asserting anything about the corresponding *signed* response. It avoids repeatedly choosing analytic harmonics that J242 approximates to enormous accuracy.

## Complete information vs finitely sampled shadow

For any original odd strong action `g∈L2_odd((-B,B))`, set `r=(I-P_S)g`. Its continuum normalized sign-box observation is

`F(t)=<g,(I-P_S)o_{2t}>=<r,o_{2t}>=sqrt(2)*∫_0^t r(x)dx`, `0<=t<=B`.

Thus `F∈H¹(0,B)`, `F'(t)=sqrt(2)r(t)` a.e., and the **exact full-information identity** is

`||r||²_L2(-B,B)=∫_0^B |F'(t)|² dt`.

A complete sign-box continuum therefore determines the entire odd L2 residual; merely increasing the accuracy of a fixed finite-node set does **not**. For any chosen `t`, the projected sign-box `Q_S o_{2t}` gives the usual one-dimensional Cauchy **lower**, never a full upper, bound. This identity applies to `g=g4_low` under NF375's existing L2 construction, or to a full `W u4` only if its original strong-domain realization is established.

The geometric witness lemma and observation identity are derived from elementary Hilbert-space facts, not from the paper's finite Gershgorin positivity certificate. A rank finite set of observations cannot give a universal full residual *upper* bound without regularity/inverse-response information.

## Exact source-adapted signed pairing route (conditional on original normalization and domain)

For an odd piecewise C¹ source `f` on `(-B,B)`, with physical one-sided endpoint `f(B-)`, the exact L2 identity using normalized boxes is

`f=√2 f(B-) o_{2B} - √2∫_0^B f'(s)o_{2s} ds`.

Hence **if** the original Weil form is legitimately transported through the Mittermeier/Suzuki signed form and its logarithmic domain, any full-frequency odd Weil cross-pairing with an annulus `delta_i` can be written using a signed coefficient measure `dmu_f(s)=√2 f(B-)delta_B(ds)-√2 f'(s)ds`:

`B_W(f,delta_i)=∫_0^B [Ko(2s,2t_i)-Ko(2s,2t_(i-1))] dmu_f(s)`.

For the **projected** `q_i=delta_i-P_S delta_i`, the finite correction must be subtracted by independently certified original signed source matrix elements:

`B_W(u4,q_i)=B_W(u4,delta_i)-B_W(u4,P_S delta_i)`.

Neither the signed source correction, nor original sign conventions/pole treatment, nor a justified L2 strong-action identification, nor interval-cancelled arithmetic has been calculated in this pass.

The exact **NF375 lowband** dual is distinct from the full-frequency form: `I4(q_i;Lambda)=<g4_low,q_i>`. If a separately **certified** highband bound `beta_Lambda` holds, then `|I4-B_W|<=beta_Lambda||q_i||` after the original normalization/pole audit. A strict outward result `|I4|/||q_i||>1.5e-13` would STOP only the NF375 individual sufficient direction-four lowband method. A small value proves no upper residual or operator positivity.

For the guaranteed selected annulus, `0.0334348<||q_i||<=sqrt(h)≈0.047283...`; the corresponding **bare decision threshold** `1.5e-13||q_i||` lies between about `5.0152e-15` and `7.0925e-15`, not near the q5_perp absolute threshold `3.07e-102`. The actual signed signal might nevertheless vanish. The statement is conditioning/geometry, not an observed coupling.

## Decision and two gates

**Answer:** YES as a **quantitatively robust witness-selection architecture**, with a short analytic existence proof and explicit 492-node candidate set. NOT YET demonstrated as a cheaper or sufficiently rigorous **signed integral evaluator** than the Fourier method. It cannot yet provide a bound for `I4`, `H4`, or `B*C^-1B`.

**Candidate method-promotion condition (still NOT MET):** locate and SHA-custody a specific rational node i with an outward original physical `||(I-P_S)delta_i||²` enclosure and all projection conventions; compute an *original* signed coupling to NF370 u4 with independently enclosed seven-prime/pole/arch pieces and certified highband separation; show that the resulting bound changes NF376's accept/STOP test or yields a useful complete residual bound. The general guaranteed existence can be used as a **provisional preflight design** now, but is not an accepted NF376 signed response.

**Separate theorem-closure condition (NOT MET):** satisfy the full original W-ODD-NEG O1/O2 conditions, including 238 other selected directions, full infinite exterior response and independent form/domain transfer. Even/whole Weil and RH remain separately OPEN.

**Next bounded experiment:** evaluate 492 rational annular source projection norms, or use Bessel trace to construct one selected i, followed by **one** full signed scalar/event-cell dual calculation with strict original source covariance. Avoid a bulk 492 signed integral campaign, an enlarged selected source, or a new branch.
