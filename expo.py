from fastapi import APIRouter
from fastapi.responses import JSONResponse


router = APIRouter()


@router.get("/exponenciacao")


def exponenciacao(a: float, b: float):
    if a == 0:
        return JSONResponse(
            status_code=400,
            content= {"erro:" "O elevado a expoente negativo é indefinido"}
        )
    return {"resultado:": a ** b}