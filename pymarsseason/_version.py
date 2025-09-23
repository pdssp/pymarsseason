# PyMarsSeason - Computes the season based on the solar longitude
# Copyright (C) 2022-2025 - CNES (Jean-Christophe Malapert for PDSSP (Pôle de Données et Services Surfaces Planétaires))
# This file is part of PyMarsSeason <https://github.com/pdssp/pymarsseason>
# SPDX-License-Identifier: Apache-2.0
"""Project metadata."""
from importlib.metadata import metadata

pkg_metadata = metadata("pymarsseason")

__name_soft__ = pkg_metadata.get("name", "unknown")
__version__ = pkg_metadata.get("version", "0.0.0")
__title__ = pkg_metadata.get("name", "unknown")
__description__ = pkg_metadata.get("summary", "")
__url__ = pkg_metadata.get("homepage", "")
__author__ = pkg_metadata.get("authors", "unknown")
__author_email__ = pkg_metadata.get("author-email", "unknown")
__license__ = pkg_metadata.get("license", "")
__copyright__ = "2022-2025, CNES (Jean-Christophe Malapert for PDSSP (Pôle de Données et Services Surfaces Planétaires))"
