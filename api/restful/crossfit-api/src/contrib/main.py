from fastapi import FastAPI
from contrib.routers import api_router
from fastapi_pagination import Page, add_pagination

app = FastAPI(title="WorkoutApi")
app.include_router(api_router)
add_pagination(app)
