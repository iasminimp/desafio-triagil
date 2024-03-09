FROM ubuntu

ARG GIT_USERNAME
ARG GIT_EMAIL

RUN apt update
RUN apt upgrade -y

RUN apt install git -y
RUN git config --global user.name ${GIT_USERNAME}
RUN git config --global user.email ${GIT_EMAIL}

RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip install Flask
RUN pip install requests

COPY api.py /server/

ENTRYPOINT cd server/ && python3 api.py