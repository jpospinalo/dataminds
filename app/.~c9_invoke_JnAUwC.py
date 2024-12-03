from sqlmodel import Field, Relationship, SQLModel

# Conexión con la base de datos de la tabla Cliente.
class Client(SQLModel, table=True):
    
    __tablename__ = "cliente"
 
    id_cliente: int | None = Field(primary_key=True)
    tipo_documento: str 
    primer_nombre: str
    segundo_nombre: str | None = None
    primer_apellido: str
    segundo_apellido: str | None = None
    obligaciones : list["Obligacion"] = Relationship(back_populates="cliente", cascade_delete=True)

# Conexión con la base de datos de la tabla Obligación.
class Obligacion(SQLModel, table=True):
    
    #__tablename__ = "obligacion"
 
    id_obligacion: int | None = Field(primary_key=True)
    id_empresa: int = Field(foreign_key="empresa.id_empresa")

    id_cliente: int = Field(foreign_key="cliente.id_cliente")
    cliente : Client = Relationship(back_populates="obligaciones")

    
# Conexión con la base de datos de la tabla Empresa.
class Empresa(SQLModel, table=True):
    
    __tablename__ = "empresa"
 
    id_empresa: int | None = Field(primary_key=True)
    nombre_empresa: str