# jenkins-docker

[![Build](https://github.com/jljl1337/jenkins-docker/actions/workflows/build.yml/badge.svg)](https://github.com/jljl1337/jenkins-docker/actions/workflows/build.yml)
[![Source](https://img.shields.io/badge/Source-GitHub-blue?logo=github)](https://github.com/jljl1337/jenkins-docker)
[![Docker](https://img.shields.io/badge/Docker-jljl1337%2Fjenkins--docker-blue?logo=docker)](https://hub.docker.com/r/jljl1337/jenkins-docker)
[![License](https://img.shields.io/github/license/jljl1337/jenkins-docker)](https://github.com/jljl1337/jenkins-docker/blob/main/LICENSE)

## What is this?

This is a Docker image of [Jenkins](https://www.jenkins.io/) with Docker
installed. This image is based on the official Jenkins image and adds Docker to
it.

This is created since in the official Jenkins
[documentation](https://www.jenkins.io/doc/book/installing/docker/#on-macos-and-linux),
you are asked to customize the Dockerfile to install Docker. Now you can just
pull and use this image instead.

## Build

The images are built using GitHub Actions. The workflow is defined in
[here](https://github.com/jljl1337/jenkins-docker/blob/main/.github/workflows/build.yml).

The build is triggered every day, so the latest image from the official Jenkins
image should be updated within 24 hours.

## License

This project is licensed under the MIT License - see the
[LICENSE](https://github.com/jljl1337/jenkins-docker/blob/main/LICENSE)