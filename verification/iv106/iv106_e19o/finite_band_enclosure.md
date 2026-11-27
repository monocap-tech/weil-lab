# IV106-E19O — fixed boundary row numerical upper enclosure

Input: E19N row_pilot.json SHA256 37b6434006b5ef0d56e990e4993517cb22a83d38541f477f2995274ebee968ae.
Original cell width h=11/3325, target index 0. Interior x_i on cells 0..664;
exterior corrections on -64..-1 and 665..728. Let q be delta_0 minus exterior
coefficients. X(u)=sum x_i exp(-2 pi i i u), Z(u)=sum q_i exp(-2 pi i i u).
The raw defect squared is h times the integral over u in [-1/2,1/2] of
sum_{m=-128}^{128} sinc(u+m)^2 |Z(u)-w((u+m)/h) X(u)|^2/w((u+m)/h),
plus the tail |xi|>T=(257/2)/h. The omitted common phase has modulus one.
No supported projection has been equated with the identity.

Integer-only replay used Q=16384 midpoints; coefficient and twiddle FFT at
scale 2^60, certified root by Machin pi and Taylor remainders. Root recursion
error <=12Q/2^60, butterfly max error recurrence e_next <=(2+R)e+2R+2/2^60
with R=12Q/2^60; final error <2^-20. Output floor to scale 2^20 gives
component errors <2*2^-20. Exact rational log bounds by 12-term atanh
series, monotonicity on 2048 central bins and 16 per other alias. Sinc
upper bounds 1 (central) and |u|/|m+u| (other aliases). Integer ceil
arithmetic bounds residual components, squares and weighted sum.
No floating-point FFT, log, sine or quadrature value enters the bound.

Analytic midpoint remainder: for each alias F_m(u)=sqrt(h) sinc(u+m)
[Z(u)/sqrt(w)-sqrt(w)X(u)], weighted direct-sum L2 derivative <=6.
Parseval in u gives norms of X,Z and derivatives from coefficients.
The sinc identities sum_m sinc(u+m)^2=1 and sum_m sinc'(u+m)^2=pi^2/3
follow by Parseval of exp(-2 pi i u t) and -2 pi i t exp(-2 pi i u t)
on [-1/2,1/2]. Bound sqrt(w)<4, w>=1, |d w/du|<120 on band,
and both sqrt-weight and inverse sqrt-weight derivatives by 60 a.e.
Exact coefficient inequalities: ||x||_2<.243, ||q||_2<1.02,
||i*x_i||_2<.462, ||i*q_i||_2<.535. Thus derivative norm <=
.06*(2*(1.02+4*.243)+7*(.535+4*.462)+60*(1.02+.243))<6.
Piecewise midpoint approximation L2 error <=3/Q by Cauchy-Schwarz
on each half-interval. Triangle inequality yields finite-band reserve.
Tail repeated exactly using jump totals, pi>3 and 9<w(T)<11, and
integral_T^infty w(x)/x^2 dx <=(w(T)+1)/T.

Results: midpoint squared <=149238622320777/8556839292003942400;
finite-band squared <=19459861354940449/1024000000000000000000;
tail <=20317889743898149359575333/2163016406250000000000000000000;
total <=31448759235919125311473273621/1107464400000000000000000000000000;
norm <=1332223/250000000 = .005328892.

Status: locally executed exact-integer arithmetic certificate conditional
on the stated Fourier and midpoint estimates. These analytic arguments,
step-function carrier admission and E19M row-error receiver are not yet
natively certified. The full executable replay and certificate JSON are
delivered as conversation artifacts; this note records their result,
not an independent repository-native Lean receipt. No terminal Gram
positivity or RH conclusion.
