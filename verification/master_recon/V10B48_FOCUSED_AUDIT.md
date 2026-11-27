# V10B48 focused optimized coverage audit

Status: source readback and named-audit inventory PASS; native verification pending.
Pinned checkout: dc42ce5d2c6167422748a668bc99ff7e48fc8cbb. Workflow blob: c76aaa2d697e3c872c5bbb2fdc7f4fb70dd91887.
Existing arithmetic run 45927665008 and analytical run 45928064611 were still active at submission. New workflow shares the analytical concurrency group with cancel-in-progress false; it does not cancel the existing run.

| Module | Declared audit targets | Dependencies gated | Source blob |
|---|---:|---|---|
| V10B33a | 4 | none | 0c2a6826ebc1cb9587e7e99ffb34c11207b706c3 |
| V10B33b | 4 | none | 752dfd1d2d83fbf08065784e470d6790adfb8538 |
| V10B34a | 5 | V10B33a | 69cb18a007463e07f39b349f0391dcef0d5fd6b0 |
| V10B45a | 5 | none | fd85d71fa26a5d152e2912c725f5bd1f420908ee |
| V10B46a | 8 | V10B34a | 30029adb050f800f9d325b3b022c84b2276c4f56 |
| V10B46b | 6 | V10B45a V10B33b | a7540a4ba363dbb59bf13a9acb87ab57991d76eb |
| V10B46c | 3 | V10B46a V10B46b | ffe5f65c92fa4e448848684007c3b53fa17de1fd |
| V10B47a | 3 | V10B34a | 79ba979cc447c53c4ae5ee85cebd1823f656e4da |
| V10B47b | 6 | V10B47a | 722909ae86d15dbcd510b138628e89e5368c322d |
| V10B39b | 4 | none | 00f21d3ea624bb68fa08a23d8dddf7ae1fe82ea9 |
| V10B39c | 3 | V10B39b | b54d02f3b071d534ebcd4ef414c9480de8f9f0cd |
| V10B40a | 4 | V10B39b V10B39c | ac581d7366091ee28b104fd7b5cf32e4fe4bea28 |
| V10B43a | 4 | V10B40a | 8a2797f7b3e7edd36f13fdb5d7b1682ef924cba3 |
| V10B47c | 12 | V10B47b V10B46c V10B43a | 757e07b3e6a8f6a1f97b8e6786660c641e8967ae |

Total 71 named targets; includes prior certifications. No new declarations or native certification counted in V10B48.
Exact replay: python3 verification/master_recon/v10b45_optimized_coverage.py.
Scope: actual integer polynomial trials and normalized odd deflation on [0,1]. Physical carrier, support measure/row scaling and constraint-kernel equivalence still require attachment. Physical energy/residual congruence is separate. Original V10B19 archive remains unauthenticated. Arithmetic ADOPT 0; RH unresolved.
