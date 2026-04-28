from fastapi import FastAPI
import fato, multi, soma, sub, expo, raiz, divi


app = FastAPI()


app.include_router(fato.router)
app.include_router(multi.router)
app.include_router(soma.router)
app.include_router(sub.router)
app.include_router(expo.router)
app.include_router(raiz.router) 
app.include_router(divi.router)  

@app.get("/")
async def root():
    return {"message": "Hello World"}