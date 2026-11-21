#!/usr/bin/env python3
"""PI032: exact integer interval certificate for nine simple n=3 crossings.

Run four independent checks:
  python scripts/pi032_exact_interval_transversality.py --part core
  python scripts/pi032_exact_interval_transversality.py --part 1
  python scripts/pi032_exact_interval_transversality.py --part 2
  python scripts/pi032_exact_interval_transversality.py --part 3

Fixed original PI031 smooth test: m=1, u=3/2. This code evaluates
I(tau), I'(tau), and ||E'||_2^2 with outward integer rounding and
midpoint/Lipschitz remainders. The classical proof in the matching memo
derives Gamma derivative bounds and nine unique-in-bracket simple roots.
No Lean, spectral traces, or CI are used.
"""
from fractions import Fraction as F

S = 10**40

class I:
    def __init__(self, lo, hi):
        assert isinstance(lo, int) and isinstance(hi, int) and lo <= hi, (lo, hi)
        self.lo, self.hi = lo, hi
    def __repr__(self):
        return f'[{self.lo/S:.9f}, {self.hi/S:.9f}]'
    def __add__(self, x):
        v = asI(x)
        return I(self.lo + v.lo, self.hi + v.hi)
    __radd__ = __add__
    def __neg__(self):
        return I(-self.hi, -self.lo)
    def __sub__(self, x):
        return self + (-asI(x))
    def __rsub__(self, x):
        return asI(x) + (-self)
    def __mul__(self, x):
        v = asI(x)
        z = [a*b for a in (self.lo, self.hi) for b in (v.lo, v.hi)]
        return I(min(z)//S, -(-max(z)//S))
    __rmul__ = __mul__
    def __truediv__(self, x):
        if isinstance(x, int) and x > 0:
            return I(self.lo//x, -(-self.hi//x))
        return self*asI(x).recip()
    def __rtruediv__(self, x):
        return asI(x)*self.recip()
    def recip(self):
        assert self.lo > 0, self
        return I(S*S//self.hi, -(-S*S//self.lo))
    def __pow__(self, n):
        assert n >= 0
        z, t = C(1), self
        while n:
            if n & 1:
                z = z*t
            t = t*t
            n //= 2
        return z
    def absmax(self):
        return max(-self.lo, self.hi)

def C(x):
    f = F(x)
    return I(f.numerator*S//f.denominator, -(-f.numerator*S//f.denominator))

def asI(x):
    return x if isinstance(x, I) else C(x)

def expneg_scalar(t):
    assert t > 0
    k, div = 0, 1
    while -(-t//div) > S:
        k += 1
        div *= 2
    z = I(t//div, -(-t//div))
    term = p = C(1)
    up = None
    for n in range(1, 32):
        term = term*z/n
        p = p-term if n % 2 else p+term
        if n == 30:
            up = p.hi
    v = I(p.lo, up)
    assert v.lo > 0
    for _ in range(k):
        v = v*v
    return v

def expneg(T):
    assert T.lo > 0
    lo, hi = expneg_scalar(T.hi), expneg_scalar(T.lo)
    return I(lo.lo, hi.hi)

DELTA = I(C(F(1, 4000000)).lo, C(F(1, 3240000)).hi)
EPS = C(F(1, 20))

def envelope(y):
    """Outward intervals for E, E' and E'' on a rational y interval.

    E=g'''-delta*g', delta=ell^2/4, g=exp(-1/[y(1-y)]).
    Endpoint envelopes use the proved e^20>4e8 and T^k e^-T
    monotonicity for T>=20 and k<=10.
    """
    assert isinstance(y, I)
    outer = (I(-S//4, S//4), I(-112*S, 112*S), I(-62000*S, 62000*S))
    if y.hi <= EPS.lo or y.lo >= (C(1)-EPS).hi:
        return outer
    vals = []
    if y.lo < EPS.hi or y.hi > (C(1)-EPS).lo:
        vals.append(outer)
    lo, hi = max(y.lo, EPS.lo), min(y.hi, (C(1)-EPS).hi)
    if lo <= hi:
        y = I(lo, hi)
        c = 1-2*y
        t = (y*(1-y)).recip()
        g = expneg(t)
        c2, c3 = c*c, c*c*c
        c4, c5 = c2*c2, c2*c3
        t2, t3 = t*t, t*t*t
        t4, t5, t6 = t2*t2, t2*t3, t3*t3
        l1 = c*t2
        l2 = -2*t2-2*c2*t3
        l3 = 12*c*t3+6*c3*t4
        l4 = -24*t3-72*c2*t4-24*c4*t5
        l5 = 360*c*t4+480*c3*t5+120*c5*t6
        b3 = l1**3+3*l1*l2+l3
        b4 = l1**4+6*l1*l1*l2+3*l2*l2+4*l1*l3+l4
        b5 = (l1**5+10*l1**3*l2+15*l1*l2*l2+
              10*l1*l1*l3+10*l2*l3+5*l1*l4+l5)
        vals.append((g*(b3-DELTA*l1),
                     g*(b4-DELTA*(l1*l1+l2)),
                     g*(b5-DELTA*b3)))
    assert vals
    return tuple(I(min(v[k].lo for v in vals), max(v[k].hi for v in vals))
                 for k in range(3))

def check_boundary():
    p = term = F(1)
    for j in range(1, 25):
        term *= F(20, j)
        p += term
    assert p > 400000000
    t, delta = F(20), F(1, 3240000)
    l1, l2 = t**2, 2*t**2+2*t**3
    l3 = 12*t**3+6*t**4
    l4 = 24*t**3+72*t**4+24*t**5
    l5 = 360*t**4+480*t**5+120*t**6
    e = l1**3+3*l1*l2+l3+delta*l1
    ep = l1**4+6*l1*l1*l2+3*l2*l2+4*l1*l3+l4+delta*(l1*l1+l2)
    epp = (l1**5+10*l1**3*l2+15*l1*l2*l2+
           10*l1*l1*l3+10*l2*l3+5*l1*l4+l5+
           delta*(l1**3+3*l1*l2+l3))
    assert e*4 < 4*10**8
    assert ep < 112*4*10**8
    assert epp < 62000*4*10**8

def eval_integral(tau, N, kind='I'):
    assert 0 <= tau < 1 and kind in ('I', 'Ip', 'Ep2')
    start, end = (F(0), F(1)) if kind == 'Ep2' else (tau, F(1))
    h = (end-start)/N
    hs, errcoeff = C(h), C(h*h/F(4))
    total = C(0)
    for j in range(N):
        a = start+j*h
        b = a+h
        mid = (a+b)/2
        E, Ep, _ = envelope(C(mid))
        if kind == 'Ep2':
            center = Ep*Ep
        else:
            Ef, Epf, _ = envelope(C(mid-tau))
            center = E*Ef if kind == 'I' else -E*Epf
        ev, e1, e2 = envelope(I(C(a).lo, C(b).hi))
        if kind == 'Ep2':
            bound = 2*e1.absmax()*e2.absmax()
        else:
            fv, f1, f2 = envelope(I(C(a-tau).lo, C(b-tau).hi))
            if kind == 'I':
                bound = e1.absmax()*fv.absmax()+ev.absmax()*f1.absmax()
            else:
                bound = e1.absmax()*f1.absmax()+ev.absmax()*f2.absmax()
        M = (bound+S-1)//S
        total += hs*center+I(-M, M)*errcoeff
    return total

BRACKETS = (
    (F(106, 1000), F(115, 1000), F(111, 1000), -1),
    (F(477, 1000), F(490, 1000), F(484, 1000), 1),
    (F(692, 1000), F(704, 1000), F(698, 1000), -1),
)

def verify(which):
    check_boundary()
    assert F(3)/F(10, 9)**2 == F(243, 100) > 2
    assert F(3)*F(10, 9) == F(10, 3) < 4
    assert F(8, 9) < 1
    N = 4096
    if which == 'core':
        q0 = eval_integral(F(0), 512, 'I')
        assert q0.lo > C(17).hi and q0.hi < C(21).lo, q0
        norm = eval_integral(F(0), N, 'Ep2')
        assert norm.lo > C(0).hi and norm.hi < C(9000).lo, norm
        print('PI032 I(0):', q0)
        print('PI032 derivative L2 norm:', norm)
    else:
        left, right, center, direction = BRACKETS[int(which)-1]
        L, R = eval_integral(left, N), eval_integral(right, N)
        D = eval_integral(center, N, 'Ip')
        if direction == -1:
            assert L.lo > C(F(2, 5)).hi, (left, L)
            assert R.hi < C(-F(1, 3)).lo, (right, R)
        else:
            assert L.hi < C(-F(2, 5)).lo, (left, L)
            assert R.lo > C(F(2, 5)).hi, (right, R)
        dist = max(center-left, right-center)
        if which == '1':
            assert D.hi < C(-90).lo
            derivative_margin = F(90)-9000*dist
        elif which == '2':
            assert D.lo > C(65).hi
            derivative_margin = F(65)-9000*dist
        else:
            assert D.hi < C(-75).lo
            derivative_margin = F(75)-9000*dist
        assert derivative_margin >= 2, (center, derivative_margin)
        print('PI032 bracket:', left, right, 'I_left:', L, 'I_right:', R,
              'Iprime_center:', D, 'derivative_margin:', derivative_margin)
    mass_upper = F(13, 4)*21
    gamma_scaled = mass_upper/F(450)
    gamma_derivative_scaled = F(7, 2700)*mass_upper/F(900)
    assert gamma_scaled < F(1, 5)
    assert gamma_derivative_scaled < F(1, 1000)
    assert F(3, 2)*F(1, 3)*F(2, 5) == F(1, 5)
    assert F(1, 3)*F(3, 2)*2 == 1
    print('PI032 exact integral/derivative subcertificate PASS:', which)
    print('Four independent parts jointly imply >=9 simple live n=3 crossings; total count open.')

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--part', choices=('core', '1', '2', '3'), required=True)
    verify(parser.parse_args().part)
