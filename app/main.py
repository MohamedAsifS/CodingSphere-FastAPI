from fastapi import FastAPI
from .models import user_model
from .database import database
from .router import user,project

app=FastAPI()

database.Base.metadata.create_all(bind=database.engine)
app.include_router(user.router)
app.include_router(project.router)