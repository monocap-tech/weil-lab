"""Exact rational replay for the literal E18 polynomial bank.
No floating-point values enter the inequalities.  This is a computational
reserve, not Lean attachment or a bound on the full receiving Gram.
"""
from fractions import Fraction as F
from math import comb

def derivative(p):
    return [i*p[i] for i in range(1,len(p))]
def square_integral(p):
    return sum((a*b/F(i+j+1) for i,a in enumerate(p)
                for j,b in enumerate(p)),F(0))
h=F(11,3325)
b=[F(0)]*5+[F((-1)**j*comb(5,j)) for j in range(6)]
b1=derivative(b)
b3=derivative(derivative(b1))
v=[(b3[i] if i<len(b3) else F(0))-h*h*b1[i]/4
   for i in range(len(b1))]
mass=h*square_integral(v)
derivative_energy=square_integral(derivative(v))/h
# exp(1)+1 < 4 and 4*pi*pi > 36.
upper=4*mass+derivative_energy/36
assert mass==F(12994320639248774641,98293908912022687500000)
assert derivative_energy==F(27926390440838204641,16514364829462500)
assert upper==F(838028049024262044253097491,17840344467532117781250000)
assert upper<49
print("physical mass squared:",mass)
print("physical derivative energy:",derivative_energy)
print("rational log-energy upper:",upper)
print("PASS exact rational reserve M=7 conditional on E18V energy and affine integral attachment")
