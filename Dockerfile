FROM ghcr.io/astral-sh/uv:python3.13-alpine

WORKDIR /app

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINKE_MODE=copy
ENV UV_TOOL_BIN=/usr/local/bin
ENV UV_SYSTEM_PYTHON=1

COPY pyproject.toml uv.lock ./

RUN uv sync --locked

COPY core/ core/
COPY db/ db/
COPY models/ models/
COPY schemas/ schemas/
COPY routers/ routers/
COPY main.py .
COPY .env .

EXPOSE 9898

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9898", "--reload"]

