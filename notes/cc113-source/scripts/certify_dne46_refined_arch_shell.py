#!/usr/bin/env python3
"""Fresh rational cutoff/rate evaluation of the inherited Bessel shell bound."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import json,argparse
from dne17_nf10_complement_input import A,K,PI,ceil_grid,derivative_coeffs,integrated_mass_upper
from validate_dne43_high_floor import logarithm
from certify_dne39_signed_comparison import read
PARENT='a9eda40b874163be980da517d3dda87942f83533'
def run(output):
 ts=[F(14),F(15),F(16),F(65,4),F(33,2),F(67,4)];c=derivative_coeffs(K);y=ceil_grid(2*A*PI[1]*ts[-1]);rate=2*K+1-2*sum(x*y**(2*j+2) for j,x in enumerate(c));assert y*y<K*(K+1) and rate>50
 masses=[integrated_mass_upper(t,50) for t in ts];assert all(0<x<z for x,z in zip(masses,masses[1:]));b=[(logarithm(t)[0]-F(7,216)/t**2,logarithm(t)[1]-F(7,216)/t**2) for t in ts]
 loss=(b[0][1]+F(27,5))*masses[0]+sum((b[i][1]-b[i-1][0])*masses[i] for i in range(1,len(ts)));arch=b[-1][0]-loss;pole=16*A*(A/2)**(2*K)/factorial(K)**2
 hp='notes/data/RPB108_DNE43_HIGH_FLOOR_VALIDATION_20261010.json';h,hh=read(hp);assert h['status']=='PASS';prime=F(43387,20000);raw=arch-pole-prime;k=F((raw*1000).__floor__(),1000);assert k>F(6199377,10**7)
 out=dict(stage='DNE46',parent=PARENT,aperture=str(A),retained_cutoff=K,cutoffs=list(map(str,ts)),pi_interval=list(map(str,PI)),max_scaled_cutoff_upper=str(y),depth6_rate_lower=str(rate),conservative_rate=50,masses_upper=list(map(str,masses)),arch_multiplier_intervals=[list(map(str,x)) for x in b],arch_shell_loss_upper=str(loss),arch_lower=str(arch),pole_upper=str(pole),arch_minus_pole_lower=str(arch-pole),prime_norm_strict_upper=str(prime),high_validation_path=hp,high_validation_sha256=hh,original_high_raw_strict_lower=str(raw),certified_original_F112_lower=str(k),source_integrals_recomputed=False,true_high_inverse_evaluated=False,whole_aperture_positive=False,RH=False,Lean=False)
 Path(output).write_text(json.dumps(out,indent=2)+'\n');print('rate',float(rate),'arch-pole',float(arch-pole),'raw',float(raw),'certified high',str(k),flush=True)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);run(ap.parse_args().output)
