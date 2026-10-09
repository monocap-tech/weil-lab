# RPB108 NF42 terminology

This note adds definitions without changing NF39–NF41 or earlier reports.

**Boundary defect-source covariance packet** means the original physical
source moments (AY)*AY, (AY)*AZ and (AY)*R, after the same native retained
projection used in NF38–NF41. It includes all signed crosses, both boundary
modes, and payments for the analytic physical source approximation errors.

**Conditional joined inverse improvement certificate** is a physical
matrix lower bound for R*(A0^-1-A^-1)R under the stated background-floor
hypothesis A >= kappa I. It does not newly prove that hypothesis or certify
a whole-domain sign. A positive value on one frozen witness is not a
positive gap for the whole three-dimensional joined response matrix.

**Four-high-source minorant** means kappa I+U C4^-1 U*, where
H=(Z0,Z1,Y0,Y1), U=(A-kappa I)H and C4=H*U>0. It agrees with A on the
four named high columns and lies below A under the floor hypothesis.
Its inverse equals the sequential NF41 defect-source Woodbury update.
Failure of its resulting joined Schur lower matrix is failure of this
certificate, not a negative original Weil form.

**Carry-free integer convolution** means exact binary packing of integer
polynomial coefficients with enough bits that no coefficient carries into
its neighbor. Signed coefficients are recovered by subtracting known
offset convolutions. Interval products use integer centers and radii with
outward division by the fixed grid. This is exact arithmetic, not a
floating-point Fourier transform or numerical quadrature.
