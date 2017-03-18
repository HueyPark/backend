from datetime import datetime
from sqlalchemy import Column, BigInteger, ForeignKey, Integer, TIMESTAMP, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class ItemBase(Base):
    __tablename__ = 'item'

    id = Column(BigInteger, primary_key=True, autoincrement=False)

    def __init__(self, item_id: int):
        self.id = item_id

    def __repr__(self):
        return 'Item / id: {}'.format(self.id)

    def to_dict(self):
        return {'id': str(self.id)}


class NodeBase(Base):
    __tablename__ = 'node'

    id = Column(BigInteger, primary_key=True, autoincrement=False)
    pos_x = Column(Integer, nullable=False)
    pos_y = Column(Integer, nullable=False)
    units = relationship('Unit')


class ProductionBase(Base):
    __tablename__ = 'production'

    id = Column(BigInteger, primary_key=True, autoincrement=False)
    create_time = Column(TIMESTAMP, nullable=False, default=func.now(), server_default=func.now())
    complete_time = Column(TIMESTAMP, nullable=False, default=func.now(), server_default=func.now())

    def __init__(self, production_id: int):
        self.id = production_id
        self.create_time = datetime.now()
        complete_timestamp = self.create_time.timestamp() + (60*60)
        self.complete_time = datetime.fromtimestamp(complete_timestamp)

    def __repr__(self):
        return 'Production / id: {}, create_time: {}'.format(self.id, self.create_time)


class UnitBase(Base):
    __tablename__ = 'unit'

    id = Column(BigInteger, primary_key=True, autoincrement=False)
    node_id = Column(BigInteger, ForeignKey(NodeBase.id))
