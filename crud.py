from sqlalchemy.orm import Session
import models, schemas

#AGREGAR.
def agregar_producto(db: Session, producto: schemas.ProductoCreate):
    cat = db.query(models.Categoria).filter(models.Categoria.id == producto.categoria_id).first()
    if not cat:
        return None
    nuevo = models.Producto(**producto.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def agregar_categorias(db : Session , categoria : schemas.CategoriaCreate):
    nueva = models.Categoria(nombre = categoria.nombre)
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

#lISTAR 
def mostrar_productos(db: Session):
    return db.query(models.Producto).all()

def mostrar_categoria(db: Session):
    return db.query(models.Categoria).all()

#ACTUALIZAR

def actualizar_producto(db: Session, producto_id: int, datos: schemas.ProductoUpdate):
    producto = db.query(models.Producto).filter(models.Producto.id == producto_id).first()
    if not producto:
        return None
    for campo, valor in datos.model_dump(exclude_unset=True).items():
        setattr(producto, campo, valor)
    db.commit()
    db.refresh(producto)
    return producto

def actualizar_categoria(db: Session , categoria_id : int , datos : schemas.CategoriaUpdate):
    categoria = db.query(models.Categoria).filter(models.Categoria.id == categoria_id).first()
    if not categoria:
        return None
    for campo, valor in datos.model_dump(exclude_unset=True).items():
        setattr(categoria ,campo ,valor )
    db.commit()
    db.refresh(categoria)
    return categoria

#ELIMINAR

def eliminar_producto(db: Session , producto_id : int ):
    producto = db.query(models.Producto).filter( models.Producto.id == producto_id ).first()
    if not producto :
        return None
    db.delete(producto)
    db.commit()
    return producto

def eliminar_categoria(db : Session , categoria_id : int):
    categoria = db.query(models.Categoria).filter(models.Categoria.id == categoria_id).first()
    if not categoria:
        return None
    db.delete(categoria)
    db.commit()
    return categoria