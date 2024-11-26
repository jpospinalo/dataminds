from pydantic import BaseModel
from pydantic import Field

from pydantic import BaseModel, Field

class BaseClient(BaseModel):
    id_cliente: int = Field(
        gt=0,
        le=30,
        title="ID Cliente",
        description="El identificador único del cliente en la base de datos. Debe estar entre 8 y 30."
    )
    
    tipo_documento: str = Field(
        min_length=5,
        max_length=15,
        title="Tipo de Documento",
        description="El número del documento de identificación. Debe contener entre 5 y 15 dígitos."
    )
    
    primer_nombre: str = Field(
        min_length=1,
        max_length=50,
        pattern=r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$",  # Solo letras y espacios
        title="Primer Nombre",
        description="El primer nombre del cliente. Solo se permiten letras y espacios."
    )
    
    segundo_nombre: str | None = Field(
        min_length=0,
        max_length=50,
        pattern=r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]*$",  # Letras, espacios, o vacío
        title="Segundo Nombre",
        description="El segundo nombre del cliente (opcional). Solo se permiten letras y espacios."
    )
    
    primer_apellido: str = Field(
        min_length=1,
        max_length=50,
        pattern=r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$",  # Solo letras y espacios
        title="Primer Apellido",
        description="El primer apellido del cliente. Solo se permiten letras y espacios."
    )
    
    segundo_apellido: str | None = Field(
        min_length=1,
        max_length=50,
        pattern=r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]*$",  # Letras, espacios, o vacío
        title="Segundo Apellido",
        description="El segundo apellido del cliente (opcional). Solo se permiten letras y espacios."
    )


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
