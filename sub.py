from fastapi import APIRouter
from fastapi.responses import JSONResponse


router = APIRouter()

@router.get("/subtração")

def subtracao(a: float, b: float):
   
    return {"resultado": a - b}