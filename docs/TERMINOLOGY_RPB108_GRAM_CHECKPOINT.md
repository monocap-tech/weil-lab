# RPB108 terminology: recoverable complete Gram panels

- **Complete panel checkpoint:** the cumulative CS, smooth and cross interval matrices after an integer number of whole translation panels, together with the panel count. Partial panel work is never resumed.
- **Lossless endpoint encoding:** each endpoint is an integer multiple of the current 10^-300 interval grid, stored as its exact scaled integer. Loading reconstructs precisely the original rational endpoint.
- **Input binding:** the source, native matrix, Gram constructor, geometry engine, Hankel helper and checkpoint codec hashes, aperture and logarithm precision must all match before recovery. The matrix keys, dimensions, grid and interval order are checked.
- **Independent repetition:** separate runs use separate checkpoints. Agreement is assessed on complete certificate outputs, not on intermediate state.
- **Recovery scope:** a checkpoint retains completed contractions; it is not a sign certificate. Endpoint primitives and the final projection, correction and sign audit must still complete.

This registry supplements the 9/10 definitions without modifying any earlier mathematical certificate.
