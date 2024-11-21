from pydantic import BaseModel
from fastApi import Field

class BaseClient(BaseModel):
    id_cliente: int = Field(gt=7, le=30, description="Id cliente ")
    tipo_documento: str = Field(min_length=5, max_length=15, pattern="^\d+$")
    primer_nombre: str
    segundo_nombre: str | None = None
    primer_apellido: str
    segundo_apellido: str | None = None

class ClientIn(BaseClient):
    pass

class ClientOut(BaseClient):
    pass

class BaseEmpresa(BaseModel):
    id_empresa: int 
    nombre_empresa: str 
    
class EmpresaIn(BaseEmpresa):
    pass

class EmpresaOut(BaseEmpresa):
    pass

class BaseObligacion(BaseModel):
    id_obligacion: int 
    id_cliente: int
    id_empresa: int 
    
class ObligacionIn(BaseObligacion):
    pass

class ObligacionOut(BaseObligacion):
    pass
