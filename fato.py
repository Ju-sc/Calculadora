from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/fatorial")

 
def fatorial(a: int):
    i = 0
    fat = 1
    if a <= 0 or a != int(a):
        return JSONResponse(
            status_code=400,
            content= {"erro": "Não é possível"}
        )
    for i in range (1, a+1):
        fat = (fat * i)
    fatint = int(fat)
    return {"resultado": fatint}