from pydantic import BaseModel

class BaseClient(BaseModel):
    first_name: str
    last_name: str
    age: int | None = None

class ClientIn(BaseClient):
    pass

class ClientOut(BaseClient):
    id: int
