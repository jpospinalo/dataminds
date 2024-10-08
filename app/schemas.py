from pydantic import BaseModel

class BaseClient(BaseModel):
    id_cliente: int 
    tipo_documento: str
    primer_nombre_cliente: str
    segundo_nombre_cliente: str | None = None
    primer_apellido_cliente: str
    segundo_apellido_cliente: str | None = None

class ClientIn(BaseClient):
    pass

class ClientOut(BaseClient):
    pass
