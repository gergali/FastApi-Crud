from pydantic import BaseModel

class ProductoBase(BaseModel):
    nombre: str
    stock: int
    categoria_id: int

class ProductoCreate(ProductoBase):
    pass


class ProductoOut(ProductoBase):
    id: int
    class config():
        orm_mode = True

class ProductoUpdate(BaseModel):
    nombre : str | None = None
    stock : int | None = None
    categoria_id : int | None = None

class CategoriaBase(BaseModel):
    nombre : str

class CategoriaCreate(CategoriaBase):
    pass
 
class CategoriaOut(CategoriaBase):
    id : int
    class config():
        orm_mode = True

class CategoriaUpdate(BaseModel):
    nombre : str | None = None

