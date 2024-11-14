from pydantic import BaseModel

class BaseClient(BaseModel):
    id_cliente: int 
    tipo_documento: str #| Field(str= cedula, pasaporte, cedula extranjeria, ppt)
    primer_nombre_cliente: str
    segundo_nombre_cliente: str | None = None
    primer_apellido_cliente: str
    segundo_apellido_cliente: str | None = None

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
    id_cliente: str
    id_empresa: str 
    
class ObligacionIn(BaseObligacion):
    pass

class ObligacionOut(BaseObligacion):
    pass
