FROM kalilinux/kali-rolling:latest
ENV DEBIAN_FRONTEND noninteractive
ENV TERM xterm-256color

RUN rm -fR /var/lib/apt/ && \
    apt-get clean && \
    apt-get update -y && \
    apt-get install -y software-properties-common && \
    apt-get install -y net-tools  && \
    apt-get install -y vim && \
    apt-get install -y iputils-ping && \
    apt-get install -y netdiscover && \
    apt-get install -y pip && \
    apt-get install -y dsniff && \
    apt-get install sudo -y

CMD ["/bin/bash"]
