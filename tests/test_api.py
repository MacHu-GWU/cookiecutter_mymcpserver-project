# -*- coding: utf-8 -*-

from cookiecutter_mymcpserver import api


def test():
    _ = api


if __name__ == "__main__":
    from cookiecutter_mymcpserver.tests import run_cov_test

    run_cov_test(
        __file__,
        "cookiecutter_mymcpserver.api",
        preview=False,
    )
