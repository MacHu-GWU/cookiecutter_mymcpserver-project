# -*- coding: utf-8 -*-

from cookiecutter_mymcpserver.config.define import (
    Config,
)
from cookiecutter_mymcpserver.tests.test_config import setup_test_config
from cookiecutter_mymcpserver.paths import path_sample_config

try:
    from rich import print as rprint
except ImportError:  # pragma: no cover
    pass


class TestConfig:
    def test_seder(self):
        config = Config()
        dct = config.model_dump()
        config_1 = Config(**dct)
        dct_1 = config_1.model_dump()
        assert dct == dct_1
        assert config == config_1

    def test_load(self):
        setup_test_config()
        config = Config.load(path_sample_config)
        # rprint(config)  # for debug only


if __name__ == "__main__":
    from cookiecutter_mymcpserver.tests import run_cov_test

    run_cov_test(
        __file__,
        "cookiecutter_mymcpserver.config.define.py",
        preview=False,
    )
