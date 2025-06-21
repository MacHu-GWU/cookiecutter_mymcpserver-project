# -*- coding: utf-8 -*-

from cookiecutter_mymcpserver.tests.test_config import setup_test_config

setup_test_config()

from cookiecutter_mymcpserver.config.init import config

try:
    from rich import print as rprint
except ImportError:  # pragma: no cover
    pass


def test_config_init():
    _ = config
    # rprint(config)  # for debug only
    pass


if __name__ == "__main__":
    from cookiecutter_mymcpserver.tests import run_cov_test

    run_cov_test(
        __file__,
        "cookiecutter_mymcpserver.config.init.py",
        preview=False,
    )
