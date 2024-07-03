run:
	@uvicorn src.main:app --reload

precommit-install:
	@pre-commit install

test:
	@pytest

test-matching:
	@pytest -s -rx -k $(K) --pdb src ./src/tests/	