#!/usr/bin/python3
"""Print all City objects from the database with the state they belong in"""


from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in session.query(City, State).\
            filter(City.state_id == State.id).\
            order_by(City.id).\
            all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.commit()

    session.close()
