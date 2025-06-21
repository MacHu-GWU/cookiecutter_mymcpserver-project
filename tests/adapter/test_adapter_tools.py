# -*- coding: utf-8 -*-

from cookiecutter_mymcpserver.tests.test_adapter import test_adapter as adapter


def test_tool_get_forecast():
    s = adapter.tool_get_forecast(
        38.89773371563334,
        -77.03653255463253,
    )
    # print(s)  # for debug only


if __name__ == "__main__":
    from cookiecutter_mymcpserver.tests import run_cov_test

    run_cov_test(
        __file__,
        "cookiecutter_mymcpserver.adapter.tools_adapter",
        preview=False,
    )
