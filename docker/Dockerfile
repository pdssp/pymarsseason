# -*- coding: utf-8 -*-
# PyMarsSeason - Computes the season based on the solar longitude
# Copyright (C) 2022-2025 - CNES (Jean-Christophe Malapert for PDSSP (Pôle de Données et Services Surfaces Planétaires))
# This file is part of PyMarsSeason <https://github.com/pdssp/pymarsseason>
# SPDX-License-Identifier: LGPL-3.0-or-later

ARG DEBIAN_NAME="bullseye"
ARG PYTHON_VERSION="3.12"
FROM python:${PYTHON_VERSION}-slim-${DEBIAN_NAME} AS base

WORKDIR /app
RUN apt-get update -qq \
      && apt upgrade --yes \
      && apt-get clean all \
      && rm -rf /var/lib/apt/lists/*

FROM base AS builder
WORKDIR /app

RUN apt-get update -qq \
      && apt upgrade --yes \
      && apt-get -y --no-install-recommends install \
         build-essential \
         ca-certificates \
         gdb \
         gfortran \
         wget \
         file \
         apt-utils \
         git  \
      && apt-get clean all \
      && rm -r /var/lib/apt/lists/*

RUN pip install poetry && poetry config installer.max-workers 10 && poetry config virtualenvs.create false
COPY . .
ARG POETRY_LOCK=1
RUN make
RUN make release && VERSION=$(poetry version -s) && pip install dist/pymarsseason-${VERSION}.tar.gz

FROM python:3.12-slim-bullseye AS release
ARG BUILD_DATE
ARG VERSION
ARG DEBIAN_FRONTEND=noninteractive

WORKDIR /app

# Labels (based on OCI Image Format Specification)
LABEL \
    org.opencontainers.image.version=$VERSION \
    org.opencontainers.image.created=$BUILD_DATE \
    org.opencontainers.image.title="PyMarsSeason" \
    org.opencontainers.image.ref.name="pymarsseason" \
    org.opencontainers.image.description="Computes the season based on the solar longitude" \
    org.opencontainers.image.licenses="GNU Lesser General Public License v3" \
    org.opencontainers.image.source="https://github.com/pdssp/pymarsseason" \
    org.opencontainers.image.documentation="https://pdssp.github.io/pdssp/pymarsseason" \
    org.opencontainers.image.vendor="PDSSP (Pôle de Données et Services Surfaces Planétaires)" \
    org.opencontainers.image.authors="Jean-Christophe Malapert <jean-christophe.malapert@cnes.fr>"

# Get the installed libraries and application from the ealier stage
COPY --from=builder /usr/local/ /usr/local/

# Regenerate the shared-library cache
RUN ldconfig

ENTRYPOINT ["pymarsseason"]
