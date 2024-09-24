from sqlmodel import Field, SQLModel, create_engine


class Client(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    age: int 

