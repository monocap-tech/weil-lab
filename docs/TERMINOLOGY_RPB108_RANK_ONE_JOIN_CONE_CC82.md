# CC82 — complete rank-one join cone

Definitions are additive. Use CC81's original residual column y, defect source f1, signed row p=f1*A1^-1R and positive denominator b=d1+f1*A1^-1f1. The exact conditional joined lower matrix K1=Q-R*A1^-1R retains NF42's meaning.

Partition K1=[[E,r],[r*,c]], where E is the leading two-by-two pair and r its two-coordinate border. NF42 certifies E>0 and s=c-r*E^-1r<0. The signed border center is beta=r*E^-1. The effective response coordinate is t=p2-beta pE*, where pE=(p0,p1). Real coordinates are used in the frozen certificates; stars are physical matrix adjoints.

The rank-one join cone is the set of signed rows p and positive denominators b satisfying |t|^2 > (-s)(b+pE E^-1 pE*). This is equivalent to positivity of the entire updated lower matrix K1+p*p/b, rather than just one fixed witness. The equivalent inverse-cone condition is b+p K1^-1 p*<0. These are conditions for this minorant certificate; their failure does not imply negativity of the actual original Weil form.

An outward cone certificate pays every original source and matrix uncertainty, encloses t,b+pE E^-1pE* and -s, and proves the strict cone inequality. The coefficients alone do not certify a newly constructed source row p.
