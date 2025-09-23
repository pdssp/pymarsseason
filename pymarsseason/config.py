# PyMarsSeason - Computes the season based on the solar longitude
# Copyright (C) 2022-2025 - CNES (Jean-Christophe Malapert for PDSSP (Pôle de Données et Services Surfaces Planétaires))
# This file is part of PyMarsSeason <https://github.com/pdssp/pymarsseason>
# SPDX-License-Identifier: Apache-2.0
import sys

from loguru import logger


# ---- Logging configuration ----
def configure_logging(level="INFO", sink=sys.stderr, **kwargs):
    """
    Configure a global loguru logger.
    """
    logger.remove()
    logger.add(sink, level=level.upper(), **kwargs)
