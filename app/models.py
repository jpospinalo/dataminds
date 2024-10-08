from sqlmodel import Field, SQLModel, create_engine


class Client(SQLModel, table=True):
    
    __tablename__ = "cliente"
 
    id_cliente: int | None = Field(default=None, primary_key=True)
    tipo_documento: str
    primer_nombre_cliente: str
    segundo_nombre_cliente: str | None = None
    primer_apellido_cliente: str
    segundo_apellido_cliente: str | None = None

