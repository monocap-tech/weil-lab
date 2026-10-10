#!/usr/bin/env python3
"""Run the unchanged independent DNE46 high validator in its authenticated workspace."""
from pathlib import Path
import importlib.util,os,sys
BASE=Path(__file__).resolve().parents[1]
sys.path[0:0]=[str(BASE/'notes/cc103-source/scripts'),str(BASE/'notes/cc101-source/scripts')]
spec=importlib.util.spec_from_file_location('cc113_unchanged_dne46_high_validator',BASE/'notes/cc113-source/scripts/validate_dne46_refined_arch_shell.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
os.chdir(BASE/'notes/cc109-source')
module.run('../cc113-source/notes/data/RPB108_DNE46_REFINED_ARCH_SHELL_20261010.json',str(BASE/'notes/data/RPB108_CC113_FRESH_HIGH_FLOOR_AUDIT_20261010.json'))
