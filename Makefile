.PHONY: install run test clean

install:
	uv sync

run test:
	rm -rf zvec_example
	uv run python example.py

clean:
	rm -rf .venv uv.lock zvec_example
