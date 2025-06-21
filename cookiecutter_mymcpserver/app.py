# -*- coding: utf-8 -*-

from cookiecutter_mymcpserver.create_app import create_app


def main():
    """Main entry point for the MCP server."""
    mcp = create_app()
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
