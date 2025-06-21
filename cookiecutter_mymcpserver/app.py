# -*- coding: utf-8 -*-

import typing as T
import fire
from cookiecutter_mymcpserver.create_app import create_app


def _main(config: T.Optional[str] = None):
    """
    :param config: Path to the configuration file.
    """
    mcp = create_app(config=config)
    mcp.run(transport="stdio")


def main():
    fire.Fire(_main)


if __name__ == "__main__":
    from cookiecutter_mymcpserver.paths import path_sample_config

    _main(config=str(path_sample_config))
