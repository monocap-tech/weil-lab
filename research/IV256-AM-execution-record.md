# IV256 execution record

Actual failures and recovery during this operation (not an infrastructure outage diagnosis):
- First attempted streaming command rejected because yield_time_ms is not a supported container exec argument. Retried with session_name; got StreamingExecNotEnabledContainerError. Plain exec available.
- Initial exploratory script imported the IV254 interval kernel without isolating its CLI, producing AssertionError at assert M<J<=32768 and J%2==0. Fixed by using the literal bank directly. Exploratory 14080-dimensional even tapered probe passed Cholesky at shift .005 (min squared pivot .13667323740158233); this was not a proof. Subsequent conservative far-tail probes at shift .01 both passed (even .13166333580659417, odd .13080624021290027). Diagnostic only, superseded by rigorous checker.
- First rigorous all-in-one command timed out with requested timeout 120000 ms; partial stdout:
  tail Gram verified 0 10.874533653259277
  built 0 14080 25.278666496276855
  Local superseded source Git hash 9762fe92017e08703b503e1e9c8b7686696030a0.
- Bounded block multiplication repair also timed out; partial stdout:
  tail Gram verified 0 10.562856912612915
  built 0 14080 24.929115295410156
  factored 0 30.376219034194946
  quantized 0 31.87284016609192
  factor integer norms verified 0 32.46302318572998
  Local superseded source Git hash 0eecb85f0a2ce9515f1a698c9a29384a3731a3d6.
- Staged preparation command also hit a tool timeout; partial stdout:
  tail Gram verified 0 10.46285367012024
  built 0 14080 26.06232523918152
  factored 0 31.740185976028442
- cgroup memory limit 4294967296 bytes; memory.events showed oom=0 and oom_kill=0 on inspection. The precise internal cause of command deadline failures is not claimed.
- Successful repair: run same staged checker in a local subprocess, poll within the same user turn; factor preparation persisted temporary checkpoints and independent residual blocks were verified and combined. All 14 blocks completed, both finish commands passed. No job left for future delivery. Executed source Git hash 43bab72e8f11a5cc8698b9c7452b7cee95b46eda. Raw output receipts retain every integer margin and checkpoint identity; prepare and verify runtime fields retained. Prior unsuccessful program versions not admitted as evidence, and their full byte contents are not in this commit; their hashes, failure outputs, and repair descriptions are recorded. No prior diagnostic is used for sign certification.
- Repository reads and blob writes succeeded during the operation. Repository custody remains authoritative. The final checker and receipts are reproducible without the ephemeral large checkpoints. No native Lean check or workflow dispatched.
