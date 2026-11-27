# IV106 E19 joint replay custody — 2026-11-26 Pacific

The eight-member local replay ZIP is preserved intact in 19 ordered parts. This is a custody snapshot, not acceptance of a theorem. Its joint certificate explicitly says “conditional analytic joint Loewner bound; integer replay not Lean.” The bank digest inside that certificate matches the included row bank: `e55b8992e769d09ee83fdd66a9d6a3cbaf592933f7d85d3ca0d8dd9a2e4d886e`.

Dependency order: `iv106_e19p/row_bank.npz` and `row_bank_receipt.json` → `certify_bank.py` and `bank_certificate.json` → `iv106_e19q/joint_matrix.npz` and `joint.py` → `joint_certificate.json` and `sha256.json`. The upstream analytic hypotheses and runner proof status are not independently verified by this archive. Conditional index ≤205 in the separate canonical-return EP lineage is unchanged; global positivity and RH are unresolved.

Reconstruct with `cat custody/iv106-e19/joint_replay_bundle.zip.part??? > joint_replay_bundle.zip`, then check `sha256sum` equals `8fdfe3275b99f0bd058a99abdfd00e9615a8dc976ca3b7a02763fcf53ee6b49d` and `unzip -t`. Each member's SHA-256 is in `manifest.json`.

| Member | Bytes | SHA-256 |
| --- | ---: | --- |
| iv106_e19q/joint.py | 6732 | `a17002d1987640b3f0efab0c5591ece79c2b15efc9a21c6600ea051ea3e566f1` |
| iv106_e19q/joint_certificate.json | 1015 | `d61da378760ca11e21c7e828b46a717d810116d35dfc03d5ec325f1f6ddbb8c9` |
| iv106_e19q/joint_matrix.npz | 2689684 | `24e37cd533c5efbc554c926695fc89f64d39d60aee90cb6643c5aa3a69da23e7` |
| iv106_e19p/certify_bank.py | 7111 | `814bb90590a546c67bce52659e612657a3e880754957c3aff2d8553391cc1f2a` |
| iv106_e19p/row_bank.npz | 2238992 | `e55b8992e769d09ee83fdd66a9d6a3cbaf592933f7d85d3ca0d8dd9a2e4d886e` |
| iv106_e19p/row_bank_receipt.json | 212443 | `e1f9bf1a11194227e726a9172705a637ff13ebb15afb11fedb5821c8853f8fd1` |
| iv106_e19p/bank_certificate.json | 262710 | `4c4940d86081e9a9d4e412fded7c57fcf5c85aa32824bbb933ab668835d683c4` |
| iv106_e19q/sha256.json | 713 | `1a796b39b16d8dc32425eb27f39771d3a3fa89c37403edbcb153f6b051bc0e0c` |
