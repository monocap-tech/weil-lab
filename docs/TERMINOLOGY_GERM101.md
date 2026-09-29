# Terminology registry — GERM-101 additive research supplement

**Date:** 2026-09-29  
**Standing:** RESEARCH-LOCAL / UNRATIFIED  
**Canonical cursor:** SZ-CROSS-COLLAR-3, unchanged

Historical definitions and the GERM-72/GERM-87 corrections remain unchanged.

## Post-nine-visit excess

Let b=e-e100=a-9w, with a=e-e99, w=omega11, ell=c11, r=rho12=ell-10w,
and d=delta13=w-2r. The d here is explicitly delta13, not GERM-91's parameter.
Define tau14=r-35d. Exact logarithm bounds establish 0<tau14<d.
GERM-101 proves exclusion for 0<b<=35d. Formulas below extend through b=r;
that larger formula domain is not claimed excluded.

## Local return matrices

The inputs A0/A1/B0/B1 in the next line retain GERM-100 eleventh definitions.
GERM-101-local twelfth maps are C=B0 A1^9, D=B0 A0 A1^9, E=B0 A1^10.
Their full formula domain is 0<b<=r.

GERM-101-local thirteenth maps are H0=C D, H1=C E, J0=C^2 D, J1=C^2 E.
They act on (0,r), by positive-d rotation; H is the shorter branch and J the
longer branch. The subscript is the initial source bit relative to b.
The verifier keys A0/A1/B0/B1 at level 13 mean H0/H1/J0/J1 respectively.
They must not be identified with the GERM-100 inputs above.

## Fourteenth section and words

K14=(0,d), with return map y -> y-tau14 modulo d. Complete returns have
35 or 36 thirteenth steps. Internal source visits are an initial run.
The complete matrices are J0 H0^(N-s-1) H1^s, N=35,36 and 0<=s<N,
plus J1 H1^34. The next all-internal 36-step product is J1 H1^35.

Three integer charts serve four fixed-parameter regimes. Each chart is
constant along an orbit; no orbit-dependent transition is introduced.
