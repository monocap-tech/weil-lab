# RPB108: matched eleven-panel residual Gram at 49/50

Additive definitions, 2026-10-07 UTC.

- The source surrogate is the complete 90/104 polynomial source with the exact universal endpoint-log contribution added separately. All eleven panels and all endpoint, smooth and mixed terms are retained.
- The residual Gram projects away all 96 physical Legendre coordinates from that actual matched source. Its outward intervals use a 300-digit grid; the integration degree is derived from the complete source polynomial lengths.
- The complete panel checkpoint stores all native/source contractions, smooth Gram entries and endpoint-log mixed contractions. Its decoded hash is distinct from the compressed archive hash.
- The actual Gram correction is delta=eta(2M+eta), where eta is the complete source-map allowance and M bounds the surrogate residual-map norm. Both are tied to the saved inputs.
- The corrected Schur matrix is Q96-(125/104)R96-[(125/104)delta+tau]I. The factor 125/104 is the inverse of the independently proved complement 104/125.
- A finite physical Schur margin tau and a lift bound L give whole-domain physical coercivity mu=tau*c/[tau+c(1+L^2)]. Gårding constant 24 gives logarithmic coercivity mu/[10(mu+24)]. Positive source, finite-block and complement checks alone do not prove these bounds.
- Extraction-stage audit flags precede the corrected sign decision. Final whole-domain standing, if established, belongs to the final conversion validation record.
- Repeating identical stored archives checks custody only. A fresh-construction repeat starts each constructor with a distinct absent checkpoint.
- Fixed-aperture whole-domain positivity does not close global endpoint exclusion, F4, full transport, Lean formalization or RH.
