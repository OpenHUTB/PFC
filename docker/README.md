# LaTeX

![LaTeX Logo](/latex.png)

A convenient way to run LaTeX on various platform using Docker (latexmk, pdflatex...).

[![Docker Build](https://github.com/leplusorg/docker-latex/workflows/Docker/badge.svg)](https://github.com/leplusorg/docker-latex/actions?query=workflow:"Docker")
[![Docker Stars](https://img.shields.io/docker/stars/leplusorg/latex)](https://hub.docker.com/r/leplusorg/latex)
[![Docker Pulls](https://img.shields.io/docker/pulls/leplusorg/latex)](https://hub.docker.com/r/leplusorg/latex)
[![Docker Automated](https://img.shields.io/docker/cloud/automated/leplusorg/latex)](https://hub.docker.com/r/leplusorg/latex)
[![Docker Build](https://img.shields.io/docker/cloud/build/leplusorg/latex)](https://hub.docker.com/r/leplusorg/latex)
[![Docker Version](https://img.shields.io/docker/v/leplusorg/latex?sort=semver)](https://hub.docker.com/r/leplusorg/latex)

## Example

Assuming that you have a file `foo.tex` in your current working directory that you want to convert into a PDF `foo.pdf`:

**Mac/Linux**

```bash
docker run --rm -t --user="$(id -u):$(id -g)" --net=none -v "$(pwd):/tmp" leplusorg/latex latexmk -outdir=/tmp -pdf /tmp/foo.tex
```

**Windows**

In `cmd`:

```batch
docker run --rm -t --net=none -v "%cd%:/tmp" leplusorg/latex latexmk -outdir=/tmp -pdf /tmp/foo.tex
```

In PowerShell:

```pwsh
docker run --rm -t --net=none -v "${PWD}:/tmp" leplusorg/latex latexmk -outdir=/tmp -pdf /tmp/foo.tex
```

## Help

To know more command-line options of `latexmk`:

```bash
docker run --rm --net=none leplusorg/latex latexmk -h
```

## Request new tool

Please use [this link](https://github.com/leplusorg/docker-latex/issues/new?assignees=thomasleplus&labels=enhancement&template=feature_request.md&title=%5BFEAT%5D) (GitHub account required) to request that a new tool be added to the image. I am always interested in adding new capabilities to these images.
