# RPB108 smooth-source enclosure terminology

- **Actual smooth source h_i:** the actual interior Q-source for v_i after subtracting the exact endpoint logarithm v_i L.
- **Piecewise polynomial surrogate:** the rational polynomial approximation on the three exact prime panels; normalization by sqrt(2i+1) remains explicit.
- **Uniform source error epsilon_i:** certified supremum error for one source, including kernel truncation, poles and coefficient rounding.
- **Source-map error eta:** an upper bound for the operator norm of the eight-source approximation error from physical coordinates to L2; bounded by the square sum of epsilon_i.
- **Surrogate residual Gram:** the Gram after projecting the surrogate sources off degrees 0..63. Its integral enclosure remains to be computed; the certified source error does not turn a floating Gram into a certificate.

The new result closes the actual source approximation remainder. F4 entry and full transport closure are not asserted.
