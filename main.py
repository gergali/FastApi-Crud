
from fastapi import FastAPI, Depends , HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database2 import engine, SessionLocal, Base

app=FastAPI()

Base.metadata.create_all(bind=engine)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/productos", response_model=schemas.ProductoOut)
def crear_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    nuevo = crud.agregar_producto(db, producto)
    if not nuevo:
        raise HTTPException(status_code=404 , detail="La categoria no existe")
    return nuevo

@app.patch('/productos/{producto_id}' , response_model = schemas.ProductoOut)
def update_productos( productos_id : int , datos : schemas.ProductoUpdate , db :Session = Depends(get_db)):
 producto = crud.actualizar_producto(db , productos_id , datos)
 if not producto:
     raise HTTPException(status_code=404, detail= "Producto no encontrado")
 return producto

@app.get("/productos", response_model=list[schemas.ProductoOut])
def listar_productos(db: Session = Depends(get_db)):
    return crud.mostrar_productos(db)

@app.delete('/productos/{producto_id}' , response_model=schemas.ProductoOut)
def eliminar_producto(producto_id : int , db : Session = Depends(get_db)):
    producto = crud.eliminar_producto(db , producto_id)
    if not producto:
        raise HTTPException(status_code=404 , detail= "No se encontro el producto")
    return producto



@app.post('/categorias', response_model = schemas.CategoriaOut)
def crear_categoria(categoria : schemas.CategoriaCreate , db : Session = Depends(get_db)):
    return crud.agregar_categorias(db , categoria)

@app.get('/categorias' ,response_model=list[schemas.CategoriaOut])
def listar_categorias(db: Session = Depends(get_db)):
    return crud.mostrar_categoria(db)
    

@app.patch("/categorias/{categoria_id}" , response_model= schemas.CategoriaOut)
def update_categorias(categorias_id : int , datos : schemas.CategoriaUpdate , db : Session = Depends(get_db) ):
    categorias =  crud.actualizar_categoria(db, categorias_id , datos )
    if not categorias:
        raise HTTPException(status_code= 404 ,  detail= " Categoria inexistente.")
    return categorias

@app.delete("/categorias/{categoria_id}" , response_model= schemas.CategoriaOut)
def eliminar_catergoria(categoria_id : int , db: Session = Depends(get_db)):
    categoria = crud.eliminar_categoria(db , categoria_id)
    if not categoria:
        raise HTTPException(status_code= 404 , detail = "La categoria no existe")
    return categoria

