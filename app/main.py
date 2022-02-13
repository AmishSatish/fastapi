from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import engine
from .routers import post,user,auth,vote
from .config import settings

#! Alembic is going to handle this portion
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["https://www.google.com"] # list of domains / urls that can talk to my API to allow all domains to access set origins to ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
