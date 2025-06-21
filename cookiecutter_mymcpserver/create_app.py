# -*- coding: utf-8 -*-


def create_app(config=None):
    from .server import mcp

    from .tools import get_forecast
    
    if config:
        import os
        os.environ.setdefault('COOKIECUTTER_MYMCPSERVER_CONFIG', config)

    return mcp
