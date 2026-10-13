# RC192: complete P0 and P2 action refinement

Starting head: d7f1e98dd02901d3cc50d0df5cec886bb4655b9f (RC191).

RC191's witness-budget accounting identified P2 and f0 as large regular-action payments. RC192 first resolves the exact finite polynomial sources P0 and P2. Their sources have no regular input tail or coefficient approximation error. The aperture, supported canonical operator M=D^-1 L, and D-energy norm are unchanged.

| Source | Previous complete action norm error upper | RC192 complete action norm error upper |
| --- | ---: | ---: |
| P0 | 0.00017934886534629448 | 0.000000009677069110802506 |
| P2 | 0.0005125425305773098 | 0.000000009677223111160453 |

Decimal values in this table summarize exact rational upper bounds in the certificate. They show action precision on the same sources; they do not assert a corresponding reduction in inverse width.

The validator reuses RC179's analytic regular-action construction with exact input coefficient 1 in the indicated Legendre degree. It retains kernel degrees 0 through 192 and all even output coefficients through 768. Polynomial contributions have maximum power 193 for P0 and 195 for P2. Their omitted polynomial output is zero beyond 768. Every omitted logarithmic basis contribution is bounded by the differentiated-beta tail estimate and the triangle inequality. Parameter uncertainty, analytic kernel truncation, coefficient rounding, D-denominator uncertainty, and the complete output tail are paid. The historical 360-digit directed interval contexts suffice for these degree-0 and degree-2 inputs, with no modification to any historical helper.

The endpoint and negative-r corrections are retained from RC171 and RC172, with their inherited coefficient-error norm payments. In particular, P0 retains f0+psi0, and P2 retains its exact xi2 analytic endpoint tail. These tails are not truncated when computing the complete action errors.

Replay reverses the source order and analytic kernel summation order, and requires equality of the entire generated certificate. The certificate binds six input certificates by SHA-256 and verifies the direct historical attachments used for the low-source actions.

No new inverse response is evaluated. RC191's width 1.254303, ratio 2.508606, and failed half-Gram gate remain the latest inverse result. Stage I, original Weil positivity, RH, F4, and Lean closure remain unclaimed. Native v10, z_b6, and t10 action coverage remains open.

Next: refine f0's regular carrier, investigate analytic retention of q185's endpoint output tail, then reconstruct complete mixed rows and recompute the unchanged five-source inverse. The RC192 carriers must be attached to that reconstruction before any inverse improvement is claimed.
