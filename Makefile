.PHONY: install test clean

install:
	uv sync

test:
	uv run python example.py

clean:
	rm -rf .venv uv.lock
