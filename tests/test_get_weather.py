# -*- coding: utf-8 -*-

from cookiecutter_mymcpserver.get_weather import get_forecast


def test_get_forecast():
    forecast_data = get_forecast(
        38.89773371563334,
        -77.03653255463253,
    )  # The White House
    # print(forecast_data)  # for debug only


if __name__ == "__main__":
    from cookiecutter_mymcpserver.tests import run_cov_test

    run_cov_test(
        __file__,
        "cookiecutter_mymcpserver.get_weather",
        preview=False,
    )
