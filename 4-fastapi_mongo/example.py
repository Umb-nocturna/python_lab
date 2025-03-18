from fastapi import FastAPI
from routes.producto_routes import router as producto_router

app = FastAPI(title="API personalizada")

app.include_router(producto_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI! crud mongoDB"}
