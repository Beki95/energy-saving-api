from sqlalchemy import Column, BigInteger, String

from db.postgres.config import Base


class Device(Base):
    __tablename__ = 'devices'

    id = Column(BigInteger, primary_key=True, index=True)
    dev_id = Column(String(length=120), nullable=False, index=True)
    dev_type = Column(String(length=120), nullable=False, index=True)
