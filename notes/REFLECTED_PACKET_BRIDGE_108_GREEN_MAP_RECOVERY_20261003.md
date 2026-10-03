# RPB-108 — recovered Green form-carrier map
Date: 2026-10-03
Parent: bd36dee70a3473e2a9e16cafad24f2b709d1af6d

## Scope and terminology

This is recovery of the retained RPB-24 construction and a written derivation, not a new Lean attachment certificate. No conditional representation module is added.

- Native vector: a vector g in the Dirichlet negative-order space H^{-1}_{L_c}.
- Unitary transport: k = U_c g, where U_c extends G_c^{1/2} from the dense L2 copy.
- Physical form map: J_c = G_c^{1/2} U_c; on the dense L2 copy J_c g = G_c g.
- Physical vector: f = J_c g, not k. Its whole-line zero extension is denoted E_c f.
- Green-compatible extension: the map L_a E_{c,a} J_c from the native c-space into the native a-space. Here L_a acts weakly from H_0^1 to H^{-1}, not as an ordinary L2 operator.

RPB-24 already states the map and its form congruence. The prior recovery located actual columns but did not recover this retained carrier-level construction. Historical wording is not rewritten.

## 1. Exact retained map

RPB-24 §§1–4 defines L_c = -d²/dx² + 1/4 with Dirichlet boundary conditions, G_c = L_c^{-1}, and the native completion with squared norm <g,G_c g>.

Its unitary map U_c takes this completion to ordinary interval L2. The physical map is the additional Green square root:

```math
J_c g = G_c^{1/2} U_c g \in H_0^1(-c,c).
```

Confusing U_c g with J_c g would put the source form on the wrong vector. The pulled-back full native form, when the full zero-side synthesis realization is the one in RPB-24, is

```math
q_{\mathrm{nat},c}(g,v)=Q_c(J_c g,J_c v).
```

The retained explicit quadratic identity and complex polarization give this mixed identity on the native source space. The RPB-24 background form has the analogous identity with Q_{B,c}. A background/selected identity must not be renamed a full Weil identity: effective-positive/background elimination still has to match the actual WD-T38 P and C.

This is the bounded form-space representation that avoids identifying a globally bounded ordinary-L2 operator with the unbounded logarithmic Weil operator.

## 2. Energy and spectral membership for this mapped vector

The zero extension of f in H_0^1(-c,c) belongs to H^1 on the line. Plancherel and the weak derivative identity give

```math
\int (1+|\xi|^2)|\mathcal F(E_c f)(\xi)|^2\,d\xi<\infty.
```

The elementary bounds log(e+|xi|) <= C(1+|xi|²) and
log(e+|xi|)² <= C'(1+|xi|²) therefore give both genuine logarithmic form energy and squared-log energy of this actual mapped vector.

Under the retained EXT-5/finite-prime symbol bound at any fixed a,

```math
|\Psi_a^{\mathrm{Mathlib}}(\xi)|\le C_a\log(e+|\xi|),
```

the product Psi_a^Mathlib * Fourier(E_c f) is L2. Thus spectral membership is derived for a carrier genuinely identified with E_c J_c g; it is not assumed and is not inferred from one-log energy.

This does NOT establish spectral membership for the independently supplied current NeutralPhysicalFourierCarrier. Its representative has not been proved equal to E_c J_c g. Nor does it prove every canonical Friedrichs null vector is in H_0^1: the retained resolvent vector of RPB-30 and the Green-mapped native vector have different regularity requirements.

## 3. Endpoint mixed nullity requires no operator-domain shortcut

Suppose the actual full native null equation is realized by the mixed form in §1. Native nullity then gives Q_c(f,J_c v)=0 for every native v.

Every compact smooth u supported strictly inside (-c,c) has the exact native lift v = L_c u. Since J_c is the weak Dirichlet inverse on the native completion, J_c v = u. Therefore Q_c(f,u)=0. No spectral L2 membership is used in this attachment argument.

This recovers the concrete test-lift mechanism; it does not instantiate the actual WD-T38 source realization. It also does not enlarge the test window.

## 4. Fixed physical extension is a separate commuting law

For c<a, let E_{c,a}:H_0^1(-c,c)->H_0^1(-a,a) be zero extension. Define the Green-compatible native extension by

```math
\mathcal E^{\mathrm{Green}}_{c,a}
=L_a E_{c,a} J_c.
```

The weak inverse relation gives the exact commuting law

```math
J_a\mathcal E^{\mathrm{Green}}_{c,a}g
=E_{c,a}J_cg.
```

Consequently, if the retained strict native persistence is realized at a with this extension and the full source form there, the exact test lift v=L_a u transports it to Q_a(E_{c,a}f,u)=0 for every compact smooth test in (-a,a). The existing source-window bridge then supplies the required frozen compact action zero.

This is not automatic for WD-T38's arbitrary extend map. In particular, native distributional extension and fixed physical extension cannot be identified merely by calling both maps zero extension. A general H^{-1} distribution on the smaller open interval has no canonical extension by restricting arbitrary H_0^1 tests from the larger interval; those restrictions need not have zero trace at the smaller endpoints.

For smooth Dirichlet f, applying L to its physical zero extension produces the interior Lf plus boundary delta terms determined by endpoint derivatives. Omitting those terms changes the native source. For rough H_0^1 f the weak operator L_a E_{c,a}f is the lawful definition; no classical derivative trace is presumed.

## 5. Actual custody still missing

The following equalities have not been instantiated in the current Lean branch:

1. WD-T38's source H, P, C, k realize the full native form of RPB-24 (or its lawful effective-positive version).
2. The current concrete carrier's l2Mode is E_c J_c g for that same retained native null vector.
3. The endpoint/right observations are mixed test observations of that same form.
4. Strict persistence's extend is the Green-compatible map, or has an independently proved commuting law yielding the same fixed physical vector.

Choosing a new vector J_c g without these equalities would replace the requested carrier rather than attach its witness. These facts cannot be supplied by reusing the independent density parameter or by assuming spectral membership.

Once these actual laws are recovered, use existing diagonal/polarization/window bridges and immediately invoke the certified inner-collar assembly. It already constructs the regular defect and consumes boundary removal from actual central cancellation, so spectral L2 is optional rather than an attachment prerequisite.

## Standing and next implementation target

| Item | Standing |
| --- | --- |
| J_c = G_c^{1/2} U_c and native form congruence | Recovered retained RPB-24 mathematical construction |
| Exact compact-test lift and compatible extension formula | Written derivation, not Lean-certified |
| Log energy and spectral L2 of E_c J_c g | Written derivation from H_0^1 and retained symbol bounds |
| Identification with the actual WD-T38/current carrier | OPEN |
| Actual enlarged central cancellation | OPEN |
| Regularity/boundary removal from actual central cancellation | Previously Lean-certified; actual central input still absent |
| Spectral L2 from the current typed WD-T38 package alone | Not derived; unproved and unassumed |

The next concrete implementation target is the Dirichlet weak Green map and its carrier/extension commuting identities, not another generic representation record. First pin whether the retained source realization is the full native map or the canonical resolvent construction; the two are not interchangeable.

Documentation-only checkpoint. No Lean modules, manifests, workflows or historical notes change. Existing root certificate e1959d1c6858c092a7cc51511bf667b13812768e remains valid for unchanged code. Threshold bookkeeping is CLOSED; F-4 is NOT STARTED; WD-T40/RH standing is unchanged.
