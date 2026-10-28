from sqlalchemy import Column,Integer,String,Float
from sqlalchemy.orm import declarative_base
Base = declarative_base
class Electronicproduct(Base):
    __tablename__= "Electronic_products"
    product_no = Column(Integer,primary_key=True)
    product_name = Column(String(255))
    price = Column(Float)