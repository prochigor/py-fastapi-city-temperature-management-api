from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship

from database import Base


class DBTemperature(Base):
    __tablename__ = "temperature"

    id = Column(Integer, primary_key=True, index=True)
    city_id = Column(Integer, ForeignKey("city.id"))
    date_time = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
    temperature = Column(Float)


cities = relationship("DBTemperature", back_populates="city")