# RPB108 prime-3 activation terminology

- **Activated prime-3 aperture:** a=11/20, with log(3)<2a<log(4). The native prime powers are exactly 2 and 3.
- **Five-panel source custody:** the exact source coordinate t=(x+a)/(2a) has cuts 0, 1-log(3)/(2a), 1-log(2)/(2a), log(2)/(2a), log(3)/(2a), 1. Every active translated polynomial is included on its proper panel.
- **Compressed prime-3 adjacency:** C_3 is the sum of the supported translations by plus and minus log(3). At this aperture the two edge strips are disjoint and C_3 swaps them, with physical L2 operator norm one. The actual prime-3 form is -(log(3)/sqrt(3))<f,C_3 f>.
- **Twenty-moment complement limit check:** a negative sufficient lower bound obtained by subtracting the sharp compressed prime-3 norm penalty from the previous prime-2-only estimate. It does not establish actual negativity or prove that every twenty-moment estimate must fail.
- **Thirty-six-moment complement certificate:** actual physical coercivity 1/4 and logarithmic coercivity 9/100 on the complement of degrees 0..35, uniformly for 1/2<=a<=11/20. This supplies inverse factor 4 and a lawful 36-coordinate exact Schur reduction, without deciding its sign.
- **Prime-3 omission control:** the source/native constant-vector pairing error caused by deleting prime 3 exceeds its certified source error, so the incorrect source cannot pass the custody check.

Historical statements are unchanged. Whole-domain positivity is certified through 27/50; the full sign at 11/20, global endpoint exclusion, F4 and FULL TRANSPORT CLOSED remain open. No Lean formalization is claimed.
