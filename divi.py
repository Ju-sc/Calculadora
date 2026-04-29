from fastapi.responses import JSONResponse
from fastapi import APIRouter

router = APIRouter()


@router.get("/divisão")
def divisao(a: float, b: float):
    if b == 0:
        return JSONResponse(
            status_code=400,
            content={"erro": "Não é possível dividir por 0"}
        )
    return {"resultado": a / b}     

    