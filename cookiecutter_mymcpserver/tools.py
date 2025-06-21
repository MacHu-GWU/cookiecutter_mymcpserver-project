# -*- coding: utf-8 -*-

import typing as T
import textwrap

from .server import mcp
from .adapter.adapter_init import adapter


def get_description(method: T.Callable) -> str:
    """
    Get the description of a function, falling back to its docstring if available.
    """
    return textwrap.dedent(method.__doc__).strip()


@mcp.tool(
    description=get_description(adapter.tool_list_databases),
)
async def get_forecast(
    latitude: float,
    longitude: float,
) -> str:
    return adapter.tool_get_forecast(latitude, longitude)
