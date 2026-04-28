from fastapi import FastAPI, APIRouter
from fastapi.responses import JSONResponse



router = APIRouter()

@router.get("/multiplicacao")
def multiplicacao(a: float, b: float):
   
    return {"resultado": a * b}