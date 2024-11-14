from pydantic import BaseModel

class BaseClient(BaseModel):
    id_cliente: int 
    tipo_documento: str #| Field(str= cedula, pasaporte, cedula extranjeria, ppt)
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
