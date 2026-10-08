"""Exact PS2 physical Schur controls, not an actual arithmetic certificate."""
from fractions import Fraction as F
import json
checks=0
def check(x):
 global checks
 assert x
 checks+=1
c=F(93,100);tau=F(1,320*10**27);M2=F(49)
zstar=tau*c*c/(M2+tau*c)
omega_star=zstar/F(2493,10)
F0=M2/c+tau
for scale in [F(0),F(1,2),F(1),F(3,2)]:
 z=scale*zstar;C=c-z
 check(C>0)
 schur=F0-M2/C
 check(schur==tau-M2*z/(c*C))
 check((schur>0)==(scale<1))
 check((schur==0)==(scale==1))
 check((schur<0)==(scale>1))
 check(F0*C-M2==C*schur)
check(F(55,10**33)<zstar<F(56,10**33))
check(F(22,10**35)<omega_star<F(23,10**35))
check(10*c+240==F(2493,10))

# Independent scalar mixed-block controls for the perturbation inequality.
for c0 in [F(1),F(3,2),F(2)]:
 for c1 in [c0-F(1,10),c0+F(1,10)]:
  for b0 in [F(-2),F(1,2),F(3)]:
   for db in [F(-1,10),F(0),F(1,10)]:
    t=F(1,3);df=F(-1,20);f0=b0*b0/c0+t;b1=b0+db;f1=f0+df
    alpha=abs(df);eps=abs(db);m=abs(b0)
    lower=t-alpha-(2*m*eps+eps*eps)/c1-max(F(0),1/c1-1/c0)*m*m
    check(f1-b1*b1/c1>=lower)

# Physical mass shift: wrong canonical-I replacement changes the Schur law.
f,b,d,mu,mv,mw=F(4),F(1),F(3),F(1,10),F(2),F(5)
physical=(f-mu*mv)-b*b/(d-mu*mw)
wrong=(f-mu)-b*b/(d-mu)
check(physical!=wrong)
check(d-mu*mw>0)
if __name__=='__main__':
 print(json.dumps({'checks':checks,'passed':True,'finite_rational_only':True,
   'complement_loss_contact':str(zstar),'uniform_modulus_scale':str(omega_star),
   'complement_loss_display':float(zstar),'uniform_modulus_display':float(omega_star),
   'scope':'generic block inequality and mass controls; no actual contact or gain bound'},indent=2))
