# NF381 — Stop the PR verification feedback loop; preserve informal Mittermeier/event-cell custody

**Date:** 2026-10-28 Pacific. **Classification:** OPERATIONAL VERIFICATION-ROUTING CORRECTION, not a mathematical NF377 certificate. **This audit branch is a *docket*, NOT a new mathematical proof frontier.** Original `W-ODD-NEG` and RH remain OPEN. External Mittermeier source remains CONTEXTUAL and NOT PROMOTED.

## Previous / current / next

**Previous:** Draft PR #361 on `research/nf376-original-fifth-exterior-signed-lowband` had head `a7b3d751040b4829395c8a982650852907b466a4`, encompassing NF376 native matched original source geometry and informal Mittermeier NF377–NF380 annular analyses. Its two relevant runs — native 4096-bit `40814284507` and exact-rational conditional threshold `40814284627` — were still **QUEUED** at this audit, **not FAILED** and **not PASSED**. No particular original annulus, signed integral or full original exterior inverse was accepted.

**Current (operational cause):** Additional notes pushed directly to the PR branch repeatedly generate many GitHub Actions runs. GitHub's published `pull_request.paths` semantics use a **three-dot diff against the PR base**, not merely the files changed in the latest single commit: https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow . The NF377 workflow explicitly has `on: pull_request: paths:` including its new script/workflow, both of which remain changed across the whole PR. Thus another note-only push can retrigger that verification. A GitHub Actions query on 2026-10-28 Pacific reported about 993 queued runs across the repo and about 1844 runs for this topic branch (historical totals; not all simultaneously queued), so continuing to push unrelated notes to the active PR is counterproductive. No cause for GitHub runner capacity or network queue is asserted from those counts alone; the **repeated PR-diff triggering behavior is documented and observed**.

**Next (mathematics):** Wait for *actual* native result on a stable verification head (or obtain an equivalent independent, 4096-bit/outward original J242+E4 projection certificate). After one **specific** annulus `i` satisfies `||(I-P_S)delta_i||²>(49/100)*(11/4920)`, evaluate one actual signed continuum pairing against the unchanged NF370 `u4` and compare with the existing direction-four lowband target `1.5e-13`, or a **separately justified** full-frequency signed pairing against the exact highband-paid threshold `beta+h4≈3.3122287474e-13`. The fast analytic population proof guarantees at least ten qualifying indices but does **not** identify any.

## Custody separation rule

1. **Freeze further informal-note commits to the active PR #361 head while its targeted verification checks remain pending.** This is a practical pause, **not** a reimposition of old `NO_TRANSFER` policy.
2. Keep additional external-literature questions and method/source triage on this GitHub branch `audit/eventcells-informal-nf381-custody`, starting from the exact verified NF380 PR head. Do **not** create a separate PR or a parallel active proof obligation for this docket. This prevents further `pull_request` events on PR #361 while maintaining GitHub-first custody.
3. On a PASS, record the original report's SHA, exact annulus endpoints and outward `q_i` norm, then proceed to one signed integral under the original normalization and domain hypotheses. On FAIL, inspect the exact job log and repair the native calculation in one narrowly scoped consolidated PR update; never silently label an initial queue or failure a positivity result.
4. Stop trying to use pure geometric witness abundance as a substitute for an actual signed dual. The native annulus test is a **physical conditioning gate**, not a positivity certificate.

## Separate gates

**External method promotion (UNMET):** verified original signed dual or certified complete derivative-paid residual upper, with exact Suzuki/form identification and independently replayable arithmetic, changing the acceptance or method-STOP decision for the original NF375/NF376 obligation. Native annulus indexing is necessary for the current one-cell path but not in itself sufficient.

**Theorem closure (UNMET):** original `W-ODD-NEG` O1/O2 full odd signed operator, including infinite exterior inverse, all relevant original selected couplings and actual source/form domain; other parity, whole-Weil and RH remain separately open.

**This note does not:** alter `research/obligations.json`, `docs/IMPORTED_SOURCE_PINS.md`, a proof certificate, user-visible mathematical accepted status, or PR #361; it does not cancel the existing queued jobs, merge any branch, or assert new numerical results.

## Sources and pointers

- Live governance: `GOVERNANCE.md` on PR #361.
- Original annulus native script: `scripts/verify_nf377_original_annular_outfit_witness.py`.
- Exact annular population preflight: `notes/provisional/NF380_ANNULAR_SURVIVOR_POPULATION_GATE_20261028.md`.
- Original NF375 lowband margin: `notes/provisional/NF375_ORIGINAL_LOWBAND_WINDOW_REDUCTION_20261028.md`.
- Existing GitHub Actions run #40814284507: https://github.com/monocap-tech/weil-lab/actions/runs/40814284507
- Existing GitHub Actions run #40814284627: https://github.com/monocap-tech/weil-lab/actions/runs/40814284627
- Draft PR #361: https://github.com/monocap-tech/weil-lab/pull/361
