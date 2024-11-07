from sqlmodel import create_engine

username = 'admin'
password = 'adminadmin'
host = '35.170.189.6'
database = 'dataminds'


# Create a SQLModel engine
engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@{host}:3306/{database}')
