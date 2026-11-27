# REGROUP-001 / W02-AM-01 — custody reconciliation

Owner manually uploaded the exact terminal evidence package and instructed verification, recording, and stop. No new mathematics, proof execution, or workflow dispatch.

- Repository: monocap-tech/weil-lab
- Custody branch: staging/iv235-am-final-sector-custody
- Prior governance head: 80a2835b5ca8f3ef335927ef3ff92c9975751032
- Manual upload commit: 93bce03eae92fc9038ab6abd990c29d6d802d932
- Upload tree: 6257fd41edc6c60cd49f42db6c296e10aedfa22d
- Path: custody/W02-AM-01-terminal-evidence.zip
- Remote tree entry: regular blob mode 100644, 8973935 bytes, SHA-1 0cc03067d478267ebcf081eb3250634ffc76b9c1
- Local original package: 8973935 bytes; recomputed Git blob SHA-1 0cc03067d478267ebcf081eb3250634ffc76b9c1; SHA-256 c0b9e1d582c66bc140b45b1c5409339a2f0f128461af4945a142acf6585c0fe2.

Remote branch ref, commit ancestry, tree entry, and content-addressed object identity independently read back and match the original handoff. The upload is a regular permanent Git blob, not an expiring Actions artifact or LFS pointer. Local package CRC and recovery-wrapper CRC passed. All eleven original nested archives passed exact length, SHA-256, Git blob SHA-1 and ZIP CRC against the handoff inventory. This includes integrated artifact 15176097236 (5103453 bytes; SHA-256 775df6e9ff3ffad67f7fe9aa1ed0d7acb1d86643daf39e131d44f7fe82975ebe).

**Evidence boundary:** The remote connector returned the expected blob SHA but no base64 bytes for the large file; alternate blob reads rejected binary as non-UTF-8. Direct raw HTTPS from the local environment failed DNS resolution. Thus permanent content-addressed repository custody is established by matching tree/size/Git object identity; SHA-256 and CRC were freshly computed from the matching local original, not from a newly downloaded remote byte stream. The stricter independent remote-byte SHA-256/CRC gate remains unfulfilled. Do not describe this as direct binary readback or claim final program-level acceptance.

Mathematics and formal verification: IV215 original supported-Schwartz terminal verified at source 12da3689018ed2c6e7e3965f1386cb44f0f0f8a0, run 45930758374. Exact resolved dependency revisions recorded in evidence; original lake-manifest.json not exported. No AP/BK/global positivity adoption.

Disposition: repository archive transfer reconciled at Git-object level; direct binary readback limitation disclosed; adoption held for central review. W02-AM-01 stops. No successor authorization. Record-only commit uses [skip ci]; verification branch untouched.
