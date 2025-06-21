# -*- coding: utf-8 -*-

"""
Adapter integration layer that coordinates configuration, and MCP tools.
"""

from pydantic import BaseModel, Field

from ..config.api import Config

from .tool_adapter import ToolAdapterMixin


class Adapter(
    BaseModel,
    ToolAdapterMixin,
):
    """
    Master adapter class that integrates configuration MCP tool implementations.
    """

    config: Config = Field()
