# CC114 fixed-trial response terminology

Definitions are registered before use. Historical terms and certificates remain unchanged.

* `L`: the original unshifted operator compressed to the complete infinite F112 space, with certified physical lower bound k=647/1000.
* `f`: the complete projected source of the original 44-column packet Z.
* `Y`: CC113's authenticated pure-high physical trial family (11 even, 10 odd).
* `W=f*(L-k)Y`: CC113's complete signed response cross matrix.
* `N=Y*L(L-k)Y/k`: the CC113 finite response denominator, already certified positive.
* `H`: a frozen rational trial coefficient matrix, with one row per Y column and 44 columns. Numerical solves only propose H; acceptance treats every coefficient as exact.
* `Fixed-trial credit`: (WH+H*W*-H*NH)/k². Unlike optimized credit, it requires no evaluated or certified inverse.
* `Optimized credit`: W N^-1 W*/k². Its difference from fixed-trial credit is (H-N^-1 W*)*N(H-N^-1 W*)/k², positive semidefinite.
* `Residual trial`: J=H/k. DNE48's residual-response formula with the same physical Y equals the fixed-trial formula exactly. Different trial families can yield different bounds.
* `Local inverse elimination`: removal of certified finite inversion from acceptance for this existing packet. It does not imply lower total source construction cost or a general computational complexity advantage over the plain bound.
