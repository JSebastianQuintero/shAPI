from fastapi import FastAPI, APIRouter

# routes
from paths.houses import router as houseRouter
from paths.persons import router as personRouter
from paths.marketing import router as marketingRouter

app = FastAPI()

app.include_router(houseRouter)
app.include_router(personRouter)
app.include_router(marketingRouter)