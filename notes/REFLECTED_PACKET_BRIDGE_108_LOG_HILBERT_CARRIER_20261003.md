# RPB-108 — concrete complete logarithmic form carrier
Date: 2026-10-03
Parent: 6645b05195b6232b99d5796a7adddb5b1c3b71e5

## Construction and terminology

The logarithmic Hilbert carrier is a closed subspace of genuine weighted Fourier L2 coordinates. Its physical reconstruction is inverse Fourier transformation after multiplication by 1/sqrt(log(e+|xi|)). It is not the ordinary-L2 norm inherited by the existing canonical-domain subtype.

The bounded inverse-weight multiplier is built from its actual continuous/measurable function and the pointwise norm bound <=1. Physical reconstruction is consequently an actual continuous linear map, with no source-representation or operator-domain assumption.

Support is enforced by the kernel of a concrete bounded map: reconstruct physically, then multiply by the indicator outside [-a,a]. A kernel is closed. Its subtype therefore has the inherited complex inner product and a proved CompleteSpace instance.

Every coordinate in this closed kernel reconstructs an actual supported physical L2 vector with finite logarithmic Fourier energy. Conversely the previously constructed square-root-weighted Fourier coordinate of every canonical-domain vector lies in this kernel. The two maps are mutually inverse.

The carrier norm squared is exactly the physical logarithmic Fourier energy. This proves completeness for the correct form topology; it does not silently assert that the old canonical-domain subtype is complete with its inherited ordinary-L2 norm.

## Why this is witness work

The manuscript says WD-T38's source is identified with the compact-window Weil form, but the current Lean constructor still accepts independent Q, density, P, k and extension parameters. Its physical Fourier lift identifies an L2 class, not the logarithmic source norm or the source quadratic. Another assumed identification field would not resolve that gap.

This module instead constructs the concrete complete domain needed to realize actual source synthesis by Hilbert adjoints. It certifies one component of the b382eec/6645b05 written attachment construction without assuming the desired source law.

## Witness boundary

PROVED by this module after validation: actual complete logarithmic carrier, concrete physical reconstruction, exact canonical-domain correspondence, exact energy norm. No source-identity or spectral-product premise is added.

WRITTEN / RETAINED: actual-zeta upper sampling, explicit-formula diagonal extension, effective background norm comparison and form-completed endpoint mixed null witness from the previous notes.

OPEN: identify the retained WD-T38 source operators and current physical vector with this model; attach the actual diagonal/polarization/normalized estimates; attach enlarged central cancellation.

Current-carrier spectral L2 is not derived here and remains unassumed. Logarithmic energy is the one-log form criterion, not the log-squared operator criterion. Once actual enlarged central cancellation is available, the certified inner-collar theorem already constructs regularity and consumes boundary removal. Do not reopen exterior, digamma or boundary work.

Threshold bookkeeping CLOSED; F-4 NOT STARTED; WD-T40/RH unchanged.

## Validation

Whole-root build succeeded (9,023 jobs), followed by six public-declaration axiom audits, each depending only on propext, Classical.choice and Quot.sound. The unfinished-declaration gate passed.

Validation commit: ff5aab0b47c19b9b76f8772bfa2cf6c5d94387e0
Validation tree: 74830e51e5f5c7f05bc63a8ae9c5949b8e5456d7
Run: https://github.com/monocap-tech/weil-lab/actions/runs/37107333285
Job: 111158325513
Source blob: 99fdae5a00829b231964b6d4e48ad0c966dffdf0
Root blob: 91603701de502591a301b7347bdc37d4e3bbe5fc

Exact promotion is two certified code files plus this new note and four current status documents. All other Lean sources/manifests match the successful validation tree. The research workflow is preserved byte for byte. No historical note is rewritten.
