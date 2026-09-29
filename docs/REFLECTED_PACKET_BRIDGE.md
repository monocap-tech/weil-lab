# Reflected-Packet Bridge

**Repository:** Weil-Lab  
**Branch:** research/reflected-packet-bridge  
**Standing:** experimental / not canonical promotion  
**Imported provenance source:** monocap-tech/weil@research/reflected-packet-bridge through RPB-35.

## Current standing

~~~math
\boxed{
\textbf{RPB-54 — A NONZERO OPTIMAL LOGARITHMIC BOUNDARY AMPLITUDE FORCES AN UNCANCELLABLE \(\sqrt{\log(1/s)}\) EXTERIOR WEIL LEAK.}
}
~~~

Let \(\widetilde h\) be the zero extension of a compact-window Friedrichs zero
mode and suppose at the right endpoint

~~~math
h(c-r)
=
b_+\,
(\log(1/r))^{-1/2}
+
o\!\left((\log(1/r))^{-1/2}\right),
\qquad
b_+\ne0.
~~~

Using the one-dimensional Chen--Weth integral representation outside the
support,

~~~math
L_\Delta\widetilde h(c+s)
=
-
\int_{-c}^{c}
\frac{h(y)}{c+s-y}\,dy,
~~~

and the model integral

~~~math
\int_0^\delta
\frac{dr}{
(s+r)\sqrt{\log(1/r)}
}
=
2\sqrt{\log(1/s)}
+
O(1),
~~~

RPB-54 obtains

~~~math
\boxed{
L_\Delta\widetilde h(c+s)
=
-2b_+\sqrt{\log(1/s)}
+
o(\sqrt{\log(1/s)}).
}
~~~

Since

~~~math
\mathcal A_\infty
=
\frac12L_\Delta
-
\log(2\pi)I
+
\mathcal S_{-2},
~~~

the actual archimedean contribution satisfies

~~~math
\boxed{
\mathcal A_\infty\widetilde h(c+s)
=
-b_+\sqrt{\log(1/s)}
+
o(\sqrt{\log(1/s)}).
}
~~~

RPB-43's analytic-ellipticity argument extends to every Friedrichs zero mode:
the proof uses compact support plus the scalar equation, not screw-core
membership.  Hence every strict-endpoint active prime translation samples a
fixed analytic interior point and is \(O(1)\) near the exterior edge.

Therefore, away from a prime-power equality threshold, a single nonzero
endpoint amplitude already excludes strict null extension.

At a threshold

~~~math
2c=\log n_0,
~~~

the strict right-limit operator adds the equality-prime translation.  Under a
two-sided optimal logarithmic trace,

~~~math
h(-c+s)
=
O((\log(1/s))^{-1/2}),
~~~

so this correction is still lower by a factor of \(\log(1/s)\) than the
archimedean exterior leak and cannot cancel it.

Thus every optimal-trace mode with

~~~math
(b_+,b_-)\ne(0,0)
~~~

is excluded from strict null extension.

Current branch-local partition:

~~~text
CORE ZERO MODE:
    excluded conditionally by RPB-34–49

NONCORE MODE WITH NONZERO OPTIMAL LOG AMPLITUDE:
    excluded by RPB-54

LOG-FLAT NONCORE ZERO MODE:
    OPEN

BOUNDARY-UNTYPED ZERO MODE:
    OPEN
~~~

## Next cursor

~~~text
RPB-55 / OPTIMAL LOG-TRACE EXISTENCE AND FLAT-RESIDUE TEST
~~~

The next pass should determine whether every actual Friedrichs zero mode admits
a two-sided optimal logarithmic trace

~~~math
h(\pm c\mp r)
=
b_\pm(h)\,(\log(1/r))^{-1/2}
+
o((\log(1/r))^{-1/2}).
~~~

If so, the boundary-untyped residue disappears.  Then test whether simultaneous
vanishing \(b_+=b_-=0\) forces screw-core membership, triviality, or a smaller
next boundary species.

## Governance

The RPB line is a lab investigation. A committed pass may contain proved
branch-local statements, imported results, scope/no-go statements, or open
residue. Commit status is not canonical status. Promotion into the stable Weil
theorem line requires a separate explicit audit.

Historical RPB notes are immutable. Later corrections are additive.

## Ledger

The full pass-by-pass record is stored in notes/REFLECTED_PACKET_BRIDGE_0_20260928.md through notes/REFLECTED_PACKET_BRIDGE_54_20260928.md.
