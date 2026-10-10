# RPB108 — CC98: quantify the integrated collective source margin

2026-10-10 UTC, October 9 America/Los_Angeles. CC parent 1e0ac7d82e5e6493259ec9f5bbd07d868854d805. Read-only DNE35 and Native Source NF48 heads remain 2154898d5d346883cfb201d3a846f19758ac72da and 6847ef8c2501682d60d497043f510987dd70d93b. [Definitions](../docs/TERMINOLOGY_RPB108_COLLECTIVE_SOURCE_CREDIT_CC98.md) precede use.

CC98 certifies native-energy-relative source bounds on the entire integrated twelve-column packet per parity:

| Paid collective bound | Even | Odd |
| --- | ---: | ---: |
| Source Gram upper relative to original native Q | Gamma < (197/500)Q = 0.394Q | Gamma < (47/125)Q = 0.376Q |
| Margin beneath original high floor 0.44 | 23/500 = 0.046 | 8/125 = 0.064 |
| Retained rank of this packet | 12 | 12 |

These are new quantitative collective credits for the already-certified 24-direction restriction. They are not new retained directions or a whole-aperture certificate. Unlike the tiny physical gap, the credit directly controls the energy-normalized interaction with the next block.

The consumer first reruns CC97's authenticated source and collective checks. It then retains every original native/source interval, forms (0.44-c)Q-Gamma, and transforms it by the fixed DNE35 rational congruence. Floating Cholesky selects a further rational congruence on a 10^-30 coefficient grid. Fresh outward Fraction arithmetic checks strictly positive paid Gershgorin margins after both transformations. No floating eigenvalue or midpoint sign is accepted as proof. The frozen new matrices and paid margins are recorded in the machine certificate.

The next joint certificate can use Ht>=c A for the current packet, Hr>=d C for the new remaining frame and the signed mixed block E=0.44 B-Gamma_tr. A paid t bounding ||A^-1/2 E C^-1/2|| gives the sufficient criterion t²<c d. The resulting remaining signed Schur lower is (d-t²/c)C. This preserves cancellation between native and source cross terms and does not allocate the new source norm below the tested packet's credit as an independent scalar budget.

The criterion follows from Ht^-1<=A^-1/c and E-star A^-1 E<=t² C. It is a sufficient common-matrix test, not a claim that the actual remaining block has any particular d or t. Native Source NF48's finite native positivity supplies useful original native information on its named frame; it supplies no new Gamma_rr or Gamma_tr and cannot discharge this source condition by itself.

Exact controls use positive finite native and complete source Gram matrices throughout genuine positive/null/negative signed joint crossings. At coupling values 1/7,1/6,1/5, credits 1/4 and 1/9 give the three signs of d-t²/c. The same test runs at coordinate scale 1e-18 and retains the true crossing. These are assembly controls, not original Weil counterexamples.

Relative to the imported restriction, 44 retained dimensions per parity remain uncovered. Completing its source Gram requires 990 symmetric remaining entries and 528 signed packet/remaining entries per parity. Current credit changes the available acceptance margin; it does not remove those complete-source obligations or justify adding separately certified ranks.

Reproduction:

```sh
python3 scripts/certify_cc98_collective_source_credit.py notes/cc97-source --output notes/data/RPB108_CC98_COLLECTIVE_SOURCE_CREDIT_20261010.json
```

PASS: authenticated CC97 replay, exact paid credit congruences and six extension-crossing controls. No new original source integration or remaining-source sign is claimed. The 24-direction-plus-all-F physical guard above 10^-37 and NF48's byte-identical original replay remain standing. Whole aperture remains 21/20=1.05; whole 53/50, all-aperture continuation, RH, F4, full transport and Lean remain open. Other branches are unchanged.
