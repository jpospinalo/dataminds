from fastapi import FastAPI
from .routes import router
from .routes_empresa import router_empresa
from .crud import *
from .crud_empresa import *
import sys

app = FastAPI()
app.include_router(router)  # Incluir las rutas
app.include_router(router_empresa)
