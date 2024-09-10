from sqlmodel import Field, SQLModel, create_engine, Session
 
 
class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None
 
 # Replace the placeholders with your actual MySQL credentials and database information
username = 'admin'
password = 'adminadmin'
host = 'proyecto-dataminds.cfzybbinygh8.us-east-1.rds.amazonaws.com'
database = 'DataMinds'
 
sqlite_file_name = "database.db"
#sqlite_url = f"sqlite:///{proyecto-dataminds.cfzybbinygh8.us-east-1.rds.amazonaws.com}"
 
# Create a SQLModel engine
engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@{host}:3306/{database}')

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def create_heroes():
    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
    hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)
 
    session = Session(engine)
 
    session.add(hero_1)
    session.add(hero_2)
    session.add(hero_3)
 
    session.commit()
 
    session.close()
 
 
def main():
    create_db_and_tables()
    create_heroes()
 
 
if __name__ == "__main__":
    main()
