# -*- coding: utf-8 -*-

import typing as T

from ..get_weather import get_forecast


if T.TYPE_CHECKING:  # pragma: no cover
    from .adapter import Adapter


class ToolsAdapterMixin:
    """
    MCP tools low-level implementation.
    """

    def tool_get_forecast(
        self: "Adapter",
        latitude: float,
        longitude: float,
    ) -> str:
        """
        Get the weather forecast for a location.

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
        try:
            forecast_data = get_forecast(latitude, longitude)
        except Exception as e:
            return str(e)

        # Format the periods into a readable forecast
        periods = forecast_data["properties"]["periods"]
        forecasts = []
        for period in periods[:5]:  # Only show next 5 periods
            name = period["name"]
            temperature = period["temperature"]
            temperatureUnit = period["temperatureUnit"]
            windSpeed = period["windSpeed"]
            windDirection = period["windDirection"]
            detailedForecast = period["detailedForecast"]
            forecast = f"""
{name}:
Temperature: {temperature}°{temperatureUnit}
Wind: {windSpeed} {windDirection}
Forecast: {detailedForecast}
        """.strip()
            forecasts.append(forecast)
        text = "\n---\n".join(forecasts)
        return text
