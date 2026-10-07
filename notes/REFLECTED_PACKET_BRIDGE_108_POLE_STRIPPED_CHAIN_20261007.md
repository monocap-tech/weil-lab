# RPB108: exact pole stripping exposes an excited pole-free null chain

Date: 2026-10-07 UTC. Recovered live head 33fbef69e59461016b28250f2eb886d3a5ca1fcc and current canonical cursor.
Definitions: [pole-stripped actual chain](../docs/TERMINOLOGY_RPB108_POLE_STRIPPED_CHAIN.md).
Category: actual structural compatibility and outside-theorem hypothesis audit. Analytic, not Lean-certified.

## Result

Use the complete actual operator A=H+2|c><c|-2|s><s| and its already proved r-vector derivative chain K. The following structure is forced without changing the window or deleting actual sources:

1. If the pole moments are active, their rank on K is min(2,r). Hence dim Z=max(r-2,0).
2. For r>=3, L_p=D^2-1/4 maps F_2 injectively into Z. Its image is an actual pole-free null chain of length r-2, with a nonzero terminal endpoint trace. In the active case its image is all Z.
3. If actual A>=0 and Z!=0, H has EXACTLY one negative eigenvalue, simple and even, and zero is an excited eigenvalue. In particular any r>=3 actual contact forces an excited pole-free zero chain, not a pole-free groundstate defect. If the pole moments are inactive, the entire original K is already pole-free, and the same excited-level conclusion holds even for r=1 or 2.

This is useful internal structure, not a replacement global criterion. It does not establish a bound on r, exclude the r=1 or 2 active cases, or produce a bounded signed sharp head.

## 1. Exact moment propagation; no rough differentiation

Choose the real parity generator h_* in F_(r-1), and let h_j=D^j h_*, 0<=j<r. Reality follows by choosing a real generator of the conjugation-invariant one-dimensional top flag. The existing chain theorem gives parity and all the required global Sobolev memberships. Each integration by parts below is taken on a previous global H1 vector, whose zero extension has no boundary delta:

    C(Du)=-(1/2)S(u), S(Du)=-(1/2)C(u).

Consequently (C(h_j),S(h_j))=(-1/2)^j swap^j(C(h_*),S(h_*)). Since h_* has definite parity, at most one initial moment is nonzero. If both are zero, every moment on K is zero. If one is nonzero, the first two vectors have nonzero moments in opposite coordinates (when r>=2), proving the exact rank assertion. There is no claim that the initial moment must be nonzero.

For u in F_2, integrating twice gives C(L_p u)=S(L_p u)=0. The two lawful derivative promotions put D^2u in K, so L_p u is in K as well. Actual full mixed-nullity then gives H L_pu=-P L_pu=0 against EVERY canonical test. A supported form vector with zero representing function is in dom H; this is the physical associated operator equation.

L_p has no nonzero supported L2 kernel: Fourier transformation of L_pu=0 gives (-eta^2-1/4) F_u(eta)=0. Thus the map on F_2 is injective, with image dimension r-2. Active moments give dim Z=r-2, hence equality. Inactive moments give Z=K, and the image is a proper subspace of codimension two.

## 2. The terminal defect survives pole stripping

For r>=3 put w=L_p h_*. Its derivatives through order r-3 are

    D^j w=h_(j+2)-(1/4)h_j, 0<=j<=r-3.

They all belong to Z. Their linear independence follows from polynomial(D) independence on the same compact physical generator. For j<r-3 they are H1. The last has

    kappa_R(D^(r-3)w)=kappa_R(h_(r-1))!=0,

because h_(r-3) is H2 and its endpoint trace is zero. Thus the inherited chain has length r-2 and retains the actual averaged terminal trace. It is not asserted to exhaust ker H outside Z. For r=3 this produces a single rough pole-free zero eigenfunction; no derivative of that rough vector is taken.

This operation changes the physical vector. It does not provide same-vector enlarged/null transport, any historical packet attachment, or a new source carrier. Its source coordinates are those of that newly formed actual supported vector.

## 3. Why this is necessarily an excited pole-free level at contact

The NF39 actual identity shows that A>=0 implies n_-(H)<=1, with every negative spectral vector even. Let 0!=z in Z and choose a nonzero real or imaginary part; H and all moments are real, so this part is still in Z. Since c(x)>0 and C(z)=0, this real z has positive and negative sets of positive measure.

The complete pole-free energy has the Euler jump part and the actual negative prime correlations. Modulus replacement lowers every prime contribution, since Re[z(x)z(y)]<=|z(x)||z(y)| and every w_n>=0. It lowers the archimedean jump part STRICTLY: its positive kernel k(|x-y|) interacts with every opposite-sign pair. Hence

    E_H(|z|)<E_H(z)=0.

Modulus preserves the canonical form domain: the lowered positive jump energy and unchanged mass are finite; finite prime terms are bounded. Therefore H has a negative direction. Combined with n_-(H)<=1, it has exactly one negative eigenvalue counting multiplicity. Compact form inclusion and a mass shift give compact resolvent, so the statement is about the physical discrete spectrum. That eigenvalue is simple and even by the preceding index bound. Its real ground eigenfunction can be chosen nonnegative using the same modulus inequality. Zero is strictly above it; a Hopf theorem for the groundstate cannot be applied to z.

