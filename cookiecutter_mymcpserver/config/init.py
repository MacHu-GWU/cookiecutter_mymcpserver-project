# -*- coding: utf-8 -*-

"""
Singleton instance of Config.
"""

import os
from pathlib import Path

from ..constants import EnvVarEnum

from .define import Config

if "READTHEDOCS" in os.environ:  # pragma: no cover
    from ..paths import path_sample_config

    COOKIECUTTER_MYMCPSERVER_CONFIG = str(path_sample_config)
else:
    COOKIECUTTER_MYMCPSERVER_CONFIG = EnvVarEnum.COOKIECUTTER_MYMCPSERVER_CONFIG.value

path_config = Path(COOKIECUTTER_MYMCPSERVER_CONFIG)
config = Config.load(path=path_config)
