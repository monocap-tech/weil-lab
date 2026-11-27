# V10B50 physical constraint-kernel transport

Status: new source readback and named-audit inventory PASS; no native compilation of V10B50 asserted.
Parent ledger V10B49: 744adf315f822cedb7f9f1d8f42fd4c53f2c7b34.

- V10B50a: commit 4cb7880c1c6e4d074f844997529571adda80996f; blob 9a05d6d4e18ee798109fc3b901b8d9b0ed1a6751; named targets moment_literal, eval_literal, pole_literal, adjoint_span_iff.
- V10B50b: commit 2ddcdd5f13efb97d08c92419dcc43f77124dfaad; blob 384ab51f03af9c7898d318bc2a4bd5abef6f3a94; named targets affine_support_integral, reversible_rows.

V10B50a attaches V10B13a.moment and V10B8c.eval to restricted-support integrals of the actual physical inclusion, records the raw pole difference as the difference of integrals, and gives a generic adjoint-span orthogonal-complement iff simultaneous vanishing. It deliberately does not import the blocked V10B17b positivity pilot. V10B50b gives the affine support integral (including half-measure scaling) and generic reversible row-kernel equivalence under explicit forward/inverse row identities and nonzero scalars. These are six staged declarations, not certified. The actual low polynomial expansion, pole deflation integral identity, trial carrier membership, specialization to the V10B17b retained bank, and optimized matrix surjectivity still require native attachment. The original V10B19 ZIP remains unauthenticated. The exact rational row replay is retained as verification/master_recon/v10b49_physical_rows.py; no new computational certificate is claimed here.

Reproduction after dependencies build: lake build WeilDefect.MasterRecon.V10B50a WeilDefect.MasterRecon.V10B50b; lake env lean WeilDefect/MasterRecon/V10B50a.lean; lake env lean WeilDefect/MasterRecon/V10B50b.lean. Check named axioms against {propext, Classical.choice, Quot.sound} and require successful build, not merely axiom output.

Run states observed: [{"id":45927665008,"status":"in_progress","conclusion":null,"head":"4cfc3a85f3e627a50776919c1a300ae8287180f5"},{"id":45928684686,"status":"in_progress","conclusion":null,"head":"dc42ce5d2c6167422748a668bc99ff7e48fc8cbb"}]. No workflow interrupted or activated. Minimum certified inventory 581; staged 819. Arithmetic ADOPT 0; RH unresolved.
