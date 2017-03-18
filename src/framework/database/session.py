from .engine import engine
from sqlalchemy.orm import scoped_session, sessionmaker

session = scoped_session(sessionmaker(bind=engine))
