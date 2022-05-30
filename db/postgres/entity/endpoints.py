from sqlalchemy import Column, BigInteger, Integer, ForeignKey, Text

from db.postgres.config import Base


class Endpoint(Base):
    __tablename__ = 'endpoints'

    id = Column(BigInteger, primary_key=True, index=True)
    device_id = Column(
        Integer,
        ForeignKey('devices.id', onupdate='CASCADE', ondelete='CASCADE')
    )
    comment = Column(Text)
