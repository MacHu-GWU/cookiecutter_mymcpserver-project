# -*- coding: utf-8 -*-

"""
Singleton instance of Adapter.
"""

from ..config.init import config
from .adapter import Adapter

adapter = Adapter(config=config)
