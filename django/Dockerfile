# syntax = docker/dockerfile:1.2
FROM python:3
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /code

ENV PIP_CACHE_DIR=/var/cache/buildkit/pip
RUN mkdir -p "$PIP_CACHE_DIR"

# We're using a BuildKit cache for apt packages, so don't let apt clear it
RUN rm -f /etc/apt/apt.conf.d/docker-clean
RUN --mount=type=cache,target=/var/cache/apt apt-get update && \
    apt-get install -y \
      binutils \
      libproj-dev \
      gdal-bin \
    && \
    apt-get -y autoremove

COPY requirements.in .
RUN pip install -r requirements.in
COPY . .
EXPOSE 8000

ENTRYPOINT ["/code/docker-entrypoint.sh"]
