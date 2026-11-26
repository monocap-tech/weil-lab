# IV131 checkpoint — explicit function equality repair

Run 45753829426 at 43944ce3ccdba5af7f91379b58b06b4e9988297b: IV124 all five and IV125 four of five printed only standard axioms. IV125Cell_bound alone failed at line 26. The previous simplifier repair did not rewrite the function-level subtraction; this change proves the exact equality by funext and ring, then rewrites before applying Integrable.sub. No mathematical statements changed.

The integrated gate on the IV130 descendant now targets both IV129 and IV130 (43 exact named declarations, seven compiled modules). IV130 has no dependency on IV125–129, but the combined build tests both paths. The workflow remains fail-closed. Native acceptance pending; the previous failed gate did not produce complete compiled custody. No new sign claim.
