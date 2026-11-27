from fractions import Fraction as F
N=665
h=F(11,3325)
c=F(5003,5000)
P=F(471031,125000)
# exp(11/20) <= 1+x+x^2/(2*(1-x)), since n! >= 2 for n>=2
x=F(11,20)
exp_upper=1+x+x*x/(2*(1-x))
assert exp_upper<2
assert N*h==F(11,5)
delta2=N*h**3/12
pole_loss=2*delta2
c0=c-pole_loss
assert c0>1
# Explicit archived E17A Gamma shift, no dependency on new sharper shift.
D=F(12)
lam=c0/(c+P+D)
assert lam>0 and lam<1
assert (1-lam)*(c+P)-lam*D-P-pole_loss==0
assert 1/lam<17
# Optional sharper conditional envelope from grouped-prime receiver.
D2=F(20,3)
lam2=c0/(c+P+D2)
assert (1-lam2)*(c+P)-lam2*D2-P-pole_loss==0
assert 1/lam2<F(23,2)
for k,v in [('exp_upper',exp_upper),('moment_norm_squared',delta2),('pole_loss',pole_loss),('mass_margin',c0),('lambda_D12',lam),('inverse_D12',1/lam),('lambda_D20_3',lam2),('inverse_D20_3',1/lam2)]:
 print(f'{k} = {v} ({float(v):.12g})')
print('PASS: exact cell-only scalar reserve and coefficient identities')
