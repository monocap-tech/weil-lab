#!/usr/bin/env python3
"""NF21: exact algebraic source-square Gram residual identity.

A physical source on finite E_low + H_high has 2 low and 2 measured high
columns; Q is its symmetric original-form model block, R are unseen
physical source coefficients. A real zeta source requires separate
construction of the actual source-square matrix D; this is an exact
algebraic control, NOT a computed complete Weil source Gram.
"""
import sympy as S
F=S.Rational
Q=S.Matrix([[3,F(1,4),F(1,5),-F(1,7)],
            [F(1,4),5,F(2,9),F(1,8)],
            [F(1,5),F(2,9),7,F(1,11)],
            [-F(1,7),F(1,8),F(1,11),9]])
R=S.Matrix([[F(1,7),-F(1,9),F(1,5),0],
            [0,F(1,8),-F(1,6),F(1,7)],
            [F(1,17),0,F(1,19),F(1,23)]])
A=Q[:2,:2];B=Q[:2,2:];C=Q[2:,2:]
Y=C.inv()*B.T
T=S.eye(2).col_join(-Y)
S2=A-B*Y
source=Q.col_join(R)
D=source.T*source
residual_square=(T.T*D*T-S2*S2).applyfunc(S.factor)
projection_source=source*T
assert projection_source[:2,:]==S2
assert projection_source[2:4,:]==S.zeros(2,2)
assert residual_square==(R*T).T*(R*T)
assert residual_square==T.T*(D-Q.T*Q)*T
assert residual_square.det()>0 and residual_square[0,0]>0
print('NF21 exact symbolic source residual Gram identity: PASS')
print('Low source square projection and two-high annihilation: PASS')
print('Physical residual Gram positive definite: PASS')
print('P11 approx:',float(residual_square[0,0]),'P22 approx:',float(residual_square[1,1]))
