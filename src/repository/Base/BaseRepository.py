from sqlalchemy import create_engine, MetaData, Table, Column, ForeignKey,Integer
from .ConnectionFactory import ConnectionFactory
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

class BaseRepository:  
    engine = ConnectionFactory.getInstance()  
    metadata = MetaData() 
    metadata.reflect(engine)  
    Base = automap_base(metadata=metadata) 
    Base.prepare()   
    Tables = Base.classes
    context = Session(engine) 
