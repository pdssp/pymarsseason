#!/bin/sh
# PyMarsSeason - Computes the season based on the solar longitude
# Copyright (C) 2022-2025 - CNES (Jean-Christophe Malapert for PDSSP (Pôle de Données et Services Surfaces Planétaires))
# This file is part of PyMarsSeason <https://github.com/pdssp/pymarsseason>
# SPDX-License-Identifier: LGPL-3.0-or-later
docker build -t pymarsseason_image -f docker/Dockerfile --build-arg POETRY_LOCK="$( stat poetry.lock )" .
