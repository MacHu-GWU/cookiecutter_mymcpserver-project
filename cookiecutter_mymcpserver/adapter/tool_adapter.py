# -*- coding: utf-8 -*-

import typing as T

from ..get_weather import get_forecast


if T.TYPE_CHECKING:  # pragma: no cover
    from .adapter import Adapter


class ToolAdapterMixin:
    """
    MCP tools low level implementation.
    """

    def tool_get_forecast(
        self: "Adapter",
        latitude: float,
        longitude: float,
    ) -> str:
        return get_forecast(latitude, longitude)

    tool_get_forecast.__doc__ = get_forecast.__doc__
