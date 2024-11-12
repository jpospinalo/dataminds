from sqlmodel import Field, SQLModel, create_engine

# Conexión con la base de datos de la tabla Cliente.
class Client(SQLModel, table=True):
    
    __tablename__ = "cliente"
 
    id_cliente: int | None = Field(default=None, primary_key=True)
    tipo_documento: str 
    primer_nombre_cliente: str
    segundo_nombre_cliente: str | None = None
    primer_apellido_cliente: str
    segundo_apellido_cliente: str | None = None

# Conexión con la base de datos de la tabla Empresa.
class Empresa(SQLModel, table=True):
    
    __tablename__ = "empresa"
 
    id_empresa: int | None = Field(default=None, primary_key=True)
    nombre_empresa: str

# Conexión con la base de datos de la tabla Obligación.
class Obligacion(SQLModel, table=True):
    
    __tablename__ = "obligacion"
 
    id_obligacion: int | None = Field(default=None, primary_key=True)
    id_cliente: str
    id_empresa: str 
    
    
