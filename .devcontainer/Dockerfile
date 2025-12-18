# Devcontainer Dockerfile for Python 3.12
FROM python:3.12-slim

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    graphviz \
    git \
    curl \
    build-essential \
    sudo \
    ca-certificates \
    chromium \
 && rm -rf /var/lib/apt/lists/*

# Create a non-root user 'vscode' to match common devcontainer setups
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=1000

RUN groupadd --gid ${USER_GID} ${USERNAME} || true \
 && useradd -s /bin/bash --uid ${USER_UID} --gid ${USER_GID} -m ${USERNAME} || true \
 && echo "${USERNAME} ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/${USERNAME} \
 && chmod 0440 /etc/sudoers.d/${USERNAME}

WORKDIR /workspaces/${LOCAL_WORKSPACE_FOLDER:-app}

ENV SHELL=/bin/bash

# Keep pip tooling up to date
RUN python -m pip install --upgrade pip setuptools wheel

# By design we install Python packages in the postCreateCommand so the mounted
# workspace's requirements.txt is used (and won't be baked into the image).
