run:
	@uvicorn contrib.main:app --reload

create-migrations:
	@PYTHONPATH = $PYTONPATH:$(pwd) alembic revision --autogenerate -m $(d)

run-migrations:
	@@PYTHONPATH = $PYTONPATH:$(pwd) alembic upgrade head