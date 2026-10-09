# CC88 correlated response terminology

Definitions are additive; historical statements remain unchanged.

* **Paid high moments:** physical M=H*H, native QH=H*AH and complete source GH=(AH)*(AH), with the original projection and all inherited physical/source errors.
* **Woodbury denominator N:** C+T/kappa, where C=QH-kappa M and T=GH-2 kappa QH+kappa^2 M. Exact cancellation gives N=GH/kappa-QH.
* **Signed coupling W:** R*(A-kappa I)H, computed as joined source crosses minus kappa times joined native crosses.
* **Block innovation z:** w7-W6 N6^-1 n, where N7=[[N6,n],[n*,n77]] and W7=(W6,w7).
* **Direct seventh response:** z z*/[kappa^2 (n77-n*N6^-1n)]. This encloses the same original inverse improvement as subtracting the six- and seven-source reaction matrices, while retaining their algebraic correlation.
* **Verified inverse enclosure:** a rational midpoint inverse plus a Neumann residual error bound. It is checked against the complete paid moment intervals.
* **Tightened interval matrix:** entrywise intersection of two valid interval enclosures for the same original lower matrix. An interval matrix is not itself a Loewner lower bound for every arbitrary entry choice.

CC88's positive even witness response is a certificate-level refinement of NF45, not a new polynomial or whole-domain positivity result. The background floor A >= (207/1000) I remains an explicit hypothesis.
