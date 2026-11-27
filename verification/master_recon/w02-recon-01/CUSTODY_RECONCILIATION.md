# W02-RECON-01 — Native evidence custody reconciliation
Owner-directed verification only; no mathematical execution or workflow activation. Prior gate report d5e0bc25bc702c0d92744d8b610a18654bbfe64a is historical and unchanged. Owner manually uploaded original evidence package; this reconciliation closes its bounded native-archive transfer deficit, not all historical custody deficits.

## Remote identity — PASS
Repository monocap-tech/weil-lab; branch master-recon-v10b20-staging; owner upload commit 7d0a1978f5b97f2d482b430577dec2eedbe4e19d.
Path verification/master_recon/w02-recon-01/W02-RECON-01-native-evidence.zip
- Actual Git blob 4ea35319249b0c4a20043e591170e2c782d7b9da.
- Actual decoded remote byte count 697891.
- Actual decoded remote SHA256 8010010abeaf1ab08cb35cd222c99f5235b35556aaaa08b71bff67c81153c78d, exact match to frozen GATE_REPORT.md digest.
- Full remote file fetched at immutable upload commit with base64 encoding (930524 base64 characters after whitespace removal); decoded and SHA256 computed directly in the connector execution environment (standard SHA256 implementation checked on abc test vector). No inference from metadata alone.
- Independently computed local original package length, SHA256 and Git blob SHA1 match remote. Archive inspection used this hash-identical local copy, not an assumed remote mount. Python hashlib, zipfile.testzip and JSON parsing used. Outer ZIP CRC/integrity PASS; exact outer member inventory PASS (manifest.json plus twelve original ZIPs, no extras).
- manifest.json 116731 bytes, SHA256 a38313d2074da705d0f485daa3fbceda3bbc921f01d1f9e2b4370020052996a3. Operation, repository, branch, frozen mathematical head and predecessor head all match. Unique run IDs and artifact IDs: 12 each.
- All nested ZIP sizes, SHA256 digests, Git blob SHA1 identifiers and CRC tests PASS. All twelve nested ZIPs additionally byte-equal to the corresponding locally retained original downloaded archives. All listed nested paths, entry sizes and SHA256 digests verified, no unlisted or duplicate entries within any archive. Totals 579356 original ZIP bytes, 656 entries (not unique across archives).

| Run | Original artifact | ZIP bytes | Entries | SHA256 |
|---|---|---:|---:|---|
|45929425517|15167614615|23307|43|dc57c449a4dba108a8dce2c448d058f4597c92836aafb02282b9ee7acf66639f|
|45928684686|15167543830|11516|25|ef48e1d2521251050175a23d128af05901b34762cfa5754a052509d4a16baf5f|
|45928064611|15167378493|102377|121|c300ca6f7b18405d55a1eebd6a56b994e807ef4c6b28ab2f21682ea4d8313433|
|45927665008|15169035564|4518|12|6bc26d95b08f85b45dfe08af03dc177ce0ac845f2e9c1ed5c6151f23de2bf821|
|45927293904|15167560423|5672|8|bd3d230d85f73fdb15868741eea8ca4feb97b72dfd89f9a68dd0dfd03c107d15|
|45927275023|15167166546|548|2|e7013483598ed1c28fbf32017bac3502ad6bfa8b4015d56a41451ce9a9ab03ce|
|45926940051|15166937559|95070|110|a6a2f54c14cf9100166639b0a0dc921fa1d50e5520ee58f6978cba8610a9a112|
|45925779995|15167046090|91282|95|271940a9e7719e79ba5ce41ee2fe7fad90e6178303611fb7d0ada829f509617b|
|45924912449|15166152045|83671|83|0bcd0163a2801f57e3faa75aa0c1305d3a20b32d3115d1c7cac3a6dd56e36b30|
|45924191517|15165837407|57560|65|b61df4161a5766e6aab507fa838004e97e2dd0b84ec4017562aff9af2b5c4f98|
|45923353564|15164778233|52394|51|e086c38c127536ead7a6c7fa8e878d1f3f58398bd58cf2f9094028ced533df1c|
|45922355675|15165576061|51441|41|7d911cc7f0a0ef17e65c55ffb109909af2e7b680bd82931e673d72d613ffcf72|

All twelve match the original provider digests recorded in the frozen gate report; no claim of a new independent provider archive census outside that scope. Two prior standalone ZIPs remain; all twelve are now durably contained within the original bundle.

## Scope and stop
Compared upload head with d5e0bc25: one commit ahead, only the ZIP added. Pre-record workflow census: 12 total, none active, no runs associated with owner upload commit. Reconciliation is an additive documentation-only commit with [skip ci], no workflow dispatch or branch creation. Frozen mathematical source V10B52 at 3973964c66f368d1aa3fbe58dda833245e879dfe, accepted subsets and reported 608/829 inventory unchanged; no new certification. Arithmetic ADOPT 0.
Custody PASS for 12/12 native archives of the frozen staging branch census. Original V10B19 physical-generation archive remains missing; explicit supersession proposal still pending. Earlier branch history not exhaustively audited. 108-W collective acceptance and actual physical receiver remain open. No mathematical release or dependency adoption inferred from this custody reconciliation. Stop after repository record and readback.
