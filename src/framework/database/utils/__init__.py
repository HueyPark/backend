from framework.database.models.base import Base
from framework.database.engine import engine


def create_all():
    Base.metadata.create_all(engine)


def drop_all():
    Base.metadata.drop_all(engine)


def drop_and_create_all():
    drop_all()
    create_all()
