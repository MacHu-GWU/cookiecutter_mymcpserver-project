# -*- coding: utf-8 -*-

"""
Defines the sample configuration to be used during testing.
"""

import json
import os

from ..paths import path_sample_config
from ..constants import EnvVarEnum
from ..config.api import (
    Config,
)

test_config = Config()


def setup_test_config():
    path_sample_config.write_text(
        json.dumps(
            test_config.model_dump(),
            indent=4,
            ensure_ascii=False,
        ),
    )
    os.environ[EnvVarEnum.COOKIECUTTER_MYMCPSERVER_CONFIG.name] = str(
        path_sample_config
    )