This proof retains all actual primes. It uses no invertibility of H, no cyclicity of c or s, no simplicity theorem for an excited eigenvalue, and no positivity-preserving property of A. Applying this conclusion to r>=3 uses the actual w constructed above, rather than postulating an auxiliary zero mode.

## 4. A precise outside simplicity theorem, and two failed hypotheses

[Kwasnicki-Wszola, arXiv:2609.24892v1, Theorem 1.2 and Section 2.3](https://arxiv.org/html/2609.24892v1) prove interval eigenvalue simplicity via strict Dirichlet-Neumann bracketing for complete Bernstein functions having no meromorphic continuation to C without zero. Its useful transferable hypothesis is stricter than having a positive killed semigroup.

The actual archimedean function is

    psi_0(q)=2sum_(j>=0) q/[alpha_j(alpha_j^2+q)], alpha_j=2j+1/2.

This is a complete Bernstein function, with discrete positive representing masses. The sum converges locally normally off the discrete poles -alpha_j^2. It therefore DOES extend meromorphically. The theorem's strictness hypothesis fails even before actual prime shifts are added. Its non-strict bracketing alone does not imply simplicity.

With any nonzero frozen actual prime dictionary, Phi_a(eta) is not psi(eta^2) for ANY Bernstein function psi. Differentiate the complete actual exponent:

    Phi_a'(eta)=2eta psi_0'(eta^2)+2sum_n w_n log(n) sin(eta log n).

The archimedean term tends to zero: psi_0'(q)=2sum alpha_j/(alpha_j^2+q)^2=O(1/q). This follows by comparison of the unimodal summand with its integral, which is 1/(2q), plus a maximum O(q^(-3/2)). The finite sine polynomial f(eta)=sum w_n log(n)sin(eta log n) is positive near zero and odd, hence negative somewhere. Simultaneous recurrence of finitely many phases produces eta_k->infinity with f(eta_k) bounded strictly below zero. One elementary proof uses Dirichlet simultaneous approximation for log(n)/(2pi); unbounded approximate return times exist, or a bounded returning subsequence supplies an exact common period and its unbounded multiples. Translating a fixed negative point by these returns gives the asserted sequence.

Thus Phi_a'(eta_k)<0 for all sufficiently large k, and d[Phi_a(sqrt(q))]/dq<0 at q=eta_k^2. Bernstein functions are increasing, so the hypothesis fails outright. The prime atoms cannot be dropped because they are bounded perturbations: simplicity and strict bracketing do not automatically survive such perturbations. A scalar eigenvalue shift changes neither this derivative nor the meromorphic archimedean exception.

The outside theorem supplies a concrete mechanism (strict spectral brackets), but no lawful transfer to our actual excited chain. These are checked hypothesis failures, not a claimed counterexample to actual spectral simplicity.

## 5. Controls and dependency standing

| Control | Exact audit |
|---|---|
| Actual rough positive eigenmode | For its whole eigenspace K^mu, moment propagation and pole stripping are identical. They yield (H-mu)w=0, not Hw=0. If A-mu>=0, the one-negative-level statement applies to H-mu. The same construction is therefore compatible with the control, with the spectral level explicitly retained. |
| Artificial compact-good rows | Their correction does not equal this prescribed P and prime operator. No identification with Z or the actual excited spectrum is inferred. Their positive sharp/log slope remains a control against abstract defect exclusion. |
| Fixed finite actual restoration | The proof consumes the full native form. Its known o(1) normalized sharp-head change remains unchanged; changing the form requires changing the operator identities as well. |
| Two-row comparison contact | Auxiliary rows are additional in its null equation. Pole stripping does not silently remove them or produce an actual H-null vector. |

No actual bounded-return/oscillation mechanism found. The global dependency graph does not shorten, and the remaining exclusion theorem is still signed sharp-head arithmetic. The implication actual unshifted source-range nullity -> bounded/sublogarithmic sharp subsequence remains unproved. The new internal target for a long chain is precise: an excited zero eigenspace of the prescribed pole-free killed jump operator, above one simple even negative eigenvalue, carrying pole-annihilated rough data. Eliminating that target would address long chains only; the active r=1 or 2 cases must also be discharged before global/F4 closure.

## Custody and validation

Inputs at the recovered head:

- KERNEL_DERIVATIVE_CHAIN_20261007: e124b8a31a00df61908ce71cedd4ab7f83a14c76.
- NATIVE_ORDER_OBSTRUCTION_20261007: 738289b9df5d11436c79ea72dfbe8e85841904f1.
- CRITICAL_RECIPROCAL_PROMOTION_20261007: 9983be22ab58e926b5e15127f8feaf53d43329e0.
- CRITICAL_EIGENMODE_TARGET_20261007: 3354b89638b643d5b21c4c428f069f738ccf59f5.

The exact companion script checks moment recurrence, active/inactive ranks, stripping image dimensions and terminal-coordinate preservation for r=1 through 16 and both parities: 2,068 assertions pass across 64 cases. Results and input pins are recorded in notes/data/RPB108_POLE_STRIPPED_CHAIN_20261007.json. These are finite algebra controls; analytic domain, strict-modulus, compact-resolvent, recurrence and external-hypothesis arguments are documented above rather than claimed Lean proofs. No external theorem is imported into the global proof as a satisfied dependency. Historical certificates and aperture cursor are preserved. No aperture estimate, RH, F4 or FULL TRANSPORT CLOSED claim.
