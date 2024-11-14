from sqlmodel import Field, SQLModel, create_engine

# Conexión con la base de datos de la tabla Cliente.
class Client(SQLModel, table=True):
    
    __tablename__ = "cliente"
 
    id_cliente: int | None = Field(default=None, primary_key=True)
    tipo_documento: str 
    primer_nombre: str
    segundo_nombre: str | None = None
    primer_apellido: str
    segundo_apellido: str | None = None

# Conexión con la base de datos de la tabla Empresa.
class Empresa(SQLModel, table=True):
    
    __tablename__ = "empresa"
 
    id_empresa: int | None = Field(default=None, primary_key=True)
    nombre_empresa: str

# Conexión con la base de datos de la tabla Obligación.
class Obligacion(SQLModel, table=True):
    
    __tablename__ = "obligacion"
 
    id_obligacion: int | None = Field(default=None, primary_key=True)
    id_cliente: int
    id_empresa: int 
    
    
