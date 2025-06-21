# -*- coding: utf-8 -*-

import typing as T
import textwrap
from pathlib import Path

from mcp.server.fastmcp import FastMCP

from .constants import EnvVarEnum
from .paths import path_default_config
from .docs import DocFilesEnum
from .config.api import Config
from .adapter.api import Adapter


def get_description(method: T.Callable) -> str:
    """
    Get the description of a function, falling back to its docstring if available.
    """
    return textwrap.dedent(method.__doc__).strip()


def create_app(
    config: T.Optional[str] = None,
) -> FastMCP:
    """
    :param config: Path to the configuration file.
    """
    mcp = FastMCP(
        name="My MCP Server",
        instructions=DocFilesEnum.mcp_instructions,
    )
    if config is not None:
        config = Config.load(path=Path(config))
    elif EnvVarEnum.COOKIECUTTER_MYMCPSERVER_CONFIG.exists():
        config = Config.load(
            path=Path(EnvVarEnum.COOKIECUTTER_MYMCPSERVER_CONFIG.value)
        )
    else:
        config = Config.load(path=path_default_config)

    adapter = Adapter(
        config=config,
    )

    def add_tool(func: T.Callable):
        mcp.tool(description=get_description(func))(func)

    add_tool(adapter.tool_get_forecast)

    return mcp
