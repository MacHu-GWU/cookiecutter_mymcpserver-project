# -*- coding: utf-8 -*-

from pathlib import Path
from claude_desktop_config.api import ClaudeDesktopConfig, Mcp, BaseMcpEnum
from cookiecutter_mymcpserver.constants import EnvVarEnum
from cookiecutter_mymcpserver.paths import (
    PACKAGE_NAME,
    PACKAGE_NAME_SLUG,
    dir_venv_bin,
    dir_unit_test,
    path_sample_config,
)


cdc = ClaudeDesktopConfig()


dir_home = Path.home()


class MCPEnum(BaseMcpEnum):
    COOKIECUTTER_MYMCPSERVER_DEV_PYTHON = Mcp(
        name=f"{PACKAGE_NAME}_dev_python",
        settings={
            "command": f"{dir_venv_bin}/python",
            "args": [
                f"{dir_unit_test}/app.py",
            ],
            "env": {
                EnvVarEnum.COOKIECUTTER_MYMCPSERVER_CONFIG.name: f"{path_sample_config}",
            },
        },
    )
    COOKIECUTTER_MYMCPSERVER_DEV_CLI = Mcp(
        name=f"{PACKAGE_NAME}_dev_cli",
        settings={
            "command": f"{dir_venv_bin}/cookiecuttermymcpserver",
            "args": [
                "--config",
                f"{path_sample_config}",
            ],
        },
    )
    COOKIECUTTER_MYMCPSERVER_DEV_DOCKER = Mcp(
        name=f"{PACKAGE_NAME}_dev_docker",
        settings={
            "command": "docker",
            "args": [
                "run",
                "-i",
                "--rm",
                "--mount",
                f"type=bind,source={path_sample_config},target=/usr/src/app/config.json",
                "cookiecutter-mymcpserver:latest",
            ],
        },
    )
    COOKIECUTTER_MYMCPSERVER_PRE_RELEASE = Mcp(
        name=f"{PACKAGE_NAME}_pre_release",
        settings={
            "command": f"{dir_home}/.pyenv/shims/uvx",
            "args": [
                f"{PACKAGE_NAME_SLUG}",
            ],
            "env": {
                EnvVarEnum.COOKIECUTTER_MYMCPSERVER_CONFIG.name: f"{path_sample_config}",
            },
        },
    )
    COOKIECUTTER_MYMCPSERVER = Mcp(
        name=PACKAGE_NAME,
        settings={
            "command": f"{dir_home}/.pyenv/shims/uvx",
            "args": [
                f"{PACKAGE_NAME_SLUG}",
            ],
            "env": {
                EnvVarEnum.COOKIECUTTER_MYMCPSERVER_CONFIG.name: f"{path_sample_config}",
            },
        },
    )


wanted_mcps = {
    # MCPEnum.COOKIECUTTER_MYMCPSERVER_DEV_PYTHON,
    # MCPEnum.COOKIECUTTER_MYMCPSERVER_DEV_CLI,
    MCPEnum.COOKIECUTTER_MYMCPSERVER_DEV_DOCKER,
    # MCPEnum.COOKIECUTTER_MYMCPSERVER_PRE_RELEASE,
    # MCPEnum.COOKIECUTTER_MYMCPSERVER,
}
MCPEnum.apply(wanted_mcps, cdc)
