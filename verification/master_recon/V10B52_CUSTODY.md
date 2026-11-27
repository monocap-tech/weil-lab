# V10B52 literal physical polynomial span

Parent V10B51 ledger 518ecc44dbb963313a4203a88e87281c3bd2c0f5. Native verification pending for all new/modified sources. V10B39a repaired from actual run 45928064611 diagnostics: explicit Nat quantifier, field_simp followed by ring, explicit real cast before exact_mod_cast. V10B52a constructs the physical affine Legendre polynomial from shiftedReal and affine composition, establishes degree and evaluation, and derives simultaneous vanishing of monomials and Legendre rows for an arbitrary real-linear polynomial functional. V10B52b constructs the actual physical integral functional using the existing restricted L1 moment integrability and polynomial induction; its terminal theorem is the original fifteen-moment kernel iff the physical Legendre kernel. No rational inverse oracle. No new numerical computation. The V10B49 exact rational coordinate replay remains separate.

| Module | Immutable commit | Blob | Named targets |
|---|---|---|---:|
| V10B39a | 8cfc55ade4274c2eeeab0bc96fb9b52ab25a71e2 | 5590d59494f028ea407efb865f534323372ac425 | 5 |
| V10B52a | 3b32f3c3df190ba358615755cc5de9dc005fbd8c | afe76f8a911789cb4f5e1e4f92385884dc95639b | 5 |
| V10B52b | 76f928d436d3fc5a65b3250190fb14e88d11b4a7 | 4a2e6b845d9cb1420cc13d4b7e37e244a43392f4 | 5 |

All listed sources read back from immutable commits; named axiom command sets match declarations. Reproduce with lake build WeilDefect.MasterRecon.V10B39a WeilDefect.MasterRecon.V10B52a WeilDefect.MasterRecon.V10B52b, followed by lake env lean for each source and strict named axiom audit (only propext, Classical.choice, Quot.sound allowed). No compiled result asserted. Neither existing workflow modified or interrupted. Current workflow states: [{"id":45927665008,"status":"in_progress","conclusion":null,"head":"4cfc3a85f3e627a50776919c1a300ae8287180f5"},{"id":45929425517,"status":"in_progress","conclusion":null,"head":"03764a40922e2dbfd391804e615c6288924731cd"}].

Ten new candidates; conservative inventory 581/829 unless further completed strict audits are independently reconciled. Remaining: literal pole row elimination, actual carrier trial membership, retained-kernel specialization, optimized matrix surjectivity, physical residual-energy congruence, original V10B19 archive authentication. Arithmetic ADOPT 0; global positivity and RH unresolved.
