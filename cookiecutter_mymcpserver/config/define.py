# -*- coding: utf-8 -*-

"""
cookiecutter_mymcpserver Configuration System
"""

import json
from pathlib import Path

from pydantic import BaseModel


class Config(BaseModel):
    @classmethod
    def load(cls, path: Path) -> "Config":
        """
        Load configuration from a JSON file.

        Reads and parses a JSON configuration file, validates it against the
        configuration schema, and returns a Config object. Provides detailed
        error messages for common configuration problems.

        :paaram path: Path to the JSON configuration file. Must be readable by
            the current process.

        :returns: :class:`Config` Validated configuration object ready for use.

        :raises: If file cannot be read, JSON is invalid, or validation
            fails. Error messages include specific details about the
            failure to help with troubleshooting.

        This method performs three validation steps:

        1. File system access (can read the file)
        2. JSON parsing (valid JSON syntax)
        3. Schema validation (matches expected structure and types)
        """
        try:
            s = path.read_text()
        except Exception as e:  # pragma: no cover
            raise Exception(
                f"Failed to read configuration content from {path}! Error: {e!r}"
            )

        try:
            dct = json.loads(s)
        except Exception as e:  # pragma: no cover
            raise Exception(
                f"Failed to load configuration from {path}! Check your JSON content! Error: {e!r}"
            )

        try:
            config = cls(**dct)
        except Exception as e:  # pragma: no cover
            raise Exception(
                f"Configuration Validation failed! Check your JSON content! Error: {e!r}"
            )

        return config
