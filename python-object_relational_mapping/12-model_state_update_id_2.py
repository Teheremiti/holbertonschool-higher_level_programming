#!/usr/bin/python3
"""Add a new State object and commit changes to the database"""


from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    second = session.query(State).filter(State.id == 2).first()
    second.name = "New Mexico"
    session.commit()

    session.close()
