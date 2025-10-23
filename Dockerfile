FROM ghcr.io/astral-sh/uv:python3.13-alpine

WORKDIR /app

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINKE_MODE=copy
ENV UV_TOOL_BIN=/usr/local/bin
ENV UV_SYSTEM_PYTHON=1

COPY pyproject.toml uv.lock ./

RUN uv sync --locked

COPY database.py .
COPY models.py .
COPY main.py .

EXPOSE 9898

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9898", "--reload"]

