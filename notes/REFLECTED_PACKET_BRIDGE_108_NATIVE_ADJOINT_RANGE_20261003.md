# RPB-108 — native adjoint realization is a range condition
Date: 2026-10-03
Parent: cbd4e49f02c1cbf8394fe1cc9e090e93149a5fde

## Determination

The recovered Green construction is valid for its stated native realization. It does not attach the present WD-T38 carrier merely from unit gain. The missing native adjoint realization can be identified exactly with a regularity/range condition on the canonical background resolvent vector.

This is a written deduction from the retained RPB-24 model, not a new Lean theorem, an actual-zeta counterexample, or an assertion that the actual adjoint realization is impossible. No new conditional representation layer or stronger premise is added.

## Terminology and retained setup

- Reduced compensator: the signed Douglas solution C with S=-TC and Cu orthogonal to ker T.
- Native adjoint realization: an actual k in the transported native L2 space satisfying T* k=Cu. This is an operator-range condition, not membership in the closure of that range.
- Canonical resolvent vector: r_u=A_B^{-1} Phi* u in the ordinary physical interval L2 carrier.

Use the RPB-24 notation R=G^{1/2}. Its retained background congruence is D_B=R A_B R in the form sense, with D_B=TT*, S=R Phi*, and a strictly positive closed background form Q_B associated with A_B. The Green range is H_0^1 and is a core for Q_B. These are the retained model facts consumed here; this pass does not construct their actual-zeta Lean instances.

The signed convention S=-TC is essential below.

## Exact range equivalence

For this model, for each selected u,

```math
\exists k\in L^2:\ T^*k=Cu
\quad\Longleftrightarrow\quad
r_u\in\operatorname{Ran}R=H_0^1.
```

Moreover every such k satisfies

```math
Rk=-r_u.
```

### Forward direction

Suppose T* k=Cu. Then

```math
D_Bk=TT^*k=TCu=-Su=-R\Phi^*u.
```

Set f=Rk. It lies in H_0^1 and hence in the canonical logarithmic form domain.

Test this identity against v in L2 and use the form congruence. It states the background weak equation for f against Rv, with forcing -Phi* u. Because Ran R is a Q_B form core, continuity extends that equation to every vector of the background form domain. The closed-form representation theorem and strict background positivity therefore give

```math
f=-A_B^{-1}\Phi^*u=-r_u.
```

In particular r_u belongs to H_0^1. This proof obtains operator membership for the compressed background equation from its weak form; it does not assume whole-line spectral product L2.

### Reverse direction

Suppose r_u lies in Ran R. Choose k with Rk=-r_u.

Since A_B r_u=Phi* u, the congruence gives D_Bk=-R Phi* u=-Su=TCu. Therefore

```math
T(T^*k-Cu)=0.
```

Both T* k and Cu are orthogonal to ker T: the first by the adjoint identity and the second by reducedness. Their difference belongs to ker T and to its orthogonal complement, and is zero. Hence T* k=Cu.

## Why unit gain does not fill this witness

RPB-24 proves the weaker minimum-compensation identity

```math
C^*C=\Phi A_B^{-1}\Phi^*.
```

If C*Cu=u, then r_u is a full canonical null vector by the retained RPB-30 calculation. This gives logarithmic form membership, not H_0^1 membership.

Finiteness of the inverse-form sandwich in RPB-24 §9 places S u in Ran(D_B^{1/2})=Ran T. That is the range statement needed to solve TC u=-S u. It does not place Cu in Ran T*. The latter is precisely the additional native adjoint realization above. Confusing these two ranges would silently add a regularity witness.

RPB-30 supplies a logarithmic comparison model with smooth finite selected forcing and unit gain whose neutral vector is not even in H^{1/2}. It is not an actual-zeta counterexample. Its lawful use here is to rule out an abstract inference from those structural hypotheses to H_0^1; it does not refute WD-T38's separately stated physical adjoint premise.

WD-T38 hypothesis 6 already assumes an adjoint realization in its specified source H. The current Lean constructor accepts generic H and P and does not identify them with this particular native T. Thus:
- if the actual source is proved to be this native model and the retained adjoint witness is transported into it, the Green route supplies H_0^1 and then spectral L2;
- that actual source/witness transport has not been recovered;
- unit gain alone cannot supply it;
- choosing the canonical resolvent vector and declaring it to be the current carrier would substitute a witness.

## Disposition

Stop the Green/spectral shortcut until the actual source realization is identified. Do not add H_0^1, inverse Green membership, or spectral L2 as a new hypothesis merely to complete attachment.

The next target remains the actual canonical logarithmic source form realization and its endpoint/enlarged mixed observation law, or an already supplied native adjoint witness with an actual transport proof. Existing diagonal/polarization bridges must consume that same-domain law. Actual central cancellation would immediately activate the certified inner-collar regularity and boundary-removal assembly, without a spectral-L2 prerequisite.

## Witness status and validation

No new actual carrier/domain, diagonal, central, regularity-instance, or spectral-L2 witness is proved in Lean here. The exact native range equivalence above is a written model deduction. Actual central cancellation remains OPEN. Spectral L2 for the current carrier remains unproved and unassumed.

Documentation-only checkpoint; five additive/current documentation changes, no Lean, manifest, workflow or historical note changes. The unchanged code retains the prior e1959d1c6858c092a7cc51511bf667b13812768e root certificate. Threshold bookkeeping is CLOSED; F-4 NOT STARTED; WD-T40/RH standing unchanged.
