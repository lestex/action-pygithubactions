FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && apt upgrade -y
RUN pip install pygithubactions==0.1.3

WORKDIR /app
COPY bin /app/

ENV HOME="/home/nonadmin"
RUN groupadd -r -g 1001 nonadmin && useradd -r -d $HOME -u 1001 -g nonadmin nonadmin
RUN mkdir -p $HOME
RUN chown nonadmin $HOME
USER nonadmin

ENTRYPOINT [ "python", "/app/test_core.py"]
