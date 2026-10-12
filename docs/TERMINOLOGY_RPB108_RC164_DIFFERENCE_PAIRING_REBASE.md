# RC164 terminology additions

Historical definitions remain immutable. These definitions apply to the RC163 physical delta trial.

**Direct changed-trial row.** The seven D pairings of q_delta_new with the fixed source frame (P0, f0, w14-alpha*psi0, (v10+z_b6)/2, t10, psi0, delta), evaluated through even degree 16382 with directed coefficient intervals and paid signed analytic polynomial tails.

**Changed trial Gram row.** The seven D pairings of q_delta_new with the five original action approximation columns, q_psi, and q_delta_new. Its last entry is the new trial's own energy. The original delta trial diagonal is not retained as the new diagonal.

**Coherent reference reassembly.** Keep the source matrix W, conditioned source transform X, and rational inverse-source coefficient matrix Y fixed. Substitute the new direct delta row in both the combined endpoint approximation and the nominal residual Gram. Use the improved delta action error with those changed vectors in every Young estimate. The source Gram bounds and Gram functional remain valid without change because the physical source vectors y=WY have not changed.

**Joint candidate selection.** Compare the full inverse-width estimate across the tested weighted/uniform error blends, endpoint Young parameters, residual Young parameters, and structural/variational upper choices. Selecting solely the smallest endpoint width need not select the smallest inverse width.
