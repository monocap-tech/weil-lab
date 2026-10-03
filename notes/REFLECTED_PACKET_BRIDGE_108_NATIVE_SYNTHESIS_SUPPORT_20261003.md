# RPB-108 — actual native synthesis support (2026-10-03)

Parent: `f9916c79029abc714d9ab269e7eca2c27908f5e6`.
Cursor: WD-T38 actual source/quadratic/null attachment; F-4 pending.
Threshold bookkeeping is closed.

## Existing map made reusable

`NeutralLogHilbertCarrier.lean` already constructed the actual bounded
physical L2 map `neutralOutsideRestriction a`, restricting to the complement
of the closed window, and proved

    outsideRestriction a f = 0
      iff f vanishes almost everywhere outside [-a,a].

This chunk makes those two declarations public, without changing their
definitions or proofs. The logarithmic Hilbert submodule continues to use
the same concrete map. No duplicate support projection is introduced.

## Proved spatial witnesses

`NeutralNativeSupport.lean` attaches almost-everywhere compact support to
the actual full Green and compact derivative L2 columns. Their indicator
definitions and actual `toLp` representatives give the witnesses directly,
for every window and ordinate.

For the actual native shell syntheses, apply the existing outside restriction
to the already certified HasSum. Every restricted coefficient-column term
is zero by the column witnesses. Continuity therefore gives zero outside
restriction of each synthesized vector, hence actual almost-everywhere
support in the same closed window.

The synthesis results use the retained positive window, actual shell data,
shell-count inputs, and genuine `lp 2` coefficient vector. They add no
assumed representation or regularity premise.

## What is now attached and what remains

The actual native Green synthesis has compact support and an actual
physical L2 weak derivative, the equally supported derivative synthesis
certified in the parent chunk. These are spatial witnesses for the same
vectors. The Fourier weak-derivative bridge and finite logarithmic Fourier
energy still need certification before canonical form-domain membership
can be claimed. Native background completion remains retained/written.

The current WD-T38 physical carrier is still independently parameterized;
it is not identified with this native synthesis or with the retained
background completion vector. Its actual source quadratic/null law and
same-domain mixed/normalized attachment remain open. No enlarged-window
frozen-action central cancellation is claimed.

Current-mode membership
`MemLp (neutralWeilSpectralProduct carrier a) 2` is not derived from WD-T38
and is not assumed. The native spatial support/derivative witnesses are
not substitutes for identification of that current physical mode.

Once actual central cancellation is attached, immediately consume
`neutralExteriorIntegralGrowthResidual_realizes_of_central` for the
locally integrable actual residual, boundary removal, and whole compact weak
realization. Exterior, digamma, boundary, and threshold work remain closed.
F-4 is pending.

## Validation

Validation commit: `0027279a20bdf72a3d262ed1192aa012207c4128`.
GitHub Actions run `37140812856`, job `111254691535`:
root build passed (9036 jobs). All five public theorem audits use only
`propext, Classical.choice, Quot.sound`, with no `sorryAx`.
The unfinished/project-axiom declaration gate passed.
Research workflow and historical notes are preserved.
