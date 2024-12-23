ARG TAG=alpine

FROM jenkins/jenkins:${TAG}

USER root

RUN apk add docker

USER jenkins

RUN jenkins-plugin-cli --plugins "blueocean docker-workflow"

# docker build --build-arg TAG=alpine -t jenkins:test -f alpine.Dockerfile .