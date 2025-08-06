from fastapi import FastAPI
from routers import users
from routers import status

app = FastAPI()

app.include_router(users.router)
app.include_router(status.router)




