# RPB108 LF24: actual exterior half-line kernel identities

Submit the exact right and left exterior identities for the actual jump
kernel. At an interior observation point x, integration over y>B equals
tail(B-x), and integration over y<-B equals tail(B+x).

The right change of variable is r=y-x, a volume-preserving translation;
its preimage of r>B-x is y>B. The left change is r=x-y, a volume-preserving
reflection followed by translation; its preimage of r>B+x is y<-B.
On these respective sets the absolute difference is exactly the chosen
positive distance. The restricted integral identities are therefore exact.
Convergence of the target tails at these positive distances is supplied
separately by the checked LF12 theorem, not inferred from totalized values.

This identifies the two real geometric exterior pieces. A complete
complex zero-extended jump split must still combine the internal cancelled
integral and both exterior pieces with verified integrability. Mixture
exchange, weak physical attachment and spectral identity remain open.

At submission LF22 run 38103549861 is in progress. Checked modules remain
LF05 through LF10, LF12 and LF19; complete-root validation remains LF01
through LF04. LF13/LF20/LF21/LF22/LF23 and this LF24 module await cumulative
CI. There is no local Lean executable. Targeted CI and root imports include
the new module. No hand-written sorry, admit or project axiom is introduced.
Research refs remain unchanged. No aperture, F4 or RH claim is made.
