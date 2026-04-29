from fastapi import FastAPI, APIRouter
from fastapi.responses import JSONResponse



router = APIRouter()


@router.get("/multiplicação")

def multiplicacao(a: float, b: float):
   
    return {"resultado": a * b}