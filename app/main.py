from fastapi import FastAPI
from .routes import router
from .crud import *
import sys

app = FastAPI()
app.include_router(router)  # Incluir las rutas
