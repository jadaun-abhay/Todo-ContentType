FROM python:3.13-trixie

RUN apt update && apt -y upgrade

WORKDIR /dead_task

COPY ./docker/packages.txt .

RUN xargs apt -y install < packages.txt

ENV PYTHONPATH="/dead_task"

ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh
ENV PATH="/root/.local/bin/:$PATH"
ENV UV_LINK_MODE=copy

COPY pyproject.toml .
COPY uv.lock .

RUN uv venv

RUN uv pip install -r pyproject.toml
RUN uv pip install -e .

EXPOSE 8000
