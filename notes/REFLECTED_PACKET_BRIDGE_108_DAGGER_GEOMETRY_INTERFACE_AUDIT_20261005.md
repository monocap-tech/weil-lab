# RPB-108 dagger-geometry interface audit — 2026-10-05

## Standing

**Source:** Jón Hákon Garðarsson and Paolo Perrone, *Dagger Categories in Riemannian Geometry*, arXiv:2610.02257v1, submitted 2026-09-30.

**Repository status:** external literature audit / contextual, non-load-bearing.

**Immediate effect:** no theorem is closed, no current RPB hypothesis is discharged, no Lean dependency is added, and F-4 remains open.

The source is nevertheless close to the current carrier/analysis architecture and should be cited rather than rediscovered whenever the project discusses the general relation between daggers, metric data, orthogonality, and formal adjoints.

---

## 1. Exact external statements relevant to the project

The source proves the following results at a level more general than the finite-dimensional language normally used informally in the RPB notes.

### 1.1 Dagger reconstructs Hermitian metric data

Theorem 5.8 classifies daggers on finite-dimensional vector spaces over a field: a dagger determines a unique involution of the scalars together with a unique family of unimodular Hermitian forms, standard on the scalar object, whose adjoints are the given dagger.

Theorem 7.8 extends the same pattern to finitely generated projective modules over a commutative ring.

This is relevant as **general background** for the principle

```math
\text{coherent adjoint operation}
\quad\Longleftrightarrow\quad
\text{nondegenerate Hermitian metric data}
```

in the categories treated by the paper.

It is not a new RPB theorem and must not be presented as one.

### 1.2 Orthogonal complements as dagger kernels

Proposition 6.16 states:

> For an **isometry** (i), an orthogonal complement of (i) is the same as an isometric kernel of (i^{\dagger}).

This is the closest external result to the current RPB observability language, but its hypotheses matter.

It does **not** say that for an arbitrary bounded observation or synthesis map (G), the quotient by (ker G), the closure of (operatorname{Ran}G^{\dagger}), and every desired positive-energy completion follow categorically without further analysis.

The RPB Hilbert-space identities and closure statements therefore retain their own proofs and custody.

### 1.3 Formal adjoints split metric and divergence data

Theorem 13.3 classifies daggers on the locally graded category of differential operators of a Lie–Rinehart algebra by a metric-divergence structure: real structure, divergence, and unimodular Hermitian forms. The dagger acts as the formal adjoint.

The paper further records that the metric and divergence are independent data (Propositions 13.7 and 11.12), while Green-type formulas express the discrepancy between an operator pairing and its adjoint pairing as a divergence.

For RPB this is a useful **architecture warning**:

```math
\text{metric / bulk quadratic geometry}
\qquad\text{and}\qquad
\text{boundary-divergence correction}
```

must not be conflated merely because they occur in one adjoint or integration-by-parts identity.

No identification is made here between the paper's abstract divergence and the actual Weil prime, pole, archimedean, boundary, or residual terms.

---

## 2. Mapping to the current RPB carrier architecture

The live RPB stack already distinguishes:

- raw actual-divisor multiplicity copies;
- physical Green synthesis;
- graph closure;
- graph analysis as the adjoint of the bounded synthesis;
- the analysis kernel;
- same-ordinate copy collisions in coefficient space;
- canonical logarithmic form-domain energy;
- full-source positivity/coercivity.

The new source is compatible with that separation but does not collapse it.

### 2.1 Copy redundancy remains a synthesis-kernel fact

Same-ordinate divisor copies can synthesize identical graph packets. Their coefficient difference is therefore a nonzero vector in the **coefficient-space synthesis kernel**.

This does not produce a nonzero vector in the source-graph analysis kernel.

The current terminology files already enforce this distinction. Proposition 6.16 should not be used to erase it.

### 2.2 Observable quotient/completion remains project-specific

A natural observation carrier may be represented schematically by

```math
\mathcal H_{\mathrm{raw}}/\ker G
```

followed, when needed, by the lawful Hilbert or form completion.

Garðarsson–Perrone supplies useful categorical vocabulary for dagger-compatible orthogonality, but it does not prove that the current actual-divisor raw carrier automatically has the exact quotient norm, completion, source identity, or energy required by WD-T10/F-4.

Those are still RPB transport and coercivity obligations.

### 2.3 Analysis-kernel orthogonality keeps its native Hilbert proof

The current actual Green graph analysis is the adjoint of the proved bounded actual Green Hilbert synthesis, and its kernel is identified with the orthogonal complement of the certified graph closure.

That statement is already native Hilbert-space analysis.

The new paper provides conceptual neighboring structure, not a replacement proof.

---

## 3. Positivity firewall

The most important scope guard is explicit in the source: **no positivity is imposed**. Indefinite Hermitian forms, including Minkowski-type examples, are admitted on the same footing as positive-definite forms.

Therefore

```math
\boxed{
\text{dagger coherence}
\not\Longrightarrow
\text{positive-energy coercivity}
}
```

without additional hypotheses.

For the current project this means:

```math
\text{dagger / adjoint geometry}
\quad\text{is upstream of}\quad
\text{full-source WD-T10 domination / F-4}.
```

The certified half-aperture estimate

```math
Q(h)\ge \frac{1}{520000000}\lVert h\rVert_2^2
```

is strictly stronger information of a different type. It is not supplied by the dagger classification.

Larger apertures, global endpoint exclusion, F-4, and FULL TRANSPORT CLOSED remain unaffected by this literature import.

---

## 4. Novelty and citation guard

After this audit, repository prose should avoid claiming novelty for any bare statement of the form:

- a dagger determines metric/Hermitian data;
- orthogonality can be expressed through dagger structure;
- formal adjoints encode metric plus divergence data.

Those are established external results in the categories covered by Garðarsson–Perrone.

The project-specific novelty burden remains downstream and specialized:

```math
\boxed{
\text{actual-zeta divisor custody}
\to
\text{canonical observable quotient/completion}
\to
\text{actual Weil source/form attachment}
\to
\text{positive-energy coercivity}
\to
\text{F-4 / full transport}.
}
```

Any future use of the paper as a **load-bearing** source requires a new exact source pin and a scope audit showing that the relevant RPB carrier and morphisms satisfy the paper's categorical hypotheses.

At present the paper is **contextual/non-load-bearing**.

---

## 5. Repository action

1. Add Garðarsson–Perrone to `docs/REFERENCES.md` as contextual dagger/formal-adjoint literature.
2. Retain the existing RPB synthesis-kernel versus analysis-kernel distinction.
3. Do not add an imported-source dependency edge to WD-T10, RPB-108, or F-4.
4. Use Proposition 6.16 only with its isometry hypothesis visible.
5. Use Theorem 13.3 as architectural support for keeping metric/bulk and divergence/boundary data separately typed.
6. Treat positivity/coercivity as an additional theorem obligation, not a consequence of dagger structure.

## Source

Jón Hákon Garðarsson and Paolo Perrone, *Dagger Categories in Riemannian Geometry*, arXiv:2610.02257v1 (2026).

https://arxiv.org/abs/2610.02257
