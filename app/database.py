from sqlmodel import create_engine

username = 'admin'
password = 'adminadmin'
host = 'proyecto-dataminds.cfzybbinygh8.us-east-1.rds.amazonaws.com'
database = 'dataminds'


# Create a SQLModel engine
engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@{host}:3306/{database}')
