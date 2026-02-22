FROM python:3.8.10-slim
LABEL authors="SimpleIN1"

ENV PYTHONDONTWIRTEBYTECODE=1
ENV PYTHONUNBUFFERED=1


RUN useradd -s /bin/bash django-user \
     && mkdir -p /usr/src/app/ \
     && chown -R django-user:django-user /usr/src/app/

WORKDIR /usr/src/app/

COPY --chown=django-user:django-user requirements.txt .

USER django-user

RUN python -m venv venv  \
    && venv/bin/python -m pip install --upgrade pip
RUN --mount=type=cache,target=/root/.cache/pip \
    venv/bin/pip install -r requirements.txt

COPY --chown=django-user:django-user ./SubscriptionAIProject .
RUN chown -R django-user:django-user /usr/src/app/SubscriptionAIProject