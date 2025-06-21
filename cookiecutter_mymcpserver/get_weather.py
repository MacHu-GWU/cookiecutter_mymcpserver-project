# -*- coding: utf-8 -*-

import typing as T
import requests

NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"


def make_nws_request(url: str) -> dict[str, T.Any] | None:
    """Make a request to the NWS API with proper error handling."""
    headers = {"User-Agent": USER_AGENT, "Accept": "application/geo+json"}
    try:
        response = requests.get(url, headers=headers, timeout=3)
        response.raise_for_status()
        return response.json()
    except Exception:
        return None


def get_forecast(latitude: float, longitude: float) -> str:
    """
    Get weather forecast for a location.

    :param latitude: Latitude of the location
    :param longitude: Longitude of the location

    :return: Formatted weather forecast string or error message

    Example latitude and longitude:

        - Washington, DC: 38.8951, -77.0364
        - San Francisco, CA: 37.7749, -122.4194
        - New York, NY: 40.7128, -74.0060
        - Chicago, IL: 41.8781, -87.6298
        - Seattle, WA: 47.6062, -122.3321

    Example returns::

        Today:
        Temperature: 92°F
        Wind: 2 to 7 mph S
        Forecast: Mostly sunny, with a high near 92. South wind 2 to 7 mph.
    """
    # First get the forecast grid endpoint
    points_url = f"{NWS_API_BASE}/points/{latitude},{longitude}"
    points_data = make_nws_request(points_url)

    if not points_data:
        return "Unable to fetch forecast data for this location."

    # Get the forecast URL from the points response
    forecast_url = points_data["properties"]["forecast"]
    forecast_data = make_nws_request(forecast_url)

    if not forecast_data:
        return "Unable to fetch detailed forecast."

    # Format the periods into a readable forecast
    periods = forecast_data["properties"]["periods"]
    forecasts = []
    for period in periods[:5]:  # Only show next 5 periods
        forecast = f"""
{period['name']}:
Temperature: {period['temperature']}°{period['temperatureUnit']}
Wind: {period['windSpeed']} {period['windDirection']}
Forecast: {period['detailedForecast']}
"""
        forecasts.append(forecast)
    text = "\n---\n".join(forecasts)
    return text
