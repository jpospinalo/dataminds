from sqlmodel import create_engine

username = 'root'
password = 'adminadmin'
host = 'localhost'
database = 'prueba'
 

# Create a SQLModel engine
engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@{host}:3306/{database}')
