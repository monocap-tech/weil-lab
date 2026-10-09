# RPB108 NF41 terminology

This is an additive note; earlier reports and terminology are unchanged.

**Signed boundary/source cross matrix** means J=Y*R, where Y consists of
orthonormal boundary Legendre columns and R consists of the three frozen
NF37 complete physical sources projected off the native retained block.
Because Y lies outside that block, J can be computed directly by original
signed native source pairings. Signs and all three source sectors are retained.

**Projected boundary inverse coupling** means H=Ytilde*A0^-1 R, with
Ytilde=(I-P_span(Z))Y and A0 the NF39 rank-two background minorant.
A nonzero H is physical coupling to inverse source vectors. It is not a
lower bound for the response of the actual defect operator D=A-A0.

**Defect-source columns** means F=D Y=(A-A0)Y. They contain the original
boundary sources AY and the explicit minorant sources A0Y. Their signed
coupling to A0^-1 R, rather than Y's physical coupling alone, determines
whether the boundary defect yields a joined inverse improvement.

**Fixed-cross zero-response extension** means an exact finite Hilbert
model that preserves the chosen enclosure-compatible NF39/NF40 packet,
fixes J inside NF41's original signed cross intervals, and still has
R*(A0^-1-Aminus^-1)R=0. It is a test of information sufficiency, not an
actual Weil operator or an original negative-form certificate.
