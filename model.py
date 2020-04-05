
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
Base = declarative_base()
class Item(Base):
	__tablename__ ="items"
	id = Column(Integer,primary_key=True)
	name_of_item = Column(String)
	description = Column(String)
	price_d = Column(String)
	imglink = Column(String)
	place = Column(String)
	view = Column(String)
	exp = Column(String)
	def __repr__(self):
		return("item: {}\n"
				"Description: {}\n"
				"price_d : {}\n"
				"Link : {}\n"
				"place : {}\n"
				"view : {}\n"
				"exp : {}\n").format(
				self.name_of_item,
				self.descriptions,
				self.price,
				self.imglink,
				self.place,
				self.view,
				self.exp)
			
			
