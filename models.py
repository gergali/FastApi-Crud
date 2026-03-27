from sqlalchemy import Integer , Column , String , ForeignKey
from database2 import Base
from sqlalchemy.orm import relationship

class Categoria(Base):
    __tablename__ = "Categorias"

    id = Column(Integer , primary_key=True ,index = True )
    nombre = Column(String , unique=True , nullable=False )

    productos = relationship( "Producto", back_populates = "categorias")


class Producto(Base):
    __tablename__ = "Producto"

    id = Column(Integer , primary_key=True , index=True)
    nombre = Column(String , nullable=False )
    stock = Column(Integer , default=0 )
    categoria_id = Column(Integer ,ForeignKey("Categorias.id"))

    categorias = relationship("Categoria" , back_populates = "productos")