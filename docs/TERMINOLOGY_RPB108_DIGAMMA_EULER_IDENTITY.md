# RPB-108 terminology: actual right-half-plane Euler identity

The actual Euler identity means equality of `Complex.digamma z` with the
independently defined `neutralDigammaEulerSeries z` whenever `0<z.re`.
The associated HasSum has endpoint `Complex.digamma z + γ` and the
regularized rational terms registered in the holomorphic-candidate pass.

Analytic uniqueness here uses the connected right half-plane, holomorphy
of both functions and full complex equality at positive real arguments.
The accumulation point is 1, approached through embedded real arguments
strictly larger than 1. Equality of real parts is not the input.
This identity supplies actual representation; source-line residual
cancellation and source attachment remain subsequent obligations.
