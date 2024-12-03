from sqlmodel import create_engine, SQLModel

username = 'admin'
password = 'adminadmin'
host = '35.170.189.6'
database = 'dataminds2'


# Create a SQLModel engine
engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@{host}:3306/{database}')
#def create_db_and_tables():
SQLModel.metadata.create_all(engine)