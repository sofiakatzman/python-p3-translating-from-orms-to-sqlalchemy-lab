from models import Dog
from sqlalchemy.orm import sessionmaker


def create_table(base, engine):
    base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()


def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name.ilike(name)).first()

def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id.ilike(id)).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name.ilike(name), Dog.breed.ilike(breed)).first()

def update_breed(session, dog, breed):
    for dog in session.query(Dog):
            dog.breed = breed

    session.commit()