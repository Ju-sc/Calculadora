from fastapi import APIRouter
from fastapi.responses import JSONResponse


router = APIRouter()

@router.get("/subtracao")

def subtracao(a: float, b: float):
   
    return {"resultado": a - b}