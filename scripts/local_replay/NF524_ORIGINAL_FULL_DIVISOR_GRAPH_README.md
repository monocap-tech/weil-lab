# NF524 — Actual zeta divisor graph source verification

Source SHA: 39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181 (NF494 H400/U400, all original 400 coefficients).
Read the source proof and scope from notes/provisional/NF524_ORIGINAL_ENDPOINT_ACTUAL_TWO_SOURCE_GRAPH_20261115.md.

Replay in Python 3.11+ with no third-party dependencies:

1. Run the first exact Fraction check:
   python scripts/local_replay/verify_nf524_original_endpoint_divisor_sampling_exact.py --output /tmp/nf524-primary.json
2. Supply the original NF494 SHA-pinned native JSON from original archived source (it is not duplicated in the repo), and run:
   python scripts/local_replay/verify_nf524_independent_original_400_source_pair_tail.py --nf494 /path/to/nf494-original-J8-source-H400-joint-compact-native.json --primary /tmp/nf524-primary.json --output /tmp/nf524-independent.json

The first verifies the complex-window Fourier decay 1e-4*(1+log(2+t))/(1+t), exponential-strip fee and dyadic tail by exact Fraction. The second independently rechecks all genuine original U400 coefficient balls, reverse dual-Horner U and U' Cauchy fees and the dyadic tail. No numerical zeta-zero list is required. The dyadic actual full divisor multiplicity count bound is already proved in WeilDefect/Arithmetic/ActualZetaDyadicSummability.lean. The mathematical graph-lift and exact-242-moment smooth graph-convergence proof uses that existing theorem; it has NOT been newly Lean compiled.

The full reproducibility package, including original ~1MB source native JSON and exact locally accepted receipts, is NF524_original_two_source_divisor_graph_exact_pack.zip, SHA256 162ed903e833c869275abd94ee622b15490101a72e8138f9fcd75bae56759fb3.

Actual Green-packet closed-span membership and the same-source complete signed Weil diagonal are NOT established by source graph membership. W_ODD_NEG, RH, GitHub CI OPEN. No merge to main.
