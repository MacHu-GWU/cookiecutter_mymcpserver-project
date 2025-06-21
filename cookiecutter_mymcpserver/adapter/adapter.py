# -*- coding: utf-8 -*-

"""
Adapter integration layer that coordinates configuration, and MCP tools.
"""

from pydantic import BaseModel, Field

from ..config.api import Config

from .tools_adapter import ToolsAdapterMixin


class Adapter(
    BaseModel,
    ToolsAdapterMixin,
):
    """
    Master adapter class that integrates configuration MCP tool implementations.
    """

    config: Config = Field()
