from fastapi import APIRouter

router = APIRouter(prefix="/houses", tags=["Houses"])

@router.get("/", tags=["houses"])
async def read_houses():
    return [{"house": "Gryffindor"}, {"house": "Slytherin"}]