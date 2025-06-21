# -*- coding: utf-8 -*-

"""
Constant variables used in this project.
"""

import os

from pydantic import BaseModel, Field


class EnvVar(BaseModel):
    """
    Environment variable wrapper with default value support.
    Used for accessing environment variables throughout the application with fallback defaults.
    """

    name: str = Field()
    default: str = Field(default="")

    def exists(self) -> bool:
        return self.name in os.environ

    @property
    def value(self) -> str:
        return os.environ.get(self.name, self.default)


class EnvVarEnum:
    """
    Collection of predefined environment variables used throughout the application.
    Used for centralized environment variable management and configuration loading.
    """

    COOKIECUTTER_MYMCPSERVER_CONFIG = EnvVar(name="COOKIECUTTER_MYMCPSERVER_CONFIG")
