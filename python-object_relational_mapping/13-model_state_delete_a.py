#!/usr/bin/python3
"""Delete all State objects with the letter a and commit
changes to the database"""


from model_state import Base, State
from sqlalchemy import create_engine, delete
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).filter(State.name.ilike("%a%")).all():
        session.delete(state)
    session.commit()

    session.close()
