from fractions import Fraction as F
h=F(11,3325)
a=F(11,10)
c=F(5003,5000)
P=F(471031,125000)
# exp(a/2) <= 1+a/2+(a/2)^2 < 2
exp_bound=1+a/2+(a/2)**2
assert exp_bound<2
column_sq=4*2*a
moment_sq=F(1,4)*column_sq*h*h/6
loss=2*moment_sq
c0=c-loss
assert c0>1
# G+12M >= L; P<=P0 M; pole >=-loss M
assert 12+P+loss <= 16*c0
inv=(c+P+12)/c0
assert inv<17
for k,v in [('exp_upper',exp_bound),('moment_column_norm_sq',column_sq),('primitive_moment_sq_factor',moment_sq),('pole_loss',loss),('mass_margin',c0),('inverse_bound_D12',inv),('inverse_bound_D20_3',(c+P+F(20,3))/c0)]:
    print(k, '=', v, f'({float(v):.12g})')
print('PASS: exact primitive-pole budget and factor-17 receiver')
