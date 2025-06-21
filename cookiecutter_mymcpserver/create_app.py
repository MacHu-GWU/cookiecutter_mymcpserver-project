# -*- coding: utf-8 -*-


def create_app():
    from .server import mcp

    return mcp
