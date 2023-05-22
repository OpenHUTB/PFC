FROM debian:stable-slim

ARG USER_NAME=latex
ARG USER_HOME=/home/latex
ARG USER_ID=1000
ARG USER_GECOS=LaTeX

RUN adduser \
  --home "$USER_HOME" \
  --uid $USER_ID \
  --gecos "$USER_GECOS" \
  --disabled-password \
  "$USER_NAME"

ARG WGET=wget
ARG GIT=git
ARG SSH=openssh-client
ARG MAKE=make
ARG PANDOC=pandoc
ARG PCITEPROC=pandoc-citeproc
ARG PYGMENTS=python3-pygments
ARG PYTHONIS=python-is-python3
ARG FIG2DEV=fig2dev
ARG JRE=default-jre-headless

# hadolint ignore=DL3008
RUN apt-get update && apt-get install --no-install-recommends -y \
  texlive-full \
  # some auxiliary tools
  "$WGET" \
  "$GIT" \
  "$SSH" \
  "$MAKE" \
  # markup format conversion tool
  "$PANDOC" \
  "$PCITEPROC" \
  # XFig utilities
  "$FIG2DEV" \
  # syntax highlighting package
  "$PYGMENTS" \
  # temporary fix for minted, see https://github.com/gpoore/minted/issues/277
  "$PYTHONIS" \
  # Java runtime environment (e.g. for arara)
  "$JRE" && \
  # Removing documentation packages *after* installing them is kind of hacky,
  # but it only adds some overhead while building the image.
  apt-get --purge remove -y .\*-doc$ && \
  # Remove more unnecessary stuff
  apt-get clean -y && \
  rm -rf /var/lib/apt/lists/*
