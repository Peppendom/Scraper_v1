from datetime import datetime
from sqlalchemy import Column, Integer, Text, BigInteger, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key = True, autoincrement = True)
    url = Column(Text, unique = True, nullable = False)
    title = Column(Text, nullable = True)
    price_usd = Column(Integer, nullable = True)
    odometer = Column(Integer, nullable = True)
    username = Column(Text, nullable = True)
    phone_number = Column(BigInteger, nullable = True)
    image_url = Column(Text, nullable = True)
    images_count = Column(Integer, nullable = True)
    car_number = Column(Text, nullable = True)
    car_vin = Column(Text, nullable = True)
    datetime_found = Column(DateTime, nullable = False, default = datetime.now)
