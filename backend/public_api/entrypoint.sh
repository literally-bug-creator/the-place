#!/bin/sh

uv run alembic upgrade head
uv run main.py