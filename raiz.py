from fastapi.responses import JSONResponse
from fastapi import APIRouter
import math


router = APIRouter()


@router.get("/raizquad")


def raizquad(a: float):
    if a == 0:
        return JSONResponse(
            status_code=400,
            content={"erro": "Não é possível dividir por 0"}
        )
    res = math.sqrt(a)
    resint = int(res)
   
    return {"resultado": resint}