from pydantic import BaseModel
from pydantic import Field
from pydantic import BaseModel, Field
from enum import Enum

# DocumentType: Enum que define los tipos de documentos permitidos.
class DocumentType(str, Enum):
    CEDULA = "CEDULA"
    PASAPORTE = "PASAPORTE"
    CEDULA_DE_EXTRANJERIA = "CEDULA DE EXTRANJERIA"
    TARJETA_DE_IDENTIDAD = "TARJETA DE IDENTIDAD"
# BaseClient: Modelo base para la información del cliente.
class BaseClient(BaseModel):
    id_cliente: str = Field(
        max_length = 50,
        title="ID Cliente",
        description="El identificador único del cliente en la base de datos. Debe estar entre 8 y 30."
    )
    
    tipo_documento: DocumentType = Field(
        title="Tipo de Documento",
        description="Tipo de documento del cliente"
    )
    
    primer_nombre: str = Field(
        max_length=50,
        pattern=r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$",  # Solo letras y espacios
        title="Primer Nombre",
        description="El primer nombre del cliente. Solo se permiten letras y espacios."
    )
    
    segundo_nombre: str | None = Field(
        max_length=50,
        pattern=r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]*$",  # Letras, espacios, o vacío
        title="Segundo Nombre",
        description="El segundo nombre del cliente (opcional). Solo se permiten letras y espacios."
    )
    
    primer_apellido: str = Field(
        max_length=50,
        pattern=r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$",  # Solo letras y espacios
        title="Primer Apellido",
        description="El primer apellido del cliente. Solo se permiten letras y espacios."
    )
    
    segundo_apellido: str | None = Field(
        max_length=50,
        pattern=r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]*$",  # Letras, espacios, o vacío
        title="Segundo Apellido",
        description="El segundo apellido del cliente (opcional). Solo se permiten letras y espacios."
    )
    
    obligaciones: list["Obligacion"] = Field(
        default=[],
        title="Obligaciones",
        description="Lista de obligaciones asociadas al cliente."
    )
    
# ClientIn: Modelo de entrada para la información del cliente.
class ClientIn(BaseClient):
    pass

# ClientOut: Modelo de salida para la información del cliente.
class ClientOut(BaseClient):
    pass

# BaseEmpresa: Modelo base para la información de la empresa.
class BaseEmpresa(BaseModel):
    id_empresa: int 
    nombre_empresa: str 

# EmpresaIn: Modelo de entrada para la información de la empresa.
class EmpresaIn(BaseEmpresa):
    pass

# EmpresaOut: Modelo de salida para la información de la empresa. 
class EmpresaOut(BaseEmpresa):
    pass

# BaseObligacion: Modelo base para la información de la obligación.
class BaseObligacion(BaseModel):
    id_obligacion: int 
    id_cliente: str
    id_empresa: int 

# Obligacion: Modelo para la información de la obligación.
class Obligacion(BaseModel):
    id_obligacion: int
    id_cliente: str
    id_empresa: int

# ObligacionIn: Modelo de entrada para la información de la obligación.
class ObligacionIn(BaseObligacion):
    pass

# ObligacionOut: Modelo de salida para la información de la obligación.
class ObligacionOut(BaseObligacion):
    pass