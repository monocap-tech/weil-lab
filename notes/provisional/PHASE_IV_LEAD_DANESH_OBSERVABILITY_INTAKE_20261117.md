# Phase IV lead register — Danesh two-interval observability (DT)

Intake date: 2026-11-17. Status: QUEUED RESEARCH LEAD / external preprint theorem and internal analytic candidate; neither is a Lean-certified global positivity result. This entry is intended for Phase IV kickoff, not as a prerequisite for completing Phase III original Weil carrier (OWC) certification.

Companion internal note: [DT01 fixed-template reduction and audit](DT01_DANESH_FIXED_TEMPLATE_TWO_INTERVAL_AUDIT_20261117.md), immutable commit 8444b3b8be461ee3000f78f321ad348bb0be0b42. Side branch: research/side-danesh-two-interval-20261117. No changes to original NF source definitions, proof files, or workflow configuration.

## 1. External sources and custody

Primary source: Payam Danesh, *A quantitative two-interval criterion for the Riemann hypothesis*, arXiv:2611.10726v1, submitted 2026-11-07. [Versioned record](https://arxiv.org/abs/2611.10726v1) | [HTML full text](https://arxiv.org/html/2611.10726v1) | [PDF](https://arxiv.org/pdf/2611.10726v1) | [DOI](https://doi.org/10.48550/arXiv.2611.10726). The v1 full HTML and its abstract record were accessible and rechecked on intake. The source identifies a CC BY-NC-ND 4.0 license. Store bibliographic records, links and independent mathematical notes, not a modified or copied manuscript in this public repository. No PDF hash or independent author confirmation is claimed.

Reading anchors: section 2, Eqs. (1)–(4), centered complete zero form and summability; Lemma 1 and Eqs. (9)–(14), positivity of short supports and width quantifiers; Lemma 2, localization and partition cost; Lemma 3, Eqs. (26)–(29), one-sided Laplace singularity; Theorem 4, full equivalence and quantitative violations; section 5, Eq. (36), exact arithmetic cross term. Reinspect versions on reactivation.

Related reading queue (metadata/abstract checks, not full proof audits unless explicitly indicated):

| Priority | Source | Relevance / boundary |
|---|---|---|
| A | Danesh, *Recovering Dirichlet coefficients from even samples*, [arXiv:2610.24174](https://arxiv.org/abs/2610.24174), Oct 2026 | Finite noisy recovery and worst-case error. Different information model; no inference to Weil sign completeness. Abstract indexed; direct record fetch unavailable during intake. |
| A | Danesh, *A Ramanujan view of Robin's inequality*, [Cambridge Open Engage record](https://client.prod.orp.cambridge.org/engage/coe/article-details/6a47bd64810b9dcc82b9c788); related [author preprint index](https://vixra.org/author/payam_danesh) | Smoothing versus pointwise defect positivity. Abstract result indexed; full record fetch timed out. Match versions before any equivalence claim. |
| B | Danesh, *A Moment Framework for the Riemann Hypothesis*, [viXra:2605.0060v1](https://vixra.org/abs/2605.0060) (May 2026) | Moment positivity proposal; compare finite observables and sufficiency; not a verified RH proof. |
| B | Bianchetti and Danesh, *A Phase-Corrected Representation of the Riemann Zeta Function*, [SSRN DOI](https://doi.org/10.2139/ssrn.6797780) (May 2026) | Displacement/defect estimate with explicit nondegeneracy requirements. |
| A | Danesh, *Riemann Zeros as quantum energy levels*, [Cambridge v1, July 20](https://doi.org/10.33774/COE-2026-SCGGH); Danesh and Bianchetti, *Riemann Zeros as Quantum Energy Levels*, [IPI Letters 4(4), 32–42](https://doi.org/10.59973/ipil.379), Oct 12 2026 | Conditional Hilbert–Pólya realization, exact determinant and trace requirements. Publisher record checked. A different operator program, not evidence that its realization or the OWC has been completed. |
| A | Suzuki, *Aspects of the screw function corresponding to the Riemann zeta function*, [arXiv:2206.03682](https://arxiv.org/abs/2206.03682), [journal DOI](https://doi.org/10.1112/jlms.12785) | Explicit cited antecedent for translation-growth/Laplace criteria. Audit overlap with DT01 and novelty before attribution beyond the internal derivation. |
| A | Suzuki, *Weil's quadratic form via the screw function*, [arXiv:2606.09096v4](https://arxiv.org/abs/2606.09096v4) | Record confirms v4 revised Nov 15, 2026. Unified operator framework and de Branges connections; operator limit remains conjectural at abstract level. Version diff and full proof comparison queued. |
| B | Yoshida, *On Hermitian Forms attached to Zeta Functions*, [DOI](https://doi.org/10.2969/ASPM/02110281) (1992); Bombieri, *Remarks on Weil's quadratic functional in the theory of prime numbers, I* (2000); Connes–Consani, [archimedean trace formula](https://doi.org/10.1007/s00029-021-00689-4) (2021); Bombieri–Lagarias, [Complements to Li's criterion](https://doi.org/10.1006/JNTH.1999.2392) (1999) | Classical cited local positivity, disconnected support and alternative criteria. Compare existing Weil-Lab exterior notes before duplicating work. Identifiers sourced from Danesh's reference list. |

Do not infer personal research methods, access to our work, priority, or research rank from publication frequency. Prior contact with every antecedent has not been exhaustively reconstructed.

## 2. What the lead is, mathematically

Write z_rho = rho-1/2 and H_f(z) = integral f(x) exp(zx) dx. Danesh starts from the classical compact-smooth domain and B(f,g)=sum_rho H_f(z_rho) conjugate(H_g(-conjugate(z_rho))), with actual multiplicities. Theorem 4 asserts that normalized two-interval cross-energy at most one, for all real admissible pairs eventually, is equivalent to RH. The prescribed nonincreasing width w(L) tends to zero with log(1/w(L))=o(L). A zero of positive horizontal displacement implies exponentially large violations along arbitrarily large spans (any positive exponent below that displacement). This is an equivalence, not a proof of its uniform inequality.

DT01's additional internal candidate replaces variable test shapes by translates of a fixed real even smooth unit-mass bump b, rescaled by dyadic d=2^-n <= w(L), r=L-d. Set b_d(x)=b(x/d)/d; q_d=Q(b_d), c_d(r)=B(tau_r b_d,b_d). With q_d>0 for small d, the proposed eventual all-scale test is abs(c_d(r))<=q_d. The internal proof is based on exact convolution, all-zero error estimates and the pole obstruction. The dyadic quantifier means ALL eligible scales, not just one prescribed scale or a finite set. Proof audit and independent formalization pending.

Distinguish three levels:

- OWC (Weil-Lab working formulation): authentic source, domains/topology, full spectral graph, exact identities, closure and relation-preserving transport.
- Observation: restriction of the complete form to span{tau_{-r/2} b_d, tau_{r/2} b_d}; a two-dimensional compression at each parameter.
- Detection: the claim that the entire unbounded family detects every failure of RH. This is property-specific sufficiency, not reconstruction or injectivity on the carrier.

Danesh's theorem works directly with the classical test domain; it does not require the NF carrier realization. It does not establish a common carrier in our technical sense. Our internal term “sign-complete observation family” is descriptive, not a literature-priority claim. If subsequent estimates require alternative representations, transport and correlation become live obligations again. A direct arithmetic argument could also avoid an OWC realization. Neither possibility is presumed.

## 3. Concrete Phase IV arithmetic entry point

For the DT01 template take b nonnegative, even and unit-mass, define K(v)=integral b(y+v)b(y)dy and k_{d,r}(u)=K((u-r)/d)/d. Then k is the exact translated autocorrelation, has support in [r-d,r+d], and integral 1. For r>d and d<log 2, Danesh Eq. (36) gives the cross term on its separated support. Rearrange it, WITHOUT splitting the large prime and pole terms into unrelated error budgets, using psi(x)=sum_{n<=x} Lambda(n):

    W_{d,r}(x) = x^(-1/2) k_{d,r}(log x)
    D(d,r) = integral W_{d,r}(x) d(psi(x)-x)
    T(d,r) = integral k_{d,r}(u) exp(-5u/2)/(1-exp(-2u)) du
    c_d(r) = -D(d,r)-T(d,r).

Derivation: x=e^u converts integral k(u) exp(u/2) du to integral W(x) dx. The remaining two kernels combine exactly as exp(-u/2)-exp(-u/2)/(1-exp(-2u)) = -exp(-5u/2)/(1-exp(-2u)). All prime-power and pole charges are retained, no PNT or RH assumed. The remaining tail is nonnegative for this nonnegative b, with T<=exp(-5(r-d)/2)/(1-exp(-2(r-d))) from unit mass. These are analytic algebraic reformulations of Eq. (36), not Lean-verified or tested against repository normalizations.

The Phase IV scalar target is therefore:

    |D(d,r)+T(d,r)| <= q_d

for every eligible dyadic scale and sufficiently large real span L=r+d. The diagonal has no prime shifts for d<log 2; it retains the local gamma and pole contributions. Lemma 1 provides an eventual positive lower bound of order d^(-1)log(1/d); a matching upper order follows from the smooth transform decay and zero count as in DT01. This is a comparison of scales, not an asserted sharp constant. In arithmetic coordinates the window is [exp(r-d),exp(r+d)], with width of order d exp(r). Any numerical scout must retain correlation in D, use certified weighted prime-power sums including higher powers, and distinguish evidence at sampled parameters from a uniform theorem.

Even and odd combinations of symmetric translates have energies 2(q_d+c_d(r)) and 2(q_d-c_d(r)). Both are required. This makes the coupling formulation directly relevant to the older even/odd, Schur and cross-collar studies. The NF527 fixed B=11/10, delta=1/500 result cannot imply the unbounded-span inequality, even if completely certified. No new signed energy claim about the original NF494 source follows from this lead.

## 4. Phase IV reactivation checklist

1. Review Phase III completion report and unresolved OWC gates; do not treat DT as an admission or closure dependency.
2. Re-fetch Danesh and Suzuki versions, compare against prior exterior notes and independently audit Danesh Lemmas 1–3 / Theorem 4 and DT01 (uniform dyadic eligibility, full-multiplicity convolution interchanges, exponential approximation error, Laplace pole identity). Record counterexamples or missing hypotheses rather than silently modifying quantifiers.
3. Verify exact OWC/centered-Weil coordinate dictionary, including Fourier sign and 2pi conventions, multiplicity, P/N factors, conjugation, translation, physical domain, and native signed explicit formula. The phase III graph at a fixed aperture must not be treated as a uniform family without proof.
4. Formalize the scalar discrepancy identity and parity equivalence if compatible; derive diagonal q_d bounds with real constants. Compare direct arithmetic, correlation-preserving Schur, and first-contact routes without assuming any is superior.
5. Map the limiting regimes d small, large span and d exp(r), and identify when each estimate actually has decision quality. Keep the infinite parameter quantifiers explicit. Do not replace scale exhaustion by a grid or prime cutoff absent a valid uniform remainder.
6. Seek a genuine new estimate or a rigorous method stop. Promote to an active Phase IV line only after the audit. Until then: potential lead, not dependency, not external novelty, not proof of RH.

Explicit unresolved questions: Is the fixed-template reduction already covered by an earlier screw-function/translate theorem? Can one prove the arithmetic discrepancy uniformly at the q_d tolerance without RH-strength input? Does a given successful representation introduce new carrier obligations? Record these separately from the original OWC realization.

Research disposition: ARCHIVED AND QUEUED. No merge, new CI workflow, or automated monitoring requested by this entry.
