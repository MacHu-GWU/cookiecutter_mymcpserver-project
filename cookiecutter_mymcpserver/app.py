# -*- coding: utf-8 -*-

import fire
from cookiecutter_mymcpserver.create_app import create_app


def main(config=None):
    """Main entry point for the MCP server.
    
    Args:
        config (str, optional): Path to the configuration file.
    """
    mcp = create_app(config=config)
    mcp.run(transport="stdio")


if __name__ == "__main__":
    fire.Fire(main)
