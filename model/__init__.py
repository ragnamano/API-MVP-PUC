from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker

url_object = URL.create(
        'mysql+mysqlconnector',
        username = 'root',
        password = 'admin',
        host = 'localhost',
        database = 'Coleção'
        )

engine = create_engine(url_object)
Session = sessionmaker(bind=engine)