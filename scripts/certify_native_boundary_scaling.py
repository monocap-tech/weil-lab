#!/usr/bin/env python3
"""Exact rational constant/control audit; universal analytic proofs are in the note."""
from fractions import Fraction as F
import json
from pathlib import Path
import argparse
p=argparse.ArgumentParser(); p.add_argument('--output',required=True); args=p.parse_args()
checks={
 'arch_scaled_lower': F(3,4)*F(1,8)==F(3,32),
 'pole_scaled_upper': F(2,64)==F(1,32),
 'residual_scaled_lower': F(3,32)-F(1,32)==F(1,16),
 'residual_mass_lower': F(1,16)**2==F(1,256),
 'near_remainder_area': F(1,2)>0,
 'exp_lower_8_over_3': sum((F(1,1),F(1,1),F(1,2),F(1,6),F(1,24)),F(0))>F(8,3),
 'tail_hs_coefficient': F(2)*F(3,8)+F(1,2)==F(5,4),
 'log_energy_bound': F(4)+F(2,9)*F(3)==F(14,3)<F(5),
 'kernel_scale_range': F(4)*F(1,8)==F(1,2),
 'exponential_lower': F(1)-F(2)*F(1,8)==F(3,4),
}
# Dropping the singular part leaves epsilon*r bounded by epsilon.
# Such a proposed lower bound cannot retain 3/32 at epsilon=1/1024.
control_rejected=F(1,1024)<F(3,32)
assert all(checks.values()) and control_rejected
out={'base_commit':'b3dc9e56d29c2ace138a04fa9b71c6ca50dbdb65',
 'checks':checks,'negative_control_drop_singular_term_rejected':control_rejected,
 'scope':'exact rational constants; universal kernel/operator/Fourier arguments are analytic proofs',
 'actual_weak_null_sequence_asserted':False,'signed_gaussian_counterexample_asserted':False,
 'global_endpoint_exclusion':False,'F4':False,'FULL_TRANSPORT_CLOSED':False,'Lean_changed':False}
Path(args.output).write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
print(json.dumps({'checks_passed':len(checks),'negative_control_rejected':control_rejected}))
