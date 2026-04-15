from fastapi import FastAPI
import fatorial, multi, soma, sub, expo


app = FastAPI()


app.include_router(fatorial.router)
app.include_router(multi.router)
app.include_router(soma.router)
app.include_router(sub.router)
app.include_router(expo.router)
    

@app.get("/")
async def root():
    return {"message": "Hello World"}