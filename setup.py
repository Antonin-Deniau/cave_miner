#!/usr/bin/env python3
import os
from setuptools import setup
from setuptools.config import read_configuration

from pathlib import Path
thisDir=Path(__file__).parent
formatsPath=thisDir / "kaitai_struct_formats"
execFormatsPath=formatsPath / "executable"

cfg = read_configuration(str((thisDir / 'setup.cfg').absolute()))
#print(cfg)
cfg["options"].update(cfg["metadata"])
cfg=cfg["options"]

cfg["kaitai"]={
    "formatsRepo": {
        "localPath" : str(formatsPath),
        "update": True
    },
    "formats":{
        "mach_o.py": {"path": "mach_o.ksy"},
        "elf.py": {"path": "elf.ksy"},
        "microsoft_pe.py": {"path": "microsoft_pe.ksy"},
    },
    "outputDir": thisDir / "cave_miner" / "formats",
    "inputDir": execFormatsPath
}

setup(use_scm_version = True, **cfg)
