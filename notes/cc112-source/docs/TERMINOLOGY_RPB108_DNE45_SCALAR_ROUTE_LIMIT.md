# DNE45 terminology: scalar route limit

Registered before DNE45 load-bearing computation; parent DNE44,
`bb7220c07aa66c2fea00bbc36452a59130ee3fb1`.

* **Full-packet scalar threshold**: the largest generalized eigenvalue of
  the original projected source Gram G44 relative to the positive native
  matrix N44, separately in each parity. A floor strictly above this
  threshold makes k N44 - G44 positive. This is a sufficient comparison
  threshold, not the original high operator's least eigenvalue.
* **Fixed arch input**: alpha = 2772351243732/10^12, the inherited certified
  arch-minus-pole lower bound used by the global prime norm subtraction route.
  It is a fixed input of this route, not an upper bound on the true arch term.
* **Global prime operator**: the symmetric clipped sum on (-53/50,53/50)
  with shifts plus/minus log n and coefficients Lambda(n)/sqrt(n),
  n = 2,3,4,5,7,8. It preserves nonnegative functions; no positive
  semidefinite claim is made.
* **Rayleigh norm lower bound**: a positive lower enclosure r of
  <w,Pw>/<w,w>, w=P^17 1, so ||P|| >= r.
* **Scalar route ceiling**: alpha-r. Every valid global norm upper bound
  beta satisfies beta >= r, hence this fixed-input route can certify at
  most alpha-beta <= alpha-r. This excludes closure by improving only
  the global prime norm bound; it does not exclude stronger arch inputs,
  restricted estimates, directional inverse response, or original positivity.

No DNE44 dimensions, original high floor, or physical guard are upgraded
by these definitions. Whole-aperture positivity, first-contact exclusion,
actual high inverse evaluation, RH, and Lean remain open.
