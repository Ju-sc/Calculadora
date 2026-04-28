from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi import APIRouter


router = APIRouter()


@router.get("/soma")


def soma(a: float, b: float):


    return {"resultado:": a + b}