# -*- coding: utf-8 -*-

import typing as T
import requests

NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"


def make_nws_request(url: str) -> dict[str, T.Any] | None:
    """
    Make a request to the NWS API with proper error handling.
    """
    headers = {"User-Agent": USER_AGENT, "Accept": "application/geo+json"}
    try:
        response = requests.get(url, headers=headers, timeout=3)
        response.raise_for_status()
        return response.json()
    except Exception:
        return None


def get_forecast(latitude: float, longitude: float) -> dict[str, T.Any]:
    """
    Get the weather forecast for a location.

    :param latitude: Latitude of the location
    :param longitude: Longitude of the location
    """
    # First, get the forecast grid endpoint
    points_url = f"{NWS_API_BASE}/points/{latitude},{longitude}"
    points_data = make_nws_request(points_url)
    if not points_data:
        raise ValueError(
            f"Unable to fetch forecast data for this location: {latitude}, {longitude}"
        )

    # Get the forecast URL from the points response
    forecast_url = points_data["properties"]["forecast"]
    forecast_data = make_nws_request(forecast_url)

    if not forecast_data:
        raise ValueError(
            f"Unable to fetch detailed forecastfor this location: {latitude}, {longitude}"
        )

    return forecast_data
