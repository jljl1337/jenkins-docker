# The default tag is to suppress the warning message
ARG TAG=rhel

FROM jenkins/jenkins:${TAG}

USER root

RUN dnf -y install dnf-plugins-core
RUN dnf config-manager --add-repo https://download.docker.com/linux/rhel/docker-ce.repo

RUN dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y

USER jenkins

RUN jenkins-plugin-cli --plugins "blueocean docker-workflow"

# docker build --build-arg TAG=rhel -t jenkins:test -f rhel.Dockerfile .