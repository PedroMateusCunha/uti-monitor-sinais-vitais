# STAGE 1: Create base image
FROM python:3.8-slim-buster as base

ARG APP_NAME
ARG ENV_NAME
ARG USER_HOME=/usr/app
LABEL app=${APP_NAME}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR $USER_HOME

COPY . .

RUN python3 -m pip install --upgrade pip && \
    pip install -r ${USER_HOME}/monitor-sinais-vitais/requirements/requirements.${ENV_NAME}.txt

WORKDIR ${USER_HOME}/monitor-sinais-vitais/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000","--reload"]
